#!/usr/bin/env python
# coding: utf-8

# In[1]:


from qiskit.visualization import plot_coupling_map
get_ipython().run_line_magic('matplotlib', 'inline')

num_qubits = 8
coupling_map = [[0, 1], [1, 2], [2, 3], [3, 5], [4, 5], [5, 6], [2, 4], [6, 7]]
qubit_coordinates = [[0, 1], [1, 1], [1, 0], [1, 2], [2, 0], [2, 2], [2, 1], [3, 1]]
plot_coupling_map(num_qubits, coupling_map, qubit_coordinates)

