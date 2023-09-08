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
    B3 = Etat('B3', 1)
    B3.bords = {Bord('0'): s, Bord('1'): s}
    B3.permuts = {Permut('0'): B3}
    ##############################
    # all edges impl
    B3.subs = {Sub('0'): B3, Sub('1'): B3, Sub('2'): B3}
    B3.buildIntern()
    B3.space = [Bord_('0'), Intern_(''), Bord_('1')]
    B3(Permut('0') + Bord('0'), Bord('1'))
    B3(Permut('0') + Bord('1'), Bord('0'))
    B3(Permut('0') + Intern(''), Intern(''))
    B3(Permut('0') + Sub(0), Sub(2) + Permut('0'))
    B3(Permut('0') + Sub(1), Sub(1) + Permut('0'))
    B3(Permut('0') + Sub(2), Sub(0) + Permut('0'))
    B3.grid.elems = [Figure(1, [Bord_('0'), Intern_(''), Bord_('1')])]
    B3.prim.elems = [Figure(1, [Bord_('0'), Bord_('1')])]
    B3.initMat[Sub_('0')] = FMat([
        [1.000000, 0.666667, 0.444444],
        [0.000000, 0.333333, 0.444444],
        [0.000000, 0.000000, 0.111111]]).setTyp('Const')
    B3.initMat[Sub_('1')] = FMat([
        [0.444444, 0.222222, 0.111111],
        [0.444444, 0.555556, 0.444444],
        [0.111111, 0.222222, 0.444444]]).setTyp('Const')
    B3.initMat[Sub_('2')] = FMat([
        [0.111111, 0.000000, 0.000000],
        [0.444444, 0.333333, 0.000000],
        [0.444444, 0.666667, 1.000000]]).setTyp('Const')
    ##############################
    # all cells states
    # Cell_0 -- B3 (5) -- B3 (1) -- B3 (2)
    Cell_0 = Etat('Cell_0', 0)
    ##############################
    # subd of init
    init.subs = {Sub('0'): Cell_0}
    ##############################
    # edges of all states
    Cell_0.bords = {Bord('0'): B3, Bord('1'): B3, Bord('2'): B3}
    ##############################
    # subdivisions of all states
    Cell_0.subs = {Sub('0'): Cell_0, Sub('1'): Cell_0, Sub('2'): Cell_0, Sub('3'): Cell_0, Sub('4'): Cell_0, Sub('5'): Cell_0, Sub('6'): Cell_0}
    ##############################
    # build intern of all states
    Cell_0.buildIntern()
    ##############################
    # spaces of all states
    Cell_0.space = [Bord_('0'), Bord_('1'), Bord_('2')]
    ##############################
    # grid of all states
    Cell_0.addGrid(Bord)
    ##############################
    # prim of all states
    Cell_0.prim.elems = [Figure(2, [
        Bord_('0') + Sub('0') + Bord('0'),
        Bord_('0') + Sub('1') + Bord('0'),
        Bord_('0') + Sub('2') + Bord('0'),
        Bord_('1') + Sub('0') + Bord('0'),
        Bord_('1') + Sub('1') + Bord('0'),
        Bord_('1') + Sub('2') + Bord('0'),
        Bord_('2') + Sub('0') + Bord('0'),
        Bord_('2') + Sub('1') + Bord('0'),
        Bord_('2') + Sub('2') + Bord('0'),
    ])]
    ##############################
    # constraints of all states
    # incidence constraints
    Cell_0(Bord('0') + Sub('0') + Permut('0'), Sub('0') + Bord('0'))
    Cell_0(Bord('2') + Sub('2') + Permut('0'), Sub('0') + Bord('1'))
    Cell_0(Bord('0') + Sub('1') + Permut('0'), Sub('1') + Bord('0'))
    Cell_0(Bord('0') + Sub('2') + Permut('0'), Sub('2') + Bord('0'))
    Cell_0(Bord('1') + Sub('0') + Permut('0'), Sub('2') + Bord('2'))
    Cell_0(Bord('2') + Sub('0') + Permut('0'), Sub('3') + Bord('0'))
    Cell_0(Bord('1') + Sub('2') + Permut('0'), Sub('3') + Bord('1'))
    Cell_0(Bord('2') + Sub('1') + Permut('0'), Sub('4') + Bord('1'))
    Cell_0(Bord('1') + Sub('1') + Permut('0'), Sub('6') + Bord('0'))
    # adjacency constraints
    Cell_0(Sub('0') + Bord('1') + Bord('1'), Sub('4') + Bord('0') + Bord('1'))
    Cell_0(Sub('0') + Bord('2') + Bord('1'), Sub('1') + Bord('0') + Bord('1'))
    Cell_0(Sub('1') + Bord('1') + Bord('1'), Sub('5') + Bord('0') + Bord('1'))
    Cell_0(Sub('1') + Bord('2') + Bord('1'), Sub('2') + Bord('0') + Bord('1'))
    Cell_0(Sub('2') + Bord('1') + Bord('1'), Sub('6') + Bord('0') + Bord('1'))
    Cell_0(Sub('3') + Bord('1') + Bord('1'), Sub('6') + Bord('2') + Bord('1'))
    Cell_0(Sub('3') + Bord('2') + Bord('1'), Sub('4') + Bord('1') + Bord('1'))
    Cell_0(Sub('4') + Bord('2') + Bord('1'), Sub('5') + Bord('1') + Bord('1'))
    Cell_0(Sub('5') + Bord('2') + Bord('1'), Sub('6') + Bord('1') + Bord('1'))
    # edges adjacency constraints
    Cell_0(Bord('0') + Bord('1'), Bord('1') + Bord('0'))
    Cell_0(Bord('1') + Bord('1'), Bord('2') + Bord('0'))
    Cell_0(Bord('2') + Bord('1'), Bord('0') + Bord('0'))
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
