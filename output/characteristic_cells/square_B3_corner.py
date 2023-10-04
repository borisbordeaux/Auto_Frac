# -*- coding: utf-8 -*-

# Automatically generated, from file : square_B3_full_B3_corner.py, function : modele()

from __future__ import division
import sys
if './../../../../../../python' not in sys.path:
	sys.path.append('./../../../../../../python')
from etat import *

def modele():
	
	etat0 = EtatInit()
	etat1 = Etat('Cell_0',0)
	etat2 = Etat('B3',1)
	etat3 = Etat('s',1)
	
	
	etat0.subs   = {Sub('0'): etat1, }
	
	etat0.eqs = [
		]
	
	
	etat0.space = []
	
	etat0.initMat[Chem([Sub('0')])] = FMat([
		[Coef('Var'  , 1.48256     ), Coef('Var'  , 0.53303     ), Coef('Var'  ,-0.446598    ), Coef('Var'  ,-1.00592     ), Coef('Var'  ,-1.54494     ), Coef('Var'  ,-0.6041      ), Coef('Var'  , 0.384214    ), Coef('Var'  , 0.951253    ), ], 
		[Coef('Var'  , 0.413301    ), Coef('Var'  , 0.95262     ), Coef('Var'  , 1.5117      ), Coef('Var'  , 0.54533     ), Coef('Var'  ,-0.417412    ), Coef('Var'  ,-0.95262     ), Coef('Var'  ,-1.51581     ), Coef('Var'  ,-0.526196    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), ], ])
	
	
	
	etat1.bords   = {Bord('0'): etat2, Bord('1'): etat2, Bord('2'): etat2, Bord('3'): etat2, }
	etat1.permuts = {}
	etat1.interns = {Intern('_'): etat1, }
	etat1.subs    = {Sub('0'): etat1, Sub('G', True): Etat.etatPoint, Sub('1'): etat1, Sub('2'): etat1, Sub('3'): etat1, Sub('4'): etat1, Sub('5'): etat1, Sub('6'): etat1, Sub('7'): etat1, Sub('8'): etat1, Sub('9'): etat1, Sub('10'): etat1, Sub('11'): etat1, }
	
	etat1.buildIntern()
	
	
	etat1.eqs = [
		(Chem([Bord('0'), Sub('0'), ])	,	Chem([Sub('0'), Bord('0'), ])),
		(Chem([Bord('0'), Sub('1'), ])	,	Chem([Sub('1'), Bord('0'), ])),
		(Chem([Bord('0'), Sub('2'), ])	,	Chem([Sub('2'), Bord('0'), ])),
		(Chem([Bord('1'), Sub('0'), ])	,	Chem([Sub('3'), Bord('0'), ])),
		(Chem([Bord('1'), Sub('1'), ])	,	Chem([Sub('4'), Bord('0'), ])),
		(Chem([Bord('1'), Sub('2'), ])	,	Chem([Sub('5'), Bord('0'), ])),
		(Chem([Bord('2'), Sub('0'), ])	,	Chem([Sub('6'), Bord('0'), ])),
		(Chem([Bord('2'), Sub('1'), ])	,	Chem([Sub('7'), Bord('0'), ])),
		(Chem([Bord('2'), Sub('2'), ])	,	Chem([Sub('8'), Bord('0'), ])),
		(Chem([Bord('3'), Sub('0'), ])	,	Chem([Sub('9'), Bord('0'), ])),
		(Chem([Bord('3'), Sub('1'), ])	,	Chem([Sub('10'), Bord('0'), ])),
		(Chem([Bord('3'), Sub('2'), ])	,	Chem([Sub('11'), Bord('0'), ])),
		(Chem([Sub('0'), Bord('1'), Permut('0'), ])	,	Chem([Sub('1'), Bord('3'), ])),
		(Chem([Sub('1'), Bord('1'), Permut('0'), ])	,	Chem([Sub('2'), Bord('3'), ])),
		(Chem([Sub('2'), Bord('1'), Permut('0'), ])	,	Chem([Sub('3'), Bord('3'), ])),
		(Chem([Sub('3'), Bord('1'), Permut('0'), ])	,	Chem([Sub('4'), Bord('3'), ])),
		(Chem([Sub('4'), Bord('1'), Permut('0'), ])	,	Chem([Sub('5'), Bord('3'), ])),
		(Chem([Sub('5'), Bord('1'), Permut('0'), ])	,	Chem([Sub('6'), Bord('3'), ])),
		(Chem([Sub('6'), Bord('1'), Permut('0'), ])	,	Chem([Sub('7'), Bord('3'), ])),
		(Chem([Sub('7'), Bord('1'), Permut('0'), ])	,	Chem([Sub('8'), Bord('3'), ])),
		(Chem([Sub('8'), Bord('1'), Permut('0'), ])	,	Chem([Sub('9'), Bord('3'), ])),
		(Chem([Sub('9'), Bord('1'), Permut('0'), ])	,	Chem([Sub('10'), Bord('3'), ])),
		(Chem([Sub('10'), Bord('1'), Permut('0'), ])	,	Chem([Sub('11'), Bord('3'), ])),
		(Chem([Sub('11'), Bord('1'), Permut('0'), ])	,	Chem([Sub('0'), Bord('3'), ])),
		(Chem([Bord('0'), Bord('1'), ])	,	Chem([Bord('1'), Bord('0'), ])),
		(Chem([Bord('1'), Bord('1'), ])	,	Chem([Bord('2'), Bord('0'), ])),
		(Chem([Bord('2'), Bord('1'), ])	,	Chem([Bord('3'), Bord('0'), ])),
		(Chem([Bord('3'), Bord('1'), ])	,	Chem([Bord('0'), Bord('0'), ])),
		]
	
	
	etat1.prim.elems = [Figure(2, [Chem([Bord('0'), Sub('0'), Bord('0'), ]), Chem([Bord('0'), Sub('1'), Bord('0'), ]), Chem([Bord('0'), Sub('2'), Bord('0'), ]), Chem([Bord('1'), Sub('0'), Bord('0'), ]), Chem([Bord('1'), Sub('1'), Bord('0'), ]), Chem([Bord('1'), Sub('2'), Bord('0'), ]), Chem([Bord('2'), Sub('0'), Bord('0'), ]), Chem([Bord('2'), Sub('1'), Bord('0'), ]), Chem([Bord('2'), Sub('2'), Bord('0'), ]), Chem([Bord('3'), Sub('0'), Bord('0'), ]), Chem([Bord('3'), Sub('1'), Bord('0'), ]), Chem([Bord('3'), Sub('2'), Bord('0'), ]), ])]
	etat1.grid.elems = [
		Figure(1, [Chem([Bord('1'), Bord('0'), ]), Chem([Bord('1'), Intern(''), ]), Chem([Bord('1'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('2'), Bord('0'), ]), Chem([Bord('2'), Intern(''), ]), Chem([Bord('2'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('0'), Bord('0'), ]), Chem([Bord('0'), Intern(''), ]), Chem([Bord('0'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('3'), Bord('0'), ]), Chem([Bord('3'), Intern(''), ]), Chem([Bord('3'), Bord('1'), ]), ]), ]
	
	
	etat1.space = [Chem([Bord('0'), Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('2'), Intern('0'), Intern('0'), ]), Chem([Bord('2'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('3'), Intern('0'), Intern('0'), ]), ]
	
	etat1.initMat[Chem([Sub('0')])] = FMat([
		[Coef('Const', 1           ), Coef('Const', 0.666667    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.35101     ), Coef('Var'  , 0.231306    ), Coef('Var'  , 0.251033    ), Coef('Var'  , 0.250358    ), Coef('Var'  , 0.349858    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.333333    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.344856    ), Coef('Var'  , 0.206435    ), Coef('Var'  , 0.204987    ), Coef('Var'  , 0.190664    ), Coef('Var'  , 0.240686    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.111111    ), Coef('Var'  , 0.134111    ), Coef('Var'  , 0.180916    ), Coef('Var'  , 0.157593    ), Coef('Var'  , 0.129141    ), Coef('Var'  , 0.12816     ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0402281   ), Coef('Var'  , 0.0989695   ), Coef('Var'  , 0.0773417   ), Coef('Var'  , 0.0635018   ), Coef('Var'  , 0.0125618   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0200935   ), Coef('Var'  , 0.0183493   ), Coef('Var'  ,-0.00129791  ), Coef('Var'  ,-0.000501677 ), Coef('Var'  ,-0.100097    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0212498   ), Coef('Var'  , 0.0429491   ), Coef('Var'  , 0.0442917   ), Coef('Var'  , 0.0586263   ), Coef('Var'  , 0.0080428   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0316945   ), Coef('Var'  , 0.0687389   ), Coef('Var'  , 0.0921413   ), Coef('Var'  , 0.120715    ), Coef('Var'  , 0.1216      ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0567572   ), Coef('Var'  , 0.152336    ), Coef('Var'  , 0.17391     ), Coef('Var'  , 0.187495    ), Coef('Var'  , 0.239189    ), ], ])
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
		[Coef('Const', 0.444444    ), Coef('Const', 0.222222    ), Coef('Const', 0.111111    ), Coef('Var'  , 0.133921    ), Coef('Var'  , 0.180141    ), Coef('Var'  , 0.20811     ), Coef('Var'  , 0.231306    ), Coef('Var'  , 0.35101     ), ], 
		[Coef('Const', 0.444444    ), Coef('Const', 0.555556    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.342868    ), Coef('Var'  , 0.202483    ), Coef('Var'  , 0.20819     ), Coef('Var'  , 0.206435    ), Coef('Var'  , 0.344856    ), ], 
		[Coef('Const', 0.111111    ), Coef('Const', 0.222222    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.348544    ), Coef('Var'  , 0.225724    ), Coef('Var'  , 0.208447    ), Coef('Var'  , 0.180916    ), Coef('Var'  , 0.134111    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0544663   ), Coef('Var'  , 0.147247    ), Coef('Var'  , 0.124454    ), Coef('Var'  , 0.0989695   ), Coef('Var'  , 0.0402281   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0334241   ), Coef('Var'  , 0.0693752   ), Coef('Var'  , 0.041452    ), Coef('Var'  , 0.0183493   ), Coef('Var'  , 0.0200935   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0238286   ), Coef('Var'  , 0.0471785   ), Coef('Var'  , 0.0413184   ), Coef('Var'  , 0.0429491   ), Coef('Var'  , 0.0212498   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0213529   ), Coef('Var'  , 0.023792    ), Coef('Var'  , 0.0411141   ), Coef('Var'  , 0.0687389   ), Coef('Var'  , 0.0316945   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0415938   ), Coef('Var'  , 0.104059    ), Coef('Var'  , 0.126915    ), Coef('Var'  , 0.152336    ), Coef('Var'  , 0.0567572   ), ], ])
	etat1.initMat[Chem([Sub('2')])] = FMat([
		[Coef('Const', 0.111111    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.123515    ), Coef('Var'  , 0.122168    ), Coef('Var'  , 0.150817    ), Coef('Var'  , 0.180141    ), Coef('Var'  , 0.133921    ), ], 
		[Coef('Const', 0.444444    ), Coef('Const', 0.333333    ), Coef('Const', 0           ), Coef('Var'  , 0.234851    ), Coef('Var'  , 0.182583    ), Coef('Var'  , 0.197319    ), Coef('Var'  , 0.202483    ), Coef('Var'  , 0.342868    ), ], 
		[Coef('Const', 0.444444    ), Coef('Const', 0.666667    ), Coef('Const', 1           ), Coef('Var'  , 0.350085    ), Coef('Var'  , 0.245109    ), Coef('Var'  , 0.245505    ), Coef('Var'  , 0.225724    ), Coef('Var'  , 0.348544    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.237948    ), Coef('Var'  , 0.186305    ), Coef('Var'  , 0.171976    ), Coef('Var'  , 0.147247    ), Coef('Var'  , 0.0544663   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.125529    ), Coef('Var'  , 0.127324    ), Coef('Var'  , 0.0986449   ), Coef('Var'  , 0.0693752   ), Coef('Var'  , 0.0334241   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0150977   ), Coef('Var'  , 0.067401    ), Coef('Var'  , 0.0525034   ), Coef('Var'  , 0.0471785   ), Coef('Var'  , 0.0238286   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  ,-0.101041    ), Coef('Var'  , 0.00438276  ), Coef('Var'  , 0.00395666  ), Coef('Var'  , 0.023792    ), Coef('Var'  , 0.0213529   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0140154   ), Coef('Var'  , 0.0647269   ), Coef('Var'  , 0.0792787   ), Coef('Var'  , 0.104059    ), Coef('Var'  , 0.0415938   ), ], ])
	etat1.initMat[Chem([Sub('3')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0300359   ), Coef('Var'  , 0.0639504   ), Coef('Var'  , 0.0901249   ), Coef('Var'  , 0.122168    ), Coef('Var'  , 0.123515    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0510973   ), Coef('Var'  , 0.140885    ), Coef('Var'  , 0.164701    ), Coef('Var'  , 0.182583    ), Coef('Var'  , 0.234851    ), ], 
		[Coef('Const', 1           ), Coef('Const', 0.666667    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.344999    ), Coef('Var'  , 0.220388    ), Coef('Var'  , 0.241816    ), Coef('Var'  , 0.245109    ), Coef('Var'  , 0.350085    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.333333    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.342401    ), Coef('Var'  , 0.203502    ), Coef('Var'  , 0.200911    ), Coef('Var'  , 0.186305    ), Coef('Var'  , 0.237948    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.111111    ), Coef('Var'  , 0.137458    ), Coef('Var'  , 0.185705    ), Coef('Var'  , 0.159413    ), Coef('Var'  , 0.127324    ), Coef('Var'  , 0.125529    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0477605   ), Coef('Var'  , 0.109434    ), Coef('Var'  , 0.0854655   ), Coef('Var'  , 0.067401    ), Coef('Var'  , 0.0150977   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0242749   ), Coef('Var'  , 0.0292677   ), Coef('Var'  , 0.00772187  ), Coef('Var'  , 0.00438276  ), Coef('Var'  ,-0.101041    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0219726   ), Coef('Var'  , 0.0468671   ), Coef('Var'  , 0.0498463   ), Coef('Var'  , 0.0647269   ), Coef('Var'  , 0.0140154   ), ], ])
	etat1.initMat[Chem([Sub('4')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  ,-0.0404831   ), Coef('Var'  , 0.0174075   ), Coef('Var'  , 0.0358072   ), Coef('Var'  , 0.0639504   ), Coef('Var'  , 0.0300359   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0804834   ), Coef('Var'  , 0.093888    ), Coef('Var'  , 0.11654     ), Coef('Var'  , 0.140885    ), Coef('Var'  , 0.0510973   ), ], 
		[Coef('Const', 0.444444    ), Coef('Const', 0.222222    ), Coef('Const', 0.111111    ), Coef('Var'  , 0.205341    ), Coef('Var'  , 0.172823    ), Coef('Var'  , 0.199915    ), Coef('Var'  , 0.220388    ), Coef('Var'  , 0.344999    ), ], 
		[Coef('Const', 0.444444    ), Coef('Const', 0.555556    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.248954    ), Coef('Var'  , 0.203392    ), Coef('Var'  , 0.207567    ), Coef('Var'  , 0.203502    ), Coef('Var'  , 0.342401    ), ], 
		[Coef('Const', 0.111111    ), Coef('Const', 0.222222    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.290307    ), Coef('Var'  , 0.232497    ), Coef('Var'  , 0.213964    ), Coef('Var'  , 0.185705    ), Coef('Var'  , 0.137458    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.170431    ), Coef('Var'  , 0.156707    ), Coef('Var'  , 0.133944    ), Coef('Var'  , 0.109434    ), Coef('Var'  , 0.0477605   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0444838   ), Coef('Var'  , 0.0770825   ), Coef('Var'  , 0.0498565   ), Coef('Var'  , 0.0292677   ), Coef('Var'  , 0.0242749   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.00048232  ), Coef('Var'  , 0.0462031   ), Coef('Var'  , 0.042407    ), Coef('Var'  , 0.0468671   ), Coef('Var'  , 0.0219726   ), ], ])
	etat1.initMat[Chem([Sub('5')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  ,-0.0936312   ), Coef('Var'  , 0.000141213 ), Coef('Var'  , 0.00165104  ), Coef('Var'  , 0.0174075   ), Coef('Var'  ,-0.0404831   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0131123   ), Coef('Var'  , 0.0599692   ), Coef('Var'  , 0.0742537   ), Coef('Var'  , 0.093888    ), Coef('Var'  , 0.0804834   ), ], 
		[Coef('Const', 0.111111    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.123138    ), Coef('Var'  , 0.121631    ), Coef('Var'  , 0.149141    ), Coef('Var'  , 0.172823    ), Coef('Var'  , 0.205341    ), ], 
		[Coef('Const', 0.444444    ), Coef('Const', 0.333333    ), Coef('Const', 0           ), Coef('Var'  , 0.234928    ), Coef('Var'  , 0.18663     ), Coef('Var'  , 0.199577    ), Coef('Var'  , 0.203392    ), Coef('Var'  , 0.248954    ), ], 
		[Coef('Const', 0.444444    ), Coef('Const', 0.666667    ), Coef('Const', 1           ), Coef('Var'  , 0.343859    ), Coef('Var'  , 0.249998    ), Coef('Var'  , 0.24837     ), Coef('Var'  , 0.232497    ), Coef('Var'  , 0.290307    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.238124    ), Coef('Var'  , 0.190737    ), Coef('Var'  , 0.176437    ), Coef('Var'  , 0.156707    ), Coef('Var'  , 0.170431    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.127091    ), Coef('Var'  , 0.128509    ), Coef('Var'  , 0.10088     ), Coef('Var'  , 0.0770825   ), Coef('Var'  , 0.0444838   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0133802   ), Coef('Var'  , 0.0623836   ), Coef('Var'  , 0.0496894   ), Coef('Var'  , 0.0462031   ), Coef('Var'  , 0.00048232  ), ], ])
	etat1.initMat[Chem([Sub('6')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0216469   ), Coef('Var'  , 0.0206619   ), Coef('Var'  , 0.00117843  ), Coef('Var'  , 0.000141213 ), Coef('Var'  ,-0.0936312   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0232363   ), Coef('Var'  , 0.0451892   ), Coef('Var'  , 0.0470256   ), Coef('Var'  , 0.0599692   ), Coef('Var'  , 0.0131123   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0325105   ), Coef('Var'  , 0.0703572   ), Coef('Var'  , 0.0942196   ), Coef('Var'  , 0.121631    ), Coef('Var'  , 0.123138    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0564959   ), Coef('Var'  , 0.150667    ), Coef('Var'  , 0.172441    ), Coef('Var'  , 0.18663     ), Coef('Var'  , 0.234928    ), ], 
		[Coef('Const', 1           ), Coef('Const', 0.666667    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.349672    ), Coef('Var'  , 0.229675    ), Coef('Var'  , 0.249077    ), Coef('Var'  , 0.249998    ), Coef('Var'  , 0.343859    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.333333    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.342376    ), Coef('Var'  , 0.205415    ), Coef('Var'  , 0.203682    ), Coef('Var'  , 0.190737    ), Coef('Var'  , 0.238124    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.111111    ), Coef('Var'  , 0.133245    ), Coef('Var'  , 0.179981    ), Coef('Var'  , 0.156036    ), Coef('Var'  , 0.128509    ), Coef('Var'  , 0.127091    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0408176   ), Coef('Var'  , 0.0980539   ), Coef('Var'  , 0.0763405   ), Coef('Var'  , 0.0623836   ), Coef('Var'  , 0.0133802   ), ], ])
	etat1.initMat[Chem([Sub('7')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0334303   ), Coef('Var'  , 0.0698712   ), Coef('Var'  , 0.042565    ), Coef('Var'  , 0.0206619   ), Coef('Var'  , 0.0216469   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0251605   ), Coef('Var'  , 0.0486409   ), Coef('Var'  , 0.0438509   ), Coef('Var'  , 0.0451892   ), Coef('Var'  , 0.0232363   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0228112   ), Coef('Var'  , 0.0265512   ), Coef('Var'  , 0.0450092   ), Coef('Var'  , 0.0703572   ), Coef('Var'  , 0.0325105   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0432226   ), Coef('Var'  , 0.10388     ), Coef('Var'  , 0.126926    ), Coef('Var'  , 0.150667    ), Coef('Var'  , 0.0564959   ), ], 
		[Coef('Const', 0.444444    ), Coef('Const', 0.222222    ), Coef('Const', 0.111111    ), Coef('Var'  , 0.134084    ), Coef('Var'  , 0.180603    ), Coef('Var'  , 0.207858    ), Coef('Var'  , 0.229675    ), Coef('Var'  , 0.349672    ), ], 
		[Coef('Const', 0.444444    ), Coef('Const', 0.555556    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.340492    ), Coef('Var'  , 0.201697    ), Coef('Var'  , 0.206636    ), Coef('Var'  , 0.205415    ), Coef('Var'  , 0.342376    ), ], 
		[Coef('Const', 0.111111    ), Coef('Const', 0.222222    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.34684     ), Coef('Var'  , 0.223923    ), Coef('Var'  , 0.205414    ), Coef('Var'  , 0.179981    ), Coef('Var'  , 0.133245    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0539586   ), Coef('Var'  , 0.144834    ), Coef('Var'  , 0.12174     ), Coef('Var'  , 0.0980539   ), Coef('Var'  , 0.0408176   ), ], ])
	etat1.initMat[Chem([Sub('8')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.125514    ), Coef('Var'  , 0.12502     ), Coef('Var'  , 0.0971466   ), Coef('Var'  , 0.0698712   ), Coef('Var'  , 0.0334303   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0173269   ), Coef('Var'  , 0.066824    ), Coef('Var'  , 0.0527233   ), Coef('Var'  , 0.0486409   ), Coef('Var'  , 0.0251605   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  ,-0.0946499   ), Coef('Var'  , 0.00658874  ), Coef('Var'  , 0.00668526  ), Coef('Var'  , 0.0265512   ), Coef('Var'  , 0.0228112   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.015253    ), Coef('Var'  , 0.0659667   ), Coef('Var'  , 0.0801482   ), Coef('Var'  , 0.10388     ), Coef('Var'  , 0.0432226   ), ], 
		[Coef('Const', 0.111111    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.12542     ), Coef('Var'  , 0.125483    ), Coef('Var'  , 0.153385    ), Coef('Var'  , 0.180603    ), Coef('Var'  , 0.134084    ), ], 
		[Coef('Const', 0.444444    ), Coef('Const', 0.333333    ), Coef('Const', 0           ), Coef('Var'  , 0.232728    ), Coef('Var'  , 0.183207    ), Coef('Var'  , 0.197465    ), Coef('Var'  , 0.201697    ), Coef('Var'  , 0.340492    ), ], 
		[Coef('Const', 0.444444    ), Coef('Const', 0.666667    ), Coef('Const', 1           ), Coef('Var'  , 0.345584    ), Coef('Var'  , 0.243915    ), Coef('Var'  , 0.243846    ), Coef('Var'  , 0.223923    ), Coef('Var'  , 0.34684     ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.232824    ), Coef('Var'  , 0.182995    ), Coef('Var'  , 0.1686      ), Coef('Var'  , 0.144834    ), Coef('Var'  , 0.0539586   ), ], ])
	etat1.initMat[Chem([Sub('9')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.111111    ), Coef('Var'  , 0.133568    ), Coef('Var'  , 0.182217    ), Coef('Var'  , 0.153151    ), Coef('Var'  , 0.12502     ), Coef('Var'  , 0.125514    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0431672   ), Coef('Var'  , 0.10613     ), Coef('Var'  , 0.0816165   ), Coef('Var'  , 0.066824    ), Coef('Var'  , 0.0173269   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0224261   ), Coef('Var'  , 0.0274962   ), Coef('Var'  , 0.00763496  ), Coef('Var'  , 0.00658874  ), Coef('Var'  ,-0.0946499   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0245211   ), Coef('Var'  , 0.0473867   ), Coef('Var'  , 0.0522247   ), Coef('Var'  , 0.0659667   ), Coef('Var'  , 0.015253    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0341396   ), Coef('Var'  , 0.0681402   ), Coef('Var'  , 0.0973204   ), Coef('Var'  , 0.125483    ), Coef('Var'  , 0.12542     ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0537416   ), Coef('Var'  , 0.143573    ), Coef('Var'  , 0.168255    ), Coef('Var'  , 0.183207    ), Coef('Var'  , 0.232728    ), ], 
		[Coef('Const', 1           ), Coef('Const', 0.666667    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.3474      ), Coef('Var'  , 0.222861    ), Coef('Var'  , 0.242836    ), Coef('Var'  , 0.243915    ), Coef('Var'  , 0.345584    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.333333    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.341037    ), Coef('Var'  , 0.202196    ), Coef('Var'  , 0.196961    ), Coef('Var'  , 0.182995    ), Coef('Var'  , 0.232824    ), ], ])
	etat1.initMat[Chem([Sub('10')])] = FMat([
		[Coef('Const', 0.111111    ), Coef('Const', 0.222222    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.350204    ), Coef('Var'  , 0.229888    ), Coef('Var'  , 0.208537    ), Coef('Var'  , 0.182217    ), Coef('Var'  , 0.133568    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0584713   ), Coef('Var'  , 0.153321    ), Coef('Var'  , 0.129377    ), Coef('Var'  , 0.10613     ), Coef('Var'  , 0.0431672   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0348093   ), Coef('Var'  , 0.0742912   ), Coef('Var'  , 0.0476192   ), Coef('Var'  , 0.0274962   ), Coef('Var'  , 0.0224261   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0241092   ), Coef('Var'  , 0.0465406   ), Coef('Var'  , 0.0440718   ), Coef('Var'  , 0.0473867   ), Coef('Var'  , 0.0245211   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0210145   ), Coef('Var'  , 0.0202224   ), Coef('Var'  , 0.0417086   ), Coef('Var'  , 0.0681402   ), Coef('Var'  , 0.0341396   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0382574   ), Coef('Var'  , 0.0960996   ), Coef('Var'  , 0.120171    ), Coef('Var'  , 0.143573    ), Coef('Var'  , 0.0537416   ), ], 
		[Coef('Const', 0.444444    ), Coef('Const', 0.222222    ), Coef('Const', 0.111111    ), Coef('Var'  , 0.131123    ), Coef('Var'  , 0.175819    ), Coef('Var'  , 0.202626    ), Coef('Var'  , 0.222861    ), Coef('Var'  , 0.3474      ), ], 
		[Coef('Const', 0.444444    ), Coef('Const', 0.555556    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.342011    ), Coef('Var'  , 0.203818    ), Coef('Var'  , 0.205889    ), Coef('Var'  , 0.202196    ), Coef('Var'  , 0.341037    ), ], ])
	etat1.initMat[Chem([Sub('11')])] = FMat([
		[Coef('Const', 0.444444    ), Coef('Const', 0.666667    ), Coef('Const', 1           ), Coef('Var'  , 0.349858    ), Coef('Var'  , 0.250358    ), Coef('Var'  , 0.250258    ), Coef('Var'  , 0.229888    ), Coef('Var'  , 0.350204    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.240686    ), Coef('Var'  , 0.190664    ), Coef('Var'  , 0.177051    ), Coef('Var'  , 0.153321    ), Coef('Var'  , 0.0584713   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.12816     ), Coef('Var'  , 0.129141    ), Coef('Var'  , 0.101541    ), Coef('Var'  , 0.0742912   ), Coef('Var'  , 0.0348093   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0125618   ), Coef('Var'  , 0.0635018   ), Coef('Var'  , 0.0497953   ), Coef('Var'  , 0.0465406   ), Coef('Var'  , 0.0241092   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  ,-0.100097    ), Coef('Var'  ,-0.000501677 ), Coef('Var'  ,-0.000283501 ), Coef('Var'  , 0.0202224   ), Coef('Var'  , 0.0210145   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0080428   ), Coef('Var'  , 0.0586263   ), Coef('Var'  , 0.0722477   ), Coef('Var'  , 0.0960996   ), Coef('Var'  , 0.0382574   ), ], 
		[Coef('Const', 0.111111    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.1216      ), Coef('Var'  , 0.120715    ), Coef('Var'  , 0.148432    ), Coef('Var'  , 0.175819    ), Coef('Var'  , 0.131123    ), ], 
		[Coef('Const', 0.444444    ), Coef('Const', 0.333333    ), Coef('Const', 0           ), Coef('Var'  , 0.239189    ), Coef('Var'  , 0.187495    ), Coef('Var'  , 0.200959    ), Coef('Var'  , 0.203818    ), Coef('Var'  , 0.342011    ), ], ])
	
	
	
	etat2.bords   = {Bord('0'): etat3, Bord('1'): etat3, }
	etat2.permuts = {Permut('0'): etat2, }
	etat2.interns = {Intern('_'): etat2, }
	etat2.subs    = {Sub('0'): etat2, Sub('G', True): Etat.etatPoint, Sub('1'): etat2, Sub('2'): etat2, }
	
	etat2.buildIntern()
	etat2.fm_[Permut('0')] = PMat(3, [2, 1, 0, ])
	
	
	etat2.eqs = [
		(Chem([Permut('0'), Bord('0'), ])	,	Chem([Bord('1')])),
		(Chem([Permut('0'), Bord('1'), ])	,	Chem([Bord('0')])),
		(Chem([Permut('0'), Intern(''), ])	,	Chem([Intern('')])),
		(Chem([Permut('0'), Sub('0'), ])	,	Chem([Sub('2'), Permut('0'), ])),
		(Chem([Permut('0'), Sub('1'), ])	,	Chem([Sub('1'), Permut('0'), ])),
		(Chem([Permut('0'), Sub('2'), ])	,	Chem([Sub('0'), Permut('0'), ])),
		]
	
	
	etat2.prim.elems = [Figure(1, [Chem([Bord('0')]), Chem([Bord('1')]), ])]
	etat2.grid.elems = [Figure(1, [Chem([Bord('0')]), Chem([Intern('')]), Chem([Bord('1')]), ])]
	
	
	etat2.space = [Chem([Bord('0'), Intern('0'), Intern('0'), ]), Chem([Intern('0'), Intern('0'), ]), Chem([Bord('1'), Intern('0'), Intern('0'), ]), ]
	
	etat2.initMat[Chem([Sub('0')])] = FMat([
		[Coef('Const', 1           ), Coef('Const', 0.666667    ), Coef('Const', 0.444444    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.333333    ), Coef('Const', 0.444444    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.111111    ), ], ])
	etat2.initMat[Chem([Sub('G')])] = FMat([
		[Coef('Const', 0           )], 
		[Coef('Const', 1           )], 
		[Coef('Const', 0           )], ])
	etat2.initMat[Chem([Sub('1')])] = FMat([
		[Coef('Const', 0.444444    ), Coef('Const', 0.222222    ), Coef('Const', 0.111111    ), ], 
		[Coef('Const', 0.444444    ), Coef('Const', 0.555556    ), Coef('Const', 0.444444    ), ], 
		[Coef('Const', 0.111111    ), Coef('Const', 0.222222    ), Coef('Const', 0.444444    ), ], ])
	etat2.initMat[Chem([Sub('2')])] = FMat([
		[Coef('Const', 0.111111    ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.444444    ), Coef('Const', 0.333333    ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.444444    ), Coef('Const', 0.666667    ), Coef('Const', 1           ), ], ])
	
	
	
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
