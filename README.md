# python_minitest
Script for fastq simple processing
Script is writen on Python 3 and performes simple processing of fastq reads.
It can:
1. headcrop (n_bases is required)
2. tailcrop
3. quality trimming
          in the presented in the list order



usage: seq_trimmer.py [-h] [-hd HEAD] [-t TAIL]
                      [-q QUALITY_TRIMMING QUALITY_TRIMMING] -i INPUT
                      [-o OUTPUT]
seq_trimmer.py: error: the following arguments are required: -i/--input

Example FastQC reports on test fastq file are included in the repository, it was processed with command:
```bash
python3.6 seq_trimmer.py -t 5 -hd 5 -q 35 4 -i test_classwork3.fastq -o test_file3_all.fastq
```
File with "all" suffix is processed file.



