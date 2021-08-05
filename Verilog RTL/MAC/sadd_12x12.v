//David Coe
//EE278
//12 bit Signed Add/Subtractor 
//11-27-2019
`timescale 1ns / 1ps
module sadd12x12(
    clk,
    a,
    b,
    sum
    );
input clk;
input [11:0]a,b;
output reg [11:0]sum;

reg [12:0]csum;      //sum with carry
reg [12:0]presum=0;    //sum before overflow check
always@*
    begin
    sum=0;
    if((a[11]==0)&&(b[11]==0))    //2 pos numbers
        begin
            csum[11:0]=a[11:0]+b[11:0];
            if(csum[11])sum=12'b011111111111;
            else sum=csum[11:0];
        end
    else 
        begin
        presum[11:0]=a[11:0]+b[11:0];
        if((a[11]==1'b1)&&(b[11]==1'b1)&&(presum[11]==1'b0)) sum[11:0]=12'b100000000000;          //2 neg became pos
        else sum=presum[11:0];
        end
    end
endmodule
