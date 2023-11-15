# Computational Discovery of Micropeptides in Brain Cells
## Abstract
Micropeptides are short proteins ranging from 15 to 100 amino acids in length. Due to their short length, they are mostly overlooked and considered as noise in the translation process. There are many micropeptides translated from long non-coding RNAs that were previously ignored. Some new experimental discoveries have shown some of these micropeptides act as regulatory agents in the human body. On the other hand, micropeptides have long been studied in the prokaryote domain. The new discoveries in eukaryotes gave us the idea to use the knowledge from the prokaryote domain and create a pipeline that uses different tools to predict promising micropeptides. The idea was to use the tools and extract features we think are interesting and have the top few candidates tested at the lab to be able to tune and improve the pipeline introduce new features or changes and remove the features that were proved to be less important for our purpose. Unfortunately, due to time restraints, we did not reach the experimental stage of the work and could not wait for the candidates to be tested in the lab.
    
For the tools' choice, first, we needed a micropeptide predictor for which we used SmORFinder. We decided the features we are going to take into account at this stage are the following: The micropeptides have to be transmembrane micropeptides for which we used the DeepTMHMM tool, and we want to study the amphipathicity of the candidates for which we used the HeliQuest. Our data was from three developmental stages of embryo (stem cell) to glia progenitor of the brain cell to astrocyte (fully developed brain cell), also containing control and patient data. Our results can be used for experimental validation or rejection of this work, which would lead to improvement or correction of the pipeline. The results can also be used for the comparison of the micropeptides expressed in different developmental stages, or the comparison of patient and control data.

## Data_preprocessing folder
First, we preprocess the data after BEDtools. To do so, the output from BEDtools is given to Transcripts.py in the Data_preprocessing folder.
tr.py attaches all the exons and creates intron-free transcripts.
Exctracting_read.py is to check the output of MiPepid. This script extracts all the possible micropeptides in a certain length.

## Data_splicing folder
To be able to feed the data to DeepTMHMM we need to split the data into files of around 2000 lines meaning 1000 sequences. To do this splicing_file.py is used.

## After_DeepTMHMM folder
To extract the candidates that are predicted to be transmembrane we used the my_script.sh. This script takes all the DeepTMHMM outputs and extracts only those with TM and SP+TM and reattaches them.
Then using fetching_headers.py, the headers corresponding to each candidate are found and replaced. This makes it possible to trace back each candidate to its original place on the genome.

# DeepTMHMM
The output of DeepTMHMM for the whole dataset is in this folder.

# Micropeptides.xlsx
Contains all the final candidates, their expression in different stages, their sequences and DeepTMHMM prediction of the sequences.
