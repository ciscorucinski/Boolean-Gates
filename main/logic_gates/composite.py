from main.logic_gates.basic import and_gate, or_gate, not_gate


def xor_gate(a, b):

    # return not input1 == input2

    and_not_result = not_gate(and_gate(a, b))
    or_result = or_gate(a, b)

    return and_gate(and_not_result, or_result)

    # return and_gate(not_gate(and_gate(a, b)), or_gate(a, b))
