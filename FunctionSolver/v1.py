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
    print(NombresFonction)
    return NombresFonction

def GetDiviseurs(n) :
    ListeDiviseurs = []
    for x in range(1,int(n)+1) :
        if n%x == 0 : 
            ListeDiviseurs.append(n)
            ListeDiviseurs.append(-n)
    return ListeDiviseurs

def CalculFonction(f,n) :
    c = 0
    somme = len(f) - 1
    for x in f : 
        somme += n**c * x
        c -= 1
    return somme

Fonction = DemandeFonctionInitial()
ListeRésultat = []
while len(Fonction) != 3 :
    DiviseursDernierNombre = GetDiviseurs(Fonction[-1])
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

    

