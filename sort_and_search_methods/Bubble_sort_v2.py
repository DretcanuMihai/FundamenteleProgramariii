def bubble_sort(lista):
    for i in range(1,len(lista)):
        for j in range(0,len(lista)-i):
            if(lista[j]>lista[j+1]):
                lista[j],lista[j+1]=lista[j+1],lista[j]

lista=[1,5,7,2,3,9,0,8,4,6]
bubble_sort(lista)
print(lista)
