# -*- coding: utf-8 -*-

# Automatically generated, from file : result_struct_delay.py, function : modele()

from __future__ import division
import sys
if './../../../../../../python' not in sys.path:
	sys.path.append('./../../../../../../python')
from etat import *

def modele():
	
	etat0 = EtatInit()
	etat1 = Etat('Cell_0',0)
	etat2 = Etat('Cell_1',0)
	etat3 = Etat('Cell_2_1',0)
	etat4 = Etat('Cell_3',0)
	etat5 = Etat('Cell_4',0)
	etat6 = Etat('B2',1)
	etat7 = Etat('C2',0)
	etat8 = Etat('C2_1',0)
	etat9 = Etat('Cell_5',0)
	etat10 = Etat('B2_1',1)
	etat11 = Etat('s',1)
	
	
	etat0.subs   = {Sub('0'): etat1, Sub('1'): etat2, Sub('2'): etat3, Sub('3'): etat2, Sub('4'): etat1, }
	
	etat0.eqs = [
		(Chem([Sub('0'), Bord('2'), Permut('0'), ])	,	Chem([Sub('1'), Bord('0'), ])),
		(Chem([Sub('1'), Bord('2'), Permut('0'), ])	,	Chem([Sub('2'), Bord('0'), ])),
		(Chem([Sub('2'), Bord('2'), Permut('0'), ])	,	Chem([Sub('3'), Bord('2'), ])),
		(Chem([Sub('3'), Bord('0'), Permut('0'), ])	,	Chem([Sub('4'), Bord('2'), ])),
		]
	
	
	etat0.space = []
	
	etat0.initMat[Chem([Sub('0')])] = FMat([
		[Coef('Var'  ,-7.5         ), Coef('Var'  ,-7.5         ), Coef('Var'  ,-7.5         ), Coef('Var'  ,-5.5         ), Coef('Var'  ,-3.5         ), Coef('Var'  ,-3.5         ), Coef('Var'  ,-5.5         ), ], 
		[Coef('Var'  , 2           ), Coef('Var'  , 0           ), Coef('Var'  ,-2           ), Coef('Var'  ,-2           ), Coef('Var'  ,-2           ), Coef('Var'  , 2           ), Coef('Var'  , 2           ), ], 
		[Coef('Var'  , 0           ), Coef('Var'  , 0           ), Coef('Var'  , 0           ), Coef('Var'  , 0           ), Coef('Var'  , 0           ), Coef('Var'  , 0           ), Coef('Var'  , 0           ), ], 
		[Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), ], ])
	etat0.initMat[Chem([Sub('1')])] = FMat([
		[Coef('Var'  ,-3.5         ), Coef('Var'  ,-3.5         ), Coef('Var'  ,-2           ), Coef('Var'  ,-0.5         ), Coef('Var'  ,-0.5         ), Coef('Var'  ,-2           ), ], 
		[Coef('Var'  , 2           ), Coef('Var'  ,-2           ), Coef('Var'  ,-0.5         ), Coef('Var'  ,-0.5         ), Coef('Var'  , 0.5         ), Coef('Var'  , 0.5         ), ], 
		[Coef('Var'  , 0           ), Coef('Var'  , 0           ), Coef('Var'  , 0           ), Coef('Var'  , 0           ), Coef('Var'  , 0           ), Coef('Var'  , 0           ), ], 
		[Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), ], ])
	etat0.initMat[Chem([Sub('2')])] = FMat([
		[Coef('Var'  ,-0.5         ), Coef('Var'  ,-0.5         ), Coef('Var'  , 0           ), Coef('Var'  , 0.5         ), Coef('Var'  , 0.5         ), Coef('Var'  , 0           ), ], 
		[Coef('Var'  , 0.5         ), Coef('Var'  ,-0.5         ), Coef('Var'  ,-0.5         ), Coef('Var'  ,-0.5         ), Coef('Var'  , 0.5         ), Coef('Var'  , 0.5         ), ], 
		[Coef('Var'  , 0           ), Coef('Var'  , 0           ), Coef('Var'  , 0           ), Coef('Var'  , 0           ), Coef('Var'  , 0           ), Coef('Var'  , 0           ), ], 
		[Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), ], ])
	etat0.initMat[Chem([Sub('3')])] = FMat([
		[Coef('Var'  , 3.5         ), Coef('Var'  , 3.5         ), Coef('Var'  , 2           ), Coef('Var'  , 0.5         ), Coef('Var'  , 0.5         ), Coef('Var'  , 2           ), ], 
		[Coef('Var'  ,-2           ), Coef('Var'  , 2           ), Coef('Var'  , 0.5         ), Coef('Var'  , 0.5         ), Coef('Var'  ,-0.5         ), Coef('Var'  ,-0.5         ), ], 
		[Coef('Var'  , 0           ), Coef('Var'  , 0           ), Coef('Var'  , 0           ), Coef('Var'  , 0           ), Coef('Var'  , 0           ), Coef('Var'  , 0           ), ], 
		[Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), ], ])
	etat0.initMat[Chem([Sub('4')])] = FMat([
		[Coef('Var'  , 7.5         ), Coef('Var'  , 7.5         ), Coef('Var'  , 7.5         ), Coef('Var'  , 5.5         ), Coef('Var'  , 3.5         ), Coef('Var'  , 3.5         ), Coef('Var'  , 5.5         ), ], 
		[Coef('Var'  ,-2           ), Coef('Var'  , 0           ), Coef('Var'  , 2           ), Coef('Var'  , 2           ), Coef('Var'  , 2           ), Coef('Var'  ,-2           ), Coef('Var'  ,-2           ), ], 
		[Coef('Var'  , 0           ), Coef('Var'  , 0           ), Coef('Var'  , 0           ), Coef('Var'  , 0           ), Coef('Var'  , 0           ), Coef('Var'  , 0           ), Coef('Var'  , 0           ), ], 
		[Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), ], ])
	
	
	
	etat1.bords   = {Bord('0'): etat6, Bord('1'): etat6, Bord('2'): etat7, Bord('3'): etat6, }
	etat1.permuts = {}
	etat1.interns = {Intern('_'): etat1, }
	etat1.subs    = {Sub('0'): etat4, Sub('1'): etat5, Sub('2'): etat5, Sub('3'): etat4, Sub('G', True): Etat.etatPoint, }
	
	etat1.buildIntern()
	
	
	etat1.eqs = [
		(Chem([Bord('0'), Sub('1'), ])	,	Chem([Sub('0'), Bord('0'), ])),
		(Chem([Bord('1'), Sub('0'), ])	,	Chem([Sub('0'), Bord('1'), ])),
		(Chem([Bord('1'), Sub('1'), ])	,	Chem([Sub('1'), Bord('0'), ])),
		(Chem([Bord('2'), Sub('0'), ])	,	Chem([Sub('1'), Bord('1'), ])),
		(Chem([Bord('2'), Sub('1'), ])	,	Chem([Sub('2'), Bord('5'), ])),
		(Chem([Bord('3'), Sub('0'), ])	,	Chem([Sub('2'), Bord('0'), ])),
		(Chem([Bord('3'), Sub('1'), ])	,	Chem([Sub('3'), Bord('0'), ])),
		(Chem([Bord('0'), Sub('0'), ])	,	Chem([Sub('3'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('2'), Permut('0'), ])	,	Chem([Sub('1'), Bord('5'), ])),
		(Chem([Sub('1'), Bord('3'), Permut('0'), ])	,	Chem([Sub('2'), Bord('3'), ])),
		(Chem([Sub('2'), Bord('1'), Permut('0'), ])	,	Chem([Sub('3'), Bord('4'), ])),
		(Chem([Sub('3'), Bord('2'), Permut('0'), ])	,	Chem([Sub('0'), Bord('4'), ])),
		(Chem([Bord('0'), Bord('1'), ])	,	Chem([Bord('1'), Bord('0'), ])),
		(Chem([Bord('1'), Bord('1'), ])	,	Chem([Bord('2'), Bord('0'), ])),
		(Chem([Bord('2'), Bord('1'), ])	,	Chem([Bord('3'), Bord('0'), ])),
		(Chem([Bord('3'), Bord('1'), ])	,	Chem([Bord('0'), Bord('0'), ])),
		]
	
	
	etat1.prim.elems = [Figure(2, [Chem([Bord('0'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('0'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('0'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('0'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('1'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('1'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('1'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('1'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('2'), Bord('0'), ]), Chem([Bord('3'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('3'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('3'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('3'), Sub('1'), Sub('1'), Bord('0'), ]), ])]
	etat1.grid.elems = [
		Figure(1, [Chem([Bord('1'), Bord('0'), ]), Chem([Bord('1'), Intern(''), ]), Chem([Bord('1'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('2'), Bord('0'), ]), Chem([Bord('2'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('0'), Bord('0'), ]), Chem([Bord('0'), Intern(''), ]), Chem([Bord('0'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('3'), Bord('0'), ]), Chem([Bord('3'), Intern(''), ]), Chem([Bord('3'), Bord('1'), ]), ]), ]
	
	
	etat1.space = [Chem([Bord('0'), Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('2'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('3'), Intern('0'), Intern('0'), ]), ]
	
	etat1.initMat[Chem([Sub('0')])] = FMat([
		[Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0702086   ), Coef('Var'  , 0.130905    ), Coef('Var'  , 0.19147     ), ], 
		[Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0887528   ), Coef('Var'  , 0.191747    ), Coef('Var'  , 0.294547    ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.195592    ), Coef('Var'  , 0.193829    ), Coef('Var'  , 0.191789    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.301281    ), Coef('Var'  , 0.194643    ), Coef('Var'  , 0.088077    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.208428    ), Coef('Var'  , 0.140299    ), Coef('Var'  , 0.0725939   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0838942   ), Coef('Var'  , 0.0783135   ), Coef('Var'  , 0.0729804   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0518437   ), Coef('Var'  , 0.0702631   ), Coef('Var'  , 0.0885435   ), ], ])
	etat1.initMat[Chem([Sub('1')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0222953   ), Coef('Var'  , 0.0445088   ), Coef('Var'  , 0.0888007   ), Coef('Var'  , 0.0795997   ), Coef('Var'  , 0.0702086   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0150462   ), Coef('Var'  , 0.0299757   ), Coef('Var'  , 0.0596418   ), Coef('Var'  , 0.0743349   ), Coef('Var'  , 0.0887528   ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0225455   ), Coef('Var'  , 0.044924    ), Coef('Var'  , 0.0894048   ), Coef('Var'  , 0.142695    ), Coef('Var'  , 0.195592    ), ], 
		[Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0292887   ), Coef('Var'  , 0.058619    ), Coef('Var'  , 0.117349    ), Coef('Var'  , 0.209265    ), Coef('Var'  , 0.301281    ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.666667    ), Coef('Var'  , 0.523763    ), Coef('Var'  , 0.381116    ), Coef('Var'  , 0.262914    ), Coef('Var'  , 0.235369    ), Coef('Var'  , 0.208428    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.333333    ), Coef('Var'  , 0.357402    ), Coef('Var'  , 0.381624    ), Coef('Var'  , 0.263651    ), Coef('Var'  , 0.173595    ), Coef('Var'  , 0.0838942   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0296589   ), Coef('Var'  , 0.0592325   ), Coef('Var'  , 0.118239    ), Coef('Var'  , 0.0851409   ), Coef('Var'  , 0.0518437   ), ], ])
	etat1.initMat[Chem([Sub('2')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.195209    ), Coef('Var'  , 0.1421      ), Coef('Var'  , 0.0888007   ), Coef('Var'  , 0.0445088   ), Coef('Var'  , 0.0222953   ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0887528   ), Coef('Var'  , 0.0743349   ), Coef('Var'  , 0.0596418   ), Coef('Var'  , 0.0299757   ), Coef('Var'  , 0.0150462   ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0705921   ), Coef('Var'  , 0.0801951   ), Coef('Var'  , 0.0894048   ), Coef('Var'  , 0.044924    ), Coef('Var'  , 0.0225455   ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0512809   ), Coef('Var'  , 0.0842648   ), Coef('Var'  , 0.117349    ), Coef('Var'  , 0.058619    ), Coef('Var'  , 0.0292887   ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0834279   ), Coef('Var'  , 0.172869    ), Coef('Var'  , 0.262914    ), Coef('Var'  , 0.381116    ), Coef('Var'  , 0.357096    ), Coef('Const', 0.333333    ), ], 
		[Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.208894    ), Coef('Var'  , 0.236095    ), Coef('Var'  , 0.263651    ), Coef('Var'  , 0.381624    ), Coef('Var'  , 0.524069    ), Coef('Const', 0.666667    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.301844    ), Coef('Var'  , 0.210141    ), Coef('Var'  , 0.118239    ), Coef('Var'  , 0.0592325   ), Coef('Var'  , 0.0296589   ), Coef('Const', 0           ), ], ])
	etat1.initMat[Chem([Sub('3')])] = FMat([
		[Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.19147     ), Coef('Var'  , 0.193405    ), Coef('Var'  , 0.195209    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.294547    ), Coef('Var'  , 0.191747    ), Coef('Var'  , 0.0887528   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.191789    ), Coef('Var'  , 0.131329    ), Coef('Var'  , 0.0705921   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.088077    ), Coef('Var'  , 0.0696428   ), Coef('Var'  , 0.0512809   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0725939   ), Coef('Var'  , 0.0777995   ), Coef('Var'  , 0.0834279   ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0729804   ), Coef('Var'  , 0.140813    ), Coef('Var'  , 0.208894    ), ], 
		[Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0885435   ), Coef('Var'  , 0.195263    ), Coef('Var'  , 0.301844    ), ], ])
	etat1.initMat[Chem([Sub('G')])] = FMat([
		[Coef('Const', 0.142857    )], 
		[Coef('Const', 0.142857    )], 
		[Coef('Const', 0.142857    )], 
		[Coef('Const', 0.142857    )], 
		[Coef('Const', 0.142857    )], 
		[Coef('Const', 0.142857    )], 
		[Coef('Const', 0.142857    )], ])
	
	
	
	etat2.bords   = {Bord('0'): etat7, Bord('1'): etat6, Bord('2'): etat8, Bord('3'): etat6, }
	etat2.permuts = {}
	etat2.interns = {Intern('_'): etat2, }
	etat2.subs    = {Sub('0'): etat5, Sub('1'): etat5, Sub('2'): etat5, Sub('G', True): Etat.etatPoint, }
	
	etat2.buildIntern()
	
	
	etat2.eqs = [
		(Chem([Bord('0'), Sub('1'), ])	,	Chem([Sub('0'), Bord('5'), ])),
		(Chem([Bord('1'), Sub('0'), ])	,	Chem([Sub('0'), Bord('0'), ])),
		(Chem([Bord('1'), Sub('1'), ])	,	Chem([Sub('1'), Bord('0'), ])),
		(Chem([Bord('2'), Sub('0'), ])	,	Chem([Sub('1'), Bord('1'), ])),
		(Chem([Bord('3'), Sub('0'), ])	,	Chem([Sub('1'), Bord('2'), ])),
		(Chem([Bord('3'), Sub('1'), ])	,	Chem([Sub('2'), Bord('0'), ])),
		(Chem([Bord('0'), Sub('0'), ])	,	Chem([Sub('2'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('1'), Permut('0'), ])	,	Chem([Sub('1'), Bord('5'), ])),
		(Chem([Sub('1'), Bord('3'), Permut('0'), ])	,	Chem([Sub('2'), Bord('5'), ])),
		(Chem([Sub('2'), Bord('3'), Permut('0'), ])	,	Chem([Sub('0'), Bord('3'), ])),
		(Chem([Bord('0'), Bord('1'), ])	,	Chem([Bord('1'), Bord('0'), ])),
		(Chem([Bord('1'), Bord('1'), ])	,	Chem([Bord('2'), Bord('0'), ])),
		(Chem([Bord('2'), Bord('1'), ])	,	Chem([Bord('3'), Bord('0'), ])),
		(Chem([Bord('3'), Bord('1'), ])	,	Chem([Bord('0'), Bord('0'), ])),
		]
	
	
	etat2.prim.elems = [Figure(2, [Chem([Bord('0'), Bord('0'), ]), Chem([Bord('1'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('1'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('1'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('1'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('2'), Bord('0'), ]), Chem([Bord('3'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('3'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('3'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('3'), Sub('1'), Sub('1'), Bord('0'), ]), ])]
	etat2.grid.elems = [
		Figure(1, [Chem([Bord('1'), Bord('0'), ]), Chem([Bord('1'), Intern(''), ]), Chem([Bord('1'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('2'), Bord('0'), ]), Chem([Bord('2'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('0'), Bord('0'), ]), Chem([Bord('0'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('3'), Bord('0'), ]), Chem([Bord('3'), Intern(''), ]), Chem([Bord('3'), Bord('1'), ]), ]), ]
	
	
	etat2.space = [Chem([Bord('0'), Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('2'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('3'), Intern('0'), Intern('0'), ]), ]
	
	etat2.initMat[Chem([Sub('0')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.12735     ), Coef('Var'  , 0.205333    ), Coef('Var'  , 0.283904    ), Coef('Var'  , 0.391635    ), Coef('Var'  , 0.362365    ), Coef('Const', 0.333333    ), ], 
		[Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.226926    ), Coef('Var'  , 0.254706    ), Coef('Var'  , 0.283277    ), Coef('Var'  , 0.391211    ), Coef('Var'  , 0.528779    ), Coef('Const', 0.666667    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.313472    ), Coef('Var'  , 0.227366    ), Coef('Var'  , 0.141652    ), Coef('Var'  , 0.070615    ), Coef('Var'  , 0.0352287   ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.158682    ), Coef('Var'  , 0.116565    ), Coef('Var'  , 0.0737084   ), Coef('Var'  , 0.0372541   ), Coef('Var'  , 0.0187766   ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0586698   ), Coef('Var'  , 0.0665476   ), Coef('Var'  , 0.0736907   ), Coef('Var'  , 0.0372419   ), Coef('Var'  , 0.0187692   ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.114901    ), Coef('Var'  , 0.129483    ), Coef('Var'  , 0.143768    ), Coef('Var'  , 0.0720439   ), Coef('Var'  , 0.0360817   ), Coef('Const', 0           ), ], ])
	etat2.initMat[Chem([Sub('1')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.22735     ), Coef('Var'  , 0.177113    ), Coef('Var'  , 0.12735     ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.126926    ), Coef('Var'  , 0.176608    ), Coef('Var'  , 0.226926    ), ], 
		[Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.113472    ), Coef('Var'  , 0.213314    ), Coef('Var'  , 0.313472    ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0586815   ), Coef('Var'  , 0.10898     ), Coef('Var'  , 0.158682    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.15867     ), Coef('Var'  , 0.108966    ), Coef('Var'  , 0.0586698   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.314901    ), Coef('Var'  , 0.21502     ), Coef('Var'  , 0.114901    ), ], ])
	etat2.initMat[Chem([Sub('2')])] = FMat([
		[Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.666667    ), Coef('Var'  , 0.529032    ), Coef('Var'  , 0.391635    ), Coef('Var'  , 0.283904    ), Coef('Var'  , 0.255333    ), Coef('Var'  , 0.22735     ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.333333    ), Coef('Var'  , 0.362112    ), Coef('Var'  , 0.391211    ), Coef('Var'  , 0.283277    ), Coef('Var'  , 0.204706    ), Coef('Var'  , 0.126926    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0352287   ), Coef('Var'  , 0.070615    ), Coef('Var'  , 0.141652    ), Coef('Var'  , 0.127366    ), Coef('Var'  , 0.113472    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0187766   ), Coef('Var'  , 0.0372541   ), Coef('Var'  , 0.0737084   ), Coef('Var'  , 0.0665652   ), Coef('Var'  , 0.0586815   ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0187692   ), Coef('Var'  , 0.0372419   ), Coef('Var'  , 0.0736907   ), Coef('Var'  , 0.116548    ), Coef('Var'  , 0.15867     ), ], 
		[Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0360817   ), Coef('Var'  , 0.0720439   ), Coef('Var'  , 0.143768    ), Coef('Var'  , 0.229483    ), Coef('Var'  , 0.314901    ), ], ])
	etat2.initMat[Chem([Sub('G')])] = FMat([
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], ])
	
	
	
	etat3.bords   = {Bord('0'): etat8, Bord('1'): etat10, Bord('2'): etat8, Bord('3'): etat10, }
	etat3.permuts = {}
	etat3.interns = {Intern('_'): etat3, }
	etat3.subs    = {Sub('0'): etat9, Sub('G', True): Etat.etatPoint, }
	
	etat3.buildIntern()
	
	
	etat3.eqs = [
		(Chem([Bord('0'), Sub('0'), ])	,	Chem([Sub('0'), Bord('0'), ])),
		(Chem([Bord('1'), Sub('0'), ])	,	Chem([Sub('0'), Bord('1'), ])),
		(Chem([Bord('2'), Sub('0'), ])	,	Chem([Sub('0'), Bord('2'), ])),
		(Chem([Bord('3'), Sub('0'), ])	,	Chem([Sub('0'), Bord('3'), ])),
		(Chem([Bord('0'), Bord('1'), ])	,	Chem([Bord('1'), Bord('0'), ])),
		(Chem([Bord('1'), Bord('1'), ])	,	Chem([Bord('2'), Bord('0'), ])),
		(Chem([Bord('2'), Bord('1'), ])	,	Chem([Bord('3'), Bord('0'), ])),
		(Chem([Bord('3'), Bord('1'), ])	,	Chem([Bord('0'), Bord('0'), ])),
		]
	
	
	etat3.prim.elems = [Figure(2, [Chem([Bord('0'), Bord('0'), ]), Chem([Bord('1'), Bord('0'), ]), Chem([Bord('2'), Bord('0'), ]), Chem([Bord('3'), Bord('0'), ]), ])]
	etat3.grid.elems = [
		Figure(1, [Chem([Bord('1'), Bord('0'), ]), Chem([Bord('1'), Intern(''), ]), Chem([Bord('1'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('2'), Bord('0'), ]), Chem([Bord('2'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('0'), Bord('0'), ]), Chem([Bord('0'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('3'), Bord('0'), ]), Chem([Bord('3'), Intern(''), ]), Chem([Bord('3'), Bord('1'), ]), ]), ]
	
	
	etat3.space = [Chem([Bord('0'), Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('2'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('3'), Intern('0'), Intern('0'), ]), ]
	
	etat3.initMat[Chem([Sub('0')])] = FMat([
		[Coef('Const', 1           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 1           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 1           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 1           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 1           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 1           ), ], ])
	etat3.initMat[Chem([Sub('G')])] = FMat([
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], ])
	
	
	
	etat4.bords   = {Bord('0'): etat6, Bord('1'): etat6, Bord('2'): etat7, Bord('3'): etat6, Bord('4'): etat7, }
	etat4.permuts = {}
	etat4.interns = {Intern('_'): etat4, }
	etat4.subs    = {Sub('0'): etat4, Sub('1'): etat5, Sub('2'): etat5, Sub('3'): etat5, Sub('4'): etat5, Sub('G', True): Etat.etatPoint, }
	
	etat4.buildIntern()
	
	
	etat4.eqs = [
		(Chem([Bord('0'), Sub('1'), ])	,	Chem([Sub('0'), Bord('0'), ])),
		(Chem([Bord('1'), Sub('0'), ])	,	Chem([Sub('0'), Bord('1'), ])),
		(Chem([Bord('1'), Sub('1'), ])	,	Chem([Sub('1'), Bord('0'), ])),
		(Chem([Bord('2'), Sub('0'), ])	,	Chem([Sub('1'), Bord('1'), ])),
		(Chem([Bord('2'), Sub('1'), ])	,	Chem([Sub('2'), Bord('5'), ])),
		(Chem([Bord('3'), Sub('0'), ])	,	Chem([Sub('2'), Bord('0'), ])),
		(Chem([Bord('3'), Sub('1'), ])	,	Chem([Sub('3'), Bord('0'), ])),
		(Chem([Bord('4'), Sub('0'), ])	,	Chem([Sub('3'), Bord('1'), ])),
		(Chem([Bord('4'), Sub('1'), ])	,	Chem([Sub('4'), Bord('5'), ])),
		(Chem([Bord('0'), Sub('0'), ])	,	Chem([Sub('4'), Bord('0'), ])),
		(Chem([Sub('0'), Bord('2'), Permut('0'), ])	,	Chem([Sub('1'), Bord('5'), ])),
		(Chem([Sub('1'), Bord('3'), Permut('0'), ])	,	Chem([Sub('2'), Bord('3'), ])),
		(Chem([Sub('2'), Bord('1'), Permut('0'), ])	,	Chem([Sub('3'), Bord('5'), ])),
		(Chem([Sub('3'), Bord('3'), Permut('0'), ])	,	Chem([Sub('4'), Bord('3'), ])),
		(Chem([Sub('4'), Bord('1'), Permut('0'), ])	,	Chem([Sub('0'), Bord('4'), ])),
		(Chem([Bord('0'), Bord('1'), ])	,	Chem([Bord('1'), Bord('0'), ])),
		(Chem([Bord('1'), Bord('1'), ])	,	Chem([Bord('2'), Bord('0'), ])),
		(Chem([Bord('2'), Bord('1'), ])	,	Chem([Bord('3'), Bord('0'), ])),
		(Chem([Bord('3'), Bord('1'), ])	,	Chem([Bord('4'), Bord('0'), ])),
		(Chem([Bord('4'), Bord('1'), ])	,	Chem([Bord('0'), Bord('0'), ])),
		]
	
	
	etat4.prim.elems = [Figure(2, [Chem([Bord('0'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('0'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('0'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('0'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('1'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('1'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('1'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('1'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('2'), Bord('0'), ]), Chem([Bord('3'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('3'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('3'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('3'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('4'), Bord('0'), ]), ])]
	etat4.grid.elems = [
		Figure(1, [Chem([Bord('1'), Bord('0'), ]), Chem([Bord('1'), Intern(''), ]), Chem([Bord('1'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('4'), Bord('0'), ]), Chem([Bord('4'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('2'), Bord('0'), ]), Chem([Bord('2'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('0'), Bord('0'), ]), Chem([Bord('0'), Intern(''), ]), Chem([Bord('0'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('3'), Bord('0'), ]), Chem([Bord('3'), Intern(''), ]), Chem([Bord('3'), Bord('1'), ]), ]), ]
	
	
	etat4.space = [Chem([Bord('4'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('2'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('3'), Intern('0'), Intern('0'), ]), Chem([Bord('4'), Bord('0'), Intern('0'), Intern('0'), ]), ]
	
	etat4.initMat[Chem([Sub('0')])] = FMat([
		[Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0630003   ), Coef('Var'  , 0.134283    ), Coef('Var'  , 0.205667    ), ], 
		[Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0854234   ), Coef('Var'  , 0.192603    ), Coef('Var'  , 0.299692    ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.193103    ), Coef('Var'  , 0.193236    ), Coef('Var'  , 0.193084    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.30052     ), Coef('Var'  , 0.193605    ), Coef('Var'  , 0.0862899   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.205656    ), Coef('Var'  , 0.134247    ), Coef('Var'  , 0.0629516   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0745329   ), Coef('Var'  , 0.0565596   ), Coef('Var'  , 0.0389351   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0385688   ), Coef('Var'  , 0.0386041   ), Coef('Var'  , 0.0385943   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0391954   ), Coef('Var'  , 0.0568631   ), Coef('Var'  , 0.0747857   ), ], ])
	etat4.initMat[Chem([Sub('1')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0116558   ), Coef('Var'  , 0.0232863   ), Coef('Var'  , 0.0465208   ), Coef('Var'  , 0.0547559   ), Coef('Var'  , 0.0630003   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0104695   ), Coef('Var'  , 0.0208841   ), Coef('Var'  , 0.0416225   ), Coef('Var'  , 0.0635867   ), Coef('Var'  , 0.0854234   ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.019726    ), Coef('Var'  , 0.0392954   ), Coef('Var'  , 0.0781713   ), Coef('Var'  , 0.135827    ), Coef('Var'  , 0.193103    ), ], 
		[Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0287849   ), Coef('Var'  , 0.0573852   ), Coef('Var'  , 0.114269    ), Coef('Var'  , 0.207633    ), Coef('Var'  , 0.30052     ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.666667    ), Coef('Var'  , 0.523268    ), Coef('Var'  , 0.379991    ), Coef('Var'  , 0.260298    ), Coef('Var'  , 0.232855    ), Coef('Var'  , 0.205656    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.333333    ), Coef('Var'  , 0.35658     ), Coef('Var'  , 0.380056    ), Coef('Var'  , 0.260718    ), Coef('Var'  , 0.167365    ), Coef('Var'  , 0.0745329   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0288976   ), Coef('Var'  , 0.0577838   ), Coef('Var'  , 0.115534    ), Coef('Var'  , 0.0770713   ), Coef('Var'  , 0.0385688   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0206183   ), Coef('Var'  , 0.0413182   ), Coef('Var'  , 0.0828661   ), Coef('Var'  , 0.0609071   ), Coef('Var'  , 0.0391954   ), ], ])
	etat4.initMat[Chem([Sub('2')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0765801   ), Coef('Var'  , 0.0615235   ), Coef('Var'  , 0.0465208   ), Coef('Var'  , 0.0232863   ), Coef('Var'  , 0.0116558   ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0387689   ), Coef('Var'  , 0.0402638   ), Coef('Var'  , 0.0416225   ), Coef('Var'  , 0.0208841   ), Coef('Var'  , 0.0104695   ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0394208   ), Coef('Var'  , 0.0590004   ), Coef('Var'  , 0.0781713   ), Coef('Var'  , 0.0392954   ), Coef('Var'  , 0.019726    ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0398008   ), Coef('Var'  , 0.077301    ), Coef('Var'  , 0.114269    ), Coef('Var'  , 0.0573852   ), Coef('Var'  , 0.0287849   ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0765412   ), Coef('Var'  , 0.168304    ), Coef('Var'  , 0.260298    ), Coef('Var'  , 0.379991    ), Coef('Var'  , 0.356601    ), Coef('Const', 0.333333    ), ], 
		[Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.21037     ), Coef('Var'  , 0.235274    ), Coef('Var'  , 0.260718    ), Coef('Var'  , 0.380056    ), Coef('Var'  , 0.523247    ), Coef('Const', 0.666667    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.307836    ), Coef('Var'  , 0.211709    ), Coef('Var'  , 0.115534    ), Coef('Var'  , 0.0577838   ), Coef('Var'  , 0.0288976   ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.210682    ), Coef('Var'  , 0.146625    ), Coef('Var'  , 0.0828661   ), Coef('Var'  , 0.0413182   ), Coef('Var'  , 0.0206183   ), Coef('Const', 0           ), ], ])
	etat4.initMat[Chem([Sub('3')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.333333    ), Coef('Var'  , 0.356591    ), Coef('Var'  , 0.37998     ), Coef('Var'  , 0.260297    ), Coef('Var'  , 0.168323    ), Coef('Var'  , 0.0765801   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0282995   ), Coef('Var'  , 0.0565582   ), Coef('Var'  , 0.113006    ), Coef('Var'  , 0.0759474   ), Coef('Var'  , 0.0387689   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0196949   ), Coef('Var'  , 0.0392493   ), Coef('Var'  , 0.078119    ), Coef('Var'  , 0.0589651   ), Coef('Var'  , 0.0394208   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.011016    ), Coef('Var'  , 0.0218018   ), Coef('Var'  , 0.0429892   ), Coef('Var'  , 0.0416867   ), Coef('Var'  , 0.0398008   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.011607    ), Coef('Var'  , 0.0232101   ), Coef('Var'  , 0.0464226   ), Coef('Var'  , 0.0614381   ), Coef('Var'  , 0.0765412   ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0204566   ), Coef('Var'  , 0.0410459   ), Coef('Var'  , 0.0824588   ), Coef('Var'  , 0.146199    ), Coef('Var'  , 0.21037     ), ], 
		[Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0289384   ), Coef('Var'  , 0.0578441   ), Coef('Var'  , 0.115603    ), Coef('Var'  , 0.211755    ), Coef('Var'  , 0.307836    ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.666667    ), Coef('Var'  , 0.523397    ), Coef('Var'  , 0.380311    ), Coef('Var'  , 0.261105    ), Coef('Var'  , 0.235686    ), Coef('Var'  , 0.210682    ), ], ])
	etat4.initMat[Chem([Sub('4')])] = FMat([
		[Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.205667    ), Coef('Var'  , 0.232856    ), Coef('Var'  , 0.260297    ), Coef('Var'  , 0.37998     ), Coef('Var'  , 0.523258    ), Coef('Const', 0.666667    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.299692    ), Coef('Var'  , 0.206402    ), Coef('Var'  , 0.113006    ), Coef('Var'  , 0.0565582   ), Coef('Var'  , 0.0282995   ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.193084    ), Coef('Var'  , 0.135778    ), Coef('Var'  , 0.078119    ), Coef('Var'  , 0.0392493   ), Coef('Var'  , 0.0196949   ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0862899   ), Coef('Var'  , 0.0649131   ), Coef('Var'  , 0.0429892   ), Coef('Var'  , 0.0218018   ), Coef('Var'  , 0.011016    ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0629516   ), Coef('Var'  , 0.0546636   ), Coef('Var'  , 0.0464226   ), Coef('Var'  , 0.0232101   ), Coef('Var'  , 0.011607    ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0389351   ), Coef('Var'  , 0.060511    ), Coef('Var'  , 0.0824588   ), Coef('Var'  , 0.0410459   ), Coef('Var'  , 0.0204566   ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0385943   ), Coef('Var'  , 0.0771347   ), Coef('Var'  , 0.115603    ), Coef('Var'  , 0.0578441   ), Coef('Var'  , 0.0289384   ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0747857   ), Coef('Var'  , 0.167742    ), Coef('Var'  , 0.261105    ), Coef('Var'  , 0.380311    ), Coef('Var'  , 0.35673     ), Coef('Const', 0.333333    ), ], ])
	etat4.initMat[Chem([Sub('G')])] = FMat([
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], ])
	
	
	
	etat5.bords   = {Bord('0'): etat6, Bord('1'): etat7, Bord('2'): etat6, Bord('3'): etat7, Bord('4'): etat6, Bord('5'): etat7, }
	etat5.permuts = {}
	etat5.interns = {Intern('_'): etat5, }
	etat5.subs    = {Sub('0'): etat5, Sub('1'): etat5, Sub('2'): etat5, Sub('3'): etat5, Sub('4'): etat5, Sub('5'): etat5, Sub('G', True): Etat.etatPoint, }
	
	etat5.buildIntern()
	
	
	etat5.eqs = [
		(Chem([Bord('0'), Sub('1'), ])	,	Chem([Sub('0'), Bord('0'), ])),
		(Chem([Bord('1'), Sub('0'), ])	,	Chem([Sub('0'), Bord('1'), ])),
		(Chem([Bord('1'), Sub('1'), ])	,	Chem([Sub('1'), Bord('5'), ])),
		(Chem([Bord('2'), Sub('0'), ])	,	Chem([Sub('1'), Bord('0'), ])),
		(Chem([Bord('2'), Sub('1'), ])	,	Chem([Sub('2'), Bord('0'), ])),
		(Chem([Bord('3'), Sub('0'), ])	,	Chem([Sub('2'), Bord('1'), ])),
		(Chem([Bord('3'), Sub('1'), ])	,	Chem([Sub('3'), Bord('5'), ])),
		(Chem([Bord('4'), Sub('0'), ])	,	Chem([Sub('3'), Bord('0'), ])),
		(Chem([Bord('4'), Sub('1'), ])	,	Chem([Sub('4'), Bord('0'), ])),
		(Chem([Bord('5'), Sub('0'), ])	,	Chem([Sub('4'), Bord('1'), ])),
		(Chem([Bord('5'), Sub('1'), ])	,	Chem([Sub('5'), Bord('5'), ])),
		(Chem([Bord('0'), Sub('0'), ])	,	Chem([Sub('5'), Bord('0'), ])),
		(Chem([Sub('0'), Bord('3'), Permut('0'), ])	,	Chem([Sub('1'), Bord('3'), ])),
		(Chem([Sub('1'), Bord('1'), Permut('0'), ])	,	Chem([Sub('2'), Bord('5'), ])),
		(Chem([Sub('2'), Bord('3'), Permut('0'), ])	,	Chem([Sub('3'), Bord('3'), ])),
		(Chem([Sub('3'), Bord('1'), Permut('0'), ])	,	Chem([Sub('4'), Bord('5'), ])),
		(Chem([Sub('4'), Bord('3'), Permut('0'), ])	,	Chem([Sub('5'), Bord('3'), ])),
		(Chem([Sub('5'), Bord('1'), Permut('0'), ])	,	Chem([Sub('0'), Bord('5'), ])),
		(Chem([Bord('0'), Bord('1'), ])	,	Chem([Bord('1'), Bord('0'), ])),
		(Chem([Bord('1'), Bord('1'), ])	,	Chem([Bord('2'), Bord('0'), ])),
		(Chem([Bord('2'), Bord('1'), ])	,	Chem([Bord('3'), Bord('0'), ])),
		(Chem([Bord('3'), Bord('1'), ])	,	Chem([Bord('4'), Bord('0'), ])),
		(Chem([Bord('4'), Bord('1'), ])	,	Chem([Bord('5'), Bord('0'), ])),
		(Chem([Bord('5'), Bord('1'), ])	,	Chem([Bord('0'), Bord('0'), ])),
		]
	
	
	etat5.prim.elems = [Figure(2, [Chem([Bord('0'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('0'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('0'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('0'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('1'), Bord('0'), ]), Chem([Bord('2'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('2'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('2'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('2'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('3'), Bord('0'), ]), Chem([Bord('4'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('4'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('4'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('4'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('5'), Bord('0'), ]), ])]
	etat5.grid.elems = [
		Figure(1, [Chem([Bord('1'), Bord('0'), ]), Chem([Bord('1'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('2'), Bord('0'), ]), Chem([Bord('2'), Intern(''), ]), Chem([Bord('2'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('3'), Bord('0'), ]), Chem([Bord('3'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('4'), Bord('0'), ]), Chem([Bord('4'), Intern(''), ]), Chem([Bord('4'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('5'), Bord('0'), ]), Chem([Bord('5'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('0'), Bord('0'), ]), Chem([Bord('0'), Intern(''), ]), Chem([Bord('0'), Bord('1'), ]), ]), ]
	
	
	etat5.space = [Chem([Bord('5'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('2'), Intern('0'), Intern('0'), ]), Chem([Bord('2'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('3'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('4'), Intern('0'), Intern('0'), ]), Chem([Bord('4'), Bord('1'), Intern('0'), Intern('0'), ]), ]
	
	etat5.initMat[Chem([Sub('0')])] = FMat([
		[Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0198506   ), Coef('Var'  , 0.0396933   ), Coef('Var'  , 0.0793738   ), Coef('Var'  , 0.144549    ), Coef('Var'  , 0.209819    ), ], 
		[Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0287845   ), Coef('Var'  , 0.0574715   ), Coef('Var'  , 0.114673    ), Coef('Var'  , 0.211257    ), Coef('Var'  , 0.307571    ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.666667    ), Coef('Var'  , 0.52325     ), Coef('Var'  , 0.379996    ), Coef('Var'  , 0.260414    ), Coef('Var'  , 0.234871    ), Coef('Var'  , 0.20966     ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.333333    ), Coef('Var'  , 0.356794    ), Coef('Var'  , 0.380359    ), Coef('Var'  , 0.260982    ), Coef('Var'  , 0.167319    ), Coef('Var'  , 0.0738022   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0285264   ), Coef('Var'  , 0.0570257   ), Coef('Var'  , 0.113975    ), Coef('Var'  , 0.074279    ), Coef('Var'  , 0.0344628   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0197301   ), Coef('Var'  , 0.0394958   ), Coef('Var'  , 0.0790927   ), Coef('Var'  , 0.0535874   ), Coef('Var'  , 0.0281623   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.00854567  ), Coef('Var'  , 0.017055    ), Coef('Var'  , 0.0340259   ), Coef('Var'  , 0.0312382   ), Coef('Var'  , 0.0283878   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.00602448  ), Coef('Var'  , 0.0119237   ), Coef('Var'  , 0.0235207   ), Coef('Var'  , 0.0291719   ), Coef('Var'  , 0.0345641   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.00849432  ), Coef('Var'  , 0.0169794   ), Coef('Var'  , 0.0339421   ), Coef('Var'  , 0.0537277   ), Coef('Var'  , 0.0735716   ), ], ])
	etat5.initMat[Chem([Sub('1')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.028389    ), Coef('Var'  , 0.0538959   ), Coef('Var'  , 0.0793738   ), Coef('Var'  , 0.0396933   ), Coef('Var'  , 0.0198506   ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0350214   ), Coef('Var'  , 0.0750108   ), Coef('Var'  , 0.114673    ), Coef('Var'  , 0.0574715   ), Coef('Var'  , 0.0287845   ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0733483   ), Coef('Var'  , 0.166724    ), Coef('Var'  , 0.260414    ), Coef('Var'  , 0.379996    ), Coef('Var'  , 0.356583    ), Coef('Const', 0.333333    ), ], 
		[Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.2101      ), Coef('Var'  , 0.235457    ), Coef('Var'  , 0.260982    ), Coef('Var'  , 0.380359    ), Coef('Var'  , 0.523461    ), Coef('Const', 0.666667    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.307027    ), Coef('Var'  , 0.210535    ), Coef('Var'  , 0.113975    ), Coef('Var'  , 0.0570257   ), Coef('Var'  , 0.0285264   ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.209696    ), Coef('Var'  , 0.144309    ), Coef('Var'  , 0.0790927   ), Coef('Var'  , 0.0394958   ), Coef('Var'  , 0.0197301   ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0735146   ), Coef('Var'  , 0.0537494   ), Coef('Var'  , 0.0340259   ), Coef('Var'  , 0.017055    ), Coef('Var'  , 0.00854567  ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0345902   ), Coef('Var'  , 0.0291892   ), Coef('Var'  , 0.0235207   ), Coef('Var'  , 0.0119237   ), Coef('Var'  , 0.00602448  ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0283146   ), Coef('Var'  , 0.0311307   ), Coef('Var'  , 0.0339421   ), Coef('Var'  , 0.0169794   ), Coef('Var'  , 0.00849432  ), Coef('Const', 0           ), ], ])
	etat5.initMat[Chem([Sub('2')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.00853846  ), Coef('Var'  , 0.0170441   ), Coef('Var'  , 0.0340128   ), Coef('Var'  , 0.0312303   ), Coef('Var'  , 0.028389    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.00623693  ), Coef('Var'  , 0.0122895   ), Coef('Var'  , 0.0240907   ), Coef('Var'  , 0.0297716   ), Coef('Var'  , 0.0350214   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.00843145  ), Coef('Var'  , 0.0168647   ), Coef('Var'  , 0.0337463   ), Coef('Var'  , 0.0534858   ), Coef('Var'  , 0.0733483   ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0199724   ), Coef('Var'  , 0.0399048   ), Coef('Var'  , 0.0797084   ), Coef('Var'  , 0.144907    ), Coef('Var'  , 0.2101      ), ], 
		[Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0285004   ), Coef('Var'  , 0.0569864   ), Coef('Var'  , 0.113928    ), Coef('Var'  , 0.210504    ), Coef('Var'  , 0.307027    ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.666667    ), Coef('Var'  , 0.523299    ), Coef('Var'  , 0.380073    ), Coef('Var'  , 0.260513    ), Coef('Var'  , 0.234955    ), Coef('Var'  , 0.209696    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.333333    ), Coef('Var'  , 0.356635    ), Coef('Var'  , 0.380092    ), Coef('Var'  , 0.260581    ), Coef('Var'  , 0.166913    ), Coef('Var'  , 0.0735146   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0285658   ), Coef('Var'  , 0.0570963   ), Coef('Var'  , 0.114092    ), Coef('Var'  , 0.074421    ), Coef('Var'  , 0.0345902   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0198203   ), Coef('Var'  , 0.0396495   ), Coef('Var'  , 0.0793282   ), Coef('Var'  , 0.0538128   ), Coef('Var'  , 0.0283146   ), ], ])
	etat5.initMat[Chem([Sub('3')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0735064   ), Coef('Var'  , 0.0537353   ), Coef('Var'  , 0.0340128   ), Coef('Var'  , 0.0170441   ), Coef('Var'  , 0.00853846  ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0350235   ), Coef('Var'  , 0.0297729   ), Coef('Var'  , 0.0240907   ), Coef('Var'  , 0.0122895   ), Coef('Var'  , 0.00623693  ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0281743   ), Coef('Var'  , 0.0309435   ), Coef('Var'  , 0.0337463   ), Coef('Var'  , 0.0168647   ), Coef('Var'  , 0.00843145  ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0286473   ), Coef('Var'  , 0.0542389   ), Coef('Var'  , 0.0797084   ), Coef('Var'  , 0.0399048   ), Coef('Var'  , 0.0199724   ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0344369   ), Coef('Var'  , 0.0742308   ), Coef('Var'  , 0.113928    ), Coef('Var'  , 0.0569864   ), Coef('Var'  , 0.0285004   ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0733979   ), Coef('Var'  , 0.166817    ), Coef('Var'  , 0.260513    ), Coef('Var'  , 0.380073    ), Coef('Var'  , 0.356632    ), Coef('Const', 0.333333    ), ], 
		[Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.209811    ), Coef('Var'  , 0.23505     ), Coef('Var'  , 0.260581    ), Coef('Var'  , 0.380092    ), Coef('Var'  , 0.523302    ), Coef('Const', 0.666667    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.307105    ), Coef('Var'  , 0.210645    ), Coef('Var'  , 0.114092    ), Coef('Var'  , 0.0570963   ), Coef('Var'  , 0.0285658   ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.209897    ), Coef('Var'  , 0.144567    ), Coef('Var'  , 0.0793282   ), Coef('Var'  , 0.0396495   ), Coef('Var'  , 0.0198203   ), Coef('Const', 0           ), ], ])
	etat5.initMat[Chem([Sub('4')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.333333    ), Coef('Var'  , 0.356634    ), Coef('Var'  , 0.380091    ), Coef('Var'  , 0.260579    ), Coef('Var'  , 0.166906    ), Coef('Var'  , 0.0735064   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0287866   ), Coef('Var'  , 0.0574747   ), Coef('Var'  , 0.114677    ), Coef('Var'  , 0.0750147   ), Coef('Var'  , 0.0350235   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0197429   ), Coef('Var'  , 0.0395129   ), Coef('Var'  , 0.079106    ), Coef('Var'  , 0.0536083   ), Coef('Var'  , 0.0281743   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0086749   ), Coef('Var'  , 0.0172778   ), Coef('Var'  , 0.034374    ), Coef('Var'  , 0.0315909   ), Coef('Var'  , 0.0286473   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.00593653  ), Coef('Var'  , 0.0117797   ), Coef('Var'  , 0.0233157   ), Coef('Var'  , 0.0289721   ), Coef('Var'  , 0.0344369   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.00843226  ), Coef('Var'  , 0.0168683   ), Coef('Var'  , 0.0337577   ), Coef('Var'  , 0.0535219   ), Coef('Var'  , 0.0733979   ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0198421   ), Coef('Var'  , 0.0396803   ), Coef('Var'  , 0.0793583   ), Coef('Var'  , 0.144534    ), Coef('Var'  , 0.209811    ), ], 
		[Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0285397   ), Coef('Var'  , 0.0570567   ), Coef('Var'  , 0.114044    ), Coef('Var'  , 0.210613    ), Coef('Var'  , 0.307105    ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.666667    ), Coef('Var'  , 0.523411    ), Coef('Var'  , 0.380259    ), Coef('Var'  , 0.260787    ), Coef('Var'  , 0.235239    ), Coef('Var'  , 0.209897    ), ], ])
	etat5.initMat[Chem([Sub('5')])] = FMat([
		[Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.209819    ), Coef('Var'  , 0.235054    ), Coef('Var'  , 0.260579    ), Coef('Var'  , 0.380091    ), Coef('Var'  , 0.523301    ), Coef('Const', 0.666667    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.307571    ), Coef('Var'  , 0.21126     ), Coef('Var'  , 0.114677    ), Coef('Var'  , 0.0574747   ), Coef('Var'  , 0.0287866   ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.20966     ), Coef('Var'  , 0.144298    ), Coef('Var'  , 0.079106    ), Coef('Var'  , 0.0395129   ), Coef('Var'  , 0.0197429   ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0738022   ), Coef('Var'  , 0.0541206   ), Coef('Var'  , 0.034374    ), Coef('Var'  , 0.0172778   ), Coef('Var'  , 0.0086749   ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0344628   ), Coef('Var'  , 0.0289892   ), Coef('Var'  , 0.0233157   ), Coef('Var'  , 0.0117797   ), Coef('Var'  , 0.00593653  ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0281623   ), Coef('Var'  , 0.030939    ), Coef('Var'  , 0.0337577   ), Coef('Var'  , 0.0168683   ), Coef('Var'  , 0.00843226  ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0283878   ), Coef('Var'  , 0.0538849   ), Coef('Var'  , 0.0793583   ), Coef('Var'  , 0.0396803   ), Coef('Var'  , 0.0198421   ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0345641   ), Coef('Var'  , 0.0743724   ), Coef('Var'  , 0.114044    ), Coef('Var'  , 0.0570567   ), Coef('Var'  , 0.0285397   ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0735716   ), Coef('Var'  , 0.167082    ), Coef('Var'  , 0.260787    ), Coef('Var'  , 0.380259    ), Coef('Var'  , 0.356744    ), Coef('Const', 0.333333    ), ], ])
	etat5.initMat[Chem([Sub('G')])] = FMat([
		[Coef('Const', 0.111111    )], 
		[Coef('Const', 0.111111    )], 
		[Coef('Const', 0.111111    )], 
		[Coef('Const', 0.111111    )], 
		[Coef('Const', 0.111111    )], 
		[Coef('Const', 0.111111    )], 
		[Coef('Const', 0.111111    )], 
		[Coef('Const', 0.111111    )], 
		[Coef('Const', 0.111111    )], ])
	
	
	
	etat6.bords   = {Bord('0'): etat11, Bord('1'): etat11, }
	etat6.permuts = {Permut('0'): etat6, }
	etat6.interns = {Intern('_'): etat6, }
	etat6.subs    = {Sub('0'): etat6, Sub('1'): etat6, Sub('G', True): Etat.etatPoint, }
	
	etat6.buildIntern()
	etat6.fm_[Permut('0')] = PMat(3, [2, 1, 0, ])
	
	
	etat6.eqs = [
		(Chem([Permut('0'), Bord('0'), ])	,	Chem([Bord('1')])),
		(Chem([Permut('0'), Bord('1'), ])	,	Chem([Bord('0')])),
		(Chem([Permut('0'), Intern(''), ])	,	Chem([Intern('')])),
		(Chem([Permut('0'), Sub('0'), ])	,	Chem([Sub('1'), Permut('0'), ])),
		(Chem([Permut('0'), Sub('1'), ])	,	Chem([Sub('0'), Permut('0'), ])),
		]
	
	
	etat6.prim.elems = [Figure(1, [Chem([Bord('0')]), Chem([Bord('1')]), ])]
	etat6.grid.elems = [Figure(1, [Chem([Bord('0')]), Chem([Intern('')]), Chem([Bord('1')]), ])]
	
	
	etat6.space = [Chem([Bord('0'), Intern('0'), Intern('0'), ]), Chem([Intern('0'), Intern('0'), ]), Chem([Bord('1'), Intern('0'), Intern('0'), ]), ]
	
	etat6.initMat[Chem([Sub('0')])] = FMat([
		[Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), ], ])
	etat6.initMat[Chem([Sub('1')])] = FMat([
		[Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), ], ])
	etat6.initMat[Chem([Sub('G')])] = FMat([
		[Coef('Const', 0           )], 
		[Coef('Const', 1           )], 
		[Coef('Const', 0           )], ])
	
	
	
	etat7.bords   = {Bord('0'): etat11, Bord('1'): etat11, }
	etat7.permuts = {Permut('0'): etat7, }
	etat7.interns = {Intern('_'): etat7, }
	etat7.subs    = {Sub('0'): etat7, Sub('1'): etat7, Sub('G', True): Etat.etatPoint, }
	
	etat7.buildIntern()
	etat7.fm_[Permut('0')] = PMat(2, [1, 0, ])
	
	
	etat7.eqs = [
		(Chem([Permut('0'), Bord('0'), ])	,	Chem([Bord('1')])),
		(Chem([Permut('0'), Bord('1'), ])	,	Chem([Bord('0')])),
		(Chem([Permut('0'), Sub('0'), ])	,	Chem([Sub('1'), Permut('0'), ])),
		(Chem([Permut('0'), Sub('1'), ])	,	Chem([Sub('0'), Permut('0'), ])),
		(Chem([Bord('0'), Sub('0'), ])	,	Chem([Sub('0'), Bord('0'), ])),
		(Chem([Bord('1'), Sub('0'), ])	,	Chem([Sub('1'), Bord('1'), ])),
		]
	
	
	etat7.prim.elems = []
	etat7.grid.elems = [Figure(1, [Chem([Bord('0')]), Chem([Bord('1')]), ])]
	
	
	etat7.space = [Chem([Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Intern('0'), Intern('0'), ]), ]
	
	etat7.initMat[Chem([Sub('0')])] = FMat([
		[Coef('Const', 1           ), Coef('Const', 0.666667    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.333333    ), ], ])
	etat7.initMat[Chem([Sub('1')])] = FMat([
		[Coef('Const', 0.333333    ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.666667    ), Coef('Const', 1           ), ], ])
	etat7.initMat[Chem([Sub('G')])] = FMat([
		[Coef('Const', 0.5         )], 
		[Coef('Const', 0.5         )], ])
	
	
	
	etat8.bords   = {Bord('0'): etat11, Bord('1'): etat11, }
	etat8.permuts = {Permut('0'): etat8, }
	etat8.interns = {Intern('_'): etat8, }
	etat8.subs    = {Sub('0'): etat7, Sub('G', True): Etat.etatPoint, }
	
	etat8.buildIntern()
	etat8.fm_[Permut('0')] = PMat(2, [1, 0, ])
	
	
	etat8.eqs = [
		(Chem([Permut('0'), Bord('0'), ])	,	Chem([Bord('1')])),
		(Chem([Permut('0'), Bord('1'), ])	,	Chem([Bord('0')])),
		(Chem([Permut('0'), Sub('0'), ])	,	Chem([Sub('0'), Permut('0'), ])),
		(Chem([Bord('0'), Sub('0'), ])	,	Chem([Sub('0'), Bord('0'), ])),
		(Chem([Bord('1'), Sub('0'), ])	,	Chem([Sub('0'), Bord('1'), ])),
		]
	
	
	etat8.prim.elems = [Figure(1, [Chem([Bord('0')]), Chem([Bord('1')]), ])]
	etat8.grid.elems = [Figure(1, [Chem([Bord('0')]), Chem([Bord('1')]), ])]
	
	
	etat8.space = [Chem([Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Intern('0'), Intern('0'), ]), ]
	
	etat8.initMat[Chem([Sub('0')])] = FMat([
		[Coef('Const', 1           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 1           ), ], ])
	etat8.initMat[Chem([Sub('G')])] = FMat([
		[Coef('Const', 0.5         )], 
		[Coef('Const', 0.5         )], ])
	
	
	
	etat9.bords   = {Bord('0'): etat7, Bord('1'): etat6, Bord('2'): etat7, Bord('3'): etat6, }
	etat9.permuts = {}
	etat9.interns = {Intern('_'): etat9, }
	etat9.subs    = {Sub('0'): etat5, Sub('1'): etat5, Sub('2'): etat5, Sub('3'): etat5, Sub('G', True): Etat.etatPoint, }
	
	etat9.buildIntern()
	
	
	etat9.eqs = [
		(Chem([Bord('0'), Sub('1'), ])	,	Chem([Sub('0'), Bord('5'), ])),
		(Chem([Bord('1'), Sub('0'), ])	,	Chem([Sub('0'), Bord('0'), ])),
		(Chem([Bord('1'), Sub('1'), ])	,	Chem([Sub('1'), Bord('0'), ])),
		(Chem([Bord('2'), Sub('0'), ])	,	Chem([Sub('1'), Bord('1'), ])),
		(Chem([Bord('2'), Sub('1'), ])	,	Chem([Sub('2'), Bord('5'), ])),
		(Chem([Bord('3'), Sub('0'), ])	,	Chem([Sub('2'), Bord('0'), ])),
		(Chem([Bord('3'), Sub('1'), ])	,	Chem([Sub('3'), Bord('0'), ])),
		(Chem([Bord('0'), Sub('0'), ])	,	Chem([Sub('3'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('1'), Permut('0'), ])	,	Chem([Sub('1'), Bord('5'), ])),
		(Chem([Sub('1'), Bord('3'), Permut('0'), ])	,	Chem([Sub('2'), Bord('3'), ])),
		(Chem([Sub('2'), Bord('1'), Permut('0'), ])	,	Chem([Sub('3'), Bord('5'), ])),
		(Chem([Sub('3'), Bord('3'), Permut('0'), ])	,	Chem([Sub('0'), Bord('3'), ])),
		(Chem([Bord('0'), Bord('1'), ])	,	Chem([Bord('1'), Bord('0'), ])),
		(Chem([Bord('1'), Bord('1'), ])	,	Chem([Bord('2'), Bord('0'), ])),
		(Chem([Bord('2'), Bord('1'), ])	,	Chem([Bord('3'), Bord('0'), ])),
		(Chem([Bord('3'), Bord('1'), ])	,	Chem([Bord('0'), Bord('0'), ])),
		]
	
	
	etat9.prim.elems = [Figure(2, [Chem([Bord('0'), Bord('0'), ]), Chem([Bord('1'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('1'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('1'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('1'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('2'), Bord('0'), ]), Chem([Bord('3'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('3'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('3'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('3'), Sub('1'), Sub('1'), Bord('0'), ]), ])]
	etat9.grid.elems = [
		Figure(1, [Chem([Bord('1'), Bord('0'), ]), Chem([Bord('1'), Intern(''), ]), Chem([Bord('1'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('2'), Bord('0'), ]), Chem([Bord('2'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('0'), Bord('0'), ]), Chem([Bord('0'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('3'), Bord('0'), ]), Chem([Bord('3'), Intern(''), ]), Chem([Bord('3'), Bord('1'), ]), ]), ]
	
	
	etat9.space = [Chem([Bord('0'), Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('2'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('3'), Intern('0'), Intern('0'), ]), ]
	
	etat9.initMat[Chem([Sub('0')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.093024    ), Coef('Var'  , 0.181254    ), Coef('Var'  , 0.269802    ), Coef('Var'  , 0.38472     ), Coef('Var'  , 0.358958    ), Coef('Const', 0.333333    ), ], 
		[Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.218146    ), Coef('Var'  , 0.243926    ), Coef('Var'  , 0.269972    ), Coef('Var'  , 0.384834    ), Coef('Var'  , 0.525693    ), Coef('Const', 0.666667    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.313182    ), Coef('Var'  , 0.219675    ), Coef('Var'  , 0.125899    ), Coef('Var'  , 0.0630849   ), Coef('Var'  , 0.0315924   ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.218255    ), Coef('Var'  , 0.160843    ), Coef('Var'  , 0.103593    ), Coef('Var'  , 0.0517381   ), Coef('Var'  , 0.0258492   ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0940067   ), Coef('Var'  , 0.0993356   ), Coef('Var'  , 0.104546    ), Coef('Var'  , 0.0523445   ), Coef('Var'  , 0.0261995   ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0633868   ), Coef('Var'  , 0.0949664   ), Coef('Var'  , 0.126188    ), Coef('Var'  , 0.0632793   ), Coef('Var'  , 0.0317086   ), Coef('Const', 0           ), ], ])
	etat9.initMat[Chem([Sub('1')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0257327   ), Coef('Var'  , 0.0515393   ), Coef('Var'  , 0.103288    ), Coef('Var'  , 0.0980289   ), Coef('Var'  , 0.093024    ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0257864   ), Coef('Var'  , 0.0516332   ), Coef('Var'  , 0.103438    ), Coef('Var'  , 0.160686    ), Coef('Var'  , 0.218146    ), ], 
		[Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0315897   ), Coef('Var'  , 0.063081    ), Coef('Var'  , 0.125895    ), Coef('Var'  , 0.219673    ), Coef('Var'  , 0.313182    ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.666667    ), Coef('Var'  , 0.525739    ), Coef('Var'  , 0.384916    ), Coef('Var'  , 0.270104    ), Coef('Var'  , 0.244066    ), Coef('Var'  , 0.218255    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.333333    ), Coef('Var'  , 0.359474    ), Coef('Var'  , 0.385594    ), Coef('Var'  , 0.271129    ), Coef('Var'  , 0.18261     ), Coef('Var'  , 0.0940067   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0316784   ), Coef('Var'  , 0.0632366   ), Coef('Var'  , 0.126145    ), Coef('Var'  , 0.0949362   ), Coef('Var'  , 0.0633868   ), ], ])
	etat9.initMat[Chem([Sub('2')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.218024    ), Coef('Var'  , 0.160529    ), Coef('Var'  , 0.103288    ), Coef('Var'  , 0.0515393   ), Coef('Var'  , 0.0257327   ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0931455   ), Coef('Var'  , 0.0981865   ), Coef('Var'  , 0.103438    ), Coef('Var'  , 0.0516332   ), Coef('Var'  , 0.0257864   ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0631821   ), Coef('Var'  , 0.0946726   ), Coef('Var'  , 0.125895    ), Coef('Var'  , 0.063081    ), Coef('Var'  , 0.0315897   ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.093255    ), Coef('Var'  , 0.181566    ), Coef('Var'  , 0.270104    ), Coef('Var'  , 0.384916    ), Coef('Var'  , 0.359072    ), Coef('Const', 0.333333    ), ], 
		[Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.219007    ), Coef('Var'  , 0.24511     ), Coef('Var'  , 0.271129    ), Coef('Var'  , 0.385594    ), Coef('Var'  , 0.526141    ), Coef('Const', 0.666667    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.313387    ), Coef('Var'  , 0.219936    ), Coef('Var'  , 0.126145    ), Coef('Var'  , 0.0632366   ), Coef('Var'  , 0.0316784   ), Coef('Const', 0           ), ], ])
	etat9.initMat[Chem([Sub('3')])] = FMat([
		[Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.666667    ), Coef('Var'  , 0.525625    ), Coef('Var'  , 0.38472     ), Coef('Var'  , 0.269802    ), Coef('Var'  , 0.243754    ), Coef('Var'  , 0.218024    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.333333    ), Coef('Var'  , 0.359026    ), Coef('Var'  , 0.384834    ), Coef('Var'  , 0.269972    ), Coef('Var'  , 0.181426    ), Coef('Var'  , 0.0931455   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0315924   ), Coef('Var'  , 0.0630849   ), Coef('Var'  , 0.125899    ), Coef('Var'  , 0.0946753   ), Coef('Var'  , 0.0631821   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0258492   ), Coef('Var'  , 0.0517381   ), Coef('Var'  , 0.103593    ), Coef('Var'  , 0.0983428   ), Coef('Var'  , 0.093255    ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0261995   ), Coef('Var'  , 0.0523445   ), Coef('Var'  , 0.104546    ), Coef('Var'  , 0.161836    ), Coef('Var'  , 0.219007    ), ], 
		[Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0317086   ), Coef('Var'  , 0.0632793   ), Coef('Var'  , 0.126188    ), Coef('Var'  , 0.219966    ), Coef('Var'  , 0.313387    ), ], ])
	etat9.initMat[Chem([Sub('G')])] = FMat([
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], ])
	
	
	
	etat10.bords   = {Bord('0'): etat11, Bord('1'): etat11, }
	etat10.permuts = {Permut('0'): etat10, }
	etat10.interns = {Intern('_'): etat10, }
	etat10.subs    = {Sub('0'): etat6, Sub('G', True): Etat.etatPoint, }
	
	etat10.buildIntern()
	etat10.fm_[Permut('0')] = PMat(3, [2, 1, 0, ])
	
	
	etat10.eqs = [
		(Chem([Permut('0'), Bord('0'), ])	,	Chem([Bord('1')])),
		(Chem([Permut('0'), Bord('1'), ])	,	Chem([Bord('0')])),
		(Chem([Permut('0'), Intern(''), ])	,	Chem([Intern('')])),
		(Chem([Permut('0'), Sub('0'), ])	,	Chem([Sub('0'), Permut('0'), ])),
		(Chem([Bord('0'), Sub('0'), ])	,	Chem([Sub('0'), Bord('0'), ])),
		(Chem([Bord('1'), Sub('0'), ])	,	Chem([Sub('0'), Bord('1'), ])),
		]
	
	
	etat10.prim.elems = [Figure(1, [Chem([Bord('0')]), Chem([Bord('1')]), ])]
	etat10.grid.elems = [Figure(1, [Chem([Bord('0')]), Chem([Intern('')]), Chem([Bord('1')]), ])]
	
	
	etat10.space = [Chem([Bord('0'), Intern('0'), Intern('0'), ]), Chem([Intern('0'), Intern('0'), ]), Chem([Bord('1'), Intern('0'), Intern('0'), ]), ]
	
	etat10.initMat[Chem([Sub('0')])] = FMat([
		[Coef('Const', 1           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 1           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 1           ), ], ])
	etat10.initMat[Chem([Sub('G')])] = FMat([
		[Coef('Const', 0           )], 
		[Coef('Const', 1           )], 
		[Coef('Const', 0           )], ])
	
	
	
	etat11.bords   = {}
	etat11.permuts = {}
	etat11.interns = {Intern('_'): etat11, }
	etat11.subs    = {Sub('0'): etat11, Sub('G', True): Etat.etatPoint, }
	
	etat11.buildIntern()
	
	
	etat11.eqs = [
		]
	
	
	etat11.prim.elems = []
	etat11.grid.elems = []
	
	
	etat11.space = [Chem([Intern('0'), Intern('0'), ])]
	
	etat11.initMat[Chem([Sub('0')])] = FMat([[Coef('Const', 1           )]])
	etat11.initMat[Chem([Sub('G')])] = FMat([[Coef('Const', 1           )]])
	
	
	
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
