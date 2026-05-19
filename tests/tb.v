`default_nettype none
`timescale 1ns / 1ps

module tb ();

  // Dump the signals to a FST file. You can view it with gtkwave or surfer.
  initial begin
    $dumpfile("tb.fst");
    $dumpvars(0, tb);
    #1;
  end

  wire clk;
  wire reset;
  wire kb_dp_oe;
  wire kb_dp_in;
  wire kb_dp_out;
  wire kb_dm_oe;
  wire kb_dm_in;
  wire kb_dm_out;
  wire tp_usb_init;
  wire tp_sync_detected;

  usb_hid_keyboard u_usb_hid_keyboard (
      .clk  (clk),
      .reset  (reset),
      .kb_dp_oe (kb_dp_oe),
      .kb_dp_in (kb_dp_in),
      .kb_dp_out (kb_dp_out),
      .kb_dm_oe (kb_dm_oe),
      .kb_dm_in (kb_dm_in),
      .kb_dm_out (kb_dm_out),
      .tp_usb_init (tp_usb_init),
      .tp_sync_detected(tp_sync_detected)
  );

endmodule
