--  
--  Avertec Release v3.4p5 (64 bits on Linux 6.7.12+bpo-amd64)
--  [AVT_only] host: fsdev
--  [AVT_only] arch: x86_64
--  [AVT_only] path: /opt/tasyag-3.4p5/bin/avt_shell
--  argv: 
--  
--  User: verhaegs
--  Generation date Tue Sep 24 13:35:36 2024
--  
--  VHDL data flow description generated from `IOPadIn`
--  

library IEEE;
use IEEE.std_logic_1164.all;

-- Entity Declaration

ENTITY IOPadIn IS
  PORT (
         p2c : out   STD_LOGIC;
         pad : in    STD_LOGIC
  );
END IOPadIn;

-- Architecture Declaration

ARCHITECTURE RTL OF IOPadIn IS
  SIGNAL LevelDown_padres_n : STD_LOGIC;
  SIGNAL yag_zero : STD_LOGIC;
  SIGNAL yag_one : STD_LOGIC;

BEGIN


  yag_one <= '1';
  yag_zero <= '0';
  LevelDown_padres_n <= not (pad);

  p2c <= not (LevelDown_padres_n);

END;
