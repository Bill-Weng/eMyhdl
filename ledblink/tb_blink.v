module tb_blink;

reg clock;
reg enable;
wire led;

initial begin
    $from_myhdl(
        clock,
        enable
    );
    $to_myhdl(
        led
    );
end

blink dut(
    clock,
    enable,
    led
);

endmodule
