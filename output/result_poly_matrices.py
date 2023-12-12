# -*- coding: utf-8 -*-

# Automatically generated, from file : result_poly_matrices.py, function : modele()

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
		[Coef('Var'  , 0.67427     ), Coef('Var'  ,-0.524396    ), Coef('Var'  ,-1.19491     ), Coef('Var'  ,-0.667005    ), Coef('Var'  , 0.531684    ), Coef('Var'  , 1.20216     ), ], 
		[Coef('Var'  , 0.987622    ), Coef('Var'  , 1.06992     ), Coef('Var'  , 0.0729474   ), Coef('Var'  ,-1.00628     ), Coef('Var'  ,-1.0886      ), Coef('Var'  ,-0.0916477   ), ], 
		[Coef('Var'  , 8.98083e-10 ), Coef('Var'  , 3.93228e-10 ), Coef('Var'  , 4.73386e-10 ), Coef('Var'  , 5.37239e-10 ), Coef('Var'  , 1.72616e-09 ), Coef('Var'  , 1.1982e-09  ), ], 
		[Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), ], ])
	
	
	
	etat1.bords   = {Bord('0'): etat2, Bord('1'): etat2, Bord('2'): etat2, }
	etat1.permuts = {}
	etat1.interns = {Intern('_'): etat1, }
	etat1.subs    = {Sub('0'): etat1, Sub('1'): etat1, Sub('2'): etat1, Sub('G', True): Etat.etatPoint, }
	
	etat1.buildIntern()
	
	
	etat1.eqs = [
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
	
	
	etat1.prim.elems = [Figure(2, [Chem([Bord('0'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('0'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('0'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('0'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('1'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('1'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('1'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('1'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('2'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('2'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('2'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('2'), Sub('1'), Sub('1'), Bord('0'), ]), ])]
	etat1.grid.elems = [
		Figure(1, [Chem([Bord('1'), Bord('0'), ]), Chem([Bord('1'), Intern(''), ]), Chem([Bord('1'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('2'), Bord('0'), ]), Chem([Bord('2'), Intern(''), ]), Chem([Bord('2'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('0'), Bord('0'), ]), Chem([Bord('0'), Intern(''), ]), Chem([Bord('0'), Bord('1'), ]), ]), ]
	
	
	etat1.space = [Chem([Bord('2'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('2'), Intern('0'), Intern('0'), ]), ]
	
	etat1.initMat[Chem([Sub('0')])] = FMat([
		[Coef('Const', 0.25        ), Coef('Var'  , 0.125       ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.5         ), Coef('Var'  , 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0.25        ), Coef('Var'  , 0.25        ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.25        ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.125       ), Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 9.3957e-19  ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], ])
	etat1.initMat[Chem([Sub('1')])] = FMat([
		[Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.125       ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 1.00613e-17 ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.125       ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.25        ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.25        ), ], 
		[Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.25        ), ], ])
	etat1.initMat[Chem([Sub('2')])] = FMat([
		[Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.25        ), ], 
		[Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.25        ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.125       ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 2.39389e-17 ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.125       ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.25        ), ], ])
	etat1.initMat[Chem([Sub('G')])] = FMat([
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], ])
	
	
	
	etat2.bords   = {Bord('0'): etat3, Bord('1'): etat3, }
	etat2.permuts = {Permut('0'): etat2, }
	etat2.interns = {Intern('_'): etat2, }
	etat2.subs    = {Sub('0'): etat2, Sub('1'): etat2, Sub('G', True): Etat.etatPoint, }
	
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
	etat2.initMat[Chem([Sub('1')])] = FMat([
		[Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), ], ])
	etat2.initMat[Chem([Sub('G')])] = FMat([
		[Coef('Const', 0           )], 
		[Coef('Const', 1           )], 
		[Coef('Const', 0           )], ])
	
	
	
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
