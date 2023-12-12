# -*- coding: utf-8 -*-

# Automatically generated, from file : result_poly_matrices_square.py, function : modele()

from __future__ import division
import sys
if './../../../../../../python' not in sys.path:
	sys.path.append('./../../../../../../python')
from etat import *

def modele():
	
	etat0 = EtatInit()
	etat1 = Etat('Cell_0',0)
	etat2 = Etat('B2',1)
	etat3 = Etat('s',1)
	
	
	etat0.subs   = {Sub('0'): etat1, }
	
	etat0.eqs = [
		]
	
	
	etat0.space = []
	
	etat0.initMat[Chem([Sub('0')])] = FMat([
		[Coef('Var'  ,-0.184095    ), Coef('Var'  ,-1.21254     ), Coef('Var'  ,-1.49978     ), Coef('Var'  ,-0.878262    ), Coef('Var'  , 0.288261    ), Coef('Var'  , 1.31665     ), Coef('Var'  , 1.6039      ), Coef('Var'  , 0.982535    ), ], 
		[Coef('Var'  , 1.58438     ), Coef('Var'  , 0.963152    ), Coef('Var'  ,-0.203551    ), Coef('Var'  ,-1.23167     ), Coef('Var'  ,-1.51887     ), Coef('Var'  ,-0.897636    ), Coef('Var'  , 0.268998    ), Coef('Var'  , 1.29728     ), ], 
		[Coef('Var'  , 1.64843e-09 ), Coef('Var'  , 1.88522e-09 ), Coef('Var'  , 2.01124e-09 ), Coef('Var'  , 6.06908e-10 ), Coef('Var'  , 6.45539e-10 ), Coef('Var'  , 1.13181e-09 ), Coef('Var'  , 1.18025e-09 ), Coef('Var'  , 1.74819e-09 ), ], 
		[Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), ], ])
	
	
	
	etat1.bords   = {Bord('0'): etat2, Bord('1'): etat2, Bord('2'): etat2, Bord('3'): etat2, }
	etat1.permuts = {}
	etat1.interns = {Intern('_'): etat1, }
	etat1.subs    = {Sub('0'): etat1, Sub('G', True): Etat.etatPoint, Sub('1'): etat1, Sub('2'): etat1, Sub('3'): etat1, Sub('4'): etat1, }
	
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
		Figure(1, [Chem([Bord('1'), Bord('0'), ]), Chem([Bord('1'), Intern(''), ]), Chem([Bord('1'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('2'), Bord('0'), ]), Chem([Bord('2'), Intern(''), ]), Chem([Bord('2'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('0'), Bord('0'), ]), Chem([Bord('0'), Intern(''), ]), Chem([Bord('0'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('3'), Bord('0'), ]), Chem([Bord('3'), Intern(''), ]), Chem([Bord('3'), Bord('1'), ]), ]), ]
	
	
	etat1.space = [Chem([Bord('0'), Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('2'), Intern('0'), Intern('0'), ]), Chem([Bord('2'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('3'), Intern('0'), Intern('0'), ]), ]
	
	etat1.initMat[Chem([Sub('0')])] = FMat([
		[Coef('Const', 0.25        ), Coef('Var'  , 0.21875     ), Coef('Var'  , 0.1875      ), Coef('Var'  , 0.21875     ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0937481   ), Coef('Var'  , 0.187497    ), Coef('Var'  , 0.343748    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0625024   ), Coef('Var'  , 0.125004    ), Coef('Var'  , 0.187502    ), Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0312498   ), Coef('Var'  , 0.0624997   ), Coef('Var'  , 0.0312498   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0312496   ), Coef('Var'  , 0.0624994   ), Coef('Var'  , 0.0312496   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0312494   ), Coef('Var'  , 0.062499    ), Coef('Var'  , 0.0312494   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.25        ), Coef('Var'  , 0.187501    ), Coef('Var'  , 0.125001    ), Coef('Var'  , 0.0625008   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.5         ), Coef('Var'  , 0.34375     ), Coef('Var'  , 0.1875      ), Coef('Var'  , 0.09375     ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), ], ])
	etat1.initMat[Chem([Sub('G')])] = FMat([
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], ])
	etat1.initMat[Chem([Sub('1')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0312499   ), Coef('Var'  , 0.0624999   ), Coef('Var'  , 0.0312499   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0312481   ), Coef('Var'  , 0.0624968   ), Coef('Var'  , 0.0312481   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.187502    ), Coef('Var'  , 0.125004    ), Coef('Var'  , 0.0625024   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.34375     ), Coef('Var'  , 0.1875      ), Coef('Var'  , 0.0937498   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.21875     ), Coef('Var'  , 0.187499    ), Coef('Var'  , 0.21875     ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0937494   ), Coef('Var'  , 0.187499    ), Coef('Var'  , 0.343749    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0625008   ), Coef('Var'  , 0.125001    ), Coef('Var'  , 0.187501    ), Coef('Const', 0.25        ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.03125     ), Coef('Var'  , 0.0625      ), Coef('Var'  , 0.03125     ), Coef('Const', 0           ), Coef('Const', 0           ), ], ])
	etat1.initMat[Chem([Sub('2')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0624999   ), Coef('Var'  , 0.125       ), Coef('Var'  , 0.1875      ), Coef('Const', 0.25        ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0312481   ), Coef('Var'  , 0.0624968   ), Coef('Var'  , 0.0312481   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0312524   ), Coef('Var'  , 0.0625039   ), Coef('Var'  , 0.0312524   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0312498   ), Coef('Var'  , 0.0624997   ), Coef('Var'  , 0.0312498   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.1875      ), Coef('Var'  , 0.124999    ), Coef('Var'  , 0.0624996   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.343749    ), Coef('Var'  , 0.187499    ), Coef('Var'  , 0.0937494   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.218751    ), Coef('Var'  , 0.187501    ), Coef('Var'  , 0.218751    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.09375     ), Coef('Var'  , 0.1875      ), Coef('Var'  , 0.34375     ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), ], ])
	etat1.initMat[Chem([Sub('3')])] = FMat([
		[Coef('Var'  , 0.125       ), Coef('Var'  , 0.0624999   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.1875      ), ], 
		[Coef('Var'  , 0.187497    ), Coef('Var'  , 0.0937481   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.343748    ), ], 
		[Coef('Var'  , 0.187504    ), Coef('Var'  , 0.218752    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.218752    ), ], 
		[Coef('Var'  , 0.1875      ), Coef('Var'  , 0.34375     ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0937498   ), ], 
		[Coef('Var'  , 0.124999    ), Coef('Var'  , 0.1875      ), Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0624996   ), ], 
		[Coef('Var'  , 0.062499    ), Coef('Var'  , 0.0312494   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0312494   ), ], 
		[Coef('Var'  , 0.0625013   ), Coef('Var'  , 0.0312508   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0312508   ), ], 
		[Coef('Var'  , 0.0625      ), Coef('Var'  , 0.03125     ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.03125     ), ], ])
	etat1.initMat[Chem([Sub('4')])] = FMat([
		[Coef('Var'  , 0.125       ), Coef('Var'  , 0.0937499   ), Coef('Var'  , 0.0624999   ), Coef('Var'  , 0.0937499   ), Coef('Var'  , 0.125       ), Coef('Var'  , 0.15625     ), Coef('Var'  , 0.1875      ), Coef('Var'  , 0.15625     ), ], 
		[Coef('Var'  , 0.0624968   ), Coef('Var'  , 0.0624962   ), Coef('Var'  , 0.0624968   ), Coef('Var'  , 0.124996    ), Coef('Var'  , 0.187497    ), Coef('Var'  , 0.187496    ), Coef('Var'  , 0.187497    ), Coef('Var'  , 0.124996    ), ], 
		[Coef('Var'  , 0.0625039   ), Coef('Var'  , 0.0937548   ), Coef('Var'  , 0.125004    ), Coef('Var'  , 0.156255    ), Coef('Var'  , 0.187504    ), Coef('Var'  , 0.156255    ), Coef('Var'  , 0.125004    ), Coef('Var'  , 0.0937548   ), ], 
		[Coef('Var'  , 0.0624997   ), Coef('Var'  , 0.125       ), Coef('Var'  , 0.1875      ), Coef('Var'  , 0.1875      ), Coef('Var'  , 0.1875      ), Coef('Var'  , 0.125       ), Coef('Var'  , 0.0624997   ), Coef('Var'  , 0.0624996   ), ], 
		[Coef('Var'  , 0.124999    ), Coef('Var'  , 0.156249    ), Coef('Var'  , 0.187499    ), Coef('Var'  , 0.156249    ), Coef('Var'  , 0.124999    ), Coef('Var'  , 0.0937493   ), Coef('Var'  , 0.0624994   ), Coef('Var'  , 0.0937493   ), ], 
		[Coef('Var'  , 0.187499    ), Coef('Var'  , 0.187499    ), Coef('Var'  , 0.187499    ), Coef('Var'  , 0.124999    ), Coef('Var'  , 0.062499    ), Coef('Var'  , 0.0624987   ), Coef('Var'  , 0.062499    ), Coef('Var'  , 0.124999    ), ], 
		[Coef('Var'  , 0.187501    ), Coef('Var'  , 0.156252    ), Coef('Var'  , 0.125001    ), Coef('Var'  , 0.0937515   ), Coef('Var'  , 0.0625013   ), Coef('Var'  , 0.0937515   ), Coef('Var'  , 0.125001    ), Coef('Var'  , 0.156252    ), ], 
		[Coef('Var'  , 0.1875      ), Coef('Var'  , 0.125       ), Coef('Var'  , 0.0625      ), Coef('Var'  , 0.0625      ), Coef('Var'  , 0.0625      ), Coef('Var'  , 0.125       ), Coef('Var'  , 0.1875      ), Coef('Var'  , 0.1875      ), ], ])
	
	
	
	etat2.bords   = {Bord('0'): etat3, Bord('1'): etat3, }
	etat2.permuts = {Permut('0'): etat2, }
	etat2.interns = {Intern('_'): etat2, }
	etat2.subs    = {Sub('0'): etat2, Sub('G', True): Etat.etatPoint, Sub('1'): etat2, }
	
	etat2.buildIntern()
	etat2.fm_[Permut('0')] = PMat(3, [2, 1, 0, ])
	
	
	etat2.eqs = [
		(Chem([Permut('0'), Bord('0'), ])	,	Chem([Bord('1')])),
		(Chem([Permut('0'), Bord('1'), ])	,	Chem([Bord('0')])),
		(Chem([Permut('0'), Intern(''), ])	,	Chem([Intern('')])),
		(Chem([Permut('0'), Sub('0'), ])	,	Chem([Sub('1'), Permut('0'), ])),
		(Chem([Permut('0'), Sub('1'), ])	,	Chem([Sub('0'), Permut('0'), ])),
		]
	
	
	etat2.prim.elems = [Figure(1, [Chem([Bord('0')]), Chem([Bord('1')]), ])]
	etat2.grid.elems = [Figure(1, [Chem([Bord('0')]), Chem([Intern('')]), Chem([Bord('1')]), ])]
	
	
	etat2.space = [Chem([Bord('0'), Intern('0'), Intern('0'), ]), Chem([Intern('0'), Intern('0'), ]), Chem([Bord('1'), Intern('0'), Intern('0'), ]), ]
	
	etat2.initMat[Chem([Sub('0')])] = FMat([
		[Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), ], ])
	etat2.initMat[Chem([Sub('G')])] = FMat([
		[Coef('Const', 0           )], 
		[Coef('Const', 1           )], 
		[Coef('Const', 0           )], ])
	etat2.initMat[Chem([Sub('1')])] = FMat([
		[Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), ], ])
	
	
	
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
