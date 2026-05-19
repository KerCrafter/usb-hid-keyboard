`default_nettype none

module usb_hid_keyboard (
    input  wire clk,
    input  wire reset,
    input wire kb_dp_in,
    input wire kb_dm_in,
    output wire kb_dp_out,
    output wire kb_dm_out,
    output reg kb_dp_oe,
    output reg kb_dm_oe,
    output reg tp_usb_init
);

  reg lock = 0;

  always @(posedge clk) begin
      if (reset) begin
          tp_usb_init <= 0;
          kb_dp_oe    <= 0;
          kb_dm_oe    <= 0;
          lock         <= 0;
      end else begin
          if(lock == 0) begin
            tp_usb_init <= 1;
            lock <= 1;
          end

          if(lock && kb_dp_in == 0 && kb_dm_in == 0) begin
            tp_usb_init <= 0;
          end
      end
  end

endmodule
