import random
import numpy as np
import pulp
import time
from ortools.sat.python import cp_model

def estimate_solutions(n, m, CM, samples=100000000):
    """Szybka estymacja przez losowe próbkowanie."""
    start_time = time.time()
    valid = 0
    for _ in range(samples):
        assignment = [random.randint(1, m) for _ in range(n)]
        if not has_conflicts(assignment, CM, n, m):
            valid += 1
    estimated = (valid / samples) * (m ** n)
    print(f"Szacowana liczba rozwiązań: ~{int(estimated)}")
    elapsed_time = time.time() - start_time  # Oblicz czas wykonania
    print(f"Czas wykonania: {elapsed_time:.2f} sekund")
    return estimated

def has_conflicts(assignment, CM, n, m):
    """Sprawdź, czy przypisanie powoduje konflikty."""
    for i in range(n):
        for j in range(i + 1, n):
            if CM[i * m + assignment[i] - 1][j * m + assignment[j] - 1] == 1:
                return True
    return False

def solve_airplane_conflict(n, m, CM, cost):
    # Stwórz problem optymalizacyjny
    model = pulp.LpProblem("Airplane_Conflict_Resolution", pulp.LpMinimize)

    # Stwórz zmienne binarne x_i_j
    variables = pulp.LpVariable.dicts("x",
                                      [(i, j) for i in range(1, n + 1) for j in range(1, m + 1)],
                                      cat='Binary')

    # Funkcja celu: minimalizacja całkowitego kosztu
    model += pulp.lpSum([variables[(i, j)] * cost[j - 1]
                         for i in range(1, n + 1) for j in range(1, m + 1)])

    # Każdy samolot musi wybrać dokładnie jeden manewr
    for i in range(1, n + 1):
        model += pulp.lpSum([variables[(i, j)] for j in range(1, m + 1)]) == 1

    # Ograniczenia dotyczące unikania konfliktów
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            for k in range(i, n + 1):
                start_l = j + 1 if k == i else 1
                for l in range(start_l, m + 1):
                    if CM[(i - 1) * m + j - 1][(k - 1) * m + l - 1] == 1:
                        model += variables[(i, j)] + variables[(k, l)] <= 1

    # Rozwiąż problem
    model.solve()

    # Wypisz status rozwiązania
    print("Status:", pulp.LpStatus[model.status])

    # Wypisz wybrane manewry dla każdego samolotu
    solution = np.zeros((n, m))
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if pulp.value(variables[(i, j)]) == 1:
                print(f"Samolot {i} wykonuje manewr {j}")
                solution[i - 1, j - 1] = 1

    return solution

# Przykład użycia
n = 40
CM = np.loadtxt('data/CM_n='+str(n)+'_m=7.txt')
m = 7
cost = [i + 1 for i in range(m)]
solution = solve_airplane_conflict(n, m, CM, cost)
#estimate_solutions(n, m, CM)

print("\nMacierz rozwiązania:")
#print(solution)
