def insertion_sort(lista):
    for i in range(1,len(lista)):
        ind=i-1
        a=lista[i]
        while(a<lista[ind]):
            lista[ind+1]=lista[ind]
            ind=ind-1
            if(ind<0):
                break
        lista[ind+1]=a

lista=[1,5,7,2,3,9,0,8,4,6]
insertion_sort(lista)
print(lista)
