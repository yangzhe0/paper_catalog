# 需要拍板的修改决策清单（all polish · decisions）

目标期刊：ApJS
原文件：`paper_en/paper_en.tex`

## 关于本文件

机械性的、客观的修改（连字符、双花括号、引用前空格、tile/pixel、source/target catalog、positional/position、proper motion 连字符、Gaia~DR 硬空格、删除重复 GSC 举例等共约 35 处）已经直接在 `paper_en.tex` 中落地。

本文件列出**剩余需要你判断**的项目。每条都给出：
- **当前文本**
- **建议修改**
- **理由**
- **决策框** `[ ]`：勾上即认为采纳

按"决策成本（高/中/低）"分组，建议从"低决策成本"开始扫一遍。

---

## ① 低决策成本（用词替换层面，但有偏好风险）

### D1 · 标题：error → bias，连字符规范

`[ ]`

**当前** (line 23–24)
```latex
% \title{Star Catalog Position and Proper Motion Corrections in Natural Satellite Astrometry}
\title{Correction of Star Catalog Positional and Proper Motion Systematic Errors for Natural Satellite Astrometry}
```

**建议**
```latex
\title{Correction of Star Catalog Position and Proper-Motion Systematic Biases for Natural-Satellite Astrometry}
```

**理由**
1. `Errors` 与正文统一术语 `biases` 矛盾（A-3 规范）。
2. `Positional` 与正文 `position correction/offset/difference` 不一致（A-7 规范）。
3. `Proper Motion` 作定语未连字符（A-6）。
4. `Natural Satellite` 作定语未连字符（A-5）。

**风险**
- 标题包含 `Bias` 偶尔被审稿人误读为"有偏估计"——本文中含义无歧义，但可斟酌是否保留 `Errors` 以减少阅读门槛。如果保留 `Errors`，正文 A-3 规范也需要重新评估。

**备选方案**
```latex
\title{Position and Proper-Motion Corrections of Historical Star Catalogs for Natural-Satellite Astrometry}
```
（彻底回避 error/bias 词，强调"corrections"，与 abstract 第二句 "derive position and proper-motion corrections" 完全对应）

---

### D2 · Section 3.2 标题：操作顺序对调

`[ ]`

**当前** (line 142)
```latex
\subsection{Frame and Epoch Propagation}
```

**建议**
```latex
\subsection{Frame Transformation and Epoch Propagation}
```

**理由**
"frame" 不能 `propagate`，原标题语法上错配。改后两个动词分别匹配两个对象，且与正文实际描述顺序一致：先做坐标系变换，再做历元传播。

---

### D3 · Section 4.3 标题改名

`[ ]`

**当前** (line 260)
```latex
\subsection{Origin of the Bias Patterns} \label{subsec:interpretation}
```

**建议**
```latex
\subsection{Interpretation of the Spatial Patterns} \label{subsec:interpretation}
```

**理由**
（1）"Origin" 太宏大，本节只做现象解释。
（2）与 4.2 标题 `Spatial Structure of the Systematic Biases` 形成"现象 → 解释"的配对。
（3）alter2_todo_list 已标记。

---

### D4 · 公式下标 catalog → cat（全文统一）

`[ ]`

**当前**
- 公式 (1) 用 `\alpha_{\rm catalog}`、`\mu_{\alpha,{\rm catalog}}`、`\mu_{\delta,{\rm catalog}}`
- 公式 (3) 中 `t_{\rm catalog}` 共 3 处
- 文中 `catalog epoch` 改为 `the catalog epoch $t_{\rm cat}$`（line 180–181）

**建议**：全文公式中的 `_{\rm catalog}` → `_{\rm cat}`（共 6 处）。文字叙述保留 `catalog`。

**理由**
公式中 6 字母下标在排版上偏丑；2–3 字母下标是标准做法。

**备选**：保持 `_{\rm catalog}` 不动——理由是和正文术语完全一致，零认知成本。**这是个偏好选择**。

---

### D5 · Conclusion 末段术语 stochastic → random

`[ ]`

**当前** (line 416)
```latex
Both tests demonstrate that the proposed approach effectively mitigates catalog-dependent systematic offsets without degrading the stochastic error component, leading to improved consistency in orbit determination solutions \citep{Desmars2013}. The improvement is particularly relevant for historical observations that cannot be directly reduced in the Gaia reference frame.
```

**建议**
```latex
Both tests demonstrate that the proposed approach effectively mitigates catalog-dependent systematic offsets without degrading the random component of the residuals, leading to improved consistency in orbit determination solutions. The improvement is particularly relevant for historical observations that cannot be re-reduced in the Gaia reference frame.
```

**理由**
1. `stochastic error component` 与 5.2 节 `random scatter` / `within-file scatter` 不一致（A-11）。
2. `\citep{Desmars2013}` 在 Introduction Para 1 已引，Conclusion 不必再引。
3. `directly reduced` → `re-reduced`，与全文 `re-reduce` 用语统一。

---

### D6 · Conclusion: 多余形容词与术语清理

`[ ]`

**当前** (line 414)
```latex
Using Gaia DR3 as the astrometric reference, we derive systematic position and proper-motion corrections for 17 historical star catalogs. A unified catalog debiasing framework is developed based on HEALPix sky partitioning combined with RBF interpolation, enabling the construction of continuous all-sky correction fields while suppressing artificial discontinuities introduced by discrete tiling. The resulting model preserves the intrinsic large-scale structure of catalog systematics while removing non-physical small-scale variations.
```

**建议**
```latex
Using Gaia DR3 as the astrometric reference, we derive systematic position and proper-motion corrections for 17 historical star catalogs. A correction framework is developed based on HEALPix sky partitioning combined with RBF interpolation, enabling the construction of continuous all-sky correction fields while suppressing the discontinuities introduced by tile-based estimation. The resulting model preserves the intrinsic large-scale structure of catalog systematics while suppressing small-scale sampling noise.
```

**理由**
1. `unified catalog debiasing framework` → `correction framework`（A-4：framework 用于产物体系，model 用于方法本体）。
2. `artificial discontinuities introduced by discrete tiling` → `discontinuities introduced by tile-based estimation`（与 4.4 节用语一致）。
3. `removing non-physical small-scale variations` → `suppressing small-scale sampling noise`（"non-physical" 措辞过强；本质是采样噪声，4.4 节已有同表述）。

---

### D7 · Conclusion: 中段术语统一

`[ ]`

**当前** (line 416)
```latex
The plate re-reduction test shows that the debiased data exhibit reduced systematic residuals while maintaining the original dispersion of the observations.
```

**建议**
```latex
The plate re-reduction test shows that the debiased data exhibit reduced systematic residuals while preserving the random scatter of the observations.
```

**理由**
`dispersion of the observations` 与 5.2 节 `within-file scatter` / `random scatter` 不一致（A-11）。

---

## ② 中决策成本（句法重写或数字调整，影响阅读）

### D8 · Section 4.1 / Abstract 数字与正文对齐

`[ ]`

**当前**
- Abstract (line 61): `older photographic catalogs show position offsets exceeding 100~mas, accompanied by pronounced spatial structures.`
- Section 4.1 Para 1 (line 208): `... reaching nearly 0.5 arcsecond in the most extreme cases (e.g., AGK1)`

**问题**
AGK1 的 MAD ≈ 785 mas，median ≈ 383 mas（见 Table 3）。
- Abstract 说 "exceeding 100 mas" —— 描述偏弱（实际峰值近 1 arcsec）。
- 4.1 节说 "0.5 arcsecond" —— 描述偏弱（MAD 已达 0.79 arcsec）。

**建议**
- Abstract: `older photographic catalogs show position offsets reaching the hundred-mas to arcsecond level`
- 4.1 节: ``

**理由**
两处都改为 "arcsecond level"，与实际数据一致，且 abstract 与正文措辞同步。

**风险**
"reaching the arcsecond level" 比原措辞略激进，需要确认是否愿意在 abstract 用此较强的描述。

---

### D9 · Abstract 拆长句

`[ ]`

**当前** (line 61) — 第一句 73 词，含 4 个分句
```latex
Precise orbit determination of natural satellites relies on the consistent combination of heterogeneous astrometric observations spanning long time intervals, but the use of different reference star catalogs introduces spatially correlated systematic biases that degrade data consistency and limit orbit accuracy.
```

**建议**：拆为两句
```latex
Precise orbit determination of natural satellites relies on the consistent combination of heterogeneous astrometric observations spanning long time intervals. However, the use of different reference star catalogs introduces spatially correlated systematic biases that degrade data consistency and limit orbit accuracy.
```

**理由**
ApJS abstract 偏好中等句长。原句 73 词、4 分句、含一个 "but" 转折和两个 "that" 嵌套——节奏偏沉。

---

### D10 · Abstract 末句精简

`[ ]`

**当前** (line 61)
```latex
This framework provides a consistent basis for reprocessing historical observations and helps improve the astrometric positioning accuracy of natural satellites, thereby enhancing the precision of orbit determination and dynamical studies for natural-satellite systems.
```

**建议**
```latex
This framework provides a consistent basis for reprocessing historical observations and improves the astrometric accuracy of natural-satellite observations, thereby enhancing the precision of orbit determination and dynamical studies of natural-satellite systems.
```

**理由**
1. `astrometric positioning accuracy of natural satellites` 在正文中无对应；正文用 `astrometric accuracy of natural satellite observations`（Intro Para 6 末）。统一为后者。
2. `helps improve` → `improves`（更直接，符合 abstract 风格）。
3. 介词 `for` → `of` 与 `studies of` 习惯搭配一致。

---

### D11 · Introduction Para 4 拆超长句（C-3）

`[ ]`

**当前** (line 75) — 单句 38 词
```latex
\citet{Tholen2013b} further showed that the lack of proper-motion information in 2MASS can generate regional signatures in high-precision astrometry, motivating the proper-motion-corrected debiasing scheme developed by \citet{Farnocchia2015} with a PPMXL-based reference \citep{Roeser2010}.
```

**建议**：拆为两句
```latex
\citet{Tholen2013b} further found that the absence of proper motions in 2MASS produces regional position offsets in high-precision astrometry. This motivated the proper-motion-corrected scheme of \citet{Farnocchia2015}, which uses PPMXL as the reference catalog \citep{Roeser2010}.
```

**理由**
1. 拆开后两句均在 18–22 词，节奏更舒。
2. `regional signatures` 抽象，改为 `regional position offsets` 与全文术语 A-7 一致。

---

### D12 · Introduction Para 5 句首改写（C-2）

`[ ]`

**当前** (line 78)
```latex
In the context of natural satellites, similar approaches have only recently begun to be explored.
```

**建议**
```latex
Comparable efforts in natural-satellite astrometry remain limited.
```

**理由**
"only recently begun to be explored" 偏口语，且承接 Para 4 末"已有 Eggl(2020) 但不足"略显生硬。直接陈述事实更顺。

---

### D13 · Introduction Para 6 拆超长句（C-4）

`[ ]`

**当前** (line 79) — 单句 41 词
```latex
In this work, we adopt Gaia DR3 as the common reference frame and derive systematic position and proper-motion corrections for 17 star catalogs identified as the most comprehensively used reference catalogs in historical natural-satellite astrometry, based on a systematic survey of the NSDC archive.
```

**建议**：拆为两句
```latex
In this work, we adopt Gaia DR3 as the common reference frame and derive position and proper-motion corrections for 17 historical star catalogs. These 17 catalogs are identified, based on a systematic survey of the NSDC archive, as the most prevalent reference catalogs in historical natural-satellite astrometry.
```

**理由**
1. 单句 41 词偏长，且嵌套 "identified as..." + "based on..." 两层。
2. 拆开后第一句直接陈述工作内容，第二句解释 17 个星表的选取依据。

---

### D14 · 5.2 节超长段拆句（G-6）

`[ ]`

**当前** (line 343) — 单段 99 词，单句最长 30 词
```latex
The typical single-observation residual in this dataset is 100--200~mas, whereas the median catalog correction is only 10--30~mas. At the individual-observation level, the correction signal is dominated by random measurement noise. However, observations within a single file share the same reference catalog and reduction pipeline; averaging over the $N$ observations in a file suppresses the random component by a factor of $1/\sqrt{N}$. We therefore adopt the file-level mean residuals $\overline{\Delta\alpha}$ and $\overline{\Delta\delta}$ as diagnostics of systematic offsets, and the within-file standard deviations $\sigma_\alpha$ and $\sigma_\delta$ as diagnostics of random scatter.
```

**建议**：保持段落不分，但拆为更紧凑的句式
```latex
Typical single-observation residuals in this dataset are 100--200~mas, while median catalog corrections are only 10--30~mas. At the individual-observation level, the correction signal is therefore dominated by random measurement noise. Observations within a single file, however, share the same reference catalog and reduction pipeline; averaging over the $N$ observations of a file suppresses the random component by $1/\sqrt{N}$. We therefore adopt file-level mean residuals $\overline{\Delta\alpha}$ and $\overline{\Delta\delta}$ as diagnostics of systematic offsets, and within-file standard deviations $\sigma_\alpha$ and $\sigma_\delta$ as diagnostics of random scatter.
```

**理由**
1. `whereas` → `while`，主从关系更轻。
2. `dominated by` 后面加上 `therefore` 补全因果。
3. `by a factor of $1/\sqrt{N}$` → `by $1/\sqrt{N}$`（"factor of"在数学表达里多余）。
4. 删去多余 "the"（the file-level → file-level；the within-file → within-file），更紧凑。

---

### D15 · 5.1 节首段精简（G-1）

`[ ]`

**当前** (line 309)
```latex
The earlier reduction, based on the UCAC2 catalog, yielded 943 positions \citep{Qiao2007}, whereas a later re-reduction of the same images using Gaia DR2 as the reference catalog produced 1007 positions, including 941 updated measurements \citep{Yan2020}.
```

**建议**
```latex
The earlier reduction, based on UCAC2, yielded 943 positions \citep{Qiao2007}, whereas a later re-reduction of the same frames using Gaia DR2 produced 1007 positions \citep{Yan2020}.
```

**理由**
1. `the UCAC2 catalog` 啰嗦，UCAC2 已是星表名。
2. `same images` → `same frames`（与上一句 "Triton CCD frames" 一致；A-15）。
3. `using Gaia DR2 as the reference catalog` → `using Gaia DR2`（reference catalog 含义在 Section 2 已建立，无需重复）。
4. 删除 `including 941 updated measurements`——这两个数字（1007 与 941）的关系下一句不再用到，反而引起读者困惑。

---

### D16 · 5.1 节末段拆句（G-4）

`[ ]`

**当前** (line 327) — 单句 36 词
```latex
Although the debiasing model is constructed using Gaia DR3 whereas the benchmark reduction uses Gaia DR2 as the reference catalog, both Gaia releases share a consistent ICRS realization, and the DR3--DR2 differences are negligible compared with the original UCAC2 systematic offsets. The reduction in position offset relative to this benchmark therefore provides a conservative validation of the debiasing model.
```

**建议**
```latex
The debiasing model is built from Gaia DR3, whereas the benchmark reduction uses Gaia DR2 as the reference catalog. Since both releases share a consistent ICRS realization and their differences are far smaller than UCAC2 systematics.
```

**理由**
1. 拆为两句（19 + 27 词）。
2. `Although ... whereas` 双让步连词重叠，改为 `whereas` 单一对比。
3. `provides a conservative validation` → `constitutes a conservative test`（更地道的英文搭配）。

---

### D17 · 5.2 节验证样本描述（G-5）

`[ ]`

**当前** (line 333)
```latex
The validation sample consists of 11\,731 absolute astrometric observations of the Galilean satellites (J1--J4) from the LTE/NSDC archive, spanning the period 1962--2019 and covering 8 reference catalogs across 19 observation files. Because some files contain segments reduced with multiple catalogs, observations are grouped by (file, catalog) pairs, giving 21 groups.
```

**建议**
```latex
The validation sample consists of 11\,731 absolute astrometric observations of the four Galilean satellites from the NSDC archive, spanning 1962--2019 and covering 8 reference catalogs across 19 observation files. Because some files contain segments reduced with multiple catalogs, observations are grouped by (file, catalog) pairs, giving 21 groups.
```

**理由**
1. `the Galilean satellites (J1--J4)` → `the four Galilean satellites`（J1–J4 编号写法不必要）。
2. `LTE/NSDC` → `NSDC`（NSDC 在 Intro Para 2 已与 LTE 关联，5.2 节简写即可）。
3. `spanning the period` → `spanning`（删冗余 the period）。

---

### D18 · 5.2 节示例顺序与表格一致

`[ ]`

**当前** (line 388–389)
```latex
Files reduced with catalogs carrying large known biases show substantial positive improvements: AGK3/jg0032 ($+101$~mas), UCAC2/jg0043 ($+24$~mas), Gaia DR1/jg0059 ($+20$~mas), and Tycho-2/jg0023 ($+21$~mas).
```

**建议**：把 `catalog/file` 改为 `file/catalog` 顺序，与 Table 2 的"file 列在前"对齐
```latex
Files reduced with catalogs carrying large known biases show substantial positive improvements: jg0032/AGK3 ($+101$~mas), jg0043/UCAC2 ($+24$~mas), jg0059/Gaia DR1 ($+20$~mas), and jg0023/Tycho-2 ($+21$~mas).
```

**理由**
Table 2 列序为 `File | Catalog | ...`，正文与表格用同一顺序更便于读者查表。同时下一句的 `jg0043/UCAC4` `jg0044` 已是"file 在前"格式，前后保持一致。

---

### D19 · 5.2 节"near-zero change" 措辞

`[ ]`

**当前** (line 391)
```latex
The two Gaia DR2 files show near-zero change, consistent with the negligible correction amplitude for that catalog.
```

**建议**
```latex
The two Gaia DR2 files show no significant change, as expected for a catalog whose corrections are negligible.
```

**理由**
"near-zero change" 偏口语；ApJS 多用 "no significant change" 或 "remain unchanged"。

---

### D20 · 4.1 节 USNO-A2.0 数字格式（F-3）

`[ ]`

**当前** (line 238)
```latex
Its median corrections at J2000.0 are $68.0$~mas in $\Delta\alpha_{\rm J2000}$ and $151.9$~mas in $\Delta\delta_{\rm J2000}$, with MAD values of $104.2$~mas and $121.5$~mas, respectively.
```

**建议**
```latex
The median corrections at J2000.0 are $\Delta\alpha_{\rm J2000} = 68.0$~mas and $\Delta\delta_{\rm J2000} = 151.9$~mas, with MAD values of 104.2 and 121.5~mas, respectively.
```

**理由**
1. `Its` 与上一句 `USNO-A2.0 provides a representative example` 衔接其实不顺——上一句"Its"指 USNO-A2.0，但本句已经在专门讨论它，"Its" 可以省略。
2. `$68.0$~mas in $\Delta\alpha_{\rm J2000}$` 这种 "数值 in 符号" 的英文用法不自然，改为 "符号 = 数值" 更标准。

---

### D21 · 4.1 节 RA/Dec → α/δ 一致

`[ ]`

**当前** (line 240)
```latex
... while the proper-motion corrections display asymmetric behavior between RA and Dec.
```

**建议**
```latex
... while the proper-motion corrections display asymmetric behavior between $\alpha$ and $\delta$.
```

**理由**
全文公式与 Table 表头都用 $\alpha$、$\delta$，而文中突然出现 "RA"、"Dec" 是新缩写。统一为符号即可。

---

### D22 · 4.1 节 sky-to-sky scatter（F-2）

`[ ]`

**当前** (line 208)
```latex
... show significantly larger offsets and broader sky-to-sky scatter, with typical position systematics ranging from tens to hundreds of mas, and reaching nearly 0.5 arcsecond in the most extreme cases (e.g., AGK1).
```

**建议**（与 D8 联动）
```latex
... show significantly larger offsets and broader spatial dispersion, with typical position systematics ranging from tens to hundreds of mas and reaching the arcsecond level in the most extreme cases (e.g., AGK1).
```

**理由**
1. `sky-to-sky scatter` 仅此一处出现（A-11），改为 `spatial dispersion` 与 4.1 节前文 `with small dispersions across the sky` 配对。
2. 与 D8 同步把数字描述改为 `arcsecond level`。
3. 多余逗号 `, and reaching` → `and reaching`。

---

### D23 · 4.2 节 localized → block-like（F-5）

`[ ]`

**当前** (line 246)
```latex
As shown in Figure~\ref{fig:bias_usno_a2_2x2}, the USNO-A2.0 corrections display large-scale gradients together with localized discontinuities.
```

**建议**
```latex
As shown in Figure~\ref{fig:bias_usno_a2_2x2}, the USNO-A2.0 corrections display large-scale gradients together with block-like discontinuities.
```

**理由**
4.3 节正文用 "block-like or discontinuous structures"；4.2 节先用 "localized" 后用 "block-like" 是同物两名。统一为 `block-like`。

---

### D24 · 4.4 节 $k=8$ 是否保留

`[ ]`

**当前** (line 287)
```latex
The interpolation uses the $k=8$ nearest neighboring tiles as support points, with contributions weighted by angular distance via the RBF kernel to ensure locality and global smoothness.
```

**建议（二选一）**

(A) **删除具体数字**：
```latex
The interpolation uses the nearest neighboring tiles as support points, with contributions weighted by angular distance via the RBF kernel to ensure locality and global smoothness.
```

(B) **保留并补充说明**：
```latex
The interpolation uses the $k=8$ nearest neighboring tiles as support points (empirically chosen to balance locality and smoothness), with contributions weighted by angular distance via the RBF kernel.
```

**理由**
当前直接给 $k=8$ 但没说为什么是 8。要么删（方法节不必给所有超参），要么补一笔说明。**A 简洁、B 完整，看你想保留多少细节**。

---

### D25 · 3.5 节"set of parameters"措辞（E-6）

`[ ]`

**当前** (line 191)
```latex
The resulting corrections are stored on a HEALPix grid. Each tile is associated with a set of parameters, including the HEALPix index, $\Delta \alpha_{\rm J2000}$, $\Delta \delta_{\rm J2000}$, $\Delta \mu_{\alpha}$, and $\Delta \mu_{\delta}$.
```

**建议**
```latex
The resulting corrections are stored on a HEALPix grid. Each tile is associated with the four correction parameters $\Delta\alpha_{\rm J2000}$, $\Delta\delta_{\rm J2000}$, $\Delta\mu_\alpha$, $\Delta\mu_\delta$, indexed by its HEALPix pixel number.
```

**理由**
1. `a set of parameters, including ...` 句式松散；改为 "the four correction parameters" 更明确。
2. `HEALPix index` 改为 `HEALPix pixel number`（更标准的字段名）。

---

## ③ 高决策成本（结构性 / 已在前序 alter 中标注但需复议）

### D26 · 引言 Para 4 末句的位置（C-1）

`[ ]`

**当前** Para 4 末（line 75）
```latex
... \citet{Eggl2020} utilized the Gaia DR2 reference frame to derive ... 26 astrometric catalogs used in asteroid astrometry. However, the catalog selection in that work is tailored to asteroid observations and does not cover several catalogs prevalent in historical natural-satellite astrometry, particularly those spanning earlier observational epochs. As the raw observational data are in many cases no longer available for re-reduction, applying catalog corrections to the existing reduced positions is the only viable means of recovering their astrometric accuracy. Taken together, these studies establish that catalog debiasing within a common reference frame is essential for improving the consistency of astrometric data.
```

**建议**：把 `As the raw observational data are in many cases no longer available...` 这一句**移到 Para 5 末**（紧接 `is still lacking.` 之后），作为 Para 5 与 Para 6 的过渡。

**理由**
1. 这句话本质是"为什么本工作必要"——属于 motivation，更适合放在 Para 5 末（紧邻 Para 6 "In this work"）。
2. Para 4 末的逻辑收束为"Taken together, these studies establish..."更纯粹是文献综述结论。
3. 移走后 Para 4 缩短一些，与 Para 5 长度差距缩小（K 节统计：Para 4 196 词、Para 5 79 词反差太大）。

**风险**
逻辑链改变；Para 5 增长后整体节奏更平衡，但需要确认你认为"raw observational data 不可获取"这个论点放在 Para 5（讲天然卫星现状）还是 Para 4（讲文献综述）更合理。

---

### D27 · 5.1 节验证段重写（已在 alter2_section5 R1+R2 提出）

`[ ]`

**当前** (line 317)
```latex
Relative to the Gaia DR2 re-reduction, the UCAC2-based reduction has a mean position offset of 86.2~mas and a median of 82.5~mas. After application of the Gaia DR3-based debiasing model, the mean and median offsets decrease to 76.2~mas and 67.7~mas, respectively. This corresponds to an 11.6\% reduction in the mean offset, with 78.0\% of the common positions showing smaller $\Delta$ values after correction. The remaining difference should not be interpreted solely as uncorrected catalog bias, because the two reductions also differ in centroiding and reduction procedures \citep{Yan2020}.
```

**问题**
- 末句防御性语气过重（"should not be interpreted solely as ..."）。
- alter2_section5 中 R1/R2 已规划重写，但因涉及"在数字段之前先建立 Δ 由两部分构成的前提"这种结构改动，这里再列出来等你确认。

**建议（按 alter2_section5 R1+R2 思路）**
在数字段**之前**插入一段前提说明：
```latex
The position offset $\Delta$ measured here arises from two contributions: catalog-dependent systematic biases (which the debiasing model addresses) and reduction-procedure differences such as centroiding (which it does not). The Gaia DR3-based debiasing therefore acts on the first component while leaving the second unchanged \citep{Yan2020}.
```

并把数字段末句删除：
```latex
... with 78.0\% of the common positions showing smaller $\Delta$ values after correction.
```
（删去 "The remaining difference should not be interpreted..." 一句）

**理由**
1. 把"两部分构成"的前提前置后，读者读到数字段就不会困惑"为什么没全部消除"。
2. 末句的防御性语气可以彻底删掉。

**风险**
段落数量从 1 段变 2 段；数字段的解释逻辑改变。需要决定是否采纳这个结构性变化。

---

### D28 · 5.2 节末段重写（alter2_section5 中 5.2-1 已提出）

`[ ]`

**问题**：alter2_section5 文件中已有详细方案（"Taken together"段落重写），此处提示需要决定是否采纳那个建议。

**理由**
当前段落 Panel (a)/(b) 混杂叙述、"Taken together...diagnostics support" 句式绕口、Table 4 在叙述中作用未体现。alter2_section5 已给出重写文本。

**风险**
原文涉及对 Figure 6 Panel A 的引用，alter2_section5 提到 Panel A 待重绘，所以重写时会暂时移除该引用——需要确认现状。

---

### D29 · 公式 (1) 后增加 cos δ 说明

`[ ]`

**当前** (line 173–179)
```latex
\begin{equation}
\begin{aligned}
\Delta \alpha = (\alpha_{\rm catalog}-\alpha_{\rm Gaia})\cos\delta_{\rm Gaia},\quad
\Delta \delta = \delta_{\rm catalog}-\delta_{\rm Gaia},\\
\Delta \mu_{\alpha} = \mu_{\alpha,{\rm catalog}}-\mu_{\alpha,{\rm Gaia}},\quad
\Delta \mu_{\delta} = \mu_{\delta,{\rm catalog}}-\mu_{\delta,{\rm Gaia}}.
\end{aligned}
\end{equation}

Here $\delta_{\rm Gaia}$ denotes the Gaia DR3 declination of the matched source at the comparison epoch. The $\cos\delta_{\rm Gaia}$ factor converts the coordinate difference to a great-circle arc length.
```

**当前已经有 cos δ 说明**，但 alter2_section3 中 3.4-1c 曾建议改为更简明的版本：
```latex
Here $\Delta\alpha$ includes the $\cos\delta$ factor, so that both position differences represent great-circle arc lengths.
```

**建议**：保持当前版本（已经够好），不再改动。

**理由**
当前两句已经说明 (1) 哪个 δ；(2) cos δ 的作用——alter2_section3 里更短的版本反而少了"哪个 δ"的信息。

**这条建议你直接 [✓] 标记 "保持现状不改"**。

---

## ④ 结构性建议（不一定要做，但值得考虑）

### D30 · Section 2.2 Para 2 单句段是否合并

`[ ]`

**当前** (line 95) — 50 词单句独立成段
```latex
Optical astrometric observations from different epochs rely on a variety of reference star catalogs that differ significantly in epoch, sky coverage, source density, and available astrometric parameters. The catalogs included in this study are those most prevalently used in historical natural-satellite observations, as identified from a systematic survey of the NSDC archive.
```

（注：现在已是 2 句段，刚才 D2 删除 GSC 那句之后）

**建议**：与下一段（讲三类星表细节那段）合并？

**或保留现状**——单段独立陈述选取依据，紧邻 Table 1，结构上其实挺好的。

**理由**
看你的写作偏好。如果觉得段太短可以合并；如果希望把"选取依据"独立成段强调，保持现状即可。

**这条非必须，看个人风格选择即可**。

---

### D31 · 致谢段 IMCCE/LTE 名称

`[ ]`

**当前** (line 431)
```latex
This work has made use of the Natural Satellites Data Center (NSDC), maintained by the Laboratoire Temps Espace (LTE), which provides a comprehensive compilation of astrometric observations of planetary satellites. We are grateful to the NSDC team for their efforts in collecting and maintaining these datasets.
```

**问题**：与 Intro Para 2 (line 71) `Natural Satellites Data Center (NSDC), maintained by the Laboratoire Temps Espace (LTE) at Paris Observatory` 比，致谢里少了 "at Paris Observatory"。

**建议**：保持致谢段现状（致谢语境下信息可以略简），但 Intro 与致谢两处都使用相同的全称展开。当前已基本一致，无需改动。

**这条直接 [✓] 标记 "保持现状"**。

---

## 决策建议路径

如果想最小化决策时间，建议按以下顺序快速勾选：

**第一轮（10 分钟，预期都采纳）**
D2、D3、D5、D7、D11、D12、D13、D15、D16、D17、D18、D19、D21、D23、D29、D31

**第二轮（看偏好）**
D1（标题选 主方案 / 备选方案 / 不动）
D4（公式下标 cat vs catalog）
D8（数字描述）
D24（$k=8$ 删 vs 留）

**第三轮（结构性）**
D26（Para 4 末句搬家）
D27（5.1 节插入"两部分构成"前提）
D28（5.2 节末段重写）

---

## 完成后的最终自检 grep（与 alter2_all_polish.md M 节相同）

机械修改已完成自检：
- ✅ `[a-zA-Z0-9]\\citep`：0 命中
- ✅ `{{\rm`：0 命中
- ✅ `source catalog`：0 命中
- ✅ `HEALPix pixels`：0 命中
- ✅ `proper motion ` 后跟名词作定语：仅剩**标题中**的 `Proper Motion Corrections` 与 `Proper Motion Systematic Errors`（待 D1 决策）
- ✅ `positional`（非注释行）：仅剩你的偏好待定项

---

*生成日期：2026-05-18*
