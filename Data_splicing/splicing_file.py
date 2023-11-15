# To use TMHMM we need to feed it about 1000 sequences which is 2000 lines 
in a fasta file at a time. This program simply splices the data to smaller 
files.
import fileinput
import string
from json.tool import main
if __name__ == '__main__':
	with open("AA_sorted_uniq.fa", "r") as f:
		raw = f.read()
	lines = raw.split("\n")
	length = 2000
	t = int(len(lines)/length)
	for i in range(t):
		f = open(f"file{i}.fa", "a")
		for j in range(i*length, (i+1)*length):
			f.write(lines[j])
			f.write("\n")
		f.close()
	g = open("file_rest.fa", "a")
	for i in range(t*length, len(lines)):
		g.write(lines[i])
		g.write("\n")
	g.close()
