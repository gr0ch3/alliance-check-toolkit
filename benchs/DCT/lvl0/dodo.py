
from coriolis.designflow.technos import setupCMOS

setupCMOS()

DOIT_CONFIG = { 'verbosity' : 2 }

from coriolis.designflow.task import Tasks
from coriolis.designflow      import routecheck

routecheck.mkRuleSet( globals(), 'operator_lvl0_flat' )
