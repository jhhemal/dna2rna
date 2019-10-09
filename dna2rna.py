#!/usr/bin/env python3
#
# dna2rna.py - A python program to convert your DNA to RNA
#
# Author : Jahidul Hasan Hemal
#
# url: https://jhhemal.github.io
# 
dna = input("Enter DNA sequence : ").upper()
rna = dna.maketrans('ACGT','UGCA')  # Make a translation for converting DNA to RNA
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
