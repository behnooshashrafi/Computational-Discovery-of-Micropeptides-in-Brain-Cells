import fileinput
import string 
from json.tool import main
# This code is to create an intron-free transcript.
with open("AS_P_E1_header.fa", "r") as p:
	raw = p.read()
all = raw.split("\n")
f = open("tr_header.fa", "a") 
for i in range(int(len(all)/2)):
	if "transcript" in all[2*i]:
		f.write(all[2*i])
		#temp=all[2*i].split(";")
		#temp_2=temp[0]+"/"+temp[2]+"/"+temp[3]
		#f.write(temp_2)
		f.write("\n")
		f.write(all[2*i+1])
		f.write("\n")
f.close
