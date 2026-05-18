# Section 2.2 修改对照表

目标期刊：ApJS  
原文件：paper_en/paper_en.tex（lines 109–141）

---

## 正文部分

### Para 1（line 111）

| # | 原文 | 建议修改 | 理由 |
|---|---|---|---|
| 1-1 | `In contrast to \citet{Eggl2020}, which focuses on star catalogs used in asteroid astrometry, this work targets catalogs that are frequently employed in natural satellite observations, including additional historical catalogs relevant to this context.` | `This work targets catalogs that are frequently employed in historical natural-satellite observations, including older releases that were prevalent before high-precision space-based astrometry became available.` | Introduction 已说明与 Eggl(2020) 的差异，此处再对比重复；改为直接陈述本文目标，不做对比。 |

---

### Para 2（line 113）

| # | 原文 | 建议修改 | 理由 |
|---|---|---|---|
| 2-1 | `The catalogs considered in this study are selected based on their prevalence in historical observations of natural satellites and their representation of major astrometric reference systems.` | `The catalogs included in this study are those most prevalently used in historical natural-satellite observations, as identified from a systematic survey of the NSDC archive.` | "representation of major astrometric reference systems"语义模糊；改为明确说明选取依据来自 NSDC 档案统计，与 Introduction Para 6 改后的叙述呼应。 |

---

### Para 3（line 115）

| # | 原文 | 建议修改 | 理由 |
|---|---|---|---|
| 3-1 | `These catalogs can be broadly classified into three categories.` | **【删除此句】** | 三分类无文献依据；删去标签，保留后续对各类星表特点的描述。 |
| 3-2 | `such as USNO-A and GSC` | `such as USNO-A2.0 and GSC~1.2` | A5：规范星表名称。 |
| 3-3 | `time-dependent positional errors` | `time-dependent position offsets` | A4："position"作复合名词修饰语；"error"保留给随机误差，此处是系统性偏移，用"offset"。 |
| 3-4 | `provide improved astrometric information but may still exhibit regional systematic biases \citep{Urban1998ACT,Zacharias2004UCAC2,Zacharias2013UCAC4}` | `provide improved positional accuracy and proper-motion coverage but may still exhibit regional systematic biases \citep{Roeser1991PPM,Urban1998ACT,Zacharias2004UCAC2,Zacharias2013UCAC4}` | （1）"astrometric information"不具体，改为"positional accuracy and proper-motion coverage"（A4）。（2）补 PPM 引用（原文漏引）。 |
| 3-5 | `offer a stable reference frame but are limited by relatively low source density` | `provide a stable and well-characterized reference frame but are limited in source density, which can restrict the number of usable reference stars in fields near bright planets` | 补充"near bright planets"说明密度不足对天然卫星观测的具体影响，增强说服力。 |
| 3-6 | `These characteristics motivate the need for catalog debiasing within a unified reference frame. A summary of the catalogs adopted in this work is provided in Table~\ref{tab:catalog_overview}.` | `Together with Gaia DR1 and DR2 described in Section~\ref{subsec:gaia}, this work derives corrections for 17 star catalogs in total; their key properties are summarized in Table~\ref{tab:catalog_overview}.` | （1）"motivate the need for..."是空洞过渡语（B5），删去。（2）在引向表格的句子引入"17"，与 Section 2.1 的 Gaia DR1/DR2 合并计入，仅在此处出现一次。 |

---

## 表格部分

### 表头列名

| # | 原文 | 建议修改 | 理由 |
|---|---|---|---|
| T1 | `\colhead{Star Count}` | `\colhead{Number of Stars}` | Part C 明确指出；"Star Count"非 ApJS 标准列名。 |

---

### 星表名称（A5）

| # | 原文 | 建议修改 | 理由 |
|---|---|---|---|
| T2 | `Tycho 2` | `Tycho-2` | A5 |
| T3 | `USNO A2.0` | `USNO-A2.0` | A5 |
| T4 | `UCAC 2` | `UCAC2` | A5 |
| T5 | `UCAC 4` | `UCAC4` | A5 |

---

### 表格排序

| # | 原排序 | 建议排序 | 理由 |
|---|---|---|---|
| T6 | 混排 | 全局字母序（见下表） | 无需解释依据，最简洁；取消分组标题行。 |

新行顺序：

| 序 | 星表 |
|---|---|
| 1 | AC |
| 2 | ACRS |
| 3 | ACT |
| 4 | AGK1 |
| 5 | AGK3 |
| 6 | FK4 catalogue |
| 7 | Gaia DR1 |
| 8 | Gaia DR2 |
| 9 | GSC 1.2 |
| 10 | Hipparcos |
| 11 | PPM |
| 12 | SAO |
| 13 | Tycho-2 |
| 14 | UCAC2 |
| 15 | UCAC4 |
| 16 | USNO-A2.0 |
| 17 | Yale |

原表 Gaia DR2 在前、DR1 在后，字母序下 DR1 应在 DR2 前（历元亦更早）。

---

### tablecomments

| # | 原文 | 建议修改 | 理由 |
|---|---|---|---|
| T7 | `Primary literature references correspond to the original catalog publications listed in the CDS entries.` | `Catalogs are listed in alphabetical order. Gaia DR1 and DR2 are included for completeness; their astrometric properties are described in detail in Section~\ref{subsec:gaia}. The Proper Motion column indicates whether the catalog provides proper-motion data. Coverage gives the approximate fraction of the sky covered by the catalog. Primary literature references correspond to the original catalog publications listed in the CDS entries.` | 补充排序说明、Gaia 参见说明、各列含义说明。 |

---

*生成日期：2026-05-06*  
*确认无误后可授权直接修改 paper_en.tex*
