CodindgStrand=input()
def Transcribe(x):
    for i in range (len(x)):
        if x[i]=='T':x=x.replace(x[i],'U')
    return x
print (Transcribe(CodindgStrand))
