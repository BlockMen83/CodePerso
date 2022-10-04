def DemandeFonctionInitial() :
    NombresFonction = []
    tempo = ""
    print("Remplir les nombres en fonction du degré de x(stop pour arreter) : ")
    c = 0
    while tempo != "stop" :
        tempo = input(f"Degrée {c} : ")
        NombresFonction = [tempo] + NombresFonction
        c += 1
    del NombresFonction[0]
    NombresFonction = list(map(float, NombresFonction))
    return NombresFonction

def GetDiviseurs(n) :
    ListeDiviseurs = []
    for x in range(1,int(abs(n))+1) :
        if n%x == 0 : 
            ListeDiviseurs.append(x)
            ListeDiviseurs.append(-x)
    return ListeDiviseurs

def CalculFonction(f,n) :
    somme = 0
    c = len(f) - 1
    for x in f : 
        print(x)
        print(n)
        somme += x*(n**c)
        c -= 1
        if c == 0 :
            break
    return somme

Fonction = [3.0,-5.0,1.0,-6.0] #DemandeFonctionInitial()
ListeRésultat = []
while len(Fonction) != 3 :
    DernierNombre = Fonction[len(Fonction)-1]
    DiviseursDernierNombre = GetDiviseurs(DernierNombre)
    for n in DiviseursDernierNombre :
        if CalculFonction(Fonction,n) == 0 :
            ListeRésultat.append(n)
            Diviseurs0 = n
            print(Diviseurs0)
    n = 0
    for x in range(len(Fonction)) :
        n = n*Diviseurs0
        n += Fonction[x]
        Fonction.insert(x,n)
    Fonction = Fonction[:-1]

    

