# -*- coding: utf-8 -*-

# Automatically generated, from file : frac_cube.py, function : modele()

from __future__ import division
import sys
if './../../../../../../python' not in sys.path:
	sys.path.append('./../../../../../../python')
from etat import *

def modele():
	
	etat0 = EtatInit()
	etat1 = Etat('Cell_0',0)
	etat2 = Etat('B2',1)
	etat3 = Etat('s',1)
	
	
	etat0.subs   = {Sub('0'): etat1, Sub('1'): etat1, Sub('2'): etat1, Sub('3'): etat1, Sub('4'): etat1, Sub('5'): etat1, }
	
	etat0.eqs = [
		(Chem([Sub('0'), Bord('0'), Permut('0'), ])	,	Chem([Sub('4'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('1'), Permut('0'), ])	,	Chem([Sub('2'), Bord('3'), ])),
		(Chem([Sub('0'), Bord('2'), Permut('0'), ])	,	Chem([Sub('3'), Bord('3'), ])),
		(Chem([Sub('0'), Bord('3'), Permut('0'), ])	,	Chem([Sub('1'), Bord('2'), ])),
		(Chem([Sub('1'), Bord('0'), Permut('0'), ])	,	Chem([Sub('5'), Bord('2'), ])),
		(Chem([Sub('1'), Bord('1'), Permut('0'), ])	,	Chem([Sub('4'), Bord('2'), ])),
		(Chem([Sub('1'), Bord('3'), Permut('0'), ])	,	Chem([Sub('3'), Bord('2'), ])),
		(Chem([Sub('2'), Bord('0'), Permut('0'), ])	,	Chem([Sub('4'), Bord('0'), ])),
		(Chem([Sub('2'), Bord('1'), Permut('0'), ])	,	Chem([Sub('5'), Bord('0'), ])),
		(Chem([Sub('2'), Bord('2'), Permut('0'), ])	,	Chem([Sub('3'), Bord('0'), ])),
		(Chem([Sub('3'), Bord('1'), Permut('0'), ])	,	Chem([Sub('5'), Bord('3'), ])),
		(Chem([Sub('4'), Bord('3'), Permut('0'), ])	,	Chem([Sub('5'), Bord('1'), ])),
		]
	
	
	etat0.space = []
	
	etat0.initMat[Chem([Sub('0')])] = FMat([
		[Coef('Var'  ,-0.00379111  ), Coef('Var'  , 0.862326    ), Coef('Var'  , 1.11159     ), Coef('Var'  , 0.241656    ), Coef('Var'  ,-0.960136    ), Coef('Var'  ,-1.79992     ), Coef('Var'  ,-2.04759     ), Coef('Var'  ,-1.18304     ), ], 
		[Coef('Var'  ,-1.41174     ), Coef('Var'  ,-0.616823    ), Coef('Var'  , 0.59716     ), Coef('Var'  , 1.41991     ), Coef('Var'  , 1.71425     ), Coef('Var'  , 0.80775     ), Coef('Var'  ,-0.339688    ), Coef('Var'  ,-1.22962     ), ], 
		[Coef('Var'  , 0.618212    ), Coef('Var'  , 0.164326    ), Coef('Var'  , 0.373654    ), Coef('Var'  , 1.63999e-08 ), Coef('Var'  , 0.204534    ), Coef('Var'  , 3.43076e-08 ), Coef('Var'  , 0.450606    ), Coef('Var'  , 0.215587    ), ], 
		[Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), ], ])
	etat0.initMat[Chem([Sub('1')])] = FMat([
		[Coef('Var'  ,-2.07883     ), Coef('Var'  ,-1.21878     ), Coef('Var'  ,-0.0305609   ), Coef('Var'  , 0.120303    ), Coef('Var'  ,-0.00379111  ), Coef('Var'  ,-1.18304     ), Coef('Var'  ,-2.04759     ), Coef('Var'  ,-2.53374     ), ], 
		[Coef('Var'  , 0.0374787   ), Coef('Var'  ,-0.739548    ), Coef('Var'  ,-1.03601     ), Coef('Var'  ,-1.6773      ), Coef('Var'  ,-1.41174     ), Coef('Var'  ,-1.22962     ), Coef('Var'  ,-0.339688    ), Coef('Var'  ,-0.302852    ), ], 
		[Coef('Var'  , 2.7389      ), Coef('Var'  , 3.21957     ), Coef('Var'  , 2.91814     ), Coef('Var'  , 1.84426     ), Coef('Var'  , 0.618212    ), Coef('Var'  , 0.215587    ), Coef('Var'  , 0.450606    ), Coef('Var'  , 1.61139     ), ], 
		[Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), ], ])
	etat0.initMat[Chem([Sub('2')])] = FMat([
		[Coef('Var'  , 1.11159     ), Coef('Var'  , 1.57785     ), Coef('Var'  , 1.07664     ), Coef('Var'  , 0.206069    ), Coef('Var'  ,-0.979831    ), Coef('Var'  ,-1.1263      ), Coef('Var'  ,-0.960136    ), Coef('Var'  , 0.241656    ), ], 
		[Coef('Var'  , 0.59716     ), Coef('Var'  , 0.927231    ), Coef('Var'  , 0.982228    ), Coef('Var'  , 1.88126     ), Coef('Var'  , 2.07102     ), Coef('Var'  , 2.37761     ), Coef('Var'  , 1.71425     ), Coef('Var'  , 1.41991     ), ], 
		[Coef('Var'  , 0.373654    ), Coef('Var'  , 1.49032     ), Coef('Var'  , 2.6383      ), Coef('Var'  , 2.83979     ), Coef('Var'  , 2.46592     ), Coef('Var'  , 1.25176     ), Coef('Var'  , 0.204534    ), Coef('Var'  , 1.63999e-08 ), ], 
		[Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), ], ])
	etat0.initMat[Chem([Sub('3')])] = FMat([
		[Coef('Var'  ,-0.960136    ), Coef('Var'  ,-1.1263      ), Coef('Var'  ,-0.979831    ), Coef('Var'  ,-1.84242     ), Coef('Var'  ,-2.07883     ), Coef('Var'  ,-2.53374     ), Coef('Var'  ,-2.04759     ), Coef('Var'  ,-1.79992     ), ], 
		[Coef('Var'  , 1.71425     ), Coef('Var'  , 2.37761     ), Coef('Var'  , 2.07102     ), Coef('Var'  , 1.26685     ), Coef('Var'  , 0.0374787   ), Coef('Var'  ,-0.302852    ), Coef('Var'  ,-0.339688    ), Coef('Var'  , 0.80775     ), ], 
		[Coef('Var'  , 0.204534    ), Coef('Var'  , 1.25176     ), Coef('Var'  , 2.46592     ), Coef('Var'  , 2.90638     ), Coef('Var'  , 2.7389      ), Coef('Var'  , 1.61139     ), Coef('Var'  , 0.450606    ), Coef('Var'  , 3.43076e-08 ), ], 
		[Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), ], ])
	etat0.initMat[Chem([Sub('4')])] = FMat([
		[Coef('Var'  , 1.07664     ), Coef('Var'  , 1.57785     ), Coef('Var'  , 1.11159     ), Coef('Var'  , 0.862326    ), Coef('Var'  ,-0.00379111  ), Coef('Var'  , 0.120303    ), Coef('Var'  ,-0.0305609   ), Coef('Var'  , 0.817731    ), ], 
		[Coef('Var'  , 0.982228    ), Coef('Var'  , 0.927231    ), Coef('Var'  , 0.59716     ), Coef('Var'  ,-0.616823    ), Coef('Var'  ,-1.41174     ), Coef('Var'  ,-1.6773      ), Coef('Var'  ,-1.03601     ), Coef('Var'  ,-0.135932    ), ], 
		[Coef('Var'  , 2.6383      ), Coef('Var'  , 1.49032     ), Coef('Var'  , 0.373654    ), Coef('Var'  , 0.164326    ), Coef('Var'  , 0.618212    ), Coef('Var'  , 1.84426     ), Coef('Var'  , 2.91814     ), Coef('Var'  , 3.14839     ), ], 
		[Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), ], ])
	etat0.initMat[Chem([Sub('5')])] = FMat([
		[Coef('Var'  ,-0.979831    ), Coef('Var'  , 0.206069    ), Coef('Var'  , 1.07664     ), Coef('Var'  , 0.817731    ), Coef('Var'  ,-0.0305609   ), Coef('Var'  ,-1.21878     ), Coef('Var'  ,-2.07883     ), Coef('Var'  ,-1.84242     ), ], 
		[Coef('Var'  , 2.07102     ), Coef('Var'  , 1.88126     ), Coef('Var'  , 0.982228    ), Coef('Var'  ,-0.135932    ), Coef('Var'  ,-1.03601     ), Coef('Var'  ,-0.739548    ), Coef('Var'  , 0.0374787   ), Coef('Var'  , 1.26685     ), ], 
		[Coef('Var'  , 2.46592     ), Coef('Var'  , 2.83979     ), Coef('Var'  , 2.6383      ), Coef('Var'  , 3.14839     ), Coef('Var'  , 2.91814     ), Coef('Var'  , 3.21957     ), Coef('Var'  , 2.7389      ), Coef('Var'  , 2.90638     ), ], 
		[Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), ], ])
	
	
	
	etat1.bords   = {Bord('0'): etat2, Bord('1'): etat2, Bord('2'): etat2, Bord('3'): etat2, }
	etat1.permuts = {}
	etat1.interns = {Intern('_'): etat1, }
	etat1.subs    = {Sub('0'): etat1, Sub('1'): etat1, Sub('2'): etat1, Sub('3'): etat1, Sub('4'): etat1, Sub('G', True): Etat.etatPoint, }
	
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
		[Coef('Const', 0.25        ), Coef('Var'  , 0.218792    ), Coef('Var'  , 0.18757     ), Coef('Var'  , 0.218792    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0937361   ), Coef('Var'  , 0.187477    ), Coef('Var'  , 0.343736    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0625084   ), Coef('Var'  , 0.125014    ), Coef('Var'  , 0.187508    ), Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.03123     ), Coef('Var'  , 0.062467    ), Coef('Var'  , 0.03123     ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0312835   ), Coef('Var'  , 0.0625551   ), Coef('Var'  , 0.0312835   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0311869   ), Coef('Var'  , 0.0623962   ), Coef('Var'  , 0.0311869   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.25        ), Coef('Var'  , 0.187524    ), Coef('Var'  , 0.125039    ), Coef('Var'  , 0.0625235   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.5         ), Coef('Var'  , 0.343739    ), Coef('Var'  , 0.187482    ), Coef('Var'  , 0.0937391   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), ], ])
	etat1.initMat[Chem([Sub('1')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0312925   ), Coef('Var'  , 0.06257     ), Coef('Var'  , 0.0312925   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0312363   ), Coef('Var'  , 0.0624773   ), Coef('Var'  , 0.0312363   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.187508    ), Coef('Var'  , 0.125014    ), Coef('Var'  , 0.0625085   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.34373     ), Coef('Var'  , 0.187467    ), Coef('Var'  , 0.0937298   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.218783    ), Coef('Var'  , 0.187555    ), Coef('Var'  , 0.218783    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0936868   ), Coef('Var'  , 0.187396    ), Coef('Var'  , 0.343687    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0625236   ), Coef('Var'  , 0.125039    ), Coef('Var'  , 0.187524    ), Coef('Const', 0.25        ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0312393   ), Coef('Var'  , 0.0624824   ), Coef('Var'  , 0.0312393   ), Coef('Const', 0           ), Coef('Const', 0           ), ], ])
	etat1.initMat[Chem([Sub('2')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0625425   ), Coef('Var'  , 0.12507     ), Coef('Var'  , 0.187542    ), Coef('Const', 0.25        ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0312363   ), Coef('Var'  , 0.0624774   ), Coef('Var'  , 0.0312363   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0312585   ), Coef('Var'  , 0.062514    ), Coef('Var'  , 0.0312585   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.03123     ), Coef('Var'  , 0.062467    ), Coef('Var'  , 0.03123     ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.187533    ), Coef('Var'  , 0.125055    ), Coef('Var'  , 0.0625334   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.343687    ), Coef('Var'  , 0.187396    ), Coef('Var'  , 0.0936868   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.218773    ), Coef('Var'  , 0.187539    ), Coef('Var'  , 0.218773    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0937391   ), Coef('Var'  , 0.187482    ), Coef('Var'  , 0.343739    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), ], ])
	etat1.initMat[Chem([Sub('3')])] = FMat([
		[Coef('Var'  , 0.12507     ), Coef('Var'  , 0.0625425   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.187542    ), ], 
		[Coef('Var'  , 0.187477    ), Coef('Var'  , 0.0937361   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.343736    ), ], 
		[Coef('Var'  , 0.187514    ), Coef('Var'  , 0.218758    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.218758    ), ], 
		[Coef('Var'  , 0.187467    ), Coef('Var'  , 0.34373     ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0937298   ), ], 
		[Coef('Var'  , 0.125055    ), Coef('Var'  , 0.187533    ), Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0625333   ), ], 
		[Coef('Var'  , 0.0623961   ), Coef('Var'  , 0.0311869   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0311869   ), ], 
		[Coef('Var'  , 0.062539    ), Coef('Var'  , 0.0312737   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0312737   ), ], 
		[Coef('Var'  , 0.0624825   ), Coef('Var'  , 0.0312394   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0312394   ), ], ])
	etat1.initMat[Chem([Sub('4')])] = FMat([
		[Coef('Var'  , 0.12507     ), Coef('Var'  , 0.093835    ), Coef('Var'  , 0.06257     ), Coef('Var'  , 0.093835    ), Coef('Var'  , 0.12507     ), Coef('Var'  , 0.156335    ), Coef('Var'  , 0.18757     ), Coef('Var'  , 0.156335    ), ], 
		[Coef('Var'  , 0.0624774   ), Coef('Var'  , 0.0624725   ), Coef('Var'  , 0.0624773   ), Coef('Var'  , 0.124972    ), Coef('Var'  , 0.187477    ), Coef('Var'  , 0.187472    ), Coef('Var'  , 0.187477    ), Coef('Var'  , 0.124972    ), ], 
		[Coef('Var'  , 0.062514    ), Coef('Var'  , 0.093767    ), Coef('Var'  , 0.125014    ), Coef('Var'  , 0.156267    ), Coef('Var'  , 0.187514    ), Coef('Var'  , 0.156267    ), Coef('Var'  , 0.125014    ), Coef('Var'  , 0.0937669   ), ], 
		[Coef('Var'  , 0.062467    ), Coef('Var'  , 0.12496     ), Coef('Var'  , 0.187467    ), Coef('Var'  , 0.18746     ), Coef('Var'  , 0.187467    ), Coef('Var'  , 0.12496     ), Coef('Var'  , 0.062467    ), Coef('Var'  , 0.06246     ), ], 
		[Coef('Var'  , 0.125055    ), Coef('Var'  , 0.156317    ), Coef('Var'  , 0.187555    ), Coef('Var'  , 0.156317    ), Coef('Var'  , 0.125055    ), Coef('Var'  , 0.0938168   ), Coef('Var'  , 0.0625551   ), Coef('Var'  , 0.0938169   ), ], 
		[Coef('Var'  , 0.187396    ), Coef('Var'  , 0.187374    ), Coef('Var'  , 0.187396    ), Coef('Var'  , 0.124874    ), Coef('Var'  , 0.0623961   ), Coef('Var'  , 0.0623738   ), Coef('Var'  , 0.0623962   ), Coef('Var'  , 0.124874    ), ], 
		[Coef('Var'  , 0.187539    ), Coef('Var'  , 0.156297    ), Coef('Var'  , 0.125039    ), Coef('Var'  , 0.0937973   ), Coef('Var'  , 0.062539    ), Coef('Var'  , 0.0937972   ), Coef('Var'  , 0.125039    ), Coef('Var'  , 0.156297    ), ], 
		[Coef('Var'  , 0.187482    ), Coef('Var'  , 0.124978    ), Coef('Var'  , 0.0624824   ), Coef('Var'  , 0.0624787   ), Coef('Var'  , 0.0624825   ), Coef('Var'  , 0.124979    ), Coef('Var'  , 0.187482    ), Coef('Var'  , 0.187478    ), ], ])
	etat1.initMat[Chem([Sub('G')])] = FMat([
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], ])
	
	
	
	etat2.bords   = {Bord('0'): etat3, Bord('1'): etat3, }
	etat2.permuts = {Permut('0'): etat2, }
	etat2.interns = {Intern('_'): etat2, }
	etat2.subs    = {Sub('0'): etat2, Sub('1'): etat2, Sub('G', True): Etat.etatPoint, }
	
	etat2.buildIntern()
	etat2.fm_[Permut('0')] = PMat(3, [2, 1, 0, ])
	
	
	etat2.eqs = [
		(Chem([Permut('0'), Bord('0'), ])	,	Chem([Bord('1')])),
		(Chem([Permut('0'), Bord('1'), ])	,	Chem([Bord('0')])),
		(Chem([Permut('0'), Intern(''), ])	,	Chem([Intern('')])),
		(Chem([Permut('0'), Sub('0'), ])	,	Chem([Sub('1'), Permut('0'), ])),
		(Chem([Permut('0'), Sub('1'), ])	,	Chem([Sub('0'), Permut('0'), ])),
		]
	
	
	etat2.prim.elems = [Figure(1, [Chem([Bord('0')]), Chem([Bord('1')]), ])]
	etat2.grid.elems = [Figure(1, [Chem([Bord('0')]), Chem([Intern('')]), Chem([Bord('1')]), ])]
	
	
	etat2.space = [Chem([Bord('0'), Intern('0'), Intern('0'), ]), Chem([Intern('0'), Intern('0'), ]), Chem([Bord('1'), Intern('0'), Intern('0'), ]), ]
	
	etat2.initMat[Chem([Sub('0')])] = FMat([
		[Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), ], ])
	etat2.initMat[Chem([Sub('1')])] = FMat([
		[Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), ], ])
	etat2.initMat[Chem([Sub('G')])] = FMat([
		[Coef('Const', 0           )], 
		[Coef('Const', 1           )], 
		[Coef('Const', 0           )], ])
	
	
	
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
