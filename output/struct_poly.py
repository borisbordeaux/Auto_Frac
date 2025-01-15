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
        [1.0000, 0.5000, 0.2500],
        [0.0000, 0.5000, 0.5000],
        [0.0000, 0.0000, 0.2500]]).setTyp('Var')
    B2.initMat[Sub_('1')] = FMat([
        [0.2500, 0.0000, 0.0000],
        [0.5000, 0.5000, 0.0000],
        [0.2500, 0.5000, 1.0000]]).setTyp('Var')
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
        [1.0000, 0.6667, 0.4444],
        [0.0000, 0.3333, 0.4444],
        [0.0000, 0.0000, 0.1111]]).setTyp('Var')
    B3.initMat[Sub_('1')] = FMat([
        [0.4444, 0.2222, 0.1111],
        [0.4444, 0.5556, 0.4444],
        [0.1111, 0.2222, 0.4444]]).setTyp('Var')
    B3.initMat[Sub_('2')] = FMat([
        [0.1111, 0.0000, 0.0000],
        [0.4444, 0.3333, 0.0000],
        [0.4444, 0.6667, 1.0000]]).setTyp('Var')
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
        [1.0000, 0.7500, 0.5625],
        [0.0000, 0.2500, 0.3750],
        [0.0000, 0.0000, 0.0625]]).setTyp('Var')
    B4.initMat[Sub_('1')] = FMat([
        [0.5625, 0.3750, 0.2500],
        [0.3750, 0.5000, 0.5000],
        [0.0625, 0.1250, 0.2500]]).setTyp('Var')
    B4.initMat[Sub_('2')] = FMat([
        [0.2500, 0.1250, 0.0625],
        [0.5000, 0.5000, 0.3750],
        [0.2500, 0.3750, 0.5625]]).setTyp('Var')
    B4.initMat[Sub_('3')] = FMat([
        [0.0625, 0.0000, 0.0000],
        [0.3750, 0.2500, 0.0000],
        [0.5625, 0.7500, 1.0000]]).setTyp('Var')
    ##############################
    # all cells states
    # Cube -- B2 (2) -- B2 (1) -- B2 (3) -- B2 (4)
    Cube = Etat('Cube', 0)
    # Octa -- B3 (3) -- B3 (1) -- B3 (2)
    Octa = Etat('Octa', 0)
    # Icosa -- B4 (5) -- B4 (1) -- B4 (9)
    Icosa = Etat('Icosa', 0)
    # Dodeca -- B2 (18) -- B2 (17) -- B2 (5) -- B2 (15) -- B2 (7)
    Dodeca = Etat('Dodeca', 0)
    # Tetra -- B2 (3) -- B2 (1) -- B2 (2)
    Tetra = Etat('Tetra', 0)
    # Tri_Penta_Pyr -- B2 (3) -- B2 (1) -- B4 (2)
    Tri_Penta_Pyr = Etat('Tri_Penta_Pyr', 0)
    # Base_Penta_Pyr -- B2 (6) -- B2 (1) -- B2 (3) -- B2 (4) -- B2 (5)
    Base_Penta_Pyr = Etat('Base_Penta_Pyr', 0)
    # Base_Square_Pyr -- B2 (4) -- B2 (1) -- B2 (2) -- B2 (3)
    Base_Square_Pyr = Etat('Base_Square_Pyr', 0)
    # Tri_Square_Pyr -- B3 (5) -- B2 (4) -- B2 (3)
    Tri_Square_Pyr = Etat('Tri_Square_Pyr', 0)
    ##############################
    # subd of init
    init.subs = {Sub('0'): Cube, Sub('1'): Tri_Penta_Pyr, Sub('2'): Icosa, Sub('3'): Tetra, Sub('4'): Base_Penta_Pyr, Sub('5'): Base_Square_Pyr, Sub('6'): Dodeca, Sub('7'): Octa, Sub('8'): Tri_Square_Pyr}
    ##############################
    # edges of all states
    Cube.bords = {Bord('0'): B2, Bord('1'): B2, Bord('2'): B2, Bord('3'): B2}
    Octa.bords = {Bord('0'): B3, Bord('1'): B3, Bord('2'): B3}
    Icosa.bords = {Bord('0'): B4, Bord('1'): B4, Bord('2'): B4}
    Dodeca.bords = {Bord('0'): B2, Bord('1'): B2, Bord('2'): B2, Bord('3'): B2, Bord('4'): B2}
    Tetra.bords = {Bord('0'): B2, Bord('1'): B2, Bord('2'): B2}
    Tri_Penta_Pyr.bords = {Bord('0'): B2, Bord('1'): B2, Bord('2'): B4}
    Base_Penta_Pyr.bords = {Bord('0'): B2, Bord('1'): B2, Bord('2'): B2, Bord('3'): B2, Bord('4'): B2}
    Base_Square_Pyr.bords = {Bord('0'): B2, Bord('1'): B2, Bord('2'): B2, Bord('3'): B2}
    Tri_Square_Pyr.bords = {Bord('0'): B3, Bord('1'): B2, Bord('2'): B2}
    ##############################
    # subdivisions of all states
    Cube.subs = {Sub('0'): Cube, Sub('1'): Cube, Sub('2'): Cube, Sub('3'): Cube, Sub('4'): Cube}
    Octa.subs = {Sub('0'): Octa, Sub('1'): Octa, Sub('2'): Octa, Sub('3'): Octa, Sub('4'): Octa, Sub('5'): Octa, Sub('6'): Octa}
    Icosa.subs = {Sub('0'): Icosa, Sub('1'): Icosa, Sub('2'): Icosa, Sub('3'): Icosa, Sub('4'): Icosa, Sub('5'): Icosa, Sub('6'): Icosa, Sub('7'): Icosa, Sub('8'): Icosa, Sub('9'): Icosa, Sub('10'): Icosa, Sub('11'): Icosa, Sub('12'): Icosa, Sub('13'): Icosa, Sub('14'): Icosa, Sub('15'): Icosa, Sub('16'): Icosa, Sub('17'): Icosa, Sub('18'): Icosa}
    Dodeca.subs = {Sub('0'): Dodeca, Sub('1'): Dodeca, Sub('2'): Dodeca, Sub('3'): Dodeca, Sub('4'): Dodeca, Sub('5'): Dodeca, Sub('6'): Dodeca, Sub('7'): Dodeca, Sub('8'): Dodeca, Sub('9'): Dodeca, Sub('10'): Dodeca}
    Tetra.subs = {Sub('0'): Tetra, Sub('1'): Tetra, Sub('2'): Tetra}
    Tri_Penta_Pyr.subs = {Sub('0'): Tri_Penta_Pyr, Sub('1'): Tri_Penta_Pyr, Sub('2'): Base_Penta_Pyr, Sub('3'): Tri_Penta_Pyr, Sub('4'): Tri_Penta_Pyr}
    Base_Penta_Pyr.subs = {Sub('0'): Tri_Penta_Pyr, Sub('1'): Tri_Penta_Pyr, Sub('2'): Tri_Penta_Pyr, Sub('3'): Tri_Penta_Pyr, Sub('4'): Tri_Penta_Pyr}
    Base_Square_Pyr.subs = {Sub('0'): Tri_Square_Pyr, Sub('1'): Tri_Square_Pyr, Sub('2'): Tri_Square_Pyr, Sub('3'): Tri_Square_Pyr}
    Tri_Square_Pyr.subs = {Sub('0'): Base_Square_Pyr, Sub('1'): Tri_Square_Pyr, Sub('2'): Tri_Square_Pyr, Sub('3'): Tri_Square_Pyr}
    ##############################
    # build intern of all states
    Cube.buildIntern()
    Octa.buildIntern()
    Icosa.buildIntern()
    Dodeca.buildIntern()
    Tetra.buildIntern()
    Tri_Penta_Pyr.buildIntern()
    Base_Penta_Pyr.buildIntern()
    Base_Square_Pyr.buildIntern()
    Tri_Square_Pyr.buildIntern()
    ##############################
    # spaces of all states
    Cube.space = [Bord_('0'), Bord_('1'), Bord_('2'), Bord_('3')]
    Octa.space = [Bord_('0'), Bord_('1'), Bord_('2')]
    Icosa.space = [Bord_('0'), Bord_('1'), Bord_('2')]
    Dodeca.space = [Bord_('0'), Bord_('1'), Bord_('2'), Bord_('3'), Bord_('4')]
    Tetra.space = [Bord_('0'), Bord_('1'), Bord_('2')]
    Tri_Penta_Pyr.space = [Bord_('0'), Bord_('1'), Bord_('2')]
    Base_Penta_Pyr.space = [Bord_('0'), Bord_('1'), Bord_('2'), Bord_('3'), Bord_('4')]
    Base_Square_Pyr.space = [Bord_('0'), Bord_('1'), Bord_('2'), Bord_('3')]
    Tri_Square_Pyr.space = [Bord_('0'), Bord_('1'), Bord_('2')]
    ##############################
    # grid of all states
    Cube.addGrid(Bord)
    Octa.addGrid(Bord)
    Icosa.addGrid(Bord)
    Dodeca.addGrid(Bord)
    Tetra.addGrid(Bord)
    Tri_Penta_Pyr.addGrid(Bord)
    Base_Penta_Pyr.addGrid(Bord)
    Base_Square_Pyr.addGrid(Bord)
    Tri_Square_Pyr.addGrid(Bord)
    ##############################
    # prim of all states
    Cube.prim.elems = [Figure(2, [
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
    Octa.prim.elems = [Figure(2, [
        Bord_('0') + Sub('0') + Bord('0'),
        Bord_('0') + Sub('1') + Bord('0'),
        Bord_('0') + Sub('2') + Bord('0'),
        Bord_('1') + Sub('0') + Bord('0'),
        Bord_('1') + Sub('1') + Bord('0'),
        Bord_('1') + Sub('2') + Bord('0'),
        Bord_('2') + Sub('0') + Bord('0'),
        Bord_('2') + Sub('1') + Bord('0'),
        Bord_('2') + Sub('2') + Bord('0'),
    ])]
    Icosa.prim.elems = [Figure(2, [
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
        Bord_('2') + Sub('3') + Bord('0'),
    ])]
    Dodeca.prim.elems = [Figure(2, [
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
    Tetra.prim.elems = [Figure(2, [
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
    ])]
    Tri_Penta_Pyr.prim.elems = [Figure(2, [
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
    Base_Penta_Pyr.prim.elems = [Figure(2, [
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
    Base_Square_Pyr.prim.elems = [Figure(2, [
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
    Tri_Square_Pyr.prim.elems = [Figure(2, [
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
    ])]
    ##############################
    # constraints of all states
    # incidence constraints
    Cube(Bord('0') + Sub('0') + Permut('0'), Sub('0') + Bord('2'))
    Cube(Bord('3') + Sub('1') + Permut('0'), Sub('0') + Bord('3'))
    Cube(Bord('1') + Sub('1') + Permut('0'), Sub('1') + Bord('0'))
    Cube(Bord('2') + Sub('0') + Permut('0'), Sub('1') + Bord('3'))
    Cube(Bord('2') + Sub('1') + Permut('0'), Sub('2') + Bord('0'))
    Cube(Bord('3') + Sub('0') + Permut('0'), Sub('2') + Bord('3'))
    Cube(Bord('1') + Sub('0') + Permut('0'), Sub('3') + Bord('1'))
    Cube(Bord('0') + Sub('1') + Permut('0'), Sub('3') + Bord('2'))
    # adjacency constraints
    Cube(Sub('0') + Bord('0') + Bord('1'), Sub('4') + Bord('2') + Bord('1'))
    Cube(Sub('0') + Bord('1') + Bord('1'), Sub('3') + Bord('2') + Bord('1'))
    Cube(Sub('0') + Bord('3') + Bord('1'), Sub('2') + Bord('2') + Bord('1'))
    Cube(Sub('1') + Bord('0') + Bord('1'), Sub('3') + Bord('0') + Bord('1'))
    Cube(Sub('1') + Bord('1') + Bord('1'), Sub('4') + Bord('0') + Bord('1'))
    Cube(Sub('1') + Bord('2') + Bord('1'), Sub('2') + Bord('0') + Bord('1'))
    Cube(Sub('2') + Bord('1') + Bord('1'), Sub('4') + Bord('3') + Bord('1'))
    Cube(Sub('3') + Bord('3') + Bord('1'), Sub('4') + Bord('1') + Bord('1'))
    # edges adjacency constraints
    Cube(Bord('0') + Bord('1'), Bord('1') + Bord('0'))
    Cube(Bord('1') + Bord('1'), Bord('2') + Bord('0'))
    Cube(Bord('2') + Bord('1'), Bord('3') + Bord('0'))
    Cube(Bord('3') + Bord('1'), Bord('0') + Bord('0'))
    # incidence constraints
    Octa(Bord('0') + Sub('0') + Permut('0'), Sub('0') + Bord('0'))
    Octa(Bord('2') + Sub('2') + Permut('0'), Sub('0') + Bord('1'))
    Octa(Bord('0') + Sub('1') + Permut('0'), Sub('1') + Bord('0'))
    Octa(Bord('0') + Sub('2') + Permut('0'), Sub('2') + Bord('0'))
    Octa(Bord('1') + Sub('0') + Permut('0'), Sub('2') + Bord('2'))
    Octa(Bord('2') + Sub('0') + Permut('0'), Sub('3') + Bord('0'))
    Octa(Bord('1') + Sub('2') + Permut('0'), Sub('3') + Bord('1'))
    Octa(Bord('2') + Sub('1') + Permut('0'), Sub('4') + Bord('1'))
    Octa(Bord('1') + Sub('1') + Permut('0'), Sub('6') + Bord('0'))
    # adjacency constraints
    Octa(Sub('0') + Bord('1') + Bord('1'), Sub('4') + Bord('0') + Bord('1'))
    Octa(Sub('0') + Bord('2') + Bord('1'), Sub('1') + Bord('0') + Bord('1'))
    Octa(Sub('1') + Bord('1') + Bord('1'), Sub('5') + Bord('0') + Bord('1'))
    Octa(Sub('1') + Bord('2') + Bord('1'), Sub('2') + Bord('0') + Bord('1'))
    Octa(Sub('2') + Bord('1') + Bord('1'), Sub('6') + Bord('0') + Bord('1'))
    Octa(Sub('3') + Bord('1') + Bord('1'), Sub('6') + Bord('2') + Bord('1'))
    Octa(Sub('3') + Bord('2') + Bord('1'), Sub('4') + Bord('1') + Bord('1'))
    Octa(Sub('4') + Bord('2') + Bord('1'), Sub('5') + Bord('1') + Bord('1'))
    Octa(Sub('5') + Bord('2') + Bord('1'), Sub('6') + Bord('1') + Bord('1'))
    # edges adjacency constraints
    Octa(Bord('0') + Bord('1'), Bord('1') + Bord('0'))
    Octa(Bord('1') + Bord('1'), Bord('2') + Bord('0'))
    Octa(Bord('2') + Bord('1'), Bord('0') + Bord('0'))
    # incidence constraints
    Icosa(Bord('1') + Sub('2') + Permut('0'), Sub('0') + Bord('1'))
    Icosa(Bord('0') + Sub('2') + Permut('0'), Sub('1') + Bord('2'))
    Icosa(Bord('2') + Sub('2') + Permut('0'), Sub('3') + Bord('0'))
    Icosa(Bord('2') + Sub('0') + Permut('0'), Sub('7') + Bord('0'))
    Icosa(Bord('1') + Sub('3') + Permut('0'), Sub('7') + Bord('1'))
    Icosa(Bord('2') + Sub('1') + Permut('0'), Sub('8') + Bord('2'))
    Icosa(Bord('1') + Sub('0') + Permut('0'), Sub('11') + Bord('0'))
    Icosa(Bord('0') + Sub('3') + Permut('0'), Sub('11') + Bord('1'))
    Icosa(Bord('1') + Sub('1') + Permut('0'), Sub('12') + Bord('2'))
    Icosa(Bord('0') + Sub('0') + Permut('0'), Sub('15') + Bord('0'))
    Icosa(Bord('2') + Sub('3') + Permut('0'), Sub('15') + Bord('1'))
    Icosa(Bord('0') + Sub('1') + Permut('0'), Sub('16') + Bord('2'))
    # adjacency constraints
    Icosa(Sub('0') + Bord('0') + Bord('1'), Sub('7') + Bord('1') + Bord('1'))
    Icosa(Sub('0') + Bord('1') + Bord('1'), Sub('12') + Bord('1') + Bord('1'))
    Icosa(Sub('0') + Bord('2') + Bord('1'), Sub('17') + Bord('1') + Bord('1'))
    Icosa(Sub('1') + Bord('0') + Bord('1'), Sub('9') + Bord('1') + Bord('1'))
    Icosa(Sub('1') + Bord('1') + Bord('1'), Sub('11') + Bord('1') + Bord('1'))
    Icosa(Sub('1') + Bord('2') + Bord('1'), Sub('16') + Bord('1') + Bord('1'))
    Icosa(Sub('2') + Bord('0') + Bord('1'), Sub('12') + Bord('0') + Bord('1'))
    Icosa(Sub('2') + Bord('1') + Bord('1'), Sub('9') + Bord('0') + Bord('1'))
    Icosa(Sub('2') + Bord('2') + Bord('1'), Sub('18') + Bord('0') + Bord('1'))
    Icosa(Sub('3') + Bord('0') + Bord('1'), Sub('8') + Bord('1') + Bord('1'))
    Icosa(Sub('3') + Bord('1') + Bord('1'), Sub('13') + Bord('1') + Bord('1'))
    Icosa(Sub('3') + Bord('2') + Bord('1'), Sub('15') + Bord('1') + Bord('1'))
    Icosa(Sub('4') + Bord('0') + Bord('1'), Sub('14') + Bord('0') + Bord('1'))
    Icosa(Sub('4') + Bord('1') + Bord('1'), Sub('8') + Bord('0') + Bord('1'))
    Icosa(Sub('4') + Bord('2') + Bord('1'), Sub('17') + Bord('0') + Bord('1'))
    Icosa(Sub('5') + Bord('0') + Bord('1'), Sub('13') + Bord('0') + Bord('1'))
    Icosa(Sub('5') + Bord('1') + Bord('1'), Sub('10') + Bord('0') + Bord('1'))
    Icosa(Sub('5') + Bord('2') + Bord('1'), Sub('16') + Bord('0') + Bord('1'))
    Icosa(Sub('6') + Bord('0') + Bord('1'), Sub('10') + Bord('1') + Bord('1'))
    Icosa(Sub('6') + Bord('1') + Bord('1'), Sub('14') + Bord('1') + Bord('1'))
    Icosa(Sub('6') + Bord('2') + Bord('1'), Sub('18') + Bord('1') + Bord('1'))
    Icosa(Sub('7') + Bord('2') + Bord('1'), Sub('8') + Bord('2') + Bord('1'))
    Icosa(Sub('9') + Bord('2') + Bord('1'), Sub('10') + Bord('2') + Bord('1'))
    Icosa(Sub('11') + Bord('2') + Bord('1'), Sub('12') + Bord('2') + Bord('1'))
    Icosa(Sub('13') + Bord('2') + Bord('1'), Sub('14') + Bord('2') + Bord('1'))
    Icosa(Sub('15') + Bord('2') + Bord('1'), Sub('16') + Bord('2') + Bord('1'))
    Icosa(Sub('17') + Bord('2') + Bord('1'), Sub('18') + Bord('2') + Bord('1'))
    # edges adjacency constraints
    Icosa(Bord('0') + Bord('1'), Bord('1') + Bord('0'))
    Icosa(Bord('1') + Bord('1'), Bord('2') + Bord('0'))
    Icosa(Bord('2') + Bord('1'), Bord('0') + Bord('0'))
    # incidence constraints
    Dodeca(Bord('2') + Sub('1') + Permut('0'), Sub('0') + Bord('0'))
    Dodeca(Bord('3') + Sub('0') + Permut('0'), Sub('0') + Bord('4'))
    Dodeca(Bord('1') + Sub('0') + Permut('0'), Sub('3') + Bord('2'))
    Dodeca(Bord('0') + Sub('1') + Permut('0'), Sub('3') + Bord('3'))
    Dodeca(Bord('0') + Sub('0') + Permut('0'), Sub('4') + Bord('0'))
    Dodeca(Bord('4') + Sub('1') + Permut('0'), Sub('4') + Bord('1'))
    Dodeca(Bord('1') + Sub('1') + Permut('0'), Sub('9') + Bord('0'))
    Dodeca(Bord('2') + Sub('0') + Permut('0'), Sub('9') + Bord('4'))
    Dodeca(Bord('4') + Sub('0') + Permut('0'), Sub('10') + Bord('3'))
    Dodeca(Bord('3') + Sub('1') + Permut('0'), Sub('10') + Bord('4'))
    # adjacency constraints
    Dodeca(Sub('0') + Bord('0') + Bord('1'), Sub('9') + Bord('3') + Bord('1'))
    Dodeca(Sub('0') + Bord('1') + Bord('1'), Sub('7') + Bord('4') + Bord('1'))
    Dodeca(Sub('0') + Bord('2') + Bord('1'), Sub('8') + Bord('2') + Bord('1'))
    Dodeca(Sub('0') + Bord('3') + Bord('1'), Sub('10') + Bord('4') + Bord('1'))
    Dodeca(Sub('1') + Bord('0') + Bord('1'), Sub('9') + Bord('1') + Bord('1'))
    Dodeca(Sub('1') + Bord('1') + Bord('1'), Sub('3') + Bord('0') + Bord('1'))
    Dodeca(Sub('1') + Bord('2') + Bord('1'), Sub('6') + Bord('0') + Bord('1'))
    Dodeca(Sub('1') + Bord('3') + Bord('1'), Sub('2') + Bord('4') + Bord('1'))
    Dodeca(Sub('1') + Bord('4') + Bord('1'), Sub('7') + Bord('1') + Bord('1'))
    Dodeca(Sub('2') + Bord('0') + Bord('1'), Sub('6') + Bord('4') + Bord('1'))
    Dodeca(Sub('2') + Bord('1') + Bord('1'), Sub('5') + Bord('2') + Bord('1'))
    Dodeca(Sub('2') + Bord('2') + Bord('1'), Sub('8') + Bord('4') + Bord('1'))
    Dodeca(Sub('2') + Bord('3') + Bord('1'), Sub('7') + Bord('2') + Bord('1'))
    Dodeca(Sub('3') + Bord('1') + Bord('1'), Sub('9') + Bord('0') + Bord('1'))
    Dodeca(Sub('3') + Bord('3') + Bord('1'), Sub('4') + Bord('4') + Bord('1'))
    Dodeca(Sub('3') + Bord('4') + Bord('1'), Sub('6') + Bord('1') + Bord('1'))
    Dodeca(Sub('4') + Bord('1') + Bord('1'), Sub('10') + Bord('2') + Bord('1'))
    Dodeca(Sub('4') + Bord('2') + Bord('1'), Sub('5') + Bord('4') + Bord('1'))
    Dodeca(Sub('4') + Bord('3') + Bord('1'), Sub('6') + Bord('2') + Bord('1'))
    Dodeca(Sub('5') + Bord('0') + Bord('1'), Sub('10') + Bord('1') + Bord('1'))
    Dodeca(Sub('5') + Bord('1') + Bord('1'), Sub('8') + Bord('0') + Bord('1'))
    Dodeca(Sub('5') + Bord('3') + Bord('1'), Sub('6') + Bord('3') + Bord('1'))
    Dodeca(Sub('7') + Bord('0') + Bord('1'), Sub('9') + Bord('2') + Bord('1'))
    Dodeca(Sub('7') + Bord('3') + Bord('1'), Sub('8') + Bord('3') + Bord('1'))
    Dodeca(Sub('8') + Bord('1') + Bord('1'), Sub('10') + Bord('0') + Bord('1'))
    # edges adjacency constraints
    Dodeca(Bord('0') + Bord('1'), Bord('1') + Bord('0'))
    Dodeca(Bord('1') + Bord('1'), Bord('2') + Bord('0'))
    Dodeca(Bord('2') + Bord('1'), Bord('3') + Bord('0'))
    Dodeca(Bord('3') + Bord('1'), Bord('4') + Bord('0'))
    Dodeca(Bord('4') + Bord('1'), Bord('0') + Bord('0'))
    # incidence constraints
    Tetra(Bord('1') + Sub('0') + Permut('0'), Sub('0') + Bord('1'))
    Tetra(Bord('0') + Sub('1') + Permut('0'), Sub('0') + Bord('2'))
    Tetra(Bord('2') + Sub('0') + Permut('0'), Sub('1') + Bord('0'))
    Tetra(Bord('1') + Sub('1') + Permut('0'), Sub('1') + Bord('1'))
    Tetra(Bord('0') + Sub('0') + Permut('0'), Sub('2') + Bord('0'))
    Tetra(Bord('2') + Sub('1') + Permut('0'), Sub('2') + Bord('1'))
    # adjacency constraints
    Tetra(Sub('0') + Bord('0') + Bord('1'), Sub('1') + Bord('1') + Bord('1'))
    Tetra(Sub('0') + Bord('2') + Bord('1'), Sub('2') + Bord('2') + Bord('1'))
    Tetra(Sub('1') + Bord('2') + Bord('1'), Sub('2') + Bord('1') + Bord('1'))
    # edges adjacency constraints
    Tetra(Bord('0') + Bord('1'), Bord('1') + Bord('0'))
    Tetra(Bord('1') + Bord('1'), Bord('2') + Bord('0'))
    Tetra(Bord('2') + Bord('1'), Bord('0') + Bord('0'))
    # incidence constraints
    Tri_Penta_Pyr(Bord('0') + Sub('0') + Permut('0'), Sub('0') + Bord('1'))
    Tri_Penta_Pyr(Bord('2') + Sub('3') + Permut('0'), Sub('0') + Bord('2'))
    Tri_Penta_Pyr(Bord('2') + Sub('2') + Permut('0'), Sub('1') + Bord('2'))
    Tri_Penta_Pyr(Bord('1') + Sub('0') + Permut('0'), Sub('2') + Bord('1'))
    Tri_Penta_Pyr(Bord('0') + Sub('1') + Permut('0'), Sub('2') + Bord('2'))
    Tri_Penta_Pyr(Bord('2') + Sub('1') + Permut('0'), Sub('3') + Bord('2'))
    Tri_Penta_Pyr(Bord('1') + Sub('1') + Permut('0'), Sub('4') + Bord('0'))
    Tri_Penta_Pyr(Bord('2') + Sub('0') + Permut('0'), Sub('4') + Bord('2'))
    # adjacency constraints
    Tri_Penta_Pyr(Sub('0') + Bord('0') + Bord('1'), Sub('2') + Bord('2') + Bord('1'))
    Tri_Penta_Pyr(Sub('0') + Bord('2') + Bord('1'), Sub('1') + Bord('1') + Bord('1'))
    Tri_Penta_Pyr(Sub('1') + Bord('0') + Bord('1'), Sub('2') + Bord('3') + Bord('1'))
    Tri_Penta_Pyr(Sub('1') + Bord('2') + Bord('1'), Sub('3') + Bord('1') + Bord('1'))
    Tri_Penta_Pyr(Sub('2') + Bord('0') + Bord('1'), Sub('4') + Bord('0') + Bord('1'))
    Tri_Penta_Pyr(Sub('2') + Bord('4') + Bord('1'), Sub('3') + Bord('0') + Bord('1'))
    Tri_Penta_Pyr(Sub('3') + Bord('2') + Bord('1'), Sub('4') + Bord('1') + Bord('1'))
    # edges adjacency constraints
    Tri_Penta_Pyr(Bord('0') + Bord('1'), Bord('1') + Bord('0'))
    Tri_Penta_Pyr(Bord('1') + Bord('1'), Bord('2') + Bord('0'))
    Tri_Penta_Pyr(Bord('2') + Bord('1'), Bord('0') + Bord('0'))
    # incidence constraints
    Base_Penta_Pyr(Bord('2') + Sub('0') + Permut('0'), Sub('0') + Bord('0'))
    Base_Penta_Pyr(Bord('1') + Sub('1') + Permut('0'), Sub('0') + Bord('1'))
    Base_Penta_Pyr(Bord('3') + Sub('0') + Permut('0'), Sub('1') + Bord('0'))
    Base_Penta_Pyr(Bord('2') + Sub('1') + Permut('0'), Sub('1') + Bord('1'))
    Base_Penta_Pyr(Bord('4') + Sub('0') + Permut('0'), Sub('2') + Bord('0'))
    Base_Penta_Pyr(Bord('3') + Sub('1') + Permut('0'), Sub('2') + Bord('1'))
    Base_Penta_Pyr(Bord('0') + Sub('0') + Permut('0'), Sub('3') + Bord('0'))
    Base_Penta_Pyr(Bord('4') + Sub('1') + Permut('0'), Sub('3') + Bord('1'))
    Base_Penta_Pyr(Bord('1') + Sub('0') + Permut('0'), Sub('4') + Bord('0'))
    Base_Penta_Pyr(Bord('0') + Sub('1') + Permut('0'), Sub('4') + Bord('1'))
    # adjacency constraints
    Base_Penta_Pyr(Sub('0') + Bord('1') + Bord('1'), Sub('4') + Bord('2') + Bord('1'))
    Base_Penta_Pyr(Sub('0') + Bord('2') + Bord('1'), Sub('1') + Bord('1') + Bord('1'))
    Base_Penta_Pyr(Sub('1') + Bord('2') + Bord('1'), Sub('2') + Bord('1') + Bord('1'))
    Base_Penta_Pyr(Sub('2') + Bord('2') + Bord('1'), Sub('3') + Bord('1') + Bord('1'))
    Base_Penta_Pyr(Sub('3') + Bord('2') + Bord('1'), Sub('4') + Bord('1') + Bord('1'))
    # edges adjacency constraints
    Base_Penta_Pyr(Bord('0') + Bord('1'), Bord('1') + Bord('0'))
    Base_Penta_Pyr(Bord('1') + Bord('1'), Bord('2') + Bord('0'))
    Base_Penta_Pyr(Bord('2') + Bord('1'), Bord('3') + Bord('0'))
    Base_Penta_Pyr(Bord('3') + Bord('1'), Bord('4') + Bord('0'))
    Base_Penta_Pyr(Bord('4') + Bord('1'), Bord('0') + Bord('0'))
    # incidence constraints
    Base_Square_Pyr(Bord('0') + Sub('0') + Permut('0'), Sub('0') + Bord('1'))
    Base_Square_Pyr(Bord('3') + Sub('1') + Permut('0'), Sub('0') + Bord('2'))
    Base_Square_Pyr(Bord('3') + Sub('0') + Permut('0'), Sub('1') + Bord('1'))
    Base_Square_Pyr(Bord('2') + Sub('1') + Permut('0'), Sub('1') + Bord('2'))
    Base_Square_Pyr(Bord('2') + Sub('0') + Permut('0'), Sub('2') + Bord('1'))
    Base_Square_Pyr(Bord('1') + Sub('1') + Permut('0'), Sub('2') + Bord('2'))
    Base_Square_Pyr(Bord('1') + Sub('0') + Permut('0'), Sub('3') + Bord('1'))
    Base_Square_Pyr(Bord('0') + Sub('1') + Permut('0'), Sub('3') + Bord('2'))
    # adjacency constraints
    Base_Square_Pyr(Sub('0') + Bord('0') + Bord('1'), Sub('3') + Bord('2') + Bord('1'))
    Base_Square_Pyr(Sub('0') + Bord('2') + Bord('1'), Sub('1') + Bord('0') + Bord('1'))
    Base_Square_Pyr(Sub('1') + Bord('2') + Bord('1'), Sub('2') + Bord('0') + Bord('1'))
    Base_Square_Pyr(Sub('2') + Bord('2') + Bord('1'), Sub('3') + Bord('0') + Bord('1'))
    # edges adjacency constraints
    Base_Square_Pyr(Bord('0') + Bord('1'), Bord('1') + Bord('0'))
    Base_Square_Pyr(Bord('1') + Bord('1'), Bord('2') + Bord('0'))
    Base_Square_Pyr(Bord('2') + Bord('1'), Bord('3') + Bord('0'))
    Base_Square_Pyr(Bord('3') + Bord('1'), Bord('0') + Bord('0'))
    # incidence constraints
    Tri_Square_Pyr(Bord('1') + Sub('1') + Permut('0'), Sub('0') + Bord('0'))
    Tri_Square_Pyr(Bord('2') + Sub('0') + Permut('0'), Sub('0') + Bord('3'))
    Tri_Square_Pyr(Bord('0') + Sub('0') + Permut('0'), Sub('1') + Bord('0'))
    Tri_Square_Pyr(Bord('2') + Sub('1') + Permut('0'), Sub('1') + Bord('1'))
    Tri_Square_Pyr(Bord('0') + Sub('1') + Permut('0'), Sub('2') + Bord('0'))
    Tri_Square_Pyr(Bord('0') + Sub('2') + Permut('0'), Sub('3') + Bord('0'))
    Tri_Square_Pyr(Bord('1') + Sub('0') + Permut('0'), Sub('3') + Bord('2'))
    # adjacency constraints
    Tri_Square_Pyr(Sub('0') + Bord('0') + Bord('1'), Sub('3') + Bord('1') + Bord('1'))
    Tri_Square_Pyr(Sub('0') + Bord('1') + Bord('1'), Sub('2') + Bord('1') + Bord('1'))
    Tri_Square_Pyr(Sub('0') + Bord('2') + Bord('1'), Sub('1') + Bord('1') + Bord('1'))
    Tri_Square_Pyr(Sub('1') + Bord('2') + Bord('1'), Sub('2') + Bord('0') + Bord('1'))
    Tri_Square_Pyr(Sub('2') + Bord('2') + Bord('1'), Sub('3') + Bord('0') + Bord('1'))
    # edges adjacency constraints
    Tri_Square_Pyr(Bord('0') + Bord('1'), Bord('1') + Bord('0'))
    Tri_Square_Pyr(Bord('1') + Bord('1'), Bord('2') + Bord('0'))
    Tri_Square_Pyr(Bord('2') + Bord('1'), Bord('0') + Bord('0'))
    # constraints on init cells
    init(Sub('0') + Bord('0') + Permut('0'), Sub('4') + Bord('0'))
    init(Sub('0') + Bord('1') + Permut('0'), Sub('1') + Bord('0'))
    init(Sub('1') + Bord('2') + Permut('0'), Sub('2') + Bord('0'))
    init(Sub('3') + Bord('0') + Permut('0'), Sub('4') + Bord('1'))
    init(Sub('3') + Bord('2') + Permut('0'), Sub('6') + Bord('1'))
    init(Sub('4') + Bord('2') + Permut('0'), Sub('6') + Bord('0'))
    init(Sub('4') + Bord('3') + Permut('0'), Sub('5') + Bord('0'))
    init(Sub('6') + Bord('3') + Permut('0'), Sub('8') + Bord('2'))
    init(Sub('7') + Bord('0') + Permut('0'), Sub('8') + Bord('0'))
    # control points
    # control points
    init.initMat[Sub_('2')] = FMat([
        [1, 2.0, 3, 3.0, 3, 2],
        [5, 4.5, 4, 4.5, 5, 5],
        [0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1]]).setTyp('Var')

    init.initMat[Sub_('1')] = FMat([
        [1, 1.0, 1, 2, 3, 2.0],
        [5, 4.5, 4, 4, 4, 4.5],
        [0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1]]).setTyp('Var')

    init.initMat[Sub_('0')] = FMat([
        [0, 0.5, 1, 1.0, 1, 0.5, 0, 0],
        [3, 3.5, 4, 4.5, 5, 5.0, 5, 4],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1]]).setTyp('Var')

    init.initMat[Sub_('3')] = FMat([
        [0.4, 0.2, 0, 0.0, 0, 0.2],
        [2.4, 2.7, 3, 2.5, 2, 2.2],
        [0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1]]).setTyp('Var')

    init.initMat[Sub_('4')] = FMat([
        [1, 0.5, 0, 0.2, 0.4, 0.7, 1, 1.1, 1.2, 1.1],
        [4, 3.5, 3, 2.7, 2.4, 2.2, 2, 2.5, 3.0, 3.5],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]).setTyp('Var')

    init.initMat[Sub_('5')] = FMat([
        [1.2, 1.1, 1, 1.5, 2, 2.0, 2, 1.6],
        [3.0, 2.5, 2, 2.0, 2, 2.5, 3, 3.0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1]]).setTyp('Var')

    init.initMat[Sub_('6')] = FMat([
        [1, 0.7, 0.4, 0.2, 0, 0.0, 0.0, 0.5, 1.0, 1.0],
        [2, 2.2, 2.4, 2.2, 2, 1.5, 1.2, 1.2, 1.2, 1.5],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]).setTyp('Var')

    init.initMat[Sub_('7')] = FMat([
        [1, 0.5, 0.0, 0.0, 0, 0.5],
        [0, 0.6, 1.2, 0.6, 0, 0.0],
        [0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1]]).setTyp('Var')

    init.initMat[Sub_('8')] = FMat([
        [0.0, 0.5, 1, 1.0, 1.0, 0.5],
        [1.2, 0.6, 0, 0.6, 1.2, 1.2],
        [0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1]]).setTyp('Var')

    auto = Auto(init)
    auto.autoSubs(800)
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
