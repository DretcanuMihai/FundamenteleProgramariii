def binary_search(element,lista,st,dr):
    if(dr-st<=1):
        if(element==lista[dr]):
            return dr
        if(element==lista[st]):
            return st
        return -1
    mid=(st+dr)//2
    if(lista[mid]==element):
        return mid
    if(element<lista[mid]):
        return binary_search(element,lista,st,mid-1)
    else:
        return binary_search(element,lista,mid+1,dr)

def search(element,lista):
    if(len(lista)==0):
        return -1
    return binary_search(element,lista,0,len(lista))

print(search(6,[1,2,3,4,5,6,7,8,9,10]))
