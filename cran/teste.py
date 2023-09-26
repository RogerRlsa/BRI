import timeit


def lerColecao(path):
    cont = ""
    with open(path, "r") as f:
        cont = f.read()
    return cont.split(".I")

def removerLixo(s):
    return s.replace(".T","").replace(".A","").replace(".B","").replace(".W","")

def addIndice(doc):
    #doc = doc.split()
    indice.append(doc)


indice = list()

documentos = lerColecao("cran.all.1400")
print("#docs:",len(documentos))

antesLixo = timeit.default_timer()

for doc in documentos:
    doc = removerLixo(doc)
    addIndice(doc)
    #print("#ind:",len(indice))

depoisLixo = timeit.default_timer() - antesLixo

print("%f" %(depoisLixo))

#consultas = lerColecao("cran.qry")
#print("#qry:",len(consultas))
