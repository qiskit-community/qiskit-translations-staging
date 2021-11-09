#!/usr/bin/env python
# coding: utf-8

# In[1]:


from qiskit import QuantumCircuit
from qiskit.quantum_info import StabilizerState, Pauli

# Bell state generation circuit
qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
stab = StabilizerState(qc)

# Print the StabilizerState
print(stab)

# Calculate the StabilizerState measurement probabilities dictionary
print (stab.probabilities_dict())

# Calculate expectation value of the StabilizerState
print (stab.expectation_value(Pauli('ZZ')))

