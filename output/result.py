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
    C2_1 = Etat('C2_1', 0)
    C2_1.bords = {Bord('0'): s, Bord('1'): s}
    C2_1.permuts = {Permut('0'): C2_1}
    B2_1 = Etat('B2_1', 1)
    B2_1.bords = {Bord('0'): s, Bord('1'): s}
    B2_1.permuts = {Permut('0'): B2_1}
    B2 = Etat('B2', 1)
    B2.bords = {Bord('0'): s, Bord('1'): s}
    B2.permuts = {Permut('0'): B2}
    C2 = Etat('C2', 0)
    C2.bords = {Bord('0'): s, Bord('1'): s}
    C2.permuts = {Permut('0'): C2}
    ##############################
    # all edges impl
    C2_1.subs = {Sub('0'): C2}
    C2_1.buildIntern()
    C2_1.space = [Bord_('0'), Bord_('1')]
    C2_1(Permut('0') + Bord('0'), Bord('1'))
    C2_1(Permut('0') + Bord('1'), Bord('0'))
    C2_1(Permut('0') + Sub('0'), Sub('0') + Permut('0'))
    C2_1(Bord('0') + Sub('0'), Sub('0') + Bord('0'))
    C2_1(Bord('1') + Sub('0'), Sub('0') + Bord('1'))
    C2_1.grid.elems = [Figure(1, [Bord_('0'), Bord_('1')])]
    C2_1.prim.elems = [Figure(1, [Bord_('0'), Bord_('1')])]
    B2_1.subs = {Sub('0'): B2}
    B2_1.buildIntern()
    B2_1.space = [Bord_('0'), Intern_(''), Bord_('1')]
    B2_1(Permut('0') + Bord('0'), Bord('1'))
    B2_1(Permut('0') + Bord('1'), Bord('0'))
    B2_1(Permut('0') + Intern(''), Intern(''))
    B2_1(Permut('0') + Sub('0'), Sub('0') + Permut('0'))
    B2_1(Bord('0') + Sub('0'), Sub('0') + Bord('0'))
    B2_1(Bord('1') + Sub('0'), Sub('0') + Bord('1'))
    B2_1.grid.elems = [Figure(1, [Bord_('0'), Intern_(''), Bord_('1')])]
    B2_1.prim.elems = [Figure(1, [Bord_('0'), Bord_('1')])]
    B2_1.initMat[Sub_('0') + Intern('')] = FMat([
        [0.0],
        [1.0],
        [0.0]]).setTyp('Const')
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
    C2.subs = {Sub('0'): C2, Sub('1'): C2}
    C2.buildIntern()
    C2.space = [Bord_('0'), Bord_('1')]
    C2(Permut('0') + Bord('0'), Bord('1'))
    C2(Permut('0') + Bord('1'), Bord('0'))
    C2(Permut('0') + Sub('0'), Sub('1') + Permut('0'))
    C2(Permut('0') + Sub('1'), Sub('0') + Permut('0'))
    C2(Bord('0') + Sub('0'), Sub('0') + Bord('0'))
    C2(Bord('1') + Sub('0'), Sub(1) + Bord('1'))
    C2.grid.elems = [Figure(1, [Bord_('0'), Bord_('1')])]
    C2.initMat[Sub_('0') + Bord('1')] = FMat([
        [0.666667],
        [0.333333]]).setTyp('Const')
    C2.initMat[Sub_('1') + Bord('0')] = FMat([
        [0.333333],
        [0.666667]]).setTyp('Const')
    ##############################
    # all cells states
    # C_2_1 - B_2_1 - C_2_1 - B_2_1 - C_2_1 - B_2_1 / C_2_0 - B_2_0 - B_2_0 / 1 / 1
    Cell_0_1 = Etat('Cell_0_1', 0)
    # C_2_1 - B_2_0 - C_2_1 - B_2_0 - C_2_1 - B_2_0 - C_2_0 - B_2_0 / C_2_0 - B_2_0 - B_2_0 / 0 / 1
    Cell_1 = Etat('Cell_1', 0)
    # C_2_0 - B_2_0 - C_2_0 - B_2_0 - C_2_0 - B_2_0 / C_2_0 - B_2_0 - B_2_0 / 0 / 1
    Cell_2 = Etat('Cell_2', 0)
    ##############################
    # subd of init
    init.subs = {Sub('0'): Cell_0_1, Sub('1'): Cell_1, Sub('2'): Cell_2}
    ##############################
    # edges of all states
    Cell_0_1.bords = {Bord('0'): C2_1, Bord('1'): B2_1, Bord('2'): C2_1, Bord('3'): B2_1, Bord('4'): C2_1, Bord('5'): B2_1}
    Cell_1.bords = {Bord('0'): C2_1, Bord('1'): B2, Bord('2'): C2_1, Bord('3'): B2, Bord('4'): C2_1, Bord('5'): B2, Bord('6'): C2, Bord('7'): B2}
    Cell_2.bords = {Bord('0'): C2, Bord('1'): B2, Bord('2'): C2, Bord('3'): B2, Bord('4'): C2, Bord('5'): B2}
    ##############################
    # subdivisions of all states
    Cell_0_1.subs = {Sub('0'): Cell_2}
    Cell_1.subs = {Sub('0'): Cell_2, Sub('1'): Cell_2, Sub('2'): Cell_2, Sub('3'): Cell_2, Sub('4'): Cell_2}
    Cell_2.subs = {Sub('0'): Cell_2, Sub('1'): Cell_2, Sub('2'): Cell_2, Sub('3'): Cell_2, Sub('4'): Cell_2, Sub('5'): Cell_2}
    ##############################
    # build intern of all states
    Cell_0_1.buildIntern()
    Cell_1.buildIntern()
    Cell_2.buildIntern()
    ##############################
    # spaces of all states
    Cell_0_1.space = [Bord_('0'), Bord_('1'), Bord_('2'), Bord_('3'), Bord_('4'), Bord_('5')]
    Cell_1.space = [Bord_('0'), Bord_('1'), Bord_('2'), Bord_('3'), Bord_('4'), Bord_('5'), Bord_('6'), Bord_('7')]
    Cell_2.space = [Bord_('0'), Bord_('1'), Bord_('2'), Bord_('3'), Bord_('4'), Bord_('5')]
    ##############################
    # grid of all states
    Cell_0_1.addGrid(Bord)
    Cell_1.addGrid(Bord)
    Cell_2.addGrid(Bord)
    ##############################
    # prim of all states
    Cell_0_1.prim.elems = [Figure(2, [
        Bord_('0') + Bord('0'),
        Bord_('1') + Bord('0'),
        Bord_('2') + Bord('0'),
        Bord_('3') + Bord('0'),
        Bord_('4') + Bord('0'),
        Bord_('5') + Bord('0'),
    ])]
    Cell_1.prim.elems = [Figure(2, [
        Bord_('0') + Bord('0'),
        Bord_('1') + Sub('0') + Sub('0') + Bord('0'),
        Bord_('1') + Sub('0') + Sub('1') + Bord('0'),
        Bord_('1') + Sub('1') + Sub('0') + Bord('0'),
        Bord_('1') + Sub('1') + Sub('1') + Bord('0'),
        Bord_('2') + Bord('0'),
        Bord_('3') + Sub('0') + Sub('0') + Bord('0'),
        Bord_('3') + Sub('0') + Sub('1') + Bord('0'),
        Bord_('3') + Sub('1') + Sub('0') + Bord('0'),
        Bord_('3') + Sub('1') + Sub('1') + Bord('0'),
        Bord_('4') + Bord('0'),
        Bord_('5') + Sub('0') + Sub('0') + Bord('0'),
        Bord_('5') + Sub('0') + Sub('1') + Bord('0'),
        Bord_('5') + Sub('1') + Sub('0') + Bord('0'),
        Bord_('5') + Sub('1') + Sub('1') + Bord('0'),
        Bord_('6') + Bord('0'),
        Bord_('7') + Sub('0') + Sub('0') + Bord('0'),
        Bord_('7') + Sub('0') + Sub('1') + Bord('0'),
        Bord_('7') + Sub('1') + Sub('0') + Bord('0'),
        Bord_('7') + Sub('1') + Sub('1') + Bord('0'),
    ])]
    Cell_2.prim.elems = [Figure(2, [
        Bord_('0') + Bord('0'),
        Bord_('1') + Sub('0') + Sub('0') + Bord('0'),
        Bord_('1') + Sub('0') + Sub('1') + Bord('0'),
        Bord_('1') + Sub('1') + Sub('0') + Bord('0'),
        Bord_('1') + Sub('1') + Sub('1') + Bord('0'),
        Bord_('2') + Bord('0'),
        Bord_('3') + Sub('0') + Sub('0') + Bord('0'),
        Bord_('3') + Sub('0') + Sub('1') + Bord('0'),
        Bord_('3') + Sub('1') + Sub('0') + Bord('0'),
        Bord_('3') + Sub('1') + Sub('1') + Bord('0'),
        Bord_('4') + Bord('0'),
        Bord_('5') + Sub('0') + Sub('0') + Bord('0'),
        Bord_('5') + Sub('0') + Sub('1') + Bord('0'),
        Bord_('5') + Sub('1') + Sub('0') + Bord('0'),
        Bord_('5') + Sub('1') + Sub('1') + Bord('0'),
    ])]
    ##############################
    # constraints of all states
    # incidence constraints
    Cell_0_1(Bord('0') + Sub('0'), Sub('0') + Bord('0'))
    Cell_0_1(Bord('1') + Sub('0'), Sub('0') + Bord('1'))
    Cell_0_1(Bord('2') + Sub('0'), Sub('0') + Bord('2'))
    Cell_0_1(Bord('3') + Sub('0'), Sub('0') + Bord('3'))
    Cell_0_1(Bord('4') + Sub('0'), Sub('0') + Bord('4'))
    Cell_0_1(Bord('5') + Sub('0'), Sub('0') + Bord('5'))
    # adjacency constraints
    # edges adjacency constraints
    Cell_0_1(Bord('0') + Bord('1'), Bord('1') + Bord('0'))
    Cell_0_1(Bord('1') + Bord('1'), Bord('2') + Bord('0'))
    Cell_0_1(Bord('2') + Bord('1'), Bord('3') + Bord('0'))
    Cell_0_1(Bord('3') + Bord('1'), Bord('4') + Bord('0'))
    Cell_0_1(Bord('4') + Bord('1'), Bord('5') + Bord('0'))
    Cell_0_1(Bord('5') + Bord('1'), Bord('0') + Bord('0'))
    # incidence constraints
    Cell_1(Bord('7') + Sub('1'), Sub('0') + Bord('5'))
    Cell_1(Bord('0') + Sub('0'), Sub('0') + Bord('0'))
    Cell_1(Bord('1') + Sub('0'), Sub('0') + Bord('1'))
    Cell_1(Bord('1') + Sub('1'), Sub('1') + Bord('5'))
    Cell_1(Bord('2') + Sub('0'), Sub('1') + Bord('0'))
    Cell_1(Bord('3') + Sub('0'), Sub('1') + Bord('1'))
    Cell_1(Bord('3') + Sub('1'), Sub('2') + Bord('5'))
    Cell_1(Bord('4') + Sub('0'), Sub('2') + Bord('0'))
    Cell_1(Bord('5') + Sub('0'), Sub('2') + Bord('1'))
    Cell_1(Bord('5') + Sub('1'), Sub('3') + Bord('5'))
    Cell_1(Bord('6') + Sub('0'), Sub('3') + Bord('0'))
    Cell_1(Bord('6') + Sub('1'), Sub('4') + Bord('0'))
    Cell_1(Bord('7') + Sub('0'), Sub('4') + Bord('1'))
    # adjacency constraints
    Cell_1(Sub('0') + Bord('2') + Permut('0'), Sub('1') + Bord('4'))
    Cell_1(Sub('1') + Bord('2') + Permut('0'), Sub('2') + Bord('4'))
    Cell_1(Sub('2') + Bord('2') + Permut('0'), Sub('3') + Bord('4'))
    Cell_1(Sub('3') + Bord('2') + Permut('0'), Sub('4') + Bord('4'))
    Cell_1(Sub('4') + Bord('2') + Permut('0'), Sub('0') + Bord('4'))
    # edges adjacency constraints
    Cell_1(Bord('0') + Bord('1'), Bord('1') + Bord('0'))
    Cell_1(Bord('1') + Bord('1'), Bord('2') + Bord('0'))
    Cell_1(Bord('2') + Bord('1'), Bord('3') + Bord('0'))
    Cell_1(Bord('3') + Bord('1'), Bord('4') + Bord('0'))
    Cell_1(Bord('4') + Bord('1'), Bord('5') + Bord('0'))
    Cell_1(Bord('5') + Bord('1'), Bord('6') + Bord('0'))
    Cell_1(Bord('6') + Bord('1'), Bord('7') + Bord('0'))
    Cell_1(Bord('7') + Bord('1'), Bord('0') + Bord('0'))
    # incidence constraints
    Cell_2(Bord('0') + Sub('1'), Sub('0') + Bord('0'))
    Cell_2(Bord('1') + Sub('0'), Sub('0') + Bord('1'))
    Cell_2(Bord('1') + Sub('1'), Sub('1') + Bord('5'))
    Cell_2(Bord('2') + Sub('0'), Sub('1') + Bord('0'))
    Cell_2(Bord('2') + Sub('1'), Sub('2') + Bord('0'))
    Cell_2(Bord('3') + Sub('0'), Sub('2') + Bord('1'))
    Cell_2(Bord('3') + Sub('1'), Sub('3') + Bord('5'))
    Cell_2(Bord('4') + Sub('0'), Sub('3') + Bord('0'))
    Cell_2(Bord('4') + Sub('1'), Sub('4') + Bord('0'))
    Cell_2(Bord('5') + Sub('0'), Sub('4') + Bord('1'))
    Cell_2(Bord('5') + Sub('1'), Sub('5') + Bord('5'))
    Cell_2(Bord('0') + Sub('0'), Sub('5') + Bord('0'))
    # adjacency constraints
    Cell_2(Sub('0') + Bord('2') + Permut('0'), Sub('1') + Bord('4'))
    Cell_2(Sub('1') + Bord('2') + Permut('0'), Sub('2') + Bord('4'))
    Cell_2(Sub('2') + Bord('2') + Permut('0'), Sub('3') + Bord('4'))
    Cell_2(Sub('3') + Bord('2') + Permut('0'), Sub('4') + Bord('4'))
    Cell_2(Sub('4') + Bord('2') + Permut('0'), Sub('5') + Bord('4'))
    Cell_2(Sub('5') + Bord('2') + Permut('0'), Sub('0') + Bord('4'))
    # edges adjacency constraints
    Cell_2(Bord('0') + Bord('1'), Bord('1') + Bord('0'))
    Cell_2(Bord('1') + Bord('1'), Bord('2') + Bord('0'))
    Cell_2(Bord('2') + Bord('1'), Bord('3') + Bord('0'))
    Cell_2(Bord('3') + Bord('1'), Bord('4') + Bord('0'))
    Cell_2(Bord('4') + Bord('1'), Bord('5') + Bord('0'))
    Cell_2(Bord('5') + Bord('1'), Bord('0') + Bord('0'))
    # constraints on init cells
    # control points
    init.initMat[Sub_('0')] = FMat([
        [1.000000, 0.766044, 0.090000, -0.500000, -0.939693, -0.450000, -0.500000, 0.173648, 0.330000],
        [0.000000, 0.642788, 0.450000, 0.866025, 0.342020, -0.150000, -0.866025, -0.984808, -0.280000],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1]]).setTyp('Var')
    for i in range(init.initMat[Sub_('0')].n):
        init.initMat[Sub_('0')][2, i].setTyp('Const')

    init.initMat[Sub_('1')] = FMat([
        [3.200000, 3.066025, 2.510000, 2.200000, 1.700000, 1.600000, 1.200000, 1.333975, 1.880000, 2.200000, 2.699999, 2.760000],
        [0.000000, 0.500000, 0.500000, 1.000000, 0.866026, 0.340000, -0.000000, -0.500000, -0.650000, -1.000000, -0.866026, -0.340000],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]).setTyp('Var')
    for i in range(init.initMat[Sub_('1')].n):
        init.initMat[Sub_('1')][2, i].setTyp('Const')

    init.initMat[Sub_('2')] = FMat([
        [5.400000, 5.166044, 4.490000, 3.900000, 3.460307, 3.920000, 3.900000, 4.573648, 4.710000],
        [0.000000, 0.642788, 0.430000, 0.866025, 0.342020, -0.180000, -0.866025, -0.984808, -0.300000],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1]]).setTyp('Var')
    for i in range(init.initMat[Sub_('2')].n):
        init.initMat[Sub_('2')][2, i].setTyp('Const')

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
