def sigmod_func(x):
    e = 2.718281
    return (1/(e**(-x)+1))

def ANDgate(x1, x2):
    bias_x0 = 1
    hidden_neuron = bias_x0*(-30) + x1*20+x2*20
    output_neuron = round(sigmod_func(hidden_neuron))
    return (output_neuron)

def NANDgate(x1, x2):
    bias_x0 = 1
    hidden_neuron = bias_x0*(30) + x1*(-20)+x2*(-20)
    output_neuron = round(sigmod_func(hidden_neuron))
    return (output_neuron)

def ORgate(x1, x2):
    bias_x0 = 1
    hidden_neuron = bias_x0*(-10) + x1*(20)+x2*(20)
    output_neuron = round(sigmod_func(hidden_neuron))
    return (output_neuron)

def NORgate(x1, x2):
    bias_x0 = 1
    hidden_neuron = bias_x0*(10) + x1*(-20)+x2*(-20)
    output_neuron = round(sigmod_func(hidden_neuron))
    return (output_neuron)

print ("Please, input Gate Name (AND, NOR, XNOR, etc.)")
GATE_name = input()
print ("Input x1: ")
x1 = int(input())
print ("Input x2: ")
x2 = int(input())
if (GATE_name == "AND"):
    print (ANDgate(x1, x2))
if (GATE_name == "NAND"):
    print (NANDgate(x1, x2))
if (GATE_name == "OR"):
    print (ORgate(x1, x2))
if (GATE_name == "NOR"):
    print (NORgate(x1, x2))

if (GATE_name == "XOR"):
    OR = ORgate(x1, x2)
    NAND = NANDgate(x1, x2)
    print (ANDgate(OR, NAND))
if (GATE_name == "XNOR"):
    AND = ANDgate(x1, x2)
    NOR = NORgate(x1, x2)
    print (ORgate(AND, NOR))