def quick_sort(lista,st,dr):
    if(dr-st<=0):
        return
    mid=(st+dr)//2
    pivot=lista[mid]
    st_a=st
    dr_a=dr
    while(st_a<dr_a):
        while(lista[st_a]<pivot and st_a<dr_a):
            st_a+=1
        while(pivot<lista[dr_a] and st_a<dr_a):
            dr_a-=1
        if(st_a<dr_a):
            lista[st_a],lista[dr_a]=lista[dr_a],lista[st_a]
            if(lista[st_a]==lista[dr_a]):
                st_a+=1
    quick_sort(lista,st,st_a-1)
    quick_sort(lista,dr_a+1,dr)
    

def sort(lista):
    if(len(lista)==0):
        return
    quick_sort(lista,0,len(lista)-1)

lista=[1,5,7,2,3,9,0,8,4,6]
sort(lista)
print(lista)
