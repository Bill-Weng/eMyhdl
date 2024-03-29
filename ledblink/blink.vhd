-- File: blink.vhd
-- Generated by MyHDL 0.10
-- Date: Sat Oct 19 11:14:41 2019


library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;
use std.textio.all;

use work.pck_myhdl_010.all;

entity blink is
    port (
        clock: in std_logic;
        enable: in std_logic;
        led: out std_logic
    );
end entity blink;


architecture MyHDL of blink is



signal countor: unsigned(11 downto 0);

begin




inc: process (clock) is
begin
    if rising_edge(clock) then
        if bool(enable) then
            countor <= (countor + 1);
        end if;
    end if;
end process inc;


led <= countor(11);

end architecture MyHDL;
