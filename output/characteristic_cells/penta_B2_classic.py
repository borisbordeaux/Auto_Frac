# -*- coding: utf-8 -*-

# Automatically generated, from file : penta_B2__B2_B2_B2_classic.py, function : modele()

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
	
	
	etat0.subs   = {Sub('0'): etat1, }
	
	etat0.eqs = [
		]
	
	
	etat0.space = []
	
	etat0.initMat[Chem([Sub('0')])] = FMat([
		[Coef('Var'  ,-1.92966     ), Coef('Var'  ,-1.16663     ), Coef('Var'  ,-0.416259    ), Coef('Var'  , 0.627221    ), Coef('Var'  , 1.67466     ), Coef('Var'  , 1.55524     ), Coef('Var'  , 1.45351     ), Coef('Var'  , 0.335421    ), Coef('Var'  ,-0.774809    ), Coef('Var'  ,-1.35319     ), ], 
		[Coef('Var'  , 0.168797    ), Coef('Var'  , 1.02232     ), Coef('Var'  , 1.87502     ), Coef('Var'  , 1.41458     ), Coef('Var'  , 0.96264     ), Coef('Var'  ,-0.168793    ), Coef('Var'  ,-1.30829     ), Coef('Var'  ,-1.55604     ), Coef('Var'  ,-1.79832     ), Coef('Var'  ,-0.809795    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), ], ])
	
	
	
	etat1.bords   = {Bord('0'): etat2, Bord('1'): etat2, Bord('2'): etat2, Bord('3'): etat2, Bord('4'): etat2, }
	etat1.permuts = {}
	etat1.interns = {Intern('_'): etat1, }
	etat1.subs    = {Sub('0'): etat1, Sub('G', True): Etat.etatPoint, Sub('1'): etat1, Sub('2'): etat1, Sub('3'): etat1, Sub('4'): etat1, }
	
	etat1.buildIntern()
	
	
	etat1.eqs = [
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
	
	
	etat1.prim.elems = [Figure(2, [Chem([Bord('0'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('0'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('0'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('0'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('1'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('1'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('1'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('1'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('2'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('2'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('2'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('2'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('3'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('3'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('3'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('3'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('4'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('4'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('4'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('4'), Sub('1'), Sub('1'), Bord('0'), ]), ])]
	etat1.grid.elems = [
		Figure(1, [Chem([Bord('1'), Bord('0'), ]), Chem([Bord('1'), Intern(''), ]), Chem([Bord('1'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('4'), Bord('0'), ]), Chem([Bord('4'), Intern(''), ]), Chem([Bord('4'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('2'), Bord('0'), ]), Chem([Bord('2'), Intern(''), ]), Chem([Bord('2'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('0'), Bord('0'), ]), Chem([Bord('0'), Intern(''), ]), Chem([Bord('0'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('3'), Bord('0'), ]), Chem([Bord('3'), Intern(''), ]), Chem([Bord('3'), Bord('1'), ]), ]), ]
	
	
	etat1.space = [Chem([Bord('4'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('2'), Intern('0'), Intern('0'), ]), Chem([Bord('2'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('3'), Intern('0'), Intern('0'), ]), Chem([Bord('4'), Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('4'), Intern('0'), Intern('0'), ]), ]
	
	etat1.initMat[Chem([Sub('0')])] = FMat([
		[Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0340967   ), Coef('Var'  , 0.0772309   ), Coef('Var'  , 0.127692    ), Coef('Var'  , 0.159451    ), Coef('Var'  , 0.204549    ), ], 
		[Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0454743   ), Coef('Var'  , 0.122812    ), Coef('Var'  , 0.169153    ), Coef('Var'  , 0.174651    ), Coef('Var'  , 0.363653    ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.204577    ), Coef('Var'  , 0.159667    ), Coef('Var'  , 0.184156    ), Coef('Var'  , 0.161289    ), Coef('Var'  , 0.204577    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.363656    ), Coef('Var'  , 0.173752    ), Coef('Var'  , 0.167047    ), Coef('Var'  , 0.124542    ), Coef('Var'  , 0.0454773   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.204542    ), Coef('Var'  , 0.159664    ), Coef('Var'  , 0.124326    ), Coef('Var'  , 0.0784207   ), Coef('Var'  , 0.0340897   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0454472   ), Coef('Var'  , 0.12277     ), Coef('Var'  , 0.0723079   ), Coef('Var'  , 0.0405489   ), Coef('Var'  , 0.0227247   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0340739   ), Coef('Var'  , 0.0771877   ), Coef('Var'  , 0.0308472   ), Coef('Var'  , 0.0253492   ), Coef('Var'  , 0.0227117   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0227229   ), Coef('Var'  , 0.0403321   ), Coef('Var'  , 0.0158435   ), Coef('Var'  , 0.0387109   ), Coef('Var'  , 0.0227228   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0226881   ), Coef('Var'  , 0.0262474   ), Coef('Var'  , 0.0329529   ), Coef('Var'  , 0.0754578   ), Coef('Var'  , 0.03405     ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0227225   ), Coef('Var'  , 0.0403364   ), Coef('Var'  , 0.0756741   ), Coef('Var'  , 0.121579    ), Coef('Var'  , 0.0454449   ), ], ])
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
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0227347   ), Coef('Var'  , 0.0247536   ), Coef('Var'  , 0.0271134   ), Coef('Var'  , 0.0772309   ), Coef('Var'  , 0.0340967   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.022752    ), Coef('Var'  , 0.0394219   ), Coef('Var'  , 0.0758562   ), Coef('Var'  , 0.122812    ), Coef('Var'  , 0.0454743   ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0341247   ), Coef('Var'  , 0.077269    ), Coef('Var'  , 0.133839    ), Coef('Var'  , 0.159667    ), Coef('Var'  , 0.204577    ), ], 
		[Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0454772   ), Coef('Var'  , 0.123787    ), Coef('Var'  , 0.178905    ), Coef('Var'  , 0.173752    ), Coef('Var'  , 0.363656    ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.204542    ), Coef('Var'  , 0.161217    ), Coef('Var'  , 0.193829    ), Coef('Var'  , 0.159664    ), Coef('Var'  , 0.204542    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.363626    ), Coef('Var'  , 0.175247    ), Coef('Var'  , 0.172888    ), Coef('Var'  , 0.12277     ), Coef('Var'  , 0.0454472   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.204526    ), Coef('Var'  , 0.160578    ), Coef('Var'  , 0.124143    ), Coef('Var'  , 0.0771877   ), Coef('Var'  , 0.0340739   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0454453   ), Coef('Var'  , 0.12273     ), Coef('Var'  , 0.0661603   ), Coef('Var'  , 0.0403321   ), Coef('Var'  , 0.0227229   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0340501   ), Coef('Var'  , 0.0762132   ), Coef('Var'  , 0.0210944   ), Coef('Var'  , 0.0262474   ), Coef('Var'  , 0.0226881   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0227226   ), Coef('Var'  , 0.0387831   ), Coef('Var'  , 0.00617113  ), Coef('Var'  , 0.0403364   ), Coef('Var'  , 0.0227225   ), ], ])
	etat1.initMat[Chem([Sub('2')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0340969   ), Coef('Var'  , 0.0765022   ), Coef('Var'  , 0.0235696   ), Coef('Var'  , 0.0247536   ), Coef('Var'  , 0.0227347   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0227522   ), Coef('Var'  , 0.038668    ), Coef('Var'  , 0.00503564  ), Coef('Var'  , 0.0394219   ), Coef('Var'  , 0.022752    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0227628   ), Coef('Var'  , 0.0242988   ), Coef('Var'  , 0.0228359   ), Coef('Var'  , 0.077269    ), Coef('Var'  , 0.0341247   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0227549   ), Coef('Var'  , 0.0388162   ), Coef('Var'  , 0.0700783   ), Coef('Var'  , 0.123787    ), Coef('Var'  , 0.0454772   ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0340896   ), Coef('Var'  , 0.0767053   ), Coef('Var'  , 0.12875     ), Coef('Var'  , 0.161217    ), Coef('Var'  , 0.204542    ), ], 
		[Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.045447    ), Coef('Var'  , 0.123497    ), Coef('Var'  , 0.176431    ), Coef('Var'  , 0.175247    ), Coef('Var'  , 0.363626    ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.204526    ), Coef('Var'  , 0.161332    ), Coef('Var'  , 0.194964    ), Coef('Var'  , 0.160578    ), Coef('Var'  , 0.204526    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.363624    ), Coef('Var'  , 0.175701    ), Coef('Var'  , 0.177164    ), Coef('Var'  , 0.12273     ), Coef('Var'  , 0.0454453   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.204502    ), Coef('Var'  , 0.161184    ), Coef('Var'  , 0.129922    ), Coef('Var'  , 0.0762132   ), Coef('Var'  , 0.0340501   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.045445    ), Coef('Var'  , 0.123295    ), Coef('Var'  , 0.0712501   ), Coef('Var'  , 0.0387831   ), Coef('Var'  , 0.0227226   ), ], ])
	etat1.initMat[Chem([Sub('3')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.204549    ), Coef('Var'  , 0.162213    ), Coef('Var'  , 0.131052    ), Coef('Var'  , 0.0765022   ), Coef('Var'  , 0.0340969   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0454746   ), Coef('Var'  , 0.125751    ), Coef('Var'  , 0.0743889   ), Coef('Var'  , 0.038668    ), Coef('Var'  , 0.0227522   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0341249   ), Coef('Var'  , 0.0794353   ), Coef('Var'  , 0.0275221   ), Coef('Var'  , 0.0242988   ), Coef('Var'  , 0.0227628   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.022755    ), Coef('Var'  , 0.0409698   ), Coef('Var'  , 0.00831463  ), Coef('Var'  , 0.0388162   ), Coef('Var'  , 0.0227549   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0227276   ), Coef('Var'  , 0.0250541   ), Coef('Var'  , 0.0241308   ), Coef('Var'  , 0.0767053   ), Coef('Var'  , 0.0340896   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0227246   ), Coef('Var'  , 0.0377862   ), Coef('Var'  , 0.0689469   ), Coef('Var'  , 0.123497    ), Coef('Var'  , 0.045447    ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0340737   ), Coef('Var'  , 0.074249    ), Coef('Var'  , 0.125611    ), Coef('Var'  , 0.161332    ), Coef('Var'  , 0.204526    ), ], 
		[Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0454451   ), Coef('Var'  , 0.120565    ), Coef('Var'  , 0.172478    ), Coef('Var'  , 0.175701    ), Coef('Var'  , 0.363624    ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.204502    ), Coef('Var'  , 0.15903     ), Coef('Var'  , 0.191686    ), Coef('Var'  , 0.161184    ), Coef('Var'  , 0.204502    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.363624    ), Coef('Var'  , 0.174946    ), Coef('Var'  , 0.175869    ), Coef('Var'  , 0.123295    ), Coef('Var'  , 0.045445    ), ], ])
	etat1.initMat[Chem([Sub('4')])] = FMat([
		[Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.204549    ), Coef('Var'  , 0.159451    ), Coef('Var'  , 0.191262    ), Coef('Var'  , 0.162213    ), Coef('Var'  , 0.204549    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.363653    ), Coef('Var'  , 0.174651    ), Coef('Var'  , 0.177567    ), Coef('Var'  , 0.125751    ), Coef('Var'  , 0.0454746   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.204577    ), Coef('Var'  , 0.161289    ), Coef('Var'  , 0.134193    ), Coef('Var'  , 0.0794353   ), Coef('Var'  , 0.0341249   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0454773   ), Coef('Var'  , 0.124542    ), Coef('Var'  , 0.0777757   ), Coef('Var'  , 0.0409698   ), Coef('Var'  , 0.022755    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0340897   ), Coef('Var'  , 0.0784207   ), Coef('Var'  , 0.0298485   ), Coef('Var'  , 0.0250541   ), Coef('Var'  , 0.0227276   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0227247   ), Coef('Var'  , 0.0405489   ), Coef('Var'  , 0.00873753  ), Coef('Var'  , 0.0377862   ), Coef('Var'  , 0.0227246   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0227117   ), Coef('Var'  , 0.0253492   ), Coef('Var'  , 0.0224336   ), Coef('Var'  , 0.074249    ), Coef('Var'  , 0.0340737   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0227228   ), Coef('Var'  , 0.0387109   ), Coef('Var'  , 0.0658073   ), Coef('Var'  , 0.120565    ), Coef('Var'  , 0.0454451   ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.03405     ), Coef('Var'  , 0.0754578   ), Coef('Var'  , 0.122224    ), Coef('Var'  , 0.15903     ), Coef('Var'  , 0.204502    ), ], 
		[Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0454449   ), Coef('Var'  , 0.121579    ), Coef('Var'  , 0.170151    ), Coef('Var'  , 0.174946    ), Coef('Var'  , 0.363624    ), ], ])
	
	
	
	etat2.bords   = {Bord('0'): etat3, Bord('1'): etat3, }
	etat2.permuts = {Permut('0'): etat2, }
	etat2.interns = {Intern('_'): etat2, }
	etat2.subs    = {Sub('0'): etat2, Sub('G', True): Etat.etatPoint, Sub('1'): etat2, }
	
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
	etat2.initMat[Chem([Sub('G')])] = FMat([
		[Coef('Const', 0           )], 
		[Coef('Const', 1           )], 
		[Coef('Const', 0           )], ])
	etat2.initMat[Chem([Sub('1')])] = FMat([
		[Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), ], ])
	
	
	
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
