#!/usr/bin/env python
# coding: utf-8

# In[1]:


from qiskit.quantum_info.operators import PauliList

pt = PauliList(['X', 'Y', '-X', 'I', 'I', 'Z', 'X', 'iZ'])
unique = pt.unique()
print(unique)

