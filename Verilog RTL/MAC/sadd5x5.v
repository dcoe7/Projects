//David Coe
//EE278
//5 bit Signed Add/Subtractor 
//10-8-2019
`timescale 1ns / 1ps
module sadd5x5(
    clk,
    a,
    b,
    sum
    );
input clk;
input [4:0]a,b;
output reg [4:0]sum;

reg [5:0]csum;      //sum with carry
reg [5:0]presum=0;    //sum before overflow check
always@*
    begin
    sum=0;
    if((a[4]==0)&&(b[4]==0))    //2 pos numbers
        begin
            csum[4:0]=a[4:0]+b[4:0];
            if(csum[4])sum=5'b01111;
            else sum=csum[4:0];
        end
    else 
        begin
        presum[4:0]=a[4:0]+b[4:0];
        if((a[4]==1'b1)&&(b[4]==1'b1)&&(presum[4]==1'b0)) sum[4:0]=5'b10000;          //2 neg became pos
        else sum=presum[4:0];
        end
    end
endmodule
