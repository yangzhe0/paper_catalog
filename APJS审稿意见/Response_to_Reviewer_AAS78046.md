**Response to Reviewer**

We sincerely thank the reviewer for the positive evaluation of our manuscript and for the constructive comments and corrections. We have revised the manuscript accordingly. All changes in the revised manuscript have been highlighted in bold, as requested by the editor. Point-by-point responses are given below.

**Comment 1:** *Since this work is based in part on data extracted from the Natural Satellite Data Base (NSDB), the bibliographic reference Arlot et al., A&A, 691, A295 (2024) and its citation must be added. It should also be noted that, in this text, the term "NSDB" (database) should be used rather than "NSDC," which refers to the Center (and thus encompasses the NSDB as well as other services).*

**Response 1:** We thank the reviewer for pointing this out. We have added the bibliographic reference to Arlot et al. (2024) to the reference list and cited it at the first mention of the Natural Satellite Database (NSDB) in the Introduction. We have also revised the terminology throughout the manuscript, replacing NSDC with NSDB where the database or archive is meant. These changes appear in the Introduction, the catalog-selection description, the validation-sample description, and the acknowledgments.

**Comment 2:** *You use the median absolute deviation (MAD) in your text (line 190) and in Table 2; it might be helpful to provide a definition of it somewhere (or to add a reference).*

**Response 2:** We agree with the reviewer. We have added an explicit definition of MAD in the note to Table 2. MAD is now defined as `median(|x_i - median(x)|)`.

**Comment 3:** *On figure 5 the caption of the ordinate axis is too small and must be more explicit than it is (explain CDF : P(Ddisc <= x).*

**Response 3:** We thank the reviewer for this suggestion. We have revised Figure 5 by increasing the axis-label and tick-label sizes. The ordinate label now explicitly reads `CDF: P(D_disc <= x)`. We have also revised the Figure 5 caption to define the CDF as the cumulative distribution function, `P(D_disc <= x)`, and clarified in the surrounding text that the CDFs shift toward smaller `D_disc` after smoothing.

**Comment 4:** *Figure 6: I would replace "thin line" by "dashed line" in the caption.*

**Response 4:** We have revised the Figure 6 caption accordingly. The caption now explicitly states that the light translucent lines show individual measurements, while the dashed black and solid blue lines show the running-mean trends before and after debiasing, respectively.

**Comment 5:** *Sect. 5.2 line 275, O-C stands for "Observed minus Calculated" rather than "observation-minus-ephemeris".*

**Response 5:** We thank the reviewer for the correction. We have revised the definition of O-C in Section 5.2 to "Observed minus Calculated (O-C)".

**Comment 6:** *Line 288: I would prefer "decreases the random component" instead of "suppresses the random component".*

**Response 6:** We have revised the wording as suggested. The sentence now states that averaging over the `N` observations of a file "decreases the random component" by `1/sqrt(N)`.

**Response to Data Editor's Review**

**Comment:** *Once your paper is accepted, please publish your NADC repository and replace the URL (https://nadc.china-vo.org/res/r101824/) with the DOI using the AASTeX `\dataset[]{}` command to ensure the repository DOI is tagged as article data in production.*

**Response:** Thank you for the instruction. We will publish the NADC repository after the manuscript is accepted and replace the current URL with the repository DOI using the AASTeX `\dataset[]{}` command, so that the repository DOI is properly tagged as article data in production. Since the repository DOI is not yet available at this revision stage, we have retained the current NADC URL for review.

Once again, we thank the reviewer and the Data Editor for their valuable comments, which have helped us improve the clarity and accuracy of the manuscript.
