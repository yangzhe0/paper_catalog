#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
图片压缩最终版脚本
一键将 Figue_s 中的图片压缩后替换到 Figue 文件夹
"""

import os
import shutil
from PIL import Image
import sys

def compress_png_aggressive(input_path, output_path, max_width=1200, quality=85):
    """
    智能压缩PNG图片 - 只压缩大文件，小文件直接复制
    """
    try:
        # 获取文件大小，小于500KB的文件直接复制
        file_size_kb = os.path.getsize(input_path) / 1024
        if file_size_kb < 500:
            shutil.copy2(input_path, output_path)
            print(f"    文件较小({file_size_kb:.0f}KB)，直接复制")
            return True
        
        with Image.open(input_path) as img:
            # 获取原始尺寸
            original_width, original_height = img.size
            
            # 如果图片太大，先缩放
            if original_width > max_width:
                ratio = max_width / original_width
                new_width = max_width
                new_height = int(original_height * ratio)
                img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
                print(f"    缩放: {original_width}x{original_height} -> {new_width}x{new_height}")
            
            # 转换为RGB并使用JPEG压缩，然后转回PNG
            if img.mode != 'RGB':
                img = img.convert('RGB')
            
            # 先保存为高质量JPEG进行有损压缩
            temp_jpg = output_path + '.temp.jpg'
            img.save(temp_jpg, 'JPEG', quality=quality, optimize=True)
            
            # 重新加载JPEG并转换为PNG
            with Image.open(temp_jpg) as jpg_img:
                jpg_img.save(output_path, 'PNG', optimize=True)
            
            # 删除临时文件
            if os.path.exists(temp_jpg):
                os.remove(temp_jpg)
        
        return True
    except Exception as e:
        print(f"    压缩失败: {e}")
        return False

def get_file_size(file_path):
    """获取文件大小（KB）"""
    return os.path.getsize(file_path) / 1024

def get_folder_size(folder_path):
    """计算文件夹中PNG文件总大小"""
    total_size = 0
    png_count = 0
    for filename in os.listdir(folder_path):
        if filename.lower().endswith('.png'):
            file_path = os.path.join(folder_path, filename)
            if os.path.isfile(file_path):
                total_size += os.path.getsize(file_path)
                png_count += 1
    return total_size / 1024, png_count  # 返回KB和文件数量

def main():
    source_folder = "Figue原始"
    target_folder = "Figue"
    
    # 检查文件夹是否存在
    if not os.path.exists(source_folder):
        print(f"错误: 源文件夹 {source_folder} 不存在")
        return
    
    if not os.path.exists(target_folder):
        print(f"错误: 目标文件夹 {target_folder} 不存在")
        return
    
    # 获取所有PNG文件
    png_files = [f for f in os.listdir(source_folder) if f.lower().endswith('.png')]
    
    if not png_files:
        print(f"错误: 在 {source_folder} 中没有找到PNG文件")
        return
    
    # 计算原始大小
    original_size, original_count = get_folder_size(target_folder)
    
    print("=" * 60)
    print("图片压缩脚本 - 最终版")
    print("=" * 60)
    print(f"源文件夹: {source_folder}")
    print(f"目标文件夹: {target_folder}")
    print(f"找到 {len(png_files)} 个PNG文件需要处理")
    print(f"目标文件夹原始大小: {original_size:.2f} KB ({original_size/1024:.2f} MB)")
    print("-" * 60)
    
    # 创建临时文件夹用于压缩
    temp_folder = "temp_compressed"
    if os.path.exists(temp_folder):
        shutil.rmtree(temp_folder)
    os.makedirs(temp_folder)
    
    total_original_size = 0
    total_compressed_size = 0
    success_count = 0
    
    try:
        # 压缩所有图片到临时文件夹
        for filename in png_files:
            source_file = os.path.join(source_folder, filename)
            temp_file = os.path.join(temp_folder, filename)
            
            # 获取原始文件大小
            original_file_size = get_file_size(source_file)
            total_original_size += original_file_size
            
            print(f"正在压缩: {filename}")
            print(f"  原始大小: {original_file_size:.2f} KB")
            
            # 压缩图片
            if compress_png_aggressive(source_file, temp_file):
                # 获取压缩后文件大小
                compressed_file_size = get_file_size(temp_file)
                total_compressed_size += compressed_file_size
                
                compression_ratio = (1 - compressed_file_size / original_file_size) * 100 if original_file_size > 0 else 0
                
                print(f"  压缩后大小: {compressed_file_size:.2f} KB")
                print(f"  压缩率: {compression_ratio:.2f}%")
                print(f"  节省: {original_file_size - compressed_file_size:.2f} KB")
                success_count += 1
            else:
                # 如果压缩失败，复制原文件
                shutil.copy2(source_file, temp_file)
                total_compressed_size += original_file_size
                print(f"  压缩失败，使用原文件")
            
            print()
        
        # 如果所有文件都处理成功，替换目标文件夹中的文件
        if success_count > 0:
            print("-" * 60)
            print("正在替换目标文件夹中的文件...")
            
            replaced_count = 0
            for filename in png_files:
                temp_file = os.path.join(temp_folder, filename)
                target_file = os.path.join(target_folder, filename)
                
                if os.path.exists(temp_file):
                    try:
                        shutil.copy2(temp_file, target_file)
                        replaced_count += 1
                        print(f"  已替换: {filename}")
                    except Exception as e:
                        print(f"  替换失败 {filename}: {e}")
            
            print(f"成功替换 {replaced_count} 个文件")
        
        # 计算最终结果
        final_size, final_count = get_folder_size(target_folder)
        total_compression_ratio = (1 - final_size / original_size) * 100 if original_size > 0 else 0
        
        print("=" * 60)
        print("压缩完成！最终统计:")
        print("=" * 60)
        print(f"处理文件数量: {len(png_files)}")
        print(f"成功压缩: {success_count}")
        print(f"原始总大小: {original_size:.2f} KB ({original_size/1024:.2f} MB)")
        print(f"压缩后总大小: {final_size:.2f} KB ({final_size/1024:.2f} MB)")
        print(f"总压缩率: {total_compression_ratio:.2f}%")
        print(f"节省空间: {original_size - final_size:.2f} KB ({(original_size - final_size)/1024:.2f} MB)")
        print(f"平均每个文件节省: {(original_size - final_size)/len(png_files):.2f} KB")
        print("=" * 60)
        
    finally:
        # 清理临时文件夹
        if os.path.exists(temp_folder):
            shutil.rmtree(temp_folder)
            print("已清理临时文件")

if __name__ == "__main__":
    main()