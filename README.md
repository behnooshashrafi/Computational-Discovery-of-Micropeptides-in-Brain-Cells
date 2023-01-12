# Micropeptide
Discovery of micropeptides in neurons
Surprisingly, only 1.5% of the human genome encodes our ~21,000 distinct protein-coding genes. Most of the genome is, however, turned into RNA and this includes tens of thousands of long non-coding RNAs (lncRNAs). Recent work has found that many lncRNAs actually do encode short proteins (approximately 30-100 amino acids), referred to as microproteins. This project seeks to identify neuron specific microproteins within previously gathered RNA sequencing data.
Water insoluble small proteins (~30 amino acids) are used in bacteria to affect the flow of small charged molecules across the impermeable plasma membrane in response to stress. This can lead to various effects such as allowing the bacteria to enter into a dormant state that allows them to evade the toxicity of antibiotics whilst preserving their optimised genome.
We hypothesise that large numbers of small proteins, microproteins, exist in higher organisms such as in humans as an effective way to regulate channels in cells that heavily use membrane channels as part of their functioning such as cells found in the heart and brain. As with bacteria, annotation of such small proteins in humans was missed as such small open reading frames were discarded as non-functional noise. However, recent work has given a tantalizing glimpse of what may lie hidden in the genome when a few small proteins were found to regulate a calcium channel in heart cells (Nelson et al., 2016; Payre & Desplan, 2016).
We propose here to carry out an automated search based on the properties of known small proteins and their genetic organisation so as to find new candidates. The top candidates will then be manually checked as to their suitability. If they’re deemed to have a low probability of functionality then the reasons for this will be used to further optimise the search algorithm. Interesting hits following the manual check will then be deleted in cells and overexpressed in cells to look for detectable effects.
To carry out this project, lncRNAs from human neuron RNA sequencing data need to be assessed for their likelihood to contain microprotein expressing open reading frames. The most promising candidates among these will be selected for further study using a set of criteria. These criteria could be based on properties of the protein (like length, amino acids, secondary structure, tertiary structure), properties of the encoding RNA
(e.g. length, codon usage, untranslated regions etc) or properties of the genomic region. Scripts should be written to automate this selection in combination with existing tools. Machine learning approaches may be used to weight and combine these criteria for the selection.
