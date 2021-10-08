#!/usr/bin/env python
# coding: utf-8

# In[1]:


from qiskit import pulse
from qiskit.pulse import transforms

d0 = pulse.DriveChannel(0)
m0 = pulse.MeasureChannel(0)
a0 = pulse.AcquireChannel(0)
mem0 = pulse.MemorySlot(0)

sched = pulse.Schedule()
sched.append(pulse.Play(pulse.Constant(10, 0.5), d0), inplace=True)
sched.append(pulse.Play(pulse.Constant(10, 1.), m0).shift(sched.duration), inplace=True)
sched.append(pulse.Acquire(20, a0, mem0).shift(sched.duration), inplace=True)

sched_shifted = sched << 20

aligned_sched, aligned_sched_shifted = transforms.align_measures([sched, sched_shifted])

assert aligned_sched == aligned_sched_shifted


# In[2]:


aligned_sched, aligned_sched_shifted = transforms.align_measures(
    [sched, sched_shifted],
    align_all=False,
)

assert aligned_sched != aligned_sched_shifted

