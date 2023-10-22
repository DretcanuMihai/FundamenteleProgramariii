def merge_sort(lista):
    if(len(lista)<=1):
        return lista
    mid=(len(lista))//2
    l1=merge_sort(lista[0:mid])
    l2=merge_sort(lista[mid:len(lista)])
    p1=0
    p2=0
    i=0
    while(p1<len(l1) and p2<len(l2)):
        if(l1[p1]<=l2[p2]):
            lista[i]=l1[p1]
            p1+=1
        else:
            lista[i]=l2[p2]
            p2+=1
        i+=1
    while(p1<len(l1)):
        lista[i]=l1[p1]
        p1+=1
        i+=1
    while(p2<len(l2)):
        lista[i]=l2[p2]
        p2+=1
        i+=1
    return lista
    

def sort(lista):
    merge_sort(lista)

lista=[1,5,7,2,3,9,0,8,4,6]
sort(lista)
print(lista)
