def transistor_internals(control_wire, source, base):
    if control_wire:
        base = source
    return base


def transistor(control_wire):
    return transistor_internals(control_wire, 1, 0)
