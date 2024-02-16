import qiskit
from qiskit import QuantumRegister, QuantumCircuit 
from qiskit_ibm_runtime import QiskitRuntimeService, Sampler

def set_qubits(n: int):
    global circuit
    qr = QuantumRegister(n) # Create a quantum register of size n
    cr = qiskit.ClassicalRegister(n)
    circuit = QuantumCircuit(qr, cr)
    circuit.h(qr) # Apply Hadamard gate to qubits
    circuit.measure(qr, cr)


service = QiskitRuntimeService(channel="ibm_quantum", token="") # Add API token here
backend = service.backend('ibm_osaka')
set_qubits(1) # Adjust register size as needed
job = Sampler(backend).run(circuit)
result = job.result()
print(result) # Prints quantum random number