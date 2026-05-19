`default_nettype none

module usb_hid_keyboard (
    input  wire clk,
    input  wire clk_locked,
    input  wire reset,
    input wire kb_dp_in,
    input wire kb_dm_in,
    output wire kb_dp_out,
    output wire kb_dm_out,
    output reg kb_dp_oe,
    output reg kb_dm_oe,
    output reg tp_usb_init,
    output reg tp_sync_detected
);

  reg lock = 0;

  reg start_check_sync = 0;
  reg [4:0] cnt_sync = 0;

  always @(posedge clk) begin
      if (reset) begin
          tp_usb_init <= 0;
          kb_dp_oe    <= 0;
          kb_dm_oe    <= 0;
          lock         <= 0;
          tp_sync_detected <= 0;
          start_check_sync <= 0;
      end else begin
          if(lock == 0) begin
            tp_usb_init <= 1;
            tp_sync_detected <= 0;
            lock <= 1;
          end

          if(lock && kb_dp_in == 0 && kb_dm_in == 1) begin
            start_check_sync <= 1;
          end

          if(lock && kb_dp_in == 0 && kb_dm_in == 0) begin
            tp_usb_init <= 0;
          end

          if(start_check_sync) begin
            if(cnt_sync <= 28) begin
              cnt_sync <= cnt_sync + 1;
            end

            if(cnt_sync == 28 && kb_dp_in == 1 && kb_dm_in == 0) begin
              tp_sync_detected <= 1;
            end
          end

      end
  end

endmodule
