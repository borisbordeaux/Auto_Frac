# -*- coding: utf-8 -*-

# Automatically generated, from file : octahedron.py, function : modele()

from __future__ import division
import sys
if './../../../../../python' not in sys.path:
	sys.path.append('./../../../../../python')
from etat import *

def modele():
	
	etat0 = EtatInit()
	etat1 = Etat('Cell_0',0)
	etat2 = Etat('Cell_1',0)
	etat3 = Etat('Cell_2',0)
	etat4 = Etat('Cell_3',0)
	etat5 = Etat('Cell_4',0)
	etat6 = Etat('Cell_5',0)
	etat7 = Etat('Cell_6',0)
	etat8 = Etat('Cell_7',0)
	etat9 = Etat('B3',1)
	etat10 = Etat('s',1)
	
	
	etat0.subs   = {Sub('0'): etat1, Sub('1'): etat2, Sub('2'): etat3, Sub('3'): etat4, Sub('4'): etat5, Sub('5'): etat6, Sub('6'): etat7, Sub('7'): etat8, }
	
	etat0.eqs = [
		(Chem([Sub('0'), Bord('0'), Bord('1'), ])	,	Chem([Sub('3'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('1'), Bord('1'), ])	,	Chem([Sub('4'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('2'), Bord('1'), ])	,	Chem([Sub('1'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('1'), Bord('1'), ])	,	Chem([Sub('5'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('2'), Bord('1'), ])	,	Chem([Sub('2'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('1'), Bord('1'), ])	,	Chem([Sub('6'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('2'), Bord('1'), ])	,	Chem([Sub('3'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('3'), Bord('1'), Bord('1'), ])	,	Chem([Sub('7'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('4'), Bord('1'), Bord('1'), ])	,	Chem([Sub('7'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('4'), Bord('2'), Bord('1'), ])	,	Chem([Sub('5'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('5'), Bord('2'), Bord('1'), ])	,	Chem([Sub('6'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('6'), Bord('2'), Bord('1'), ])	,	Chem([Sub('7'), Bord('1'), Bord('1'), ])),
		]
	
	
	etat0.space = []
	
	etat0.initMat[Chem([Sub('0')])] = FMat([
		[Coef('Var'  ,-1.38196     ), Coef('Var'  ,-1.95649     ), Coef('Var'  ,-2.03989     ), Coef('Var'  ,-2.73662     ), Coef('Var'  ,-2.42793     ), Coef('Var'  ,-2.26163     ), ], 
		[Coef('Var'  ,-1.65421     ), Coef('Var'  ,-2.06216     ), Coef('Var'  ,-1.55937     ), Coef('Var'  ,-0.604894    ), Coef('Var'  , 0.329199    ), Coef('Var'  ,-0.68015     ), ], 
		[Coef('Var'  , 1.03987     ), Coef('Var'  , 2.15117     ), Coef('Var'  , 3.37011     ), Coef('Var'  , 2.78614     ), Coef('Var'  , 1.90306     ), Coef('Var'  , 1.08355     ), ], 
		[Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), ], ])
	etat0.initMat[Chem([Sub('1')])] = FMat([
		[Coef('Var'  , 0.865046    ), Coef('Var'  ,-0.329731    ), Coef('Var'  ,-1.38196     ), Coef('Var'  ,-0.614106    ), Coef('Var'  , 0.487533    ), Coef('Var'  , 1.05129     ), ], 
		[Coef('Var'  ,-2.20412     ), Coef('Var'  ,-2.41664     ), Coef('Var'  ,-1.65421     ), Coef('Var'  ,-1.05005     ), Coef('Var'  ,-0.338449    ), Coef('Var'  ,-1.46869     ), ], 
		[Coef('Var'  , 1.76052     ), Coef('Var'  , 1.24077     ), Coef('Var'  , 1.03987     ), Coef('Var'  , 0.159429    ), Coef('Var'  , 0.277226    ), Coef('Var'  , 0.681102    ), ], 
		[Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), ], ])
	etat0.initMat[Chem([Sub('2')])] = FMat([
		[Coef('Var'  , 0.204433    ), Coef('Var'  , 0.560854    ), Coef('Var'  , 0.865046    ), Coef('Var'  , 1.90045     ), Coef('Var'  , 2.0558      ), Coef('Var'  , 1.43708     ), ], 
		[Coef('Var'  ,-2.09905     ), Coef('Var'  ,-2.67055     ), Coef('Var'  ,-2.20412     ), Coef('Var'  ,-1.69181     ), Coef('Var'  ,-0.763111    ), Coef('Var'  ,-1.63177     ), ], 
		[Coef('Var'  , 4.08        ), Coef('Var'  , 2.95014     ), Coef('Var'  , 1.76052     ), Coef('Var'  , 2.3772      ), Coef('Var'  , 3.29562     ), Coef('Var'  , 4.07453     ), ], 
		[Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), ], ])
	etat0.initMat[Chem([Sub('3')])] = FMat([
		[Coef('Var'  ,-2.03989     ), Coef('Var'  ,-1.07185     ), Coef('Var'  , 0.204433    ), Coef('Var'  ,-0.197029    ), Coef('Var'  ,-0.852571    ), Coef('Var'  ,-1.84408     ), ], 
		[Coef('Var'  ,-1.55937     ), Coef('Var'  ,-2.31578     ), Coef('Var'  ,-2.09905     ), Coef('Var'  ,-1.25104     ), Coef('Var'  ,-0.109299    ), Coef('Var'  ,-0.854828    ), ], 
		[Coef('Var'  , 3.37011     ), Coef('Var'  , 3.84574     ), Coef('Var'  , 4.08        ), Coef('Var'  , 5.0001      ), Coef('Var'  , 4.93978     ), Coef('Var'  , 4.47332     ), ], 
		[Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), ], ])
	etat0.initMat[Chem([Sub('4')])] = FMat([
		[Coef('Var'  ,-0.567028    ), Coef('Var'  ,-1.78837     ), Coef('Var'  ,-2.42793     ), Coef('Var'  ,-2.29618     ), Coef('Var'  ,-1.25584     ), Coef('Var'  ,-0.921872    ), ], 
		[Coef('Var'  , 1.65064     ), Coef('Var'  , 1.17463     ), Coef('Var'  , 0.329199    ), Coef('Var'  , 1.25743     ), Coef('Var'  , 1.76321     ), Coef('Var'  , 2.22849     ), ], 
		[Coef('Var'  , 1.1346      ), Coef('Var'  , 1.12462     ), Coef('Var'  , 1.90306     ), Coef('Var'  , 2.83134     ), Coef('Var'  , 3.4559      ), Coef('Var'  , 2.26493     ), ], 
		[Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), ], ])
	etat0.initMat[Chem([Sub('5')])] = FMat([
		[Coef('Var'  , 1.67815     ), Coef('Var'  , 1.48744     ), Coef('Var'  , 0.487533    ), Coef('Var'  ,-0.164786    ), Coef('Var'  ,-0.567028    ), Coef('Var'  , 0.714489    ), ], 
		[Coef('Var'  , 1.10938     ), Coef('Var'  , 0.405855    ), Coef('Var'  ,-0.338449    ), Coef('Var'  , 0.807131    ), Coef('Var'  , 1.65064     ), Coef('Var'  , 1.86926     ), ], 
		[Coef('Var'  , 1.80598     ), Coef('Var'  , 0.704247    ), Coef('Var'  , 0.277226    ), Coef('Var'  , 0.205779    ), Coef('Var'  , 1.1346      ), Coef('Var'  , 1.33397     ), ], 
		[Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), ], ])
	etat0.initMat[Chem([Sub('6')])] = FMat([
		[Coef('Var'  , 0.992783    ), Coef('Var'  , 1.85956     ), Coef('Var'  , 2.0558      ), Coef('Var'  , 2.37036     ), Coef('Var'  , 1.67815     ), Coef('Var'  , 1.58917     ), ], 
		[Coef('Var'  , 1.22903     ), Coef('Var'  , 0.244944    ), Coef('Var'  ,-0.763111    ), Coef('Var'  , 0.158982    ), Coef('Var'  , 1.10938     ), Coef('Var'  , 1.63261     ), ], 
		[Coef('Var'  , 4.12701     ), Coef('Var'  , 4.10928     ), Coef('Var'  , 3.29562     ), Coef('Var'  , 2.40095     ), Coef('Var'  , 1.80598     ), Coef('Var'  , 3.01476     ), ], 
		[Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), ], ])
	etat0.initMat[Chem([Sub('7')])] = FMat([
		[Coef('Var'  ,-1.25584     ), Coef('Var'  ,-1.42323     ), Coef('Var'  ,-0.852571    ), Coef('Var'  , 0.239915    ), Coef('Var'  , 0.992783    ), Coef('Var'  ,-0.0610586   ), ], 
		[Coef('Var'  , 1.76321     ), Coef('Var'  , 1.0093      ), Coef('Var'  ,-0.109299    ), Coef('Var'  , 0.626154    ), Coef('Var'  , 1.22903     ), Coef('Var'  , 1.99184     ), ], 
		[Coef('Var'  , 3.4559      ), Coef('Var'  , 4.53715     ), Coef('Var'  , 4.93978     ), Coef('Var'  , 5.03391     ), Coef('Var'  , 4.12701     ), Coef('Var'  , 3.94688     ), ], 
		[Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), ], ])
	
	
	
	etat1.bords   = {Bord('0'): etat9, Bord('1'): etat9, Bord('2'): etat9, }
	etat1.permuts = {}
	etat1.interns = {Intern('_'): etat1, }
	etat1.subs    = {Sub('0'): etat2, Sub('1'): etat3, Sub('2'): etat4, Sub('3'): etat5, Sub('G', True): Etat.etatPoint, Sub('4'): etat6, Sub('5'): etat7, Sub('6'): etat8, }
	
	etat1.buildIntern()
	
	
	etat1.eqs = [
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
	
	
	etat1.prim.elems = [Figure(2, [Chem([Bord('0'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('0'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('0'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('0'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('1'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('1'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('1'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('1'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('2'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('2'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('2'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('2'), Sub('1'), Sub('1'), Bord('0'), ]), ])]
	etat1.grid.elems = [
		Figure(1, [Chem([Bord('1'), Bord('0'), ]), Chem([Bord('1'), Intern(''), ]), Chem([Bord('1'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('2'), Bord('0'), ]), Chem([Bord('2'), Intern(''), ]), Chem([Bord('2'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('0'), Bord('0'), ]), Chem([Bord('0'), Intern(''), ]), Chem([Bord('0'), Bord('1'), ]), ]), ]
	
	
	etat1.space = [Chem([Bord('2'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('2'), Intern('0'), Intern('0'), ]), ]
	
	etat1.initMat[Chem([Sub('0')])] = FMat([
		[Coef('Const', 0.444444    ), Coef('Const', 0.666667    ), Coef('Const', 1           ), Coef('Const', 0.666667    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.444445    ), ], 
		[Coef('Const', 0.444444    ), Coef('Const', 0.333333    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.222222    ), ], 
		[Coef('Const', 0.111111    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0555555   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  ,-4.5879e-08  ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.111111    ), Coef('Var'  , 0.0555553   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.333333    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.222222    ), ], ])
	etat1.initMat[Chem([Sub('1')])] = FMat([
		[Coef('Const', 0.111111    ), Coef('Const', 0.222222    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.329857    ), Coef('Var'  , 0.21691     ), Coef('Var'  , 0.163191    ), ], 
		[Coef('Const', 0.444444    ), Coef('Const', 0.555556    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.356527    ), Coef('Var'  , 0.268871    ), Coef('Var'  , 0.356527    ), ], 
		[Coef('Const', 0.444444    ), Coef('Const', 0.222222    ), Coef('Const', 0.111111    ), Coef('Var'  , 0.162898    ), Coef('Var'  , 0.215978    ), Coef('Var'  , 0.329565    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0502455   ), Coef('Var'  , 0.0974617   ), Coef('Var'  , 0.0502454   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0628704   ), Coef('Var'  , 0.123235    ), Coef('Var'  , 0.0628704   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0376014   ), Coef('Var'  , 0.0775446   ), Coef('Var'  , 0.0376014   ), ], ])
	etat1.initMat[Chem([Sub('2')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.111111    ), Coef('Var'  , 0.0555554   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.333333    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.222222    ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 1           ), Coef('Const', 0.666667    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.444445    ), Coef('Const', 0.444444    ), Coef('Const', 0.666667    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.222222    ), Coef('Const', 0.444444    ), Coef('Const', 0.333333    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0555556   ), Coef('Const', 0.111111    ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 1.53036e-07 ), Coef('Const', 0           ), Coef('Const', 0           ), ], ])
	etat1.initMat[Chem([Sub('3')])] = FMat([
		[Coef('Const', 0.111111    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0555555   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  ,-2.77706e-07 ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.111111    ), Coef('Var'  , 0.0555553   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.333333    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.222222    ), ], 
		[Coef('Const', 0.444444    ), Coef('Const', 0.666667    ), Coef('Const', 1           ), Coef('Const', 0.666667    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.444445    ), ], 
		[Coef('Const', 0.444444    ), Coef('Const', 0.333333    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.222222    ), ], ])
	etat1.initMat[Chem([Sub('G')])] = FMat([
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], ])
	etat1.initMat[Chem([Sub('4')])] = FMat([
		[Coef('Var'  , 0.217257    ), Coef('Var'  , 0.330204    ), Coef('Const', 0.444444    ), Coef('Const', 0.222222    ), Coef('Const', 0.111111    ), Coef('Var'  , 0.163538    ), ], 
		[Coef('Var'  , 0.0920306   ), Coef('Var'  , 0.0463538   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0463538   ), ], 
		[Coef('Var'  , 0.105773    ), Coef('Var'  , 0.052693    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.052693    ), ], 
		[Coef('Var'  , 0.09679     ), Coef('Var'  , 0.0495738   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0495739   ), ], 
		[Coef('Var'  , 0.234273    ), Coef('Var'  , 0.173908    ), Coef('Const', 0.111111    ), Coef('Const', 0.222222    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.340574    ), ], 
		[Coef('Var'  , 0.253877    ), Coef('Var'  , 0.347267    ), Coef('Const', 0.444444    ), Coef('Const', 0.555556    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.347267    ), ], ])
	etat1.initMat[Chem([Sub('5')])] = FMat([
		[Coef('Var'  , 0.107346    ), Coef('Var'  , 0.161262    ), Coef('Var'  , 0.21691     ), Coef('Var'  , 0.215617    ), Coef('Var'  , 0.217257    ), Coef('Var'  , 0.16161     ), ], 
		[Coef('Var'  , 0.0929649   ), Coef('Var'  , 0.181593    ), Coef('Var'  , 0.268871    ), Coef('Var'  , 0.180659    ), Coef('Var'  , 0.0920306   ), Coef('Var'  , 0.0936421   ), ], 
		[Coef('Var'  , 0.214875    ), Coef('Var'  , 0.213583    ), Coef('Var'  , 0.215978    ), Coef('Var'  , 0.160036    ), Coef('Var'  , 0.105773    ), Coef('Var'  , 0.158933    ), ], 
		[Coef('Var'  , 0.271385    ), Coef('Var'  , 0.185526    ), Coef('Var'  , 0.0974617   ), Coef('Var'  , 0.0998191   ), Coef('Var'  , 0.09679     ), Coef('Var'  , 0.184854    ), ], 
		[Coef('Var'  , 0.23482     ), Coef('Var'  , 0.18177     ), Coef('Var'  , 0.123235    ), Coef('Var'  , 0.181222    ), Coef('Var'  , 0.234273    ), Coef('Var'  , 0.237251    ), ], 
		[Coef('Var'  , 0.078608    ), Coef('Var'  , 0.0762662   ), Coef('Var'  , 0.0775446   ), Coef('Var'  , 0.162646    ), Coef('Var'  , 0.253877    ), Coef('Var'  , 0.16371     ), ], ])
	etat1.initMat[Chem([Sub('6')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0536276   ), Coef('Var'  , 0.107346    ), Coef('Var'  , 0.0536274   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0472883   ), Coef('Var'  , 0.0929649   ), Coef('Var'  , 0.0472881   ), ], 
		[Coef('Const', 0.111111    ), Coef('Const', 0.222222    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.328462    ), Coef('Var'  , 0.214875    ), Coef('Var'  , 0.161796    ), ], 
		[Coef('Const', 0.444444    ), Coef('Const', 0.555556    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.357503    ), Coef('Var'  , 0.271385    ), Coef('Var'  , 0.357503    ), ], 
		[Coef('Const', 0.444444    ), Coef('Const', 0.222222    ), Coef('Const', 0.111111    ), Coef('Var'  , 0.174455    ), Coef('Var'  , 0.23482     ), Coef('Var'  , 0.341122    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0386648   ), Coef('Var'  , 0.078608    ), Coef('Var'  , 0.0386648   ), ], ])
	
	
	
	etat2.bords   = {Bord('0'): etat9, Bord('1'): etat9, Bord('2'): etat9, }
	etat2.permuts = {}
	etat2.interns = {Intern('_'): etat2, }
	etat2.subs    = {Sub('0'): etat1, Sub('1'): etat3, Sub('2'): etat4, Sub('3'): etat5, Sub('G', True): Etat.etatPoint, Sub('4'): etat6, Sub('5'): etat7, Sub('6'): etat8, }
	
	etat2.buildIntern()
	
	
	etat2.eqs = [
		(Chem([Bord('0'), Sub('2'), Permut('0'), ])	,	Chem([Sub('0'), Bord('0'), ])),
		(Chem([Bord('1'), Sub('0'), Permut('0'), ])	,	Chem([Sub('0'), Bord('2'), ])),
		(Chem([Bord('0'), Sub('0'), Permut('0'), ])	,	Chem([Sub('1'), Bord('0'), ])),
		(Chem([Bord('2'), Sub('2'), Permut('0'), ])	,	Chem([Sub('1'), Bord('1'), ])),
		(Chem([Bord('0'), Sub('1'), Permut('0'), ])	,	Chem([Sub('2'), Bord('0'), ])),
		(Chem([Bord('1'), Sub('1'), Permut('0'), ])	,	Chem([Sub('3'), Bord('0'), ])),
		(Chem([Bord('2'), Sub('0'), Permut('0'), ])	,	Chem([Sub('4'), Bord('0'), ])),
		(Chem([Bord('1'), Sub('2'), Permut('0'), ])	,	Chem([Sub('4'), Bord('1'), ])),
		(Chem([Bord('2'), Sub('1'), Permut('0'), ])	,	Chem([Sub('5'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('0'), Bord('1'), ])	,	Chem([Sub('2'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('1'), Bord('1'), ])	,	Chem([Sub('3'), Bord('0'), Bord('1'), ])),
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
	
	
	etat2.prim.elems = [Figure(2, [Chem([Bord('0'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('0'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('0'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('0'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('1'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('1'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('1'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('1'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('2'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('2'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('2'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('2'), Sub('1'), Sub('1'), Bord('0'), ]), ])]
	etat2.grid.elems = [
		Figure(1, [Chem([Bord('1'), Bord('0'), ]), Chem([Bord('1'), Intern(''), ]), Chem([Bord('1'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('2'), Bord('0'), ]), Chem([Bord('2'), Intern(''), ]), Chem([Bord('2'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('0'), Bord('0'), ]), Chem([Bord('0'), Intern(''), ]), Chem([Bord('0'), Bord('1'), ]), ]), ]
	
	
	etat2.space = [Chem([Bord('2'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('2'), Intern('0'), Intern('0'), ]), ]
	
	etat2.initMat[Chem([Sub('0')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.111111    ), Coef('Var'  , 0.0555556   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.333333    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.222222    ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 1           ), Coef('Const', 0.666667    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.444445    ), Coef('Const', 0.444444    ), Coef('Const', 0.666667    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.222222    ), Coef('Const', 0.444444    ), Coef('Const', 0.333333    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0555555   ), Coef('Const', 0.111111    ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  ,-8.19883e-08 ), Coef('Const', 0           ), Coef('Const', 0           ), ], ])
	etat2.initMat[Chem([Sub('1')])] = FMat([
		[Coef('Const', 0.444444    ), Coef('Const', 0.666667    ), Coef('Const', 1           ), Coef('Const', 0.666667    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.444445    ), ], 
		[Coef('Const', 0.444444    ), Coef('Const', 0.333333    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.222222    ), ], 
		[Coef('Const', 0.111111    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0555553   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  ,-6.08444e-08 ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.111111    ), Coef('Var'  , 0.0555555   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.333333    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.222222    ), ], ])
	etat2.initMat[Chem([Sub('2')])] = FMat([
		[Coef('Const', 0.111111    ), Coef('Const', 0.222222    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.336635    ), Coef('Var'  , 0.228059    ), Coef('Var'  , 0.169968    ), ], 
		[Coef('Const', 0.444444    ), Coef('Const', 0.555556    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.358328    ), Coef('Var'  , 0.272146    ), Coef('Var'  , 0.358328    ), ], 
		[Coef('Const', 0.444444    ), Coef('Const', 0.222222    ), Coef('Const', 0.111111    ), Coef('Var'  , 0.161009    ), Coef('Var'  , 0.213794    ), Coef('Var'  , 0.327676    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0462475   ), Coef('Var'  , 0.0915068   ), Coef('Var'  , 0.0462473   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0530352   ), Coef('Var'  , 0.106119    ), Coef('Var'  , 0.0530352   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0447455   ), Coef('Var'  , 0.0883747   ), Coef('Var'  , 0.0447452   ), ], ])
	etat2.initMat[Chem([Sub('3')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0600895   ), Coef('Var'  , 0.11818     ), Coef('Var'  , 0.0600895   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0495188   ), Coef('Var'  , 0.0966703   ), Coef('Var'  , 0.0495187   ), ], 
		[Coef('Const', 0.111111    ), Coef('Const', 0.222222    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.329229    ), Coef('Var'  , 0.215348    ), Coef('Var'  , 0.162562    ), ], 
		[Coef('Const', 0.444444    ), Coef('Const', 0.555556    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.355364    ), Coef('Var'  , 0.26729     ), Coef('Var'  , 0.355364    ), ], 
		[Coef('Const', 0.444444    ), Coef('Const', 0.222222    ), Coef('Const', 0.111111    ), Coef('Var'  , 0.162338    ), Coef('Var'  , 0.215422    ), Coef('Var'  , 0.329005    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0434606   ), Coef('Var'  , 0.0870899   ), Coef('Var'  , 0.0434605   ), ], ])
	etat2.initMat[Chem([Sub('G')])] = FMat([
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], ])
	etat2.initMat[Chem([Sub('4')])] = FMat([
		[Coef('Const', 0.111111    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0555557   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  ,-2.56982e-07 ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.111111    ), Coef('Var'  , 0.0555555   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.333333    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.222222    ), ], 
		[Coef('Const', 0.444444    ), Coef('Const', 0.666667    ), Coef('Const', 1           ), Coef('Const', 0.666667    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.444445    ), ], 
		[Coef('Const', 0.444444    ), Coef('Const', 0.333333    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.222222    ), ], ])
	etat2.initMat[Chem([Sub('5')])] = FMat([
		[Coef('Var'  , 0.2287      ), Coef('Var'  , 0.337276    ), Coef('Const', 0.444444    ), Coef('Const', 0.222222    ), Coef('Const', 0.111111    ), Coef('Var'  , 0.170609    ), ], 
		[Coef('Var'  , 0.0963257   ), Coef('Var'  , 0.049174    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0491742   ), ], 
		[Coef('Var'  , 0.105231    ), Coef('Var'  , 0.052446    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0524458   ), ], 
		[Coef('Var'  , 0.0918782   ), Coef('Var'  , 0.0466188   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0466191   ), ], 
		[Coef('Var'  , 0.215117    ), Coef('Var'  , 0.162033    ), Coef('Const', 0.111111    ), Coef('Const', 0.222222    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.3287      ), ], 
		[Coef('Var'  , 0.262748    ), Coef('Var'  , 0.352452    ), Coef('Const', 0.444444    ), Coef('Const', 0.555556    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.352452    ), ], ])
	etat2.initMat[Chem([Sub('6')])] = FMat([
		[Coef('Var'  , 0.11818     ), Coef('Var'  , 0.174502    ), Coef('Var'  , 0.228059    ), Coef('Var'  , 0.229466    ), Coef('Var'  , 0.2287      ), Coef('Var'  , 0.175143    ), ], 
		[Coef('Var'  , 0.0966703   ), Coef('Var'  , 0.185624    ), Coef('Var'  , 0.272146    ), Coef('Var'  , 0.18528     ), Coef('Var'  , 0.0963257   ), Coef('Var'  , 0.0986932   ), ], 
		[Coef('Var'  , 0.215348    ), Coef('Var'  , 0.212461    ), Coef('Var'  , 0.213794    ), Coef('Var'  , 0.1579      ), Coef('Var'  , 0.105231    ), Coef('Var'  , 0.159453    ), ], 
		[Coef('Var'  , 0.26729     ), Coef('Var'  , 0.179389    ), Coef('Var'  , 0.0915068   ), Coef('Var'  , 0.0928664   ), Coef('Var'  , 0.0918782   ), Coef('Var'  , 0.179761    ), ], 
		[Coef('Var'  , 0.215422    ), Coef('Var'  , 0.159818    ), Coef('Var'  , 0.106119    ), Coef('Var'  , 0.159513    ), Coef('Var'  , 0.215117    ), Coef('Var'  , 0.21326     ), ], 
		[Coef('Var'  , 0.0870899   ), Coef('Var'  , 0.0882061   ), Coef('Var'  , 0.0883747   ), Coef('Var'  , 0.174975    ), Coef('Var'  , 0.262748    ), Coef('Var'  , 0.17369     ), ], ])
	
	
	
	etat3.bords   = {Bord('0'): etat9, Bord('1'): etat9, Bord('2'): etat9, }
	etat3.permuts = {}
	etat3.interns = {Intern('_'): etat3, }
	etat3.subs    = {Sub('0'): etat1, Sub('1'): etat2, Sub('2'): etat4, Sub('3'): etat5, Sub('G', True): Etat.etatPoint, Sub('4'): etat6, Sub('5'): etat7, Sub('6'): etat8, }
	
	etat3.buildIntern()
	
	
	etat3.eqs = [
		(Chem([Bord('0'), Sub('1'), Permut('0'), ])	,	Chem([Sub('0'), Bord('0'), ])),
		(Chem([Bord('0'), Sub('2'), Permut('0'), ])	,	Chem([Sub('1'), Bord('0'), ])),
		(Chem([Bord('1'), Sub('0'), Permut('0'), ])	,	Chem([Sub('1'), Bord('2'), ])),
		(Chem([Bord('0'), Sub('0'), Permut('0'), ])	,	Chem([Sub('2'), Bord('0'), ])),
		(Chem([Bord('2'), Sub('2'), Permut('0'), ])	,	Chem([Sub('2'), Bord('1'), ])),
		(Chem([Bord('1'), Sub('1'), Permut('0'), ])	,	Chem([Sub('4'), Bord('0'), ])),
		(Chem([Bord('2'), Sub('0'), Permut('0'), ])	,	Chem([Sub('5'), Bord('0'), ])),
		(Chem([Bord('1'), Sub('2'), Permut('0'), ])	,	Chem([Sub('5'), Bord('1'), ])),
		(Chem([Bord('2'), Sub('1'), Permut('0'), ])	,	Chem([Sub('6'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('0'), Bord('1'), ])	,	Chem([Sub('2'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('1'), Bord('1'), ])	,	Chem([Sub('3'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('2'), Bord('1'), ])	,	Chem([Sub('1'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('1'), Bord('1'), ])	,	Chem([Sub('4'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('1'), Bord('1'), ])	,	Chem([Sub('6'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('3'), Bord('1'), Bord('1'), ])	,	Chem([Sub('6'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('3'), Bord('2'), Bord('1'), ])	,	Chem([Sub('4'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('4'), Bord('2'), Bord('1'), ])	,	Chem([Sub('5'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('5'), Bord('2'), Bord('1'), ])	,	Chem([Sub('6'), Bord('1'), Bord('1'), ])),
		(Chem([Bord('0'), Bord('1'), ])	,	Chem([Bord('1'), Bord('0'), ])),
		(Chem([Bord('1'), Bord('1'), ])	,	Chem([Bord('2'), Bord('0'), ])),
		(Chem([Bord('2'), Bord('1'), ])	,	Chem([Bord('0'), Bord('0'), ])),
		]
	
	
	etat3.prim.elems = [Figure(2, [Chem([Bord('0'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('0'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('0'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('0'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('1'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('1'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('1'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('1'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('2'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('2'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('2'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('2'), Sub('1'), Sub('1'), Bord('0'), ]), ])]
	etat3.grid.elems = [
		Figure(1, [Chem([Bord('1'), Bord('0'), ]), Chem([Bord('1'), Intern(''), ]), Chem([Bord('1'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('2'), Bord('0'), ]), Chem([Bord('2'), Intern(''), ]), Chem([Bord('2'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('0'), Bord('0'), ]), Chem([Bord('0'), Intern(''), ]), Chem([Bord('0'), Bord('1'), ]), ]), ]
	
	
	etat3.space = [Chem([Bord('2'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('2'), Intern('0'), Intern('0'), ]), ]
	
	etat3.initMat[Chem([Sub('0')])] = FMat([
		[Coef('Const', 0.111111    ), Coef('Const', 0.222222    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.330744    ), Coef('Var'  , 0.218501    ), Coef('Var'  , 0.164078    ), ], 
		[Coef('Const', 0.444444    ), Coef('Const', 0.555556    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.364832    ), Coef('Var'  , 0.282878    ), Coef('Var'  , 0.364832    ), ], 
		[Coef('Const', 0.444444    ), Coef('Const', 0.222222    ), Coef('Const', 0.111111    ), Coef('Var'  , 0.162651    ), Coef('Var'  , 0.215865    ), Coef('Var'  , 0.329318    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0490283   ), Coef('Var'  , 0.0960201   ), Coef('Var'  , 0.0490286   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0529814   ), Coef('Var'  , 0.106219    ), Coef('Var'  , 0.0529811   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0397626   ), Coef('Var'  , 0.0805171   ), Coef('Var'  , 0.0397622   ), ], ])
	etat3.initMat[Chem([Sub('1')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.111111    ), Coef('Var'  , 0.0555553   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.333333    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.222222    ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 1           ), Coef('Const', 0.666667    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.444445    ), Coef('Const', 0.444444    ), Coef('Const', 0.666667    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.222222    ), Coef('Const', 0.444444    ), Coef('Const', 0.333333    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0555557   ), Coef('Const', 0.111111    ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  ,-2.71795e-08 ), Coef('Const', 0           ), Coef('Const', 0           ), ], ])
	etat3.initMat[Chem([Sub('2')])] = FMat([
		[Coef('Const', 0.444444    ), Coef('Const', 0.666667    ), Coef('Const', 1           ), Coef('Const', 0.666667    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.444444    ), ], 
		[Coef('Const', 0.444444    ), Coef('Const', 0.333333    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.222222    ), ], 
		[Coef('Const', 0.111111    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0555556   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  ,-1.14763e-07 ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.111111    ), Coef('Var'  , 0.0555556   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.333333    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.222222    ), ], ])
	etat3.initMat[Chem([Sub('3')])] = FMat([
		[Coef('Var'  , 0.109696    ), Coef('Var'  , 0.163796    ), Coef('Var'  , 0.218501    ), Coef('Var'  , 0.217241    ), Coef('Var'  , 0.218698    ), Coef('Var'  , 0.163993    ), ], 
		[Coef('Var'  , 0.106809    ), Coef('Var'  , 0.198039    ), Coef('Var'  , 0.282878    ), Coef('Var'  , 0.19901     ), Coef('Var'  , 0.10778     ), Coef('Var'  , 0.11183     ), ], 
		[Coef('Var'  , 0.21598     ), Coef('Var'  , 0.214306    ), Coef('Var'  , 0.215865    ), Coef('Var'  , 0.159687    ), Coef('Var'  , 0.105805    ), Coef('Var'  , 0.159802    ), ], 
		[Coef('Var'  , 0.271562    ), Coef('Var'  , 0.184709    ), Coef('Var'  , 0.0960201   ), Coef('Var'  , 0.0983752   ), Coef('Var'  , 0.0963383   ), Coef('Var'  , 0.185027    ), ], 
		[Coef('Var'  , 0.215901    ), Coef('Var'  , 0.160089    ), Coef('Var'  , 0.106219    ), Coef('Var'  , 0.159903    ), Coef('Var'  , 0.215715    ), Coef('Var'  , 0.214029    ), ], 
		[Coef('Var'  , 0.080052    ), Coef('Var'  , 0.0790598   ), Coef('Var'  , 0.0805171   ), Coef('Var'  , 0.165783    ), Coef('Var'  , 0.255665    ), Coef('Var'  , 0.165318    ), ], ])
	etat3.initMat[Chem([Sub('G')])] = FMat([
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], ])
	etat3.initMat[Chem([Sub('4')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0552733   ), Coef('Var'  , 0.109696    ), Coef('Var'  , 0.0552734   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0554296   ), Coef('Var'  , 0.106809    ), Coef('Var'  , 0.0554297   ), ], 
		[Coef('Const', 0.111111    ), Coef('Const', 0.222222    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.329433    ), Coef('Var'  , 0.21598     ), Coef('Var'  , 0.162766    ), ], 
		[Coef('Const', 0.444444    ), Coef('Const', 0.555556    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.357903    ), Coef('Var'  , 0.271562    ), Coef('Var'  , 0.357903    ), ], 
		[Coef('Const', 0.444444    ), Coef('Const', 0.222222    ), Coef('Const', 0.111111    ), Coef('Var'  , 0.162664    ), Coef('Var'  , 0.215901    ), Coef('Var'  , 0.32933     ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0392972   ), Coef('Var'  , 0.080052    ), Coef('Var'  , 0.0392973   ), ], ])
	etat3.initMat[Chem([Sub('5')])] = FMat([
		[Coef('Const', 0.111111    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0555555   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 1.14039e-07 ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.111111    ), Coef('Var'  , 0.0555556   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.333333    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.222222    ), ], 
		[Coef('Const', 0.444444    ), Coef('Const', 0.666667    ), Coef('Const', 1           ), Coef('Const', 0.666667    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.444445    ), ], 
		[Coef('Const', 0.444444    ), Coef('Const', 0.333333    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.222222    ), ], ])
	etat3.initMat[Chem([Sub('6')])] = FMat([
		[Coef('Var'  , 0.218698    ), Coef('Var'  , 0.330942    ), Coef('Const', 0.444444    ), Coef('Const', 0.222222    ), Coef('Const', 0.111111    ), Coef('Var'  , 0.164275    ), ], 
		[Coef('Var'  , 0.10778     ), Coef('Var'  , 0.0564002   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0564006   ), ], 
		[Coef('Var'  , 0.105805    ), Coef('Var'  , 0.0525913   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0525913   ), ], 
		[Coef('Var'  , 0.0963383   ), Coef('Var'  , 0.0493467   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0493467   ), ], 
		[Coef('Var'  , 0.215715    ), Coef('Var'  , 0.162477    ), Coef('Const', 0.111111    ), Coef('Const', 0.222222    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.329143    ), ], 
		[Coef('Var'  , 0.255665    ), Coef('Var'  , 0.348243    ), Coef('Const', 0.444444    ), Coef('Const', 0.555556    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.348243    ), ], ])
	
	
	
	etat4.bords   = {Bord('0'): etat9, Bord('1'): etat9, Bord('2'): etat9, }
	etat4.permuts = {}
	etat4.interns = {Intern('_'): etat4, }
	etat4.subs    = {Sub('0'): etat1, Sub('1'): etat2, Sub('2'): etat3, Sub('3'): etat5, Sub('G', True): Etat.etatPoint, Sub('4'): etat6, Sub('5'): etat7, Sub('6'): etat8, }
	
	etat4.buildIntern()
	
	
	etat4.eqs = [
		(Chem([Bord('0'), Sub('0'), Permut('0'), ])	,	Chem([Sub('0'), Bord('0'), ])),
		(Chem([Bord('2'), Sub('2'), Permut('0'), ])	,	Chem([Sub('0'), Bord('1'), ])),
		(Chem([Bord('0'), Sub('1'), Permut('0'), ])	,	Chem([Sub('1'), Bord('0'), ])),
		(Chem([Bord('0'), Sub('2'), Permut('0'), ])	,	Chem([Sub('2'), Bord('0'), ])),
		(Chem([Bord('1'), Sub('0'), Permut('0'), ])	,	Chem([Sub('2'), Bord('2'), ])),
		(Chem([Bord('2'), Sub('1'), Permut('0'), ])	,	Chem([Sub('3'), Bord('1'), ])),
		(Chem([Bord('1'), Sub('1'), Permut('0'), ])	,	Chem([Sub('5'), Bord('0'), ])),
		(Chem([Bord('2'), Sub('0'), Permut('0'), ])	,	Chem([Sub('6'), Bord('0'), ])),
		(Chem([Bord('1'), Sub('2'), Permut('0'), ])	,	Chem([Sub('6'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('1'), Bord('1'), ])	,	Chem([Sub('3'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('2'), Bord('1'), ])	,	Chem([Sub('1'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('1'), Bord('1'), ])	,	Chem([Sub('4'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('2'), Bord('1'), ])	,	Chem([Sub('2'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('1'), Bord('1'), ])	,	Chem([Sub('5'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('3'), Bord('1'), Bord('1'), ])	,	Chem([Sub('6'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('3'), Bord('2'), Bord('1'), ])	,	Chem([Sub('4'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('4'), Bord('2'), Bord('1'), ])	,	Chem([Sub('5'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('5'), Bord('2'), Bord('1'), ])	,	Chem([Sub('6'), Bord('1'), Bord('1'), ])),
		(Chem([Bord('0'), Bord('1'), ])	,	Chem([Bord('1'), Bord('0'), ])),
		(Chem([Bord('1'), Bord('1'), ])	,	Chem([Bord('2'), Bord('0'), ])),
		(Chem([Bord('2'), Bord('1'), ])	,	Chem([Bord('0'), Bord('0'), ])),
		]
	
	
	etat4.prim.elems = [Figure(2, [Chem([Bord('0'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('0'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('0'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('0'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('1'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('1'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('1'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('1'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('2'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('2'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('2'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('2'), Sub('1'), Sub('1'), Bord('0'), ]), ])]
	etat4.grid.elems = [
		Figure(1, [Chem([Bord('1'), Bord('0'), ]), Chem([Bord('1'), Intern(''), ]), Chem([Bord('1'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('2'), Bord('0'), ]), Chem([Bord('2'), Intern(''), ]), Chem([Bord('2'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('0'), Bord('0'), ]), Chem([Bord('0'), Intern(''), ]), Chem([Bord('0'), Bord('1'), ]), ]), ]
	
	
	etat4.space = [Chem([Bord('2'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('2'), Intern('0'), Intern('0'), ]), ]
	
	etat4.initMat[Chem([Sub('0')])] = FMat([
		[Coef('Const', 0.444444    ), Coef('Const', 0.666667    ), Coef('Const', 1           ), Coef('Const', 0.666667    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.444445    ), ], 
		[Coef('Const', 0.444444    ), Coef('Const', 0.333333    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.222222    ), ], 
		[Coef('Const', 0.111111    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0555556   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  ,-3.3825e-07  ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.111111    ), Coef('Var'  , 0.0555554   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.333333    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.222222    ), ], ])
	etat4.initMat[Chem([Sub('1')])] = FMat([
		[Coef('Const', 0.111111    ), Coef('Const', 0.222222    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.327738    ), Coef('Var'  , 0.213085    ), Coef('Var'  , 0.161071    ), ], 
		[Coef('Const', 0.444444    ), Coef('Const', 0.555556    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.358265    ), Coef('Var'  , 0.271804    ), Coef('Var'  , 0.358266    ), ], 
		[Coef('Const', 0.444444    ), Coef('Const', 0.222222    ), Coef('Const', 0.111111    ), Coef('Var'  , 0.161991    ), Coef('Var'  , 0.214821    ), Coef('Var'  , 0.328658    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0489684   ), Coef('Var'  , 0.0957747   ), Coef('Var'  , 0.0489686   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0519264   ), Coef('Var'  , 0.104848    ), Coef('Var'  , 0.0519263   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0511104   ), Coef('Var'  , 0.0996677   ), Coef('Var'  , 0.0511107   ), ], ])
	etat4.initMat[Chem([Sub('2')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.111111    ), Coef('Var'  , 0.0555556   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.333333    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.222222    ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 1           ), Coef('Const', 0.666667    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.444445    ), Coef('Const', 0.444444    ), Coef('Const', 0.666667    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.222222    ), Coef('Const', 0.444444    ), Coef('Const', 0.333333    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0555555   ), Coef('Const', 0.111111    ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  ,-9.95363e-08 ), Coef('Const', 0           ), Coef('Const', 0           ), ], ])
	etat4.initMat[Chem([Sub('3')])] = FMat([
		[Coef('Var'  , 0.212096    ), Coef('Var'  , 0.326748    ), Coef('Const', 0.444444    ), Coef('Const', 0.222222    ), Coef('Const', 0.111111    ), Coef('Var'  , 0.160081    ), ], 
		[Coef('Var'  , 0.095265    ), Coef('Var'  , 0.0483937   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0483936   ), ], 
		[Coef('Var'  , 0.104895    ), Coef('Var'  , 0.0520659   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.052066    ), ], 
		[Coef('Var'  , 0.0963722   ), Coef('Var'  , 0.0495661   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0495662   ), ], 
		[Coef('Var'  , 0.215311    ), Coef('Var'  , 0.162389    ), Coef('Const', 0.111111    ), Coef('Const', 0.222222    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.329055    ), ], 
		[Coef('Var'  , 0.276061    ), Coef('Var'  , 0.360838    ), Coef('Const', 0.444444    ), Coef('Const', 0.555556    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.360838    ), ], ])
	etat4.initMat[Chem([Sub('G')])] = FMat([
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], ])
	etat4.initMat[Chem([Sub('4')])] = FMat([
		[Coef('Var'  , 0.103299    ), Coef('Var'  , 0.1568      ), Coef('Var'  , 0.213085    ), Coef('Var'  , 0.210041    ), Coef('Var'  , 0.212096    ), Coef('Var'  , 0.155811    ), ], 
		[Coef('Var'  , 0.095932    ), Coef('Var'  , 0.185104    ), Coef('Var'  , 0.271804    ), Coef('Var'  , 0.184437    ), Coef('Var'  , 0.095265    ), Coef('Var'  , 0.0974542   ), ], 
		[Coef('Var'  , 0.214995    ), Coef('Var'  , 0.213046    ), Coef('Var'  , 0.214821    ), Coef('Var'  , 0.158502    ), Coef('Var'  , 0.104895    ), Coef('Var'  , 0.158676    ), ], 
		[Coef('Var'  , 0.270355    ), Coef('Var'  , 0.183628    ), Coef('Var'  , 0.0957747   ), Coef('Var'  , 0.0985344   ), Coef('Var'  , 0.0963722   ), Coef('Var'  , 0.184226    ), ], 
		[Coef('Var'  , 0.21526     ), Coef('Var'  , 0.158709    ), Coef('Var'  , 0.104848    ), Coef('Var'  , 0.15876     ), Coef('Var'  , 0.215311    ), Coef('Var'  , 0.213616    ), ], 
		[Coef('Var'  , 0.100159    ), Coef('Var'  , 0.102713    ), Coef('Var'  , 0.0996677   ), Coef('Var'  , 0.189726    ), Coef('Var'  , 0.276061    ), Coef('Var'  , 0.190218    ), ], ])
	etat4.initMat[Chem([Sub('5')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0512849   ), Coef('Var'  , 0.103299    ), Coef('Var'  , 0.0512847   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0490605   ), Coef('Var'  , 0.095932    ), Coef('Var'  , 0.0490607   ), ], 
		[Coef('Const', 0.111111    ), Coef('Const', 0.222222    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.328832    ), Coef('Var'  , 0.214995    ), Coef('Var'  , 0.162166    ), ], 
		[Coef('Const', 0.444444    ), Coef('Const', 0.555556    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.356882    ), Coef('Var'  , 0.270355    ), Coef('Var'  , 0.356882    ), ], 
		[Coef('Const', 0.444444    ), Coef('Const', 0.222222    ), Coef('Const', 0.111111    ), Coef('Var'  , 0.162338    ), Coef('Var'  , 0.21526     ), Coef('Var'  , 0.329005    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0516022   ), Coef('Var'  , 0.100159    ), Coef('Var'  , 0.0516021   ), ], ])
	etat4.initMat[Chem([Sub('6')])] = FMat([
		[Coef('Const', 0.111111    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0555555   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  ,-1.77847e-07 ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.111111    ), Coef('Var'  , 0.0555555   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.333333    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.222222    ), ], 
		[Coef('Const', 0.444444    ), Coef('Const', 0.666667    ), Coef('Const', 1           ), Coef('Const', 0.666667    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.444444    ), ], 
		[Coef('Const', 0.444444    ), Coef('Const', 0.333333    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.222222    ), ], ])
	
	
	
	etat5.bords   = {Bord('0'): etat9, Bord('1'): etat9, Bord('2'): etat9, }
	etat5.permuts = {}
	etat5.interns = {Intern('_'): etat5, }
	etat5.subs    = {Sub('0'): etat1, Sub('1'): etat2, Sub('2'): etat3, Sub('3'): etat4, Sub('G', True): Etat.etatPoint, Sub('4'): etat6, Sub('5'): etat7, Sub('6'): etat8, }
	
	etat5.buildIntern()
	
	
	etat5.eqs = [
		(Chem([Bord('1'), Sub('0'), Permut('0'), ])	,	Chem([Sub('0'), Bord('1'), ])),
		(Chem([Bord('0'), Sub('2'), Permut('0'), ])	,	Chem([Sub('0'), Bord('2'), ])),
		(Chem([Bord('0'), Sub('1'), Permut('0'), ])	,	Chem([Sub('1'), Bord('1'), ])),
		(Chem([Bord('1'), Sub('1'), Permut('0'), ])	,	Chem([Sub('3'), Bord('2'), ])),
		(Chem([Bord('0'), Sub('0'), Permut('0'), ])	,	Chem([Sub('4'), Bord('1'), ])),
		(Chem([Bord('2'), Sub('2'), Permut('0'), ])	,	Chem([Sub('4'), Bord('2'), ])),
		(Chem([Bord('2'), Sub('1'), Permut('0'), ])	,	Chem([Sub('5'), Bord('2'), ])),
		(Chem([Bord('1'), Sub('2'), Permut('0'), ])	,	Chem([Sub('6'), Bord('0'), ])),
		(Chem([Bord('2'), Sub('0'), Permut('0'), ])	,	Chem([Sub('6'), Bord('2'), ])),
		(Chem([Sub('0'), Bord('0'), Bord('1'), ])	,	Chem([Sub('3'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('2'), Bord('1'), ])	,	Chem([Sub('1'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('1'), Bord('1'), ])	,	Chem([Sub('4'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('2'), Bord('1'), ])	,	Chem([Sub('2'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('1'), Bord('1'), ])	,	Chem([Sub('5'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('2'), Bord('1'), ])	,	Chem([Sub('3'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('3'), Bord('1'), Bord('1'), ])	,	Chem([Sub('6'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('4'), Bord('2'), Bord('1'), ])	,	Chem([Sub('5'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('5'), Bord('2'), Bord('1'), ])	,	Chem([Sub('6'), Bord('1'), Bord('1'), ])),
		(Chem([Bord('0'), Bord('1'), ])	,	Chem([Bord('1'), Bord('0'), ])),
		(Chem([Bord('1'), Bord('1'), ])	,	Chem([Bord('2'), Bord('0'), ])),
		(Chem([Bord('2'), Bord('1'), ])	,	Chem([Bord('0'), Bord('0'), ])),
		]
	
	
	etat5.prim.elems = [Figure(2, [Chem([Bord('0'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('0'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('0'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('0'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('1'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('1'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('1'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('1'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('2'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('2'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('2'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('2'), Sub('1'), Sub('1'), Bord('0'), ]), ])]
	etat5.grid.elems = [
		Figure(1, [Chem([Bord('1'), Bord('0'), ]), Chem([Bord('1'), Intern(''), ]), Chem([Bord('1'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('2'), Bord('0'), ]), Chem([Bord('2'), Intern(''), ]), Chem([Bord('2'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('0'), Bord('0'), ]), Chem([Bord('0'), Intern(''), ]), Chem([Bord('0'), Bord('1'), ]), ]), ]
	
	
	etat5.space = [Chem([Bord('2'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('2'), Intern('0'), Intern('0'), ]), ]
	
	etat5.initMat[Chem([Sub('0')])] = FMat([
		[Coef('Const', 0.111111    ), Coef('Var'  , 0.0555555   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.444444    ), Coef('Var'  , 0.222222    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.333333    ), ], 
		[Coef('Const', 0.444444    ), Coef('Var'  , 0.444445    ), Coef('Const', 0.444444    ), Coef('Const', 0.666667    ), Coef('Const', 1           ), Coef('Const', 0.666667    ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.222222    ), Coef('Const', 0.444444    ), Coef('Const', 0.333333    ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0555554   ), Coef('Const', 0.111111    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  ,-1.36676e-07 ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], ])
	etat5.initMat[Chem([Sub('1')])] = FMat([
		[Coef('Var'  , 0.208419    ), Coef('Var'  , 0.158033    ), Coef('Const', 0.111111    ), Coef('Const', 0.222222    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.324699    ), ], 
		[Coef('Var'  , 0.275796    ), Coef('Var'  , 0.360667    ), Coef('Const', 0.444444    ), Coef('Const', 0.555556    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.360667    ), ], 
		[Coef('Var'  , 0.226442    ), Coef('Var'  , 0.335809    ), Coef('Const', 0.444444    ), Coef('Const', 0.222222    ), Coef('Const', 0.111111    ), Coef('Var'  , 0.169143    ), ], 
		[Coef('Var'  , 0.0939631   ), Coef('Var'  , 0.0477034   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0477035   ), ], 
		[Coef('Var'  , 0.114989    ), Coef('Var'  , 0.0582515   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0582515   ), ], 
		[Coef('Var'  , 0.080391    ), Coef('Var'  , 0.0395364   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0395364   ), ], ])
	etat5.initMat[Chem([Sub('2')])] = FMat([
		[Coef('Var'  , 0.0991499   ), Coef('Var'  , 0.151241    ), Coef('Var'  , 0.208419    ), Coef('Var'  , 0.204999    ), Coef('Var'  , 0.208464    ), Coef('Var'  , 0.151285    ), ], 
		[Coef('Var'  , 0.0995422   ), Coef('Var'  , 0.189523    ), Coef('Var'  , 0.275796    ), Coef('Var'  , 0.189812    ), Coef('Var'  , 0.099831    ), Coef('Var'  , 0.102447    ), ], 
		[Coef('Var'  , 0.226191    ), Coef('Var'  , 0.226923    ), Coef('Var'  , 0.226442    ), Coef('Var'  , 0.172543    ), Coef('Var'  , 0.116255    ), Coef('Var'  , 0.172292    ), ], 
		[Coef('Var'  , 0.269648    ), Coef('Var'  , 0.182203    ), Coef('Var'  , 0.0939631   ), Coef('Var'  , 0.0961559   ), Coef('Var'  , 0.0947125   ), Coef('Var'  , 0.182952    ), ], 
		[Coef('Var'  , 0.225062    ), Coef('Var'  , 0.171021    ), Coef('Var'  , 0.114989    ), Coef('Var'  , 0.170497    ), Coef('Var'  , 0.224538    ), Coef('Var'  , 0.225015    ), ], 
		[Coef('Var'  , 0.080406    ), Coef('Var'  , 0.0790884   ), Coef('Var'  , 0.080391    ), Coef('Var'  , 0.165992    ), Coef('Var'  , 0.256199    ), Coef('Var'  , 0.166007    ), ], ])
	etat5.initMat[Chem([Sub('3')])] = FMat([
		[Coef('Const', 0           ), Coef('Var'  , 0.0487635   ), Coef('Var'  , 0.0991499   ), Coef('Var'  , 0.0487636   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0510792   ), Coef('Var'  , 0.0995422   ), Coef('Var'  , 0.0510793   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.444444    ), Coef('Var'  , 0.335559    ), Coef('Var'  , 0.226191    ), Coef('Var'  , 0.168892    ), Coef('Const', 0.111111    ), Coef('Const', 0.222222    ), ], 
		[Coef('Const', 0.444444    ), Coef('Var'  , 0.356722    ), Coef('Var'  , 0.269648    ), Coef('Var'  , 0.356722    ), Coef('Const', 0.444444    ), Coef('Const', 0.555556    ), ], 
		[Coef('Const', 0.111111    ), Coef('Var'  , 0.168325    ), Coef('Var'  , 0.225062    ), Coef('Var'  , 0.334992    ), Coef('Const', 0.444444    ), Coef('Const', 0.222222    ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0395516   ), Coef('Var'  , 0.080406    ), Coef('Var'  , 0.0395516   ), Coef('Const', 0           ), Coef('Const', 0           ), ], ])
	etat5.initMat[Chem([Sub('G')])] = FMat([
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], ])
	etat5.initMat[Chem([Sub('4')])] = FMat([
		[Coef('Const', 0.444444    ), Coef('Var'  , 0.444445    ), Coef('Const', 0.444444    ), Coef('Const', 0.666667    ), Coef('Const', 1           ), Coef('Const', 0.666667    ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.222222    ), Coef('Const', 0.444444    ), Coef('Const', 0.333333    ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0555554   ), Coef('Const', 0.111111    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 4.59675e-08 ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.111111    ), Coef('Var'  , 0.0555555   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.444444    ), Coef('Var'  , 0.222222    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.333333    ), ], ])
	etat5.initMat[Chem([Sub('5')])] = FMat([
		[Coef('Const', 0.111111    ), Coef('Var'  , 0.158077    ), Coef('Var'  , 0.208464    ), Coef('Var'  , 0.324744    ), Coef('Const', 0.444444    ), Coef('Const', 0.222222    ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.051368    ), Coef('Var'  , 0.099831    ), Coef('Var'  , 0.051368    ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0589561   ), Coef('Var'  , 0.116255    ), Coef('Var'  , 0.0589559   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0484528   ), Coef('Var'  , 0.0947125   ), Coef('Var'  , 0.0484528   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.444444    ), Coef('Var'  , 0.334468    ), Coef('Var'  , 0.224538    ), Coef('Var'  , 0.167801    ), Coef('Const', 0.111111    ), Coef('Const', 0.222222    ), ], 
		[Coef('Const', 0.444444    ), Coef('Var'  , 0.348678    ), Coef('Var'  , 0.256199    ), Coef('Var'  , 0.348678    ), Coef('Const', 0.444444    ), Coef('Const', 0.555556    ), ], ])
	etat5.initMat[Chem([Sub('6')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0555556   ), Coef('Const', 0.111111    ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  ,-7.20238e-08 ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.111111    ), Coef('Var'  , 0.0555557   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.333333    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.222222    ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 1           ), Coef('Const', 0.666667    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.444444    ), Coef('Const', 0.444444    ), Coef('Const', 0.666667    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.222222    ), Coef('Const', 0.444444    ), Coef('Const', 0.333333    ), ], ])
	
	
	
	etat6.bords   = {Bord('0'): etat9, Bord('1'): etat9, Bord('2'): etat9, }
	etat6.permuts = {}
	etat6.interns = {Intern('_'): etat6, }
	etat6.subs    = {Sub('0'): etat1, Sub('1'): etat2, Sub('2'): etat3, Sub('3'): etat4, Sub('G', True): Etat.etatPoint, Sub('4'): etat5, Sub('5'): etat7, Sub('6'): etat8, }
	
	etat6.buildIntern()
	
	
	etat6.eqs = [
		(Chem([Bord('1'), Sub('1'), Permut('0'), ])	,	Chem([Sub('0'), Bord('2'), ])),
		(Chem([Bord('1'), Sub('0'), Permut('0'), ])	,	Chem([Sub('1'), Bord('1'), ])),
		(Chem([Bord('0'), Sub('2'), Permut('0'), ])	,	Chem([Sub('1'), Bord('2'), ])),
		(Chem([Bord('0'), Sub('1'), Permut('0'), ])	,	Chem([Sub('2'), Bord('1'), ])),
		(Chem([Bord('1'), Sub('2'), Permut('0'), ])	,	Chem([Sub('4'), Bord('0'), ])),
		(Chem([Bord('2'), Sub('0'), Permut('0'), ])	,	Chem([Sub('4'), Bord('2'), ])),
		(Chem([Bord('0'), Sub('0'), Permut('0'), ])	,	Chem([Sub('5'), Bord('1'), ])),
		(Chem([Bord('2'), Sub('2'), Permut('0'), ])	,	Chem([Sub('5'), Bord('2'), ])),
		(Chem([Bord('2'), Sub('1'), Permut('0'), ])	,	Chem([Sub('6'), Bord('2'), ])),
		(Chem([Sub('0'), Bord('0'), Bord('1'), ])	,	Chem([Sub('3'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('1'), Bord('1'), ])	,	Chem([Sub('4'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('2'), Bord('1'), ])	,	Chem([Sub('1'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('2'), Bord('1'), ])	,	Chem([Sub('2'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('1'), Bord('1'), ])	,	Chem([Sub('5'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('2'), Bord('1'), ])	,	Chem([Sub('3'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('3'), Bord('1'), Bord('1'), ])	,	Chem([Sub('6'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('4'), Bord('1'), Bord('1'), ])	,	Chem([Sub('6'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('5'), Bord('2'), Bord('1'), ])	,	Chem([Sub('6'), Bord('1'), Bord('1'), ])),
		(Chem([Bord('0'), Bord('1'), ])	,	Chem([Bord('1'), Bord('0'), ])),
		(Chem([Bord('1'), Bord('1'), ])	,	Chem([Bord('2'), Bord('0'), ])),
		(Chem([Bord('2'), Bord('1'), ])	,	Chem([Bord('0'), Bord('0'), ])),
		]
	
	
	etat6.prim.elems = [Figure(2, [Chem([Bord('0'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('0'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('0'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('0'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('1'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('1'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('1'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('1'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('2'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('2'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('2'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('2'), Sub('1'), Sub('1'), Bord('0'), ]), ])]
	etat6.grid.elems = [
		Figure(1, [Chem([Bord('1'), Bord('0'), ]), Chem([Bord('1'), Intern(''), ]), Chem([Bord('1'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('2'), Bord('0'), ]), Chem([Bord('2'), Intern(''), ]), Chem([Bord('2'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('0'), Bord('0'), ]), Chem([Bord('0'), Intern(''), ]), Chem([Bord('0'), Bord('1'), ]), ]), ]
	
	
	etat6.space = [Chem([Bord('2'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('2'), Intern('0'), Intern('0'), ]), ]
	
	etat6.initMat[Chem([Sub('0')])] = FMat([
		[Coef('Const', 0           ), Coef('Var'  , 0.0496273   ), Coef('Var'  , 0.100423    ), Coef('Var'  , 0.0496275   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0492196   ), Coef('Var'  , 0.096361    ), Coef('Var'  , 0.0492192   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.444444    ), Coef('Var'  , 0.330029    ), Coef('Var'  , 0.217227    ), Coef('Var'  , 0.163362    ), Coef('Const', 0.111111    ), Coef('Const', 0.222222    ), ], 
		[Coef('Const', 0.444444    ), Coef('Var'  , 0.361796    ), Coef('Var'  , 0.277886    ), Coef('Var'  , 0.361796    ), Coef('Const', 0.444444    ), Coef('Const', 0.555556    ), ], 
		[Coef('Const', 0.111111    ), Coef('Var'  , 0.164158    ), Coef('Var'  , 0.218499    ), Coef('Var'  , 0.330825    ), Coef('Const', 0.444444    ), Coef('Const', 0.222222    ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0451706   ), Coef('Var'  , 0.089604    ), Coef('Var'  , 0.0451706   ), Coef('Const', 0           ), Coef('Const', 0           ), ], ])
	etat6.initMat[Chem([Sub('1')])] = FMat([
		[Coef('Const', 0.111111    ), Coef('Var'  , 0.0555554   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.444444    ), Coef('Var'  , 0.222222    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.333333    ), ], 
		[Coef('Const', 0.444444    ), Coef('Var'  , 0.444445    ), Coef('Const', 0.444444    ), Coef('Const', 0.666667    ), Coef('Const', 1           ), Coef('Const', 0.666667    ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.222222    ), Coef('Const', 0.444444    ), Coef('Const', 0.333333    ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0555554   ), Coef('Const', 0.111111    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 1.09451e-07 ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], ])
	etat6.initMat[Chem([Sub('2')])] = FMat([
		[Coef('Var'  , 0.209096    ), Coef('Var'  , 0.158301    ), Coef('Const', 0.111111    ), Coef('Const', 0.222222    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.324968    ), ], 
		[Coef('Var'  , 0.272516    ), Coef('Var'  , 0.358708    ), Coef('Const', 0.444444    ), Coef('Const', 0.555556    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.358708    ), ], 
		[Coef('Var'  , 0.217552    ), Coef('Var'  , 0.330355    ), Coef('Const', 0.444444    ), Coef('Const', 0.222222    ), Coef('Const', 0.111111    ), Coef('Var'  , 0.163688    ), ], 
		[Coef('Var'  , 0.10204     ), Coef('Var'  , 0.0526164   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0526164   ), ], 
		[Coef('Var'  , 0.108975    ), Coef('Var'  , 0.0546338   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0546337   ), ], 
		[Coef('Var'  , 0.0898199   ), Coef('Var'  , 0.0453865   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0453864   ), ], ])
	etat6.initMat[Chem([Sub('3')])] = FMat([
		[Coef('Var'  , 0.100423    ), Coef('Var'  , 0.152373    ), Coef('Var'  , 0.209096    ), Coef('Var'  , 0.206035    ), Coef('Var'  , 0.209641    ), Coef('Var'  , 0.152917    ), ], 
		[Coef('Var'  , 0.096361    ), Coef('Var'  , 0.185705    ), Coef('Var'  , 0.272516    ), Coef('Var'  , 0.185533    ), Coef('Var'  , 0.0961887   ), Coef('Var'  , 0.0982669   ), ], 
		[Coef('Var'  , 0.217227    ), Coef('Var'  , 0.21594     ), Coef('Var'  , 0.217552    ), Coef('Var'  , 0.162113    ), Coef('Var'  , 0.107845    ), Coef('Var'  , 0.161788    ), ], 
		[Coef('Var'  , 0.277886    ), Coef('Var'  , 0.19219     ), Coef('Var'  , 0.10204     ), Coef('Var'  , 0.105783    ), Coef('Var'  , 0.10259     ), Coef('Var'  , 0.192739    ), ], 
		[Coef('Var'  , 0.218499    ), Coef('Var'  , 0.163236    ), Coef('Var'  , 0.108975    ), Coef('Var'  , 0.163536    ), Coef('Var'  , 0.2188      ), Coef('Var'  , 0.217505    ), ], 
		[Coef('Var'  , 0.089604    ), Coef('Var'  , 0.0905572   ), Coef('Var'  , 0.0898199   ), Coef('Var'  , 0.177       ), Coef('Var'  , 0.264936    ), Coef('Var'  , 0.176784    ), ], ])
	etat6.initMat[Chem([Sub('G')])] = FMat([
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], ])
	etat6.initMat[Chem([Sub('4')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0555557   ), Coef('Const', 0.111111    ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 1.89976e-09 ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.111111    ), Coef('Var'  , 0.0555557   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.333333    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.222222    ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 1           ), Coef('Const', 0.666667    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.444444    ), Coef('Const', 0.444444    ), Coef('Const', 0.666667    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.222222    ), Coef('Const', 0.444444    ), Coef('Const', 0.333333    ), ], ])
	etat6.initMat[Chem([Sub('5')])] = FMat([
		[Coef('Const', 0.444444    ), Coef('Var'  , 0.444444    ), Coef('Const', 0.444444    ), Coef('Const', 0.666667    ), Coef('Const', 1           ), Coef('Const', 0.666667    ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.222222    ), Coef('Const', 0.444444    ), Coef('Const', 0.333333    ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0555557   ), Coef('Const', 0.111111    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  ,-1.45565e-07 ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.111111    ), Coef('Var'  , 0.0555556   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.444444    ), Coef('Var'  , 0.222222    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.333333    ), ], ])
	etat6.initMat[Chem([Sub('6')])] = FMat([
		[Coef('Const', 0.111111    ), Coef('Var'  , 0.158845    ), Coef('Var'  , 0.209641    ), Coef('Var'  , 0.325512    ), Coef('Const', 0.444444    ), Coef('Const', 0.222222    ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0490475   ), Coef('Var'  , 0.0961887   ), Coef('Var'  , 0.0490472   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0539804   ), Coef('Var'  , 0.107845    ), Coef('Var'  , 0.0539806   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0531661   ), Coef('Var'  , 0.10259     ), Coef('Var'  , 0.053166    ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.444444    ), Coef('Var'  , 0.331125    ), Coef('Var'  , 0.2188      ), Coef('Var'  , 0.164458    ), Coef('Const', 0.111111    ), Coef('Const', 0.222222    ), ], 
		[Coef('Const', 0.444444    ), Coef('Var'  , 0.353836    ), Coef('Var'  , 0.264936    ), Coef('Var'  , 0.353836    ), Coef('Const', 0.444444    ), Coef('Const', 0.555556    ), ], ])
	
	
	
	etat7.bords   = {Bord('0'): etat9, Bord('1'): etat9, Bord('2'): etat9, }
	etat7.permuts = {}
	etat7.interns = {Intern('_'): etat7, }
	etat7.subs    = {Sub('0'): etat1, Sub('1'): etat2, Sub('2'): etat3, Sub('3'): etat4, Sub('G', True): Etat.etatPoint, Sub('4'): etat5, Sub('5'): etat6, Sub('6'): etat8, }
	
	etat7.buildIntern()
	
	
	etat7.eqs = [
		(Chem([Bord('1'), Sub('1'), Permut('0'), ])	,	Chem([Sub('1'), Bord('2'), ])),
		(Chem([Bord('1'), Sub('0'), Permut('0'), ])	,	Chem([Sub('2'), Bord('1'), ])),
		(Chem([Bord('0'), Sub('2'), Permut('0'), ])	,	Chem([Sub('2'), Bord('2'), ])),
		(Chem([Bord('0'), Sub('1'), Permut('0'), ])	,	Chem([Sub('3'), Bord('1'), ])),
		(Chem([Bord('2'), Sub('1'), Permut('0'), ])	,	Chem([Sub('4'), Bord('2'), ])),
		(Chem([Bord('1'), Sub('2'), Permut('0'), ])	,	Chem([Sub('5'), Bord('0'), ])),
		(Chem([Bord('2'), Sub('0'), Permut('0'), ])	,	Chem([Sub('5'), Bord('2'), ])),
		(Chem([Bord('0'), Sub('0'), Permut('0'), ])	,	Chem([Sub('6'), Bord('1'), ])),
		(Chem([Bord('2'), Sub('2'), Permut('0'), ])	,	Chem([Sub('6'), Bord('2'), ])),
		(Chem([Sub('0'), Bord('0'), Bord('1'), ])	,	Chem([Sub('3'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('1'), Bord('1'), ])	,	Chem([Sub('4'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('2'), Bord('1'), ])	,	Chem([Sub('1'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('1'), Bord('1'), ])	,	Chem([Sub('5'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('2'), Bord('1'), ])	,	Chem([Sub('2'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('2'), Bord('1'), ])	,	Chem([Sub('3'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('3'), Bord('1'), Bord('1'), ])	,	Chem([Sub('6'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('4'), Bord('1'), Bord('1'), ])	,	Chem([Sub('6'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('4'), Bord('2'), Bord('1'), ])	,	Chem([Sub('5'), Bord('1'), Bord('1'), ])),
		(Chem([Bord('0'), Bord('1'), ])	,	Chem([Bord('1'), Bord('0'), ])),
		(Chem([Bord('1'), Bord('1'), ])	,	Chem([Bord('2'), Bord('0'), ])),
		(Chem([Bord('2'), Bord('1'), ])	,	Chem([Bord('0'), Bord('0'), ])),
		]
	
	
	etat7.prim.elems = [Figure(2, [Chem([Bord('0'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('0'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('0'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('0'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('1'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('1'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('1'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('1'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('2'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('2'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('2'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('2'), Sub('1'), Sub('1'), Bord('0'), ]), ])]
	etat7.grid.elems = [
		Figure(1, [Chem([Bord('1'), Bord('0'), ]), Chem([Bord('1'), Intern(''), ]), Chem([Bord('1'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('2'), Bord('0'), ]), Chem([Bord('2'), Intern(''), ]), Chem([Bord('2'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('0'), Bord('0'), ]), Chem([Bord('0'), Intern(''), ]), Chem([Bord('0'), Bord('1'), ]), ]), ]
	
	
	etat7.space = [Chem([Bord('2'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('2'), Intern('0'), Intern('0'), ]), ]
	
	etat7.initMat[Chem([Sub('0')])] = FMat([
		[Coef('Var'  , 0.103816    ), Coef('Var'  , 0.156678    ), Coef('Var'  , 0.212884    ), Coef('Var'  , 0.210759    ), Coef('Var'  , 0.213452    ), Coef('Var'  , 0.157246    ), ], 
		[Coef('Var'  , 0.0782347   ), Coef('Var'  , 0.162985    ), Coef('Var'  , 0.253366    ), Coef('Var'  , 0.162568    ), Coef('Var'  , 0.0778169   ), Coef('Var'  , 0.0763253   ), ], 
		[Coef('Var'  , 0.218301    ), Coef('Var'  , 0.217306    ), Coef('Var'  , 0.218511    ), Coef('Var'  , 0.162918    ), Coef('Var'  , 0.108357    ), Coef('Var'  , 0.162708    ), ], 
		[Coef('Var'  , 0.273065    ), Coef('Var'  , 0.18686     ), Coef('Var'  , 0.0980842   ), Coef('Var'  , 0.100872    ), Coef('Var'  , 0.0981877   ), Coef('Var'  , 0.186963    ), ], 
		[Coef('Var'  , 0.213087    ), Coef('Var'  , 0.156566    ), Coef('Var'  , 0.102876    ), Coef('Var'  , 0.155282    ), Coef('Var'  , 0.211803    ), Coef('Var'  , 0.209937    ), ], 
		[Coef('Var'  , 0.113497    ), Coef('Var'  , 0.119605    ), Coef('Var'  , 0.114279    ), Coef('Var'  , 0.207601    ), Coef('Var'  , 0.290382    ), Coef('Var'  , 0.206819    ), ], ])
	etat7.initMat[Chem([Sub('1')])] = FMat([
		[Coef('Const', 0           ), Coef('Var'  , 0.0515826   ), Coef('Var'  , 0.103816    ), Coef('Var'  , 0.0515826   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0383715   ), Coef('Var'  , 0.0782347   ), Coef('Var'  , 0.0383712   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.444444    ), Coef('Var'  , 0.33077     ), Coef('Var'  , 0.218301    ), Coef('Var'  , 0.164104    ), Coef('Const', 0.111111    ), Coef('Const', 0.222222    ), ], 
		[Coef('Const', 0.444444    ), Coef('Var'  , 0.358698    ), Coef('Var'  , 0.273065    ), Coef('Var'  , 0.358698    ), Coef('Const', 0.444444    ), Coef('Const', 0.555556    ), ], 
		[Coef('Const', 0.111111    ), Coef('Var'  , 0.161166    ), Coef('Var'  , 0.213087    ), Coef('Var'  , 0.327833    ), Coef('Const', 0.444444    ), Coef('Const', 0.222222    ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0594115   ), Coef('Var'  , 0.113497    ), Coef('Var'  , 0.0594116   ), Coef('Const', 0           ), Coef('Const', 0           ), ], ])
	etat7.initMat[Chem([Sub('2')])] = FMat([
		[Coef('Const', 0.111111    ), Coef('Var'  , 0.0555552   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.444444    ), Coef('Var'  , 0.222222    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.333333    ), ], 
		[Coef('Const', 0.444444    ), Coef('Var'  , 0.444445    ), Coef('Const', 0.444444    ), Coef('Const', 0.666667    ), Coef('Const', 1           ), Coef('Const', 0.666667    ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.222222    ), Coef('Const', 0.444444    ), Coef('Const', 0.333333    ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0555557   ), Coef('Const', 0.111111    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  ,-1.95217e-07 ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], ])
	etat7.initMat[Chem([Sub('3')])] = FMat([
		[Coef('Var'  , 0.212884    ), Coef('Var'  , 0.160651    ), Coef('Const', 0.111111    ), Coef('Const', 0.222222    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.327318    ), ], 
		[Coef('Var'  , 0.253366    ), Coef('Var'  , 0.346836    ), Coef('Const', 0.444444    ), Coef('Const', 0.555556    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.346836    ), ], 
		[Coef('Var'  , 0.218511    ), Coef('Var'  , 0.330981    ), Coef('Const', 0.444444    ), Coef('Const', 0.222222    ), Coef('Const', 0.111111    ), Coef('Var'  , 0.164314    ), ], 
		[Coef('Var'  , 0.0980842   ), Coef('Var'  , 0.0503839   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.050384    ), ], 
		[Coef('Var'  , 0.102876    ), Coef('Var'  , 0.0509547   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0509547   ), ], 
		[Coef('Var'  , 0.114279    ), Coef('Var'  , 0.0601935   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0601931   ), ], ])
	etat7.initMat[Chem([Sub('G')])] = FMat([
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], ])
	etat7.initMat[Chem([Sub('4')])] = FMat([
		[Coef('Const', 0.111111    ), Coef('Var'  , 0.161219    ), Coef('Var'  , 0.213452    ), Coef('Var'  , 0.327886    ), Coef('Const', 0.444444    ), Coef('Const', 0.222222    ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0379534   ), Coef('Var'  , 0.0778169   ), Coef('Var'  , 0.0379539   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0541602   ), Coef('Var'  , 0.108357    ), Coef('Var'  , 0.0541603   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0504878   ), Coef('Var'  , 0.0981877   ), Coef('Var'  , 0.0504877   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.444444    ), Coef('Var'  , 0.326549    ), Coef('Var'  , 0.211803    ), Coef('Var'  , 0.159882    ), Coef('Const', 0.111111    ), Coef('Const', 0.222222    ), ], 
		[Coef('Const', 0.444444    ), Coef('Var'  , 0.36963     ), Coef('Var'  , 0.290382    ), Coef('Var'  , 0.36963     ), Coef('Const', 0.444444    ), Coef('Const', 0.555556    ), ], ])
	etat7.initMat[Chem([Sub('5')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0555554   ), Coef('Const', 0.111111    ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  ,-1.71957e-07 ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.111111    ), Coef('Var'  , 0.0555556   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.333333    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.222222    ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 1           ), Coef('Const', 0.666667    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.444445    ), Coef('Const', 0.444444    ), Coef('Const', 0.666667    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.222222    ), Coef('Const', 0.444444    ), Coef('Const', 0.333333    ), ], ])
	etat7.initMat[Chem([Sub('6')])] = FMat([
		[Coef('Const', 0.444444    ), Coef('Var'  , 0.444445    ), Coef('Const', 0.444444    ), Coef('Const', 0.666667    ), Coef('Const', 1           ), Coef('Const', 0.666667    ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.222222    ), Coef('Const', 0.444444    ), Coef('Const', 0.333333    ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0555554   ), Coef('Const', 0.111111    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  ,-1.22205e-07 ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.111111    ), Coef('Var'  , 0.0555555   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.444444    ), Coef('Var'  , 0.222222    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.333333    ), ], ])
	
	
	
	etat8.bords   = {Bord('0'): etat9, Bord('1'): etat9, Bord('2'): etat9, }
	etat8.permuts = {}
	etat8.interns = {Intern('_'): etat8, }
	etat8.subs    = {Sub('0'): etat1, Sub('1'): etat2, Sub('2'): etat3, Sub('3'): etat4, Sub('G', True): Etat.etatPoint, Sub('4'): etat5, Sub('5'): etat6, Sub('6'): etat7, }
	
	etat8.buildIntern()
	
	
	etat8.eqs = [
		(Chem([Bord('0'), Sub('1'), Permut('0'), ])	,	Chem([Sub('0'), Bord('1'), ])),
		(Chem([Bord('1'), Sub('1'), Permut('0'), ])	,	Chem([Sub('2'), Bord('2'), ])),
		(Chem([Bord('1'), Sub('0'), Permut('0'), ])	,	Chem([Sub('3'), Bord('1'), ])),
		(Chem([Bord('0'), Sub('2'), Permut('0'), ])	,	Chem([Sub('3'), Bord('2'), ])),
		(Chem([Bord('0'), Sub('0'), Permut('0'), ])	,	Chem([Sub('4'), Bord('1'), ])),
		(Chem([Bord('2'), Sub('2'), Permut('0'), ])	,	Chem([Sub('4'), Bord('2'), ])),
		(Chem([Bord('2'), Sub('1'), Permut('0'), ])	,	Chem([Sub('5'), Bord('2'), ])),
		(Chem([Bord('1'), Sub('2'), Permut('0'), ])	,	Chem([Sub('6'), Bord('0'), ])),
		(Chem([Bord('2'), Sub('0'), Permut('0'), ])	,	Chem([Sub('6'), Bord('2'), ])),
		(Chem([Sub('0'), Bord('0'), Bord('1'), ])	,	Chem([Sub('3'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('1'), Bord('1'), ])	,	Chem([Sub('4'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('2'), Bord('1'), ])	,	Chem([Sub('1'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('1'), Bord('1'), ])	,	Chem([Sub('5'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('2'), Bord('1'), ])	,	Chem([Sub('2'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('1'), Bord('1'), ])	,	Chem([Sub('6'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('2'), Bord('1'), ])	,	Chem([Sub('3'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('4'), Bord('2'), Bord('1'), ])	,	Chem([Sub('5'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('5'), Bord('2'), Bord('1'), ])	,	Chem([Sub('6'), Bord('1'), Bord('1'), ])),
		(Chem([Bord('0'), Bord('1'), ])	,	Chem([Bord('1'), Bord('0'), ])),
		(Chem([Bord('1'), Bord('1'), ])	,	Chem([Bord('2'), Bord('0'), ])),
		(Chem([Bord('2'), Bord('1'), ])	,	Chem([Bord('0'), Bord('0'), ])),
		]
	
	
	etat8.prim.elems = [Figure(2, [Chem([Bord('0'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('0'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('0'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('0'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('1'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('1'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('1'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('1'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('2'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('2'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('2'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('2'), Sub('1'), Sub('1'), Bord('0'), ]), ])]
	etat8.grid.elems = [
		Figure(1, [Chem([Bord('1'), Bord('0'), ]), Chem([Bord('1'), Intern(''), ]), Chem([Bord('1'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('2'), Bord('0'), ]), Chem([Bord('2'), Intern(''), ]), Chem([Bord('2'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('0'), Bord('0'), ]), Chem([Bord('0'), Intern(''), ]), Chem([Bord('0'), Bord('1'), ]), ]), ]
	
	
	etat8.space = [Chem([Bord('2'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('2'), Intern('0'), Intern('0'), ]), ]
	
	etat8.initMat[Chem([Sub('0')])] = FMat([
		[Coef('Var'  , 0.226206    ), Coef('Var'  , 0.169046    ), Coef('Const', 0.111111    ), Coef('Const', 0.222222    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.335712    ), ], 
		[Coef('Var'  , 0.252843    ), Coef('Var'  , 0.34629     ), Coef('Const', 0.444444    ), Coef('Const', 0.555556    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.34629     ), ], 
		[Coef('Var'  , 0.215256    ), Coef('Var'  , 0.329089    ), Coef('Const', 0.444444    ), Coef('Const', 0.222222    ), Coef('Const', 0.111111    ), Coef('Var'  , 0.162423    ), ], 
		[Coef('Var'  , 0.087267    ), Coef('Var'  , 0.043748    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0437482   ), ], 
		[Coef('Var'  , 0.116527    ), Coef('Var'  , 0.0590157   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0590156   ), ], 
		[Coef('Var'  , 0.101901    ), Coef('Var'  , 0.0528111   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0528107   ), ], ])
	etat8.initMat[Chem([Sub('1')])] = FMat([
		[Coef('Var'  , 0.116281    ), Coef('Var'  , 0.172611    ), Coef('Var'  , 0.226206    ), Coef('Var'  , 0.226113    ), Coef('Var'  , 0.225339    ), Coef('Var'  , 0.171743    ), ], 
		[Coef('Var'  , 0.0786631   ), Coef('Var'  , 0.162845    ), Coef('Var'  , 0.252843    ), Coef('Var'  , 0.16227     ), Coef('Var'  , 0.0780884   ), Coef('Var'  , 0.0769787   ), ], 
		[Coef('Var'  , 0.214273    ), Coef('Var'  , 0.212752    ), Coef('Var'  , 0.215256    ), Coef('Var'  , 0.159244    ), Coef('Var'  , 0.105209    ), Coef('Var'  , 0.158261    ), ], 
		[Coef('Var'  , 0.262552    ), Coef('Var'  , 0.173891    ), Coef('Var'  , 0.087267    ), Coef('Var'  , 0.0877798   ), Coef('Var'  , 0.0875508   ), Coef('Var'  , 0.174175    ), ], 
		[Coef('Var'  , 0.227093    ), Coef('Var'  , 0.173042    ), Coef('Var'  , 0.116527    ), Coef('Var'  , 0.172836    ), Coef('Var'  , 0.226887    ), Coef('Var'  , 0.227846    ), ], 
		[Coef('Var'  , 0.101138    ), Coef('Var'  , 0.104859    ), Coef('Var'  , 0.101901    ), Coef('Var'  , 0.191758    ), Coef('Var'  , 0.276927    ), Coef('Var'  , 0.190995    ), ], ])
	etat8.initMat[Chem([Sub('2')])] = FMat([
		[Coef('Const', 0           ), Coef('Var'  , 0.0591205   ), Coef('Var'  , 0.116281    ), Coef('Var'  , 0.0591205   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0387768   ), Coef('Var'  , 0.0786631   ), Coef('Var'  , 0.0387768   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.444444    ), Coef('Var'  , 0.328107    ), Coef('Var'  , 0.214273    ), Coef('Var'  , 0.16144     ), Coef('Const', 0.111111    ), Coef('Const', 0.222222    ), ], 
		[Coef('Const', 0.444444    ), Coef('Var'  , 0.352366    ), Coef('Var'  , 0.262552    ), Coef('Var'  , 0.352366    ), Coef('Const', 0.444444    ), Coef('Const', 0.555556    ), ], 
		[Coef('Const', 0.111111    ), Coef('Var'  , 0.169582    ), Coef('Var'  , 0.227093    ), Coef('Var'  , 0.336248    ), Coef('Const', 0.444444    ), Coef('Const', 0.222222    ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.052048    ), Coef('Var'  , 0.101138    ), Coef('Var'  , 0.0520482   ), Coef('Const', 0           ), Coef('Const', 0           ), ], ])
	etat8.initMat[Chem([Sub('3')])] = FMat([
		[Coef('Const', 0.111111    ), Coef('Var'  , 0.0555555   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.444444    ), Coef('Var'  , 0.222222    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.333333    ), ], 
		[Coef('Const', 0.444444    ), Coef('Var'  , 0.444445    ), Coef('Const', 0.444444    ), Coef('Const', 0.666667    ), Coef('Const', 1           ), Coef('Const', 0.666667    ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.222222    ), Coef('Const', 0.444444    ), Coef('Const', 0.333333    ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0555556   ), Coef('Const', 0.111111    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  ,-2.15742e-07 ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], ])
	etat8.initMat[Chem([Sub('G')])] = FMat([
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], ])
	etat8.initMat[Chem([Sub('4')])] = FMat([
		[Coef('Const', 0.444444    ), Coef('Var'  , 0.444444    ), Coef('Const', 0.444444    ), Coef('Const', 0.666667    ), Coef('Const', 1           ), Coef('Const', 0.666667    ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.222222    ), Coef('Const', 0.444444    ), Coef('Const', 0.333333    ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0555553   ), Coef('Const', 0.111111    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  ,-1.08528e-07 ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.111111    ), Coef('Var'  , 0.0555557   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.444444    ), Coef('Var'  , 0.222222    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.333333    ), ], ])
	etat8.initMat[Chem([Sub('5')])] = FMat([
		[Coef('Const', 0.111111    ), Coef('Var'  , 0.168178    ), Coef('Var'  , 0.225339    ), Coef('Var'  , 0.334845    ), Coef('Const', 0.444444    ), Coef('Const', 0.222222    ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.038202    ), Coef('Var'  , 0.0780884   ), Coef('Var'  , 0.038202    ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0523762   ), Coef('Var'  , 0.105209    ), Coef('Var'  , 0.0523762   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0440318   ), Coef('Var'  , 0.0875508   ), Coef('Var'  , 0.0440316   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.444444    ), Coef('Var'  , 0.336042    ), Coef('Var'  , 0.226887    ), Coef('Var'  , 0.169376    ), Coef('Const', 0.111111    ), Coef('Const', 0.222222    ), ], 
		[Coef('Const', 0.444444    ), Coef('Var'  , 0.361169    ), Coef('Var'  , 0.276927    ), Coef('Var'  , 0.36117     ), Coef('Const', 0.444444    ), Coef('Const', 0.555556    ), ], ])
	etat8.initMat[Chem([Sub('6')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0555553   ), Coef('Const', 0.111111    ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  ,-1.23448e-07 ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.111111    ), Coef('Var'  , 0.0555557   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.333333    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.222222    ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 1           ), Coef('Const', 0.666667    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.444445    ), Coef('Const', 0.444444    ), Coef('Const', 0.666667    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.222222    ), Coef('Const', 0.444444    ), Coef('Const', 0.333333    ), ], ])
	
	
	
	etat9.bords   = {Bord('0'): etat10, Bord('1'): etat10, }
	etat9.permuts = {Permut('0'): etat9, }
	etat9.interns = {Intern('_'): etat9, }
	etat9.subs    = {Sub('0'): etat9, Sub('1'): etat9, Sub('2'): etat9, Sub('G', True): Etat.etatPoint, }
	
	etat9.buildIntern()
	etat9.fm_[Permut('0')] = PMat(3, [2, 1, 0, ])
	
	
	etat9.eqs = [
		(Chem([Permut('0'), Bord('0'), ])	,	Chem([Bord('1')])),
		(Chem([Permut('0'), Bord('1'), ])	,	Chem([Bord('0')])),
		(Chem([Permut('0'), Intern(''), ])	,	Chem([Intern('')])),
		(Chem([Permut('0'), Sub('0'), ])	,	Chem([Sub('2'), Permut('0'), ])),
		(Chem([Permut('0'), Sub('1'), ])	,	Chem([Sub('1'), Permut('0'), ])),
		(Chem([Permut('0'), Sub('2'), ])	,	Chem([Sub('0'), Permut('0'), ])),
		]
	
	
	etat9.prim.elems = [Figure(1, [Chem([Bord('0')]), Chem([Bord('1')]), ])]
	etat9.grid.elems = [Figure(1, [Chem([Bord('0')]), Chem([Intern('')]), Chem([Bord('1')]), ])]
	
	
	etat9.space = [Chem([Bord('0'), Intern('0'), Intern('0'), ]), Chem([Intern('0'), Intern('0'), ]), Chem([Bord('1'), Intern('0'), Intern('0'), ]), ]
	
	etat9.initMat[Chem([Sub('0')])] = FMat([
		[Coef('Const', 1           ), Coef('Const', 0.666667    ), Coef('Const', 0.444444    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.333333    ), Coef('Const', 0.444444    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.111111    ), ], ])
	etat9.initMat[Chem([Sub('1')])] = FMat([
		[Coef('Const', 0.444444    ), Coef('Const', 0.222222    ), Coef('Const', 0.111111    ), ], 
		[Coef('Const', 0.444444    ), Coef('Const', 0.555556    ), Coef('Const', 0.444444    ), ], 
		[Coef('Const', 0.111111    ), Coef('Const', 0.222222    ), Coef('Const', 0.444444    ), ], ])
	etat9.initMat[Chem([Sub('2')])] = FMat([
		[Coef('Const', 0.111111    ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.444444    ), Coef('Const', 0.333333    ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.444444    ), Coef('Const', 0.666667    ), Coef('Const', 1           ), ], ])
	etat9.initMat[Chem([Sub('G')])] = FMat([
		[Coef('Const', 0           )], 
		[Coef('Const', 1           )], 
		[Coef('Const', 0           )], ])
	
	
	
	etat10.bords   = {}
	etat10.permuts = {}
	etat10.interns = {Intern('_'): etat10, }
	etat10.subs    = {Sub('0'): etat10, Sub('G', True): Etat.etatPoint, }
	
	etat10.buildIntern()
	
	
	etat10.eqs = [
		]
	
	
	etat10.prim.elems = []
	etat10.grid.elems = []
	
	
	etat10.space = [Chem([Intern('0'), Intern('0'), ])]
	
	etat10.initMat[Chem([Sub('0')])] = FMat([[Coef('Var'  , 1           )]])
	etat10.initMat[Chem([Sub('G')])] = FMat([[Coef('Const', 1           )]])
	
	
	
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
