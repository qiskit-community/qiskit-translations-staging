#!/usr/bin/env python
# coding: utf-8

# In[1]:


from qiskit_nature.problems.second_quantization.lattice import (
    BoundaryCondition,
    HyperCubicLattice,
    )

lattice = HyperCubicLattice(
    size = (3, 4, 5),
    edge_parameter = (1.0, -2.0, 3.0),
    onsite_parameter = 2.0,
    boundary_condition = (BoundaryCondition.OPEN, BoundaryCondition.OPEN, BoundaryCondition.OPEN)
    )

