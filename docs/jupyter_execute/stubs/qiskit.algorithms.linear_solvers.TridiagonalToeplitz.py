#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from qiskit import QuantumCircuit
from qiskit.algorithms.linear_solvers.matrices import TridiagonalToeplitz

matrix = TridiagonalToeplitz(2, 1, -1 / 3)
power = 3

# Controlled power (as within QPE)
num_qubits = matrix.num_state_qubits
pow_circ = matrix.power(power).control()
circ_qubits = pow_circ.num_qubits
qc = QuantumCircuit(circ_qubits)
qc.append(matrix.power(power).control(), list(range(circ_qubits)))

