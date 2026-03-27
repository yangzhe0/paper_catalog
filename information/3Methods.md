\section{修正方法（Correction Methodology）}

\subsection{方法总体框架}

整体方法包括五个步骤：将所有星表统一至共同的参考系与比较历元基准，采用 HEALPix 对全天进行空间划分，在各天区内对目标星表与 Gaia DR3 进行交叉匹配，估计局部位置与自行系统偏差，（5）构建修正模型并生成可用于观测修正的数据表。

该方法以待修正星表与 Gaia DR3 为输入，输出为基于 HEALPix 网格的修正参数，包括位置偏差 $(\Delta \alpha_{2000}, \Delta \delta_{2000})$ 及自行偏差 $(\Delta \mu_{\alpha *}, \Delta \mu_{\delta})$，其中 $\alpha * \equiv \alpha \cos\delta$。

\subsection{历元统一与参考系转换}

为保证比较一致性，所有星表统一至相同参考系与比较历元基准。对于 ICRS 星表，若包含自行信息，则将其位置传播至 J2000.0；若不包含自行信息，则将 Gaia 位置传播至该星表观测历元，从而在共同历元下进行比较。对于非 ICRS 星表（如 FK4），先转换至 ICRS，并以其原始历元作为比较基准完成匹配。该处理确保所得差异主要反映星表本身的系统偏差。

Gaia DR3 的参考历元为 J2016.0，其位置基于发布的天体测量参数（位置、自行及视差）传播至所需比较历元；当径向速度可用时一并纳入，缺失时取 $v_r=0$。

\subsection{天区划分与交叉匹配}

在完成参考系与历元统一后，采用 HEALPix 对全天进行划分，取 $N_{\rm side}=64$，对应 $N_{\rm pix}=49{,}152$ 个等面积天区，每个天区面积约为 $0.839\ {\rm deg}^2$。

在各天区内进行交叉匹配。对于目标星表中的每一颗恒星，在其位置周围 1 角秒范围内检索 Gaia DR3 候选源，匹配规则如下：

1. 若仅存在一个候选源，则匹配成功；
2. 若存在多个候选源，仅当最近邻满足
\[
d_1 < 0.2\, d_2
\]
时判定为匹配成功，其中 $d_1$ 与 $d_2$ 分别为最近邻与次近邻角距离；
3. 若无候选源，则判定为匹配失败。

所有匹配均基于已统一至相同参考系与比较历元的坐标进行。

\subsection{偏差估计与修正模型}

对每一对成功匹配的恒星，定义其位置与自行差异为：

\[
\Delta \alpha_* = (\alpha_{\rm cat}-\alpha_{\rm Gaia})\cos\delta,\quad
\Delta \delta = \delta_{\rm cat}-\delta_{\rm Gaia},
\]
\[
\Delta \mu_{\alpha *} = \mu_{\alpha *,{\rm cat}}-\mu_{\alpha *,{\rm Gaia}},\quad
\Delta \mu_{\delta} = \mu_{\delta,{\rm cat}}-\mu_{\delta,{\rm Gaia}}。
\]

其中 $\alpha * = \alpha \cos\delta$，自行项 $\mu_{\alpha *}$ 采用相同约定；对不含自行的星表取 $\mu_{\rm cat}=0$。

在每个 HEALPix 天区内，采用中位数统计所有匹配恒星的差异，并统一换算至 J2000.0 历元，得到系统偏差参数：

\[
(\Delta \alpha_{2000}, \Delta \delta_{2000}, \Delta \mu_{\alpha *}, \Delta \mu_{\delta})。
\]

上述参数均表示为 J2000.0 历元下的系统偏差。除匹配筛选外，不再进行额外异常值剔除。

对任意历元 $t$，修正量由线性模型给出：

\[
\Delta \alpha_*(t) = \Delta \alpha_{2000} + \Delta \mu_{\alpha *}\,\Delta t,\quad
\Delta \delta(t) = \Delta \delta_{2000} + \Delta \mu_{\delta}\,\Delta t。
\]

\subsection{修正数据产品与应用}

修正结果以 HEALPix 网格形式存储。每个天区对应一组参数：HEALPix 索引、$\Delta \alpha_{2000}$、$\Delta \delta_{2000}$、$\Delta \mu_{\alpha *}$ 和 $\Delta \mu_{\delta}$。

在应用中，根据观测坐标确定其所属天区，读取对应参数，并代入时间模型计算 $\Delta \alpha_*(t)$ 与 $\Delta \delta(t)$，从而对观测位置进行修正，使其与 Gaia DR3 参考体系一致。