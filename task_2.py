def DNA_strand(dna):
    s1 = "ACTG"
    return "".join([s1[(s1.find(dna[i])+2) % 4] for i in range(len(dna))])

print(DNA_strand("ATCG"))
print(DNA_strand("ATTGC"))
print(DNA_strand("GTAT"))