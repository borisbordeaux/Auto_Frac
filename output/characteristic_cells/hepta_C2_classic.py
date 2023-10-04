# -*- coding: utf-8 -*-

# Automatically generated, from file : hepta_C2__C2_C2_C2_classic.py, function : modele()

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
		[Coef('Var'  , 0.201072    ), Coef('Var'  , 1.1958      ), Coef('Var'  , 1.2882      ), Coef('Var'  , 0.408911    ), Coef('Var'  ,-0.780178    ), Coef('Var'  ,-1.38323     ), Coef('Var'  ,-0.946872    ), ], 
		[Coef('Var'  , 1.35957     ), Coef('Var'  , 0.684826    ), Coef('Var'  ,-0.513665    ), Coef('Var'  ,-1.33321     ), Coef('Var'  ,-1.15682     ), Coef('Var'  ,-0.117125    ), Coef('Var'  , 1.00284     ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), ], ])
	
	
	
	etat1.bords   = {Bord('0'): etat2, Bord('1'): etat2, Bord('2'): etat2, Bord('3'): etat2, Bord('4'): etat2, Bord('5'): etat2, Bord('6'): etat2, }
	etat1.permuts = {}
	etat1.interns = {Intern('_'): etat1, }
	etat1.subs    = {Sub('0'): etat1, Sub('G', True): Etat.etatPoint, Sub('1'): etat1, Sub('2'): etat1, Sub('3'): etat1, Sub('4'): etat1, Sub('5'): etat1, Sub('6'): etat1, }
	
	etat1.buildIntern()
	
	
	etat1.eqs = [
		(Chem([Bord('0'), Sub('1'), ])	,	Chem([Sub('0'), Bord('0'), ])),
		(Chem([Bord('1'), Sub('0'), ])	,	Chem([Sub('0'), Bord('1'), ])),
		(Chem([Bord('1'), Sub('1'), ])	,	Chem([Sub('1'), Bord('0'), ])),
		(Chem([Bord('2'), Sub('0'), ])	,	Chem([Sub('1'), Bord('1'), ])),
		(Chem([Bord('2'), Sub('1'), ])	,	Chem([Sub('2'), Bord('0'), ])),
		(Chem([Bord('3'), Sub('0'), ])	,	Chem([Sub('2'), Bord('1'), ])),
		(Chem([Bord('3'), Sub('1'), ])	,	Chem([Sub('3'), Bord('0'), ])),
		(Chem([Bord('4'), Sub('0'), ])	,	Chem([Sub('3'), Bord('1'), ])),
		(Chem([Bord('4'), Sub('1'), ])	,	Chem([Sub('4'), Bord('0'), ])),
		(Chem([Bord('5'), Sub('0'), ])	,	Chem([Sub('4'), Bord('1'), ])),
		(Chem([Bord('5'), Sub('1'), ])	,	Chem([Sub('5'), Bord('0'), ])),
		(Chem([Bord('6'), Sub('0'), ])	,	Chem([Sub('5'), Bord('1'), ])),
		(Chem([Bord('6'), Sub('1'), ])	,	Chem([Sub('6'), Bord('0'), ])),
		(Chem([Bord('0'), Sub('0'), ])	,	Chem([Sub('6'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('3'), Permut('0'), ])	,	Chem([Sub('1'), Bord('5'), ])),
		(Chem([Sub('1'), Bord('3'), Permut('0'), ])	,	Chem([Sub('2'), Bord('5'), ])),
		(Chem([Sub('2'), Bord('3'), Permut('0'), ])	,	Chem([Sub('3'), Bord('5'), ])),
		(Chem([Sub('3'), Bord('3'), Permut('0'), ])	,	Chem([Sub('4'), Bord('5'), ])),
		(Chem([Sub('4'), Bord('3'), Permut('0'), ])	,	Chem([Sub('5'), Bord('5'), ])),
		(Chem([Sub('5'), Bord('3'), Permut('0'), ])	,	Chem([Sub('6'), Bord('5'), ])),
		(Chem([Sub('6'), Bord('3'), Permut('0'), ])	,	Chem([Sub('0'), Bord('5'), ])),
		(Chem([Bord('0'), Bord('1'), ])	,	Chem([Bord('1'), Bord('0'), ])),
		(Chem([Bord('1'), Bord('1'), ])	,	Chem([Bord('2'), Bord('0'), ])),
		(Chem([Bord('2'), Bord('1'), ])	,	Chem([Bord('3'), Bord('0'), ])),
		(Chem([Bord('3'), Bord('1'), ])	,	Chem([Bord('4'), Bord('0'), ])),
		(Chem([Bord('4'), Bord('1'), ])	,	Chem([Bord('5'), Bord('0'), ])),
		(Chem([Bord('5'), Bord('1'), ])	,	Chem([Bord('6'), Bord('0'), ])),
		(Chem([Bord('6'), Bord('1'), ])	,	Chem([Bord('0'), Bord('0'), ])),
		]
	
	
	etat1.prim.elems = [Figure(2, [Chem([Bord('0'), Bord('0'), ]), Chem([Bord('1'), Bord('0'), ]), Chem([Bord('2'), Bord('0'), ]), Chem([Bord('3'), Bord('0'), ]), Chem([Bord('4'), Bord('0'), ]), Chem([Bord('5'), Bord('0'), ]), Chem([Bord('6'), Bord('0'), ]), ])]
	etat1.grid.elems = [
		Figure(1, [Chem([Bord('1'), Bord('0'), ]), Chem([Bord('1'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('2'), Bord('0'), ]), Chem([Bord('2'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('3'), Bord('0'), ]), Chem([Bord('3'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('4'), Bord('0'), ]), Chem([Bord('4'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('5'), Bord('0'), ]), Chem([Bord('5'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('6'), Bord('0'), ]), Chem([Bord('6'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('0'), Bord('0'), ]), Chem([Bord('0'), Bord('1'), ]), ]), ]
	
	
	etat1.space = [Chem([Bord('6'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('2'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('3'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('4'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('5'), Bord('1'), Intern('0'), Intern('0'), ]), ]
	
	etat1.initMat[Chem([Sub('0')])] = FMat([
		[Coef('Const', 0.333333    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0431516   ), Coef('Var'  , 0.129455    ), Coef('Var'  , 0.277673    ), Coef('Var'  , 0.425891    ), ], 
		[Coef('Const', 0.666667    ), Coef('Var'  , 1           ), Coef('Const', 0.666667    ), Coef('Var'  , 0.425892    ), Coef('Var'  , 0.277676    ), Coef('Var'  , 0.277676    ), Coef('Var'  , 0.425892    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.333333    ), Coef('Var'  , 0.425891    ), Coef('Var'  , 0.277672    ), Coef('Var'  , 0.129455    ), Coef('Var'  , 0.0431515   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.043152    ), Coef('Var'  , 0.129456    ), Coef('Var'  , 0.0675424   ), Coef('Var'  , 0.0225141   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0225139   ), Coef('Var'  , 0.0675417   ), Coef('Var'  , 0.0506562   ), Coef('Var'  , 0.0168854   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0168856   ), Coef('Var'  , 0.0506567   ), Coef('Var'  , 0.0675422   ), Coef('Var'  , 0.0225141   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0225141   ), Coef('Var'  , 0.0675423   ), Coef('Var'  , 0.129456    ), Coef('Var'  , 0.043152    ), ], ])
	etat1.initMat[Chem([Sub('G')])] = FMat([
		[Coef('Const', 0.142857    )], 
		[Coef('Const', 0.142857    )], 
		[Coef('Const', 0.142857    )], 
		[Coef('Const', 0.142857    )], 
		[Coef('Const', 0.142857    )], 
		[Coef('Const', 0.142857    )], 
		[Coef('Const', 0.142857    )], ])
	etat1.initMat[Chem([Sub('1')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0225137   ), Coef('Var'  , 0.0675414   ), Coef('Var'  , 0.129455    ), Coef('Var'  , 0.0431516   ), ], 
		[Coef('Const', 0.333333    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0431529   ), Coef('Var'  , 0.129458    ), Coef('Var'  , 0.277676    ), Coef('Var'  , 0.425892    ), ], 
		[Coef('Const', 0.666667    ), Coef('Var'  , 1           ), Coef('Const', 0.666667    ), Coef('Var'  , 0.425891    ), Coef('Var'  , 0.277672    ), Coef('Var'  , 0.277672    ), Coef('Var'  , 0.425891    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.333333    ), Coef('Var'  , 0.425891    ), Coef('Var'  , 0.277674    ), Coef('Var'  , 0.129456    ), Coef('Var'  , 0.043152    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0431518   ), Coef('Var'  , 0.129455    ), Coef('Var'  , 0.0675417   ), Coef('Var'  , 0.0225139   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0225141   ), Coef('Var'  , 0.0675422   ), Coef('Var'  , 0.0506567   ), Coef('Var'  , 0.0168856   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0168856   ), Coef('Var'  , 0.0506568   ), Coef('Var'  , 0.0675423   ), Coef('Var'  , 0.0225141   ), ], ])
	etat1.initMat[Chem([Sub('2')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0168852   ), Coef('Var'  , 0.0506558   ), Coef('Var'  , 0.0675414   ), Coef('Var'  , 0.0225137   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.022515    ), Coef('Var'  , 0.0675444   ), Coef('Var'  , 0.129458    ), Coef('Var'  , 0.0431529   ), ], 
		[Coef('Const', 0.333333    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0431515   ), Coef('Var'  , 0.129455    ), Coef('Var'  , 0.277672    ), Coef('Var'  , 0.425891    ), ], 
		[Coef('Const', 0.666667    ), Coef('Var'  , 1           ), Coef('Const', 0.666667    ), Coef('Var'  , 0.425891    ), Coef('Var'  , 0.277674    ), Coef('Var'  , 0.277674    ), Coef('Var'  , 0.425891    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.333333    ), Coef('Var'  , 0.425891    ), Coef('Var'  , 0.277673    ), Coef('Var'  , 0.129455    ), Coef('Var'  , 0.0431518   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.043152    ), Coef('Var'  , 0.129456    ), Coef('Var'  , 0.0675422   ), Coef('Var'  , 0.0225141   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0225141   ), Coef('Var'  , 0.0675423   ), Coef('Var'  , 0.0506568   ), Coef('Var'  , 0.0168856   ), ], ])
	etat1.initMat[Chem([Sub('3')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0225137   ), Coef('Var'  , 0.0675414   ), Coef('Var'  , 0.0506558   ), Coef('Var'  , 0.0168852   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0168865   ), Coef('Var'  , 0.0506589   ), Coef('Var'  , 0.0675444   ), Coef('Var'  , 0.022515    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0225136   ), Coef('Var'  , 0.0675411   ), Coef('Var'  , 0.129455    ), Coef('Var'  , 0.0431515   ), ], 
		[Coef('Const', 0.333333    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.043152    ), Coef('Var'  , 0.129456    ), Coef('Var'  , 0.277674    ), Coef('Var'  , 0.425891    ), ], 
		[Coef('Const', 0.666667    ), Coef('Var'  , 1           ), Coef('Const', 0.666667    ), Coef('Var'  , 0.425891    ), Coef('Var'  , 0.277673    ), Coef('Var'  , 0.277673    ), Coef('Var'  , 0.425891    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.333333    ), Coef('Var'  , 0.425891    ), Coef('Var'  , 0.277674    ), Coef('Var'  , 0.129456    ), Coef('Var'  , 0.043152    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.043152    ), Coef('Var'  , 0.129456    ), Coef('Var'  , 0.0675423   ), Coef('Var'  , 0.0225141   ), ], ])
	etat1.initMat[Chem([Sub('4')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0431516   ), Coef('Var'  , 0.129455    ), Coef('Var'  , 0.0675414   ), Coef('Var'  , 0.0225137   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.022515    ), Coef('Var'  , 0.0675444   ), Coef('Var'  , 0.0506589   ), Coef('Var'  , 0.0168865   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0168851   ), Coef('Var'  , 0.0506555   ), Coef('Var'  , 0.0675411   ), Coef('Var'  , 0.0225136   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0225141   ), Coef('Var'  , 0.0675424   ), Coef('Var'  , 0.129456    ), Coef('Var'  , 0.043152    ), ], 
		[Coef('Const', 0.333333    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0431518   ), Coef('Var'  , 0.129455    ), Coef('Var'  , 0.277673    ), Coef('Var'  , 0.425891    ), ], 
		[Coef('Const', 0.666667    ), Coef('Var'  , 1           ), Coef('Const', 0.666667    ), Coef('Var'  , 0.425891    ), Coef('Var'  , 0.277674    ), Coef('Var'  , 0.277674    ), Coef('Var'  , 0.425891    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.333333    ), Coef('Var'  , 0.425891    ), Coef('Var'  , 0.277674    ), Coef('Var'  , 0.129456    ), Coef('Var'  , 0.043152    ), ], ])
	etat1.initMat[Chem([Sub('5')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.333333    ), Coef('Var'  , 0.425891    ), Coef('Var'  , 0.277673    ), Coef('Var'  , 0.129455    ), Coef('Var'  , 0.0431516   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0431529   ), Coef('Var'  , 0.129458    ), Coef('Var'  , 0.0675444   ), Coef('Var'  , 0.022515    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0225136   ), Coef('Var'  , 0.0675411   ), Coef('Var'  , 0.0506555   ), Coef('Var'  , 0.0168851   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0168856   ), Coef('Var'  , 0.0506568   ), Coef('Var'  , 0.0675424   ), Coef('Var'  , 0.0225141   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0225139   ), Coef('Var'  , 0.0675417   ), Coef('Var'  , 0.129455    ), Coef('Var'  , 0.0431518   ), ], 
		[Coef('Const', 0.333333    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.043152    ), Coef('Var'  , 0.129456    ), Coef('Var'  , 0.277674    ), Coef('Var'  , 0.425891    ), ], 
		[Coef('Const', 0.666667    ), Coef('Var'  , 1           ), Coef('Const', 0.666667    ), Coef('Var'  , 0.425891    ), Coef('Var'  , 0.277674    ), Coef('Var'  , 0.277674    ), Coef('Var'  , 0.425891    ), ], ])
	etat1.initMat[Chem([Sub('6')])] = FMat([
		[Coef('Const', 0.666667    ), Coef('Var'  , 1           ), Coef('Const', 0.666667    ), Coef('Var'  , 0.425891    ), Coef('Var'  , 0.277673    ), Coef('Var'  , 0.277673    ), Coef('Var'  , 0.425891    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.333333    ), Coef('Var'  , 0.425892    ), Coef('Var'  , 0.277676    ), Coef('Var'  , 0.129458    ), Coef('Var'  , 0.0431529   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0431515   ), Coef('Var'  , 0.129455    ), Coef('Var'  , 0.0675411   ), Coef('Var'  , 0.0225136   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0225141   ), Coef('Var'  , 0.0675424   ), Coef('Var'  , 0.0506568   ), Coef('Var'  , 0.0168856   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0168854   ), Coef('Var'  , 0.0506562   ), Coef('Var'  , 0.0675417   ), Coef('Var'  , 0.0225139   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0225141   ), Coef('Var'  , 0.0675422   ), Coef('Var'  , 0.129456    ), Coef('Var'  , 0.043152    ), ], 
		[Coef('Const', 0.333333    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.043152    ), Coef('Var'  , 0.129456    ), Coef('Var'  , 0.277674    ), Coef('Var'  , 0.425891    ), ], ])
	
	
	
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
