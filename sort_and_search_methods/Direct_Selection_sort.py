def selection_sort(lista):
    for i in range(0,len(lista)-1):
        for j in range(i+1,len(lista)):
            if(lista[i]>lista[j]):
                lista[i],lista[j]=lista[j],lista[i]

lista=[1,5,7,2,3,9,0,8,4,6]
selection_sort(lista)
print(lista)
