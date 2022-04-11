#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from qiskit import QuantumCircuit
from qiskit.algorithms.linear_solvers.observables.absolute_average import \
AbsoluteAverage
from qiskit.opflow import StateFn

observable = AbsoluteAverage()
vector = [1.0, -2.1, 3.2, -4.3]

init_state = vector / np.linalg.norm(vector)
num_qubits = int(np.log2(len(vector)))

qc = QuantumCircuit(num_qubits)
qc.isometry(init_state, list(range(num_qubits)), None)
qc.append(observable.observable_circuit(num_qubits), list(range(num_qubits)))

# Observable operator
observable_op = observable.observable(num_qubits)
state_vec = (~StateFn(observable_op) @ StateFn(qc)).eval()

# Obtain result
result = observable.post_processing(state_vec, num_qubits)

# Obtain analytical evaluation
exact = observable.evaluate_classically(init_state)

