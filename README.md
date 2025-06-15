# Geographical information systems Project Repository

## 📋 Problem Description  
This project addresses the problem of resolving conflicts between airplanes in airspace by assigning optimal maneuvers to each aircraft. The goal is to **minimize the total cost of maneuvers** while ensuring **no conflicts occur** between any two aircraft.  

---

## 🧩 Key Components  

###  1. Problem Formulation  
- **Inputs**:  
  - `n`: Number of airplanes  
  - `m`: Number of available maneuvers per airplane  
  - `CM`: Conflict Matrix (binary matrix indicating conflicts between maneuver pairs)  
  - `cost`: Cost associated with each maneuver  

- **Output**:  
  - An optimal assignment of maneuvers to airplanes that avoids all conflicts at minimal cost  

###  2. Solution Approach  
The problem is solved using **Integer Linear Programming (ILP)** with the `PuLP` library. The solution:  
1. Creates binary decision variables for each airplane-maneuver pair  
2. Sets constraints to ensure:  
   - Each airplane selects exactly one maneuver
   - No conflicting maneuvers are assigned to any two airplanes
3. Minimizes the total cost of selected maneuvers

###  3. Solution Estimation  
An additional function `estimate_solutions()` provides a **Monte Carlo estimation** of the total number of valid solutions by random sampling.  

---

## 📂 Implementation Files  

1. **`main.py`** - Contains:  
   - `solve_airplane_conflict()`: Main optimization function  
   - `estimate_solutions()`: Solution space estimation function  
   - `has_conflicts()`: Helper function for conflict detection  

2. **`konflikty_vs_n.png`** - Graph showing:  
   - Number of conflicts vs. number of airplanes
   - Demonstrates how problem complexity scales with fleet size  

3. **`czas_vs_n.png`** - Graph showing:  
   - Solution time vs. number of airplanes
   - Illustrates computational complexity of the problem 

---

## 🚀 Usage  

1. **Prepare input files**:  
   - Conflict matrix (`CM`) as a text file in `data/CM_n=X_m=Y.txt`  
   - Define maneuver costs  

2. **Run the solver**:  
   ```python
   n = 40  # Number of airplanes  
   m = 7   # Number of maneuvers  
   CM = np.loadtxt('data/CM_n='+str(n)+'_m=7.txt')  
   cost = [i + 1 for i in range(m)]  # Example cost array  
   solution = solve_airplane_conflict(n, m, CM, cost)  
   ```

3. **For solution space estimation**:  
   ```python
   estimate_solutions(n, m, CM)  
   ```

---

## 📊 Results Interpretation  
- The solver outputs:  
  - Status of the solution (`Optimal`/`Infeasible`)  
  - Selected maneuvers for each airplane
  - Total computation time
- The estimation function provides:
  - Approximate number of valid solutions
  - Time taken for estimation 

---

## 📦 Dependencies  
- Python 3.x
- NumPy
- PuLP
- OR-Tools (for CP-SAT solver)
- Matplotlib (for visualization)

---

## 🎓 Course Relevance  
This project demonstrates the application of **optimization techniques** in **Geographical Information Systems**, particularly for:  
- Air traffic management
- Spatial conflict resolution
- Resource allocation in constrained environments
- Computational geometry applicationss

The implementation shows how **mathematical programming** can solve complex spatial problems in transportation networks.  

--- 

### Course: Geographical information systems
### Institution: Poznań University of Technology
