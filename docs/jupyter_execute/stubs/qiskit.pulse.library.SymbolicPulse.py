#!/usr/bin/env python
# coding: utf-8

# In[1]:


from qiskit.pulse.library import SymbolicPulse

my_pulse = SymbolicPulse(
    pulse_type="Sawtooth",
    duration=100,
    parameters={"amp": 0.1, "freq": 0.05},
    name="pulse1",
)


# In[2]:


import sympy

t, amp, freq = sympy.symbols("t, amp, freq")
envelope = 2 * amp * (freq * t - sympy.floor(1 / 2 + freq * t))

my_pulse = SymbolicPulse(
    pulse_type="Sawtooth",
    duration=100,
    parameters={"amp": 0.1, "freq": 0.05},
    envelope=envelope,
    name="pulse1",
)

my_pulse.draw()

