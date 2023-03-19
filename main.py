import time
import random
import unittest
with open("teste.txt",'r') as f:
    n=int(f.readline())
    Lista=[]
    for i in range(n):
        Lista.append(f.readline().split(sep=' '))
    for i in range(len(Lista)):
        Lista[i][0]=int(Lista[i][0])
        Lista[i][1].replace("\n",'')
        Lista[i][1]=int(Lista[i][1])
    print(Lista)
L=[]
aux=int(input("Test:"))
for i in range(int(Lista[aux][0])):
    x=random.randint(0,int(Lista[aux][1]))
    L.append(x)
L1=L.copy()
L2=L.copy()
L3=L.copy()
L4=L.copy()
L5=L.copy()

def test_sort(v):
    for i in range(len(v)-1):
        if v[i]>v[i+1]:
            return False
    return True

def heapify(vector, n, i):
    maxim = i
    stanga = 2 * i + 1
    dreapta = 2 * i + 2
    
    if stanga < n and vector[i] < vector[stanga]:
        maxim = stanga
    
    if dreapta < n and vector[maxim] < vector[dreapta]:
        maxim = dreapta
        
    if maxim != i:
        vector[i], vector[maxim] = vector[maxim], vector[i]
        heapify(vector, n, maxim)
        
def heap_sort(vector):
    n = len(vector)
    
    for i in range(n // 2 - 1, -1, -1):
        heapify(vector, n, i)
        
    for i in range(n - 1, 0, -1):
        vector[0], vector[i] = vector[i], vector[0]
        heapify(vector, i, 0)
        
    return vector
start_time1=time.time()
heap_sort(L1)
end_time1=time.time()
elapsed_time1=end_time1-start_time1

def counting_sort(vector, x):
    nr_aparitii = [0] * 10
    out = [0] * len(vector)

    for num in vector:
        digit = (num // x) % 10
        nr_aparitii[digit] += 1

    for i in range(1, 10):
        nr_aparitii[i] += nr_aparitii[i-1]
        
    for i in range(len(vector)-1, -1, -1):
        digit = (vector[i] // x) % 10
        out[nr_aparitii[digit]-1] = vector[i]
        nr_aparitii[digit] -= 1

    return out
        
def radix_sort(vector):
    nr_maxim_vector = len(str(max(vector)))
    
    for x in range(1, 10**nr_maxim_vector):
        vector = counting_sort(vector, x)
    
    return vector


start_time2=time.time()
radix_sort(L2)
end_time2=time.time()
elapsed_time2=end_time2-start_time2

def merge_sort(vector):
    if len(vector) <= 1:
        return vector
    
    mijloc = len(vector) // 2
    partea_s = merge_sort(vector[:mijloc])
    partea_d = merge_sort(vector[mijloc:])
    

    vector_unit = []
    i = j = 0
    while i < len(partea_s) and j < len(partea_d):
        if partea_s[i] < partea_d[j]:
            vector_unit.append(partea_s[i])
            i += 1
        else:
            vector_unit.append(partea_d[j])
            j += 1
    vector_unit += partea_s[i:]
    vector_unit += partea_d[j:]
    

    return vector_unit

start_time3=time.time()
merge_sort(L3)
end_time3=time.time()
elapsed_time1=end_time1-start_time3

def shell_sort(vector):

    n = len(vector)
    interval = n // 2
    

    while interval > 0:

        for i in range(interval, n):
            temporar = vector[i]
            j = i
            
            while j >= interval and vector[j - interval] > temporar:
                vector[j] = vector[j - interval]
                j -= interval
            
            vector[j] = temporar
        
        interval //= 2
    
    return vector

start_time4=time.time()
shell_sort(L4)
end_time4=time.time()
elapsed_time4=end_time4-start_time4

def bubble_sort(vector):
    lungime_vector = len(vector)
    for i in range(lungime_vector):
        for j in range(0, lungime_vector-i-1):
            if vector[j] > vector[j+1]:
                vector[j], vector[j+1] = vector[j+1], vector[j]
    return vector



start_time5=time.time()
bubble_sort(L5)
end_time5=time.time()
elapsed_time5=end_time5-start_time5