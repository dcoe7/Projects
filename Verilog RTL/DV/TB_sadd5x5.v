//David Coe
//EE278
//TESTBENCH
//5x5 add/subtract
//10-16-19
`timescale 1 ns / 1 ps
module testbench;
reg clk;
reg [4:0]a,b;
wire [4:0]sum;
 // Instantiate signed adder
sadd5x5 mysadd5x5(
    .clk(clk),
    .a(a),
    .b(b),
    .sum(sum)
    );
//100MHz Clock
    always
        begin
        clk = 1'b0;
        #5;
        clk = 1'b1;
        #5;
    end/*
initial
    begin
    a=0; b=0;
    #5;
    a=5'b10001; b=5'b10001;
    #5;
    end   */ 
initial 
    begin
    a=0; b=1;
    end
always
    begin
    #5
    a=a+1;   
    end

//Display Output
    initial  begin
        $display("\t\t\t\ttime,\tclk,\ta,\tb,\t\tsum"); 
        $monitor("%d,\t%b,\t%b,\t%b,\t%b",$time, clk,a,b,sum); 
    end 
//Hardstop
    initial 
        #110  $finish;
endmodule
