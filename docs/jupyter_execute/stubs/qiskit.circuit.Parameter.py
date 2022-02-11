#!/usr/bin/env python
# coding: utf-8

# In[1]:


from qiskit.circuit import QuantumCircuit, Parameter

# create the parameter
phi = Parameter('phi')
qc = QuantumCircuit(1)

# parameterize the rotation
qc.rx(phi, 0)
qc.draw()

# bind the parameters after circuit to create a bound circuit
bc = qc.bind_parameters({phi: 3.14})
bc.measure_all()
bc.draw()

