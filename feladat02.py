lista = []
def beolvas():
    with open("kutyusok.txt", encoding="utf-8") as f:
        for i in f:
            
            i = i.strip()
            lista.append(i)


def NB():
    global Nlista
    Nlista = []
    for i in lista:
        i = i.upper()
        Nlista.append(i)
    #print(Nlista)
    print(len(Nlista))


def IV(): #i-re végződik
    lista0 = []
    for i in Nlista:
        if i[-1] =="I":
            lista0.append(i)
    print(lista0)


def main():
    beolvas()
    NB()
    IV()


main()