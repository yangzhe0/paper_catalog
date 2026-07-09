**Response to Reviewers**

We sincerely thank the reviewers for their insightful comments and constructive suggestions, which have helped us significantly improve the clarity and quality of our manuscript. We have revised the manuscript accordingly. Point-by-point responses are given below.

**Response to Reviewer #1**

**Comment ****0****: ***It is a concise paper on a specific subject.** **The authors of the article are masters of observation.** **They regularly provide the most accurate observations.** **The paper presents a new method that improves the accuracy** **of observations of Uranus's satellites under the influence** **of the planet's halo.*

**Response**** 0****: ***We sincerely appreciate your positive feedback on the paper’s focus, our observational work, and the proposed new method; your comment is highly motivating to our team.** *

**Comment 1: ***The authors use the term "Retinex algorithm". Please explain what "Retinex" is? Is it the name of the algorithm's author or a colleague?*

**Response 1: **We appreciate this suggestion. The term "Retinex" has been  defined in the revised manuscript (Lines 66–70). It is a computational model inspired by human visual perception, and the name is a portmanteau of "retina" and "cortex," originally introduced by Edwin H. Land (Land & McCann, 1971). It is not a person's name but a technical term for an image. enhancement theory.

**Comment 2: ***Why does a halo form around the planet? Is this halo caused by scattering in the telescope or by atmospheric scattering?*

**Response 2: **Thank you for raising this point. We have added a detailed explanation in Lines 49–50. The planetary halo is primarily formed by light scattering—both within the telescope's optical system (e.g., multiple reflections between lenses or at the CCD surface) and by atmospheric scattering.

**Comment 3:** *Why and how does the halo reduce observational accuracy? This should be explained in the Introduction.*

**Response 3: **We have clarified this mechanism in Lines 45–48. The halo reduces the signal-to-noise ratio (SNR) of nearby faint satellites and introduces biases in centroid determination due to the influence of the halo's grayscale values, thereby degrading both the detectability and astrometric accuracy of the satellites. In particular, when the halo is very bright as a background, it becomes extremely difficult to detect faint natural satellites within the halo.

**Comment 4: ***What is the criterion for evaluating observational accuracy? The authors use a comparison with ephemerides. Are the ephemerides considered absolutely accurate?*

**Response 4: **This is an important point. We have added a clarification in Lines 87–90. The root mean square (RMS) of O-C values reflects the internal consistency accuracy of the observational data, or in other words, the stability of locating the observed targets from the images. The mean value of O-C represents the systematic error of the observational data, which includes potential systematic errors in the observations themselves, systematic errors in the ephemeris used for comparison, and naturally, possible positional deviations in that reference ephemeris. Precisely because of the existence of such systematic errors, long-term and continuous observations of natural satellites are necessary to improve their orbital parameters. The RMS of O-C values for the positional data obtained by our current method demonstrates the accuracy of our data—and high-precision data can better support subsequent orbital improvements.

**Comment 5: ***In the Conclusions: Can the authors state precisely that the detection rate has been improved? If so, please explain "how".*

**Response 5: **We thank the reviewer for this suggestion. We have strengthened the Conclusions section (Lines 294–306) to explicitly state the improvement in the detection rate (i.e., the number of valid observations), directly linking it to the data volume increases reported in Table 4. We clarify that the enhanced detection, particularly for the faint satellite Miranda (U5), is a direct result of the BSSR-Gaussian method's ability to suppress the planetary halo and improve the SNR of the satellites, making them detectable in more individual frames.

**Response to Reviewer #2**

**Comment ****0****:** *Because of the vicinity of the planet, natural satellites are usually in the halo, making some satellites hardly detectable and degrading the astrometry. Here the authors propose a new method to remove and correct this effect : Bilateral filtered Single-scale Retinex by Gaussian filtering (BSSR-Gaussian). They apply the technique to CCD images of Uranus and five natural satellites. They compare to previous method and show their method is very efficient in both detecting natural satellites (in particular Miranda) and improving the astrometry.** **The paper is well written and detailed. Tables and Figures clearly demonstrate the efficiency of the method.** **I think the paper can be published in Icarus after minor corrections.*

**Response ****0****:**We deeply appreciate your positive evaluation of the paper's theme, our fieldwork efforts, and the newly proposed technique; your comment provides immense motivation for our research team.

**Comment 1:** *Introduction: "Some researchers have used coronographs [...]" is a bit vague. You should give some references.*

**Response 1:** We agree and have added relevant references (Bourget et al., 2004; Assafin et al., 2008) in Lines 50–51 of the revised manuscript.

**Comment 2: ***Figure 1. It may be good to present also a comparison with an image treated with the Method 1 (for figure 1 and figure 2) as later, you compare the residuals of the two methods.*

**Response 2:** We thank the reviewer for this suggestion. We have updated Figure 1 and Figure 2 to include the results from Method 1 (Median Filtering) for a direct visual comparison. The revised Figure 1 now includes three panels: (a) original image, (b) image processed by Method 1 (MF), and (c) image processed by Method 2 (BSSR-Gaussian). Similarly, Figure 2 now includes the corresponding three local regions.

**Comment 3: ***Table 3: Probably, for a better reading, you can add the name of the satellite on the satellite column (such as U1 Ariel, U2 Umbriel, etc).*

**Response 3: **We have revised Table 3 to include the full satellite names (e.g., U1 Ariel) in the satellite column for clarity.

**Comment 4: ***Section 4: Do you try to quantify if the better detection and/or better astrometry is linked to the proximity of the satellite to the planet or magnitude of the satellite? I mean, how do you improve the astrometry or the detection depending of the distance between satellite and the planet on the frame? My question is also related to the current limitation of your method. Why do you still have undetected satellite on the frames? Because of to close proximity with the planet? too faint objects? Can you discuss about this point?*

**Response 4: **We thank the reviewer for raising this important point. This method significantly enhances detection and positioning accuracy for natural satellites near major planets within their halos, as demonstrated by the case of U5. For satellites farther from the parent planet like U3 and U4, while they are also affected by halo effects, they generally remain undiminished or obscured by Uranus's body. The occasional data gaps observed in these targets primarily result from statistical processing limitations, though all such objects are reliably detected. As shown in Table 3, during Day14 data collection, U2 and U3 showed fewer measurements compared to U4 and U1. This discrepancy mainly stems from our data processing criteria: only observations with O-C values below 3σ were retained, while those exceeding 3σ were discarded. Consequently, some targets exhibited reduced measurement counts.

**Comment 5: ***The paragraph before (5) is not clear. You mention the standard deviations in RA and DEC now reflect the limitations of dynamical model. I do not fully agree. The standard deviations are mainly due to observational errors. At least I do not think the current orbital model is limited. This is more the observations used to fit the dynamical model that are not accurate and so produce error in ephemeris. The error of the ephemeris can be separated in two: (1) error in planet ephemeris (2) error in satellite ephemeris. The first one should be constant for the period (between 13-18 November 2020) and independent of the satellite. Here you don't have constant bias in your residual so your data do not highlight a problem in the Uranus ephemeris. The second one is satellite dependent. With your method, you act directly on the observation and reduce the O-C, which proves, in my opinion, that the standard deviations finally reflect the observation error and not the ephemeris error. So please, explain better what you mean.*

**Response 5:** We agree with the reviewer that our original phrasing was unclear and could be misinterpreted. We have thoroughly rewritten the paragraph in question to provide a more precise and correct interpretation. As explained earlier, the root mean square (RMS) of O-C values reflects the internal consistency accuracy of the observational data, the stability of locating the observed targets from the images. The mean value of O-C represents the systematic error of the observational data, which includes potential systematic errors in the observations themselves, systematic errors in the ephemeris used for comparison, and naturally, possible positional deviations in that reference ephemeris.

The revised text now states that the reduction in the residual scatter (standard deviation) is a direct result of suppressing observational errors like halo-induced noise. We then clarify that it is the remaining small, satellite-dependent biases in the mean (O-C) values (after random errors are suppressed) that might hint at other factors, such as subtle systematics or dynamical model limits.

Once again, we are grateful to both reviewers for their valuable time and comments, which have been instrumental in refining our paper.
