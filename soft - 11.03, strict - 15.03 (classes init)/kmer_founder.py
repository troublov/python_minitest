# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 11:10:51 2018

@author: Orlov
"""
from Bio import SeqIO


class kmer:
    sequence=''
    
    def __init__(self, seq):
        self.counter= 1
        self.sequence=seq
        self.coord=[]
        
    def increase(self):
        self.counter+=1
    
    def show_info(self):
        print(self.sequence, 'occurs ', self.counter, 'times')
        for position in self.coord:
            print('from:\t', position[0], '\tbp ', ' to\t', position[1], '\tbp')

file_path="seq_y_pestis.fasta"
kmer_length=23
seq_dict={}


for fasta in SeqIO.parse(file_path, 'fasta'):
    inp_seq= str(fasta.seq).upper()
    seq_len=len(inp_seq)
    for index in range(seq_len-kmer_length+1):
        start=index
        end=index+kmer_length
        subseq = inp_seq[start:end]
        if subseq in seq_dict.keys():
            seq_dict[subseq].increase()
        else:
            seq_dict[subseq]=kmer(subseq)
        seq_dict[subseq].coord.append([start, end])
        
print('Hello, all kmers were recorded ')


max_freq=0
max_freq_seq=[]
for ind in seq_dict.keys():
    if seq_dict[ind].counter>max_freq:
        max_freq=seq_dict[ind].counter
        max_freq_seq=[]
        max_freq_seq.append(seq_dict[ind])
    elif seq_dict[ind].counter==max_freq:
        max_freq_seq.append(seq_dict[ind])

for element in max_freq_seq:
    print(element.counter, element.sequence, element.coord)


for element in max_freq_seq:
    element.show_info()
    print('\n')           

