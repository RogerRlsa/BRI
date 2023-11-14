import timeit
from multiprocessing import process

def lerColecao(path):
    cont = ""
    with open(path, "r") as f:
        cont = f.read()
    return cont.split(".I")

def removerLixo(s):
    return s.replace(".T","").replace(".A","").replace(".B","").replace(".W","").replace("the ","").replace("a ","").replace("of ","")

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
    for i in enumerate(indice[1:-1]):
        limite = comparar(i[1],q)
        if limite > 0.09:
            if i in d:
                if d[i[0]] < limite:
                    d[i[0]] = limite
            else:
                d[i[0]] = limite
    return d

def rankear(resultados):
    return sorted(resultados.items(), key = lambda x : x[1], reverse=True)


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
#i=0
for con in qry[1:-1]:
    di = {}
    print("consulta:",con)
    consultaLimpa = removerLixo(con)
    print("consulta limpa: ",consultaLimpa)
    listaConsulta = extrairExpandir(consultaLimpa)
    for sdi in listaConsulta:
        di = buscar(sdi,di) # resultados de uma pesquisa
    
    resultados = rankear(di)

    listaResultados.append(di) # resultados de todas as pesquisa
    #print(len(di))
    print(resultados)    
    #if i==2: break
    #i+=1


#print(listaResultados)
#print("docs:",indice[1])
#consultas = lerColecao("cran.qry")
#print("#qry:",len(consultas))
