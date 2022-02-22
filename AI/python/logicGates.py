# Logic gates class

class Input:

    def __init__(self, state):
        self.name = 'INPUT'
        self.state = state

    def output(self):
        return self.state


class Output:

    def __init__(self, out):
        self.name = 'OUTPUT'
        self.out = out

    def output(self):
        return self.out.output()


class LG_NOT:

    def __init__(self, input):
        self.name = 'NOT'
        self.input = input

    def output(self):
        return not self.input.output()


class LG_AND:

    def __init__(self, inputs):
        self.name = 'AND'
        self.inputs = inputs

    def output(self):
        AND_out = True
        for inp in self.inputs:
            AND_out = AND_out and inp.output()
        return AND_out


class LG_OR:

    def __init__(self, inputs):
        self.name = 'OR'
        self.inputs = inputs

    def output(self):
        OR_out = False
        for inp in self.inputs:
            OR_out = OR_out or inp.output()
        return OR_out


class LG_NAND:

    def __init__(self, inputs):
        self.name = 'NAND'
        self.inputs = inputs

    def output(self):
        NAND_out = True
        for inp in self.inputs:
            NAND_out = NAND_out and inp.output()
        return not NAND_out


class LG_NOR:

    def __init__(self, inputs):
        self.name = 'NOR'
        self.inputs = inputs

    def output(self):
        NOR_out = True
        for inp in self.inputs:
            NOR_out = NOR_out or inp.output()
        return not NOR_out


class LG_XOR:

    def __init__(self, inputs):
        self.name = 'XOR'
        self.inputs = inputs

    def output(self):
        return self.inputs[0].output() != self.inputs[1].output()


class LogicGatesMesh:

    def __init__(self, inputs, outputs):
        self.inputs = inputs
        self.outputs = outputs

    def getInputs(self):
        return [inp.state for inp in self.inputs]

    def setInputs(self, inputsValues):
        if len(inputsValues) != len(self.inputs):
            return
        for inp, new_value in zip(self.inputs, inputsValues):
            inp.state = new_value

    def getOutputs(self):
        return [out.output() for out in self.outputs]

    def getTruthTable(self):
        save_inputs = self.getInputs()

        TruthTable = []
        num_of_inputs = len(self.inputs)
        num_of_combinations = 2**num_of_inputs
        for i in range(num_of_combinations):
            str_bin = bin(i)[2:]
            new_inputs = [False] * (num_of_inputs - len(str_bin)) + [bool(int(c)) for c in str_bin]
            self.setInputs(new_inputs)
            out = self.getOutputs()
            TruthTable.append((new_inputs, out))

        self.setInputs(save_inputs)
        return TruthTable

    def printTruthTable(self):
        for t in self.getTruthTable():
            print([int(b) for b in t[0]], [int(b) for b in t[1]])
