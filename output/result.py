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
    C2 = Etat('C2', 0)
    C2.bords = {Bord('0'): s, Bord('1'): s}
    C2.permuts = {Permut('0'): C2}
    ##############################
    # all edges impl
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
    # C_2_0 - C_2_0 - C_2_0 - C_2_0 - C_2_0 / C_2_0 - C_2_0 - C_2_0 / 0 / 2
    Cell_0 = Etat('Cell_0', 0)
    ##############################
    # subd of init
    init.subs = {Sub('0'): Cell_0}
    ##############################
    # edges of all states
    Cell_0.bords = {Bord('0'): C2, Bord('1'): C2, Bord('2'): C2, Bord('3'): C2, Bord('4'): C2}
    ##############################
    # subdivisions of all states
    Cell_0.subs = {Sub('0'): Cell_0, Sub('1'): Cell_0, Sub('2'): Cell_0, Sub('3'): Cell_0, Sub('4'): Cell_0, Sub('5'): Cell_0, Sub('6'): Cell_0, Sub('7'): Cell_0, Sub('8'): Cell_0, Sub('9'): Cell_0}
    ##############################
    # build intern of all states
    Cell_0.buildIntern()
    ##############################
    # spaces of all states
    Cell_0.space = [Bord_('0'), Bord_('1'), Bord_('2'), Bord_('3'), Bord_('4')]
    ##############################
    # grid of all states
    Cell_0.addGrid(Bord)
    ##############################
    # prim of all states
    Cell_0.prim.elems = [Figure(2, [
        Bord_('0') + Bord('0'),
        Bord_('1') + Bord('0'),
        Bord_('2') + Bord('0'),
        Bord_('3') + Bord('0'),
        Bord_('4') + Bord('0'),
    ])]
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
    Cell_0(Bord('4') + Sub('0'), Sub('8') + Bord('0'))
    Cell_0(Bord('4') + Sub('1'), Sub('9') + Bord('0'))
    # adjacency constraints
    Cell_0(Sub('0') + Bord('2') + Permut('0'), Sub('1') + Bord('3'))
    Cell_0(Sub('1') + Bord('1') + Permut('0'), Sub('2') + Bord('4'))
    Cell_0(Sub('2') + Bord('2') + Permut('0'), Sub('3') + Bord('3'))
    Cell_0(Sub('3') + Bord('1') + Permut('0'), Sub('4') + Bord('4'))
    Cell_0(Sub('4') + Bord('2') + Permut('0'), Sub('5') + Bord('3'))
    Cell_0(Sub('5') + Bord('1') + Permut('0'), Sub('6') + Bord('4'))
    Cell_0(Sub('6') + Bord('2') + Permut('0'), Sub('7') + Bord('3'))
    Cell_0(Sub('7') + Bord('1') + Permut('0'), Sub('8') + Bord('4'))
    Cell_0(Sub('8') + Bord('2') + Permut('0'), Sub('9') + Bord('3'))
    Cell_0(Sub('9') + Bord('1') + Permut('0'), Sub('0') + Bord('4'))
    # edges adjacency constraints
    Cell_0(Bord('0') + Bord('1'), Bord('1') + Bord('0'))
    Cell_0(Bord('1') + Bord('1'), Bord('2') + Bord('0'))
    Cell_0(Bord('2') + Bord('1'), Bord('3') + Bord('0'))
    Cell_0(Bord('3') + Bord('1'), Bord('4') + Bord('0'))
    Cell_0(Bord('4') + Bord('1'), Bord('0') + Bord('0'))
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
