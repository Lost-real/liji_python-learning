

d = []
chl_fasta = {}
fn1=open ("Ahalleri_264_v1.1.gene.gff5minuspromoter","r")
fn2=open("Ahalleri_264_v1.1.gene.gff5minuspromoterout.txt","w")
for row in fn1:
    if ">" in row:
        fsy = row.split()
        chl_gene = fsy[0].replace('>', '')
        fsy_sequence = ''
    else:
        ro=row.strip()
        # print(ro)
        sequences = ro.split()
        # print(row)
        # print(sequences)
        store = sequences[0]
        # print(sequences[0])
        fsy_sequence = str(fsy_sequence) + str(store)
        chl_fasta[chl_gene] = fsy_sequence
def reverse_complement(seq):
  ntComplement = {'A':'T','T':'A','G':'C','C':'G','N':'N','a':'t','t':'a','c':'g','g':'c','n':'n'}
  RevSeqList = list(reversed(seq))
  RevComSeqList = [ntComplement[k] for k in RevSeqList]
  RevComSeq = ''.join(RevComSeqList)
  return RevComSeq
for i in chl_fasta:
    h=reverse_complement(chl_fasta[i])
    # print(h)
    result=">"+str(i)+"\n"+str(h)+'\n'
    fn2.write(result)