#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from qiskit import QuantumCircuit
from qiskit.circuit.library.arithmetic.piecewise_chebyshev import PiecewiseChebyshev
f_x, degree, breakpoints, num_state_qubits = lambda x: np.arcsin(1 / x), 2, [2, 4], 2
pw_approximation = PiecewiseChebyshev(f_x, degree, breakpoints, num_state_qubits)
pw_approximation._build()
qc = QuantumCircuit(pw_approximation.num_qubits)
qc.h(list(range(num_state_qubits)))
qc.append(pw_approximation.to_instruction(), qc.qubits)
qc.draw(output='mpl')

