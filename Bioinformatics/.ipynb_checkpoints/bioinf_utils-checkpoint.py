import numpy as np


def readSeq(filename):
    """Reads in a FASTA sequence. Assumes one sequence in the file"""
    seq = []

    with open(filename, "r") as f:
        for line in f:
            if line.startswith(">"):
                continue
            seq.append(line.rstrip().upper())

    return "".join(seq)

def gen_seqs(seq_len, percent_diff):

    choices = ['A', 'T', 'G', 'C']

    seq1 = np.random.choice(choices, seq_len)

    n_diffs = int(seq_len*percent_diff)

    sub_idxs = np.random.choice(list(range(seq_len)), n_diffs, replace=False)
    bases_to_sub = np.random.choice(choices, n_diffs)
    subs = dict(zip(sub_idxs, bases_to_sub))

    seq2 = np.array([subs[i] if i in sub_idxs else b for i,b in enumerate(seq1)])

    return seq1,seq2

def dotplot(seq1, seq2=None):
    if not seq2:
        seq2=seq1.copy()
    return np.array([[int(i==j) for j in seq2] for i in seq1])


def make_del(seq, amnt):
    
    del_start = np.random.choice(len(seq),1)[0]
    del_end = del_start+amnt
    
    print(f'seq del at {del_start} to {del_end} - {del_end-del_start} total')
    seq = np.concatenate([seq[:del_start],seq[del_end:]], axis=0)
    return seq

def gen_dels(seqs, amnt, variation):
    del_seqs = []
    for seq in seqs:
        sign = np.random.choice([1,-1],1)[0]
        var_amnt = sign * np.random.choice(np.linspace(0, variation, 1000),1)[0]
        amnt += int(var_amnt)
        del_seqs.append(make_del(seq,amnt))
    return del_seqs