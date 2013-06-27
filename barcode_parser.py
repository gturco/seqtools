from pysam import Samfile

def parse_barcode(bamfile):
	"""parses a sorted and index bam file, removes all cases where rna hits more than one spot in genome
	and writes to a file, create file for mutant and wildtype based on barcodes"""
	samfile = Samfile(bamfile, "rb")
	multi_hit_file = Samfile("MultiHit.bam","wb",template=samfile)
	mutant = Samfile("Mutant.bam","wb",template=samfile)
	wildtype = Samfile("Wildtype.bam","wb",template=samfile)
	for line in samfile.fetch():
		#if line.is_secondary:
		## does this hit to more than one spot in genome
		#	multi_hit_file.write(line)
		if "#GAGT"in line.qname or "#TTAG" in line.qname: 
		## write to mutant file
			mutant.write(line)
		elif "#ACCC" in line.qname or "#CGTA" in line.qname:
		### write to wildtype file
			wildtype.write(line)

	multi_hit_file.close()
	mutant.close()
	wildtype.close()
	samfile.close()

parse_barcode("file_sorted.bam")


def parse_barcode(bamfile):
	"""parses a sorted and index bam file, removes all cases where rna hits more than one spot in genome
	and writes to a file, create file for mutant and wildtype based on barcodes"""
	samfile = Samfile(bamfile, "rb")
	multi_hit_file = Samfile("MultiHit.bam","wb",template=samfile)
	mutant_one = Samfile("MutantOne.bam","wb",template=samfile)
	wildtype_one = Samfile("WildtypeOne.bam","wb",template=samfile)
	mutant_two = Samfile("MutantTwo.bam","wb",template=samfile)
	wildtype_two = Samfile("WildtypeTwo.bam","wb",template=samfile)
	for line in samfile.fetch():
		#if line.is_secondary:
		## does this hit to more than one spot in genome
		#	multi_hit_file.write(line)
		if "#GAGT"in line.qname: 
		## write to mutant file
			mutant_one.write(line)
		elif "#TTAG" in line.qname:
			mutant_two.write(line)
		elif "#ACCC" in line.qname:
		### write to wildtype file
			wildtype_one.write(line)
		elif "#CGTA" in line.qname:
		### write to wildtype file
			wildtype_two.write(line)

	multi_hit_file.close()
	mutant_one.close()
	wildtype_one.close()
	mutant_two.close()
	wildtype_two.close()
	samfile.close()

parse_barcode("file_sorted.bam")
#
### is_duplicate NOPE, is_proper_pair, is_read1, is_qcfail, is_seconday nope, is_unmapped
