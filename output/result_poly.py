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
    ##############################
    # all cells states
    # Cell_0 -- B4 associated HE vertex : 5 -- B4 associated HE vertex : 1 -- B4 associated HE vertex : 9
    Cell_0 = Etat('Cell_0', 0)
    ##############################
    # subd of init
    init.subs = {Sub('0'): Cell_0, Sub('1'): Cell_0, Sub('2'): Cell_0, Sub('3'): Cell_0, Sub('4'): Cell_0, Sub('5'): Cell_0, Sub('6'): Cell_0, Sub('7'): Cell_0, Sub('8'): Cell_0, Sub('9'): Cell_0, Sub('10'): Cell_0, Sub('11'): Cell_0, Sub('12'): Cell_0, Sub('13'): Cell_0, Sub('14'): Cell_0, Sub('15'): Cell_0, Sub('16'): Cell_0, Sub('17'): Cell_0, Sub('18'): Cell_0, Sub('19'): Cell_0}
    ##############################
    # edges of all states
    Cell_0.bords = {Bord('0'): B4, Bord('1'): B4, Bord('2'): B4}
    ##############################
    # subdivisions of all states
    Cell_0.subs = {Sub('0'): Cell_0, Sub('1'): Cell_0, Sub('2'): Cell_0, Sub('3'): Cell_0, Sub('4'): Cell_0, Sub('5'): Cell_0, Sub('6'): Cell_0, Sub('7'): Cell_0, Sub('8'): Cell_0, Sub('9'): Cell_0, Sub('10'): Cell_0, Sub('11'): Cell_0, Sub('12'): Cell_0, Sub('13'): Cell_0, Sub('14'): Cell_0, Sub('15'): Cell_0, Sub('16'): Cell_0, Sub('17'): Cell_0, Sub('18'): Cell_0}
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
    Cell_0.prim.elems = [Figure(2, [Bord_('0') + Sub('0') + Sub('0') + Bord('0'), Bord_('0') + Sub('0') + Sub('1') + Bord('0'), Bord_('0') + Sub('1') + Sub('0') + Bord('0'), Bord_('0') + Sub('1') + Sub('1') + Bord('0'), Bord_('1') + Sub('0') + Sub('0') + Bord('0'), Bord_('1') + Sub('0') + Sub('1') + Bord('0'), Bord_('1') + Sub('1') + Sub('0') + Bord('0'), Bord_('1') + Sub('1') + Sub('1') + Bord('0'), Bord_('2') + Sub('0') + Sub('0') + Bord('0'), Bord_('2') + Sub('0') + Sub('1') + Bord('0'), Bord_('2') + Sub('1') + Sub('0') + Bord('0'), Bord_('2') + Sub('1') + Sub('1') + Bord('0')])]
    ##############################
    # constraints of all states
    # incidence constraints
    Cell_0(Bord('1') + Sub('2') + Permut('0'), Sub('0') + Bord('1'))
    Cell_0(Bord('0') + Sub('2') + Permut('0'), Sub('1') + Bord('2'))
    Cell_0(Bord('2') + Sub('2') + Permut('0'), Sub('3') + Bord('0'))
    Cell_0(Bord('2') + Sub('0') + Permut('0'), Sub('7') + Bord('0'))
    Cell_0(Bord('1') + Sub('3') + Permut('0'), Sub('7') + Bord('1'))
    Cell_0(Bord('2') + Sub('1') + Permut('0'), Sub('8') + Bord('2'))
    Cell_0(Bord('1') + Sub('0') + Permut('0'), Sub('11') + Bord('0'))
    Cell_0(Bord('0') + Sub('3') + Permut('0'), Sub('11') + Bord('1'))
    Cell_0(Bord('1') + Sub('1') + Permut('0'), Sub('12') + Bord('2'))
    Cell_0(Bord('0') + Sub('0') + Permut('0'), Sub('15') + Bord('0'))
    Cell_0(Bord('2') + Sub('3') + Permut('0'), Sub('15') + Bord('1'))
    Cell_0(Bord('0') + Sub('1') + Permut('0'), Sub('16') + Bord('2'))
    # adjacency constraints
    Cell_0(Sub('0') + Bord('0') + Bord('1'), Sub('7') + Bord('1') + Bord('1'))
    Cell_0(Sub('0') + Bord('1') + Bord('1'), Sub('12') + Bord('1') + Bord('1'))
    Cell_0(Sub('0') + Bord('2') + Bord('1'), Sub('17') + Bord('1') + Bord('1'))
    Cell_0(Sub('1') + Bord('0') + Bord('1'), Sub('9') + Bord('1') + Bord('1'))
    Cell_0(Sub('1') + Bord('1') + Bord('1'), Sub('11') + Bord('1') + Bord('1'))
    Cell_0(Sub('1') + Bord('2') + Bord('1'), Sub('16') + Bord('1') + Bord('1'))
    Cell_0(Sub('2') + Bord('0') + Bord('1'), Sub('12') + Bord('0') + Bord('1'))
    Cell_0(Sub('2') + Bord('1') + Bord('1'), Sub('9') + Bord('0') + Bord('1'))
    Cell_0(Sub('2') + Bord('2') + Bord('1'), Sub('18') + Bord('0') + Bord('1'))
    Cell_0(Sub('3') + Bord('0') + Bord('1'), Sub('8') + Bord('1') + Bord('1'))
    Cell_0(Sub('3') + Bord('1') + Bord('1'), Sub('13') + Bord('1') + Bord('1'))
    Cell_0(Sub('3') + Bord('2') + Bord('1'), Sub('15') + Bord('1') + Bord('1'))
    Cell_0(Sub('4') + Bord('0') + Bord('1'), Sub('14') + Bord('0') + Bord('1'))
    Cell_0(Sub('4') + Bord('1') + Bord('1'), Sub('8') + Bord('0') + Bord('1'))
    Cell_0(Sub('4') + Bord('2') + Bord('1'), Sub('17') + Bord('0') + Bord('1'))
    Cell_0(Sub('5') + Bord('0') + Bord('1'), Sub('13') + Bord('0') + Bord('1'))
    Cell_0(Sub('5') + Bord('1') + Bord('1'), Sub('10') + Bord('0') + Bord('1'))
    Cell_0(Sub('5') + Bord('2') + Bord('1'), Sub('16') + Bord('0') + Bord('1'))
    Cell_0(Sub('6') + Bord('0') + Bord('1'), Sub('10') + Bord('1') + Bord('1'))
    Cell_0(Sub('6') + Bord('1') + Bord('1'), Sub('14') + Bord('1') + Bord('1'))
    Cell_0(Sub('6') + Bord('2') + Bord('1'), Sub('18') + Bord('1') + Bord('1'))
    Cell_0(Sub('7') + Bord('2') + Bord('1'), Sub('8') + Bord('2') + Bord('1'))
    Cell_0(Sub('9') + Bord('2') + Bord('1'), Sub('10') + Bord('2') + Bord('1'))
    Cell_0(Sub('11') + Bord('2') + Bord('1'), Sub('12') + Bord('2') + Bord('1'))
    Cell_0(Sub('13') + Bord('2') + Bord('1'), Sub('14') + Bord('2') + Bord('1'))
    Cell_0(Sub('15') + Bord('2') + Bord('1'), Sub('16') + Bord('2') + Bord('1'))
    Cell_0(Sub('17') + Bord('2') + Bord('1'), Sub('18') + Bord('2') + Bord('1'))
    # edges adjacency constraints
    Cell_0(Bord('0') + Bord('1'), Bord('1') + Bord('0'))
    Cell_0(Bord('1') + Bord('1'), Bord('2') + Bord('0'))
    Cell_0(Bord('2') + Bord('1'), Bord('0') + Bord('0'))
    # constraints on init cells
    init(Sub('0') + Bord('0') + Bord('1'), Sub('12') + Bord('0') + Bord('1'))
    init(Sub('0') + Bord('1') + Bord('1'), Sub('8') + Bord('0') + Bord('1'))
    init(Sub('0') + Bord('2') + Bord('1'), Sub('16') + Bord('0') + Bord('1'))
    init(Sub('1') + Bord('0') + Bord('1'), Sub('8') + Bord('1') + Bord('1'))
    init(Sub('1') + Bord('1') + Bord('1'), Sub('13') + Bord('1') + Bord('1'))
    init(Sub('1') + Bord('2') + Bord('1'), Sub('18') + Bord('1') + Bord('1'))
    init(Sub('2') + Bord('0') + Bord('1'), Sub('10') + Bord('1') + Bord('1'))
    init(Sub('2') + Bord('1') + Bord('1'), Sub('12') + Bord('1') + Bord('1'))
    init(Sub('2') + Bord('2') + Bord('1'), Sub('17') + Bord('1') + Bord('1'))
    init(Sub('3') + Bord('0') + Bord('1'), Sub('13') + Bord('0') + Bord('1'))
    init(Sub('3') + Bord('1') + Bord('1'), Sub('10') + Bord('0') + Bord('1'))
    init(Sub('3') + Bord('2') + Bord('1'), Sub('19') + Bord('0') + Bord('1'))
    init(Sub('4') + Bord('0') + Bord('1'), Sub('9') + Bord('1') + Bord('1'))
    init(Sub('4') + Bord('1') + Bord('1'), Sub('14') + Bord('1') + Bord('1'))
    init(Sub('4') + Bord('2') + Bord('1'), Sub('16') + Bord('1') + Bord('1'))
    init(Sub('5') + Bord('0') + Bord('1'), Sub('15') + Bord('0') + Bord('1'))
    init(Sub('5') + Bord('1') + Bord('1'), Sub('9') + Bord('0') + Bord('1'))
    init(Sub('5') + Bord('2') + Bord('1'), Sub('18') + Bord('0') + Bord('1'))
    init(Sub('6') + Bord('0') + Bord('1'), Sub('14') + Bord('0') + Bord('1'))
    init(Sub('6') + Bord('1') + Bord('1'), Sub('11') + Bord('0') + Bord('1'))
    init(Sub('6') + Bord('2') + Bord('1'), Sub('17') + Bord('0') + Bord('1'))
    init(Sub('7') + Bord('0') + Bord('1'), Sub('11') + Bord('1') + Bord('1'))
    init(Sub('7') + Bord('1') + Bord('1'), Sub('15') + Bord('1') + Bord('1'))
    init(Sub('7') + Bord('2') + Bord('1'), Sub('19') + Bord('1') + Bord('1'))
    init(Sub('8') + Bord('2') + Bord('1'), Sub('9') + Bord('2') + Bord('1'))
    init(Sub('10') + Bord('2') + Bord('1'), Sub('11') + Bord('2') + Bord('1'))
    init(Sub('12') + Bord('2') + Bord('1'), Sub('13') + Bord('2') + Bord('1'))
    init(Sub('14') + Bord('2') + Bord('1'), Sub('15') + Bord('2') + Bord('1'))
    init(Sub('16') + Bord('2') + Bord('1'), Sub('17') + Bord('2') + Bord('1'))
    init(Sub('18') + Bord('2') + Bord('1'), Sub('19') + Bord('2') + Bord('1'))
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
