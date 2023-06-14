# -*- coding: utf-8 -*-

# Automatically generated, from file : double_tetra.py, function : modele()

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
	etat7 = Etat('B3',1)
	etat8 = Etat('B2',1)
	etat9 = Etat('s',1)
	
	
	etat0.subs   = {Sub('0'): etat1, Sub('1'): etat2, Sub('2'): etat3, Sub('3'): etat4, Sub('4'): etat5, Sub('5'): etat6, }
	
	etat0.eqs = [
		(Chem([Sub('0'), Bord('0'), Bord('1'), ])	,	Chem([Sub('1'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('1'), Bord('1'), ])	,	Chem([Sub('2'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('2'), Bord('1'), ])	,	Chem([Sub('3'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('0'), Bord('1'), ])	,	Chem([Sub('2'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('2'), Bord('1'), ])	,	Chem([Sub('4'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('1'), Bord('1'), ])	,	Chem([Sub('5'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('3'), Bord('0'), Bord('1'), ])	,	Chem([Sub('5'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('3'), Bord('1'), Bord('1'), ])	,	Chem([Sub('4'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('4'), Bord('1'), Bord('1'), ])	,	Chem([Sub('5'), Bord('0'), Bord('1'), ])),
		]
	
	
	etat0.space = []
	
	etat0.initMat[Chem([Sub('0')])] = FMat([
		[Coef('Var'  , 1.18888     ), Coef('Var'  , 0.0922862   ), Coef('Var'  ,-1.07425     ), Coef('Var'  ,-1.26327     ), Coef('Var'  ,-0.695051    ), Coef('Var'  , 0.403037    ), ], 
		[Coef('Var'  , 0.407789    ), Coef('Var'  , 1.12968     ), Coef('Var'  , 1.13931     ), Coef('Var'  ,-0.0157431   ), Coef('Var'  ,-1.03133     ), Coef('Var'  ,-0.6399      ), ], 
		[Coef('Var'  , 0.0963154   ), Coef('Var'  , 5.8921e-08  ), Coef('Var'  , 0.573149    ), Coef('Var'  , 6.37029e-09 ), Coef('Var'  , 0.587085    ), Coef('Var'  , 1.75282e-08 ), ], 
		[Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), ], ])
	etat0.initMat[Chem([Sub('1')])] = FMat([
		[Coef('Var'  ,-0.107646    ), Coef('Var'  ,-1.11692     ), Coef('Var'  ,-1.56125     ), Coef('Var'  ,-1.98853     ), Coef('Var'  ,-1.07425     ), Coef('Var'  ,-0.735879    ), ], 
		[Coef('Var'  , 1.8381      ), Coef('Var'  , 1.03833     ), Coef('Var'  ,-0.0506827   ), Coef('Var'  , 0.762595    ), Coef('Var'  , 1.13931     ), Coef('Var'  , 2.03157     ), ], 
		[Coef('Var'  , 2.62167     ), Coef('Var'  , 2.92361     ), Coef('Var'  , 2.32719     ), Coef('Var'  , 1.40838     ), Coef('Var'  , 0.573149    ), Coef('Var'  , 1.47835     ), ], 
		[Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), ], ])
	etat0.initMat[Chem([Sub('2')])] = FMat([
		[Coef('Var'  ,-0.695051    ), Coef('Var'  ,-1.68853     ), Coef('Var'  ,-1.56125     ), Coef('Var'  ,-0.77393     ), Coef('Var'  , 0.448876    ), Coef('Var'  ,-0.0737154   ), ], 
		[Coef('Var'  ,-1.03133     ), Coef('Var'  ,-0.974755    ), Coef('Var'  ,-0.0506827   ), Coef('Var'  ,-0.913623    ), Coef('Var'  ,-1.32608     ), Coef('Var'  ,-1.73696     ), ], 
		[Coef('Var'  , 0.587085    ), Coef('Var'  , 1.42401     ), Coef('Var'  , 2.32719     ), Coef('Var'  , 2.93777     ), Coef('Var'  , 2.64636     ), Coef('Var'  , 1.50614     ), ], 
		[Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), ], ])
	etat0.initMat[Chem([Sub('3')])] = FMat([
		[Coef('Var'  , 1.18888     ), Coef('Var'  , 2.15712     ), Coef('Var'  , 2.53277     ), Coef('Var'  , 3.01234     ), Coef('Var'  , 2.15192     ), Coef('Var'  , 1.8439      ), ], 
		[Coef('Var'  , 0.407789    ), Coef('Var'  ,-0.338702    ), Coef('Var'  ,-0.455974    ), Coef('Var'  , 0.744385    ), Coef('Var'  , 1.71319     ), Coef('Var'  , 1.44702     ), ], 
		[Coef('Var'  , 0.0963154   ), Coef('Var'  , 0.571169    ), Coef('Var'  , 1.82759     ), Coef('Var'  , 1.67362     ), Coef('Var'  , 1.80705     ), Coef('Var'  , 0.553676    ), ], 
		[Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), ], ])
	etat0.initMat[Chem([Sub('4')])] = FMat([
		[Coef('Var'  ,-0.107646    ), Coef('Var'  , 1.02938     ), Coef('Var'  , 2.15192     ), Coef('Var'  , 2.30416     ), Coef('Var'  , 1.64683     ), Coef('Var'  , 0.622301    ), ], 
		[Coef('Var'  , 1.8381      ), Coef('Var'  , 2.32044     ), Coef('Var'  , 1.71319     ), Coef('Var'  , 1.52884     ), Coef('Var'  , 0.52394     ), Coef('Var'  , 1.35222     ), ], 
		[Coef('Var'  , 2.62167     ), Coef('Var'  , 2.14347     ), Coef('Var'  , 1.80705     ), Coef('Var'  , 3.08295     ), Coef('Var'  , 3.58331     ), Coef('Var'  , 3.60688     ), ], 
		[Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), ], ])
	etat0.initMat[Chem([Sub('5')])] = FMat([
		[Coef('Var'  , 0.448876    ), Coef('Var'  , 0.96527     ), Coef('Var'  , 1.64683     ), Coef('Var'  , 2.60894     ), Coef('Var'  , 2.53277     ), Coef('Var'  , 1.68336     ), ], 
		[Coef('Var'  ,-1.32608     ), Coef('Var'  ,-0.603747    ), Coef('Var'  , 0.52394     ), Coef('Var'  ,-0.207377    ), Coef('Var'  ,-0.455974    ), Coef('Var'  ,-1.40371     ), ], 
		[Coef('Var'  , 2.64636     ), Coef('Var'  , 3.6221      ), Coef('Var'  , 3.58331     ), Coef('Var'  , 3.09652     ), Coef('Var'  , 1.82759     ), Coef('Var'  , 2.1771      ), ], 
		[Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), ], ])
	
	
	
	etat1.bords   = {Bord('0'): etat7, Bord('1'): etat8, Bord('2'): etat7, }
	etat1.permuts = {}
	etat1.interns = {Intern('_'): etat1, }
	etat1.subs    = {Sub('0'): etat2, Sub('1'): etat3, Sub('2'): etat4, Sub('3'): etat5, Sub('G', True): Etat.etatPoint, Sub('4'): etat6, }
	
	etat1.buildIntern()
	
	
	etat1.eqs = [
		(Chem([Bord('1'), Sub('0'), Permut('0'), ])	,	Chem([Sub('0'), Bord('1'), ])),
		(Chem([Bord('0'), Sub('2'), Permut('0'), ])	,	Chem([Sub('0'), Bord('2'), ])),
		(Chem([Bord('1'), Sub('1'), Permut('0'), ])	,	Chem([Sub('1'), Bord('0'), ])),
		(Chem([Bord('2'), Sub('0'), Permut('0'), ])	,	Chem([Sub('1'), Bord('2'), ])),
		(Chem([Bord('2'), Sub('2'), Permut('0'), ])	,	Chem([Sub('2'), Bord('0'), ])),
		(Chem([Bord('0'), Sub('0'), Permut('0'), ])	,	Chem([Sub('2'), Bord('2'), ])),
		(Chem([Bord('0'), Sub('1'), Permut('0'), ])	,	Chem([Sub('3'), Bord('0'), ])),
		(Chem([Bord('2'), Sub('1'), Permut('0'), ])	,	Chem([Sub('4'), Bord('2'), ])),
		(Chem([Sub('0'), Bord('0'), Bord('1'), ])	,	Chem([Sub('1'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('2'), Bord('1'), ])	,	Chem([Sub('3'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('1'), Bord('1'), ])	,	Chem([Sub('4'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('0'), Bord('1'), ])	,	Chem([Sub('4'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('1'), Bord('1'), ])	,	Chem([Sub('3'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('3'), Bord('1'), Bord('1'), ])	,	Chem([Sub('4'), Bord('0'), Bord('1'), ])),
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
		[Coef('Const', 0.111111    ), Coef('Var'  , 0.0555556   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.444444    ), Coef('Var'  , 0.222222    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.333333    ), ], 
		[Coef('Const', 0.444444    ), Coef('Var'  , 0.347222    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.666667    ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.25        ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.125       ), Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 8.33337e-08 ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], ])
	etat1.initMat[Chem([Sub('1')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0555556   ), Coef('Const', 0.111111    ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 8.33334e-08 ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.125       ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.347222    ), Coef('Const', 0.444444    ), Coef('Const', 0.666667    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.222222    ), Coef('Const', 0.444444    ), Coef('Const', 0.333333    ), ], ])
	etat1.initMat[Chem([Sub('2')])] = FMat([
		[Coef('Const', 1           ), Coef('Const', 0.666667    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.444444    ), Coef('Const', 0.444444    ), Coef('Const', 0.666667    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.222222    ), Coef('Const', 0.444444    ), Coef('Const', 0.333333    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0555557   ), Coef('Const', 0.111111    ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 1.66667e-07 ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.111111    ), Coef('Var'  , 0.0555557   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.333333    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.222222    ), Coef('Const', 0           ), Coef('Const', 0           ), ], ])
	etat1.initMat[Chem([Sub('3')])] = FMat([
		[Coef('Const', 0.111111    ), Coef('Const', 0.222222    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.361068    ), Coef('Var'  , 0.277724    ), Coef('Var'  , 0.194401    ), ], 
		[Coef('Const', 0.444444    ), Coef('Const', 0.555556    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.333228    ), Coef('Var'  , 0.222092    ), Coef('Var'  , 0.333228    ), ], 
		[Coef('Const', 0.444444    ), Coef('Const', 0.222222    ), Coef('Const', 0.111111    ), Coef('Var'  , 0.124941    ), Coef('Var'  , 0.138816    ), Coef('Var'  , 0.291608    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.000243064 ), Coef('Var'  , 0.000300405 ), Coef('Var'  , 0.000243064 ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0694897   ), Coef('Var'  , 0.138945    ), Coef('Var'  , 0.0694897   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.11103     ), Coef('Var'  , 0.222122    ), Coef('Var'  , 0.11103     ), ], ])
	etat1.initMat[Chem([Sub('G')])] = FMat([
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], ])
	etat1.initMat[Chem([Sub('4')])] = FMat([
		[Coef('Const', 0.111111    ), Coef('Var'  , 0.194401    ), Coef('Var'  , 0.277724    ), Coef('Var'  , 0.361068    ), Coef('Const', 0.444444    ), Coef('Const', 0.222222    ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.111006    ), Coef('Var'  , 0.222092    ), Coef('Var'  , 0.111006    ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0693859   ), Coef('Var'  , 0.138816    ), Coef('Var'  , 0.0693859   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.000243064 ), Coef('Var'  , 0.000300405 ), Coef('Var'  , 0.000243064 ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.444444    ), Coef('Var'  , 0.291712    ), Coef('Var'  , 0.138945    ), Coef('Var'  , 0.125045    ), Coef('Const', 0.111111    ), Coef('Const', 0.222222    ), ], 
		[Coef('Const', 0.444444    ), Coef('Var'  , 0.333252    ), Coef('Var'  , 0.222122    ), Coef('Var'  , 0.333252    ), Coef('Const', 0.444444    ), Coef('Const', 0.555556    ), ], ])
	
	
	
	etat2.bords   = {Bord('0'): etat7, Bord('1'): etat8, Bord('2'): etat7, }
	etat2.permuts = {}
	etat2.interns = {Intern('_'): etat2, }
	etat2.subs    = {Sub('0'): etat1, Sub('1'): etat3, Sub('2'): etat4, Sub('3'): etat5, Sub('G', True): Etat.etatPoint, Sub('4'): etat6, }
	
	etat2.buildIntern()
	
	
	etat2.eqs = [
		(Chem([Bord('2'), Sub('0'), Permut('0'), ])	,	Chem([Sub('0'), Bord('0'), ])),
		(Chem([Bord('1'), Sub('1'), Permut('0'), ])	,	Chem([Sub('0'), Bord('1'), ])),
		(Chem([Bord('1'), Sub('0'), Permut('0'), ])	,	Chem([Sub('1'), Bord('0'), ])),
		(Chem([Bord('0'), Sub('2'), Permut('0'), ])	,	Chem([Sub('1'), Bord('1'), ])),
		(Chem([Bord('2'), Sub('1'), Permut('0'), ])	,	Chem([Sub('2'), Bord('2'), ])),
		(Chem([Bord('2'), Sub('2'), Permut('0'), ])	,	Chem([Sub('3'), Bord('0'), ])),
		(Chem([Bord('0'), Sub('0'), Permut('0'), ])	,	Chem([Sub('3'), Bord('2'), ])),
		(Chem([Bord('0'), Sub('1'), Permut('0'), ])	,	Chem([Sub('4'), Bord('0'), ])),
		(Chem([Sub('0'), Bord('1'), Bord('1'), ])	,	Chem([Sub('1'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('2'), Bord('1'), ])	,	Chem([Sub('2'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('1'), Bord('1'), ])	,	Chem([Sub('4'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('0'), Bord('1'), ])	,	Chem([Sub('4'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('1'), Bord('1'), ])	,	Chem([Sub('3'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('3'), Bord('1'), Bord('1'), ])	,	Chem([Sub('4'), Bord('0'), Bord('1'), ])),
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
		[Coef('Const', 0.111111    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0555556   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 8.33337e-08 ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.125       ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.25        ), ], 
		[Coef('Const', 0.444444    ), Coef('Const', 0.666667    ), Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.347222    ), ], 
		[Coef('Const', 0.444444    ), Coef('Const', 0.333333    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.222222    ), ], ])
	etat2.initMat[Chem([Sub('1')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.111111    ), Coef('Var'  , 0.0555556   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.333333    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.222222    ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.666667    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.347222    ), ], 
		[Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.25        ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.125       ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 8.33342e-08 ), ], ])
	etat2.initMat[Chem([Sub('2')])] = FMat([
		[Coef('Const', 0.111111    ), Coef('Var'  , 0.194322    ), Coef('Var'  , 0.277626    ), Coef('Var'  , 0.360989    ), Coef('Const', 0.444444    ), Coef('Const', 0.222222    ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.111058    ), Coef('Var'  , 0.222156    ), Coef('Var'  , 0.111058    ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0694903   ), Coef('Var'  , 0.138945    ), Coef('Var'  , 0.0694903   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.000246053 ), Coef('Var'  , 0.000304099 ), Coef('Var'  , 0.000246053 ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.444444    ), Coef('Var'  , 0.291598    ), Coef('Var'  , 0.138805    ), Coef('Var'  , 0.124932    ), Coef('Const', 0.111111    ), Coef('Const', 0.222222    ), ], 
		[Coef('Const', 0.444444    ), Coef('Var'  , 0.333285    ), Coef('Var'  , 0.222163    ), Coef('Var'  , 0.333285    ), Coef('Const', 0.444444    ), Coef('Const', 0.555556    ), ], ])
	etat2.initMat[Chem([Sub('3')])] = FMat([
		[Coef('Const', 1           ), Coef('Const', 0.666667    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.444444    ), Coef('Const', 0.444444    ), Coef('Const', 0.666667    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.222222    ), Coef('Const', 0.444444    ), Coef('Const', 0.333333    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0555557   ), Coef('Const', 0.111111    ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 1.66667e-07 ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.111111    ), Coef('Var'  , 0.0555557   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.333333    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.222222    ), Coef('Const', 0           ), Coef('Const', 0           ), ], ])
	etat2.initMat[Chem([Sub('G')])] = FMat([
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], ])
	etat2.initMat[Chem([Sub('4')])] = FMat([
		[Coef('Const', 0.111111    ), Coef('Const', 0.222222    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.360989    ), Coef('Var'  , 0.277626    ), Coef('Var'  , 0.194322    ), ], 
		[Coef('Const', 0.444444    ), Coef('Const', 0.555556    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.33328     ), Coef('Var'  , 0.222156    ), Coef('Var'  , 0.33328     ), ], 
		[Coef('Const', 0.444444    ), Coef('Const', 0.222222    ), Coef('Const', 0.111111    ), Coef('Var'  , 0.125046    ), Coef('Var'  , 0.138945    ), Coef('Var'  , 0.291712    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.000246053 ), Coef('Var'  , 0.000304099 ), Coef('Var'  , 0.000246053 ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0693763   ), Coef('Var'  , 0.138805    ), Coef('Var'  , 0.0693763   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.111063    ), Coef('Var'  , 0.222163    ), Coef('Var'  , 0.111063    ), ], ])
	
	
	
	etat3.bords   = {Bord('0'): etat8, Bord('1'): etat7, Bord('2'): etat7, }
	etat3.permuts = {}
	etat3.interns = {Intern('_'): etat3, }
	etat3.subs    = {Sub('0'): etat1, Sub('1'): etat2, Sub('2'): etat4, Sub('3'): etat5, Sub('G', True): Etat.etatPoint, Sub('4'): etat6, }
	
	etat3.buildIntern()
	
	
	etat3.eqs = [
		(Chem([Bord('0'), Sub('0'), Permut('0'), ])	,	Chem([Sub('0'), Bord('1'), ])),
		(Chem([Bord('2'), Sub('2'), Permut('0'), ])	,	Chem([Sub('0'), Bord('2'), ])),
		(Chem([Bord('1'), Sub('0'), Permut('0'), ])	,	Chem([Sub('1'), Bord('0'), ])),
		(Chem([Bord('0'), Sub('1'), Permut('0'), ])	,	Chem([Sub('1'), Bord('1'), ])),
		(Chem([Bord('2'), Sub('1'), Permut('0'), ])	,	Chem([Sub('2'), Bord('0'), ])),
		(Chem([Bord('1'), Sub('1'), Permut('0'), ])	,	Chem([Sub('3'), Bord('2'), ])),
		(Chem([Bord('1'), Sub('2'), Permut('0'), ])	,	Chem([Sub('4'), Bord('0'), ])),
		(Chem([Bord('2'), Sub('0'), Permut('0'), ])	,	Chem([Sub('4'), Bord('2'), ])),
		(Chem([Sub('0'), Bord('0'), Bord('1'), ])	,	Chem([Sub('1'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('2'), Bord('1'), ])	,	Chem([Sub('2'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('2'), Bord('1'), ])	,	Chem([Sub('3'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('0'), Bord('1'), ])	,	Chem([Sub('4'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('1'), Bord('1'), ])	,	Chem([Sub('3'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('3'), Bord('1'), Bord('1'), ])	,	Chem([Sub('4'), Bord('0'), Bord('1'), ])),
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
		[Coef('Const', 0.444444    ), Coef('Var'  , 0.347222    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.666667    ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.25        ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.125       ), Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 8.33334e-08 ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.111111    ), Coef('Var'  , 0.0555556   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.444444    ), Coef('Var'  , 0.222222    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.333333    ), ], ])
	etat3.initMat[Chem([Sub('1')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.125       ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.25        ), ], 
		[Coef('Const', 0.444444    ), Coef('Const', 0.666667    ), Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.347222    ), ], 
		[Coef('Const', 0.444444    ), Coef('Const', 0.333333    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.222222    ), ], 
		[Coef('Const', 0.111111    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0555556   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 8.33337e-08 ), ], ])
	etat3.initMat[Chem([Sub('2')])] = FMat([
		[Coef('Const', 0.444444    ), Coef('Const', 0.222222    ), Coef('Const', 0.111111    ), Coef('Var'  , 0.125116    ), Coef('Var'  , 0.139032    ), Coef('Var'  , 0.291782    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.000209329 ), Coef('Var'  , 0.000258705 ), Coef('Var'  , 0.000209329 ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0694214   ), Coef('Var'  , 0.13886     ), Coef('Var'  , 0.0694214   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.11091     ), Coef('Var'  , 0.221973    ), Coef('Var'  , 0.11091     ), ], 
		[Coef('Const', 0.111111    ), Coef('Const', 0.222222    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.360986    ), Coef('Var'  , 0.277623    ), Coef('Var'  , 0.19432     ), ], 
		[Coef('Const', 0.444444    ), Coef('Const', 0.555556    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.333358    ), Coef('Var'  , 0.222253    ), Coef('Var'  , 0.333358    ), ], ])
	etat3.initMat[Chem([Sub('3')])] = FMat([
		[Coef('Const', 0           ), Coef('Var'  , 0.0695602   ), Coef('Var'  , 0.139032    ), Coef('Var'  , 0.0695602   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.000209329 ), Coef('Var'  , 0.000258705 ), Coef('Var'  , 0.000209329 ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.444444    ), Coef('Var'  , 0.291643    ), Coef('Var'  , 0.13886     ), Coef('Var'  , 0.124977    ), Coef('Const', 0.111111    ), Coef('Const', 0.222222    ), ], 
		[Coef('Const', 0.444444    ), Coef('Var'  , 0.333132    ), Coef('Var'  , 0.221973    ), Coef('Var'  , 0.333132    ), Coef('Const', 0.444444    ), Coef('Const', 0.555556    ), ], 
		[Coef('Const', 0.111111    ), Coef('Var'  , 0.19432     ), Coef('Var'  , 0.277623    ), Coef('Var'  , 0.360986    ), Coef('Const', 0.444444    ), Coef('Const', 0.222222    ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.111136    ), Coef('Var'  , 0.222253    ), Coef('Var'  , 0.111136    ), Coef('Const', 0           ), Coef('Const', 0           ), ], ])
	etat3.initMat[Chem([Sub('G')])] = FMat([
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], ])
	etat3.initMat[Chem([Sub('4')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0555557   ), Coef('Const', 0.111111    ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 1.66667e-07 ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.111111    ), Coef('Var'  , 0.0555557   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.333333    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.222222    ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 1           ), Coef('Const', 0.666667    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.444444    ), Coef('Const', 0.444444    ), Coef('Const', 0.666667    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.222222    ), Coef('Const', 0.444444    ), Coef('Const', 0.333333    ), ], ])
	
	
	
	etat4.bords   = {Bord('0'): etat7, Bord('1'): etat8, Bord('2'): etat7, }
	etat4.permuts = {}
	etat4.interns = {Intern('_'): etat4, }
	etat4.subs    = {Sub('0'): etat1, Sub('1'): etat2, Sub('2'): etat3, Sub('3'): etat5, Sub('G', True): Etat.etatPoint, Sub('4'): etat6, }
	
	etat4.buildIntern()
	
	
	etat4.eqs = [
		(Chem([Bord('2'), Sub('2'), Permut('0'), ])	,	Chem([Sub('0'), Bord('0'), ])),
		(Chem([Bord('0'), Sub('0'), Permut('0'), ])	,	Chem([Sub('0'), Bord('2'), ])),
		(Chem([Bord('2'), Sub('1'), Permut('0'), ])	,	Chem([Sub('1'), Bord('2'), ])),
		(Chem([Bord('0'), Sub('1'), Permut('0'), ])	,	Chem([Sub('2'), Bord('2'), ])),
		(Chem([Bord('2'), Sub('0'), Permut('0'), ])	,	Chem([Sub('3'), Bord('0'), ])),
		(Chem([Bord('1'), Sub('1'), Permut('0'), ])	,	Chem([Sub('3'), Bord('1'), ])),
		(Chem([Bord('1'), Sub('0'), Permut('0'), ])	,	Chem([Sub('4'), Bord('1'), ])),
		(Chem([Bord('0'), Sub('2'), Permut('0'), ])	,	Chem([Sub('4'), Bord('2'), ])),
		(Chem([Sub('0'), Bord('0'), Bord('1'), ])	,	Chem([Sub('1'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('1'), Bord('1'), ])	,	Chem([Sub('2'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('0'), Bord('1'), ])	,	Chem([Sub('2'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('2'), Bord('1'), ])	,	Chem([Sub('3'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('1'), Bord('1'), ])	,	Chem([Sub('4'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('3'), Bord('1'), Bord('1'), ])	,	Chem([Sub('4'), Bord('0'), Bord('1'), ])),
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
		[Coef('Const', 1           ), Coef('Const', 0.666667    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.444444    ), Coef('Const', 0.444444    ), Coef('Const', 0.666667    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.222222    ), Coef('Const', 0.444444    ), Coef('Const', 0.333333    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0555557   ), Coef('Const', 0.111111    ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 1.66667e-07 ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.111111    ), Coef('Var'  , 0.0555557   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.333333    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.222222    ), Coef('Const', 0           ), Coef('Const', 0           ), ], ])
	etat4.initMat[Chem([Sub('1')])] = FMat([
		[Coef('Const', 0.111111    ), Coef('Var'  , 0.194333    ), Coef('Var'  , 0.27764     ), Coef('Var'  , 0.361       ), Coef('Const', 0.444444    ), Coef('Const', 0.222222    ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.111078    ), Coef('Var'  , 0.222182    ), Coef('Var'  , 0.111078    ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0695553   ), Coef('Var'  , 0.139026    ), Coef('Var'  , 0.0695553   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 9.90146e-05 ), Coef('Var'  , 0.000122349 ), Coef('Var'  , 9.90146e-05 ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.444444    ), Coef('Var'  , 0.291722    ), Coef('Var'  , 0.138957    ), Coef('Var'  , 0.125055    ), Coef('Const', 0.111111    ), Coef('Const', 0.222222    ), ], 
		[Coef('Const', 0.444444    ), Coef('Var'  , 0.333212    ), Coef('Var'  , 0.222073    ), Coef('Var'  , 0.333212    ), Coef('Const', 0.444444    ), Coef('Const', 0.555556    ), ], ])
	etat4.initMat[Chem([Sub('2')])] = FMat([
		[Coef('Const', 0.444444    ), Coef('Var'  , 0.361       ), Coef('Var'  , 0.27764     ), Coef('Var'  , 0.194333    ), Coef('Const', 0.111111    ), Coef('Const', 0.222222    ), ], 
		[Coef('Const', 0.444444    ), Coef('Var'  , 0.3333      ), Coef('Var'  , 0.222182    ), Coef('Var'  , 0.3333      ), Coef('Const', 0.444444    ), Coef('Const', 0.555556    ), ], 
		[Coef('Const', 0.111111    ), Coef('Var'  , 0.125111    ), Coef('Var'  , 0.139026    ), Coef('Var'  , 0.291777    ), Coef('Const', 0.444444    ), Coef('Const', 0.222222    ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 9.90146e-05 ), Coef('Var'  , 0.000122349 ), Coef('Var'  , 9.90146e-05 ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0694997   ), Coef('Var'  , 0.138957    ), Coef('Var'  , 0.0694997   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.11099     ), Coef('Var'  , 0.222073    ), Coef('Var'  , 0.11099     ), Coef('Const', 0           ), Coef('Const', 0           ), ], ])
	etat4.initMat[Chem([Sub('3')])] = FMat([
		[Coef('Const', 0.111111    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0555556   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 8.33335e-08 ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.125       ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.25        ), ], 
		[Coef('Const', 0.444444    ), Coef('Const', 0.666667    ), Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.347222    ), ], 
		[Coef('Const', 0.444444    ), Coef('Const', 0.333333    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.222222    ), ], ])
	etat4.initMat[Chem([Sub('G')])] = FMat([
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], ])
	etat4.initMat[Chem([Sub('4')])] = FMat([
		[Coef('Const', 0.111111    ), Coef('Var'  , 0.0555556   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.444444    ), Coef('Var'  , 0.222222    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.333333    ), ], 
		[Coef('Const', 0.444444    ), Coef('Var'  , 0.347222    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.666667    ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.25        ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.125       ), Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 8.33338e-08 ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], ])
	
	
	
	etat5.bords   = {Bord('0'): etat7, Bord('1'): etat8, Bord('2'): etat7, }
	etat5.permuts = {}
	etat5.interns = {Intern('_'): etat5, }
	etat5.subs    = {Sub('0'): etat1, Sub('1'): etat2, Sub('2'): etat3, Sub('3'): etat4, Sub('G', True): Etat.etatPoint, Sub('4'): etat6, }
	
	etat5.buildIntern()
	
	
	etat5.eqs = [
		(Chem([Bord('0'), Sub('1'), Permut('0'), ])	,	Chem([Sub('0'), Bord('0'), ])),
		(Chem([Bord('2'), Sub('2'), Permut('0'), ])	,	Chem([Sub('1'), Bord('0'), ])),
		(Chem([Bord('0'), Sub('0'), Permut('0'), ])	,	Chem([Sub('1'), Bord('2'), ])),
		(Chem([Bord('2'), Sub('1'), Permut('0'), ])	,	Chem([Sub('2'), Bord('1'), ])),
		(Chem([Bord('1'), Sub('0'), Permut('0'), ])	,	Chem([Sub('3'), Bord('1'), ])),
		(Chem([Bord('0'), Sub('2'), Permut('0'), ])	,	Chem([Sub('3'), Bord('2'), ])),
		(Chem([Bord('2'), Sub('0'), Permut('0'), ])	,	Chem([Sub('4'), Bord('0'), ])),
		(Chem([Bord('1'), Sub('1'), Permut('0'), ])	,	Chem([Sub('4'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('0'), Bord('1'), ])	,	Chem([Sub('1'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('1'), Bord('1'), ])	,	Chem([Sub('2'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('2'), Bord('1'), ])	,	Chem([Sub('3'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('0'), Bord('1'), ])	,	Chem([Sub('2'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('1'), Bord('1'), ])	,	Chem([Sub('4'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('3'), Bord('0'), Bord('1'), ])	,	Chem([Sub('4'), Bord('1'), Bord('1'), ])),
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
		[Coef('Const', 0.111111    ), Coef('Const', 0.222222    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.361011    ), Coef('Var'  , 0.277655    ), Coef('Var'  , 0.194345    ), ], 
		[Coef('Const', 0.444444    ), Coef('Const', 0.555556    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.333267    ), Coef('Var'  , 0.222141    ), Coef('Var'  , 0.333267    ), ], 
		[Coef('Const', 0.444444    ), Coef('Const', 0.222222    ), Coef('Const', 0.111111    ), Coef('Var'  , 0.125024    ), Coef('Var'  , 0.138919    ), Coef('Var'  , 0.291691    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.000120496 ), Coef('Var'  , 0.000148902 ), Coef('Var'  , 0.000120496 ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.069479    ), Coef('Var'  , 0.138932    ), Coef('Var'  , 0.069479    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.111098    ), Coef('Var'  , 0.222206    ), Coef('Var'  , 0.111098    ), ], ])
	etat5.initMat[Chem([Sub('1')])] = FMat([
		[Coef('Const', 1           ), Coef('Const', 0.666667    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.444444    ), Coef('Const', 0.444444    ), Coef('Const', 0.666667    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.222222    ), Coef('Const', 0.444444    ), Coef('Const', 0.333333    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0555557   ), Coef('Const', 0.111111    ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 1.66667e-07 ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.111111    ), Coef('Var'  , 0.0555557   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.333333    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.222222    ), Coef('Const', 0           ), Coef('Const', 0           ), ], ])
	etat5.initMat[Chem([Sub('2')])] = FMat([
		[Coef('Var'  , 0.277655    ), Coef('Var'  , 0.361011    ), Coef('Const', 0.444444    ), Coef('Const', 0.222222    ), Coef('Const', 0.111111    ), Coef('Var'  , 0.194345    ), ], 
		[Coef('Var'  , 0.222141    ), Coef('Var'  , 0.111045    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.111045    ), ], 
		[Coef('Var'  , 0.138919    ), Coef('Var'  , 0.0694685   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0694685   ), ], 
		[Coef('Var'  , 0.000148902 ), Coef('Var'  , 0.000120496 ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.000120496 ), ], 
		[Coef('Var'  , 0.138932    ), Coef('Var'  , 0.125035    ), Coef('Const', 0.111111    ), Coef('Const', 0.222222    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.291701    ), ], 
		[Coef('Var'  , 0.222206    ), Coef('Var'  , 0.33332     ), Coef('Const', 0.444444    ), Coef('Const', 0.555556    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.33332     ), ], ])
	etat5.initMat[Chem([Sub('3')])] = FMat([
		[Coef('Const', 0.111111    ), Coef('Var'  , 0.0555556   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.444444    ), Coef('Var'  , 0.222222    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.333333    ), ], 
		[Coef('Const', 0.444444    ), Coef('Var'  , 0.347222    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.666667    ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.25        ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.125       ), Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 8.33334e-08 ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], ])
	etat5.initMat[Chem([Sub('G')])] = FMat([
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], ])
	etat5.initMat[Chem([Sub('4')])] = FMat([
		[Coef('Const', 0.111111    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0555556   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 8.33338e-08 ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.125       ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.25        ), ], 
		[Coef('Const', 0.444444    ), Coef('Const', 0.666667    ), Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.347222    ), ], 
		[Coef('Const', 0.444444    ), Coef('Const', 0.333333    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.222222    ), ], ])
	
	
	
	etat6.bords   = {Bord('0'): etat7, Bord('1'): etat8, Bord('2'): etat7, }
	etat6.permuts = {}
	etat6.interns = {Intern('_'): etat6, }
	etat6.subs    = {Sub('0'): etat1, Sub('1'): etat2, Sub('2'): etat3, Sub('3'): etat4, Sub('G', True): Etat.etatPoint, Sub('4'): etat5, }
	
	etat6.buildIntern()
	
	
	etat6.eqs = [
		(Chem([Bord('2'), Sub('1'), Permut('0'), ])	,	Chem([Sub('0'), Bord('2'), ])),
		(Chem([Bord('0'), Sub('1'), Permut('0'), ])	,	Chem([Sub('1'), Bord('0'), ])),
		(Chem([Bord('0'), Sub('0'), Permut('0'), ])	,	Chem([Sub('2'), Bord('1'), ])),
		(Chem([Bord('2'), Sub('2'), Permut('0'), ])	,	Chem([Sub('2'), Bord('2'), ])),
		(Chem([Bord('2'), Sub('0'), Permut('0'), ])	,	Chem([Sub('3'), Bord('0'), ])),
		(Chem([Bord('1'), Sub('1'), Permut('0'), ])	,	Chem([Sub('3'), Bord('1'), ])),
		(Chem([Bord('1'), Sub('0'), Permut('0'), ])	,	Chem([Sub('4'), Bord('1'), ])),
		(Chem([Bord('0'), Sub('2'), Permut('0'), ])	,	Chem([Sub('4'), Bord('2'), ])),
		(Chem([Sub('0'), Bord('0'), Bord('1'), ])	,	Chem([Sub('1'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('1'), Bord('1'), ])	,	Chem([Sub('2'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('2'), Bord('1'), ])	,	Chem([Sub('3'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('0'), Bord('1'), ])	,	Chem([Sub('2'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('2'), Bord('1'), ])	,	Chem([Sub('4'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('3'), Bord('1'), Bord('1'), ])	,	Chem([Sub('4'), Bord('0'), Bord('1'), ])),
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
		[Coef('Const', 0.111111    ), Coef('Var'  , 0.194292    ), Coef('Var'  , 0.27759     ), Coef('Var'  , 0.360959    ), Coef('Const', 0.444444    ), Coef('Const', 0.222222    ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.111067    ), Coef('Var'  , 0.222168    ), Coef('Var'  , 0.111067    ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0694332   ), Coef('Var'  , 0.138875    ), Coef('Var'  , 0.0694332   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.000231152 ), Coef('Var'  , 0.000285681 ), Coef('Var'  , 0.000231152 ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.444444    ), Coef('Var'  , 0.291781    ), Coef('Var'  , 0.139031    ), Coef('Var'  , 0.125115    ), Coef('Const', 0.111111    ), Coef('Const', 0.222222    ), ], 
		[Coef('Const', 0.444444    ), Coef('Var'  , 0.333195    ), Coef('Var'  , 0.222051    ), Coef('Var'  , 0.333195    ), Coef('Const', 0.444444    ), Coef('Const', 0.555556    ), ], ])
	etat6.initMat[Chem([Sub('1')])] = FMat([
		[Coef('Const', 0.111111    ), Coef('Const', 0.222222    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.360959    ), Coef('Var'  , 0.27759     ), Coef('Var'  , 0.194292    ), ], 
		[Coef('Const', 0.444444    ), Coef('Const', 0.555556    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.333289    ), Coef('Var'  , 0.222168    ), Coef('Var'  , 0.333289    ), ], 
		[Coef('Const', 0.444444    ), Coef('Const', 0.222222    ), Coef('Const', 0.111111    ), Coef('Var'  , 0.124989    ), Coef('Var'  , 0.138875    ), Coef('Var'  , 0.291655    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.000231152 ), Coef('Var'  , 0.000285681 ), Coef('Var'  , 0.000231152 ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0695592   ), Coef('Var'  , 0.139031    ), Coef('Var'  , 0.0695592   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.110973    ), Coef('Var'  , 0.222051    ), Coef('Var'  , 0.110973    ), ], ])
	etat6.initMat[Chem([Sub('2')])] = FMat([
		[Coef('Const', 0.444444    ), Coef('Var'  , 0.444444    ), Coef('Const', 0.444444    ), Coef('Const', 0.666667    ), Coef('Const', 1           ), Coef('Const', 0.666667    ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.222222    ), Coef('Const', 0.444444    ), Coef('Const', 0.333333    ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0555557   ), Coef('Const', 0.111111    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 1.66667e-07 ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.111111    ), Coef('Var'  , 0.0555557   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.444444    ), Coef('Var'  , 0.222222    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.333333    ), ], ])
	etat6.initMat[Chem([Sub('3')])] = FMat([
		[Coef('Const', 0.111111    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0555556   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 8.33337e-08 ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.125       ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.25        ), ], 
		[Coef('Const', 0.444444    ), Coef('Const', 0.666667    ), Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.347222    ), ], 
		[Coef('Const', 0.444444    ), Coef('Const', 0.333333    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.222222    ), ], ])
	etat6.initMat[Chem([Sub('G')])] = FMat([
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], ])
	etat6.initMat[Chem([Sub('4')])] = FMat([
		[Coef('Const', 0.111111    ), Coef('Var'  , 0.0555556   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.444444    ), Coef('Var'  , 0.222222    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.333333    ), ], 
		[Coef('Const', 0.444444    ), Coef('Var'  , 0.347222    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.666667    ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.25        ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.125       ), Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 8.33335e-08 ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], ])
	
	
	
	etat7.bords   = {Bord('0'): etat9, Bord('1'): etat9, }
	etat7.permuts = {Permut('0'): etat7, }
	etat7.interns = {Intern('_'): etat7, }
	etat7.subs    = {Sub('0'): etat7, Sub('1'): etat7, Sub('2'): etat7, Sub('G', True): Etat.etatPoint, }
	
	etat7.buildIntern()
	etat7.fm_[Permut('0')] = PMat(3, [2, 1, 0, ])
	
	
	etat7.eqs = [
		(Chem([Permut('0'), Bord('0'), ])	,	Chem([Bord('1')])),
		(Chem([Permut('0'), Bord('1'), ])	,	Chem([Bord('0')])),
		(Chem([Permut('0'), Intern(''), ])	,	Chem([Intern('')])),
		(Chem([Permut('0'), Sub('0'), ])	,	Chem([Sub('2'), Permut('0'), ])),
		(Chem([Permut('0'), Sub('1'), ])	,	Chem([Sub('1'), Permut('0'), ])),
		(Chem([Permut('0'), Sub('2'), ])	,	Chem([Sub('0'), Permut('0'), ])),
		]
	
	
	etat7.prim.elems = [Figure(1, [Chem([Bord('0')]), Chem([Bord('1')]), ])]
	etat7.grid.elems = [Figure(1, [Chem([Bord('0')]), Chem([Intern('')]), Chem([Bord('1')]), ])]
	
	
	etat7.space = [Chem([Bord('0'), Intern('0'), Intern('0'), ]), Chem([Intern('0'), Intern('0'), ]), Chem([Bord('1'), Intern('0'), Intern('0'), ]), ]
	
	etat7.initMat[Chem([Sub('0')])] = FMat([
		[Coef('Const', 1           ), Coef('Const', 0.666667    ), Coef('Const', 0.444444    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.333333    ), Coef('Const', 0.444444    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.111111    ), ], ])
	etat7.initMat[Chem([Sub('1')])] = FMat([
		[Coef('Const', 0.444444    ), Coef('Const', 0.222222    ), Coef('Const', 0.111111    ), ], 
		[Coef('Const', 0.444444    ), Coef('Const', 0.555556    ), Coef('Const', 0.444444    ), ], 
		[Coef('Const', 0.111111    ), Coef('Const', 0.222222    ), Coef('Const', 0.444444    ), ], ])
	etat7.initMat[Chem([Sub('2')])] = FMat([
		[Coef('Const', 0.111111    ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.444444    ), Coef('Const', 0.333333    ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.444444    ), Coef('Const', 0.666667    ), Coef('Const', 1           ), ], ])
	etat7.initMat[Chem([Sub('G')])] = FMat([
		[Coef('Const', 0           )], 
		[Coef('Const', 1           )], 
		[Coef('Const', 0           )], ])
	
	
	
	etat8.bords   = {Bord('0'): etat9, Bord('1'): etat9, }
	etat8.permuts = {Permut('0'): etat8, }
	etat8.interns = {Intern('_'): etat8, }
	etat8.subs    = {Sub('0'): etat8, Sub('1'): etat8, Sub('G', True): Etat.etatPoint, }
	
	etat8.buildIntern()
	etat8.fm_[Permut('0')] = PMat(3, [2, 1, 0, ])
	
	
	etat8.eqs = [
		(Chem([Permut('0'), Bord('0'), ])	,	Chem([Bord('1')])),
		(Chem([Permut('0'), Bord('1'), ])	,	Chem([Bord('0')])),
		(Chem([Permut('0'), Intern(''), ])	,	Chem([Intern('')])),
		(Chem([Permut('0'), Sub('0'), ])	,	Chem([Sub('1'), Permut('0'), ])),
		(Chem([Permut('0'), Sub('1'), ])	,	Chem([Sub('0'), Permut('0'), ])),
		]
	
	
	etat8.prim.elems = [Figure(1, [Chem([Bord('0')]), Chem([Bord('1')]), ])]
	etat8.grid.elems = [Figure(1, [Chem([Bord('0')]), Chem([Intern('')]), Chem([Bord('1')]), ])]
	
	
	etat8.space = [Chem([Bord('0'), Intern('0'), Intern('0'), ]), Chem([Intern('0'), Intern('0'), ]), Chem([Bord('1'), Intern('0'), Intern('0'), ]), ]
	
	etat8.initMat[Chem([Sub('0')])] = FMat([
		[Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), ], ])
	etat8.initMat[Chem([Sub('1')])] = FMat([
		[Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), ], ])
	etat8.initMat[Chem([Sub('G')])] = FMat([
		[Coef('Const', 0           )], 
		[Coef('Const', 1           )], 
		[Coef('Const', 0           )], ])
	
	
	
	etat9.bords   = {}
	etat9.permuts = {}
	etat9.interns = {Intern('_'): etat9, }
	etat9.subs    = {Sub('0'): etat9, Sub('G', True): Etat.etatPoint, }
	
	etat9.buildIntern()
	
	
	etat9.eqs = [
		]
	
	
	etat9.prim.elems = []
	etat9.grid.elems = []
	
	
	etat9.space = [Chem([Intern('0'), Intern('0'), ])]
	
	etat9.initMat[Chem([Sub('0')])] = FMat([[Coef('Var'  , 1           )]])
	etat9.initMat[Chem([Sub('G')])] = FMat([[Coef('Const', 1           )]])
	
	
	
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
