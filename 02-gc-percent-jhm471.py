# Week 2 homework GCpercent.
# Jesse Matsubara 10-23-2017.

# First 100 nucleotides of the influenza H1N1 virus segment 8.
flu_ns1_seq = 'GTGACAAAGACATAATGGATCCAAACACTGTGTCAAGCTTTCAGGTAGATTGCTTTCTTTGGCATGTCCGCAAACGAGTTGCAGACCAAGAACTAGGTGA'

# 1) Count the number of "C's".
c_count = 0
for i in range(len(flu_ns1_seq)):
    if flu_ns1_seq[i] == 'C':
       c_count = c_count + 1

# 2) Count the number of "G's".
g_count = 0
for i in range(len(flu_ns1_seq)):
    if flu_ns1_seq[i] == 'G':
        g_count = g_count + 1

# 3) Add "C" and "G" counts.
gc_count = c_count + g_count

# 4) Count total number of nucleotides.
total_count = len(flu_ns1_seq)

# 5) Divide number of "C" and "G" nucleuotides by total number of nucleotides.
gc_percent = gc_count / total_count

# 6) print percentage
print("'GC' percentage = ", gc_percent * 100)
