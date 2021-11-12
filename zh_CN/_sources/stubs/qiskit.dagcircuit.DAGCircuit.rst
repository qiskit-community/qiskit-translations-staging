﻿DAGCircuit
==========

.. currentmodule:: qiskit.dagcircuit

.. autoclass:: DAGCircuit
   :no-members:
   :show-inheritance:

   .. rubric:: Methods

   .. autosummary::
      :nosignatures:
      :toctree: ../stubs/

      ~DAGCircuit.add_calibration
      ~DAGCircuit.add_clbits
      ~DAGCircuit.add_creg
      ~DAGCircuit.add_qreg
      ~DAGCircuit.add_qubits
      ~DAGCircuit.ancestors
      ~DAGCircuit.apply_operation_back
      ~DAGCircuit.apply_operation_front
      ~DAGCircuit.bfs_successors
      ~DAGCircuit.collect_1q_runs
      ~DAGCircuit.collect_runs
      ~DAGCircuit.compose
      ~DAGCircuit.compose_back
      ~DAGCircuit.count_ops
      ~DAGCircuit.count_ops_longest_path
      ~DAGCircuit.depth
      ~DAGCircuit.descendants
      ~DAGCircuit.draw
      ~DAGCircuit.edges
      ~DAGCircuit.extend_back
      ~DAGCircuit.from_networkx
      ~DAGCircuit.front_layer
      ~DAGCircuit.gate_nodes
      ~DAGCircuit.has_calibration_for
      ~DAGCircuit.idle_wires
      ~DAGCircuit.is_predecessor
      ~DAGCircuit.is_successor
      ~DAGCircuit.layers
      ~DAGCircuit.longest_path
      ~DAGCircuit.multi_qubit_ops
      ~DAGCircuit.multigraph_layers
      ~DAGCircuit.named_nodes
      ~DAGCircuit.node
      ~DAGCircuit.nodes
      ~DAGCircuit.nodes_on_wire
      ~DAGCircuit.num_clbits
      ~DAGCircuit.num_qubits
      ~DAGCircuit.num_tensor_factors
      ~DAGCircuit.op_nodes
      ~DAGCircuit.predecessors
      ~DAGCircuit.properties
      ~DAGCircuit.quantum_predecessors
      ~DAGCircuit.quantum_successors
      ~DAGCircuit.remove_all_ops_named
      ~DAGCircuit.remove_ancestors_of
      ~DAGCircuit.remove_descendants_of
      ~DAGCircuit.remove_nonancestors_of
      ~DAGCircuit.remove_nondescendants_of
      ~DAGCircuit.remove_op_node
      ~DAGCircuit.reverse_ops
      ~DAGCircuit.serial_layers
      ~DAGCircuit.size
      ~DAGCircuit.substitute_node
      ~DAGCircuit.substitute_node_with_dag
      ~DAGCircuit.successors
      ~DAGCircuit.threeQ_or_more_gates
      ~DAGCircuit.to_networkx
      ~DAGCircuit.topological_nodes
      ~DAGCircuit.topological_op_nodes
      ~DAGCircuit.twoQ_gates
      ~DAGCircuit.two_qubit_ops
      ~DAGCircuit.width



   .. rubric:: Attributes

   .. autoattribute:: calibrations
   .. autoattribute:: global_phase
   .. autoattribute:: node_counter
   .. autoattribute:: wires
