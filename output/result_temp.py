# -*- coding: utf-8 -*-

# Automatically generated, from file : result_temp.py, function : modele()

from __future__ import division
import sys
if './../../../../../../python' not in sys.path:
	sys.path.append('./../../../../../../python')
from etat import *

def modele():
	
	etat0 = EtatInit()
	etat1 = Etat('Cell_0',0)
	etat2 = Etat('Cell_1',0)
	etat3 = Etat('Cell_2',0)
	etat4 = Etat('Cell_3',0)
	etat5 = Etat('B2',1)
	etat6 = Etat('C2',0)
	etat7 = Etat('s',1)
	
	
	# etat0.subs   = {Sub('0'): etat1, Sub('1'): etat2, Sub('2'): etat2, Sub('3'): etat2, Sub('4'): etat1, }
	etat0.subs   = {Sub('2'): etat2}
	
	#etat0.eqs = [
	#	(Chem([Sub('0'), Bord('2'), Permut('0'), ])	,	Chem([Sub('1'), Bord('0'), ])),
	#	(Chem([Sub('1'), Bord('2'), Permut('0'), ])	,	Chem([Sub('2'), Bord('0'), ])),
	#	(Chem([Sub('2'), Bord('2'), Permut('0'), ])	,	Chem([Sub('3'), Bord('2'), ])),
	#	(Chem([Sub('3'), Bord('0'), Permut('0'), ])	,	Chem([Sub('4'), Bord('2'), ])),
	#	]
	
	
	etat0.space = []
	
	#etat0.initMat[Chem([Sub('0')])] = FMat([
	#	[Coef('Var'  ,-7.5         ), Coef('Var'  ,-7.5         ), Coef('Var'  ,-7.5         ), Coef('Var'  ,-5.5         ), Coef('Var'  ,-3.5         ), Coef('Var'  ,-3.5         ), Coef('Var'  ,-5.5         ), ], 
	#	[Coef('Var'  , 2           ), Coef('Var'  , 0           ), Coef('Var'  ,-2           ), Coef('Var'  ,-2           ), Coef('Var'  ,-2           ), Coef('Var'  , 2           ), Coef('Var'  , 2           ), ], 
	#	[Coef('Var'  , 0           ), Coef('Var'  , 0           ), Coef('Var'  , 0           ), Coef('Var'  , 0           ), Coef('Var'  , 0           ), Coef('Var'  , 0           ), Coef('Var'  , 0           ), ], 
	#	[Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), ], ])
	#etat0.initMat[Chem([Sub('1')])] = FMat([
	#	[Coef('Var'  ,-3.5         ), Coef('Var'  ,-3.5         ), Coef('Var'  ,-2           ), Coef('Var'  ,-0.5         ), Coef('Var'  ,-0.5         ), Coef('Var'  ,-2           ), ], 
	#	[Coef('Var'  , 2           ), Coef('Var'  ,-2           ), Coef('Var'  ,-0.5         ), Coef('Var'  ,-0.5         ), Coef('Var'  , 0.5         ), Coef('Var'  , 0.5         ), ], 
	#	[Coef('Var'  , 0           ), Coef('Var'  , 0           ), Coef('Var'  , 0           ), Coef('Var'  , 0           ), Coef('Var'  , 0           ), Coef('Var'  , 0           ), ], 
	#	[Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), ], ])
	etat0.initMat[Chem([Sub('2')])] = FMat([
		[Coef('Var'  ,-0.5         ), Coef('Var'  ,-0.5         ), Coef('Var'  , 0           ), Coef('Var'  , 0.5         ), Coef('Var'  , 0.5         ), Coef('Var'  , 0           ), ], 
		[Coef('Var'  , 0.5         ), Coef('Var'  ,-0.5         ), Coef('Var'  ,-0.5         ), Coef('Var'  ,-0.5         ), Coef('Var'  , 0.5         ), Coef('Var'  , 0.5         ), ], 
		[Coef('Var'  , 0           ), Coef('Var'  , 0           ), Coef('Var'  , 0           ), Coef('Var'  , 0           ), Coef('Var'  , 0           ), Coef('Var'  , 0           ), ], 
		[Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), ], ])
	#etat0.initMat[Chem([Sub('3')])] = FMat([
	#	[Coef('Var'  , 3.5         ), Coef('Var'  , 3.5         ), Coef('Var'  , 2           ), Coef('Var'  , 0.5         ), Coef('Var'  , 0.5         ), Coef('Var'  , 2           ), ], 
	#	[Coef('Var'  ,-2           ), Coef('Var'  , 2           ), Coef('Var'  , 0.5         ), Coef('Var'  , 0.5         ), Coef('Var'  ,-0.5         ), Coef('Var'  ,-0.5         ), ], 
	#	[Coef('Var'  , 0           ), Coef('Var'  , 0           ), Coef('Var'  , 0           ), Coef('Var'  , 0           ), Coef('Var'  , 0           ), Coef('Var'  , 0           ), ], 
	#	[Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), ], ])
	#etat0.initMat[Chem([Sub('4')])] = FMat([
	#	[Coef('Var'  , 7.5         ), Coef('Var'  , 7.5         ), Coef('Var'  , 7.5         ), Coef('Var'  , 5.5         ), Coef('Var'  , 3.5         ), Coef('Var'  , 3.5         ), Coef('Var'  , 5.5         ), ], 
	#	[Coef('Var'  ,-2           ), Coef('Var'  , 0           ), Coef('Var'  , 2           ), Coef('Var'  , 2           ), Coef('Var'  , 2           ), Coef('Var'  ,-2           ), Coef('Var'  ,-2           ), ], 
	#	[Coef('Var'  , 0           ), Coef('Var'  , 0           ), Coef('Var'  , 0           ), Coef('Var'  , 0           ), Coef('Var'  , 0           ), Coef('Var'  , 0           ), Coef('Var'  , 0           ), ], 
	#	[Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), ], ])
	
	
	
	etat1.bords   = {Bord('0'): etat5, Bord('1'): etat5, Bord('2'): etat6, Bord('3'): etat5, }
	etat1.permuts = {}
	etat1.interns = {Intern('_'): etat1, }
	etat1.subs    = {Sub('0'): etat3, Sub('1'): etat4, Sub('2'): etat4, Sub('3'): etat3, Sub('G', True): Etat.etatPoint, }
	
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
		[Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0706343   ), Coef('Var'  , 0.131374    ), Coef('Var'  , 0.191823    ), ], 
		[Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0884155   ), Coef('Var'  , 0.191371    ), Coef('Var'  , 0.294263    ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.195267    ), Coef('Var'  , 0.19347     ), Coef('Var'  , 0.191519    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.302181    ), Coef('Var'  , 0.195635    ), Coef('Var'  , 0.0888233   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.208546    ), Coef('Var'  , 0.140432    ), Coef('Var'  , 0.0726944   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0835294   ), Coef('Var'  , 0.0779141   ), Coef('Var'  , 0.0726806   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0514272   ), Coef('Var'  , 0.0698026   ), Coef('Var'  , 0.0881968   ), ], ])
	etat1.initMat[Chem([Sub('1')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.022575    ), Coef('Var'  , 0.0449723   ), Coef('Var'  , 0.0894734   ), Coef('Var'  , 0.0802621   ), Coef('Var'  , 0.0706343   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.014831    ), Coef('Var'  , 0.0296171   ), Coef('Var'  , 0.0591162   ), Coef('Var'  , 0.073815    ), Coef('Var'  , 0.0884155   ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0223312   ), Coef('Var'  , 0.044569    ), Coef('Var'  , 0.0888898   ), Coef('Var'  , 0.142188    ), Coef('Var'  , 0.195267    ), ], 
		[Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0298808   ), Coef('Var'  , 0.0596003   ), Coef('Var'  , 0.118773    ), Coef('Var'  , 0.210666    ), Coef('Var'  , 0.302181    ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.666667    ), Coef('Var'  , 0.523836    ), Coef('Var'  , 0.381239    ), Coef('Var'  , 0.263095    ), Coef('Var'  , 0.23555     ), Coef('Var'  , 0.208546    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.333333    ), Coef('Var'  , 0.357158    ), Coef('Var'  , 0.381221    ), Coef('Var'  , 0.263069    ), Coef('Var'  , 0.173024    ), Coef('Var'  , 0.0835294   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0293873   ), Coef('Var'  , 0.0587816   ), Coef('Var'  , 0.117583    ), Coef('Var'  , 0.0844943   ), Coef('Var'  , 0.0514272   ), ], ])
	etat1.initMat[Chem([Sub('2')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.195634    ), Coef('Var'  , 0.142762    ), Coef('Var'  , 0.0894734   ), Coef('Var'  , 0.0449723   ), Coef('Var'  , 0.022575    ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0884154   ), Coef('Var'  , 0.0738149   ), Coef('Var'  , 0.0591162   ), Coef('Var'  , 0.0296171   ), Coef('Var'  , 0.014831    ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0702667   ), Coef('Var'  , 0.0796884   ), Coef('Var'  , 0.0888898   ), Coef('Var'  , 0.044569    ), Coef('Var'  , 0.0223312   ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0521813   ), Coef('Var'  , 0.0856663   ), Coef('Var'  , 0.118773    ), Coef('Var'  , 0.0596003   ), Coef('Var'  , 0.0298808   ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.083546    ), Coef('Var'  , 0.17305     ), Coef('Var'  , 0.263095    ), Coef('Var'  , 0.381239    ), Coef('Var'  , 0.357169    ), Coef('Const', 0.333333    ), ], 
		[Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.208529    ), Coef('Var'  , 0.235524    ), Coef('Var'  , 0.263069    ), Coef('Var'  , 0.381221    ), Coef('Var'  , 0.523825    ), Coef('Const', 0.666667    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.301427    ), Coef('Var'  , 0.209494    ), Coef('Var'  , 0.117583    ), Coef('Var'  , 0.0587816   ), Coef('Var'  , 0.0293873   ), Coef('Const', 0           ), ], ])
	etat1.initMat[Chem([Sub('3')])] = FMat([
		[Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.191823    ), Coef('Var'  , 0.193874    ), Coef('Var'  , 0.195634    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.294263    ), Coef('Var'  , 0.191371    ), Coef('Var'  , 0.0884154   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.191519    ), Coef('Var'  , 0.130971    ), Coef('Var'  , 0.0702667   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0888233   ), Coef('Var'  , 0.0706353   ), Coef('Var'  , 0.0521813   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0726944   ), Coef('Var'  , 0.0779324   ), Coef('Var'  , 0.083546    ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0726806   ), Coef('Var'  , 0.140414    ), Coef('Var'  , 0.208529    ), ], 
		[Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0881968   ), Coef('Var'  , 0.194802    ), Coef('Var'  , 0.301427    ), ], ])
	etat1.initMat[Chem([Sub('G')])] = FMat([
		[Coef('Const', 0.142857    )], 
		[Coef('Const', 0.142857    )], 
		[Coef('Const', 0.142857    )], 
		[Coef('Const', 0.142857    )], 
		[Coef('Const', 0.142857    )], 
		[Coef('Const', 0.142857    )], 
		[Coef('Const', 0.142857    )], ])
	
	
	
	etat2.bords   = {Bord('0'): etat6, Bord('1'): etat5, Bord('2'): etat6, Bord('3'): etat5, }
	etat2.permuts = {}
	etat2.interns = {Intern('_'): etat2, }
	etat2.subs    = {Sub('0'): etat4, Sub('1'): etat4, Sub('2'): etat4, Sub('3'): etat4, Sub('G', True): Etat.etatPoint, }
	
	etat2.buildIntern()
	
	
	etat2.eqs = [
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
	
	
	etat2.prim.elems = [Figure(2, [Chem([Bord('0'), Bord('0'), ]), Chem([Bord('1'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('1'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('1'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('1'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('2'), Bord('0'), ]), Chem([Bord('3'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('3'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('3'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('3'), Sub('1'), Sub('1'), Bord('0'), ]), ])]
	etat2.grid.elems = [
		Figure(1, [Chem([Bord('1'), Bord('0'), ]), Chem([Bord('1'), Intern(''), ]), Chem([Bord('1'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('2'), Bord('0'), ]), Chem([Bord('2'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('0'), Bord('0'), ]), Chem([Bord('0'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('3'), Bord('0'), ]), Chem([Bord('3'), Intern(''), ]), Chem([Bord('3'), Bord('1'), ]), ]), ]
	
	
	etat2.space = [Chem([Bord('0'), Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('2'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('3'), Intern('0'), Intern('0'), ]), ]
	
	etat2.initMat[Chem([Sub('0')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0931163   ), Coef('Var'  , 0.18138     ), Coef('Var'  , 0.269924    ), Coef('Var'  , 0.384799    ), Coef('Var'  , 0.359004    ), Coef('Const', 0.333333    ), ], 
		[Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.217102    ), Coef('Var'  , 0.2425      ), Coef('Var'  , 0.268582    ), Coef('Var'  , 0.383925    ), Coef('Var'  , 0.525159    ), Coef('Const', 0.666667    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.315166    ), Coef('Var'  , 0.222337    ), Coef('Var'  , 0.128473    ), Coef('Var'  , 0.0647446   ), Coef('Var'  , 0.0325591   ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.218578    ), Coef('Var'  , 0.161273    ), Coef('Var'  , 0.104009    ), Coef('Var'  , 0.0520047   ), Coef('Var'  , 0.026004    ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0923935   ), Coef('Var'  , 0.097206    ), Coef('Var'  , 0.102503    ), Coef('Var'  , 0.0510446   ), Coef('Var'  , 0.0254486   ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0636448   ), Coef('Var'  , 0.0953036   ), Coef('Var'  , 0.12651     ), Coef('Var'  , 0.0634824   ), Coef('Var'  , 0.0318252   ), Coef('Const', 0           ), ], ])
	etat2.initMat[Chem([Sub('1')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0257784   ), Coef('Var'  , 0.0516176   ), Coef('Var'  , 0.103409    ), Coef('Var'  , 0.0981535   ), Coef('Var'  , 0.0931163   ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.025277    ), Coef('Var'  , 0.0507588   ), Coef('Var'  , 0.102083    ), Coef('Var'  , 0.159285    ), Coef('Var'  , 0.217102    ), ], 
		[Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0326068   ), Coef('Var'  , 0.064812    ), Coef('Var'  , 0.12854     ), Coef('Var'  , 0.222385    ), Coef('Var'  , 0.315166    ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.666667    ), Coef('Var'  , 0.525907    ), Coef('Var'  , 0.385201    ), Coef('Var'  , 0.270538    ), Coef('Var'  , 0.24451     ), Coef('Var'  , 0.218578    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.333333    ), Coef('Var'  , 0.358611    ), Coef('Var'  , 0.384136    ), Coef('Var'  , 0.268928    ), Coef('Var'  , 0.180369    ), Coef('Var'  , 0.0923935   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0318196   ), Coef('Var'  , 0.0634745   ), Coef('Var'  , 0.126502    ), Coef('Var'  , 0.095298    ), Coef('Var'  , 0.0636448   ), ], ])
	etat2.initMat[Chem([Sub('2')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.218116    ), Coef('Var'  , 0.160653    ), Coef('Var'  , 0.103409    ), Coef('Var'  , 0.0516176   ), Coef('Var'  , 0.0257784   ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0921023   ), Coef('Var'  , 0.0967854   ), Coef('Var'  , 0.102083    ), Coef('Var'  , 0.0507588   ), Coef('Var'  , 0.025277    ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0651658   ), Coef('Var'  , 0.0973851   ), Coef('Var'  , 0.12854     ), Coef('Var'  , 0.064812    ), Coef('Var'  , 0.0326068   ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0935778   ), Coef('Var'  , 0.18201     ), Coef('Var'  , 0.270538    ), Coef('Var'  , 0.385201    ), Coef('Var'  , 0.35924     ), Coef('Const', 0.333333    ), ], 
		[Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.217393    ), Coef('Var'  , 0.242869    ), Coef('Var'  , 0.268928    ), Coef('Var'  , 0.384136    ), Coef('Var'  , 0.525278    ), Coef('Const', 0.666667    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.313645    ), Coef('Var'  , 0.220298    ), Coef('Var'  , 0.126502    ), Coef('Var'  , 0.0634745   ), Coef('Var'  , 0.0318196   ), Coef('Const', 0           ), ], ])
	etat2.initMat[Chem([Sub('3')])] = FMat([
		[Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.666667    ), Coef('Var'  , 0.525671    ), Coef('Var'  , 0.384799    ), Coef('Var'  , 0.269924    ), Coef('Var'  , 0.243879    ), Coef('Var'  , 0.218116    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.333333    ), Coef('Var'  , 0.358492    ), Coef('Var'  , 0.383925    ), Coef('Var'  , 0.268582    ), Coef('Var'  , 0.18        ), Coef('Var'  , 0.0921023   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0325591   ), Coef('Var'  , 0.0647446   ), Coef('Var'  , 0.128473    ), Coef('Var'  , 0.0973374   ), Coef('Var'  , 0.0651658   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.026004    ), Coef('Var'  , 0.0520047   ), Coef('Var'  , 0.104009    ), Coef('Var'  , 0.0987736   ), Coef('Var'  , 0.0935778   ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0254486   ), Coef('Var'  , 0.0510446   ), Coef('Var'  , 0.102503    ), Coef('Var'  , 0.159706    ), Coef('Var'  , 0.217393    ), ], 
		[Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0318252   ), Coef('Var'  , 0.0634824   ), Coef('Var'  , 0.12651     ), Coef('Var'  , 0.220303    ), Coef('Var'  , 0.313645    ), ], ])
	etat2.initMat[Chem([Sub('G')])] = FMat([
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], ])
	
	
	
	etat3.bords   = {Bord('0'): etat5, Bord('1'): etat5, Bord('2'): etat6, Bord('3'): etat5, Bord('4'): etat6, }
	etat3.permuts = {}
	etat3.interns = {Intern('_'): etat3, }
	etat3.subs    = {Sub('0'): etat3, Sub('1'): etat4, Sub('2'): etat4, Sub('3'): etat4, Sub('4'): etat4, Sub('G', True): Etat.etatPoint, }
	
	etat3.buildIntern()
	
	
	etat3.eqs = [
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
	
	
	etat3.prim.elems = [Figure(2, [Chem([Bord('0'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('0'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('0'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('0'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('1'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('1'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('1'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('1'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('2'), Bord('0'), ]), Chem([Bord('3'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('3'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('3'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('3'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('4'), Bord('0'), ]), ])]
	etat3.grid.elems = [
		Figure(1, [Chem([Bord('1'), Bord('0'), ]), Chem([Bord('1'), Intern(''), ]), Chem([Bord('1'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('4'), Bord('0'), ]), Chem([Bord('4'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('2'), Bord('0'), ]), Chem([Bord('2'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('0'), Bord('0'), ]), Chem([Bord('0'), Intern(''), ]), Chem([Bord('0'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('3'), Bord('0'), ]), Chem([Bord('3'), Intern(''), ]), Chem([Bord('3'), Bord('1'), ]), ]), ]
	
	
	etat3.space = [Chem([Bord('4'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('2'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('3'), Intern('0'), Intern('0'), ]), Chem([Bord('4'), Bord('0'), Intern('0'), Intern('0'), ]), ]
	
	etat3.initMat[Chem([Sub('0')])] = FMat([
		[Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0631293   ), Coef('Var'  , 0.134448    ), Coef('Var'  , 0.205818    ), ], 
		[Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0855975   ), Coef('Var'  , 0.192787    ), Coef('Var'  , 0.29983     ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.192763    ), Coef('Var'  , 0.192859    ), Coef('Var'  , 0.192787    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.300088    ), Coef('Var'  , 0.193076    ), Coef('Var'  , 0.0858303   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.20549     ), Coef('Var'  , 0.134098    ), Coef('Var'  , 0.0628648   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0748221   ), Coef('Var'  , 0.056919    ), Coef('Var'  , 0.0392529   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0390711   ), Coef('Var'  , 0.0391418   ), Coef('Var'  , 0.039       ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0390384   ), Coef('Var'  , 0.0566708   ), Coef('Var'  , 0.0746168   ), ], ])
	etat3.initMat[Chem([Sub('1')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.011723    ), Coef('Var'  , 0.0234037   ), Coef('Var'  , 0.0467076   ), Coef('Var'  , 0.0549395   ), Coef('Var'  , 0.0631293   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0105935   ), Coef('Var'  , 0.0210878   ), Coef('Var'  , 0.0419135   ), Coef('Var'  , 0.0638672   ), Coef('Var'  , 0.0855975   ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0194997   ), Coef('Var'  , 0.0389196   ), Coef('Var'  , 0.077623    ), Coef('Var'  , 0.135295    ), Coef('Var'  , 0.192763    ), ], 
		[Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0285376   ), Coef('Var'  , 0.0569622   ), Coef('Var'  , 0.113619    ), Coef('Var'  , 0.206996    ), Coef('Var'  , 0.300088    ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.666667    ), Coef('Var'  , 0.523129    ), Coef('Var'  , 0.379769    ), Coef('Var'  , 0.259997    ), Coef('Var'  , 0.232567    ), Coef('Var'  , 0.20549     ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.333333    ), Coef('Var'  , 0.356741    ), Coef('Var'  , 0.380333    ), Coef('Var'  , 0.261148    ), Coef('Var'  , 0.167786    ), Coef('Var'  , 0.0748221   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0292489   ), Coef('Var'  , 0.058362    ), Coef('Var'  , 0.116364    ), Coef('Var'  , 0.0778742   ), Coef('Var'  , 0.0390711   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0205278   ), Coef('Var'  , 0.0411633   ), Coef('Var'  , 0.0826277   ), Coef('Var'  , 0.0606751   ), Coef('Var'  , 0.0390384   ), ], ])
	etat3.initMat[Chem([Sub('2')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0767492   ), Coef('Var'  , 0.0617315   ), Coef('Var'  , 0.0467076   ), Coef('Var'  , 0.0234037   ), Coef('Var'  , 0.011723    ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0389594   ), Coef('Var'  , 0.0405527   ), Coef('Var'  , 0.0419135   ), Coef('Var'  , 0.0210878   ), Coef('Var'  , 0.0105935   ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0390367   ), Coef('Var'  , 0.0584445   ), Coef('Var'  , 0.077623    ), Coef('Var'  , 0.0389196   ), Coef('Var'  , 0.0194997   ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.039263    ), Coef('Var'  , 0.0766015   ), Coef('Var'  , 0.113619    ), Coef('Var'  , 0.0569622   ), Coef('Var'  , 0.0285376   ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0763884   ), Coef('Var'  , 0.168027    ), Coef('Var'  , 0.259997    ), Coef('Var'  , 0.379769    ), Coef('Var'  , 0.356462    ), Coef('Const', 0.333333    ), ], 
		[Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.210737    ), Coef('Var'  , 0.235742    ), Coef('Var'  , 0.261148    ), Coef('Var'  , 0.380333    ), Coef('Var'  , 0.523408    ), Coef('Const', 0.666667    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.308384    ), Coef('Var'  , 0.212534    ), Coef('Var'  , 0.116364    ), Coef('Var'  , 0.058362    ), Coef('Var'  , 0.0292489   ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.210482    ), Coef('Var'  , 0.146366    ), Coef('Var'  , 0.0826277   ), Coef('Var'  , 0.0411633   ), Coef('Var'  , 0.0205278   ), Coef('Const', 0           ), ], ])
	etat3.initMat[Chem([Sub('3')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.333333    ), Coef('Var'  , 0.356693    ), Coef('Var'  , 0.380149    ), Coef('Var'  , 0.260542    ), Coef('Var'  , 0.16857     ), Coef('Var'  , 0.0767492   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.028366    ), Coef('Var'  , 0.0566765   ), Coef('Var'  , 0.1132      ), Coef('Var'  , 0.0761709   ), Coef('Var'  , 0.0389594   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0195371   ), Coef('Var'  , 0.038975    ), Coef('Var'  , 0.0776858   ), Coef('Var'  , 0.0584869   ), Coef('Var'  , 0.0390367   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0107255   ), Coef('Var'  , 0.0213147   ), Coef('Var'  , 0.0422656   ), Coef('Var'  , 0.0409383   ), Coef('Var'  , 0.039263    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0115931   ), Coef('Var'  , 0.0231735   ), Coef('Var'  , 0.0463326   ), Coef('Var'  , 0.0613033   ), Coef('Var'  , 0.0763884   ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.020663    ), Coef('Var'  , 0.0413903   ), Coef('Var'  , 0.0829658   ), Coef('Var'  , 0.146719    ), Coef('Var'  , 0.210737    ), ], 
		[Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0291354   ), Coef('Var'  , 0.0581937   ), Coef('Var'  , 0.116173    ), Coef('Var'  , 0.212405    ), Coef('Var'  , 0.308384    ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.666667    ), Coef('Var'  , 0.523287    ), Coef('Var'  , 0.380128    ), Coef('Var'  , 0.260835    ), Coef('Var'  , 0.235406    ), Coef('Var'  , 0.210482    ), ], ])
	etat3.initMat[Chem([Sub('4')])] = FMat([
		[Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.205818    ), Coef('Var'  , 0.233093    ), Coef('Var'  , 0.260542    ), Coef('Var'  , 0.380149    ), Coef('Var'  , 0.52336     ), Coef('Const', 0.666667    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.29983     ), Coef('Var'  , 0.206592    ), Coef('Var'  , 0.1132      ), Coef('Var'  , 0.0566765   ), Coef('Var'  , 0.028366    ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.192787    ), Coef('Var'  , 0.135353    ), Coef('Var'  , 0.0776858   ), Coef('Var'  , 0.038975    ), Coef('Var'  , 0.0195371   ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0858303   ), Coef('Var'  , 0.0642088   ), Coef('Var'  , 0.0422656   ), Coef('Var'  , 0.0213147   ), Coef('Var'  , 0.0107255   ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0628648   ), Coef('Var'  , 0.0545711   ), Coef('Var'  , 0.0463326   ), Coef('Var'  , 0.0231735   ), Coef('Var'  , 0.0115931   ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0392529   ), Coef('Var'  , 0.0610034   ), Coef('Var'  , 0.0829658   ), Coef('Var'  , 0.0413903   ), Coef('Var'  , 0.020663    ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.039       ), Coef('Var'  , 0.0776976   ), Coef('Var'  , 0.116173    ), Coef('Var'  , 0.0581937   ), Coef('Var'  , 0.0291354   ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0746168   ), Coef('Var'  , 0.167481    ), Coef('Var'  , 0.260835    ), Coef('Var'  , 0.380128    ), Coef('Var'  , 0.35662     ), Coef('Const', 0.333333    ), ], ])
	etat3.initMat[Chem([Sub('G')])] = FMat([
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], ])
	
	
	
	etat4.bords   = {Bord('0'): etat5, Bord('1'): etat6, Bord('2'): etat5, Bord('3'): etat6, Bord('4'): etat5, Bord('5'): etat6, }
	etat4.permuts = {}
	etat4.interns = {Intern('_'): etat4, }
	etat4.subs    = {Sub('0'): etat4, Sub('1'): etat4, Sub('2'): etat4, Sub('3'): etat4, Sub('4'): etat4, Sub('G', True): Etat.etatPoint, Sub('5'): etat4, }
	
	etat4.buildIntern()
	
	
	etat4.eqs = [
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
	
	
	etat4.prim.elems = [Figure(2, [Chem([Bord('0'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('0'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('0'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('0'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('1'), Bord('0'), ]), Chem([Bord('2'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('2'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('2'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('2'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('3'), Bord('0'), ]), Chem([Bord('4'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('4'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('4'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('4'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('5'), Bord('0'), ]), ])]
	etat4.grid.elems = [
		Figure(1, [Chem([Bord('1'), Bord('0'), ]), Chem([Bord('1'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('2'), Bord('0'), ]), Chem([Bord('2'), Intern(''), ]), Chem([Bord('2'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('3'), Bord('0'), ]), Chem([Bord('3'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('4'), Bord('0'), ]), Chem([Bord('4'), Intern(''), ]), Chem([Bord('4'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('5'), Bord('0'), ]), Chem([Bord('5'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('0'), Bord('0'), ]), Chem([Bord('0'), Intern(''), ]), Chem([Bord('0'), Bord('1'), ]), ]), ]
	
	
	etat4.space = [Chem([Bord('5'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('2'), Intern('0'), Intern('0'), ]), Chem([Bord('2'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('3'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('4'), Intern('0'), Intern('0'), ]), Chem([Bord('4'), Bord('1'), Intern('0'), Intern('0'), ]), ]
	
	etat4.initMat[Chem([Sub('0')])] = FMat([
		[Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0199425   ), Coef('Var'  , 0.0398532   ), Coef('Var'  , 0.0796278   ), Coef('Var'  , 0.144823    ), Coef('Var'  , 0.210036    ), ], 
		[Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0283868   ), Coef('Var'  , 0.0568032   ), Coef('Var'  , 0.113675    ), Coef('Var'  , 0.210228    ), Coef('Var'  , 0.306832    ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.666667    ), Coef('Var'  , 0.523251    ), Coef('Var'  , 0.380017    ), Coef('Var'  , 0.260499    ), Coef('Var'  , 0.234979    ), Coef('Var'  , 0.209793    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.333333    ), Coef('Var'  , 0.356627    ), Coef('Var'  , 0.380091    ), Coef('Var'  , 0.260614    ), Coef('Var'  , 0.166982    ), Coef('Var'  , 0.0736173   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0285489   ), Coef('Var'  , 0.0570711   ), Coef('Var'  , 0.114063    ), Coef('Var'  , 0.0743672   ), Coef('Var'  , 0.0345388   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0200223   ), Coef('Var'  , 0.0399728   ), Coef('Var'  , 0.0797668   ), Coef('Var'  , 0.054281    ), Coef('Var'  , 0.0286321   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.00844209  ), Coef('Var'  , 0.0168659   ), Coef('Var'  , 0.0337024   ), Coef('Var'  , 0.0309105   ), Coef('Var'  , 0.0281275   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.00649424  ), Coef('Var'  , 0.0127253   ), Coef('Var'  , 0.0247506   ), Coef('Var'  , 0.0304612   ), Coef('Var'  , 0.0355308   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0082858   ), Coef('Var'  , 0.0166009   ), Coef('Var'  , 0.0333002   ), Coef('Var'  , 0.0529685   ), Coef('Var'  , 0.0728934   ), ], ])
	etat4.initMat[Chem([Sub('1')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0285847   ), Coef('Var'  , 0.0541556   ), Coef('Var'  , 0.0796278   ), Coef('Var'  , 0.0398532   ), Coef('Var'  , 0.0199425   ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.034348    ), Coef('Var'  , 0.0740252   ), Coef('Var'  , 0.113675    ), Coef('Var'  , 0.0568032   ), Coef('Var'  , 0.0283868   ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0735255   ), Coef('Var'  , 0.166861    ), Coef('Var'  , 0.260499    ), Coef('Var'  , 0.380017    ), Coef('Var'  , 0.356584    ), Coef('Const', 0.333333    ), ], 
		[Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.20988     ), Coef('Var'  , 0.235097    ), Coef('Var'  , 0.260614    ), Coef('Var'  , 0.380091    ), Coef('Var'  , 0.523294    ), Coef('Const', 0.666667    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.307147    ), Coef('Var'  , 0.210652    ), Coef('Var'  , 0.114063    ), Coef('Var'  , 0.0570711   ), Coef('Var'  , 0.0285489   ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.210046    ), Coef('Var'  , 0.144924    ), Coef('Var'  , 0.0797668   ), Coef('Var'  , 0.0399728   ), Coef('Var'  , 0.0200223   ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0731728   ), Coef('Var'  , 0.053368    ), Coef('Var'  , 0.0337024   ), Coef('Var'  , 0.0168659   ), Coef('Var'  , 0.00844209  ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0354804   ), Coef('Var'  , 0.030428    ), Coef('Var'  , 0.0247506   ), Coef('Var'  , 0.0127253   ), Coef('Var'  , 0.00649424  ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.027815    ), Coef('Var'  , 0.0304892   ), Coef('Var'  , 0.0333002   ), Coef('Var'  , 0.0166009   ), Coef('Var'  , 0.0082858   ), Coef('Const', 0           ), ], ])
	etat4.initMat[Chem([Sub('2')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.00864235  ), Coef('Var'  , 0.0172222   ), Coef('Var'  , 0.0342886   ), Coef('Var'  , 0.0315044   ), Coef('Var'  , 0.0285847   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.00596134  ), Coef('Var'  , 0.0118064   ), Coef('Var'  , 0.0233147   ), Coef('Var'  , 0.0289323   ), Coef('Var'  , 0.034348    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.00860816  ), Coef('Var'  , 0.0171526   ), Coef('Var'  , 0.0341513   ), Coef('Var'  , 0.0538343   ), Coef('Var'  , 0.0735255   ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0199196   ), Coef('Var'  , 0.0398094   ), Coef('Var'  , 0.0795479   ), Coef('Var'  , 0.144683    ), Coef('Var'  , 0.20988     ), ], 
		[Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0285986   ), Coef('Var'  , 0.0571465   ), Coef('Var'  , 0.114153    ), Coef('Var'  , 0.210712    ), Coef('Var'  , 0.307147    ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.666667    ), Coef('Var'  , 0.523357    ), Coef('Var'  , 0.380195    ), Coef('Var'  , 0.260762    ), Coef('Var'  , 0.23529     ), Coef('Var'  , 0.210046    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.333333    ), Coef('Var'  , 0.356397    ), Coef('Var'  , 0.379699    ), Coef('Var'  , 0.260013    ), Coef('Var'  , 0.16637     ), Coef('Var'  , 0.0731728   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0289863   ), Coef('Var'  , 0.057823    ), Coef('Var'  , 0.115232    ), Coef('Var'  , 0.0756006   ), Coef('Var'  , 0.0354804   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0195293   ), Coef('Var'  , 0.039146    ), Coef('Var'  , 0.0785366   ), Coef('Var'  , 0.0530726   ), Coef('Var'  , 0.027815    ), ], ])
	etat4.initMat[Chem([Sub('3')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0737355   ), Coef('Var'  , 0.0540314   ), Coef('Var'  , 0.0342886   ), Coef('Var'  , 0.0172222   ), Coef('Var'  , 0.00864235  ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0344068   ), Coef('Var'  , 0.0289711   ), Coef('Var'  , 0.0233147   ), Coef('Var'  , 0.0118064   ), Coef('Var'  , 0.00596134  ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0284833   ), Coef('Var'  , 0.0313788   ), Coef('Var'  , 0.0341513   ), Coef('Var'  , 0.0171526   ), Coef('Var'  , 0.00860816  ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0285764   ), Coef('Var'  , 0.0541136   ), Coef('Var'  , 0.0795479   ), Coef('Var'  , 0.0398094   ), Coef('Var'  , 0.0199196   ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0345885   ), Coef('Var'  , 0.0744596   ), Coef('Var'  , 0.114153    ), Coef('Var'  , 0.0571465   ), Coef('Var'  , 0.0285986   ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.073634    ), Coef('Var'  , 0.167077    ), Coef('Var'  , 0.260762    ), Coef('Var'  , 0.380195    ), Coef('Var'  , 0.35669     ), Coef('Const', 0.333333    ), ], 
		[Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.209416    ), Coef('Var'  , 0.234472    ), Coef('Var'  , 0.260013    ), Coef('Var'  , 0.379699    ), Coef('Var'  , 0.523064    ), Coef('Const', 0.666667    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.308023    ), Coef('Var'  , 0.211842    ), Coef('Var'  , 0.115232    ), Coef('Var'  , 0.057823    ), Coef('Var'  , 0.0289863   ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.209137    ), Coef('Var'  , 0.143655    ), Coef('Var'  , 0.0785366   ), Coef('Var'  , 0.039146    ), Coef('Var'  , 0.0195293   ), Coef('Const', 0           ), ], ])
	etat4.initMat[Chem([Sub('4')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.333333    ), Coef('Var'  , 0.356759    ), Coef('Var'  , 0.380301    ), Coef('Var'  , 0.260894    ), Coef('Var'  , 0.167228    ), Coef('Var'  , 0.0737355   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0284456   ), Coef('Var'  , 0.0568923   ), Coef('Var'  , 0.113782    ), Coef('Var'  , 0.0741344   ), Coef('Var'  , 0.0344068   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0198753   ), Coef('Var'  , 0.0397335   ), Coef('Var'  , 0.0794304   ), Coef('Var'  , 0.0539904   ), Coef('Var'  , 0.0284833   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.00865688  ), Coef('Var'  , 0.0172352   ), Coef('Var'  , 0.0342767   ), Coef('Var'  , 0.0315073   ), Coef('Var'  , 0.0285764   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.00599     ), Coef('Var'  , 0.011872    ), Coef('Var'  , 0.0234601   ), Coef('Var'  , 0.0291473   ), Coef('Var'  , 0.0345885   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.00860998  ), Coef('Var'  , 0.0171717   ), Coef('Var'  , 0.0342239   ), Coef('Var'  , 0.0539243   ), Coef('Var'  , 0.073634    ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0196854   ), Coef('Var'  , 0.0394107   ), Coef('Var'  , 0.0789383   ), Coef('Var'  , 0.144053    ), Coef('Var'  , 0.209416    ), ], 
		[Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0290365   ), Coef('Var'  , 0.0578993   ), Coef('Var'  , 0.115324    ), Coef('Var'  , 0.211903    ), Coef('Var'  , 0.308023    ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.666667    ), Coef('Var'  , 0.522941    ), Coef('Var'  , 0.379484    ), Coef('Var'  , 0.259671    ), Coef('Var'  , 0.234113    ), Coef('Var'  , 0.209137    ), ], ])
	etat4.initMat[Chem([Sub('G')])] = FMat([
		[Coef('Const', 0.111111    )], 
		[Coef('Const', 0.111111    )], 
		[Coef('Const', 0.111111    )], 
		[Coef('Const', 0.111111    )], 
		[Coef('Const', 0.111111    )], 
		[Coef('Const', 0.111111    )], 
		[Coef('Const', 0.111111    )], 
		[Coef('Const', 0.111111    )], 
		[Coef('Const', 0.111111    )], ])
	etat4.initMat[Chem([Sub('5')])] = FMat([
		[Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.210036    ), Coef('Var'  , 0.235368    ), Coef('Var'  , 0.260894    ), Coef('Var'  , 0.380301    ), Coef('Var'  , 0.523426    ), Coef('Const', 0.666667    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.306832    ), Coef('Var'  , 0.210299    ), Coef('Var'  , 0.113782    ), Coef('Var'  , 0.0568923   ), Coef('Var'  , 0.0284456   ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.209793    ), Coef('Var'  , 0.144564    ), Coef('Var'  , 0.0794304   ), Coef('Var'  , 0.0397335   ), Coef('Var'  , 0.0198753   ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0736173   ), Coef('Var'  , 0.0539619   ), Coef('Var'  , 0.0342767   ), Coef('Var'  , 0.0172352   ), Coef('Var'  , 0.00865688  ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0345388   ), Coef('Var'  , 0.0291145   ), Coef('Var'  , 0.0234601   ), Coef('Var'  , 0.011872    ), Coef('Var'  , 0.00599     ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0286321   ), Coef('Var'  , 0.0314954   ), Coef('Var'  , 0.0342239   ), Coef('Var'  , 0.0171717   ), Coef('Var'  , 0.00860998  ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0281275   ), Coef('Var'  , 0.0534935   ), Coef('Var'  , 0.0789383   ), Coef('Var'  , 0.0394107   ), Coef('Var'  , 0.0196854   ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0355308   ), Coef('Var'  , 0.0756942   ), Coef('Var'  , 0.115324    ), Coef('Var'  , 0.0578993   ), Coef('Var'  , 0.0290365   ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0728934   ), Coef('Var'  , 0.16601     ), Coef('Var'  , 0.259671    ), Coef('Var'  , 0.379484    ), Coef('Var'  , 0.356274    ), Coef('Const', 0.333333    ), ], ])
	
	
	
	etat5.bords   = {Bord('0'): etat7, Bord('1'): etat7, }
	etat5.permuts = {Permut('0'): etat5, }
	etat5.interns = {Intern('_'): etat5, }
	etat5.subs    = {Sub('0'): etat5, Sub('1'): etat5, Sub('G', True): Etat.etatPoint, }
	
	etat5.buildIntern()
	etat5.fm_[Permut('0')] = PMat(3, [2, 1, 0, ])
	
	
	etat5.eqs = [
		(Chem([Permut('0'), Bord('0'), ])	,	Chem([Bord('1')])),
		(Chem([Permut('0'), Bord('1'), ])	,	Chem([Bord('0')])),
		(Chem([Permut('0'), Intern(''), ])	,	Chem([Intern('')])),
		(Chem([Permut('0'), Sub('0'), ])	,	Chem([Sub('1'), Permut('0'), ])),
		(Chem([Permut('0'), Sub('1'), ])	,	Chem([Sub('0'), Permut('0'), ])),
		]
	
	
	etat5.prim.elems = [Figure(1, [Chem([Bord('0')]), Chem([Bord('1')]), ])]
	etat5.grid.elems = [Figure(1, [Chem([Bord('0')]), Chem([Intern('')]), Chem([Bord('1')]), ])]
	
	
	etat5.space = [Chem([Bord('0'), Intern('0'), Intern('0'), ]), Chem([Intern('0'), Intern('0'), ]), Chem([Bord('1'), Intern('0'), Intern('0'), ]), ]
	
	etat5.initMat[Chem([Sub('0')])] = FMat([
		[Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), ], ])
	etat5.initMat[Chem([Sub('1')])] = FMat([
		[Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), ], ])
	etat5.initMat[Chem([Sub('G')])] = FMat([
		[Coef('Const', 0           )], 
		[Coef('Const', 1           )], 
		[Coef('Const', 0           )], ])
	
	
	
	etat6.bords   = {Bord('0'): etat7, Bord('1'): etat7, }
	etat6.permuts = {Permut('0'): etat6, }
	etat6.interns = {Intern('_'): etat6, }
	etat6.subs    = {Sub('0'): etat6, Sub('1'): etat6, Sub('G', True): Etat.etatPoint, }
	
	etat6.buildIntern()
	etat6.fm_[Permut('0')] = PMat(2, [1, 0, ])
	
	
	etat6.eqs = [
		(Chem([Permut('0'), Bord('0'), ])	,	Chem([Bord('1')])),
		(Chem([Permut('0'), Bord('1'), ])	,	Chem([Bord('0')])),
		(Chem([Permut('0'), Sub('0'), ])	,	Chem([Sub('1'), Permut('0'), ])),
		(Chem([Permut('0'), Sub('1'), ])	,	Chem([Sub('0'), Permut('0'), ])),
		(Chem([Bord('0'), Sub('0'), ])	,	Chem([Sub('0'), Bord('0'), ])),
		(Chem([Bord('1'), Sub('0'), ])	,	Chem([Sub('1'), Bord('1'), ])),
		]
	
	
	etat6.prim.elems = []
	etat6.grid.elems = [Figure(1, [Chem([Bord('0')]), Chem([Bord('1')]), ])]
	
	
	etat6.space = [Chem([Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Intern('0'), Intern('0'), ]), ]
	
	etat6.initMat[Chem([Sub('0')])] = FMat([
		[Coef('Const', 1           ), Coef('Const', 0.666667    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.333333    ), ], ])
	etat6.initMat[Chem([Sub('1')])] = FMat([
		[Coef('Const', 0.333333    ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.666667    ), Coef('Const', 1           ), ], ])
	etat6.initMat[Chem([Sub('G')])] = FMat([
		[Coef('Const', 0.5         )], 
		[Coef('Const', 0.5         )], ])
	
	
	
	etat7.bords   = {}
	etat7.permuts = {}
	etat7.interns = {Intern('_'): etat7, }
	etat7.subs    = {Sub('0'): etat7, Sub('G', True): Etat.etatPoint, }
	
	etat7.buildIntern()
	
	
	etat7.eqs = [
		]
	
	
	etat7.prim.elems = []
	etat7.grid.elems = []
	
	
	etat7.space = [Chem([Intern('0'), Intern('0'), ])]
	
	etat7.initMat[Chem([Sub('0')])] = FMat([[Coef('Const', 1           )]])
	etat7.initMat[Chem([Sub('G')])] = FMat([[Coef('Const', 1           )]])
	
	
	
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
