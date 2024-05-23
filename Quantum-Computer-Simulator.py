import numpy as np
class Qubit:
    def __init__(self, state=0):
        if state == 0:
            self.state = np.array([1, 0], dtype=complex)
        elif state == 1:
            self.state = np.array([0, 1], dtype=complex)
        else:
            raise ValueError("Invalid initial state. State must be 0 or 1.")
    
    def apply_gate(self, gate):
        self.state = np.dot(gate, self.state)
    
    def measure(self):
        probabilities = np.abs(self.state) ** 2
        result = np.random.choice([0, 1], p=probabilities)
        return result

class QuantumGate:
    @staticmethod
    def I():
        return np.array([[1, 0], [0, 1]], dtype=complex)  # Identity gate
    
    @staticmethod
    def X():
        return np.array([[0, 1], [1, 0]], dtype=complex)  # Pauli-X (NOT) gate
    
    @staticmethod
    def H():
        return (1/np.sqrt(2)) * np.array([[1, 1], [1, -1]], dtype=complex)  # Hadamard gate
    
    @staticmethod
    def get_gate(gate_name):
        if gate_name == 'I':
            return QuantumGate.I()
        elif gate_name == 'X':
            return QuantumGate.X()
        elif gate_name == 'H':
            return QuantumGate.H()
        else:
            raise ValueError("Unknown gate")

class QuantumCircuit:
    def __init__(self, initial_state):
        self.qubit = Qubit(initial_state)
    
    def apply_gates(self, gates):
        for gate_name in gates:
            gate = QuantumGate.get_gate(gate_name)
            self.qubit.apply_gate(gate)
            print(f"After applying {gate_name} gate:", self.qubit.state)
    
    def measure_qubit(self):
        result = self.qubit.measure()
        print("Measurement result:", result)
        return result

def main():
    # Get initial state from user
    initial_state = int(input("Enter initial state (0 or 1): "))
    
    # Get sequence of gates from user
    gates = input("Enter sequence of gates (I, X, H) separated by spaces: ").split()
    
    # Create quantum circuit with initial state
    circuit = QuantumCircuit(initial_state)
    
    # Apply gates to the qubit
    circuit.apply_gates(gates)
    
    # Measure the qubit
    circuit.measure_qubit()

if __name__ == "__main__":
    main()
