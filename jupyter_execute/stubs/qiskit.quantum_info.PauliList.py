#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np

from qiskit.quantum_info import Pauli, PauliList

# 1. init from list[str]
pauli_list = PauliList(["II", "+ZI", "-iYY"])
print("1. ", pauli_list)

pauli1 = Pauli("iXI")
pauli2 = Pauli("iZZ")

# 2. init from Pauli
print("2. ", PauliList(pauli1))

# 3. init from list[Pauli]
print("3. ", PauliList([pauli1, pauli2]))

# 4. init from np.ndarray
z = np.array([[True, True], [False, False]])
x = np.array([[False, True], [True, False]])
phase = np.array([0, 1])
pauli_list = PauliList.from_symplectic(z, x)
print("4. ", pauli_list)


# In[2]:


pauli_list = PauliList(["XX", "ZZ", "IZ"])
print("Integer: ", repr(pauli_list[1]))
print("List: ", repr(pauli_list[[0, 2]]))
print("Slice: ", repr(pauli_list[0:2]))

