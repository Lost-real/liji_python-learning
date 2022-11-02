import argparse
parser = argparse.ArgumentParser(description="Advanced screening always by hash")
parser.add_argument("-f1","--file1",help="the original file,tabulated,make sure do not contain blank line")
args = parser.parse_args()
with open(args.file1,"r") as fr:
    B = 0
    E = 0
    H = 0
    I = 0
    M = 0
    P = 0
    S = 0
    s = 0
    for i in fr:
        i = i.strip()
        if i.startswith("B"):
            B += 1
        elif i.startswith("E"):
            E += 0
        elif i.startswith("H"):
            H += 0
        elif i.startswith("I"):
            I += 0
        elif i.startswith("M"):
            M += 0
        elif i.startswith("P"):
            P += 0
        elif i.startswith("S"):
            S += 0
        elif i.startswith("s"):
            s += 0
        else:
            continue

    print(args.file1+" B "+str(B)+"\n"+args.file1+" E "+str(E)+"\n"+args.file1+" H "+str(H)+"\n"+args.file1+" I "+str(I)+"\n"+args.file1+" M "+str(M)+"\n"+args.file1+" P "+str(P)+"\n"+args.file1+" S "+str(S)+"\n"+args.file1+" s "+str(s))
