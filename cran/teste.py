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
    indice.append(doc)

def extrairExpandir(texto):
    return [texto]

def comparar(q, i)-> bool:

    palavrasQ = set(q.split(" "))
    palavrasD = set(i.split(" "))
    intdq = palavrasD.intersection(palavrasQ)

    return (len(intdq)/len(palavrasQ))  

def buscar(q, d):
    for i in indice:
        if i in d:
            if d[i] < comparar(i,q):
                d[i] = comparar(i,q)
        else:
            d[i] = comparar(i,q)
    return d

def rankear(resultados):
    return resultados[max(resultados,key=resultados.get)]


indice = list()


#arquivo carn
documentos = lerColecao("/home/aluno/Downloads/BRI-main/cran/docs/cran.all.1400")
print("#docs:",len(documentos),"\n")

antesLixo = timeit.default_timer()

for doc in documentos:
    doc = removerLixo(doc)
    addIndice(doc)
    #print("#ind:",len(indice))

depoisLixo = timeit.default_timer() - antesLixo

print("%f" %(depoisLixo),"\n")

#arquivo qry
qry = lerColecao("/home/aluno/Downloads/BRI-main/cran/docs/cran.qry")
print("#qry:",len(qry),"\n")

listaResultados = []

for con in qry[1:-1]:
    di = {}
    #print(con)
    consultaLimpa = removerLixo(con)
    #print(consultaLimpa)
    listaConsulta = extrairExpandir(consultaLimpa)
    for sdi in listaConsulta:
        di = buscar(sdi,di) # resultados de uma pesquisa

    #resultados = rankear(resultados)

    listaResultados.append(di) # resultados de todas as pesquisa
    print(len(di))
    print(di.values())
    break

#print(listaResultados)
#print("docs:",indice[1])
#consultas = lerColecao("cran.qry")
#print("#qry:",len(consultas))
