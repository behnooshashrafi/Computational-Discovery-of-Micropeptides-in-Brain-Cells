for i in {0..3}
do
	cd file$i/
	grep -A 2 " TM" predicted_topologies.3line > TM9.fa
	grep -v "^--" TM9.fa > TM$i.fa
	grep -A 2 " SP+TM" predicted_topologies.3line > SPTM9.fa
	grep -v "^--" SPTM9.fa > SPTM.fa
	cat SPTM.fa | tee -a TM$i.fa
	rm TM9.fa SPTM9.fa
	cat TM$i.fa | tee -a ../TM.fa
	cd ..
done
