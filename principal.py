import math
import numpy as np
import stl
from stl import mesh
import matplotlib.pyplot as plt



def quicksort(myList, start, end):
    if start < end:
        pivot = partition(myList, start, end)
        quicksort(myList, start, pivot-1)
        quicksort(myList, pivot+1, end)
    return myList

def partition(myList, start, end):
    pivot = myList[start][0]
    left = start+1
    right = end
    done = False
    while not done:
        while left <= right and myList[left][0] <= pivot:
            left = left + 1
        while myList[right][0] >= pivot and right >=left:
            right = right -1
        if right < left:
            done= True
        else:
            temp=myList[left]
            myList[left]=myList[right]
            myList[right]=temp
    temp=myList[start]
    myList[start]=myList[right]
    myList[right]=temp
    return right

def calculo(nl):
    orden = []
    actual = 0
    siguiente = 2
    dist = math.hypot(nl[1][0] - nl[actual][0],nl[1][1] - nl[actual][1])
    pos = 0
    fin = False
    while not fin:
        while siguiente <len(nl)-1:
            if actual != siguiente:
                dist1 = math.hypot(nl[siguiente][0] - nl[actual][0],nl[siguiente][1] - nl[actual][1])
                if  dist1 < dist:
                    pos = siguiente
                dist = dist1
            siguiente+=1

        orden.append(nl[pos])
        nl.remove(nl[actual])
        siguiente = 0
        actual = pos
        dist = 100000
        pos = 0
        if len(nl) == 1:
            orden.append(nl[0])
            fin = True
    nl = []
    inicio = 0
    anterior = 0

    while(inicio <len(orden)):
        if inicio == 0:
            x = orden[inicio][0]
            y = orden[inicio][1]
            nl.append([round(x),round(y)])
            inicio = 1
        else:
            rx = orden[inicio][0] - orden[anterior][0]
            ry = orden[inicio][1] - orden[anterior][1]
            nl.append([round(rx),round(ry)])
            inicio+=1
            anterior+=1
    return nl

def main():
    obj = mesh.Mesh.from_file('cilindro.stl')
    points = []
    for p in obj.points:
        if (p[2] and p[5] and p[8]) <= 0:
            points.append(p)
    coord = []
    for i in points:
        pareja = 1
        minimo = math.sqrt((i[0]-i[3])**2+(i[1]-i[4])**2)
        if math.sqrt((i[0]-i[6])**2+(i[1]-i[7])**2) < minimo:
            minimo =  math.sqrt((i[0]-i[6])**2+(i[1]-i[7])**2)
            pareja = 2
        if math.sqrt((i[3]-i[6])**2+(i[4]-i[7])**2) < minimo:
            pareja = 3
        if pareja == 1:
            coord.append([i[0], i[1]])
            coord.append([i[3], i[4]])
        if pareja == 2:
            coord.append([i[0], i[1]])
            coord.append([i[6], i[7]])
        if pareja == 3:
            coord.append([i[3], i[4]])
            coord.append([i[6], i[7]])

    lsort = quicksort(coord,0,len(coord)-1)

    nl = []
    for elemento in range(0,(len(lsort)-1)):
        if lsort[elemento][0] != lsort[elemento+1][0] and lsort[elemento][1] != lsort[elemento+1][1] :
            nl.append(lsort[elemento])

    orden = calculo(nl)
    return orden




if __name__ == '__main__':
    orden = main()
    #para mostrar los puntos
    maxtime = 0

    for elemento in orden:
        for x in elemento:
            print(x)
            if x > maxtime:
                maxtime = x
    print 1

    """my_points = np.array(orden)
    plt.figure()

    plt.plot(my_points[:,0], my_points[:,1])
    plt.plot(my_points[:,0], my_points[:,1], 'r.')


    plt.show()"""
