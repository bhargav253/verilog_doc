Documentation for RTL common and shared files
*********************************************
This is the documentation page for all the common RTL files

Commmon files
=========================

.. veri:module:: encoder

   :parameter NUM_BITS: number of bits to encode
   :parameter OUT_BITS: output bits

.. list-table:: 
   :widths: 20 50 20 50
   :header-rows: 1

   * - Signal direction
     - Signal type
     - Signal name
     - comments
   * - input
     - logic [NUM_BITS-1:0]
     - encoder_in
     - encoder input
   * - input
     - logic
     - enable
     - Enable for the encoder
   * - output
     - logic [OUT_BITS-1:0]
     - binary_out
     - encoder output

-------------------------

.. veri:module:: decoder

   :parameter NUM_BITS: number of bits to decode
   :parameter IN_BITS: input bits

.. list-table:: 
   :widths: 20 50 20 50
   :header-rows: 1

   * - Signal direction
     - Signal type
     - Signal name
     - comments
   * - input
     - logic [IN_BITS-1:0]
     - binary_in
     - deccoder input
   * - input
     - logic
     - enable
     - Enable for the decoder
   * - output
     - logic [NUM_BITS-1:0]
     - decoder_out
     - decoder output
