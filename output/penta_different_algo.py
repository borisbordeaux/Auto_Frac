# -*- coding: utf-8 -*-

# Automatically generated, from file : penta_different_algo.py, function : modele()

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
	etat4 = Etat('B2',1)
	etat5 = Etat('s',1)
	
	
	etat0.subs   = {Sub('0'): etat1, Sub('1'): etat2, }
	
	etat0.eqs = [
		]
	
	
	etat0.space = []
	
	etat0.initMat[Chem([Sub('0')])] = FMat([
		[Coef('Var'  ,-0.011       ), Coef('Var'  ,-0.48        ), Coef('Var'  ,-0.962056    ), Coef('Var'  ,-0.781       ), Coef('Var'  ,-0.598785    ), Coef('Var'  , 0           ), Coef('Var'  , 0.576785    ), Coef('Var'  , 0.789       ), Coef('Var'  , 0.940057    ), Coef('Var'  , 0.499       ), ], 
		[Coef('Var'  , 0.995       ), Coef('Var'  , 0.67        ), Coef('Var'  , 0.304017    ), Coef('Var'  ,-0.255       ), Coef('Var'  ,-0.814017    ), Coef('Var'  ,-0.8         ), Coef('Var'  ,-0.814017    ), Coef('Var'  ,-0.255       ), Coef('Var'  , 0.304017    ), Coef('Var'  , 0.635       ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), ], ])
	etat0.initMat[Chem([Sub('1')])] = FMat([
		[Coef('Var'  , 3.15213     ), Coef('Var'  , 2.7         ), Coef('Var'  , 2.20107     ), Coef('Var'  , 1.72        ), Coef('Var'  , 1.25002     ), Coef('Var'  , 1.42        ), Coef('Var'  , 1.61329     ), Coef('Var'  , 2.21385     ), Coef('Var'  , 2.78886     ), Coef('Var'  , 2.97377     ), ], 
		[Coef('Var'  , 0.308237    ), Coef('Var'  , 0.67        ), Coef('Var'  , 0.99922     ), Coef('Var'  , 0.64        ), Coef('Var'  , 0.308237    ), Coef('Var'  ,-0.27        ), Coef('Var'  ,-0.809797    ), Coef('Var'  ,-0.816768    ), Coef('Var'  ,-0.809797    ), Coef('Var'  ,-0.275447    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), ], ])
	
	
	
	etat1.bords   = {Bord('0'): etat4, Bord('1'): etat4, Bord('2'): etat4, Bord('3'): etat4, Bord('4'): etat4, }
	etat1.permuts = {}
	etat1.interns = {Intern('_'): etat1, }
	etat1.subs    = {Sub('0'): etat3, Sub('G', True): Etat.etatPoint, Sub('1'): etat3, Sub('2'): etat3, Sub('3'): etat3, Sub('4'): etat3, Sub('5'): etat3, Sub('6'): etat3, Sub('7'): etat3, Sub('8'): etat3, Sub('9'): etat3, }
	
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
		(Chem([Sub('0'), Bord('1'), Permut('0'), ])	,	Chem([Sub('1'), Bord('3'), ])),
		(Chem([Sub('1'), Bord('1'), Permut('0'), ])	,	Chem([Sub('2'), Bord('3'), ])),
		(Chem([Sub('2'), Bord('1'), Permut('0'), ])	,	Chem([Sub('3'), Bord('3'), ])),
		(Chem([Sub('3'), Bord('1'), Permut('0'), ])	,	Chem([Sub('4'), Bord('3'), ])),
		(Chem([Sub('4'), Bord('1'), Permut('0'), ])	,	Chem([Sub('5'), Bord('3'), ])),
		(Chem([Sub('5'), Bord('1'), Permut('0'), ])	,	Chem([Sub('6'), Bord('3'), ])),
		(Chem([Sub('6'), Bord('1'), Permut('0'), ])	,	Chem([Sub('7'), Bord('3'), ])),
		(Chem([Sub('7'), Bord('1'), Permut('0'), ])	,	Chem([Sub('8'), Bord('3'), ])),
		(Chem([Sub('8'), Bord('1'), Permut('0'), ])	,	Chem([Sub('9'), Bord('3'), ])),
		(Chem([Sub('9'), Bord('1'), Permut('0'), ])	,	Chem([Sub('0'), Bord('3'), ])),
		(Chem([Bord('0'), Bord('1'), ])	,	Chem([Bord('1'), Bord('0'), ])),
		(Chem([Bord('1'), Bord('1'), ])	,	Chem([Bord('2'), Bord('0'), ])),
		(Chem([Bord('2'), Bord('1'), ])	,	Chem([Bord('3'), Bord('0'), ])),
		(Chem([Bord('3'), Bord('1'), ])	,	Chem([Bord('4'), Bord('0'), ])),
		(Chem([Bord('4'), Bord('1'), ])	,	Chem([Bord('0'), Bord('0'), ])),
		]
	
	
	etat1.prim.elems = [Figure(2, [Chem([Bord('0'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('0'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('0'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('0'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('1'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('1'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('1'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('1'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('2'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('2'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('2'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('2'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('3'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('3'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('3'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('3'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('4'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('4'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('4'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('4'), Sub('1'), Sub('1'), Bord('0'), ]), ])]
	etat1.grid.elems = [
		Figure(1, [Chem([Bord('1'), Bord('0'), ]), Chem([Bord('1'), Intern(''), ]), Chem([Bord('1'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('4'), Bord('0'), ]), Chem([Bord('4'), Intern(''), ]), Chem([Bord('4'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('2'), Bord('0'), ]), Chem([Bord('2'), Intern(''), ]), Chem([Bord('2'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('0'), Bord('0'), ]), Chem([Bord('0'), Intern(''), ]), Chem([Bord('0'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('3'), Bord('0'), ]), Chem([Bord('3'), Intern(''), ]), Chem([Bord('3'), Bord('1'), ]), ]), ]
	
	
	etat1.space = [Chem([Bord('4'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('2'), Intern('0'), Intern('0'), ]), Chem([Bord('2'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('3'), Intern('0'), Intern('0'), ]), Chem([Bord('4'), Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('4'), Intern('0'), Intern('0'), ]), ]
	
	etat1.initMat[Chem([Sub('0')])] = FMat([
		[Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.222964    ), Coef('Var'  , 0.210269    ), Coef('Var'  , 0.197677    ), Coef('Var'  , 0.423159    ), Coef('Var'  , 0.701318    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.363443    ), Coef('Var'  , 0.229122    ), Coef('Var'  , 0.182464    ), Coef('Var'  , 0.105456    ), Coef('Var'  , 0.0536916   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.229825    ), Coef('Var'  , 0.221879    ), Coef('Var'  , 0.163711    ), Coef('Var'  , 0.0779351   ), Coef('Var'  , 0.0376587   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0337178   ), Coef('Var'  , 0.0626277   ), Coef('Var'  , 0.10279     ), Coef('Var'  , 0.0534176   ), Coef('Var'  , 0.0295988   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0227675   ), Coef('Var'  , 0.0435077   ), Coef('Var'  , 0.0418275   ), Coef('Var'  , 0.0391449   ), Coef('Var'  , 0.0215533   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.03008     ), Coef('Var'  , 0.0535452   ), Coef('Var'  , 0.0221275   ), Coef('Var'  , 0.0561934   ), Coef('Var'  , 0.0318017   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0204726   ), Coef('Var'  , 0.0366465   ), Coef('Var'  , 0.000465762 ), Coef('Var'  , 0.0424716   ), Coef('Var'  , 0.0235048   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0241786   ), Coef('Var'  , 0.0434735   ), Coef('Var'  , 0.0475498   ), Coef('Var'  , 0.0432471   ), Coef('Var'  , 0.0240351   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0263493   ), Coef('Var'  , 0.0492669   ), Coef('Var'  , 0.0967856   ), Coef('Var'  , 0.0793106   ), Coef('Var'  , 0.0383498   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0262019   ), Coef('Var'  , 0.0496623   ), Coef('Var'  , 0.144603    ), Coef('Var'  , 0.0796654   ), Coef('Var'  , 0.0384882   ), ], ])
	etat1.initMat[Chem([Sub('G')])] = FMat([
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
	etat1.initMat[Chem([Sub('1')])] = FMat([
		[Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0353056   ), Coef('Var'  , 0.0741275   ), Coef('Var'  , 0.159594    ), Coef('Var'  , 0.210269    ), Coef('Var'  , 0.222964    ), ], 
		[Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Var'  , 0.0460191   ), Coef('Var'  , 0.0929598   ), Coef('Var'  , 0.182339    ), Coef('Var'  , 0.229122    ), Coef('Var'  , 0.363443    ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Var'  , 0.709734    ), Coef('Var'  , 0.438045    ), Coef('Var'  , 0.203835    ), Coef('Var'  , 0.221879    ), Coef('Var'  , 0.229825    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0492401   ), Coef('Var'  , 0.0976162   ), Coef('Var'  , 0.154684    ), Coef('Var'  , 0.0626277   ), Coef('Var'  , 0.0337178   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0376211   ), Coef('Var'  , 0.0778785   ), Coef('Var'  , 0.105429    ), Coef('Var'  , 0.0435077   ), Coef('Var'  , 0.0227675   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0269779   ), Coef('Var'  , 0.0491754   ), Coef('Var'  , 0.0527436   ), Coef('Var'  , 0.0535452   ), Coef('Var'  , 0.03008     ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0176064   ), Coef('Var'  , 0.0324212   ), Coef('Var'  , 0.000370554 ), Coef('Var'  , 0.0366465   ), Coef('Var'  , 0.0204726   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0249258   ), Coef('Var'  , 0.0443876   ), Coef('Var'  , 0.0143755   ), Coef('Var'  , 0.0434735   ), Coef('Var'  , 0.0241786   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0251445   ), Coef('Var'  , 0.0448418   ), Coef('Var'  , 0.033846    ), Coef('Var'  , 0.0492669   ), Coef('Var'  , 0.0263493   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0274253   ), Coef('Var'  , 0.0485466   ), Coef('Var'  , 0.0927836   ), Coef('Var'  , 0.0496623   ), Coef('Var'  , 0.0262019   ), ], ])
	etat1.initMat[Chem([Sub('2')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.025657    ), Coef('Var'  , 0.0476103   ), Coef('Var'  , 0.103527    ), Coef('Var'  , 0.0741275   ), Coef('Var'  , 0.0353056   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0285934   ), Coef('Var'  , 0.0546922   ), Coef('Var'  , 0.152778    ), Coef('Var'  , 0.0929598   ), Coef('Var'  , 0.0460191   ), ], 
		[Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.235221    ), Coef('Var'  , 0.231947    ), Coef('Var'  , 0.203315    ), Coef('Var'  , 0.438045    ), Coef('Var'  , 0.709734    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.359793    ), Coef('Var'  , 0.222246    ), Coef('Var'  , 0.182484    ), Coef('Var'  , 0.0976162   ), Coef('Var'  , 0.0492401   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.228831    ), Coef('Var'  , 0.219565    ), Coef('Var'  , 0.161529    ), Coef('Var'  , 0.0778785   ), Coef('Var'  , 0.0376211   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0278842   ), Coef('Var'  , 0.0527434   ), Coef('Var'  , 0.097584    ), Coef('Var'  , 0.0491754   ), Coef('Var'  , 0.0269779   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0191447   ), Coef('Var'  , 0.0378257   ), Coef('Var'  , 0.0359157   ), Coef('Var'  , 0.0324212   ), Coef('Var'  , 0.0176064   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0247467   ), Coef('Var'  , 0.0446848   ), Coef('Var'  , 0.0147245   ), Coef('Var'  , 0.0443876   ), Coef('Var'  , 0.0249258   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0234671   ), Coef('Var'  , 0.0417274   ), Coef('Var'  , 6.82796e-05 ), Coef('Var'  , 0.0448418   ), Coef('Var'  , 0.0251445   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0266613   ), Coef('Var'  , 0.0469588   ), Coef('Var'  , 0.0480755   ), Coef('Var'  , 0.0485466   ), Coef('Var'  , 0.0274253   ), ], ])
	etat1.initMat[Chem([Sub('3')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0251806   ), Coef('Var'  , 0.0449578   ), Coef('Var'  , 0.041303    ), Coef('Var'  , 0.0476103   ), Coef('Var'  , 0.025657    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0279943   ), Coef('Var'  , 0.0508178   ), Coef('Var'  , 0.101746    ), Coef('Var'  , 0.0546922   ), Coef('Var'  , 0.0285934   ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.049849    ), Coef('Var'  , 0.0987991   ), Coef('Var'  , 0.165772    ), Coef('Var'  , 0.231947    ), Coef('Var'  , 0.235221    ), ], 
		[Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Var'  , 0.0416773   ), Coef('Var'  , 0.0845987   ), Coef('Var'  , 0.183189    ), Coef('Var'  , 0.222246    ), Coef('Var'  , 0.359793    ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Var'  , 0.705548    ), Coef('Var'  , 0.430275    ), Coef('Var'  , 0.200504    ), Coef('Var'  , 0.219565    ), Coef('Var'  , 0.228831    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0426571   ), Coef('Var'  , 0.0860204   ), Coef('Var'  , 0.147204    ), Coef('Var'  , 0.0527434   ), Coef('Var'  , 0.0278842   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0378195   ), Coef('Var'  , 0.0786819   ), Coef('Var'  , 0.0975      ), Coef('Var'  , 0.0378257   ), Coef('Var'  , 0.0191447   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0261168   ), Coef('Var'  , 0.0474881   ), Coef('Var'  , 0.0456249   ), Coef('Var'  , 0.0446848   ), Coef('Var'  , 0.0247467   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0205698   ), Coef('Var'  , 0.0373727   ), Coef('Var'  ,-0.000891637 ), Coef('Var'  , 0.0417274   ), Coef('Var'  , 0.0234671   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.022588    ), Coef('Var'  , 0.0409889   ), Coef('Var'  , 0.018049    ), Coef('Var'  , 0.0469588   ), Coef('Var'  , 0.0266613   ), ], ])
	etat1.initMat[Chem([Sub('4')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0245204   ), Coef('Var'  , 0.0443239   ), Coef('Var'  , 0.00350973  ), Coef('Var'  , 0.0449578   ), Coef('Var'  , 0.0251806   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0309014   ), Coef('Var'  , 0.0552223   ), Coef('Var'  , 0.0521267   ), Coef('Var'  , 0.0508178   ), Coef('Var'  , 0.0279943   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0366139   ), Coef('Var'  , 0.0665324   ), Coef('Var'  , 0.105194    ), Coef('Var'  , 0.0987991   ), Coef('Var'  , 0.049849    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0210929   ), Coef('Var'  , 0.0413096   ), Coef('Var'  , 0.152809    ), Coef('Var'  , 0.0845987   ), Coef('Var'  , 0.0416773   ), ], 
		[Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.226647    ), Coef('Var'  , 0.21685     ), Coef('Var'  , 0.200382    ), Coef('Var'  , 0.430275    ), Coef('Var'  , 0.705548    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.353605    ), Coef('Var'  , 0.211926    ), Coef('Var'  , 0.177194    ), Coef('Var'  , 0.0860204   ), Coef('Var'  , 0.0426571   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.234843    ), Coef('Var'  , 0.230102    ), Coef('Var'  , 0.157526    ), Coef('Var'  , 0.0786819   ), Coef('Var'  , 0.0378195   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0307652   ), Coef('Var'  , 0.0567181   ), Coef('Var'  , 0.0955746   ), Coef('Var'  , 0.0474881   ), Coef('Var'  , 0.0261168   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0203228   ), Coef('Var'  , 0.0390756   ), Coef('Var'  , 0.0358526   ), Coef('Var'  , 0.0373727   ), Coef('Var'  , 0.0205698   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0206887   ), Coef('Var'  , 0.0379393   ), Coef('Var'  , 0.0198316   ), Coef('Var'  , 0.0409889   ), Coef('Var'  , 0.022588    ), ], ])
	etat1.initMat[Chem([Sub('5')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0255073   ), Coef('Var'  , 0.0460322   ), Coef('Var'  , 0.00307556  ), Coef('Var'  , 0.0443239   ), Coef('Var'  , 0.0245204   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0333458   ), Coef('Var'  , 0.0594788   ), Coef('Var'  , 0.0208351   ), Coef('Var'  , 0.0552223   ), Coef('Var'  , 0.0309014   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0293969   ), Coef('Var'  , 0.0528411   ), Coef('Var'  , 0.042183    ), Coef('Var'  , 0.0665324   ), Coef('Var'  , 0.0366139   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0176025   ), Coef('Var'  , 0.032966    ), Coef('Var'  , 0.101638    ), Coef('Var'  , 0.0413096   ), Coef('Var'  , 0.0210929   ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0381235   ), Coef('Var'  , 0.0787118   ), Coef('Var'  , 0.161128    ), Coef('Var'  , 0.21685     ), Coef('Var'  , 0.226647    ), ], 
		[Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Var'  , 0.0392974   ), Coef('Var'  , 0.0812334   ), Coef('Var'  , 0.177294    ), Coef('Var'  , 0.211926    ), Coef('Var'  , 0.353605    ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Var'  , 0.716293    ), Coef('Var'  , 0.448557    ), Coef('Var'  , 0.195532    ), Coef('Var'  , 0.230102    ), Coef('Var'  , 0.234843    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0443214   ), Coef('Var'  , 0.0887016   ), Coef('Var'  , 0.147586    ), Coef('Var'  , 0.0567181   ), Coef('Var'  , 0.0307652   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.033552    ), Coef('Var'  , 0.0708394   ), Coef('Var'  , 0.0978506   ), Coef('Var'  , 0.0390756   ), Coef('Var'  , 0.0203228   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0225606   ), Coef('Var'  , 0.0406392   ), Coef('Var'  , 0.0528775   ), Coef('Var'  , 0.0379393   ), Coef('Var'  , 0.0206887   ), ], ])
	etat1.initMat[Chem([Sub('6')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0283065   ), Coef('Var'  , 0.0523095   ), Coef('Var'  , 0.038227    ), Coef('Var'  , 0.0460322   ), Coef('Var'  , 0.0255073   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0346849   ), Coef('Var'  , 0.0620237   ), Coef('Var'  , 0.0208083   ), Coef('Var'  , 0.0594788   ), Coef('Var'  , 0.0333458   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0232332   ), Coef('Var'  , 0.0423019   ), Coef('Var'  , 0.00486043  ), Coef('Var'  , 0.0528411   ), Coef('Var'  , 0.0293969   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0208153   ), Coef('Var'  , 0.037431    ), Coef('Var'  , 0.0535046   ), Coef('Var'  , 0.032966    ), Coef('Var'  , 0.0176025   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.025823    ), Coef('Var'  , 0.0482389   ), Coef('Var'  , 0.102241    ), Coef('Var'  , 0.0787118   ), Coef('Var'  , 0.0381235   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0262342   ), Coef('Var'  , 0.049921    ), Coef('Var'  , 0.149033    ), Coef('Var'  , 0.0812334   ), Coef('Var'  , 0.0392974   ), ], 
		[Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.237851    ), Coef('Var'  , 0.235895    ), Coef('Var'  , 0.195792    ), Coef('Var'  , 0.448557    ), Coef('Var'  , 0.716293    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.352688    ), Coef('Var'  , 0.210937    ), Coef('Var'  , 0.178444    ), Coef('Var'  , 0.0887016   ), Coef('Var'  , 0.0443214   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.224362    ), Coef('Var'  , 0.212345    ), Coef('Var'  , 0.156229    ), Coef('Var'  , 0.0708394   ), Coef('Var'  , 0.033552    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0260023   ), Coef('Var'  , 0.0485965   ), Coef('Var'  , 0.10086     ), Coef('Var'  , 0.0406392   ), Coef('Var'  , 0.0225606   ), ], ])
	etat1.initMat[Chem([Sub('7')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.039994    ), Coef('Var'  , 0.0816858   ), Coef('Var'  , 0.0992035   ), Coef('Var'  , 0.0523095   ), Coef('Var'  , 0.0283065   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0355962   ), Coef('Var'  , 0.0641438   ), Coef('Var'  , 0.0523094   ), Coef('Var'  , 0.0620237   ), Coef('Var'  , 0.0346849   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0201392   ), Coef('Var'  , 0.0370841   ), Coef('Var'  , 0.00410905  ), Coef('Var'  , 0.0423019   ), Coef('Var'  , 0.0232332   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0248762   ), Coef('Var'  , 0.0442231   ), Coef('Var'  , 0.0221965   ), Coef('Var'  , 0.037431    ), Coef('Var'  , 0.0208153   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0239966   ), Coef('Var'  , 0.0431226   ), Coef('Var'  , 0.0403997   ), Coef('Var'  , 0.0482389   ), Coef('Var'  , 0.025823    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0277091   ), Coef('Var'  , 0.0497415   ), Coef('Var'  , 0.100261    ), Coef('Var'  , 0.049921    ), Coef('Var'  , 0.0262342   ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0453367   ), Coef('Var'  , 0.0915459   ), Coef('Var'  , 0.157923    ), Coef('Var'  , 0.235895    ), Coef('Var'  , 0.237851    ), ], 
		[Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Var'  , 0.0383895   ), Coef('Var'  , 0.0795728   ), Coef('Var'  , 0.179151    ), Coef('Var'  , 0.210937    ), Coef('Var'  , 0.352688    ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Var'  , 0.703901    ), Coef('Var'  , 0.427166    ), Coef('Var'  , 0.194266    ), Coef('Var'  , 0.212345    ), Coef('Var'  , 0.224362    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0400612   ), Coef('Var'  , 0.0817138   ), Coef('Var'  , 0.15018     ), Coef('Var'  , 0.0485965   ), Coef('Var'  , 0.0260023   ), ], ])
	etat1.initMat[Chem([Sub('8')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.226164    ), Coef('Var'  , 0.215638    ), Coef('Var'  , 0.15847     ), Coef('Var'  , 0.0816858   ), Coef('Var'  , 0.039994    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0385688   ), Coef('Var'  , 0.0715143   ), Coef('Var'  , 0.101349    ), Coef('Var'  , 0.0641438   ), Coef('Var'  , 0.0355962   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0219546   ), Coef('Var'  , 0.0420883   ), Coef('Var'  , 0.0407461   ), Coef('Var'  , 0.0370841   ), Coef('Var'  , 0.0201392   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0275404   ), Coef('Var'  , 0.049186    ), Coef('Var'  , 0.0222414   ), Coef('Var'  , 0.0442231   ), Coef('Var'  , 0.0248762   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.023079    ), Coef('Var'  , 0.041159    ), Coef('Var'  , 0.00383028  ), Coef('Var'  , 0.0431226   ), Coef('Var'  , 0.0239966   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0302356   ), Coef('Var'  , 0.0539787   ), Coef('Var'  , 0.0530033   ), Coef('Var'  , 0.0497415   ), Coef('Var'  , 0.0277091   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0285074   ), Coef('Var'  , 0.053367    ), Coef('Var'  , 0.0987392   ), Coef('Var'  , 0.0915459   ), Coef('Var'  , 0.0453367   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0252065   ), Coef('Var'  , 0.0474578   ), Coef('Var'  , 0.148994    ), Coef('Var'  , 0.0795728   ), Coef('Var'  , 0.0383895   ), ], 
		[Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.227214    ), Coef('Var'  , 0.217238    ), Coef('Var'  , 0.194312    ), Coef('Var'  , 0.427166    ), Coef('Var'  , 0.703901    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.35153     ), Coef('Var'  , 0.208373    ), Coef('Var'  , 0.178314    ), Coef('Var'  , 0.0817138   ), Coef('Var'  , 0.0400612   ), ], ])
	etat1.initMat[Chem([Sub('9')])] = FMat([
		[Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Var'  , 0.701318    ), Coef('Var'  , 0.423159    ), Coef('Var'  , 0.195297    ), Coef('Var'  , 0.215638    ), Coef('Var'  , 0.226164    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0536916   ), Coef('Var'  , 0.105456    ), Coef('Var'  , 0.151685    ), Coef('Var'  , 0.0715143   ), Coef('Var'  , 0.0385688   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0376587   ), Coef('Var'  , 0.0779351   ), Coef('Var'  , 0.103802    ), Coef('Var'  , 0.0420883   ), Coef('Var'  , 0.0219546   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0295988   ), Coef('Var'  , 0.0534176   ), Coef('Var'  , 0.0551289   ), Coef('Var'  , 0.049186    ), Coef('Var'  , 0.0275404   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0215533   ), Coef('Var'  , 0.0391449   ), Coef('Var'  , 0.0064863   ), Coef('Var'  , 0.041159    ), Coef('Var'  , 0.023079    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0318017   ), Coef('Var'  , 0.0561934   ), Coef('Var'  , 0.0237961   ), Coef('Var'  , 0.0539787   ), Coef('Var'  , 0.0302356   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0235048   ), Coef('Var'  , 0.0424716   ), Coef('Var'  , 0.0378363   ), Coef('Var'  , 0.053367    ), Coef('Var'  , 0.0285074   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0240351   ), Coef('Var'  , 0.0432471   ), Coef('Var'  , 0.0969974   ), Coef('Var'  , 0.0474578   ), Coef('Var'  , 0.0252065   ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0383498   ), Coef('Var'  , 0.0793106   ), Coef('Var'  , 0.154528    ), Coef('Var'  , 0.217238    ), Coef('Var'  , 0.227214    ), ], 
		[Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Var'  , 0.0384882   ), Coef('Var'  , 0.0796654   ), Coef('Var'  , 0.174443    ), Coef('Var'  , 0.208373    ), Coef('Var'  , 0.35153     ), ], ])
	
	
	
	etat2.bords   = {Bord('0'): etat4, Bord('1'): etat4, Bord('2'): etat4, Bord('3'): etat4, Bord('4'): etat4, }
	etat2.permuts = {}
	etat2.interns = {Intern('_'): etat2, }
	etat2.subs    = {Sub('0'): etat2, Sub('G', True): Etat.etatPoint, Sub('1'): etat2, Sub('2'): etat2, Sub('3'): etat2, Sub('4'): etat2, }
	
	etat2.buildIntern()
	
	
	etat2.eqs = [
		(Chem([Bord('0'), Sub('1'), ])	,	Chem([Sub('0'), Bord('0'), ])),
		(Chem([Bord('1'), Sub('0'), ])	,	Chem([Sub('0'), Bord('1'), ])),
		(Chem([Bord('1'), Sub('1'), ])	,	Chem([Sub('1'), Bord('0'), ])),
		(Chem([Bord('2'), Sub('0'), ])	,	Chem([Sub('1'), Bord('1'), ])),
		(Chem([Bord('2'), Sub('1'), ])	,	Chem([Sub('2'), Bord('0'), ])),
		(Chem([Bord('3'), Sub('0'), ])	,	Chem([Sub('2'), Bord('1'), ])),
		(Chem([Bord('3'), Sub('1'), ])	,	Chem([Sub('3'), Bord('0'), ])),
		(Chem([Bord('4'), Sub('0'), ])	,	Chem([Sub('3'), Bord('1'), ])),
		(Chem([Bord('4'), Sub('1'), ])	,	Chem([Sub('4'), Bord('0'), ])),
		(Chem([Bord('0'), Sub('0'), ])	,	Chem([Sub('4'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('2'), Permut('0'), ])	,	Chem([Sub('1'), Bord('4'), ])),
		(Chem([Sub('1'), Bord('2'), Permut('0'), ])	,	Chem([Sub('2'), Bord('4'), ])),
		(Chem([Sub('2'), Bord('2'), Permut('0'), ])	,	Chem([Sub('3'), Bord('4'), ])),
		(Chem([Sub('3'), Bord('2'), Permut('0'), ])	,	Chem([Sub('4'), Bord('4'), ])),
		(Chem([Sub('4'), Bord('2'), Permut('0'), ])	,	Chem([Sub('0'), Bord('4'), ])),
		(Chem([Bord('0'), Bord('1'), ])	,	Chem([Bord('1'), Bord('0'), ])),
		(Chem([Bord('1'), Bord('1'), ])	,	Chem([Bord('2'), Bord('0'), ])),
		(Chem([Bord('2'), Bord('1'), ])	,	Chem([Bord('3'), Bord('0'), ])),
		(Chem([Bord('3'), Bord('1'), ])	,	Chem([Bord('4'), Bord('0'), ])),
		(Chem([Bord('4'), Bord('1'), ])	,	Chem([Bord('0'), Bord('0'), ])),
		]
	
	
	etat2.prim.elems = [Figure(2, [Chem([Bord('0'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('0'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('0'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('0'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('1'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('1'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('1'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('1'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('2'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('2'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('2'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('2'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('3'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('3'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('3'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('3'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('4'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('4'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('4'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('4'), Sub('1'), Sub('1'), Bord('0'), ]), ])]
	etat2.grid.elems = [
		Figure(1, [Chem([Bord('1'), Bord('0'), ]), Chem([Bord('1'), Intern(''), ]), Chem([Bord('1'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('4'), Bord('0'), ]), Chem([Bord('4'), Intern(''), ]), Chem([Bord('4'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('2'), Bord('0'), ]), Chem([Bord('2'), Intern(''), ]), Chem([Bord('2'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('0'), Bord('0'), ]), Chem([Bord('0'), Intern(''), ]), Chem([Bord('0'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('3'), Bord('0'), ]), Chem([Bord('3'), Intern(''), ]), Chem([Bord('3'), Bord('1'), ]), ]), ]
	
	
	etat2.space = [Chem([Bord('4'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('2'), Intern('0'), Intern('0'), ]), Chem([Bord('2'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('3'), Intern('0'), Intern('0'), ]), Chem([Bord('4'), Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('4'), Intern('0'), Intern('0'), ]), ]
	
	etat2.initMat[Chem([Sub('0')])] = FMat([
		[Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0339542   ), Coef('Var'  , 0.0667408   ), Coef('Var'  , 0.118259    ), Coef('Var'  , 0.146542    ), Coef('Var'  , 0.196828    ), ], 
		[Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0373296   ), Coef('Var'  , 0.0779075   ), Coef('Var'  , 0.137237    ), Coef('Var'  , 0.207898    ), Coef('Var'  , 0.350897    ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.200782    ), Coef('Var'  , 0.153535    ), Coef('Var'  , 0.15439     ), Coef('Var'  , 0.149291    ), Coef('Var'  , 0.197983    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.358454    ), Coef('Var'  , 0.220064    ), Coef('Var'  , 0.134301    ), Coef('Var'  , 0.0938528   ), Coef('Var'  , 0.0473251   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.199934    ), Coef('Var'  , 0.152593    ), Coef('Var'  , 0.115713    ), Coef('Var'  , 0.0699835   ), Coef('Var'  , 0.0352005   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0409502   ), Coef('Var'  , 0.083521    ), Coef('Var'  , 0.0846397   ), Coef('Var'  , 0.0462893   ), Coef('Var'  , 0.0236402   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0356721   ), Coef('Var'  , 0.0705146   ), Coef('Var'  , 0.0556784   ), Coef('Var'  , 0.0527098   ), Coef('Var'  , 0.027583    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0371106   ), Coef('Var'  , 0.0691574   ), Coef('Var'  , 0.056105    ), Coef('Var'  , 0.0706403   ), Coef('Var'  , 0.0381925   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0264317   ), Coef('Var'  , 0.0498376   ), Coef('Var'  , 0.0572521   ), Coef('Var'  , 0.0688076   ), Coef('Var'  , 0.0352781   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0293811   ), Coef('Var'  , 0.0561293   ), Coef('Var'  , 0.0864248   ), Coef('Var'  , 0.0939851   ), Coef('Var'  , 0.0470732   ), ], ])
	etat2.initMat[Chem([Sub('G')])] = FMat([
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
	etat2.initMat[Chem([Sub('1')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0250887   ), Coef('Var'  , 0.0477049   ), Coef('Var'  , 0.0484033   ), Coef('Var'  , 0.0667408   ), Coef('Var'  , 0.0339542   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0260476   ), Coef('Var'  , 0.0496323   ), Coef('Var'  , 0.079826    ), Coef('Var'  , 0.0779075   ), Coef('Var'  , 0.0373296   ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0380892   ), Coef('Var'  , 0.0738416   ), Coef('Var'  , 0.113565    ), Coef('Var'  , 0.153535    ), Coef('Var'  , 0.200782    ), ], 
		[Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.041938    ), Coef('Var'  , 0.0859328   ), Coef('Var'  , 0.13705     ), Coef('Var'  , 0.220064    ), Coef('Var'  , 0.358454    ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.201671    ), Coef('Var'  , 0.155073    ), Coef('Var'  , 0.160251    ), Coef('Var'  , 0.152593    ), Coef('Var'  , 0.199934    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.356796    ), Coef('Var'  , 0.216834    ), Coef('Var'  , 0.142524    ), Coef('Var'  , 0.083521    ), Coef('Var'  , 0.0409502   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.200767    ), Coef('Var'  , 0.153592    ), Coef('Var'  , 0.123942    ), Coef('Var'  , 0.0705146   ), Coef('Var'  , 0.0356721   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0498712   ), Coef('Var'  , 0.0997242   ), Coef('Var'  , 0.0885344   ), Coef('Var'  , 0.0691574   ), Coef('Var'  , 0.0371106   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.030693    ), Coef('Var'  , 0.0621111   ), Coef('Var'  , 0.0548163   ), Coef('Var'  , 0.0498376   ), Coef('Var'  , 0.0264317   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0290387   ), Coef('Var'  , 0.0555543   ), Coef('Var'  , 0.0510875   ), Coef('Var'  , 0.0561293   ), Coef('Var'  , 0.0293811   ), ], ])
	etat2.initMat[Chem([Sub('2')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0305034   ), Coef('Var'  , 0.0616744   ), Coef('Var'  , 0.0489686   ), Coef('Var'  , 0.0477049   ), Coef('Var'  , 0.0250887   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0297788   ), Coef('Var'  , 0.0548656   ), Coef('Var'  , 0.0491656   ), Coef('Var'  , 0.0496323   ), Coef('Var'  , 0.0260476   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0281763   ), Coef('Var'  , 0.0533777   ), Coef('Var'  , 0.0526844   ), Coef('Var'  , 0.0738416   ), Coef('Var'  , 0.0380892   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0266094   ), Coef('Var'  , 0.051479    ), Coef('Var'  , 0.0879972   ), Coef('Var'  , 0.0859328   ), Coef('Var'  , 0.041938    ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0377918   ), Coef('Var'  , 0.0738257   ), Coef('Var'  , 0.121591    ), Coef('Var'  , 0.155073    ), Coef('Var'  , 0.201671    ), ], 
		[Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0438066   ), Coef('Var'  , 0.0877553   ), Coef('Var'  , 0.142378    ), Coef('Var'  , 0.216834    ), Coef('Var'  , 0.356796    ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.200827    ), Coef('Var'  , 0.153751    ), Coef('Var'  , 0.160462    ), Coef('Var'  , 0.153592    ), Coef('Var'  , 0.200767    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.362102    ), Coef('Var'  , 0.227691    ), Coef('Var'  , 0.137861    ), Coef('Var'  , 0.0997242   ), Coef('Var'  , 0.0498712   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.194122    ), Coef('Var'  , 0.14271     ), Coef('Var'  , 0.115579    ), Coef('Var'  , 0.0621111   ), Coef('Var'  , 0.030693    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0462827   ), Coef('Var'  , 0.0928708   ), Coef('Var'  , 0.0833125   ), Coef('Var'  , 0.0555543   ), Coef('Var'  , 0.0290387   ), ], ])
	etat2.initMat[Chem([Sub('3')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.194679    ), Coef('Var'  , 0.143399    ), Coef('Var'  , 0.114707    ), Coef('Var'  , 0.0616744   ), Coef('Var'  , 0.0305034   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0425899   ), Coef('Var'  , 0.085771    ), Coef('Var'  , 0.0824598   ), Coef('Var'  , 0.0548656   ), Coef('Var'  , 0.0297788   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0331137   ), Coef('Var'  , 0.066629    ), Coef('Var'  , 0.0503301   ), Coef('Var'  , 0.0533777   ), Coef('Var'  , 0.0281763   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0299991   ), Coef('Var'  , 0.0564208   ), Coef('Var'  , 0.0527503   ), Coef('Var'  , 0.051479    ), Coef('Var'  , 0.0266094   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.028813    ), Coef('Var'  , 0.0546352   ), Coef('Var'  , 0.0541682   ), Coef('Var'  , 0.0738257   ), Coef('Var'  , 0.0377918   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0255509   ), Coef('Var'  , 0.0490193   ), Coef('Var'  , 0.0881203   ), Coef('Var'  , 0.0877553   ), Coef('Var'  , 0.0438066   ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0359983   ), Coef('Var'  , 0.0709493   ), Coef('Var'  , 0.120917    ), Coef('Var'  , 0.153751    ), Coef('Var'  , 0.200827    ), ], 
		[Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0512849   ), Coef('Var'  , 0.101862    ), Coef('Var'  , 0.140375    ), Coef('Var'  , 0.227691    ), Coef('Var'  , 0.362102    ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.196863    ), Coef('Var'  , 0.146776    ), Coef('Var'  , 0.158332    ), Coef('Var'  , 0.14271     ), Coef('Var'  , 0.194122    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.361108    ), Coef('Var'  , 0.224539    ), Coef('Var'  , 0.137841    ), Coef('Var'  , 0.0928708   ), Coef('Var'  , 0.0462827   ), ], ])
	etat2.initMat[Chem([Sub('4')])] = FMat([
		[Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.196828    ), Coef('Var'  , 0.146542    ), Coef('Var'  , 0.153144    ), Coef('Var'  , 0.143399    ), Coef('Var'  , 0.194679    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.350897    ), Coef('Var'  , 0.207898    ), Coef('Var'  , 0.133966    ), Coef('Var'  , 0.085771    ), Coef('Var'  , 0.0425899   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.197983    ), Coef('Var'  , 0.149291    ), Coef('Var'  , 0.111961    ), Coef('Var'  , 0.066629    ), Coef('Var'  , 0.0331137   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0473251   ), Coef('Var'  , 0.0938528   ), Coef('Var'  , 0.0826114   ), Coef('Var'  , 0.0564208   ), Coef('Var'  , 0.0299991   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0352005   ), Coef('Var'  , 0.0699835   ), Coef('Var'  , 0.0541684   ), Coef('Var'  , 0.0546352   ), Coef('Var'  , 0.028813    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0236402   ), Coef('Var'  , 0.0462893   ), Coef('Var'  , 0.0560635   ), Coef('Var'  , 0.0490193   ), Coef('Var'  , 0.0255509   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.027583    ), Coef('Var'  , 0.0527098   ), Coef('Var'  , 0.0596334   ), Coef('Var'  , 0.0709493   ), Coef('Var'  , 0.0359983   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0381925   ), Coef('Var'  , 0.0706403   ), Coef('Var'  , 0.0907998   ), Coef('Var'  , 0.101862    ), Coef('Var'  , 0.0512849   ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0352781   ), Coef('Var'  , 0.0688076   ), Coef('Var'  , 0.120804    ), Coef('Var'  , 0.146776    ), Coef('Var'  , 0.196863    ), ], 
		[Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0470732   ), Coef('Var'  , 0.0939851   ), Coef('Var'  , 0.136848    ), Coef('Var'  , 0.224539    ), Coef('Var'  , 0.361108    ), ], ])
	
	
	
	etat3.bords   = {Bord('0'): etat4, Bord('1'): etat4, Bord('2'): etat4, Bord('3'): etat4, }
	etat3.permuts = {}
	etat3.interns = {Intern('_'): etat3, }
	etat3.subs    = {Sub('0'): etat3, Sub('G', True): Etat.etatPoint, Sub('1'): etat3, Sub('2'): etat3, Sub('3'): etat3, Sub('4'): etat3, Sub('5'): etat3, Sub('6'): etat3, Sub('7'): etat3, }
	
	etat3.buildIntern()
	
	
	etat3.eqs = [
		(Chem([Bord('0'), Sub('0'), ])	,	Chem([Sub('0'), Bord('0'), ])),
		(Chem([Bord('0'), Sub('1'), ])	,	Chem([Sub('1'), Bord('0'), ])),
		(Chem([Bord('1'), Sub('0'), ])	,	Chem([Sub('2'), Bord('0'), ])),
		(Chem([Bord('1'), Sub('1'), ])	,	Chem([Sub('3'), Bord('0'), ])),
		(Chem([Bord('2'), Sub('0'), ])	,	Chem([Sub('4'), Bord('0'), ])),
		(Chem([Bord('2'), Sub('1'), ])	,	Chem([Sub('5'), Bord('0'), ])),
		(Chem([Bord('3'), Sub('0'), ])	,	Chem([Sub('6'), Bord('0'), ])),
		(Chem([Bord('3'), Sub('1'), ])	,	Chem([Sub('7'), Bord('0'), ])),
		(Chem([Sub('0'), Bord('1'), Permut('0'), ])	,	Chem([Sub('1'), Bord('3'), ])),
		(Chem([Sub('1'), Bord('1'), Permut('0'), ])	,	Chem([Sub('2'), Bord('3'), ])),
		(Chem([Sub('2'), Bord('1'), Permut('0'), ])	,	Chem([Sub('3'), Bord('3'), ])),
		(Chem([Sub('3'), Bord('1'), Permut('0'), ])	,	Chem([Sub('4'), Bord('3'), ])),
		(Chem([Sub('4'), Bord('1'), Permut('0'), ])	,	Chem([Sub('5'), Bord('3'), ])),
		(Chem([Sub('5'), Bord('1'), Permut('0'), ])	,	Chem([Sub('6'), Bord('3'), ])),
		(Chem([Sub('6'), Bord('1'), Permut('0'), ])	,	Chem([Sub('7'), Bord('3'), ])),
		(Chem([Sub('7'), Bord('1'), Permut('0'), ])	,	Chem([Sub('0'), Bord('3'), ])),
		(Chem([Bord('0'), Bord('1'), ])	,	Chem([Bord('1'), Bord('0'), ])),
		(Chem([Bord('1'), Bord('1'), ])	,	Chem([Bord('2'), Bord('0'), ])),
		(Chem([Bord('2'), Bord('1'), ])	,	Chem([Bord('3'), Bord('0'), ])),
		(Chem([Bord('3'), Bord('1'), ])	,	Chem([Bord('0'), Bord('0'), ])),
		]
	
	
	etat3.prim.elems = [Figure(2, [Chem([Bord('0'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('0'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('0'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('0'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('1'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('1'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('1'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('1'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('2'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('2'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('2'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('2'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('3'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('3'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('3'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('3'), Sub('1'), Sub('1'), Bord('0'), ]), ])]
	etat3.grid.elems = [
		Figure(1, [Chem([Bord('1'), Bord('0'), ]), Chem([Bord('1'), Intern(''), ]), Chem([Bord('1'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('2'), Bord('0'), ]), Chem([Bord('2'), Intern(''), ]), Chem([Bord('2'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('0'), Bord('0'), ]), Chem([Bord('0'), Intern(''), ]), Chem([Bord('0'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('3'), Bord('0'), ]), Chem([Bord('3'), Intern(''), ]), Chem([Bord('3'), Bord('1'), ]), ]), ]
	
	
	etat3.space = [Chem([Bord('0'), Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('2'), Intern('0'), Intern('0'), ]), Chem([Bord('2'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('3'), Intern('0'), Intern('0'), ]), ]
	
	etat3.initMat[Chem([Sub('0')])] = FMat([
		[Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.231464    ), Coef('Var'  , 0.225568    ), Coef('Var'  , 0.249223    ), Coef('Var'  , 0.442764    ), Coef('Var'  , 0.712679    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.358258    ), Coef('Var'  , 0.219955    ), Coef('Var'  , 0.198509    ), Coef('Var'  , 0.0911752   ), Coef('Var'  , 0.0450424   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.22675     ), Coef('Var'  , 0.216999    ), Coef('Var'  , 0.142979    ), Coef('Var'  , 0.07397     ), Coef('Var'  , 0.0347185   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.04073     ), Coef('Var'  , 0.0742815   ), Coef('Var'  , 0.0778005   ), Coef('Var'  , 0.0639296   ), Coef('Var'  , 0.0360949   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0449293   ), Coef('Var'  , 0.0824818   ), Coef('Var'  , 0.0217386   ), Coef('Var'  , 0.0821493   ), Coef('Var'  , 0.0462348   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0267428   ), Coef('Var'  , 0.0479927   ), Coef('Var'  , 0.0568478   ), Coef('Var'  , 0.0493168   ), Coef('Var'  , 0.0269763   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.035791    ), Coef('Var'  , 0.0661554   ), Coef('Var'  , 0.0904742   ), Coef('Var'  , 0.0959681   ), Coef('Var'  , 0.0478873   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0353341   ), Coef('Var'  , 0.066567    ), Coef('Var'  , 0.162427    ), Coef('Var'  , 0.100727    ), Coef('Var'  , 0.0503666   ), ], ])
	etat3.initMat[Chem([Sub('G')])] = FMat([
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], ])
	etat3.initMat[Chem([Sub('1')])] = FMat([
		[Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.04107     ), Coef('Var'  , 0.0845675   ), Coef('Var'  , 0.139112    ), Coef('Var'  , 0.225568    ), Coef('Var'  , 0.231464    ), ], 
		[Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Var'  , 0.0450026   ), Coef('Var'  , 0.0907213   ), Coef('Var'  , 0.199463    ), Coef('Var'  , 0.219955    ), Coef('Var'  , 0.358258    ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Var'  , 0.709162    ), Coef('Var'  , 0.435945    ), Coef('Var'  , 0.262359    ), Coef('Var'  , 0.216999    ), Coef('Var'  , 0.22675     ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0527738   ), Coef('Var'  , 0.104079    ), Coef('Var'  , 0.161838    ), Coef('Var'  , 0.0742815   ), Coef('Var'  , 0.04073     ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0539706   ), Coef('Var'  , 0.107167    ), Coef('Var'  , 0.0745018   ), Coef('Var'  , 0.0824818   ), Coef('Var'  , 0.0449293   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0272474   ), Coef('Var'  , 0.0494536   ), Coef('Var'  , 0.052529    ), Coef('Var'  , 0.0479927   ), Coef('Var'  , 0.0267428   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0344554   ), Coef('Var'  , 0.0622771   ), Coef('Var'  , 0.0306353   ), Coef('Var'  , 0.0661554   ), Coef('Var'  , 0.035791    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0363181   ), Coef('Var'  , 0.0657906   ), Coef('Var'  , 0.0795624   ), Coef('Var'  , 0.066567    ), Coef('Var'  , 0.0353341   ), ], ])
	etat3.initMat[Chem([Sub('2')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0292876   ), Coef('Var'  , 0.0545192   ), Coef('Var'  , 0.045143    ), Coef('Var'  , 0.0845675   ), Coef('Var'  , 0.04107     ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0300442   ), Coef('Var'  , 0.0572041   ), Coef('Var'  , 0.1523      ), Coef('Var'  , 0.0907213   ), Coef('Var'  , 0.0450026   ), ], 
		[Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.232653    ), Coef('Var'  , 0.226423    ), Coef('Var'  , 0.26604     ), Coef('Var'  , 0.435945    ), Coef('Var'  , 0.709162    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.360483    ), Coef('Var'  , 0.224662    ), Coef('Var'  , 0.202931    ), Coef('Var'  , 0.104079    ), Coef('Var'  , 0.0527738   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.239393    ), Coef('Var'  , 0.23921     ), Coef('Var'  , 0.147663    ), Coef('Var'  , 0.107167    ), Coef('Var'  , 0.0539706   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.031033    ), Coef('Var'  , 0.0584778   ), Coef('Var'  , 0.0958162   ), Coef('Var'  , 0.0494536   ), Coef('Var'  , 0.0272474   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0361715   ), Coef('Var'  , 0.0665863   ), Coef('Var'  , 0.0452018   ), Coef('Var'  , 0.0622771   ), Coef('Var'  , 0.0344554   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0409347   ), Coef('Var'  , 0.0729176   ), Coef('Var'  , 0.0449047   ), Coef('Var'  , 0.0657906   ), Coef('Var'  , 0.0363181   ), ], ])
	etat3.initMat[Chem([Sub('3')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0285131   ), Coef('Var'  , 0.0515997   ), Coef('Var'  , 0.00169553  ), Coef('Var'  , 0.0545192   ), Coef('Var'  , 0.0292876   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0313601   ), Coef('Var'  , 0.0564878   ), Coef('Var'  , 0.0790215   ), Coef('Var'  , 0.0572041   ), Coef('Var'  , 0.0300442   ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0415688   ), Coef('Var'  , 0.0852764   ), Coef('Var'  , 0.16239     ), Coef('Var'  , 0.226423    ), Coef('Var'  , 0.232653    ), ], 
		[Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Var'  , 0.0444871   ), Coef('Var'  , 0.0899882   ), Coef('Var'  , 0.189076    ), Coef('Var'  , 0.224662    ), Coef('Var'  , 0.360483    ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Var'  , 0.713397    ), Coef('Var'  , 0.444853    ), Coef('Var'  , 0.211673    ), Coef('Var'  , 0.23921     ), Coef('Var'  , 0.239393    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0491457   ), Coef('Var'  , 0.098091    ), Coef('Var'  , 0.166226    ), Coef('Var'  , 0.0584778   ), Coef('Var'  , 0.031033    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0476095   ), Coef('Var'  , 0.09544     ), Coef('Var'  , 0.122352    ), Coef('Var'  , 0.0665863   ), Coef('Var'  , 0.0361715   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0439191   ), Coef('Var'  , 0.078264    ), Coef('Var'  , 0.0675666   ), Coef('Var'  , 0.0729176   ), Coef('Var'  , 0.0409347   ), ], ])
	etat3.initMat[Chem([Sub('4')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0308624   ), Coef('Var'  , 0.0578592   ), Coef('Var'  , 0.0196167   ), Coef('Var'  , 0.0515997   ), Coef('Var'  , 0.0285131   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0344469   ), Coef('Var'  , 0.0606304   ), Coef('Var'  , 0.0408736   ), Coef('Var'  , 0.0564878   ), Coef('Var'  , 0.0313601   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0280886   ), Coef('Var'  , 0.052623    ), Coef('Var'  , 0.0651977   ), Coef('Var'  , 0.0852764   ), Coef('Var'  , 0.0415688   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0275547   ), Coef('Var'  , 0.052039    ), Coef('Var'  , 0.151148    ), Coef('Var'  , 0.0899882   ), Coef('Var'  , 0.0444871   ), ], 
		[Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.234359    ), Coef('Var'  , 0.231683    ), Coef('Var'  , 0.225364    ), Coef('Var'  , 0.444853    ), Coef('Var'  , 0.713397    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.365045    ), Coef('Var'  , 0.231478    ), Coef('Var'  , 0.204126    ), Coef('Var'  , 0.098091    ), Coef('Var'  , 0.0491457   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.234122    ), Coef('Var'  , 0.230214    ), Coef('Var'  , 0.184066    ), Coef('Var'  , 0.09544     ), Coef('Var'  , 0.0476095   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.045521    ), Coef('Var'  , 0.0834746   ), Coef('Var'  , 0.109608    ), Coef('Var'  , 0.078264    ), Coef('Var'  , 0.0439191   ), ], ])
	etat3.initMat[Chem([Sub('5')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0461724   ), Coef('Var'  , 0.09303     ), Coef('Var'  , 0.0914915   ), Coef('Var'  , 0.0578592   ), Coef('Var'  , 0.0308624   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0331322   ), Coef('Var'  , 0.0591986   ), Coef('Var'  , 0.0474166   ), Coef('Var'  , 0.0606304   ), Coef('Var'  , 0.0344469   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.026387    ), Coef('Var'  , 0.0469878   ), Coef('Var'  , 0.0019393   ), Coef('Var'  , 0.052623    ), Coef('Var'  , 0.0280886   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0244269   ), Coef('Var'  , 0.0454338   ), Coef('Var'  , 0.100867    ), Coef('Var'  , 0.052039    ), Coef('Var'  , 0.0275547   ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0501933   ), Coef('Var'  , 0.101093    ), Coef('Var'  , 0.186721    ), Coef('Var'  , 0.231683    ), Coef('Var'  , 0.234359    ), ], 
		[Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Var'  , 0.0515083   ), Coef('Var'  , 0.101385    ), Coef('Var'  , 0.19993     ), Coef('Var'  , 0.231478    ), Coef('Var'  , 0.365045    ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Var'  , 0.711006    ), Coef('Var'  , 0.440704    ), Coef('Var'  , 0.213323    ), Coef('Var'  , 0.230214    ), Coef('Var'  , 0.234122    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0571743   ), Coef('Var'  , 0.112167    ), Coef('Var'  , 0.158312    ), Coef('Var'  , 0.0834746   ), Coef('Var'  , 0.045521    ), ], ])
	etat3.initMat[Chem([Sub('6')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.237085    ), Coef('Var'  , 0.234178    ), Coef('Var'  , 0.179629    ), Coef('Var'  , 0.09303     ), Coef('Var'  , 0.0461724   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0316021   ), Coef('Var'  , 0.0596784   ), Coef('Var'  , 0.0887219   ), Coef('Var'  , 0.0591986   ), Coef('Var'  , 0.0331322   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0245244   ), Coef('Var'  , 0.0462458   ), Coef('Var'  ,-0.00751215  ), Coef('Var'  , 0.0469878   ), Coef('Var'  , 0.026387    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0288878   ), Coef('Var'  , 0.0523687   ), Coef('Var'  , 0.0604527   ), Coef('Var'  , 0.0454338   ), Coef('Var'  , 0.0244269   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0453103   ), Coef('Var'  , 0.0820093   ), Coef('Var'  , 0.119819    ), Coef('Var'  , 0.101093    ), Coef('Var'  , 0.0501933   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0319609   ), Coef('Var'  , 0.0602393   ), Coef('Var'  , 0.162198    ), Coef('Var'  , 0.101385    ), Coef('Var'  , 0.0515083   ), ], 
		[Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.235131    ), Coef('Var'  , 0.231593    ), Coef('Var'  , 0.203669    ), Coef('Var'  , 0.440704    ), Coef('Var'  , 0.711006    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.365499    ), Coef('Var'  , 0.233687    ), Coef('Var'  , 0.193022    ), Coef('Var'  , 0.112167    ), Coef('Var'  , 0.0571743   ), ], ])
	etat3.initMat[Chem([Sub('7')])] = FMat([
		[Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Var'  , 0.712679    ), Coef('Var'  , 0.442764    ), Coef('Var'  , 0.261323    ), Coef('Var'  , 0.234178    ), Coef('Var'  , 0.237085    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0450424   ), Coef('Var'  , 0.0911752   ), Coef('Var'  , 0.155608    ), Coef('Var'  , 0.0596784   ), Coef('Var'  , 0.0316021   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0347185   ), Coef('Var'  , 0.07397     ), Coef('Var'  , 0.0422669   ), Coef('Var'  , 0.0462458   ), Coef('Var'  , 0.0245244   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0360949   ), Coef('Var'  , 0.0639296   ), Coef('Var'  , 0.0412492   ), Coef('Var'  , 0.0523687   ), Coef('Var'  , 0.0288878   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0462348   ), Coef('Var'  , 0.0821493   ), Coef('Var'  , 0.0410362   ), Coef('Var'  , 0.0820093   ), Coef('Var'  , 0.0453103   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0269763   ), Coef('Var'  , 0.0493168   ), Coef('Var'  , 0.0992232   ), Coef('Var'  , 0.0602393   ), Coef('Var'  , 0.0319609   ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0478873   ), Coef('Var'  , 0.0959681   ), Coef('Var'  , 0.155595    ), Coef('Var'  , 0.231593    ), Coef('Var'  , 0.235131    ), ], 
		[Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Var'  , 0.0503666   ), Coef('Var'  , 0.100727    ), Coef('Var'  , 0.203698    ), Coef('Var'  , 0.233687    ), Coef('Var'  , 0.365499    ), ], ])
	
	
	
	etat4.bords   = {Bord('0'): etat5, Bord('1'): etat5, }
	etat4.permuts = {Permut('0'): etat4, }
	etat4.interns = {Intern('_'): etat4, }
	etat4.subs    = {Sub('0'): etat4, Sub('G', True): Etat.etatPoint, Sub('1'): etat4, }
	
	etat4.buildIntern()
	etat4.fm_[Permut('0')] = PMat(3, [2, 1, 0, ])
	
	
	etat4.eqs = [
		(Chem([Permut('0'), Bord('0'), ])	,	Chem([Bord('1')])),
		(Chem([Permut('0'), Bord('1'), ])	,	Chem([Bord('0')])),
		(Chem([Permut('0'), Intern(''), ])	,	Chem([Intern('')])),
		(Chem([Permut('0'), Sub('0'), ])	,	Chem([Sub('1'), Permut('0'), ])),
		(Chem([Permut('0'), Sub('1'), ])	,	Chem([Sub('0'), Permut('0'), ])),
		]
	
	
	etat4.prim.elems = [Figure(1, [Chem([Bord('0')]), Chem([Bord('1')]), ])]
	etat4.grid.elems = [Figure(1, [Chem([Bord('0')]), Chem([Intern('')]), Chem([Bord('1')]), ])]
	
	
	etat4.space = [Chem([Bord('0'), Intern('0'), Intern('0'), ]), Chem([Intern('0'), Intern('0'), ]), Chem([Bord('1'), Intern('0'), Intern('0'), ]), ]
	
	etat4.initMat[Chem([Sub('0')])] = FMat([
		[Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), ], ])
	etat4.initMat[Chem([Sub('G')])] = FMat([
		[Coef('Const', 0           )], 
		[Coef('Const', 1           )], 
		[Coef('Const', 0           )], ])
	etat4.initMat[Chem([Sub('1')])] = FMat([
		[Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), ], ])
	
	
	
	etat5.bords   = {}
	etat5.permuts = {}
	etat5.interns = {Intern('_'): etat5, }
	etat5.subs    = {Sub('0'): etat5, Sub('G', True): Etat.etatPoint, }
	
	etat5.buildIntern()
	
	
	etat5.eqs = [
		]
	
	
	etat5.prim.elems = []
	etat5.grid.elems = []
	
	
	etat5.space = [Chem([Intern('0'), Intern('0'), ])]
	
	etat5.initMat[Chem([Sub('0')])] = FMat([[Coef('Var'  , 1           )]])
	etat5.initMat[Chem([Sub('G')])] = FMat([[Coef('Const', 1           )]])
	
	
	
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
