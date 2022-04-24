#!/usr/bin/env python
# coding: utf-8

# In[1]:


from qiskit.circuit.library import MCXGate
gate = MCXGate(4)

from qiskit import QuantumCircuit
circuit = QuantumCircuit(5)
circuit.append(gate, [0, 1, 4, 2, 3])
circuit.draw('mpl')


# In[2]:


from qiskit.circuit.library import XGate
gate = XGate()
print(gate.to_matrix())             # X gate
print(gate.power(1/2).to_matrix())  # √X gate
print(gate.control(1).to_matrix())  # CX (controlled X) gate


# In[3]:


from qiskit.circuit.library import Diagonal

diagonal = Diagonal([1, 1])
print(diagonal.num_qubits)

diagonal = Diagonal([1, 1, 1, 1])
print(diagonal.num_qubits)


# In[4]:


from qiskit.circuit.library.templates import template_nct_4b_1
from qiskit.quantum_info import Operator
import numpy as np

template = template_nct_4b_1()

identity = np.identity(2 ** len(template.qubits), dtype=complex)
data = Operator(template).data
np.allclose(data, identity)  # True, template_nct_4b_1 is the identity

