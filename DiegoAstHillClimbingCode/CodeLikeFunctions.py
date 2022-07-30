from time import time
from Funciones import *
import time

### Mas informacion de los codigos en main.py

def codigo111(n: int, m: int, calificaciones: list, horas: list):
    tiempo = time.time()
    p_solution = New_p_solution(n, m, 1, calificaciones, horas)
    if p_solution == False:
        return -1, -1
    best_value = fo(calificaciones,p_solution)
    new_solution, value = new_vecino1_masmejor(p_solution, m, horas, calificaciones, best_value)
    while value > best_value:
        best_value = value
        new_solution, value = new_vecino1_masmejor(new_solution, m, horas, calificaciones, value)
    return time.time()-tiempo, best_value

def codigo112(n: int, m: int, calificaciones: list, horas: list):
    tiempo = time.time()
    p_solution = New_p_solution(n, m, 1, calificaciones, horas)
    if p_solution == False:
        return -1, -1
    best_value = fo(calificaciones,p_solution)
    new_solution, value = new_vecino1_primeromejor(p_solution, m, horas, calificaciones, best_value)
    while value > best_value:
        best_value = value
        new_solution, value = new_vecino1_primeromejor(new_solution, m, horas, calificaciones, value)
    return time.time()-tiempo, best_value

def codigo121(n: int, m: int, calificaciones: list, horas: list):
    tiempo = time.time()
    p_solution = New_p_solution(n, m, 1, calificaciones, horas)
    if p_solution == False:
        return -1, -1
    best_value = fo(calificaciones,p_solution)
    new_solution, value = new_vecino2_masmejor(p_solution, m, horas, calificaciones, best_value)
    while value > best_value:
        best_value = value
        new_solution, value = new_vecino2_masmejor(new_solution, m, horas, calificaciones, value)
    return time.time()-tiempo, best_value

def codigo221(n: int, m: int, calificaciones: list, horas: list):
    tiempo = time.time()
    p_solution = New_p_solution(n, m, 10, calificaciones, horas)
    if p_solution == False:
        return -1, -1
    best_value = fo(calificaciones,p_solution)
    new_solution, value = new_vecino2_masmejor(p_solution, m, horas, calificaciones, best_value)
    while value > best_value:
        best_value = value
        new_solution, value = new_vecino2_masmejor(new_solution, m, horas, calificaciones, value)
    return time.time()-tiempo, best_value

def codigo211(n: int, m: int, calificaciones: list, horas: list):
    tiempo = time.time()
    p_solution = New_p_solution(n, m, 10, calificaciones, horas)
    if p_solution == False:
        return -1, -1
    best_value = fo(calificaciones,p_solution)
    new_solution, value = new_vecino1_masmejor(p_solution, m, horas, calificaciones, best_value)
    while value > best_value:
        best_value = value
        new_solution, value = new_vecino1_masmejor(new_solution, m, horas, calificaciones, value)
    return time.time()-tiempo, best_value

def codigo222(n: int, m: int, calificaciones: list, horas: list):
    tiempo = time.time()
    p_solution = New_p_solution(n, m, 10, calificaciones, horas)
    if p_solution == False:
        return -1, -1
    best_value = fo(calificaciones,p_solution)
    new_solution, value = new_vecino2_primeromejor(p_solution, m, horas, calificaciones, best_value)
    while value > best_value:
        best_value = value
        new_solution, value = new_vecino2_primeromejor(new_solution, m, horas, calificaciones, value)
    return time.time()-tiempo, best_value