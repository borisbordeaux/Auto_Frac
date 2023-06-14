# -*- coding: utf-8 -*-

# Automatically generated, from file : cube.py, function : modele()

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
	etat7 = Etat('B2',1)
	etat8 = Etat('s',1)
	
	
	etat0.subs   = {Sub('0'): etat1, Sub('1'): etat2, Sub('2'): etat3, Sub('3'): etat4, Sub('4'): etat5, Sub('5'): etat6, }
	
	etat0.eqs = [
		(Chem([Sub('0'), Bord('0'), Bord('1'), ])	,	Chem([Sub('4'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('1'), Bord('1'), ])	,	Chem([Sub('2'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('2'), Bord('1'), ])	,	Chem([Sub('3'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('3'), Bord('1'), ])	,	Chem([Sub('1'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('0'), Bord('1'), ])	,	Chem([Sub('5'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('1'), Bord('1'), ])	,	Chem([Sub('4'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('3'), Bord('1'), ])	,	Chem([Sub('3'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('0'), Bord('1'), ])	,	Chem([Sub('4'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('1'), Bord('1'), ])	,	Chem([Sub('5'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('2'), Bord('1'), ])	,	Chem([Sub('3'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('3'), Bord('1'), Bord('1'), ])	,	Chem([Sub('5'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('4'), Bord('3'), Bord('1'), ])	,	Chem([Sub('5'), Bord('1'), Bord('1'), ])),
		]
	
	
	etat0.space = []
	
	etat0.initMat[Chem([Sub('0')])] = FMat([
		[Coef('Var'  ,-1.81512     ), Coef('Var'  ,-1.89458     ), Coef('Var'  ,-1.27685     ), Coef('Var'  ,-0.414503    ), Coef('Var'  , 0.81999     ), Coef('Var'  , 0.450428    ), Coef('Var'  , 0.275697    ), Coef('Var'  ,-1.03379     ), ], 
		[Coef('Var'  ,-0.527637    ), Coef('Var'  ,-1.41623     ), Coef('Var'  ,-1.55484     ), Coef('Var'  ,-2.43391     ), Coef('Var'  ,-2.33865     ), Coef('Var'  ,-2.29729     ), Coef('Var'  ,-1.31361     ), Coef('Var'  ,-1.28149     ), ], 
		[Coef('Var'  , 3.55864     ), Coef('Var'  , 2.58984     ), Coef('Var'  , 1.43111     ), Coef('Var'  , 1.91732     ), Coef('Var'  , 2.36776     ), Coef('Var'  , 3.63375     ), Coef('Var'  , 4.48936     ), Coef('Var'  , 4.29199     ), ], 
		[Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), ], ])
	etat0.initMat[Chem([Sub('1')])] = FMat([
		[Coef('Var'  ,-0.281466    ), Coef('Var'  ,-0.591419    ), Coef('Var'  ,-0.305394    ), Coef('Var'  ,-1.46158     ), Coef('Var'  ,-1.83796     ), Coef('Var'  ,-2.30793     ), Coef('Var'  ,-1.81512     ), Coef('Var'  ,-1.443       ), ], 
		[Coef('Var'  , 1.04169     ), Coef('Var'  , 2.06038     ), Coef('Var'  , 2.36575     ), Coef('Var'  , 1.9244      ), Coef('Var'  , 0.804415    ), Coef('Var'  , 0.313508    ), Coef('Var'  ,-0.527637    ), Coef('Var'  , 0.4304      ), ], 
		[Coef('Var'  , 4.5973      ), Coef('Var'  , 3.82254     ), Coef('Var'  , 2.57938     ), Coef('Var'  , 2.11088     ), Coef('Var'  , 1.53635     ), Coef('Var'  , 2.6416      ), Coef('Var'  , 3.55864     ), Coef('Var'  , 4.36734     ), ], 
		[Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), ], ])
	etat0.initMat[Chem([Sub('2')])] = FMat([
		[Coef('Var'  , 0.81999     ), Coef('Var'  , 1.11718     ), Coef('Var'  , 0.812821    ), Coef('Var'  , 1.96796     ), Coef('Var'  , 2.33859     ), Coef('Var'  , 2.82705     ), Coef('Var'  , 2.35369     ), Coef('Var'  , 1.97653     ), ], 
		[Coef('Var'  ,-2.33865     ), Coef('Var'  ,-2.05833     ), Coef('Var'  ,-1.02647     ), Coef('Var'  ,-0.412393    ), Coef('Var'  , 0.563793    ), Coef('Var'  ,-0.270399    ), Coef('Var'  ,-0.765595    ), Coef('Var'  ,-1.8957      ), ], 
		[Coef('Var'  , 2.36776     ), Coef('Var'  , 1.12243     ), Coef('Var'  , 0.363779    ), Coef('Var'  , 0.549641    ), Coef('Var'  , 1.36215     ), Coef('Var'  , 2.25707     ), Coef('Var'  , 3.38369     ), Coef('Var'  , 2.81878     ), ], 
		[Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), ], ])
	etat0.initMat[Chem([Sub('3')])] = FMat([
		[Coef('Var'  , 0.275697    ), Coef('Var'  , 1.57685     ), Coef('Var'  , 2.35369     ), Coef('Var'  , 2.42776     ), Coef('Var'  , 1.79345     ), Coef('Var'  , 0.951792    ), Coef('Var'  ,-0.281466    ), Coef('Var'  , 0.0968679   ), ], 
		[Coef('Var'  ,-1.31361     ), Coef('Var'  ,-1.15067     ), Coef('Var'  ,-0.765595    ), Coef('Var'  , 0.47224     ), Coef('Var'  , 1.58254     ), Coef('Var'  , 1.49332     ), Coef('Var'  , 1.04169     ), Coef('Var'  ,-0.135156    ), ], 
		[Coef('Var'  , 4.48936     ), Coef('Var'  , 4.37816     ), Coef('Var'  , 3.38369     ), Coef('Var'  , 3.81884     ), Coef('Var'  , 3.49849     ), Coef('Var'  , 4.51161     ), Coef('Var'  , 4.5973      ), Coef('Var'  , 5.06084     ), ], 
		[Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), ], ])
	etat0.initMat[Chem([Sub('4')])] = FMat([
		[Coef('Var'  , 0.240513    ), Coef('Var'  , 0.408236    ), Coef('Var'  , 0.812821    ), Coef('Var'  ,-0.418124    ), Coef('Var'  ,-1.27685     ), Coef('Var'  ,-1.90558     ), Coef('Var'  ,-1.83796     ), Coef('Var'  ,-1.05818     ), ], 
		[Coef('Var'  , 1.36187     ), Coef('Var'  , 0.159771    ), Coef('Var'  ,-1.02647     ), Coef('Var'  ,-1.47432     ), Coef('Var'  ,-1.55484     ), Coef('Var'  ,-0.453194    ), Coef('Var'  , 0.804415    ), Coef('Var'  , 1.2022      ), ], 
		[Coef('Var'  , 0.470807    ), Coef('Var'  , 1.42341e-08 ), Coef('Var'  , 0.363779    ), Coef('Var'  , 0.418636    ), Coef('Var'  , 1.43111     ), Coef('Var'  , 1.08781     ), Coef('Var'  , 1.53635     ), Coef('Var'  , 0.537915    ), ], 
		[Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), ], ])
	etat0.initMat[Chem([Sub('5')])] = FMat([
		[Coef('Var'  , 1.79345     ), Coef('Var'  , 2.41119     ), Coef('Var'  , 2.33859     ), Coef('Var'  , 1.5516      ), Coef('Var'  , 0.240513    ), Coef('Var'  , 0.0636405   ), Coef('Var'  ,-0.305394    ), Coef('Var'  , 0.931098    ), ], 
		[Coef('Var'  , 1.58254     ), Coef('Var'  , 1.44894     ), Coef('Var'  , 0.563793    ), Coef('Var'  , 1.32748     ), Coef('Var'  , 1.36187     ), Coef('Var'  , 2.3479      ), Coef('Var'  , 2.36575     ), Coef('Var'  , 2.45852     ), ], 
		[Coef('Var'  , 3.49849     ), Coef('Var'  , 2.33878     ), Coef('Var'  , 1.36215     ), Coef('Var'  , 0.626787    ), Coef('Var'  , 0.470807    ), Coef('Var'  , 1.31479     ), Coef('Var'  , 2.57938     ), Coef('Var'  , 3.01814     ), ], 
		[Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), ], ])
	
	
	
	etat1.bords   = {Bord('0'): etat7, Bord('1'): etat7, Bord('2'): etat7, Bord('3'): etat7, }
	etat1.permuts = {}
	etat1.interns = {Intern('_'): etat1, }
	etat1.subs    = {Sub('0'): etat2, Sub('1'): etat3, Sub('2'): etat4, Sub('3'): etat5, Sub('G', True): Etat.etatPoint, Sub('4'): etat6, }
	
	etat1.buildIntern()
	
	
	etat1.eqs = [
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
	
	
	etat1.prim.elems = [Figure(2, [Chem([Bord('0'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('0'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('0'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('0'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('1'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('1'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('1'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('1'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('2'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('2'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('2'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('2'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('3'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('3'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('3'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('3'), Sub('1'), Sub('1'), Bord('0'), ]), ])]
	etat1.grid.elems = [
		Figure(1, [Chem([Bord('1'), Bord('0'), ]), Chem([Bord('1'), Intern(''), ]), Chem([Bord('1'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('2'), Bord('0'), ]), Chem([Bord('2'), Intern(''), ]), Chem([Bord('2'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('0'), Bord('0'), ]), Chem([Bord('0'), Intern(''), ]), Chem([Bord('0'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('3'), Bord('0'), ]), Chem([Bord('3'), Intern(''), ]), Chem([Bord('3'), Bord('1'), ]), ]), ]
	
	
	etat1.space = [Chem([Bord('0'), Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('2'), Intern('0'), Intern('0'), ]), Chem([Bord('2'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('3'), Intern('0'), Intern('0'), ]), ]
	
	etat1.initMat[Chem([Sub('0')])] = FMat([
		[Coef('Const', 0.25        ), Coef('Var'  , 0.219073    ), Coef('Var'  , 0.188068    ), Coef('Var'  , 0.219073    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0930163   ), Coef('Var'  , 0.186317    ), Coef('Var'  , 0.343016    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0625784   ), Coef('Var'  , 0.125126    ), Coef('Var'  , 0.187578    ), Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0321855   ), Coef('Var'  , 0.0640112   ), Coef('Var'  , 0.0321855   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0313713   ), Coef('Var'  , 0.0626655   ), Coef('Var'  , 0.0313713   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0317066   ), Coef('Var'  , 0.063221    ), Coef('Var'  , 0.0317066   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.25        ), Coef('Var'  , 0.18707     ), Coef('Var'  , 0.124294    ), Coef('Var'  , 0.0620699   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.5         ), Coef('Var'  , 0.342999    ), Coef('Var'  , 0.186297    ), Coef('Var'  , 0.092999    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), ], ])
	etat1.initMat[Chem([Sub('1')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0317499   ), Coef('Var'  , 0.0632865   ), Coef('Var'  , 0.0317499   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0306357   ), Coef('Var'  , 0.0614646   ), Coef('Var'  , 0.0306357   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.187565    ), Coef('Var'  , 0.12511     ), Coef('Var'  , 0.0625649   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.344548    ), Coef('Var'  , 0.188841    ), Coef('Var'  , 0.0945478   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.218704    ), Coef('Var'  , 0.187459    ), Coef('Var'  , 0.218704    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.094058    ), Coef('Var'  , 0.188037    ), Coef('Var'  , 0.344058    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0620801   ), Coef('Var'  , 0.124307    ), Coef('Var'  , 0.18708     ), Coef('Const', 0.25        ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0306594   ), Coef('Var'  , 0.0614953   ), Coef('Var'  , 0.0306594   ), Coef('Const', 0           ), Coef('Const', 0           ), ], ])
	etat1.initMat[Chem([Sub('2')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0629241   ), Coef('Var'  , 0.125693    ), Coef('Var'  , 0.187924    ), Coef('Const', 0.25        ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0306378   ), Coef('Var'  , 0.0614672   ), Coef('Var'  , 0.0306378   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0314227   ), Coef('Var'  , 0.0627428   ), Coef('Var'  , 0.0314227   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0321699   ), Coef('Var'  , 0.0639921   ), Coef('Var'  , 0.0321699   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.187514    ), Coef('Var'  , 0.125033    ), Coef('Var'  , 0.0625139   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.3441      ), Coef('Var'  , 0.188089    ), Coef('Var'  , 0.0940997   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.218247    ), Coef('Var'  , 0.186704    ), Coef('Var'  , 0.218247    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0929853   ), Coef('Var'  , 0.18628     ), Coef('Var'  , 0.342985    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), ], ])
	etat1.initMat[Chem([Sub('3')])] = FMat([
		[Coef('Var'  , 0.125661    ), Coef('Var'  , 0.0628986   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.187899    ), ], 
		[Coef('Var'  , 0.186314    ), Coef('Var'  , 0.0930142   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.343014    ), ], 
		[Coef('Var'  , 0.187493    ), Coef('Var'  , 0.218721    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.218721    ), ], 
		[Coef('Var'  , 0.18886     ), Coef('Var'  , 0.344563    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0945627   ), ], 
		[Coef('Var'  , 0.125092    ), Coef('Var'  , 0.187562    ), Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0625621   ), ], 
		[Coef('Var'  , 0.0631693   ), Coef('Var'  , 0.0316648   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0316648   ), ], 
		[Coef('Var'  , 0.0618974   ), Coef('Var'  , 0.0309033   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0309033   ), ], 
		[Coef('Var'  , 0.0615127   ), Coef('Var'  , 0.0306736   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0306736   ), ], ])
	etat1.initMat[Chem([Sub('G')])] = FMat([
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], ])
	etat1.initMat[Chem([Sub('4')])] = FMat([
		[Coef('Var'  , 0.125693    ), Coef('Var'  , 0.094674    ), Coef('Var'  , 0.0632865   ), Coef('Var'  , 0.0946485   ), Coef('Var'  , 0.125661    ), Coef('Var'  , 0.156972    ), Coef('Var'  , 0.188068    ), Coef('Var'  , 0.156997    ), ], 
		[Coef('Var'  , 0.0614672   ), Coef('Var'  , 0.0612735   ), Coef('Var'  , 0.0614646   ), Coef('Var'  , 0.12365     ), Coef('Var'  , 0.186314    ), Coef('Var'  , 0.186031    ), Coef('Var'  , 0.186317    ), Coef('Var'  , 0.123654    ), ], 
		[Coef('Var'  , 0.0627428   ), Coef('Var'  , 0.0939876   ), Coef('Var'  , 0.12511     ), Coef('Var'  , 0.156286    ), Coef('Var'  , 0.187493    ), Coef('Var'  , 0.156299    ), Coef('Var'  , 0.125126    ), Coef('Var'  , 0.0940011   ), ], 
		[Coef('Var'  , 0.0639921   ), Coef('Var'  , 0.126718    ), Coef('Var'  , 0.188841    ), Coef('Var'  , 0.18911     ), Coef('Var'  , 0.18886     ), Coef('Var'  , 0.126748    ), Coef('Var'  , 0.0640112   ), Coef('Var'  , 0.0643553   ), ], 
		[Coef('Var'  , 0.125033    ), Coef('Var'  , 0.156218    ), Coef('Var'  , 0.187459    ), Coef('Var'  , 0.156266    ), Coef('Var'  , 0.125092    ), Coef('Var'  , 0.0939334   ), Coef('Var'  , 0.0626655   ), Coef('Var'  , 0.0938852   ), ], 
		[Coef('Var'  , 0.188089    ), Coef('Var'  , 0.188158    ), Coef('Var'  , 0.188037    ), Coef('Var'  , 0.125723    ), Coef('Var'  , 0.0631693   ), Coef('Var'  , 0.0633713   ), Coef('Var'  , 0.063221    ), Coef('Var'  , 0.125806    ), ], 
		[Coef('Var'  , 0.186704    ), Coef('Var'  , 0.155327    ), Coef('Var'  , 0.124307    ), Coef('Var'  , 0.0929835   ), Coef('Var'  , 0.0618974   ), Coef('Var'  , 0.0929732   ), Coef('Var'  , 0.124294    ), Coef('Var'  , 0.155317    ), ], 
		[Coef('Var'  , 0.18628     ), Coef('Var'  , 0.123645    ), Coef('Var'  , 0.0614953   ), Coef('Var'  , 0.061333    ), Coef('Var'  , 0.0615127   ), Coef('Var'  , 0.123673    ), Coef('Var'  , 0.186297    ), Coef('Var'  , 0.185984    ), ], ])
	
	
	
	etat2.bords   = {Bord('0'): etat7, Bord('1'): etat7, Bord('2'): etat7, Bord('3'): etat7, }
	etat2.permuts = {}
	etat2.interns = {Intern('_'): etat2, }
	etat2.subs    = {Sub('0'): etat1, Sub('1'): etat3, Sub('2'): etat4, Sub('3'): etat5, Sub('G', True): Etat.etatPoint, Sub('4'): etat6, }
	
	etat2.buildIntern()
	
	
	etat2.eqs = [
		(Chem([Bord('2'), Sub('1'), Permut('0'), ])	,	Chem([Sub('0'), Bord('0'), ])),
		(Chem([Bord('3'), Sub('0'), Permut('0'), ])	,	Chem([Sub('0'), Bord('3'), ])),
		(Chem([Bord('0'), Sub('0'), Permut('0'), ])	,	Chem([Sub('2'), Bord('2'), ])),
		(Chem([Bord('3'), Sub('1'), Permut('0'), ])	,	Chem([Sub('2'), Bord('3'), ])),
		(Chem([Bord('2'), Sub('0'), Permut('0'), ])	,	Chem([Sub('3'), Bord('2'), ])),
		(Chem([Bord('1'), Sub('1'), Permut('0'), ])	,	Chem([Sub('3'), Bord('3'), ])),
		(Chem([Bord('1'), Sub('0'), Permut('0'), ])	,	Chem([Sub('4'), Bord('2'), ])),
		(Chem([Bord('0'), Sub('1'), Permut('0'), ])	,	Chem([Sub('4'), Bord('3'), ])),
		(Chem([Sub('0'), Bord('0'), Bord('1'), ])	,	Chem([Sub('3'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('1'), Bord('1'), ])	,	Chem([Sub('1'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('2'), Bord('1'), ])	,	Chem([Sub('2'), Bord('3'), Bord('1'), ])),
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
	
	
	etat2.prim.elems = [Figure(2, [Chem([Bord('0'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('0'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('0'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('0'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('1'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('1'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('1'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('1'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('2'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('2'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('2'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('2'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('3'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('3'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('3'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('3'), Sub('1'), Sub('1'), Bord('0'), ]), ])]
	etat2.grid.elems = [
		Figure(1, [Chem([Bord('1'), Bord('0'), ]), Chem([Bord('1'), Intern(''), ]), Chem([Bord('1'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('2'), Bord('0'), ]), Chem([Bord('2'), Intern(''), ]), Chem([Bord('2'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('0'), Bord('0'), ]), Chem([Bord('0'), Intern(''), ]), Chem([Bord('0'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('3'), Bord('0'), ]), Chem([Bord('3'), Intern(''), ]), Chem([Bord('3'), Bord('1'), ]), ]), ]
	
	
	etat2.space = [Chem([Bord('0'), Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('2'), Intern('0'), Intern('0'), ]), Chem([Bord('2'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('3'), Intern('0'), Intern('0'), ]), ]
	
	etat2.initMat[Chem([Sub('0')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0619981   ), Coef('Var'  , 0.124165    ), Coef('Var'  , 0.186998    ), Coef('Const', 0.25        ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.031465    ), Coef('Var'  , 0.0628264   ), Coef('Var'  , 0.031465    ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0312737   ), Coef('Var'  , 0.0624957   ), Coef('Var'  , 0.0312737   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0309849   ), Coef('Var'  , 0.0620368   ), Coef('Var'  , 0.0309849   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.186883    ), Coef('Var'  , 0.123999    ), Coef('Var'  , 0.0618828   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.345881    ), Coef('Var'  , 0.191045    ), Coef('Var'  , 0.0958806   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.218432    ), Coef('Var'  , 0.186995    ), Coef('Var'  , 0.218432    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0930831   ), Coef('Var'  , 0.186437    ), Coef('Var'  , 0.343083    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), ], ])
	etat2.initMat[Chem([Sub('1')])] = FMat([
		[Coef('Var'  , 0.124165    ), Coef('Var'  , 0.0928405   ), Coef('Var'  , 0.0617817   ), Coef('Var'  , 0.0927973   ), Coef('Var'  , 0.124112    ), Coef('Var'  , 0.155066    ), Coef('Var'  , 0.186495    ), Coef('Var'  , 0.155109    ), ], 
		[Coef('Var'  , 0.0628264   ), Coef('Var'  , 0.0629217   ), Coef('Var'  , 0.0628162   ), Coef('Var'  , 0.125288    ), Coef('Var'  , 0.187662    ), Coef('Var'  , 0.187671    ), Coef('Var'  , 0.187672    ), Coef('Var'  , 0.125305    ), ], 
		[Coef('Var'  , 0.0624957   ), Coef('Var'  , 0.0936848   ), Coef('Var'  , 0.124856    ), Coef('Var'  , 0.155973    ), Coef('Var'  , 0.187234    ), Coef('Var'  , 0.155986    ), Coef('Var'  , 0.124873    ), Coef('Var'  , 0.0936983   ), ], 
		[Coef('Var'  , 0.0620368   ), Coef('Var'  , 0.124335    ), Coef('Var'  , 0.18687     ), Coef('Var'  , 0.186703    ), Coef('Var'  , 0.186873    ), Coef('Var'  , 0.124341    ), Coef('Var'  , 0.062041    ), Coef('Var'  , 0.0619733   ), ], 
		[Coef('Var'  , 0.123999    ), Coef('Var'  , 0.154979    ), Coef('Var'  , 0.186454    ), Coef('Var'  , 0.15505     ), Coef('Var'  , 0.124086    ), Coef('Var'  , 0.0926929   ), Coef('Var'  , 0.0616306   ), Coef('Var'  , 0.0926223   ), ], 
		[Coef('Var'  , 0.191045    ), Coef('Var'  , 0.191811    ), Coef('Var'  , 0.191106    ), Coef('Var'  , 0.129499    ), Coef('Var'  , 0.0662772   ), Coef('Var'  , 0.0670872   ), Coef('Var'  , 0.0662156   ), Coef('Var'  , 0.129399    ), ], 
		[Coef('Var'  , 0.186995    ), Coef('Var'  , 0.155635    ), Coef('Var'  , 0.124523    ), Coef('Var'  , 0.0932297   ), Coef('Var'  , 0.0621122   ), Coef('Var'  , 0.0932803   ), Coef('Var'  , 0.124585    ), Coef('Var'  , 0.155686    ), ], 
		[Coef('Var'  , 0.186437    ), Coef('Var'  , 0.123793    ), Coef('Var'  , 0.0615933   ), Coef('Var'  , 0.0614606   ), Coef('Var'  , 0.0616443   ), Coef('Var'  , 0.123875    ), Coef('Var'  , 0.186488    ), Coef('Var'  , 0.186208    ), ], ])
	etat2.initMat[Chem([Sub('2')])] = FMat([
		[Coef('Const', 0.25        ), Coef('Var'  , 0.218111    ), Coef('Var'  , 0.186495    ), Coef('Var'  , 0.218111    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0938396   ), Coef('Var'  , 0.187672    ), Coef('Var'  , 0.34384     ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0624245   ), Coef('Var'  , 0.124873    ), Coef('Var'  , 0.187425    ), Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0309884   ), Coef('Var'  , 0.062041    ), Coef('Var'  , 0.0309884   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0307395   ), Coef('Var'  , 0.0616306   ), Coef('Var'  , 0.0307395   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0335187   ), Coef('Var'  , 0.0662156   ), Coef('Var'  , 0.0335187   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.25        ), Coef('Var'  , 0.187254    ), Coef('Var'  , 0.124585    ), Coef('Var'  , 0.0622541   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.5         ), Coef('Var'  , 0.343124    ), Coef('Var'  , 0.186488    ), Coef('Var'  , 0.0931245   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), ], ])
	etat2.initMat[Chem([Sub('3')])] = FMat([
		[Coef('Const', 0           ), Coef('Var'  , 0.0308424   ), Coef('Var'  , 0.0617817   ), Coef('Var'  , 0.0308424   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0314567   ), Coef('Var'  , 0.0628162   ), Coef('Var'  , 0.0314567   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.25        ), Coef('Var'  , 0.187411    ), Coef('Var'  , 0.124856    ), Coef('Var'  , 0.062411    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.5         ), Coef('Var'  , 0.34335     ), Coef('Var'  , 0.18687     ), Coef('Var'  , 0.0933498   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0.25        ), Coef('Var'  , 0.218097    ), Coef('Var'  , 0.186454    ), Coef('Var'  , 0.218097    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0959302   ), Coef('Var'  , 0.191106    ), Coef('Var'  , 0.34593     ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0622036   ), Coef('Var'  , 0.124523    ), Coef('Var'  , 0.187204    ), Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0307097   ), Coef('Var'  , 0.0615933   ), Coef('Var'  , 0.0307097   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], ])
	etat2.initMat[Chem([Sub('G')])] = FMat([
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], ])
	etat2.initMat[Chem([Sub('4')])] = FMat([
		[Coef('Const', 0.25        ), Coef('Var'  , 0.186955    ), Coef('Var'  , 0.124112    ), Coef('Var'  , 0.0619549   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.5         ), Coef('Var'  , 0.343832    ), Coef('Var'  , 0.187662    ), Coef('Var'  , 0.0938316   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0.25        ), Coef('Var'  , 0.218562    ), Coef('Var'  , 0.187234    ), Coef('Var'  , 0.218562    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0933528   ), Coef('Var'  , 0.186873    ), Coef('Var'  , 0.343353    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0619533   ), Coef('Var'  , 0.124086    ), Coef('Var'  , 0.186953    ), Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0335685   ), Coef('Var'  , 0.0662772   ), Coef('Var'  , 0.0335685   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0310261   ), Coef('Var'  , 0.0621122   ), Coef('Var'  , 0.0310261   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0307509   ), Coef('Var'  , 0.0616443   ), Coef('Var'  , 0.0307509   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], ])
	
	
	
	etat3.bords   = {Bord('0'): etat7, Bord('1'): etat7, Bord('2'): etat7, Bord('3'): etat7, }
	etat3.permuts = {}
	etat3.interns = {Intern('_'): etat3, }
	etat3.subs    = {Sub('0'): etat1, Sub('1'): etat2, Sub('2'): etat4, Sub('3'): etat5, Sub('G', True): Etat.etatPoint, Sub('4'): etat6, }
	
	etat3.buildIntern()
	
	
	etat3.eqs = [
		(Chem([Bord('0'), Sub('0'), Permut('0'), ])	,	Chem([Sub('0'), Bord('1'), ])),
		(Chem([Bord('3'), Sub('1'), Permut('0'), ])	,	Chem([Sub('0'), Bord('2'), ])),
		(Chem([Bord('3'), Sub('0'), Permut('0'), ])	,	Chem([Sub('2'), Bord('0'), ])),
		(Chem([Bord('2'), Sub('1'), Permut('0'), ])	,	Chem([Sub('2'), Bord('1'), ])),
		(Chem([Bord('1'), Sub('0'), Permut('0'), ])	,	Chem([Sub('3'), Bord('0'), ])),
		(Chem([Bord('0'), Sub('1'), Permut('0'), ])	,	Chem([Sub('3'), Bord('1'), ])),
		(Chem([Bord('2'), Sub('0'), Permut('0'), ])	,	Chem([Sub('4'), Bord('0'), ])),
		(Chem([Bord('1'), Sub('1'), Permut('0'), ])	,	Chem([Sub('4'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('0'), Bord('1'), ])	,	Chem([Sub('3'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('2'), Bord('1'), ])	,	Chem([Sub('2'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('3'), Bord('1'), ])	,	Chem([Sub('1'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('0'), Bord('1'), ])	,	Chem([Sub('4'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('1'), Bord('1'), ])	,	Chem([Sub('3'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('3'), Bord('1'), ])	,	Chem([Sub('2'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('1'), Bord('1'), ])	,	Chem([Sub('4'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('3'), Bord('3'), Bord('1'), ])	,	Chem([Sub('4'), Bord('1'), Bord('1'), ])),
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
		[Coef('Var'  , 0.187294    ), Coef('Var'  , 0.218607    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.218607    ), ], 
		[Coef('Var'  , 0.185988    ), Coef('Var'  , 0.342811    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0928109   ), ], 
		[Coef('Var'  , 0.124463    ), Coef('Var'  , 0.187178    ), Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.062178    ), ], 
		[Coef('Var'  , 0.0614656   ), Coef('Var'  , 0.0306348   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0306348   ), ], 
		[Coef('Var'  , 0.0648306   ), Coef('Var'  , 0.0326998   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0326998   ), ], 
		[Coef('Var'  , 0.0628581   ), Coef('Var'  , 0.0314837   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0314837   ), ], 
		[Coef('Var'  , 0.124369    ), Coef('Var'  , 0.0621064   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.187106    ), ], 
		[Coef('Var'  , 0.18873     ), Coef('Var'  , 0.0944789   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.344479    ), ], ])
	etat3.initMat[Chem([Sub('1')])] = FMat([
		[Coef('Var'  , 0.124883    ), Coef('Var'  , 0.0936779   ), Coef('Var'  , 0.0624695   ), Coef('Var'  , 0.093677    ), Coef('Var'  , 0.124882    ), Coef('Var'  , 0.156035    ), Coef('Var'  , 0.187294    ), Coef('Var'  , 0.156036    ), ], 
		[Coef('Var'  , 0.0611923   ), Coef('Var'  , 0.0609515   ), Coef('Var'  , 0.0611915   ), Coef('Var'  , 0.123285    ), Coef('Var'  , 0.185987    ), Coef('Var'  , 0.185621    ), Coef('Var'  , 0.185988    ), Coef('Var'  , 0.123287    ), ], 
		[Coef('Var'  , 0.0619842   ), Coef('Var'  , 0.0930904   ), Coef('Var'  , 0.124423    ), Coef('Var'  , 0.155524    ), Coef('Var'  , 0.186903    ), Coef('Var'  , 0.155557    ), Coef('Var'  , 0.124463    ), Coef('Var'  , 0.0931229   ), ], 
		[Coef('Var'  , 0.0614572   ), Coef('Var'  , 0.123656    ), Coef('Var'  , 0.186333    ), Coef('Var'  , 0.186062    ), Coef('Var'  , 0.186341    ), Coef('Var'  , 0.123669    ), Coef('Var'  , 0.0614656   ), Coef('Var'  , 0.0612628   ), ], 
		[Coef('Var'  , 0.127147    ), Coef('Var'  , 0.15873     ), Coef('Var'  , 0.189496    ), Coef('Var'  , 0.158757    ), Coef('Var'  , 0.12718     ), Coef('Var'  , 0.096528    ), Coef('Var'  , 0.0648306   ), Coef('Var'  , 0.0965008   ), ], 
		[Coef('Var'  , 0.187741    ), Coef('Var'  , 0.187744    ), Coef('Var'  , 0.187698    ), Coef('Var'  , 0.125303    ), Coef('Var'  , 0.0628147   ), Coef('Var'  , 0.0629323   ), Coef('Var'  , 0.0628581   ), Coef('Var'  , 0.125373    ), ], 
		[Coef('Var'  , 0.186844    ), Coef('Var'  , 0.155525    ), Coef('Var'  , 0.124471    ), Coef('Var'  , 0.0931489   ), Coef('Var'  , 0.061997    ), Coef('Var'  , 0.0930663   ), Coef('Var'  , 0.124369    ), Coef('Var'  , 0.155442    ), ], 
		[Coef('Var'  , 0.188752    ), Coef('Var'  , 0.126626    ), Coef('Var'  , 0.0639168   ), Coef('Var'  , 0.0642418   ), Coef('Var'  , 0.0638952   ), Coef('Var'  , 0.126591    ), Coef('Var'  , 0.18873     ), Coef('Var'  , 0.188975    ), ], ])
	etat3.initMat[Chem([Sub('2')])] = FMat([
		[Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0624289   ), Coef('Var'  , 0.124883    ), Coef('Var'  , 0.187429    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0304761   ), Coef('Var'  , 0.0611923   ), Coef('Var'  , 0.0304761   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0309448   ), Coef('Var'  , 0.0619842   ), Coef('Var'  , 0.0309448   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.030628    ), Coef('Var'  , 0.0614572   ), Coef('Var'  , 0.030628    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.188801    ), Coef('Var'  , 0.127147    ), Coef('Var'  , 0.0638009   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.343889    ), Coef('Var'  , 0.187741    ), Coef('Var'  , 0.0938892   ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.218336    ), Coef('Var'  , 0.186844    ), Coef('Var'  , 0.218336    ), ], 
		[Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0944964   ), Coef('Var'  , 0.188752    ), Coef('Var'  , 0.344496    ), ], ])
	etat3.initMat[Chem([Sub('3')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.187428    ), Coef('Var'  , 0.124882    ), Coef('Var'  , 0.062428    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.34281     ), Coef('Var'  , 0.185987    ), Coef('Var'  , 0.09281     ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.218379    ), Coef('Var'  , 0.186903    ), Coef('Var'  , 0.218379    ), ], 
		[Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0930344   ), Coef('Var'  , 0.186341    ), Coef('Var'  , 0.343034    ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0638282   ), Coef('Var'  , 0.12718     ), Coef('Var'  , 0.188828    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0314486   ), Coef('Var'  , 0.0628147   ), Coef('Var'  , 0.0314486   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0309598   ), Coef('Var'  , 0.061997    ), Coef('Var'  , 0.0309598   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0321122   ), Coef('Var'  , 0.0638952   ), Coef('Var'  , 0.0321122   ), ], ])
	etat3.initMat[Chem([Sub('G')])] = FMat([
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], ])
	etat3.initMat[Chem([Sub('4')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.031249    ), Coef('Var'  , 0.0624695   ), Coef('Var'  , 0.031249    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0304754   ), Coef('Var'  , 0.0611915   ), Coef('Var'  , 0.0304754   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.187146    ), Coef('Var'  , 0.124423    ), Coef('Var'  , 0.0621456   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.343028    ), Coef('Var'  , 0.186333    ), Coef('Var'  , 0.0930278   ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.219929    ), Coef('Var'  , 0.189496    ), Coef('Var'  , 0.219929    ), ], 
		[Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0938544   ), Coef('Var'  , 0.187698    ), Coef('Var'  , 0.343854    ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0621891   ), Coef('Var'  , 0.124471    ), Coef('Var'  , 0.187189    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0321296   ), Coef('Var'  , 0.0639168   ), Coef('Var'  , 0.0321296   ), ], ])
	
	
	
	etat4.bords   = {Bord('0'): etat7, Bord('1'): etat7, Bord('2'): etat7, Bord('3'): etat7, }
	etat4.permuts = {}
	etat4.interns = {Intern('_'): etat4, }
	etat4.subs    = {Sub('0'): etat1, Sub('1'): etat2, Sub('2'): etat3, Sub('3'): etat5, Sub('G', True): Etat.etatPoint, Sub('4'): etat6, }
	
	etat4.buildIntern()
	
	
	etat4.eqs = [
		(Chem([Bord('0'), Sub('0'), Permut('0'), ])	,	Chem([Sub('0'), Bord('2'), ])),
		(Chem([Bord('3'), Sub('1'), Permut('0'), ])	,	Chem([Sub('0'), Bord('3'), ])),
		(Chem([Bord('2'), Sub('1'), Permut('0'), ])	,	Chem([Sub('1'), Bord('0'), ])),
		(Chem([Bord('3'), Sub('0'), Permut('0'), ])	,	Chem([Sub('1'), Bord('3'), ])),
		(Chem([Bord('1'), Sub('0'), Permut('0'), ])	,	Chem([Sub('2'), Bord('2'), ])),
		(Chem([Bord('0'), Sub('1'), Permut('0'), ])	,	Chem([Sub('2'), Bord('3'), ])),
		(Chem([Bord('1'), Sub('1'), Permut('0'), ])	,	Chem([Sub('4'), Bord('0'), ])),
		(Chem([Bord('2'), Sub('0'), Permut('0'), ])	,	Chem([Sub('4'), Bord('3'), ])),
		(Chem([Sub('0'), Bord('0'), Bord('1'), ])	,	Chem([Sub('3'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('1'), Bord('1'), ])	,	Chem([Sub('2'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('3'), Bord('1'), ])	,	Chem([Sub('1'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('0'), Bord('1'), ])	,	Chem([Sub('4'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('1'), Bord('1'), ])	,	Chem([Sub('3'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('0'), Bord('1'), ])	,	Chem([Sub('3'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('1'), Bord('1'), ])	,	Chem([Sub('4'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('3'), Bord('3'), Bord('1'), ])	,	Chem([Sub('4'), Bord('1'), Bord('1'), ])),
		(Chem([Bord('0'), Bord('1'), ])	,	Chem([Bord('1'), Bord('0'), ])),
		(Chem([Bord('1'), Bord('1'), ])	,	Chem([Bord('2'), Bord('0'), ])),
		(Chem([Bord('2'), Bord('1'), ])	,	Chem([Bord('3'), Bord('0'), ])),
		(Chem([Bord('3'), Bord('1'), ])	,	Chem([Bord('0'), Bord('0'), ])),
		]
	
	
	etat4.prim.elems = [Figure(2, [Chem([Bord('0'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('0'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('0'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('0'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('1'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('1'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('1'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('1'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('2'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('2'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('2'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('2'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('3'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('3'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('3'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('3'), Sub('1'), Sub('1'), Bord('0'), ]), ])]
	etat4.grid.elems = [
		Figure(1, [Chem([Bord('1'), Bord('0'), ]), Chem([Bord('1'), Intern(''), ]), Chem([Bord('1'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('2'), Bord('0'), ]), Chem([Bord('2'), Intern(''), ]), Chem([Bord('2'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('0'), Bord('0'), ]), Chem([Bord('0'), Intern(''), ]), Chem([Bord('0'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('3'), Bord('0'), ]), Chem([Bord('3'), Intern(''), ]), Chem([Bord('3'), Bord('1'), ]), ]), ]
	
	
	etat4.space = [Chem([Bord('0'), Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('2'), Intern('0'), Intern('0'), ]), Chem([Bord('2'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('3'), Intern('0'), Intern('0'), ]), ]
	
	etat4.initMat[Chem([Sub('0')])] = FMat([
		[Coef('Const', 0.25        ), Coef('Var'  , 0.219114    ), Coef('Var'  , 0.188139    ), Coef('Var'  , 0.219114    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0933445   ), Coef('Var'  , 0.186876    ), Coef('Var'  , 0.343344    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0626487   ), Coef('Var'  , 0.125237    ), Coef('Var'  , 0.187649    ), Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0319138   ), Coef('Var'  , 0.0635423   ), Coef('Var'  , 0.0319138   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0320581   ), Coef('Var'  , 0.0637914   ), Coef('Var'  , 0.0320581   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0303123   ), Coef('Var'  , 0.0609253   ), Coef('Var'  , 0.0303123   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.25        ), Coef('Var'  , 0.187323    ), Coef('Var'  , 0.124727    ), Coef('Var'  , 0.0623233   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.5         ), Coef('Var'  , 0.343285    ), Coef('Var'  , 0.186763    ), Coef('Var'  , 0.093285    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), ], ])
	etat4.initMat[Chem([Sub('1')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0629464   ), Coef('Var'  , 0.12574     ), Coef('Var'  , 0.187946    ), Coef('Const', 0.25        ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0310738   ), Coef('Var'  , 0.0621594   ), Coef('Var'  , 0.0310738   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0314085   ), Coef('Var'  , 0.0627485   ), Coef('Var'  , 0.0314085   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0319114   ), Coef('Var'  , 0.0635396   ), Coef('Var'  , 0.0319114   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.188222    ), Coef('Var'  , 0.126185    ), Coef('Var'  , 0.0632216   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.342698    ), Coef('Var'  , 0.185784    ), Coef('Var'  , 0.0926979   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.218514    ), Coef('Var'  , 0.187154    ), Coef('Var'  , 0.218514    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0932263   ), Coef('Var'  , 0.18669     ), Coef('Var'  , 0.343226    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), ], ])
	etat4.initMat[Chem([Sub('2')])] = FMat([
		[Coef('Const', 0.25        ), Coef('Var'  , 0.187974    ), Coef('Var'  , 0.125775    ), Coef('Var'  , 0.0629742   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.5         ), Coef('Var'  , 0.343327    ), Coef('Var'  , 0.186854    ), Coef('Var'  , 0.0933267   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0.25        ), Coef('Var'  , 0.218849    ), Coef('Var'  , 0.187674    ), Coef('Var'  , 0.218849    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0941718   ), Coef('Var'  , 0.188243    ), Coef('Var'  , 0.344172    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0632064   ), Coef('Var'  , 0.126166    ), Coef('Var'  , 0.188206    ), Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0302734   ), Coef('Var'  , 0.0608773   ), Coef('Var'  , 0.0302734   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0312182   ), Coef('Var'  , 0.0624058   ), Coef('Var'  , 0.0312182   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0309807   ), Coef('Var'  , 0.0620046   ), Coef('Var'  , 0.0309807   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], ])
	etat4.initMat[Chem([Sub('3')])] = FMat([
		[Coef('Var'  , 0.063376    ), Coef('Var'  , 0.0947803   ), Coef('Var'  , 0.125775    ), Coef('Var'  , 0.157089    ), Coef('Var'  , 0.188139    ), Coef('Var'  , 0.157061    ), Coef('Var'  , 0.12574     ), Coef('Var'  , 0.0947525   ), ], 
		[Coef('Var'  , 0.0621376   ), Coef('Var'  , 0.124383    ), Coef('Var'  , 0.186854    ), Coef('Var'  , 0.186671    ), Coef('Var'  , 0.186876    ), Coef('Var'  , 0.124418    ), Coef('Var'  , 0.0621594   ), Coef('Var'  , 0.06213     ), ], 
		[Coef('Var'  , 0.125186    ), Coef('Var'  , 0.156457    ), Coef('Var'  , 0.187674    ), Coef('Var'  , 0.156497    ), Coef('Var'  , 0.125237    ), Coef('Var'  , 0.0940573   ), Coef('Var'  , 0.0627485   ), Coef('Var'  , 0.0940164   ), ], 
		[Coef('Var'  , 0.188241    ), Coef('Var'  , 0.188342    ), Coef('Var'  , 0.188243    ), Coef('Var'  , 0.126086    ), Coef('Var'  , 0.0635423   ), Coef('Var'  , 0.0638252   ), Coef('Var'  , 0.0635396   ), Coef('Var'  , 0.126082    ), ], 
		[Coef('Var'  , 0.188559    ), Coef('Var'  , 0.157577    ), Coef('Var'  , 0.126166    ), Coef('Var'  , 0.0952645   ), Coef('Var'  , 0.0637914   ), Coef('Var'  , 0.0952797   ), Coef('Var'  , 0.126185    ), Coef('Var'  , 0.157592    ), ], 
		[Coef('Var'  , 0.185736    ), Coef('Var'  , 0.122932    ), Coef('Var'  , 0.0608773   ), Coef('Var'  , 0.0605857   ), Coef('Var'  , 0.0609253   ), Coef('Var'  , 0.12301     ), Coef('Var'  , 0.185784    ), Coef('Var'  , 0.185357    ), ], 
		[Coef('Var'  , 0.124832    ), Coef('Var'  , 0.093627    ), Coef('Var'  , 0.0624058   ), Coef('Var'  , 0.0935415   ), Coef('Var'  , 0.124727    ), Coef('Var'  , 0.155837    ), Coef('Var'  , 0.187154    ), Coef('Var'  , 0.155923    ), ], 
		[Coef('Var'  , 0.0619317   ), Coef('Var'  , 0.0619023   ), Coef('Var'  , 0.0620046   ), Coef('Var'  , 0.124266    ), Coef('Var'  , 0.186763    ), Coef('Var'  , 0.186511    ), Coef('Var'  , 0.18669     ), Coef('Var'  , 0.124148    ), ], ])
	etat4.initMat[Chem([Sub('G')])] = FMat([
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], ])
	etat4.initMat[Chem([Sub('4')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0318061   ), Coef('Var'  , 0.063376    ), Coef('Var'  , 0.0318061   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0310562   ), Coef('Var'  , 0.0621376   ), Coef('Var'  , 0.0310562   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.187608    ), Coef('Var'  , 0.125186    ), Coef('Var'  , 0.0626079   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.34417     ), Coef('Var'  , 0.188241    ), Coef('Var'  , 0.0941703   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.21937     ), Coef('Var'  , 0.188559    ), Coef('Var'  , 0.21937     ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.092659    ), Coef('Var'  , 0.185736    ), Coef('Var'  , 0.342659    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0624087   ), Coef('Var'  , 0.124832    ), Coef('Var'  , 0.187409    ), Coef('Const', 0.25        ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0309217   ), Coef('Var'  , 0.0619317   ), Coef('Var'  , 0.0309217   ), Coef('Const', 0           ), Coef('Const', 0           ), ], ])
	
	
	
	etat5.bords   = {Bord('0'): etat7, Bord('1'): etat7, Bord('2'): etat7, Bord('3'): etat7, }
	etat5.permuts = {}
	etat5.interns = {Intern('_'): etat5, }
	etat5.subs    = {Sub('0'): etat1, Sub('1'): etat2, Sub('2'): etat3, Sub('3'): etat4, Sub('G', True): Etat.etatPoint, Sub('4'): etat6, }
	
	etat5.buildIntern()
	
	
	etat5.eqs = [
		(Chem([Bord('2'), Sub('0'), Permut('0'), ])	,	Chem([Sub('0'), Bord('0'), ])),
		(Chem([Bord('1'), Sub('1'), Permut('0'), ])	,	Chem([Sub('0'), Bord('1'), ])),
		(Chem([Bord('3'), Sub('0'), Permut('0'), ])	,	Chem([Sub('1'), Bord('1'), ])),
		(Chem([Bord('2'), Sub('1'), Permut('0'), ])	,	Chem([Sub('1'), Bord('2'), ])),
		(Chem([Bord('1'), Sub('0'), Permut('0'), ])	,	Chem([Sub('2'), Bord('0'), ])),
		(Chem([Bord('0'), Sub('1'), Permut('0'), ])	,	Chem([Sub('2'), Bord('1'), ])),
		(Chem([Bord('0'), Sub('0'), Permut('0'), ])	,	Chem([Sub('4'), Bord('1'), ])),
		(Chem([Bord('3'), Sub('1'), Permut('0'), ])	,	Chem([Sub('4'), Bord('2'), ])),
		(Chem([Sub('0'), Bord('1'), Bord('1'), ])	,	Chem([Sub('2'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('2'), Bord('1'), ])	,	Chem([Sub('3'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('3'), Bord('1'), ])	,	Chem([Sub('1'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('0'), Bord('1'), ])	,	Chem([Sub('4'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('3'), Bord('1'), ])	,	Chem([Sub('3'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('1'), Bord('1'), ])	,	Chem([Sub('4'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('2'), Bord('1'), ])	,	Chem([Sub('3'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('3'), Bord('1'), Bord('1'), ])	,	Chem([Sub('4'), Bord('3'), Bord('1'), ])),
		(Chem([Bord('0'), Bord('1'), ])	,	Chem([Bord('1'), Bord('0'), ])),
		(Chem([Bord('1'), Bord('1'), ])	,	Chem([Bord('2'), Bord('0'), ])),
		(Chem([Bord('2'), Bord('1'), ])	,	Chem([Bord('3'), Bord('0'), ])),
		(Chem([Bord('3'), Bord('1'), ])	,	Chem([Bord('0'), Bord('0'), ])),
		]
	
	
	etat5.prim.elems = [Figure(2, [Chem([Bord('0'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('0'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('0'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('0'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('1'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('1'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('1'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('1'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('2'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('2'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('2'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('2'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('3'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('3'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('3'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('3'), Sub('1'), Sub('1'), Bord('0'), ]), ])]
	etat5.grid.elems = [
		Figure(1, [Chem([Bord('1'), Bord('0'), ]), Chem([Bord('1'), Intern(''), ]), Chem([Bord('1'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('2'), Bord('0'), ]), Chem([Bord('2'), Intern(''), ]), Chem([Bord('2'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('0'), Bord('0'), ]), Chem([Bord('0'), Intern(''), ]), Chem([Bord('0'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('3'), Bord('0'), ]), Chem([Bord('3'), Intern(''), ]), Chem([Bord('3'), Bord('1'), ]), ]), ]
	
	
	etat5.space = [Chem([Bord('0'), Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('2'), Intern('0'), Intern('0'), ]), Chem([Bord('2'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('3'), Intern('0'), Intern('0'), ]), ]
	
	etat5.initMat[Chem([Sub('0')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0304312   ), Coef('Var'  , 0.0611306   ), Coef('Var'  , 0.0304312   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0331705   ), Coef('Var'  , 0.0656345   ), Coef('Var'  , 0.0331705   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.186593    ), Coef('Var'  , 0.123503    ), Coef('Var'  , 0.0615928   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.343458    ), Coef('Var'  , 0.187061    ), Coef('Var'  , 0.093458    ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.217113    ), Coef('Var'  , 0.184819    ), Coef('Var'  , 0.217113    ), ], 
		[Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0941883   ), Coef('Var'  , 0.188236    ), Coef('Var'  , 0.344188    ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0627946   ), Coef('Var'  , 0.125491    ), Coef('Var'  , 0.187795    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0322519   ), Coef('Var'  , 0.0641249   ), Coef('Var'  , 0.0322519   ), ], ])
	etat5.initMat[Chem([Sub('1')])] = FMat([
		[Coef('Var'  , 0.123607    ), Coef('Var'  , 0.186662    ), Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0616623   ), ], 
		[Coef('Var'  , 0.0655991   ), Coef('Var'  , 0.0331419   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0331419   ), ], 
		[Coef('Var'  , 0.0610808   ), Coef('Var'  , 0.0304058   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0304058   ), ], 
		[Coef('Var'  , 0.0622194   ), Coef('Var'  , 0.0310865   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0310865   ), ], 
		[Coef('Var'  , 0.122395    ), Coef('Var'  , 0.0609242   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.185924    ), ], 
		[Coef('Var'  , 0.188205    ), Coef('Var'  , 0.0941635   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.344164    ), ], 
		[Coef('Var'  , 0.18797     ), Coef('Var'  , 0.219027    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.219027    ), ], 
		[Coef('Var'  , 0.188923    ), Coef('Var'  , 0.344588    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0945885   ), ], ])
	etat5.initMat[Chem([Sub('2')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.186593    ), Coef('Var'  , 0.123522    ), Coef('Var'  , 0.0615935   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.345571    ), Coef('Var'  , 0.190512    ), Coef('Var'  , 0.0955711   ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.21776     ), Coef('Var'  , 0.185901    ), Coef('Var'  , 0.21776     ), ], 
		[Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0935312   ), Coef('Var'  , 0.187151    ), Coef('Var'  , 0.343531    ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0608692   ), Coef('Var'  , 0.122327    ), Coef('Var'  , 0.185869    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0317833   ), Coef('Var'  , 0.0633531   ), Coef('Var'  , 0.0317833   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.031593    ), Coef('Var'  , 0.0630512   ), Coef('Var'  , 0.031593    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0322985   ), Coef('Var'  , 0.0641825   ), Coef('Var'  , 0.0322985   ), ], ])
	etat5.initMat[Chem([Sub('3')])] = FMat([
		[Coef('Var'  , 0.0611306   ), Coef('Var'  , 0.0920247   ), Coef('Var'  , 0.123522    ), Coef('Var'  , 0.154418    ), Coef('Var'  , 0.185999    ), Coef('Var'  , 0.154487    ), Coef('Var'  , 0.123607    ), Coef('Var'  , 0.0920935   ), ], 
		[Coef('Var'  , 0.0656345   ), Coef('Var'  , 0.128742    ), Coef('Var'  , 0.190512    ), Coef('Var'  , 0.191114    ), Coef('Var'  , 0.190476    ), Coef('Var'  , 0.128685    ), Coef('Var'  , 0.0655991   ), Coef('Var'  , 0.0663124   ), ], 
		[Coef('Var'  , 0.123503    ), Coef('Var'  , 0.154353    ), Coef('Var'  , 0.185901    ), Coef('Var'  , 0.154333    ), Coef('Var'  , 0.123478    ), Coef('Var'  , 0.0919787   ), Coef('Var'  , 0.0610808   ), Coef('Var'  , 0.0919986   ), ], 
		[Coef('Var'  , 0.187061    ), Coef('Var'  , 0.186989    ), Coef('Var'  , 0.187151    ), Coef('Var'  , 0.12469     ), Coef('Var'  , 0.0623093   ), Coef('Var'  , 0.0622455   ), Coef('Var'  , 0.0622194   ), Coef('Var'  , 0.124544    ), ], 
		[Coef('Var'  , 0.184819    ), Coef('Var'  , 0.152982    ), Coef('Var'  , 0.122327    ), Coef('Var'  , 0.0905503   ), Coef('Var'  , 0.0599039   ), Coef('Var'  , 0.0906053   ), Coef('Var'  , 0.122395    ), Coef('Var'  , 0.153037    ), ], 
		[Coef('Var'  , 0.188236    ), Coef('Var'  , 0.125972    ), Coef('Var'  , 0.0633531   ), Coef('Var'  , 0.0635416   ), Coef('Var'  , 0.0633222   ), Coef('Var'  , 0.125922    ), Coef('Var'  , 0.188205    ), Coef('Var'  , 0.188352    ), ], 
		[Coef('Var'  , 0.125491    ), Coef('Var'  , 0.0943876   ), Coef('Var'  , 0.0630512   ), Coef('Var'  , 0.0944194   ), Coef('Var'  , 0.125531    ), Coef('Var'  , 0.156854    ), Coef('Var'  , 0.18797     ), Coef('Var'  , 0.156822    ), ], 
		[Coef('Var'  , 0.0641249   ), Coef('Var'  , 0.0645504   ), Coef('Var'  , 0.0641825   ), Coef('Var'  , 0.126934    ), Coef('Var'  , 0.188981    ), Coef('Var'  , 0.189224    ), Coef('Var'  , 0.188923    ), Coef('Var'  , 0.12684     ), ], ])
	etat5.initMat[Chem([Sub('G')])] = FMat([
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], ])
	etat5.initMat[Chem([Sub('4')])] = FMat([
		[Coef('Var'  , 0.185999    ), Coef('Var'  , 0.217824    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.217824    ), ], 
		[Coef('Var'  , 0.190476    ), Coef('Var'  , 0.345543    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0955426   ), ], 
		[Coef('Var'  , 0.123478    ), Coef('Var'  , 0.186573    ), Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0615729   ), ], 
		[Coef('Var'  , 0.0623093   ), Coef('Var'  , 0.0311591   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0311591   ), ], 
		[Coef('Var'  , 0.0599039   ), Coef('Var'  , 0.0296811   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0296811   ), ], 
		[Coef('Var'  , 0.0633222   ), Coef('Var'  , 0.0317582   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0317582   ), ], 
		[Coef('Var'  , 0.125531    ), Coef('Var'  , 0.0628264   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.187826    ), ], 
		[Coef('Var'  , 0.188981    ), Coef('Var'  , 0.0946352   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.344635    ), ], ])
	
	
	
	etat6.bords   = {Bord('0'): etat7, Bord('1'): etat7, Bord('2'): etat7, Bord('3'): etat7, }
	etat6.permuts = {}
	etat6.interns = {Intern('_'): etat6, }
	etat6.subs    = {Sub('0'): etat1, Sub('1'): etat2, Sub('2'): etat3, Sub('3'): etat4, Sub('G', True): Etat.etatPoint, Sub('4'): etat5, }
	
	etat6.buildIntern()
	
	
	etat6.eqs = [
		(Chem([Bord('3'), Sub('0'), Permut('0'), ])	,	Chem([Sub('1'), Bord('0'), ])),
		(Chem([Bord('2'), Sub('1'), Permut('0'), ])	,	Chem([Sub('1'), Bord('1'), ])),
		(Chem([Bord('1'), Sub('0'), Permut('0'), ])	,	Chem([Sub('2'), Bord('1'), ])),
		(Chem([Bord('0'), Sub('1'), Permut('0'), ])	,	Chem([Sub('2'), Bord('2'), ])),
		(Chem([Bord('0'), Sub('0'), Permut('0'), ])	,	Chem([Sub('3'), Bord('1'), ])),
		(Chem([Bord('3'), Sub('1'), Permut('0'), ])	,	Chem([Sub('3'), Bord('2'), ])),
		(Chem([Bord('1'), Sub('1'), Permut('0'), ])	,	Chem([Sub('4'), Bord('0'), ])),
		(Chem([Bord('2'), Sub('0'), Permut('0'), ])	,	Chem([Sub('4'), Bord('3'), ])),
		(Chem([Sub('0'), Bord('0'), Bord('1'), ])	,	Chem([Sub('4'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('1'), Bord('1'), ])	,	Chem([Sub('2'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('2'), Bord('1'), ])	,	Chem([Sub('3'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('3'), Bord('1'), ])	,	Chem([Sub('1'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('1'), Bord('1'), ])	,	Chem([Sub('4'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('3'), Bord('1'), ])	,	Chem([Sub('3'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('0'), Bord('1'), ])	,	Chem([Sub('4'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('2'), Bord('1'), ])	,	Chem([Sub('3'), Bord('0'), Bord('1'), ])),
		(Chem([Bord('0'), Bord('1'), ])	,	Chem([Bord('1'), Bord('0'), ])),
		(Chem([Bord('1'), Bord('1'), ])	,	Chem([Bord('2'), Bord('0'), ])),
		(Chem([Bord('2'), Bord('1'), ])	,	Chem([Bord('3'), Bord('0'), ])),
		(Chem([Bord('3'), Bord('1'), ])	,	Chem([Bord('0'), Bord('0'), ])),
		]
	
	
	etat6.prim.elems = [Figure(2, [Chem([Bord('0'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('0'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('0'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('0'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('1'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('1'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('1'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('1'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('2'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('2'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('2'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('2'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('3'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('3'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('3'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('3'), Sub('1'), Sub('1'), Bord('0'), ]), ])]
	etat6.grid.elems = [
		Figure(1, [Chem([Bord('1'), Bord('0'), ]), Chem([Bord('1'), Intern(''), ]), Chem([Bord('1'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('2'), Bord('0'), ]), Chem([Bord('2'), Intern(''), ]), Chem([Bord('2'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('0'), Bord('0'), ]), Chem([Bord('0'), Intern(''), ]), Chem([Bord('0'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('3'), Bord('0'), ]), Chem([Bord('3'), Intern(''), ]), Chem([Bord('3'), Bord('1'), ]), ]), ]
	
	
	etat6.space = [Chem([Bord('0'), Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('2'), Intern('0'), Intern('0'), ]), Chem([Bord('2'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('3'), Intern('0'), Intern('0'), ]), ]
	
	etat6.initMat[Chem([Sub('0')])] = FMat([
		[Coef('Var'  , 0.124643    ), Coef('Var'  , 0.0934347   ), Coef('Var'  , 0.0623044   ), Coef('Var'  , 0.0934838   ), Coef('Var'  , 0.124704    ), Coef('Var'  , 0.155772    ), Coef('Var'  , 0.187043    ), Coef('Var'  , 0.155723    ), ], 
		[Coef('Var'  , 0.0634624   ), Coef('Var'  , 0.0636515   ), Coef('Var'  , 0.0633752   ), Coef('Var'  , 0.125941    ), Coef('Var'  , 0.188202    ), Coef('Var'  , 0.188371    ), Coef('Var'  , 0.188289    ), Coef('Var'  , 0.126082    ), ], 
		[Coef('Var'  , 0.0630432   ), Coef('Var'  , 0.0943609   ), Coef('Var'  , 0.125419    ), Coef('Var'  , 0.156656    ), Coef('Var'  , 0.18779     ), Coef('Var'  , 0.156652    ), Coef('Var'  , 0.125414    ), Coef('Var'  , 0.0943565   ), ], 
		[Coef('Var'  , 0.0630865   ), Coef('Var'  , 0.12561     ), Coef('Var'  , 0.187929    ), Coef('Var'  , 0.188012    ), Coef('Var'  , 0.187966    ), Coef('Var'  , 0.125669    ), Coef('Var'  , 0.0631235   ), Coef('Var'  , 0.063267    ), ], 
		[Coef('Var'  , 0.124567    ), Coef('Var'  , 0.155673    ), Coef('Var'  , 0.187006    ), Coef('Var'  , 0.15568     ), Coef('Var'  , 0.124576    ), Coef('Var'  , 0.0932864   ), Coef('Var'  , 0.0621377   ), Coef('Var'  , 0.0932795   ), ], 
		[Coef('Var'  , 0.187863    ), Coef('Var'  , 0.187937    ), Coef('Var'  , 0.18791     ), Coef('Var'  , 0.125607    ), Coef('Var'  , 0.0630725   ), Coef('Var'  , 0.0631997   ), Coef('Var'  , 0.0630253   ), Coef('Var'  , 0.12553     ), ], 
		[Coef('Var'  , 0.187564    ), Coef('Var'  , 0.156345    ), Coef('Var'  , 0.125123    ), Coef('Var'  , 0.0939658   ), Coef('Var'  , 0.0627124   ), Coef('Var'  , 0.09399     ), Coef('Var'  , 0.125153    ), Coef('Var'  , 0.15637     ), ], 
		[Coef('Var'  , 0.185771    ), Coef('Var'  , 0.122988    ), Coef('Var'  , 0.0609331   ), Coef('Var'  , 0.0606554   ), Coef('Var'  , 0.0609772   ), Coef('Var'  , 0.123059    ), Coef('Var'  , 0.185815    ), Coef('Var'  , 0.185392    ), ], ])
	etat6.initMat[Chem([Sub('1')])] = FMat([
		[Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0622772   ), Coef('Var'  , 0.124643    ), Coef('Var'  , 0.187277    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.031861    ), Coef('Var'  , 0.0634624   ), Coef('Var'  , 0.031861    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0316055   ), Coef('Var'  , 0.0630432   ), Coef('Var'  , 0.0316055   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0316185   ), Coef('Var'  , 0.0630865   ), Coef('Var'  , 0.0316185   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.187236    ), Coef('Var'  , 0.124567    ), Coef('Var'  , 0.0622364   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.343949    ), Coef('Var'  , 0.187863    ), Coef('Var'  , 0.0939495   ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.218774    ), Coef('Var'  , 0.187564    ), Coef('Var'  , 0.218774    ), ], 
		[Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0926783   ), Coef('Var'  , 0.185771    ), Coef('Var'  , 0.342678    ), ], ])
	etat6.initMat[Chem([Sub('2')])] = FMat([
		[Coef('Var'  , 0.124704    ), Coef('Var'  , 0.0623263   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.187326    ), ], 
		[Coef('Var'  , 0.188202    ), Coef('Var'  , 0.09415     ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.34415     ), ], 
		[Coef('Var'  , 0.18779     ), Coef('Var'  , 0.218901    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.218901    ), ], 
		[Coef('Var'  , 0.187966    ), Coef('Var'  , 0.344021    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0940207   ), ], 
		[Coef('Var'  , 0.124576    ), Coef('Var'  , 0.187243    ), Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0622433   ), ], 
		[Coef('Var'  , 0.0630725   ), Coef('Var'  , 0.031619    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.031619    ), ], 
		[Coef('Var'  , 0.0627124   ), Coef('Var'  , 0.0313941   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0313941   ), ], 
		[Coef('Var'  , 0.0609772   ), Coef('Var'  , 0.0303455   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0303455   ), ], ])
	etat6.initMat[Chem([Sub('3')])] = FMat([
		[Coef('Var'  , 0.187043    ), Coef('Var'  , 0.218446    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.218446    ), ], 
		[Coef('Var'  , 0.188289    ), Coef('Var'  , 0.344221    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.094221    ), ], 
		[Coef('Var'  , 0.125414    ), Coef('Var'  , 0.187751    ), Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.062751    ), ], 
		[Coef('Var'  , 0.0631235   ), Coef('Var'  , 0.0316485   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0316485   ), ], 
		[Coef('Var'  , 0.0621377   ), Coef('Var'  , 0.0310431   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0310431   ), ], 
		[Coef('Var'  , 0.0630253   ), Coef('Var'  , 0.0315807   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0315807   ), ], 
		[Coef('Var'  , 0.125153    ), Coef('Var'  , 0.0625959   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.187596    ), ], 
		[Coef('Var'  , 0.185815    ), Coef('Var'  , 0.092714    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.342714    ), ], ])
	etat6.initMat[Chem([Sub('G')])] = FMat([
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], ])
	etat6.initMat[Chem([Sub('4')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0311575   ), Coef('Var'  , 0.0623044   ), Coef('Var'  , 0.0311575   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0317905   ), Coef('Var'  , 0.0633752   ), Coef('Var'  , 0.0317905   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.187755    ), Coef('Var'  , 0.125419    ), Coef('Var'  , 0.0627554   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.343991    ), Coef('Var'  , 0.187929    ), Coef('Var'  , 0.0939911   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.218436    ), Coef('Var'  , 0.187006    ), Coef('Var'  , 0.218436    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0939876   ), Coef('Var'  , 0.18791     ), Coef('Var'  , 0.343988    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0625718   ), Coef('Var'  , 0.125123    ), Coef('Var'  , 0.187572    ), Coef('Const', 0.25        ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0303098   ), Coef('Var'  , 0.0609331   ), Coef('Var'  , 0.0303098   ), Coef('Const', 0           ), Coef('Const', 0           ), ], ])
	
	
	
	etat7.bords   = {Bord('0'): etat8, Bord('1'): etat8, }
	etat7.permuts = {Permut('0'): etat7, }
	etat7.interns = {Intern('_'): etat7, }
	etat7.subs    = {Sub('0'): etat7, Sub('1'): etat7, Sub('G', True): Etat.etatPoint, }
	
	etat7.buildIntern()
	etat7.fm_[Permut('0')] = PMat(3, [2, 1, 0, ])
	
	
	etat7.eqs = [
		(Chem([Permut('0'), Bord('0'), ])	,	Chem([Bord('1')])),
		(Chem([Permut('0'), Bord('1'), ])	,	Chem([Bord('0')])),
		(Chem([Permut('0'), Intern(''), ])	,	Chem([Intern('')])),
		(Chem([Permut('0'), Sub('0'), ])	,	Chem([Sub('1'), Permut('0'), ])),
		(Chem([Permut('0'), Sub('1'), ])	,	Chem([Sub('0'), Permut('0'), ])),
		]
	
	
	etat7.prim.elems = [Figure(1, [Chem([Bord('0')]), Chem([Bord('1')]), ])]
	etat7.grid.elems = [Figure(1, [Chem([Bord('0')]), Chem([Intern('')]), Chem([Bord('1')]), ])]
	
	
	etat7.space = [Chem([Bord('0'), Intern('0'), Intern('0'), ]), Chem([Intern('0'), Intern('0'), ]), Chem([Bord('1'), Intern('0'), Intern('0'), ]), ]
	
	etat7.initMat[Chem([Sub('0')])] = FMat([
		[Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), ], ])
	etat7.initMat[Chem([Sub('1')])] = FMat([
		[Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), ], ])
	etat7.initMat[Chem([Sub('G')])] = FMat([
		[Coef('Const', 0           )], 
		[Coef('Const', 1           )], 
		[Coef('Const', 0           )], ])
	
	
	
	etat8.bords   = {}
	etat8.permuts = {}
	etat8.interns = {Intern('_'): etat8, }
	etat8.subs    = {Sub('0'): etat8, Sub('G', True): Etat.etatPoint, }
	
	etat8.buildIntern()
	
	
	etat8.eqs = [
		]
	
	
	etat8.prim.elems = []
	etat8.grid.elems = []
	
	
	etat8.space = [Chem([Intern('0'), Intern('0'), ])]
	
	etat8.initMat[Chem([Sub('0')])] = FMat([[Coef('Var'  , 1           )]])
	etat8.initMat[Chem([Sub('G')])] = FMat([[Coef('Const', 1           )]])
	
	
	
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
