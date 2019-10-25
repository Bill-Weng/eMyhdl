'''
Created on Oct 17, 2019

@author: Bill
'''
from myhdl import block, always_seq, Signal, modbv
from myhdl._always_comb import always_comb


@block
def blink_b(clock, enable, led):

    countor = Signal(modbv(0)[12:])

    @always_seq(clock.posedge, reset=None)
    def inc():
        if enable:
            countor.next = countor + 1

    @always_comb
    def led_assign():
            led.next = countor[11]

    return inc, led_assign

# new change 11
# if __name__ == '__main__':
#
#     @block
#     def convert_blink(hdl):
#         """convert inc block to Verilog or VHDL."""
#
#         enable = Signal(bool(0))
#         clock = Signal(bool(0))
#          reset = ResetSignal(0, active=0, isasync=True)
#         led = Signal(bool(0))
#
#         blink_1 = blink(led, enable, clock)
#
#         blink_1.convert(hdl=hdl)
#
#     convert_blink(hdl='Verilog')
#     convert_blink(hdl='VHDL')
