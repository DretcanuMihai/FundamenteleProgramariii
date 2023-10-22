def search(element,lista):
    st=0
    dr=len(lista)-1
    while(dr-st>1):
        mid=(st+dr)//2
        if(lista[mid]==element):
            return mid
        if(element<lista[mid]):
            dr=mid-1
        else:
            st=mid+1
    if(lista[dr]==element):
        return dr
    if(lista[st]==element):
        return st
    return -1

print(search(6,[1,2,3,4,5,6,7,8,9,10]))
