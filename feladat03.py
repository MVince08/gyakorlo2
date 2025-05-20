class Kutya():
    def __init__(self, nev, fajta, eletkor, gazdi):
        self.nev = nev
        self.fajta = fajta
        self.eletkor = eletkor
        self.gazdi = gazdi

    def __str__():
        return f""

lista = []

def f1():
    with open("kutyak.txt", encoding="utf-8") as f:
        for i in f:
            i = i.strip()
            i = i.split(";")
            lista.append(Kutya(i[0], i[1], i[2], i[3]))   
    #print(lista)


def f2():
    print(len(lista), "Ennyi db kutya van")


def f3():
    count = 0
    x = [] # fajták
    for i in lista:
        if i.fajta not in x:
            x.append(i.fajta)
        else:
            count += 1
    #print(*x)
    #print(count)
    print(len(x), "Ennyi kutya fajta van a listába")


def f4():
    x = 0
    for i in lista:
        if x < i.eletkor:
            x = i.eletkor
    print(x)





def main():
    f1()
    f2()
    f3()


main()