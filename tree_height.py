# 221RDB119 Artis Ozols 12.gr

import sys
import threading
import numpy

def height(n, vec):
    max_height = 0
    list = []
    chl = {i:[] for i in range(0, n)}
    
    for i, a in enumerate(vec):
        if a == -1:
            list.append(i)
        else:
            chl[a].append(i)

    def get_dzl(node, dzl): 
        max_dzl=0  
        if not chl[node]:
            return dzl
        else:
            for b in chl[node]:
                chl_dzl = get_dzl(b, dzl+1)
                max_dzl = max(max_dzl, chl_dzl)
            return max_dzl
        
    for root in list:
        height = get_dzl(root, 0)
        max_height = max(max_height, height)
    return (max_height+1)

def main():
    izvele = input()
    
    if izvele == "I":
        n = int(input())
        vec = list(map(int, input().split()))
        print(height(n, vec))
        
    if izvele == "F":
        filename = ("test/" + input())
        if filename.__contains__('a')==False:
            with open(filename, mode ='r') as filename:
                return filename.read()

sys.setrecursionlimit(10**7)
threading.stack_size(2**27)
threading.Thread(target=main).start()
