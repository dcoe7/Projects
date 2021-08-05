//David Coe
//EE278
//10x10 Unsigned Multiplier
//10-1-19

`timescale 1ns / 1ps

module umult10x10 (clk,St,Mplier,Mcand,Prod,ACC,done,pstate);
    input clk;
    input St;
    input [9:0]Mplier;
    input [9:0]Mcand;
    output [20:0] Prod;
    output [20:0] ACC;
    output done;
    output [4:0]pstate;
    
    reg done;
    reg [4:0]pstate, nstate;
    reg [20:0] Prod; 
    parameter   s0= 5'b00000, 
                s1= 5'b00001, 
                s2= 5'b00010, 
                s3= 5'b00011, 
                s4= 5'b00100, 
                s5= 5'b00101, 
                s6= 5'b00110, 
                s7= 5'b00111, 
                s8= 5'b01000, 
                s9= 5'b01001,
                s10=5'b01010,
                s11=5'b01011,
                s12=5'b01100,
                s13=5'b01101,
                s14=5'b01110,
                s15=5'b01111,
                s16=5'b10000, 
                s17=5'b10001, 
                s18=5'b10010, 
                s19=5'b10011, 
                s20=5'b10100, 
                s21=5'b10101;
    
    reg [20:0] ACC;   //accumulator
    wire M;
    assign M = ACC[0];
    always @(posedge clk or posedge St)
        if (St) begin 
        pstate = s0;
        done = 1'b0;
                end
        else pstate = nstate;
    always @(pstate)  //state transition
        case (pstate)
            s0:  if(St) nstate = s1;
            s1:  if(M) nstate = s2; else nstate = s3;
            s2:  nstate = s3;
            s3:  if(M) nstate = s4; else nstate = s5;
            s4:  nstate = s5;
            s5:  if(M) nstate = s6; else nstate = s7;
            s6:  nstate = s7;
            s7:  if(M) nstate = s8; else nstate = s9;
            s8:  nstate = s9;
            s9:  if(M) nstate = s10; else nstate = s11;
            s10:  nstate = s11;
            s11:  if(M) nstate = s12; else nstate = s13;
            s12:  nstate = s13;
            s13:  if(M) nstate = s14; else nstate = s15;
            s14:  nstate = s15;
            s15:  if(M) nstate = s16; else nstate = s17;
            s16:  nstate = s17;
            s17:  if(M) nstate = s18; else nstate = s19;
            s18:  nstate = s19;
            s19:  if(M) nstate = s20; else nstate = s21;
            s20:  nstate = s21;
            s21:  nstate = s0;
        endcase
    always @(pstate)  //Output (Action)
        case (pstate)
            s0:  begin
                ACC[20:10] = 11'b0;
                ACC[9:0] = Mplier;
                done = 1'b0;
                 end
            s1:  if (ACC[0])ACC[20:10] = ACC[20:10] + {1'b0, Mcand};    //ADD
            s2:  ACC = {1'b0, ACC[20:1]};                               //SHIFT     1b
            s3:  if (ACC[0])ACC[20:10] = ACC[20:10] + {1'b0, Mcand};    //ADD
            s4:  ACC = {1'b0, ACC[20:1]};                               //SHIFT     2b
            s5:  if (ACC[0])ACC[20:10] = ACC[20:10] + {1'b0, Mcand};    //ADD
            s6:  ACC = {1'b0, ACC[20:1]};                               //SHIFT     3b
            s7:  if (ACC[0])ACC[20:10] = ACC[20:10] + {1'b0, Mcand};    //ADD
            s8:  ACC = {1'b0, ACC[20:1]};                               //SHIFT     4b
            s9:  if (ACC[0])ACC[20:10] = ACC[20:10] + {1'b0, Mcand};    //ADD
            s10:  ACC = {1'b0, ACC[20:1]};                              //SHIFT     5b
            s11:  if (ACC[0])ACC[20:10] = ACC[20:10] + {1'b0, Mcand};   //ADD
            s12:  ACC = {1'b0, ACC[20:1]};                              //SHIFT     6b
            s13:  if (ACC[0])ACC[20:10] = ACC[20:10] + {1'b0, Mcand};   //ADD
            s14:  ACC = {1'b0, ACC[20:1]};                              //SHIFT     7b
            s15:  if (ACC[0])ACC[20:10] = ACC[20:10] + {1'b0, Mcand};   //ADD
            s16:  ACC = {1'b0, ACC[20:1]};                              //SHIFT     8b
            s17:  if (ACC[0])ACC[20:10] = ACC[20:10] + {1'b0, Mcand};   //ADD
            s18:  ACC = {1'b0, ACC[20:1]};                              //SHIFT     9b
            s19:  if (ACC[0])ACC[20:10] = ACC[20:10] + {1'b0, Mcand};   //ADD
            s20:  ACC = {1'b0, ACC[20:1]};                              //SHIFT     10b
            s21:
                begin  
                    done = 1'b1;
                    Prod = ACC;
                end
        endcase
endmodule


