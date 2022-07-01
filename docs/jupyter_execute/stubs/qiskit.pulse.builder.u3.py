#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math

from qiskit import pulse
from qiskit.providers.fake_provider import FakeOpenPulse2Q

backend = FakeOpenPulse2Q()

with pulse.build(backend) as pulse_prog:
    pulse.u3(math.pi, 0, math.pi, 1)

