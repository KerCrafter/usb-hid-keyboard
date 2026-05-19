import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles, Timer

async def inital_reset(dut):
  dut.reset.value = '1'
  await Timer(1, unit='ns');

  dut.clk.value = '1';
  await Timer(1, unit='ns');
  dut.clk.value = '0';
  await Timer(1, unit='ns');

  dut.reset.value = '0'
  await Timer(1, unit='ns');

  dut.clk.value = '1';
  await Timer(1, unit='ns');
  dut.clk.value = '0';
  await Timer(1, unit='ns');

@cocotb.test()
async def init_test(dut):
  await inital_reset(dut);

  assert dut.tp_usb_init.value == 1
