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
    c = len(f)
    for x in f : 
        c -= 1
        somme += x*(n**c)
    return somme

Fonction = [3,-4,-1,-4,5]#DemandeFonctionInitial()
while len(Fonction) != 3 :
    Degré_Actuel = len(Fonction) -1
    ListeRésultat = []
    DernierNombre = Fonction[len(Fonction)-1]
    DiviseursDernierNombre = GetDiviseurs(DernierNombre)
    Diviseurs0 = ""
    for nb in DiviseursDernierNombre :
        if CalculFonction(Fonction,nb) == 0 :
            Diviseurs0 = nb
            ListeRésultat.append(Diviseurs0)
            break
    n = 0
    for x in range(len(Fonction)) :
        n += Fonction[x]
        Fonction.append(n)
        if x == len(Fonction) :
            break
        n = n*Diviseurs0
    for x in range(Degré_Actuel+1) :
        Fonction.remove(Fonction[0])
    Fonction.remove(Fonction[len(Fonction)-1]) 
    print(Fonction)

a = Fonction[0]
b = Fonction[1]
c = Fonction[2]
if (b**2) - 4*a*c == 0 :
    ListeRésultat.append((-b)/(2*a))
if (b**2) - 4*a*c > 0 :
    ListeRésultat.append(((-b)+((b**2)-(4*a*c))**(1/2))/(2*a))
    ListeRésultat.append(((-b)-((b**2)-(4*a*c))**(1/2))/(2*a))
print("Valeurs de x :",ListeRésultat)

    

