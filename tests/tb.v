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
  wire kb_dp;
  wire kb_dm;
  wire tp_usb_init;

  usb_hid_keyboard u_usb_hid_keyboard (
      .clk  (clk),
      .reset  (reset),
      .kb_dp (kb_dp),
      .kb_dm (kb_dm),
      .tp_usb_init (tp_usb_init)
  );

endmodule
