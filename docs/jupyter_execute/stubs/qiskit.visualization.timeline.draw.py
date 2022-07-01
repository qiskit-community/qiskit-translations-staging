#!/usr/bin/env python
# coding: utf-8

# In[1]:


from qiskit import QuantumCircuit, transpile, schedule
from qiskit.visualization.timeline import draw
from qiskit.providers.fake_provider import FakeAlmaden

qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0,1)

qc = transpile(qc, FakeAlmaden(), scheduling_method='alap', layout_method='trivial')
draw(qc)


# In[2]:


from qiskit import QuantumCircuit, transpile, schedule
from qiskit.visualization.timeline import draw, IQXSimple
from qiskit.providers.fake_provider import FakeAlmaden

qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0,1)

qc = transpile(qc, FakeAlmaden(), scheduling_method='alap', layout_method='trivial')
draw(qc, style=IQXSimple())


# In[3]:


from qiskit import QuantumCircuit, transpile, schedule
from qiskit.visualization.timeline import draw, IQXDebugging
from qiskit.providers.fake_provider import FakeAlmaden

qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0,1)

qc = transpile(qc, FakeAlmaden(), scheduling_method='alap', layout_method='trivial')
draw(qc, style=IQXDebugging())

