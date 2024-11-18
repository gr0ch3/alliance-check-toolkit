#!/usr/bin/env avt_shell

#############################################################
# Timing Database Generation                                #
#############################################################

# General config
avt_config avtLibraryDirs .

avt_config tasGenerateConeFile yes
avt_config avtVerboseConeFile yes 

avt_config simVthHigh 0.8
avt_config simVthLow 0.2
avt_config simSlope 10e-12 
avt_config simTemperature 25.0

avt_config simToolModel hspice
avt_config tasGenerateDetailTimingFile yes

avt_LoadFile psp103_nqs.osdi osdi

# Files of transistor model of the technology, that may require modifications
#

avt_LoadFile test.spice spice

# Database generation
set fig [hitas inv_1]

set temp   [ttv_GetTimingFigureProperty $fig TEMP]
set supply [ttv_GetTimingFigureProperty $fig DEF_SUPPLY]

set slope  [ttv_GetTimingFigureProperty $fig DEF_SLOPE]
set cload   [ttv_GetTimingFigureProperty $fig DEF_LOAD]
set date   [ttv_GetTimingFigureProperty $fig DATE]

puts ""
puts "Power supply: [ttv_GetTimingFigureProperty $fig DEF_SUPPLY]V"
puts "Temperature: [ttv_GetTimingFigureProperty $fig TEMP] deg C"
set sig [ttv_GetTimingSignal $fig out]

puts ""
puts "out signal capacitance: [ttv_GetTimingSignalProperty $sig CAPA]F"


puts "input slope     : $slope s"
puts "generation date : $date"

puts "output load     : $cload"
