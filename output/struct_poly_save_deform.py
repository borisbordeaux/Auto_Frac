# -*- coding: utf-8 -*-

# Automatically generated, from file : struct_poly_save_deform.py, function : modele()

from __future__ import division
import sys
if './../../../../../../python' not in sys.path:
	sys.path.append('./../../../../../../python')
from etat import *

def modele():
	
	etat0 = EtatInit()
	etat1 = Etat('Tri_Square_Pyr',0)
	etat2 = Etat('Octa',0)
	etat3 = Etat('Dodeca',0)
	etat4 = Etat('Base_Square_Pyr',0)
	etat5 = Etat('Base_Penta_Pyr',0)
	etat6 = Etat('Tetra',0)
	etat7 = Etat('Icosa',0)
	etat8 = Etat('Tri_Penta_Pyr',0)
	etat9 = Etat('Cube',0)
	etat10 = Etat('B2',1)
	etat11 = Etat('B3',1)
	etat12 = Etat('B4',1)
	etat13 = Etat('s',1)
	
	
	etat0.subs   = {Sub('8'): etat1, Sub('7'): etat2, Sub('6'): etat3, Sub('5'): etat4, Sub('4'): etat5, Sub('3'): etat6, Sub('2'): etat7, Sub('1'): etat8, Sub('0'): etat9, }
	
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
		[Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 1           ), Coef('Const', 1           ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 1.2         ), Coef('Const', 0.6         ), Coef('Const', 0           ), Coef('Const', 0.6         ), Coef('Const', 1.2         ), Coef('Const', 1.2         ), ], 
		[Coef('Var'  , 0           ), Coef('Var'  ,-0.461829    ), Coef('Var'  , 0.0879353   ), Coef('Var'  , 0           ), Coef('Var'  , 0           ), Coef('Var'  , 0           ), ], 
		[Coef('Const', 1           ), Coef('Const', 1           ), Coef('Const', 1           ), Coef('Const', 1           ), Coef('Const', 1           ), Coef('Const', 1           ), ], ])
	etat0.initMat[Chem([Sub('7')])] = FMat([
		[Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.6         ), Coef('Const', 1.2         ), Coef('Const', 0.6         ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Var'  , 0.0879353   ), Coef('Var'  ,-0.461829    ), Coef('Var'  , 0           ), Coef('Var'  ,-0.550349    ), Coef('Var'  , 0.578233    ), Coef('Var'  , 0.788767    ), ], 
		[Coef('Const', 1           ), Coef('Const', 1           ), Coef('Const', 1           ), Coef('Const', 1           ), Coef('Const', 1           ), Coef('Const', 1           ), ], ])
	etat0.initMat[Chem([Sub('6')])] = FMat([
		[Coef('Const', 1           ), Coef('Const', 0.7         ), Coef('Const', 0.4         ), Coef('Const', 0.2         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 1           ), ], 
		[Coef('Const', 2           ), Coef('Const', 2.2         ), Coef('Const', 2.4         ), Coef('Const', 2.2         ), Coef('Const', 2           ), Coef('Const', 1.5         ), Coef('Const', 1.2         ), Coef('Const', 1.2         ), Coef('Const', 1.2         ), Coef('Const', 1.5         ), ], 
		[Coef('Var'  ,-0.28259     ), Coef('Var'  ,-0.359351    ), Coef('Var'  ,-0.812086    ), Coef('Var'  ,-0.359935    ), Coef('Var'  ,-0.248533    ), Coef('Var'  , 0.319661    ), Coef('Var'  , 0           ), Coef('Var'  , 0           ), Coef('Var'  , 0           ), Coef('Var'  , 0.35968     ), ], 
		[Coef('Const', 1           ), Coef('Const', 1           ), Coef('Const', 1           ), Coef('Const', 1           ), Coef('Const', 1           ), Coef('Const', 1           ), Coef('Const', 1           ), Coef('Const', 1           ), Coef('Const', 1           ), Coef('Const', 1           ), ], ])
	etat0.initMat[Chem([Sub('5')])] = FMat([
		[Coef('Const', 1.2         ), Coef('Const', 1.1         ), Coef('Const', 1           ), Coef('Const', 1.5         ), Coef('Const', 2           ), Coef('Const', 2           ), Coef('Const', 2           ), Coef('Const', 1.6         ), ], 
		[Coef('Const', 3           ), Coef('Const', 2.5         ), Coef('Const', 2           ), Coef('Const', 2           ), Coef('Const', 2           ), Coef('Const', 2.5         ), Coef('Const', 3           ), Coef('Const', 3           ), ], 
		[Coef('Var'  , 0           ), Coef('Var'  , 0.81277     ), Coef('Var'  ,-0.28259     ), Coef('Var'  , 0.576932    ), Coef('Var'  , 0.357254    ), Coef('Var'  , 0.0912814   ), Coef('Var'  , 0.364488    ), Coef('Var'  , 0.761569    ), ], 
		[Coef('Const', 1           ), Coef('Const', 1           ), Coef('Const', 1           ), Coef('Const', 1           ), Coef('Const', 1           ), Coef('Const', 1           ), Coef('Const', 1           ), Coef('Const', 1           ), ], ])
	etat0.initMat[Chem([Sub('4')])] = FMat([
		[Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0.2         ), Coef('Const', 0.4         ), Coef('Const', 0.7         ), Coef('Const', 1           ), Coef('Const', 1.1         ), Coef('Const', 1.2         ), Coef('Const', 1.1         ), ], 
		[Coef('Const', 4           ), Coef('Const', 3.5         ), Coef('Const', 3           ), Coef('Const', 2.7         ), Coef('Const', 2.4         ), Coef('Const', 2.2         ), Coef('Const', 2           ), Coef('Const', 2.5         ), Coef('Const', 3           ), Coef('Const', 3.5         ), ], 
		[Coef('Var'  ,-0.231095    ), Coef('Var'  , 0           ), Coef('Var'  , 0           ), Coef('Var'  , 0.368251    ), Coef('Var'  ,-0.812086    ), Coef('Var'  ,-0.359351    ), Coef('Var'  ,-0.28259     ), Coef('Var'  , 0.81277     ), Coef('Var'  , 0           ), Coef('Var'  ,-0.0851461   ), ], 
		[Coef('Const', 1           ), Coef('Const', 1           ), Coef('Const', 1           ), Coef('Const', 1           ), Coef('Const', 1           ), Coef('Const', 1           ), Coef('Const', 1           ), Coef('Const', 1           ), Coef('Const', 1           ), Coef('Const', 1           ), ], ])
	etat0.initMat[Chem([Sub('3')])] = FMat([
		[Coef('Const', 0.4         ), Coef('Const', 0.2         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.2         ), ], 
		[Coef('Const', 2.4         ), Coef('Const', 2.7         ), Coef('Const', 3           ), Coef('Const', 2.5         ), Coef('Const', 2           ), Coef('Const', 2.2         ), ], 
		[Coef('Var'  ,-0.812086    ), Coef('Var'  , 0.368251    ), Coef('Var'  , 0           ), Coef('Var'  , 0.803562    ), Coef('Var'  ,-0.248533    ), Coef('Var'  ,-0.359935    ), ], 
		[Coef('Const', 1           ), Coef('Const', 1           ), Coef('Const', 1           ), Coef('Const', 1           ), Coef('Const', 1           ), Coef('Const', 1           ), ], ])
	etat0.initMat[Chem([Sub('2')])] = FMat([
		[Coef('Const', 1           ), Coef('Const', 2           ), Coef('Const', 3           ), Coef('Const', 3           ), Coef('Const', 3           ), Coef('Const', 2           ), ], 
		[Coef('Const', 5           ), Coef('Const', 4.5         ), Coef('Const', 4           ), Coef('Const', 4.5         ), Coef('Const', 5           ), Coef('Const', 5           ), ], 
		[Coef('Var'  , 0           ), Coef('Var'  , 0.200072    ), Coef('Var'  ,-0.281935    ), Coef('Var'  , 0.507699    ), Coef('Var'  , 0.26391     ), Coef('Var'  , 0.815962    ), ], 
		[Coef('Const', 1           ), Coef('Const', 1           ), Coef('Const', 1           ), Coef('Const', 1           ), Coef('Const', 1           ), Coef('Const', 1           ), ], ])
	etat0.initMat[Chem([Sub('1')])] = FMat([
		[Coef('Const', 1           ), Coef('Const', 1           ), Coef('Const', 1           ), Coef('Const', 2           ), Coef('Const', 3           ), Coef('Const', 2           ), ], 
		[Coef('Const', 5           ), Coef('Const', 4.5         ), Coef('Const', 4           ), Coef('Const', 4           ), Coef('Const', 4           ), Coef('Const', 4.5         ), ], 
		[Coef('Var'  , 0           ), Coef('Var'  , 0           ), Coef('Var'  ,-0.231095    ), Coef('Var'  ,-0.621738    ), Coef('Var'  ,-0.281935    ), Coef('Var'  , 0.200072    ), ], 
		[Coef('Const', 1           ), Coef('Const', 1           ), Coef('Const', 1           ), Coef('Const', 1           ), Coef('Const', 1           ), Coef('Const', 1           ), ], ])
	etat0.initMat[Chem([Sub('0')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 1           ), Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 3           ), Coef('Const', 3.5         ), Coef('Const', 4           ), Coef('Const', 4.5         ), Coef('Const', 5           ), Coef('Const', 5           ), Coef('Const', 5           ), Coef('Const', 4           ), ], 
		[Coef('Var'  , 0           ), Coef('Var'  , 0           ), Coef('Var'  ,-0.231095    ), Coef('Var'  , 0           ), Coef('Var'  , 0           ), Coef('Var'  ,-0.304399    ), Coef('Var'  , 0.351399    ), Coef('Var'  , 0.681923    ), ], 
		[Coef('Const', 1           ), Coef('Const', 1           ), Coef('Const', 1           ), Coef('Const', 1           ), Coef('Const', 1           ), Coef('Const', 1           ), Coef('Const', 1           ), Coef('Const', 1           ), ], ])
	
	
	
	etat1.bords   = {Bord('2'): etat10, Bord('1'): etat10, Bord('0'): etat11, }
	etat1.permuts = {}
	etat1.interns = {Intern('_'): etat1, }
	etat1.subs    = {Sub('3'): etat1, Sub('2'): etat1, Sub('1'): etat1, Sub('0'): etat4, Sub('G', True): Etat.etatPoint, }
	
	etat1.buildIntern()
	
	
	etat1.eqs = [
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
	
	
	etat1.prim.elems = [Figure(2, [Chem([Bord('0'), Sub('0'), Bord('0'), ]), Chem([Bord('0'), Sub('1'), Bord('0'), ]), Chem([Bord('0'), Sub('2'), Bord('0'), ]), Chem([Bord('1'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('1'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('1'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('1'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('2'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('2'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('2'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('2'), Sub('1'), Sub('1'), Bord('0'), ]), ])]
	etat1.grid.elems = [
		Figure(1, [Chem([Bord('0'), Bord('0'), ]), Chem([Bord('0'), Intern(''), ]), Chem([Bord('0'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('1'), Bord('0'), ]), Chem([Bord('1'), Intern(''), ]), Chem([Bord('1'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('2'), Bord('0'), ]), Chem([Bord('2'), Intern(''), ]), Chem([Bord('2'), Bord('1'), ]), ]), ]
	
	
	etat1.space = [Chem([Bord('2'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('2'), Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('2'), Intern('0'), Intern('0'), ]), ]
	
	etat1.initMat[Chem([Sub('3')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.1111      ), Coef('Var'  , 0.0555583   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.3333      ), Coef('Const', 0.4444      ), Coef('Var'  , 0.222208    ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 1           ), Coef('Const', 0.6667      ), Coef('Const', 0.4444      ), Coef('Var'  , 0.347208    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.250008    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.125008    ), Coef('Const', 0.25        ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 8.33334e-06 ), Coef('Const', 0           ), Coef('Const', 0           ), ], ])
	etat1.initMat[Chem([Sub('2')])] = FMat([
		[Coef('Const', 0.1111      ), Coef('Const', 0.2222      ), Coef('Const', 0.4444      ), Coef('Var'  , 0.322896    ), Coef('Var'  , 0.201379    ), Coef('Var'  , 0.156246    ), ], 
		[Coef('Const', 0.4444      ), Coef('Const', 0.5556      ), Coef('Const', 0.4444      ), Coef('Var'  , 0.333286    ), Coef('Var'  , 0.222176    ), Coef('Var'  , 0.333286    ), ], 
		[Coef('Const', 0.4444      ), Coef('Const', 0.2222      ), Coef('Const', 0.1111      ), Coef('Var'  , 0.156225    ), Coef('Var'  , 0.201353    ), Coef('Var'  , 0.322875    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0625252   ), Coef('Var'  , 0.125024    ), Coef('Var'  , 0.0625252   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0625275   ), Coef('Var'  , 0.125027    ), Coef('Var'  , 0.0625275   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0625396   ), Coef('Var'  , 0.125042    ), Coef('Var'  , 0.0625396   ), ], ])
	etat1.initMat[Chem([Sub('1')])] = FMat([
		[Coef('Const', 0.4444      ), Coef('Const', 0.6667      ), Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.347208    ), ], 
		[Coef('Const', 0.4444      ), Coef('Const', 0.3333      ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.222208    ), ], 
		[Coef('Const', 0.1111      ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0555583   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 8.33334e-06 ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.125008    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.250008    ), ], ])
	etat1.initMat[Chem([Sub('0')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.100688    ), Coef('Var'  , 0.201379    ), Coef('Var'  , 0.225688    ), Coef('Const', 0.25        ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.111078    ), Coef('Var'  , 0.222176    ), Coef('Var'  , 0.111078    ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.225667    ), Coef('Var'  , 0.201353    ), Coef('Var'  , 0.100667    ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.312517    ), Coef('Var'  , 0.125024    ), Coef('Var'  , 0.0625168   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.187519    ), Coef('Var'  , 0.125027    ), Coef('Var'  , 0.187519    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0625313   ), Coef('Var'  , 0.125042    ), Coef('Var'  , 0.312531    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), ], ])
	etat1.initMat[Chem([Sub('G')])] = FMat([
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], ])
	
	
	
	etat2.bords   = {Bord('2'): etat11, Bord('1'): etat11, Bord('0'): etat11, }
	etat2.permuts = {}
	etat2.interns = {Intern('_'): etat2, }
	etat2.subs    = {Sub('6'): etat2, Sub('5'): etat2, Sub('4'): etat2, Sub('3'): etat2, Sub('2'): etat2, Sub('1'): etat2, Sub('0'): etat2, Sub('G', True): Etat.etatPoint, }
	
	etat2.buildIntern()
	
	
	etat2.eqs = [
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
	
	
	etat2.prim.elems = [Figure(2, [Chem([Bord('0'), Sub('0'), Bord('0'), ]), Chem([Bord('0'), Sub('1'), Bord('0'), ]), Chem([Bord('0'), Sub('2'), Bord('0'), ]), Chem([Bord('1'), Sub('0'), Bord('0'), ]), Chem([Bord('1'), Sub('1'), Bord('0'), ]), Chem([Bord('1'), Sub('2'), Bord('0'), ]), Chem([Bord('2'), Sub('0'), Bord('0'), ]), Chem([Bord('2'), Sub('1'), Bord('0'), ]), Chem([Bord('2'), Sub('2'), Bord('0'), ]), ])]
	etat2.grid.elems = [
		Figure(1, [Chem([Bord('0'), Bord('0'), ]), Chem([Bord('0'), Intern(''), ]), Chem([Bord('0'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('1'), Bord('0'), ]), Chem([Bord('1'), Intern(''), ]), Chem([Bord('1'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('2'), Bord('0'), ]), Chem([Bord('2'), Intern(''), ]), Chem([Bord('2'), Bord('1'), ]), ]), ]
	
	
	etat2.space = [Chem([Bord('2'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('2'), Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('2'), Intern('0'), Intern('0'), ]), ]
	
	etat2.initMat[Chem([Sub('6')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0544784   ), Coef('Var'  , 0.0493568   ), Coef('Var'  , 0.0143568   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.192827    ), Coef('Var'  , 0.136912    ), Coef('Var'  , 0.0838434   ), ], 
		[Coef('Const', 0.1111      ), Coef('Const', 0.2222      ), Coef('Const', 0.4444      ), Coef('Var'  , 0.331175    ), Coef('Var'  , 0.224468    ), Coef('Var'  , 0.15333     ), ], 
		[Coef('Const', 0.4444      ), Coef('Const', 0.5556      ), Coef('Const', 0.4444      ), Coef('Var'  , 0.222761    ), Coef('Var'  , 0.225322    ), Coef('Var'  , 0.242822    ), ], 
		[Coef('Const', 0.4444      ), Coef('Const', 0.2222      ), Coef('Const', 0.1111      ), Coef('Var'  , 0.114346    ), Coef('Var'  , 0.226175    ), Coef('Var'  , 0.332313    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0844123   ), Coef('Var'  , 0.137766    ), Coef('Var'  , 0.173335    ), ], ])
	etat2.initMat[Chem([Sub('5')])] = FMat([
		[Coef('Var'  , 0.0493568   ), Coef('Var'  , 0.117649    ), Coef('Var'  , 0.220942    ), Coef('Var'  , 0.302039    ), Coef('Var'  , 0.232039    ), Coef('Var'  , 0.0689904   ), ], 
		[Coef('Var'  , 0.136912    ), Coef('Var'  , 0.192755    ), Coef('Var'  , 0.218081    ), Coef('Var'  , 0.204565    ), Coef('Var'  , 0.133284    ), Coef('Var'  , 0.088396    ), ], 
		[Coef('Var'  , 0.224468    ), Coef('Var'  , 0.267862    ), Coef('Var'  , 0.21522     ), Coef('Var'  , 0.10709     ), Coef('Var'  , 0.0345287   ), Coef('Var'  , 0.107801    ), ], 
		[Coef('Var'  , 0.225322    ), Coef('Var'  , 0.191176    ), Coef('Var'  , 0.139529    ), Coef('Var'  , 0.0989804   ), Coef('Var'  , 0.13398     ), Coef('Var'  , 0.215505    ), ], 
		[Coef('Var'  , 0.226175    ), Coef('Var'  , 0.114489    ), Coef('Var'  , 0.0638384   ), Coef('Var'  , 0.0908708   ), Coef('Var'  , 0.233432    ), Coef('Var'  , 0.323208    ), ], 
		[Coef('Var'  , 0.137766    ), Coef('Var'  , 0.116069    ), Coef('Var'  , 0.14239     ), Coef('Var'  , 0.196455    ), Coef('Var'  , 0.232736    ), Coef('Var'  , 0.196099    ), ], ])
	etat2.initMat[Chem([Sub('4')])] = FMat([
		[Coef('Var'  , 0.232039    ), Coef('Var'  , 0.318869    ), Coef('Const', 0.4444      ), Coef('Const', 0.2222      ), Coef('Const', 0.1111      ), Coef('Var'  , 0.152406    ), ], 
		[Coef('Var'  , 0.133284    ), Coef('Var'  , 0.174056    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0886908   ), ], 
		[Coef('Var'  , 0.0345287   ), Coef('Var'  , 0.029244    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.024976    ), ], 
		[Coef('Var'  , 0.13398     ), Coef('Var'  , 0.0905656   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.173797    ), ], 
		[Coef('Var'  , 0.233432    ), Coef('Var'  , 0.151887    ), Coef('Const', 0.1111      ), Coef('Const', 0.2222      ), Coef('Const', 0.4444      ), Coef('Var'  , 0.322618    ), ], 
		[Coef('Var'  , 0.232736    ), Coef('Var'  , 0.235378    ), Coef('Const', 0.4444      ), Coef('Const', 0.5556      ), Coef('Const', 0.4444      ), Coef('Var'  , 0.237512    ), ], ])
	etat2.initMat[Chem([Sub('3')])] = FMat([
		[Coef('Const', 0.1111      ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0997223   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0927354   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.1111      ), Coef('Var'  , 0.0857486   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.3333      ), Coef('Const', 0.4444      ), Coef('Var'  , 0.200139    ), ], 
		[Coef('Const', 0.4444      ), Coef('Const', 0.6667      ), Coef('Const', 1           ), Coef('Const', 0.6667      ), Coef('Const', 0.4444      ), Coef('Var'  , 0.314529    ), ], 
		[Coef('Const', 0.4444      ), Coef('Const', 0.3333      ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.207126    ), ], ])
	etat2.initMat[Chem([Sub('2')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.1111      ), Coef('Var'  , 0.0647224   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.3333      ), Coef('Const', 0.4444      ), Coef('Var'  , 0.213599    ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 1           ), Coef('Const', 0.6667      ), Coef('Const', 0.4444      ), Coef('Var'  , 0.362476    ), Coef('Const', 0.4444      ), Coef('Const', 0.6667      ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.217639    ), Coef('Const', 0.4444      ), Coef('Const', 0.3333      ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0728016   ), Coef('Const', 0.1111      ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.068762    ), Coef('Const', 0           ), Coef('Const', 0           ), ], ])
	etat2.initMat[Chem([Sub('1')])] = FMat([
		[Coef('Const', 0.1111      ), Coef('Const', 0.2222      ), Coef('Const', 0.4444      ), Coef('Var'  , 0.331064    ), Coef('Var'  , 0.220942    ), Coef('Var'  , 0.10143     ), ], 
		[Coef('Const', 0.4444      ), Coef('Const', 0.5556      ), Coef('Const', 0.4444      ), Coef('Var'  , 0.232949    ), Coef('Var'  , 0.218081    ), Coef('Var'  , 0.218436    ), ], 
		[Coef('Const', 0.4444      ), Coef('Const', 0.2222      ), Coef('Const', 0.1111      ), Coef('Var'  , 0.134834    ), Coef('Var'  , 0.21522     ), Coef('Var'  , 0.335443    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.084468    ), Coef('Var'  , 0.139529    ), Coef('Var'  , 0.199285    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.034102    ), Coef('Var'  , 0.0638384   ), Coef('Var'  , 0.0631271   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.182583    ), Coef('Var'  , 0.14239     ), Coef('Var'  , 0.0822783   ), ], ])
	etat2.initMat[Chem([Sub('0')])] = FMat([
		[Coef('Const', 0.4444      ), Coef('Const', 0.6667      ), Coef('Const', 1           ), Coef('Const', 0.6667      ), Coef('Const', 0.4444      ), Coef('Var'  , 0.3396      ), ], 
		[Coef('Const', 0.4444      ), Coef('Const', 0.3333      ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.202003    ), ], 
		[Coef('Const', 0.1111      ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0644067   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0802      ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.1111      ), Coef('Var'  , 0.0959933   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.3333      ), Coef('Const', 0.4444      ), Coef('Var'  , 0.217797    ), ], ])
	etat2.initMat[Chem([Sub('G')])] = FMat([
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], ])
	
	
	
	etat3.bords   = {Bord('4'): etat10, Bord('3'): etat10, Bord('2'): etat10, Bord('1'): etat10, Bord('0'): etat10, }
	etat3.permuts = {}
	etat3.interns = {Intern('_'): etat3, }
	etat3.subs    = {Sub('8'): etat3, Sub('7'): etat3, Sub('6'): etat3, Sub('5'): etat3, Sub('4'): etat3, Sub('3'): etat3, Sub('2'): etat3, Sub('1'): etat3, Sub('0'): etat3, Sub('G', True): Etat.etatPoint, Sub('10'): etat3, Sub('9'): etat3, }
	
	etat3.buildIntern()
	
	
	etat3.eqs = [
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
	
	
	etat3.prim.elems = [Figure(2, [Chem([Bord('0'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('0'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('0'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('0'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('1'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('1'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('1'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('1'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('2'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('2'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('2'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('2'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('3'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('3'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('3'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('3'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('4'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('4'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('4'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('4'), Sub('1'), Sub('1'), Bord('0'), ]), ])]
	etat3.grid.elems = [
		Figure(1, [Chem([Bord('0'), Bord('0'), ]), Chem([Bord('0'), Intern(''), ]), Chem([Bord('0'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('1'), Bord('0'), ]), Chem([Bord('1'), Intern(''), ]), Chem([Bord('1'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('2'), Bord('0'), ]), Chem([Bord('2'), Intern(''), ]), Chem([Bord('2'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('3'), Bord('0'), ]), Chem([Bord('3'), Intern(''), ]), Chem([Bord('3'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('4'), Bord('0'), ]), Chem([Bord('4'), Intern(''), ]), Chem([Bord('4'), Bord('1'), ]), ]), ]
	
	
	etat3.space = [Chem([Bord('4'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('2'), Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('2'), Intern('0'), Intern('0'), ]), Chem([Bord('3'), Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('3'), Intern('0'), Intern('0'), ]), Chem([Bord('4'), Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('4'), Intern('0'), Intern('0'), ]), ]
	
	etat3.initMat[Chem([Sub('8')])] = FMat([
		[Coef('Var'  , 0.0851498   ), Coef('Var'  , 0.0928919   ), Coef('Var'  , 0.101055    ), Coef('Var'  , 0.0866666   ), Coef('Var'  , 0.0729064   ), Coef('Var'  , 0.058896    ), Coef('Var'  , 0.0444954   ), Coef('Var'  , 0.0539153   ), Coef('Var'  , 0.0620632   ), Coef('Var'  , 0.0739973   ), ], 
		[Coef('Var'  , 0.0846868   ), Coef('Var'  , 0.0808385   ), Coef('Var'  , 0.0757306   ), Coef('Var'  , 0.0611489   ), Coef('Var'  , 0.0453175   ), Coef('Var'  , 0.0431348   ), Coef('Var'  , 0.039435    ), Coef('Var'  , 0.0528103   ), Coef('Var'  , 0.0643614   ), Coef('Var'  , 0.0753484   ), ], 
		[Coef('Var'  , 0.0857188   ), Coef('Var'  , 0.0797275   ), Coef('Var'  , 0.0719887   ), Coef('Var'  , 0.0590486   ), Coef('Var'  , 0.0441123   ), Coef('Var'  , 0.0447218   ), Coef('Var'  , 0.0434466   ), Coef('Var'  , 0.057945    ), Coef('Var'  , 0.0707322   ), Coef('Var'  , 0.0790043   ), ], 
		[Coef('Var'  , 0.087535    ), Coef('Var'  , 0.079273    ), Coef('Var'  , 0.0686778   ), Coef('Var'  , 0.0571077   ), Coef('Var'  , 0.0428848   ), Coef('Var'  , 0.0462173   ), Coef('Var'  , 0.0473938   ), Coef('Var'  , 0.0632674   ), Coef('Var'  , 0.0774763   ), Coef('Var'  , 0.0833427   ), ], 
		[Coef('Var'  , 0.0933463   ), Coef('Var'  , 0.0811046   ), Coef('Var'  , 0.0677556   ), Coef('Var'  , 0.0584181   ), Coef('Var'  , 0.0477749   ), Coef('Var'  , 0.062756    ), Coef('Var'  , 0.077207    ), Coef('Var'  , 0.0927998   ), Coef('Var'  , 0.108529    ), Coef('Var'  , 0.101035    ), ], 
		[Coef('Var'  , 0.113595    ), Coef('Var'  , 0.0972149   ), Coef('Var'  , 0.080294    ), Coef('Var'  , 0.0710486   ), Coef('Var'  , 0.0610174   ), Coef('Var'  , 0.0872335   ), Coef('Var'  , 0.113971    ), Coef('Var'  , 0.131325    ), Coef('Var'  , 0.150339    ), Coef('Var'  , 0.131467    ), ], 
		[Coef('Var'  , 0.106203    ), Coef('Var'  , 0.10387     ), Coef('Var'  , 0.103       ), Coef('Var'  , 0.125463    ), Coef('Var'  , 0.149015    ), Coef('Var'  , 0.161182    ), Coef('Var'  , 0.174982    ), Coef('Var'  , 0.154784    ), Coef('Var'  , 0.137036    ), Coef('Var'  , 0.120456    ), ], 
		[Coef('Var'  , 0.117568    ), Coef('Var'  , 0.127731    ), Coef('Var'  , 0.14003     ), Coef('Var'  , 0.191517    ), Coef('Var'  , 0.245343    ), Coef('Var'  , 0.244062    ), Coef('Var'  , 0.245145    ), Coef('Var'  , 0.191206    ), Coef('Var'  , 0.139602    ), Coef('Var'  , 0.127516    ), ], 
		[Coef('Var'  , 0.115613    ), Coef('Var'  , 0.129502    ), Coef('Var'  , 0.14494     ), Coef('Var'  , 0.161342    ), Coef('Var'  , 0.179674    ), Coef('Var'  , 0.165837    ), Coef('Var'  , 0.153388    ), Coef('Var'  , 0.13151     ), Coef('Var'  , 0.110399    ), Coef('Var'  , 0.112603    ), ], 
		[Coef('Var'  , 0.110585    ), Coef('Var'  , 0.127847    ), Coef('Var'  , 0.146528    ), Coef('Var'  , 0.12824     ), Coef('Var'  , 0.111954    ), Coef('Var'  , 0.0859601   ), Coef('Var'  , 0.0605355   ), Coef('Var'  , 0.0704365   ), Coef('Var'  , 0.0794613   ), Coef('Var'  , 0.0952308   ), ], ])
	etat3.initMat[Chem([Sub('7')])] = FMat([
		[Coef('Var'  , 0.037643    ), Coef('Var'  , 0.0377879   ), Coef('Var'  , 0.036602    ), Coef('Var'  , 0.0489261   ), Coef('Var'  , 0.060202    ), Coef('Var'  , 0.0674267   ), Coef('Var'  , 0.0737488   ), Coef('Var'  , 0.0684916   ), Coef('Var'  , 0.0620632   ), Coef('Var'  , 0.0505881   ), ], 
		[Coef('Var'  , 0.0391142   ), Coef('Var'  , 0.042255    ), Coef('Var'  , 0.0440301   ), Coef('Var'  , 0.0594338   ), Coef('Var'  , 0.073895    ), Coef('Var'  , 0.0793482   ), Coef('Var'  , 0.0838177   ), Coef('Var'  , 0.0748683   ), Coef('Var'  , 0.0643614   ), Coef('Var'  , 0.0526354   ), ], 
		[Coef('Var'  , 0.0497185   ), Coef('Var'  , 0.0642312   ), Coef('Var'  , 0.0780696   ), Coef('Var'  , 0.0935593   ), Coef('Var'  , 0.109344    ), Coef('Var'  , 0.102271    ), Coef('Var'  , 0.0953889   ), Coef('Var'  , 0.0835342   ), Coef('Var'  , 0.0707322   ), Coef('Var'  , 0.0609577   ), ], 
		[Coef('Var'  , 0.0599546   ), Coef('Var'  , 0.0853378   ), Coef('Var'  , 0.111037    ), Coef('Var'  , 0.12661     ), Coef('Var'  , 0.144067    ), Coef('Var'  , 0.125009    ), Coef('Var'  , 0.107333    ), Coef('Var'  , 0.0926733   ), Coef('Var'  , 0.0774763   ), Coef('Var'  , 0.0692904   ), ], 
		[Coef('Var'  , 0.152524    ), Coef('Var'  , 0.164801    ), Coef('Var'  , 0.178382    ), Coef('Var'  , 0.159386    ), Coef('Var'  , 0.142334    ), Coef('Var'  , 0.126744    ), Coef('Var'  , 0.112634    ), Coef('Var'  , 0.110291    ), Coef('Var'  , 0.108529    ), Coef('Var'  , 0.13026     ), ], 
		[Coef('Var'  , 0.251666    ), Coef('Var'  , 0.251223    ), Coef('Var'  , 0.252738    ), Coef('Var'  , 0.201725    ), Coef('Var'  , 0.152315    ), Coef('Var'  , 0.141321    ), Coef('Var'  , 0.131591    ), Coef('Var'  , 0.140206    ), Coef('Var'  , 0.150339    ), Coef('Var'  , 0.200006    ), ], 
		[Coef('Var'  , 0.175013    ), Coef('Var'  , 0.161321    ), Coef('Var'  , 0.149309    ), Coef('Var'  , 0.125893    ), Coef('Var'  , 0.10358     ), Coef('Var'  , 0.104333    ), Coef('Var'  , 0.106519    ), Coef('Var'  , 0.120623    ), Coef('Var'  , 0.137036    ), Coef('Var'  , 0.154789    ), ], 
		[Coef('Var'  , 0.107685    ), Coef('Var'  , 0.0807004   ), Coef('Var'  , 0.0545148   ), Coef('Var'  , 0.0620471   ), Coef('Var'  , 0.0692791   ), Coef('Var'  , 0.0846815   ), Coef('Var'  , 0.100185    ), Coef('Var'  , 0.119123    ), Coef('Var'  , 0.139602    ), Coef('Var'  , 0.122658    ), ], 
		[Coef('Var'  , 0.0783635   ), Coef('Var'  , 0.0645872   ), Coef('Var'  , 0.0502219   ), Coef('Var'  , 0.0619128   ), Coef('Var'  , 0.0719912   ), Coef('Var'  , 0.0851922   ), Coef('Var'  , 0.097092    ), Coef('Var'  , 0.103773    ), Coef('Var'  , 0.110399    ), Coef('Var'  , 0.0942098   ), ], 
		[Coef('Var'  , 0.0483184   ), Coef('Var'  , 0.047755    ), Coef('Var'  , 0.0450956   ), Coef('Var'  , 0.0605058   ), Coef('Var'  , 0.0729928   ), Coef('Var'  , 0.0836731   ), Coef('Var'  , 0.0916915   ), Coef('Var'  , 0.0864164   ), Coef('Var'  , 0.0794613   ), Coef('Var'  , 0.0646064   ), ], ])
	etat3.initMat[Chem([Sub('6')])] = FMat([
		[Coef('Var'  , 0.102455    ), Coef('Var'  , 0.0997893   ), Coef('Var'  , 0.0987911   ), Coef('Var'  , 0.121808    ), Coef('Var'  , 0.146281    ), Coef('Var'  , 0.158838    ), Coef('Var'  , 0.173249    ), Coef('Var'  , 0.152748    ), Coef('Var'  , 0.134685    ), Coef('Var'  , 0.117428    ), ], 
		[Coef('Var'  , 0.124407    ), Coef('Var'  , 0.133918    ), Coef('Var'  , 0.145204    ), Coef('Var'  , 0.196238    ), Coef('Var'  , 0.249234    ), Coef('Var'  , 0.248786    ), Coef('Var'  , 0.250125    ), Coef('Var'  , 0.197643    ), Coef('Var'  , 0.146761    ), Coef('Var'  , 0.13481     ), ], 
		[Coef('Var'  , 0.114956    ), Coef('Var'  , 0.12869     ), Coef('Var'  , 0.14414     ), Coef('Var'  , 0.16087     ), Coef('Var'  , 0.179625    ), Coef('Var'  , 0.166214    ), Coef('Var'  , 0.154043    ), Coef('Var'  , 0.13219     ), Coef('Var'  , 0.110836    ), Coef('Var'  , 0.112526    ), ], 
		[Coef('Var'  , 0.10616     ), Coef('Var'  , 0.123852    ), Coef('Var'  , 0.14314     ), Coef('Var'  , 0.125526    ), Coef('Var'  , 0.110003    ), Coef('Var'  , 0.0839238   ), Coef('Var'  , 0.0584628   ), Coef('Var'  , 0.067495    ), Coef('Var'  , 0.0757662   ), Coef('Var'  , 0.0910697   ), ], 
		[Coef('Var'  , 0.0911623   ), Coef('Var'  , 0.0982114   ), Coef('Var'  , 0.105716    ), Coef('Var'  , 0.0900127   ), Coef('Var'  , 0.0750228   ), Coef('Var'  , 0.0607098   ), Coef('Var'  , 0.0462332   ), Coef('Var'  , 0.0566837   ), Coef('Var'  , 0.0661513   ), Coef('Var'  , 0.0789703   ), ], 
		[Coef('Var'  , 0.0938517   ), Coef('Var'  , 0.0895324   ), Coef('Var'  , 0.083188    ), Coef('Var'  , 0.067436    ), Coef('Var'  , 0.0499115   ), Coef('Var'  , 0.0479575   ), Coef('Var'  , 0.0441271   ), Coef('Var'  , 0.0592311   ), Coef('Var'  , 0.0720151   ), Coef('Var'  , 0.0841315   ), ], 
		[Coef('Var'  , 0.0789244   ), Coef('Var'  , 0.0734919   ), Coef('Var'  , 0.0664853   ), Coef('Var'  , 0.0547072   ), Coef('Var'  , 0.0410108   ), Coef('Var'  , 0.0415488   ), Coef('Var'  , 0.0402785   ), Coef('Var'  , 0.0535689   ), Coef('Var'  , 0.0653096   ), Coef('Var'  , 0.0727928   ), ], 
		[Coef('Var'  , 0.0791897   ), Coef('Var'  , 0.0705045   ), Coef('Var'  , 0.060274    ), Coef('Var'  , 0.0494501   ), Coef('Var'  , 0.036879    ), Coef('Var'  , 0.0402654   ), Coef('Var'  , 0.0422552   ), Coef('Var'  , 0.0569823   ), Coef('Var'  , 0.0706541   ), Coef('Var'  , 0.0754597   ), ], 
		[Coef('Var'  , 0.0969118   ), Coef('Var'  , 0.0849835   ), Coef('Var'  , 0.0717909   ), Coef('Var'  , 0.061662    ), Coef('Var'  , 0.0499829   ), Coef('Var'  , 0.0642924   ), Coef('Var'  , 0.0780885   ), Coef('Var'  , 0.0939082   ), Coef('Var'  , 0.110135    ), Coef('Var'  , 0.103532    ), ], 
		[Coef('Var'  , 0.111982    ), Coef('Var'  , 0.0970272   ), Coef('Var'  , 0.0812713   ), Coef('Var'  , 0.0722912   ), Coef('Var'  , 0.0620496   ), Coef('Var'  , 0.0874641   ), Coef('Var'  , 0.113137    ), Coef('Var'  , 0.129549    ), Coef('Var'  , 0.147687    ), Coef('Var'  , 0.12928     ), ], ])
	etat3.initMat[Chem([Sub('5')])] = FMat([
		[Coef('Var'  , 0.173621    ), Coef('Var'  , 0.159874    ), Coef('Var'  , 0.147816    ), Coef('Var'  , 0.123895    ), Coef('Var'  , 0.101055    ), Coef('Var'  , 0.101654    ), Coef('Var'  , 0.103555    ), Coef('Var'  , 0.118042    ), Coef('Var'  , 0.134685    ), Coef('Var'  , 0.152947    ), ], 
		[Coef('Var'  , 0.112895    ), Coef('Var'  , 0.0860536   ), Coef('Var'  , 0.0593154   ), Coef('Var'  , 0.0679838   ), Coef('Var'  , 0.0757306   ), Coef('Var'  , 0.0919162   ), Coef('Var'  , 0.107624    ), Coef('Var'  , 0.126753    ), Coef('Var'  , 0.146761    ), Coef('Var'  , 0.129221    ), ], 
		[Coef('Var'  , 0.0792334   ), Coef('Var'  , 0.0654965   ), Coef('Var'  , 0.0508484   ), Coef('Var'  , 0.0623153   ), Coef('Var'  , 0.0719887   ), Coef('Var'  , 0.0850524   ), Coef('Var'  , 0.0967722   ), Coef('Var'  , 0.103895    ), Coef('Var'  , 0.110836    ), Coef('Var'  , 0.0950192   ), ], 
		[Coef('Var'  , 0.046065    ), Coef('Var'  , 0.0452557   ), Coef('Var'  , 0.0425172   ), Coef('Var'  , 0.0568977   ), Coef('Var'  , 0.0686778   ), Coef('Var'  , 0.0788583   ), Coef('Var'  , 0.0867861   ), Coef('Var'  , 0.0819716   ), Coef('Var'  , 0.0757662   ), Coef('Var'  , 0.0615595   ), ], 
		[Coef('Var'  , 0.0398543   ), Coef('Var'  , 0.0409123   ), Coef('Var'  , 0.0406495   ), Coef('Var'  , 0.0549397   ), Coef('Var'  , 0.0677556   ), Coef('Var'  , 0.0751685   ), Coef('Var'  , 0.0811959   ), Coef('Var'  , 0.0742753   ), Coef('Var'  , 0.0661513   ), Coef('Var'  , 0.0536114   ), ], 
		[Coef('Var'  , 0.0435966   ), Coef('Var'  , 0.046525    ), Coef('Var'  , 0.0478556   ), Coef('Var'  , 0.0646858   ), Coef('Var'  , 0.080294    ), Coef('Var'  , 0.0871556   ), Coef('Var'  , 0.0924831   ), Coef('Var'  , 0.0833659   ), Coef('Var'  , 0.0720151   ), Coef('Var'  , 0.0589376   ), ], 
		[Coef('Var'  , 0.046294    ), Coef('Var'  , 0.0604228   ), Coef('Var'  , 0.0741578   ), Coef('Var'  , 0.088248    ), Coef('Var'  , 0.103       ), Coef('Var'  , 0.0953885   ), Coef('Var'  , 0.0883074   ), Coef('Var'  , 0.0771633   ), Coef('Var'  , 0.0653096   ), Coef('Var'  , 0.0564281   ), ], 
		[Coef('Var'  , 0.0556572   ), Coef('Var'  , 0.0816374   ), Coef('Var'  , 0.108231    ), Coef('Var'  , 0.123162    ), Coef('Var'  , 0.14003     ), Coef('Var'  , 0.119783    ), Coef('Var'  , 0.100996    ), Coef('Var'  , 0.0859056   ), Coef('Var'  , 0.0706541   ), Coef('Var'  , 0.063475    ), ], 
		[Coef('Var'  , 0.153168    ), Coef('Var'  , 0.165678    ), Coef('Var'  , 0.179614    ), Coef('Var'  , 0.161307    ), Coef('Var'  , 0.14494     ), Coef('Var'  , 0.129447    ), Coef('Var'  , 0.115509    ), Coef('Var'  , 0.112403    ), Coef('Var'  , 0.110135    ), Coef('Var'  , 0.131241    ), ], 
		[Coef('Var'  , 0.249615    ), Coef('Var'  , 0.248145    ), Coef('Var'  , 0.248995    ), Coef('Var'  , 0.196565    ), Coef('Var'  , 0.146528    ), Coef('Var'  , 0.135577    ), Coef('Var'  , 0.126772    ), Coef('Var'  , 0.136225    ), Coef('Var'  , 0.147687    ), Coef('Var'  , 0.197561    ), ], ])
	etat3.initMat[Chem([Sub('4')])] = FMat([
		[Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.211269    ), Coef('Var'  , 0.173621    ), Coef('Var'  , 0.172339    ), Coef('Var'  , 0.173249    ), Coef('Var'  , 0.21107     ), ], 
		[Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0562271   ), Coef('Var'  , 0.112895    ), Coef('Var'  , 0.180877    ), Coef('Var'  , 0.250125    ), Coef('Var'  , 0.37465     ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0396787   ), Coef('Var'  , 0.0792334   ), Coef('Var'  , 0.116528    ), Coef('Var'  , 0.154043    ), Coef('Var'  , 0.201849    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0234021   ), Coef('Var'  , 0.046065    ), Coef('Var'  , 0.0527397   ), Coef('Var'  , 0.0584628   ), Coef('Var'  , 0.0293376   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0202386   ), Coef('Var'  , 0.0398543   ), Coef('Var'  , 0.0435496   ), Coef('Var'  , 0.0462332   ), Coef('Var'  , 0.023311    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0222833   ), Coef('Var'  , 0.0435966   ), Coef('Var'  , 0.04486     ), Coef('Var'  , 0.0441271   ), Coef('Var'  , 0.0225768   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.023414    ), Coef('Var'  , 0.046294    ), Coef('Var'  , 0.0439688   ), Coef('Var'  , 0.0402785   ), Coef('Var'  , 0.0205548   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0279138   ), Coef('Var'  , 0.0556572   ), Coef('Var'  , 0.049335    ), Coef('Var'  , 0.0422552   ), Coef('Var'  , 0.0214212   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.201328    ), Coef('Var'  , 0.153168    ), Coef('Var'  , 0.115323    ), Coef('Var'  , 0.0780885   ), Coef('Var'  , 0.0389951   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.374246    ), Coef('Var'  , 0.249615    ), Coef('Var'  , 0.180481    ), Coef('Var'  , 0.113137    ), Coef('Var'  , 0.0562348   ), ], ])
	etat3.initMat[Chem([Sub('3')])] = FMat([
		[Coef('Var'  , 0.146281    ), Coef('Var'  , 0.108059    ), Coef('Var'  , 0.070943    ), Coef('Var'  , 0.035291    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.197768    ), ], 
		[Coef('Var'  , 0.249234    ), Coef('Var'  , 0.179464    ), Coef('Var'  , 0.11132     ), Coef('Var'  , 0.0553277   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.374136    ), ], 
		[Coef('Var'  , 0.179625    ), Coef('Var'  , 0.178631    ), Coef('Var'  , 0.179428    ), Coef('Var'  , 0.214266    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.214365    ), ], 
		[Coef('Var'  , 0.110003    ), Coef('Var'  , 0.177462    ), Coef('Var'  , 0.246997    ), Coef('Var'  , 0.372876    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0545861   ), ], 
		[Coef('Var'  , 0.0750228   ), Coef('Var'  , 0.112388    ), Coef('Var'  , 0.150587    ), Coef('Var'  , 0.199989    ), Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0373989   ), ], 
		[Coef('Var'  , 0.0499115   ), Coef('Var'  , 0.0573438   ), Coef('Var'  , 0.0634653   ), Coef('Var'  , 0.0319631   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0253808   ), ], 
		[Coef('Var'  , 0.0410108   ), Coef('Var'  , 0.0450809   ), Coef('Var'  , 0.047429    ), Coef('Var'  , 0.0240869   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.020994    ), ], 
		[Coef('Var'  , 0.036879    ), Coef('Var'  , 0.0375015   ), Coef('Var'  , 0.0365566   ), Coef('Var'  , 0.0186573   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0188442   ), ], 
		[Coef('Var'  , 0.0499829   ), Coef('Var'  , 0.047582    ), Coef('Var'  , 0.0436847   ), Coef('Var'  , 0.0222848   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0252972   ), ], 
		[Coef('Var'  , 0.0620496   ), Coef('Var'  , 0.0564877   ), Coef('Var'  , 0.0495895   ), Coef('Var'  , 0.0252584   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0312293   ), ], ])
	etat3.initMat[Chem([Sub('2')])] = FMat([
		[Coef('Var'  , 0.0832296   ), Coef('Var'  , 0.0922705   ), Coef('Var'  , 0.102455    ), Coef('Var'  , 0.102114    ), Coef('Var'  , 0.103555    ), Coef('Var'  , 0.0939653   ), Coef('Var'  , 0.0851498   ), Coef('Var'  , 0.0796976   ), Coef('Var'  , 0.0737488   ), Coef('Var'  , 0.0786164   ), ], 
		[Coef('Var'  , 0.106088    ), Coef('Var'  , 0.114716    ), Coef('Var'  , 0.124407    ), Coef('Var'  , 0.115575    ), Coef('Var'  , 0.107624    ), Coef('Var'  , 0.0964402   ), Coef('Var'  , 0.0846868   ), Coef('Var'  , 0.0848824   ), Coef('Var'  , 0.0838177   ), Coef('Var'  , 0.0951012   ), ], 
		[Coef('Var'  , 0.114163    ), Coef('Var'  , 0.113919    ), Coef('Var'  , 0.114956    ), Coef('Var'  , 0.10574     ), Coef('Var'  , 0.0967722   ), Coef('Var'  , 0.0917849   ), Coef('Var'  , 0.0857188   ), Coef('Var'  , 0.0909899   ), Coef('Var'  , 0.0953889   ), Coef('Var'  , 0.104493    ), ], 
		[Coef('Var'  , 0.122417    ), Coef('Var'  , 0.11359     ), Coef('Var'  , 0.10616     ), Coef('Var'  , 0.0967265   ), Coef('Var'  , 0.0867861   ), Coef('Var'  , 0.0880431   ), Coef('Var'  , 0.087535    ), Coef('Var'  , 0.0977884   ), Coef('Var'  , 0.107333    ), Coef('Var'  , 0.114238    ), ], 
		[Coef('Var'  , 0.111259    ), Coef('Var'  , 0.10091     ), Coef('Var'  , 0.0911623   ), Coef('Var'  , 0.0865      ), Coef('Var'  , 0.0811959   ), Coef('Var'  , 0.0877411   ), Coef('Var'  , 0.0933463   ), Coef('Var'  , 0.102934    ), Coef('Var'  , 0.112634    ), Coef('Var'  , 0.111407    ), ], 
		[Coef('Var'  , 0.115868    ), Coef('Var'  , 0.105524    ), Coef('Var'  , 0.0938517   ), Coef('Var'  , 0.0941887   ), Coef('Var'  , 0.0924831   ), Coef('Var'  , 0.103482    ), Coef('Var'  , 0.113595    ), Coef('Var'  , 0.12228     ), Coef('Var'  , 0.131591    ), Coef('Var'  , 0.123557    ), ], 
		[Coef('Var'  , 0.0890669   ), Coef('Var'  , 0.084355    ), Coef('Var'  , 0.0789244   ), Coef('Var'  , 0.083928    ), Coef('Var'  , 0.0883074   ), Coef('Var'  , 0.0967799   ), Coef('Var'  , 0.106203    ), Coef('Var'  , 0.105428    ), Coef('Var'  , 0.106519    ), Coef('Var'  , 0.097374    ), ], 
		[Coef('Var'  , 0.078609    ), Coef('Var'  , 0.0794722   ), Coef('Var'  , 0.0791897   ), Coef('Var'  , 0.0902431   ), Coef('Var'  , 0.100996    ), Coef('Var'  , 0.108637    ), Coef('Var'  , 0.117568    ), Coef('Var'  , 0.108193    ), Coef('Var'  , 0.100185    ), Coef('Var'  , 0.0894738   ), ], 
		[Coef('Var'  , 0.0867494   ), Coef('Var'  , 0.0924284   ), Coef('Var'  , 0.0969118   ), Coef('Var'  , 0.106109    ), Coef('Var'  , 0.115509    ), Coef('Var'  , 0.115035    ), Coef('Var'  , 0.115613    ), Coef('Var'  , 0.106259    ), Coef('Var'  , 0.097092    ), Coef('Var'  , 0.0925243   ), ], 
		[Coef('Var'  , 0.0925498   ), Coef('Var'  , 0.102814    ), Coef('Var'  , 0.111982    ), Coef('Var'  , 0.118876    ), Coef('Var'  , 0.126772    ), Coef('Var'  , 0.118091    ), Coef('Var'  , 0.110585    ), Coef('Var'  , 0.101547    ), Coef('Var'  , 0.0916915   ), Coef('Var'  , 0.0932152   ), ], ])
	etat3.initMat[Chem([Sub('1')])] = FMat([
		[Coef('Var'  , 0.060202    ), Coef('Var'  , 0.0518054   ), Coef('Var'  , 0.0426548   ), Coef('Var'  , 0.0567657   ), Coef('Var'  , 0.070943    ), Coef('Var'  , 0.0843302   ), Coef('Var'  , 0.0987911   ), Coef('Var'  , 0.0905597   ), Coef('Var'  , 0.0832296   ), Coef('Var'  , 0.0718512   ), ], 
		[Coef('Var'  , 0.073895    ), Coef('Var'  , 0.0660576   ), Coef('Var'  , 0.0576637   ), Coef('Var'  , 0.0842382   ), Coef('Var'  , 0.11132     ), Coef('Var'  , 0.12743     ), Coef('Var'  , 0.145204    ), Coef('Var'  , 0.125002    ), Coef('Var'  , 0.106088    ), Coef('Var'  , 0.0900472   ), ], 
		[Coef('Var'  , 0.109344    ), Coef('Var'  , 0.130885    ), Coef('Var'  , 0.153147    ), Coef('Var'  , 0.165639    ), Coef('Var'  , 0.179428    ), Coef('Var'  , 0.16077     ), Coef('Var'  , 0.14414     ), Coef('Var'  , 0.128238    ), Coef('Var'  , 0.114163    ), Coef('Var'  , 0.111245    ), ], 
		[Coef('Var'  , 0.144067    ), Coef('Var'  , 0.194603    ), Coef('Var'  , 0.2475      ), Coef('Var'  , 0.246029    ), Coef('Var'  , 0.246997    ), Coef('Var'  , 0.193815    ), Coef('Var'  , 0.14314     ), Coef('Var'  , 0.131617    ), Coef('Var'  , 0.122417    ), Coef('Var'  , 0.132127    ), ], 
		[Coef('Var'  , 0.142334    ), Coef('Var'  , 0.159111    ), Coef('Var'  , 0.177883    ), Coef('Var'  , 0.163452    ), Coef('Var'  , 0.150587    ), Coef('Var'  , 0.127603    ), Coef('Var'  , 0.105716    ), Coef('Var'  , 0.107926    ), Coef('Var'  , 0.111259    ), Coef('Var'  , 0.125961    ), ], 
		[Coef('Var'  , 0.152315    ), Coef('Var'  , 0.133558    ), Coef('Var'  , 0.115965    ), Coef('Var'  , 0.0897093   ), Coef('Var'  , 0.0634653   ), Coef('Var'  , 0.0740183   ), Coef('Var'  , 0.083188    ), Coef('Var'  , 0.100103    ), Coef('Var'  , 0.115868    ), Coef('Var'  , 0.133859    ), ], 
		[Coef('Var'  , 0.10358     ), Coef('Var'  , 0.0889074   ), Coef('Var'  , 0.0748245   ), Coef('Var'  , 0.0614586   ), Coef('Var'  , 0.047429    ), Coef('Var'  , 0.0578001   ), Coef('Var'  , 0.0664853   ), Coef('Var'  , 0.0782894   ), Coef('Var'  , 0.0890669   ), Coef('Var'  , 0.0961119   ), ], 
		[Coef('Var'  , 0.0692791   ), Coef('Var'  , 0.0555606   ), Coef('Var'  , 0.0411385   ), Coef('Var'  , 0.0394366   ), Coef('Var'  , 0.0365566   ), Coef('Var'  , 0.0492632   ), Coef('Var'  , 0.060274    ), Coef('Var'  , 0.0701795   ), Coef('Var'  , 0.078609    ), Coef('Var'  , 0.074355    ), ], 
		[Coef('Var'  , 0.0719912   ), Coef('Var'  , 0.0588337   ), Coef('Var'  , 0.0438089   ), Coef('Var'  , 0.044641    ), Coef('Var'  , 0.0436847   ), Coef('Var'  , 0.0586495   ), Coef('Var'  , 0.0717909   ), Coef('Var'  , 0.0801744   ), Coef('Var'  , 0.0867494   ), Coef('Var'  , 0.0802871   ), ], 
		[Coef('Var'  , 0.0729928   ), Coef('Var'  , 0.0606793   ), Coef('Var'  , 0.0454151   ), Coef('Var'  , 0.0486308   ), Coef('Var'  , 0.0495895   ), Coef('Var'  , 0.0663204   ), Coef('Var'  , 0.0812713   ), Coef('Var'  , 0.0879109   ), Coef('Var'  , 0.0925498   ), Coef('Var'  , 0.0841559   ), ], ])
	etat3.initMat[Chem([Sub('0')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0191925   ), Coef('Var'  , 0.037643    ), Coef('Var'  , 0.0417122   ), Coef('Var'  , 0.0444954   ), Coef('Var'  , 0.0225197   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0199683   ), Coef('Var'  , 0.0391142   ), Coef('Var'  , 0.0401115   ), Coef('Var'  , 0.039435    ), Coef('Var'  , 0.0201432   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0251834   ), Coef('Var'  , 0.0497185   ), Coef('Var'  , 0.0473541   ), Coef('Var'  , 0.0434466   ), Coef('Var'  , 0.0221707   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0301766   ), Coef('Var'  , 0.0599546   ), Coef('Var'  , 0.0543303   ), Coef('Var'  , 0.0473938   ), Coef('Var'  , 0.0241537   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.201064    ), Coef('Var'  , 0.152524    ), Coef('Var'  , 0.114668    ), Coef('Var'  , 0.077207    ), Coef('Var'  , 0.0386039   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.375309    ), Coef('Var'  , 0.251666    ), Coef('Var'  , 0.181938    ), Coef('Var'  , 0.113971    ), Coef('Var'  , 0.0566289   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.211964    ), Coef('Var'  , 0.175013    ), Coef('Var'  , 0.173922    ), Coef('Var'  , 0.174982    ), Coef('Var'  , 0.211959    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0534346   ), Coef('Var'  , 0.107685    ), Coef('Var'  , 0.175417    ), Coef('Var'  , 0.245145    ), Coef('Var'  , 0.371983    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0391519   ), Coef('Var'  , 0.0783635   ), Coef('Var'  , 0.115604    ), Coef('Var'  , 0.153388    ), Coef('Var'  , 0.201452    ), Coef('Const', 0.25        ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0245561   ), Coef('Var'  , 0.0483184   ), Coef('Var'  , 0.0549424   ), Coef('Var'  , 0.0605355   ), Coef('Var'  , 0.0303863   ), Coef('Const', 0           ), Coef('Const', 0           ), ], ])
	etat3.initMat[Chem([Sub('G')])] = FMat([
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
	etat3.initMat[Chem([Sub('10')])] = FMat([
		[Coef('Const', 0           ), Coef('Var'  , 0.0363763   ), Coef('Var'  , 0.0729064   ), Coef('Var'  , 0.109981    ), Coef('Var'  , 0.147816    ), Coef('Var'  , 0.198605    ), Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0229916   ), Coef('Var'  , 0.0453175   ), Coef('Var'  , 0.0528181   ), Coef('Var'  , 0.0593154   ), Coef('Var'  , 0.0298265   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0225511   ), Coef('Var'  , 0.0441123   ), Coef('Var'  , 0.0483688   ), Coef('Var'  , 0.0508484   ), Coef('Var'  , 0.0258177   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0220636   ), Coef('Var'  , 0.0428848   ), Coef('Var'  , 0.0439172   ), Coef('Var'  , 0.0425172   ), Coef('Var'  , 0.0218536   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0241521   ), Coef('Var'  , 0.0477749   ), Coef('Var'  , 0.0448257   ), Coef('Var'  , 0.0406495   ), Coef('Var'  , 0.0206736   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0306046   ), Coef('Var'  , 0.0610174   ), Coef('Var'  , 0.0548463   ), Coef('Var'  , 0.0478556   ), Coef('Var'  , 0.0242417   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.25        ), Coef('Var'  , 0.199223    ), Coef('Var'  , 0.149015    ), Coef('Var'  , 0.111232    ), Coef('Var'  , 0.0741578   ), Coef('Var'  , 0.0370088   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.5         ), Coef('Var'  , 0.372079    ), Coef('Var'  , 0.245343    ), Coef('Var'  , 0.175802    ), Coef('Var'  , 0.108231    ), Coef('Var'  , 0.0537236   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0.25        ), Coef('Var'  , 0.214385    ), Coef('Var'  , 0.179674    ), Coef('Var'  , 0.178735    ), Coef('Var'  , 0.179614    ), Coef('Var'  , 0.21435     ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0555738   ), Coef('Var'  , 0.111954    ), Coef('Var'  , 0.179473    ), Coef('Var'  , 0.248995    ), Coef('Var'  , 0.373899    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), ], ])
	etat3.initMat[Chem([Sub('9')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0214747   ), Coef('Var'  , 0.0426548   ), Coef('Var'  , 0.04007     ), Coef('Var'  , 0.036602    ), Coef('Var'  , 0.0185954   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0289105   ), Coef('Var'  , 0.0576637   ), Coef('Var'  , 0.0511972   ), Coef('Var'  , 0.0440301   ), Coef('Var'  , 0.0222867   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.201373    ), Coef('Var'  , 0.153147    ), Coef('Var'  , 0.115421    ), Coef('Var'  , 0.0780696   ), Coef('Var'  , 0.0390478   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.373153    ), Coef('Var'  , 0.2475      ), Coef('Var'  , 0.178314    ), Coef('Var'  , 0.111037    ), Coef('Var'  , 0.0551612   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.213462    ), Coef('Var'  , 0.177883    ), Coef('Var'  , 0.1772      ), Coef('Var'  , 0.178382    ), Coef('Var'  , 0.213738    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0577462   ), Coef('Var'  , 0.115965    ), Coef('Var'  , 0.18366     ), Coef('Var'  , 0.252738    ), Coef('Var'  , 0.375914    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0373717   ), Coef('Var'  , 0.0748245   ), Coef('Var'  , 0.111729    ), Coef('Var'  , 0.149309    ), Coef('Var'  , 0.199358    ), Coef('Const', 0.25        ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0207793   ), Coef('Var'  , 0.0411385   ), Coef('Var'  , 0.0480452   ), Coef('Var'  , 0.0545148   ), Coef('Var'  , 0.0272658   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0223562   ), Coef('Var'  , 0.0438089   ), Coef('Var'  , 0.0477915   ), Coef('Var'  , 0.0502219   ), Coef('Var'  , 0.0254353   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0233724   ), Coef('Var'  , 0.0454151   ), Coef('Var'  , 0.0465713   ), Coef('Var'  , 0.0450956   ), Coef('Var'  , 0.0231989   ), Coef('Const', 0           ), Coef('Const', 0           ), ], ])
	
	
	
	etat4.bords   = {Bord('3'): etat10, Bord('2'): etat10, Bord('1'): etat10, Bord('0'): etat10, }
	etat4.permuts = {}
	etat4.interns = {Intern('_'): etat4, }
	etat4.subs    = {Sub('3'): etat1, Sub('2'): etat1, Sub('1'): etat1, Sub('0'): etat1, Sub('G', True): Etat.etatPoint, }
	
	etat4.buildIntern()
	
	
	etat4.eqs = [
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
	
	
	etat4.prim.elems = [Figure(2, [Chem([Bord('0'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('0'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('0'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('0'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('1'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('1'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('1'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('1'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('2'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('2'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('2'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('2'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('3'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('3'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('3'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('3'), Sub('1'), Sub('1'), Bord('0'), ]), ])]
	etat4.grid.elems = [
		Figure(1, [Chem([Bord('0'), Bord('0'), ]), Chem([Bord('0'), Intern(''), ]), Chem([Bord('0'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('1'), Bord('0'), ]), Chem([Bord('1'), Intern(''), ]), Chem([Bord('1'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('2'), Bord('0'), ]), Chem([Bord('2'), Intern(''), ]), Chem([Bord('2'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('3'), Bord('0'), ]), Chem([Bord('3'), Intern(''), ]), Chem([Bord('3'), Bord('1'), ]), ]), ]
	
	
	etat4.space = [Chem([Bord('3'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('2'), Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('2'), Intern('0'), Intern('0'), ]), Chem([Bord('3'), Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('3'), Intern('0'), Intern('0'), ]), ]
	
	etat4.initMat[Chem([Sub('3')])] = FMat([
		[Coef('Const', 0.25        ), Coef('Var'  , 0.123679    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.5         ), Coef('Var'  , 0.148853    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0.25        ), Coef('Var'  , 0.174027    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.147523    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.12102     ), Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.101147    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0812741   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.102477    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], ])
	etat4.initMat[Chem([Sub('2')])] = FMat([
		[Coef('Const', 0           ), Coef('Var'  , 0.0812852   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0981859   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.25        ), Coef('Var'  , 0.115087    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.5         ), Coef('Var'  , 0.14488     ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0.25        ), Coef('Var'  , 0.174673    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.151814    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.128955    ), Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.10512     ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], ])
	etat4.initMat[Chem([Sub('1')])] = FMat([
		[Coef('Const', 0           ), Coef('Var'  , 0.135113    ), Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.102264    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0694143   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0946768   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.25        ), Coef('Var'  , 0.119939    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.5         ), Coef('Var'  , 0.147736    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0.25        ), Coef('Var'  , 0.175533    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.155323    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), ], ])
	etat4.initMat[Chem([Sub('0')])] = FMat([
		[Coef('Const', 0.25        ), Coef('Var'  , 0.185898    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.156423    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.126948    ), Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0920333   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.057119    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0935771   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.25        ), Coef('Var'  , 0.130035    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.5         ), Coef('Var'  , 0.157967    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), ], ])
	etat4.initMat[Chem([Sub('G')])] = FMat([
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], ])
	
	
	
	etat5.bords   = {Bord('4'): etat10, Bord('3'): etat10, Bord('2'): etat10, Bord('1'): etat10, Bord('0'): etat10, }
	etat5.permuts = {}
	etat5.interns = {Intern('_'): etat5, }
	etat5.subs    = {Sub('4'): etat8, Sub('3'): etat8, Sub('2'): etat8, Sub('1'): etat8, Sub('0'): etat8, Sub('G', True): Etat.etatPoint, }
	
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
	
	
	etat5.space = [Chem([Bord('4'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('2'), Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('2'), Intern('0'), Intern('0'), ]), Chem([Bord('3'), Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('3'), Intern('0'), Intern('0'), ]), Chem([Bord('4'), Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('4'), Intern('0'), Intern('0'), ]), ]
	
	etat5.initMat[Chem([Sub('4')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.118636    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.140222    ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.161809    ), ], 
		[Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.134886    ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.107963    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.076723    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0454829   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0557961   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0661093   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0923725   ), ], ])
	etat5.initMat[Chem([Sub('3')])] = FMat([
		[Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.182175    ), ], 
		[Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.138668    ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0951606   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0781521   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0611436   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0528366   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0445296   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0807602   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.116991    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.149583    ), ], ])
	etat5.initMat[Chem([Sub('2')])] = FMat([
		[Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.143159    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.110293    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0774272   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0758389   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0742506   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0792356   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.0842205   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.102581    ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.120943    ), ], 
		[Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.132051    ), ], ])
	etat5.initMat[Chem([Sub('1')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0611964   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.060431    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0596656   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0833242   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.106983    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.130795    ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.154606    ), ], 
		[Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.136078    ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.117549    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0893724   ), ], ])
	etat5.initMat[Chem([Sub('0')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.041423    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0824246   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.123426    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.128226    ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.133025    ), ], 
		[Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.129624    ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.126223    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.101063    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0759026   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0586628   ), ], ])
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
	
	
	
	etat6.bords   = {Bord('2'): etat10, Bord('1'): etat10, Bord('0'): etat10, }
	etat6.permuts = {}
	etat6.interns = {Intern('_'): etat6, }
	etat6.subs    = {Sub('2'): etat6, Sub('1'): etat6, Sub('0'): etat6, Sub('G', True): Etat.etatPoint, }
	
	etat6.buildIntern()
	
	
	etat6.eqs = [
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
	
	
	etat6.prim.elems = [Figure(2, [Chem([Bord('0'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('0'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('0'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('0'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('1'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('1'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('1'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('1'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('2'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('2'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('2'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('2'), Sub('1'), Sub('1'), Bord('0'), ]), ])]
	etat6.grid.elems = [
		Figure(1, [Chem([Bord('0'), Bord('0'), ]), Chem([Bord('0'), Intern(''), ]), Chem([Bord('0'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('1'), Bord('0'), ]), Chem([Bord('1'), Intern(''), ]), Chem([Bord('1'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('2'), Bord('0'), ]), Chem([Bord('2'), Intern(''), ]), Chem([Bord('2'), Bord('1'), ]), ]), ]
	
	
	etat6.space = [Chem([Bord('2'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('2'), Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('2'), Intern('0'), Intern('0'), ]), ]
	
	etat6.initMat[Chem([Sub('2')])] = FMat([
		[Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.25        ), ], 
		[Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.25        ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.125       ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 1.14841e-11 ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.125       ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.25        ), ], ])
	etat6.initMat[Chem([Sub('1')])] = FMat([
		[Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.125       ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 6.38354e-12 ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.125       ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.25        ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.25        ), ], 
		[Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.25        ), ], ])
	etat6.initMat[Chem([Sub('0')])] = FMat([
		[Coef('Const', 0.25        ), Coef('Var'  , 0.125       ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.5         ), Coef('Var'  , 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0.25        ), Coef('Var'  , 0.25        ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.25        ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.125       ), Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 1.02583e-11 ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], ])
	etat6.initMat[Chem([Sub('G')])] = FMat([
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], ])
	
	
	
	etat7.bords   = {Bord('2'): etat12, Bord('1'): etat12, Bord('0'): etat12, }
	etat7.permuts = {}
	etat7.interns = {Intern('_'): etat7, }
	etat7.subs    = {Sub('8'): etat7, Sub('7'): etat7, Sub('6'): etat7, Sub('5'): etat7, Sub('4'): etat7, Sub('3'): etat7, Sub('2'): etat7, Sub('1'): etat7, Sub('0'): etat7, Sub('G', True): Etat.etatPoint, Sub('10'): etat7, Sub('9'): etat7, Sub('11'): etat7, Sub('12'): etat7, Sub('13'): etat7, Sub('14'): etat7, Sub('15'): etat7, Sub('16'): etat7, Sub('17'): etat7, Sub('18'): etat7, }
	
	etat7.buildIntern()
	
	
	etat7.eqs = [
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
	
	
	etat7.prim.elems = [Figure(2, [Chem([Bord('0'), Sub('0'), Bord('0'), ]), Chem([Bord('0'), Sub('1'), Bord('0'), ]), Chem([Bord('0'), Sub('2'), Bord('0'), ]), Chem([Bord('0'), Sub('3'), Bord('0'), ]), Chem([Bord('1'), Sub('0'), Bord('0'), ]), Chem([Bord('1'), Sub('1'), Bord('0'), ]), Chem([Bord('1'), Sub('2'), Bord('0'), ]), Chem([Bord('1'), Sub('3'), Bord('0'), ]), Chem([Bord('2'), Sub('0'), Bord('0'), ]), Chem([Bord('2'), Sub('1'), Bord('0'), ]), Chem([Bord('2'), Sub('2'), Bord('0'), ]), Chem([Bord('2'), Sub('3'), Bord('0'), ]), ])]
	etat7.grid.elems = [
		Figure(1, [Chem([Bord('0'), Bord('0'), ]), Chem([Bord('0'), Intern(''), ]), Chem([Bord('0'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('1'), Bord('0'), ]), Chem([Bord('1'), Intern(''), ]), Chem([Bord('1'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('2'), Bord('0'), ]), Chem([Bord('2'), Intern(''), ]), Chem([Bord('2'), Bord('1'), ]), ]), ]
	
	
	etat7.space = [Chem([Bord('2'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('2'), Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('2'), Intern('0'), Intern('0'), ]), ]
	
	etat7.initMat[Chem([Sub('8')])] = FMat([
		[Coef('Const', 0.0625      ), Coef('Var'  , 0.127944    ), Coef('Var'  , 0.158715    ), Coef('Var'  , 0.242092    ), Coef('Const', 0.25        ), Coef('Const', 0.125       ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.061976    ), Coef('Var'  , 0.0551824   ), Coef('Var'  , 0.123806    ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  ,-0.003992    ), Coef('Var'  , 0.0660969   ), Coef('Var'  , 0.00552     ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.186028    ), Coef('Var'  , 0.079421    ), Coef('Var'  , 0.128954    ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.5625      ), Coef('Var'  , 0.376048    ), Coef('Var'  , 0.323561    ), Coef('Var'  , 0.252388    ), Coef('Const', 0.25        ), Coef('Const', 0.375       ), ], 
		[Coef('Const', 0.375       ), Coef('Var'  , 0.251996    ), Coef('Var'  , 0.317024    ), Coef('Var'  , 0.24724     ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), ], ])
	etat7.initMat[Chem([Sub('7')])] = FMat([
		[Coef('Const', 0.0625      ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.052152    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.063652    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.0625      ), Coef('Var'  , 0.075152    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Const', 0.375       ), Coef('Var'  , 0.223924    ), ], 
		[Coef('Const', 0.5625      ), Coef('Const', 0.75        ), Coef('Const', 1           ), Coef('Const', 0.75        ), Coef('Const', 0.5625      ), Coef('Var'  , 0.372696    ), ], 
		[Coef('Const', 0.375       ), Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.212424    ), ], ])
	etat7.initMat[Chem([Sub('6')])] = FMat([
		[Coef('Var'  , 0.161281    ), Coef('Var'  , 0.165688    ), Coef('Var'  , 0.193779    ), Coef('Var'  , 0.198552    ), Coef('Var'  , 0.194252    ), Coef('Var'  , 0.164408    ), ], 
		[Coef('Var'  , 0.153213    ), Coef('Var'  , 0.186576    ), Coef('Var'  , 0.195129    ), Coef('Var'  , 0.18124     ), Coef('Var'  , 0.154421    ), Coef('Var'  , 0.151792    ), ], 
		[Coef('Var'  , 0.192431    ), Coef('Var'  , 0.207464    ), Coef('Var'  , 0.193302    ), Coef('Var'  , 0.163928    ), Coef('Var'  , 0.160028    ), Coef('Var'  , 0.139176    ), ], 
		[Coef('Var'  , 0.182027    ), Coef('Var'  , 0.167156    ), Coef('Var'  , 0.140836    ), Coef('Var'  , 0.150724    ), Coef('Var'  , 0.142597    ), Coef('Var'  , 0.167796    ), ], 
		[Coef('Var'  , 0.174688    ), Coef('Var'  , 0.126848    ), Coef('Var'  , 0.140931    ), Coef('Var'  , 0.13752     ), Coef('Var'  , 0.173554    ), Coef('Var'  , 0.196416    ), ], 
		[Coef('Var'  , 0.13636     ), Coef('Var'  , 0.146268    ), Coef('Var'  , 0.136022    ), Coef('Var'  , 0.168036    ), Coef('Var'  , 0.175148    ), Coef('Var'  , 0.180412    ), ], ])
	etat7.initMat[Chem([Sub('5')])] = FMat([
		[Coef('Var'  , 0.331456    ), Coef('Var'  , 0.321908    ), Coef('Var'  , 0.284772    ), Coef('Var'  , 0.242092    ), Coef('Var'  , 0.249772    ), Coef('Var'  , 0.283064    ), ], 
		[Coef('Var'  , 0.326837    ), Coef('Var'  , 0.21603     ), Coef('Var'  , 0.202158    ), Coef('Var'  , 0.202158    ), Coef('Var'  , 0.231182    ), Coef('Var'  , 0.265328    ), ], 
		[Coef('Var'  , 0.157631    ), Coef('Var'  , 0.110152    ), Coef('Var'  , 0.119544    ), Coef('Var'  , 0.162224    ), Coef('Var'  , 0.212592    ), Coef('Var'  , 0.247592    ), ], 
		[Coef('Var'  , 0.0506266   ), Coef('Var'  , 0.089046    ), Coef('Var'  , 0.107614    ), Coef('Var'  , 0.128954    ), Coef('Var'  , 0.125114    ), Coef('Var'  , 0.108468    ), ], 
		[Coef('Var'  , 0.0571514   ), Coef('Var'  , 0.06794     ), Coef('Var'  , 0.095684    ), Coef('Var'  , 0.095684    ), Coef('Var'  , 0.037636    ), Coef('Var'  ,-0.030656    ), ], 
		[Coef('Var'  , 0.0762976   ), Coef('Var'  , 0.194924    ), Coef('Var'  , 0.190228    ), Coef('Var'  , 0.168888    ), Coef('Var'  , 0.143704    ), Coef('Var'  , 0.126204    ), ], ])
	etat7.initMat[Chem([Sub('4')])] = FMat([
		[Coef('Var'  , 0.136163    ), Coef('Var'  , 0.153308    ), Coef('Var'  , 0.182926    ), Coef('Var'  , 0.20404     ), Coef('Var'  , 0.158715    ), Coef('Var'  , 0.116848    ), ], 
		[Coef('Var'  , 0.09062     ), Coef('Var'  , 0.155206    ), Coef('Var'  , 0.115431    ), Coef('Var'  , 0.125388    ), Coef('Var'  , 0.0551824   ), Coef('Var'  , 0.075452    ), ], 
		[Coef('Var'  , 0.13317     ), Coef('Var'  , 0.157104    ), Coef('Var'  , 0.123988    ), Coef('Var'  , 0.046736    ), Coef('Var'  , 0.0660969   ), Coef('Var'  , 0.034056    ), ], 
		[Coef('Var'  , 0.187212    ), Coef('Var'  , 0.173346    ), Coef('Var'  , 0.130925    ), Coef('Var'  , 0.14798     ), Coef('Var'  , 0.079421    ), Coef('Var'  , 0.191576    ), ], 
		[Coef('Var'  , 0.269862    ), Coef('Var'  , 0.189588    ), Coef('Var'  , 0.227488    ), Coef('Var'  , 0.249224    ), Coef('Var'  , 0.323561    ), Coef('Var'  , 0.349096    ), ], 
		[Coef('Var'  , 0.182973    ), Coef('Var'  , 0.171448    ), Coef('Var'  , 0.219242    ), Coef('Var'  , 0.226632    ), Coef('Var'  , 0.317024    ), Coef('Var'  , 0.232972    ), ], ])
	etat7.initMat[Chem([Sub('3')])] = FMat([
		[Coef('Const', 0.5625      ), Coef('Const', 0.375       ), Coef('Const', 0.25        ), Coef('Var'  , 0.283308    ), Coef('Var'  , 0.331728    ), Coef('Var'  , 0.402212    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.128558    ), Coef('Var'  , 0.0857564   ), Coef('Var'  , 0.208622    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  ,-0.026192    ), Coef('Var'  , 0.066479    ), Coef('Var'  , 0.015032    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.108346    ), Coef('Var'  , 0.0518234   ), Coef('Var'  , 0.048894    ), ], 
		[Coef('Const', 0.0625      ), Coef('Const', 0.125       ), Coef('Const', 0.25        ), Coef('Var'  , 0.242884    ), Coef('Var'  , 0.147949    ), Coef('Var'  , 0.082756    ), ], 
		[Coef('Const', 0.375       ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.263096    ), Coef('Var'  , 0.316264    ), Coef('Var'  , 0.242484    ), ], ])
	etat7.initMat[Chem([Sub('2')])] = FMat([
		[Coef('Var'  , 0.125459    ), Coef('Var'  , 0.03282     ), Coef('Var'  , 0.0669931   ), Coef('Var'  , 0.076052    ), Coef('Var'  , 0.118308    ), Coef('Var'  , 0.117456    ), ], 
		[Coef('Var'  , 0.13796     ), Coef('Var'  , 0.125386    ), Coef('Var'  , 0.0830706   ), Coef('Var'  , 0.243346    ), Coef('Var'  , 0.212402    ), Coef('Var'  , 0.183376    ), ], 
		[Coef('Var'  , 0.242549    ), Coef('Var'  , 0.217952    ), Coef('Var'  , 0.331115    ), Coef('Var'  , 0.41064     ), Coef('Var'  , 0.306496    ), Coef('Var'  , 0.249296    ), ], 
		[Coef('Var'  , 0.224533    ), Coef('Var'  , 0.23359     ), Coef('Var'  , 0.319122    ), Coef('Var'  , 0.211974    ), Coef('Var'  , 0.190846    ), Coef('Var'  , 0.191272    ), ], 
		[Coef('Var'  , 0.167003    ), Coef('Var'  , 0.249228    ), Coef('Var'  , 0.150251    ), Coef('Var'  , 0.013308    ), Coef('Var'  , 0.075196    ), Coef('Var'  , 0.133248    ), ], 
		[Coef('Var'  , 0.102496    ), Coef('Var'  , 0.141024    ), Coef('Var'  , 0.0494478   ), Coef('Var'  , 0.04468     ), Coef('Var'  , 0.096752    ), Coef('Var'  , 0.125352    ), ], ])
	etat7.initMat[Chem([Sub('1')])] = FMat([
		[Coef('Const', 0.25        ), Coef('Var'  , 0.237332    ), Coef('Var'  , 0.157881    ), Coef('Var'  , 0.100992    ), Coef('Const', 0.0625      ), Coef('Const', 0.125       ), ], 
		[Coef('Const', 0.5         ), Coef('Var'  , 0.245082    ), Coef('Var'  , 0.324535    ), Coef('Var'  , 0.230816    ), Coef('Const', 0.375       ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0.25        ), Coef('Var'  , 0.252832    ), Coef('Var'  , 0.331648    ), Coef('Var'  , 0.36064     ), Coef('Const', 0.5625      ), Coef('Const', 0.375       ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.131334    ), Coef('Var'  , 0.0775171   ), Coef('Var'  , 0.199504    ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.009836    ), Coef('Var'  , 0.059048    ), Coef('Var'  , 0.038368    ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.123584    ), Coef('Var'  , 0.0493702   ), Coef('Var'  , 0.06968     ), Coef('Const', 0           ), Coef('Const', 0           ), ], ])
	etat7.initMat[Chem([Sub('0')])] = FMat([
		[Coef('Var'  , 0.067707    ), Coef('Var'  ,-0.03218     ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  ,-0.029008    ), ], 
		[Coef('Var'  , 0.0547572   ), Coef('Var'  , 0.031058    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.107156    ), ], 
		[Coef('Var'  , 0.156554    ), Coef('Var'  , 0.094296    ), Coef('Const', 0.0625      ), Coef('Const', 0.125       ), Coef('Const', 0.25        ), Coef('Var'  , 0.24332     ), ], 
		[Coef('Var'  , 0.319836    ), Coef('Var'  , 0.26609     ), Coef('Const', 0.375       ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.264504    ), ], 
		[Coef('Var'  , 0.323996    ), Coef('Var'  , 0.437884    ), Coef('Const', 0.5625      ), Coef('Const', 0.375       ), Coef('Const', 0.25        ), Coef('Var'  , 0.285688    ), ], 
		[Coef('Var'  , 0.0771498   ), Coef('Var'  , 0.202852    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.12834     ), ], ])
	etat7.initMat[Chem([Sub('G')])] = FMat([
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], ])
	etat7.initMat[Chem([Sub('10')])] = FMat([
		[Coef('Var'  , 0.181789    ), Coef('Var'  , 0.225872    ), Coef('Var'  , 0.249772    ), Coef('Var'  , 0.216908    ), Coef('Var'  , 0.193779    ), Coef('Var'  , 0.173372    ), ], 
		[Coef('Var'  , 0.235521    ), Coef('Var'  , 0.241424    ), Coef('Var'  , 0.231182    ), Coef('Var'  , 0.18231     ), Coef('Var'  , 0.195129    ), Coef('Var'  , 0.192126    ), ], 
		[Coef('Var'  , 0.243833    ), Coef('Var'  , 0.256976    ), Coef('Var'  , 0.212592    ), Coef('Var'  , 0.147712    ), Coef('Var'  , 0.193302    ), Coef('Var'  , 0.21088     ), ], 
		[Coef('Var'  , 0.127648    ), Coef('Var'  , 0.137064    ), Coef('Var'  , 0.125114    ), Coef('Var'  , 0.141546    ), Coef('Var'  , 0.140836    ), Coef('Var'  , 0.163314    ), ], 
		[Coef('Var'  , 0.109124    ), Coef('Var'  , 0.017152    ), Coef('Var'  , 0.037636    ), Coef('Var'  , 0.13538     ), Coef('Var'  , 0.140931    ), Coef('Var'  , 0.115748    ), ], 
		[Coef('Var'  , 0.102085    ), Coef('Var'  , 0.121512    ), Coef('Var'  , 0.143704    ), Coef('Var'  , 0.176144    ), Coef('Var'  , 0.136022    ), Coef('Var'  , 0.14456     ), ], ])
	etat7.initMat[Chem([Sub('9')])] = FMat([
		[Coef('Var'  , 0.181789    ), Coef('Var'  , 0.147332    ), Coef('Var'  , 0.118308    ), Coef('Var'  , 0.134104    ), Coef('Var'  , 0.157881    ), Coef('Var'  , 0.194712    ), ], 
		[Coef('Var'  , 0.235521    ), Coef('Var'  , 0.18679     ), Coef('Var'  , 0.212402    ), Coef('Var'  , 0.233104    ), Coef('Var'  , 0.324535    ), Coef('Var'  , 0.236516    ), ], 
		[Coef('Var'  , 0.243833    ), Coef('Var'  , 0.226248    ), Coef('Var'  , 0.306496    ), Coef('Var'  , 0.332104    ), Coef('Var'  , 0.331648    ), Coef('Var'  , 0.27832     ), ], 
		[Coef('Var'  , 0.127648    ), Coef('Var'  , 0.176334    ), Coef('Var'  , 0.190846    ), Coef('Var'  , 0.182948    ), Coef('Var'  , 0.0775171   ), Coef('Var'  , 0.152644    ), ], 
		[Coef('Var'  , 0.109124    ), Coef('Var'  , 0.12642     ), Coef('Var'  , 0.075196    ), Coef('Var'  , 0.033792    ), Coef('Var'  , 0.059048    ), Coef('Var'  , 0.026968    ), ], 
		[Coef('Var'  , 0.102085    ), Coef('Var'  , 0.136876    ), Coef('Var'  , 0.096752    ), Coef('Var'  , 0.083948    ), Coef('Var'  , 0.0493702   ), Coef('Var'  , 0.11084     ), ], ])
	etat7.initMat[Chem([Sub('11')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.0625      ), Coef('Var'  , 0.045748    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Const', 0.375       ), Coef('Var'  , 0.220082    ), ], 
		[Coef('Const', 0.5625      ), Coef('Const', 0.75        ), Coef('Const', 1           ), Coef('Const', 0.75        ), Coef('Const', 0.5625      ), Coef('Var'  , 0.394416    ), ], 
		[Coef('Const', 0.375       ), Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.227126    ), ], 
		[Coef('Const', 0.0625      ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.059836    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.052792    ), ], ])
	etat7.initMat[Chem([Sub('12')])] = FMat([
		[Coef('Const', 0           ), Coef('Var'  ,-0.029008    ), Coef('Var'  , 0.0669931   ), Coef('Var'  ,-0.035348    ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.195936    ), Coef('Var'  , 0.0830706   ), Coef('Var'  , 0.12301     ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.5625      ), Coef('Var'  , 0.42088     ), Coef('Var'  , 0.331115    ), Coef('Var'  , 0.281368    ), Coef('Const', 0.25        ), Coef('Const', 0.375       ), ], 
		[Coef('Const', 0.375       ), Coef('Var'  , 0.264504    ), Coef('Var'  , 0.319122    ), Coef('Var'  , 0.267674    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0.0625      ), Coef('Var'  , 0.108128    ), Coef('Var'  , 0.150251    ), Coef('Var'  , 0.25398     ), Coef('Const', 0.25        ), Coef('Const', 0.125       ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.03956     ), Coef('Var'  , 0.0494478   ), Coef('Var'  , 0.109316    ), Coef('Const', 0           ), Coef('Const', 0           ), ], ])
	etat7.initMat[Chem([Sub('13')])] = FMat([
		[Coef('Var'  , 0.244344    ), Coef('Var'  , 0.243372    ), Coef('Var'  , 0.284772    ), Coef('Var'  , 0.331724    ), Coef('Var'  , 0.331728    ), Coef('Var'  , 0.25636     ), ], 
		[Coef('Var'  , 0.141281    ), Coef('Var'  , 0.19597     ), Coef('Var'  , 0.202158    ), Coef('Var'  , 0.209838    ), Coef('Var'  , 0.0857564   ), Coef('Var'  , 0.146792    ), ], 
		[Coef('Var'  , 0.124319    ), Coef('Var'  , 0.148568    ), Coef('Var'  , 0.119544    ), Coef('Var'  , 0.087952    ), Coef('Var'  , 0.066479    ), Coef('Var'  , 0.037224    ), ], 
		[Coef('Var'  , 0.107346    ), Coef('Var'  , 0.128314    ), Coef('Var'  , 0.107614    ), Coef('Var'  , 0.084138    ), Coef('Var'  , 0.0518234   ), Coef('Var'  , 0.12182     ), ], 
		[Coef('Var'  , 0.164054    ), Coef('Var'  , 0.10806     ), Coef('Var'  , 0.095684    ), Coef('Var'  , 0.080324    ), Coef('Var'  , 0.147949    ), Coef('Var'  , 0.206416    ), ], 
		[Coef('Var'  , 0.218656    ), Coef('Var'  , 0.175716    ), Coef('Var'  , 0.190228    ), Coef('Var'  , 0.206024    ), Coef('Var'  , 0.316264    ), Coef('Var'  , 0.231388    ), ], ])
	etat7.initMat[Chem([Sub('14')])] = FMat([
		[Coef('Var'  , 0.244344    ), Coef('Var'  , 0.221604    ), Coef('Var'  , 0.182926    ), Coef('Var'  , 0.172516    ), Coef('Var'  , 0.194252    ), Coef('Var'  , 0.224592    ), ], 
		[Coef('Var'  , 0.141281    ), Coef('Var'  , 0.13429     ), Coef('Var'  , 0.115431    ), Coef('Var'  , 0.151578    ), Coef('Var'  , 0.154421    ), Coef('Var'  , 0.184016    ), ], 
		[Coef('Var'  , 0.124319    ), Coef('Var'  , 0.046976    ), Coef('Var'  , 0.123988    ), Coef('Var'  , 0.13064     ), Coef('Var'  , 0.160028    ), Coef('Var'  , 0.14344     ), ], 
		[Coef('Var'  , 0.107346    ), Coef('Var'  , 0.139198    ), Coef('Var'  , 0.130925    ), Coef('Var'  , 0.163742    ), Coef('Var'  , 0.142597    ), Coef('Var'  , 0.137704    ), ], 
		[Coef('Var'  , 0.164054    ), Coef('Var'  , 0.23142     ), Coef('Var'  , 0.227488    ), Coef('Var'  , 0.196844    ), Coef('Var'  , 0.173554    ), Coef('Var'  , 0.131968    ), ], 
		[Coef('Var'  , 0.218656    ), Coef('Var'  , 0.226512    ), Coef('Var'  , 0.219242    ), Coef('Var'  , 0.18468     ), Coef('Var'  , 0.175148    ), Coef('Var'  , 0.17828     ), ], ])
	etat7.initMat[Chem([Sub('15')])] = FMat([
		[Coef('Const', 0.5625      ), Coef('Const', 0.75        ), Coef('Const', 1           ), Coef('Const', 0.75        ), Coef('Const', 0.5625      ), Coef('Var'  , 0.445016    ), ], 
		[Coef('Const', 0.375       ), Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.228436    ), ], 
		[Coef('Const', 0.0625      ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.011856    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.027492    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.0625      ), Coef('Var'  , 0.043128    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Const', 0.375       ), Coef('Var'  , 0.244072    ), ], ])
	etat7.initMat[Chem([Sub('16')])] = FMat([
		[Coef('Const', 0.5625      ), Coef('Var'  , 0.395872    ), Coef('Var'  , 0.331456    ), Coef('Var'  , 0.295992    ), Coef('Const', 0.25        ), Coef('Const', 0.375       ), ], 
		[Coef('Const', 0.375       ), Coef('Var'  , 0.230816    ), Coef('Var'  , 0.326837    ), Coef('Var'  , 0.263316    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0.0625      ), Coef('Var'  , 0.06576     ), Coef('Var'  , 0.157631    ), Coef('Var'  , 0.23064     ), Coef('Const', 0.25        ), Coef('Const', 0.125       ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.052064    ), Coef('Var'  , 0.0506266   ), Coef('Var'  , 0.102004    ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.038368    ), Coef('Var'  , 0.0571514   ), Coef('Var'  ,-0.026632    ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.21712     ), Coef('Var'  , 0.0762976   ), Coef('Var'  , 0.13468     ), Coef('Const', 0           ), Coef('Const', 0           ), ], ])
	etat7.initMat[Chem([Sub('17')])] = FMat([
		[Coef('Var'  , 0.126009    ), Coef('Var'  , 0.12386     ), Coef('Var'  , 0.136163    ), Coef('Var'  , 0.069224    ), Coef('Var'  , 0.067707    ), Coef('Var'  , 0.056604    ), ], 
		[Coef('Var'  , 0.113864    ), Coef('Var'  , 0.131946    ), Coef('Var'  , 0.09062     ), Coef('Var'  , 0.059384    ), Coef('Var'  , 0.0547572   ), Coef('Var'  , 0.135694    ), ], 
		[Coef('Var'  , 0.179934    ), Coef('Var'  , 0.140032    ), Coef('Var'  , 0.13317     ), Coef('Var'  , 0.049544    ), Coef('Var'  , 0.156554    ), Coef('Var'  , 0.214784    ), ], 
		[Coef('Var'  , 0.225141    ), Coef('Var'  , 0.18807     ), Coef('Var'  , 0.187212    ), Coef('Var'  , 0.215388    ), Coef('Var'  , 0.319836    ), Coef('Var'  , 0.221698    ), ], 
		[Coef('Var'  , 0.228985    ), Coef('Var'  , 0.236108    ), Coef('Var'  , 0.269862    ), Coef('Var'  , 0.381232    ), Coef('Var'  , 0.323996    ), Coef('Var'  , 0.228612    ), ], 
		[Coef('Var'  , 0.126068    ), Coef('Var'  , 0.179984    ), Coef('Var'  , 0.182973    ), Coef('Var'  , 0.225228    ), Coef('Var'  , 0.0771498   ), Coef('Var'  , 0.142608    ), ], ])
	etat7.initMat[Chem([Sub('18')])] = FMat([
		[Coef('Var'  , 0.126009    ), Coef('Var'  , 0.077332    ), Coef('Var'  , 0.125459    ), Coef('Var'  , 0.136664    ), Coef('Var'  , 0.161281    ), Coef('Var'  , 0.12898     ), ], 
		[Coef('Var'  , 0.113864    ), Coef('Var'  , 0.144962    ), Coef('Var'  , 0.13796     ), Coef('Var'  , 0.189564    ), Coef('Var'  , 0.153213    ), Coef('Var'  , 0.137066    ), ], 
		[Coef('Var'  , 0.179934    ), Coef('Var'  , 0.212592    ), Coef('Var'  , 0.242549    ), Coef('Var'  , 0.242464    ), Coef('Var'  , 0.192431    ), Coef('Var'  , 0.145152    ), ], 
		[Coef('Var'  , 0.225141    ), Coef('Var'  , 0.211334    ), Coef('Var'  , 0.224533    ), Coef('Var'  , 0.181668    ), Coef('Var'  , 0.182027    ), Coef('Var'  , 0.18551     ), ], 
		[Coef('Var'  , 0.228985    ), Coef('Var'  , 0.210076    ), Coef('Var'  , 0.167003    ), Coef('Var'  , 0.120872    ), Coef('Var'  , 0.174688    ), Coef('Var'  , 0.225868    ), ], 
		[Coef('Var'  , 0.126068    ), Coef('Var'  , 0.143704    ), Coef('Var'  , 0.102496    ), Coef('Var'  , 0.128768    ), Coef('Var'  , 0.13636     ), Coef('Var'  , 0.177424    ), ], ])
	
	
	
	etat8.bords   = {Bord('2'): etat12, Bord('1'): etat10, Bord('0'): etat10, }
	etat8.permuts = {}
	etat8.interns = {Intern('_'): etat8, }
	etat8.subs    = {Sub('4'): etat8, Sub('3'): etat8, Sub('2'): etat5, Sub('1'): etat8, Sub('0'): etat8, Sub('G', True): Etat.etatPoint, }
	
	etat8.buildIntern()
	
	
	etat8.eqs = [
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
	
	
	etat8.prim.elems = [Figure(2, [Chem([Bord('0'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('0'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('0'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('0'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('1'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('1'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('1'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('1'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('2'), Sub('0'), Bord('0'), ]), Chem([Bord('2'), Sub('1'), Bord('0'), ]), Chem([Bord('2'), Sub('2'), Bord('0'), ]), Chem([Bord('2'), Sub('3'), Bord('0'), ]), ])]
	etat8.grid.elems = [
		Figure(1, [Chem([Bord('0'), Bord('0'), ]), Chem([Bord('0'), Intern(''), ]), Chem([Bord('0'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('1'), Bord('0'), ]), Chem([Bord('1'), Intern(''), ]), Chem([Bord('1'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('2'), Bord('0'), ]), Chem([Bord('2'), Intern(''), ]), Chem([Bord('2'), Bord('1'), ]), ]), ]
	
	
	etat8.space = [Chem([Bord('2'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('2'), Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('2'), Intern('0'), Intern('0'), ]), ]
	
	etat8.initMat[Chem([Sub('4')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.03125     ), Coef('Const', 0.0625      ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 1.2288e-11  ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.125       ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.40625     ), Coef('Const', 0.5625      ), Coef('Const', 0.75        ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.1875      ), Coef('Const', 0.375       ), Coef('Const', 0.25        ), ], ])
	etat8.initMat[Chem([Sub('3')])] = FMat([
		[Coef('Const', 0.0625      ), Coef('Var'  , 0.108159    ), Coef('Var'  , 0.153913    ), Coef('Var'  , 0.201909    ), Coef('Const', 0.25        ), Coef('Const', 0.125       ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0169129   ), Coef('Var'  , 0.0336901   ), Coef('Var'  , 0.0169129   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0417634   ), Coef('Var'  , 0.0834732   ), Coef('Var'  , 0.0417634   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0669573   ), Coef('Var'  , 0.133756    ), Coef('Var'  , 0.0669573   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.5625      ), Coef('Var'  , 0.43321     ), Coef('Var'  , 0.303988    ), Coef('Var'  , 0.27696     ), Coef('Const', 0.25        ), Coef('Const', 0.375       ), ], 
		[Coef('Const', 0.375       ), Coef('Var'  , 0.332998    ), Coef('Var'  , 0.291181    ), Coef('Var'  , 0.395498    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), ], ])
	etat8.initMat[Chem([Sub('2')])] = FMat([
		[Coef('Var'  , 0.153913    ), Coef('Var'  , 0.0769088   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.276904    ), Coef('Var'  , 0.303907    ), Coef('Var'  , 0.228813    ), ], 
		[Coef('Var'  , 0.0336901   ), Coef('Var'  , 0.0169129   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.316912    ), Coef('Var'  , 0.133689    ), Coef('Var'  , 0.0838251   ), ], 
		[Coef('Var'  , 0.0834732   ), Coef('Var'  , 0.166763    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.166762    ), Coef('Var'  , 0.0834715   ), Coef('Var'  , 0.0835252   ), ], 
		[Coef('Var'  , 0.133756    ), Coef('Var'  , 0.316957    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0169624   ), Coef('Var'  , 0.0337608   ), Coef('Var'  , 0.0839196   ), ], 
		[Coef('Var'  , 0.303988    ), Coef('Var'  , 0.27696     ), Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0769618   ), Coef('Var'  , 0.15399     ), Coef('Var'  , 0.228921    ), ], 
		[Coef('Var'  , 0.291181    ), Coef('Var'  , 0.145498    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.145498    ), Coef('Var'  , 0.291181    ), Coef('Var'  , 0.290996    ), ], ])
	etat8.initMat[Chem([Sub('1')])] = FMat([
		[Coef('Const', 0.25        ), Coef('Var'  , 0.276904    ), Coef('Var'  , 0.303907    ), Coef('Var'  , 0.433154    ), Coef('Const', 0.5625      ), Coef('Const', 0.375       ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0669123   ), Coef('Var'  , 0.133689    ), Coef('Var'  , 0.0669123   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0417617   ), Coef('Var'  , 0.0834715   ), Coef('Var'  , 0.0417617   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0169624   ), Coef('Var'  , 0.0337608   ), Coef('Var'  , 0.0169624   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.25        ), Coef('Var'  , 0.201962    ), Coef('Var'  , 0.15399     ), Coef('Var'  , 0.108212    ), Coef('Const', 0.0625      ), Coef('Const', 0.125       ), ], 
		[Coef('Const', 0.5         ), Coef('Var'  , 0.395498    ), Coef('Var'  , 0.291181    ), Coef('Var'  , 0.332998    ), Coef('Const', 0.375       ), Coef('Const', 0.5         ), ], ])
	etat8.initMat[Chem([Sub('0')])] = FMat([
		[Coef('Const', 0.5625      ), Coef('Var'  , 0.40625     ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.75        ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.25        ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.125       ), Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 6.0804e-12  ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.0625      ), Coef('Var'  , 0.03125     ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.375       ), Coef('Var'  , 0.1875      ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), ], ])
	etat8.initMat[Chem([Sub('G')])] = FMat([
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], ])
	
	
	
	etat9.bords   = {Bord('3'): etat10, Bord('2'): etat10, Bord('1'): etat10, Bord('0'): etat10, }
	etat9.permuts = {}
	etat9.interns = {Intern('_'): etat9, }
	etat9.subs    = {Sub('4'): etat9, Sub('3'): etat9, Sub('2'): etat9, Sub('1'): etat9, Sub('0'): etat9, Sub('G', True): Etat.etatPoint, }
	
	etat9.buildIntern()
	
	
	etat9.eqs = [
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
	
	
	etat9.prim.elems = [Figure(2, [Chem([Bord('0'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('0'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('0'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('0'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('1'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('1'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('1'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('1'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('2'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('2'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('2'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('2'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('3'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('3'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('3'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('3'), Sub('1'), Sub('1'), Bord('0'), ]), ])]
	etat9.grid.elems = [
		Figure(1, [Chem([Bord('0'), Bord('0'), ]), Chem([Bord('0'), Intern(''), ]), Chem([Bord('0'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('1'), Bord('0'), ]), Chem([Bord('1'), Intern(''), ]), Chem([Bord('1'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('2'), Bord('0'), ]), Chem([Bord('2'), Intern(''), ]), Chem([Bord('2'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('3'), Bord('0'), ]), Chem([Bord('3'), Intern(''), ]), Chem([Bord('3'), Bord('1'), ]), ]), ]
	
	
	etat9.space = [Chem([Bord('3'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('2'), Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('2'), Intern('0'), Intern('0'), ]), Chem([Bord('3'), Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('3'), Intern('0'), Intern('0'), ]), ]
	
	etat9.initMat[Chem([Sub('4')])] = FMat([
		[Coef('Var'  , 0.124558    ), Coef('Var'  , 0.093234    ), Coef('Var'  , 0.0620845   ), Coef('Var'  , 0.0932353   ), Coef('Var'  , 0.12456     ), Coef('Var'  , 0.155694    ), Coef('Var'  , 0.187033    ), Coef('Var'  , 0.155693    ), ], 
		[Coef('Var'  , 0.0636747   ), Coef('Var'  , 0.06394     ), Coef('Var'  , 0.063674    ), Coef('Var'  , 0.126388    ), Coef('Var'  , 0.18861     ), Coef('Var'  , 0.188836    ), Coef('Var'  , 0.188611    ), Coef('Var'  , 0.126389    ), ], 
		[Coef('Var'  , 0.0618668   ), Coef('Var'  , 0.0929735   ), Coef('Var'  , 0.124342    ), Coef('Var'  , 0.155422    ), Coef('Var'  , 0.186803    ), Coef('Var'  , 0.15541     ), Coef('Var'  , 0.124327    ), Coef('Var'  , 0.0929615   ), ], 
		[Coef('Var'  , 0.06343     ), Coef('Var'  , 0.126084    ), Coef('Var'  , 0.188356    ), Coef('Var'  , 0.188532    ), Coef('Var'  , 0.188366    ), Coef('Var'  , 0.126099    ), Coef('Var'  , 0.0634396   ), Coef('Var'  , 0.0636508   ), ], 
		[Coef('Var'  , 0.124896    ), Coef('Var'  , 0.156113    ), Coef('Var'  , 0.187388    ), Coef('Var'  , 0.156132    ), Coef('Var'  , 0.124919    ), Coef('Var'  , 0.0936627   ), Coef('Var'  , 0.0624268   ), Coef('Var'  , 0.0936437   ), ], 
		[Coef('Var'  , 0.187052    ), Coef('Var'  , 0.186943    ), Coef('Var'  , 0.187049    ), Coef('Var'  , 0.124482    ), Coef('Var'  , 0.0621      ), Coef('Var'  , 0.0620259   ), Coef('Var'  , 0.0621028   ), Coef('Var'  , 0.124487    ), ], 
		[Coef('Var'  , 0.187395    ), Coef('Var'  , 0.156125    ), Coef('Var'  , 0.12491     ), Coef('Var'  , 0.0936635   ), Coef('Var'  , 0.0624433   ), Coef('Var'  , 0.093679    ), Coef('Var'  , 0.124929    ), Coef('Var'  , 0.15614     ), ], 
		[Coef('Var'  , 0.187128    ), Coef('Var'  , 0.124589    ), Coef('Var'  , 0.0621961   ), Coef('Var'  , 0.0621463   ), Coef('Var'  , 0.0621992   ), Coef('Var'  , 0.124593    ), Coef('Var'  , 0.187131    ), Coef('Var'  , 0.187036    ), ], ])
	etat9.initMat[Chem([Sub('3')])] = FMat([
		[Coef('Var'  , 0.12456     ), Coef('Var'  , 0.0622326   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.187233    ), ], 
		[Coef('Var'  , 0.18861     ), Coef('Var'  , 0.0944179   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.344418    ), ], 
		[Coef('Var'  , 0.186803    ), Coef('Var'  , 0.21832     ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.21832     ), ], 
		[Coef('Var'  , 0.188366    ), Coef('Var'  , 0.34427     ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0942698   ), ], 
		[Coef('Var'  , 0.124919    ), Coef('Var'  , 0.187453    ), Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0624533   ), ], 
		[Coef('Var'  , 0.0621      ), Coef('Var'  , 0.0310118   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0310118   ), ], 
		[Coef('Var'  , 0.0624433   ), Coef('Var'  , 0.0312204   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0312204   ), ], 
		[Coef('Var'  , 0.0621992   ), Coef('Var'  , 0.0310744   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0310744   ), ], ])
	etat9.initMat[Chem([Sub('2')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0622314   ), Coef('Var'  , 0.124558    ), Coef('Var'  , 0.187231    ), Coef('Const', 0.25        ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0319703   ), Coef('Var'  , 0.0636747   ), Coef('Var'  , 0.0319703   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0308717   ), Coef('Var'  , 0.0618668   ), Coef('Var'  , 0.0308717   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0318215   ), Coef('Var'  , 0.06343     ), Coef('Var'  , 0.0318215   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.187434    ), Coef('Var'  , 0.124896    ), Coef('Var'  , 0.0624343   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.343473    ), Coef('Var'  , 0.187052    ), Coef('Var'  , 0.0934728   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.218681    ), Coef('Var'  , 0.187395    ), Coef('Var'  , 0.218681    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0935166   ), Coef('Var'  , 0.187128    ), Coef('Var'  , 0.343517    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), ], ])
	etat9.initMat[Chem([Sub('1')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0310026   ), Coef('Var'  , 0.0620845   ), Coef('Var'  , 0.0310026   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0319697   ), Coef('Var'  , 0.063674    ), Coef('Var'  , 0.0319697   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.187102    ), Coef('Var'  , 0.124342    ), Coef('Var'  , 0.0621018   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.344262    ), Coef('Var'  , 0.188356    ), Coef('Var'  , 0.0942621   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.218678    ), Coef('Var'  , 0.187388    ), Coef('Var'  , 0.218678    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0934705   ), Coef('Var'  , 0.187049    ), Coef('Var'  , 0.34347     ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0624431   ), Coef('Var'  , 0.12491     ), Coef('Var'  , 0.187443    ), Coef('Const', 0.25        ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.031072    ), Coef('Var'  , 0.0621961   ), Coef('Var'  , 0.031072    ), Coef('Const', 0           ), Coef('Const', 0           ), ], ])
	etat9.initMat[Chem([Sub('0')])] = FMat([
		[Coef('Const', 0.25        ), Coef('Var'  , 0.218461    ), Coef('Var'  , 0.187033    ), Coef('Var'  , 0.218461    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0944184   ), Coef('Var'  , 0.188611    ), Coef('Var'  , 0.344418    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0620898   ), Coef('Var'  , 0.124327    ), Coef('Var'  , 0.18709     ), Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0318293   ), Coef('Var'  , 0.0634396   ), Coef('Var'  , 0.0318293   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0312094   ), Coef('Var'  , 0.0624268   ), Coef('Var'  , 0.0312094   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0310141   ), Coef('Var'  , 0.0621028   ), Coef('Var'  , 0.0310141   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.25        ), Coef('Var'  , 0.187459    ), Coef('Var'  , 0.124929    ), Coef('Var'  , 0.0624586   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.5         ), Coef('Var'  , 0.343519    ), Coef('Var'  , 0.187131    ), Coef('Var'  , 0.0935191   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), ], ])
	etat9.initMat[Chem([Sub('G')])] = FMat([
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], ])
	
	
	
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
	etat11.subs    = {Sub('2'): etat11, Sub('1'): etat11, Sub('0'): etat11, Sub('G', True): Etat.etatPoint, }
	
	etat11.buildIntern()
	etat11.fm_[Permut('0')] = PMat(3, [2, 1, 0, ])
	
	
	etat11.eqs = [
		(Chem([Permut('0'), Bord('0'), ])	,	Chem([Bord('1')])),
		(Chem([Permut('0'), Bord('1'), ])	,	Chem([Bord('0')])),
		(Chem([Permut('0'), Intern(''), ])	,	Chem([Intern('')])),
		(Chem([Permut('0'), Sub('0'), ])	,	Chem([Sub('2'), Permut('0'), ])),
		(Chem([Permut('0'), Sub('1'), ])	,	Chem([Sub('1'), Permut('0'), ])),
		(Chem([Permut('0'), Sub('2'), ])	,	Chem([Sub('0'), Permut('0'), ])),
		]
	
	
	etat11.prim.elems = [Figure(1, [Chem([Bord('0')]), Chem([Bord('1')]), ])]
	etat11.grid.elems = [Figure(1, [Chem([Bord('0')]), Chem([Intern('')]), Chem([Bord('1')]), ])]
	
	
	etat11.space = [Chem([Bord('0'), Intern('0'), Intern('0'), ]), Chem([Intern('0'), Intern('0'), ]), Chem([Bord('1'), Intern('0'), Intern('0'), ]), ]
	
	etat11.initMat[Chem([Sub('2')])] = FMat([
		[Coef('Const', 0.1111      ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.4444      ), Coef('Const', 0.3333      ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.4444      ), Coef('Const', 0.6667      ), Coef('Const', 1           ), ], ])
	etat11.initMat[Chem([Sub('1')])] = FMat([
		[Coef('Const', 0.4444      ), Coef('Const', 0.2222      ), Coef('Const', 0.1111      ), ], 
		[Coef('Const', 0.4444      ), Coef('Const', 0.5556      ), Coef('Const', 0.4444      ), ], 
		[Coef('Const', 0.1111      ), Coef('Const', 0.2222      ), Coef('Const', 0.4444      ), ], ])
	etat11.initMat[Chem([Sub('0')])] = FMat([
		[Coef('Const', 1           ), Coef('Const', 0.6667      ), Coef('Const', 0.4444      ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.3333      ), Coef('Const', 0.4444      ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.1111      ), ], ])
	etat11.initMat[Chem([Sub('G')])] = FMat([
		[Coef('Const', 0           )], 
		[Coef('Const', 1           )], 
		[Coef('Const', 0           )], ])
	
	
	
	etat12.bords   = {Bord('1'): etat13, Bord('0'): etat13, }
	etat12.permuts = {Permut('0'): etat12, }
	etat12.interns = {Intern('_'): etat12, }
	etat12.subs    = {Sub('3'): etat12, Sub('2'): etat12, Sub('1'): etat12, Sub('0'): etat12, Sub('G', True): Etat.etatPoint, }
	
	etat12.buildIntern()
	etat12.fm_[Permut('0')] = PMat(3, [2, 1, 0, ])
	
	
	etat12.eqs = [
		(Chem([Permut('0'), Bord('0'), ])	,	Chem([Bord('1')])),
		(Chem([Permut('0'), Bord('1'), ])	,	Chem([Bord('0')])),
		(Chem([Permut('0'), Intern(''), ])	,	Chem([Intern('')])),
		(Chem([Permut('0'), Sub('0'), ])	,	Chem([Sub('3'), Permut('0'), ])),
		(Chem([Permut('0'), Sub('1'), ])	,	Chem([Sub('2'), Permut('0'), ])),
		(Chem([Permut('0'), Sub('2'), ])	,	Chem([Sub('1'), Permut('0'), ])),
		(Chem([Permut('0'), Sub('3'), ])	,	Chem([Sub('0'), Permut('0'), ])),
		]
	
	
	etat12.prim.elems = [Figure(1, [Chem([Bord('0')]), Chem([Bord('1')]), ])]
	etat12.grid.elems = [Figure(1, [Chem([Bord('0')]), Chem([Intern('')]), Chem([Bord('1')]), ])]
	
	
	etat12.space = [Chem([Bord('0'), Intern('0'), Intern('0'), ]), Chem([Intern('0'), Intern('0'), ]), Chem([Bord('1'), Intern('0'), Intern('0'), ]), ]
	
	etat12.initMat[Chem([Sub('3')])] = FMat([
		[Coef('Const', 0.0625      ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.375       ), Coef('Const', 0.25        ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.5625      ), Coef('Const', 0.75        ), Coef('Const', 1           ), ], ])
	etat12.initMat[Chem([Sub('2')])] = FMat([
		[Coef('Const', 0.25        ), Coef('Const', 0.125       ), Coef('Const', 0.0625      ), ], 
		[Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0.375       ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0.375       ), Coef('Const', 0.5625      ), ], ])
	etat12.initMat[Chem([Sub('1')])] = FMat([
		[Coef('Const', 0.5625      ), Coef('Const', 0.375       ), Coef('Const', 0.25        ), ], 
		[Coef('Const', 0.375       ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0.0625      ), Coef('Const', 0.125       ), Coef('Const', 0.25        ), ], ])
	etat12.initMat[Chem([Sub('0')])] = FMat([
		[Coef('Const', 1           ), Coef('Const', 0.75        ), Coef('Const', 0.5625      ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Const', 0.375       ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.0625      ), ], ])
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
