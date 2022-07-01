#!/usr/bin/env python
# coding: utf-8

# In[1]:


from qiskit.opflow import X, Z, Zero
from qiskit.algorithms import EvolutionProblem, TrotterQRTE
from qiskit import BasicAer
from qiskit.utils import QuantumInstance

operator = X + Z
initial_state = Zero
time = 1
evolution_problem = EvolutionProblem(operator, 1, initial_state)
# LieTrotter with 1 rep
backend = BasicAer.get_backend("statevector_simulator")
quantum_instance = QuantumInstance(backend=backend)
trotter_qrte = TrotterQRTE(quantum_instance=quantum_instance)
evolved_state = trotter_qrte.evolve(evolution_problem).evolved_state

