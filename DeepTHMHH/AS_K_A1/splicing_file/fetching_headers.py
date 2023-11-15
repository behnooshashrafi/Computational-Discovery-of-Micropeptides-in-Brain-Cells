import fileinput
import string
from json.tool import main
# We need the whole header from the original database from smorfinder so we can find the locations on the chromosomes.
if __name__ == '__main__':
	with open("TM.fa", "r") as f:
		raw = f.read()
	query = raw.split("\n")
	with open("aa_sorted_uniq.fa", "r") as g:
		raw_2 = g.read()
	DB = raw_2.split("\n")
	h = open("headers.fa", "a")
	for i in range(int(len(query)/3)):
		for j in range(int(len(DB)/2)):
			if query[3*i].split(" |")[0] in DB[2*j]:
#				h.write(query[i*3])
#				h.write("\n")
				h.write(DB[j*2])
				h.write("\n")
				h.write(DB[j*2+1])
				h.write("\n")
				h.write(query[i*3+2])
				h.write("\n")
	h.close()

