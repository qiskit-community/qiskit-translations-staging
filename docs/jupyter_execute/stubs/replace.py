#!/usr/bin/env python
# coding: utf-8

# In[1]:


from qiskit import pulse

d0 = pulse.DriveChannel(0)

sched = pulse.Schedule()

old = pulse.Play(pulse.Constant(100, 1.0), d0)
new = pulse.Play(pulse.Constant(100, 0.1), d0)

sched += old

sched = sched.replace(old, new)

assert sched == pulse.Schedule(new)

