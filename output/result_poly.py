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
    ##############################
    # all cells states
    # Cell_0 -- B2 (2) -- B2 (1) -- B2 (3) -- B2 (4)
    Cell_0 = Etat('Cell_0', 0)
    # Cell_1 -- B2 (2) -- B2 (4) -- B2 (6) -- B2 (8) -- B2 (10) -- B2 (12) -- B2 (14) -- B2 (16) -- B2 (18) -- B2 (20) -- B2 (22) -- B2 (24) -- B2 (26) -- B2 (28) -- B2 (30)
    Cell_1 = Etat('Cell_1', 0)
    ##############################
    # subd of init
    init.subs = {Sub('0'): Cell_0}
    ##############################
    # edges of all states
    Cell_0.bords = {Bord('0'): B2, Bord('1'): B2, Bord('2'): B2, Bord('3'): B2}
    Cell_1.bords = {Bord('0'): B2, Bord('1'): B2, Bord('2'): B2, Bord('3'): B2, Bord('4'): B2, Bord('5'): B2, Bord('6'): B2, Bord('7'): B2, Bord('8'): B2, Bord('9'): B2, Bord('10'): B2, Bord('11'): B2, Bord('12'): B2, Bord('13'): B2, Bord('14'): B2}
    ##############################
    # subdivisions of all states
    Cell_0.subs = {Sub('0'): Cell_0, Sub('1'): Cell_0, Sub('2'): Cell_0, Sub('3'): Cell_0, Sub('4'): Cell_0, Sub('5'): Cell_0, Sub('6'): Cell_0, Sub('7'): Cell_0, Sub('8'): Cell_0, Sub('9'): Cell_0, Sub('10'): Cell_0, Sub('11'): Cell_0, Sub('12'): Cell_1, Sub('13'): Cell_0, Sub('14'): Cell_0, Sub('15'): Cell_1}
    Cell_1.subs = {Sub('0'): Cell_0, Sub('1'): Cell_0, Sub('2'): Cell_0, Sub('3'): Cell_0, Sub('4'): Cell_0, Sub('5'): Cell_0, Sub('6'): Cell_0, Sub('7'): Cell_0, Sub('8'): Cell_0, Sub('9'): Cell_0, Sub('10'): Cell_0, Sub('11'): Cell_0, Sub('12'): Cell_0, Sub('13'): Cell_0, Sub('14'): Cell_0, Sub('15'): Cell_1}
    ##############################
    # build intern of all states
    Cell_0.buildIntern()
    Cell_1.buildIntern()
    ##############################
    # spaces of all states
    Cell_0.space = [Bord_('0'), Bord_('1'), Bord_('2'), Bord_('3')]
    Cell_1.space = [Bord_('0'), Bord_('1'), Bord_('2'), Bord_('3'), Bord_('4'), Bord_('5'), Bord_('6'), Bord_('7'), Bord_('8'), Bord_('9'), Bord_('10'), Bord_('11'), Bord_('12'), Bord_('13'), Bord_('14')]
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
        Bord_('2') + Sub('0') + Sub('0') + Bord('0'),
        Bord_('2') + Sub('0') + Sub('1') + Bord('0'),
        Bord_('2') + Sub('1') + Sub('0') + Bord('0'),
        Bord_('2') + Sub('1') + Sub('1') + Bord('0'),
        Bord_('3') + Sub('0') + Sub('0') + Bord('0'),
        Bord_('3') + Sub('0') + Sub('1') + Bord('0'),
        Bord_('3') + Sub('1') + Sub('0') + Bord('0'),
        Bord_('3') + Sub('1') + Sub('1') + Bord('0'),
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
        Bord_('5') + Sub('0') + Sub('0') + Bord('0'),
        Bord_('5') + Sub('0') + Sub('1') + Bord('0'),
        Bord_('5') + Sub('1') + Sub('0') + Bord('0'),
        Bord_('5') + Sub('1') + Sub('1') + Bord('0'),
        Bord_('6') + Sub('0') + Sub('0') + Bord('0'),
        Bord_('6') + Sub('0') + Sub('1') + Bord('0'),
        Bord_('6') + Sub('1') + Sub('0') + Bord('0'),
        Bord_('6') + Sub('1') + Sub('1') + Bord('0'),
        Bord_('7') + Sub('0') + Sub('0') + Bord('0'),
        Bord_('7') + Sub('0') + Sub('1') + Bord('0'),
        Bord_('7') + Sub('1') + Sub('0') + Bord('0'),
        Bord_('7') + Sub('1') + Sub('1') + Bord('0'),
        Bord_('8') + Sub('0') + Sub('0') + Bord('0'),
        Bord_('8') + Sub('0') + Sub('1') + Bord('0'),
        Bord_('8') + Sub('1') + Sub('0') + Bord('0'),
        Bord_('8') + Sub('1') + Sub('1') + Bord('0'),
        Bord_('9') + Sub('0') + Sub('0') + Bord('0'),
        Bord_('9') + Sub('0') + Sub('1') + Bord('0'),
        Bord_('9') + Sub('1') + Sub('0') + Bord('0'),
        Bord_('9') + Sub('1') + Sub('1') + Bord('0'),
        Bord_('10') + Sub('0') + Sub('0') + Bord('0'),
        Bord_('10') + Sub('0') + Sub('1') + Bord('0'),
        Bord_('10') + Sub('1') + Sub('0') + Bord('0'),
        Bord_('10') + Sub('1') + Sub('1') + Bord('0'),
        Bord_('11') + Sub('0') + Sub('0') + Bord('0'),
        Bord_('11') + Sub('0') + Sub('1') + Bord('0'),
        Bord_('11') + Sub('1') + Sub('0') + Bord('0'),
        Bord_('11') + Sub('1') + Sub('1') + Bord('0'),
        Bord_('12') + Sub('0') + Sub('0') + Bord('0'),
        Bord_('12') + Sub('0') + Sub('1') + Bord('0'),
        Bord_('12') + Sub('1') + Sub('0') + Bord('0'),
        Bord_('12') + Sub('1') + Sub('1') + Bord('0'),
        Bord_('13') + Sub('0') + Sub('0') + Bord('0'),
        Bord_('13') + Sub('0') + Sub('1') + Bord('0'),
        Bord_('13') + Sub('1') + Sub('0') + Bord('0'),
        Bord_('13') + Sub('1') + Sub('1') + Bord('0'),
        Bord_('14') + Sub('0') + Sub('0') + Bord('0'),
        Bord_('14') + Sub('0') + Sub('1') + Bord('0'),
        Bord_('14') + Sub('1') + Sub('0') + Bord('0'),
        Bord_('14') + Sub('1') + Sub('1') + Bord('0'),
    ])]
    ##############################
    # constraints of all states
    # incidence constraints
    Cell_0(Bord('3') + Sub('0') + Permut('0'), Sub('0') + Bord('0'))
    Cell_0(Bord('2') + Sub('1') + Permut('0'), Sub('0') + Bord('1'))
    Cell_0(Bord('0') + Sub('0') + Permut('0'), Sub('12') + Bord('0'))
    Cell_0(Bord('3') + Sub('1') + Permut('0'), Sub('12') + Bord('1'))
    Cell_0(Bord('1') + Sub('0') + Permut('0'), Sub('14') + Bord('2'))
    Cell_0(Bord('0') + Sub('1') + Permut('0'), Sub('14') + Bord('3'))
    Cell_0(Bord('2') + Sub('0') + Permut('0'), Sub('15') + Bord('0'))
    Cell_0(Bord('1') + Sub('1') + Permut('0'), Sub('15') + Bord('1'))
    # adjacency constraints
    Cell_0(Sub('0') + Bord('1') + Bord('1'), Sub('15') + Bord('14') + Bord('1'))
    Cell_0(Sub('0') + Bord('2') + Bord('1'), Sub('1') + Bord('0') + Bord('1'))
    Cell_0(Sub('0') + Bord('3') + Bord('1'), Sub('12') + Bord('1') + Bord('1'))
    Cell_0(Sub('1') + Bord('1') + Bord('1'), Sub('15') + Bord('13') + Bord('1'))
    Cell_0(Sub('1') + Bord('2') + Bord('1'), Sub('2') + Bord('0') + Bord('1'))
    Cell_0(Sub('1') + Bord('3') + Bord('1'), Sub('12') + Bord('2') + Bord('1'))
    Cell_0(Sub('2') + Bord('1') + Bord('1'), Sub('15') + Bord('12') + Bord('1'))
    Cell_0(Sub('2') + Bord('2') + Bord('1'), Sub('3') + Bord('0') + Bord('1'))
    Cell_0(Sub('2') + Bord('3') + Bord('1'), Sub('12') + Bord('3') + Bord('1'))
    Cell_0(Sub('3') + Bord('1') + Bord('1'), Sub('15') + Bord('11') + Bord('1'))
    Cell_0(Sub('3') + Bord('2') + Bord('1'), Sub('4') + Bord('0') + Bord('1'))
    Cell_0(Sub('3') + Bord('3') + Bord('1'), Sub('12') + Bord('4') + Bord('1'))
    Cell_0(Sub('4') + Bord('1') + Bord('1'), Sub('15') + Bord('10') + Bord('1'))
    Cell_0(Sub('4') + Bord('2') + Bord('1'), Sub('5') + Bord('0') + Bord('1'))
    Cell_0(Sub('4') + Bord('3') + Bord('1'), Sub('12') + Bord('5') + Bord('1'))
    Cell_0(Sub('5') + Bord('1') + Bord('1'), Sub('15') + Bord('9') + Bord('1'))
    Cell_0(Sub('5') + Bord('2') + Bord('1'), Sub('6') + Bord('0') + Bord('1'))
    Cell_0(Sub('5') + Bord('3') + Bord('1'), Sub('12') + Bord('6') + Bord('1'))
    Cell_0(Sub('6') + Bord('1') + Bord('1'), Sub('15') + Bord('8') + Bord('1'))
    Cell_0(Sub('6') + Bord('2') + Bord('1'), Sub('7') + Bord('0') + Bord('1'))
    Cell_0(Sub('6') + Bord('3') + Bord('1'), Sub('12') + Bord('7') + Bord('1'))
    Cell_0(Sub('7') + Bord('1') + Bord('1'), Sub('15') + Bord('7') + Bord('1'))
    Cell_0(Sub('7') + Bord('2') + Bord('1'), Sub('8') + Bord('0') + Bord('1'))
    Cell_0(Sub('7') + Bord('3') + Bord('1'), Sub('12') + Bord('8') + Bord('1'))
    Cell_0(Sub('8') + Bord('1') + Bord('1'), Sub('15') + Bord('6') + Bord('1'))
    Cell_0(Sub('8') + Bord('2') + Bord('1'), Sub('9') + Bord('0') + Bord('1'))
    Cell_0(Sub('8') + Bord('3') + Bord('1'), Sub('12') + Bord('9') + Bord('1'))
    Cell_0(Sub('9') + Bord('1') + Bord('1'), Sub('15') + Bord('5') + Bord('1'))
    Cell_0(Sub('9') + Bord('2') + Bord('1'), Sub('10') + Bord('0') + Bord('1'))
    Cell_0(Sub('9') + Bord('3') + Bord('1'), Sub('12') + Bord('10') + Bord('1'))
    Cell_0(Sub('10') + Bord('1') + Bord('1'), Sub('15') + Bord('4') + Bord('1'))
    Cell_0(Sub('10') + Bord('2') + Bord('1'), Sub('11') + Bord('0') + Bord('1'))
    Cell_0(Sub('10') + Bord('3') + Bord('1'), Sub('12') + Bord('11') + Bord('1'))
    Cell_0(Sub('11') + Bord('1') + Bord('1'), Sub('15') + Bord('3') + Bord('1'))
    Cell_0(Sub('11') + Bord('2') + Bord('1'), Sub('13') + Bord('0') + Bord('1'))
    Cell_0(Sub('11') + Bord('3') + Bord('1'), Sub('12') + Bord('12') + Bord('1'))
    Cell_0(Sub('12') + Bord('13') + Bord('1'), Sub('13') + Bord('3') + Bord('1'))
    Cell_0(Sub('12') + Bord('14') + Bord('1'), Sub('14') + Bord('3') + Bord('1'))
    Cell_0(Sub('13') + Bord('1') + Bord('1'), Sub('15') + Bord('2') + Bord('1'))
    Cell_0(Sub('13') + Bord('2') + Bord('1'), Sub('14') + Bord('0') + Bord('1'))
    Cell_0(Sub('14') + Bord('1') + Bord('1'), Sub('15') + Bord('1') + Bord('1'))
    # edges adjacency constraints
    Cell_0(Bord('0') + Bord('1'), Bord('1') + Bord('0'))
    Cell_0(Bord('1') + Bord('1'), Bord('2') + Bord('0'))
    Cell_0(Bord('2') + Bord('1'), Bord('3') + Bord('0'))
    Cell_0(Bord('3') + Bord('1'), Bord('0') + Bord('0'))
    # incidence constraints
    Cell_1(Bord('0') + Sub('1') + Permut('0'), Sub('0') + Bord('0'))
    Cell_1(Bord('1') + Sub('0') + Permut('0'), Sub('0') + Bord('3'))
    Cell_1(Bord('1') + Sub('1') + Permut('0'), Sub('1') + Bord('0'))
    Cell_1(Bord('2') + Sub('0') + Permut('0'), Sub('1') + Bord('3'))
    Cell_1(Bord('2') + Sub('1') + Permut('0'), Sub('2') + Bord('0'))
    Cell_1(Bord('3') + Sub('0') + Permut('0'), Sub('2') + Bord('3'))
    Cell_1(Bord('3') + Sub('1') + Permut('0'), Sub('3') + Bord('0'))
    Cell_1(Bord('4') + Sub('0') + Permut('0'), Sub('3') + Bord('3'))
    Cell_1(Bord('4') + Sub('1') + Permut('0'), Sub('4') + Bord('0'))
    Cell_1(Bord('5') + Sub('0') + Permut('0'), Sub('4') + Bord('3'))
    Cell_1(Bord('5') + Sub('1') + Permut('0'), Sub('5') + Bord('0'))
    Cell_1(Bord('6') + Sub('0') + Permut('0'), Sub('5') + Bord('3'))
    Cell_1(Bord('6') + Sub('1') + Permut('0'), Sub('6') + Bord('0'))
    Cell_1(Bord('7') + Sub('0') + Permut('0'), Sub('6') + Bord('3'))
    Cell_1(Bord('7') + Sub('1') + Permut('0'), Sub('7') + Bord('0'))
    Cell_1(Bord('8') + Sub('0') + Permut('0'), Sub('7') + Bord('3'))
    Cell_1(Bord('8') + Sub('1') + Permut('0'), Sub('8') + Bord('0'))
    Cell_1(Bord('9') + Sub('0') + Permut('0'), Sub('8') + Bord('3'))
    Cell_1(Bord('9') + Sub('1') + Permut('0'), Sub('9') + Bord('0'))
    Cell_1(Bord('10') + Sub('0') + Permut('0'), Sub('9') + Bord('3'))
    Cell_1(Bord('10') + Sub('1') + Permut('0'), Sub('10') + Bord('0'))
    Cell_1(Bord('11') + Sub('0') + Permut('0'), Sub('10') + Bord('3'))
    Cell_1(Bord('11') + Sub('1') + Permut('0'), Sub('11') + Bord('0'))
    Cell_1(Bord('12') + Sub('0') + Permut('0'), Sub('11') + Bord('3'))
    Cell_1(Bord('12') + Sub('1') + Permut('0'), Sub('12') + Bord('0'))
    Cell_1(Bord('13') + Sub('0') + Permut('0'), Sub('12') + Bord('3'))
    Cell_1(Bord('13') + Sub('1') + Permut('0'), Sub('13') + Bord('0'))
    Cell_1(Bord('14') + Sub('0') + Permut('0'), Sub('13') + Bord('3'))
    Cell_1(Bord('14') + Sub('1') + Permut('0'), Sub('14') + Bord('0'))
    Cell_1(Bord('0') + Sub('0') + Permut('0'), Sub('14') + Bord('3'))
    # adjacency constraints
    Cell_1(Sub('0') + Bord('0') + Bord('1'), Sub('14') + Bord('2') + Bord('1'))
    Cell_1(Sub('0') + Bord('1') + Bord('1'), Sub('15') + Bord('0') + Bord('1'))
    Cell_1(Sub('0') + Bord('2') + Bord('1'), Sub('1') + Bord('0') + Bord('1'))
    Cell_1(Sub('1') + Bord('1') + Bord('1'), Sub('15') + Bord('14') + Bord('1'))
    Cell_1(Sub('1') + Bord('2') + Bord('1'), Sub('2') + Bord('0') + Bord('1'))
    Cell_1(Sub('2') + Bord('1') + Bord('1'), Sub('15') + Bord('13') + Bord('1'))
    Cell_1(Sub('2') + Bord('2') + Bord('1'), Sub('3') + Bord('0') + Bord('1'))
    Cell_1(Sub('3') + Bord('1') + Bord('1'), Sub('15') + Bord('12') + Bord('1'))
    Cell_1(Sub('3') + Bord('2') + Bord('1'), Sub('4') + Bord('0') + Bord('1'))
    Cell_1(Sub('4') + Bord('1') + Bord('1'), Sub('15') + Bord('11') + Bord('1'))
    Cell_1(Sub('4') + Bord('2') + Bord('1'), Sub('5') + Bord('0') + Bord('1'))
    Cell_1(Sub('5') + Bord('1') + Bord('1'), Sub('15') + Bord('10') + Bord('1'))
    Cell_1(Sub('5') + Bord('2') + Bord('1'), Sub('6') + Bord('0') + Bord('1'))
    Cell_1(Sub('6') + Bord('1') + Bord('1'), Sub('15') + Bord('9') + Bord('1'))
    Cell_1(Sub('6') + Bord('2') + Bord('1'), Sub('7') + Bord('0') + Bord('1'))
    Cell_1(Sub('7') + Bord('1') + Bord('1'), Sub('15') + Bord('8') + Bord('1'))
    Cell_1(Sub('7') + Bord('2') + Bord('1'), Sub('8') + Bord('0') + Bord('1'))
    Cell_1(Sub('8') + Bord('1') + Bord('1'), Sub('15') + Bord('7') + Bord('1'))
    Cell_1(Sub('8') + Bord('2') + Bord('1'), Sub('9') + Bord('0') + Bord('1'))
    Cell_1(Sub('9') + Bord('1') + Bord('1'), Sub('15') + Bord('6') + Bord('1'))
    Cell_1(Sub('9') + Bord('2') + Bord('1'), Sub('10') + Bord('0') + Bord('1'))
    Cell_1(Sub('10') + Bord('1') + Bord('1'), Sub('15') + Bord('5') + Bord('1'))
    Cell_1(Sub('10') + Bord('2') + Bord('1'), Sub('11') + Bord('0') + Bord('1'))
    Cell_1(Sub('11') + Bord('1') + Bord('1'), Sub('15') + Bord('4') + Bord('1'))
    Cell_1(Sub('11') + Bord('2') + Bord('1'), Sub('12') + Bord('0') + Bord('1'))
    Cell_1(Sub('12') + Bord('1') + Bord('1'), Sub('15') + Bord('3') + Bord('1'))
    Cell_1(Sub('12') + Bord('2') + Bord('1'), Sub('13') + Bord('0') + Bord('1'))
    Cell_1(Sub('13') + Bord('1') + Bord('1'), Sub('15') + Bord('2') + Bord('1'))
    Cell_1(Sub('13') + Bord('2') + Bord('1'), Sub('14') + Bord('0') + Bord('1'))
    Cell_1(Sub('14') + Bord('1') + Bord('1'), Sub('15') + Bord('1') + Bord('1'))
    # edges adjacency constraints
    Cell_1(Bord('0') + Bord('1'), Bord('1') + Bord('0'))
    Cell_1(Bord('1') + Bord('1'), Bord('2') + Bord('0'))
    Cell_1(Bord('2') + Bord('1'), Bord('3') + Bord('0'))
    Cell_1(Bord('3') + Bord('1'), Bord('4') + Bord('0'))
    Cell_1(Bord('4') + Bord('1'), Bord('5') + Bord('0'))
    Cell_1(Bord('5') + Bord('1'), Bord('6') + Bord('0'))
    Cell_1(Bord('6') + Bord('1'), Bord('7') + Bord('0'))
    Cell_1(Bord('7') + Bord('1'), Bord('8') + Bord('0'))
    Cell_1(Bord('8') + Bord('1'), Bord('9') + Bord('0'))
    Cell_1(Bord('9') + Bord('1'), Bord('10') + Bord('0'))
    Cell_1(Bord('10') + Bord('1'), Bord('11') + Bord('0'))
    Cell_1(Bord('11') + Bord('1'), Bord('12') + Bord('0'))
    Cell_1(Bord('12') + Bord('1'), Bord('13') + Bord('0'))
    Cell_1(Bord('13') + Bord('1'), Bord('14') + Bord('0'))
    Cell_1(Bord('14') + Bord('1'), Bord('0') + Bord('0'))
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
