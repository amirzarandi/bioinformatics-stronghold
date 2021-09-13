TemplateStrand=input()
def Transcribe(x):
    RNA=[]
    for i in range (len(x)): 
        if x[-i-1]=='A':RNA.append('U')
        if x[-i-1]=='T':RNA.append('A')
        if x[-i-1]=='C':RNA.append('G')
        if x[-i-1]=='G':RNA.append('C')
    return ''.join(RNA)
print (Transcribe(TemplateStrand))
