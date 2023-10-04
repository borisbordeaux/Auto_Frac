# -*- coding: utf-8 -*-

# Automatically generated, from file : LinkStruct_EG.py, function : modele()

from __future__ import division
import sys
if './../../../../python' not in sys.path:
	sys.path.append('./../../../../python')
from etat import *

def modele():
	
	etat0 = EtatInit()
	etat1 = Etat('g2temp',0)
	etat2 = Etat('m',0)
	etat3 = Etat('g2',0)
	etat4 = Etat('c2temp',0)
	etat5 = Etat('c1temp',1)
	etat6 = Etat('c1',1)
	etat7 = Etat('c2',0)
	etat8 = Etat('s',1)
	
	
	#etat0.subs   = {Sub('init_0'): etat1, Sub('init_1'): etat2, Sub('init_2'): etat3, }
	etat0.subs   = {Sub('init_2'): etat3}
	
	#etat0.eqs = [
	#	(Chem([Sub('init_0'), Bord('g2temp_0'), ])	,	Chem([Sub('init_1'), Bord('m_6'), ])),
	#	(Chem([Sub('init_2'), Bord('g2_0'), ])	,	Chem([Sub('init_1'), Bord('m_2'), ])),
	#	]
	
	
	etat0.space = []
	
	#etat0.initMat[Chem([Sub('init_0')])] = FMat([
	#	[Coef('Const',-1.00397     ), Coef('Const',-1.00397     ), Coef('Const',-1.52        ), Coef('Const',-1.87        ), Coef('Const',-2.73603     ), Coef('Const',-2.57        ), Coef('Const',-2.73603     ), Coef('Const',-1.87        ), Coef('Const',-1.52        ), ], 
	#	[Coef('Const', 0.5         ), Coef('Const',-0.5         ), Coef('Const',-0.606218    ), Coef('Const',-1           ), Coef('Const',-0.5         ), Coef('Const',-1.28588e-16 ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.606218    ), ], 
	#	[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
	#	[Coef('Const', 1           ), Coef('Const', 1           ), Coef('Const', 1           ), Coef('Const', 1           ), Coef('Const', 1           ), Coef('Const', 1           ), Coef('Const', 1           ), Coef('Const', 1           ), Coef('Const', 1           ), ], ])
	#etat0.initMat[Chem([Sub('init_1')])] = FMat([
	#	[Coef('Const',-0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.362394    ), Coef('Const', 1.00397     ), Coef('Const', 1.00397     ), Coef('Var'  , 0.376165    ), Coef('Const', 0.5         ), Coef('Const',-0.5         ), Coef('Var'  ,-0.395021    ), Coef('Const',-1.00397     ), Coef('Const',-1.00397     ), Coef('Var'  ,-0.411547    ), ], 
	#	[Coef('Const',-1           ), Coef('Const',-1           ), Coef('Var'  ,-0.374364    ), Coef('Const',-0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.36928     ), Coef('Const', 1           ), Coef('Const', 1           ), Coef('Var'  , 0.374788    ), Coef('Const', 0.5         ), Coef('Const',-0.5         ), Coef('Var'  ,-0.385381    ), ], 
	#	[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0           ), ], 
	#	[Coef('Const', 1           ), Coef('Const', 1           ), Coef('Var'  , 1           ), Coef('Const', 1           ), Coef('Const', 1           ), Coef('Var'  , 1           ), Coef('Const', 1           ), Coef('Const', 1           ), Coef('Var'  , 1           ), Coef('Const', 1           ), Coef('Const', 1           ), Coef('Var'  , 1           ), ], ])
	etat0.initMat[Chem([Sub('init_2')])] = FMat([
		[Coef('Const', 1.00397     ), Coef('Const', 1.00397     ), Coef('Const', 1.52        ), Coef('Const', 1.87        ), Coef('Const', 2.73603     ), Coef('Const', 2.57        ), Coef('Const', 2.73603     ), Coef('Const', 1.87        ), Coef('Const', 1.52        ), ], 
		[Coef('Const',-0.5         ), Coef('Const', 0.5         ), Coef('Const', 0.606218    ), Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 2.14313e-16 ), Coef('Const',-0.5         ), Coef('Const',-1           ), Coef('Const',-0.606218    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 1           ), Coef('Const', 1           ), Coef('Const', 1           ), Coef('Const', 1           ), Coef('Const', 1           ), Coef('Const', 1           ), Coef('Const', 1           ), Coef('Const', 1           ), Coef('Const', 1           ), ], ])
	
	
	
	etat1.bords   = {Bord('g2temp_0'): etat4, Bord('g2temp_1'): etat5, Bord('g2temp_2'): etat4, Bord('g2temp_3'): etat5, Bord('g2temp_4'): etat4, Bord('g2temp_5'): etat5, }
	etat1.permuts = {}
	etat1.interns = {Intern('_'): etat1, }
	etat1.subs    = {Sub('g2temp_0'): etat3, Sub('G', True): Etat.etatPoint, }
	
	etat1.buildIntern()
	
	
	etat1.eqs = [
		(Chem([Sub('g2temp_0'), Bord('g2_0'), ])	,	Chem([Bord('g2temp_0'), Sub('c2temp_0'), ])),
		(Chem([Sub('g2temp_0'), Bord('g2_2'), ])	,	Chem([Bord('g2temp_2'), Sub('c2temp_0'), ])),
		(Chem([Sub('g2temp_0'), Bord('g2_4'), ])	,	Chem([Bord('g2temp_4'), Sub('c2temp_0'), ])),
		(Chem([Sub('g2temp_0'), Bord('g2_1'), ])	,	Chem([Bord('g2temp_1'), Sub('c1temp_0'), ])),
		(Chem([Sub('g2temp_0'), Bord('g2_3'), ])	,	Chem([Bord('g2temp_3'), Sub('c1temp_0'), ])),
		(Chem([Sub('g2temp_0'), Bord('g2_5'), ])	,	Chem([Bord('g2temp_5'), Sub('c1temp_0'), ])),
		(Chem([Bord('g2temp_0'), Bord('c2temp_0'), ])	,	Chem([Bord('g2temp_5'), Bord('c1temp_1'), ])),
		(Chem([Bord('g2temp_0'), Bord('c2temp_1'), ])	,	Chem([Bord('g2temp_1'), Bord('c1temp_0'), ])),
		(Chem([Bord('g2temp_2'), Bord('c2temp_0'), ])	,	Chem([Bord('g2temp_1'), Bord('c1temp_1'), ])),
		(Chem([Bord('g2temp_2'), Bord('c2temp_1'), ])	,	Chem([Bord('g2temp_3'), Bord('c1temp_0'), ])),
		(Chem([Bord('g2temp_4'), Bord('c2temp_0'), ])	,	Chem([Bord('g2temp_3'), Bord('c1temp_1'), ])),
		(Chem([Bord('g2temp_4'), Bord('c2temp_1'), ])	,	Chem([Bord('g2temp_5'), Bord('c1temp_0'), ])),
		]
	
	
	etat1.prim.elems = [Figure(2, [
		Chem([Bord('g2temp_0'), Bord('c2temp_0'), ]),
		Chem([Bord('g2temp_1'), Bord('c1temp_0'), ]),
		Chem([Bord('g2temp_1'), Sub('c1temp_0'), Intern(''), ]),
		Chem([Bord('g2temp_2'), Bord('c2temp_0'), ]),
		Chem([Bord('g2temp_3'), Bord('c1temp_0'), ]),
		Chem([Bord('g2temp_3'), Sub('c1temp_0'), Intern(''), ]),
		Chem([Bord('g2temp_4'), Bord('c2temp_0'), ]),
		Chem([Bord('g2temp_5'), Bord('c1temp_0'), ]),
		Chem([Bord('g2temp_5'), Sub('c1temp_0'), Intern(''), ]),
		])]
	etat1.grid.elems = [
		Figure(1, [Chem([Bord('g2temp_0'), Bord('c2temp_0'), ]), Chem([Bord('g2temp_0'), Bord('c2temp_1'), ]), ]), 
		Figure(1, [Chem([Bord('g2temp_3'), Bord('c1temp_0'), ]), Chem([Bord('g2temp_3'), Intern(''), ]), Chem([Bord('g2temp_3'), Bord('c1temp_1'), ]), ]), 
		Figure(1, [Chem([Bord('g2temp_2'), Bord('c2temp_0'), ]), Chem([Bord('g2temp_2'), Bord('c2temp_1'), ]), ]), 
		Figure(1, [Chem([Bord('g2temp_5'), Bord('c1temp_0'), ]), Chem([Bord('g2temp_5'), Intern(''), ]), Chem([Bord('g2temp_5'), Bord('c1temp_1'), ]), ]), 
		Figure(1, [Chem([Bord('g2temp_4'), Bord('c2temp_0'), ]), Chem([Bord('g2temp_4'), Bord('c2temp_1'), ]), ]), 
		Figure(1, [Chem([Bord('g2temp_1'), Bord('c1temp_0'), ]), Chem([Bord('g2temp_1'), Intern(''), ]), Chem([Bord('g2temp_1'), Bord('c1temp_1'), ]), ]), ]
	
	
	etat1.space = [Chem([Bord('g2temp_0'), Bord('c2temp_0'), Intern('0'), Intern('0'), ]), Chem([Bord('g2temp_0'), Bord('c2temp_1'), Intern('0'), Intern('0'), ]), Chem([Bord('g2temp_1'), Intern('0'), Intern('0'), ]), Chem([Bord('g2temp_2'), Bord('c2temp_0'), Intern('0'), Intern('0'), ]), Chem([Bord('g2temp_3'), Bord('c1temp_0'), Intern('0'), Intern('0'), ]), Chem([Bord('g2temp_3'), Intern('0'), Intern('0'), ]), Chem([Bord('g2temp_3'), Bord('c1temp_1'), Intern('0'), Intern('0'), ]), Chem([Bord('g2temp_5'), Bord('c1temp_0'), Intern('0'), Intern('0'), ]), Chem([Bord('g2temp_5'), Intern('0'), Intern('0'), ]), ]
	
	etat1.initMat[Chem([Sub('g2temp_0')])] = FMat([
		[Coef('Const', 1           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 1           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 1           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 1           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 1           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 1           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 1           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 1           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 1           ), ], ])
	etat1.initMat[Chem([Sub('G')])] = FMat([
		[Coef('Const', 0.111111    )], 
		[Coef('Const', 0.111111    )], 
		[Coef('Const', 0.111111    )], 
		[Coef('Const', 0.111111    )], 
		[Coef('Const', 0.111111    )], 
		[Coef('Const', 0.111111    )], 
		[Coef('Const', 0.111111    )], 
		[Coef('Const', 0.111111    )], 
		[Coef('Const', 0.111111    )], ])
	
	
	
	etat2.bords   = {Bord('m_6'): etat4, Bord('m_2'): etat7, Bord('m_0'): etat4, Bord('m_1'): etat6, Bord('m_3'): etat6, Bord('m_4'): etat4, Bord('m_5'): etat6, Bord('m_7'): etat6, }
	etat2.permuts = {}
	etat2.interns = {Intern('_'): etat2, }
	etat2.subs    = {Sub('m_2'): etat3, Sub('G', True): Etat.etatPoint, Sub('m_0'): etat3, Sub('m_1'): etat3, Sub('m_3'): etat3, Sub('m_4'): etat3, }
	
	etat2.buildIntern()
	
	
	etat2.eqs = [
		(Chem([Sub('m_0'), Bord('g2_2'), Permut('c2'), ])	,	Chem([Sub('m_1'), Bord('g2_4'), ])),
		(Chem([Sub('m_1'), Bord('g2_2'), Permut('c2'), ])	,	Chem([Sub('m_2'), Bord('g2_4'), ])),
		(Chem([Sub('m_2'), Bord('g2_2'), Permut('c2'), ])	,	Chem([Sub('m_3'), Bord('g2_4'), ])),
		(Chem([Sub('m_3'), Bord('g2_2'), Permut('c2'), ])	,	Chem([Sub('m_4'), Bord('g2_4'), ])),
		(Chem([Sub('m_4'), Bord('g2_2'), Permut('c2'), ])	,	Chem([Sub('m_0'), Bord('g2_4'), ])),
		(Chem([Sub('m_0'), Bord('g2_0'), ])	,	Chem([Bord('m_0'), Sub('c2temp_0'), ])),
		(Chem([Sub('m_1'), Bord('g2_0'), ])	,	Chem([Bord('m_2'), Sub('c2_0'), ])),
		(Chem([Sub('m_2'), Bord('g2_0'), ])	,	Chem([Bord('m_2'), Sub('c2_1'), ])),
		(Chem([Sub('m_3'), Bord('g2_0'), ])	,	Chem([Bord('m_4'), Sub('c2temp_0'), ])),
		(Chem([Sub('m_4'), Bord('g2_0'), ])	,	Chem([Bord('m_6'), Sub('c2temp_0'), ])),
		(Chem([Sub('m_4'), Bord('g2_1'), ])	,	Chem([Bord('m_7'), Sub('c1_0'), ])),
		(Chem([Sub('m_0'), Bord('g2_5'), ])	,	Chem([Bord('m_7'), Sub('c1_1'), ])),
		(Chem([Sub('m_0'), Bord('g2_1'), ])	,	Chem([Bord('m_1'), Sub('c1_0'), ])),
		(Chem([Sub('m_1'), Bord('g2_5'), ])	,	Chem([Bord('m_1'), Sub('c1_1'), ])),
		(Chem([Sub('m_2'), Bord('g2_1'), ])	,	Chem([Bord('m_3'), Sub('c1_0'), ])),
		(Chem([Sub('m_3'), Bord('g2_5'), ])	,	Chem([Bord('m_3'), Sub('c1_1'), ])),
		(Chem([Sub('m_3'), Bord('g2_1'), ])	,	Chem([Bord('m_5'), Sub('c1_0'), ])),
		(Chem([Sub('m_4'), Bord('g2_5'), ])	,	Chem([Bord('m_5'), Sub('c1_1'), ])),
		(Chem([Bord('m_0'), Bord('c2temp_0'), ])	,	Chem([Bord('m_7'), Bord('c1_1'), ])),
		(Chem([Bord('m_1'), Bord('c1_0'), ])	,	Chem([Bord('m_0'), Bord('c2temp_1'), ])),
		(Chem([Bord('m_2'), Bord('c2_0'), ])	,	Chem([Bord('m_1'), Bord('c1_1'), ])),
		(Chem([Bord('m_3'), Bord('c1_0'), ])	,	Chem([Bord('m_2'), Bord('c2_1'), ])),
		(Chem([Bord('m_4'), Bord('c2temp_0'), ])	,	Chem([Bord('m_3'), Bord('c1_1'), ])),
		(Chem([Bord('m_5'), Bord('c1_0'), ])	,	Chem([Bord('m_4'), Bord('c2temp_1'), ])),
		(Chem([Bord('m_6'), Bord('c2temp_0'), ])	,	Chem([Bord('m_5'), Bord('c1_1'), ])),
		(Chem([Bord('m_7'), Bord('c1_0'), ])	,	Chem([Bord('m_6'), Bord('c2temp_1'), ])),
		]
	
	
	etat2.prim.elems = [Figure(2, [Chem([Bord('m_0'), Bord('c2temp_0'), ]), Chem([Bord('m_1'), Bord('c1_0'), ]), Chem([Bord('m_2'), Bord('c2_0'), ]), Chem([Bord('m_3'), Bord('c1_0'), ]), Chem([Bord('m_4'), Bord('c2temp_0'), ]), Chem([Bord('m_5'), Bord('c1_0'), ]), Chem([Bord('m_6'), Bord('c2temp_0'), ]), Chem([Bord('m_7'), Bord('c1_0'), ]), ])]
	etat2.grid.elems = [
		Figure(1, [Chem([Bord('m_6'), Bord('c2temp_0'), ]), Chem([Bord('m_6'), Bord('c2temp_1'), ]), ]), 
		Figure(1, [Chem([Bord('m_7'), Bord('c1_0'), ]), Chem([Bord('m_7'), Intern(''), ]), Chem([Bord('m_7'), Bord('c1_1'), ]), ]), 
		Figure(1, [Chem([Bord('m_2'), Bord('c2_0'), ]), Chem([Bord('m_2'), Bord('c2_1'), ]), ]), 
		Figure(1, [Chem([Bord('m_4'), Bord('c2temp_0'), ]), Chem([Bord('m_4'), Bord('c2temp_1'), ]), ]), 
		Figure(1, [Chem([Bord('m_3'), Bord('c1_0'), ]), Chem([Bord('m_3'), Intern(''), ]), Chem([Bord('m_3'), Bord('c1_1'), ]), ]), 
		Figure(1, [Chem([Bord('m_5'), Bord('c1_0'), ]), Chem([Bord('m_5'), Intern(''), ]), Chem([Bord('m_5'), Bord('c1_1'), ]), ]), 
		Figure(1, [Chem([Bord('m_0'), Bord('c2temp_0'), ]), Chem([Bord('m_0'), Bord('c2temp_1'), ]), ]), 
		Figure(1, [Chem([Bord('m_1'), Bord('c1_0'), ]), Chem([Bord('m_1'), Intern(''), ]), Chem([Bord('m_1'), Bord('c1_1'), ]), ]), ]
	
	
	etat2.space = [Chem([Bord('m_7'), Bord('c1_1'), Intern('0'), Intern('0'), ]), Chem([Bord('m_0'), Bord('c2temp_1'), Intern('0'), Intern('0'), ]), Chem([Bord('m_1'), Intern('0'), Intern('0'), ]), Chem([Bord('m_2'), Bord('c2_0'), Intern('0'), Intern('0'), ]), Chem([Bord('m_2'), Bord('c2_1'), Intern('0'), Intern('0'), ]), Chem([Bord('m_3'), Intern('0'), Intern('0'), ]), Chem([Bord('m_4'), Bord('c2temp_0'), Intern('0'), Intern('0'), ]), Chem([Bord('m_4'), Bord('c2temp_1'), Intern('0'), Intern('0'), ]), Chem([Bord('m_5'), Intern('0'), Intern('0'), ]), Chem([Bord('m_6'), Bord('c2temp_0'), Intern('0'), Intern('0'), ]), Chem([Bord('m_6'), Bord('c2temp_1'), Intern('0'), Intern('0'), ]), Chem([Bord('m_7'), Intern('0'), Intern('0'), ]), ]
	
	etat2.initMat[Chem([Sub('m_2')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0281219   ), Coef('Var'  , 0.0270085   ), Coef('Var'  , 0.0516061   ), Coef('Var'  , 0.0103584   ), Coef('Var'  ,-0.017125    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0638651   ), Coef('Var'  , 0.0863389   ), Coef('Var'  , 0.111039    ), Coef('Var'  , 0.158578    ), Coef('Var'  , 0.131656    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0822048   ), Coef('Var'  , 0.0942851   ), Coef('Var'  , 0.10311     ), Coef('Var'  , 0.135288    ), Coef('Var'  , 0.125456    ), ], 
		[Coef('Const', 0.333333    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.100686    ), Coef('Var'  , 0.129791    ), Coef('Var'  , 0.14219     ), Coef('Var'  , 0.233249    ), Coef('Var'  , 0.22013     ), ], 
		[Coef('Const', 0.666667    ), Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.1383      ), Coef('Var'  , 0.156893    ), Coef('Var'  , 0.144586    ), Coef('Var'  , 0.233192    ), Coef('Var'  , 0.247114    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.110944    ), Coef('Var'  , 0.116102    ), Coef('Var'  , 0.106961    ), Coef('Var'  , 0.140146    ), Coef('Var'  , 0.15018     ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.139094    ), Coef('Var'  , 0.140542    ), Coef('Var'  , 0.115832    ), Coef('Var'  , 0.158465    ), Coef('Var'  , 0.185624    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.103351    ), Coef('Var'  , 0.0812119   ), Coef('Var'  , 0.0563992   ), Coef('Var'  , 0.0102449   ), Coef('Var'  , 0.0368424   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0835861   ), Coef('Var'  , 0.070496    ), Coef('Var'  , 0.0611401   ), Coef('Var'  , 0.0258403   ), Coef('Var'  , 0.0355908   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0665299   ), Coef('Var'  , 0.03776     ), Coef('Var'  , 0.0252483   ), Coef('Var'  ,-0.0644256   ), Coef('Var'  ,-0.0516314   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0289155   ), Coef('Var'  , 0.0106583   ), Coef('Var'  , 0.0228518   ), Coef('Var'  ,-0.0643688   ), Coef('Var'  ,-0.078615    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0544021   ), Coef('Var'  , 0.0489137   ), Coef('Var'  , 0.0590371   ), Coef('Var'  , 0.023434    ), Coef('Var'  , 0.0147792   ), ], ])
	etat2.initMat[Chem([Sub('G')])] = FMat([
		[Coef('Const', 0.0833333   )], 
		[Coef('Const', 0.0833333   )], 
		[Coef('Const', 0.0833333   )], 
		[Coef('Const', 0.0833333   )], 
		[Coef('Const', 0.0833333   )], 
		[Coef('Const', 0.0833333   )], 
		[Coef('Const', 0.0833333   )], 
		[Coef('Const', 0.0833333   )], 
		[Coef('Const', 0.0833333   )], 
		[Coef('Const', 0.0833333   )], 
		[Coef('Const', 0.0833333   )], 
		[Coef('Const', 0.0833333   )], ])
	etat2.initMat[Chem([Sub('m_0')])] = FMat([
		[Coef('Const', 1           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.105479    ), Coef('Var'  , 0.139304    ), Coef('Var'  , 0.120374    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.141072    ), Coef('Var'  , 0.141133    ), Coef('Var'  , 0.0970522   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.110214    ), Coef('Var'  , 0.104624    ), Coef('Var'  , 0.0844386   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.139161    ), Coef('Var'  , 0.113608    ), Coef('Var'  , 0.0725192   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0994624   ), Coef('Var'  , 0.0567138   ), Coef('Var'  , 0.04696     ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0823059   ), Coef('Var'  , 0.0630028   ), Coef('Var'  , 0.0649424   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0616749   ), Coef('Var'  , 0.0273449   ), Coef('Var'  , 0.0459338   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0260815   ), Coef('Var'  , 0.0255159   ), Coef('Var'  , 0.0692551   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0546381   ), Coef('Var'  , 0.0612788   ), Coef('Var'  , 0.0827868   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0279926   ), Coef('Var'  , 0.0530411   ), Coef('Var'  , 0.0937882   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0676912   ), Coef('Var'  , 0.109935    ), Coef('Var'  , 0.119348    ), Coef('Const', 0.25        ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0842275   ), Coef('Var'  , 0.104498    ), Coef('Var'  , 0.102602    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), ], ])
	etat2.initMat[Chem([Sub('m_1')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0368135   ), Coef('Var'  , 0.0103584   ), Coef('Var'  , 0.0516061   ), Coef('Var'  , 0.038717    ), Coef('Var'  , 0.105479    ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.185642    ), Coef('Var'  , 0.158578    ), Coef('Var'  , 0.111039    ), Coef('Var'  , 0.107112    ), Coef('Var'  , 0.141072    ), Coef('Const', 0.25        ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.145216    ), Coef('Var'  , 0.135288    ), Coef('Var'  , 0.10311     ), Coef('Var'  , 0.197413    ), Coef('Var'  , 0.110214    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 1           ), Coef('Const', 0.666667    ), Coef('Var'  , 0.247236    ), Coef('Var'  , 0.233249    ), Coef('Var'  , 0.14219     ), Coef('Var'  , 0.190124    ), Coef('Var'  , 0.139161    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.333333    ), Coef('Var'  , 0.220414    ), Coef('Var'  , 0.233192    ), Coef('Var'  , 0.144586    ), Coef('Var'  , 0.123206    ), Coef('Var'  , 0.0994624   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.130485    ), Coef('Var'  , 0.140146    ), Coef('Var'  , 0.106961    ), Coef('Var'  , 0.0660186   ), Coef('Var'  , 0.0823059   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.131998    ), Coef('Var'  , 0.158465    ), Coef('Var'  , 0.115832    ), Coef('Var'  , 0.0493245   ), Coef('Var'  , 0.0616749   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  ,-0.0168305   ), Coef('Var'  , 0.0102449   ), Coef('Var'  , 0.0563992   ), Coef('Var'  , 0.0377661   ), Coef('Var'  , 0.0260815   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0155627   ), Coef('Var'  , 0.0258403   ), Coef('Var'  , 0.0611401   ), Coef('Var'  , 0.0417002   ), Coef('Var'  , 0.0546381   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  ,-0.078425    ), Coef('Var'  ,-0.0644256   ), Coef('Var'  , 0.0252483   ), Coef('Var'  , 0.0331324   ), Coef('Var'  , 0.0279926   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  ,-0.0516031   ), Coef('Var'  ,-0.0643688   ), Coef('Var'  , 0.0228518   ), Coef('Var'  , 0.0450892   ), Coef('Var'  , 0.0676912   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0334924   ), Coef('Var'  , 0.023434    ), Coef('Var'  , 0.0590371   ), Coef('Var'  , 0.0703983   ), Coef('Var'  , 0.0842275   ), Coef('Const', 0           ), Coef('Const', 0           ), ], ])
	etat2.initMat[Chem([Sub('m_3')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0667762   ), Coef('Var'  , 0.0313291   ), Coef('Var'  , 0.0281219   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0456754   ), Coef('Var'  , 0.0351384   ), Coef('Var'  , 0.0638651   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0661528   ), Coef('Var'  , 0.0664669   ), Coef('Var'  , 0.0822048   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0485233   ), Coef('Var'  , 0.0621316   ), Coef('Var'  , 0.100686    ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0754878   ), Coef('Var'  , 0.112278    ), Coef('Var'  , 0.1383      ), Coef('Const', 0.25        ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0852104   ), Coef('Var'  , 0.103332    ), Coef('Var'  , 0.110944    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 1           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0996044   ), Coef('Var'  , 0.135432    ), Coef('Var'  , 0.139094    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.120705    ), Coef('Var'  , 0.131623    ), Coef('Var'  , 0.103351    ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.101632    ), Coef('Var'  , 0.10067     ), Coef('Var'  , 0.0835861   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.117857    ), Coef('Var'  , 0.104629    ), Coef('Var'  , 0.0665299   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0908928   ), Coef('Var'  , 0.0544827   ), Coef('Var'  , 0.0289155   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0814827   ), Coef('Var'  , 0.0624872   ), Coef('Var'  , 0.0544021   ), Coef('Const', 0           ), Coef('Const', 0           ), ], ])
	etat2.initMat[Chem([Sub('m_4')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.120374    ), Coef('Var'  , 0.101551    ), Coef('Var'  , 0.0667762   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0970522   ), Coef('Var'  , 0.0599608   ), Coef('Var'  , 0.0456754   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0844386   ), Coef('Var'  , 0.0679345   ), Coef('Var'  , 0.0661528   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0725192   ), Coef('Var'  , 0.0401381   ), Coef('Var'  , 0.0485233   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.04696     ), Coef('Var'  , 0.0424138   ), Coef('Var'  , 0.0754878   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0649424   ), Coef('Var'  , 0.0682271   ), Coef('Var'  , 0.0852104   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0459338   ), Coef('Var'  , 0.0645121   ), Coef('Var'  , 0.0996044   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0692551   ), Coef('Var'  , 0.106103    ), Coef('Var'  , 0.120705    ), Coef('Const', 0.25        ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0827868   ), Coef('Var'  , 0.100314    ), Coef('Var'  , 0.101632    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 1           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0937882   ), Coef('Var'  , 0.125925    ), Coef('Var'  , 0.117857    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.119348    ), Coef('Var'  , 0.12365     ), Coef('Var'  , 0.0908928   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.102602    ), Coef('Var'  , 0.099271    ), Coef('Var'  , 0.0814827   ), Coef('Const', 0           ), Coef('Const', 0           ), ], ])
	
	
	
	etat3.bords   = {Bord('g2_0'): etat7, Bord('g2_2'): etat7, Bord('g2_4'): etat7, Bord('g2_1'): etat6, Bord('g2_3'): etat6, Bord('g2_5'): etat6, }
	etat3.permuts = {}
	etat3.interns = {Intern('_'): etat3, }
	etat3.subs    = {Sub('g2_0'): etat3, Sub('G', True): Etat.etatPoint, Sub('g2_2'): etat3, Sub('g2_4'): etat3, Sub('g2_1'): etat3, Sub('g2_3'): etat3, Sub('g2_5'): etat3, }
	
	etat3.buildIntern()
	
	
	etat3.eqs = [
		(Chem([Sub('g2_0'), Bord('g2_2'), Permut('c2'), ])	,	Chem([Sub('g2_1'), Bord('g2_4'), ])),
		(Chem([Sub('g2_1'), Bord('g2_2'), Permut('c2'), ])	,	Chem([Sub('g2_2'), Bord('g2_4'), ])),
		(Chem([Sub('g2_2'), Bord('g2_2'), Permut('c2'), ])	,	Chem([Sub('g2_3'), Bord('g2_4'), ])),
		(Chem([Sub('g2_3'), Bord('g2_2'), Permut('c2'), ])	,	Chem([Sub('g2_4'), Bord('g2_4'), ])),
		(Chem([Sub('g2_4'), Bord('g2_2'), Permut('c2'), ])	,	Chem([Sub('g2_5'), Bord('g2_4'), ])),
		(Chem([Sub('g2_5'), Bord('g2_2'), Permut('c2'), ])	,	Chem([Sub('g2_0'), Bord('g2_4'), ])),
		(Chem([Sub('g2_0'), Bord('g2_0'), ])	,	Chem([Bord('g2_0'), Sub('c2_0'), ])),
		(Chem([Sub('g2_1'), Bord('g2_0'), ])	,	Chem([Bord('g2_0'), Sub('c2_1'), ])),
		(Chem([Sub('g2_2'), Bord('g2_0'), ])	,	Chem([Bord('g2_2'), Sub('c2_0'), ])),
		(Chem([Sub('g2_3'), Bord('g2_0'), ])	,	Chem([Bord('g2_2'), Sub('c2_1'), ])),
		(Chem([Sub('g2_4'), Bord('g2_0'), ])	,	Chem([Bord('g2_4'), Sub('c2_0'), ])),
		(Chem([Sub('g2_5'), Bord('g2_0'), ])	,	Chem([Bord('g2_4'), Sub('c2_1'), ])),
		(Chem([Sub('g2_5'), Bord('g2_1'), ])	,	Chem([Bord('g2_5'), Sub('c1_0'), ])),
		(Chem([Sub('g2_0'), Bord('g2_5'), ])	,	Chem([Bord('g2_5'), Sub('c1_1'), ])),
		(Chem([Sub('g2_1'), Bord('g2_1'), ])	,	Chem([Bord('g2_1'), Sub('c1_0'), ])),
		(Chem([Sub('g2_2'), Bord('g2_5'), ])	,	Chem([Bord('g2_1'), Sub('c1_1'), ])),
		(Chem([Sub('g2_3'), Bord('g2_1'), ])	,	Chem([Bord('g2_3'), Sub('c1_0'), ])),
		(Chem([Sub('g2_4'), Bord('g2_5'), ])	,	Chem([Bord('g2_3'), Sub('c1_1'), ])),
		(Chem([Bord('g2_0'), Bord('c2_0'), ])	,	Chem([Bord('g2_5'), Bord('c1_1'), ])),
		(Chem([Bord('g2_0'), Bord('c2_1'), ])	,	Chem([Bord('g2_1'), Bord('c1_0'), ])),
		(Chem([Bord('g2_2'), Bord('c2_0'), ])	,	Chem([Bord('g2_1'), Bord('c1_1'), ])),
		(Chem([Bord('g2_2'), Bord('c2_1'), ])	,	Chem([Bord('g2_3'), Bord('c1_0'), ])),
		(Chem([Bord('g2_4'), Bord('c2_0'), ])	,	Chem([Bord('g2_3'), Bord('c1_1'), ])),
		(Chem([Bord('g2_4'), Bord('c2_1'), ])	,	Chem([Bord('g2_5'), Bord('c1_0'), ])),
		]
	
	
	etat3.prim.elems = [Figure(2, [Chem([Bord('g2_0'), Bord('c2_0'), ]), Chem([Bord('g2_1'), Bord('c1_0'), ]), Chem([Bord('g2_1'), Intern(''), ]), Chem([Bord('g2_2'), Bord('c2_0'), ]), Chem([Bord('g2_3'), Bord('c1_0'), ]), Chem([Bord('g2_3'), Intern(''), ]), Chem([Bord('g2_4'), Bord('c2_0'), ]), Chem([Bord('g2_5'), Bord('c1_0'), ]), Chem([Bord('g2_5'), Intern(''), ]), ])]
	etat3.grid.elems = [
		Figure(1, [Chem([Bord('g2_3'), Bord('c1_0'), ]), Chem([Bord('g2_3'), Intern(''), ]), Chem([Bord('g2_3'), Bord('c1_1'), ]), ]), 
		Figure(1, [Chem([Bord('g2_2'), Bord('c2_0'), ]), Chem([Bord('g2_2'), Bord('c2_1'), ]), ]), 
		Figure(1, [Chem([Bord('g2_1'), Bord('c1_0'), ]), Chem([Bord('g2_1'), Intern(''), ]), Chem([Bord('g2_1'), Bord('c1_1'), ]), ]), 
		Figure(1, [Chem([Bord('g2_0'), Bord('c2_0'), ]), Chem([Bord('g2_0'), Bord('c2_1'), ]), ]), 
		Figure(1, [Chem([Bord('g2_5'), Bord('c1_0'), ]), Chem([Bord('g2_5'), Intern(''), ]), Chem([Bord('g2_5'), Bord('c1_1'), ]), ]), 
		Figure(1, [Chem([Bord('g2_4'), Bord('c2_0'), ]), Chem([Bord('g2_4'), Bord('c2_1'), ]), ]), ]
	
	
	etat3.space = [Chem([Bord('g2_0'), Bord('c2_0'), Intern('0'), Intern('0'), ]), Chem([Bord('g2_1'), Bord('c1_0'), Intern('0'), Intern('0'), ]), Chem([Bord('g2_1'), Intern('0'), Intern('0'), ]), Chem([Bord('g2_2'), Bord('c2_0'), Intern('0'), Intern('0'), ]), Chem([Bord('g2_3'), Bord('c1_0'), Intern('0'), Intern('0'), ]), Chem([Bord('g2_3'), Intern('0'), Intern('0'), ]), Chem([Bord('g2_3'), Bord('c1_1'), Intern('0'), Intern('0'), ]), Chem([Bord('g2_5'), Bord('c1_0'), Intern('0'), Intern('0'), ]), Chem([Bord('g2_5'), Intern('0'), Intern('0'), ]), ]
	
	etat3.initMat[Chem([Sub('g2_0')])] = FMat([
		[Coef('Const', 1           ), Coef('Const', 0.666667    ), Coef('Const', 0.528041    ), Coef('Const', 0.393259    ), Coef('Var'  , 0.195793    ), Coef('Var'  , 0.232744    ), Coef('Var'  , 0.202188    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.333333    ), Coef('Const', 0.249959    ), Coef('Const', 0.393259    ), Coef('Var'  , 0.198062    ), Coef('Var'  , 0.168095    ), Coef('Var'  , 0.113755    ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.0381468   ), Coef('Const', 0.0625117   ), Coef('Var'  , 0.147169    ), Coef('Var'  , 0.0835896   ), Coef('Var'  , 0.0764399   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.0134426   ), Coef('Const', 0.0141972   ), Coef('Var'  , 0.11338     ), Coef('Var'  , 0.0423919   ), Coef('Var'  , 0.0226782   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.0175775   ), Coef('Const', 0.0209399   ), Coef('Var'  , 0.0264291   ), Coef('Var'  , 0.0289801   ), Coef('Var'  , 0.0200342   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.0167843   ), Coef('Const', 0.0181835   ), Coef('Var'  , 0.0417465   ), Coef('Var'  , 0.0362382   ), Coef('Var'  , 0.0732343   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.0214091   ), Coef('Const', 0.0209399   ), Coef('Var'  , 0.0241601   ), Coef('Var'  , 0.0539952   ), Coef('Var'  , 0.108467    ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.0109833   ), Coef('Const', 0.0141972   ), Coef('Var'  , 0.108842    ), Coef('Var'  , 0.132099    ), Coef('Var'  , 0.199544    ), Coef('Const', 0.25        ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.103657    ), Coef('Const', 0.0625117   ), Coef('Var'  , 0.144418    ), Coef('Var'  , 0.221867    ), Coef('Var'  , 0.183659    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), ], ])
	etat3.initMat[Chem([Sub('G')])] = FMat([
		[Coef('Const', 0.111111    )], 
		[Coef('Const', 0.111111    )], 
		[Coef('Const', 0.111111    )], 
		[Coef('Const', 0.111111    )], 
		[Coef('Const', 0.111111    )], 
		[Coef('Const', 0.111111    )], 
		[Coef('Const', 0.111111    )], 
		[Coef('Const', 0.111111    )], 
		[Coef('Const', 0.111111    )], ])
	etat3.initMat[Chem([Sub('g2_2')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.0215644   ), Coef('Const', 0.0210108   ), Coef('Var'  , 0.0252272   ), Coef('Var'  , 0.0539497   ), Coef('Var'  , 0.112518    ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.0110463   ), Coef('Const', 0.014179    ), Coef('Var'  , 0.109349    ), Coef('Var'  , 0.131876    ), Coef('Var'  , 0.19959     ), Coef('Const', 0.25        ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.102675    ), Coef('Const', 0.0618224   ), Coef('Var'  , 0.144396    ), Coef('Var'  , 0.221675    ), Coef('Var'  , 0.182059    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 1           ), Coef('Const', 0.666667    ), Coef('Const', 0.527836    ), Coef('Const', 0.393061    ), Coef('Var'  , 0.195233    ), Coef('Var'  , 0.232965    ), Coef('Var'  , 0.198183    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.333333    ), Coef('Const', 0.250305    ), Coef('Const', 0.393414    ), Coef('Var'  , 0.196995    ), Coef('Var'  , 0.168238    ), Coef('Var'  , 0.109704    ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.0381114   ), Coef('Const', 0.0624824   ), Coef('Var'  , 0.146533    ), Coef('Var'  , 0.0832376   ), Coef('Var'  , 0.0747842   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.0135908   ), Coef('Const', 0.0143779   ), Coef('Var'  , 0.112873    ), Coef('Var'  , 0.0423628   ), Coef('Var'  , 0.0226325   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.0178225   ), Coef('Const', 0.0212268   ), Coef('Var'  , 0.0269893   ), Coef('Var'  , 0.0291521   ), Coef('Var'  , 0.0240396   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.0170488   ), Coef('Const', 0.0184254   ), Coef('Var'  , 0.0424041   ), Coef('Var'  , 0.0365439   ), Coef('Var'  , 0.0764903   ), Coef('Const', 0           ), Coef('Const', 0           ), ], ])
	etat3.initMat[Chem([Sub('g2_4')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.0133751   ), Coef('Const', 0.014179    ), Coef('Var'  , 0.109758    ), Coef('Var'  , 0.0422124   ), Coef('Var'  , 0.0233648   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.0175819   ), Coef('Const', 0.0210108   ), Coef('Var'  , 0.0235379   ), Coef('Var'  , 0.0289354   ), Coef('Var'  , 0.0256338   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.016968    ), Coef('Const', 0.0184254   ), Coef('Var'  , 0.0408732   ), Coef('Var'  , 0.0364907   ), Coef('Var'  , 0.0774829   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.0217012   ), Coef('Const', 0.0212268   ), Coef('Var'  , 0.0248905   ), Coef('Var'  , 0.0542069   ), Coef('Var'  , 0.11338     ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.0111588   ), Coef('Const', 0.0143779   ), Coef('Var'  , 0.112464    ), Coef('Var'  , 0.13208     ), Coef('Var'  , 0.198857    ), Coef('Const', 0.25        ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.103795    ), Coef('Const', 0.0624824   ), Coef('Var'  , 0.14705     ), Coef('Var'  , 0.221477    ), Coef('Var'  , 0.181119    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 1           ), Coef('Const', 0.666667    ), Coef('Const', 0.527974    ), Coef('Const', 0.393414    ), Coef('Var'  , 0.198684    ), Coef('Var'  , 0.23294     ), Coef('Var'  , 0.196588    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.333333    ), Coef('Const', 0.249746    ), Coef('Const', 0.393061    ), Coef('Var'  , 0.197332    ), Coef('Var'  , 0.168313    ), Coef('Var'  , 0.108842    ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.0377      ), Coef('Const', 0.0618224   ), Coef('Var'  , 0.14541     ), Coef('Var'  , 0.0833439   ), Coef('Var'  , 0.074732    ), Coef('Const', 0           ), Coef('Const', 0           ), ], ])
	etat3.initMat[Chem([Sub('g2_1')])] = FMat([
		[Coef('Const', 0.333333    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.112518    ), Coef('Var'  , 0.168095    ), Coef('Var'  , 0.195793    ), Coef('Const', 0.393259    ), Coef('Const', 0.249959    ), ], 
		[Coef('Const', 0.666667    ), Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.19959     ), Coef('Var'  , 0.232744    ), Coef('Var'  , 0.198062    ), Coef('Const', 0.393259    ), Coef('Const', 0.528041    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.182059    ), Coef('Var'  , 0.221867    ), Coef('Var'  , 0.147169    ), Coef('Const', 0.0625117   ), Coef('Const', 0.103657    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.198183    ), Coef('Var'  , 0.132099    ), Coef('Var'  , 0.11338     ), Coef('Const', 0.0141972   ), Coef('Const', 0.0109833   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.109704    ), Coef('Var'  , 0.0539952   ), Coef('Var'  , 0.0264291   ), Coef('Const', 0.0209399   ), Coef('Const', 0.0214091   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0747842   ), Coef('Var'  , 0.0362382   ), Coef('Var'  , 0.0417465   ), Coef('Const', 0.0181835   ), Coef('Const', 0.0167843   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0226325   ), Coef('Var'  , 0.0289801   ), Coef('Var'  , 0.0241601   ), Coef('Const', 0.0209399   ), Coef('Const', 0.0175775   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0240396   ), Coef('Var'  , 0.0423919   ), Coef('Var'  , 0.108842    ), Coef('Const', 0.0141972   ), Coef('Const', 0.0134426   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0764903   ), Coef('Var'  , 0.0835896   ), Coef('Var'  , 0.144418    ), Coef('Const', 0.0625117   ), Coef('Const', 0.0381468   ), ], ])
	etat3.initMat[Chem([Sub('g2_3')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0233648   ), Coef('Var'  , 0.0289354   ), Coef('Var'  , 0.0252272   ), Coef('Const', 0.0210108   ), Coef('Const', 0.0175819   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0256338   ), Coef('Var'  , 0.0422124   ), Coef('Var'  , 0.109349    ), Coef('Const', 0.014179    ), Coef('Const', 0.0133751   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0774829   ), Coef('Var'  , 0.0833439   ), Coef('Var'  , 0.144396    ), Coef('Const', 0.0618224   ), Coef('Const', 0.0377      ), ], 
		[Coef('Const', 0.333333    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.11338     ), Coef('Var'  , 0.168313    ), Coef('Var'  , 0.195233    ), Coef('Const', 0.393061    ), Coef('Const', 0.249746    ), ], 
		[Coef('Const', 0.666667    ), Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.198857    ), Coef('Var'  , 0.23294     ), Coef('Var'  , 0.196995    ), Coef('Const', 0.393414    ), Coef('Const', 0.527974    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.181119    ), Coef('Var'  , 0.221477    ), Coef('Var'  , 0.146533    ), Coef('Const', 0.0624824   ), Coef('Const', 0.103795    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.196588    ), Coef('Var'  , 0.13208     ), Coef('Var'  , 0.112873    ), Coef('Const', 0.0143779   ), Coef('Const', 0.0111588   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.108842    ), Coef('Var'  , 0.0542069   ), Coef('Var'  , 0.0269893   ), Coef('Const', 0.0212268   ), Coef('Const', 0.0217012   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.074732    ), Coef('Var'  , 0.0364907   ), Coef('Var'  , 0.0424041   ), Coef('Const', 0.0184254   ), Coef('Const', 0.016968    ), ], ])
	etat3.initMat[Chem([Sub('g2_5')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.202188    ), Coef('Var'  , 0.131876    ), Coef('Var'  , 0.109758    ), Coef('Const', 0.014179    ), Coef('Const', 0.0110463   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.113755    ), Coef('Var'  , 0.0539497   ), Coef('Var'  , 0.0235379   ), Coef('Const', 0.0210108   ), Coef('Const', 0.0215644   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0764399   ), Coef('Var'  , 0.0365439   ), Coef('Var'  , 0.0408732   ), Coef('Const', 0.0184254   ), Coef('Const', 0.0170488   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0226782   ), Coef('Var'  , 0.0291521   ), Coef('Var'  , 0.0248905   ), Coef('Const', 0.0212268   ), Coef('Const', 0.0178225   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0200342   ), Coef('Var'  , 0.0423628   ), Coef('Var'  , 0.112464    ), Coef('Const', 0.0143779   ), Coef('Const', 0.0135908   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0732343   ), Coef('Var'  , 0.0832376   ), Coef('Var'  , 0.14705     ), Coef('Const', 0.0624824   ), Coef('Const', 0.0381114   ), ], 
		[Coef('Const', 0.333333    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.108467    ), Coef('Var'  , 0.168238    ), Coef('Var'  , 0.198684    ), Coef('Const', 0.393414    ), Coef('Const', 0.250305    ), ], 
		[Coef('Const', 0.666667    ), Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.199544    ), Coef('Var'  , 0.232965    ), Coef('Var'  , 0.197332    ), Coef('Const', 0.393061    ), Coef('Const', 0.527836    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.183659    ), Coef('Var'  , 0.221675    ), Coef('Var'  , 0.14541     ), Coef('Const', 0.0618224   ), Coef('Const', 0.102675    ), ], ])
	
	
	
	etat4.bords   = {Bord('c2temp_0'): etat8, Bord('c2temp_1'): etat8, }
	etat4.permuts = {Permut('c2temp'): etat4, }
	etat4.interns = {Intern('_'): etat4, }
	etat4.subs    = {Sub('G', True): Etat.etatPoint, Sub('c2temp_0'): etat7, }
	
	etat4.buildIntern()
	etat4.fm_[Permut('c2temp')] = PMat(2, [1, 0, ])
	
	
	etat4.eqs = [
		(Chem([Permut('c2temp'), Bord('c2temp_0'), ])	,	Chem([Bord('c2temp_1')])),
		(Chem([Permut('c2temp'), Bord('c2temp_1'), ])	,	Chem([Bord('c2temp_0')])),
		(Chem([Permut('c2temp'), Sub('c2temp_0'), ])	,	Chem([Sub('c2temp_0'), Permut('c2'), ])),
		(Chem([Bord('c2temp_0'), Sub('s_0'), ])	,	Chem([Sub('c2temp_0'), Bord('c2_0'), ])),
		(Chem([Bord('c2temp_1'), Sub('s_0'), ])	,	Chem([Sub('c2temp_0'), Bord('c2_1'), ])),
		]
	
	
	etat4.prim.elems = [Figure(1, [Chem([Bord('c2temp_0')]), Chem([Bord('c2temp_1')]), ])]
	etat4.grid.elems = [Figure(1, [Chem([Bord('c2temp_0')]), Chem([Bord('c2temp_1')]), ])]
	
	
	etat4.space = [Chem([Bord('c2temp_0'), Intern('0'), Intern('0'), ]), Chem([Bord('c2temp_1'), Intern('0'), Intern('0'), ]), ]
	
	etat4.initMat[Chem([Sub('G')])] = FMat([
		[Coef('Const', 0.5         )], 
		[Coef('Const', 0.5         )], ])
	etat4.initMat[Chem([Sub('c2temp_0')])] = FMat([
		[Coef('Const', 1           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 1           ), ], ])
	
	
	
	etat5.bords   = {Bord('c1temp_0'): etat8, Bord('c1temp_1'): etat8, }
	etat5.permuts = {}
	etat5.interns = {Intern('_'): etat5, }
	etat5.subs    = {Sub('G', True): Etat.etatPoint, Sub('c1temp_0'): etat6, }
	
	etat5.buildIntern()
	
	
	etat5.eqs = [
		(Chem([Bord('c1temp_0'), Sub('s_0'), ])	,	Chem([Sub('c1temp_0'), Bord('c1_0'), ])),
		(Chem([Bord('c1temp_1'), Sub('s_0'), ])	,	Chem([Sub('c1temp_0'), Bord('c1_1'), ])),
		]
	
	
	etat5.prim.elems = [Figure(1, [Chem([Bord('c1temp_0')]), Chem([Bord('c1temp_1')]), ])]
	etat5.grid.elems = [Figure(1, [Chem([Bord('c1temp_0')]), Chem([Intern('')]), Chem([Bord('c1temp_1')]), ])]
	
	
	etat5.space = [Chem([Bord('c1temp_0'), Intern('0'), Intern('0'), ]), Chem([Intern('0'), Intern('0'), ]), Chem([Bord('c1temp_1'), Intern('0'), Intern('0'), ]), ]
	
	etat5.initMat[Chem([Sub('G')])] = FMat([
		[Coef('Const', 0           )], 
		[Coef('Const', 1           )], 
		[Coef('Const', 0           )], ])
	etat5.initMat[Chem([Sub('c1temp_0')])] = FMat([
		[Coef('Const', 1           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 1           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 1           ), ], ])
	
	
	
	etat6.bords   = {Bord('c1_0'): etat8, Bord('c1_1'): etat8, }
	etat6.permuts = {}
	etat6.interns = {Intern('_'): etat6, }
	etat6.subs    = {Sub('G', True): Etat.etatPoint, Sub('c1_0'): etat6, Sub('c1_1'): etat6, }
	
	etat6.buildIntern()
	
	
	etat6.eqs = [
		(Chem([Bord('c1_0'), Sub('s_0'), ])	,	Chem([Sub('c1_0'), Bord('c1_0'), ])),
		(Chem([Sub('c1_0'), Bord('c1_1'), ])	,	Chem([Sub('c1_1'), Bord('c1_0'), ])),
		(Chem([Bord('c1_1'), Sub('s_0'), ])	,	Chem([Sub('c1_1'), Bord('c1_1'), ])),
		]
	
	
	etat6.prim.elems = [Figure(1, [Chem([Bord('c1_0')]), Chem([Bord('c1_1')]), ])]
	etat6.grid.elems = [Figure(1, [Chem([Bord('c1_0')]), Chem([Intern('')]), Chem([Bord('c1_1')]), ])]
	
	
	etat6.space = [Chem([Bord('c1_0'), Intern('0'), Intern('0'), ]), Chem([Intern('0'), Intern('0'), ]), Chem([Bord('c1_1'), Intern('0'), Intern('0'), ]), ]
	
	etat6.initMat[Chem([Sub('G')])] = FMat([
		[Coef('Const', 0           )], 
		[Coef('Const', 1           )], 
		[Coef('Const', 0           )], ])
	etat6.initMat[Chem([Sub('c1_0')])] = FMat([
		[Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), ], ])
	etat6.initMat[Chem([Sub('c1_1')])] = FMat([
		[Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), ], ])
	
	
	
	etat7.bords   = {Bord('c2_0'): etat8, Bord('c2_1'): etat8, }
	etat7.permuts = {Permut('c2'): etat7, }
	etat7.interns = {Intern('_'): etat7, }
	etat7.subs    = {Sub('G', True): Etat.etatPoint, Sub('c2_0'): etat7, Sub('c2_1'): etat7, }
	
	etat7.buildIntern()
	etat7.fm_[Permut('c2')] = PMat(2, [1, 0, ])
	
	
	etat7.eqs = [
		(Chem([Permut('c2'), Bord('c2_0'), ])	,	Chem([Bord('c2_1')])),
		(Chem([Permut('c2'), Bord('c2_1'), ])	,	Chem([Bord('c2_0')])),
		(Chem([Permut('c2'), Sub('c2_0'), ])	,	Chem([Sub('c2_1'), Permut('c2'), ])),
		(Chem([Permut('c2'), Sub('c2_1'), ])	,	Chem([Sub('c2_0'), Permut('c2'), ])),
		(Chem([Bord('c2_0'), Sub('s_0'), ])	,	Chem([Sub('c2_0'), Bord('c2_0'), ])),
		(Chem([Bord('c2_1'), Sub('s_0'), ])	,	Chem([Sub('c2_1'), Bord('c2_1'), ])),
		]
	
	
	etat7.prim.elems = []
	etat7.grid.elems = [Figure(1, [Chem([Bord('c2_0')]), Chem([Bord('c2_1')]), ])]
	
	
	etat7.space = [Chem([Bord('c2_0'), Intern('0'), Intern('0'), ]), Chem([Bord('c2_1'), Intern('0'), Intern('0'), ]), ]
	
	etat7.initMat[Chem([Sub('G')])] = FMat([
		[Coef('Const', 0.5         )], 
		[Coef('Const', 0.5         )], ])
	etat7.initMat[Chem([Sub('c2_0')])] = FMat([
		[Coef('Const', 1           ), Coef('Const', 0.666667    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.333333    ), ], ])
	etat7.initMat[Chem([Sub('c2_1')])] = FMat([
		[Coef('Const', 0.333333    ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.666667    ), Coef('Const', 1           ), ], ])
	
	
	
	etat8.bords   = {}
	etat8.permuts = {}
	etat8.interns = {Intern('_'): etat8, }
	etat8.subs    = {Sub('G', True): Etat.etatPoint, Sub('s_0'): etat8, }
	
	etat8.buildIntern()
	
	
	etat8.eqs = [
		]
	
	
	etat8.prim.elems = []
	etat8.grid.elems = []
	
	
	etat8.space = [Chem([Intern('0'), Intern('0'), ])]
	
	etat8.initMat[Chem([Sub('G')])] = FMat([[Coef('Const', 1           )]])
	etat8.initMat[Chem([Sub('s_0')])] = FMat([[Coef('Const', 1           )]])
	
	
	
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
