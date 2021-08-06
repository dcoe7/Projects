//David Coe
//EE278
//TESTBENCH
//10x10 Unsigned Multiplier
//10-16-19
`timescale 1 ns / 1 ps
module testbench;
 reg [9:0] mplierT, mcandT;
 reg startT,clk;
 wire [19:0] productT;
 wire doneT;
 //TB vars
 reg test_passed=0;
 wire [19:0] ACCT;
 wire [4:0]pstate;
 // Instantiate multiplier
umult10x10 my_umult10x10 (
    .clk(clk),
    .St(startT),
    .Mplier(mplierT),
    .Mcand(mcandT),
    .Prod(productT),
    .done(doneT),
    .ACC(ACCT),
    .pstate(pstate)
    );
//100MHz Clock
    always
        begin
        clk = 1'b0;
        #5;
        clk = 1'b1;
        #5;
    end
 // Test Case #0   
    initial begin
        test_passed = 1'b0;       
        mplierT = 10'b1111111111;
        mcandT = 10'b1111111111;
        #5;
        startT=1'b1;
        #5;
        startT=1'b0;
    end
//Display Output
    initial  begin
        $display("\t\t\t\ttime,\tclk,\tACC\t\t\tproduct"); 
        $monitor("%d,\t%b,\t\t%b,\t%b",$time, clk,ACCT,productT); 
    end 
//Hardstop
    initial 
        #310  $finish;
endmodule
