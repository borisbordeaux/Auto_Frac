# -*- coding: utf-8 -*-

# Automatically generated, from file : penta_B2__B2_B2_B2_corner.py, function : modele()

from __future__ import division
import sys
if './../../../../../../python' not in sys.path:
	sys.path.append('./../../../../../../python')
from etat import *

def modele():
	
	etat0 = EtatInit()
	etat1 = Etat('Cell_0',0)
	etat2 = Etat('C2',0)
	etat3 = Etat('s',1)
	
	
	etat0.subs   = {Sub('0'): etat1, }
	
	etat0.eqs = [
		]
	
	
	etat0.space = []
	
	etat0.initMat[Chem([Sub('0')])] = FMat([
		[Coef('Var'  ,-0.800104    ), Coef('Var'  ,-0.911813    ), Coef('Var'  , 0.188044    ), Coef('Var'  , 0.979219    ), Coef('Var'  , 0.368747    ), ], 
		[Coef('Var'  , 0.660911    ), Coef('Var'  ,-0.532005    ), Coef('Var'  ,-1.00676     ), Coef('Var'  ,-0.107549    ), Coef('Var'  , 0.922892    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), ], ])
	
	
	
	etat1.bords   = {Bord('0'): etat2, Bord('1'): etat2, Bord('2'): etat2, Bord('3'): etat2, Bord('4'): etat2, }
	etat1.permuts = {}
	etat1.interns = {Intern('_'): etat1, }
	etat1.subs    = {Sub('0'): etat1, Sub('G', True): Etat.etatPoint, Sub('1'): etat1, Sub('2'): etat1, Sub('3'): etat1, Sub('4'): etat1, Sub('5'): etat1, Sub('6'): etat1, Sub('7'): etat1, Sub('8'): etat1, Sub('9'): etat1, }
	
	etat1.buildIntern()
	
	
	etat1.eqs = [
		(Chem([Bord('0'), Sub('0'), ])	,	Chem([Sub('0'), Bord('0'), ])),
		(Chem([Bord('0'), Sub('1'), ])	,	Chem([Sub('1'), Bord('0'), ])),
		(Chem([Bord('1'), Sub('0'), ])	,	Chem([Sub('2'), Bord('0'), ])),
		(Chem([Bord('1'), Sub('1'), ])	,	Chem([Sub('3'), Bord('0'), ])),
		(Chem([Bord('2'), Sub('0'), ])	,	Chem([Sub('4'), Bord('0'), ])),
		(Chem([Bord('2'), Sub('1'), ])	,	Chem([Sub('5'), Bord('0'), ])),
		(Chem([Bord('3'), Sub('0'), ])	,	Chem([Sub('6'), Bord('0'), ])),
		(Chem([Bord('3'), Sub('1'), ])	,	Chem([Sub('7'), Bord('0'), ])),
		(Chem([Bord('4'), Sub('0'), ])	,	Chem([Sub('8'), Bord('0'), ])),
		(Chem([Bord('4'), Sub('1'), ])	,	Chem([Sub('9'), Bord('0'), ])),
		(Chem([Sub('0'), Bord('2'), Permut('0'), ])	,	Chem([Sub('1'), Bord('3'), ])),
		(Chem([Sub('1'), Bord('1'), Permut('0'), ])	,	Chem([Sub('2'), Bord('4'), ])),
		(Chem([Sub('2'), Bord('2'), Permut('0'), ])	,	Chem([Sub('3'), Bord('3'), ])),
		(Chem([Sub('3'), Bord('1'), Permut('0'), ])	,	Chem([Sub('4'), Bord('4'), ])),
		(Chem([Sub('4'), Bord('2'), Permut('0'), ])	,	Chem([Sub('5'), Bord('3'), ])),
		(Chem([Sub('5'), Bord('1'), Permut('0'), ])	,	Chem([Sub('6'), Bord('4'), ])),
		(Chem([Sub('6'), Bord('2'), Permut('0'), ])	,	Chem([Sub('7'), Bord('3'), ])),
		(Chem([Sub('7'), Bord('1'), Permut('0'), ])	,	Chem([Sub('8'), Bord('4'), ])),
		(Chem([Sub('8'), Bord('2'), Permut('0'), ])	,	Chem([Sub('9'), Bord('3'), ])),
		(Chem([Sub('9'), Bord('1'), Permut('0'), ])	,	Chem([Sub('0'), Bord('4'), ])),
		(Chem([Bord('0'), Bord('1'), ])	,	Chem([Bord('1'), Bord('0'), ])),
		(Chem([Bord('1'), Bord('1'), ])	,	Chem([Bord('2'), Bord('0'), ])),
		(Chem([Bord('2'), Bord('1'), ])	,	Chem([Bord('3'), Bord('0'), ])),
		(Chem([Bord('3'), Bord('1'), ])	,	Chem([Bord('4'), Bord('0'), ])),
		(Chem([Bord('4'), Bord('1'), ])	,	Chem([Bord('0'), Bord('0'), ])),
		]
	
	
	etat1.prim.elems = [Figure(2, [Chem([Bord('0'), Bord('0'), ]), Chem([Bord('1'), Bord('0'), ]), Chem([Bord('2'), Bord('0'), ]), Chem([Bord('3'), Bord('0'), ]), Chem([Bord('4'), Bord('0'), ]), ])]
	etat1.grid.elems = [
		Figure(1, [Chem([Bord('1'), Bord('0'), ]), Chem([Bord('1'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('4'), Bord('0'), ]), Chem([Bord('4'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('2'), Bord('0'), ]), Chem([Bord('2'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('0'), Bord('0'), ]), Chem([Bord('0'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('3'), Bord('0'), ]), Chem([Bord('3'), Bord('1'), ]), ]), ]
	
	
	etat1.space = [Chem([Bord('4'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('2'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('4'), Bord('0'), Intern('0'), Intern('0'), ]), ]
	
	etat1.initMat[Chem([Sub('0')])] = FMat([
		[Coef('Var'  , 1           ), Coef('Const', 0.666667    ), Coef('Var'  , 0.397546    ), Coef('Var'  , 0.31349     ), Coef('Var'  , 0.334445    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.333333    ), Coef('Var'  , 0.388589    ), Coef('Var'  , 0.297232    ), Coef('Var'  , 0.230598    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.118995    ), Coef('Var'  , 0.146597    ), Coef('Var'  , 0.0844784   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  ,-0.0386108   ), Coef('Var'  , 0.069786    ), Coef('Var'  , 0.0980172   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.133481    ), Coef('Var'  , 0.172895    ), Coef('Var'  , 0.252461    ), ], ])
	etat1.initMat[Chem([Sub('G')])] = FMat([
		[Coef('Const', 0.2         )], 
		[Coef('Const', 0.2         )], 
		[Coef('Const', 0.2         )], 
		[Coef('Const', 0.2         )], 
		[Coef('Const', 0.2         )], ])
	etat1.initMat[Chem([Sub('1')])] = FMat([
		[Coef('Const', 0.333333    ), Coef('Const', 0           ), Coef('Var'  , 0.254815    ), Coef('Var'  , 0.31349     ), Coef('Var'  , 0.397546    ), ], 
		[Coef('Const', 0.666667    ), Coef('Var'  , 1           ), Coef('Var'  , 0.31882     ), Coef('Var'  , 0.297232    ), Coef('Var'  , 0.388589    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.2186      ), Coef('Var'  , 0.146597    ), Coef('Var'  , 0.118995    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0926994   ), Coef('Var'  , 0.069786    ), Coef('Var'  ,-0.0386108   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.115066    ), Coef('Var'  , 0.172895    ), Coef('Var'  , 0.133481    ), ], ])
	etat1.initMat[Chem([Sub('2')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.129007    ), Coef('Var'  , 0.178317    ), Coef('Var'  , 0.254815    ), ], 
		[Coef('Var'  , 1           ), Coef('Const', 0.666667    ), Coef('Var'  , 0.37451     ), Coef('Var'  , 0.28825     ), Coef('Var'  , 0.31882     ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.333333    ), Coef('Var'  , 0.378794    ), Coef('Var'  , 0.2762      ), Coef('Var'  , 0.2186      ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.136019    ), Coef('Var'  , 0.15886     ), Coef('Var'  , 0.0926994   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  ,-0.0183307   ), Coef('Var'  , 0.0983732   ), Coef('Var'  , 0.115066    ), ], ])
	etat1.initMat[Chem([Sub('3')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.108979    ), Coef('Var'  , 0.178317    ), Coef('Var'  , 0.129007    ), ], 
		[Coef('Const', 0.333333    ), Coef('Const', 0           ), Coef('Var'  , 0.20787     ), Coef('Var'  , 0.28825     ), Coef('Var'  , 0.37451     ), ], 
		[Coef('Const', 0.666667    ), Coef('Var'  , 1           ), Coef('Var'  , 0.295869    ), Coef('Var'  , 0.2762      ), Coef('Var'  , 0.378794    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.251378    ), Coef('Var'  , 0.15886     ), Coef('Var'  , 0.136019    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.135904    ), Coef('Var'  , 0.0983732   ), Coef('Var'  ,-0.0183307   ), ], ])
	etat1.initMat[Chem([Sub('4')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  ,-0.0219164   ), Coef('Var'  , 0.093477    ), Coef('Var'  , 0.108979    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.117897    ), Coef('Var'  , 0.145682    ), Coef('Var'  , 0.20787     ), ], 
		[Coef('Var'  , 1           ), Coef('Const', 0.666667    ), Coef('Var'  , 0.371159    ), Coef('Var'  , 0.272949    ), Coef('Var'  , 0.295869    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.333333    ), Coef('Var'  , 0.387861    ), Coef('Var'  , 0.299389    ), Coef('Var'  , 0.251378    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.144999    ), Coef('Var'  , 0.188504    ), Coef('Var'  , 0.135904    ), ], ])
	etat1.initMat[Chem([Sub('5')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.109748    ), Coef('Var'  , 0.093477    ), Coef('Var'  ,-0.0219164   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0909019   ), Coef('Var'  , 0.145682    ), Coef('Var'  , 0.117897    ), ], 
		[Coef('Const', 0.333333    ), Coef('Const', 0           ), Coef('Var'  , 0.222838    ), Coef('Var'  , 0.272949    ), Coef('Var'  , 0.371159    ), ], 
		[Coef('Const', 0.666667    ), Coef('Var'  , 1           ), Coef('Var'  , 0.323189    ), Coef('Var'  , 0.299389    ), Coef('Var'  , 0.387861    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.253323    ), Coef('Var'  , 0.188504    ), Coef('Var'  , 0.144999    ), ], ])
	etat1.initMat[Chem([Sub('6')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.126431    ), Coef('Var'  , 0.16492     ), Coef('Var'  , 0.109748    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  ,-0.039441    ), Coef('Var'  , 0.0689261   ), Coef('Var'  , 0.0909019   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.125632    ), Coef('Var'  , 0.154097    ), Coef('Var'  , 0.222838    ), ], 
		[Coef('Var'  , 1           ), Coef('Const', 0.666667    ), Coef('Var'  , 0.393432    ), Coef('Var'  , 0.302679    ), Coef('Var'  , 0.323189    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.333333    ), Coef('Var'  , 0.393946    ), Coef('Var'  , 0.309377    ), Coef('Var'  , 0.253323    ), ], ])
	etat1.initMat[Chem([Sub('7')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.231817    ), Coef('Var'  , 0.16492     ), Coef('Var'  , 0.126431    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.089397    ), Coef('Var'  , 0.0689261   ), Coef('Var'  ,-0.039441    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0998573   ), Coef('Var'  , 0.154097    ), Coef('Var'  , 0.125632    ), ], 
		[Coef('Const', 0.333333    ), Coef('Const', 0           ), Coef('Var'  , 0.248693    ), Coef('Var'  , 0.302679    ), Coef('Var'  , 0.393432    ), ], 
		[Coef('Const', 0.666667    ), Coef('Var'  , 1           ), Coef('Var'  , 0.330236    ), Coef('Var'  , 0.309377    ), Coef('Var'  , 0.393946    ), ], ])
	etat1.initMat[Chem([Sub('8')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0.333333    ), Coef('Var'  , 0.379577    ), Coef('Var'  , 0.297312    ), Coef('Var'  , 0.231817    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.123231    ), Coef('Var'  , 0.149055    ), Coef('Var'  , 0.089397    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  ,-0.0269774   ), Coef('Var'  , 0.0712294   ), Coef('Var'  , 0.0998573   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.136483    ), Coef('Var'  , 0.171355    ), Coef('Var'  , 0.248693    ), ], 
		[Coef('Var'  , 1           ), Coef('Const', 0.666667    ), Coef('Var'  , 0.387686    ), Coef('Var'  , 0.311048    ), Coef('Var'  , 0.330236    ), ], ])
	etat1.initMat[Chem([Sub('9')])] = FMat([
		[Coef('Const', 0.666667    ), Coef('Var'  , 1           ), Coef('Var'  , 0.334445    ), Coef('Var'  , 0.297312    ), Coef('Var'  , 0.379577    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.230598    ), Coef('Var'  , 0.149055    ), Coef('Var'  , 0.123231    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0844784   ), Coef('Var'  , 0.0712294   ), Coef('Var'  ,-0.0269774   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0980172   ), Coef('Var'  , 0.171355    ), Coef('Var'  , 0.136483    ), ], 
		[Coef('Const', 0.333333    ), Coef('Const', 0           ), Coef('Var'  , 0.252461    ), Coef('Var'  , 0.311048    ), Coef('Var'  , 0.387686    ), ], ])
	
	
	
	etat2.bords   = {Bord('0'): etat3, Bord('1'): etat3, }
	etat2.permuts = {Permut('0'): etat2, }
	etat2.interns = {Intern('_'): etat2, }
	etat2.subs    = {Sub('0'): etat2, Sub('G', True): Etat.etatPoint, Sub('1'): etat2, }
	
	etat2.buildIntern()
	etat2.fm_[Permut('0')] = PMat(2, [1, 0, ])
	
	
	etat2.eqs = [
		(Chem([Permut('0'), Bord('0'), ])	,	Chem([Bord('1')])),
		(Chem([Permut('0'), Bord('1'), ])	,	Chem([Bord('0')])),
		(Chem([Permut('0'), Sub('0'), ])	,	Chem([Sub('1'), Permut('0'), ])),
		(Chem([Permut('0'), Sub('1'), ])	,	Chem([Sub('0'), Permut('0'), ])),
		(Chem([Bord('0'), Sub('0'), ])	,	Chem([Sub('0'), Bord('0'), ])),
		(Chem([Bord('1'), Sub('0'), ])	,	Chem([Sub('1'), Bord('1'), ])),
		]
	
	
	etat2.prim.elems = []
	etat2.grid.elems = [Figure(1, [Chem([Bord('0')]), Chem([Bord('1')]), ])]
	
	
	etat2.space = [Chem([Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Intern('0'), Intern('0'), ]), ]
	
	etat2.initMat[Chem([Sub('0')])] = FMat([
		[Coef('Var'  , 1           ), Coef('Const', 0.666667    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.333333    ), ], ])
	etat2.initMat[Chem([Sub('G')])] = FMat([
		[Coef('Const', 0.5         )], 
		[Coef('Const', 0.5         )], ])
	etat2.initMat[Chem([Sub('1')])] = FMat([
		[Coef('Const', 0.333333    ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.666667    ), Coef('Var'  , 1           ), ], ])
	
	
	
	etat3.bords   = {}
	etat3.permuts = {}
	etat3.interns = {Intern('_'): etat3, }
	etat3.subs    = {Sub('0'): etat3, Sub('G', True): Etat.etatPoint, }
	
	etat3.buildIntern()
	
	
	etat3.eqs = [
		]
	
	
	etat3.prim.elems = []
	etat3.grid.elems = []
	
	
	etat3.space = [Chem([Intern('0'), Intern('0'), ])]
	
	etat3.initMat[Chem([Sub('0')])] = FMat([[Coef('Var'  , 1           )]])
	etat3.initMat[Chem([Sub('G')])] = FMat([[Coef('Const', 1           )]])
	
	
	
	etat0.xmlDesc = ''
	return etat0

if __name__ == '__main__':
	print('modele()')
	init = modele()
	print('check()')
	init.check()
	print('solve()')
	init.solve()
	init.display()
	print('End')
