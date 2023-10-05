import timeit
from multiprocessing import process

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

def extrairExpandir(texto):
    return [texto]

def comparar(q, i)-> bool:
    palavrasQ = set(q[0].split(" "))
    palavrasD = set(i.split(" "))
    #print(q)
    intdq = palavrasD.intersection(palavrasQ)
    #print(palavrasQ)
    #print()
    #print(len(intdq))
    #exit()
    if (len(intdq)/len(palavrasQ)) > 0.35:
        return True
    else:
        return False

def buscar(q):
    resultados = []
    for i in enumerate(indice):
        if comparar(q,i[1]):
            resultados.append(i[0])
    return resultados
    
def rankear(resultados):
    
    pass

indice = list()

#arquivo carn
documentos = lerColecao("cran.all.1400")
print("#docs:",len(documentos),"\n")

antesLixo = timeit.default_timer()

for doc in documentos:
    doc = removerLixo(doc)
    addIndice(doc)
    #print("#ind:",len(indice))

depoisLixo = timeit.default_timer() - antesLixo

print("%f" %(depoisLixo),"\n")

#arquivo qry
qry = lerColecao("cran.qry")
print("#qry:",len(qry),"\n")

for con in qry[1:-1]:
    #print(con)
    consultaLimpa = removerLixo(con)
    #print(consultaLimpa)
    listaConsulta = extrairExpandir(consultaLimpa)
    #print(listaConsulta)
    listaResultados = []
    resultados = buscar(listaConsulta) # resultados de uma pesquisa
    
    listaResultados.append(resultados) # resultados de todas as pesquisa

    rankear(listaResultados)

    print(resultados)
    break


#print("docs:",indice[1])
#consultas = lerColecao("cran.qry")
#print("#qry:",len(consultas))
