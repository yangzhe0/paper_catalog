# Section 3 修改对照表

目标期刊：ApJS  
原文件：paper_en/paper_en.tex（lines 143–211）

符号规范（本节统一）：
- 固定历元改正（下标）：$\Delta\alpha_{2000}$，$\Delta\delta_{2000}$
- 星表历元中间量（括号，变量）：$\Delta\alpha(t_{\rm cat})$，$\Delta\delta(t_{\rm cat})$
- 时间相关应用（括号，变量）：$\Delta\alpha(t)$，$\Delta\delta(t)$
- 自行改正：$\Delta\mu_\alpha$，$\Delta\mu_\delta$（不带星号）
- 全文赤经差均含 $\cos\delta$，即 $\Delta\alpha = (\alpha_{\rm cat}-\alpha_{\rm Gaia})\cos\delta$；说明位置在 Eq(1) 之后

---

## 3.1 Overview of the Method

| # | 原文 | 建议修改 | 理由 |
|---|---|---|---|
| 3.1-1 | `within each sky region` | `within each tile` | 统一使用"tile"。 |
| 3.1-2 | 第二段整段（`The method uses...J2000.0.`） | **删除** | 3.1 只做流程概述；参数符号在 3.4 方程出现时自然引入。 |

---

## 3.2 标题

| # | 原文 | 建议修改 | 理由 |
|---|---|---|---|
| 3.2-0 | `\subsection{Epoch Propagation and Frame Transformation}` | `\subsection{Frame Transformation and Epoch Propagation}` | 操作顺序：先坐标系变换，再历元传播。 |

---

## 3.2 正文

| # | 原文 | 建议修改 | 理由 |
|---|---|---|---|
| 3.2-1 | `For catalogs not originally in the ICRS (e.g., FK4), coordinates are first transformed into the ICRS` | `For catalogs based on the FK4 reference frame (AC, AGK1, AGK3, FK4 catalogue, and Yale), coordinates are first transformed into the ICRS` | 列出涉及的具体星表，而非用 e.g. 模糊带过。 |

---

## 3.3 Sky Partitioning and Cross-Matching

| # | 原文 | 建议修改 | 理由 |
|---|---|---|---|
| 3.3-1 | `within a search radius of $1''$.` | `within a search radius of $1''$ \citep{Farnocchia2015}.` | 补引用。 |

---

## 3.4 Bias Estimation

逻辑顺序：Eq(1) 定义逐对差值 → $\cos\delta$ 说明（紧跟方程后） → 无自行情形 → tile 中位数 → 输出四元组（结果）

### Eq(1) 及方程后说明

| # | 原文 | 建议修改 | 理由 |
|---|---|---|---|
| 3.4-1a | `\Delta \alpha_* = (\alpha_{\rm cat}-\alpha_{\rm Gaia})\cos\delta` | `\Delta \alpha = (\alpha_{\rm cat}-\alpha_{\rm Gaia})\cos\delta` | 去掉星号。 |
| 3.4-1b | `\Delta \mu_{\alpha *} = \mu_{\alpha *{\rm cat}}-\mu_{\alpha *{\rm Gaia}}` | `\Delta \mu_{\alpha} = \mu_{\alpha,{\rm cat}}-\mu_{\alpha,{\rm Gaia}}` | 去掉星号；下标用逗号分隔。 |
| 3.4-1c | （Eq(1) 后无说明） | 在 Eq(1) 与下一段之间新增：`Here $\Delta\alpha$ includes the $\cos\delta$ factor, so that both position differences represent great-circle arc lengths.` | $\cos\delta$ 约定在方程出现后立即说明。 |

### 无自行星表处理

| # | 原文 | 建议修改 | 理由 |
|---|---|---|---|
| 3.4-2 | `For catalogs without proper motion information, only positional differences are used, while proper motion terms are constrained through Gaia-based propagation.` | `For catalogs without proper motion information, only position differences are used. In this case, Gaia source positions are propagated to the catalog epoch $t_{\rm cat}$, and the differences $\Delta\alpha(t_{\rm cat})$ and $\Delta\delta(t_{\rm cat})$ are computed at that epoch. The tile-level medians are then referred to J2000.0 using the median Gaia proper motion of the tile.` | 明确无自行的两步：推进 Gaia 到星表历元比较，再用 Gaia 自行折算到 J2000.0。 |

### tile 中位数与输出

| # | 原文 | 建议修改 | 理由 |
|---|---|---|---|
| 3.4-3 | `(\Delta \alpha_{*,2000}, \Delta \delta_{2000}, \Delta \mu_{\alpha *}, \Delta \mu_{\delta}).` | `(\Delta \alpha_{2000},\, \Delta \delta_{2000},\, \Delta \mu_{\alpha},\, \Delta \mu_{\delta}).` | 新符号规范；去掉星号。 |

### 线性模型移出

| # | 原文 | 建议修改 | 理由 |
|---|---|---|---|
| 3.4-4 | `For an arbitrary epoch $t$...` 及 Eq(3) | **整块移入 3.5** | 应用公式放在 3.5 节。 |

---

## 3.5 Correction Tables and Application

| # | 原文 | 建议修改 | 理由 |
|---|---|---|---|
| 3.5-1 | `$\Delta \alpha_{2000}$, $\Delta \delta_{2000}$, $\Delta \mu_{\alpha *}$, and $\Delta \mu_{\delta}$` | `$\Delta \alpha_{2000}$, $\Delta \delta_{2000}$, $\Delta \mu_{\alpha}$, and $\Delta \mu_{\delta}$` | 去掉自行的星号。 |
| 3.5-2 | `In practical applications...` 段落前 | 插入从 3.4 移来的线性模型：`For an arbitrary epoch $t$, the corrections are applied via` + Eq: $\Delta\alpha(t) = \Delta\alpha_{2000} + \Delta\mu_\alpha\,\Delta t$，$\Delta\delta(t) = \Delta\delta_{2000} + \Delta\mu_\delta\,\Delta t$，$\Delta t = t - 2000.0$ | 使用方法在此统一说明。 |
| 3.5-3 | `\Delta \alpha_*(t)` and `\Delta \delta(t)` | `\Delta \alpha(t)` and `\Delta \delta(t)` | 去掉星号。 |
| 3.5-4 | `...thereby aligning the observations with the Gaia DR3 reference frame.` | 句末追加：`For the data format and usage of the released correction tables, see Section~\ref{sec:data}.` | 引向 Data 节。 |

---

## Table 3（Section 4.1）

| # | 原文 | 建议修改 | 理由 |
|---|---|---|---|
| T3-1 | 行顺序：FK4 Catalogue, GSC 1.2, Gaia DR1, Gaia DR2 | 字母序：FK4 catalogue, Gaia DR1, Gaia DR2, GSC 1.2 | Gaia（Ga）在 GSC（GS）之前。 |
| T3-2 | `FK4 Catalogue` | `FK4 catalogue` | 小写 c，与正文一致。 |
| T3-3 | 表头 `$\Delta\alpha_{*,J2000}$ [mas/yr]` 等 | `$\Delta\alpha_{2000}$ [mas]`，`$\Delta\delta_{2000}$ [mas]`，`$\Delta\mu_{\alpha}$ [mas\,yr$^{-1}$]`，`$\Delta\mu_\delta$ [mas\,yr$^{-1}$]` | 新符号规范；位置单位为 mas。 |
| T3-4 | tablecomments | 开头补充：`MED denotes the median and MAD the median absolute deviation over all valid tiles.` | MED、MAD 需在表注中定义。 |

---

*生成日期：2026-05-06*  
*确认无误后可授权直接修改 paper_en.tex*
