#Problema 1:
#Pentru listă de monede cu valorile a1,....,an, și o valoare S. Tipăriţi toate modalităţile de aplăti suma S
#cu monedele disponibile. Tipăriți un mesaj dacă suma nu se poate plăti.


"""
Solutie candidat:
    x=(x0,x1,x2,..,xk),xi din (0,1,...,n-1), xi<=xj, oricare ar fi i<=j
Conditie consistent:
    x=(x0,x1,x2,...,xk) este consistent daca suma valorilor monezilor reprezentate de indici xi (monezi[xi]) este mai mica sau egala cu suma data
Conditie solutie:
    x=(x0,x1,x2,...,xk) este solutie daca suma valorilor monezilor reprezentate de indici xi (monezi[xi]) este egala ca suma data
---------------------
M={m0,m1,...,mn)
Solutie candidat:
    x=(x0,x1,x2,..,xk),xi din M, indicele monedei xi in M <= indicele monedei xj in M, oricare ar fi i<=j
Conditie consistent:
    x=(x0,x1,x2,...,xk) este consistent daca suma valorilor xi este mai mica sau egala cu suma data
Conditie solutie:
    x=(x0,x1,x2,...,xk) este consistent daca suma valorilor xi este egala ca suma data
"""

def calcul_suma(candidat,monezi):
    S=0
    for i in range(0,len(candidat)):
        S+=monezi[candidat[i]]
    return S

def candidat_prim():
    return [-1]

def extinde(candidat):
    candidat.append(candidat[-1]-1)

def urmator(candidat,n):
    candidat[-1]+=1
    return candidat[-1]<n

def consistent(candidat,monezi,suma):
    return calcul_suma(candidat,monezi)<=suma

def solutie(candidat,monezi,suma):
    return calcul_suma(candidat,monezi)==suma

def backtrack(candidat):
    candidat.pop()

def output(candidat,monezi,ok):
    if(ok==0):
        print("Suma se poate scrie in urmatoarele modalitati:")
    for i in range(0,len(candidat)-1):
        print(monezi[candidat[i]],end="+")
    print(monezi[candidat[-1]])

def generare_modalitati_plata_iterativ(monezi,suma):
    candidat=candidat_prim()
    ok=0
    while(len(candidat)>0):
        if(not urmator(candidat,len(monezi))):
            backtrack(candidat)
        elif(consistent(candidat,monezi,suma)):
            if(solutie(candidat,monezi,suma)):
                output(candidat,monezi,ok)
                ok=1
            else:
                extinde(candidat)
    if(ok==0):
        print("Nu exista modalitati de a scrie aceasta suma folosind monezile date.")
    else:
        print("Sfarsitul generari de modalitati de scriere a sumei.")

def modalitate_recursiva(candidat,monezi,suma,ok):
    while(urmator(candidat,len(monezi))):
        if(consistent(candidat,monezi,suma)):
            if(solutie(candidat,monezi,suma)):
                output(candidat,monezi,ok)
                ok=1
            else:
                extinde(candidat)
                ok=modalitate_recursiva(candidat,monezi,suma,ok)
    backtrack(candidat)
    return ok

def generare_modalitati_plata_recursiv(monezi,suma):
    candidat=candidat_prim()
    ok=modalitate_recursiva(candidat,monezi,suma,0)
    if(ok==0):
        print("Nu exista modalitati de a scrie aceasta suma folosind monezile date.")
    else:
        print("Sfarsitul generari de modalitati de scriere a sumei.")

generare_modalitati_plata_iterativ([1,3,5],7)
print("--------------------------------------------------------------------------------")
generare_modalitati_plata_recursiv([1,3,5],7)
print("================================================================================")
generare_modalitati_plata_iterativ([2,3,5],1)
print("--------------------------------------------------------------------------------")
generare_modalitati_plata_recursiv([2,3,5],1)
print("================================================================================")
generare_modalitati_plata_iterativ([5,7,9],11)
print("--------------------------------------------------------------------------------")
generare_modalitati_plata_recursiv([5,7,9],11)
print("================================================================================")
generare_modalitati_plata_iterativ([2,3,4],10)
print("--------------------------------------------------------------------------------")
generare_modalitati_plata_recursiv([2,3,4],10)
print("================================================================================")
