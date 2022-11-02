
d = {}
chl_fasta = {}
fn1=open ("0919.txt","r")
fn2=open("0920.txt","r")
for i in fn1:
    i1=i.strip().split()
    d[i1[0]]=1

for row in fn2:
    if ">" in row:
        fsy = row.split()
        chl_gene = fsy[0].replace('>', '')
        fsy_sequence = ''
    else:
        ro=row.strip()
        # print(ro)
        sequences = ro.split()
        # sequences=''.join(sequences)
        # print(row)
        # print(sequences)
        store = sequences[0]
        # print(store)
        fsy_sequence = fsy_sequence + store
        chl_fasta[chl_gene] = fsy_sequence
# print(chl_fasta['aaa'][0:2])
#
for i in d.keys():
    if i in chl_fasta.keys():
        print(">"+str(i)+"\n"+chl_fasta[i][0:1])
    else:
        continue