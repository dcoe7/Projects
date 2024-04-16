#-----------------------------------------------------------------------------
# VHDL TB Gen
#-----------------------------------------------------------------------------
# Revision History:
# Date      Author     Comment
# 16APR2024 TB Gen     Created
#-----------------------------------------------------------------------------
# Description:
# This script generates a testbench from a VHDL source file for use in
# Notepad++.
#-----------------------------------------------------------------------------
import sys
import time
import os
#define company
company = "UserCompany"
file_path = sys.argv[2]
# file_path = "C:/user_path/source_file.vhd"
file_dir,file_name = os.path.split(file_path)
file,file_ext = os.path.splitext(file_name)
# check that the source file is VHDL
if file_ext != ".vhd":
    print("Not a .vhd file")
else:
    with open(os.path.join(file_dir,'{}_tb.vhd'.format(file)),'wb') as tb_file, open(file_path, 'rb') as src_file:
        tb_file.write(b"-------------------------------------------------------------------------------\n")
        tb_file.write(b"-- Author: TB Gen\n")
        tb_file.write(bytes("-- Copyright: {0} {1}\n".format(company,time.strftime("%Y")),encoding='utf8'))
        tb_file.write(b"-------------------------------------------------------------------------------\n")
        tb_file.write(b"-- Revision History:\n")
        tb_file.write(b"-- Date      Author     Comment\n")
        tb_file.write(bytes("-- {0} TB Gen     Created @ {1}\n".format(time.strftime("%d%b%Y").upper(),time.strftime("%T")),encoding='utf8'))
        tb_file.write(b"-------------------------------------------------------------------------------\n")
        tb_file.write(b"-- Description:\n")
        tb_file.write(bytes("-- This is an {} testbench.\n".format(file_name),encoding='utf8'))
        tb_file.write(b"-------------------------------------------------------------------------------\n\n")
        # add libraries
        tb_file.write(b"library IEEE;\n")
        tb_file.write(b"use IEEE.std_logic_1164.all;\n")
        tb_file.write(b"use IEEE.numeric_std.all;\n\n")
        tb_file.write(b"library osvvm;\n")
        tb_file.write(b"use osvvm.RandomPkg.all;\n")
        tb_file.write(b"use osvvm.CoveragePkg.all;\n\n")
        # script var declarations
        line_numb = 0
        ent_label = 0
        generic_1 = 0
        port_1 = 0
        entity_1 = 0
        ports_1 = 0
        signals_1 = 0
        tb_signals_1 = 0
        p_map_1 = 0
        p_map_2 = 0
        stim_1 = 0
        wb_bus = 0
        generics = list()
        ports = list()
        # start rtl processing
        for line in src_file:
            line_numb +=1
            line = str(line)
            line = line.strip()
            line = line.replace("b'",'')
            line = line.replace('b"','')
            line = line.replace(r'\t','')
            line = line.replace(r'\n"','')
            line = line.replace(r'\n','')
            if line.find("wb_clk"):
                wb_bus = 1
            if line.endswith("'"):
                line = line[:(len(line)-1)]
            if stim_1 == 0:
            # copy entity
                if line.startswith("--"):
                    commentfound = 1
                elif line.find("entity") != -1:
                    if entity_1 == 0:
                        uut_name = line.replace("entity",'')
                        uut_name = uut_name.replace("is",'').strip()
                        end = uut_name.rfind(" ")
                        # uut_name = uut_name[:end].rstrip()
                        tb_file.write(bytes("entity {}_tb is\n".format(uut_name),encoding='utf8'))
                elif line.find("generic") != -1:
                    generic_1 = 1
                    tb_file.write(bytes("    generic (\n",encoding='utf8'))
                    # line_numb +=1
                elif line.find(":in ") != -1:
                    ports.append(line)
                elif line.find(": in ") != -1:
                    ports.append(line)
                elif line.find(": out ") != -1:
                    ports.append(line)
                elif line.find(":out ") != -1:
                    ports.append(line)
                elif line.find(":inout ") != -1:
                    ports.append(line)
                elif line.find(": inout ") != -1:
                    ports.append(line)
                elif line == '':
                    newline = 1
                elif line.find(":") != -1:
                    if entity_1 == 0:
                        tb_file.write(bytes("        {}\n".format(line),encoding='utf8'))
                        generics.append(line)
                elif line.find("port") != -1:
                    if entity_1 == 0:
                        port_1 = 1
                        tb_file.write(bytes("    );\n".format(line),encoding='utf8'))
                        tb_file.write(bytes("end;\n".format(line),encoding='utf8'))
                        entity_1 = 1
            # add architecture
                        tb_file.write(bytes("architecture tb of {}_tb is\n\n".format(uut_name),encoding='utf8'))
            # generate component
                        tb_file.write(bytes("    -- uut declaration\n",encoding='utf8'))
                        tb_file.write(bytes("    component {}\n".format(uut_name),encoding='utf8'))
                        tb_file.write(bytes("        generic (\n",encoding='utf8'))
                        g_len = len(generics)
                        for i in range(g_len):
                            end = generics[i].rfind(":=")
                            g_line = generics[i]
                            g_truncated = g_line[:end].rstrip()
                            if i == g_len-1:
                                tb_file.write(bytes("            {}".format(g_truncated),encoding='utf8'))
                            else:
                                tb_file.write(bytes("            {};".format(g_truncated),encoding='utf8'))
                        tb_file.write(bytes("\n        );",encoding='utf8'))
                        tb_file.write(bytes("\n        port (",encoding='utf8'))
                elif signals_1 == 0:
                    if entity_1 == 1:
                        if ports_1 == 0:
                            p_len = len(ports)
                            for i in range(p_len):
                                p_line = ports[i]
                                if i == p_len-1:
                                    ports_1 = 1
                                    tb_file.write(bytes("\n            {}".format(p_line),encoding='utf8'))
                                    tb_file.write(bytes("\n        );",encoding='utf8'))
                                    tb_file.write(bytes("\n    end component;\n",encoding='utf8'))
                                    tb_file.write(bytes("\n    -- uut signals",encoding='utf8'))
                                else:
                                    tb_file.write(bytes("\n            {}".format(p_line),encoding='utf8'))
            # generate signals
                        else:
                            for i in range(p_len):
                                p_line = ports[i]
                                port_type = [": in  ",": out  ",": inout  ",": in ",": out ",": inout ",": in",": out",": inout"]
                                for type in port_type:
                                    p_line = p_line.replace(type,' : ')
                                    comment = p_line.rfind("--")
                                    p_truncated = p_line[:comment].rstrip()
                                if i == p_len-1:
                                    signals_1 = 1
                                    tb_file.write(bytes("\n    signal {} := '0';".format(p_truncated),encoding='utf8'))
                                elif p_truncated.find("std_logic;") != -1:
                                    p_truncated = p_truncated.replace(";",'')
                                    tb_file.write(bytes("\n    signal {} := '0';".format(p_truncated),encoding='utf8'))
                                elif p_truncated.find(");") != -1:
                                    p_truncated = p_truncated.replace(";",'')
                                    tb_file.write(bytes("\n    signal {} := (others => '0');".format(p_truncated),encoding='utf8'))
                                else:
                                    tb_file.write(bytes("\n    signal {}".format(p_truncated),encoding='utf8'))
            # add test signals
                elif signals_1 == 1:
                    if tb_signals_1 == 0:
                        tb_file.write(bytes("\n\n    -- test signals",encoding='utf8'))
                        tb_file.write(bytes("\n    signal clk              : std_logic := '0';",encoding='utf8'))
                        tb_file.write(bytes("\n    signal reset            : std_logic := '0';",encoding='utf8'))
                        tb_file.write(bytes("\n    signal sim_done         : boolean := FALSE;",encoding='utf8'))
                        tb_file.write(bytes("\n    signal error            : std_logic_vector(1 downto 0)  := (others => '0');\n",encoding='utf8'))
                        tb_file.write(bytes("\n    -- constants",encoding='utf8'))
                        tb_file.write(bytes("\n    constant CLK_PERIOD     : time := 10 ns;\n",encoding='utf8'))
                        if wb_bus == 1:
                            tb_file.write(bytes("    constant WB_CLK_PERIOD  : time := 10 ns;\n",encoding='utf8'))
            # add coverpoint var
                        tb_file.write(bytes("\n    -- coverpoint variables",encoding='utf8'))
                        tb_file.write(bytes("\n    shared variable cp_error    :covptype;\n\n",encoding='utf8'))
                        tb_signals_1 = 1
                    elif tb_signals_1 == 1:
                        if p_map_1 == 0:
            # generate global procedures
                            tb_file.write(bytes("-- Global Procedures -------------------------------------------\n\n",encoding='utf8'))
                            tb_file.write(bytes("    -- alternative to report function",encoding='utf8'))
                            tb_file.write(bytes('\n    procedure nowechol(arg : in string := ""; unit :  time := ns) is',encoding='utf8'))
                            tb_file.write(bytes("\n        begin",encoding='utf8'))
                            tb_file.write(bytes('\n            std.textio.write(std.textio.output, arg & to_string(NOW, unit) & " " & LF);',encoding='utf8'))
                            tb_file.write(bytes("\n    end procedure nowechol;\n",encoding='utf8'))
                            tb_file.write(bytes('\n    -- report without timestamp',encoding='utf8'))
                            tb_file.write(bytes('\n    procedure echol(arg : in string := "") is',encoding='utf8'))
                            tb_file.write(bytes("\n        begin",encoding='utf8'))
                            tb_file.write(bytes("\n            std.textio.write(std.textio.output, arg & LF);",encoding='utf8'))
                            tb_file.write(bytes("\n    end procedure echol;\n",encoding='utf8'))
                            tb_file.write(bytes("\n----------------------------------------------------------------",encoding='utf8'))
            # generate port map
                            tb_file.write(bytes("\nbegin\n",encoding='utf8'))
                            tb_file.write(bytes("\n    -- uut instantiation",encoding='utf8'))
                            tb_file.write(bytes("\n    uut: {}".format(uut_name),encoding='utf8'))
                            tb_file.write(bytes("\n        generic map (",encoding='utf8'))
                            for i in range(g_len):
                                end = generics[i].find(":")
                                g_line = generics[i]
                                g_truncated = g_line[:end]
                                if i == g_len-1:
                                    tb_file.write(bytes("\n            {0}=> {1}\n        )".format(g_truncated,g_truncated.rstrip()),encoding='utf8'))
                                    p_map_1 = 1
                                else:
                                    tb_file.write(bytes("\n            {0}=> {1},".format(g_truncated,g_truncated.rstrip()),encoding='utf8'))
                        elif p_map_2 == 0:
                            tb_file.write(bytes("\n        port map (\n",encoding='utf8'))
                            for i in range(p_len):
                                end = ports[i].find(":")
                                p_line = ports[i]
                                p_line = p_line[:end]
                                if i == p_len-1:
                                    tb_file.write(bytes("            {0}=> {1}\n        );".format(p_line,p_line.rstrip()),encoding='utf8'))
                                    p_map_2 = 1
                                elif p_line.find("clk") != -1:
                                    if p_line.find("wb_clk") == -1:
                                        tb_file.write(bytes("            {0}=> clk,\n".format(p_line),encoding='utf8'))
                                    else:
                                        tb_file.write(bytes("            {0}=> {1},\n".format(p_line,p_line.rstrip()),encoding='utf8'))
                                elif p_line.find("clock") != -1:
                                    tb_file.write(bytes("            {0}=> clk,\n".format(p_line),encoding='utf8'))
                                elif p_line.find("rst") != -1:
                                    tb_file.write(bytes("            {0}=> reset,\n".format(p_line),encoding='utf8'))
                                elif p_line.find("reset") != -1:
                                    tb_file.write(bytes("            {0}=> reset,\n".format(p_line),encoding='utf8'))
                                else:
                                    tb_file.write(bytes("            {0}=> {1},\n".format(p_line,p_line.rstrip()),encoding='utf8'))
            # add clock
                        elif p_map_2 == 1:
                            if stim_1 == 0:
                                # wb clk
                                if wb_bus ==1:
                                    tb_file.write(bytes("\n\n    -- wishbone clk generator",encoding='utf8'))
                                    tb_file.write(bytes("\n    wb_clk_gen: process begin",encoding='utf8'))
                                    tb_file.write(bytes("\n        while not sim_done loop",encoding='utf8'))
                                    tb_file.write(bytes("\n            wait for WB_CLK_PERIOD/2;",encoding='utf8'))
                                    tb_file.write(bytes("\n            wb_clk_i <= not wb_clk_i;",encoding='utf8'))
                                    tb_file.write(bytes("\n        end loop;",encoding='utf8'))
                                    tb_file.write(bytes("\n        wait;",encoding='utf8'))
                                    tb_file.write(bytes("\n    end process wb_clk_gen;",encoding='utf8'))
                                # clk
                                tb_file.write(bytes("\n\n    -- clk generator",encoding='utf8'))
                                tb_file.write(bytes("\n    clk_gen: process begin",encoding='utf8'))
                                tb_file.write(bytes("\n        while not sim_done loop",encoding='utf8'))
                                tb_file.write(bytes("\n            wait for CLK_PERIOD/2;",encoding='utf8'))
                                tb_file.write(bytes("\n            clk <= not clk;",encoding='utf8'))
                                tb_file.write(bytes("\n        end loop;",encoding='utf8'))
                                tb_file.write(bytes("\n        wait;",encoding='utf8'))
                                tb_file.write(bytes("\n    end process clk_gen;",encoding='utf8'))
            # add reset
                                tb_file.write(bytes("\n\n    -- reset generator",encoding='utf8'))
                                tb_file.write(bytes("\n    reset_gen: process begin",encoding='utf8'))
                                tb_file.write(bytes("\n        reset <= '1';",encoding='utf8'))
                                tb_file.write(bytes("\n        wait for 50 ns;",encoding='utf8'))
                                tb_file.write(bytes("\n        reset <= '0';",encoding='utf8'))
                                tb_file.write(bytes("\n        wait;",encoding='utf8'))
                                tb_file.write(bytes("\n    end process reset_gen;",encoding='utf8'))
            # add stimulus block
                                tb_file.write(bytes("\n\n----------------------------------------------------------------",encoding='utf8'))
                                tb_file.write(bytes("\n\nStimulus_Process: block begin",encoding='utf8'))
                                tb_file.write(bytes("\n\n    uut_stimuli: process",encoding='utf8'))
            # add stimulus procedures
                            #tb_file.write(bytes("-- Stimulus Procedures -------------------------------------------\n\n",encoding='utf8'))
            # add stimulus process
                                tb_file.write(bytes("\n        -- declare random variables",encoding='utf8'))
                                tb_file.write(bytes("\n        -- variable rnd_var    : RandomPType;",encoding='utf8'))
                                tb_file.write(bytes("\n    begin",encoding='utf8'))
                                tb_file.write(bytes("\n        -- init random variables",encoding='utf8'))
                                tb_file.write(bytes("\n        -- rnd_var.initseed(rnd_var'instance_name);",encoding='utf8'))
                                tb_file.write(bytes("\n        wait for 100 ns;",encoding='utf8'))
                                tb_file.write(bytes("\n        wait until clk = '1';",encoding='utf8'))
                                tb_file.write(bytes("\n        wait for 100 ps;",encoding='utf8'))
                                tb_file.write(bytes("\n\n        -- end simulation run",encoding='utf8'))
                                tb_file.write(bytes("\n        sim_done <= TRUE;",encoding='utf8'))
                                tb_file.write(bytes('\n        report "Simulation Run Complete" severity note;',encoding='utf8'))
                                tb_file.write(bytes("\n        wait;",encoding='utf8'))
                                tb_file.write(bytes("\n\n    end process uut_stimuli;",encoding='utf8'))
                                tb_file.write(bytes("\nend block Stimulus_Process;",encoding='utf8'))
            # add error process
                                tb_file.write(bytes("\n\n----------------------------------------------------------------",encoding='utf8'))
                                tb_file.write(bytes("\n\nError_Detect: block begin",encoding='utf8'))
                                tb_file.write(bytes("\n\n    -- init coverpoints",encoding='utf8'))
                                tb_file.write(bytes("\n    Cover_Init: process begin",encoding='utf8'))
                                tb_file.write(bytes("\n        cp_error.addbins(genbin(1));",encoding='utf8'))
                                tb_file.write(bytes("\n        wait;",encoding='utf8'))
                                tb_file.write(bytes("\n    end process Cover_Init;",encoding='utf8'))
                                tb_file.write(bytes("\n\n    -- sample coverpoints",encoding='utf8'))
                                tb_file.write(bytes("\n    Cover_Sample: process begin",encoding='utf8'))
                                tb_file.write(bytes("\n        loop",encoding='utf8'))
                                tb_file.write(bytes("\n            wait until error(0) = '1';",encoding='utf8'))
                                tb_file.write(bytes("\n            if error(0) = '1' then",encoding='utf8'))
                                tb_file.write(bytes("\n                cp_error.icover(to_integer(error(0)));",encoding='utf8'))
                                tb_file.write(bytes("\n            end if;",encoding='utf8'))
                                tb_file.write(bytes("\n            exit when sim_done = TRUE;",encoding='utf8'))
                                tb_file.write(bytes("\n            wait until error(0) = '0';",encoding='utf8'))
                                tb_file.write(bytes("\n        end loop;",encoding='utf8'))
                                tb_file.write(bytes("\n    end process Cover_Sample;",encoding='utf8'))
                                tb_file.write(bytes("\n\n    -- report coverpoints",encoding='utf8'))
                                tb_file.write(bytes("\n    Cover_Report: process begin",encoding='utf8'))
                                tb_file.write(bytes("\n        wait until sim_done = TRUE;",encoding='utf8'))
                                tb_file.write(bytes('\n        echol("---------------------------- Errors Present ----------------------------");',encoding='utf8'))
                                tb_file.write(bytes("\n        cp_error.writebin;",encoding='utf8'))
                                tb_file.write(bytes("\n        wait;",encoding='utf8'))
                                tb_file.write(bytes("\n    end process Cover_Report;",encoding='utf8'))
                                tb_file.write(bytes("\n\nend block Error_Detect;",encoding='utf8'))
                                tb_file.write(bytes("\n\nend tb;",encoding='utf8'))
                                stim_1 = 1
            else:
                break

        src_file.close()
        tb_file.close()
        print("{}_tb.vhd generated on {}".format(uut_name,time.strftime("%A %B %Y %T")))
        print("Saved at {}".format(file_path))