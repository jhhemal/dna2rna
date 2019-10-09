dna = input("Enter DNA sequence : ").upper()
rna = dna.maketrans('ACGT','UGCA')
a = dna.count('A')
c = dna.count('C')
g = dna.count('G')
t = dna.count('T')

print(f"Total no. of A : {a}")
print(f"Total no. of C : {c}")
print(f"Total no. of G : {g}")
print(f"Total no. of T : {t}")

print(f"The DNA was : {dna}")
print(f"The RNA is : {dna.translate(rna)}")