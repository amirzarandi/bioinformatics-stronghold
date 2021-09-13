N=input()
def NucleotideCount(x):
    A=0
    T=0
    C=0
    G=0
    for i in range(len(x)): 
        if x[i]=='A':A += 1 
        if x[i]=='T':T += 1 
        if x[i]=='C':C += 1 
        if x[i]=='G':G += 1 
    return str(A)+' '+str(C)+' '+str(G)+' '+str(T)
print (NucleotideCount(N))
