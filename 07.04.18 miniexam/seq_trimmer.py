#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  7 11:18:07 2018

@author: orlov
"""

from Bio import SeqIO, Seq
import argparse


def quality_trim(phred, tres, win_l):
    for ind in range(len(phred)-win_l):
        if (sum(phred[ind:(ind+win_l)])/win_l) < tres:
            return(ind)
    return(len(phred))
    



parser=argparse.ArgumentParser(description="Baby-matic script that offers head/tail cropping and 3' quality trimming of fastq files")
parser.add_argument('-hd', '--head', help="number of bases to crop from the 5'", type=int)
parser.add_argument('-t', '--tail', help="number of bases to crop from the 3'", type=int)
parser.add_argument('-q', '--quality_trimming', help='quality treshold and size of the sliding window', nargs=2)
parser.add_argument('-i', '--input', help='path to input file', type=str, required=True)
parser.add_argument('-o', '--output', help='path to output file', type=str, default='stdout')


args=parser.parse_args()
head_trim=args.head
tail_trim=args.tail
print('tail', tail_trim)
inp_file=args.input
out_file=args.output
if args.quality_trimming!=None:
    q_tres=int(args.quality_trimming[0])
    sliding_window_len=int(args.quality_trimming[1])

with open (out_file, 'w') as out_fastq:
    for rec in SeqIO.parse(inp_file, 'fastq'):
        curr_seq= str(rec.seq).upper()
        curr_qual=rec.letter_annotations['phred_quality']
        if tail_trim!=None:
            rec=rec[:len(rec)-tail_trim]
            print("Tail crop's been done")
        if head_trim!=None:
            rec=rec[head_trim:]
            print("Head crop's been done") 
        if (args.quality_trimming!=None):
            tr_ind=quality_trim(curr_qual, q_tres, sliding_window_len)
            rec=rec[:tr_ind]
        print(len(rec))
        SeqIO.write(rec, out_fastq,'fastq')
        














