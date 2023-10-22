def cautare_succesiva(element,lista):
    poz=0
    while(poz<len(lista) and lista[poz]!=element):
        poz=poz+1
    if(poz<len(l)):
        return poz
    return -1
