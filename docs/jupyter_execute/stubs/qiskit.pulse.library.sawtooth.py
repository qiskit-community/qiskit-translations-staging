#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
from qiskit.pulse.library import sawtooth
import numpy as np

duration = 100
amp = 1
freq = 1 / duration
sawtooth_wave = np.real(sawtooth(duration, amp, freq).samples)
plt.plot(range(duration), sawtooth_wave)

