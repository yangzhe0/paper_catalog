# Section 4 修改对照表

目标期刊：ApJS  
原文件：paper_en/paper_en.tex（lines 210–308）

---

## 4.1 Statistical Properties of the Corrections

### Para 1（line 214）

| # | 原文 | 建议修改 | 理由 |
|---|---|---|---|
| 4.1-1 | `with typical position systematics reaching or exceeding $10^2$~mas` | `with typical position systematics ranging from tens to hundreds of mas, and reaching nearly 1 arcsecond in the most extreme cases (e.g., AGK1)` | 实际数据中 AGK1 的 MAD 约 785 mas，接近 1 角秒；"$10^2$~mas"太笼统且与具体数值不匹配。 |

### Table 3 表头（line 219）

| # | 原文 | 建议修改 | 理由 |
|---|---|---|---|
| 4.1-2 | `$\Delta\alpha_{*,J2000}$ [mas]` / `$\Delta\delta_{J2000}$ [mas]` / `$\Delta\mu_{\alpha *}$ [mas/yr]` / `$\Delta\mu_{\delta}$ [mas/yr]` | `$\Delta\alpha_{2000}$ [mas]` / `$\Delta\delta_{2000}$ [mas]` / `$\Delta\mu_{\alpha}$ [mas\,yr$^{-1}$]` / `$\Delta\mu_{\delta}$ [mas\,yr$^{-1}$]` | 新符号规范；单位格式统一为 ApJS 标准。 |

### Table 3 行顺序与名称（lines 227–230）

| # | 原文 | 建议修改 | 理由 |
|---|---|---|---|
| 4.1-3 | 行顺序：FK4 Catalogue, GSC 1.2, Gaia DR1, Gaia DR2 | 字母序：FK4 catalogue, Gaia DR1, Gaia DR2, GSC 1.2 | Gaia（Ga）在 GSC（GS）之前；与 Table 2 统一。 |
| 4.1-4 | `FK4 Catalogue` | `FK4 catalogue` | 小写 c，与正文一致。 |

### Table 3 tablecomments（line 241）

| # | 原文 | 建议修改 | 理由 |
|---|---|---|---|
| 4.1-5 | `The tabulated values correspond to the median (MED) and median absolute deviation (MAD) of the correction terms over all valid HEALPix sky regions. Position corrections refer to the $\Delta\alpha_*$ and $\Delta\delta$ components at epoch J2000.0. Proper motion corrections are given in units of mas\,yr$^{-1}$.` | `MED denotes the median and MAD the median absolute deviation over all valid tiles. Position corrections $\Delta\alpha_{2000}$ and $\Delta\delta_{2000}$ are in mas; proper motion corrections $\Delta\mu_\alpha$ and $\Delta\mu_\delta$ are in mas\,yr$^{-1}$.` | 新符号规范；"sky regions"→"tiles"；缩短冗余表述。 |

### 正文（line 244）

| # | 原文 | 建议修改 | 理由 |
|---|---|---|---|
| 4.1-6 | `$68.0$~mas in $\Delta\alpha_{*,J2000}$ and $151.9$~mas in $\Delta\delta_{J2000}$` / `in $\Delta\mu_{\alpha *}$` | `$68.0$~mas in $\Delta\alpha_{2000}$ and $151.9$~mas in $\Delta\delta_{2000}$` / `in $\Delta\mu_{\alpha}$` | 新符号规范。 |

---

## 4.2 Spatial Structure

| # | 原文 | 建议修改 | 理由 |
|---|---|---|---|
| 4.2-1 | `HEALPix regions`（line 246） | `HEALPix tiles` | 统一用"tile"。 |

---

## 4.4 Smoothing and Practical Implementation（lines 284–308）

整节按新逻辑重写，结构：动机 → 方法 → 效果（连续性）→ 效果（大尺度保留）

**替换文本：**

```latex
\subsection{Smoothing and Practical Implementation} \label{subsec:smoothing}

For practical applications, a higher-resolution correction map better represents
the spatial structure of catalog systematics. However, directly estimating
corrections at finer resolution (e.g., $N_{\rm side}=256$) would significantly
reduce the number of matched stars per tile, degrading the statistical robustness
of the median estimates.

To balance spatial resolution and statistical stability, we adopt a similar
strategy to that of \citet{Eggl2020}: a continuous correction field is
reconstructed from the statistically robust $N_{\rm side}=64$ tile estimates
using radial basis function (RBF) interpolation with a thin-plate spline kernel
\citep{Wahba1990,Schaback1995}. The interpolation uses the nearest neighboring
tiles as support points, with contributions weighted by angular distance via the
RBF kernel to ensure locality and global smoothness. The final correction product
is provided on a HEALPix grid with $N_{\rm side}=256$. Since these values are
reconstructed from the coarse-grid estimates rather than independently derived
from observations at that resolution, they represent an interpolated continuous
field rather than independent measurements.

The effect on spatial continuity is illustrated in
Figure~\ref{fig:bias_ucac4_zoom_compare_n256}. The reconstructed field eliminates
the block-like structures present in the original tile-based map while preserving
the underlying large-scale patterns. To quantify this improvement, we evaluate
the inter-tile discontinuity $\delta_{\mathrm{disc}}$ defined in
Section~\ref{subsec:interpretation}. As shown in Figure~\ref{fig:bias_jump}, the
high-percentile and maximum values of $\delta_{\mathrm{disc}}$ are reduced by
factors of roughly 2--4 after smoothing.

At the same time, the large-scale spatial structure of the corrections is
preserved, indicating that the smoothing primarily suppresses sampling noise at
small scales rather than altering the underlying systematic patterns.

\begin{figure}[ht!]
\plotone{"../Figue/bias_ucac4_zoom_compare_n256.png"}
\caption{Example of RBF smoothing applied to the correction field.}
\label{fig:bias_ucac4_zoom_compare_n256}
\end{figure}

\begin{figure}[ht!]
\plotone{"../Figue/figure_Y_jump_distribution.png"}
\caption{Cumulative distributions of inter-tile discontinuities before and after smoothing.}
\label{fig:bias_jump}
\end{figure}
```

改动说明：
- "pixel"全部改为"tile"（正文和图注）
- 删除 4.4 中对 $\delta_{\mathrm{disc}}$ 的重复定义，改为引用 Section~\ref{subsec:interpretation}
- 图移至节末（先文字后图，符合 ApJS 惯例）
- 四段结构：动机 / 方法 / 效果：连续性 / 效果：大尺度保留

---

*生成日期：2026-05-06*  
*确认无误后可授权直接修改 paper_en.tex*
