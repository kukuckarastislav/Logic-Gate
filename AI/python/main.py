from logicGates import *

# one bit full adder
iA = Input(False)
iB = Input(False)
iC = Input(False)

xor_1 = LG_XOR(inputs=[iA, iB])
and_1 = LG_AND(inputs=[iA, iB])

xor_2 = LG_XOR(inputs=[xor_1, iC])
and_2 = LG_AND(inputs=[xor_1, iC])

lg_or = LG_OR(inputs=[and_2, and_1])

sum_out = Output(xor_2)
carry_out = Output(lg_or)

one_bit_full_adder = LogicGatesMesh(inputs=[iA, iB, iC], outputs=[sum_out, carry_out])
TB = one_bit_full_adder.printTruthTable()













