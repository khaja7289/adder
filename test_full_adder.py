import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge, Timer

@cocotb.test()
async def test_full_adder(dut):
    clock = Clock(dut.clk, 10, units="ns")
    cocotb.fork(clock.start())

    for a, b, cin, expected_sum, expected_cout in [(0, 0, 0, 0, 0),
                                                   (0, 0, 1, 1, 0),
                                                   (0, 1, 0, 1, 0),
                                                   (0, 1, 1, 0, 1),
                                                   (1, 0, 0, 1, 0),
                                                   (1, 0, 1, 0, 1),
                                                   (1, 1, 0, 0, 1),
                                                   (1, 1, 1, 1, 1)]:
        dut.a <= a
        dut.b <= b
        dut.cin <= cin

        await RisingEdge(dut.clk)
        sum = dut.sum.value.integer
        cout = dut.cout.value.integer

        assert sum == expected_sum, f"Error: a={a}, b={b}, cin={cin}, sum={sum}, expected_sum={expected_sum}"
        assert cout == expected_cout, f"Error: a={a}, b={b}, cin={cin}, cout={cout}, expected_cout={expected_cout}"

        await FallingEdge(dut.clk)
