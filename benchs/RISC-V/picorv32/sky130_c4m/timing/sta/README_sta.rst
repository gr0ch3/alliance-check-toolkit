README_sta.rst
=================

Marie-Minerve Louerat

24 April, 2024 : STA of picorv32 and 
                 generation of a timing path (transistor level) for simualtion with ngspice
---------------------------------------------------------------------------------------------------

/alliance-check-toolkit/benchs/picorv32/sky130_c4m/timing/sta/README_sta.rst

Goal
--------
This directory contains the files to analyze the timing response of:
  * picorv32_cts_r.spi, (C4M.Sky130 standard cell library)
    from picorv32 provided by YosysHQ
    synthesis with Yosys, P&R with Coriolis
    by ALi Oudhriri and Mazher Iqbal
    it is a wip design
    
by static timing analysis with Hitas
to be compared with ngspice simulation

Note
----
Transistor model files have to be tuned, compared to those used by ngspice, as they require :
  * full path of the file in a hierarchical description
  * level = 14 for analysis BSIM4 model, if the reference simulator (parameters provided by the foundry)
    is ngspice
  * for simulation with ngspice of a generated netlist of a slected timing path by HiTas,
    at transistor level,
    models of transistors have to instantiate the model directly MWWW (not the .SUBCKT wrapper).


Subdirectories
---------------
hitas:  contains the tcl commands to launch HiTas

Environment
-----------
Launch:
  bash
  source ./hitas/avt_env.sh
  ./hitas/clean removes files generated by HiTas

Runing HiTas
----------------
example:
1. Building the timing database
   ./hitas/db_ng.tcl

creates picorv32_cts_r.dtx and other files

(see picorv32_cts_r.rep and the cone netlist: picorv32_cts_r.cns)

2. Report critical paths
   ./hitas/report_picorv32_cts_r.tcl

provides the picorv32_cts_r.paths file that shows the 10 longest paths of the picorv32_cts_r.spi, 
with tha path details (propagation delays of the logical gates).

Generating the transistor level netlist of a selected timing path and performing ngspice simulation
---------------------------------------------------------------------------------------------------
When the timing data base is generated (.dtx file), you may run:

    ./hitas/paths_select_simu.tcl

it uses 
    picorv32_cts_r.dtx

it generates:
    picorv32_cts_r_ext.spi     : transistor-level netlist of the selected timing path
                                 compliant with ngspice
    cmd_picorv32_cts_r_ext.spi : input file for ngspice, including 
                                 picorv32_cts_r_ext.spi netlist model 
                                 and commands to compute gate delays
                                 compliant with ngspice

it automatically launches the command:
    ngspice -b cmd_picorv32_cts_r_ext.spi

which generates:
    cmd_picorv32_cts_r_ext.out : ngspice simulation result
                                 with delays estimation of
                                 the selected timing path
    picorv32_cts_r.selectedPath: HiTas estimation of the same timing path
                                 that can be compared
                                           

Runing the graphical interface Xtas
--------------------------------------
run   xtas
In the menu, select:
   file/open picorv32_cts_r.dtx

Then: 
   Tools/Get Paths

Then click on a path and choose in the menu:
   path Detail


