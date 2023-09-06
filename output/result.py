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
    B2 = Etat('B2', 1)
    B2.bords = {Bord('0'): s, Bord('1'): s}
    B2.permuts = {Permut('0'): B2}
    B2_2 = Etat('B2_2', 1)
    B2_2.bords = {Bord('0'): s, Bord('1'): s}
    B2_2.permuts = {Permut('0'): B2_2}
    C2_1 = Etat('C2_1', 0)
    C2_1.bords = {Bord('0'): s, Bord('1'): s}
    C2_1.permuts = {Permut('0'): C2_1}
    B3 = Etat('B3', 1)
    B3.bords = {Bord('0'): s, Bord('1'): s}
    B3.permuts = {Permut('0'): B3}
    C3_1 = Etat('C3_1', 0)
    C3_1.bords = {Bord('0'): s, Bord('1'): s}
    C3_1.permuts = {Permut('0'): C3_1}
    B2_1 = Etat('B2_1', 1)
    B2_1.bords = {Bord('0'): s, Bord('1'): s}
    B2_1.permuts = {Permut('0'): B2_1}
    C3 = Etat('C3', 0)
    C3.bords = {Bord('0'): s, Bord('1'): s}
    C3.permuts = {Permut('0'): C3}
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
    B2_2.subs = {Sub('0'): B2_1}
    B2_2.buildIntern()
    B2_2.space = [Bord_('0'), Intern_(''), Bord_('1')]
    B2_2(Permut('0') + Bord('0'), Bord('1'))
    B2_2(Permut('0') + Bord('1'), Bord('0'))
    B2_2(Permut('0') + Intern(''), Intern(''))
    B2_2(Permut('0') + Sub('0'), Sub('0') + Permut('0'))
    B2_2(Bord('0') + Sub('0'), Sub('0') + Bord('0'))
    B2_2(Bord('1') + Sub('0'), Sub('0') + Bord('1'))
    B2_2.grid.elems = [Figure(1, [Bord_('0'), Intern_(''), Bord_('1')])]
    B2_2.prim.elems = [Figure(1, [Bord_('0'), Bord_('1')])]
    B2_2.initMat[Sub_('0') + Intern('')] = FMat([
        [0.0],
        [1.0],
        [0.0]]).setTyp('Const')
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
    C3_1.subs = {Sub('0'): C3}
    C3_1.buildIntern()
    C3_1.space = [Bord_('0'), Bord_('1')]
    C3_1(Permut('0') + Bord('0'), Bord('1'))
    C3_1(Permut('0') + Bord('1'), Bord('0'))
    C3_1(Permut('0') + Sub('0'), Sub('0') + Permut('0'))
    C3_1(Bord('0') + Sub('0'), Sub('0') + Bord('0'))
    C3_1(Bord('1') + Sub('0'), Sub('0') + Bord('1'))
    C3_1.grid.elems = [Figure(1, [Bord_('0'), Bord_('1')])]
    C3_1.prim.elems = [Figure(1, [Bord_('0'), Bord_('1')])]
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
    C3.subs = {Sub('0'): C3, Sub('1'): C3, Sub('2'): C3}
    C3.buildIntern()
    C3.space = [Bord_('0'), Bord_('1')]
    C3(Permut('0') + Bord('0'), Bord('1'))
    C3(Permut('0') + Bord('1'), Bord('0'))
    C3(Permut('0') + Sub('0'), Sub('2') + Permut('0'))
    C3(Permut('0') + Sub('1'), Sub('1') + Permut('0'))
    C3(Permut('0') + Sub('2'), Sub('0') + Permut('0'))
    C3(Bord('0') + Sub('0'), Sub('0') + Bord('0'))
    C3(Bord('1') + Sub('0'), Sub(2) + Bord('1'))
    C3.grid.elems = [Figure(1, [Bord_('0'), Bord_('1')])]
    C3.initMat[Sub_('0') + Bord('1')] = FMat([
        [0.800000],
        [0.200000]]).setTyp('Const')
    C3.initMat[Sub_('1')] = FMat([
        [0.600000, 0.400000],
        [0.400000, 0.600000]]).setTyp('Const')
    C3.initMat[Sub_('2') + Bord('0')] = FMat([
        [0.200000],
        [0.800000]]).setTyp('Const')
    ##############################
    # all cells states
    # C_2_0 - B_2_0 - B_2_0 - B_2_2 - C_2_1 - B_2_0 / B_3_0 - C_2_0 - C_3_1 / 0
    Cell_0 = Etat('Cell_0', 0)
    # C_2_0 - B_2_0 - B_3_0 - C_2_0 - B_3_0 - C_3_1 / B_3_0 - C_2_0 - C_3_1 / 0
    Cell_1 = Etat('Cell_1', 0)
    # B_2_0 - B_2_0 - B_3_0 - C_2_0 - B_3_0 / B_3_0 - C_2_0 - C_3_1 / 0
    Cell_2 = Etat('Cell_2', 0)
    # B_2_0 - B_2_1 - B_3_0 - C_2_0 - B_3_0 / B_3_0 - C_2_0 - C_3_1 / 0
    Cell_3 = Etat('Cell_3', 0)
    # C_2_0 - B_2_0 - B_3_0 - C_2_0 - B_3_0 / B_3_0 - C_2_0 - C_3_1 / 0
    Cell_4 = Etat('Cell_4', 0)
    # B_2_0 - C_2_0 - C_3_1 - B_3_0 - C_2_0 - B_3_0 / B_3_0 - C_2_0 - C_3_1 / 0
    Cell_5 = Etat('Cell_5', 0)
    # C_2_0 - C_3_1 - B_3_0 - C_2_0 - B_3_0 / B_3_0 - C_2_0 - C_3_1 / 0
    Cell_6 = Etat('Cell_6', 0)
    # B_2_0 - B_3_0 - B_3_0 - C_2_0 - B_3_0 / B_3_0 - C_2_0 - C_3_1 / 0
    Cell_7 = Etat('Cell_7', 0)
    # B_3_0 - B_3_0 - C_2_0 - B_3_0 / B_3_0 - C_2_0 - C_3_1 / 0
    Cell_8 = Etat('Cell_8', 0)
    # B_3_0 - C_2_0 - C_3_1 - B_3_0 - C_2_0 - B_3_0 / B_3_0 - C_2_0 - C_3_1 / 0
    Cell_9 = Etat('Cell_9', 0)
    # C_2_0 - B_3_0 - B_3_0 - C_2_0 - B_3_0 - C_3_1 / B_3_0 - C_2_0 - C_3_1 / 0
    Cell_10 = Etat('Cell_10', 0)
    # B_3_0 - C_3_0 - B_3_0 - C_2_0 - B_3_0 / B_3_0 - C_2_0 - C_3_1 / 0
    Cell_11 = Etat('Cell_11', 0)
    # B_3_0 - B_2_0 - B_3_0 - C_2_0 - B_3_0 / B_3_0 - C_2_0 - C_3_1 / 0
    Cell_12 = Etat('Cell_12', 0)
    # B_2_0 - B_2_0 - B_3_0 - B_3_0 - C_2_0 - B_3_0 / B_3_0 - C_2_0 - C_3_1 / 0
    Cell_13 = Etat('Cell_13', 0)
    # C_2_0 - B_3_0 - C_2_0 - B_3_0 - C_3_1 / B_3_0 - C_2_0 - C_3_1 / 0
    Cell_14 = Etat('Cell_14', 0)
    # C_3_0 - B_3_0 - B_3_0 - C_2_0 - B_3_0 / B_3_0 - C_2_0 - C_3_1 / 0
    Cell_15 = Etat('Cell_15', 0)
    # B_3_0 - B_3_0 - B_3_0 - C_2_0 - B_3_0 / B_3_0 - C_2_0 - C_3_1 / 0
    Cell_16 = Etat('Cell_16', 0)
    # B_3_0 - C_3_0 - C_3_1 - B_3_0 - C_2_0 - B_3_0 / B_3_0 - C_2_0 - C_3_1 / 0
    Cell_17 = Etat('Cell_17', 0)
    # C_3_0 - C_3_1 - B_3_0 - C_2_0 - B_3_0 - C_3_1 / B_3_0 - C_2_0 - C_3_1 / 0
    Cell_18 = Etat('Cell_18', 0)
    # C_3_0 - B_3_0 - B_3_0 - C_2_0 - B_3_0 - C_3_1 / B_3_0 - C_2_0 - C_3_1 / 0
    Cell_19 = Etat('Cell_19', 0)
    # C_3_0 - B_3_0 - C_2_0 - B_3_0 - C_3_1 / B_3_0 - C_2_0 - C_3_1 / 0
    Cell_20 = Etat('Cell_20', 0)
    # C_3_0 - C_3_1 - B_3_0 - C_2_0 - B_3_0 / B_3_0 - C_2_0 - C_3_1 / 0
    Cell_21 = Etat('Cell_21', 0)
    ##############################
    # subd of init
    init.subs = {Sub('0'): Cell_0}
    ##############################
    # edges of all states
    Cell_0.bords = {Bord('0'): C2, Bord('1'): B2, Bord('2'): B2, Bord('3'): B2_2, Bord('4'): C2_1, Bord('5'): B2}
    Cell_1.bords = {Bord('0'): C2, Bord('1'): B2, Bord('2'): B3, Bord('3'): C2, Bord('4'): B3, Bord('5'): C3_1}
    Cell_2.bords = {Bord('0'): B2, Bord('1'): B2, Bord('2'): B3, Bord('3'): C2, Bord('4'): B3}
    Cell_3.bords = {Bord('0'): B2, Bord('1'): B2_1, Bord('2'): B3, Bord('3'): C2, Bord('4'): B3}
    Cell_4.bords = {Bord('0'): C2, Bord('1'): B2, Bord('2'): B3, Bord('3'): C2, Bord('4'): B3}
    Cell_5.bords = {Bord('0'): B2, Bord('1'): C2, Bord('2'): C3_1, Bord('3'): B3, Bord('4'): C2, Bord('5'): B3}
    Cell_6.bords = {Bord('0'): C2, Bord('1'): C3_1, Bord('2'): B3, Bord('3'): C2, Bord('4'): B3}
    Cell_7.bords = {Bord('0'): B2, Bord('1'): B3, Bord('2'): B3, Bord('3'): C2, Bord('4'): B3}
    Cell_8.bords = {Bord('0'): B3, Bord('1'): B3, Bord('2'): C2, Bord('3'): B3}
    Cell_9.bords = {Bord('0'): B3, Bord('1'): C2, Bord('2'): C3_1, Bord('3'): B3, Bord('4'): C2, Bord('5'): B3}
    Cell_10.bords = {Bord('0'): C2, Bord('1'): B3, Bord('2'): B3, Bord('3'): C2, Bord('4'): B3, Bord('5'): C3_1}
    Cell_11.bords = {Bord('0'): B3, Bord('1'): C3, Bord('2'): B3, Bord('3'): C2, Bord('4'): B3}
    Cell_12.bords = {Bord('0'): B3, Bord('1'): B2, Bord('2'): B3, Bord('3'): C2, Bord('4'): B3}
    Cell_13.bords = {Bord('0'): B2, Bord('1'): B2, Bord('2'): B3, Bord('3'): B3, Bord('4'): C2, Bord('5'): B3}
    Cell_14.bords = {Bord('0'): C2, Bord('1'): B3, Bord('2'): C2, Bord('3'): B3, Bord('4'): C3_1}
    Cell_15.bords = {Bord('0'): C3, Bord('1'): B3, Bord('2'): B3, Bord('3'): C2, Bord('4'): B3}
    Cell_16.bords = {Bord('0'): B3, Bord('1'): B3, Bord('2'): B3, Bord('3'): C2, Bord('4'): B3}
    Cell_17.bords = {Bord('0'): B3, Bord('1'): C3, Bord('2'): C3_1, Bord('3'): B3, Bord('4'): C2, Bord('5'): B3}
    Cell_18.bords = {Bord('0'): C3, Bord('1'): C3_1, Bord('2'): B3, Bord('3'): C2, Bord('4'): B3, Bord('5'): C3_1}
    Cell_19.bords = {Bord('0'): C3, Bord('1'): B3, Bord('2'): B3, Bord('3'): C2, Bord('4'): B3, Bord('5'): C3_1}
    Cell_20.bords = {Bord('0'): C3, Bord('1'): B3, Bord('2'): C2, Bord('3'): B3, Bord('4'): C3_1}
    Cell_21.bords = {Bord('0'): C3, Bord('1'): C3_1, Bord('2'): B3, Bord('3'): C2, Bord('4'): B3}
    ##############################
    # subdivisions of all states
    Cell_0.subs = {Sub('0'): Cell_1, Sub('1'): Cell_2, Sub('2'): Cell_3, Sub('3'): Cell_4, Sub('4'): Cell_5}
    Cell_1.subs = {Sub('0'): Cell_6, Sub('1'): Cell_1, Sub('2'): Cell_7, Sub('3'): Cell_8, Sub('4'): Cell_9, Sub('5'): Cell_10, Sub('6'): Cell_8, Sub('7'): Cell_11}
    Cell_2.subs = {Sub('0'): Cell_2, Sub('1'): Cell_7, Sub('2'): Cell_8, Sub('3'): Cell_9, Sub('4'): Cell_10, Sub('5'): Cell_8, Sub('6'): Cell_12}
    Cell_3.subs = {Sub('0'): Cell_13, Sub('1'): Cell_8, Sub('2'): Cell_9, Sub('3'): Cell_10, Sub('4'): Cell_8, Sub('5'): Cell_12}
    Cell_4.subs = {Sub('0'): Cell_1, Sub('1'): Cell_7, Sub('2'): Cell_8, Sub('3'): Cell_9, Sub('4'): Cell_10, Sub('5'): Cell_8, Sub('6'): Cell_9}
    Cell_5.subs = {Sub('0'): Cell_5, Sub('1'): Cell_14, Sub('2'): Cell_15, Sub('3'): Cell_8, Sub('4'): Cell_9, Sub('5'): Cell_10, Sub('6'): Cell_8, Sub('7'): Cell_12}
    Cell_6.subs = {Sub('0'): Cell_14, Sub('1'): Cell_15, Sub('2'): Cell_8, Sub('3'): Cell_9, Sub('4'): Cell_10, Sub('5'): Cell_8, Sub('6'): Cell_9}
    Cell_7.subs = {Sub('0'): Cell_7, Sub('1'): Cell_8, Sub('2'): Cell_16, Sub('3'): Cell_8, Sub('4'): Cell_9, Sub('5'): Cell_10, Sub('6'): Cell_8, Sub('7'): Cell_12}
    Cell_8.subs = {Sub('0'): Cell_8, Sub('1'): Cell_16, Sub('2'): Cell_8, Sub('3'): Cell_9, Sub('4'): Cell_10, Sub('5'): Cell_8, Sub('6'): Cell_16}
    Cell_9.subs = {Sub('0'): Cell_8, Sub('1'): Cell_9, Sub('2'): Cell_14, Sub('3'): Cell_15, Sub('4'): Cell_8, Sub('5'): Cell_9, Sub('6'): Cell_10, Sub('7'): Cell_8, Sub('8'): Cell_16}
    Cell_10.subs = {Sub('0'): Cell_6, Sub('1'): Cell_10, Sub('2'): Cell_8, Sub('3'): Cell_16, Sub('4'): Cell_8, Sub('5'): Cell_9, Sub('6'): Cell_10, Sub('7'): Cell_8, Sub('8'): Cell_11}
    Cell_11.subs = {Sub('0'): Cell_8, Sub('1'): Cell_17, Sub('2'): Cell_18, Sub('3'): Cell_19, Sub('4'): Cell_8, Sub('5'): Cell_9, Sub('6'): Cell_10, Sub('7'): Cell_8, Sub('8'): Cell_16}
    Cell_12.subs = {Sub('0'): Cell_8, Sub('1'): Cell_12, Sub('2'): Cell_7, Sub('3'): Cell_8, Sub('4'): Cell_9, Sub('5'): Cell_10, Sub('6'): Cell_8, Sub('7'): Cell_16}
    Cell_13.subs = {Sub('0'): Cell_2, Sub('1'): Cell_7, Sub('2'): Cell_8, Sub('3'): Cell_16, Sub('4'): Cell_8, Sub('5'): Cell_9, Sub('6'): Cell_10, Sub('7'): Cell_8, Sub('8'): Cell_12}
    Cell_14.subs = {Sub('0'): Cell_6, Sub('1'): Cell_10, Sub('2'): Cell_8, Sub('3'): Cell_9, Sub('4'): Cell_10, Sub('5'): Cell_8, Sub('6'): Cell_11}
    Cell_15.subs = {Sub('0'): Cell_18, Sub('1'): Cell_19, Sub('2'): Cell_8, Sub('3'): Cell_16, Sub('4'): Cell_8, Sub('5'): Cell_9, Sub('6'): Cell_10, Sub('7'): Cell_8, Sub('8'): Cell_17}
    Cell_16.subs = {Sub('0'): Cell_8, Sub('1'): Cell_16, Sub('2'): Cell_8, Sub('3'): Cell_16, Sub('4'): Cell_8, Sub('5'): Cell_9, Sub('6'): Cell_10, Sub('7'): Cell_8, Sub('8'): Cell_16}
    Cell_17.subs = {Sub('0'): Cell_8, Sub('1'): Cell_17, Sub('2'): Cell_18, Sub('3'): Cell_20, Sub('4'): Cell_15, Sub('5'): Cell_8, Sub('6'): Cell_9, Sub('7'): Cell_10, Sub('8'): Cell_8, Sub('9'): Cell_16}
    Cell_18.subs = {Sub('0'): Cell_21, Sub('1'): Cell_18, Sub('2'): Cell_20, Sub('3'): Cell_15, Sub('4'): Cell_8, Sub('5'): Cell_9, Sub('6'): Cell_10, Sub('7'): Cell_8, Sub('8'): Cell_11}
    Cell_19.subs = {Sub('0'): Cell_21, Sub('1'): Cell_18, Sub('2'): Cell_19, Sub('3'): Cell_8, Sub('4'): Cell_16, Sub('5'): Cell_8, Sub('6'): Cell_9, Sub('7'): Cell_10, Sub('8'): Cell_8, Sub('9'): Cell_11}
    Cell_20.subs = {Sub('0'): Cell_21, Sub('1'): Cell_18, Sub('2'): Cell_19, Sub('3'): Cell_8, Sub('4'): Cell_9, Sub('5'): Cell_10, Sub('6'): Cell_8, Sub('7'): Cell_11}
    Cell_21.subs = {Sub('0'): Cell_18, Sub('1'): Cell_20, Sub('2'): Cell_15, Sub('3'): Cell_8, Sub('4'): Cell_9, Sub('5'): Cell_10, Sub('6'): Cell_8, Sub('7'): Cell_17}
    ##############################
    # build intern of all states
    Cell_0.buildIntern()
    Cell_1.buildIntern()
    Cell_2.buildIntern()
    Cell_3.buildIntern()
    Cell_4.buildIntern()
    Cell_5.buildIntern()
    Cell_6.buildIntern()
    Cell_7.buildIntern()
    Cell_8.buildIntern()
    Cell_9.buildIntern()
    Cell_10.buildIntern()
    Cell_11.buildIntern()
    Cell_12.buildIntern()
    Cell_13.buildIntern()
    Cell_14.buildIntern()
    Cell_15.buildIntern()
    Cell_16.buildIntern()
    Cell_17.buildIntern()
    Cell_18.buildIntern()
    Cell_19.buildIntern()
    Cell_20.buildIntern()
    Cell_21.buildIntern()
    ##############################
    # spaces of all states
    Cell_0.space = [Bord_('0'), Bord_('1'), Bord_('2'), Bord_('3'), Bord_('4'), Bord_('5')]
    Cell_1.space = [Bord_('0'), Bord_('1'), Bord_('2'), Bord_('3'), Bord_('4'), Bord_('5')]
    Cell_2.space = [Bord_('0'), Bord_('1'), Bord_('2'), Bord_('3'), Bord_('4')]
    Cell_3.space = [Bord_('0'), Bord_('1'), Bord_('2'), Bord_('3'), Bord_('4')]
    Cell_4.space = [Bord_('0'), Bord_('1'), Bord_('2'), Bord_('3'), Bord_('4')]
    Cell_5.space = [Bord_('0'), Bord_('1'), Bord_('2'), Bord_('3'), Bord_('4'), Bord_('5')]
    Cell_6.space = [Bord_('0'), Bord_('1'), Bord_('2'), Bord_('3'), Bord_('4')]
    Cell_7.space = [Bord_('0'), Bord_('1'), Bord_('2'), Bord_('3'), Bord_('4')]
    Cell_8.space = [Bord_('0'), Bord_('1'), Bord_('2'), Bord_('3')]
    Cell_9.space = [Bord_('0'), Bord_('1'), Bord_('2'), Bord_('3'), Bord_('4'), Bord_('5')]
    Cell_10.space = [Bord_('0'), Bord_('1'), Bord_('2'), Bord_('3'), Bord_('4'), Bord_('5')]
    Cell_11.space = [Bord_('0'), Bord_('1'), Bord_('2'), Bord_('3'), Bord_('4')]
    Cell_12.space = [Bord_('0'), Bord_('1'), Bord_('2'), Bord_('3'), Bord_('4')]
    Cell_13.space = [Bord_('0'), Bord_('1'), Bord_('2'), Bord_('3'), Bord_('4'), Bord_('5')]
    Cell_14.space = [Bord_('0'), Bord_('1'), Bord_('2'), Bord_('3'), Bord_('4')]
    Cell_15.space = [Bord_('0'), Bord_('1'), Bord_('2'), Bord_('3'), Bord_('4')]
    Cell_16.space = [Bord_('0'), Bord_('1'), Bord_('2'), Bord_('3'), Bord_('4')]
    Cell_17.space = [Bord_('0'), Bord_('1'), Bord_('2'), Bord_('3'), Bord_('4'), Bord_('5')]
    Cell_18.space = [Bord_('0'), Bord_('1'), Bord_('2'), Bord_('3'), Bord_('4'), Bord_('5')]
    Cell_19.space = [Bord_('0'), Bord_('1'), Bord_('2'), Bord_('3'), Bord_('4'), Bord_('5')]
    Cell_20.space = [Bord_('0'), Bord_('1'), Bord_('2'), Bord_('3'), Bord_('4')]
    Cell_21.space = [Bord_('0'), Bord_('1'), Bord_('2'), Bord_('3'), Bord_('4')]
    ##############################
    # grid of all states
    Cell_0.addGrid(Bord)
    Cell_1.addGrid(Bord)
    Cell_2.addGrid(Bord)
    Cell_3.addGrid(Bord)
    Cell_4.addGrid(Bord)
    Cell_5.addGrid(Bord)
    Cell_6.addGrid(Bord)
    Cell_7.addGrid(Bord)
    Cell_8.addGrid(Bord)
    Cell_9.addGrid(Bord)
    Cell_10.addGrid(Bord)
    Cell_11.addGrid(Bord)
    Cell_12.addGrid(Bord)
    Cell_13.addGrid(Bord)
    Cell_14.addGrid(Bord)
    Cell_15.addGrid(Bord)
    Cell_16.addGrid(Bord)
    Cell_17.addGrid(Bord)
    Cell_18.addGrid(Bord)
    Cell_19.addGrid(Bord)
    Cell_20.addGrid(Bord)
    Cell_21.addGrid(Bord)
    ##############################
    # prim of all states
    Cell_0.prim.elems = [Figure(2, [
        Bord_('0') + Bord('0'),
        Bord_('1') + Sub('0') + Sub('0') + Bord('0'),
        Bord_('1') + Sub('0') + Sub('1') + Bord('0'),
        Bord_('1') + Sub('1') + Sub('0') + Bord('0'),
        Bord_('1') + Sub('1') + Sub('1') + Bord('0'),
        Bord_('2') + Sub('0') + Sub('0') + Bord('0'),
        Bord_('2') + Sub('0') + Sub('1') + Bord('0'),
        Bord_('2') + Sub('1') + Sub('0') + Bord('0'),
        Bord_('2') + Sub('1') + Sub('1') + Bord('0'),
        Bord_('3') + Bord('0'),
        Bord_('4') + Bord('0'),
        Bord_('5') + Sub('0') + Sub('0') + Bord('0'),
        Bord_('5') + Sub('0') + Sub('1') + Bord('0'),
        Bord_('5') + Sub('1') + Sub('0') + Bord('0'),
        Bord_('5') + Sub('1') + Sub('1') + Bord('0'),
    ])]
    Cell_1.prim.elems = [Figure(2, [
        Bord_('0') + Bord('0'),
        Bord_('1') + Sub('0') + Sub('0') + Bord('0'),
        Bord_('1') + Sub('0') + Sub('1') + Bord('0'),
        Bord_('1') + Sub('1') + Sub('0') + Bord('0'),
        Bord_('1') + Sub('1') + Sub('1') + Bord('0'),
        Bord_('2') + Sub('0') + Bord('0'),
        Bord_('2') + Sub('1') + Bord('0'),
        Bord_('2') + Sub('2') + Bord('0'),
        Bord_('3') + Bord('0'),
        Bord_('4') + Sub('0') + Bord('0'),
        Bord_('4') + Sub('1') + Bord('0'),
        Bord_('4') + Sub('2') + Bord('0'),
        Bord_('5') + Bord('0'),
    ])]
    Cell_2.prim.elems = [Figure(2, [
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
        Bord_('3') + Bord('0'),
        Bord_('4') + Sub('0') + Bord('0'),
        Bord_('4') + Sub('1') + Bord('0'),
        Bord_('4') + Sub('2') + Bord('0'),
    ])]
    Cell_3.prim.elems = [Figure(2, [
        Bord_('0') + Sub('0') + Sub('0') + Bord('0'),
        Bord_('0') + Sub('0') + Sub('1') + Bord('0'),
        Bord_('0') + Sub('1') + Sub('0') + Bord('0'),
        Bord_('0') + Sub('1') + Sub('1') + Bord('0'),
        Bord_('1') + Bord('0'),
        Bord_('2') + Sub('0') + Bord('0'),
        Bord_('2') + Sub('1') + Bord('0'),
        Bord_('2') + Sub('2') + Bord('0'),
        Bord_('3') + Bord('0'),
        Bord_('4') + Sub('0') + Bord('0'),
        Bord_('4') + Sub('1') + Bord('0'),
        Bord_('4') + Sub('2') + Bord('0'),
    ])]
    Cell_4.prim.elems = [Figure(2, [
        Bord_('0') + Bord('0'),
        Bord_('1') + Sub('0') + Sub('0') + Bord('0'),
        Bord_('1') + Sub('0') + Sub('1') + Bord('0'),
        Bord_('1') + Sub('1') + Sub('0') + Bord('0'),
        Bord_('1') + Sub('1') + Sub('1') + Bord('0'),
        Bord_('2') + Sub('0') + Bord('0'),
        Bord_('2') + Sub('1') + Bord('0'),
        Bord_('2') + Sub('2') + Bord('0'),
        Bord_('3') + Bord('0'),
        Bord_('4') + Sub('0') + Bord('0'),
        Bord_('4') + Sub('1') + Bord('0'),
        Bord_('4') + Sub('2') + Bord('0'),
    ])]
    Cell_5.prim.elems = [Figure(2, [
        Bord_('0') + Sub('0') + Sub('0') + Bord('0'),
        Bord_('0') + Sub('0') + Sub('1') + Bord('0'),
        Bord_('0') + Sub('1') + Sub('0') + Bord('0'),
        Bord_('0') + Sub('1') + Sub('1') + Bord('0'),
        Bord_('1') + Bord('0'),
        Bord_('2') + Bord('0'),
        Bord_('3') + Sub('0') + Bord('0'),
        Bord_('3') + Sub('1') + Bord('0'),
        Bord_('3') + Sub('2') + Bord('0'),
        Bord_('4') + Bord('0'),
        Bord_('5') + Sub('0') + Bord('0'),
        Bord_('5') + Sub('1') + Bord('0'),
        Bord_('5') + Sub('2') + Bord('0'),
    ])]
    Cell_6.prim.elems = [Figure(2, [
        Bord_('0') + Bord('0'),
        Bord_('1') + Bord('0'),
        Bord_('2') + Sub('0') + Bord('0'),
        Bord_('2') + Sub('1') + Bord('0'),
        Bord_('2') + Sub('2') + Bord('0'),
        Bord_('3') + Bord('0'),
        Bord_('4') + Sub('0') + Bord('0'),
        Bord_('4') + Sub('1') + Bord('0'),
        Bord_('4') + Sub('2') + Bord('0'),
    ])]
    Cell_7.prim.elems = [Figure(2, [
        Bord_('0') + Sub('0') + Sub('0') + Bord('0'),
        Bord_('0') + Sub('0') + Sub('1') + Bord('0'),
        Bord_('0') + Sub('1') + Sub('0') + Bord('0'),
        Bord_('0') + Sub('1') + Sub('1') + Bord('0'),
        Bord_('1') + Sub('0') + Bord('0'),
        Bord_('1') + Sub('1') + Bord('0'),
        Bord_('1') + Sub('2') + Bord('0'),
        Bord_('2') + Sub('0') + Bord('0'),
        Bord_('2') + Sub('1') + Bord('0'),
        Bord_('2') + Sub('2') + Bord('0'),
        Bord_('3') + Bord('0'),
        Bord_('4') + Sub('0') + Bord('0'),
        Bord_('4') + Sub('1') + Bord('0'),
        Bord_('4') + Sub('2') + Bord('0'),
    ])]
    Cell_8.prim.elems = [Figure(2, [
        Bord_('0') + Sub('0') + Bord('0'),
        Bord_('0') + Sub('1') + Bord('0'),
        Bord_('0') + Sub('2') + Bord('0'),
        Bord_('1') + Sub('0') + Bord('0'),
        Bord_('1') + Sub('1') + Bord('0'),
        Bord_('1') + Sub('2') + Bord('0'),
        Bord_('2') + Bord('0'),
        Bord_('3') + Sub('0') + Bord('0'),
        Bord_('3') + Sub('1') + Bord('0'),
        Bord_('3') + Sub('2') + Bord('0'),
    ])]
    Cell_9.prim.elems = [Figure(2, [
        Bord_('0') + Sub('0') + Bord('0'),
        Bord_('0') + Sub('1') + Bord('0'),
        Bord_('0') + Sub('2') + Bord('0'),
        Bord_('1') + Bord('0'),
        Bord_('2') + Bord('0'),
        Bord_('3') + Sub('0') + Bord('0'),
        Bord_('3') + Sub('1') + Bord('0'),
        Bord_('3') + Sub('2') + Bord('0'),
        Bord_('4') + Bord('0'),
        Bord_('5') + Sub('0') + Bord('0'),
        Bord_('5') + Sub('1') + Bord('0'),
        Bord_('5') + Sub('2') + Bord('0'),
    ])]
    Cell_10.prim.elems = [Figure(2, [
        Bord_('0') + Bord('0'),
        Bord_('1') + Sub('0') + Bord('0'),
        Bord_('1') + Sub('1') + Bord('0'),
        Bord_('1') + Sub('2') + Bord('0'),
        Bord_('2') + Sub('0') + Bord('0'),
        Bord_('2') + Sub('1') + Bord('0'),
        Bord_('2') + Sub('2') + Bord('0'),
        Bord_('3') + Bord('0'),
        Bord_('4') + Sub('0') + Bord('0'),
        Bord_('4') + Sub('1') + Bord('0'),
        Bord_('4') + Sub('2') + Bord('0'),
        Bord_('5') + Bord('0'),
    ])]
    Cell_11.prim.elems = [Figure(2, [
        Bord_('0') + Sub('0') + Bord('0'),
        Bord_('0') + Sub('1') + Bord('0'),
        Bord_('0') + Sub('2') + Bord('0'),
        Bord_('1') + Bord('0'),
        Bord_('2') + Sub('0') + Bord('0'),
        Bord_('2') + Sub('1') + Bord('0'),
        Bord_('2') + Sub('2') + Bord('0'),
        Bord_('3') + Bord('0'),
        Bord_('4') + Sub('0') + Bord('0'),
        Bord_('4') + Sub('1') + Bord('0'),
        Bord_('4') + Sub('2') + Bord('0'),
    ])]
    Cell_12.prim.elems = [Figure(2, [
        Bord_('0') + Sub('0') + Bord('0'),
        Bord_('0') + Sub('1') + Bord('0'),
        Bord_('0') + Sub('2') + Bord('0'),
        Bord_('1') + Sub('0') + Sub('0') + Bord('0'),
        Bord_('1') + Sub('0') + Sub('1') + Bord('0'),
        Bord_('1') + Sub('1') + Sub('0') + Bord('0'),
        Bord_('1') + Sub('1') + Sub('1') + Bord('0'),
        Bord_('2') + Sub('0') + Bord('0'),
        Bord_('2') + Sub('1') + Bord('0'),
        Bord_('2') + Sub('2') + Bord('0'),
        Bord_('3') + Bord('0'),
        Bord_('4') + Sub('0') + Bord('0'),
        Bord_('4') + Sub('1') + Bord('0'),
        Bord_('4') + Sub('2') + Bord('0'),
    ])]
    Cell_13.prim.elems = [Figure(2, [
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
        Bord_('3') + Sub('0') + Bord('0'),
        Bord_('3') + Sub('1') + Bord('0'),
        Bord_('3') + Sub('2') + Bord('0'),
        Bord_('4') + Bord('0'),
        Bord_('5') + Sub('0') + Bord('0'),
        Bord_('5') + Sub('1') + Bord('0'),
        Bord_('5') + Sub('2') + Bord('0'),
    ])]
    Cell_14.prim.elems = [Figure(2, [
        Bord_('0') + Bord('0'),
        Bord_('1') + Sub('0') + Bord('0'),
        Bord_('1') + Sub('1') + Bord('0'),
        Bord_('1') + Sub('2') + Bord('0'),
        Bord_('2') + Bord('0'),
        Bord_('3') + Sub('0') + Bord('0'),
        Bord_('3') + Sub('1') + Bord('0'),
        Bord_('3') + Sub('2') + Bord('0'),
        Bord_('4') + Bord('0'),
    ])]
    Cell_15.prim.elems = [Figure(2, [
        Bord_('0') + Bord('0'),
        Bord_('1') + Sub('0') + Bord('0'),
        Bord_('1') + Sub('1') + Bord('0'),
        Bord_('1') + Sub('2') + Bord('0'),
        Bord_('2') + Sub('0') + Bord('0'),
        Bord_('2') + Sub('1') + Bord('0'),
        Bord_('2') + Sub('2') + Bord('0'),
        Bord_('3') + Bord('0'),
        Bord_('4') + Sub('0') + Bord('0'),
        Bord_('4') + Sub('1') + Bord('0'),
        Bord_('4') + Sub('2') + Bord('0'),
    ])]
    Cell_16.prim.elems = [Figure(2, [
        Bord_('0') + Sub('0') + Bord('0'),
        Bord_('0') + Sub('1') + Bord('0'),
        Bord_('0') + Sub('2') + Bord('0'),
        Bord_('1') + Sub('0') + Bord('0'),
        Bord_('1') + Sub('1') + Bord('0'),
        Bord_('1') + Sub('2') + Bord('0'),
        Bord_('2') + Sub('0') + Bord('0'),
        Bord_('2') + Sub('1') + Bord('0'),
        Bord_('2') + Sub('2') + Bord('0'),
        Bord_('3') + Bord('0'),
        Bord_('4') + Sub('0') + Bord('0'),
        Bord_('4') + Sub('1') + Bord('0'),
        Bord_('4') + Sub('2') + Bord('0'),
    ])]
    Cell_17.prim.elems = [Figure(2, [
        Bord_('0') + Sub('0') + Bord('0'),
        Bord_('0') + Sub('1') + Bord('0'),
        Bord_('0') + Sub('2') + Bord('0'),
        Bord_('1') + Bord('0'),
        Bord_('2') + Bord('0'),
        Bord_('3') + Sub('0') + Bord('0'),
        Bord_('3') + Sub('1') + Bord('0'),
        Bord_('3') + Sub('2') + Bord('0'),
        Bord_('4') + Bord('0'),
        Bord_('5') + Sub('0') + Bord('0'),
        Bord_('5') + Sub('1') + Bord('0'),
        Bord_('5') + Sub('2') + Bord('0'),
    ])]
    Cell_18.prim.elems = [Figure(2, [
        Bord_('0') + Bord('0'),
        Bord_('1') + Bord('0'),
        Bord_('2') + Sub('0') + Bord('0'),
        Bord_('2') + Sub('1') + Bord('0'),
        Bord_('2') + Sub('2') + Bord('0'),
        Bord_('3') + Bord('0'),
        Bord_('4') + Sub('0') + Bord('0'),
        Bord_('4') + Sub('1') + Bord('0'),
        Bord_('4') + Sub('2') + Bord('0'),
        Bord_('5') + Bord('0'),
    ])]
    Cell_19.prim.elems = [Figure(2, [
        Bord_('0') + Bord('0'),
        Bord_('1') + Sub('0') + Bord('0'),
        Bord_('1') + Sub('1') + Bord('0'),
        Bord_('1') + Sub('2') + Bord('0'),
        Bord_('2') + Sub('0') + Bord('0'),
        Bord_('2') + Sub('1') + Bord('0'),
        Bord_('2') + Sub('2') + Bord('0'),
        Bord_('3') + Bord('0'),
        Bord_('4') + Sub('0') + Bord('0'),
        Bord_('4') + Sub('1') + Bord('0'),
        Bord_('4') + Sub('2') + Bord('0'),
        Bord_('5') + Bord('0'),
    ])]
    Cell_20.prim.elems = [Figure(2, [
        Bord_('0') + Bord('0'),
        Bord_('1') + Sub('0') + Bord('0'),
        Bord_('1') + Sub('1') + Bord('0'),
        Bord_('1') + Sub('2') + Bord('0'),
        Bord_('2') + Bord('0'),
        Bord_('3') + Sub('0') + Bord('0'),
        Bord_('3') + Sub('1') + Bord('0'),
        Bord_('3') + Sub('2') + Bord('0'),
        Bord_('4') + Bord('0'),
    ])]
    Cell_21.prim.elems = [Figure(2, [
        Bord_('0') + Bord('0'),
        Bord_('1') + Bord('0'),
        Bord_('2') + Sub('0') + Bord('0'),
        Bord_('2') + Sub('1') + Bord('0'),
        Bord_('2') + Sub('2') + Bord('0'),
        Bord_('3') + Bord('0'),
        Bord_('4') + Sub('0') + Bord('0'),
        Bord_('4') + Sub('1') + Bord('0'),
        Bord_('4') + Sub('2') + Bord('0'),
    ])]
    ##############################
    # constraints of all states
    # incidence constraints
    Cell_0(Bord('0') + Sub('1'), Sub('0') + Bord('0'))
    Cell_0(Bord('1') + Sub('0'), Sub('0') + Bord('1'))
    Cell_0(Bord('1') + Sub('1'), Sub('1') + Bord('0'))
    Cell_0(Bord('2') + Sub('0'), Sub('1') + Bord('1'))
    Cell_0(Bord('2') + Sub('1'), Sub('2') + Bord('0'))
    Cell_0(Bord('3') + Sub('0'), Sub('2') + Bord('1'))
    Cell_0(Bord('4') + Sub('0'), Sub('3') + Bord('0'))
    Cell_0(Bord('5') + Sub('0'), Sub('3') + Bord('1'))
    Cell_0(Bord('5') + Sub('1'), Sub('4') + Bord('0'))
    Cell_0(Bord('0') + Sub('0'), Sub('4') + Bord('1'))
    # adjacency constraints
    Cell_0(Sub('0') + Bord('2') + Permut('0'), Sub('1') + Bord('4'))
    Cell_0(Sub('1') + Bord('2') + Permut('0'), Sub('2') + Bord('4'))
    Cell_0(Sub('2') + Bord('2') + Permut('0'), Sub('3') + Bord('4'))
    Cell_0(Sub('3') + Bord('2') + Permut('0'), Sub('4') + Bord('5'))
    Cell_0(Sub('4') + Bord('3') + Permut('0'), Sub('0') + Bord('4'))
    # edges adjacency constraints
    Cell_0(Bord('0') + Bord('1'), Bord('1') + Bord('0'))
    Cell_0(Bord('1') + Bord('1'), Bord('2') + Bord('0'))
    Cell_0(Bord('2') + Bord('1'), Bord('3') + Bord('0'))
    Cell_0(Bord('3') + Bord('1'), Bord('4') + Bord('0'))
    Cell_0(Bord('4') + Bord('1'), Bord('5') + Bord('0'))
    Cell_0(Bord('5') + Bord('1'), Bord('0') + Bord('0'))
    # incidence constraints
    Cell_1(Bord('0') + Sub('0'), Sub('0') + Bord('0'))
    Cell_1(Bord('0') + Sub('1'), Sub('1') + Bord('0'))
    Cell_1(Bord('1') + Sub('0'), Sub('1') + Bord('1'))
    Cell_1(Bord('1') + Sub('1'), Sub('2') + Bord('0'))
    Cell_1(Bord('2') + Sub('0'), Sub('2') + Bord('1'))
    Cell_1(Bord('2') + Sub('1'), Sub('3') + Bord('0'))
    Cell_1(Bord('2') + Sub('2'), Sub('4') + Bord('0'))
    Cell_1(Bord('3') + Sub('0'), Sub('4') + Bord('1'))
    Cell_1(Bord('3') + Sub('1'), Sub('5') + Bord('0'))
    Cell_1(Bord('4') + Sub('0'), Sub('5') + Bord('1'))
    Cell_1(Bord('4') + Sub('1'), Sub('6') + Bord('0'))
    Cell_1(Bord('4') + Sub('2'), Sub('7') + Bord('0'))
    Cell_1(Bord('5') + Sub('0'), Sub('7') + Bord('1'))
    # adjacency constraints
    Cell_1(Sub('0') + Bord('2') + Permut('0'), Sub('1') + Bord('4'))
    Cell_1(Sub('1') + Bord('2') + Permut('0'), Sub('2') + Bord('4'))
    Cell_1(Sub('2') + Bord('2') + Permut('0'), Sub('3') + Bord('3'))
    Cell_1(Sub('3') + Bord('1') + Permut('0'), Sub('4') + Bord('5'))
    Cell_1(Sub('4') + Bord('3') + Permut('0'), Sub('5') + Bord('4'))
    Cell_1(Sub('5') + Bord('2') + Permut('0'), Sub('6') + Bord('3'))
    Cell_1(Sub('6') + Bord('1') + Permut('0'), Sub('7') + Bord('4'))
    Cell_1(Sub('7') + Bord('2') + Permut('0'), Sub('0') + Bord('4'))
    # edges adjacency constraints
    Cell_1(Bord('0') + Bord('1'), Bord('1') + Bord('0'))
    Cell_1(Bord('1') + Bord('1'), Bord('2') + Bord('0'))
    Cell_1(Bord('2') + Bord('1'), Bord('3') + Bord('0'))
    Cell_1(Bord('3') + Bord('1'), Bord('4') + Bord('0'))
    Cell_1(Bord('4') + Bord('1'), Bord('5') + Bord('0'))
    Cell_1(Bord('5') + Bord('1'), Bord('0') + Bord('0'))
    # incidence constraints
    Cell_2(Bord('0') + Sub('1'), Sub('0') + Bord('0'))
    Cell_2(Bord('1') + Sub('0'), Sub('0') + Bord('1'))
    Cell_2(Bord('1') + Sub('1'), Sub('1') + Bord('0'))
    Cell_2(Bord('2') + Sub('0'), Sub('1') + Bord('1'))
    Cell_2(Bord('2') + Sub('1'), Sub('2') + Bord('0'))
    Cell_2(Bord('2') + Sub('2'), Sub('3') + Bord('0'))
    Cell_2(Bord('3') + Sub('0'), Sub('3') + Bord('1'))
    Cell_2(Bord('3') + Sub('1'), Sub('4') + Bord('0'))
    Cell_2(Bord('4') + Sub('0'), Sub('4') + Bord('1'))
    Cell_2(Bord('4') + Sub('1'), Sub('5') + Bord('0'))
    Cell_2(Bord('4') + Sub('2'), Sub('6') + Bord('0'))
    Cell_2(Bord('0') + Sub('0'), Sub('6') + Bord('1'))
    # adjacency constraints
    Cell_2(Sub('0') + Bord('2') + Permut('0'), Sub('1') + Bord('4'))
    Cell_2(Sub('1') + Bord('2') + Permut('0'), Sub('2') + Bord('3'))
    Cell_2(Sub('2') + Bord('1') + Permut('0'), Sub('3') + Bord('5'))
    Cell_2(Sub('3') + Bord('3') + Permut('0'), Sub('4') + Bord('4'))
    Cell_2(Sub('4') + Bord('2') + Permut('0'), Sub('5') + Bord('3'))
    Cell_2(Sub('5') + Bord('1') + Permut('0'), Sub('6') + Bord('4'))
    Cell_2(Sub('6') + Bord('2') + Permut('0'), Sub('0') + Bord('4'))
    # edges adjacency constraints
    Cell_2(Bord('0') + Bord('1'), Bord('1') + Bord('0'))
    Cell_2(Bord('1') + Bord('1'), Bord('2') + Bord('0'))
    Cell_2(Bord('2') + Bord('1'), Bord('3') + Bord('0'))
    Cell_2(Bord('3') + Bord('1'), Bord('4') + Bord('0'))
    Cell_2(Bord('4') + Bord('1'), Bord('0') + Bord('0'))
    # incidence constraints
    Cell_3(Bord('0') + Sub('1'), Sub('0') + Bord('0'))
    Cell_3(Bord('1') + Sub('0'), Sub('0') + Bord('1'))
    Cell_3(Bord('2') + Sub('0'), Sub('0') + Bord('2'))
    Cell_3(Bord('2') + Sub('1'), Sub('1') + Bord('0'))
    Cell_3(Bord('2') + Sub('2'), Sub('2') + Bord('0'))
    Cell_3(Bord('3') + Sub('0'), Sub('2') + Bord('1'))
    Cell_3(Bord('3') + Sub('1'), Sub('3') + Bord('0'))
    Cell_3(Bord('4') + Sub('0'), Sub('3') + Bord('1'))
    Cell_3(Bord('4') + Sub('1'), Sub('4') + Bord('0'))
    Cell_3(Bord('4') + Sub('2'), Sub('5') + Bord('0'))
    Cell_3(Bord('0') + Sub('0'), Sub('5') + Bord('1'))
    # adjacency constraints
    Cell_3(Sub('0') + Bord('3') + Permut('0'), Sub('1') + Bord('3'))
    Cell_3(Sub('1') + Bord('1') + Permut('0'), Sub('2') + Bord('5'))
    Cell_3(Sub('2') + Bord('3') + Permut('0'), Sub('3') + Bord('4'))
    Cell_3(Sub('3') + Bord('2') + Permut('0'), Sub('4') + Bord('3'))
    Cell_3(Sub('4') + Bord('1') + Permut('0'), Sub('5') + Bord('4'))
    Cell_3(Sub('5') + Bord('2') + Permut('0'), Sub('0') + Bord('5'))
    # edges adjacency constraints
    Cell_3(Bord('0') + Bord('1'), Bord('1') + Bord('0'))
    Cell_3(Bord('1') + Bord('1'), Bord('2') + Bord('0'))
    Cell_3(Bord('2') + Bord('1'), Bord('3') + Bord('0'))
    Cell_3(Bord('3') + Bord('1'), Bord('4') + Bord('0'))
    Cell_3(Bord('4') + Bord('1'), Bord('0') + Bord('0'))
    # incidence constraints
    Cell_4(Bord('0') + Sub('1'), Sub('0') + Bord('0'))
    Cell_4(Bord('1') + Sub('0'), Sub('0') + Bord('1'))
    Cell_4(Bord('1') + Sub('1'), Sub('1') + Bord('0'))
    Cell_4(Bord('2') + Sub('0'), Sub('1') + Bord('1'))
    Cell_4(Bord('2') + Sub('1'), Sub('2') + Bord('0'))
    Cell_4(Bord('2') + Sub('2'), Sub('3') + Bord('0'))
    Cell_4(Bord('3') + Sub('0'), Sub('3') + Bord('1'))
    Cell_4(Bord('3') + Sub('1'), Sub('4') + Bord('0'))
    Cell_4(Bord('4') + Sub('0'), Sub('4') + Bord('1'))
    Cell_4(Bord('4') + Sub('1'), Sub('5') + Bord('0'))
    Cell_4(Bord('4') + Sub('2'), Sub('6') + Bord('0'))
    Cell_4(Bord('0') + Sub('0'), Sub('6') + Bord('1'))
    # adjacency constraints
    Cell_4(Sub('0') + Bord('2') + Permut('0'), Sub('1') + Bord('4'))
    Cell_4(Sub('1') + Bord('2') + Permut('0'), Sub('2') + Bord('3'))
    Cell_4(Sub('2') + Bord('1') + Permut('0'), Sub('3') + Bord('5'))
    Cell_4(Sub('3') + Bord('3') + Permut('0'), Sub('4') + Bord('4'))
    Cell_4(Sub('4') + Bord('2') + Permut('0'), Sub('5') + Bord('3'))
    Cell_4(Sub('5') + Bord('1') + Permut('0'), Sub('6') + Bord('5'))
    Cell_4(Sub('6') + Bord('3') + Permut('0'), Sub('0') + Bord('4'))
    # edges adjacency constraints
    Cell_4(Bord('0') + Bord('1'), Bord('1') + Bord('0'))
    Cell_4(Bord('1') + Bord('1'), Bord('2') + Bord('0'))
    Cell_4(Bord('2') + Bord('1'), Bord('3') + Bord('0'))
    Cell_4(Bord('3') + Bord('1'), Bord('4') + Bord('0'))
    Cell_4(Bord('4') + Bord('1'), Bord('0') + Bord('0'))
    # incidence constraints
    Cell_5(Bord('0') + Sub('1'), Sub('0') + Bord('0'))
    Cell_5(Bord('1') + Sub('0'), Sub('0') + Bord('1'))
    Cell_5(Bord('1') + Sub('1'), Sub('1') + Bord('0'))
    Cell_5(Bord('2') + Sub('0'), Sub('2') + Bord('0'))
    Cell_5(Bord('3') + Sub('0'), Sub('2') + Bord('1'))
    Cell_5(Bord('3') + Sub('1'), Sub('3') + Bord('0'))
    Cell_5(Bord('3') + Sub('2'), Sub('4') + Bord('0'))
    Cell_5(Bord('4') + Sub('0'), Sub('4') + Bord('1'))
    Cell_5(Bord('4') + Sub('1'), Sub('5') + Bord('0'))
    Cell_5(Bord('5') + Sub('0'), Sub('5') + Bord('1'))
    Cell_5(Bord('5') + Sub('1'), Sub('6') + Bord('0'))
    Cell_5(Bord('5') + Sub('2'), Sub('7') + Bord('0'))
    Cell_5(Bord('0') + Sub('0'), Sub('7') + Bord('1'))
    # adjacency constraints
    Cell_5(Sub('0') + Bord('3') + Permut('0'), Sub('1') + Bord('3'))
    Cell_5(Sub('1') + Bord('1') + Permut('0'), Sub('2') + Bord('4'))
    Cell_5(Sub('2') + Bord('2') + Permut('0'), Sub('3') + Bord('3'))
    Cell_5(Sub('3') + Bord('1') + Permut('0'), Sub('4') + Bord('5'))
    Cell_5(Sub('4') + Bord('3') + Permut('0'), Sub('5') + Bord('4'))
    Cell_5(Sub('5') + Bord('2') + Permut('0'), Sub('6') + Bord('3'))
    Cell_5(Sub('6') + Bord('1') + Permut('0'), Sub('7') + Bord('4'))
    Cell_5(Sub('7') + Bord('2') + Permut('0'), Sub('0') + Bord('5'))
    # edges adjacency constraints
    Cell_5(Bord('0') + Bord('1'), Bord('1') + Bord('0'))
    Cell_5(Bord('1') + Bord('1'), Bord('2') + Bord('0'))
    Cell_5(Bord('2') + Bord('1'), Bord('3') + Bord('0'))
    Cell_5(Bord('3') + Bord('1'), Bord('4') + Bord('0'))
    Cell_5(Bord('4') + Bord('1'), Bord('5') + Bord('0'))
    Cell_5(Bord('5') + Bord('1'), Bord('0') + Bord('0'))
    # incidence constraints
    Cell_6(Bord('0') + Sub('1'), Sub('0') + Bord('0'))
    Cell_6(Bord('1') + Sub('0'), Sub('1') + Bord('0'))
    Cell_6(Bord('2') + Sub('0'), Sub('1') + Bord('1'))
    Cell_6(Bord('2') + Sub('1'), Sub('2') + Bord('0'))
    Cell_6(Bord('2') + Sub('2'), Sub('3') + Bord('0'))
    Cell_6(Bord('3') + Sub('0'), Sub('3') + Bord('1'))
    Cell_6(Bord('3') + Sub('1'), Sub('4') + Bord('0'))
    Cell_6(Bord('4') + Sub('0'), Sub('4') + Bord('1'))
    Cell_6(Bord('4') + Sub('1'), Sub('5') + Bord('0'))
    Cell_6(Bord('4') + Sub('2'), Sub('6') + Bord('0'))
    Cell_6(Bord('0') + Sub('0'), Sub('6') + Bord('1'))
    # adjacency constraints
    Cell_6(Sub('0') + Bord('1') + Permut('0'), Sub('1') + Bord('4'))
    Cell_6(Sub('1') + Bord('2') + Permut('0'), Sub('2') + Bord('3'))
    Cell_6(Sub('2') + Bord('1') + Permut('0'), Sub('3') + Bord('5'))
    Cell_6(Sub('3') + Bord('3') + Permut('0'), Sub('4') + Bord('4'))
    Cell_6(Sub('4') + Bord('2') + Permut('0'), Sub('5') + Bord('3'))
    Cell_6(Sub('5') + Bord('1') + Permut('0'), Sub('6') + Bord('5'))
    Cell_6(Sub('6') + Bord('3') + Permut('0'), Sub('0') + Bord('3'))
    # edges adjacency constraints
    Cell_6(Bord('0') + Bord('1'), Bord('1') + Bord('0'))
    Cell_6(Bord('1') + Bord('1'), Bord('2') + Bord('0'))
    Cell_6(Bord('2') + Bord('1'), Bord('3') + Bord('0'))
    Cell_6(Bord('3') + Bord('1'), Bord('4') + Bord('0'))
    Cell_6(Bord('4') + Bord('1'), Bord('0') + Bord('0'))
    # incidence constraints
    Cell_7(Bord('0') + Sub('1'), Sub('0') + Bord('0'))
    Cell_7(Bord('1') + Sub('0'), Sub('0') + Bord('1'))
    Cell_7(Bord('1') + Sub('1'), Sub('1') + Bord('0'))
    Cell_7(Bord('1') + Sub('2'), Sub('2') + Bord('0'))
    Cell_7(Bord('2') + Sub('0'), Sub('2') + Bord('1'))
    Cell_7(Bord('2') + Sub('1'), Sub('3') + Bord('0'))
    Cell_7(Bord('2') + Sub('2'), Sub('4') + Bord('0'))
    Cell_7(Bord('3') + Sub('0'), Sub('4') + Bord('1'))
    Cell_7(Bord('3') + Sub('1'), Sub('5') + Bord('0'))
    Cell_7(Bord('4') + Sub('0'), Sub('5') + Bord('1'))
    Cell_7(Bord('4') + Sub('1'), Sub('6') + Bord('0'))
    Cell_7(Bord('4') + Sub('2'), Sub('7') + Bord('0'))
    Cell_7(Bord('0') + Sub('0'), Sub('7') + Bord('1'))
    # adjacency constraints
    Cell_7(Sub('0') + Bord('2') + Permut('0'), Sub('1') + Bord('3'))
    Cell_7(Sub('1') + Bord('1') + Permut('0'), Sub('2') + Bord('4'))
    Cell_7(Sub('2') + Bord('2') + Permut('0'), Sub('3') + Bord('3'))
    Cell_7(Sub('3') + Bord('1') + Permut('0'), Sub('4') + Bord('5'))
    Cell_7(Sub('4') + Bord('3') + Permut('0'), Sub('5') + Bord('4'))
    Cell_7(Sub('5') + Bord('2') + Permut('0'), Sub('6') + Bord('3'))
    Cell_7(Sub('6') + Bord('1') + Permut('0'), Sub('7') + Bord('4'))
    Cell_7(Sub('7') + Bord('2') + Permut('0'), Sub('0') + Bord('4'))
    # edges adjacency constraints
    Cell_7(Bord('0') + Bord('1'), Bord('1') + Bord('0'))
    Cell_7(Bord('1') + Bord('1'), Bord('2') + Bord('0'))
    Cell_7(Bord('2') + Bord('1'), Bord('3') + Bord('0'))
    Cell_7(Bord('3') + Bord('1'), Bord('4') + Bord('0'))
    Cell_7(Bord('4') + Bord('1'), Bord('0') + Bord('0'))
    # incidence constraints
    Cell_8(Bord('0') + Sub('1'), Sub('0') + Bord('0'))
    Cell_8(Bord('0') + Sub('2'), Sub('1') + Bord('0'))
    Cell_8(Bord('1') + Sub('0'), Sub('1') + Bord('1'))
    Cell_8(Bord('1') + Sub('1'), Sub('2') + Bord('0'))
    Cell_8(Bord('1') + Sub('2'), Sub('3') + Bord('0'))
    Cell_8(Bord('2') + Sub('0'), Sub('3') + Bord('1'))
    Cell_8(Bord('2') + Sub('1'), Sub('4') + Bord('0'))
    Cell_8(Bord('3') + Sub('0'), Sub('4') + Bord('1'))
    Cell_8(Bord('3') + Sub('1'), Sub('5') + Bord('0'))
    Cell_8(Bord('3') + Sub('2'), Sub('6') + Bord('0'))
    Cell_8(Bord('0') + Sub('0'), Sub('6') + Bord('1'))
    # adjacency constraints
    Cell_8(Sub('0') + Bord('1') + Permut('0'), Sub('1') + Bord('4'))
    Cell_8(Sub('1') + Bord('2') + Permut('0'), Sub('2') + Bord('3'))
    Cell_8(Sub('2') + Bord('1') + Permut('0'), Sub('3') + Bord('5'))
    Cell_8(Sub('3') + Bord('3') + Permut('0'), Sub('4') + Bord('4'))
    Cell_8(Sub('4') + Bord('2') + Permut('0'), Sub('5') + Bord('3'))
    Cell_8(Sub('5') + Bord('1') + Permut('0'), Sub('6') + Bord('4'))
    Cell_8(Sub('6') + Bord('2') + Permut('0'), Sub('0') + Bord('3'))
    # edges adjacency constraints
    Cell_8(Bord('0') + Bord('1'), Bord('1') + Bord('0'))
    Cell_8(Bord('1') + Bord('1'), Bord('2') + Bord('0'))
    Cell_8(Bord('2') + Bord('1'), Bord('3') + Bord('0'))
    Cell_8(Bord('3') + Bord('1'), Bord('0') + Bord('0'))
    # incidence constraints
    Cell_9(Bord('0') + Sub('1'), Sub('0') + Bord('0'))
    Cell_9(Bord('0') + Sub('2'), Sub('1') + Bord('0'))
    Cell_9(Bord('1') + Sub('0'), Sub('1') + Bord('1'))
    Cell_9(Bord('1') + Sub('1'), Sub('2') + Bord('0'))
    Cell_9(Bord('2') + Sub('0'), Sub('3') + Bord('0'))
    Cell_9(Bord('3') + Sub('0'), Sub('3') + Bord('1'))
    Cell_9(Bord('3') + Sub('1'), Sub('4') + Bord('0'))
    Cell_9(Bord('3') + Sub('2'), Sub('5') + Bord('0'))
    Cell_9(Bord('4') + Sub('0'), Sub('5') + Bord('1'))
    Cell_9(Bord('4') + Sub('1'), Sub('6') + Bord('0'))
    Cell_9(Bord('5') + Sub('0'), Sub('6') + Bord('1'))
    Cell_9(Bord('5') + Sub('1'), Sub('7') + Bord('0'))
    Cell_9(Bord('5') + Sub('2'), Sub('8') + Bord('0'))
    Cell_9(Bord('0') + Sub('0'), Sub('8') + Bord('1'))
    # adjacency constraints
    Cell_9(Sub('0') + Bord('1') + Permut('0'), Sub('1') + Bord('5'))
    Cell_9(Sub('1') + Bord('3') + Permut('0'), Sub('2') + Bord('3'))
    Cell_9(Sub('2') + Bord('1') + Permut('0'), Sub('3') + Bord('4'))
    Cell_9(Sub('3') + Bord('2') + Permut('0'), Sub('4') + Bord('3'))
    Cell_9(Sub('4') + Bord('1') + Permut('0'), Sub('5') + Bord('5'))
    Cell_9(Sub('5') + Bord('3') + Permut('0'), Sub('6') + Bord('4'))
    Cell_9(Sub('6') + Bord('2') + Permut('0'), Sub('7') + Bord('3'))
    Cell_9(Sub('7') + Bord('1') + Permut('0'), Sub('8') + Bord('4'))
    Cell_9(Sub('8') + Bord('2') + Permut('0'), Sub('0') + Bord('3'))
    # edges adjacency constraints
    Cell_9(Bord('0') + Bord('1'), Bord('1') + Bord('0'))
    Cell_9(Bord('1') + Bord('1'), Bord('2') + Bord('0'))
    Cell_9(Bord('2') + Bord('1'), Bord('3') + Bord('0'))
    Cell_9(Bord('3') + Bord('1'), Bord('4') + Bord('0'))
    Cell_9(Bord('4') + Bord('1'), Bord('5') + Bord('0'))
    Cell_9(Bord('5') + Bord('1'), Bord('0') + Bord('0'))
    # incidence constraints
    Cell_10(Bord('0') + Sub('0'), Sub('0') + Bord('0'))
    Cell_10(Bord('0') + Sub('1'), Sub('1') + Bord('0'))
    Cell_10(Bord('1') + Sub('0'), Sub('1') + Bord('1'))
    Cell_10(Bord('1') + Sub('1'), Sub('2') + Bord('0'))
    Cell_10(Bord('1') + Sub('2'), Sub('3') + Bord('0'))
    Cell_10(Bord('2') + Sub('0'), Sub('3') + Bord('1'))
    Cell_10(Bord('2') + Sub('1'), Sub('4') + Bord('0'))
    Cell_10(Bord('2') + Sub('2'), Sub('5') + Bord('0'))
    Cell_10(Bord('3') + Sub('0'), Sub('5') + Bord('1'))
    Cell_10(Bord('3') + Sub('1'), Sub('6') + Bord('0'))
    Cell_10(Bord('4') + Sub('0'), Sub('6') + Bord('1'))
    Cell_10(Bord('4') + Sub('1'), Sub('7') + Bord('0'))
    Cell_10(Bord('4') + Sub('2'), Sub('8') + Bord('0'))
    Cell_10(Bord('5') + Sub('0'), Sub('8') + Bord('1'))
    # adjacency constraints
    Cell_10(Sub('0') + Bord('2') + Permut('0'), Sub('1') + Bord('4'))
    Cell_10(Sub('1') + Bord('2') + Permut('0'), Sub('2') + Bord('3'))
    Cell_10(Sub('2') + Bord('1') + Permut('0'), Sub('3') + Bord('4'))
    Cell_10(Sub('3') + Bord('2') + Permut('0'), Sub('4') + Bord('3'))
    Cell_10(Sub('4') + Bord('1') + Permut('0'), Sub('5') + Bord('5'))
    Cell_10(Sub('5') + Bord('3') + Permut('0'), Sub('6') + Bord('4'))
    Cell_10(Sub('6') + Bord('2') + Permut('0'), Sub('7') + Bord('3'))
    Cell_10(Sub('7') + Bord('1') + Permut('0'), Sub('8') + Bord('4'))
    Cell_10(Sub('8') + Bord('2') + Permut('0'), Sub('0') + Bord('4'))
    # edges adjacency constraints
    Cell_10(Bord('0') + Bord('1'), Bord('1') + Bord('0'))
    Cell_10(Bord('1') + Bord('1'), Bord('2') + Bord('0'))
    Cell_10(Bord('2') + Bord('1'), Bord('3') + Bord('0'))
    Cell_10(Bord('3') + Bord('1'), Bord('4') + Bord('0'))
    Cell_10(Bord('4') + Bord('1'), Bord('5') + Bord('0'))
    Cell_10(Bord('5') + Bord('1'), Bord('0') + Bord('0'))
    # incidence constraints
    Cell_11(Bord('0') + Sub('1'), Sub('0') + Bord('0'))
    Cell_11(Bord('0') + Sub('2'), Sub('1') + Bord('0'))
    Cell_11(Bord('1') + Sub('0'), Sub('1') + Bord('1'))
    Cell_11(Bord('1') + Sub('1'), Sub('2') + Bord('0'))
    Cell_11(Bord('1') + Sub('2'), Sub('3') + Bord('0'))
    Cell_11(Bord('2') + Sub('0'), Sub('3') + Bord('1'))
    Cell_11(Bord('2') + Sub('1'), Sub('4') + Bord('0'))
    Cell_11(Bord('2') + Sub('2'), Sub('5') + Bord('0'))
    Cell_11(Bord('3') + Sub('0'), Sub('5') + Bord('1'))
    Cell_11(Bord('3') + Sub('1'), Sub('6') + Bord('0'))
    Cell_11(Bord('4') + Sub('0'), Sub('6') + Bord('1'))
    Cell_11(Bord('4') + Sub('1'), Sub('7') + Bord('0'))
    Cell_11(Bord('4') + Sub('2'), Sub('8') + Bord('0'))
    Cell_11(Bord('0') + Sub('0'), Sub('8') + Bord('1'))
    # adjacency constraints
    Cell_11(Sub('0') + Bord('1') + Permut('0'), Sub('1') + Bord('5'))
    Cell_11(Sub('1') + Bord('3') + Permut('0'), Sub('2') + Bord('4'))
    Cell_11(Sub('2') + Bord('2') + Permut('0'), Sub('3') + Bord('4'))
    Cell_11(Sub('3') + Bord('2') + Permut('0'), Sub('4') + Bord('3'))
    Cell_11(Sub('4') + Bord('1') + Permut('0'), Sub('5') + Bord('5'))
    Cell_11(Sub('5') + Bord('3') + Permut('0'), Sub('6') + Bord('4'))
    Cell_11(Sub('6') + Bord('2') + Permut('0'), Sub('7') + Bord('3'))
    Cell_11(Sub('7') + Bord('1') + Permut('0'), Sub('8') + Bord('4'))
    Cell_11(Sub('8') + Bord('2') + Permut('0'), Sub('0') + Bord('3'))
    # edges adjacency constraints
    Cell_11(Bord('0') + Bord('1'), Bord('1') + Bord('0'))
    Cell_11(Bord('1') + Bord('1'), Bord('2') + Bord('0'))
    Cell_11(Bord('2') + Bord('1'), Bord('3') + Bord('0'))
    Cell_11(Bord('3') + Bord('1'), Bord('4') + Bord('0'))
    Cell_11(Bord('4') + Bord('1'), Bord('0') + Bord('0'))
    # incidence constraints
    Cell_12(Bord('0') + Sub('1'), Sub('0') + Bord('0'))
    Cell_12(Bord('0') + Sub('2'), Sub('1') + Bord('0'))
    Cell_12(Bord('1') + Sub('0'), Sub('1') + Bord('1'))
    Cell_12(Bord('1') + Sub('1'), Sub('2') + Bord('0'))
    Cell_12(Bord('2') + Sub('0'), Sub('2') + Bord('1'))
    Cell_12(Bord('2') + Sub('1'), Sub('3') + Bord('0'))
    Cell_12(Bord('2') + Sub('2'), Sub('4') + Bord('0'))
    Cell_12(Bord('3') + Sub('0'), Sub('4') + Bord('1'))
    Cell_12(Bord('3') + Sub('1'), Sub('5') + Bord('0'))
    Cell_12(Bord('4') + Sub('0'), Sub('5') + Bord('1'))
    Cell_12(Bord('4') + Sub('1'), Sub('6') + Bord('0'))
    Cell_12(Bord('4') + Sub('2'), Sub('7') + Bord('0'))
    Cell_12(Bord('0') + Sub('0'), Sub('7') + Bord('1'))
    # adjacency constraints
    Cell_12(Sub('0') + Bord('1') + Permut('0'), Sub('1') + Bord('4'))
    Cell_12(Sub('1') + Bord('2') + Permut('0'), Sub('2') + Bord('4'))
    Cell_12(Sub('2') + Bord('2') + Permut('0'), Sub('3') + Bord('3'))
    Cell_12(Sub('3') + Bord('1') + Permut('0'), Sub('4') + Bord('5'))
    Cell_12(Sub('4') + Bord('3') + Permut('0'), Sub('5') + Bord('4'))
    Cell_12(Sub('5') + Bord('2') + Permut('0'), Sub('6') + Bord('3'))
    Cell_12(Sub('6') + Bord('1') + Permut('0'), Sub('7') + Bord('4'))
    Cell_12(Sub('7') + Bord('2') + Permut('0'), Sub('0') + Bord('3'))
    # edges adjacency constraints
    Cell_12(Bord('0') + Bord('1'), Bord('1') + Bord('0'))
    Cell_12(Bord('1') + Bord('1'), Bord('2') + Bord('0'))
    Cell_12(Bord('2') + Bord('1'), Bord('3') + Bord('0'))
    Cell_12(Bord('3') + Bord('1'), Bord('4') + Bord('0'))
    Cell_12(Bord('4') + Bord('1'), Bord('0') + Bord('0'))
    # incidence constraints
    Cell_13(Bord('0') + Sub('1'), Sub('0') + Bord('0'))
    Cell_13(Bord('1') + Sub('0'), Sub('0') + Bord('1'))
    Cell_13(Bord('1') + Sub('1'), Sub('1') + Bord('0'))
    Cell_13(Bord('2') + Sub('0'), Sub('1') + Bord('1'))
    Cell_13(Bord('2') + Sub('1'), Sub('2') + Bord('0'))
    Cell_13(Bord('2') + Sub('2'), Sub('3') + Bord('0'))
    Cell_13(Bord('3') + Sub('0'), Sub('3') + Bord('1'))
    Cell_13(Bord('3') + Sub('1'), Sub('4') + Bord('0'))
    Cell_13(Bord('3') + Sub('2'), Sub('5') + Bord('0'))
    Cell_13(Bord('4') + Sub('0'), Sub('5') + Bord('1'))
    Cell_13(Bord('4') + Sub('1'), Sub('6') + Bord('0'))
    Cell_13(Bord('5') + Sub('0'), Sub('6') + Bord('1'))
    Cell_13(Bord('5') + Sub('1'), Sub('7') + Bord('0'))
    Cell_13(Bord('5') + Sub('2'), Sub('8') + Bord('0'))
    Cell_13(Bord('0') + Sub('0'), Sub('8') + Bord('1'))
    # adjacency constraints
    Cell_13(Sub('0') + Bord('2') + Permut('0'), Sub('1') + Bord('4'))
    Cell_13(Sub('1') + Bord('2') + Permut('0'), Sub('2') + Bord('3'))
    Cell_13(Sub('2') + Bord('1') + Permut('0'), Sub('3') + Bord('4'))
    Cell_13(Sub('3') + Bord('2') + Permut('0'), Sub('4') + Bord('3'))
    Cell_13(Sub('4') + Bord('1') + Permut('0'), Sub('5') + Bord('5'))
    Cell_13(Sub('5') + Bord('3') + Permut('0'), Sub('6') + Bord('4'))
    Cell_13(Sub('6') + Bord('2') + Permut('0'), Sub('7') + Bord('3'))
    Cell_13(Sub('7') + Bord('1') + Permut('0'), Sub('8') + Bord('4'))
    Cell_13(Sub('8') + Bord('2') + Permut('0'), Sub('0') + Bord('4'))
    # edges adjacency constraints
    Cell_13(Bord('0') + Bord('1'), Bord('1') + Bord('0'))
    Cell_13(Bord('1') + Bord('1'), Bord('2') + Bord('0'))
    Cell_13(Bord('2') + Bord('1'), Bord('3') + Bord('0'))
    Cell_13(Bord('3') + Bord('1'), Bord('4') + Bord('0'))
    Cell_13(Bord('4') + Bord('1'), Bord('5') + Bord('0'))
    Cell_13(Bord('5') + Bord('1'), Bord('0') + Bord('0'))
    # incidence constraints
    Cell_14(Bord('0') + Sub('0'), Sub('0') + Bord('0'))
    Cell_14(Bord('0') + Sub('1'), Sub('1') + Bord('0'))
    Cell_14(Bord('1') + Sub('0'), Sub('1') + Bord('1'))
    Cell_14(Bord('1') + Sub('1'), Sub('2') + Bord('0'))
    Cell_14(Bord('1') + Sub('2'), Sub('3') + Bord('0'))
    Cell_14(Bord('2') + Sub('0'), Sub('3') + Bord('1'))
    Cell_14(Bord('2') + Sub('1'), Sub('4') + Bord('0'))
    Cell_14(Bord('3') + Sub('0'), Sub('4') + Bord('1'))
    Cell_14(Bord('3') + Sub('1'), Sub('5') + Bord('0'))
    Cell_14(Bord('3') + Sub('2'), Sub('6') + Bord('0'))
    Cell_14(Bord('4') + Sub('0'), Sub('6') + Bord('1'))
    # adjacency constraints
    Cell_14(Sub('0') + Bord('2') + Permut('0'), Sub('1') + Bord('4'))
    Cell_14(Sub('1') + Bord('2') + Permut('0'), Sub('2') + Bord('3'))
    Cell_14(Sub('2') + Bord('1') + Permut('0'), Sub('3') + Bord('5'))
    Cell_14(Sub('3') + Bord('3') + Permut('0'), Sub('4') + Bord('4'))
    Cell_14(Sub('4') + Bord('2') + Permut('0'), Sub('5') + Bord('3'))
    Cell_14(Sub('5') + Bord('1') + Permut('0'), Sub('6') + Bord('4'))
    Cell_14(Sub('6') + Bord('2') + Permut('0'), Sub('0') + Bord('4'))
    # edges adjacency constraints
    Cell_14(Bord('0') + Bord('1'), Bord('1') + Bord('0'))
    Cell_14(Bord('1') + Bord('1'), Bord('2') + Bord('0'))
    Cell_14(Bord('2') + Bord('1'), Bord('3') + Bord('0'))
    Cell_14(Bord('3') + Bord('1'), Bord('4') + Bord('0'))
    Cell_14(Bord('4') + Bord('1'), Bord('0') + Bord('0'))
    # incidence constraints
    Cell_15(Bord('0') + Sub('1'), Sub('0') + Bord('0'))
    Cell_15(Bord('0') + Sub('2'), Sub('1') + Bord('0'))
    Cell_15(Bord('1') + Sub('0'), Sub('1') + Bord('1'))
    Cell_15(Bord('1') + Sub('1'), Sub('2') + Bord('0'))
    Cell_15(Bord('1') + Sub('2'), Sub('3') + Bord('0'))
    Cell_15(Bord('2') + Sub('0'), Sub('3') + Bord('1'))
    Cell_15(Bord('2') + Sub('1'), Sub('4') + Bord('0'))
    Cell_15(Bord('2') + Sub('2'), Sub('5') + Bord('0'))
    Cell_15(Bord('3') + Sub('0'), Sub('5') + Bord('1'))
    Cell_15(Bord('3') + Sub('1'), Sub('6') + Bord('0'))
    Cell_15(Bord('4') + Sub('0'), Sub('6') + Bord('1'))
    Cell_15(Bord('4') + Sub('1'), Sub('7') + Bord('0'))
    Cell_15(Bord('4') + Sub('2'), Sub('8') + Bord('0'))
    Cell_15(Bord('0') + Sub('0'), Sub('8') + Bord('1'))
    # adjacency constraints
    Cell_15(Sub('0') + Bord('2') + Permut('0'), Sub('1') + Bord('4'))
    Cell_15(Sub('1') + Bord('2') + Permut('0'), Sub('2') + Bord('3'))
    Cell_15(Sub('2') + Bord('1') + Permut('0'), Sub('3') + Bord('4'))
    Cell_15(Sub('3') + Bord('2') + Permut('0'), Sub('4') + Bord('3'))
    Cell_15(Sub('4') + Bord('1') + Permut('0'), Sub('5') + Bord('5'))
    Cell_15(Sub('5') + Bord('3') + Permut('0'), Sub('6') + Bord('4'))
    Cell_15(Sub('6') + Bord('2') + Permut('0'), Sub('7') + Bord('3'))
    Cell_15(Sub('7') + Bord('1') + Permut('0'), Sub('8') + Bord('5'))
    Cell_15(Sub('8') + Bord('3') + Permut('0'), Sub('0') + Bord('4'))
    # edges adjacency constraints
    Cell_15(Bord('0') + Bord('1'), Bord('1') + Bord('0'))
    Cell_15(Bord('1') + Bord('1'), Bord('2') + Bord('0'))
    Cell_15(Bord('2') + Bord('1'), Bord('3') + Bord('0'))
    Cell_15(Bord('3') + Bord('1'), Bord('4') + Bord('0'))
    Cell_15(Bord('4') + Bord('1'), Bord('0') + Bord('0'))
    # incidence constraints
    Cell_16(Bord('0') + Sub('1'), Sub('0') + Bord('0'))
    Cell_16(Bord('0') + Sub('2'), Sub('1') + Bord('0'))
    Cell_16(Bord('1') + Sub('0'), Sub('1') + Bord('1'))
    Cell_16(Bord('1') + Sub('1'), Sub('2') + Bord('0'))
    Cell_16(Bord('1') + Sub('2'), Sub('3') + Bord('0'))
    Cell_16(Bord('2') + Sub('0'), Sub('3') + Bord('1'))
    Cell_16(Bord('2') + Sub('1'), Sub('4') + Bord('0'))
    Cell_16(Bord('2') + Sub('2'), Sub('5') + Bord('0'))
    Cell_16(Bord('3') + Sub('0'), Sub('5') + Bord('1'))
    Cell_16(Bord('3') + Sub('1'), Sub('6') + Bord('0'))
    Cell_16(Bord('4') + Sub('0'), Sub('6') + Bord('1'))
    Cell_16(Bord('4') + Sub('1'), Sub('7') + Bord('0'))
    Cell_16(Bord('4') + Sub('2'), Sub('8') + Bord('0'))
    Cell_16(Bord('0') + Sub('0'), Sub('8') + Bord('1'))
    # adjacency constraints
    Cell_16(Sub('0') + Bord('1') + Permut('0'), Sub('1') + Bord('4'))
    Cell_16(Sub('1') + Bord('2') + Permut('0'), Sub('2') + Bord('3'))
    Cell_16(Sub('2') + Bord('1') + Permut('0'), Sub('3') + Bord('4'))
    Cell_16(Sub('3') + Bord('2') + Permut('0'), Sub('4') + Bord('3'))
    Cell_16(Sub('4') + Bord('1') + Permut('0'), Sub('5') + Bord('5'))
    Cell_16(Sub('5') + Bord('3') + Permut('0'), Sub('6') + Bord('4'))
    Cell_16(Sub('6') + Bord('2') + Permut('0'), Sub('7') + Bord('3'))
    Cell_16(Sub('7') + Bord('1') + Permut('0'), Sub('8') + Bord('4'))
    Cell_16(Sub('8') + Bord('2') + Permut('0'), Sub('0') + Bord('3'))
    # edges adjacency constraints
    Cell_16(Bord('0') + Bord('1'), Bord('1') + Bord('0'))
    Cell_16(Bord('1') + Bord('1'), Bord('2') + Bord('0'))
    Cell_16(Bord('2') + Bord('1'), Bord('3') + Bord('0'))
    Cell_16(Bord('3') + Bord('1'), Bord('4') + Bord('0'))
    Cell_16(Bord('4') + Bord('1'), Bord('0') + Bord('0'))
    # incidence constraints
    Cell_17(Bord('0') + Sub('1'), Sub('0') + Bord('0'))
    Cell_17(Bord('0') + Sub('2'), Sub('1') + Bord('0'))
    Cell_17(Bord('1') + Sub('0'), Sub('1') + Bord('1'))
    Cell_17(Bord('1') + Sub('1'), Sub('2') + Bord('0'))
    Cell_17(Bord('1') + Sub('2'), Sub('3') + Bord('0'))
    Cell_17(Bord('2') + Sub('0'), Sub('4') + Bord('0'))
    Cell_17(Bord('3') + Sub('0'), Sub('4') + Bord('1'))
    Cell_17(Bord('3') + Sub('1'), Sub('5') + Bord('0'))
    Cell_17(Bord('3') + Sub('2'), Sub('6') + Bord('0'))
    Cell_17(Bord('4') + Sub('0'), Sub('6') + Bord('1'))
    Cell_17(Bord('4') + Sub('1'), Sub('7') + Bord('0'))
    Cell_17(Bord('5') + Sub('0'), Sub('7') + Bord('1'))
    Cell_17(Bord('5') + Sub('1'), Sub('8') + Bord('0'))
    Cell_17(Bord('5') + Sub('2'), Sub('9') + Bord('0'))
    Cell_17(Bord('0') + Sub('0'), Sub('9') + Bord('1'))
    # adjacency constraints
    Cell_17(Sub('0') + Bord('1') + Permut('0'), Sub('1') + Bord('5'))
    Cell_17(Sub('1') + Bord('3') + Permut('0'), Sub('2') + Bord('4'))
    Cell_17(Sub('2') + Bord('2') + Permut('0'), Sub('3') + Bord('3'))
    Cell_17(Sub('3') + Bord('1') + Permut('0'), Sub('4') + Bord('4'))
    Cell_17(Sub('4') + Bord('2') + Permut('0'), Sub('5') + Bord('3'))
    Cell_17(Sub('5') + Bord('1') + Permut('0'), Sub('6') + Bord('5'))
    Cell_17(Sub('6') + Bord('3') + Permut('0'), Sub('7') + Bord('4'))
    Cell_17(Sub('7') + Bord('2') + Permut('0'), Sub('8') + Bord('3'))
    Cell_17(Sub('8') + Bord('1') + Permut('0'), Sub('9') + Bord('4'))
    Cell_17(Sub('9') + Bord('2') + Permut('0'), Sub('0') + Bord('3'))
    # edges adjacency constraints
    Cell_17(Bord('0') + Bord('1'), Bord('1') + Bord('0'))
    Cell_17(Bord('1') + Bord('1'), Bord('2') + Bord('0'))
    Cell_17(Bord('2') + Bord('1'), Bord('3') + Bord('0'))
    Cell_17(Bord('3') + Bord('1'), Bord('4') + Bord('0'))
    Cell_17(Bord('4') + Bord('1'), Bord('5') + Bord('0'))
    Cell_17(Bord('5') + Bord('1'), Bord('0') + Bord('0'))
    # incidence constraints
    Cell_18(Bord('0') + Sub('0'), Sub('0') + Bord('0'))
    Cell_18(Bord('0') + Sub('1'), Sub('1') + Bord('0'))
    Cell_18(Bord('0') + Sub('2'), Sub('2') + Bord('0'))
    Cell_18(Bord('1') + Sub('0'), Sub('3') + Bord('0'))
    Cell_18(Bord('2') + Sub('0'), Sub('3') + Bord('1'))
    Cell_18(Bord('2') + Sub('1'), Sub('4') + Bord('0'))
    Cell_18(Bord('2') + Sub('2'), Sub('5') + Bord('0'))
    Cell_18(Bord('3') + Sub('0'), Sub('5') + Bord('1'))
    Cell_18(Bord('3') + Sub('1'), Sub('6') + Bord('0'))
    Cell_18(Bord('4') + Sub('0'), Sub('6') + Bord('1'))
    Cell_18(Bord('4') + Sub('1'), Sub('7') + Bord('0'))
    Cell_18(Bord('4') + Sub('2'), Sub('8') + Bord('0'))
    Cell_18(Bord('5') + Sub('0'), Sub('8') + Bord('1'))
    # adjacency constraints
    Cell_18(Sub('0') + Bord('2') + Permut('0'), Sub('1') + Bord('4'))
    Cell_18(Sub('1') + Bord('2') + Permut('0'), Sub('2') + Bord('3'))
    Cell_18(Sub('2') + Bord('1') + Permut('0'), Sub('3') + Bord('4'))
    Cell_18(Sub('3') + Bord('2') + Permut('0'), Sub('4') + Bord('3'))
    Cell_18(Sub('4') + Bord('1') + Permut('0'), Sub('5') + Bord('5'))
    Cell_18(Sub('5') + Bord('3') + Permut('0'), Sub('6') + Bord('4'))
    Cell_18(Sub('6') + Bord('2') + Permut('0'), Sub('7') + Bord('3'))
    Cell_18(Sub('7') + Bord('1') + Permut('0'), Sub('8') + Bord('4'))
    Cell_18(Sub('8') + Bord('2') + Permut('0'), Sub('0') + Bord('4'))
    # edges adjacency constraints
    Cell_18(Bord('0') + Bord('1'), Bord('1') + Bord('0'))
    Cell_18(Bord('1') + Bord('1'), Bord('2') + Bord('0'))
    Cell_18(Bord('2') + Bord('1'), Bord('3') + Bord('0'))
    Cell_18(Bord('3') + Bord('1'), Bord('4') + Bord('0'))
    Cell_18(Bord('4') + Bord('1'), Bord('5') + Bord('0'))
    Cell_18(Bord('5') + Bord('1'), Bord('0') + Bord('0'))
    # incidence constraints
    Cell_19(Bord('0') + Sub('0'), Sub('0') + Bord('0'))
    Cell_19(Bord('0') + Sub('1'), Sub('1') + Bord('0'))
    Cell_19(Bord('0') + Sub('2'), Sub('2') + Bord('0'))
    Cell_19(Bord('1') + Sub('0'), Sub('2') + Bord('1'))
    Cell_19(Bord('1') + Sub('1'), Sub('3') + Bord('0'))
    Cell_19(Bord('1') + Sub('2'), Sub('4') + Bord('0'))
    Cell_19(Bord('2') + Sub('0'), Sub('4') + Bord('1'))
    Cell_19(Bord('2') + Sub('1'), Sub('5') + Bord('0'))
    Cell_19(Bord('2') + Sub('2'), Sub('6') + Bord('0'))
    Cell_19(Bord('3') + Sub('0'), Sub('6') + Bord('1'))
    Cell_19(Bord('3') + Sub('1'), Sub('7') + Bord('0'))
    Cell_19(Bord('4') + Sub('0'), Sub('7') + Bord('1'))
    Cell_19(Bord('4') + Sub('1'), Sub('8') + Bord('0'))
    Cell_19(Bord('4') + Sub('2'), Sub('9') + Bord('0'))
    Cell_19(Bord('5') + Sub('0'), Sub('9') + Bord('1'))
    # adjacency constraints
    Cell_19(Sub('0') + Bord('2') + Permut('0'), Sub('1') + Bord('4'))
    Cell_19(Sub('1') + Bord('2') + Permut('0'), Sub('2') + Bord('4'))
    Cell_19(Sub('2') + Bord('2') + Permut('0'), Sub('3') + Bord('3'))
    Cell_19(Sub('3') + Bord('1') + Permut('0'), Sub('4') + Bord('4'))
    Cell_19(Sub('4') + Bord('2') + Permut('0'), Sub('5') + Bord('3'))
    Cell_19(Sub('5') + Bord('1') + Permut('0'), Sub('6') + Bord('5'))
    Cell_19(Sub('6') + Bord('3') + Permut('0'), Sub('7') + Bord('4'))
    Cell_19(Sub('7') + Bord('2') + Permut('0'), Sub('8') + Bord('3'))
    Cell_19(Sub('8') + Bord('1') + Permut('0'), Sub('9') + Bord('4'))
    Cell_19(Sub('9') + Bord('2') + Permut('0'), Sub('0') + Bord('4'))
    # edges adjacency constraints
    Cell_19(Bord('0') + Bord('1'), Bord('1') + Bord('0'))
    Cell_19(Bord('1') + Bord('1'), Bord('2') + Bord('0'))
    Cell_19(Bord('2') + Bord('1'), Bord('3') + Bord('0'))
    Cell_19(Bord('3') + Bord('1'), Bord('4') + Bord('0'))
    Cell_19(Bord('4') + Bord('1'), Bord('5') + Bord('0'))
    Cell_19(Bord('5') + Bord('1'), Bord('0') + Bord('0'))
    # incidence constraints
    Cell_20(Bord('0') + Sub('0'), Sub('0') + Bord('0'))
    Cell_20(Bord('0') + Sub('1'), Sub('1') + Bord('0'))
    Cell_20(Bord('0') + Sub('2'), Sub('2') + Bord('0'))
    Cell_20(Bord('1') + Sub('0'), Sub('2') + Bord('1'))
    Cell_20(Bord('1') + Sub('1'), Sub('3') + Bord('0'))
    Cell_20(Bord('1') + Sub('2'), Sub('4') + Bord('0'))
    Cell_20(Bord('2') + Sub('0'), Sub('4') + Bord('1'))
    Cell_20(Bord('2') + Sub('1'), Sub('5') + Bord('0'))
    Cell_20(Bord('3') + Sub('0'), Sub('5') + Bord('1'))
    Cell_20(Bord('3') + Sub('1'), Sub('6') + Bord('0'))
    Cell_20(Bord('3') + Sub('2'), Sub('7') + Bord('0'))
    Cell_20(Bord('4') + Sub('0'), Sub('7') + Bord('1'))
    # adjacency constraints
    Cell_20(Sub('0') + Bord('2') + Permut('0'), Sub('1') + Bord('4'))
    Cell_20(Sub('1') + Bord('2') + Permut('0'), Sub('2') + Bord('4'))
    Cell_20(Sub('2') + Bord('2') + Permut('0'), Sub('3') + Bord('3'))
    Cell_20(Sub('3') + Bord('1') + Permut('0'), Sub('4') + Bord('5'))
    Cell_20(Sub('4') + Bord('3') + Permut('0'), Sub('5') + Bord('4'))
    Cell_20(Sub('5') + Bord('2') + Permut('0'), Sub('6') + Bord('3'))
    Cell_20(Sub('6') + Bord('1') + Permut('0'), Sub('7') + Bord('4'))
    Cell_20(Sub('7') + Bord('2') + Permut('0'), Sub('0') + Bord('4'))
    # edges adjacency constraints
    Cell_20(Bord('0') + Bord('1'), Bord('1') + Bord('0'))
    Cell_20(Bord('1') + Bord('1'), Bord('2') + Bord('0'))
    Cell_20(Bord('2') + Bord('1'), Bord('3') + Bord('0'))
    Cell_20(Bord('3') + Bord('1'), Bord('4') + Bord('0'))
    Cell_20(Bord('4') + Bord('1'), Bord('0') + Bord('0'))
    # incidence constraints
    Cell_21(Bord('0') + Sub('1'), Sub('0') + Bord('0'))
    Cell_21(Bord('0') + Sub('2'), Sub('1') + Bord('0'))
    Cell_21(Bord('1') + Sub('0'), Sub('2') + Bord('0'))
    Cell_21(Bord('2') + Sub('0'), Sub('2') + Bord('1'))
    Cell_21(Bord('2') + Sub('1'), Sub('3') + Bord('0'))
    Cell_21(Bord('2') + Sub('2'), Sub('4') + Bord('0'))
    Cell_21(Bord('3') + Sub('0'), Sub('4') + Bord('1'))
    Cell_21(Bord('3') + Sub('1'), Sub('5') + Bord('0'))
    Cell_21(Bord('4') + Sub('0'), Sub('5') + Bord('1'))
    Cell_21(Bord('4') + Sub('1'), Sub('6') + Bord('0'))
    Cell_21(Bord('4') + Sub('2'), Sub('7') + Bord('0'))
    Cell_21(Bord('0') + Sub('0'), Sub('7') + Bord('1'))
    # adjacency constraints
    Cell_21(Sub('0') + Bord('2') + Permut('0'), Sub('1') + Bord('3'))
    Cell_21(Sub('1') + Bord('1') + Permut('0'), Sub('2') + Bord('4'))
    Cell_21(Sub('2') + Bord('2') + Permut('0'), Sub('3') + Bord('3'))
    Cell_21(Sub('3') + Bord('1') + Permut('0'), Sub('4') + Bord('5'))
    Cell_21(Sub('4') + Bord('3') + Permut('0'), Sub('5') + Bord('4'))
    Cell_21(Sub('5') + Bord('2') + Permut('0'), Sub('6') + Bord('3'))
    Cell_21(Sub('6') + Bord('1') + Permut('0'), Sub('7') + Bord('5'))
    Cell_21(Sub('7') + Bord('3') + Permut('0'), Sub('0') + Bord('4'))
    # edges adjacency constraints
    Cell_21(Bord('0') + Bord('1'), Bord('1') + Bord('0'))
    Cell_21(Bord('1') + Bord('1'), Bord('2') + Bord('0'))
    Cell_21(Bord('2') + Bord('1'), Bord('3') + Bord('0'))
    Cell_21(Bord('3') + Bord('1'), Bord('4') + Bord('0'))
    Cell_21(Bord('4') + Bord('1'), Bord('0') + Bord('0'))
    # constraints on init cells
    # control points
    init.initMat[Sub_('0')] = FMat([
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]).setTyp('Var')
    for i in range(init.initMat[Sub_('0')].n):
        init.initMat[Sub_('0')][2, i].setTyp('Const')

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
