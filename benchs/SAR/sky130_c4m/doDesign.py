#!/usr/bin/env python3

import sys
import traceback
import CRL
import helpers
helpers.loadUserSettings()
from   helpers.io import ErrorMessage, WarningMessage
from   helpers    import trace, l, u, n
import plugins
from   Hurricane  import DbU, Breakpoint
from   plugins.alpha.block.block          import Block
from   plugins.alpha.block.configuration  import IoPin, GaugeConf
from   plugins.alpha.block.spares         import Spares
from   plugins.alpha.core2chip.sky130     import CoreToChip
from   plugins.alpha.chip.configuration   import ChipConf
from   plugins.alpha.chip.chip            import Chip


af = CRL.AllianceFramework.get()


def scriptMain ( **kw ):
    """The mandatory function to be called by Coriolis CGT/Unicorn."""
    global af
    rvalue = True
    try:
       #helpers.setTraceLevel( 550 )
        Breakpoint.setStopLevel( 100 )
        buildChip = False
        cell, editor = plugins.kwParseMain( **kw )
        cell = af.getCell( 'sarlogic', CRL.Catalog.State.Logical )
        if editor:
            editor.setCell( cell ) 
            editor.setDbuMode( DbU.StringModePhysical )

        m1pitch    = u(0.46)
        m2pitch    = u(0.51)

        ioPinsSpec = [ (IoPin.EAST |IoPin.A_BEGIN, 'res({})'        , 20*m1pitch, 10*m1pitch,  8)
                     , (IoPin.EAST |IoPin.A_BEGIN, 'eoc'            , 5 *m1pitch,         0 ,  1)

                     , (IoPin.WEST |IoPin.A_BEGIN, 'cmp'            , 50*m1pitch,         0 ,  1)                     

                     , (IoPin.NORTH|IoPin.A_BEGIN, 'clk'            ,  100*m2pitch,       0 ,  1)
                     , (IoPin.NORTH|IoPin.A_BEGIN, 'rst'            ,  110*m2pitch,       0 ,  1)
                     , (IoPin.NORTH|IoPin.A_BEGIN, 'soc'            ,  120*m2pitch,       0 ,  1)

                     , (IoPin.SOUTH|IoPin.A_BEGIN, 'dac_control({})',  20*m2pitch,10*m2pitch,  8)
                     , (IoPin.SOUTH|IoPin.A_BEGIN, 'se'             ,  10*m2pitch,        0 ,  1)
                     ]
        #sarlogicConf = ChipConf( cell, ioPins=ioPinsSpec, ioPads=ioPadsSpec ) 
        sarlogicConf = ChipConf( cell, ioPins=ioPinsSpec) 
        sarlogicConf.cfg.etesian.bloat               = 'disabled'
       #arlet6502Conf.cfg.etesian.bloat               = 'nsxlib'
        sarlogicConf.cfg.etesian.aspectRatio         = 1.0
       # etesian.spaceMargin is ignored if the coreSize is directly set.
        sarlogicConf.cfg.etesian.spaceMargin         = 0.02
        sarlogicConf.cfg.anabatic.searchHalo         = 2
        sarlogicConf.cfg.anabatic.globalIterations   = 10
        sarlogicConf.cfg.anabatic.topRoutingLayer    = 'm4'
        sarlogicConf.cfg.katana.hTracksReservedLocal = 6
        sarlogicConf.cfg.katana.vTracksReservedLocal = 3
        sarlogicConf.cfg.katana.hTracksReservedMin   = 3
        sarlogicConf.cfg.katana.vTracksReservedMin   = 1
        sarlogicConf.cfg.katana.trackFill            = 0
        sarlogicConf.cfg.katana.runRealignStage      = True
        sarlogicConf.cfg.block.spareSide             = u(7*12)
       #sarlogicConf.cfg.chip.padCoreSide            = 'North'
       #arlet6502Conf.cfg.chip.use45corners           = False
       #sarlogicConf.cfg.chip.useAbstractPads        = True
        sarlogicConf.cfg.chip.supplyRailWidth        = u(20.0)
        sarlogicConf.cfg.chip.supplyRailPitch        = u(40.0)
        sarlogicConf.editor              = editor
        sarlogicConf.useSpares           = True
        sarlogicConf.useClockTree        = True
        sarlogicConf.useHFNS             = True
        sarlogicConf.bColumns            = 2
        sarlogicConf.bRows               = 2
        sarlogicConf.chipName            = 'chip'
       #sarlogicConf.chipConf.ioPadGauge = 'niolib'
        sarlogicConf.coreSize            = ( u( 12*12.0), u( 10*12.0) )
       #sarlogicConf.chipSize            = ( u(  2020.0), u(  2060.0) )
        #sarlogicConf.useHTree( 'clk', Spares.HEAVY_LEAF_LOAD )
        #sarlogicConf.useHTree( 'reset' )
        if buildChip:
            sarlogicToChip = CoreToChip( sarlogicConf )
            sarlogicToChip.buildChip()
            chipBuilder = Chip( sarlogicConf )
            chipBuilder.doChipFloorplan()
            rvalue = chipBuilder.doPnR()
            chipBuilder.save()
        else:
            blockBuilder = Block( sarlogicConf )
            rvalue = blockBuilder.doPnR()
            blockBuilder.save()
    except Exception as e:
        helpers.io.catch( e )
        rvalue = False
    sys.stdout.flush()
    sys.stderr.flush()
    return rvalue


if __name__ == '__main__':
    rvalue = scriptMain()
    shellRValue = 0 if rvalue else 1
    sys.exit( shellRValue )
