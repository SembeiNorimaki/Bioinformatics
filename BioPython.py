from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

my_seq = Seq("AGTACACTGGT")   # without alphabet defined

my_seq = Seq("AGTACACTGGT", IUPAC.unambiguous_dna)   # DNA alphabet

# get the sequence alphabet
my_seq.alphabet   


# print the position, sequence and lenght
for index, letter in enumerate(my_seq) :
    print index, letter
    print len(letter)

# access elements of the sequence
print my_seq[0] #first element
print my_seq[2] #third element
print my_seq[-1] #last element

# count
my_seq.count('G')

# GC percentage   (#G + #C) / #Total
from Bio.SeqUtils import GC
GC(my_seq)


# slicing
my_seq[4:12]   # includes 4th, excludes 12th

# reversing:
my_seq[::-1]

# convert to string
my_seq.tostring()

# concatenate sequences
seq1 + seq2  # ONLY if alphabets are compatible

# otherwise, convers both seq to generic alphabets
from Bio.Alphabet import generic_alphabet
seq1.alphabet = generic_alphabet
seq2.alphabet = generic_alphabet
seq1 + seq2


# sequence complement (only if alphabet allows complement)
my_seq.complement()

# reverse complement (only if alphabet allows complement)
my_seq.reverse_complement()


# transcribe RNA  (DNA -> mRNA)
#The actual biological transcription process works from the template strand, doing a reverse complement
#(TCAG → CUGA) to give the mRNA. However, in Biopython and bioinformatics in general, we typically
#work directly with the coding strand because this means we can get the mRNA sequence just by switching
#T → U.

from Bio.Seq import transcribe
# just changes T with U from the coding strand (5' -> 3') 
messenger_rna = transcribe(coding_dna)  

# if we want to transcribe from the template strand (3' -> 5'):
transcribe(template_dna.reverse_complement())


# transcribing back to DNA:
from Bio.Seq import Seq, back_transcribe
back_transcribe(messenger_rna)   # just changes U -> T and gives the coding strand


# 3.8 Translation  (mRNA -> Protein)
# Uses standard genetic code
from Bio.Seq import Seq, translate
from Bio.Alphabet import IUPAC
messenger_rna = Seq("AUGGCCAUUGUAAUGGGCCGCUGAAAGGGUGCCCGAUAG", IUPAC.unambiguous_rna)
translate(messenger_rna)


# Direct translation (DNA -> Protein
from Bio.Seq import Seq, translate
from Bio.Alphabet import IUPAC
coding_dna = Seq("ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG", IUPAC.unambiguous_dna)
translate(coding_dna)

# we can specify other translation tables by name
translate(coding_dna, table="Vertebrate Mitochondrial")
# or by NCBI number
translate(coding_dna, table=2)

# 3.9 Transcription and Translation

# 3.10 Mutable Seqs
# convert existing sequence to mutable
mutable_seq = my_seq.tomutable()  
# or directly create a mutable one
from Bio.Seq import MutableSeq
from Bio.Alphabet import IUPAC
mutable_seq = MutableSeq("GCCATTGTAATGGGCCGCTGAAAGGGTGCCCGA", IUPAC.unambiguous_dna)

# now we can do
mutable_seq[5] = "T"

# and convert it back to an inmutable seq
new_seq = mutable_seq.toseq()


