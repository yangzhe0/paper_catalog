# 全文一致性 & 文风统一对照表（all polish）

目标期刊：ApJS
原文件：`paper_en/paper_en.tex`
关注点（区别于前序 section1–5）：**整篇行文一致性**——同一概念用同一名词、同一结构、同一缩写；段落节奏、句式繁简程度统一；删除残留的"小作文式"语气。

> ApJS 的核心审美：**简单、克制、对仗**。修饰语越少越好；同一个概念在第一次出现时定型，后文只复用，绝不"换个说法"。

---

## A. 全局术语统一（最关键）

下表是全文最严重的"一物多名"问题。每一行只允许保留**一个**叫法，其余全部改齐。

| # | 概念 | 出现过的写法（部分） | **建议唯一保留** | 备注 |
|---|---|---|---|---|
| A-1 | HEALPix 单元格 | `tile` / `pixel` / `HEALPix pixel` / `HEALPix region` / `sky region` | **`tile`** | 仅当指原始 HEALPix 输出像素索引（HEALPix index）时保留"pixel"一词；正文叙述一律 `tile`。当前残留：line 269 `HEALPix pixels`、line 191 `HEALPix index`（前者改为 tile，后者作为字段名保留）。 |
| A-2 | 待改正星表（与 Gaia 比对的那一方） | `target catalog` / `source catalog` / `the catalog` | **`target catalog`** | 当前 line 281 出现 `source catalog`，需改为 `target catalog`。Gaia DR3 是 `reference catalog`（reference frame 与 reference catalog 区分清楚）。 |
| A-3 | 系统性偏差 | `systematic error` / `systematic bias` / `systematic offset` / `systematic component` | **`systematic bias`**（普遍） + **`systematic offset`**（数值层面，特指残差/平均残差） | "error"只保留给随机误差。**标题**目前是 `Positional and Proper Motion Systematic Errors`——与正文规范冲突，建议改为 `Positional and Proper-Motion Systematic Biases`。 |
| A-4 | 改正模型 | `debiasing model` / `correction model` / `catalog debiasing model` / `correction framework` / `Gaia DR3-based correction model` / `Gaia DR3-based debiasing model` | **`debiasing model`**（指模型本体）+ **`correction framework`**（指含数据、代码、文档的整体）+ **`correction tables`**（指释出的数值产物） | 这三个层级要分开。当前 5.1 节末的 `correction model` 与全文 `debiasing model` 不一致，统一为 `debiasing model`。 |
| A-5 | "natural satellite" 作定语 | `natural satellite astrometry` / `natural-satellite astrometry` | **`natural-satellite`**（带连字符，做形容词时） | 不带连字符的形式只用作名词主语/宾语：`natural satellites`。当前 abstract 第 1 句和 keyword 块使用不带连字符——**abstract 内**的 `natural satellite astrometry` 应改为 `natural-satellite astrometry`。 |
| A-6 | "proper motion" 作定语 | `proper motion corrections` / `proper-motion corrections` | **`proper-motion`**（做形容词时） | 当前混用。所有 `proper motion + N` 改为 `proper-motion + N`。例：`proper motion corrections` → `proper-motion corrections`；`proper motion accuracy` → `proper-motion accuracy`。 |
| A-7 | 位置 | `position` / `positional` | 形容词性大多用 **`position`**（如 `position correction`、`position offset`、`position difference`）；只有用于强调"位置上的（在度量层面）"时才用 `positional` | 当前不一致：5.1 节用 `positional offset`、`positional differences`，但全文（含 abstract、Section 4）用 `position offsets/corrections/differences`。**统一为 `position offset`、`position difference`、`position correction`**。`positional` 仅保留 Introduction Para 1 的 `primary positional constraints`（此处与"约束"搭配更自然）。 |
| A-8 | 单位 mas/yr | `mas/yr` / `mas\,yr$^{-1}$` / `mas yr^-1` | **`mas/yr`**（保持现状，简洁；ApJS 也接受） | 当前已较一致。如果改为 `mas\,yr$^{-1}$`，需全文同步（包括所有表头）；建议**不动**。 |
| A-9 | "reduction" 含义 | `reduction`（指数据归算流程） / `re-reduction` / `re-reduce` | 区分：**`reduction`** = 当年的原始归算；**`re-reduction`** = 后期重新归算 | 当前一致，无需大改。 |
| A-10 | 历元名称 | `epoch J2000.0` / `J2000.0` / `J2000` | 第一次出现写 **`epoch J2000.0`**，后文一律 `J2000.0`；表格中可写 `J2000` | 当前混用，需检查 line 234、237 等位置统一。 |
| A-11 | "scatter" 类 | `scatter` / `dispersion` / `random component` / `stochastic error component` / `random scatter` / `within-file scatter` | 顶层用 **`scatter`**；统计量层面用 **`dispersion`**（如 MAD 描述）；机理层面用 **`random component`** | 当前 4.1 节用 `dispersion`、5.2 节用 `scatter` / `random scatter`、Conclusion 用 `stochastic error component`——需统一。建议 Conclusion 改为 `random component of the residuals`。 |
| A-12 | "data file / observation file / file" | `observation file` / `file` | 第一次出现写 **`observation file`**，之后用 **`file`** | 当前已基本一致。 |
| A-13 | "ephemeris" | `JPL Horizons DE441 planetary ephemeris` / `the ephemeris` / `dynamical reference` | 第一次写全名，后文一律 **`the DE441 ephemeris`** 或 **`the ephemeris`** | 当前 5.2 节使用一致。 |
| A-14 | Galilean satellites 命名 | `Galilean satellites (J1--J4)` / `Jovian satellites` | **`Galilean satellites`** 用于 5.2 节验证样本；**`Jovian, Saturnian, ...`** 用于 Introduction Para 3。两者不冲突，但需确认 5.2 节始终用 Galilean。 |
| A-15 | "image / frame / plate" | `Triton CCD frames` / `the same images` / `historical natural-satellite plates` | CCD 数据用 **`CCD frames`** 或 **`frames`**；老照相底片用 **`plates`**。5.1 节内部 `frames`/`images` 混用，需统一为 **`frames`**（Triton 是 CCD 数据，非照相底片）。 |
| A-16 | "DR3-based / Gaia-based" 复合 | `Gaia DR3-based debiasing model` / `Gaia-based re-reductions` / `Gaia DR2-based reduction`（隐含） | 统一带连字符 **`Gaia DR3–based`**（正式排版用 en-dash）或 **`Gaia DR3-based`**（朴素连字符）。**全文统一用朴素连字符 `Gaia DR3-based`**。 |
| A-17 | "Cross-matching" | 已基本一致使用 `cross-matching` | 保持 **带连字符** | OK |
| A-18 | "the use of … catalogs" / "the choice of catalog" | abstract 用 `use of different reference star catalogs`，body 用 `use of different reference catalogs` 等 | 统一为 **`use of different reference star catalogs`**（首次完整），后文 `reference catalog(s)` | — |

---

## B. 标题与摘要的"自我冲突"

| # | 位置 | 当前文本 | 问题 | 建议 |
|---|---|---|---|---|
| B-1 | Title (line 23) | `Correction of Star Catalog Positional and Proper Motion Systematic Errors for Natural Satellite Astrometry` | （1）"Errors" 与正文 A-3 的 "biases" 自相矛盾。（2）"Positional" 与正文 A-7 的 "position" 不一致。（3）"Proper Motion" 作定语未连字符，与 A-6 不一致。（4）"Natural Satellite" 作定语未连字符，与 A-5 不一致。 | `Correction of Star Catalog Position and Proper-Motion Systematic Biases for Natural-Satellite Astrometry` |
| B-2 | Abstract 开句 (line 61) | 单句 73 词，包含 4 个分句 | 句子过长，违反 ApJS 简洁原则；且与 Introduction 第一句的语义重复 | 拆为两句：第一句陈述"轨道确定依赖一致的天体测量观测合并"，第二句陈述"不同星表带来空间相关的系统偏差"。 |
| B-3 | Abstract (line 61) | `derive position and proper motion corrections for 17 star catalogs commonly used in natural satellite astrometry` | "natural satellite astrometry" 应连字符；"proper motion corrections" 应连字符 | `... for 17 star catalogs commonly used in natural-satellite astrometry` 并 `proper-motion corrections` |
| B-4 | Abstract (line 61) | `older photographic catalogs show position offsets exceeding 100~mas` | 与 Section 4.1 实际数值（AGK1 MAD ≈ 785 mas，median ≈ 383 mas）不匹配；且 Section 4.1 改后用 "tens to hundreds of mas, and reaching nearly 0.5 arcsecond"——abstract 数字与正文应同步 | 改为 `older photographic catalogs show position offsets reaching the hundred-mas to arcsecond level` |
| B-5 | Abstract (line 61) | `helps improve the astrometric positioning accuracy of natural satellites, thereby enhancing the precision of orbit determination and dynamical studies for natural satellite systems` | （1）`astrometric positioning accuracy` 在正文中无对应说法（正文用 `astrometric accuracy of natural satellite observations`）。（2）`for natural satellite systems` 与前句 `of natural satellites` 重复。 | `improves the astrometric accuracy of natural-satellite observations and thereby supports more precise orbit determination and dynamical studies` |

---

## C. Introduction（Section 1）行文节奏

整体结构 OK，但 **Para 4 与 Para 5 篇幅严重失衡**：Para 4 长达 8 句的密集文献回顾，Para 5 只有 4 句轻描淡写，到 Para 6 又突然进入"In this work"——节奏跳跃。

| # | 位置 | 问题 | 建议 |
|---|---|---|---|
| C-1 | Para 4 末 (line 75) | 现新加的 `As the raw observational data are in many cases no longer available for re-reduction, applying catalog corrections to the existing reduced positions is the only viable means of recovering their astrometric accuracy.` 这句出现在 Para 4 末尾，逻辑上是"为什么要做这个工作"，更适合放在 Para 5 或 Para 6 开头 | 把这句**整段移至 Para 5 末**（紧接 `is still lacking.` 之后），作为 Para 5 与 Para 6 的过渡。 |
| C-2 | Para 5 (line 77) | 全段过短，且与 Para 4 衔接生硬：Para 4 刚说"有了 Eggl(2020) 但不够用"，Para 5 又用 `In the context of natural satellites, similar approaches have only recently begun to be explored` 开头，"only recently begun" 这种口语化短语在 ApJS 中不太合适 | 改为：`Comparable efforts in natural-satellite astrometry remain limited.` 直接陈述事实。 |
| C-3 | Para 4 (line 75) | `\citet{Tholen2013b} further showed that the lack of proper motion information in 2MASS can generate regional signatures in high-precision astrometry, motivating the proper-motion-corrected debiasing scheme developed by \citet{Farnocchia2015}` | 单句过长（38 词），且 "regional signatures" 抽象 | 拆为两句：`\citet{Tholen2013b} found that the absence of proper motions in 2MASS produces regional position offsets in high-precision astrometry. This motivated the proper-motion-corrected scheme of \citet{Farnocchia2015}, which uses PPMXL as the reference catalog \citep{Roeser2010}.` |
| C-4 | Para 6 (line 79) | `we adopt Gaia DR3 as the common reference frame and derive systematic position and proper-motion corrections for 17 star catalogs identified as the most comprehensively used reference catalogs in historical natural-satellite astrometry, based on a systematic survey of the NSDC archive` | 单句 41 词，从句嵌套深；ApJS 偏好短句 | 拆为两句：`We adopt Gaia DR3 as the common reference frame and derive position and proper-motion corrections for 17 historical star catalogs. These 17 catalogs are identified, based on a systematic survey of the NSDC archive, as the most prevalent reference catalogs in historical natural-satellite astrometry.` |

---

## D. Section 2 局部一致性补充

前序 alter2_section2 已处理多数问题，此处仅补充全局一致性视角下的几条：

| # | 位置 | 当前文本 | 建议 | 理由 |
|---|---|---|---|---|
| D-1 | 2.2 Para 1 (line 93) | `including older releases that were prevalent before high-precision space-based astrometry became available` | "high-precision space-based astrometry" 是抽象表述，ApJS 偏好直接点名 | `including older releases that predate the Hipparcos and Gaia missions` |
| D-2 | 2.2 Para 1 (line 93) | `This is particularly true for older satellite reductions based on Guide Star Catalog releases \citep{Lasker1999,Morrison2001GSC12}.` | 引出"Guide Star Catalog"作为单点举例，与下一段"Early photographic catalogs, such as USNO-A2.0 and GSC~1.2..." 重复 | 删除此句；GSC 在下一段已被提及。 |
| D-3 | Table 1 表头 (line 102) | `Number of Stars` `Reference Frame` `Proper Motion` `Coverage` `CDS ID` | 与正文用语一致性 OK，无需改。但 `Proper Motion` 作列名若改全文连字符规范，列名保留无连字符更标准（因为是名词列名） | 保留。 |

---

## E. Section 3 一致性补充（在 alter2_section3 基础上）

| # | 位置 | 当前文本 | 建议 | 理由 |
|---|---|---|---|---|
| E-1 | 3.1 (line 130) | `The overall procedure consists of five main steps:` 然后用 (1)–(5) 分开行 | 保留分行结构；但每条尾部分号 `;` 在第 (4) 之后改为句号、第 (5) 句末用句号即可——目前 (1)(2)(3) 都用分号、(4) 用分号、(5) 用句号，已正确。但 (3) 中 `target catalog` 是首次出现，需要在该处用一句话定义：在 3.2 节（即第 (1) 步对应的 subsection）的开头可加一句 `Hereafter we use "target catalog" to refer to any of the 17 catalogs to be debiased, and "reference catalog" to refer to Gaia DR3.` | 显式建立术语对应。 |
| E-2 | 3.2 标题 (line 141) | `Frame and Epoch Propagation` | "frame" 不能 "propagate"。alter2_section3 已建议改为 `Frame Transformation and Epoch Propagation` | 沿用前述建议，正式改名。 |
| E-3 | 3.2 (line 145) | `For catalogs already in the ICRS, positions are propagated to epoch J2000.0 when proper motion information is available. For catalogs lacking proper motions, Gaia positions are propagated to the catalog epoch, and the comparison is performed at that epoch.` | 这两句承接被注释掉的旧句，逻辑上不完整：读者会问"那做完比较后呢？" | 在第二句后补一句：`The resulting tile-level differences are then referred to J2000.0 using the Gaia proper motions, as detailed in Section~\ref{subsec:correction_application}.` 与 3.4 的描述呼应。 |
| E-4 | 3.4 (line 173–177) | 公式 (1) 中 `\alpha_{\rm catalog}` `\mu_{\alpha,{\rm catalog}}` `\mu_{\delta,{\rm catalog}}` | 下标 `catalog` 太长，公式不美观；ApJS 标准是 2–3 字母下标 | 全文统一改为 `\alpha_{\rm cat}` `\mu_{\alpha,{\rm cat}}`（注意 alter2_section3 此前曾建议 cat→catalog 但未最终确认；这里反向回到 cat 简洁形式）。**或者**保留 `catalog` 但全文同步——选其一并贯穿到 line 180 的 `t_{\rm catalog}`。 |
| E-5 | 3.4 (line 180) | `For catalogs without proper motion information, only position differences are used. In this case, Gaia source positions are propagated to the catalog epoch $t_{\rm catalog}$, and the differences $\Delta\alpha(t_{\rm catalog})$ and $\Delta\delta(t_{\rm catalog})$ are computed at that epoch.` | `Gaia source positions` 中 `source` 多余 | `Gaia positions are propagated to the catalog epoch $t_{\rm cat}$` |
| E-6 | 3.5 (line 191) | `Each tile is associated with a set of parameters, including the HEALPix index` | 既然在 A-1 中保留 `HEALPix index` 作为字段名，此处 OK；但 `set of parameters` 含义抽象 | `Each tile is associated with the four correction parameters $\Delta\alpha_{\rm J2000}$, $\Delta\delta_{\rm J2000}$, $\Delta\mu_\alpha$, $\Delta\mu_\delta$, indexed by its HEALPix pixel number.` |
| E-7 | 3.5 (line 195–199) | 公式中 `$\Delta \alpha(t) = \Delta \alpha_{{\rm J2000}} + \Delta \mu_{\alpha}\,\Delta t$` 双花括号 `{{\rm J2000}}` | 单花括号即可：`{\rm J2000}` | 全文（含 Table 3 表头）所有 `{{\rm J2000}}` 改为 `{\rm J2000}`，纯排版优化。 |

---

## F. Section 4 一致性补充

| # | 位置 | 当前文本 | 建议 | 理由 |
|---|---|---|---|---|
| F-1 | 4.1 Para 1 (line 208) | `... reaching nearly 0.5 arcsecond in the most extreme cases (e.g., AGK1)` | AGK1 的 MAD = 785.1 mas ≈ 0.79 arcsec，median 382.8 mas ≈ 0.38 arcsec。`0.5 arcsecond` 没有对应数据 | 改为 `reaching the arcsecond level in the most extreme cases (e.g., AGK1)`，与 abstract 的 B-4 同步。 |
| F-2 | 4.1 Para 1 (line 208) | `... show significantly larger offsets and broader sky-to-sky scatter` | "sky-to-sky scatter" 仅此一处出现，与 A-11 不统一；4.2 节用 "spatial organization"、5.2 节用 "within-file scatter" | 改为 `larger offsets and broader spatial dispersion across the sky`。 |
| F-3 | 4.1 Para 2 (line 237–238) | `Its median corrections at J2000.0 are $68.0$~mas in $\Delta\alpha_{\rm J2000}$ and $151.9$~mas in $\Delta\delta_{\rm J2000}$, with MAD values of $104.2$~mas and $121.5$~mas, respectively.` | "in $\Delta\alpha_{\rm J2000}$" 的介词 "in" 用法不自然 | `The median corrections at J2000.0 are $\Delta\alpha_{\rm J2000} = 68.0$~mas and $\Delta\delta_{\rm J2000} = 151.9$~mas, with MAD values of 104.2 and 121.5~mas, respectively.` |
| F-4 | 4.1 Para 2 (line 240) | `display asymmetric behavior between RA and Dec` | "RA and Dec" 缩写在文中首次出现，未与 $\alpha,\delta$ 统一 | 改为 `display asymmetric behavior between $\alpha$ and $\delta$`，与公式中符号一致。**或**在 Section 3.4 公式 (1) 后注明 RA/Dec 与 $\alpha$/$\delta$ 等价（推荐前者，避免增加术语）。 |
| F-5 | 4.2 (line 246) | `As shown in Figure~\ref{fig:bias_usno_a2_2x2}, the USNO-A2.0 corrections display large-scale gradients together with localized discontinuities.` | "localized discontinuities" 与 4.3 节的 "block-like or discontinuous structures" 是同一物，但措辞不同 | 改为 `large-scale gradients together with block-like discontinuities`。让 4.2 与 4.3 用同一术语。 |
| F-6 | 4.3 节标题 (line 260) | `Origin of the Bias Patterns` | alter2_todo_list 中"4.3 改名字"——确实"Origin"过于宏大，本节只是"成因解释" | 改为 `Interpretation of the Spatial Patterns`（与 4.2 标题 `Spatial Structure of the Systematic Biases` 配对）。 |
| F-7 | 4.3 (line 263) | `block-like or discontinuous structures associated with independent plate-based reductions` | "plate-based reductions" 与 4.4 / 5.1 中 "plate re-reduction" / "image reductions" 不一致 | 保留此处 `plate-based reductions`（指历史照相底片归算），与 5.1 节的 `re-reduction` 区分。但建议加一个清晰的定语：`independent plate-by-plate reductions`，避免与"基于底片的"产生歧义。 |
| F-8 | 4.3 (line 281) | `These results show that both the amplitude and morphology of the correction fields are controlled by the intrinsic properties of the source catalogs.` | `source catalogs` 此处指"被改正的星表"，与 A-2 全局术语 `target catalog` 冲突 | 改为 `... by the intrinsic properties of the target catalogs`。 |
| F-9 | 4.4 (line 287) | `The interpolation uses the $k=8$ nearest neighboring tiles as support points` | $k=8$ 此前未在任何地方解释为何选 8 | 简单加一句：`(empirically chosen to balance smoothness and locality)`，或干脆去掉具体数字改为 `the nearest neighboring tiles`，与前序 alter2_section4 一致。**推荐去掉 $k=8$**，因为方法节并未论证此参数。 |

---

## G. Section 5 一致性补充

| # | 位置 | 当前文本 | 建议 | 理由 |
|---|---|---|---|---|
| G-1 | 5.1 (line 309) | `The earlier reduction, based on the UCAC2 catalog, yielded 943 positions \citep{Qiao2007}, whereas a later re-reduction of the same images using Gaia DR2 as the reference catalog produced 1007 positions, including 941 updated measurements \citep{Yan2020}.` | (1) `the UCAC2 catalog` 啰嗦——前文"UCAC2"已是星表名。(2) `same images` 与上一句 `Triton CCD frames` 用词不一（A-15）。(3) `produced 1007 positions, including 941 updated measurements` 含义不清——读者会问 1007 与 941 的关系。 | `The earlier reduction, based on UCAC2, yielded 943 positions \citep{Qiao2007}, while the later re-reduction of the same frames using Gaia DR2 produced 1007 positions \citep{Yan2020}.` 删除"including 941 updated measurements"——本来就要做"严格历元配对"，中间数字不必出现。 |
| G-2 | 5.1 (line 311–315) | `The positional offset $\Delta$ is defined as` + 公式 + `where $\Delta\alpha = (\alpha_{\rm UCAC2}-\alpha_{\rm Gaia\,DR2})\cos\delta$ and $\Delta\delta = \delta_{\rm UCAC2}-\delta_{\rm Gaia\,DR2}$ are the positional differences between the UCAC2-based reduction and the Gaia~DR2 re-reduction.` | (1) `positional offset` / `positional differences` 与全文 `position offset` / `position difference` 不一致（A-7）。(2) 公式 $\delta$ 未指明 reference（应为 Gaia DR2 的 $\delta$）。 | 全文 `positional` → `position`；公式注释加 `where $\delta = \delta_{\rm Gaia\,DR2}$.` |
| G-3 | 5.1 (line 317) | `Relative to the Gaia DR2 re-reduction, the UCAC2-based reduction has a mean positional offset of 86.2~mas and a median of 82.5~mas. After application of the Gaia DR3-based debiasing model, the mean and median offsets decrease to 76.2~mas and 67.7~mas, respectively. This corresponds to an 11.6\% reduction in the mean offset, with 78.0\% of the common positions showing smaller $\Delta$ values after correction. The remaining difference should not be interpreted solely as uncorrected catalog bias, because the two reductions also differ in centroiding and reduction procedures \citep{Yan2020}.` | (1) 句长不一：前两句短、第三句中、第四句长。节奏跳。(2) `should not be interpreted solely as ...` 防御性语气过重，且与 alter2_section5 中"R1+R2"重写思路冲突——alter2_section5 已计划把这段重写并删除该末句 | 按 alter2_section5 R1/R2 改写后此段消除，但若暂未改写，可做最小改动：把末句删掉，改为简短脚注式说明。 |
| G-4 | 5.1 (line 327) | `Although the debiasing model is constructed using Gaia DR3 whereas the benchmark reduction uses Gaia DR2 as the reference catalog, both Gaia releases share a consistent ICRS realization, and the DR3--DR2 differences are negligible compared with the original UCAC2 systematic offsets. The reduction in positional offset relative to this benchmark therefore provides a conservative validation of the correction model.` | (1) 单句 36 词。(2) `correction model` 与 `debiasing model` 混用（A-4）。(3) `conservative validation` 是英文中较僵的搭配，ApJS 多用 `provides a conservative test of` 或 `supports`。 | 拆两句：`The debiasing model is built from Gaia DR3, whereas the benchmark reduction uses Gaia DR2 as the reference catalog. Since both releases share a consistent ICRS realization and their differences are far smaller than UCAC2 systematics, the reduction in position offset constitutes a conservative test of the debiasing model.` |
| G-5 | 5.2 (line 333) | `The validation sample consists of 11\,731 absolute astrometric observations of the Galilean satellites (J1--J4) from the LTE/NSDC archive` | (1) `LTE/NSDC` 写法与 Introduction Para 2 中 `Natural Satellites Data Center (NSDC), maintained by the Laboratoire Temps Espace (LTE)` 不齐。(2) `the Galilean satellites (J1--J4)` 中 `J1--J4` 编号风格突兀 | `The validation sample consists of 11\,731 absolute astrometric observations of the four Galilean satellites from the NSDC archive`。J1–J4 编号删除（学术习惯里直接说"四颗伽利略卫星"足够清楚）。 |
| G-6 | 5.2 (line 343) | 完整段："The typical single-observation residual ... within-file standard deviations $\sigma_\alpha$ and $\sigma_\delta$ as diagnostics of random scatter." | 这一段是全文最长、最绕的之一。逻辑：观测噪声大 → 文件平均压噪声 → 用文件均值看系统偏差。但写法过于冗长 | 拆为三句： `Typical single-observation residuals are 100--200~mas, while median catalog corrections are 10--30~mas. At the individual-observation level the correction signal is therefore dominated by random measurement noise. We instead adopt file-level mean residuals $\overline{\Delta\alpha}$ and $\overline{\Delta\delta}$ as diagnostics of systematic offsets, and within-file standard deviations $\sigma_\alpha$ and $\sigma_\delta$ as diagnostics of random scatter; averaging over the $N$ observations of a file suppresses the random component by $1/\sqrt{N}$.` |
| G-7 | 5.2 Table 4 列名 (line 351–355) | `$\overline{\Delta\alpha}_{\rm before}$` `$\overline{\Delta\alpha}_{\rm after}$` ... | "before/after" 下标在 ApJS 表头中较少见；可保留，但至少所有下标方向一致。当前一致 | 不必改。 |
| G-8 | 5.2 (line 388–390) | `Files reduced with catalogs carrying large known biases show substantial positive improvements: AGK3/jg0032 ($+101$~mas), UCAC2/jg0043 ($+24$~mas), Gaia~DR1/jg0059 ($+20$~mas), and Tycho-2/jg0023 ($+21$~mas).` | 与 5.2 第一段所列 `8 reference catalogs` / `21 groups` 数字呼应清晰，但举例中 `AGK3/jg0032` 这类斜杠写法和表中 `jg0032 & AGK3` 的对应顺序相反 | 统一为 `jg0032/AGK3 ($+101$~mas)`，与表的"file 列在前、catalog 列在后"对应。 |
| G-9 | 5.2 (line 392) | `The two Gaia~DR2 files show near-zero change, consistent with the negligible correction amplitude for that catalog.` | "near-zero change" 偏口语 | `The two Gaia~DR2 files show no significant change, as expected for a catalog whose corrections are negligible.` |
| G-10 | 5.2 末段 (line 408–410) | `The systematic offsets are reduced for the majority of catalogs while the random scatter remains unchanged. This confirms that the debiasing correction acts on catalog-dependent systematic biases without altering the stochastic error structure of the observations. Together with the plate re-reduction test, the ephemeris comparison supports the effectiveness of the Gaia~DR3-based correction model.` | `correction model` 与 A-4 不一致；`stochastic error structure` 与全文 `random scatter` / `random component` 不一致（A-11） | 改：`This confirms that the debiasing acts on catalog-dependent systematic biases without altering the random component of the residuals. Combined with the plate re-reduction test, the ephemeris comparison validates the Gaia DR3-based debiasing model.` |

---

## H. Section 6 (Conclusions) 全段重审

Conclusion 是全文一致性检查的"试金石"——任何上文统一过的术语，在 Conclusion 中都不能再变。

| # | 位置 | 当前文本 | 建议 | 理由 |
|---|---|---|---|---|
| H-1 | line 414 | `we derive systematic position and proper motion corrections for 17 historical star catalogs` | `proper motion corrections` 应连字符（A-6） | `proper-motion corrections` |
| H-2 | line 414 | `A unified catalog debiasing framework is developed based on HEALPix sky partitioning combined with RBF interpolation` | `catalog debiasing framework` 与 `correction framework` (A-4) 混用 | 改为 `correction framework`（与 abstract 一致）；或全文统一为 `debiasing framework`，**择一贯穿**。建议 abstract、Introduction、Conclusion 都用 `correction framework` 指代整个产物体系，`debiasing model` 指代方法本体。 |
| H-3 | line 414 | `enabling the construction of continuous all-sky correction fields while suppressing artificial discontinuities introduced by discrete tiling` | "discrete tiling" 与全文 "tile-based estimates" 不一致（A-1） | `... discontinuities introduced by tile-based estimation` |
| H-4 | line 414 | `The resulting model preserves the intrinsic large-scale structure of catalog systematics while removing non-physical small-scale variations.` | `non-physical` 措辞强；其实是"采样噪声"，本质不一定 non-physical | `... while suppressing small-scale sampling noise.` 与 4.4 节末段同 |
| H-5 | line 416 | `The plate re-reduction test shows that the debiased data exhibit reduced systematic residuals while maintaining the original dispersion of the observations.` | `dispersion of the observations` 与 5.2 节 `within-file scatter` / `random scatter` 不一（A-11） | `... while preserving the random scatter of the observations.` |
| H-6 | line 416 | `The ephemeris comparison test confirms that the file-level systematic offsets are reduced for the majority of catalogs without altering the within-file scatter.` | OK，与 5.2 节末一致 | 保留。 |
| H-7 | line 416 | `Both tests demonstrate that the proposed approach effectively mitigates catalog-dependent systematic offsets without degrading the stochastic error component, leading to improved consistency in orbit determination solutions \citep{Desmars2013}.` | (1) `stochastic error component` 与 H-5 改为 `random scatter` 后又跳回，需统一。(2) `Desmars2013` 引用此处突兀——H 节是结论，按 ApJS 习惯不引新文献 | (1) 改为 `random component`。(2) 删 `\citep{Desmars2013}`（该文献 Introduction Para 1 已引）。 |
| H-8 | line 416 | `The improvement is particularly relevant for historical observations that cannot be directly reduced in the Gaia reference frame.` | `directly reduced` 与全文 `re-reduce` / `reprocess` 不一 | `The improvement is particularly relevant for historical observations that cannot be re-reduced in the Gaia reference frame.` |

---

## I. 跨节重复内容审查

下表列出了内容上**已重复出现**的位置，作为后续修改时的检查清单。重复一旦出现，要么删一处、要么相互引用。

| # | 重复内容 | 出现位置 | 建议处理 |
|---|---|---|---|
| I-1 | "17 个星表，覆盖天然卫星历史观测" | abstract / Intro Para 6 / Section 2.2 末段 / Conclusion | 三处都需要这句话，但措辞要尽量接近：`17 star catalogs commonly used in historical natural-satellite astrometry`。abstract 与 Conclusion 用同一短语，Intro Para 6 是承上启下加一段说明（已改）。 |
| I-2 | "Gaia DR3 比 DR2 更精确" | Intro / Section 2.1 / 5.1 | Intro 中只点一笔即可；Section 2.1 是详细论述；5.1 是验证语境（与 DR2 benchmark 对比）。**Intro 里的相关句**（line 75, "More recently, \citet{Eggl2020} ... Gaia DR2 reference frame"）与 Section 2.1 不直接重复，OK。 |
| I-3 | $D_{\rm disc}$ 定义 | 4.3 (line 266–269) / 4.4 (line 289 引用) | 已经改为"4.4 引用 4.3 的定义"，OK。**Conclusion 里 alter2_section5 中 C-1 已删除该重复**，确认已清理。 |
| I-4 | "改正参数四元组 $(\Delta\alpha, \Delta\delta, \Delta\mu_\alpha, \Delta\mu_\delta)$" | 3.4 公式 (2) / 3.5 文字 / Table 3 表头 / Section 7 文字 | 3.4 公式中给出后，3.5 用文字复述一次（OK）；Table 3 表头与公式一致；Section 7 再说一次（OK，因为是 data release 节）。**全部用同一符号顺序**：$\Delta\alpha_{\rm J2000}, \Delta\delta_{\rm J2000}, \Delta\mu_\alpha, \Delta\mu_\delta$。当前已一致。 |
| I-5 | NSDC 全称展开 | Intro Para 2 (line 71)：`Natural Satellites Data Center (NSDC), maintained by the Laboratoire Temps Espace (LTE) at Paris Observatory` / 致谢 (line 431)：`Natural Satellites Data Center (NSDC), maintained by the Laboratoire Temps Espace (LTE)` | 致谢里已经简化了一次（去掉"at Paris Observatory"），**保持现状即可**。 |
| I-6 | "本文方法与 Eggl(2020) 相似但适配天然卫星" | Intro Para 4 末 / Intro Para 6 / Section 2.2 第一段（已删）/ 4.4 节 | 4.4 节用 `we adopt a similar strategy to that of \citet{Eggl2020}` 是方法层面，OK。Intro Para 4 与 Para 6 都提到 Eggl(2020)——Para 4 是文献综述，Para 6 是工作定位，**两处侧重不同，可保留**。 |

---

## J. 标点、连字符、小细节

| # | 类别 | 当前问题 | 建议规则 |
|---|---|---|---|
| J-1 | 复合形容词连字符 | `space-based`、`Gaia-based`、`tile-based`、`file-level` 已规范；但 `Gaia DR3 based` / `Gaia DR3-based` 混用 | 含数字版本号的复合修饰统一为 `Gaia DR3-based`、`Gaia DR2-based`、`UCAC2-based` |
| J-2 | en-dash vs hyphen | "1962--2019"、"DR3--DR2 differences"、"observation-minus-ephemeris" | `1962--2019`、`DR3--DR2` 用 `--`（en-dash）；`observation-minus-ephemeris` 用 `-`（hyphen）。当前正确。 |
| J-3 | 省略号/逗号 | 公式 (1) `\Delta\delta = \delta_{\rm catalog}-\delta_{\rm Gaia},\\` 用 `\\` 换行后接 `\Delta \mu_\alpha = ...`，逗号换行处理 | 当前 OK，无需改 |
| J-4 | 引用前空格 | `historical catalogs\citep{Vasiliev2019}` (line 280)、`scan direction\citep{Zacharias2017UCAC5}` (line 272)、`reductions\citep{Platais1998,Eichhorn1974}` (line 263) | 缺空格。LaTeX 排版习惯：`historical catalogs \citep{Vasiliev2019}`。**全文检索 `\citep` 与前一字符之间是否有空格**，不一致需补齐。 |
| J-5 | `~` 与空格 | `100~mas` `1''` 等使用 `~` 防换行已正确 | 保留 |
| J-6 | 双花括号 | line 234, 237, 191 `\Delta\alpha_{{\rm J2000}}` 多余的 `{}` | 简化为 `\Delta\alpha_{\rm J2000}`（与 E-7 同） |
| J-7 | $1''$ vs $1\arcsec$ | 全文用 $''$，OK | 保留 |
| J-8 | "Section~\ref{...}" 与 "Section X" | 全文用 `Section~\ref{...}` 一致 | OK |
| J-9 | 表格 number formatting | Table 2 中正负数 `+84.45` `-254.16` 含显式 `+` | 保留显式正号（5.2 节本就强调方向性） |

---

## K. 段落长度与节奏统计（参考）

简单数了一下当前每段词数（括号内为 sentence count），帮助判断哪里"突然变长/变短"：

| Section / Para | Words | Sentences | 节奏判断 |
|---|---|---|---|
| Abstract | 173 | 5 | 第一句 73 词偏长（B-2） |
| Intro Para 1 | 88 | 4 | OK |
| Intro Para 2 | 87 | 3 | OK |
| Intro Para 3 | 95 | 3 | OK |
| Intro Para 4 | 196 | 6 | **偏长**，C-3 已建议拆分 |
| Intro Para 5 | 79 | 3 | **偏短**（与 Para 4 反差太大） |
| Intro Para 6 | 110 | 3 | OK，但单句过长（C-4） |
| Section 2.1 Para 1 | 90 | 2 | 第二句长 |
| Section 2.1 Para 2 | 75 | 2 | OK |
| Section 2.1 Para 3 | 60 | 2 | OK |
| Section 2.2 Para 1 | 47 | 2 | 偏短 |
| Section 2.2 Para 2 | 50 | 1 | **单句段，过短** |
| Section 2.2 Para 3 | 134 | 4 | OK |
| Section 4.1 Para 1 | 86 | 2 | OK |
| Section 4.1 Para 2 | 60 | 2 | OK |
| Section 4.1 Para 3 | 73 | 3 | OK |
| Section 5.2 长段（line 343） | 99 | 4 | 单句最长 30 词，G-6 已建议拆 |
| Conclusion Para 1 | 70 | 2 | OK |
| Conclusion Para 2 | 90 | 4 | OK |

**主要节奏问题**：(1) Intro Para 4 与 Para 5 长度悬殊；(2) Section 2.2 Para 2 是孤句段；(3) Abstract 首句过长。

---

## L. 修改优先级建议

按"改动效益 / 修改风险"排序，建议这样推进：

**第一优先（必做，影响审稿印象）**
1. A-3 / B-1：标题改为 `Position and Proper-Motion Systematic Biases`（彻底解决 error vs bias 矛盾）
2. A-5 / A-6 / B-3：abstract 与全文 `natural-satellite`、`proper-motion` 连字符统一
3. A-7 / G-2：5.1 节 `positional` → `position`
4. A-1 / F-8：`HEALPix pixels` (line 269)、`source catalogs` (line 281) 改齐
5. F-1 / B-4：`0.5 arcsecond` → `arcsecond level`，abstract 同步
6. E-2：3.2 节标题改为 `Frame Transformation and Epoch Propagation`

**第二优先（提升流畅度）**
7. C-1 / C-2：Intro Para 4–5 节奏调整（移句、缩短"only recently begun"）
8. C-3 / C-4 / G-6：拆分超长句
9. F-6：4.3 节标题改名
10. H-1 / H-7 / H-8：Conclusion 三处术语统一

**第三优先（细节抛光，可批量处理）**
11. J-4：`\citep` 前补空格（全文检索）
12. J-6 / E-7：`{{\rm J2000}}` → `{\rm J2000}`（全文检索替换）
13. A-4 全局：`correction model` 与 `debiasing model` 角色划分
14. E-4：公式下标 `catalog` 与 `cat` 二选一

**第四优先（结构性，按需）**
15. D-2：Section 2.2 Para 1 删除 GSC 单点举例
16. F-5：4.2 节 `localized discontinuities` → `block-like discontinuities`
17. H-2：abstract / Conclusion 用 `correction framework`，方法层面用 `debiasing model`

---

## M. 一致性自检清单（修改完成后跑一遍）

完成上述修改后，建议用以下关键词在全文检索一遍，检查残留：

```
□ "natural satellite "       （应不再出现作定语）
□ "proper motion "           （后跟名词时应被 proper-motion 替换）
□ "positional"               （应只出现在 Intro Para 1 一处）
□ "pixel"                    （应只在 HEALPix index 字段名上下文出现）
□ "source catalog"           （应不存在）
□ "sky region"               （应不存在）
□ "systematic error"         （应不存在；除非引用 Gaia DR2 时无可避免）
□ "correction model"         （应统一为 debiasing model 或 correction framework）
□ "Gaia based" / "DR3 based" （应均带连字符）
□ "{{\rm "                   （双花括号应不存在）
□ "0.5 arcsecond"            （应已改为 arcsecond level）
```

---

*生成日期：2026-05-18*
*这份文档不直接改动 paper_en.tex；待你逐项审阅后，再分批授权修改。*
