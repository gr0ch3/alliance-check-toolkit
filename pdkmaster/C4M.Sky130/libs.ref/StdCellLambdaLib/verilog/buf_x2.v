/*                                                                      */
/*  Avertec Release v3.4p5 (64 bits on Linux 6.6.13+bpo-amd64)          */
/*  [AVT_only] host: fsdev                                              */
/*  [AVT_only] arch: x86_64                                             */
/*  [AVT_only] path: /opt/tasyag-3.4p5/bin/avt_shell                    */
/*  argv:                                                               */
/*                                                                      */
/*  User: verhaegs                                                      */
/*  Generation date Wed May 29 10:55:23 2024                            */
/*                                                                      */
/*  Verilog data flow description generated from `buf_x2`               */
/*                                                                      */


`timescale 1 ps/1 ps

module buf_x2 (i, q);

  input  i;
  output q;

  wire v_i_n;

  assign v_i_n = ~(i);

  assign q = ~(v_i_n);

endmodule