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
    # B_2_0 - B_2_0 - B_2_0 - B_2_0 / B_2_0 - B_2_0 - B_2_0 / 0 / 2
    Cell_0 = Etat('Cell_0', 0)
    Vol_0 = Etat('Vol_0', 0)
    ##############################
    # subd of init
    init.subs = {Sub('0'): Vol_0}
    ##############################
    # edges of all states
    Cell_0.bords = {Bord('0'): B2, Bord('1'): B2, Bord('2'): B2, Bord('3'): B2}
    Vol_0.bords = {Bord('0'): Cell_0, Bord('1'): Cell_0, Bord('2'): Cell_0, Bord('3'): Cell_0, Bord('4'): Cell_0, Bord('5'): Cell_0}
    ##############################
    # subdivisions of all states
    Cell_0.subs = {Sub('0'): Cell_0, Sub('1'): Cell_0, Sub('2'): Cell_0, Sub('3'): Cell_0, Sub('4'): Cell_0, Sub('5'): Cell_0, Sub('6'): Cell_0, Sub('7'): Cell_0}
    # need 48 subs
    Vol_0.subs = {}
    for i in range(48):
        Vol_0.subs[Sub(str(i))] = Vol_0
    ##############################
    # build intern of all states
    Cell_0.buildIntern()
    Vol_0.buildIntern()
    ##############################
    # spaces of all states
    Cell_0.space = [Bord_('0'), Bord_('1'), Bord_('2'), Bord_('3')]
    Vol_0.space = [Bord_('0'), Bord_('1'), Bord_('2'), Bord_('3'), Bord_('4'), Bord_('5')]
    ##############################
    # grid of all states
    Cell_0.addGrid(Bord)
    Vol_0.addGrid(Bord)
    ##############################
    # prim of all states
    
    Vol_0.prim.elems = [
    Figure(2, [
        Bord_('0') + Bord('0') + Bord('0'),
        Bord_('0') + Bord('1') + Bord('0'),
        Bord_('0') + Bord('2') + Bord('0'),
        Bord_('0') + Bord('3') + Bord('0')]),
    Figure(2, [
        Bord_('1') + Bord('0') + Bord('0'),
        Bord_('1') + Bord('1') + Bord('0'),
        Bord_('1') + Bord('2') + Bord('0'),
        Bord_('1') + Bord('3') + Bord('0')]),
    Figure(2, [
        Bord_('2') + Bord('0') + Bord('0'),
        Bord_('2') + Bord('1') + Bord('0'),
        Bord_('2') + Bord('2') + Bord('0'),
        Bord_('2') + Bord('3') + Bord('0')]),
    Figure(2, [
        Bord_('3') + Bord('0') + Bord('0'),
        Bord_('3') + Bord('1') + Bord('0'),
        Bord_('3') + Bord('2') + Bord('0'),
        Bord_('3') + Bord('3') + Bord('0')]),
    Figure(2, [
        Bord_('4') + Bord('0') + Bord('0'),
        Bord_('4') + Bord('1') + Bord('0'),
        Bord_('4') + Bord('2') + Bord('0'),
        Bord_('4') + Bord('3') + Bord('0')]),
    Figure(2, [
        Bord_('5') + Bord('0') + Bord('0'),
        Bord_('5') + Bord('1') + Bord('0'),
        Bord_('5') + Bord('2') + Bord('0'),
        Bord_('5') + Bord('3') + Bord('0')]),
    ]
    ##############################
    # constraints of all states
    # incidence constraints
    Cell_0(Bord('0') + Sub('0'), Sub('0') + Bord('0'))
    Cell_0(Bord('0') + Sub('1'), Sub('1') + Bord('0'))
    Cell_0(Bord('1') + Sub('0'), Sub('2') + Bord('0'))
    Cell_0(Bord('1') + Sub('1'), Sub('3') + Bord('0'))
    Cell_0(Bord('2') + Sub('0'), Sub('4') + Bord('0'))
    Cell_0(Bord('2') + Sub('1'), Sub('5') + Bord('0'))
    Cell_0(Bord('3') + Sub('0'), Sub('6') + Bord('0'))
    Cell_0(Bord('3') + Sub('1'), Sub('7') + Bord('0'))
    # vol incidence constraints
    for j in range(6):
        for i in range(8):
            Vol_0(Bord(str(j)) + Sub(str(i)), Sub(str(i+j*8)) + Bord('0'))
    
    # adjacency constraints
    Cell_0(Sub('0') + Bord('1') + Permut('0'), Sub('1') + Bord('3'))
    Cell_0(Sub('1') + Bord('1') + Permut('0'), Sub('2') + Bord('3'))
    Cell_0(Sub('2') + Bord('1') + Permut('0'), Sub('3') + Bord('3'))
    Cell_0(Sub('3') + Bord('1') + Permut('0'), Sub('4') + Bord('3'))
    Cell_0(Sub('4') + Bord('1') + Permut('0'), Sub('5') + Bord('3'))
    Cell_0(Sub('5') + Bord('1') + Permut('0'), Sub('6') + Bord('3'))
    Cell_0(Sub('6') + Bord('1') + Permut('0'), Sub('7') + Bord('3'))
    Cell_0(Sub('7') + Bord('1') + Permut('0'), Sub('0') + Bord('3'))
    # edges adjacency constraints
    Cell_0(Bord('0') + Bord('1'), Bord('1') + Bord('0'))
    Cell_0(Bord('1') + Bord('1'), Bord('2') + Bord('0'))
    Cell_0(Bord('2') + Bord('1'), Bord('3') + Bord('0'))
    Cell_0(Bord('3') + Bord('1'), Bord('0') + Bord('0'))
    # faces adjacency constraints
    Vol_0(Bord('0') + Bord('0') + Permut('0'), Bord('1') + Bord('0'))
    Vol_0(Bord('0') + Bord('1') + Permut('0'), Bord('2') + Bord('0'))
    Vol_0(Bord('0') + Bord('2') + Permut('0'), Bord('3') + Bord('0'))
    Vol_0(Bord('0') + Bord('3') + Permut('0'), Bord('4') + Bord('0'))
    Vol_0(Bord('1') + Bord('1') + Permut('0'), Bord('4') + Bord('3'))
    Vol_0(Bord('1') + Bord('2') + Permut('0'), Bord('5') + Bord('0'))
    Vol_0(Bord('1') + Bord('3') + Permut('0'), Bord('2') + Bord('1'))
    Vol_0(Bord('2') + Bord('2') + Permut('0'), Bord('5') + Bord('3'))
    Vol_0(Bord('2') + Bord('3') + Permut('0'), Bord('3') + Bord('1'))
    Vol_0(Bord('3') + Bord('2') + Permut('0'), Bord('5') + Bord('2'))
    Vol_0(Bord('3') + Bord('3') + Permut('0'), Bord('4') + Bord('1'))
    Vol_0(Bord('4') + Bord('2') + Permut('0'), Bord('5') + Bord('1'))
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
