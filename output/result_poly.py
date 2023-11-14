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
    B4 = Etat('B4', 1)
    B4.bords = {Bord('0'): s, Bord('1'): s}
    B4.permuts = {Permut('0'): B4}
    B3 = Etat('B3', 1)
    B3.bords = {Bord('0'): s, Bord('1'): s}
    B3.permuts = {Permut('0'): B3}
    ##############################
    # all edges impl
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
    # Cell_0 -- B4 (3) -- B3 (1) -- B3 (2)
    Cell_0 = Etat('Cell_0', 0)
    # Cell_1 -- B3 (2) -- B4 (4) -- B4 (5)
    Cell_1 = Etat('Cell_1', 0)
    # Cell_2 -- B4 (8) -- B4 (4) -- B3 (1)
    Cell_2 = Etat('Cell_2', 0)
    # Cell_3 -- B3 (2) -- B3 (1) -- B4 (4)
    Cell_3 = Etat('Cell_3', 0)
    ##############################
    # subd of init
    init.subs = {Sub('0'): Cell_0, Sub('1'): Cell_1, Sub('2'): Cell_0, Sub('3'): Cell_1, Sub('4'): Cell_1, Sub('5'): Cell_1, Sub('6'): Cell_2, Sub('7'): Cell_3, Sub('8'): Cell_2, Sub('9'): Cell_3, Sub('10'): Cell_2, Sub('11'): Cell_2}
    ##############################
    # edges of all states
    Cell_0.bords = {Bord('0'): B4, Bord('1'): B3, Bord('2'): B3}
    Cell_1.bords = {Bord('0'): B3, Bord('1'): B4, Bord('2'): B4}
    Cell_2.bords = {Bord('0'): B4, Bord('1'): B4, Bord('2'): B3}
    Cell_3.bords = {Bord('0'): B3, Bord('1'): B3, Bord('2'): B4}
    ##############################
    # subdivisions of all states
    Cell_0.subs = {Sub('0'): Cell_1, Sub('1'): Cell_0, Sub('2'): Cell_1, Sub('3'): Cell_1, Sub('4'): Cell_1, Sub('5'): Cell_2, Sub('6'): Cell_3, Sub('7'): Cell_2, Sub('8'): Cell_3, Sub('9'): Cell_2, Sub('10'): Cell_2}
    Cell_1.subs = {Sub('0'): Cell_0, Sub('1'): Cell_0, Sub('2'): Cell_1, Sub('3'): Cell_1, Sub('4'): Cell_1, Sub('5'): Cell_2, Sub('6'): Cell_3, Sub('7'): Cell_2, Sub('8'): Cell_3, Sub('9'): Cell_2, Sub('10'): Cell_2}
    Cell_2.subs = {Sub('0'): Cell_0, Sub('1'): Cell_1, Sub('2'): Cell_0, Sub('3'): Cell_1, Sub('4'): Cell_1, Sub('5'): Cell_1, Sub('6'): Cell_3, Sub('7'): Cell_2, Sub('8'): Cell_3, Sub('9'): Cell_2, Sub('10'): Cell_2}
    Cell_3.subs = {Sub('0'): Cell_0, Sub('1'): Cell_1, Sub('2'): Cell_0, Sub('3'): Cell_1, Sub('4'): Cell_1, Sub('5'): Cell_1, Sub('6'): Cell_2, Sub('7'): Cell_2, Sub('8'): Cell_3, Sub('9'): Cell_2, Sub('10'): Cell_2}
    ##############################
    # build intern of all states
    Cell_0.buildIntern()
    Cell_1.buildIntern()
    Cell_2.buildIntern()
    Cell_3.buildIntern()
    ##############################
    # spaces of all states
    Cell_0.space = [Bord_('0'), Bord_('1'), Bord_('2')]
    Cell_1.space = [Bord_('0'), Bord_('1'), Bord_('2')]
    Cell_2.space = [Bord_('0'), Bord_('1'), Bord_('2')]
    Cell_3.space = [Bord_('0'), Bord_('1'), Bord_('2')]
    ##############################
    # grid of all states
    Cell_0.addGrid(Bord)
    Cell_1.addGrid(Bord)
    Cell_2.addGrid(Bord)
    Cell_3.addGrid(Bord)
    ##############################
    # prim of all states
    Cell_0.prim.elems = [Figure(2, [
        Bord_('0') + Sub('0') + Bord('0'),
        Bord_('0') + Sub('1') + Bord('0'),
        Bord_('0') + Sub('2') + Bord('0'),
        Bord_('0') + Sub('3') + Bord('0'),
        Bord_('1') + Sub('0') + Bord('0'),
        Bord_('1') + Sub('1') + Bord('0'),
        Bord_('1') + Sub('2') + Bord('0'),
        Bord_('2') + Sub('0') + Bord('0'),
        Bord_('2') + Sub('1') + Bord('0'),
        Bord_('2') + Sub('2') + Bord('0'),
    ])]
    Cell_1.prim.elems = [Figure(2, [
        Bord_('0') + Sub('0') + Bord('0'),
        Bord_('0') + Sub('1') + Bord('0'),
        Bord_('0') + Sub('2') + Bord('0'),
        Bord_('1') + Sub('0') + Bord('0'),
        Bord_('1') + Sub('1') + Bord('0'),
        Bord_('1') + Sub('2') + Bord('0'),
        Bord_('1') + Sub('3') + Bord('0'),
        Bord_('2') + Sub('0') + Bord('0'),
        Bord_('2') + Sub('1') + Bord('0'),
        Bord_('2') + Sub('2') + Bord('0'),
        Bord_('2') + Sub('3') + Bord('0'),
    ])]
    Cell_2.prim.elems = [Figure(2, [
        Bord_('0') + Sub('0') + Bord('0'),
        Bord_('0') + Sub('1') + Bord('0'),
        Bord_('0') + Sub('2') + Bord('0'),
        Bord_('0') + Sub('3') + Bord('0'),
        Bord_('1') + Sub('0') + Bord('0'),
        Bord_('1') + Sub('1') + Bord('0'),
        Bord_('1') + Sub('2') + Bord('0'),
        Bord_('1') + Sub('3') + Bord('0'),
        Bord_('2') + Sub('0') + Bord('0'),
        Bord_('2') + Sub('1') + Bord('0'),
        Bord_('2') + Sub('2') + Bord('0'),
    ])]
    Cell_3.prim.elems = [Figure(2, [
        Bord_('0') + Sub('0') + Bord('0'),
        Bord_('0') + Sub('1') + Bord('0'),
        Bord_('0') + Sub('2') + Bord('0'),
        Bord_('1') + Sub('0') + Bord('0'),
        Bord_('1') + Sub('1') + Bord('0'),
        Bord_('1') + Sub('2') + Bord('0'),
        Bord_('2') + Sub('0') + Bord('0'),
        Bord_('2') + Sub('1') + Bord('0'),
        Bord_('2') + Sub('2') + Bord('0'),
        Bord_('2') + Sub('3') + Bord('0'),
    ])]
    ##############################
    # constraints of all states
    # incidence constraints
    Cell_0(Bord('2') + Sub('1') + Permut('0'), Sub('0') + Bord('0'))
    Cell_0(Bord('0') + Sub('2') + Permut('0'), Sub('2') + Bord('2'))
    Cell_0(Bord('2') + Sub('2') + Permut('0'), Sub('3') + Bord('0'))
    Cell_0(Bord('0') + Sub('0') + Permut('0'), Sub('3') + Bord('2'))
    Cell_0(Bord('1') + Sub('1') + Permut('0'), Sub('5') + Bord('2'))
    Cell_0(Bord('2') + Sub('0') + Permut('0'), Sub('6') + Bord('0'))
    Cell_0(Bord('1') + Sub('2') + Permut('0'), Sub('6') + Bord('1'))
    Cell_0(Bord('0') + Sub('3') + Permut('0'), Sub('9') + Bord('0'))
    Cell_0(Bord('1') + Sub('0') + Permut('0'), Sub('9') + Bord('2'))
    Cell_0(Bord('0') + Sub('1') + Permut('0'), Sub('10') + Bord('0'))
    # adjacency constraints
    Cell_0(Sub('0') + Bord('0') + Bord('1'), Sub('6') + Bord('2') + Bord('1'))
    Cell_0(Sub('0') + Bord('1') + Bord('1'), Sub('7') + Bord('0') + Bord('1'))
    Cell_0(Sub('0') + Bord('2') + Bord('1'), Sub('3') + Bord('0') + Bord('1'))
    Cell_0(Sub('1') + Bord('0') + Bord('1'), Sub('7') + Bord('2') + Bord('1'))
    Cell_0(Sub('1') + Bord('1') + Bord('1'), Sub('8') + Bord('0') + Bord('1'))
    Cell_0(Sub('1') + Bord('2') + Bord('1'), Sub('10') + Bord('1') + Bord('1'))
    Cell_0(Sub('2') + Bord('0') + Bord('1'), Sub('8') + Bord('2') + Bord('1'))
    Cell_0(Sub('2') + Bord('1') + Bord('1'), Sub('9') + Bord('0') + Bord('1'))
    Cell_0(Sub('2') + Bord('2') + Bord('1'), Sub('10') + Bord('2') + Bord('1'))
    Cell_0(Sub('3') + Bord('1') + Bord('1'), Sub('10') + Bord('0') + Bord('1'))
    Cell_0(Sub('4') + Bord('0') + Bord('1'), Sub('7') + Bord('1') + Bord('1'))
    Cell_0(Sub('4') + Bord('1') + Bord('1'), Sub('5') + Bord('0') + Bord('1'))
    Cell_0(Sub('4') + Bord('2') + Bord('1'), Sub('8') + Bord('1') + Bord('1'))
    Cell_0(Sub('5') + Bord('1') + Bord('1'), Sub('6') + Bord('1') + Bord('1'))
    Cell_0(Sub('5') + Bord('2') + Bord('1'), Sub('9') + Bord('1') + Bord('1'))
    # edges adjacency constraints
    Cell_0(Bord('0') + Bord('1'), Bord('1') + Bord('0'))
    Cell_0(Bord('1') + Bord('1'), Bord('2') + Bord('0'))
    Cell_0(Bord('2') + Bord('1'), Bord('0') + Bord('0'))
    # incidence constraints
    Cell_1(Bord('0') + Sub('1') + Permut('0'), Sub('0') + Bord('2'))
    Cell_1(Bord('2') + Sub('1') + Permut('0'), Sub('1') + Bord('0'))
    Cell_1(Bord('0') + Sub('0') + Permut('0'), Sub('3') + Bord('0'))
    Cell_1(Bord('2') + Sub('3') + Permut('0'), Sub('3') + Bord('1'))
    Cell_1(Bord('1') + Sub('2') + Permut('0'), Sub('4') + Bord('1'))
    Cell_1(Bord('1') + Sub('1') + Permut('0'), Sub('5') + Bord('1'))
    Cell_1(Bord('0') + Sub('2') + Permut('0'), Sub('6') + Bord('0'))
    Cell_1(Bord('1') + Sub('0') + Permut('0'), Sub('6') + Bord('2'))
    Cell_1(Bord('2') + Sub('0') + Permut('0'), Sub('7') + Bord('0'))
    Cell_1(Bord('1') + Sub('3') + Permut('0'), Sub('7') + Bord('1'))
    Cell_1(Bord('2') + Sub('2') + Permut('0'), Sub('10') + Bord('1'))
    # adjacency constraints
    Cell_1(Sub('0') + Bord('0') + Bord('1'), Sub('9') + Bord('2') + Bord('1'))
    Cell_1(Sub('0') + Bord('1') + Bord('1'), Sub('6') + Bord('0') + Bord('1'))
    Cell_1(Sub('0') + Bord('2') + Bord('1'), Sub('3') + Bord('2') + Bord('1'))
    Cell_1(Sub('1') + Bord('0') + Bord('1'), Sub('7') + Bord('2') + Bord('1'))
    Cell_1(Sub('1') + Bord('1') + Bord('1'), Sub('8') + Bord('0') + Bord('1'))
    Cell_1(Sub('1') + Bord('2') + Bord('1'), Sub('10') + Bord('1') + Bord('1'))
    Cell_1(Sub('2') + Bord('0') + Bord('1'), Sub('8') + Bord('2') + Bord('1'))
    Cell_1(Sub('2') + Bord('1') + Bord('1'), Sub('9') + Bord('0') + Bord('1'))
    Cell_1(Sub('2') + Bord('2') + Bord('1'), Sub('10') + Bord('2') + Bord('1'))
    Cell_1(Sub('3') + Bord('1') + Bord('1'), Sub('10') + Bord('0') + Bord('1'))
    Cell_1(Sub('4') + Bord('0') + Bord('1'), Sub('7') + Bord('1') + Bord('1'))
    Cell_1(Sub('4') + Bord('1') + Bord('1'), Sub('5') + Bord('0') + Bord('1'))
    Cell_1(Sub('4') + Bord('2') + Bord('1'), Sub('8') + Bord('1') + Bord('1'))
    Cell_1(Sub('5') + Bord('1') + Bord('1'), Sub('6') + Bord('1') + Bord('1'))
    Cell_1(Sub('5') + Bord('2') + Bord('1'), Sub('9') + Bord('1') + Bord('1'))
    # edges adjacency constraints
    Cell_1(Bord('0') + Bord('1'), Bord('1') + Bord('0'))
    Cell_1(Bord('1') + Bord('1'), Bord('2') + Bord('0'))
    Cell_1(Bord('2') + Bord('1'), Bord('0') + Bord('0'))
    # incidence constraints
    Cell_2(Bord('2') + Sub('1') + Permut('0'), Sub('0') + Bord('1'))
    Cell_2(Bord('1') + Sub('2') + Permut('0'), Sub('1') + Bord('1'))
    Cell_2(Bord('0') + Sub('1') + Permut('0'), Sub('3') + Bord('1'))
    Cell_2(Bord('1') + Sub('0') + Permut('0'), Sub('5') + Bord('1'))
    Cell_2(Bord('0') + Sub('3') + Permut('0'), Sub('5') + Bord('2'))
    Cell_2(Bord('2') + Sub('0') + Permut('0'), Sub('6') + Bord('1'))
    Cell_2(Bord('1') + Sub('3') + Permut('0'), Sub('6') + Bord('2'))
    Cell_2(Bord('1') + Sub('1') + Permut('0'), Sub('7') + Bord('1'))
    Cell_2(Bord('0') + Sub('2') + Permut('0'), Sub('8') + Bord('2'))
    Cell_2(Bord('0') + Sub('0') + Permut('0'), Sub('9') + Bord('1'))
    Cell_2(Bord('2') + Sub('2') + Permut('0'), Sub('9') + Bord('2'))
    # adjacency constraints
    Cell_2(Sub('0') + Bord('0') + Bord('1'), Sub('9') + Bord('2') + Bord('1'))
    Cell_2(Sub('0') + Bord('1') + Bord('1'), Sub('6') + Bord('0') + Bord('1'))
    Cell_2(Sub('0') + Bord('2') + Bord('1'), Sub('4') + Bord('2') + Bord('1'))
    Cell_2(Sub('1') + Bord('0') + Bord('1'), Sub('6') + Bord('2') + Bord('1'))
    Cell_2(Sub('1') + Bord('1') + Bord('1'), Sub('7') + Bord('0') + Bord('1'))
    Cell_2(Sub('1') + Bord('2') + Bord('1'), Sub('4') + Bord('0') + Bord('1'))
    Cell_2(Sub('2') + Bord('0') + Bord('1'), Sub('7') + Bord('2') + Bord('1'))
    Cell_2(Sub('2') + Bord('1') + Bord('1'), Sub('8') + Bord('0') + Bord('1'))
    Cell_2(Sub('2') + Bord('2') + Bord('1'), Sub('10') + Bord('1') + Bord('1'))
    Cell_2(Sub('3') + Bord('0') + Bord('1'), Sub('8') + Bord('2') + Bord('1'))
    Cell_2(Sub('3') + Bord('1') + Bord('1'), Sub('9') + Bord('0') + Bord('1'))
    Cell_2(Sub('3') + Bord('2') + Bord('1'), Sub('10') + Bord('2') + Bord('1'))
    Cell_2(Sub('4') + Bord('1') + Bord('1'), Sub('10') + Bord('0') + Bord('1'))
    Cell_2(Sub('5') + Bord('0') + Bord('1'), Sub('7') + Bord('1') + Bord('1'))
    Cell_2(Sub('5') + Bord('2') + Bord('1'), Sub('8') + Bord('1') + Bord('1'))
    # edges adjacency constraints
    Cell_2(Bord('0') + Bord('1'), Bord('1') + Bord('0'))
    Cell_2(Bord('1') + Bord('1'), Bord('2') + Bord('0'))
    Cell_2(Bord('2') + Bord('1'), Bord('0') + Bord('0'))
    # incidence constraints
    Cell_3(Bord('1') + Sub('0') + Permut('0'), Sub('0') + Bord('1'))
    Cell_3(Bord('0') + Sub('2') + Permut('0'), Sub('0') + Bord('2'))
    Cell_3(Bord('0') + Sub('0') + Permut('0'), Sub('1') + Bord('0'))
    Cell_3(Bord('2') + Sub('3') + Permut('0'), Sub('1') + Bord('1'))
    Cell_3(Bord('0') + Sub('1') + Permut('0'), Sub('4') + Bord('0'))
    Cell_3(Bord('2') + Sub('1') + Permut('0'), Sub('5') + Bord('1'))
    Cell_3(Bord('2') + Sub('0') + Permut('0'), Sub('6') + Bord('1'))
    Cell_3(Bord('1') + Sub('2') + Permut('0'), Sub('6') + Bord('2'))
    Cell_3(Bord('2') + Sub('2') + Permut('0'), Sub('7') + Bord('1'))
    Cell_3(Bord('1') + Sub('1') + Permut('0'), Sub('9') + Bord('2'))
    # adjacency constraints
    Cell_3(Sub('0') + Bord('0') + Bord('1'), Sub('9') + Bord('2') + Bord('1'))
    Cell_3(Sub('0') + Bord('2') + Bord('1'), Sub('4') + Bord('2') + Bord('1'))
    Cell_3(Sub('1') + Bord('1') + Bord('1'), Sub('7') + Bord('0') + Bord('1'))
    Cell_3(Sub('1') + Bord('2') + Bord('1'), Sub('4') + Bord('0') + Bord('1'))
    Cell_3(Sub('2') + Bord('0') + Bord('1'), Sub('7') + Bord('2') + Bord('1'))
    Cell_3(Sub('2') + Bord('1') + Bord('1'), Sub('8') + Bord('0') + Bord('1'))
    Cell_3(Sub('2') + Bord('2') + Bord('1'), Sub('10') + Bord('1') + Bord('1'))
    Cell_3(Sub('3') + Bord('0') + Bord('1'), Sub('8') + Bord('2') + Bord('1'))
    Cell_3(Sub('3') + Bord('1') + Bord('1'), Sub('9') + Bord('0') + Bord('1'))
    Cell_3(Sub('3') + Bord('2') + Bord('1'), Sub('10') + Bord('2') + Bord('1'))
    Cell_3(Sub('4') + Bord('1') + Bord('1'), Sub('10') + Bord('0') + Bord('1'))
    Cell_3(Sub('5') + Bord('0') + Bord('1'), Sub('7') + Bord('1') + Bord('1'))
    Cell_3(Sub('5') + Bord('1') + Bord('1'), Sub('6') + Bord('0') + Bord('1'))
    Cell_3(Sub('5') + Bord('2') + Bord('1'), Sub('8') + Bord('1') + Bord('1'))
    Cell_3(Sub('6') + Bord('2') + Bord('1'), Sub('9') + Bord('1') + Bord('1'))
    # edges adjacency constraints
    Cell_3(Bord('0') + Bord('1'), Bord('1') + Bord('0'))
    Cell_3(Bord('1') + Bord('1'), Bord('2') + Bord('0'))
    Cell_3(Bord('2') + Bord('1'), Bord('0') + Bord('0'))
    # constraints on init cells
    init(Sub('0') + Bord('0') + Bord('1'), Sub('10') + Bord('2') + Bord('1'))
    init(Sub('0') + Bord('1') + Bord('1'), Sub('7') + Bord('0') + Bord('1'))
    init(Sub('0') + Bord('2') + Bord('1'), Sub('4') + Bord('2') + Bord('1'))
    init(Sub('1') + Bord('0') + Bord('1'), Sub('7') + Bord('2') + Bord('1'))
    init(Sub('1') + Bord('1') + Bord('1'), Sub('8') + Bord('0') + Bord('1'))
    init(Sub('1') + Bord('2') + Bord('1'), Sub('4') + Bord('0') + Bord('1'))
    init(Sub('2') + Bord('0') + Bord('1'), Sub('8') + Bord('2') + Bord('1'))
    init(Sub('2') + Bord('1') + Bord('1'), Sub('9') + Bord('0') + Bord('1'))
    init(Sub('2') + Bord('2') + Bord('1'), Sub('11') + Bord('1') + Bord('1'))
    init(Sub('3') + Bord('0') + Bord('1'), Sub('9') + Bord('2') + Bord('1'))
    init(Sub('3') + Bord('1') + Bord('1'), Sub('10') + Bord('0') + Bord('1'))
    init(Sub('3') + Bord('2') + Bord('1'), Sub('11') + Bord('2') + Bord('1'))
    init(Sub('4') + Bord('1') + Bord('1'), Sub('11') + Bord('0') + Bord('1'))
    init(Sub('5') + Bord('0') + Bord('1'), Sub('8') + Bord('1') + Bord('1'))
    init(Sub('5') + Bord('1') + Bord('1'), Sub('6') + Bord('0') + Bord('1'))
    init(Sub('5') + Bord('2') + Bord('1'), Sub('9') + Bord('1') + Bord('1'))
    init(Sub('6') + Bord('1') + Bord('1'), Sub('7') + Bord('1') + Bord('1'))
    init(Sub('6') + Bord('2') + Bord('1'), Sub('10') + Bord('1') + Bord('1'))
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
