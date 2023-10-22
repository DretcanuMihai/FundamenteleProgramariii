def quick_sort(lista,st,dr):
    if(dr-st<=0):
        return
    mid=(st+dr)//2
    lista[mid],lista[dr]=lista[dr],lista[mid]
    pivot=lista[dr]
    poz=st
    for j in range(st,dr):
        if(lista[j]<pivot):
            lista[j],lista[poz]=lista[poz],lista[j]
            poz=poz+1
    lista[dr],lista[poz]=lista[poz],lista[dr]
    quick_sort(lista,st,poz-1)
    quick_sort(lista,poz+1,dr)
    

def sort(lista):
    if(len(lista)==0):
        return
    quick_sort(lista,0,len(lista)-1)

lista=[1,5,7,2,3,9,0,8,4,6]
sort(lista)
print(lista)
