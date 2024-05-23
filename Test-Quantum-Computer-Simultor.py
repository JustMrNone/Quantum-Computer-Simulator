import unittest
import numpy as np
from project import Qubit, QuantumGate, QuantumCircuit

class TestQuantumSimulator(unittest.TestCase):
    def test_initial_state_zero(self):
        qubit = Qubit(0)
        np.testing.assert_array_equal(qubit.state, np.array([1, 0], dtype=complex))

    def test_initial_state_one(self):
        qubit = Qubit(1)
        np.testing.assert_array_equal(qubit.state, np.array([0, 1], dtype=complex))

    def test_apply_gate_I(self):
        qubit = Qubit(0)
        qubit.apply_gate(QuantumGate.I())
        np.testing.assert_array_equal(qubit.state, np.array([1, 0], dtype=complex))

    def test_apply_gate_X(self):
        qubit = Qubit(0)
        qubit.apply_gate(QuantumGate.X())
        np.testing.assert_array_equal(qubit.state, np.array([0, 1], dtype=complex))

    def test_apply_gate_H(self):
        qubit = Qubit(0)
        qubit.apply_gate(QuantumGate.H())
        expected_state = (1/np.sqrt(2)) * np.array([1, 1], dtype=complex)
        np.testing.assert_almost_equal(qubit.state, expected_state, decimal=6)

    def test_measure(self):
        qubit = Qubit(0)
        qubit.apply_gate(QuantumGate.H())
        result = qubit.measure()
        self.assertIn(result, [0, 1])

    def test_quantum_circuit(self):
        circuit = QuantumCircuit(0)
        circuit.apply_gates(['H', 'X'])
        expected_state = np.dot(QuantumGate.X(), np.dot(QuantumGate.H(), np.array([1, 0], dtype=complex)))
        np.testing.assert_almost_equal(circuit.qubit.state, expected_state, decimal=6)

if __name__ == "__main__":
    unittest.main()
