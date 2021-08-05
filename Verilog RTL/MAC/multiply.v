//David Coe
//EE278
//Stage 1 FP 16b Mult
//10-30-2019
`timescale 1ns / 1ps

module multiply(
    ai,
    bi,
    ao,
    bo,
    po,
    tm,
    clk
    );
input clk;
input [15:0]ai,bi;
output [15:0]ao,bo,po;
output [19:0]tm;                        //temp mantissa
parameter bias=5'b01111;              //Half Precision Bias
parameter nbias=~bias+1'b1;           //negative bias
reg [4:0]aix,bix,px;
reg [19:0]temp_mand;
wire ready;

assign po[15]=ai[15]^bi[15];    //compute sign
sadd5x5 unbias_a(.clk(clk),.a(ai[14:10]),.b(nbias),.sum(aix));    //unbias a
sadd5x5 unbias_b(.clk(clk),.a(bi[14:10]),.b(nbias),.sum(bix));    //unbias b
sadd5x5 add_exp(.clk(clk),.a(aix),.b(bix),.sum(px));    //add new exponent
sadd5x5 re_bias(.clk(clk),.a(px),.b(bias),.sum(po[14:10]));    //bias new exponent

umult10x10 mant_mult(.clk(clk),.Mplier(ai[9:0]),.Mcand(bi[9:0]),.Prod(temp_mand),.done(ready));

assign tm=temp_mand;
endmodule
