#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from qiskit import QuantumCircuit
from qiskit.algorithms.linear_solvers.matrices.numpy_matrix import NumPyMatrix

matrix = NumPyMatrix(np.array([[1 / 2, 1 / 6, 0, 0], [1 / 6, 1 / 2, 1 / 6, 0],
                   [0, 1 / 6, 1 / 2, 1 / 6], [0, 0, 1 / 6, 1 / 2]]))
power = 2

num_qubits = matrix.num_state_qubits
# Controlled power (as used within QPE)
pow_circ = matrix.power(power).control()
circ_qubits = pow_circ.num_qubits
qc = QuantumCircuit(circ_qubits)
qc.append(matrix.power(power).control(), list(range(circ_qubits)))

