#!/usr/bin/env python
# coding: utf-8

# In[1]:


from qiskit_nature.operators.second_quantization import FermionicOp

print("truncated str output")
print(sum(FermionicOp("I", display_format="sparse") for _ in range(25)))

FermionicOp.set_truncation(0)
print("not truncated str output")
print(sum(FermionicOp("I", display_format="sparse") for _ in range(25)))


# In[2]:


0.5 * FermionicOp("I+", display_format="dense") + FermionicOp("+I", display_format="dense")


# In[3]:


0.25 * sum(FermionicOp(label, display_format="sparse") for label in ['+_0', '-_1', 'N_2'])


# In[4]:


print(FermionicOp("+-", display_format="dense") @ FermionicOp("E+", display_format="dense"))


# In[5]:


~FermionicOp("+", display_format="dense")

