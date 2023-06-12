from __future__ import division
import sys
import os

directory = os.path.realpath(__file__)
directory = directory[:directory.find('InterfaceBCIFS')] + 'python'
if directory not in sys.path:
    sys.path.append(directory)
from etat import *


def modele():
    init = EtatInit()
    s = Etat('s', 1)
    s.subs = {Sub('0'): s}
    s.buildIntern()
    ##############################
    # all edges states
    ##############################
    # all edges impl
    ##############################
    # all cells states
    ##############################
    # subd of init
    init.subs = {}
    ##############################
    # edges of all states
    ##############################
    # subdivisions of all states
    ##############################
    # build intern of all states
    ##############################
    # spaces of all states
    ##############################
    # grid of all states
    ##############################
    # prim of all states
    ##############################
    # constraints of all states
    # constraints on init cells
    # control points
    return init


if __name__ == '__main__':
    print('modele()')
    model_init = modele()
    print('check()')
    model_init.check()
    print('solve()')
    model_init.solve()
    model_init.display()
    print('End')
