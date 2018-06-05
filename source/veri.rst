Documentation for RTL common and shared files
*********************************************
This is the documentation page for all the common RTL files

Commmon files
=========================

.. veri:module:: encoder

   describes an encoder implmentation
		 
   :parameter NUM_BITS: number of bits to encode
   :parameter OUT_BITS: output bits
			
.. csv-table:: 
   :header: "Signals direction","Signal type","Signal name","comments"
   :widths: 20 50 20 50

   "input",":veri:struct:`encoder_t`","encoder_in","encoder input"
   "input","logic","enable","Enable for the encoder"
   "output","logic [OUT_BITS-1:0]","binary_out","encoder output"

.. container:: toggle

   .. container:: header

      *[source]*

   .. literalinclude:: ../verilog/encoder.v
      :language: verilog      

   
-------------------------

.. veri:module:: decoder

   describes an decoder implmentation   
		 
   :parameter NUM_BITS: number of bits to decode
   :parameter IN_BITS: input bits

.. csv-table:: 
   :header: "Signal direction","Signal type","Signal name","comments"
   :widths: 20 50 20 50

   "input","logic [IN_BITS-1:0]","binary_in","decoder input"
   "input","logic","enable","Enable for the decoder"
   "output",":veri:struct:`decoder_t`","decoder_out","decoder output"

.. container:: toggle

   .. container:: header

      *[source]*

   .. literalinclude:: ../verilog/decoder.v
      :language: verilog      
   
