import pennylane as qml
from pennylane import numpy as np


dev1 = qml.device("default.qubit", wires=2)
#dev2 = qml.device("default.qubit", wires=2)

@qml.qnode(dev1)
def quantum_function1(angles):
    qml.RX(angles[0], wires=0)
    qml.RY(angles[1], wires=0)
    return qml.expval(qml.PauliX(0))

@qml.qnode(dev1)
def quantum_function2(angles):
    qml.RY(angles[1], wires=1)
    qml.RX(angles[0], wires=1)
    return qml.expval(qml.PauliX(1))

angle=[3.79894785, 0.71678115]
result1=quantum_function1([angle[0],angle[1]])
result2=quantum_function2([angle[0],angle[1]])
result= np.abs(result1-result2)
tolerance=()
print('The value is',result)

  