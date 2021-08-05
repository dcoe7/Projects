//David Coe
//EE278
//Stage 2 FP 16b Normalize
//11-27-2019
`timescale 1ns / 1ps

module norm(
    pi,
    po,
    tm,
    tmo,
    clk
    );
input clk;
input [15:0]pi;
input [19:0]tm; 
output reg [15:0]po;
output reg [19:0]tmo;

assign pi[15]=po[15];  
reg [1:0]int;
wire [4:0]new_x;
always@* int=tm[19:18];
always@*
    begin
        if((int==2)||(int==3))
            begin
                po[14:0]=new_x;         //inc exp
                tmo={1'b0,tm[19:1]};    //shift mant right 1
            end
        else 
            begin
                po[14:0]=pi[14:0];
                tmo=tm;
            end
    end
sadd5x5 exp_change(.clk(clk),.a(pi[14:10]),.b(5'b00001),.sum(new_x));  //inc exp
endmodule