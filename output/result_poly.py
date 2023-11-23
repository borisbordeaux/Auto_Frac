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
    B3 = Etat('B3', 1)
    B3.bords = {Bord('0'): s, Bord('1'): s}
    B3.permuts = {Permut('0'): B3}
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
    # Cell_0 -- B2 (3) -- B2 (1) -- B2 (2) -- B2 (9) -- B2 (4)
    Cell_0 = Etat('Cell_0', 0)
    # Cell_1 -- B2 (1) -- B2 (3) -- B2 (7) -- B2 (5)
    Cell_1 = Etat('Cell_1', 0)
    # Cell_2 -- B2 (12) -- B3 (13) -- B2 (9) -- B2 (2)
    Cell_2 = Etat('Cell_2', 0)
    # Cell_3 -- B2 (6) -- B2 (11) -- B3 (13) -- B2 (12)
    Cell_3 = Etat('Cell_3', 0)
    # Cell_4 -- B2 (11) -- B2 (8) -- B2 (10) -- B3 (13)
    Cell_4 = Etat('Cell_4', 0)
    # Cell_5 -- B3 (13) -- B2 (10) -- B2 (4) -- B2 (9)
    Cell_5 = Etat('Cell_5', 0)
    ##############################
    # subd of init
    init.subs = {Sub('0'): Cell_0, Sub('1'): Cell_0, Sub('2'): Cell_0, Sub('3'): Cell_0, Sub('4'): Cell_1, Sub('5'): Cell_2, Sub('6'): Cell_3, Sub('7'): Cell_4, Sub('8'): Cell_5}
    ##############################
    # edges of all states
    Cell_0.bords = {Bord('0'): B2, Bord('1'): B2, Bord('2'): B2, Bord('3'): B2, Bord('4'): B2}
    Cell_1.bords = {Bord('0'): B2, Bord('1'): B2, Bord('2'): B2, Bord('3'): B2}
    Cell_2.bords = {Bord('0'): B2, Bord('1'): B3, Bord('2'): B2, Bord('3'): B2}
    Cell_3.bords = {Bord('0'): B2, Bord('1'): B2, Bord('2'): B3, Bord('3'): B2}
    Cell_4.bords = {Bord('0'): B2, Bord('1'): B2, Bord('2'): B2, Bord('3'): B3}
    Cell_5.bords = {Bord('0'): B3, Bord('1'): B2, Bord('2'): B2, Bord('3'): B2}
    ##############################
    # subdivisions of all states
    Cell_0.subs = {Sub('0'): Cell_0, Sub('1'): Cell_0, Sub('2'): Cell_0, Sub('3'): Cell_1, Sub('4'): Cell_2, Sub('5'): Cell_3, Sub('6'): Cell_4, Sub('7'): Cell_5}
    Cell_1.subs = {Sub('0'): Cell_0, Sub('1'): Cell_0, Sub('2'): Cell_0, Sub('3'): Cell_0, Sub('4'): Cell_2, Sub('5'): Cell_3, Sub('6'): Cell_4, Sub('7'): Cell_5}
    Cell_2.subs = {Sub('0'): Cell_0, Sub('1'): Cell_0, Sub('2'): Cell_0, Sub('3'): Cell_0, Sub('4'): Cell_1, Sub('5'): Cell_3, Sub('6'): Cell_4, Sub('7'): Cell_5}
    Cell_3.subs = {Sub('0'): Cell_0, Sub('1'): Cell_0, Sub('2'): Cell_0, Sub('3'): Cell_0, Sub('4'): Cell_1, Sub('5'): Cell_2, Sub('6'): Cell_4, Sub('7'): Cell_5}
    Cell_4.subs = {Sub('0'): Cell_0, Sub('1'): Cell_0, Sub('2'): Cell_0, Sub('3'): Cell_0, Sub('4'): Cell_1, Sub('5'): Cell_2, Sub('6'): Cell_3, Sub('7'): Cell_5}
    Cell_5.subs = {Sub('0'): Cell_0, Sub('1'): Cell_0, Sub('2'): Cell_0, Sub('3'): Cell_0, Sub('4'): Cell_1, Sub('5'): Cell_2, Sub('6'): Cell_3, Sub('7'): Cell_4}
    ##############################
    # build intern of all states
    Cell_0.buildIntern()
    Cell_1.buildIntern()
    Cell_2.buildIntern()
    Cell_3.buildIntern()
    Cell_4.buildIntern()
    Cell_5.buildIntern()
    ##############################
    # spaces of all states
    Cell_0.space = [Bord_('0'), Bord_('1'), Bord_('2'), Bord_('3'), Bord_('4')]
    Cell_1.space = [Bord_('0'), Bord_('1'), Bord_('2'), Bord_('3')]
    Cell_2.space = [Bord_('0'), Bord_('1'), Bord_('2'), Bord_('3')]
    Cell_3.space = [Bord_('0'), Bord_('1'), Bord_('2'), Bord_('3')]
    Cell_4.space = [Bord_('0'), Bord_('1'), Bord_('2'), Bord_('3')]
    Cell_5.space = [Bord_('0'), Bord_('1'), Bord_('2'), Bord_('3')]
    ##############################
    # grid of all states
    Cell_0.addGrid(Bord)
    Cell_1.addGrid(Bord)
    Cell_2.addGrid(Bord)
    Cell_3.addGrid(Bord)
    Cell_4.addGrid(Bord)
    Cell_5.addGrid(Bord)
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
        Bord_('4') + Sub('0') + Sub('0') + Bord('0'),
        Bord_('4') + Sub('0') + Sub('1') + Bord('0'),
        Bord_('4') + Sub('1') + Sub('0') + Bord('0'),
        Bord_('4') + Sub('1') + Sub('1') + Bord('0'),
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
    ])]
    Cell_2.prim.elems = [Figure(2, [
        Bord_('0') + Sub('0') + Sub('0') + Bord('0'),
        Bord_('0') + Sub('0') + Sub('1') + Bord('0'),
        Bord_('0') + Sub('1') + Sub('0') + Bord('0'),
        Bord_('0') + Sub('1') + Sub('1') + Bord('0'),
        Bord_('1') + Sub('0') + Bord('0'),
        Bord_('1') + Sub('1') + Bord('0'),
        Bord_('1') + Sub('2') + Bord('0'),
        Bord_('2') + Sub('0') + Sub('0') + Bord('0'),
        Bord_('2') + Sub('0') + Sub('1') + Bord('0'),
        Bord_('2') + Sub('1') + Sub('0') + Bord('0'),
        Bord_('2') + Sub('1') + Sub('1') + Bord('0'),
        Bord_('3') + Sub('0') + Sub('0') + Bord('0'),
        Bord_('3') + Sub('0') + Sub('1') + Bord('0'),
        Bord_('3') + Sub('1') + Sub('0') + Bord('0'),
        Bord_('3') + Sub('1') + Sub('1') + Bord('0'),
    ])]
    Cell_3.prim.elems = [Figure(2, [
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
        Bord_('3') + Sub('0') + Sub('0') + Bord('0'),
        Bord_('3') + Sub('0') + Sub('1') + Bord('0'),
        Bord_('3') + Sub('1') + Sub('0') + Bord('0'),
        Bord_('3') + Sub('1') + Sub('1') + Bord('0'),
    ])]
    Cell_4.prim.elems = [Figure(2, [
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
        Bord_('3') + Sub('0') + Bord('0'),
        Bord_('3') + Sub('1') + Bord('0'),
        Bord_('3') + Sub('2') + Bord('0'),
    ])]
    Cell_5.prim.elems = [Figure(2, [
        Bord_('0') + Sub('0') + Bord('0'),
        Bord_('0') + Sub('1') + Bord('0'),
        Bord_('0') + Sub('2') + Bord('0'),
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
    ##############################
    # constraints of all states
    # incidence constraints
    Cell_0(Bord('0') + Sub('0') + Permut('0'), Sub('0') + Bord('1'))
    Cell_0(Bord('4') + Sub('1') + Permut('0'), Sub('0') + Bord('2'))
    Cell_0(Bord('1') + Sub('1') + Permut('0'), Sub('2') + Bord('0'))
    Cell_0(Bord('2') + Sub('0') + Permut('0'), Sub('2') + Bord('4'))
    Cell_0(Bord('1') + Sub('0') + Permut('0'), Sub('3') + Bord('0'))
    Cell_0(Bord('0') + Sub('1') + Permut('0'), Sub('3') + Bord('1'))
    Cell_0(Bord('3') + Sub('0') + Permut('0'), Sub('4') + Bord('2'))
    Cell_0(Bord('2') + Sub('1') + Permut('0'), Sub('4') + Bord('3'))
    Cell_0(Bord('4') + Sub('0') + Permut('0'), Sub('7') + Bord('2'))
    Cell_0(Bord('3') + Sub('1') + Permut('0'), Sub('7') + Bord('3'))
    # adjacency constraints
    Cell_0(Sub('0') + Bord('0') + Bord('1'), Sub('3') + Bord('1') + Bord('1'))
    Cell_0(Sub('0') + Bord('2') + Bord('1'), Sub('7') + Bord('1') + Bord('1'))
    Cell_0(Sub('0') + Bord('3') + Bord('1'), Sub('6') + Bord('1') + Bord('1'))
    Cell_0(Sub('0') + Bord('4') + Bord('1'), Sub('1') + Bord('1') + Bord('1'))
    Cell_0(Sub('1') + Bord('0') + Bord('1'), Sub('3') + Bord('2') + Bord('1'))
    Cell_0(Sub('1') + Bord('2') + Bord('1'), Sub('6') + Bord('0') + Bord('1'))
    Cell_0(Sub('1') + Bord('3') + Bord('1'), Sub('5') + Bord('0') + Bord('1'))
    Cell_0(Sub('1') + Bord('4') + Bord('1'), Sub('2') + Bord('1') + Bord('1'))
    Cell_0(Sub('2') + Bord('0') + Bord('1'), Sub('3') + Bord('3') + Bord('1'))
    Cell_0(Sub('2') + Bord('2') + Bord('1'), Sub('5') + Bord('3') + Bord('1'))
    Cell_0(Sub('2') + Bord('3') + Bord('1'), Sub('4') + Bord('3') + Bord('1'))
    Cell_0(Sub('4') + Bord('0') + Bord('1'), Sub('5') + Bord('2') + Bord('1'))
    Cell_0(Sub('4') + Bord('1') + Bord('1'), Sub('7') + Bord('3') + Bord('1'))
    Cell_0(Sub('5') + Bord('1') + Bord('1'), Sub('6') + Bord('3') + Bord('1'))
    Cell_0(Sub('6') + Bord('2') + Bord('1'), Sub('7') + Bord('0') + Bord('1'))
    # edges adjacency constraints
    Cell_0(Bord('0') + Bord('1'), Bord('1') + Bord('0'))
    Cell_0(Bord('1') + Bord('1'), Bord('2') + Bord('0'))
    Cell_0(Bord('2') + Bord('1'), Bord('3') + Bord('0'))
    Cell_0(Bord('3') + Bord('1'), Bord('4') + Bord('0'))
    Cell_0(Bord('4') + Bord('1'), Bord('0') + Bord('0'))
    # incidence constraints
    Cell_1(Bord('1') + Sub('0') + Permut('0'), Sub('0') + Bord('0'))
    Cell_1(Bord('0') + Sub('1') + Permut('0'), Sub('0') + Bord('1'))
    Cell_1(Bord('2') + Sub('0') + Permut('0'), Sub('1') + Bord('0'))
    Cell_1(Bord('1') + Sub('1') + Permut('0'), Sub('1') + Bord('1'))
    Cell_1(Bord('3') + Sub('0') + Permut('0'), Sub('2') + Bord('0'))
    Cell_1(Bord('2') + Sub('1') + Permut('0'), Sub('2') + Bord('1'))
    Cell_1(Bord('0') + Sub('0') + Permut('0'), Sub('3') + Bord('0'))
    Cell_1(Bord('3') + Sub('1') + Permut('0'), Sub('3') + Bord('1'))
    # adjacency constraints
    Cell_1(Sub('0') + Bord('1') + Bord('1'), Sub('3') + Bord('4') + Bord('1'))
    Cell_1(Sub('0') + Bord('2') + Bord('1'), Sub('4') + Bord('2') + Bord('1'))
    Cell_1(Sub('0') + Bord('3') + Bord('1'), Sub('7') + Bord('2') + Bord('1'))
    Cell_1(Sub('0') + Bord('4') + Bord('1'), Sub('1') + Bord('1') + Bord('1'))
    Cell_1(Sub('1') + Bord('2') + Bord('1'), Sub('7') + Bord('1') + Bord('1'))
    Cell_1(Sub('1') + Bord('3') + Bord('1'), Sub('6') + Bord('1') + Bord('1'))
    Cell_1(Sub('1') + Bord('4') + Bord('1'), Sub('2') + Bord('1') + Bord('1'))
    Cell_1(Sub('2') + Bord('2') + Bord('1'), Sub('6') + Bord('0') + Bord('1'))
    Cell_1(Sub('2') + Bord('3') + Bord('1'), Sub('5') + Bord('0') + Bord('1'))
    Cell_1(Sub('2') + Bord('4') + Bord('1'), Sub('3') + Bord('1') + Bord('1'))
    Cell_1(Sub('3') + Bord('2') + Bord('1'), Sub('5') + Bord('3') + Bord('1'))
    Cell_1(Sub('3') + Bord('3') + Bord('1'), Sub('4') + Bord('3') + Bord('1'))
    Cell_1(Sub('4') + Bord('0') + Bord('1'), Sub('5') + Bord('2') + Bord('1'))
    Cell_1(Sub('4') + Bord('1') + Bord('1'), Sub('7') + Bord('3') + Bord('1'))
    Cell_1(Sub('5') + Bord('1') + Bord('1'), Sub('6') + Bord('3') + Bord('1'))
    Cell_1(Sub('6') + Bord('2') + Bord('1'), Sub('7') + Bord('0') + Bord('1'))
    # edges adjacency constraints
    Cell_1(Bord('0') + Bord('1'), Bord('1') + Bord('0'))
    Cell_1(Bord('1') + Bord('1'), Bord('2') + Bord('0'))
    Cell_1(Bord('2') + Bord('1'), Bord('3') + Bord('0'))
    Cell_1(Bord('3') + Bord('1'), Bord('0') + Bord('0'))
    # incidence constraints
    Cell_2(Bord('3') + Sub('0') + Permut('0'), Sub('0') + Bord('2'))
    Cell_2(Bord('2') + Sub('1') + Permut('0'), Sub('0') + Bord('3'))
    Cell_2(Bord('0') + Sub('0') + Permut('0'), Sub('3') + Bord('3'))
    Cell_2(Bord('3') + Sub('1') + Permut('0'), Sub('3') + Bord('4'))
    Cell_2(Bord('1') + Sub('0') + Permut('0'), Sub('5') + Bord('2'))
    Cell_2(Bord('0') + Sub('1') + Permut('0'), Sub('5') + Bord('3'))
    Cell_2(Bord('1') + Sub('1') + Permut('0'), Sub('6') + Bord('3'))
    Cell_2(Bord('1') + Sub('2') + Permut('0'), Sub('7') + Bord('0'))
    Cell_2(Bord('2') + Sub('0') + Permut('0'), Sub('7') + Bord('3'))
    # adjacency constraints
    Cell_2(Sub('0') + Bord('0') + Bord('1'), Sub('4') + Bord('0') + Bord('1'))
    Cell_2(Sub('0') + Bord('1') + Bord('1'), Sub('3') + Bord('4') + Bord('1'))
    Cell_2(Sub('0') + Bord('3') + Bord('1'), Sub('7') + Bord('2') + Bord('1'))
    Cell_2(Sub('0') + Bord('4') + Bord('1'), Sub('1') + Bord('1') + Bord('1'))
    Cell_2(Sub('1') + Bord('0') + Bord('1'), Sub('4') + Bord('1') + Bord('1'))
    Cell_2(Sub('1') + Bord('2') + Bord('1'), Sub('7') + Bord('1') + Bord('1'))
    Cell_2(Sub('1') + Bord('3') + Bord('1'), Sub('6') + Bord('1') + Bord('1'))
    Cell_2(Sub('1') + Bord('4') + Bord('1'), Sub('2') + Bord('1') + Bord('1'))
    Cell_2(Sub('2') + Bord('0') + Bord('1'), Sub('4') + Bord('2') + Bord('1'))
    Cell_2(Sub('2') + Bord('2') + Bord('1'), Sub('6') + Bord('0') + Bord('1'))
    Cell_2(Sub('2') + Bord('3') + Bord('1'), Sub('5') + Bord('0') + Bord('1'))
    Cell_2(Sub('2') + Bord('4') + Bord('1'), Sub('3') + Bord('1') + Bord('1'))
    Cell_2(Sub('3') + Bord('0') + Bord('1'), Sub('4') + Bord('3') + Bord('1'))
    Cell_2(Sub('3') + Bord('2') + Bord('1'), Sub('5') + Bord('3') + Bord('1'))
    Cell_2(Sub('5') + Bord('1') + Bord('1'), Sub('6') + Bord('3') + Bord('1'))
    Cell_2(Sub('6') + Bord('2') + Bord('1'), Sub('7') + Bord('0') + Bord('1'))
    # edges adjacency constraints
    Cell_2(Bord('0') + Bord('1'), Bord('1') + Bord('0'))
    Cell_2(Bord('1') + Bord('1'), Bord('2') + Bord('0'))
    Cell_2(Bord('2') + Bord('1'), Bord('3') + Bord('0'))
    Cell_2(Bord('3') + Bord('1'), Bord('0') + Bord('0'))
    # incidence constraints
    Cell_3(Bord('1') + Sub('0') + Permut('0'), Sub('2') + Bord('3'))
    Cell_3(Bord('0') + Sub('1') + Permut('0'), Sub('2') + Bord('4'))
    Cell_3(Bord('0') + Sub('0') + Permut('0'), Sub('3') + Bord('2'))
    Cell_3(Bord('3') + Sub('1') + Permut('0'), Sub('3') + Bord('3'))
    Cell_3(Bord('3') + Sub('0') + Permut('0'), Sub('5') + Bord('0'))
    Cell_3(Bord('2') + Sub('2') + Permut('0'), Sub('5') + Bord('1'))
    Cell_3(Bord('1') + Sub('1') + Permut('0'), Sub('6') + Bord('0'))
    Cell_3(Bord('2') + Sub('0') + Permut('0'), Sub('6') + Bord('3'))
    Cell_3(Bord('2') + Sub('1') + Permut('0'), Sub('7') + Bord('0'))
    # adjacency constraints
    Cell_3(Sub('0') + Bord('0') + Bord('1'), Sub('4') + Bord('0') + Bord('1'))
    Cell_3(Sub('0') + Bord('1') + Bord('1'), Sub('3') + Bord('4') + Bord('1'))
    Cell_3(Sub('0') + Bord('2') + Bord('1'), Sub('5') + Bord('2') + Bord('1'))
    Cell_3(Sub('0') + Bord('3') + Bord('1'), Sub('7') + Bord('2') + Bord('1'))
    Cell_3(Sub('0') + Bord('4') + Bord('1'), Sub('1') + Bord('1') + Bord('1'))
    Cell_3(Sub('1') + Bord('0') + Bord('1'), Sub('4') + Bord('1') + Bord('1'))
    Cell_3(Sub('1') + Bord('2') + Bord('1'), Sub('7') + Bord('1') + Bord('1'))
    Cell_3(Sub('1') + Bord('3') + Bord('1'), Sub('6') + Bord('1') + Bord('1'))
    Cell_3(Sub('1') + Bord('4') + Bord('1'), Sub('2') + Bord('1') + Bord('1'))
    Cell_3(Sub('2') + Bord('0') + Bord('1'), Sub('4') + Bord('2') + Bord('1'))
    Cell_3(Sub('2') + Bord('2') + Bord('1'), Sub('6') + Bord('0') + Bord('1'))
    Cell_3(Sub('2') + Bord('4') + Bord('1'), Sub('3') + Bord('1') + Bord('1'))
    Cell_3(Sub('3') + Bord('0') + Bord('1'), Sub('4') + Bord('3') + Bord('1'))
    Cell_3(Sub('3') + Bord('3') + Bord('1'), Sub('5') + Bord('3') + Bord('1'))
    Cell_3(Sub('5') + Bord('1') + Bord('1'), Sub('7') + Bord('3') + Bord('1'))
    Cell_3(Sub('6') + Bord('2') + Bord('1'), Sub('7') + Bord('0') + Bord('1'))
    # edges adjacency constraints
    Cell_3(Bord('0') + Bord('1'), Bord('1') + Bord('0'))
    Cell_3(Bord('1') + Bord('1'), Bord('2') + Bord('0'))
    Cell_3(Bord('2') + Bord('1'), Bord('3') + Bord('0'))
    Cell_3(Bord('3') + Bord('1'), Bord('0') + Bord('0'))
    # incidence constraints
    Cell_4(Bord('2') + Sub('0') + Permut('0'), Sub('1') + Bord('3'))
    Cell_4(Bord('1') + Sub('1') + Permut('0'), Sub('1') + Bord('4'))
    Cell_4(Bord('1') + Sub('0') + Permut('0'), Sub('2') + Bord('2'))
    Cell_4(Bord('0') + Sub('1') + Permut('0'), Sub('2') + Bord('3'))
    Cell_4(Bord('3') + Sub('1') + Permut('0'), Sub('5') + Bord('1'))
    Cell_4(Bord('0') + Sub('0') + Permut('0'), Sub('6') + Bord('1'))
    Cell_4(Bord('3') + Sub('2') + Permut('0'), Sub('6') + Bord('2'))
    Cell_4(Bord('3') + Sub('0') + Permut('0'), Sub('7') + Bord('0'))
    Cell_4(Bord('2') + Sub('1') + Permut('0'), Sub('7') + Bord('1'))
    # adjacency constraints
    Cell_4(Sub('0') + Bord('0') + Bord('1'), Sub('4') + Bord('0') + Bord('1'))
    Cell_4(Sub('0') + Bord('1') + Bord('1'), Sub('3') + Bord('4') + Bord('1'))
    Cell_4(Sub('0') + Bord('2') + Bord('1'), Sub('5') + Bord('2') + Bord('1'))
    Cell_4(Sub('0') + Bord('3') + Bord('1'), Sub('7') + Bord('2') + Bord('1'))
    Cell_4(Sub('0') + Bord('4') + Bord('1'), Sub('1') + Bord('1') + Bord('1'))
    Cell_4(Sub('1') + Bord('0') + Bord('1'), Sub('4') + Bord('1') + Bord('1'))
    Cell_4(Sub('1') + Bord('2') + Bord('1'), Sub('7') + Bord('1') + Bord('1'))
    Cell_4(Sub('1') + Bord('4') + Bord('1'), Sub('2') + Bord('1') + Bord('1'))
    Cell_4(Sub('2') + Bord('0') + Bord('1'), Sub('4') + Bord('2') + Bord('1'))
    Cell_4(Sub('2') + Bord('3') + Bord('1'), Sub('6') + Bord('0') + Bord('1'))
    Cell_4(Sub('2') + Bord('4') + Bord('1'), Sub('3') + Bord('1') + Bord('1'))
    Cell_4(Sub('3') + Bord('0') + Bord('1'), Sub('4') + Bord('3') + Bord('1'))
    Cell_4(Sub('3') + Bord('2') + Bord('1'), Sub('6') + Bord('3') + Bord('1'))
    Cell_4(Sub('3') + Bord('3') + Bord('1'), Sub('5') + Bord('3') + Bord('1'))
    Cell_4(Sub('5') + Bord('0') + Bord('1'), Sub('6') + Bord('2') + Bord('1'))
    Cell_4(Sub('5') + Bord('1') + Bord('1'), Sub('7') + Bord('3') + Bord('1'))
    # edges adjacency constraints
    Cell_4(Bord('0') + Bord('1'), Bord('1') + Bord('0'))
    Cell_4(Bord('1') + Bord('1'), Bord('2') + Bord('0'))
    Cell_4(Bord('2') + Bord('1'), Bord('3') + Bord('0'))
    Cell_4(Bord('3') + Bord('1'), Bord('0') + Bord('0'))
    # incidence constraints
    Cell_5(Bord('3') + Sub('0') + Permut('0'), Sub('0') + Bord('3'))
    Cell_5(Bord('2') + Sub('1') + Permut('0'), Sub('0') + Bord('4'))
    Cell_5(Bord('2') + Sub('0') + Permut('0'), Sub('1') + Bord('2'))
    Cell_5(Bord('1') + Sub('1') + Permut('0'), Sub('1') + Bord('3'))
    Cell_5(Bord('0') + Sub('0') + Permut('0'), Sub('5') + Bord('1'))
    Cell_5(Bord('3') + Sub('1') + Permut('0'), Sub('5') + Bord('2'))
    Cell_5(Bord('0') + Sub('1') + Permut('0'), Sub('6') + Bord('2'))
    Cell_5(Bord('1') + Sub('0') + Permut('0'), Sub('7') + Bord('2'))
    Cell_5(Bord('0') + Sub('2') + Permut('0'), Sub('7') + Bord('3'))
    # adjacency constraints
    Cell_5(Sub('0') + Bord('0') + Bord('1'), Sub('4') + Bord('0') + Bord('1'))
    Cell_5(Sub('0') + Bord('1') + Bord('1'), Sub('3') + Bord('4') + Bord('1'))
    Cell_5(Sub('0') + Bord('2') + Bord('1'), Sub('5') + Bord('2') + Bord('1'))
    Cell_5(Sub('0') + Bord('4') + Bord('1'), Sub('1') + Bord('1') + Bord('1'))
    Cell_5(Sub('1') + Bord('0') + Bord('1'), Sub('4') + Bord('1') + Bord('1'))
    Cell_5(Sub('1') + Bord('3') + Bord('1'), Sub('7') + Bord('1') + Bord('1'))
    Cell_5(Sub('1') + Bord('4') + Bord('1'), Sub('2') + Bord('1') + Bord('1'))
    Cell_5(Sub('2') + Bord('0') + Bord('1'), Sub('4') + Bord('2') + Bord('1'))
    Cell_5(Sub('2') + Bord('2') + Bord('1'), Sub('7') + Bord('0') + Bord('1'))
    Cell_5(Sub('2') + Bord('3') + Bord('1'), Sub('6') + Bord('0') + Bord('1'))
    Cell_5(Sub('2') + Bord('4') + Bord('1'), Sub('3') + Bord('1') + Bord('1'))
    Cell_5(Sub('3') + Bord('0') + Bord('1'), Sub('4') + Bord('3') + Bord('1'))
    Cell_5(Sub('3') + Bord('2') + Bord('1'), Sub('6') + Bord('3') + Bord('1'))
    Cell_5(Sub('3') + Bord('3') + Bord('1'), Sub('5') + Bord('3') + Bord('1'))
    Cell_5(Sub('5') + Bord('0') + Bord('1'), Sub('6') + Bord('2') + Bord('1'))
    Cell_5(Sub('6') + Bord('1') + Bord('1'), Sub('7') + Bord('3') + Bord('1'))
    # edges adjacency constraints
    Cell_5(Bord('0') + Bord('1'), Bord('1') + Bord('0'))
    Cell_5(Bord('1') + Bord('1'), Bord('2') + Bord('0'))
    Cell_5(Bord('2') + Bord('1'), Bord('3') + Bord('0'))
    Cell_5(Bord('3') + Bord('1'), Bord('0') + Bord('0'))
    # constraints on init cells
    init(Sub('0') + Bord('0') + Bord('1'), Sub('4') + Bord('0') + Bord('1'))
    init(Sub('0') + Bord('1') + Bord('1'), Sub('3') + Bord('4') + Bord('1'))
    init(Sub('0') + Bord('2') + Bord('1'), Sub('5') + Bord('2') + Bord('1'))
    init(Sub('0') + Bord('3') + Bord('1'), Sub('8') + Bord('2') + Bord('1'))
    init(Sub('0') + Bord('4') + Bord('1'), Sub('1') + Bord('1') + Bord('1'))
    init(Sub('1') + Bord('0') + Bord('1'), Sub('4') + Bord('1') + Bord('1'))
    init(Sub('1') + Bord('2') + Bord('1'), Sub('8') + Bord('1') + Bord('1'))
    init(Sub('1') + Bord('3') + Bord('1'), Sub('7') + Bord('1') + Bord('1'))
    init(Sub('1') + Bord('4') + Bord('1'), Sub('2') + Bord('1') + Bord('1'))
    init(Sub('2') + Bord('0') + Bord('1'), Sub('4') + Bord('2') + Bord('1'))
    init(Sub('2') + Bord('2') + Bord('1'), Sub('7') + Bord('0') + Bord('1'))
    init(Sub('2') + Bord('3') + Bord('1'), Sub('6') + Bord('0') + Bord('1'))
    init(Sub('2') + Bord('4') + Bord('1'), Sub('3') + Bord('1') + Bord('1'))
    init(Sub('3') + Bord('0') + Bord('1'), Sub('4') + Bord('3') + Bord('1'))
    init(Sub('3') + Bord('2') + Bord('1'), Sub('6') + Bord('3') + Bord('1'))
    init(Sub('3') + Bord('3') + Bord('1'), Sub('5') + Bord('3') + Bord('1'))
    init(Sub('5') + Bord('0') + Bord('1'), Sub('6') + Bord('2') + Bord('1'))
    init(Sub('5') + Bord('1') + Bord('1'), Sub('8') + Bord('3') + Bord('1'))
    init(Sub('6') + Bord('1') + Bord('1'), Sub('7') + Bord('3') + Bord('1'))
    init(Sub('7') + Bord('2') + Bord('1'), Sub('8') + Bord('0') + Bord('1'))
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
