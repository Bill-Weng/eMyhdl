'''
Created on Oct 17, 2019

@author: Bill
'''

from myhdl import Signal

from blink import blink


def convert_blink(hdl):
    """convert inc block to Verilog or VHDL."""

    enable = Signal(bool(0))
    clock = Signal(bool(0))
    # reset = ResetSignal(0, active=0, isasync=True)
    led = Signal(bool(0))

    blink_1 = blink(led, enable, clock)

    blink_1.convert(hdl=hdl)


convert_blink(hdl='Verilog')
convert_blink(hdl='VHDL')
