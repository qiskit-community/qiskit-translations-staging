#!/usr/bin/env python
# coding: utf-8

# In[1]:


from qiskit_nature.operators.second_quantization import SpinOp

x = SpinOp("X", spin=3/2)
y = SpinOp("Y", spin=3/2)
z = SpinOp("Z", spin=3/2)


# In[2]:


SpinOp(
    [
        ("XX", -1),
        ("YY", -1),
        ("ZZ", -1),
        ("ZI", -0.3),
        ("IZ", -0.3),
    ],
    spin=1
)


# In[3]:


x + 1j * y


# In[4]:


~(1j * z)

