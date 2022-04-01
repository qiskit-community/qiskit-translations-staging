#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from qiskit import QuantumCircuit
from qiskit.algorithms.linear_solvers.observables.matrix_functional import             MatrixFunctional
from qiskit.transpiler.passes import RemoveResetInZeroState
from qiskit.opflow import StateFn

tpass = RemoveResetInZeroState()

vector = [1.0, -2.1, 3.2, -4.3]
observable = MatrixFunctional(1, -1 / 3)

init_state = vector / np.linalg.norm(vector)
num_qubits = int(np.log2(len(vector)))

# Get observable circuits
obs_circuits = observable.observable_circuit(num_qubits)
qcs = []
for obs_circ in obs_circuits:
    qc = QuantumCircuit(num_qubits)
    qc.isometry(init_state, list(range(num_qubits)), None)
    qc.append(obs_circ, list(range(num_qubits)))
    qcs.append(tpass(qc.decompose()))

# Get observables
observable_ops = observable.observable(num_qubits)
state_vecs = []
# First is the norm
state_vecs.append((~StateFn(observable_ops[0]) @ StateFn(qcs[0])).eval())
for i in range(1, len(observable_ops), 2):
    state_vecs += [(~StateFn(observable_ops[i]) @ StateFn(qcs[i])).eval(),
                   (~StateFn(observable_ops[i + 1]) @ StateFn(qcs[i + 1])).eval()]

# Obtain result
result = observable.post_processing(state_vecs, num_qubits)

# Obtain analytical evaluation
exact = observable.evaluate_classically(init_state)

