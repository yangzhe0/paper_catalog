# Section 5 & Conclusion 修改对照表

目标期刊：ApJS  
原文件：paper_en/paper_en.tex（lines 318–394）

---

## 5.1 Plate Re-reduction Verification

**✅ 已完成（2026-05-08）**

| # | 改动 | 说明 |
|---|---|---|
| 5.1-1 | 方程后补 Δα、Δδ 定义 | 已写入 line 327 |
| 5.1-R1 | 方程段与数字段之间新增前提段 | 说明 Δ 由两部分构成（星表系统误差 + 图像处理差异），改正模型只针对第一项；\citep{Yan2020} 移至此处 |
| 5.1-R2 | 删除原数字段末句 "The remaining difference should not be interpreted..." | 前提已在 R1 建立，此句冗余且防御性语气不当 |
| 5.1-R3 | 图 caption 重写 | 补充两个 panel 的坐标轴说明及线型含义（dashed/solid） |
| 5.1-R4 | 图描述段删除 panel (a) 描述，保留 panel (b) | panel (a) 描述与正文数字重复；panel (b) 说明时间连续性，有新信息 |

---

## 5.2 Ephemeris Comparison Validation

### "Taken together" 段落重写（line 375）

| # | 原文 | 建议修改 | 理由 |
|---|---|---|---|
| 5.2-1 | `Figure~\ref{fig:ephem_validation_overview} complements Table~\ref{tab:ephem_catalog_summary} from two levels. Panel (a) shows that the post-correction residual distribution is shifted modestly but systematically toward smaller values over the main body of the sample. Panel (b) presents the same result in a simpler catalog-by-catalog form: for several major catalogs, the typical file-level mean residuals are reduced after debiasing, whereas the differences remain small for subsets that are highly heterogeneous or represented by only one file. Taken together, these diagnostics support the interpretation that the Gaia-DR3-based corrections primarily improve external consistency by reducing systematic catalog-dependent offsets rather than by artificially narrowing the intrinsic residual distribution.` | **替换为：** `Figure~\ref{fig:ephem_validation_overview}b shows that for several widely used catalogs, the typical file-level mean residuals in RA and Dec are reduced after applying the debiasing corrections, while the within-file scatter (shown in Table~\ref{tab:ephem_catalog_summary}) remains essentially unchanged. This pattern is consistent with the design goal of the correction: to remove catalog-dependent systematic offsets without compressing the stochastic component of the residuals. The improvement is not uniform across all catalogs, as some subsets are represented by only one file or contain highly heterogeneous observations; these cases are expected to show weaker or irregular responses.` | 原段 Panel (a)/(b) 混杂叙述，"Taken together...diagnostics support" 语义绕口，Table 4 作用未体现。重写后逻辑：正向修正事实 → 与设计目标一致 → 不均匀性解释。因 Figure 6 Panel (a) 待重绘，暂移除对其引用。 |

---

## Conclusion（line 385–386）

| # | 原文 | 建议修改 | 理由 |
|---|---|---|---|
| C-1 | `To quantify this improvement, we define an inter-pixel discontinuity metric $\delta_{\mathrm{disc}}$ as the difference in correction values between adjacent HEALPix pixels. The cumulative distributions before and after smoothing are shown in Figure~\ref{fig:bias_jump}. The high-percentile and maximum values of $\delta_{\mathrm{disc}}$ are reduced by factors of roughly 2--4, demonstrating a significant improvement in the spatial continuity of the correction field.` | **删除** | 内容与 Section 4.4 完全重复；且"pixel"应为"tile"，已不符合全文规范。 |

---

## 延后处理（暂不修改）

| 项目 | 说明 |
|---|---|
| Table 4 结构 | 讨论是否改为展示修正变化量，待确认后处理 |
| Figure 6 Panel A | 纵轴含义不清、尺度问题，后续重新绘制 |
| Conclusion 整体重写 | 待后续统一梳理 |
| Section 7 URL | 等待虚拟天文台发布地址 |

---

*生成日期：2026-05-07*  
*确认无误后可授权直接修改 paper_en.tex*
