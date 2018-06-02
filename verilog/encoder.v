/*Encoder*/
//# describes an encoder implmentation

module encoder
  #( parameter NUM_BITS = 16,  // number of bits to encode
     parameter OUT_BITS = 4    // output bits
     )
   (
    output [OUT_BITS-1:0] binary_out , //  encoder Output
    input [NUM_BITS-1:0]  encoder_in , //  encoder Input
    input 		  enable       //  Enable for the encoder
    );
   
   logic [OUT_BITS-1:0]   binary_out;
   
   always @ (enable or encoder_in)
     begin
	binary_out = 0;
	
	if (enable) begin
	   case (encoder_in)
	     16'h0002 : binary_out = 1;
	     16'h0004 : binary_out = 2;
	     16'h0008 : binary_out = 3;
	     16'h0010 : binary_out = 4;
	     16'h0020 : binary_out = 5;
	     16'h0040 : binary_out = 6;
	     16'h0080 : binary_out = 7;
	     16'h0100 : binary_out = 8;
	     16'h0200 : binary_out = 9;
	     16'h0400 : binary_out = 10;
	     16'h0800 : binary_out = 11;
	     16'h1000 : binary_out = 12;
	     16'h2000 : binary_out = 13;
	     16'h4000 : binary_out = 14;
	     16'h8000 : binary_out = 15;
	   endcase
	end
     end
   
endmodule
