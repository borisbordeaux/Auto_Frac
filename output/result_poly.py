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
    B2 = Etat('B2', 1)
    B2.bords = {Bord('0'): s, Bord('1'): s}
    B2.permuts = {Permut('0'): B2}
    B4 = Etat('B4', 1)
    B4.bords = {Bord('0'): s, Bord('1'): s}
    B4.permuts = {Permut('0'): B4}
    ##############################
    # all edges impl
    B2.subs = {Sub('0'): B2, Sub('1'): B2}
    B2.buildIntern()
    B2.space = [Bord_('0'), Intern_(''), Bord_('1')]
    B2(Permut('0') + Bord('0'), Bord('1'))
    B2(Permut('0') + Bord('1'), Bord('0'))
    B2(Permut('0') + Intern(''), Intern(''))
    B2(Permut('0') + Sub(0), Sub(1) + Permut('0'))
    B2(Permut('0') + Sub(1), Sub(0) + Permut('0'))
    B2.grid.elems = [Figure(1, [Bord_('0'), Intern_(''), Bord_('1')])]
    B2.prim.elems = [Figure(1, [Bord_('0'), Bord_('1')])]
    B2.initMat[Sub_('0')] = FMat([
        [1.000000, 0.500000, 0.250000],
        [0.000000, 0.500000, 0.500000],
        [0.000000, 0.000000, 0.250000]]).setTyp('Const')
    B2.initMat[Sub_('1')] = FMat([
        [0.250000, 0.000000, 0.000000],
        [0.500000, 0.500000, 0.000000],
        [0.250000, 0.500000, 1.000000]]).setTyp('Const')
    B4.subs = {Sub('0'): B4, Sub('1'): B4, Sub('2'): B4, Sub('3'): B4}
    B4.buildIntern()
    B4.space = [Bord_('0'), Intern_(''), Bord_('1')]
    B4(Permut('0') + Bord('0'), Bord('1'))
    B4(Permut('0') + Bord('1'), Bord('0'))
    B4(Permut('0') + Intern(''), Intern(''))
    B4(Permut('0') + Sub(0), Sub(3) + Permut('0'))
    B4(Permut('0') + Sub(1), Sub(2) + Permut('0'))
    B4(Permut('0') + Sub(2), Sub(1) + Permut('0'))
    B4(Permut('0') + Sub(3), Sub(0) + Permut('0'))
    B4.grid.elems = [Figure(1, [Bord_('0'), Intern_(''), Bord_('1')])]
    B4.prim.elems = [Figure(1, [Bord_('0'), Bord_('1')])]
    B4.initMat[Sub_('0')] = FMat([
        [1.000000, 0.750000, 0.562500],
        [0.000000, 0.250000, 0.375000],
        [0.000000, 0.000000, 0.062500]]).setTyp('Const')
    B4.initMat[Sub_('1')] = FMat([
        [0.562500, 0.375000, 0.250000],
        [0.375000, 0.500000, 0.500000],
        [0.062500, 0.125000, 0.250000]]).setTyp('Const')
    B4.initMat[Sub_('2')] = FMat([
        [0.250000, 0.125000, 0.062500],
        [0.500000, 0.500000, 0.375000],
        [0.250000, 0.375000, 0.562500]]).setTyp('Const')
    B4.initMat[Sub_('3')] = FMat([
        [0.062500, 0.000000, 0.000000],
        [0.375000, 0.250000, 0.000000],
        [0.562500, 0.750000, 1.000000]]).setTyp('Const')
    ##############################
    # all cells states
    # Cell_0 -- B2 (2) -- B2 (1) -- B4 (6)
    Cell_0 = Etat('Cell_0', 0)
    # Cell_1 -- B2 (5) -- B2 (1) -- B2 (2) -- B2 (3) -- B2 (4)
    Cell_1 = Etat('Cell_1', 0)
    ##############################
    # subd of init
    init.subs = {Sub('0'): Cell_0, Sub('1'): Cell_0, Sub('2'): Cell_0, Sub('3'): Cell_1, Sub('4'): Cell_0, Sub('5'): Cell_0}
    ##############################
    # edges of all states
    Cell_0.bords = {Bord('0'): B2, Bord('1'): B2, Bord('2'): B4}
    Cell_1.bords = {Bord('0'): B2, Bord('1'): B2, Bord('2'): B2, Bord('3'): B2, Bord('4'): B2}
    ##############################
    # subdivisions of all states
    Cell_0.subs = {Sub('0'): Cell_0, Sub('1'): Cell_0, Sub('2'): Cell_1, Sub('3'): Cell_0, Sub('4'): Cell_0}
    Cell_1.subs = {Sub('0'): Cell_0, Sub('1'): Cell_0, Sub('2'): Cell_0, Sub('3'): Cell_0, Sub('4'): Cell_0}
    ##############################
    # build intern of all states
    Cell_0.buildIntern()
    Cell_1.buildIntern()
    ##############################
    # spaces of all states
    Cell_0.space = [Bord_('0'), Bord_('1'), Bord_('2')]
    Cell_1.space = [Bord_('0'), Bord_('1'), Bord_('2'), Bord_('3'), Bord_('4')]
    ##############################
    # grid of all states
    Cell_0.addGrid(Bord)
    Cell_1.addGrid(Bord)
    ##############################
    # prim of all states
    Cell_0.prim.elems = [Figure(2, [
        Bord_('0') + Sub('0') + Sub('0') + Bord('0'),
        Bord_('0') + Sub('0') + Sub('1') + Bord('0'),
        Bord_('0') + Sub('1') + Sub('0') + Bord('0'),
        Bord_('0') + Sub('1') + Sub('1') + Bord('0'),
        Bord_('1') + Sub('0') + Sub('0') + Bord('0'),
        Bord_('1') + Sub('0') + Sub('1') + Bord('0'),
        Bord_('1') + Sub('1') + Sub('0') + Bord('0'),
        Bord_('1') + Sub('1') + Sub('1') + Bord('0'),
        Bord_('2') + Sub('0') + Bord('0'),
        Bord_('2') + Sub('1') + Bord('0'),
        Bord_('2') + Sub('2') + Bord('0'),
        Bord_('2') + Sub('3') + Bord('0'),
    ])]
    Cell_1.prim.elems = [Figure(2, [
        Bord_('0') + Sub('0') + Sub('0') + Bord('0'),
        Bord_('0') + Sub('0') + Sub('1') + Bord('0'),
        Bord_('0') + Sub('1') + Sub('0') + Bord('0'),
        Bord_('0') + Sub('1') + Sub('1') + Bord('0'),
        Bord_('1') + Sub('0') + Sub('0') + Bord('0'),
        Bord_('1') + Sub('0') + Sub('1') + Bord('0'),
        Bord_('1') + Sub('1') + Sub('0') + Bord('0'),
        Bord_('1') + Sub('1') + Sub('1') + Bord('0'),
        Bord_('2') + Sub('0') + Sub('0') + Bord('0'),
        Bord_('2') + Sub('0') + Sub('1') + Bord('0'),
        Bord_('2') + Sub('1') + Sub('0') + Bord('0'),
        Bord_('2') + Sub('1') + Sub('1') + Bord('0'),
        Bord_('3') + Sub('0') + Sub('0') + Bord('0'),
        Bord_('3') + Sub('0') + Sub('1') + Bord('0'),
        Bord_('3') + Sub('1') + Sub('0') + Bord('0'),
        Bord_('3') + Sub('1') + Sub('1') + Bord('0'),
        Bord_('4') + Sub('0') + Sub('0') + Bord('0'),
        Bord_('4') + Sub('0') + Sub('1') + Bord('0'),
        Bord_('4') + Sub('1') + Sub('0') + Bord('0'),
        Bord_('4') + Sub('1') + Sub('1') + Bord('0'),
    ])]
    ##############################
    # constraints of all states
    # incidence constraints
    Cell_0(Bord('0') + Sub('0') + Permut('0'), Sub('0') + Bord('1'))
    Cell_0(Bord('2') + Sub('3') + Permut('0'), Sub('0') + Bord('2'))
    Cell_0(Bord('2') + Sub('2') + Permut('0'), Sub('1') + Bord('2'))
    Cell_0(Bord('1') + Sub('0') + Permut('0'), Sub('2') + Bord('1'))
    Cell_0(Bord('0') + Sub('1') + Permut('0'), Sub('2') + Bord('2'))
    Cell_0(Bord('2') + Sub('1') + Permut('0'), Sub('3') + Bord('2'))
    Cell_0(Bord('1') + Sub('1') + Permut('0'), Sub('4') + Bord('0'))
    Cell_0(Bord('2') + Sub('0') + Permut('0'), Sub('4') + Bord('2'))
    # adjacency constraints
    Cell_0(Sub('0') + Bord('0') + Bord('1'), Sub('2') + Bord('2') + Bord('1'))
    Cell_0(Sub('0') + Bord('2') + Bord('1'), Sub('1') + Bord('1') + Bord('1'))
    Cell_0(Sub('1') + Bord('0') + Bord('1'), Sub('2') + Bord('3') + Bord('1'))
    Cell_0(Sub('1') + Bord('2') + Bord('1'), Sub('3') + Bord('1') + Bord('1'))
    Cell_0(Sub('2') + Bord('0') + Bord('1'), Sub('4') + Bord('0') + Bord('1'))
    Cell_0(Sub('2') + Bord('4') + Bord('1'), Sub('3') + Bord('0') + Bord('1'))
    Cell_0(Sub('3') + Bord('2') + Bord('1'), Sub('4') + Bord('1') + Bord('1'))
    # edges adjacency constraints
    Cell_0(Bord('0') + Bord('1'), Bord('1') + Bord('0'))
    Cell_0(Bord('1') + Bord('1'), Bord('2') + Bord('0'))
    Cell_0(Bord('2') + Bord('1'), Bord('0') + Bord('0'))
    # incidence constraints
    Cell_1(Bord('2') + Sub('0') + Permut('0'), Sub('0') + Bord('0'))
    Cell_1(Bord('1') + Sub('1') + Permut('0'), Sub('0') + Bord('1'))
    Cell_1(Bord('3') + Sub('0') + Permut('0'), Sub('1') + Bord('0'))
    Cell_1(Bord('2') + Sub('1') + Permut('0'), Sub('1') + Bord('1'))
    Cell_1(Bord('4') + Sub('0') + Permut('0'), Sub('2') + Bord('0'))
    Cell_1(Bord('3') + Sub('1') + Permut('0'), Sub('2') + Bord('1'))
    Cell_1(Bord('0') + Sub('0') + Permut('0'), Sub('3') + Bord('0'))
    Cell_1(Bord('4') + Sub('1') + Permut('0'), Sub('3') + Bord('1'))
    Cell_1(Bord('1') + Sub('0') + Permut('0'), Sub('4') + Bord('0'))
    Cell_1(Bord('0') + Sub('1') + Permut('0'), Sub('4') + Bord('1'))
    # adjacency constraints
    Cell_1(Sub('0') + Bord('1') + Bord('1'), Sub('4') + Bord('2') + Bord('1'))
    Cell_1(Sub('0') + Bord('2') + Bord('1'), Sub('1') + Bord('1') + Bord('1'))
    Cell_1(Sub('1') + Bord('2') + Bord('1'), Sub('2') + Bord('1') + Bord('1'))
    Cell_1(Sub('2') + Bord('2') + Bord('1'), Sub('3') + Bord('1') + Bord('1'))
    Cell_1(Sub('3') + Bord('2') + Bord('1'), Sub('4') + Bord('1') + Bord('1'))
    # edges adjacency constraints
    Cell_1(Bord('0') + Bord('1'), Bord('1') + Bord('0'))
    Cell_1(Bord('1') + Bord('1'), Bord('2') + Bord('0'))
    Cell_1(Bord('2') + Bord('1'), Bord('3') + Bord('0'))
    Cell_1(Bord('3') + Bord('1'), Bord('4') + Bord('0'))
    Cell_1(Bord('4') + Bord('1'), Bord('0') + Bord('0'))
    # constraints on init cells
    init(Sub('0') + Bord('0') + Bord('1'), Sub('3') + Bord('1') + Bord('1'))
    init(Sub('0') + Bord('1') + Bord('1'), Sub('5') + Bord('2') + Bord('1'))
    init(Sub('0') + Bord('2') + Bord('1'), Sub('1') + Bord('1') + Bord('1'))
    init(Sub('1') + Bord('0') + Bord('1'), Sub('3') + Bord('2') + Bord('1'))
    init(Sub('1') + Bord('2') + Bord('1'), Sub('2') + Bord('1') + Bord('1'))
    init(Sub('2') + Bord('0') + Bord('1'), Sub('3') + Bord('3') + Bord('1'))
    init(Sub('2') + Bord('2') + Bord('1'), Sub('4') + Bord('1') + Bord('1'))
    init(Sub('3') + Bord('0') + Bord('1'), Sub('5') + Bord('0') + Bord('1'))
    init(Sub('3') + Bord('4') + Bord('1'), Sub('4') + Bord('0') + Bord('1'))
    init(Sub('4') + Bord('2') + Bord('1'), Sub('5') + Bord('1') + Bord('1'))
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
