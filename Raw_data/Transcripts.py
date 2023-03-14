import fileinput
import string
from json.tool import main


def identifier (string):
    p = line[-1].split(";")
    p[0] = p[0].replace("gene_id ", "")
    p[1] = p[1].replace(" transcript_id ", "")
    p[4] = p[4].replace(" cov ", "")
    if line[2] == "transcript":
        ### flag. create the indentifier to add at the end. when reaching the next transcript should return to this point, add string all of the exons and use this identifier for it.
        p[2] = p[2].replace(" ref_gene_name ", "")
        identifier = {
            "Chromosome" : line[0],
            #"Tool" : line[1],
            "type" : line[2],
            "start" : line[3],
            "stop" : line[4],
            #"dot1" : line[5],
            "Strand" : line[6],
            #"dot2" : line[7],
            "Gene_ID" : p[0],
            "Transcript_ID" : p[1],
            "Reference_gene_name" : p[2],
            "Cov" : p[3]
        }
    else:
        ###print as identifier and fetch the sequence
        p[2] = p[2].replace(" exon_number ", "")
        p[3] = p[3].replace(" ref_gene_name ", "")
        identifier = {
            "Chromosome" : line[0],
            #"Tool" : line[1],
            "type" : line[2],
            "start" : line[3],
            "stop" : line[4],
            #"dot1" : line[5],
            "Strand" : line[6],
            #"dot2" : line[7],
            "Gene_ID" : p[0],
            "Transcript_ID" : p[1],
            "Exon_num" : p[2],
            "Reference_gene_name" : p[3],
            "Cov" : p[4]
        }
    return identifier
def write_header(dictionary, seq):
    f = open("modified.fa", "a")
    f.write(">")
    for key, value in dictionary.items():
        f.write(key+": "+value+"; ")
    f.write("\n")
    f.write(seq)
    f.write("\n")
    f.close()


with open("AC_Ctr1_chr21.gtf", 'r') as f:
    raw_f = f.read()
header = raw_f.split("\n")
with open("chr21.fa.out", 'r') as g:
    raw_g = g.read()
seq = raw_g.split("\n")

flag = False
for i in range(len(header)-1):
    line = header[i].split("\t")
    head = identifier(line)
    if line[2] == "transcript":
        if flag == True:
            write_header(transcript_head, temp)
            flag = False
            transcript_head = head
        else:
            flag = True
            temp = ""
            transcript_head = head
    elif line[2] == "exon":
        write_header(head, seq[(2*i)+1])
        if flag == True:
            temp += seq[(2*i)+1]
            if i == (len(header)-2):
                write_header(transcript_head, temp)
