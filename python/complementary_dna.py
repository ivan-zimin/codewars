def DNA_strand(dna):
    return(dna.translate(str.maketrans({'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'})))

print(DNA_strand('ATTGC'))