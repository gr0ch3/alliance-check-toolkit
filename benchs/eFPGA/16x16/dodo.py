
from coriolis.designflow.technos import setupCMOS

setupCMOS()

DOIT_CONFIG = { 'verbosity' : 2 }

from coriolis.designflow import pnrcheck

pnrcheck.mkRuleSet( globals(), 'matrix_16_16_flat', pnrcheck.NoSynthesis|pnrcheck.NoGDS )
