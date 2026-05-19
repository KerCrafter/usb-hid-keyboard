`default_nettype none

module usb_hid_keyboard (
    input  wire clk,
    input  wire reset,
    inout  wire kb_dp,
    inout  wire kb_dm,
    output reg tp_usb_init
);

  assign tp_usb_init = 1;

endmodule
