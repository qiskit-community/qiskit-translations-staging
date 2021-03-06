#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
from qiskit.pulse.library import triangle
import numpy as np

duration = 100
amp = 1
freq = 1 / duration
triangle_wave = np.real(triangle(duration, amp, freq).samples)
plt.plot(range(duration), triangle_wave)

