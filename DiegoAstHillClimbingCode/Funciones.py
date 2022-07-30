
# Calcular valor de la funcion objetivo dada la solucion
def fo(Calificaciones,solution):
    sum = 0
    for j in range(len(solution)):
        sum+= Calificaciones[solution[j]][j]
    return sum/len(solution)

# Verificar la factibilidad de la solucion
def Verify(A, horas_ayud):
    # Checkeo rapido
    if -1 in A:
        return False
    horas = []
    aux = []
    # Por cada ayudantia
    for ayudantia in range(len(A)):
        # Si un estudiante tiene mas de 3 ayudantias, la solucion no es factible
        if A.count(A[ayudantia])>=3:
            return False
        # Este sistema cuenta las horas de cada estudiante
        if A[ayudantia] not in aux:
            aux.append(A[ayudantia])
            horas.append(horas_ayud[ayudantia])
        # Suma las horas que tiene cada esutidnate
        else:
            horas[aux.index(A[ayudantia])]+=horas_ayud[ayudantia]
            # Si el estudiante tiene mas de 15 horas, entonces la solucion no es factible
            if horas[aux.index(A[ayudantia])]>15:
                return False
    return True

# Crear solucion inicial segun p - criterio
def New_p_solution(n: int, m: int, p: int, calification, Hours):
    """Return a p-initial solution"""
    solution=[]
    for ayudantia in range(n):
        solution.append(-1)
    # Primera vuelta con valor p, busca el primer estudiante que califique alguna ayudantia con valor mayor o igual a p 
    for row in range(m):
        if -1 not in solution:
            break
        for column in range(n):
            if calification[row][column]>= p and solution[column] == -1:
                solution[column] = row
                break
    if Verify(solution, Hours):
        return solution
    # Segunda vuelta con p = 1
    for row in range(m):
        for column in range(n):
            # Estudiante presenta calificacion mayor o igual a 1 y la ayudantia no se encuentra asignada a nadie
            if calification[row][column] >= 1 and solution[column] == -1:
                # Si el estudiante no tiene ayudantia asignada, se la asigna inmediatamente
                if solution.count(row)==0:
                    solution[column]=row
                # Si ya tenia una ayudantia antes, prueba factibilidad en las horas totales
                elif Hours[solution.index(row)]+Hours[column]<=15:
                    solution[column]=row
                    break
    # Verifica la solucion encontrada
    if Verify(solution, Hours):
        return solution
    else: return False

## Siguiente vecino

def new_vecino1_masmejor(p_solution, m: int, Horas, Calificaciones, best_value):
    best_solution=p_solution.copy()
    # Por cada coordenada
    for k in range(len(p_solution)):
        # Para cada estudiante
        for j in range(m):
            aux_solution=p_solution.copy()
            # Existe permutacion
            # Si el estudiante tiene asignada una ayudantia
            if j in p_solution:
                j=p_solution.index(j)
                aux=aux_solution[j]
                aux_solution[j]=aux_solution[k]
                aux_solution[k]=aux
            else:
                aux_solution[k]=j
            # Si la solucion es factible
            if Verify(aux_solution, Horas):
                aux_value=fo(Calificaciones, aux_solution)
                # Si es factible y tiene un valor mayor a la mejor actual, se convierte en la mejor
                if aux_value>=best_value:
                    best_solution=aux_solution.copy()
                    best_value=aux_value
    return best_solution, best_value

def new_vecino1_primeromejor(p_solution, m: int, Horas, Calificaciones, best_value):
    best_solution=p_solution.copy()
    # Por cada coordenada
    for k in range(len(p_solution)):
        # Para cada estudiante
        for j in range(m):
            aux_solution=p_solution.copy()
            # Existe permutacion
            # Si el estudiante tiene asignada una ayudantia
            if j in p_solution:
                j=p_solution.index(j)
                aux=aux_solution[j]
                aux_solution[j]=aux_solution[k]
                aux_solution[k]=aux
            else:
                aux_solution[k]=j
            # Si la solucion es factible
            if Verify(aux_solution, Horas):
                aux_value=fo(Calificaciones, aux_solution)
                # Si es factible y tiene un valor mayor a la mejor actual, se convierte en la mejor y la devuelve de inmediato
                if aux_value>best_value:
                    best_solution=aux_solution.copy()
                    best_value=aux_value
                    return best_solution, best_value
    return best_solution, best_value

def new_vecino2_masmejor(p_solution, m: int, Horas, Calificaciones, best_value):
    best_solution=p_solution.copy()
    # Por cada coordenada
    for k in range(len(p_solution)):
        # Para cada estudiante
        for j in range(m):
            aux_solution=p_solution.copy()
            # No existe permutacion
            aux_solution[k]=j
            # Si la solucion es factible
            if Verify(aux_solution, Horas):
                aux_value=fo(Calificaciones, aux_solution)
                # Si es factible y tiene un valor mayor a la mejor actual, se convierte en la mejor
                if aux_value>best_value:
                    best_solution=aux_solution.copy()
                    best_value=aux_value
    return best_solution, best_value

def new_vecino2_primeromejor(p_solution, m: int, Horas, Calificaciones, best_value):
    best_solution=p_solution.copy()
    # Por cada coordenada
    for k in range(len(p_solution)):
        # Para cada estudiante
        for j in range(m):
            aux_solution=p_solution.copy()
            #  No existe permutacion
            aux_solution[k]=j
            # Si la solucion es factible
            if Verify(aux_solution, Horas):
                aux_value=fo(Calificaciones, aux_solution)
                # Si es factible y tiene un valor mayor a la mejor actual, se convierte en la mejor y la devuelve de inmediato
                if aux_value>best_value:
                    best_solution=aux_solution.copy()
                    best_value=aux_value
                    return best_solution, best_value
    return best_solution, best_value