# -*- Mode:Python -*-

import Cfg
import Viewer
import CRL
import node600.phenitec
from   helpers       import l, u, n


Cfg.Configuration.pushDefaultPriority( Cfg.Parameter.Priority.UserFile )

Viewer.Graphics.setStyle( 'Alliance.Classic [black]' )

af  = CRL.AllianceFramework.get()
env = af.getEnvironment()
env.setCLOCK( '^ck$|m_clock' )
 
Cfg.getParamBool      ( 'misc.catchCore'              ).setBool      ( False   )
Cfg.getParamBool      ( 'misc.info'                   ).setBool      ( False   )
Cfg.getParamBool      ( 'misc.paranoid'               ).setBool      ( False   )
Cfg.getParamBool      ( 'misc.bug'                    ).setBool      ( False   )
Cfg.getParamBool      ( 'misc.logMode'                ).setBool      ( True    )
Cfg.getParamBool      ( 'misc.verboseLevel1'          ).setBool      ( True    )
Cfg.getParamBool      ( 'misc.verboseLevel2'          ).setBool      ( True    )
#Cfg.getParamInt       ( 'misc.minTraceLevel'          ).setInt       ( 0       )
#Cfg.getParamInt       ( 'misc.maxTraceLevel'          ).setInt       ( 18      )
Cfg.getParamEnumerate ( 'etesian.effort'              ).setInt       ( 2       )
Cfg.getParamInt       ( 'katana.eventsLimit'          ).setInt       ( 1000000 )
#Cfg.getParamString    ( 'anabatic.topRoutingLayer'    ).setString    ( 'METAL3')
#Cfg.getParamInt       ( 'katana.hTracksReservedLocal' ).setInt       ( 5       )
#Cfg.getParamInt       ( 'katana.vTracksReservedLocal' ).setInt       ( 5       )

Cfg.Configuration.popDefaultPriority()
