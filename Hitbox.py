import pygame, sys, os, random, cv2


def tamanyo_colider(objeto):
    imagen = cv2.imread(objeto)
    ancho, alto, _ = imagen.shape
    arrx=[ancho]
    arry=[alto]
    for i in range(alto):
        for j in range(ancho):
            arrx.append(objeto.x+ancho)
            arry.append(objeto.y+alto)
    return arrx, arry
            
    

def verificar_choque(arrx , arry, arrx2, arry2):
    for i in range(len(arrx)):
        for j in range(len(arrx2)):
            if arrx[i] == arrx2[j] and arry[i] == arry2[j]:
                return True
    return False

def verificar_choque_terreno(arrx, arry, arrxterr,arryterr):
    for i in range(len(arrx)):
        for j in range(len(arrxterr)):
            if arrx[i] == arrxterr[j] and arry[i] == arryterr[j]:
                return True
    return False
