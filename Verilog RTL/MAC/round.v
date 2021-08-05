//David Coe
//EE278
//Stage 3 FP 16b Round
//11-27-2019
`timescale 1ns / 1ps

module round(
    pi,
    po,
    tm,
    clk
    );
input clk;
input [15:0]pi;
input [19:0]tm; 
output reg [15:0]po;

assign pi[15]=po[15]; 

reg [11:0]up;
reg [4:0]new_x;

always@*
    begin
    if(tm[9])   //round up
        begin
        if(~up[10:0])po[9:0]=up[9:0];   //no carry
        else                            //carry
            begin
            po[14:0]={new_x,up[10:1]};  //inc exp and shift mant right
            end
        end
    else po[9:0]=pi[9:0];   //round down
    end

sadd12x12 round_up(.clk(clk),.a({2'b00,tm[19:10]}),.b(1'b1),.sum(up));
sadd5x5 inc_x(.clk(clk),.a(pi[14:10]),.b(1'b1),.sum(new_x));
endmodule