import fileinput
import string
from json.tool import main

# To create modified file: to have transcripts and exons with a more clear headers. Here we have the gtf file (containing the desired header and the fa file with the seq)
def identifier (line):
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
        #f.write(key+": "+value+"; ")
        f.write(value + ";")
    f.write("\n")
    f.write(seq)
    f.write("\n")
    f.close()
def modified(seq, header):
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

# To create Only_transcripts from the modified file: With clear headers for the Mipepid
def Mipepid():
    with open("modified.fa", 'r') as p:
        raw_p = p.read()
    new = raw_p.split("\n")

    f = open("Only_transcripts.fa", "a")
    for i in range(int(len(new) / 2)):
        if "transcript" in new[2 * i]:
            temp = new[2 * i].split(";")
            temp_2 = temp[0] + "/" + temp[2] + "/" + temp[
                3]  # Mipepid takes only the first part as the name id of peptides.
            f.write(temp_2)
            f.write("\n")
            f.write(new[2 * i + 1])
            f.write("\n")
    f.close()



