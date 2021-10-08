#!/usr/bin/env python
# coding: utf-8

# In[1]:


from qiskit import QuantumCircuit
from qiskit.transpiler.passes import RemoveBarriers

circuit = QuantumCircuit(1)
circuit.x(0)
circuit.barrier()
circuit.h(0)

circuit = RemoveBarriers()(circuit)
circuit.draw()

