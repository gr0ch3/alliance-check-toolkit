--  
--  Avertec Release v3.4p5 (64 bits on Linux 6.7.12+bpo-amd64)
--  [AVT_only] host: fsdev
--  [AVT_only] arch: x86_64
--  [AVT_only] path: /opt/tasyag-3.4p5/bin/avt_shell
--  argv: 
--  
--  User: verhaegs
--  Generation date Tue Sep 24 13:35:35 2024
--  
--  VHDL data flow description generated from `xor2_x0`
--  

library IEEE;
use IEEE.std_logic_1164.all;

-- Entity Declaration

ENTITY xor2_x0 IS
  PORT (
         i0 : in    STD_LOGIC;
         i1 : in    STD_LOGIC;
          q : out   STD_LOGIC
  );
END xor2_x0;

-- Architecture Declaration

ARCHITECTURE RTL OF xor2_x0 IS
  SIGNAL i1_n : STD_LOGIC;
  SIGNAL i0_n : STD_LOGIC;

BEGIN


  i0_n <= not (i0);
  i1_n <= not (i1);

  q <= ((not (i0_n) and not (i1)) or (not (i0_n) and not (i0)) or (not (i1_n)
and not (i1)) or (not (i1_n) and not (i0)));

END;
