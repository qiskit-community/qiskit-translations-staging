#!/usr/bin/env python
# coding: utf-8

# In[1]:


from qiskit.circuit.library import GraphState
import qiskit.tools.jupyter
import retworkx as rx
G = rx.generators.cycle_graph(5)
circuit = GraphState(rx.adjacency_matrix(G))
get_ipython().run_line_magic('circuit_library_info', 'circuit')

