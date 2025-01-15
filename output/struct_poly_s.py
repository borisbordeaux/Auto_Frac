# -*- coding: utf-8 -*-

# Automatically generated, from file : struct_poly_s.py, function : modele()

from __future__ import division
import sys
if './../../../../../../python' not in sys.path:
	sys.path.append('./../../../../../../python')
from etat import *

def modele():
	
	etat0 = EtatInit()
	etat1 = Etat('Cube',0)
	etat2 = Etat('Tri_Penta_Pyr',0)
	etat3 = Etat('Icosa',0)
	etat4 = Etat('Tetra',0)
	etat5 = Etat('Base_Penta_Pyr',0)
	etat6 = Etat('Base_Square_Pyr',0)
	etat7 = Etat('Dodeca',0)
	etat8 = Etat('Octa',0)
	etat9 = Etat('Tri_Square_Pyr',0)
	etat10 = Etat('B2',1)
	etat11 = Etat('B4',1)
	etat12 = Etat('B3',1)
	etat13 = Etat('s',1)
	
	
	etat0.subs   = {Sub('8'): etat9, Sub('7'): etat8, Sub('6'): etat7, Sub('5'): etat6, Sub('4'): etat5, Sub('3'): etat4, Sub('2'): etat3, Sub('1'): etat2, Sub('0'): etat1, }
	
	etat0.eqs = [
		(Chem([Sub('0'), Bord('0'), Permut('0'), ])	,	Chem([Sub('4'), Bord('0'), ])),
		(Chem([Sub('0'), Bord('1'), Permut('0'), ])	,	Chem([Sub('1'), Bord('0'), ])),
		(Chem([Sub('1'), Bord('2'), Permut('0'), ])	,	Chem([Sub('2'), Bord('0'), ])),
		(Chem([Sub('3'), Bord('0'), Permut('0'), ])	,	Chem([Sub('4'), Bord('1'), ])),
		(Chem([Sub('3'), Bord('2'), Permut('0'), ])	,	Chem([Sub('6'), Bord('1'), ])),
		(Chem([Sub('4'), Bord('2'), Permut('0'), ])	,	Chem([Sub('6'), Bord('0'), ])),
		(Chem([Sub('4'), Bord('3'), Permut('0'), ])	,	Chem([Sub('5'), Bord('0'), ])),
		(Chem([Sub('6'), Bord('3'), Permut('0'), ])	,	Chem([Sub('8'), Bord('2'), ])),
		(Chem([Sub('7'), Bord('0'), Permut('0'), ])	,	Chem([Sub('8'), Bord('0'), ])),
		]
	
	
	etat0.space = []
	
	etat0.initMat[Chem([Sub('8')])] = FMat([
		[Coef('Const', 0           ), Coef('Var'  , 0.5         ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Const', 1           ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 1.2         ), Coef('Var'  , 0.6         ), Coef('Var'  , 0           ), Coef('Var'  , 0.6         ), Coef('Const', 1.2         ), Coef('Const', 1.2         ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0           ), Coef('Var'  , 0           ), Coef('Var'  , 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Const', 1           ), Coef('Const', 1           ), ], ])
	etat0.initMat[Chem([Sub('7')])] = FMat([
		[Coef('Var'  , 1           ), Coef('Var'  , 0.5         ), Coef('Const', 0           ), Coef('Var'  , 0           ), Coef('Var'  , 0           ), Coef('Var'  , 0.5         ), ], 
		[Coef('Var'  , 0           ), Coef('Var'  , 0.6         ), Coef('Const', 1.2         ), Coef('Var'  , 0.6         ), Coef('Var'  , 0           ), Coef('Var'  , 0           ), ], 
		[Coef('Var'  , 0           ), Coef('Var'  , 0           ), Coef('Const', 0           ), Coef('Var'  , 0           ), Coef('Var'  , 0           ), Coef('Var'  , 0           ), ], 
		[Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Const', 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), ], ])
	etat0.initMat[Chem([Sub('6')])] = FMat([
		[Coef('Const', 1           ), Coef('Const', 0.7         ), Coef('Const', 0.4         ), Coef('Const', 0.2         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 1           ), ], 
		[Coef('Const', 2           ), Coef('Const', 2.2         ), Coef('Const', 2.4         ), Coef('Const', 2.2         ), Coef('Const', 2           ), Coef('Const', 1.5         ), Coef('Const', 1.2         ), Coef('Const', 1.2         ), Coef('Const', 1.2         ), Coef('Const', 1.5         ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 1           ), Coef('Const', 1           ), Coef('Const', 1           ), Coef('Const', 1           ), Coef('Const', 1           ), Coef('Const', 1           ), Coef('Const', 1           ), Coef('Const', 1           ), Coef('Const', 1           ), Coef('Const', 1           ), ], ])
	etat0.initMat[Chem([Sub('5')])] = FMat([
		[Coef('Const', 1.2         ), Coef('Const', 1.1         ), Coef('Const', 1           ), Coef('Const', 1.5         ), Coef('Const', 2           ), Coef('Const', 2           ), Coef('Const', 2           ), Coef('Const', 1.6         ), ], 
		[Coef('Const', 3           ), Coef('Const', 2.5         ), Coef('Const', 2           ), Coef('Const', 2           ), Coef('Const', 2           ), Coef('Const', 2.5         ), Coef('Const', 3           ), Coef('Const', 3           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 1           ), Coef('Const', 1           ), Coef('Const', 1           ), Coef('Const', 1           ), Coef('Const', 1           ), Coef('Const', 1           ), Coef('Const', 1           ), Coef('Const', 1           ), ], ])
	etat0.initMat[Chem([Sub('4')])] = FMat([
		[Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0.2         ), Coef('Const', 0.4         ), Coef('Const', 0.7         ), Coef('Const', 1           ), Coef('Const', 1.1         ), Coef('Const', 1.2         ), Coef('Const', 1.1         ), ], 
		[Coef('Const', 4           ), Coef('Const', 3.5         ), Coef('Const', 3           ), Coef('Const', 2.7         ), Coef('Const', 2.4         ), Coef('Const', 2.2         ), Coef('Const', 2           ), Coef('Const', 2.5         ), Coef('Const', 3           ), Coef('Const', 3.5         ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 1           ), Coef('Const', 1           ), Coef('Const', 1           ), Coef('Const', 1           ), Coef('Const', 1           ), Coef('Const', 1           ), Coef('Const', 1           ), Coef('Const', 1           ), Coef('Const', 1           ), Coef('Const', 1           ), ], ])
	etat0.initMat[Chem([Sub('3')])] = FMat([
		[Coef('Const', 0.4         ), Coef('Const', 0.2         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.2         ), ], 
		[Coef('Const', 2.4         ), Coef('Const', 2.7         ), Coef('Const', 3           ), Coef('Const', 2.5         ), Coef('Const', 2           ), Coef('Const', 2.2         ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 1           ), Coef('Const', 1           ), Coef('Const', 1           ), Coef('Const', 1           ), Coef('Const', 1           ), Coef('Const', 1           ), ], ])
	etat0.initMat[Chem([Sub('2')])] = FMat([
		[Coef('Const', 1           ), Coef('Const', 2           ), Coef('Const', 3           ), Coef('Const', 3           ), Coef('Const', 3           ), Coef('Const', 2           ), ], 
		[Coef('Const', 5           ), Coef('Const', 4.5         ), Coef('Const', 4           ), Coef('Const', 4.5         ), Coef('Const', 5           ), Coef('Const', 5           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 1           ), Coef('Const', 1           ), Coef('Const', 1           ), Coef('Const', 1           ), Coef('Const', 1           ), Coef('Const', 1           ), ], ])
	etat0.initMat[Chem([Sub('1')])] = FMat([
		[Coef('Const', 1           ), Coef('Const', 1           ), Coef('Const', 1           ), Coef('Const', 2           ), Coef('Const', 3           ), Coef('Const', 2           ), ], 
		[Coef('Const', 5           ), Coef('Const', 4.5         ), Coef('Const', 4           ), Coef('Const', 4           ), Coef('Const', 4           ), Coef('Const', 4.5         ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 1           ), Coef('Const', 1           ), Coef('Const', 1           ), Coef('Const', 1           ), Coef('Const', 1           ), Coef('Const', 1           ), ], ])
	etat0.initMat[Chem([Sub('0')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 1           ), Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 3           ), Coef('Const', 3.5         ), Coef('Const', 4           ), Coef('Const', 4.5         ), Coef('Const', 5           ), Coef('Const', 5           ), Coef('Const', 5           ), Coef('Const', 4           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 1           ), Coef('Const', 1           ), Coef('Const', 1           ), Coef('Const', 1           ), Coef('Const', 1           ), Coef('Const', 1           ), Coef('Const', 1           ), Coef('Const', 1           ), ], ])
	
	
	
	etat1.bords   = {Bord('3'): etat10, Bord('2'): etat10, Bord('1'): etat10, Bord('0'): etat10, }
	etat1.permuts = {}
	etat1.interns = {Intern('_'): etat1, }
	etat1.subs    = {Sub('4'): etat1, Sub('3'): etat1, Sub('2'): etat1, Sub('1'): etat1, Sub('0'): etat1, Sub('G', True): Etat.etatPoint, }
	
	etat1.buildIntern()
	
	
	etat1.eqs = [
		(Chem([Bord('0'), Sub('0'), Permut('0'), ])	,	Chem([Sub('0'), Bord('2'), ])),
		(Chem([Bord('3'), Sub('1'), Permut('0'), ])	,	Chem([Sub('0'), Bord('3'), ])),
		(Chem([Bord('1'), Sub('1'), Permut('0'), ])	,	Chem([Sub('1'), Bord('0'), ])),
		(Chem([Bord('2'), Sub('0'), Permut('0'), ])	,	Chem([Sub('1'), Bord('3'), ])),
		(Chem([Bord('2'), Sub('1'), Permut('0'), ])	,	Chem([Sub('2'), Bord('0'), ])),
		(Chem([Bord('3'), Sub('0'), Permut('0'), ])	,	Chem([Sub('2'), Bord('3'), ])),
		(Chem([Bord('1'), Sub('0'), Permut('0'), ])	,	Chem([Sub('3'), Bord('1'), ])),
		(Chem([Bord('0'), Sub('1'), Permut('0'), ])	,	Chem([Sub('3'), Bord('2'), ])),
		(Chem([Sub('0'), Bord('0'), Bord('1'), ])	,	Chem([Sub('4'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('1'), Bord('1'), ])	,	Chem([Sub('3'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('3'), Bord('1'), ])	,	Chem([Sub('2'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('0'), Bord('1'), ])	,	Chem([Sub('3'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('1'), Bord('1'), ])	,	Chem([Sub('4'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('2'), Bord('1'), ])	,	Chem([Sub('2'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('1'), Bord('1'), ])	,	Chem([Sub('4'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('3'), Bord('3'), Bord('1'), ])	,	Chem([Sub('4'), Bord('1'), Bord('1'), ])),
		(Chem([Bord('0'), Bord('1'), ])	,	Chem([Bord('1'), Bord('0'), ])),
		(Chem([Bord('1'), Bord('1'), ])	,	Chem([Bord('2'), Bord('0'), ])),
		(Chem([Bord('2'), Bord('1'), ])	,	Chem([Bord('3'), Bord('0'), ])),
		(Chem([Bord('3'), Bord('1'), ])	,	Chem([Bord('0'), Bord('0'), ])),
		]
	
	
	etat1.prim.elems = [Figure(2, [Chem([Bord('0'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('0'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('0'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('0'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('1'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('1'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('1'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('1'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('2'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('2'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('2'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('2'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('3'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('3'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('3'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('3'), Sub('1'), Sub('1'), Bord('0'), ]), ])]
	etat1.grid.elems = [
		Figure(1, [Chem([Bord('0'), Bord('0'), ]), Chem([Bord('0'), Intern(''), ]), Chem([Bord('0'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('1'), Bord('0'), ]), Chem([Bord('1'), Intern(''), ]), Chem([Bord('1'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('2'), Bord('0'), ]), Chem([Bord('2'), Intern(''), ]), Chem([Bord('2'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('3'), Bord('0'), ]), Chem([Bord('3'), Intern(''), ]), Chem([Bord('3'), Bord('1'), ]), ]), ]
	
	
	etat1.space = [Chem([Bord('0'), Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('0'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('2'), Intern('0'), Intern('0'), ]), Chem([Bord('2'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('3'), Intern('0'), Intern('0'), ]), ]
	
	etat1.initMat[Chem([Sub('4')])] = FMat([
		[Coef('Var'  , 0.147919    ), Coef('Var'  , 0.136798    ), Coef('Var'  , 0.100915    ), Coef('Var'  , 0.125823    ), Coef('Var'  , 0.134452    ), Coef('Var'  , 0.152705    ), Coef('Var'  , 0.180902    ), Coef('Var'  , 0.162318    ), ], 
		[Coef('Var'  , 0.0951598   ), Coef('Var'  , 0.108775    ), Coef('Var'  , 0.0938293   ), Coef('Var'  , 0.140289    ), Coef('Var'  , 0.181682    ), Coef('Var'  , 0.173244    ), Coef('Var'  , 0.181341    ), Coef('Var'  , 0.140705    ), ], 
		[Coef('Var'  , 0.0699154   ), Coef('Var'  , 0.0997017   ), Coef('Var'  , 0.124035    ), Coef('Var'  , 0.148741    ), Coef('Var'  , 0.178055    ), Coef('Var'  , 0.148555    ), Coef('Var'  , 0.1234      ), Coef('Var'  , 0.0982526   ), ], 
		[Coef('Var'  , 0.0737547   ), Coef('Var'  , 0.118704    ), Coef('Var'  , 0.166495    ), Coef('Var'  , 0.155962    ), Coef('Var'  , 0.166392    ), Coef('Var'  , 0.119919    ), Coef('Var'  , 0.0745703   ), Coef('Var'  , 0.0830818   ), ], 
		[Coef('Var'  , 0.106738    ), Coef('Var'  , 0.121292    ), Coef('Var'  , 0.154623    ), Coef('Var'  , 0.126288    ), Coef('Var'  , 0.112698    ), Coef('Var'  , 0.089648    ), Coef('Var'  , 0.0617699   ), Coef('Var'  , 0.0853783   ), ], 
		[Coef('Var'  , 0.185457    ), Coef('Var'  , 0.174612    ), Coef('Var'  , 0.17898     ), Coef('Var'  , 0.134514    ), Coef('Var'  , 0.0882581   ), Coef('Var'  , 0.101308    ), Coef('Var'  , 0.0917605   ), Coef('Var'  , 0.142981    ), ], 
		[Coef('Var'  , 0.153075    ), Coef('Var'  , 0.115999    ), Coef('Var'  , 0.101376    ), Coef('Var'  , 0.081487    ), Coef('Var'  , 0.0633538   ), Coef('Var'  , 0.0942597   ), Coef('Var'  , 0.116788    ), Coef('Var'  , 0.12872     ), ], 
		[Coef('Var'  , 0.167982    ), Coef('Var'  , 0.124118    ), Coef('Var'  , 0.0797459   ), Coef('Var'  , 0.0868966   ), Coef('Var'  , 0.0751088   ), Coef('Var'  , 0.120362    ), Coef('Var'  , 0.169468    ), Coef('Var'  , 0.158564    ), ], ])
	etat1.initMat[Chem([Sub('3')])] = FMat([
		[Coef('Var'  , 0.134452    ), Coef('Var'  , 0.068183    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.190382    ), ], 
		[Coef('Var'  , 0.181682    ), Coef('Var'  , 0.0880548   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.334701    ), ], 
		[Coef('Var'  , 0.178055    ), Coef('Var'  , 0.20992     ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.211681    ), ], 
		[Coef('Var'  , 0.166392    ), Coef('Var'  , 0.326452    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.077553    ), ], 
		[Coef('Var'  , 0.112698    ), Coef('Var'  , 0.18017     ), Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0571296   ), ], 
		[Coef('Var'  , 0.0882581   ), Coef('Var'  , 0.0508631   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0508472   ), ], 
		[Coef('Var'  , 0.0633538   ), Coef('Var'  , 0.0343618   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0361739   ), ], 
		[Coef('Var'  , 0.0751088   ), Coef('Var'  , 0.041995    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0415327   ), ], ])
	etat1.initMat[Chem([Sub('2')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0785602   ), Coef('Var'  , 0.147919    ), Coef('Var'  , 0.202995    ), Coef('Const', 0.25        ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.056134    ), Coef('Var'  , 0.0951598   ), Coef('Var'  , 0.0551916   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0375517   ), Coef('Var'  , 0.0699154   ), Coef('Var'  , 0.0379528   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0412029   ), Coef('Var'  , 0.0737547   ), Coef('Var'  , 0.0416237   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.175055    ), Coef('Var'  , 0.106738    ), Coef('Var'  , 0.0522215   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.338256    ), Coef('Var'  , 0.185457    ), Coef('Var'  , 0.0917174   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.194366    ), Coef('Var'  , 0.153075    ), Coef('Var'  , 0.193032    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0788742   ), Coef('Var'  , 0.167982    ), Coef('Var'  , 0.325266    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), ], ])
	etat1.initMat[Chem([Sub('1')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0594253   ), Coef('Var'  , 0.100915    ), Coef('Var'  , 0.0589117   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0539778   ), Coef('Var'  , 0.0938293   ), Coef('Var'  , 0.0538793   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.186417    ), Coef('Var'  , 0.124035    ), Coef('Var'  , 0.0616154   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.326815    ), Coef('Var'  , 0.166495    ), Coef('Var'  , 0.078507    ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.194425    ), Coef('Var'  , 0.154623    ), Coef('Var'  , 0.195414    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0856151   ), Coef('Var'  , 0.17898     ), Coef('Var'  , 0.332615    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0471981   ), Coef('Var'  , 0.101376    ), Coef('Var'  , 0.17195     ), Coef('Const', 0.25        ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0461272   ), Coef('Var'  , 0.0797459   ), Coef('Var'  , 0.0471081   ), Coef('Const', 0           ), Coef('Const', 0           ), ], ])
	etat1.initMat[Chem([Sub('0')])] = FMat([
		[Coef('Const', 0.25        ), Coef('Var'  , 0.210484    ), Coef('Var'  , 0.180902    ), Coef('Var'  , 0.209788    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0867094   ), Coef('Var'  , 0.181341    ), Coef('Var'  , 0.334947    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0614869   ), Coef('Var'  , 0.1234      ), Coef('Var'  , 0.186126    ), Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0420793   ), Coef('Var'  , 0.0745703   ), Coef('Var'  , 0.0419402   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0331574   ), Coef('Var'  , 0.0617699   ), Coef('Var'  , 0.0332645   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.052837    ), Coef('Var'  , 0.0917605   ), Coef('Var'  , 0.0524907   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.25        ), Coef('Var'  , 0.18361     ), Coef('Var'  , 0.116788    ), Coef('Var'  , 0.0599191   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.5         ), Coef('Var'  , 0.329636    ), Coef('Var'  , 0.169468    ), Coef('Var'  , 0.0815243   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), ], ])
	etat1.initMat[Chem([Sub('G')])] = FMat([
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], ])
	
	
	
	etat2.bords   = {Bord('2'): etat11, Bord('1'): etat10, Bord('0'): etat10, }
	etat2.permuts = {}
	etat2.interns = {Intern('_'): etat2, }
	etat2.subs    = {Sub('4'): etat2, Sub('3'): etat2, Sub('2'): etat5, Sub('1'): etat2, Sub('0'): etat2, Sub('G', True): Etat.etatPoint, }
	
	etat2.buildIntern()
	
	
	etat2.eqs = [
		(Chem([Bord('0'), Sub('0'), Permut('0'), ])	,	Chem([Sub('0'), Bord('1'), ])),
		(Chem([Bord('2'), Sub('3'), Permut('0'), ])	,	Chem([Sub('0'), Bord('2'), ])),
		(Chem([Bord('2'), Sub('2'), Permut('0'), ])	,	Chem([Sub('1'), Bord('2'), ])),
		(Chem([Bord('1'), Sub('0'), Permut('0'), ])	,	Chem([Sub('2'), Bord('1'), ])),
		(Chem([Bord('0'), Sub('1'), Permut('0'), ])	,	Chem([Sub('2'), Bord('2'), ])),
		(Chem([Bord('2'), Sub('1'), Permut('0'), ])	,	Chem([Sub('3'), Bord('2'), ])),
		(Chem([Bord('1'), Sub('1'), Permut('0'), ])	,	Chem([Sub('4'), Bord('0'), ])),
		(Chem([Bord('2'), Sub('0'), Permut('0'), ])	,	Chem([Sub('4'), Bord('2'), ])),
		(Chem([Sub('0'), Bord('0'), Bord('1'), ])	,	Chem([Sub('2'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('2'), Bord('1'), ])	,	Chem([Sub('1'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('0'), Bord('1'), ])	,	Chem([Sub('2'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('2'), Bord('1'), ])	,	Chem([Sub('3'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('0'), Bord('1'), ])	,	Chem([Sub('4'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('4'), Bord('1'), ])	,	Chem([Sub('3'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('3'), Bord('2'), Bord('1'), ])	,	Chem([Sub('4'), Bord('1'), Bord('1'), ])),
		(Chem([Bord('0'), Bord('1'), ])	,	Chem([Bord('1'), Bord('0'), ])),
		(Chem([Bord('1'), Bord('1'), ])	,	Chem([Bord('2'), Bord('0'), ])),
		(Chem([Bord('2'), Bord('1'), ])	,	Chem([Bord('0'), Bord('0'), ])),
		]
	
	
	etat2.prim.elems = [Figure(2, [Chem([Bord('0'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('0'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('0'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('0'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('1'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('1'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('1'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('1'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('2'), Sub('0'), Bord('0'), ]), Chem([Bord('2'), Sub('1'), Bord('0'), ]), Chem([Bord('2'), Sub('2'), Bord('0'), ]), Chem([Bord('2'), Sub('3'), Bord('0'), ]), ])]
	etat2.grid.elems = [
		Figure(1, [Chem([Bord('0'), Bord('0'), ]), Chem([Bord('0'), Intern(''), ]), Chem([Bord('0'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('1'), Bord('0'), ]), Chem([Bord('1'), Intern(''), ]), Chem([Bord('1'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('2'), Bord('0'), ]), Chem([Bord('2'), Intern(''), ]), Chem([Bord('2'), Bord('1'), ]), ]), ]
	
	
	etat2.space = [Chem([Bord('0'), Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('0'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('2'), Intern('0'), Intern('0'), ]), ]
	
	etat2.initMat[Chem([Sub('4')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0323745   ), Coef('Const', 0.0625      ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.00229384  ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.125029    ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.249097    ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.403938    ), Coef('Const', 0.5625      ), Coef('Const', 0.75        ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.187268    ), Coef('Const', 0.375       ), Coef('Const', 0.25        ), ], ])
	etat2.initMat[Chem([Sub('3')])] = FMat([
		[Coef('Const', 0.0625      ), Coef('Var'  , 0.103006    ), Coef('Var'  , 0.135806    ), Coef('Var'  , 0.196544    ), Coef('Const', 0.25        ), Coef('Const', 0.125       ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0601432   ), Coef('Var'  , 0.0914779   ), Coef('Var'  , 0.0618862   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0540186   ), Coef('Var'  , 0.105029    ), Coef('Var'  , 0.0537496   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.084223    ), Coef('Var'  , 0.160114    ), Coef('Var'  , 0.0833565   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.5625      ), Coef('Var'  , 0.392031    ), Coef('Var'  , 0.254709    ), Coef('Var'  , 0.238245    ), Coef('Const', 0.25        ), Coef('Const', 0.375       ), ], 
		[Coef('Const', 0.375       ), Coef('Var'  , 0.306579    ), Coef('Var'  , 0.252863    ), Coef('Var'  , 0.366219    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), ], ])
	etat2.initMat[Chem([Sub('2')])] = FMat([
		[Coef('Var'  , 0.135806    ), Coef('Var'  , 0.0716832   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.226324    ), Coef('Var'  , 0.240178    ), Coef('Var'  , 0.171846    ), ], 
		[Coef('Var'  , 0.0914779   ), Coef('Var'  , 0.0623507   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.328006    ), Coef('Var'  , 0.16019     ), Coef('Var'  , 0.142491    ), ], 
		[Coef('Var'  , 0.105029    ), Coef('Var'  , 0.178991    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.196916    ), Coef('Var'  , 0.123646    ), Coef('Var'  , 0.125596    ), ], 
		[Coef('Var'  , 0.160114    ), Coef('Var'  , 0.330044    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0511361   ), Coef('Var'  , 0.077863    ), Coef('Var'  , 0.132079    ), ], 
		[Coef('Var'  , 0.254709    ), Coef('Var'  , 0.237268    ), Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0750442   ), Coef('Var'  , 0.142796    ), Coef('Var'  , 0.187081    ), ], 
		[Coef('Var'  , 0.252863    ), Coef('Var'  , 0.119663    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.122574    ), Coef('Var'  , 0.255326    ), Coef('Var'  , 0.240907    ), ], ])
	etat2.initMat[Chem([Sub('1')])] = FMat([
		[Coef('Const', 0.25        ), Coef('Var'  , 0.227089    ), Coef('Var'  , 0.240178    ), Coef('Var'  , 0.380936    ), Coef('Const', 0.5625      ), Coef('Const', 0.375       ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0811943   ), Coef('Var'  , 0.16019     ), Coef('Var'  , 0.0813146   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0729639   ), Coef('Var'  , 0.123646    ), Coef('Var'  , 0.0727321   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0498455   ), Coef('Var'  , 0.077863    ), Coef('Var'  , 0.0498886   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.25        ), Coef('Var'  , 0.199367    ), Coef('Var'  , 0.142796    ), Coef('Var'  , 0.107393    ), Coef('Const', 0.0625      ), Coef('Const', 0.125       ), ], 
		[Coef('Const', 0.5         ), Coef('Var'  , 0.36954     ), Coef('Var'  , 0.255326    ), Coef('Var'  , 0.307737    ), Coef('Const', 0.375       ), Coef('Const', 0.5         ), ], ])
	etat2.initMat[Chem([Sub('0')])] = FMat([
		[Coef('Const', 0.5625      ), Coef('Var'  , 0.403712    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.75        ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.249709    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.126221    ), Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.00164593  ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.0625      ), Coef('Var'  , 0.0314388   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.375       ), Coef('Var'  , 0.187274    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), ], ])
	etat2.initMat[Chem([Sub('G')])] = FMat([
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], ])
	
	
	
	etat3.bords   = {Bord('2'): etat11, Bord('1'): etat11, Bord('0'): etat11, }
	etat3.permuts = {}
	etat3.interns = {Intern('_'): etat3, }
	etat3.subs    = {Sub('8'): etat3, Sub('7'): etat3, Sub('6'): etat3, Sub('5'): etat3, Sub('4'): etat3, Sub('3'): etat3, Sub('2'): etat3, Sub('1'): etat3, Sub('0'): etat3, Sub('G', True): Etat.etatPoint, Sub('10'): etat3, Sub('9'): etat3, Sub('18'): etat3, Sub('17'): etat3, Sub('16'): etat3, Sub('15'): etat3, Sub('14'): etat3, Sub('13'): etat3, Sub('12'): etat3, Sub('11'): etat3, }
	
	etat3.buildIntern()
	
	
	etat3.eqs = [
		(Chem([Bord('1'), Sub('2'), Permut('0'), ])	,	Chem([Sub('0'), Bord('1'), ])),
		(Chem([Bord('0'), Sub('2'), Permut('0'), ])	,	Chem([Sub('1'), Bord('2'), ])),
		(Chem([Bord('2'), Sub('2'), Permut('0'), ])	,	Chem([Sub('3'), Bord('0'), ])),
		(Chem([Bord('2'), Sub('0'), Permut('0'), ])	,	Chem([Sub('7'), Bord('0'), ])),
		(Chem([Bord('1'), Sub('3'), Permut('0'), ])	,	Chem([Sub('7'), Bord('1'), ])),
		(Chem([Bord('2'), Sub('1'), Permut('0'), ])	,	Chem([Sub('8'), Bord('2'), ])),
		(Chem([Bord('1'), Sub('0'), Permut('0'), ])	,	Chem([Sub('11'), Bord('0'), ])),
		(Chem([Bord('0'), Sub('3'), Permut('0'), ])	,	Chem([Sub('11'), Bord('1'), ])),
		(Chem([Bord('1'), Sub('1'), Permut('0'), ])	,	Chem([Sub('12'), Bord('2'), ])),
		(Chem([Bord('0'), Sub('0'), Permut('0'), ])	,	Chem([Sub('15'), Bord('0'), ])),
		(Chem([Bord('2'), Sub('3'), Permut('0'), ])	,	Chem([Sub('15'), Bord('1'), ])),
		(Chem([Bord('0'), Sub('1'), Permut('0'), ])	,	Chem([Sub('16'), Bord('2'), ])),
		(Chem([Sub('0'), Bord('0'), Bord('1'), ])	,	Chem([Sub('7'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('1'), Bord('1'), ])	,	Chem([Sub('12'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('2'), Bord('1'), ])	,	Chem([Sub('17'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('0'), Bord('1'), ])	,	Chem([Sub('9'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('1'), Bord('1'), ])	,	Chem([Sub('11'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('2'), Bord('1'), ])	,	Chem([Sub('16'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('0'), Bord('1'), ])	,	Chem([Sub('12'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('1'), Bord('1'), ])	,	Chem([Sub('9'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('2'), Bord('1'), ])	,	Chem([Sub('18'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('3'), Bord('0'), Bord('1'), ])	,	Chem([Sub('8'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('3'), Bord('1'), Bord('1'), ])	,	Chem([Sub('13'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('3'), Bord('2'), Bord('1'), ])	,	Chem([Sub('15'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('4'), Bord('0'), Bord('1'), ])	,	Chem([Sub('14'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('4'), Bord('1'), Bord('1'), ])	,	Chem([Sub('8'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('4'), Bord('2'), Bord('1'), ])	,	Chem([Sub('17'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('5'), Bord('0'), Bord('1'), ])	,	Chem([Sub('13'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('5'), Bord('1'), Bord('1'), ])	,	Chem([Sub('10'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('5'), Bord('2'), Bord('1'), ])	,	Chem([Sub('16'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('6'), Bord('0'), Bord('1'), ])	,	Chem([Sub('10'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('6'), Bord('1'), Bord('1'), ])	,	Chem([Sub('14'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('6'), Bord('2'), Bord('1'), ])	,	Chem([Sub('18'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('7'), Bord('2'), Bord('1'), ])	,	Chem([Sub('8'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('9'), Bord('2'), Bord('1'), ])	,	Chem([Sub('10'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('11'), Bord('2'), Bord('1'), ])	,	Chem([Sub('12'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('13'), Bord('2'), Bord('1'), ])	,	Chem([Sub('14'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('15'), Bord('2'), Bord('1'), ])	,	Chem([Sub('16'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('17'), Bord('2'), Bord('1'), ])	,	Chem([Sub('18'), Bord('2'), Bord('1'), ])),
		(Chem([Bord('0'), Bord('1'), ])	,	Chem([Bord('1'), Bord('0'), ])),
		(Chem([Bord('1'), Bord('1'), ])	,	Chem([Bord('2'), Bord('0'), ])),
		(Chem([Bord('2'), Bord('1'), ])	,	Chem([Bord('0'), Bord('0'), ])),
		]
	
	
	etat3.prim.elems = [Figure(2, [Chem([Bord('0'), Sub('0'), Bord('0'), ]), Chem([Bord('0'), Sub('1'), Bord('0'), ]), Chem([Bord('0'), Sub('2'), Bord('0'), ]), Chem([Bord('0'), Sub('3'), Bord('0'), ]), Chem([Bord('1'), Sub('0'), Bord('0'), ]), Chem([Bord('1'), Sub('1'), Bord('0'), ]), Chem([Bord('1'), Sub('2'), Bord('0'), ]), Chem([Bord('1'), Sub('3'), Bord('0'), ]), Chem([Bord('2'), Sub('0'), Bord('0'), ]), Chem([Bord('2'), Sub('1'), Bord('0'), ]), Chem([Bord('2'), Sub('2'), Bord('0'), ]), Chem([Bord('2'), Sub('3'), Bord('0'), ]), ])]
	etat3.grid.elems = [
		Figure(1, [Chem([Bord('0'), Bord('0'), ]), Chem([Bord('0'), Intern(''), ]), Chem([Bord('0'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('1'), Bord('0'), ]), Chem([Bord('1'), Intern(''), ]), Chem([Bord('1'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('2'), Bord('0'), ]), Chem([Bord('2'), Intern(''), ]), Chem([Bord('2'), Bord('1'), ]), ]), ]
	
	
	etat3.space = [Chem([Bord('0'), Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('0'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('2'), Intern('0'), Intern('0'), ]), ]
	
	etat3.initMat[Chem([Sub('8')])] = FMat([
		[Coef('Const', 0.0625      ), Coef('Var'  , 0.0977311   ), Coef('Var'  , 0.139611    ), Coef('Var'  , 0.189655    ), Coef('Const', 0.25        ), Coef('Const', 0.125       ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.065047    ), Coef('Var'  , 0.116147    ), Coef('Var'  , 0.0659387   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0904946   ), Coef('Var'  , 0.150247    ), Coef('Var'  , 0.092684    ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0424689   ), Coef('Var'  , 0.0800997   ), Coef('Var'  , 0.0433487   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.5625      ), Coef('Var'  , 0.399335    ), Coef('Var'  , 0.257021    ), Coef('Var'  , 0.244239    ), Coef('Const', 0.25        ), Coef('Const', 0.375       ), ], 
		[Coef('Const', 0.375       ), Coef('Var'  , 0.304923    ), Coef('Var'  , 0.256874    ), Coef('Var'  , 0.364135    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), ], ])
	etat3.initMat[Chem([Sub('7')])] = FMat([
		[Coef('Const', 0.0625      ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0328339   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.00155779  ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.0625      ), Coef('Var'  , 0.0325555   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Const', 0.375       ), Coef('Var'  , 0.187443    ), ], 
		[Coef('Const', 0.5625      ), Coef('Const', 0.75        ), Coef('Const', 1           ), Coef('Const', 0.75        ), Coef('Const', 0.5625      ), Coef('Var'  , 0.558476    ), ], 
		[Coef('Const', 0.375       ), Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.187134    ), ], ])
	etat3.initMat[Chem([Sub('6')])] = FMat([
		[Coef('Var'  , 0.177639    ), Coef('Var'  , 0.175836    ), Coef('Var'  , 0.167673    ), Coef('Var'  , 0.166986    ), Coef('Var'  , 0.161108    ), Coef('Var'  , 0.176421    ), ], 
		[Coef('Var'  , 0.163127    ), Coef('Var'  , 0.163765    ), Coef('Var'  , 0.164015    ), Coef('Var'  , 0.183729    ), Coef('Var'  , 0.195694    ), Coef('Var'  , 0.181213    ), ], 
		[Coef('Var'  , 0.186045    ), Coef('Var'  , 0.180621    ), Coef('Var'  , 0.171009    ), Coef('Var'  , 0.175951    ), Coef('Var'  , 0.185338    ), Coef('Var'  , 0.18587     ), ], 
		[Coef('Var'  , 0.142909    ), Coef('Var'  , 0.147258    ), Coef('Var'  , 0.152754    ), Coef('Var'  , 0.135362    ), Coef('Var'  , 0.127393    ), Coef('Var'  , 0.129803    ), ], 
		[Coef('Var'  , 0.16466     ), Coef('Var'  , 0.148415    ), Coef('Var'  , 0.140302    ), Coef('Var'  , 0.150365    ), Coef('Var'  , 0.162999    ), Coef('Var'  , 0.165153    ), ], 
		[Coef('Var'  , 0.16562     ), Coef('Var'  , 0.184105    ), Coef('Var'  , 0.204247    ), Coef('Var'  , 0.187607    ), Coef('Var'  , 0.167467    ), Coef('Var'  , 0.16154     ), ], ])
	etat3.initMat[Chem([Sub('5')])] = FMat([
		[Coef('Var'  , 0.274636    ), Coef('Var'  , 0.208371    ), Coef('Var'  , 0.15904     ), Coef('Var'  , 0.149156    ), Coef('Var'  , 0.166614    ), Coef('Var'  , 0.216447    ), ], 
		[Coef('Var'  , 0.255249    ), Coef('Var'  , 0.20851     ), Coef('Var'  , 0.183918    ), Coef('Var'  , 0.166783    ), Coef('Var'  , 0.159735    ), Coef('Var'  , 0.187588    ), ], 
		[Coef('Var'  , 0.158815    ), Coef('Var'  , 0.168059    ), Coef('Var'  , 0.176503    ), Coef('Var'  , 0.172309    ), Coef('Var'  , 0.164519    ), Coef('Var'  , 0.160031    ), ], 
		[Coef('Var'  , 0.118691    ), Coef('Var'  , 0.150267    ), Coef('Var'  , 0.157708    ), Coef('Var'  , 0.176541    ), Coef('Var'  , 0.174789    ), Coef('Var'  , 0.159938    ), ], 
		[Coef('Var'  , 0.0695689   ), Coef('Var'  , 0.0986905   ), Coef('Var'  , 0.122476    ), Coef('Var'  , 0.115738    ), Coef('Var'  , 0.116688    ), Coef('Var'  , 0.0947489   ), ], 
		[Coef('Var'  , 0.123039    ), Coef('Var'  , 0.166102    ), Coef('Var'  , 0.200354    ), Coef('Var'  , 0.219473    ), Coef('Var'  , 0.217654    ), Coef('Var'  , 0.181248    ), ], ])
	etat3.initMat[Chem([Sub('4')])] = FMat([
		[Coef('Var'  , 0.151012    ), Coef('Var'  , 0.14868     ), Coef('Var'  , 0.138785    ), Coef('Var'  , 0.132453    ), Coef('Var'  , 0.139611    ), Coef('Var'  , 0.147242    ), ], 
		[Coef('Var'  , 0.160571    ), Coef('Var'  , 0.186113    ), Coef('Var'  , 0.194305    ), Coef('Var'  , 0.165212    ), Coef('Var'  , 0.116147    ), Coef('Var'  , 0.148662    ), ], 
		[Coef('Var'  , 0.192097    ), Coef('Var'  , 0.197936    ), Coef('Var'  , 0.195328    ), Coef('Var'  , 0.187786    ), Coef('Var'  , 0.150247    ), Coef('Var'  , 0.190013    ), ], 
		[Coef('Var'  , 0.15555     ), Coef('Var'  , 0.1398      ), Coef('Var'  , 0.128391    ), Coef('Var'  , 0.110192    ), Coef('Var'  , 0.0800997   ), Coef('Var'  , 0.117279    ), ], 
		[Coef('Var'  , 0.189526    ), Coef('Var'  , 0.173085    ), Coef('Var'  , 0.175743    ), Coef('Var'  , 0.205496    ), Coef('Var'  , 0.257021    ), Coef('Var'  , 0.206288    ), ], 
		[Coef('Var'  , 0.151244    ), Coef('Var'  , 0.154386    ), Coef('Var'  , 0.167447    ), Coef('Var'  , 0.198861    ), Coef('Var'  , 0.256874    ), Coef('Var'  , 0.190515    ), ], ])
	etat3.initMat[Chem([Sub('3')])] = FMat([
		[Coef('Const', 0.5625      ), Coef('Const', 0.375       ), Coef('Const', 0.25        ), Coef('Var'  , 0.228357    ), Coef('Var'  , 0.230585    ), Coef('Var'  , 0.383842    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0673801   ), Coef('Var'  , 0.120501    ), Coef('Var'  , 0.0660199   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0713724   ), Coef('Var'  , 0.123754    ), Coef('Var'  , 0.0706872   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0538016   ), Coef('Var'  , 0.0968467   ), Coef('Var'  , 0.0563654   ), ], 
		[Coef('Const', 0.0625      ), Coef('Const', 0.125       ), Coef('Const', 0.25        ), Coef('Var'  , 0.206877    ), Coef('Var'  , 0.157168    ), Coef('Var'  , 0.114181    ), ], 
		[Coef('Const', 0.375       ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.372212    ), Coef('Var'  , 0.271145    ), Coef('Var'  , 0.308905    ), ], ])
	etat3.initMat[Chem([Sub('2')])] = FMat([
		[Coef('Var'  , 0.159596    ), Coef('Var'  , 0.132173    ), Coef('Var'  , 0.0944858   ), Coef('Var'  , 0.130273    ), Coef('Var'  , 0.151954    ), Coef('Var'  , 0.161991    ), ], 
		[Coef('Var'  , 0.137765    ), Coef('Var'  , 0.119714    ), Coef('Var'  , 0.0895375   ), Coef('Var'  , 0.116678    ), Coef('Var'  , 0.137864    ), Coef('Var'  , 0.133737    ), ], 
		[Coef('Var'  , 0.187007    ), Coef('Var'  , 0.201883    ), Coef('Var'  , 0.247616    ), Coef('Var'  , 0.200262    ), Coef('Var'  , 0.188502    ), Coef('Var'  , 0.184473    ), ], 
		[Coef('Var'  , 0.15765     ), Coef('Var'  , 0.184028    ), Coef('Var'  , 0.24595     ), Coef('Var'  , 0.184963    ), Coef('Var'  , 0.156496    ), Coef('Var'  , 0.152185    ), ], 
		[Coef('Var'  , 0.174767    ), Coef('Var'  , 0.182134    ), Coef('Var'  , 0.178033    ), Coef('Var'  , 0.172507    ), Coef('Var'  , 0.154814    ), Coef('Var'  , 0.163236    ), ], 
		[Coef('Var'  , 0.183215    ), Coef('Var'  , 0.180069    ), Coef('Var'  , 0.144377    ), Coef('Var'  , 0.195317    ), Coef('Var'  , 0.21037     ), Coef('Var'  , 0.204377    ), ], ])
	etat3.initMat[Chem([Sub('1')])] = FMat([
		[Coef('Const', 0.25        ), Coef('Var'  , 0.198701    ), Coef('Var'  , 0.152689    ), Coef('Var'  , 0.107962    ), Coef('Const', 0.0625      ), Coef('Const', 0.125       ), ], 
		[Coef('Const', 0.5         ), Coef('Var'  , 0.362575    ), Coef('Var'  , 0.24825     ), Coef('Var'  , 0.29804     ), Coef('Const', 0.375       ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0.25        ), Coef('Var'  , 0.248032    ), Coef('Var'  , 0.262271    ), Coef('Var'  , 0.403889    ), Coef('Const', 0.5625      ), Coef('Const', 0.375       ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0588167   ), Coef('Var'  , 0.10401     ), Coef('Var'  , 0.0603111   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0493259   ), Coef('Var'  , 0.0888678   ), Coef('Var'  , 0.0489226   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0825491   ), Coef('Var'  , 0.143912    ), Coef('Var'  , 0.0808745   ), Coef('Const', 0           ), Coef('Const', 0           ), ], ])
	etat3.initMat[Chem([Sub('0')])] = FMat([
		[Coef('Var'  , 0.101191    ), Coef('Var'  , 0.0581693   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.056819    ), ], 
		[Coef('Var'  , 0.0937086   ), Coef('Var'  , 0.0513403   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0509527   ), ], 
		[Coef('Var'  , 0.161326    ), Coef('Var'  , 0.107739    ), Coef('Const', 0.0625      ), Coef('Const', 0.125       ), Coef('Const', 0.25        ), Coef('Var'  , 0.201234    ), ], 
		[Coef('Var'  , 0.277899    ), Coef('Var'  , 0.319918    ), Coef('Const', 0.375       ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.381001    ), ], 
		[Coef('Var'  , 0.272433    ), Coef('Var'  , 0.408811    ), Coef('Const', 0.5625      ), Coef('Const', 0.375       ), Coef('Const', 0.25        ), Coef('Var'  , 0.255446    ), ], 
		[Coef('Var'  , 0.0934424   ), Coef('Var'  , 0.0540223   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0545476   ), ], ])
	etat3.initMat[Chem([Sub('G')])] = FMat([
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], ])
	etat3.initMat[Chem([Sub('10')])] = FMat([
		[Coef('Var'  , 0.154267    ), Coef('Var'  , 0.153181    ), Coef('Var'  , 0.166614    ), Coef('Var'  , 0.16331     ), Coef('Var'  , 0.167673    ), Coef('Var'  , 0.162345    ), ], 
		[Coef('Var'  , 0.152533    ), Coef('Var'  , 0.148349    ), Coef('Var'  , 0.159735    ), Coef('Var'  , 0.156446    ), Coef('Var'  , 0.164015    ), Coef('Var'  , 0.154067    ), ], 
		[Coef('Var'  , 0.17211     ), Coef('Var'  , 0.16272     ), Coef('Var'  , 0.164519    ), Coef('Var'  , 0.166401    ), Coef('Var'  , 0.171009    ), Coef('Var'  , 0.164975    ), ], 
		[Coef('Var'  , 0.162647    ), Coef('Var'  , 0.176541    ), Coef('Var'  , 0.174789    ), Coef('Var'  , 0.16769     ), Coef('Var'  , 0.152754    ), Coef('Var'  , 0.160516    ), ], 
		[Coef('Var'  , 0.137392    ), Coef('Var'  , 0.130349    ), Coef('Var'  , 0.116688    ), Coef('Var'  , 0.126843    ), Coef('Var'  , 0.140302    ), Coef('Var'  , 0.139879    ), ], 
		[Coef('Var'  , 0.221052    ), Coef('Var'  , 0.22886     ), Coef('Var'  , 0.217654    ), Coef('Var'  , 0.21931     ), Coef('Var'  , 0.204247    ), Coef('Var'  , 0.218218    ), ], ])
	etat3.initMat[Chem([Sub('9')])] = FMat([
		[Coef('Var'  , 0.154267    ), Coef('Var'  , 0.153427    ), Coef('Var'  , 0.151954    ), Coef('Var'  , 0.153762    ), Coef('Var'  , 0.152689    ), Coef('Var'  , 0.15203     ), ], 
		[Coef('Var'  , 0.152533    ), Coef('Var'  , 0.137247    ), Coef('Var'  , 0.137864    ), Coef('Var'  , 0.177342    ), Coef('Var'  , 0.24825     ), Coef('Var'  , 0.186857    ), ], 
		[Coef('Var'  , 0.17211     ), Coef('Var'  , 0.17296     ), Coef('Var'  , 0.188502    ), Coef('Var'  , 0.214891    ), Coef('Var'  , 0.262271    ), Coef('Var'  , 0.20468     ), ], 
		[Coef('Var'  , 0.162647    ), Coef('Var'  , 0.16029     ), Coef('Var'  , 0.156496    ), Coef('Var'  , 0.136047    ), Coef('Var'  , 0.10401     ), Coef('Var'  , 0.142487    ), ], 
		[Coef('Var'  , 0.137392    ), Coef('Var'  , 0.150968    ), Coef('Var'  , 0.154814    ), Coef('Var'  , 0.126263    ), Coef('Var'  , 0.0888678   ), Coef('Var'  , 0.119446    ), ], 
		[Coef('Var'  , 0.221052    ), Coef('Var'  , 0.225109    ), Coef('Var'  , 0.21037     ), Coef('Var'  , 0.191696    ), Coef('Var'  , 0.143912    ), Coef('Var'  , 0.1945      ), ], ])
	etat3.initMat[Chem([Sub('18')])] = FMat([
		[Coef('Var'  , 0.159024    ), Coef('Var'  , 0.161186    ), Coef('Var'  , 0.159596    ), Coef('Var'  , 0.173938    ), Coef('Var'  , 0.177639    ), Coef('Var'  , 0.173141    ), ], 
		[Coef('Var'  , 0.146023    ), Coef('Var'  , 0.143345    ), Coef('Var'  , 0.137765    ), Coef('Var'  , 0.15183     ), Coef('Var'  , 0.163127    ), Coef('Var'  , 0.154554    ), ], 
		[Coef('Var'  , 0.183653    ), Coef('Var'  , 0.183944    ), Coef('Var'  , 0.187007    ), Coef('Var'  , 0.186843    ), Coef('Var'  , 0.186045    ), Coef('Var'  , 0.187115    ), ], 
		[Coef('Var'  , 0.174495    ), Coef('Var'  , 0.164306    ), Coef('Var'  , 0.15765     ), Coef('Var'  , 0.14487     ), Coef('Var'  , 0.142909    ), Coef('Var'  , 0.156371    ), ], 
		[Coef('Var'  , 0.194167    ), Coef('Var'  , 0.18515     ), Coef('Var'  , 0.174767    ), Coef('Var'  , 0.167751    ), Coef('Var'  , 0.16466     ), Coef('Var'  , 0.179851    ), ], 
		[Coef('Var'  , 0.14264     ), Coef('Var'  , 0.162069    ), Coef('Var'  , 0.183215    ), Coef('Var'  , 0.174768    ), Coef('Var'  , 0.16562     ), Coef('Var'  , 0.148967    ), ], ])
	etat3.initMat[Chem([Sub('17')])] = FMat([
		[Coef('Var'  , 0.159024    ), Coef('Var'  , 0.159177    ), Coef('Var'  , 0.151012    ), Coef('Var'  , 0.13673     ), Coef('Var'  , 0.101191    ), Coef('Var'  , 0.13567     ), ], 
		[Coef('Var'  , 0.146023    ), Coef('Var'  , 0.156815    ), Coef('Var'  , 0.160571    ), Coef('Var'  , 0.135181    ), Coef('Var'  , 0.0937086   ), Coef('Var'  , 0.12503     ), ], 
		[Coef('Var'  , 0.183653    ), Coef('Var'  , 0.19204     ), Coef('Var'  , 0.192097    ), Coef('Var'  , 0.175166    ), Coef('Var'  , 0.161326    ), Coef('Var'  , 0.169928    ), ], 
		[Coef('Var'  , 0.174495    ), Coef('Var'  , 0.163196    ), Coef('Var'  , 0.15555     ), Coef('Var'  , 0.208894    ), Coef('Var'  , 0.277899    ), Coef('Var'  , 0.219213    ), ], 
		[Coef('Var'  , 0.194167    ), Coef('Var'  , 0.186572    ), Coef('Var'  , 0.189526    ), Coef('Var'  , 0.216848    ), Coef('Var'  , 0.272433    ), Coef('Var'  , 0.227971    ), ], 
		[Coef('Var'  , 0.14264     ), Coef('Var'  , 0.142199    ), Coef('Var'  , 0.151244    ), Coef('Var'  , 0.127181    ), Coef('Var'  , 0.0934424   ), Coef('Var'  , 0.122189    ), ], ])
	etat3.initMat[Chem([Sub('16')])] = FMat([
		[Coef('Const', 0.5625      ), Coef('Var'  , 0.417212    ), Coef('Var'  , 0.274636    ), Coef('Var'  , 0.262307    ), Coef('Const', 0.25        ), Coef('Const', 0.375       ), ], 
		[Coef('Const', 0.375       ), Coef('Var'  , 0.299384    ), Coef('Var'  , 0.255249    ), Coef('Var'  , 0.36259     ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0.0625      ), Coef('Var'  , 0.109193    ), Coef('Var'  , 0.158815    ), Coef('Var'  , 0.201801    ), Coef('Const', 0.25        ), Coef('Const', 0.125       ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0699969   ), Coef('Var'  , 0.118691    ), Coef('Var'  , 0.0687026   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0381504   ), Coef('Var'  , 0.0695689   ), Coef('Var'  , 0.0390118   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0660637   ), Coef('Var'  , 0.123039    ), Coef('Var'  , 0.0655872   ), Coef('Const', 0           ), Coef('Const', 0           ), ], ])
	etat3.initMat[Chem([Sub('15')])] = FMat([
		[Coef('Const', 0.5625      ), Coef('Const', 0.75        ), Coef('Const', 1           ), Coef('Const', 0.75        ), Coef('Const', 0.5625      ), Coef('Var'  , 0.557454    ), ], 
		[Coef('Const', 0.375       ), Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.188231    ), ], 
		[Coef('Const', 0.0625      ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0327097   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.00285179  ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.0625      ), Coef('Var'  , 0.032443    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Const', 0.375       ), Coef('Var'  , 0.18631     ), ], ])
	etat3.initMat[Chem([Sub('14')])] = FMat([
		[Coef('Var'  , 0.139265    ), Coef('Var'  , 0.130262    ), Coef('Var'  , 0.138785    ), Coef('Var'  , 0.15009     ), Coef('Var'  , 0.161108    ), Coef('Var'  , 0.146346    ), ], 
		[Coef('Var'  , 0.198767    ), Coef('Var'  , 0.205085    ), Coef('Var'  , 0.194305    ), Coef('Var'  , 0.20297     ), Coef('Var'  , 0.195694    ), Coef('Var'  , 0.204205    ), ], 
		[Coef('Var'  , 0.190299    ), Coef('Var'  , 0.196734    ), Coef('Var'  , 0.195328    ), Coef('Var'  , 0.189365    ), Coef('Var'  , 0.185338    ), Coef('Var'  , 0.191261    ), ], 
		[Coef('Var'  , 0.13644     ), Coef('Var'  , 0.135558    ), Coef('Var'  , 0.128391    ), Coef('Var'  , 0.125131    ), Coef('Var'  , 0.127393    ), Coef('Var'  , 0.12909     ), ], 
		[Coef('Var'  , 0.157137    ), Coef('Var'  , 0.165004    ), Coef('Var'  , 0.175743    ), Coef('Var'  , 0.169744    ), Coef('Var'  , 0.162999    ), Coef('Var'  , 0.163443    ), ], 
		[Coef('Var'  , 0.178092    ), Coef('Var'  , 0.167356    ), Coef('Var'  , 0.167447    ), Coef('Var'  , 0.162699    ), Coef('Var'  , 0.167467    ), Coef('Var'  , 0.165655    ), ], ])
	etat3.initMat[Chem([Sub('13')])] = FMat([
		[Coef('Var'  , 0.139265    ), Coef('Var'  , 0.134065    ), Coef('Var'  , 0.15904     ), Coef('Var'  , 0.174987    ), Coef('Var'  , 0.230585    ), Coef('Var'  , 0.169127    ), ], 
		[Coef('Var'  , 0.198767    ), Coef('Var'  , 0.19862     ), Coef('Var'  , 0.183918    ), Coef('Var'  , 0.160555    ), Coef('Var'  , 0.120501    ), Coef('Var'  , 0.169832    ), ], 
		[Coef('Var'  , 0.190299    ), Coef('Var'  , 0.191881    ), Coef('Var'  , 0.176503    ), Coef('Var'  , 0.161837    ), Coef('Var'  , 0.123754    ), Coef('Var'  , 0.167605    ), ], 
		[Coef('Var'  , 0.13644     ), Coef('Var'  , 0.150963    ), Coef('Var'  , 0.157708    ), Coef('Var'  , 0.135826    ), Coef('Var'  , 0.0968467   ), Coef('Var'  , 0.124402    ), ], 
		[Coef('Var'  , 0.157137    ), Coef('Var'  , 0.137872    ), Coef('Var'  , 0.122476    ), Coef('Var'  , 0.140313    ), Coef('Var'  , 0.157168    ), Coef('Var'  , 0.16025     ), ], 
		[Coef('Var'  , 0.178092    ), Coef('Var'  , 0.186598    ), Coef('Var'  , 0.200354    ), Coef('Var'  , 0.226481    ), Coef('Var'  , 0.271145    ), Coef('Var'  , 0.208784    ), ], ])
	etat3.initMat[Chem([Sub('12')])] = FMat([
		[Coef('Const', 0           ), Coef('Var'  , 0.0524761   ), Coef('Var'  , 0.0944858   ), Coef('Var'  , 0.0509977   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0522597   ), Coef('Var'  , 0.0895375   ), Coef('Var'  , 0.0532942   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.5625      ), Coef('Var'  , 0.389672    ), Coef('Var'  , 0.247616    ), Coef('Var'  , 0.235437    ), Coef('Const', 0.25        ), Coef('Const', 0.375       ), ], 
		[Coef('Const', 0.375       ), Coef('Var'  , 0.295374    ), Coef('Var'  , 0.24595     ), Coef('Var'  , 0.357849    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0.0625      ), Coef('Var'  , 0.125174    ), Coef('Var'  , 0.178033    ), Coef('Var'  , 0.219144    ), Coef('Const', 0.25        ), Coef('Const', 0.125       ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0850442   ), Coef('Var'  , 0.144377    ), Coef('Var'  , 0.083278    ), Coef('Const', 0           ), Coef('Const', 0           ), ], ])
	etat3.initMat[Chem([Sub('11')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.0625      ), Coef('Var'  , 0.0335304   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Const', 0.375       ), Coef('Var'  , 0.18806     ), ], 
		[Coef('Const', 0.5625      ), Coef('Const', 0.75        ), Coef('Const', 1           ), Coef('Const', 0.75        ), Coef('Const', 0.5625      ), Coef('Var'  , 0.56006     ), ], 
		[Coef('Const', 0.375       ), Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.185952    ), ], 
		[Coef('Const', 0.0625      ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0309391   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.00145942  ), ], ])
	
	
	
	etat4.bords   = {Bord('2'): etat10, Bord('1'): etat10, Bord('0'): etat10, }
	etat4.permuts = {}
	etat4.interns = {Intern('_'): etat4, }
	etat4.subs    = {Sub('2'): etat4, Sub('1'): etat4, Sub('0'): etat4, Sub('G', True): Etat.etatPoint, }
	
	etat4.buildIntern()
	
	
	etat4.eqs = [
		(Chem([Bord('1'), Sub('0'), Permut('0'), ])	,	Chem([Sub('0'), Bord('1'), ])),
		(Chem([Bord('0'), Sub('1'), Permut('0'), ])	,	Chem([Sub('0'), Bord('2'), ])),
		(Chem([Bord('2'), Sub('0'), Permut('0'), ])	,	Chem([Sub('1'), Bord('0'), ])),
		(Chem([Bord('1'), Sub('1'), Permut('0'), ])	,	Chem([Sub('1'), Bord('1'), ])),
		(Chem([Bord('0'), Sub('0'), Permut('0'), ])	,	Chem([Sub('2'), Bord('0'), ])),
		(Chem([Bord('2'), Sub('1'), Permut('0'), ])	,	Chem([Sub('2'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('0'), Bord('1'), ])	,	Chem([Sub('1'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('2'), Bord('1'), ])	,	Chem([Sub('2'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('2'), Bord('1'), ])	,	Chem([Sub('2'), Bord('1'), Bord('1'), ])),
		(Chem([Bord('0'), Bord('1'), ])	,	Chem([Bord('1'), Bord('0'), ])),
		(Chem([Bord('1'), Bord('1'), ])	,	Chem([Bord('2'), Bord('0'), ])),
		(Chem([Bord('2'), Bord('1'), ])	,	Chem([Bord('0'), Bord('0'), ])),
		]
	
	
	etat4.prim.elems = [Figure(2, [Chem([Bord('0'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('0'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('0'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('0'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('1'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('1'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('1'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('1'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('2'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('2'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('2'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('2'), Sub('1'), Sub('1'), Bord('0'), ]), ])]
	etat4.grid.elems = [
		Figure(1, [Chem([Bord('0'), Bord('0'), ]), Chem([Bord('0'), Intern(''), ]), Chem([Bord('0'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('1'), Bord('0'), ]), Chem([Bord('1'), Intern(''), ]), Chem([Bord('1'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('2'), Bord('0'), ]), Chem([Bord('2'), Intern(''), ]), Chem([Bord('2'), Bord('1'), ]), ]), ]
	
	
	etat4.space = [Chem([Bord('0'), Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('0'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('2'), Intern('0'), Intern('0'), ]), ]
	
	etat4.initMat[Chem([Sub('2')])] = FMat([
		[Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.249774    ), ], 
		[Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.249422    ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.126175    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.00153185  ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.124402    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.248694    ), ], ])
	etat4.initMat[Chem([Sub('1')])] = FMat([
		[Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.125389    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.00185341  ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.12707     ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.249206    ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.248381    ), ], 
		[Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.2481      ), ], ])
	etat4.initMat[Chem([Sub('0')])] = FMat([
		[Coef('Const', 0.25        ), Coef('Var'  , 0.123795    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.5         ), Coef('Var'  , 0.250248    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0.25        ), Coef('Var'  , 0.248162    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.250322    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.125684    ), Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0017882   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], ])
	etat4.initMat[Chem([Sub('G')])] = FMat([
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], ])
	
	
	
	etat5.bords   = {Bord('4'): etat10, Bord('3'): etat10, Bord('2'): etat10, Bord('1'): etat10, Bord('0'): etat10, }
	etat5.permuts = {}
	etat5.interns = {Intern('_'): etat5, }
	etat5.subs    = {Sub('4'): etat2, Sub('3'): etat2, Sub('2'): etat2, Sub('1'): etat2, Sub('0'): etat2, Sub('G', True): Etat.etatPoint, }
	
	etat5.buildIntern()
	
	
	etat5.eqs = [
		(Chem([Bord('2'), Sub('0'), Permut('0'), ])	,	Chem([Sub('0'), Bord('0'), ])),
		(Chem([Bord('1'), Sub('1'), Permut('0'), ])	,	Chem([Sub('0'), Bord('1'), ])),
		(Chem([Bord('3'), Sub('0'), Permut('0'), ])	,	Chem([Sub('1'), Bord('0'), ])),
		(Chem([Bord('2'), Sub('1'), Permut('0'), ])	,	Chem([Sub('1'), Bord('1'), ])),
		(Chem([Bord('4'), Sub('0'), Permut('0'), ])	,	Chem([Sub('2'), Bord('0'), ])),
		(Chem([Bord('3'), Sub('1'), Permut('0'), ])	,	Chem([Sub('2'), Bord('1'), ])),
		(Chem([Bord('0'), Sub('0'), Permut('0'), ])	,	Chem([Sub('3'), Bord('0'), ])),
		(Chem([Bord('4'), Sub('1'), Permut('0'), ])	,	Chem([Sub('3'), Bord('1'), ])),
		(Chem([Bord('1'), Sub('0'), Permut('0'), ])	,	Chem([Sub('4'), Bord('0'), ])),
		(Chem([Bord('0'), Sub('1'), Permut('0'), ])	,	Chem([Sub('4'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('1'), Bord('1'), ])	,	Chem([Sub('4'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('2'), Bord('1'), ])	,	Chem([Sub('1'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('2'), Bord('1'), ])	,	Chem([Sub('2'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('2'), Bord('1'), ])	,	Chem([Sub('3'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('3'), Bord('2'), Bord('1'), ])	,	Chem([Sub('4'), Bord('1'), Bord('1'), ])),
		(Chem([Bord('0'), Bord('1'), ])	,	Chem([Bord('1'), Bord('0'), ])),
		(Chem([Bord('1'), Bord('1'), ])	,	Chem([Bord('2'), Bord('0'), ])),
		(Chem([Bord('2'), Bord('1'), ])	,	Chem([Bord('3'), Bord('0'), ])),
		(Chem([Bord('3'), Bord('1'), ])	,	Chem([Bord('4'), Bord('0'), ])),
		(Chem([Bord('4'), Bord('1'), ])	,	Chem([Bord('0'), Bord('0'), ])),
		]
	
	
	etat5.prim.elems = [Figure(2, [Chem([Bord('0'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('0'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('0'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('0'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('1'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('1'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('1'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('1'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('2'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('2'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('2'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('2'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('3'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('3'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('3'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('3'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('4'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('4'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('4'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('4'), Sub('1'), Sub('1'), Bord('0'), ]), ])]
	etat5.grid.elems = [
		Figure(1, [Chem([Bord('0'), Bord('0'), ]), Chem([Bord('0'), Intern(''), ]), Chem([Bord('0'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('1'), Bord('0'), ]), Chem([Bord('1'), Intern(''), ]), Chem([Bord('1'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('2'), Bord('0'), ]), Chem([Bord('2'), Intern(''), ]), Chem([Bord('2'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('3'), Bord('0'), ]), Chem([Bord('3'), Intern(''), ]), Chem([Bord('3'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('4'), Bord('0'), ]), Chem([Bord('4'), Intern(''), ]), Chem([Bord('4'), Bord('1'), ]), ]), ]
	
	
	etat5.space = [Chem([Bord('0'), Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('0'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('2'), Intern('0'), Intern('0'), ]), Chem([Bord('2'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('3'), Intern('0'), Intern('0'), ]), Chem([Bord('3'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('4'), Intern('0'), Intern('0'), ]), ]
	
	etat5.initMat[Chem([Sub('4')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.124258    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.25        ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.248923    ), ], 
		[Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.247768    ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.124273    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 9.08947e-05 ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.00290742  ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.00121938  ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.000114929 ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.000445876 ), ], ])
	etat5.initMat[Chem([Sub('3')])] = FMat([
		[Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.248631    ), ], 
		[Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.247766    ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.124998    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.00154687  ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0012338   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.00197867  ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 7.15539e-05 ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.00174944  ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.124062    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.247963    ), ], ])
	etat5.initMat[Chem([Sub('2')])] = FMat([
		[Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.123875    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.00168914  ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0014575   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.00123957  ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.000318882 ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.000858636 ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.124184    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.249331    ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.248621    ), ], 
		[Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.248424    ), ], ])
	etat5.initMat[Chem([Sub('1')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.000925324 ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.000633211 ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.00166643  ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.00129336  ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.123841    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.249186    ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.2486      ), ], 
		[Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.247807    ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.124634    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0014135   ), ], ])
	etat5.initMat[Chem([Sub('0')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.00163053  ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.00239772  ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.124503    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.247582    ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.247829    ), ], 
		[Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.249348    ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.123853    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.000553333 ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.00150366  ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.00079986  ), ], ])
	etat5.initMat[Chem([Sub('G')])] = FMat([
		[Coef('Const', 0.1         )], 
		[Coef('Const', 0.1         )], 
		[Coef('Const', 0.1         )], 
		[Coef('Const', 0.1         )], 
		[Coef('Const', 0.1         )], 
		[Coef('Const', 0.1         )], 
		[Coef('Const', 0.1         )], 
		[Coef('Const', 0.1         )], 
		[Coef('Const', 0.1         )], 
		[Coef('Const', 0.1         )], ])
	
	
	
	etat6.bords   = {Bord('3'): etat10, Bord('2'): etat10, Bord('1'): etat10, Bord('0'): etat10, }
	etat6.permuts = {}
	etat6.interns = {Intern('_'): etat6, }
	etat6.subs    = {Sub('3'): etat9, Sub('2'): etat9, Sub('1'): etat9, Sub('0'): etat9, Sub('G', True): Etat.etatPoint, }
	
	etat6.buildIntern()
	
	
	etat6.eqs = [
		(Chem([Bord('0'), Sub('0'), Permut('0'), ])	,	Chem([Sub('0'), Bord('1'), ])),
		(Chem([Bord('3'), Sub('1'), Permut('0'), ])	,	Chem([Sub('0'), Bord('2'), ])),
		(Chem([Bord('3'), Sub('0'), Permut('0'), ])	,	Chem([Sub('1'), Bord('1'), ])),
		(Chem([Bord('2'), Sub('1'), Permut('0'), ])	,	Chem([Sub('1'), Bord('2'), ])),
		(Chem([Bord('2'), Sub('0'), Permut('0'), ])	,	Chem([Sub('2'), Bord('1'), ])),
		(Chem([Bord('1'), Sub('1'), Permut('0'), ])	,	Chem([Sub('2'), Bord('2'), ])),
		(Chem([Bord('1'), Sub('0'), Permut('0'), ])	,	Chem([Sub('3'), Bord('1'), ])),
		(Chem([Bord('0'), Sub('1'), Permut('0'), ])	,	Chem([Sub('3'), Bord('2'), ])),
		(Chem([Sub('0'), Bord('0'), Bord('1'), ])	,	Chem([Sub('3'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('2'), Bord('1'), ])	,	Chem([Sub('1'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('2'), Bord('1'), ])	,	Chem([Sub('2'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('2'), Bord('1'), ])	,	Chem([Sub('3'), Bord('0'), Bord('1'), ])),
		(Chem([Bord('0'), Bord('1'), ])	,	Chem([Bord('1'), Bord('0'), ])),
		(Chem([Bord('1'), Bord('1'), ])	,	Chem([Bord('2'), Bord('0'), ])),
		(Chem([Bord('2'), Bord('1'), ])	,	Chem([Bord('3'), Bord('0'), ])),
		(Chem([Bord('3'), Bord('1'), ])	,	Chem([Bord('0'), Bord('0'), ])),
		]
	
	
	etat6.prim.elems = [Figure(2, [Chem([Bord('0'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('0'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('0'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('0'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('1'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('1'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('1'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('1'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('2'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('2'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('2'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('2'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('3'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('3'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('3'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('3'), Sub('1'), Sub('1'), Bord('0'), ]), ])]
	etat6.grid.elems = [
		Figure(1, [Chem([Bord('0'), Bord('0'), ]), Chem([Bord('0'), Intern(''), ]), Chem([Bord('0'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('1'), Bord('0'), ]), Chem([Bord('1'), Intern(''), ]), Chem([Bord('1'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('2'), Bord('0'), ]), Chem([Bord('2'), Intern(''), ]), Chem([Bord('2'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('3'), Bord('0'), ]), Chem([Bord('3'), Intern(''), ]), Chem([Bord('3'), Bord('1'), ]), ]), ]
	
	
	etat6.space = [Chem([Bord('0'), Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('0'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('2'), Intern('0'), Intern('0'), ]), Chem([Bord('2'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('3'), Intern('0'), Intern('0'), ]), ]
	
	etat6.initMat[Chem([Sub('3')])] = FMat([
		[Coef('Const', 0.25        ), Coef('Var'  , 0.124244    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.5         ), Coef('Var'  , 0.250997    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0.25        ), Coef('Var'  , 0.24773     ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.250462    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.123953    ), Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.000158689 ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.00219855  ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.000257389 ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], ])
	etat6.initMat[Chem([Sub('2')])] = FMat([
		[Coef('Const', 0           ), Coef('Var'  , 0.000694958 ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 4.05047e-05 ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.25        ), Coef('Var'  , 0.124897    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.5         ), Coef('Var'  , 0.248808    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0.25        ), Coef('Var'  , 0.248126    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.250026    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.12649     ), Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.000917376 ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], ])
	etat6.initMat[Chem([Sub('1')])] = FMat([
		[Coef('Const', 0           ), Coef('Var'  , 0.124864    ), Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.000554665 ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.00205651  ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.00178205  ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.25        ), Coef('Var'  , 0.125852    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.5         ), Coef('Var'  , 0.248022    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0.25        ), Coef('Var'  , 0.248498    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.248371    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), ], ])
	etat6.initMat[Chem([Sub('0')])] = FMat([
		[Coef('Const', 0.25        ), Coef('Var'  , 0.24847     ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.248462    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.124962    ), Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.00101528  ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.000904732 ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.00161851  ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.25        ), Coef('Var'  , 0.125344    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.5         ), Coef('Var'  , 0.249223    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), ], ])
	etat6.initMat[Chem([Sub('G')])] = FMat([
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], ])
	
	
	
	etat7.bords   = {Bord('4'): etat10, Bord('3'): etat10, Bord('2'): etat10, Bord('1'): etat10, Bord('0'): etat10, }
	etat7.permuts = {}
	etat7.interns = {Intern('_'): etat7, }
	etat7.subs    = {Sub('8'): etat7, Sub('7'): etat7, Sub('6'): etat7, Sub('5'): etat7, Sub('4'): etat7, Sub('3'): etat7, Sub('2'): etat7, Sub('1'): etat7, Sub('0'): etat7, Sub('G', True): Etat.etatPoint, Sub('10'): etat7, Sub('9'): etat7, }
	
	etat7.buildIntern()
	
	
	etat7.eqs = [
		(Chem([Bord('2'), Sub('1'), Permut('0'), ])	,	Chem([Sub('0'), Bord('0'), ])),
		(Chem([Bord('3'), Sub('0'), Permut('0'), ])	,	Chem([Sub('0'), Bord('4'), ])),
		(Chem([Bord('1'), Sub('0'), Permut('0'), ])	,	Chem([Sub('3'), Bord('2'), ])),
		(Chem([Bord('0'), Sub('1'), Permut('0'), ])	,	Chem([Sub('3'), Bord('3'), ])),
		(Chem([Bord('0'), Sub('0'), Permut('0'), ])	,	Chem([Sub('4'), Bord('0'), ])),
		(Chem([Bord('4'), Sub('1'), Permut('0'), ])	,	Chem([Sub('4'), Bord('1'), ])),
		(Chem([Bord('1'), Sub('1'), Permut('0'), ])	,	Chem([Sub('9'), Bord('0'), ])),
		(Chem([Bord('2'), Sub('0'), Permut('0'), ])	,	Chem([Sub('9'), Bord('4'), ])),
		(Chem([Bord('4'), Sub('0'), Permut('0'), ])	,	Chem([Sub('10'), Bord('3'), ])),
		(Chem([Bord('3'), Sub('1'), Permut('0'), ])	,	Chem([Sub('10'), Bord('4'), ])),
		(Chem([Sub('0'), Bord('0'), Bord('1'), ])	,	Chem([Sub('9'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('1'), Bord('1'), ])	,	Chem([Sub('7'), Bord('4'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('2'), Bord('1'), ])	,	Chem([Sub('8'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('3'), Bord('1'), ])	,	Chem([Sub('10'), Bord('4'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('0'), Bord('1'), ])	,	Chem([Sub('9'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('1'), Bord('1'), ])	,	Chem([Sub('3'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('2'), Bord('1'), ])	,	Chem([Sub('6'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('3'), Bord('1'), ])	,	Chem([Sub('2'), Bord('4'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('4'), Bord('1'), ])	,	Chem([Sub('7'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('0'), Bord('1'), ])	,	Chem([Sub('6'), Bord('4'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('1'), Bord('1'), ])	,	Chem([Sub('5'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('2'), Bord('1'), ])	,	Chem([Sub('8'), Bord('4'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('3'), Bord('1'), ])	,	Chem([Sub('7'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('3'), Bord('1'), Bord('1'), ])	,	Chem([Sub('9'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('3'), Bord('3'), Bord('1'), ])	,	Chem([Sub('4'), Bord('4'), Bord('1'), ])),
		(Chem([Sub('3'), Bord('4'), Bord('1'), ])	,	Chem([Sub('6'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('4'), Bord('1'), Bord('1'), ])	,	Chem([Sub('10'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('4'), Bord('2'), Bord('1'), ])	,	Chem([Sub('5'), Bord('4'), Bord('1'), ])),
		(Chem([Sub('4'), Bord('3'), Bord('1'), ])	,	Chem([Sub('6'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('5'), Bord('0'), Bord('1'), ])	,	Chem([Sub('10'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('5'), Bord('1'), Bord('1'), ])	,	Chem([Sub('8'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('5'), Bord('3'), Bord('1'), ])	,	Chem([Sub('6'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('7'), Bord('0'), Bord('1'), ])	,	Chem([Sub('9'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('7'), Bord('3'), Bord('1'), ])	,	Chem([Sub('8'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('8'), Bord('1'), Bord('1'), ])	,	Chem([Sub('10'), Bord('0'), Bord('1'), ])),
		(Chem([Bord('0'), Bord('1'), ])	,	Chem([Bord('1'), Bord('0'), ])),
		(Chem([Bord('1'), Bord('1'), ])	,	Chem([Bord('2'), Bord('0'), ])),
		(Chem([Bord('2'), Bord('1'), ])	,	Chem([Bord('3'), Bord('0'), ])),
		(Chem([Bord('3'), Bord('1'), ])	,	Chem([Bord('4'), Bord('0'), ])),
		(Chem([Bord('4'), Bord('1'), ])	,	Chem([Bord('0'), Bord('0'), ])),
		]
	
	
	etat7.prim.elems = [Figure(2, [Chem([Bord('0'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('0'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('0'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('0'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('1'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('1'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('1'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('1'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('2'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('2'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('2'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('2'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('3'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('3'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('3'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('3'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('4'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('4'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('4'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('4'), Sub('1'), Sub('1'), Bord('0'), ]), ])]
	etat7.grid.elems = [
		Figure(1, [Chem([Bord('0'), Bord('0'), ]), Chem([Bord('0'), Intern(''), ]), Chem([Bord('0'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('1'), Bord('0'), ]), Chem([Bord('1'), Intern(''), ]), Chem([Bord('1'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('2'), Bord('0'), ]), Chem([Bord('2'), Intern(''), ]), Chem([Bord('2'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('3'), Bord('0'), ]), Chem([Bord('3'), Intern(''), ]), Chem([Bord('3'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('4'), Bord('0'), ]), Chem([Bord('4'), Intern(''), ]), Chem([Bord('4'), Bord('1'), ]), ]), ]
	
	
	etat7.space = [Chem([Bord('0'), Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('0'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('2'), Intern('0'), Intern('0'), ]), Chem([Bord('2'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('3'), Intern('0'), Intern('0'), ]), Chem([Bord('3'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('4'), Intern('0'), Intern('0'), ]), ]
	
	etat7.initMat[Chem([Sub('8')])] = FMat([
		[Coef('Var'  , 0.100291    ), Coef('Var'  , 0.0952527   ), Coef('Var'  , 0.0919464   ), Coef('Var'  , 0.082911    ), Coef('Var'  , 0.0748952   ), Coef('Var'  , 0.0813217   ), Coef('Var'  , 0.0798484   ), Coef('Var'  , 0.0910569   ), Coef('Var'  , 0.0983175   ), Coef('Var'  , 0.100059    ), ], 
		[Coef('Var'  , 0.100858    ), Coef('Var'  , 0.110028    ), Coef('Var'  , 0.110653    ), Coef('Var'  , 0.101033    ), Coef('Var'  , 0.0803264   ), Coef('Var'  , 0.0877142   ), Coef('Var'  , 0.0807142   ), Coef('Var'  , 0.089246    ), Coef('Var'  , 0.0881287   ), Coef('Var'  , 0.0926397   ), ], 
		[Coef('Var'  , 0.0986555   ), Coef('Var'  , 0.0985995   ), Coef('Var'  , 0.0972559   ), Coef('Var'  , 0.0871033   ), Coef('Var'  , 0.0685749   ), Coef('Var'  , 0.0673982   ), Coef('Var'  , 0.064043    ), Coef('Var'  , 0.082663    ), Coef('Var'  , 0.0942751   ), Coef('Var'  , 0.0982322   ), ], 
		[Coef('Var'  , 0.108263    ), Coef('Var'  , 0.106938    ), Coef('Var'  , 0.0975527   ), Coef('Var'  , 0.0948635   ), Coef('Var'  , 0.0788117   ), Coef('Var'  , 0.0843969   ), Coef('Var'  , 0.0760315   ), Coef('Var'  , 0.0898948   ), Coef('Var'  , 0.0985065   ), Coef('Var'  , 0.105077    ), ], 
		[Coef('Var'  , 0.0937937   ), Coef('Var'  , 0.100281    ), Coef('Var'  , 0.105785    ), Coef('Var'  , 0.104416    ), Coef('Var'  , 0.0874287   ), Coef('Var'  , 0.0851985   ), Coef('Var'  , 0.0732931   ), Coef('Var'  , 0.0795532   ), Coef('Var'  , 0.0874312   ), Coef('Var'  , 0.0900056   ), ], 
		[Coef('Var'  , 0.107705    ), Coef('Var'  , 0.0954826   ), Coef('Var'  , 0.0854212   ), Coef('Var'  , 0.0716418   ), Coef('Var'  , 0.060076    ), Coef('Var'  , 0.0671246   ), Coef('Var'  , 0.0762804   ), Coef('Var'  , 0.0927213   ), Coef('Var'  , 0.11087     ), Coef('Var'  , 0.11044     ), ], 
		[Coef('Var'  , 0.082898    ), Coef('Var'  , 0.0717378   ), Coef('Var'  , 0.0679602   ), Coef('Var'  , 0.0815841   ), Coef('Var'  , 0.110612    ), Coef('Var'  , 0.112362    ), Coef('Var'  , 0.128774    ), Coef('Var'  , 0.106772    ), Coef('Var'  , 0.0982428   ), Coef('Var'  , 0.0885109   ), ], 
		[Coef('Var'  , 0.0986922   ), Coef('Var'  , 0.0960276   ), Coef('Var'  , 0.102045    ), Coef('Var'  , 0.133145    ), Coef('Var'  , 0.187573    ), Coef('Var'  , 0.174817    ), Coef('Var'  , 0.192616    ), Coef('Var'  , 0.145087    ), Coef('Var'  , 0.114457    ), Coef('Var'  , 0.105281    ), ], 
		[Coef('Var'  , 0.093725    ), Coef('Var'  , 0.102787    ), Coef('Var'  , 0.111634    ), Coef('Var'  , 0.12544     ), Coef('Var'  , 0.144862    ), Coef('Var'  , 0.137728    ), Coef('Var'  , 0.138384    ), Coef('Var'  , 0.116886    ), Coef('Var'  , 0.09902     ), Coef('Var'  , 0.0958673   ), ], 
		[Coef('Var'  , 0.115118    ), Coef('Var'  , 0.122867    ), Coef('Var'  , 0.129747    ), Coef('Var'  , 0.117861    ), Coef('Var'  , 0.10684     ), Coef('Var'  , 0.101939    ), Coef('Var'  , 0.0900155   ), Coef('Var'  , 0.10612     ), Coef('Var'  , 0.110752    ), Coef('Var'  , 0.113887    ), ], ])
	etat7.initMat[Chem([Sub('7')])] = FMat([
		[Coef('Var'  , 0.0908735   ), Coef('Var'  , 0.0972983   ), Coef('Var'  , 0.0815724   ), Coef('Var'  , 0.0921471   ), Coef('Var'  , 0.0931784   ), Coef('Var'  , 0.0994176   ), Coef('Var'  , 0.100826    ), Coef('Var'  , 0.0990686   ), Coef('Var'  , 0.0983175   ), Coef('Var'  , 0.100255    ), ], 
		[Coef('Var'  , 0.0731485   ), Coef('Var'  , 0.0702696   ), Coef('Var'  , 0.0610968   ), Coef('Var'  , 0.0744909   ), Coef('Var'  , 0.0878259   ), Coef('Var'  , 0.0864128   ), Coef('Var'  , 0.0890979   ), Coef('Var'  , 0.0849744   ), Coef('Var'  , 0.0881287   ), Coef('Var'  , 0.0846993   ), ], 
		[Coef('Var'  , 0.0708796   ), Coef('Var'  , 0.0898014   ), Coef('Var'  , 0.100378    ), Coef('Var'  , 0.117593    ), Coef('Var'  , 0.122425    ), Coef('Var'  , 0.117496    ), Coef('Var'  , 0.10641     ), Coef('Var'  , 0.103873    ), Coef('Var'  , 0.0942751   ), Coef('Var'  , 0.0855029   ), ], 
		[Coef('Var'  , 0.0723256   ), Coef('Var'  , 0.0841048   ), Coef('Var'  , 0.0924411   ), Coef('Var'  , 0.105228    ), Coef('Var'  , 0.116124    ), Coef('Var'  , 0.116624    ), Coef('Var'  , 0.114957    ), Coef('Var'  , 0.109846    ), Coef('Var'  , 0.0985065   ), Coef('Var'  , 0.0859806   ), ], 
		[Coef('Var'  , 0.118114    ), Coef('Var'  , 0.112936    ), Coef('Var'  , 0.123774    ), Coef('Var'  , 0.10327     ), Coef('Var'  , 0.0929071   ), Coef('Var'  , 0.0873115   ), Coef('Var'  , 0.0836905   ), Coef('Var'  , 0.0843997   ), Coef('Var'  , 0.0874312   ), Coef('Var'  , 0.098814    ), ], 
		[Coef('Var'  , 0.175249    ), Coef('Var'  , 0.160265    ), Coef('Var'  , 0.184079    ), Coef('Var'  , 0.139818    ), Coef('Var'  , 0.114742    ), Coef('Var'  , 0.11266     ), Coef('Var'  , 0.110669    ), Coef('Var'  , 0.11156     ), Coef('Var'  , 0.11087     ), Coef('Var'  , 0.132512    ), ], 
		[Coef('Var'  , 0.141032    ), Coef('Var'  , 0.143955    ), Coef('Var'  , 0.149967    ), Coef('Var'  , 0.13199     ), Coef('Var'  , 0.1117      ), Coef('Var'  , 0.105073    ), Coef('Var'  , 0.0965929   ), Coef('Var'  , 0.0938295   ), Coef('Var'  , 0.0982428   ), Coef('Var'  , 0.113519    ), ], 
		[Coef('Var'  , 0.0944095   ), Coef('Var'  , 0.089911    ), Coef('Var'  , 0.0805822   ), Coef('Var'  , 0.0929235   ), Coef('Var'  , 0.101104    ), Coef('Var'  , 0.101998    ), Coef('Var'  , 0.105379    ), Coef('Var'  , 0.108655    ), Coef('Var'  , 0.114457    ), Coef('Var'  , 0.104058    ), ], 
		[Coef('Var'  , 0.0803354   ), Coef('Var'  , 0.071958    ), Coef('Var'  , 0.0587033   ), Coef('Var'  , 0.0650318   ), Coef('Var'  , 0.0730522   ), Coef('Var'  , 0.0769876   ), Coef('Var'  , 0.0857301   ), Coef('Var'  , 0.0923287   ), Coef('Var'  , 0.09902     ), Coef('Var'  , 0.0912941   ), ], 
		[Coef('Var'  , 0.0836333   ), Coef('Var'  , 0.0795008   ), Coef('Var'  , 0.067406    ), Coef('Var'  , 0.0775064   ), Coef('Var'  , 0.0869417   ), Coef('Var'  , 0.0960188   ), Coef('Var'  , 0.106648    ), Coef('Var'  , 0.111465    ), Coef('Var'  , 0.110752    ), Coef('Var'  , 0.103364    ), ], ])
	etat7.initMat[Chem([Sub('6')])] = FMat([
		[Coef('Var'  , 0.110977    ), Coef('Var'  , 0.1129      ), Coef('Var'  , 0.108682    ), Coef('Var'  , 0.12099     ), Coef('Var'  , 0.13484     ), Coef('Var'  , 0.122164    ), Coef('Var'  , 0.121603    ), Coef('Var'  , 0.0971005   ), Coef('Var'  , 0.0926363   ), Coef('Var'  , 0.101505    ), ], 
		[Coef('Var'  , 0.113694    ), Coef('Var'  , 0.120876    ), Coef('Var'  , 0.129766    ), Coef('Var'  , 0.15779     ), Coef('Var'  , 0.197935    ), Coef('Var'  , 0.174597    ), Coef('Var'  , 0.18429     ), Coef('Var'  , 0.135852    ), Coef('Var'  , 0.110468    ), Coef('Var'  , 0.107301    ), ], 
		[Coef('Var'  , 0.0874249   ), Coef('Var'  , 0.0915003   ), Coef('Var'  , 0.0992633   ), Coef('Var'  , 0.106367    ), Coef('Var'  , 0.127047    ), Coef('Var'  , 0.119634    ), Coef('Var'  , 0.12766     ), Coef('Var'  , 0.103392    ), Coef('Var'  , 0.0895205   ), Coef('Var'  , 0.0832857   ), ], 
		[Coef('Var'  , 0.079018    ), Coef('Var'  , 0.082137    ), Coef('Var'  , 0.0965481   ), Coef('Var'  , 0.087696    ), Coef('Var'  , 0.0843676   ), Coef('Var'  , 0.0852297   ), Coef('Var'  , 0.0779185   ), Coef('Var'  , 0.0867015   ), Coef('Var'  , 0.0841807   ), Coef('Var'  , 0.0804324   ), ], 
		[Coef('Var'  , 0.0868691   ), Coef('Var'  , 0.0872873   ), Coef('Var'  , 0.0888317   ), Coef('Var'  , 0.081696    ), Coef('Var'  , 0.0729488   ), Coef('Var'  , 0.0683696   ), Coef('Var'  , 0.0606463   ), Coef('Var'  , 0.0728487   ), Coef('Var'  , 0.0845837   ), Coef('Var'  , 0.0855594   ), ], 
		[Coef('Var'  , 0.103175    ), Coef('Var'  , 0.0960533   ), Coef('Var'  , 0.0925178   ), Coef('Var'  , 0.0919106   ), Coef('Var'  , 0.0857925   ), Coef('Var'  , 0.103295    ), Coef('Var'  , 0.10262     ), Coef('Var'  , 0.119642    ), Coef('Var'  , 0.11937     ), Coef('Var'  , 0.111851    ), ], 
		[Coef('Var'  , 0.107272    ), Coef('Var'  , 0.104401    ), Coef('Var'  , 0.0933698   ), Coef('Var'  , 0.0817919   ), Coef('Var'  , 0.0665696   ), Coef('Var'  , 0.0786571   ), Coef('Var'  , 0.0838959   ), Coef('Var'  , 0.10339     ), Coef('Var'  , 0.108259    ), Coef('Var'  , 0.114174    ), ], 
		[Coef('Var'  , 0.10928     ), Coef('Var'  , 0.105709    ), Coef('Var'  , 0.100444    ), Coef('Var'  , 0.090637    ), Coef('Var'  , 0.0766101   ), Coef('Var'  , 0.0840876   ), Coef('Var'  , 0.0819398   ), Coef('Var'  , 0.0982506   ), Coef('Var'  , 0.104864    ), Coef('Var'  , 0.109629    ), ], 
		[Coef('Var'  , 0.0922989   ), Coef('Var'  , 0.0914834   ), Coef('Var'  , 0.0879204   ), Coef('Var'  , 0.0845731   ), Coef('Var'  , 0.0728309   ), Coef('Var'  , 0.0699012   ), Coef('Var'  , 0.0588154   ), Coef('Var'  , 0.0647095   ), Coef('Var'  , 0.0769815   ), Coef('Var'  , 0.0853366   ), ], 
		[Coef('Var'  , 0.109991    ), Coef('Var'  , 0.107652    ), Coef('Var'  , 0.102657    ), Coef('Var'  , 0.0965485   ), Coef('Var'  , 0.0810586   ), Coef('Var'  , 0.094065    ), Coef('Var'  , 0.100611    ), Coef('Var'  , 0.118113    ), Coef('Var'  , 0.129136    ), Coef('Var'  , 0.120926    ), ], ])
	etat7.initMat[Chem([Sub('5')])] = FMat([
		[Coef('Var'  , 0.113556    ), Coef('Var'  , 0.104482    ), Coef('Var'  , 0.115961    ), Coef('Var'  , 0.0992438   ), Coef('Var'  , 0.0919464   ), Coef('Var'  , 0.0947231   ), Coef('Var'  , 0.100389    ), Coef('Var'  , 0.0926031   ), Coef('Var'  , 0.0926363   ), Coef('Var'  , 0.0926772   ), ], 
		[Coef('Var'  , 0.0851667   ), Coef('Var'  , 0.0825103   ), Coef('Var'  , 0.0767638   ), Coef('Var'  , 0.0978606   ), Coef('Var'  , 0.110653    ), Coef('Var'  , 0.121408    ), Coef('Var'  , 0.11659     ), Coef('Var'  , 0.113583    ), Coef('Var'  , 0.110468    ), Coef('Var'  , 0.0950173   ), ], 
		[Coef('Var'  , 0.0857713   ), Coef('Var'  , 0.0897025   ), Coef('Var'  , 0.0792932   ), Coef('Var'  , 0.0943707   ), Coef('Var'  , 0.0972559   ), Coef('Var'  , 0.10062     ), Coef('Var'  , 0.0953047   ), Coef('Var'  , 0.0901574   ), Coef('Var'  , 0.0895205   ), Coef('Var'  , 0.0885057   ), ], 
		[Coef('Var'  , 0.0714876   ), Coef('Var'  , 0.0749512   ), Coef('Var'  , 0.0712113   ), Coef('Var'  , 0.0872741   ), Coef('Var'  , 0.0975527   ), Coef('Var'  , 0.0934849   ), Coef('Var'  , 0.087856    ), Coef('Var'  , 0.0850104   ), Coef('Var'  , 0.0841807   ), Coef('Var'  , 0.0810287   ), ], 
		[Coef('Var'  , 0.0709913   ), Coef('Var'  , 0.0860899   ), Coef('Var'  , 0.0865893   ), Coef('Var'  , 0.102426    ), Coef('Var'  , 0.105785    ), Coef('Var'  , 0.106757    ), Coef('Var'  , 0.099889    ), Coef('Var'  , 0.094844    ), Coef('Var'  , 0.0845837   ), Coef('Var'  , 0.0818417   ), ], 
		[Coef('Var'  , 0.0956203   ), Coef('Var'  , 0.0903733   ), Coef('Var'  , 0.0705703   ), Coef('Var'  , 0.0782185   ), Coef('Var'  , 0.0854212   ), Coef('Var'  , 0.0985021   ), Coef('Var'  , 0.111125    ), Coef('Var'  , 0.120931    ), Coef('Var'  , 0.11937     ), Coef('Var'  , 0.11412     ), ], 
		[Coef('Var'  , 0.0865187   ), Coef('Var'  , 0.079226    ), Coef('Var'  , 0.0634509   ), Coef('Var'  , 0.06068     ), Coef('Var'  , 0.0679602   ), Coef('Var'  , 0.0705827   ), Coef('Var'  , 0.0856208   ), Coef('Var'  , 0.0975165   ), Coef('Var'  , 0.108259    ), Coef('Var'  , 0.105873    ), ], 
		[Coef('Var'  , 0.088823    ), Coef('Var'  , 0.0970673   ), Coef('Var'  , 0.0949229   ), Coef('Var'  , 0.0968388   ), Coef('Var'  , 0.102045    ), Coef('Var'  , 0.0943762   ), Coef('Var'  , 0.0974248   ), Coef('Var'  , 0.101325    ), Coef('Var'  , 0.104864    ), Coef('Var'  , 0.103096    ), ], 
		[Coef('Var'  , 0.106171    ), Coef('Var'  , 0.110795    ), Coef('Var'  , 0.134632    ), Coef('Var'  , 0.12017     ), Coef('Var'  , 0.111634    ), Coef('Var'  , 0.100474    ), Coef('Var'  , 0.0910504   ), Coef('Var'  , 0.0809625   ), Coef('Var'  , 0.0769815   ), Coef('Var'  , 0.0839553   ), ], 
		[Coef('Var'  , 0.195894    ), Coef('Var'  , 0.184802    ), Coef('Var'  , 0.206605    ), Coef('Var'  , 0.162917    ), Coef('Var'  , 0.129747    ), Coef('Var'  , 0.119072    ), Coef('Var'  , 0.114751    ), Coef('Var'  , 0.123068    ), Coef('Var'  , 0.129136    ), Coef('Var'  , 0.153886    ), ], ])
	etat7.initMat[Chem([Sub('4')])] = FMat([
		[Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.174086    ), Coef('Var'  , 0.113556    ), Coef('Var'  , 0.105339    ), Coef('Var'  , 0.121603    ), Coef('Var'  , 0.180267    ), ], 
		[Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0432203   ), Coef('Var'  , 0.0851667   ), Coef('Var'  , 0.124478    ), Coef('Var'  , 0.18429     ), Coef('Var'  , 0.330723    ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0465388   ), Coef('Var'  , 0.0857713   ), Coef('Var'  , 0.109293    ), Coef('Var'  , 0.12766     ), Coef('Var'  , 0.185645    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0386614   ), Coef('Var'  , 0.0714876   ), Coef('Var'  , 0.0821419   ), Coef('Var'  , 0.0779185   ), Coef('Var'  , 0.044314    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0390752   ), Coef('Var'  , 0.0709913   ), Coef('Var'  , 0.0677255   ), Coef('Var'  , 0.0606463   ), Coef('Var'  , 0.0315848   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0526968   ), Coef('Var'  , 0.0956203   ), Coef('Var'  , 0.109575    ), Coef('Var'  , 0.10262     ), Coef('Var'  , 0.0584682   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0499591   ), Coef('Var'  , 0.0865187   ), Coef('Var'  , 0.0946316   ), Coef('Var'  , 0.0838959   ), Coef('Var'  , 0.0459385   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0495657   ), Coef('Var'  , 0.088823    ), Coef('Var'  , 0.0922483   ), Coef('Var'  , 0.0819398   ), Coef('Var'  , 0.0432893   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.171551    ), Coef('Var'  , 0.106171    ), Coef('Var'  , 0.075763    ), Coef('Var'  , 0.0588154   ), Coef('Var'  , 0.0284063   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.334645    ), Coef('Var'  , 0.195894    ), Coef('Var'  , 0.138804    ), Coef('Var'  , 0.100611    ), Coef('Var'  , 0.0513647   ), ], ])
	etat7.initMat[Chem([Sub('3')])] = FMat([
		[Coef('Var'  , 0.13484     ), Coef('Var'  , 0.108393    ), Coef('Var'  , 0.08096     ), Coef('Var'  , 0.0422551   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.191385    ), ], 
		[Coef('Var'  , 0.197935    ), Coef('Var'  , 0.141524    ), Coef('Var'  , 0.0979359   ), Coef('Var'  , 0.0497602   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.339681    ), ], 
		[Coef('Var'  , 0.127047    ), Coef('Var'  , 0.117945    ), Coef('Var'  , 0.132723    ), Coef('Var'  , 0.185599    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.182416    ), ], 
		[Coef('Var'  , 0.0843676   ), Coef('Var'  , 0.125008    ), Coef('Var'  , 0.182681    ), Coef('Var'  , 0.331107    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0425092   ), ], 
		[Coef('Var'  , 0.0729488   ), Coef('Var'  , 0.0999216   ), Coef('Var'  , 0.125937    ), Coef('Var'  , 0.18512     ), Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0384702   ), ], 
		[Coef('Var'  , 0.0857925   ), Coef('Var'  , 0.0895687   ), Coef('Var'  , 0.0814688   ), Coef('Var'  , 0.0450071   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0467749   ), ], 
		[Coef('Var'  , 0.0665696   ), Coef('Var'  , 0.0693585   ), Coef('Var'  , 0.0684603   ), Coef('Var'  , 0.0362496   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0334021   ), ], 
		[Coef('Var'  , 0.0766101   ), Coef('Var'  , 0.0831767   ), Coef('Var'  , 0.079499    ), Coef('Var'  , 0.0425227   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0408911   ), ], 
		[Coef('Var'  , 0.0728309   ), Coef('Var'  , 0.082277    ), Coef('Var'  , 0.0747311   ), Coef('Var'  , 0.0412867   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0416799   ), ], 
		[Coef('Var'  , 0.0810586   ), Coef('Var'  , 0.0828284   ), Coef('Var'  , 0.0756032   ), Coef('Var'  , 0.0410924   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0427911   ), ], ])
	etat7.initMat[Chem([Sub('2')])] = FMat([
		[Coef('Var'  , 0.103677    ), Coef('Var'  , 0.110825    ), Coef('Var'  , 0.110977    ), Coef('Var'  , 0.110835    ), Coef('Var'  , 0.100389    ), Coef('Var'  , 0.102047    ), Coef('Var'  , 0.100291    ), Coef('Var'  , 0.101952    ), Coef('Var'  , 0.100826    ), Coef('Var'  , 0.101573    ), ], 
		[Coef('Var'  , 0.112438    ), Coef('Var'  , 0.114248    ), Coef('Var'  , 0.113694    ), Coef('Var'  , 0.115316    ), Coef('Var'  , 0.11659     ), Coef('Var'  , 0.110129    ), Coef('Var'  , 0.100858    ), Coef('Var'  , 0.0912957   ), Coef('Var'  , 0.0890979   ), Coef('Var'  , 0.100337    ), ], 
		[Coef('Var'  , 0.0990228   ), Coef('Var'  , 0.0894941   ), Coef('Var'  , 0.0874249   ), Coef('Var'  , 0.0911908   ), Coef('Var'  , 0.0953047   ), Coef('Var'  , 0.097387    ), Coef('Var'  , 0.0986555   ), Coef('Var'  , 0.10091     ), Coef('Var'  , 0.10641     ), Coef('Var'  , 0.101545    ), ], 
		[Coef('Var'  , 0.0983214   ), Coef('Var'  , 0.0846205   ), Coef('Var'  , 0.079018    ), Coef('Var'  , 0.0781594   ), Coef('Var'  , 0.087856    ), Coef('Var'  , 0.0984162   ), Coef('Var'  , 0.108263    ), Coef('Var'  , 0.116615    ), Coef('Var'  , 0.114957    ), Coef('Var'  , 0.109458    ), ], 
		[Coef('Var'  , 0.0809263   ), Coef('Var'  , 0.0817049   ), Coef('Var'  , 0.0868691   ), Coef('Var'  , 0.0942685   ), Coef('Var'  , 0.099889    ), Coef('Var'  , 0.0985852   ), Coef('Var'  , 0.0937937   ), Coef('Var'  , 0.08693     ), Coef('Var'  , 0.0836905   ), Coef('Var'  , 0.0794749   ), ], 
		[Coef('Var'  , 0.100396    ), Coef('Var'  , 0.0991764   ), Coef('Var'  , 0.103175    ), Coef('Var'  , 0.108089    ), Coef('Var'  , 0.111125    ), Coef('Var'  , 0.111717    ), Coef('Var'  , 0.107705    ), Coef('Var'  , 0.11084     ), Coef('Var'  , 0.110669    ), Coef('Var'  , 0.105591    ), ], 
		[Coef('Var'  , 0.102527    ), Coef('Var'  , 0.106889    ), Coef('Var'  , 0.107272    ), Coef('Var'  , 0.0965173   ), Coef('Var'  , 0.0856208   ), Coef('Var'  , 0.0826343   ), Coef('Var'  , 0.082898    ), Coef('Var'  , 0.0907903   ), Coef('Var'  , 0.0965929   ), Coef('Var'  , 0.0980185   ), ], 
		[Coef('Var'  , 0.112024    ), Coef('Var'  , 0.115196    ), Coef('Var'  , 0.10928     ), Coef('Var'  , 0.102734    ), Coef('Var'  , 0.0974248   ), Coef('Var'  , 0.0958981   ), Coef('Var'  , 0.0986922   ), Coef('Var'  , 0.101373    ), Coef('Var'  , 0.105379    ), Coef('Var'  , 0.110431    ), ], 
		[Coef('Var'  , 0.0878493   ), Coef('Var'  , 0.0932038   ), Coef('Var'  , 0.0922989   ), Coef('Var'  , 0.0941432   ), Coef('Var'  , 0.0910504   ), Coef('Var'  , 0.090435    ), Coef('Var'  , 0.093725    ), Coef('Var'  , 0.0879939   ), Coef('Var'  , 0.0857301   ), Coef('Var'  , 0.0875708   ), ], 
		[Coef('Var'  , 0.102818    ), Coef('Var'  , 0.104642    ), Coef('Var'  , 0.109991    ), Coef('Var'  , 0.108746    ), Coef('Var'  , 0.114751    ), Coef('Var'  , 0.112751    ), Coef('Var'  , 0.115118    ), Coef('Var'  , 0.1113      ), Coef('Var'  , 0.106648    ), Coef('Var'  , 0.106001    ), ], ])
	etat7.initMat[Chem([Sub('1')])] = FMat([
		[Coef('Var'  , 0.0931784   ), Coef('Var'  , 0.080435    ), Coef('Var'  , 0.0679483   ), Coef('Var'  , 0.0753321   ), Coef('Var'  , 0.08096     ), Coef('Var'  , 0.0954436   ), Coef('Var'  , 0.108682    ), Coef('Var'  , 0.10488     ), Coef('Var'  , 0.103677    ), Coef('Var'  , 0.0977454   ), ], 
		[Coef('Var'  , 0.0878259   ), Coef('Var'  , 0.083097    ), Coef('Var'  , 0.0704542   ), Coef('Var'  , 0.0861168   ), Coef('Var'  , 0.0979359   ), Coef('Var'  , 0.115001    ), Coef('Var'  , 0.129766    ), Coef('Var'  , 0.125197    ), Coef('Var'  , 0.112438    ), Coef('Var'  , 0.104091    ), ], 
		[Coef('Var'  , 0.122425    ), Coef('Var'  , 0.136717    ), Coef('Var'  , 0.148911    ), Coef('Var'  , 0.134631    ), Coef('Var'  , 0.132723    ), Coef('Var'  , 0.109681    ), Coef('Var'  , 0.0992633   ), Coef('Var'  , 0.097123    ), Coef('Var'  , 0.0990228   ), Coef('Var'  , 0.111501    ), ], 
		[Coef('Var'  , 0.116124    ), Coef('Var'  , 0.142148    ), Coef('Var'  , 0.187798    ), Coef('Var'  , 0.169431    ), Coef('Var'  , 0.182681    ), Coef('Var'  , 0.130055    ), Coef('Var'  , 0.0965481   ), Coef('Var'  , 0.0958921   ), Coef('Var'  , 0.0983214   ), Coef('Var'  , 0.105285    ), ], 
		[Coef('Var'  , 0.0929071   ), Coef('Var'  , 0.101595    ), Coef('Var'  , 0.123519    ), Coef('Var'  , 0.117958    ), Coef('Var'  , 0.125937    ), Coef('Var'  , 0.106142    ), Coef('Var'  , 0.0888317   ), Coef('Var'  , 0.082063    ), Coef('Var'  , 0.0809263   ), Coef('Var'  , 0.0854934   ), ], 
		[Coef('Var'  , 0.114742    ), Coef('Var'  , 0.105258    ), Coef('Var'  , 0.0957903   ), Coef('Var'  , 0.0930847   ), Coef('Var'  , 0.0814688   ), Coef('Var'  , 0.0888213   ), Coef('Var'  , 0.0925178   ), Coef('Var'  , 0.0939964   ), Coef('Var'  , 0.100396    ), Coef('Var'  , 0.106297    ), ], 
		[Coef('Var'  , 0.1117      ), Coef('Var'  , 0.101841    ), Coef('Var'  , 0.088659    ), Coef('Var'  , 0.0806621   ), Coef('Var'  , 0.0684603   ), Coef('Var'  , 0.0832043   ), Coef('Var'  , 0.0933698   ), Coef('Var'  , 0.0991236   ), Coef('Var'  , 0.102527    ), Coef('Var'  , 0.106349    ), ], 
		[Coef('Var'  , 0.101104    ), Coef('Var'  , 0.0975876   ), Coef('Var'  , 0.0838492   ), Coef('Var'  , 0.0885489   ), Coef('Var'  , 0.079499    ), Coef('Var'  , 0.0937781   ), Coef('Var'  , 0.100444    ), Coef('Var'  , 0.108058    ), Coef('Var'  , 0.112024    ), Coef('Var'  , 0.108622    ), ], 
		[Coef('Var'  , 0.0730522   ), Coef('Var'  , 0.0709829   ), Coef('Var'  , 0.0650747   ), Coef('Var'  , 0.0776969   ), Coef('Var'  , 0.0747311   ), Coef('Var'  , 0.0847036   ), Coef('Var'  , 0.0879204   ), Coef('Var'  , 0.0877019   ), Coef('Var'  , 0.0878493   ), Coef('Var'  , 0.0806858   ), ], 
		[Coef('Var'  , 0.0869417   ), Coef('Var'  , 0.0803371   ), Coef('Var'  , 0.0679963   ), Coef('Var'  , 0.0765374   ), Coef('Var'  , 0.0756032   ), Coef('Var'  , 0.0931702   ), Coef('Var'  , 0.102657    ), Coef('Var'  , 0.105965    ), Coef('Var'  , 0.102818    ), Coef('Var'  , 0.0939309   ), ], ])
	etat7.initMat[Chem([Sub('0')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0522617   ), Coef('Var'  , 0.0908735   ), Coef('Var'  , 0.0948156   ), Coef('Var'  , 0.0798484   ), Coef('Var'  , 0.0425842   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0410467   ), Coef('Var'  , 0.0731485   ), Coef('Var'  , 0.0852453   ), Coef('Var'  , 0.0807142   ), Coef('Var'  , 0.0459197   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0361183   ), Coef('Var'  , 0.0708796   ), Coef('Var'  , 0.0682297   ), Coef('Var'  , 0.064043    ), Coef('Var'  , 0.0341975   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0376982   ), Coef('Var'  , 0.0723256   ), Coef('Var'  , 0.0777715   ), Coef('Var'  , 0.0760315   ), Coef('Var'  , 0.0423797   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.179579    ), Coef('Var'  , 0.118114    ), Coef('Var'  , 0.0922579   ), Coef('Var'  , 0.0732931   ), Coef('Var'  , 0.0361905   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.324551    ), Coef('Var'  , 0.175249    ), Coef('Var'  , 0.114755    ), Coef('Var'  , 0.0762804   ), Coef('Var'  , 0.0370699   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.190582    ), Coef('Var'  , 0.141032    ), Coef('Var'  , 0.127216    ), Coef('Var'  , 0.128774    ), Coef('Var'  , 0.183687    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0486609   ), Coef('Var'  , 0.0944095   ), Coef('Var'  , 0.136118    ), Coef('Var'  , 0.192616    ), Coef('Var'  , 0.33729     ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0428288   ), Coef('Var'  , 0.0803354   ), Coef('Var'  , 0.110366    ), Coef('Var'  , 0.138384    ), Coef('Var'  , 0.192321    ), Coef('Const', 0.25        ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.046673    ), Coef('Var'  , 0.0836333   ), Coef('Var'  , 0.0932243   ), Coef('Var'  , 0.0900155   ), Coef('Var'  , 0.0483595   ), Coef('Const', 0           ), Coef('Const', 0           ), ], ])
	etat7.initMat[Chem([Sub('G')])] = FMat([
		[Coef('Const', 0.1         )], 
		[Coef('Const', 0.1         )], 
		[Coef('Const', 0.1         )], 
		[Coef('Const', 0.1         )], 
		[Coef('Const', 0.1         )], 
		[Coef('Const', 0.1         )], 
		[Coef('Const', 0.1         )], 
		[Coef('Const', 0.1         )], 
		[Coef('Const', 0.1         )], 
		[Coef('Const', 0.1         )], ])
	etat7.initMat[Chem([Sub('10')])] = FMat([
		[Coef('Const', 0           ), Coef('Var'  , 0.038906    ), Coef('Var'  , 0.0748952   ), Coef('Var'  , 0.093911    ), Coef('Var'  , 0.115961    ), Coef('Var'  , 0.177982    ), Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0419602   ), Coef('Var'  , 0.0803264   ), Coef('Var'  , 0.0817213   ), Coef('Var'  , 0.0767638   ), Coef('Var'  , 0.0397417   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0362729   ), Coef('Var'  , 0.0685749   ), Coef('Var'  , 0.0779976   ), Coef('Var'  , 0.0792932   ), Coef('Var'  , 0.043495    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0440277   ), Coef('Var'  , 0.0788117   ), Coef('Var'  , 0.0793808   ), Coef('Var'  , 0.0712113   ), Coef('Var'  , 0.0373176   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0494231   ), Coef('Var'  , 0.0874287   ), Coef('Var'  , 0.0955088   ), Coef('Var'  , 0.0865893   ), Coef('Var'  , 0.0479498   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0314503   ), Coef('Var'  , 0.060076    ), Coef('Var'  , 0.0684972   ), Coef('Var'  , 0.0705703   ), Coef('Var'  , 0.0378818   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.25        ), Coef('Var'  , 0.176678    ), Coef('Var'  , 0.110612    ), Coef('Var'  , 0.0836022   ), Coef('Var'  , 0.0634509   ), Coef('Var'  , 0.03215     ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.5         ), Coef('Var'  , 0.333299    ), Coef('Var'  , 0.187573    ), Coef('Var'  , 0.13434     ), Coef('Var'  , 0.0949229   ), Coef('Var'  , 0.0502513   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0.25        ), Coef('Var'  , 0.19342     ), Coef('Var'  , 0.144862    ), Coef('Var'  , 0.132693    ), Coef('Var'  , 0.134632    ), Coef('Var'  , 0.187889    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0545623   ), Coef('Var'  , 0.10684     ), Coef('Var'  , 0.152348    ), Coef('Var'  , 0.206605    ), Coef('Var'  , 0.345342    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), ], ])
	etat7.initMat[Chem([Sub('9')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0348578   ), Coef('Var'  , 0.0679483   ), Coef('Var'  , 0.0788291   ), Coef('Var'  , 0.0815724   ), Coef('Var'  , 0.0447595   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0390223   ), Coef('Var'  , 0.0704542   ), Coef('Var'  , 0.0670548   ), Coef('Var'  , 0.0610968   ), Coef('Var'  , 0.0309526   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.198033    ), Coef('Var'  , 0.148911    ), Coef('Var'  , 0.128192    ), Coef('Var'  , 0.100378    ), Coef('Var'  , 0.0548993   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.332874    ), Coef('Var'  , 0.187798    ), Coef('Var'  , 0.132364    ), Coef('Var'  , 0.0924411   ), Coef('Var'  , 0.0482234   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.179756    ), Coef('Var'  , 0.123519    ), Coef('Var'  , 0.112591    ), Coef('Var'  , 0.123774    ), Coef('Var'  , 0.182039    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0502949   ), Coef('Var'  , 0.0957903   ), Coef('Var'  , 0.133081    ), Coef('Var'  , 0.184079    ), Coef('Var'  , 0.330365    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0460815   ), Coef('Var'  , 0.088659    ), Coef('Var'  , 0.121683    ), Coef('Var'  , 0.149967    ), Coef('Var'  , 0.200411    ), Coef('Const', 0.25        ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.046484    ), Coef('Var'  , 0.0838492   ), Coef('Var'  , 0.0893744   ), Coef('Var'  , 0.0805822   ), Coef('Var'  , 0.0425349   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0361879   ), Coef('Var'  , 0.0650747   ), Coef('Var'  , 0.0656626   ), Coef('Var'  , 0.0587033   ), Coef('Var'  , 0.029561    ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.036409    ), Coef('Var'  , 0.0679963   ), Coef('Var'  , 0.0711692   ), Coef('Var'  , 0.067406    ), Coef('Var'  , 0.0362544   ), Coef('Const', 0           ), Coef('Const', 0           ), ], ])
	
	
	
	etat8.bords   = {Bord('2'): etat12, Bord('1'): etat12, Bord('0'): etat12, }
	etat8.permuts = {}
	etat8.interns = {Intern('_'): etat8, }
	etat8.subs    = {Sub('6'): etat8, Sub('5'): etat8, Sub('4'): etat8, Sub('3'): etat8, Sub('2'): etat8, Sub('1'): etat8, Sub('0'): etat8, Sub('G', True): Etat.etatPoint, }
	
	etat8.buildIntern()
	
	
	etat8.eqs = [
		(Chem([Bord('0'), Sub('0'), Permut('0'), ])	,	Chem([Sub('0'), Bord('0'), ])),
		(Chem([Bord('2'), Sub('2'), Permut('0'), ])	,	Chem([Sub('0'), Bord('1'), ])),
		(Chem([Bord('0'), Sub('1'), Permut('0'), ])	,	Chem([Sub('1'), Bord('0'), ])),
		(Chem([Bord('0'), Sub('2'), Permut('0'), ])	,	Chem([Sub('2'), Bord('0'), ])),
		(Chem([Bord('1'), Sub('0'), Permut('0'), ])	,	Chem([Sub('2'), Bord('2'), ])),
		(Chem([Bord('2'), Sub('0'), Permut('0'), ])	,	Chem([Sub('3'), Bord('0'), ])),
		(Chem([Bord('1'), Sub('2'), Permut('0'), ])	,	Chem([Sub('3'), Bord('1'), ])),
		(Chem([Bord('2'), Sub('1'), Permut('0'), ])	,	Chem([Sub('4'), Bord('1'), ])),
		(Chem([Bord('1'), Sub('1'), Permut('0'), ])	,	Chem([Sub('6'), Bord('0'), ])),
		(Chem([Sub('0'), Bord('1'), Bord('1'), ])	,	Chem([Sub('4'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('2'), Bord('1'), ])	,	Chem([Sub('1'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('1'), Bord('1'), ])	,	Chem([Sub('5'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('2'), Bord('1'), ])	,	Chem([Sub('2'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('1'), Bord('1'), ])	,	Chem([Sub('6'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('3'), Bord('1'), Bord('1'), ])	,	Chem([Sub('6'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('3'), Bord('2'), Bord('1'), ])	,	Chem([Sub('4'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('4'), Bord('2'), Bord('1'), ])	,	Chem([Sub('5'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('5'), Bord('2'), Bord('1'), ])	,	Chem([Sub('6'), Bord('1'), Bord('1'), ])),
		(Chem([Bord('0'), Bord('1'), ])	,	Chem([Bord('1'), Bord('0'), ])),
		(Chem([Bord('1'), Bord('1'), ])	,	Chem([Bord('2'), Bord('0'), ])),
		(Chem([Bord('2'), Bord('1'), ])	,	Chem([Bord('0'), Bord('0'), ])),
		]
	
	
	etat8.prim.elems = [Figure(2, [Chem([Bord('0'), Sub('0'), Bord('0'), ]), Chem([Bord('0'), Sub('1'), Bord('0'), ]), Chem([Bord('0'), Sub('2'), Bord('0'), ]), Chem([Bord('1'), Sub('0'), Bord('0'), ]), Chem([Bord('1'), Sub('1'), Bord('0'), ]), Chem([Bord('1'), Sub('2'), Bord('0'), ]), Chem([Bord('2'), Sub('0'), Bord('0'), ]), Chem([Bord('2'), Sub('1'), Bord('0'), ]), Chem([Bord('2'), Sub('2'), Bord('0'), ]), ])]
	etat8.grid.elems = [
		Figure(1, [Chem([Bord('0'), Bord('0'), ]), Chem([Bord('0'), Intern(''), ]), Chem([Bord('0'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('1'), Bord('0'), ]), Chem([Bord('1'), Intern(''), ]), Chem([Bord('1'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('2'), Bord('0'), ]), Chem([Bord('2'), Intern(''), ]), Chem([Bord('2'), Bord('1'), ]), ]), ]
	
	
	etat8.space = [Chem([Bord('0'), Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('0'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('2'), Intern('0'), Intern('0'), ]), ]
	
	etat8.initMat[Chem([Sub('6')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0741514   ), Coef('Var'  , 0.132006    ), Coef('Var'  , 0.0730675   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0515323   ), Coef('Var'  , 0.0934992   ), Coef('Var'  , 0.0504129   ), ], 
		[Coef('Var'  , 0.261889    ), Coef('Var'  , 0.390793    ), Coef('Var'  , 0.537279    ), Coef('Var'  , 0.374874    ), Coef('Var'  , 0.255619    ), Coef('Var'  , 0.250363    ), ], 
		[Coef('Var'  , 0.200832    ), Coef('Var'  , 0.218414    ), Coef('Var'  , 0.200832    ), Coef('Var'  , 0.190738    ), Coef('Var'  , 0.163282    ), Coef('Var'  , 0.19243     ), ], 
		[Coef('Var'  , 0.537279    ), Coef('Var'  , 0.390793    ), Coef('Var'  , 0.261889    ), Coef('Var'  , 0.256165    ), Coef('Var'  , 0.264201    ), Coef('Var'  , 0.38003     ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0525405   ), Coef('Var'  , 0.0913926   ), Coef('Var'  , 0.0536975   ), ], ])
	etat8.initMat[Chem([Sub('5')])] = FMat([
		[Coef('Var'  , 0.132006    ), Coef('Var'  , 0.18305     ), Coef('Var'  , 0.244134    ), Coef('Var'  , 0.224509    ), Coef('Var'  , 0.251033    ), Coef('Var'  , 0.188749    ), ], 
		[Coef('Var'  , 0.0934992   ), Coef('Var'  , 0.147554    ), Coef('Var'  , 0.184199    ), Coef('Var'  , 0.155983    ), Coef('Var'  , 0.101797    ), Coef('Var'  , 0.109435    ), ], 
		[Coef('Var'  , 0.255619    ), Coef('Var'  , 0.248667    ), Coef('Var'  , 0.269148    ), Coef('Var'  , 0.191386    ), Coef('Var'  , 0.120602    ), Coef('Var'  , 0.178433    ), ], 
		[Coef('Var'  , 0.163282    ), Coef('Var'  , 0.121325    ), Coef('Var'  , 0.0741029   ), Coef('Var'  , 0.090456    ), Coef('Var'  , 0.0892141   ), Coef('Var'  , 0.135277    ), ], 
		[Coef('Var'  , 0.264201    ), Coef('Var'  , 0.197917    ), Coef('Var'  , 0.13739     ), Coef('Var'  , 0.195777    ), Coef('Var'  , 0.263676    ), Coef('Var'  , 0.248255    ), ], 
		[Coef('Var'  , 0.0913926   ), Coef('Var'  , 0.101487    ), Coef('Var'  , 0.0910253   ), Coef('Var'  , 0.141889    ), Coef('Var'  , 0.173677    ), Coef('Var'  , 0.139852    ), ], ])
	etat8.initMat[Chem([Sub('4')])] = FMat([
		[Coef('Var'  , 0.251033    ), Coef('Var'  , 0.372803    ), Coef('Var'  , 0.537279    ), Coef('Var'  , 0.390793    ), Coef('Var'  , 0.261889    ), Coef('Var'  , 0.248601    ), ], 
		[Coef('Var'  , 0.101797    ), Coef('Var'  , 0.0596108   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0587989   ), ], 
		[Coef('Var'  , 0.120602    ), Coef('Var'  , 0.0594144   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0594903   ), ], 
		[Coef('Var'  , 0.0892141   ), Coef('Var'  , 0.0546219   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0543373   ), ], 
		[Coef('Var'  , 0.263676    ), Coef('Var'  , 0.256439    ), Coef('Var'  , 0.261889    ), Coef('Var'  , 0.390793    ), Coef('Var'  , 0.537279    ), Coef('Var'  , 0.38032     ), ], 
		[Coef('Var'  , 0.173677    ), Coef('Var'  , 0.197111    ), Coef('Var'  , 0.200832    ), Coef('Var'  , 0.218414    ), Coef('Var'  , 0.200832    ), Coef('Var'  , 0.198452    ), ], ])
	etat8.initMat[Chem([Sub('3')])] = FMat([
		[Coef('Var'  , 0.261889    ), Coef('Var'  , 0.132017    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.134365    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.00169705  ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.132017    ), Coef('Var'  , 0.261889    ), Coef('Var'  , 0.134134    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.109252    ), Coef('Var'  , 0.200832    ), Coef('Var'  , 0.108144    ), ], 
		[Coef('Var'  , 0.537279    ), Coef('Var'  , 0.758731    ), Coef('Const', 1           ), Coef('Var'  , 0.758731    ), Coef('Var'  , 0.537279    ), Coef('Var'  , 0.512923    ), ], 
		[Coef('Var'  , 0.200832    ), Coef('Var'  , 0.109252    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.108738    ), ], ])
	etat8.initMat[Chem([Sub('2')])] = FMat([
		[Coef('Const', 0           ), Coef('Var'  , 0.132017    ), Coef('Var'  , 0.261889    ), Coef('Var'  , 0.133437    ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.109252    ), Coef('Var'  , 0.200832    ), Coef('Var'  , 0.109225    ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 1           ), Coef('Var'  , 0.758731    ), Coef('Var'  , 0.537279    ), Coef('Var'  , 0.514576    ), Coef('Var'  , 0.537279    ), Coef('Var'  , 0.758731    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.109005    ), Coef('Var'  , 0.200832    ), Coef('Var'  , 0.109252    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.132458    ), Coef('Var'  , 0.261889    ), Coef('Var'  , 0.132017    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.00129846  ), Coef('Const', 0           ), Coef('Const', 0           ), ], ])
	etat8.initMat[Chem([Sub('1')])] = FMat([
		[Coef('Var'  , 0.261889    ), Coef('Var'  , 0.390793    ), Coef('Var'  , 0.537279    ), Coef('Var'  , 0.366334    ), Coef('Var'  , 0.244134    ), Coef('Var'  , 0.240073    ), ], 
		[Coef('Var'  , 0.200832    ), Coef('Var'  , 0.218414    ), Coef('Var'  , 0.200832    ), Coef('Var'  , 0.20542     ), Coef('Var'  , 0.184199    ), Coef('Var'  , 0.204951    ), ], 
		[Coef('Var'  , 0.537279    ), Coef('Var'  , 0.390793    ), Coef('Var'  , 0.261889    ), Coef('Var'  , 0.263178    ), Coef('Var'  , 0.269148    ), Coef('Var'  , 0.389692    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0389094   ), Coef('Var'  , 0.0741029   ), Coef('Var'  , 0.0386685   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0736642   ), Coef('Var'  , 0.13739     ), Coef('Var'  , 0.0760107   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0524938   ), Coef('Var'  , 0.0910253   ), Coef('Var'  , 0.0506054   ), ], ])
	etat8.initMat[Chem([Sub('0')])] = FMat([
		[Coef('Var'  , 0.537279    ), Coef('Var'  , 0.758731    ), Coef('Const', 1           ), Coef('Var'  , 0.758731    ), Coef('Var'  , 0.537279    ), Coef('Var'  , 0.513573    ), ], 
		[Coef('Var'  , 0.200832    ), Coef('Var'  , 0.109252    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.110325    ), ], 
		[Coef('Var'  , 0.261889    ), Coef('Var'  , 0.132017    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.134496    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.00151769  ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.132017    ), Coef('Var'  , 0.261889    ), Coef('Var'  , 0.131902    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.109252    ), Coef('Var'  , 0.200832    ), Coef('Var'  , 0.108186    ), ], ])
	etat8.initMat[Chem([Sub('G')])] = FMat([
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], ])
	
	
	
	etat9.bords   = {Bord('2'): etat10, Bord('1'): etat10, Bord('0'): etat12, }
	etat9.permuts = {}
	etat9.interns = {Intern('_'): etat9, }
	etat9.subs    = {Sub('3'): etat9, Sub('2'): etat9, Sub('1'): etat9, Sub('0'): etat6, Sub('G', True): Etat.etatPoint, }
	
	etat9.buildIntern()
	
	
	etat9.eqs = [
		(Chem([Bord('1'), Sub('1'), Permut('0'), ])	,	Chem([Sub('0'), Bord('0'), ])),
		(Chem([Bord('2'), Sub('0'), Permut('0'), ])	,	Chem([Sub('0'), Bord('3'), ])),
		(Chem([Bord('0'), Sub('0'), Permut('0'), ])	,	Chem([Sub('1'), Bord('0'), ])),
		(Chem([Bord('2'), Sub('1'), Permut('0'), ])	,	Chem([Sub('1'), Bord('1'), ])),
		(Chem([Bord('0'), Sub('1'), Permut('0'), ])	,	Chem([Sub('2'), Bord('0'), ])),
		(Chem([Bord('0'), Sub('2'), Permut('0'), ])	,	Chem([Sub('3'), Bord('0'), ])),
		(Chem([Bord('1'), Sub('0'), Permut('0'), ])	,	Chem([Sub('3'), Bord('2'), ])),
		(Chem([Sub('0'), Bord('0'), Bord('1'), ])	,	Chem([Sub('3'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('1'), Bord('1'), ])	,	Chem([Sub('2'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('2'), Bord('1'), ])	,	Chem([Sub('1'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('2'), Bord('1'), ])	,	Chem([Sub('2'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('2'), Bord('1'), ])	,	Chem([Sub('3'), Bord('0'), Bord('1'), ])),
		(Chem([Bord('0'), Bord('1'), ])	,	Chem([Bord('1'), Bord('0'), ])),
		(Chem([Bord('1'), Bord('1'), ])	,	Chem([Bord('2'), Bord('0'), ])),
		(Chem([Bord('2'), Bord('1'), ])	,	Chem([Bord('0'), Bord('0'), ])),
		]
	
	
	etat9.prim.elems = [Figure(2, [Chem([Bord('0'), Sub('0'), Bord('0'), ]), Chem([Bord('0'), Sub('1'), Bord('0'), ]), Chem([Bord('0'), Sub('2'), Bord('0'), ]), Chem([Bord('1'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('1'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('1'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('1'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('2'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('2'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('2'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('2'), Sub('1'), Sub('1'), Bord('0'), ]), ])]
	etat9.grid.elems = [
		Figure(1, [Chem([Bord('0'), Bord('0'), ]), Chem([Bord('0'), Intern(''), ]), Chem([Bord('0'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('1'), Bord('0'), ]), Chem([Bord('1'), Intern(''), ]), Chem([Bord('1'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('2'), Bord('0'), ]), Chem([Bord('2'), Intern(''), ]), Chem([Bord('2'), Bord('1'), ]), ]), ]
	
	
	etat9.space = [Chem([Bord('0'), Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('0'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('2'), Intern('0'), Intern('0'), ]), ]
	
	etat9.initMat[Chem([Sub('3')])] = FMat([
		[Coef('Const', 0           ), Coef('Var'  , 0.132017    ), Coef('Var'  , 0.261889    ), Coef('Var'  , 0.114676    ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.109252    ), Coef('Var'  , 0.200832    ), Coef('Var'  , 0.151524    ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 1           ), Coef('Var'  , 0.758731    ), Coef('Var'  , 0.537279    ), Coef('Var'  , 0.359006    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.248378    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.12498     ), Coef('Const', 0.25        ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0014366   ), Coef('Const', 0           ), Coef('Const', 0           ), ], ])
	etat9.initMat[Chem([Sub('2')])] = FMat([
		[Coef('Var'  , 0.261889    ), Coef('Var'  , 0.390793    ), Coef('Var'  , 0.537279    ), Coef('Var'  , 0.317657    ), Coef('Var'  , 0.191379    ), Coef('Var'  , 0.196846    ), ], 
		[Coef('Var'  , 0.200832    ), Coef('Var'  , 0.218414    ), Coef('Var'  , 0.200832    ), Coef('Var'  , 0.24795     ), Coef('Var'  , 0.182976    ), Coef('Var'  , 0.250265    ), ], 
		[Coef('Var'  , 0.537279    ), Coef('Var'  , 0.390793    ), Coef('Var'  , 0.261889    ), Coef('Var'  , 0.24344     ), Coef('Var'  , 0.248239    ), Coef('Var'  , 0.361481    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0657857   ), Coef('Var'  , 0.128061    ), Coef('Var'  , 0.0640881   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.070946    ), Coef('Var'  , 0.135596    ), Coef('Var'  , 0.073127    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0542207   ), Coef('Var'  , 0.113749    ), Coef('Var'  , 0.0541931   ), ], ])
	etat9.initMat[Chem([Sub('1')])] = FMat([
		[Coef('Var'  , 0.537279    ), Coef('Var'  , 0.758731    ), Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.358108    ), ], 
		[Coef('Var'  , 0.200832    ), Coef('Var'  , 0.109252    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.150284    ), ], 
		[Coef('Var'  , 0.261889    ), Coef('Var'  , 0.132017    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.114393    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.00200331  ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.125609    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.249602    ), ], ])
	etat9.initMat[Chem([Sub('0')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0830256   ), Coef('Var'  , 0.191379    ), Coef('Var'  , 0.20659     ), Coef('Const', 0.25        ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.100407    ), Coef('Var'  , 0.182976    ), Coef('Var'  , 0.101351    ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.253306    ), Coef('Var'  , 0.248239    ), Coef('Var'  , 0.129896    ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.314295    ), Coef('Var'  , 0.128061    ), Coef('Var'  , 0.0657367   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.195149    ), Coef('Var'  , 0.135596    ), Coef('Var'  , 0.195067    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0538172   ), Coef('Var'  , 0.113749    ), Coef('Var'  , 0.30136     ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), ], ])
	etat9.initMat[Chem([Sub('G')])] = FMat([
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], ])
	
	
	
	etat10.bords   = {Bord('1'): etat13, Bord('0'): etat13, }
	etat10.permuts = {Permut('0'): etat10, }
	etat10.interns = {Intern('_'): etat10, }
	etat10.subs    = {Sub('1'): etat10, Sub('0'): etat10, Sub('G', True): Etat.etatPoint, }
	
	etat10.buildIntern()
	etat10.fm_[Permut('0')] = PMat(3, [2, 1, 0, ])
	
	
	etat10.eqs = [
		(Chem([Permut('0'), Bord('0'), ])	,	Chem([Bord('1')])),
		(Chem([Permut('0'), Bord('1'), ])	,	Chem([Bord('0')])),
		(Chem([Permut('0'), Intern(''), ])	,	Chem([Intern('')])),
		(Chem([Permut('0'), Sub('0'), ])	,	Chem([Sub('1'), Permut('0'), ])),
		(Chem([Permut('0'), Sub('1'), ])	,	Chem([Sub('0'), Permut('0'), ])),
		]
	
	
	etat10.prim.elems = [Figure(1, [Chem([Bord('0')]), Chem([Bord('1')]), ])]
	etat10.grid.elems = [Figure(1, [Chem([Bord('0')]), Chem([Intern('')]), Chem([Bord('1')]), ])]
	
	
	etat10.space = [Chem([Bord('0'), Intern('0'), Intern('0'), ]), Chem([Intern('0'), Intern('0'), ]), Chem([Bord('1'), Intern('0'), Intern('0'), ]), ]
	
	etat10.initMat[Chem([Sub('1')])] = FMat([
		[Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), ], ])
	etat10.initMat[Chem([Sub('0')])] = FMat([
		[Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), ], ])
	etat10.initMat[Chem([Sub('G')])] = FMat([
		[Coef('Const', 0           )], 
		[Coef('Const', 1           )], 
		[Coef('Const', 0           )], ])
	
	
	
	etat11.bords   = {Bord('1'): etat13, Bord('0'): etat13, }
	etat11.permuts = {Permut('0'): etat11, }
	etat11.interns = {Intern('_'): etat11, }
	etat11.subs    = {Sub('3'): etat11, Sub('2'): etat11, Sub('1'): etat11, Sub('0'): etat11, Sub('G', True): Etat.etatPoint, }
	
	etat11.buildIntern()
	etat11.fm_[Permut('0')] = PMat(3, [2, 1, 0, ])
	
	
	etat11.eqs = [
		(Chem([Permut('0'), Bord('0'), ])	,	Chem([Bord('1')])),
		(Chem([Permut('0'), Bord('1'), ])	,	Chem([Bord('0')])),
		(Chem([Permut('0'), Intern(''), ])	,	Chem([Intern('')])),
		(Chem([Permut('0'), Sub('0'), ])	,	Chem([Sub('3'), Permut('0'), ])),
		(Chem([Permut('0'), Sub('1'), ])	,	Chem([Sub('2'), Permut('0'), ])),
		(Chem([Permut('0'), Sub('2'), ])	,	Chem([Sub('1'), Permut('0'), ])),
		(Chem([Permut('0'), Sub('3'), ])	,	Chem([Sub('0'), Permut('0'), ])),
		]
	
	
	etat11.prim.elems = [Figure(1, [Chem([Bord('0')]), Chem([Bord('1')]), ])]
	etat11.grid.elems = [Figure(1, [Chem([Bord('0')]), Chem([Intern('')]), Chem([Bord('1')]), ])]
	
	
	etat11.space = [Chem([Bord('0'), Intern('0'), Intern('0'), ]), Chem([Intern('0'), Intern('0'), ]), Chem([Bord('1'), Intern('0'), Intern('0'), ]), ]
	
	etat11.initMat[Chem([Sub('3')])] = FMat([
		[Coef('Const', 0.0625      ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.375       ), Coef('Const', 0.25        ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.5625      ), Coef('Const', 0.75        ), Coef('Const', 1           ), ], ])
	etat11.initMat[Chem([Sub('2')])] = FMat([
		[Coef('Const', 0.25        ), Coef('Const', 0.125       ), Coef('Const', 0.0625      ), ], 
		[Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0.375       ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0.375       ), Coef('Const', 0.5625      ), ], ])
	etat11.initMat[Chem([Sub('1')])] = FMat([
		[Coef('Const', 0.5625      ), Coef('Const', 0.375       ), Coef('Const', 0.25        ), ], 
		[Coef('Const', 0.375       ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0.0625      ), Coef('Const', 0.125       ), Coef('Const', 0.25        ), ], ])
	etat11.initMat[Chem([Sub('0')])] = FMat([
		[Coef('Const', 1           ), Coef('Const', 0.75        ), Coef('Const', 0.5625      ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Const', 0.375       ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.0625      ), ], ])
	etat11.initMat[Chem([Sub('G')])] = FMat([
		[Coef('Const', 0           )], 
		[Coef('Const', 1           )], 
		[Coef('Const', 0           )], ])
	
	
	
	etat12.bords   = {Bord('1'): etat13, Bord('0'): etat13, }
	etat12.permuts = {Permut('0'): etat12, }
	etat12.interns = {Intern('_'): etat12, }
	etat12.subs    = {Sub('2'): etat12, Sub('1'): etat12, Sub('0'): etat12, Sub('G', True): Etat.etatPoint, }
	
	etat12.buildIntern()
	etat12.fm_[Permut('0')] = PMat(3, [2, 1, 0, ])
	
	
	etat12.eqs = [
		(Chem([Permut('0'), Bord('0'), ])	,	Chem([Bord('1')])),
		(Chem([Permut('0'), Bord('1'), ])	,	Chem([Bord('0')])),
		(Chem([Permut('0'), Intern(''), ])	,	Chem([Intern('')])),
		(Chem([Permut('0'), Sub('0'), ])	,	Chem([Sub('2'), Permut('0'), ])),
		(Chem([Permut('0'), Sub('1'), ])	,	Chem([Sub('1'), Permut('0'), ])),
		(Chem([Permut('0'), Sub('2'), ])	,	Chem([Sub('0'), Permut('0'), ])),
		]
	
	
	etat12.prim.elems = [Figure(1, [Chem([Bord('0')]), Chem([Bord('1')]), ])]
	etat12.grid.elems = [Figure(1, [Chem([Bord('0')]), Chem([Intern('')]), Chem([Bord('1')]), ])]
	
	
	etat12.space = [Chem([Bord('0'), Intern('0'), Intern('0'), ]), Chem([Intern('0'), Intern('0'), ]), Chem([Bord('1'), Intern('0'), Intern('0'), ]), ]
	
	etat12.initMat[Chem([Sub('2')])] = FMat([
		[Coef('Var'  , 0.261889    ), Coef('Var'  , 0.132017    ), Coef('Const', 0           ), ], 
		[Coef('Var'  , 0.200832    ), Coef('Var'  , 0.109252    ), Coef('Const', 0           ), ], 
		[Coef('Var'  , 0.537279    ), Coef('Var'  , 0.758731    ), Coef('Const', 1           ), ], ])
	etat12.initMat[Chem([Sub('1')])] = FMat([
		[Coef('Var'  , 0.537279    ), Coef('Var'  , 0.390793    ), Coef('Var'  , 0.261889    ), ], 
		[Coef('Var'  , 0.200832    ), Coef('Var'  , 0.218414    ), Coef('Var'  , 0.200832    ), ], 
		[Coef('Var'  , 0.261889    ), Coef('Var'  , 0.390793    ), Coef('Var'  , 0.537279    ), ], ])
	etat12.initMat[Chem([Sub('0')])] = FMat([
		[Coef('Const', 1           ), Coef('Var'  , 0.758731    ), Coef('Var'  , 0.537279    ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.109252    ), Coef('Var'  , 0.200832    ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.132017    ), Coef('Var'  , 0.261889    ), ], ])
	etat12.initMat[Chem([Sub('G')])] = FMat([
		[Coef('Const', 0           )], 
		[Coef('Const', 1           )], 
		[Coef('Const', 0           )], ])
	
	
	
	etat13.bords   = {}
	etat13.permuts = {}
	etat13.interns = {Intern('_'): etat13, }
	etat13.subs    = {Sub('0'): etat13, Sub('G', True): Etat.etatPoint, }
	
	etat13.buildIntern()
	
	
	etat13.eqs = [
		]
	
	
	etat13.prim.elems = []
	etat13.grid.elems = []
	
	
	etat13.space = [Chem([Intern('0'), Intern('0'), ])]
	
	etat13.initMat[Chem([Sub('0')])] = FMat([[Coef('Var'  , 1           )]])
	etat13.initMat[Chem([Sub('G')])] = FMat([[Coef('Const', 1           )]])
	
	
	
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
