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
    B3_1 = Etat('B3_1', 1)
    B3_1.bords = {Bord('0'): s, Bord('1'): s}
    B3_1.permuts = {Permut('0'): B3_1}
    B3 = Etat('B3', 1)
    B3.bords = {Bord('0'): s, Bord('1'): s}
    B3.permuts = {Permut('0'): B3}
    B2_1 = Etat('B2_1', 1)
    B2_1.bords = {Bord('0'): s, Bord('1'): s}
    B2_1.permuts = {Permut('0'): B2_1}
    B2_2 = Etat('B2_2', 1)
    B2_2.bords = {Bord('0'): s, Bord('1'): s}
    B2_2.permuts = {Permut('0'): B2_2}
    B2 = Etat('B2', 1)
    B2.bords = {Bord('0'): s, Bord('1'): s}
    B2.permuts = {Permut('0'): B2}
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
    B3_1.subs = {Sub('0'): B3}
    B3_1.buildIntern()
    B3_1.space = [Bord_('0'), Intern_(''), Bord_('1')]
    B3_1(Permut('0') + Bord('0'), Bord('1'))
    B3_1(Permut('0') + Bord('1'), Bord('0'))
    B3_1(Permut('0') + Intern(''), Intern(''))
    B3_1(Permut('0') + Sub('0'), Sub('0') + Permut('0'))
    B3_1(Bord('0') + Sub('0'), Sub('0') + Bord('0'))
    B3_1(Bord('1') + Sub('0'), Sub('0') + Bord('1'))
    B3_1.grid.elems = [Figure(1, [Bord_('0'), Intern_(''), Bord_('1')])]
    B3_1.prim.elems = [Figure(1, [Bord_('0'), Bord_('1')])]
    B3_1.initMat[Sub_('0') + Intern('')] = FMat([
        [0.0],
        [1.0],
        [0.0]]).setTyp('Const')
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
    # Cell_0_2 : [C_2_0, C_2_0, C_2_0], adj, gap, req edges are B_2_1 B_2_2 B_3_1 
    Cell_0_2 = Etat('Cell_0_2', 0)
    # Cell_1_1 : [C_2_0, B_3_1, B_3_1, C_2_0, C_2_0, B_3_1, B_3_1, C_2_0, C_2_0, B_3_1, B_3_1, C_2_0], adj, gap, req edges are B_2_1 B_2_2 B_3_1 
    Cell_1_1 = Etat('Cell_1_1', 0)
    # Cell_2 : [C_2_0, B_3_1, B_3_1, C_2_0, B_3_0, B_3_0, C_2_0, B_3_1, B_3_1, C_2_0, C_2_0, B_3_1, B_3_1, C_2_0, B_3_0, B_3_0, C_2_0, B_3_1, B_3_1, C_2_0, C_2_0, B_3_1, B_3_1, C_2_0, B_3_0, B_3_0, C_2_0, B_3_1, B_3_1, C_2_0], adj, gap, req edges are B_2_1 B_2_2 B_3_1 
    Cell_2 = Etat('Cell_2', 0)
    # Cell_3 : [C_2_0, B_2_1, B_2_2, B_2_1, B_3_1], adj, gap, req edges are B_2_1 B_2_2 B_3_1 
    Cell_3 = Etat('Cell_3', 0)
    # Cell_4 : [B_3_0, B_2_1, B_2_2, B_2_1], adj, gap, req edges are B_2_1 B_2_2 B_3_1 
    Cell_4 = Etat('Cell_4', 0)
    # Cell_5 : [C_2_0, B_3_1, B_2_1, B_2_2, B_2_1], adj, gap, req edges are B_2_1 B_2_2 B_3_1 
    Cell_5 = Etat('Cell_5', 0)
    # Cell_6 : [C_2_0, B_3_0, B_2_1, B_2_2, B_2_1, B_3_1], adj, gap, req edges are B_2_1 B_2_2 B_3_1 
    Cell_6 = Etat('Cell_6', 0)
    # Cell_7 : [B_3_0, B_3_0, B_2_1, B_2_2, B_2_1], adj, gap, req edges are B_2_1 B_2_2 B_3_1 
    Cell_7 = Etat('Cell_7', 0)
    # Cell_8 : [B_3_0, C_2_0, B_3_1, B_2_1, B_2_2, B_2_1], adj, gap, req edges are B_2_1 B_2_2 B_3_1 
    Cell_8 = Etat('Cell_8', 0)
    # Cell_9 : [C_2_0, C_2_0, B_3_1, B_2_1, B_2_2, B_2_1, B_3_1], adj, gap, req edges are B_2_1 B_2_2 B_3_1 
    Cell_9 = Etat('Cell_9', 0)
    # Cell_10 : [B_2_0, B_2_1, B_2_2, B_2_1], adj, gap, req edges are B_2_1 B_2_2 B_3_1 
    Cell_10 = Etat('Cell_10', 0)
    # Cell_11 : [B_2_1, B_2_1, B_2_2, B_2_1], adj, gap, req edges are B_2_1 B_2_2 B_3_1 
    Cell_11 = Etat('Cell_11', 0)
    ##############################
    # subd of init
    init.subs = {Sub('0'): Cell_0_2}
    ##############################
    # edges of all states
    Cell_0_2.bords = {Bord('0'): C2, Bord('1'): C2, Bord('2'): C2}
    Cell_1_1.bords = {Bord('0'): C2, Bord('1'): B3_1, Bord('2'): B3_1, Bord('3'): C2, Bord('4'): C2, Bord('5'): B3_1, Bord('6'): B3_1, Bord('7'): C2, Bord('8'): C2, Bord('9'): B3_1, Bord('10'): B3_1, Bord('11'): C2}
    Cell_2.bords = {Bord('0'): C2, Bord('1'): B3_1, Bord('2'): B3_1, Bord('3'): C2, Bord('4'): B3, Bord('5'): B3, Bord('6'): C2, Bord('7'): B3_1, Bord('8'): B3_1, Bord('9'): C2, Bord('10'): C2, Bord('11'): B3_1, Bord('12'): B3_1, Bord('13'): C2, Bord('14'): B3, Bord('15'): B3, Bord('16'): C2, Bord('17'): B3_1, Bord('18'): B3_1, Bord('19'): C2, Bord('20'): C2, Bord('21'): B3_1, Bord('22'): B3_1, Bord('23'): C2, Bord('24'): B3, Bord('25'): B3, Bord('26'): C2, Bord('27'): B3_1, Bord('28'): B3_1, Bord('29'): C2}
    Cell_3.bords = {Bord('0'): C2, Bord('1'): B2_1, Bord('2'): B2_2, Bord('3'): B2_1, Bord('4'): B3_1}
    Cell_4.bords = {Bord('0'): B3, Bord('1'): B2_1, Bord('2'): B2_2, Bord('3'): B2_1}
    Cell_5.bords = {Bord('0'): C2, Bord('1'): B3_1, Bord('2'): B2_1, Bord('3'): B2_2, Bord('4'): B2_1}
    Cell_6.bords = {Bord('0'): C2, Bord('1'): B3, Bord('2'): B2_1, Bord('3'): B2_2, Bord('4'): B2_1, Bord('5'): B3_1}
    Cell_7.bords = {Bord('0'): B3, Bord('1'): B3, Bord('2'): B2_1, Bord('3'): B2_2, Bord('4'): B2_1}
    Cell_8.bords = {Bord('0'): B3, Bord('1'): C2, Bord('2'): B3_1, Bord('3'): B2_1, Bord('4'): B2_2, Bord('5'): B2_1}
    Cell_9.bords = {Bord('0'): C2, Bord('1'): C2, Bord('2'): B3_1, Bord('3'): B2_1, Bord('4'): B2_2, Bord('5'): B2_1, Bord('6'): B3_1}
    Cell_10.bords = {Bord('0'): B2, Bord('1'): B2_1, Bord('2'): B2_2, Bord('3'): B2_1}
    Cell_11.bords = {Bord('0'): B2_1, Bord('1'): B2_1, Bord('2'): B2_2, Bord('3'): B2_1}
    ##############################
    # subdivisions of all states
    Cell_0_2.subs = {Sub('0'): Cell_1_1}
    Cell_1_1.subs = {Sub('0'): Cell_2}
    Cell_2.subs = {Sub('0'): Cell_3, Sub('1'): Cell_4, Sub('2'): Cell_4, Sub('3'): Cell_5, Sub('4'): Cell_6, Sub('5'): Cell_4, Sub('6'): Cell_7, Sub('7'): Cell_4, Sub('8'): Cell_8, Sub('9'): Cell_3, Sub('10'): Cell_4, Sub('11'): Cell_4, Sub('12'): Cell_5, Sub('13'): Cell_9, Sub('14'): Cell_3, Sub('15'): Cell_4, Sub('16'): Cell_4, Sub('17'): Cell_5, Sub('18'): Cell_6, Sub('19'): Cell_4, Sub('20'): Cell_7, Sub('21'): Cell_4, Sub('22'): Cell_8, Sub('23'): Cell_3, Sub('24'): Cell_4, Sub('25'): Cell_4, Sub('26'): Cell_5, Sub('27'): Cell_9, Sub('28'): Cell_3, Sub('29'): Cell_4, Sub('30'): Cell_4, Sub('31'): Cell_5, Sub('32'): Cell_6, Sub('33'): Cell_4, Sub('34'): Cell_7, Sub('35'): Cell_4, Sub('36'): Cell_8, Sub('37'): Cell_3, Sub('38'): Cell_4, Sub('39'): Cell_4, Sub('40'): Cell_5, Sub('41'): Cell_9}
    Cell_3.subs = {Sub('0'): Cell_5, Sub('1'): Cell_3, Sub('2'): Cell_10, Sub('3'): Cell_11, Sub('4'): Cell_10, Sub('5'): Cell_4}
    Cell_4.subs = {Sub('0'): Cell_4, Sub('1'): Cell_4, Sub('2'): Cell_4, Sub('3'): Cell_10, Sub('4'): Cell_11, Sub('5'): Cell_10}
    Cell_5.subs = {Sub('0'): Cell_5, Sub('1'): Cell_3, Sub('2'): Cell_4, Sub('3'): Cell_10, Sub('4'): Cell_11, Sub('5'): Cell_10}
    Cell_6.subs = {Sub('0'): Cell_5, Sub('1'): Cell_6, Sub('2'): Cell_4, Sub('3'): Cell_4, Sub('4'): Cell_10, Sub('5'): Cell_11, Sub('6'): Cell_10, Sub('7'): Cell_4}
    Cell_7.subs = {Sub('0'): Cell_4, Sub('1'): Cell_4, Sub('2'): Cell_7, Sub('3'): Cell_4, Sub('4'): Cell_4, Sub('5'): Cell_10, Sub('6'): Cell_11, Sub('7'): Cell_10}
    Cell_8.subs = {Sub('0'): Cell_4, Sub('1'): Cell_4, Sub('2'): Cell_8, Sub('3'): Cell_3, Sub('4'): Cell_4, Sub('5'): Cell_10, Sub('6'): Cell_11, Sub('7'): Cell_10}
    Cell_9.subs = {Sub('0'): Cell_5, Sub('1'): Cell_9, Sub('2'): Cell_3, Sub('3'): Cell_4, Sub('4'): Cell_10, Sub('5'): Cell_11, Sub('6'): Cell_10, Sub('7'): Cell_4}
    Cell_10.subs = {Sub('0'): Cell_10, Sub('1'): Cell_10, Sub('2'): Cell_10, Sub('3'): Cell_11, Sub('4'): Cell_10}
    Cell_11.subs = {Sub('0'): Cell_10, Sub('1'): Cell_10, Sub('2'): Cell_11, Sub('3'): Cell_10}
    ##############################
    # build intern of all states
    Cell_0_2.buildIntern()
    Cell_1_1.buildIntern()
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
    ##############################
    # spaces of all states
    Cell_0_2.space = [Bord_('0'), Bord_('1'), Bord_('2')]
    Cell_1_1.space = [Bord_('0'), Bord_('1'), Bord_('2'), Bord_('3'), Bord_('4'), Bord_('5'), Bord_('6'), Bord_('7'), Bord_('8'), Bord_('9'), Bord_('10'), Bord_('11')]
    Cell_2.space = [Bord_('0'), Bord_('1'), Bord_('2'), Bord_('3'), Bord_('4'), Bord_('5'), Bord_('6'), Bord_('7'), Bord_('8'), Bord_('9'), Bord_('10'), Bord_('11'), Bord_('12'), Bord_('13'), Bord_('14'), Bord_('15'), Bord_('16'), Bord_('17'), Bord_('18'), Bord_('19'), Bord_('20'), Bord_('21'), Bord_('22'), Bord_('23'), Bord_('24'), Bord_('25'), Bord_('26'), Bord_('27'), Bord_('28'), Bord_('29')]
    Cell_3.space = [Bord_('0'), Bord_('1'), Bord_('2'), Bord_('3'), Bord_('4')]
    Cell_4.space = [Bord_('0'), Bord_('1'), Bord_('2'), Bord_('3')]
    Cell_5.space = [Bord_('0'), Bord_('1'), Bord_('2'), Bord_('3'), Bord_('4')]
    Cell_6.space = [Bord_('0'), Bord_('1'), Bord_('2'), Bord_('3'), Bord_('4'), Bord_('5')]
    Cell_7.space = [Bord_('0'), Bord_('1'), Bord_('2'), Bord_('3'), Bord_('4')]
    Cell_8.space = [Bord_('0'), Bord_('1'), Bord_('2'), Bord_('3'), Bord_('4'), Bord_('5')]
    Cell_9.space = [Bord_('0'), Bord_('1'), Bord_('2'), Bord_('3'), Bord_('4'), Bord_('5'), Bord_('6')]
    Cell_10.space = [Bord_('0'), Bord_('1'), Bord_('2'), Bord_('3')]
    Cell_11.space = [Bord_('0'), Bord_('1'), Bord_('2'), Bord_('3')]
    ##############################
    # grid of all states
    Cell_0_2.addGrid(Bord)
    Cell_1_1.addGrid(Bord)
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
    ##############################
    # prim of all states
    Cell_0_2.prim.elems = [Figure(2, [Bord_('0') + Bord('0'), Bord_('1') + Bord('0'), Bord_('2') + Bord('0')])]
    Cell_1_1.prim.elems = [Figure(2, [Bord_('0') + Bord('0'), Bord_('1') + Bord('0'), Bord_('2') + Bord('0'), Bord_('3') + Bord('0'), Bord_('4') + Bord('0'), Bord_('5') + Bord('0'), Bord_('6') + Bord('0'), Bord_('7') + Bord('0'), Bord_('8') + Bord('0'), Bord_('9') + Bord('0'), Bord_('10') + Bord('0'), Bord_('11') + Bord('0')])]
    Cell_2.prim.elems = [Figure(2, [Bord_('0') + Bord('0'), Bord_('1') + Bord('0'), Bord_('2') + Bord('0'), Bord_('3') + Bord('0'), Bord_('4') + Sub('0') + Sub('0') + Bord('0'), Bord_('4') + Sub('0') + Sub('1') + Bord('0'), Bord_('4') + Sub('1') + Sub('0') + Bord('0'), Bord_('4') + Sub('1') + Sub('1') + Bord('0'), Bord_('5') + Sub('0') + Sub('0') + Bord('0'), Bord_('5') + Sub('0') + Sub('1') + Bord('0'), Bord_('5') + Sub('1') + Sub('0') + Bord('0'), Bord_('5') + Sub('1') + Sub('1') + Bord('0'), Bord_('6') + Bord('0'), Bord_('7') + Bord('0'), Bord_('8') + Bord('0'), Bord_('9') + Bord('0'), Bord_('10') + Bord('0'), Bord_('11') + Bord('0'), Bord_('12') + Bord('0'), Bord_('13') + Bord('0'), Bord_('14') + Sub('0') + Sub('0') + Bord('0'), Bord_('14') + Sub('0') + Sub('1') + Bord('0'), Bord_('14') + Sub('1') + Sub('0') + Bord('0'), Bord_('14') + Sub('1') + Sub('1') + Bord('0'), Bord_('15') + Sub('0') + Sub('0') + Bord('0'), Bord_('15') + Sub('0') + Sub('1') + Bord('0'), Bord_('15') + Sub('1') + Sub('0') + Bord('0'), Bord_('15') + Sub('1') + Sub('1') + Bord('0'), Bord_('16') + Bord('0'), Bord_('17') + Bord('0'), Bord_('18') + Bord('0'), Bord_('19') + Bord('0'), Bord_('20') + Bord('0'), Bord_('21') + Bord('0'), Bord_('22') + Bord('0'), Bord_('23') + Bord('0'), Bord_('24') + Sub('0') + Sub('0') + Bord('0'), Bord_('24') + Sub('0') + Sub('1') + Bord('0'), Bord_('24') + Sub('1') + Sub('0') + Bord('0'), Bord_('24') + Sub('1') + Sub('1') + Bord('0'), Bord_('25') + Sub('0') + Sub('0') + Bord('0'), Bord_('25') + Sub('0') + Sub('1') + Bord('0'), Bord_('25') + Sub('1') + Sub('0') + Bord('0'), Bord_('25') + Sub('1') + Sub('1') + Bord('0'), Bord_('26') + Bord('0'), Bord_('27') + Bord('0'), Bord_('28') + Bord('0'), Bord_('29') + Bord('0')])]
    Cell_3.prim.elems = [Figure(2, [Bord_('0') + Bord('0'), Bord_('1') + Bord('0'), Bord_('2') + Bord('0'), Bord_('3') + Bord('0'), Bord_('4') + Bord('0')])]
    Cell_4.prim.elems = [Figure(2, [Bord_('0') + Sub('0') + Sub('0') + Bord('0'), Bord_('0') + Sub('0') + Sub('1') + Bord('0'), Bord_('0') + Sub('1') + Sub('0') + Bord('0'), Bord_('0') + Sub('1') + Sub('1') + Bord('0'), Bord_('1') + Bord('0'), Bord_('2') + Bord('0'), Bord_('3') + Bord('0')])]
    Cell_5.prim.elems = [Figure(2, [Bord_('0') + Bord('0'), Bord_('1') + Bord('0'), Bord_('2') + Bord('0'), Bord_('3') + Bord('0'), Bord_('4') + Bord('0')])]
    Cell_6.prim.elems = [Figure(2, [Bord_('0') + Bord('0'), Bord_('1') + Sub('0') + Sub('0') + Bord('0'), Bord_('1') + Sub('0') + Sub('1') + Bord('0'), Bord_('1') + Sub('1') + Sub('0') + Bord('0'), Bord_('1') + Sub('1') + Sub('1') + Bord('0'), Bord_('2') + Bord('0'), Bord_('3') + Bord('0'), Bord_('4') + Bord('0'), Bord_('5') + Bord('0')])]
    Cell_7.prim.elems = [Figure(2, [Bord_('0') + Sub('0') + Sub('0') + Bord('0'), Bord_('0') + Sub('0') + Sub('1') + Bord('0'), Bord_('0') + Sub('1') + Sub('0') + Bord('0'), Bord_('0') + Sub('1') + Sub('1') + Bord('0'), Bord_('1') + Sub('0') + Sub('0') + Bord('0'), Bord_('1') + Sub('0') + Sub('1') + Bord('0'), Bord_('1') + Sub('1') + Sub('0') + Bord('0'), Bord_('1') + Sub('1') + Sub('1') + Bord('0'), Bord_('2') + Bord('0'), Bord_('3') + Bord('0'), Bord_('4') + Bord('0')])]
    Cell_8.prim.elems = [Figure(2, [Bord_('0') + Sub('0') + Sub('0') + Bord('0'), Bord_('0') + Sub('0') + Sub('1') + Bord('0'), Bord_('0') + Sub('1') + Sub('0') + Bord('0'), Bord_('0') + Sub('1') + Sub('1') + Bord('0'), Bord_('1') + Bord('0'), Bord_('2') + Bord('0'), Bord_('3') + Bord('0'), Bord_('4') + Bord('0'), Bord_('5') + Bord('0')])]
    Cell_9.prim.elems = [Figure(2, [Bord_('0') + Bord('0'), Bord_('1') + Bord('0'), Bord_('2') + Bord('0'), Bord_('3') + Bord('0'), Bord_('4') + Bord('0'), Bord_('5') + Bord('0'), Bord_('6') + Bord('0')])]
    Cell_10.prim.elems = [Figure(2, [Bord_('0') + Sub('0') + Sub('0') + Bord('0'), Bord_('0') + Sub('0') + Sub('1') + Bord('0'), Bord_('0') + Sub('1') + Sub('0') + Bord('0'), Bord_('0') + Sub('1') + Sub('1') + Bord('0'), Bord_('1') + Bord('0'), Bord_('2') + Bord('0'), Bord_('3') + Bord('0')])]
    Cell_11.prim.elems = [Figure(2, [Bord_('0') + Bord('0'), Bord_('1') + Bord('0'), Bord_('2') + Bord('0'), Bord_('3') + Bord('0')])]
    ##############################
    # constraints of all states
    # incidence constraints
    Cell_0_2(Bord('0') + Sub('0'), Sub('0') + Bord('0'))
    Cell_0_2(Bord('0') + Sub('1'), Sub('0') + Bord('3'))
    Cell_0_2(Bord('1') + Sub('0'), Sub('0') + Bord('4'))
    Cell_0_2(Bord('1') + Sub('1'), Sub('0') + Bord('7'))
    Cell_0_2(Bord('2') + Sub('0'), Sub('0') + Bord('8'))
    Cell_0_2(Bord('2') + Sub('1'), Sub('0') + Bord('11'))
    # adjacency constraints
    # edges adjacency constraints
    Cell_0_2(Bord('0') + Bord('1'), Bord('1') + Bord('0'))
    Cell_0_2(Bord('1') + Bord('1'), Bord('2') + Bord('0'))
    Cell_0_2(Bord('2') + Bord('1'), Bord('0') + Bord('0'))
    # incidence constraints
    Cell_1_1(Bord('0') + Sub('0'), Sub('0') + Bord('0'))
    Cell_1_1(Bord('0') + Sub('1'), Sub('0') + Bord('3'))
    Cell_1_1(Bord('1') + Sub('0'), Sub('0') + Bord('4'))
    Cell_1_1(Bord('2') + Sub('0'), Sub('0') + Bord('5'))
    Cell_1_1(Bord('3') + Sub('0'), Sub('0') + Bord('6'))
    Cell_1_1(Bord('3') + Sub('1'), Sub('0') + Bord('9'))
    Cell_1_1(Bord('4') + Sub('0'), Sub('0') + Bord('10'))
    Cell_1_1(Bord('4') + Sub('1'), Sub('0') + Bord('13'))
    Cell_1_1(Bord('5') + Sub('0'), Sub('0') + Bord('14'))
    Cell_1_1(Bord('6') + Sub('0'), Sub('0') + Bord('15'))
    Cell_1_1(Bord('7') + Sub('0'), Sub('0') + Bord('16'))
    Cell_1_1(Bord('7') + Sub('1'), Sub('0') + Bord('19'))
    Cell_1_1(Bord('8') + Sub('0'), Sub('0') + Bord('20'))
    Cell_1_1(Bord('8') + Sub('1'), Sub('0') + Bord('23'))
    Cell_1_1(Bord('9') + Sub('0'), Sub('0') + Bord('24'))
    Cell_1_1(Bord('10') + Sub('0'), Sub('0') + Bord('25'))
    Cell_1_1(Bord('11') + Sub('0'), Sub('0') + Bord('26'))
    Cell_1_1(Bord('11') + Sub('1'), Sub('0') + Bord('29'))
    # adjacency constraints
    # edges adjacency constraints
    Cell_1_1(Bord('0') + Bord('1'), Bord('1') + Bord('0'))
    Cell_1_1(Bord('1') + Bord('1'), Bord('2') + Bord('0'))
    Cell_1_1(Bord('2') + Bord('1'), Bord('3') + Bord('0'))
    Cell_1_1(Bord('3') + Bord('1'), Bord('4') + Bord('0'))
    Cell_1_1(Bord('4') + Bord('1'), Bord('5') + Bord('0'))
    Cell_1_1(Bord('5') + Bord('1'), Bord('6') + Bord('0'))
    Cell_1_1(Bord('6') + Bord('1'), Bord('7') + Bord('0'))
    Cell_1_1(Bord('7') + Bord('1'), Bord('8') + Bord('0'))
    Cell_1_1(Bord('8') + Bord('1'), Bord('9') + Bord('0'))
    Cell_1_1(Bord('9') + Bord('1'), Bord('10') + Bord('0'))
    Cell_1_1(Bord('10') + Bord('1'), Bord('11') + Bord('0'))
    Cell_1_1(Bord('11') + Bord('1'), Bord('0') + Bord('0'))
    # incidence constraints
    Cell_2(Bord('0') + Sub('1'), Sub('0') + Bord('0'))
    Cell_2(Bord('1') + Sub('0'), Sub('1') + Bord('0'))
    Cell_2(Bord('2') + Sub('0'), Sub('2') + Bord('0'))
    Cell_2(Bord('3') + Sub('0'), Sub('3') + Bord('0'))
    Cell_2(Bord('3') + Sub('1'), Sub('4') + Bord('0'))
    Cell_2(Bord('4') + Sub('0'), Sub('4') + Bord('1'))
    Cell_2(Bord('4') + Sub('1'), Sub('5') + Bord('0'))
    Cell_2(Bord('4') + Sub('2'), Sub('6') + Bord('0'))
    Cell_2(Bord('5') + Sub('0'), Sub('6') + Bord('1'))
    Cell_2(Bord('5') + Sub('1'), Sub('7') + Bord('0'))
    Cell_2(Bord('5') + Sub('2'), Sub('8') + Bord('0'))
    Cell_2(Bord('6') + Sub('0'), Sub('8') + Bord('1'))
    Cell_2(Bord('6') + Sub('1'), Sub('9') + Bord('0'))
    Cell_2(Bord('7') + Sub('0'), Sub('10') + Bord('0'))
    Cell_2(Bord('8') + Sub('0'), Sub('11') + Bord('0'))
    Cell_2(Bord('9') + Sub('0'), Sub('12') + Bord('0'))
    Cell_2(Bord('9') + Sub('1'), Sub('13') + Bord('0'))
    Cell_2(Bord('10') + Sub('0'), Sub('13') + Bord('1'))
    Cell_2(Bord('10') + Sub('1'), Sub('14') + Bord('0'))
    Cell_2(Bord('11') + Sub('0'), Sub('15') + Bord('0'))
    Cell_2(Bord('12') + Sub('0'), Sub('16') + Bord('0'))
    Cell_2(Bord('13') + Sub('0'), Sub('17') + Bord('0'))
    Cell_2(Bord('13') + Sub('1'), Sub('18') + Bord('0'))
    Cell_2(Bord('14') + Sub('0'), Sub('18') + Bord('1'))
    Cell_2(Bord('14') + Sub('1'), Sub('19') + Bord('0'))
    Cell_2(Bord('14') + Sub('2'), Sub('20') + Bord('0'))
    Cell_2(Bord('15') + Sub('0'), Sub('20') + Bord('1'))
    Cell_2(Bord('15') + Sub('1'), Sub('21') + Bord('0'))
    Cell_2(Bord('15') + Sub('2'), Sub('22') + Bord('0'))
    Cell_2(Bord('16') + Sub('0'), Sub('22') + Bord('1'))
    Cell_2(Bord('16') + Sub('1'), Sub('23') + Bord('0'))
    Cell_2(Bord('17') + Sub('0'), Sub('24') + Bord('0'))
    Cell_2(Bord('18') + Sub('0'), Sub('25') + Bord('0'))
    Cell_2(Bord('19') + Sub('0'), Sub('26') + Bord('0'))
    Cell_2(Bord('19') + Sub('1'), Sub('27') + Bord('0'))
    Cell_2(Bord('20') + Sub('0'), Sub('27') + Bord('1'))
    Cell_2(Bord('20') + Sub('1'), Sub('28') + Bord('0'))
    Cell_2(Bord('21') + Sub('0'), Sub('29') + Bord('0'))
    Cell_2(Bord('22') + Sub('0'), Sub('30') + Bord('0'))
    Cell_2(Bord('23') + Sub('0'), Sub('31') + Bord('0'))
    Cell_2(Bord('23') + Sub('1'), Sub('32') + Bord('0'))
    Cell_2(Bord('24') + Sub('0'), Sub('32') + Bord('1'))
    Cell_2(Bord('24') + Sub('1'), Sub('33') + Bord('0'))
    Cell_2(Bord('24') + Sub('2'), Sub('34') + Bord('0'))
    Cell_2(Bord('25') + Sub('0'), Sub('34') + Bord('1'))
    Cell_2(Bord('25') + Sub('1'), Sub('35') + Bord('0'))
    Cell_2(Bord('25') + Sub('2'), Sub('36') + Bord('0'))
    Cell_2(Bord('26') + Sub('0'), Sub('36') + Bord('1'))
    Cell_2(Bord('26') + Sub('1'), Sub('37') + Bord('0'))
    Cell_2(Bord('27') + Sub('0'), Sub('38') + Bord('0'))
    Cell_2(Bord('28') + Sub('0'), Sub('39') + Bord('0'))
    Cell_2(Bord('29') + Sub('0'), Sub('40') + Bord('0'))
    Cell_2(Bord('29') + Sub('1'), Sub('41') + Bord('0'))
    Cell_2(Bord('0') + Sub('0'), Sub('41') + Bord('1'))
    # adjacency constraints
    Cell_2(Sub('0') + Bord('1') + Permut('0'), Sub('1') + Bord('3'))
    Cell_2(Sub('1') + Bord('1') + Permut('0'), Sub('2') + Bord('3'))
    Cell_2(Sub('2') + Bord('1') + Permut('0'), Sub('3') + Bord('4'))
    Cell_2(Sub('3') + Bord('2') + Permut('0'), Sub('4') + Bord('4'))
    Cell_2(Sub('4') + Bord('2') + Permut('0'), Sub('5') + Bord('3'))
    Cell_2(Sub('5') + Bord('1') + Permut('0'), Sub('6') + Bord('4'))
    Cell_2(Sub('6') + Bord('2') + Permut('0'), Sub('7') + Bord('3'))
    Cell_2(Sub('7') + Bord('1') + Permut('0'), Sub('8') + Bord('5'))
    Cell_2(Sub('8') + Bord('3') + Permut('0'), Sub('9') + Bord('3'))
    Cell_2(Sub('9') + Bord('1') + Permut('0'), Sub('10') + Bord('3'))
    Cell_2(Sub('10') + Bord('1') + Permut('0'), Sub('11') + Bord('3'))
    Cell_2(Sub('11') + Bord('1') + Permut('0'), Sub('12') + Bord('4'))
    Cell_2(Sub('12') + Bord('2') + Permut('0'), Sub('13') + Bord('5'))
    Cell_2(Sub('13') + Bord('3') + Permut('0'), Sub('14') + Bord('3'))
    Cell_2(Sub('14') + Bord('1') + Permut('0'), Sub('15') + Bord('3'))
    Cell_2(Sub('15') + Bord('1') + Permut('0'), Sub('16') + Bord('3'))
    Cell_2(Sub('16') + Bord('1') + Permut('0'), Sub('17') + Bord('4'))
    Cell_2(Sub('17') + Bord('2') + Permut('0'), Sub('18') + Bord('4'))
    Cell_2(Sub('18') + Bord('2') + Permut('0'), Sub('19') + Bord('3'))
    Cell_2(Sub('19') + Bord('1') + Permut('0'), Sub('20') + Bord('4'))
    Cell_2(Sub('20') + Bord('2') + Permut('0'), Sub('21') + Bord('3'))
    Cell_2(Sub('21') + Bord('1') + Permut('0'), Sub('22') + Bord('5'))
    Cell_2(Sub('22') + Bord('3') + Permut('0'), Sub('23') + Bord('3'))
    Cell_2(Sub('23') + Bord('1') + Permut('0'), Sub('24') + Bord('3'))
    Cell_2(Sub('24') + Bord('1') + Permut('0'), Sub('25') + Bord('3'))
    Cell_2(Sub('25') + Bord('1') + Permut('0'), Sub('26') + Bord('4'))
    Cell_2(Sub('26') + Bord('2') + Permut('0'), Sub('27') + Bord('5'))
    Cell_2(Sub('27') + Bord('3') + Permut('0'), Sub('28') + Bord('3'))
    Cell_2(Sub('28') + Bord('1') + Permut('0'), Sub('29') + Bord('3'))
    Cell_2(Sub('29') + Bord('1') + Permut('0'), Sub('30') + Bord('3'))
    Cell_2(Sub('30') + Bord('1') + Permut('0'), Sub('31') + Bord('4'))
    Cell_2(Sub('31') + Bord('2') + Permut('0'), Sub('32') + Bord('4'))
    Cell_2(Sub('32') + Bord('2') + Permut('0'), Sub('33') + Bord('3'))
    Cell_2(Sub('33') + Bord('1') + Permut('0'), Sub('34') + Bord('4'))
    Cell_2(Sub('34') + Bord('2') + Permut('0'), Sub('35') + Bord('3'))
    Cell_2(Sub('35') + Bord('1') + Permut('0'), Sub('36') + Bord('5'))
    Cell_2(Sub('36') + Bord('3') + Permut('0'), Sub('37') + Bord('3'))
    Cell_2(Sub('37') + Bord('1') + Permut('0'), Sub('38') + Bord('3'))
    Cell_2(Sub('38') + Bord('1') + Permut('0'), Sub('39') + Bord('3'))
    Cell_2(Sub('39') + Bord('1') + Permut('0'), Sub('40') + Bord('4'))
    Cell_2(Sub('40') + Bord('2') + Permut('0'), Sub('41') + Bord('5'))
    Cell_2(Sub('41') + Bord('3') + Permut('0'), Sub('0') + Bord('3'))
    # edges adjacency constraints
    Cell_2(Bord('0') + Bord('1'), Bord('1') + Bord('0'))
    Cell_2(Bord('1') + Bord('1'), Bord('2') + Bord('0'))
    Cell_2(Bord('2') + Bord('1'), Bord('3') + Bord('0'))
    Cell_2(Bord('3') + Bord('1'), Bord('4') + Bord('0'))
    Cell_2(Bord('4') + Bord('1'), Bord('5') + Bord('0'))
    Cell_2(Bord('5') + Bord('1'), Bord('6') + Bord('0'))
    Cell_2(Bord('6') + Bord('1'), Bord('7') + Bord('0'))
    Cell_2(Bord('7') + Bord('1'), Bord('8') + Bord('0'))
    Cell_2(Bord('8') + Bord('1'), Bord('9') + Bord('0'))
    Cell_2(Bord('9') + Bord('1'), Bord('10') + Bord('0'))
    Cell_2(Bord('10') + Bord('1'), Bord('11') + Bord('0'))
    Cell_2(Bord('11') + Bord('1'), Bord('12') + Bord('0'))
    Cell_2(Bord('12') + Bord('1'), Bord('13') + Bord('0'))
    Cell_2(Bord('13') + Bord('1'), Bord('14') + Bord('0'))
    Cell_2(Bord('14') + Bord('1'), Bord('15') + Bord('0'))
    Cell_2(Bord('15') + Bord('1'), Bord('16') + Bord('0'))
    Cell_2(Bord('16') + Bord('1'), Bord('17') + Bord('0'))
    Cell_2(Bord('17') + Bord('1'), Bord('18') + Bord('0'))
    Cell_2(Bord('18') + Bord('1'), Bord('19') + Bord('0'))
    Cell_2(Bord('19') + Bord('1'), Bord('20') + Bord('0'))
    Cell_2(Bord('20') + Bord('1'), Bord('21') + Bord('0'))
    Cell_2(Bord('21') + Bord('1'), Bord('22') + Bord('0'))
    Cell_2(Bord('22') + Bord('1'), Bord('23') + Bord('0'))
    Cell_2(Bord('23') + Bord('1'), Bord('24') + Bord('0'))
    Cell_2(Bord('24') + Bord('1'), Bord('25') + Bord('0'))
    Cell_2(Bord('25') + Bord('1'), Bord('26') + Bord('0'))
    Cell_2(Bord('26') + Bord('1'), Bord('27') + Bord('0'))
    Cell_2(Bord('27') + Bord('1'), Bord('28') + Bord('0'))
    Cell_2(Bord('28') + Bord('1'), Bord('29') + Bord('0'))
    Cell_2(Bord('29') + Bord('1'), Bord('0') + Bord('0'))
    # incidence constraints
    Cell_3(Bord('0') + Sub('0'), Sub('0') + Bord('0'))
    Cell_3(Bord('0') + Sub('1'), Sub('1') + Bord('0'))
    Cell_3(Bord('1') + Sub('0'), Sub('2') + Bord('0'))
    Cell_3(Bord('2') + Sub('0'), Sub('3') + Bord('0'))
    Cell_3(Bord('3') + Sub('0'), Sub('4') + Bord('0'))
    Cell_3(Bord('4') + Sub('0'), Sub('5') + Bord('0'))
    # adjacency constraints
    Cell_3(Sub('0') + Bord('2') + Permut('0'), Sub('1') + Bord('3'))
    Cell_3(Sub('1') + Bord('1') + Permut('0'), Sub('2') + Bord('3'))
    Cell_3(Sub('2') + Bord('1') + Permut('0'), Sub('3') + Bord('3'))
    Cell_3(Sub('3') + Bord('1') + Permut('0'), Sub('4') + Bord('3'))
    Cell_3(Sub('4') + Bord('1') + Permut('0'), Sub('5') + Bord('3'))
    Cell_3(Sub('5') + Bord('1') + Permut('0'), Sub('0') + Bord('4'))
    # edges adjacency constraints
    Cell_3(Bord('0') + Bord('1'), Bord('1') + Bord('0'))
    Cell_3(Bord('1') + Bord('1'), Bord('2') + Bord('0'))
    Cell_3(Bord('2') + Bord('1'), Bord('3') + Bord('0'))
    Cell_3(Bord('3') + Bord('1'), Bord('4') + Bord('0'))
    Cell_3(Bord('4') + Bord('1'), Bord('0') + Bord('0'))
    # incidence constraints
    Cell_4(Bord('0') + Sub('0'), Sub('0') + Bord('0'))
    Cell_4(Bord('0') + Sub('1'), Sub('1') + Bord('0'))
    Cell_4(Bord('0') + Sub('2'), Sub('2') + Bord('0'))
    Cell_4(Bord('1') + Sub('0'), Sub('3') + Bord('0'))
    Cell_4(Bord('2') + Sub('0'), Sub('4') + Bord('0'))
    Cell_4(Bord('3') + Sub('0'), Sub('5') + Bord('0'))
    # adjacency constraints
    Cell_4(Sub('0') + Bord('1') + Permut('0'), Sub('1') + Bord('3'))
    Cell_4(Sub('1') + Bord('1') + Permut('0'), Sub('2') + Bord('3'))
    Cell_4(Sub('2') + Bord('1') + Permut('0'), Sub('3') + Bord('3'))
    Cell_4(Sub('3') + Bord('1') + Permut('0'), Sub('4') + Bord('3'))
    Cell_4(Sub('4') + Bord('1') + Permut('0'), Sub('5') + Bord('3'))
    Cell_4(Sub('5') + Bord('1') + Permut('0'), Sub('0') + Bord('3'))
    # edges adjacency constraints
    Cell_4(Bord('0') + Bord('1'), Bord('1') + Bord('0'))
    Cell_4(Bord('1') + Bord('1'), Bord('2') + Bord('0'))
    Cell_4(Bord('2') + Bord('1'), Bord('3') + Bord('0'))
    Cell_4(Bord('3') + Bord('1'), Bord('0') + Bord('0'))
    # incidence constraints
    Cell_5(Bord('0') + Sub('0'), Sub('0') + Bord('0'))
    Cell_5(Bord('0') + Sub('1'), Sub('1') + Bord('0'))
    Cell_5(Bord('1') + Sub('0'), Sub('2') + Bord('0'))
    Cell_5(Bord('2') + Sub('0'), Sub('3') + Bord('0'))
    Cell_5(Bord('3') + Sub('0'), Sub('4') + Bord('0'))
    Cell_5(Bord('4') + Sub('0'), Sub('5') + Bord('0'))
    # adjacency constraints
    Cell_5(Sub('0') + Bord('2') + Permut('0'), Sub('1') + Bord('3'))
    Cell_5(Sub('1') + Bord('1') + Permut('0'), Sub('2') + Bord('3'))
    Cell_5(Sub('2') + Bord('1') + Permut('0'), Sub('3') + Bord('3'))
    Cell_5(Sub('3') + Bord('1') + Permut('0'), Sub('4') + Bord('3'))
    Cell_5(Sub('4') + Bord('1') + Permut('0'), Sub('5') + Bord('3'))
    Cell_5(Sub('5') + Bord('1') + Permut('0'), Sub('0') + Bord('4'))
    # edges adjacency constraints
    Cell_5(Bord('0') + Bord('1'), Bord('1') + Bord('0'))
    Cell_5(Bord('1') + Bord('1'), Bord('2') + Bord('0'))
    Cell_5(Bord('2') + Bord('1'), Bord('3') + Bord('0'))
    Cell_5(Bord('3') + Bord('1'), Bord('4') + Bord('0'))
    Cell_5(Bord('4') + Bord('1'), Bord('0') + Bord('0'))
    # incidence constraints
    Cell_6(Bord('0') + Sub('0'), Sub('0') + Bord('0'))
    Cell_6(Bord('0') + Sub('1'), Sub('1') + Bord('0'))
    Cell_6(Bord('1') + Sub('0'), Sub('1') + Bord('1'))
    Cell_6(Bord('1') + Sub('1'), Sub('2') + Bord('0'))
    Cell_6(Bord('1') + Sub('2'), Sub('3') + Bord('0'))
    Cell_6(Bord('2') + Sub('0'), Sub('4') + Bord('0'))
    Cell_6(Bord('3') + Sub('0'), Sub('5') + Bord('0'))
    Cell_6(Bord('4') + Sub('0'), Sub('6') + Bord('0'))
    Cell_6(Bord('5') + Sub('0'), Sub('7') + Bord('0'))
    # adjacency constraints
    Cell_6(Sub('0') + Bord('2') + Permut('0'), Sub('1') + Bord('4'))
    Cell_6(Sub('1') + Bord('2') + Permut('0'), Sub('2') + Bord('3'))
    Cell_6(Sub('2') + Bord('1') + Permut('0'), Sub('3') + Bord('3'))
    Cell_6(Sub('3') + Bord('1') + Permut('0'), Sub('4') + Bord('3'))
    Cell_6(Sub('4') + Bord('1') + Permut('0'), Sub('5') + Bord('3'))
    Cell_6(Sub('5') + Bord('1') + Permut('0'), Sub('6') + Bord('3'))
    Cell_6(Sub('6') + Bord('1') + Permut('0'), Sub('7') + Bord('3'))
    Cell_6(Sub('7') + Bord('1') + Permut('0'), Sub('0') + Bord('4'))
    # edges adjacency constraints
    Cell_6(Bord('0') + Bord('1'), Bord('1') + Bord('0'))
    Cell_6(Bord('1') + Bord('1'), Bord('2') + Bord('0'))
    Cell_6(Bord('2') + Bord('1'), Bord('3') + Bord('0'))
    Cell_6(Bord('3') + Bord('1'), Bord('4') + Bord('0'))
    Cell_6(Bord('4') + Bord('1'), Bord('5') + Bord('0'))
    Cell_6(Bord('5') + Bord('1'), Bord('0') + Bord('0'))
    # incidence constraints
    Cell_7(Bord('0') + Sub('0'), Sub('0') + Bord('0'))
    Cell_7(Bord('0') + Sub('1'), Sub('1') + Bord('0'))
    Cell_7(Bord('0') + Sub('2'), Sub('2') + Bord('0'))
    Cell_7(Bord('1') + Sub('0'), Sub('2') + Bord('1'))
    Cell_7(Bord('1') + Sub('1'), Sub('3') + Bord('0'))
    Cell_7(Bord('1') + Sub('2'), Sub('4') + Bord('0'))
    Cell_7(Bord('2') + Sub('0'), Sub('5') + Bord('0'))
    Cell_7(Bord('3') + Sub('0'), Sub('6') + Bord('0'))
    Cell_7(Bord('4') + Sub('0'), Sub('7') + Bord('0'))
    # adjacency constraints
    Cell_7(Sub('0') + Bord('1') + Permut('0'), Sub('1') + Bord('3'))
    Cell_7(Sub('1') + Bord('1') + Permut('0'), Sub('2') + Bord('4'))
    Cell_7(Sub('2') + Bord('2') + Permut('0'), Sub('3') + Bord('3'))
    Cell_7(Sub('3') + Bord('1') + Permut('0'), Sub('4') + Bord('3'))
    Cell_7(Sub('4') + Bord('1') + Permut('0'), Sub('5') + Bord('3'))
    Cell_7(Sub('5') + Bord('1') + Permut('0'), Sub('6') + Bord('3'))
    Cell_7(Sub('6') + Bord('1') + Permut('0'), Sub('7') + Bord('3'))
    Cell_7(Sub('7') + Bord('1') + Permut('0'), Sub('0') + Bord('3'))
    # edges adjacency constraints
    Cell_7(Bord('0') + Bord('1'), Bord('1') + Bord('0'))
    Cell_7(Bord('1') + Bord('1'), Bord('2') + Bord('0'))
    Cell_7(Bord('2') + Bord('1'), Bord('3') + Bord('0'))
    Cell_7(Bord('3') + Bord('1'), Bord('4') + Bord('0'))
    Cell_7(Bord('4') + Bord('1'), Bord('0') + Bord('0'))
    # incidence constraints
    Cell_8(Bord('0') + Sub('0'), Sub('0') + Bord('0'))
    Cell_8(Bord('0') + Sub('1'), Sub('1') + Bord('0'))
    Cell_8(Bord('0') + Sub('2'), Sub('2') + Bord('0'))
    Cell_8(Bord('1') + Sub('0'), Sub('2') + Bord('1'))
    Cell_8(Bord('1') + Sub('1'), Sub('3') + Bord('0'))
    Cell_8(Bord('2') + Sub('0'), Sub('4') + Bord('0'))
    Cell_8(Bord('3') + Sub('0'), Sub('5') + Bord('0'))
    Cell_8(Bord('4') + Sub('0'), Sub('6') + Bord('0'))
    Cell_8(Bord('5') + Sub('0'), Sub('7') + Bord('0'))
    # adjacency constraints
    Cell_8(Sub('0') + Bord('1') + Permut('0'), Sub('1') + Bord('3'))
    Cell_8(Sub('1') + Bord('1') + Permut('0'), Sub('2') + Bord('5'))
    Cell_8(Sub('2') + Bord('3') + Permut('0'), Sub('3') + Bord('3'))
    Cell_8(Sub('3') + Bord('1') + Permut('0'), Sub('4') + Bord('3'))
    Cell_8(Sub('4') + Bord('1') + Permut('0'), Sub('5') + Bord('3'))
    Cell_8(Sub('5') + Bord('1') + Permut('0'), Sub('6') + Bord('3'))
    Cell_8(Sub('6') + Bord('1') + Permut('0'), Sub('7') + Bord('3'))
    Cell_8(Sub('7') + Bord('1') + Permut('0'), Sub('0') + Bord('3'))
    # edges adjacency constraints
    Cell_8(Bord('0') + Bord('1'), Bord('1') + Bord('0'))
    Cell_8(Bord('1') + Bord('1'), Bord('2') + Bord('0'))
    Cell_8(Bord('2') + Bord('1'), Bord('3') + Bord('0'))
    Cell_8(Bord('3') + Bord('1'), Bord('4') + Bord('0'))
    Cell_8(Bord('4') + Bord('1'), Bord('5') + Bord('0'))
    Cell_8(Bord('5') + Bord('1'), Bord('0') + Bord('0'))
    # incidence constraints
    Cell_9(Bord('0') + Sub('0'), Sub('0') + Bord('0'))
    Cell_9(Bord('0') + Sub('1'), Sub('1') + Bord('0'))
    Cell_9(Bord('1') + Sub('0'), Sub('1') + Bord('1'))
    Cell_9(Bord('1') + Sub('1'), Sub('2') + Bord('0'))
    Cell_9(Bord('2') + Sub('0'), Sub('3') + Bord('0'))
    Cell_9(Bord('3') + Sub('0'), Sub('4') + Bord('0'))
    Cell_9(Bord('4') + Sub('0'), Sub('5') + Bord('0'))
    Cell_9(Bord('5') + Sub('0'), Sub('6') + Bord('0'))
    Cell_9(Bord('6') + Sub('0'), Sub('7') + Bord('0'))
    # adjacency constraints
    Cell_9(Sub('0') + Bord('2') + Permut('0'), Sub('1') + Bord('5'))
    Cell_9(Sub('1') + Bord('3') + Permut('0'), Sub('2') + Bord('3'))
    Cell_9(Sub('2') + Bord('1') + Permut('0'), Sub('3') + Bord('3'))
    Cell_9(Sub('3') + Bord('1') + Permut('0'), Sub('4') + Bord('3'))
    Cell_9(Sub('4') + Bord('1') + Permut('0'), Sub('5') + Bord('3'))
    Cell_9(Sub('5') + Bord('1') + Permut('0'), Sub('6') + Bord('3'))
    Cell_9(Sub('6') + Bord('1') + Permut('0'), Sub('7') + Bord('3'))
    Cell_9(Sub('7') + Bord('1') + Permut('0'), Sub('0') + Bord('4'))
    # edges adjacency constraints
    Cell_9(Bord('0') + Bord('1'), Bord('1') + Bord('0'))
    Cell_9(Bord('1') + Bord('1'), Bord('2') + Bord('0'))
    Cell_9(Bord('2') + Bord('1'), Bord('3') + Bord('0'))
    Cell_9(Bord('3') + Bord('1'), Bord('4') + Bord('0'))
    Cell_9(Bord('4') + Bord('1'), Bord('5') + Bord('0'))
    Cell_9(Bord('5') + Bord('1'), Bord('6') + Bord('0'))
    Cell_9(Bord('6') + Bord('1'), Bord('0') + Bord('0'))
    # incidence constraints
    Cell_10(Bord('0') + Sub('0'), Sub('0') + Bord('0'))
    Cell_10(Bord('0') + Sub('1'), Sub('1') + Bord('0'))
    Cell_10(Bord('1') + Sub('0'), Sub('2') + Bord('0'))
    Cell_10(Bord('2') + Sub('0'), Sub('3') + Bord('0'))
    Cell_10(Bord('3') + Sub('0'), Sub('4') + Bord('0'))
    # adjacency constraints
    Cell_10(Sub('0') + Bord('1') + Permut('0'), Sub('1') + Bord('3'))
    Cell_10(Sub('1') + Bord('1') + Permut('0'), Sub('2') + Bord('3'))
    Cell_10(Sub('2') + Bord('1') + Permut('0'), Sub('3') + Bord('3'))
    Cell_10(Sub('3') + Bord('1') + Permut('0'), Sub('4') + Bord('3'))
    Cell_10(Sub('4') + Bord('1') + Permut('0'), Sub('0') + Bord('3'))
    # edges adjacency constraints
    Cell_10(Bord('0') + Bord('1'), Bord('1') + Bord('0'))
    Cell_10(Bord('1') + Bord('1'), Bord('2') + Bord('0'))
    Cell_10(Bord('2') + Bord('1'), Bord('3') + Bord('0'))
    Cell_10(Bord('3') + Bord('1'), Bord('0') + Bord('0'))
    # incidence constraints
    Cell_11(Bord('0') + Sub('0'), Sub('0') + Bord('0'))
    Cell_11(Bord('1') + Sub('0'), Sub('1') + Bord('0'))
    Cell_11(Bord('2') + Sub('0'), Sub('2') + Bord('0'))
    Cell_11(Bord('3') + Sub('0'), Sub('3') + Bord('0'))
    # adjacency constraints
    Cell_11(Sub('0') + Bord('1') + Permut('0'), Sub('1') + Bord('3'))
    Cell_11(Sub('1') + Bord('1') + Permut('0'), Sub('2') + Bord('3'))
    Cell_11(Sub('2') + Bord('1') + Permut('0'), Sub('3') + Bord('3'))
    Cell_11(Sub('3') + Bord('1') + Permut('0'), Sub('0') + Bord('3'))
    # edges adjacency constraints
    Cell_11(Bord('0') + Bord('1'), Bord('1') + Bord('0'))
    Cell_11(Bord('1') + Bord('1'), Bord('2') + Bord('0'))
    Cell_11(Bord('2') + Bord('1'), Bord('3') + Bord('0'))
    Cell_11(Bord('3') + Bord('1'), Bord('0') + Bord('0'))
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
