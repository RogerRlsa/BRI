import timeit
#from multiprocessing import process

def lerColecao(path):
    cont = ""
    with open(path, "r") as f:
        cont = f.read()
    return cont.split(".I")

def removerLixo(s):
    return s.replace(".T","").replace(".A","").replace(".B","").replace(".W","").replace("the ","").replace("a ","").replace("of ","")

def addIndice(doc):
    indice.append(doc)

def addIndiceInv(con):
    termos = list(set(con.split(" ")))
    for doc in enumerate(indice):
        termosDoc = set(doc[1])
        for t in termos:
            if t in termosDoc:
                if t not in indiceInv:
                    indiceInv[t] = [doc[0]]
                else:
                    indiceInv[t].append(doc[0])

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
indiceInv = dict()


#arquivo carn
documentos = lerColecao("/home/aluno/Downloads/BRI-main/m-bool/docs/cran.all.1400")
print("#docs:",len(documentos),"\n")

antesLixo = timeit.default_timer()

for doc in documentos:
    doc = removerLixo(doc)
    addIndice(doc) #passando de uma lista pra outra (???)
    #print("#ind:",len(indice))

depoisLixo = timeit.default_timer() - antesLixo

print("%f" %(depoisLixo),"\n")

#arquivo qry
qry = lerColecao("/home/aluno/Downloads/BRI-main/m-bool/docs/cran.qry")
print("#qry:",len(qry),"\n")

listaResultados = []

for con in qry[1:-1]:
    di = {}
    #print("consulta:",con)
    consultaLimpa = removerLixo(con)
    #print("consulta limpa: ",consultaLimpa)
    listaConsulta = extrairExpandir(consultaLimpa)
    for sdi in listaConsulta:
        di = buscar(sdi,di) # resultados de uma pesquisa
    
    resultados = rankear(di)

    listaResultados.append(di) # resultados de todas as pesquisa
    #print(len(di))
    print(resultados)    
    break


#print(listaResultados)
#print("docs:",indice[1])
#consultas = lerColecao("cran.qry")
#print("#qry:",len(consultas))
