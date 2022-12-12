path = "/Users/behnooshashrafi/Documents/Semester_3/Thesis/saga/"
complement_dict = {
    "A": "T",
    "T": "A",
    "C": "G",
    "G": "C",
    "a": "T",
    "t": "a",
    "c": "g",
    "g": "c",
    "n": "n",
    "N": "N",
}
RNA_dict = {
    "A": "A",
    "T": "U",
    "C": "C",
    "G": "G",
    "a": "a",
    "t": "u",
    "c": "c",
    "g": "g",
    "n": "n",
    "N": "N"
}


def reads(transcript, header):
    possible_reads = []
    possible_proteins = []
    seq = ""
    # starts = []
    # start = "AUG"
    # stop = ["UGA", "UAA", "UAG"]
    index_start = 0
    index_stop = len(transcript) - 2
    for i in range(len(transcript) - 2):
        if i == index_stop:
            break
        if transcript[i].upper() == "A" and transcript[i + 1].upper() == "T" and transcript[i + 2].upper() == "G":
            index_start = i
            # finding codons after the start codon
            codon = [transcript[j:j + 3].upper() for j in range((index_start), len(transcript) - 2)]
            # findign the first stop codon
            if "TGA" in codon:
                index_stop = codon.index("TGA")
            elif "TAA" in codon:
                if index_stop > codon.index("TAA"):
                    index_stop = codon.index("TAA")
            elif "TAG" in codon:
                if index_stop > codon.index("TAG"):
                    index_stop = codon.index("TAG")
            else:  # if the transcript has no stop codon then break
                break
            if "n" not in transcript[index_start: index_start + index_stop]:
                seq = transcript[index_start: index_start + index_stop + 3]
            if len(seq) > 45 and len(seq) < 303:
                if len(seq) % 3 == 0:
                    pro = protein(seq[:-3].upper())
                    if pro != "":
                        possible_reads.append(seq)
                        possible_proteins.append(pro)
                        FASTA(seq, header, index_start, len(seq))

    return possible_reads, possible_proteins


def reverse(transcript):
    complement = [complement_dict[i] for i in transcript]
    reverse_complement = "".join(complement)
    return reverse_complement[::-1]


def DNA2RNA(transcript):
    return "".join([RNA_dict[i] for i in transcript])


def protein(read):
    #     table = {"UUU" : "F", "CUU" : "L", "AUU" : "I", "GUU" : "V",
    #            "UUC" : "F", "CUC" : "L", "AUC" : "I", "GUC" : "V",
    #            "UUA" : "L", "CUA" : "L", "AUA" : "I", "GUA" : "V",
    #            "UUG" : "L", "CUG" : "L", "AUG" : "M", "GUG" : "V",
    #            "UCU" : "S", "CCU" : "P", "ACU" : "T", "GCU" : "A",
    #            "UCC" : "S", "CCC" : "P", "ACC" : "T", "GCC" : "A",
    #            "UCA" : "S", "CCA" : "P", "ACA" : "T", "GCA" : "A",
    #            "UCG" : "S", "CCG" : "P", "ACG" : "T", "GCG" : "A",
    #            "UAU" : "Y", "CAU" : "H", "AAU" : "N", "GAU" : "D",
    #            "UAC" : "Y", "CAC" : "H", "AAC" : "N", "GAC" : "D",
    #            "UAA" : "STOP", "CAA" : "Q", "AAA" : "K", "GAA" : "E",
    #            "UAG" : "STOP", "CAG" : "Q", "AAG" : "K", "GAG" : "E",
    #            "UGU" : "C", "CGU" : "R", "AGU" : "S", "GGU" : "G",
    #            "UGC" : "C", "CGC" : "R", "AGC" : "S", "GGC" : "G",
    #            "UGA" : "STOP", "CGA" : "R", "AGA" : "R", "GGA" : "G",
    #            "UGG" : "W", "CGG" : "R", "AGG" : "R", "GGG" : "G"
    #            }
    table = {
        'ATA': 'I', 'ATC': 'I', 'ATT': 'I', 'ATG': 'M',
        'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACT': 'T',
        'AAC': 'N', 'AAT': 'N', 'AAA': 'K', 'AAG': 'K',
        'AGC': 'S', 'AGT': 'S', 'AGA': 'R', 'AGG': 'R',
        'CTA': 'L', 'CTC': 'L', 'CTG': 'L', 'CTT': 'L',
        'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCT': 'P',
        'CAC': 'H', 'CAT': 'H', 'CAA': 'Q', 'CAG': 'Q',
        'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGT': 'R',
        'GTA': 'V', 'GTC': 'V', 'GTG': 'V', 'GTT': 'V',
        'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCT': 'A',
        'GAC': 'D', 'GAT': 'D', 'GAA': 'E', 'GAG': 'E',
        'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGT': 'G',
        'TCA': 'S', 'TCC': 'S', 'TCG': 'S', 'TCT': 'S',
        'TTC': 'F', 'TTT': 'F', 'TTA': 'L', 'TTG': 'L',
        'TAC': 'Y', 'TAT': 'Y', 'TAA': '_', 'TAG': '_',
        'TGC': 'C', 'TGT': 'C', 'TGA': '_', 'TGG': 'W',
    }
    protein = ""

    for i in range(0, len(read), 3):
        if "n" in read[i:i + 3]:
            protein += "X"
        else:
            protein += table[read[i:i + 3]]
    return protein


def FASTA(seq, header, start_index, length):
    a = header.split(" ")
    f = open(path+"possible_sORFs.fa", "a")
    f.write(">"+ a[1].replace(";","") + "st" + a[5].replace(";","") + "smp" + str(start_index) + "lmp" + str(length))
    f.write("\n")
    f.write(seq)
    f.write("\n")
    f.close()
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    with open(path+"Only_transcripts.fa", "r") as f:
        raw = f.read()
    tr = raw.splitlines()
    r = {}
    p = {}
    for i in range(int(len(tr) / 2)):
        # RNA = DNA2RNA(tr[2*i+1])
        m = []
        n = []
        if "Strand: +" in tr[2 * i]:
            m, n = reads(tr[2 * i + 1], tr[2 * i])
            r.update({tr[2 * i]: m})
            p.update({tr[2 * i]: n})

        else:
            rev = reverse(tr[2 * i + 1])
            m, n = reads(rev, tr[2 * i])
            r.update({tr[2 * i]: m})
            p.update({tr[2 * i]: n})

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
