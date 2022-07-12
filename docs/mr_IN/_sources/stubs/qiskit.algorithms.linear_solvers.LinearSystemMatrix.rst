LinearSystemMatrix
==================

.. currentmodule:: qiskit.algorithms.linear_solvers

.. autoclass:: LinearSystemMatrix
   :no-members:
   :show-inheritance:

   .. rubric:: Methods

   .. autosummary::
      :nosignatures:
      :toctree: ../stubs/

      ~LinearSystemMatrix.add_bits
      ~LinearSystemMatrix.add_calibration
      ~LinearSystemMatrix.add_register
      ~LinearSystemMatrix.append
      ~LinearSystemMatrix.assign_parameters
      ~LinearSystemMatrix.barrier
      ~LinearSystemMatrix.bind_parameters
      ~LinearSystemMatrix.break_loop
      ~LinearSystemMatrix.cast
      ~LinearSystemMatrix.cbit_argument_conversion
      ~LinearSystemMatrix.ccx
      ~LinearSystemMatrix.ch
      ~LinearSystemMatrix.clear
      ~LinearSystemMatrix.cls_instances
      ~LinearSystemMatrix.cls_prefix
      ~LinearSystemMatrix.cnot
      ~LinearSystemMatrix.combine
      ~LinearSystemMatrix.compose
      ~LinearSystemMatrix.condition_bounds
      ~LinearSystemMatrix.continue_loop
      ~LinearSystemMatrix.control
      ~LinearSystemMatrix.copy
      ~LinearSystemMatrix.copy_empty_like
      ~LinearSystemMatrix.count_ops
      ~LinearSystemMatrix.cp
      ~LinearSystemMatrix.crx
      ~LinearSystemMatrix.cry
      ~LinearSystemMatrix.crz
      ~LinearSystemMatrix.cswap
      ~LinearSystemMatrix.csx
      ~LinearSystemMatrix.cu
      ~LinearSystemMatrix.cu1
      ~LinearSystemMatrix.cu3
      ~LinearSystemMatrix.cx
      ~LinearSystemMatrix.cy
      ~LinearSystemMatrix.cz
      ~LinearSystemMatrix.dcx
      ~LinearSystemMatrix.decompose
      ~LinearSystemMatrix.delay
      ~LinearSystemMatrix.depth
      ~LinearSystemMatrix.diagonal
      ~LinearSystemMatrix.draw
      ~LinearSystemMatrix.ecr
      ~LinearSystemMatrix.eigs_bounds
      ~LinearSystemMatrix.extend
      ~LinearSystemMatrix.find_bit
      ~LinearSystemMatrix.for_loop
      ~LinearSystemMatrix.fredkin
      ~LinearSystemMatrix.from_qasm_file
      ~LinearSystemMatrix.from_qasm_str
      ~LinearSystemMatrix.get_instructions
      ~LinearSystemMatrix.h
      ~LinearSystemMatrix.hamiltonian
      ~LinearSystemMatrix.has_calibration_for
      ~LinearSystemMatrix.has_register
      ~LinearSystemMatrix.i
      ~LinearSystemMatrix.id
      ~LinearSystemMatrix.if_else
      ~LinearSystemMatrix.if_test
      ~LinearSystemMatrix.initialize
      ~LinearSystemMatrix.inverse
      ~LinearSystemMatrix.iso
      ~LinearSystemMatrix.isometry
      ~LinearSystemMatrix.iswap
      ~LinearSystemMatrix.mcp
      ~LinearSystemMatrix.mcrx
      ~LinearSystemMatrix.mcry
      ~LinearSystemMatrix.mcrz
      ~LinearSystemMatrix.mct
      ~LinearSystemMatrix.mcu1
      ~LinearSystemMatrix.mcx
      ~LinearSystemMatrix.measure
      ~LinearSystemMatrix.measure_active
      ~LinearSystemMatrix.measure_all
      ~LinearSystemMatrix.ms
      ~LinearSystemMatrix.num_connected_components
      ~LinearSystemMatrix.num_nonlocal_gates
      ~LinearSystemMatrix.num_tensor_factors
      ~LinearSystemMatrix.num_unitary_factors
      ~LinearSystemMatrix.p
      ~LinearSystemMatrix.pauli
      ~LinearSystemMatrix.power
      ~LinearSystemMatrix.prepare_state
      ~LinearSystemMatrix.qasm
      ~LinearSystemMatrix.qbit_argument_conversion
      ~LinearSystemMatrix.qubit_duration
      ~LinearSystemMatrix.qubit_start_time
      ~LinearSystemMatrix.qubit_stop_time
      ~LinearSystemMatrix.r
      ~LinearSystemMatrix.rcccx
      ~LinearSystemMatrix.rccx
      ~LinearSystemMatrix.remove_final_measurements
      ~LinearSystemMatrix.repeat
      ~LinearSystemMatrix.reset
      ~LinearSystemMatrix.reverse_bits
      ~LinearSystemMatrix.reverse_ops
      ~LinearSystemMatrix.rv
      ~LinearSystemMatrix.rx
      ~LinearSystemMatrix.rxx
      ~LinearSystemMatrix.ry
      ~LinearSystemMatrix.ryy
      ~LinearSystemMatrix.rz
      ~LinearSystemMatrix.rzx
      ~LinearSystemMatrix.rzz
      ~LinearSystemMatrix.s
      ~LinearSystemMatrix.save_amplitudes
      ~LinearSystemMatrix.save_amplitudes_squared
      ~LinearSystemMatrix.save_clifford
      ~LinearSystemMatrix.save_density_matrix
      ~LinearSystemMatrix.save_expectation_value
      ~LinearSystemMatrix.save_expectation_value_variance
      ~LinearSystemMatrix.save_matrix_product_state
      ~LinearSystemMatrix.save_probabilities
      ~LinearSystemMatrix.save_probabilities_dict
      ~LinearSystemMatrix.save_stabilizer
      ~LinearSystemMatrix.save_state
      ~LinearSystemMatrix.save_statevector
      ~LinearSystemMatrix.save_statevector_dict
      ~LinearSystemMatrix.save_superop
      ~LinearSystemMatrix.save_unitary
      ~LinearSystemMatrix.sdg
      ~LinearSystemMatrix.set_density_matrix
      ~LinearSystemMatrix.set_matrix_product_state
      ~LinearSystemMatrix.set_stabilizer
      ~LinearSystemMatrix.set_statevector
      ~LinearSystemMatrix.set_superop
      ~LinearSystemMatrix.set_unitary
      ~LinearSystemMatrix.size
      ~LinearSystemMatrix.snapshot
      ~LinearSystemMatrix.snapshot_density_matrix
      ~LinearSystemMatrix.snapshot_expectation_value
      ~LinearSystemMatrix.snapshot_probabilities
      ~LinearSystemMatrix.snapshot_stabilizer
      ~LinearSystemMatrix.snapshot_statevector
      ~LinearSystemMatrix.squ
      ~LinearSystemMatrix.swap
      ~LinearSystemMatrix.sx
      ~LinearSystemMatrix.sxdg
      ~LinearSystemMatrix.t
      ~LinearSystemMatrix.tdg
      ~LinearSystemMatrix.tensor
      ~LinearSystemMatrix.to_gate
      ~LinearSystemMatrix.to_instruction
      ~LinearSystemMatrix.toffoli
      ~LinearSystemMatrix.u
      ~LinearSystemMatrix.u1
      ~LinearSystemMatrix.u2
      ~LinearSystemMatrix.u3
      ~LinearSystemMatrix.uc
      ~LinearSystemMatrix.ucrx
      ~LinearSystemMatrix.ucry
      ~LinearSystemMatrix.ucrz
      ~LinearSystemMatrix.unitary
      ~LinearSystemMatrix.while_loop
      ~LinearSystemMatrix.width
      ~LinearSystemMatrix.x
      ~LinearSystemMatrix.y
      ~LinearSystemMatrix.z



   .. rubric:: Attributes

   .. autoattribute:: ancillas
   .. autoattribute:: calibrations
   .. autoattribute:: clbits
   .. autoattribute:: data
   .. autoattribute:: evolution_time
   .. autoattribute:: extension_lib
   .. autoattribute:: global_phase
   .. autoattribute:: header
   .. autoattribute:: instances
   .. autoattribute:: metadata
   .. autoattribute:: num_ancillas
   .. autoattribute:: num_clbits
   .. autoattribute:: num_parameters
   .. autoattribute:: num_qubits
   .. autoattribute:: num_state_qubits
   .. autoattribute:: op_start_times
   .. autoattribute:: parameters
   .. autoattribute:: prefix
   .. autoattribute:: qregs
   .. autoattribute:: qubits
   .. autoattribute:: tolerance
