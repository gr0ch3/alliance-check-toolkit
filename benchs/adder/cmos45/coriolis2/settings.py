# -*- Mode:Python -*-

useNsxlib = True

import os
import Cfg
import CRL
import Viewer
from   helpers       import overlay, l, u, n

if useNsxlib:
    if os.environ.has_key('CELLS_TOP'):
        cellsTop = os.environ['CELLS_TOP']
    else:
        cellsTop = '../../../cells'
    import symbolic.cmos45
else:
    import symbolic.cmos

with overlay.CfgCache(priority=Cfg.Parameter.Priority.UserFile) as cfg:
    cfg.misc.catchCore           = False
    cfg.misc.info                = False
    cfg.misc.paranoid            = False
    cfg.misc.bug                 = False
    cfg.misc.logMode             = True
    cfg.misc.verboseLevel1       = True
    cfg.misc.verboseLevel2       = True
    cfg.etesian.graphics         = 3
    cfg.etesian.spaceMargin      = 0.05
    cfg.etesian.aspectRatio      = 1.0
    cfg.anabatic.edgeLenght      = 24
    cfg.anabatic.edgeWidth       = 8
    if useNsxlib:
        cfg.anabatic.routingGauge    = 'msxlib4'
        cfg.anabatic.topRoutingLayer = 'METAL4'
    cfg.katana.eventsLimit       = 4000000
    Viewer.Graphics.setStyle( 'Alliance.Classic [black]' )
    af  = CRL.AllianceFramework.get()
    env = af.getEnvironment()
    env.setCLOCK( '^m_clock|^reset|^ck$' )
    if useNsxlib:
        env.addSYSTEM_LIBRARY( library=cellsTop+'/niolib', mode=CRL.Environment.Prepend )
        env.addSYSTEM_LIBRARY( library=cellsTop+'/nsxlib', mode=CRL.Environment.Prepend )