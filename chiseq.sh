
### QC
#TODO compare file of bad qulity and good qc
#TODO use trim reads on the known adaptors
#./trimReads SRR402059.fastq
#TODO also test other QC programs


### RUN BWA

#TODO use diff params for diff alignments
#$bwa aln -t 4 -n 0.1  -I $mapDbFasta $inputFastqFile
#bwa aln -t 4  genome.fa SRR072991.fastq > SRR072991.sai
#bwa aln -t 4  genome.fa SRR072992.fastq > SRR072992.sai


#### Convert BWA to SAM file

#bwa samse -n 1 -t 4  SRR072991.sai genome.fa SRR072992.fastq > SRR072991.sam
#bwa samse -n 1  SRR072992.sai genome.fa SRR072992.fastq > SRR072992.sai

#### Convert sam to sorted sam?!

#samtools view -bS a_hits.sam | samtools sort - file_sorted
#samtools index file_sorted.bam file_sorted.bai
#samtools sort accepted_hits.bam a_sort
#samtools index a_sort.bam a_index.bam

### Convert sam to bed using pysam/mycode

### Run MACS and SICER


