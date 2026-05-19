import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles, Timer

async def inital_reset(dut):
  dut.kb_dp_in.value = 1;
  dut.kb_dm_in.value = 0;

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
async def init_reset_test(dut):
  await inital_reset(dut);

  assert dut.tp_usb_init.value == 1


@cocotb.test()
async def show_led_tp_usb_init_on_init(dut):
  await inital_reset(dut);

  dut.clk.value = '1';
  await Timer(1, unit='ns');
  dut.clk.value = '0';
  await Timer(1, unit='ns');

  assert dut.tp_usb_init.value == 1

@cocotb.test()
async def pc_tempt_etablish_init(dut):
  await inital_reset(dut);

  dut.clk.value = '1';
  await Timer(1, unit='ns');
  dut.clk.value = '0';
  await Timer(1, unit='ns');

  dut.kb_dp_in.value = 0;
  dut.kb_dm_in.value = 1;

  dut.clk.value = '1';
  await Timer(1, unit='ns');
  dut.clk.value = '0';
  await Timer(1, unit='ns');

  assert dut.tp_usb_init.value == 1

@cocotb.test()
async def pc_send_SE0_signal(dut):
  await inital_reset(dut);

  dut.clk.value = '1';
  await Timer(1, unit='ns');
  dut.clk.value = '0';
  await Timer(1, unit='ns');

  dut.kb_dp_in.value = 0;
  dut.kb_dm_in.value = 0;

  dut.clk.value = '1';
  await Timer(1, unit='ns');
  dut.clk.value = '0';
  await Timer(1, unit='ns');

  assert dut.tp_usb_init.value == 0

async def PC_DP_LOW_during_12MHZ_cycle(dut):
  dut.kb_dp_in.value = 0;
  dut.kb_dm_in.value = 1;

  dut.clk.value = '1';
  await Timer(1, unit='ns');
  dut.clk.value = '0';
  await Timer(1, unit='ns');

  dut.clk.value = '1';
  await Timer(1, unit='ns');
  dut.clk.value = '0';
  await Timer(1, unit='ns');

  dut.clk.value = '1';
  await Timer(1, unit='ns');
  dut.clk.value = '0';
  await Timer(1, unit='ns');

  dut.clk.value = '1';
  await Timer(1, unit='ns');
  dut.clk.value = '0';
  await Timer(1, unit='ns');

async def PC_DP_HIGH_during_12MHZ_cycle(dut):
  dut.kb_dp_in.value = 1;
  dut.kb_dm_in.value = 0;

  dut.clk.value = '1';
  await Timer(1, unit='ns');
  dut.clk.value = '0';
  await Timer(1, unit='ns');

  dut.clk.value = '1';
  await Timer(1, unit='ns');
  dut.clk.value = '0';
  await Timer(1, unit='ns');

  dut.clk.value = '1';
  await Timer(1, unit='ns');
  dut.clk.value = '0';
  await Timer(1, unit='ns');

  dut.clk.value = '1';
  await Timer(1, unit='ns');
  dut.clk.value = '0';
  await Timer(1, unit='ns');

async def PC_transmit_SYNC(dut):
  await PC_DP_LOW_during_12MHZ_cycle(dut);
  await PC_DP_LOW_during_12MHZ_cycle(dut);
  await PC_DP_LOW_during_12MHZ_cycle(dut);
  await PC_DP_LOW_during_12MHZ_cycle(dut);
  await PC_DP_LOW_during_12MHZ_cycle(dut);
  await PC_DP_LOW_during_12MHZ_cycle(dut);
  await PC_DP_LOW_during_12MHZ_cycle(dut);
  await PC_DP_HIGH_during_12MHZ_cycle(dut);

@cocotb.test()
async def pc_send_SYNC_signal(dut):
  await inital_reset(dut);

  await PC_transmit_SYNC(dut);

  assert dut.tp_usb_init.value == 1
