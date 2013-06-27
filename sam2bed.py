from pysam import Samfile

## written for SICER 

def parse_barcode(bamfile):
	"""parses a sorted and index bam file, removes all cases where rna hits more than one spot in genome
	and writes to a file, create file for mutant and wildtype based on barcodes"""
	samfile = Samfile(bamfile, "rb")
	for line in samfile.fetch():
        print line.tid, line.qstart, line.qend, line.qqual


parse_barcode("file_sorted.bam")
#
### is_duplicate NOPE, is_proper_pair, is_read1, is_qcfail, is_seconday nope, is_unmapped
