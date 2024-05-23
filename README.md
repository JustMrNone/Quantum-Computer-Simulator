# Quantum Computer Simulator

#### Description: This project involves the implementation and testing of a quantum computer simulator using Python. The simulator models the behavior of a single qubit and allows the application of basic quantum gates. The project is divided into two main files: project.py for the core functionality and test_project.py for unit tests.

## Core Functionality (project.py)
The project.py file defines three main classes: Qubit, QuantumGate, and QuantumCircuit.

### Qubit Class:

- **Initialization**: A qubit can be initialized to state 0 or 1, represented as [1, 0] or [0, 1] respectively.
- **Apply Gate**: Allows the application of quantum gates (matrices) to change the qubit's state.
- **Measure**: Simulates the measurement of a qubit, returning 0 or 1 based on the state's probabilities.

### QuantumGate Class:

- **Static Methods for Gates**: Provides identity (I), Pauli-X (X), and Hadamard (H) gates.
- **Get Gate Method**: Returns the appropriate gate based on the input name.

### QuantumCircuit Class:

- **Initialization**: Initializes the circuit with a qubit in a specified state.
- **Apply Gates**: Applies a sequence of gates to the qubit.
- **Measure Qubit**: Measures the qubit and returns the result.

## Unit Tests (test_project.py)
The test_project.py file uses the unittest framework to define and run tests for the quantum simulator. The tests validate the correct functionality of each component in project.py.

### Imports:

- Import the unittest module and numpy for numerical operations.
- Import the Qubit, QuantumGate, and QuantumCircuit classes from project.py.

### Test Cases:

- **Initial State Tests**: Verify that qubits initialized to states 0 and 1 have the correct state vectors.
- **Gate Application Tests**: Check the correct application of identity, Pauli-X, and Hadamard gates.
- **Measurement Test**: Ensure the measurement function returns valid outcomes (0 or 1).
- **Quantum Circuit Test**: Validate the state of a qubit after applying a sequence of gates.

### Test Execution:

The tests are executed using `unittest.main()`, which runs all defined test cases and reports the results.

## Running the Tests
To run the tests, save both project.py and test_project.py in the same directory. Execute the following command in your terminal:

```bash
python test_project.py
