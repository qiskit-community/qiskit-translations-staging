NumPyMatrix
===========

.. currentmodule:: qiskit.algorithms.linear_solvers

.. autoclass:: NumPyMatrix
   :no-members:
   :show-inheritance:

   .. rubric:: Methods

   .. autosummary::
      :nosignatures:
      :toctree: ../stubs/

      ~NumPyMatrix.add_bits
      ~NumPyMatrix.add_calibration
      ~NumPyMatrix.add_register
      ~NumPyMatrix.append
      ~NumPyMatrix.assign_parameters
      ~NumPyMatrix.barrier
      ~NumPyMatrix.bind_parameters
      ~NumPyMatrix.break_loop
      ~NumPyMatrix.cast
      ~NumPyMatrix.cbit_argument_conversion
      ~NumPyMatrix.ccx
      ~NumPyMatrix.ch
      ~NumPyMatrix.clear
      ~NumPyMatrix.cls_instances
      ~NumPyMatrix.cls_prefix
      ~NumPyMatrix.cnot
      ~NumPyMatrix.combine
      ~NumPyMatrix.compose
      ~NumPyMatrix.condition_bounds
      ~NumPyMatrix.continue_loop
      ~NumPyMatrix.control
      ~NumPyMatrix.copy
      ~NumPyMatrix.copy_empty_like
      ~NumPyMatrix.count_ops
      ~NumPyMatrix.cp
      ~NumPyMatrix.crx
      ~NumPyMatrix.cry
      ~NumPyMatrix.crz
      ~NumPyMatrix.cswap
      ~NumPyMatrix.csx
      ~NumPyMatrix.cu
      ~NumPyMatrix.cu1
      ~NumPyMatrix.cu3
      ~NumPyMatrix.cx
      ~NumPyMatrix.cy
      ~NumPyMatrix.cz
      ~NumPyMatrix.dcx
      ~NumPyMatrix.decompose
      ~NumPyMatrix.delay
      ~NumPyMatrix.depth
      ~NumPyMatrix.diagonal
      ~NumPyMatrix.draw
      ~NumPyMatrix.ecr
      ~NumPyMatrix.eigs_bounds
      ~NumPyMatrix.extend
      ~NumPyMatrix.find_bit
      ~NumPyMatrix.for_loop
      ~NumPyMatrix.fredkin
      ~NumPyMatrix.from_qasm_file
      ~NumPyMatrix.from_qasm_str
      ~NumPyMatrix.get_instructions
      ~NumPyMatrix.h
      ~NumPyMatrix.hamiltonian
      ~NumPyMatrix.has_calibration_for
      ~NumPyMatrix.has_register
      ~NumPyMatrix.i
      ~NumPyMatrix.id
      ~NumPyMatrix.if_else
      ~NumPyMatrix.if_test
      ~NumPyMatrix.initialize
      ~NumPyMatrix.inverse
      ~NumPyMatrix.iso
      ~NumPyMatrix.isometry
      ~NumPyMatrix.iswap
      ~NumPyMatrix.mcp
      ~NumPyMatrix.mcrx
      ~NumPyMatrix.mcry
      ~NumPyMatrix.mcrz
      ~NumPyMatrix.mct
      ~NumPyMatrix.mcu1
      ~NumPyMatrix.mcx
      ~NumPyMatrix.measure
      ~NumPyMatrix.measure_active
      ~NumPyMatrix.measure_all
      ~NumPyMatrix.ms
      ~NumPyMatrix.num_connected_components
      ~NumPyMatrix.num_nonlocal_gates
      ~NumPyMatrix.num_tensor_factors
      ~NumPyMatrix.num_unitary_factors
      ~NumPyMatrix.p
      ~NumPyMatrix.pauli
      ~NumPyMatrix.power
      ~NumPyMatrix.prepare_state
      ~NumPyMatrix.qasm
      ~NumPyMatrix.qbit_argument_conversion
      ~NumPyMatrix.qubit_duration
      ~NumPyMatrix.qubit_start_time
      ~NumPyMatrix.qubit_stop_time
      ~NumPyMatrix.r
      ~NumPyMatrix.rcccx
      ~NumPyMatrix.rccx
      ~NumPyMatrix.remove_final_measurements
      ~NumPyMatrix.repeat
      ~NumPyMatrix.reset
      ~NumPyMatrix.reverse_bits
      ~NumPyMatrix.reverse_ops
      ~NumPyMatrix.rv
      ~NumPyMatrix.rx
      ~NumPyMatrix.rxx
      ~NumPyMatrix.ry
      ~NumPyMatrix.ryy
      ~NumPyMatrix.rz
      ~NumPyMatrix.rzx
      ~NumPyMatrix.rzz
      ~NumPyMatrix.s
      ~NumPyMatrix.save_amplitudes
      ~NumPyMatrix.save_amplitudes_squared
      ~NumPyMatrix.save_clifford
      ~NumPyMatrix.save_density_matrix
      ~NumPyMatrix.save_expectation_value
      ~NumPyMatrix.save_expectation_value_variance
      ~NumPyMatrix.save_matrix_product_state
      ~NumPyMatrix.save_probabilities
      ~NumPyMatrix.save_probabilities_dict
      ~NumPyMatrix.save_stabilizer
      ~NumPyMatrix.save_state
      ~NumPyMatrix.save_statevector
      ~NumPyMatrix.save_statevector_dict
      ~NumPyMatrix.save_superop
      ~NumPyMatrix.save_unitary
      ~NumPyMatrix.sdg
      ~NumPyMatrix.set_density_matrix
      ~NumPyMatrix.set_matrix_product_state
      ~NumPyMatrix.set_stabilizer
      ~NumPyMatrix.set_statevector
      ~NumPyMatrix.set_superop
      ~NumPyMatrix.set_unitary
      ~NumPyMatrix.size
      ~NumPyMatrix.snapshot
      ~NumPyMatrix.snapshot_density_matrix
      ~NumPyMatrix.snapshot_expectation_value
      ~NumPyMatrix.snapshot_probabilities
      ~NumPyMatrix.snapshot_stabilizer
      ~NumPyMatrix.snapshot_statevector
      ~NumPyMatrix.squ
      ~NumPyMatrix.swap
      ~NumPyMatrix.sx
      ~NumPyMatrix.sxdg
      ~NumPyMatrix.t
      ~NumPyMatrix.tdg
      ~NumPyMatrix.tensor
      ~NumPyMatrix.to_gate
      ~NumPyMatrix.to_instruction
      ~NumPyMatrix.toffoli
      ~NumPyMatrix.u
      ~NumPyMatrix.u1
      ~NumPyMatrix.u2
      ~NumPyMatrix.u3
      ~NumPyMatrix.uc
      ~NumPyMatrix.ucrx
      ~NumPyMatrix.ucry
      ~NumPyMatrix.ucrz
      ~NumPyMatrix.unitary
      ~NumPyMatrix.while_loop
      ~NumPyMatrix.width
      ~NumPyMatrix.x
      ~NumPyMatrix.y
      ~NumPyMatrix.z



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
   .. autoattribute:: matrix
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
