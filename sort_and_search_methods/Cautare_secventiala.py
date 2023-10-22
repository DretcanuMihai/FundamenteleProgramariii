def cautare_secventiala(element,lista):
    poz=-1
    for i in range(0,len(lista)):
        if(lista[i]==element):
            poz=i
    return poz

print(cautare_secventiala(11,[4,6,1,5,3,11,13,0,1,-1]))
