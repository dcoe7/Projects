//David Coe
//EE278
//Stage 1 FP 16b Adder
//11-27-2019
`timescale 1ns / 1ps

module align(
    ai,
    bi,
    sum,
    a_m,
    shift,
    clk
    );
input clk;
input [15:0]ai,bi;
output reg [15:0]sum;
output reg [19:0]a_m;      //aligned mantissa
output reg [4:0]shift;      //#shifts

reg [1:0]process;   //case var      



always@*
    begin
        if(ai[14:10]>bi[14:10])process=0;                //a>b
            if(bi[14:10]>ai[14:10])process=1;            //b>a
            else process=2;     //b=a, !=0
    end
always@*
    case(process)
        0:  //a>b
            begin
                shift=ai-bi;                //amount to shift mant
                a_m=({1'b1,bi}>>shift);     //insert 1 and shift
                sum[14:10]=ai[14:10];       //update exponent
                if(ai[15]^bi[15]) a_m=((~a_m)+1'b1);    //check for signed case & process accordingly
                sum[9:0]=ai[9:0];           //use sum to pass greater mantissa
            end
        1:  //b>a
            begin
                shift=bi-ai;                //amount to shift mant
                a_m=({1'b1,bi}>>shift);     //insert 1 and shift
                sum[14:10]=bi[14:10];       //update exponent
                if(ai[15]^bi[15]) a_m=((~a_m)+1'b1);    //check for signed case & process accordingly
                sum[9:0]=bi[9:0];           //use sum to pass greater mantissa
            end
        2:  //b=a, !=0
            begin
                a_m={1'b1,ai[9:0]};
                sum[9:0]=bi[9:0];
            end
        endcase
        
endmodule    