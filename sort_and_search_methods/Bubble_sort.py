def bubble_sort(lista):
    sortat=False
    while(not sortat):
        sortat=True
        for i in range(0,len(lista)-1):
            if(lista[i]>lista[i+1]):
                lista[i],lista[i+1]=lista[i+1],lista[i]
                sortat=False

lista=[1,5,7,2,3,9,0,8,4,6]
bubble_sort(lista)
print(lista)
