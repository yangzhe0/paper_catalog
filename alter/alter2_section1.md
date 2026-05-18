# Introduction 修改对照表

目标期刊：ApJS  
原文件：paper_en/paper_en.tex  
段落编号按 Introduction 内顺序（Para 1–6）

---

## Para 2

| # | 原文 | 建议修改 | 理由 |
|---|---|---|---|
| 2-1 | `A large body of natural satellite astrometry has been compiled in the Natural Satellite Data Center (NSDC) maintained by IMCCE.` | `A large number of astrometric positions of natural satellites have been compiled in the Natural Satellite Data Center (NSDC) of the Institut de Mécanique Céleste et de Calcul des Éphémérides (IMCCE).` | （1）"natural satellite astrometry"语义模糊，改为"astrometric positions of natural satellites"明确说明是位置测量结果。（2）IMCCE 在文中首次出现，按 ApJS 规范需写出全称并括注缩写。 |
| 2-2 | `regional systematic errors` | `regional systematic biases` | 按术语规范（A3节）：用"bias"描述星表固有的系统性偏差，"error"保留给随机误差分量。 |

---

## Para 3

| # | 原文 | 建议修改 | 理由 |
|---|---|---|---|
| 3-1 | `resulting in approximately 51,170 astrometric measurements that have been incorporated into the NSDC database.` | `yielding more than 50,000 astrometric positions, a portion of which has been incorporated into the NSDC database.` | （1）用户要求：不写具体数字，以"超过5万个"表达即可。（2）并非所有观测均已收录，改为"a portion of which"更准确。（3）"astrometric measurements"→"astrometric positions"与后文术语一致。 |
| 3-2 | `a series of studies has been carried out on the astrometry and orbit improvement of Saturnian satellites` | `a series of studies has been carried out on the astrometric reduction and orbit determination of Saturnian satellites` | "astrometry and orbit improvement"搭配不自然；"astrometric reduction and orbit determination"是更标准的天文测量术语。 |

---

## Para 4

| # | 原文 | 建议修改 | 理由 |
|---|---|---|---|
| 4-1 | `Systematic errors in star catalogs have been investigated extensively.` | `Systematic biases in star catalogs have been investigated extensively.` | 与术语规范一致（星表系统性问题用"bias"而非"error"）。 |
| 4-2 | `optical observations contain non-negligible systematic components` | `optical observations contain non-negligible systematic biases` | 同上，"systematic components"改为"systematic biases"。 |
| 4-3 | `More generally, the reliability of astrometric catalogs and their proper motions must be assessed with care in precision applications \citep{Teixeira2014}.` | **【整句删除】** | 用户要求删除。该句是泛泛而论，未推动叙述逻辑，且 Teixeira2014 引用在后文也未再出现，可整体去掉。 |
| 4-4 | `More recently, \citet{Eggl2020} utilized the high-precision Gaia reference frame to derive consistent position and proper motion corrections for a wide range of historical catalogs. Taken together, these studies establish that catalog debiasing within a common reference frame is essential for improving the consistency of astrometric data.` | `More recently, \citet{Eggl2020} utilized the Gaia DR2 reference frame to derive position and proper motion corrections for 26 astrometric catalogs used in asteroid astrometry. However, the catalog selection in that work is tailored to asteroid observations and does not cover several catalogs prevalent in historical natural-satellite astrometry, particularly those spanning earlier observational epochs. Taken together, these studies establish that catalog debiasing within a common reference frame is essential for improving the consistency of astrometric data.` | 用户要求：在 Eggl(2020) 之后引出其不足之处，为本文工作做铺垫。两点不足：（1）星表选取面向小行星测量，未覆盖天然卫星历史观测中普遍使用的较老星表；（2）基于 Gaia DR2，现可使用更精确的 DR3。同时将"high-precision"去掉（DR2 是当时的精度，冗余描述），并将"a wide range of"改为具体数字"26"，与 Eggl(2020) 原文一致。 |

---

## Para 5

| # | 原文 | 建议修改 | 理由 |
|---|---|---|---|
| 5-1 | `In the context of natural satellites, similar approaches have only recently begun to be explored.` | **【不采用，待定】** 原意：在 Para 5 开头补充说明"天然卫星与小行星所用星表不同、时间跨度更长"，回应导师关于"为什么不能直接用小行星改正方案"的批注。用户认为文字表达有问题，暂搁置，待重新措辞后再议。 | — |

---

## Para 6

| # | 原文 | 建议修改 | 理由 |
|---|---|---|---|
| 6-1 | `we adopt Gaia DR3 as the common reference frame and derive systematic corrections for 17 star catalogs frequently used in historical observations of natural satellites.` | `we adopt Gaia DR3 as the common reference frame and derive systematic position and proper-motion corrections for 17 star catalogs identified as the most comprehensively used reference catalogs in historical natural-satellite astrometry, based on a systematic survey of the NSDC archive.` | 用户要求：给出17个星表选取依据的合理叙述。改为"基于NSDC档案的系统性统计"，避免直接说"因为木星用了"，同时在学术上站得住脚。并补充"position and proper-motion"使内容更具体。 |
| 6-2 | `Building upon established catalog debiasing schemes, we introduce adaptations tailored to satellite astrometry, including refined cross-matching criteria and additional validation steps.` | `Building upon the catalog debiasing framework of \citet{Eggl2020}, we introduce adaptations tailored to natural-satellite astrometry, including refined cross-matching criteria and additional validation steps.` | "established catalog debiasing schemes"过于泛泛；明确引用 Eggl(2020) 更规范，也与 Para 4 的论述形成呼应。 |
| 6-3 | `supports improved orbit determination, tidal evolution studies, and investigations of complex dynamical behavior in satellite systems.` | `supports improved astrometric accuracy of natural satellite observations, thereby enhancing the precision of orbit determination and dynamical studies of natural satellite systems.` | 用户要求：逻辑改为"先提升天体测量精度，进而改善轨道确定和动力学研究"，层次更清晰。同时删去"tidal evolution"和"complex dynamical behavior"等超出本文范围的表述。 |

---

## 额外问题（自查发现）

| # | 位置 | 原文 | 建议修改 | 理由 |
|---|---|---|---|---|
| E-1 | Para 2 vs Acknowledgments | 正文：`Natural Satellite Data Center` / 致谢：`Natural Satellites Data Center` | 统一为 `Natural Satellites Data Center (NSDC)`（复数） | 官方名称为复数形式（NSDC 网站），正文与致谢需一致。 |
| E-2 | Para 4 | `introduced a spatially resolved correction scheme` | `introduced a spatially resolved debiasing scheme` | 与术语规范一致，统一用"debiasing scheme"描述方法。 |
| E-3 | Para 5 | `confirming the effectiveness of this approach in improving observational consistency.` | `confirming the effectiveness of this approach in improving astrometric consistency.` | "observational consistency"语义模糊；"astrometric consistency"更准确，指位置归算的自洽性。 |
| E-4 | Para 5 | `a systematic and unified debiasing framework for commonly used reference catalogs in natural satellite astrometry is still lacking.` | `a systematic debiasing framework covering the full range of reference catalogs commonly used in natural-satellite astrometry is still lacking.` | "unified"与"systematic"重复表意；改为"covering the full range of"更具体地说明缺口所在（覆盖范围不够），去掉"unified"。连字符规范同上。 |
| E-5 | Para 4 | `proper-motion-aware treatment` | `proper-motion-corrected debiasing scheme` | "treatment"偏口语；"scheme"与全文术语一致（参照 Eggl 2020 的用词）。 |

---

*生成日期：2026-05-05*  
*确认无误后可授权直接修改 paper_en.tex*
