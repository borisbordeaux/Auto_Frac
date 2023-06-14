# -*- coding: utf-8 -*-

# Automatically generated, from file : dodecahedron.py, function : modele()

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
	etat9 = Etat('Cell_8',0)
	etat10 = Etat('Cell_9',0)
	etat11 = Etat('Cell_10',0)
	etat12 = Etat('Cell_11',0)
	etat13 = Etat('B2',1)
	etat14 = Etat('s',1)
	
	
	etat0.subs   = {Sub('0'): etat1, Sub('1'): etat2, Sub('2'): etat3, Sub('3'): etat4, Sub('4'): etat5, Sub('5'): etat6, Sub('6'): etat7, Sub('7'): etat8, Sub('8'): etat9, Sub('9'): etat10, Sub('10'): etat11, Sub('11'): etat12, }
	
	etat0.eqs = [
		(Chem([Sub('0'), Bord('0'), Bord('1'), ])	,	Chem([Sub('7'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('1'), Bord('1'), ])	,	Chem([Sub('11'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('2'), Bord('1'), ])	,	Chem([Sub('6'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('3'), Bord('1'), ])	,	Chem([Sub('5'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('4'), Bord('1'), ])	,	Chem([Sub('1'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('0'), Bord('1'), ])	,	Chem([Sub('10'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('1'), Bord('1'), ])	,	Chem([Sub('2'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('2'), Bord('1'), ])	,	Chem([Sub('7'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('4'), Bord('1'), ])	,	Chem([Sub('5'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('0'), Bord('1'), ])	,	Chem([Sub('9'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('1'), Bord('1'), ])	,	Chem([Sub('7'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('3'), Bord('1'), ])	,	Chem([Sub('10'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('4'), Bord('1'), ])	,	Chem([Sub('4'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('3'), Bord('0'), Bord('1'), ])	,	Chem([Sub('5'), Bord('4'), Bord('1'), ])),
		(Chem([Sub('3'), Bord('1'), Bord('1'), ])	,	Chem([Sub('6'), Bord('4'), Bord('1'), ])),
		(Chem([Sub('3'), Bord('2'), Bord('1'), ])	,	Chem([Sub('8'), Bord('4'), Bord('1'), ])),
		(Chem([Sub('3'), Bord('3'), Bord('1'), ])	,	Chem([Sub('4'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('3'), Bord('4'), Bord('1'), ])	,	Chem([Sub('10'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('4'), Bord('1'), Bord('1'), ])	,	Chem([Sub('8'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('4'), Bord('2'), Bord('1'), ])	,	Chem([Sub('9'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('4'), Bord('4'), Bord('1'), ])	,	Chem([Sub('10'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('5'), Bord('0'), Bord('1'), ])	,	Chem([Sub('10'), Bord('4'), Bord('1'), ])),
		(Chem([Sub('5'), Bord('3'), Bord('1'), ])	,	Chem([Sub('6'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('6'), Bord('2'), Bord('1'), ])	,	Chem([Sub('11'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('6'), Bord('3'), Bord('1'), ])	,	Chem([Sub('8'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('7'), Bord('0'), Bord('1'), ])	,	Chem([Sub('11'), Bord('4'), Bord('1'), ])),
		(Chem([Sub('7'), Bord('4'), Bord('1'), ])	,	Chem([Sub('9'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('8'), Bord('1'), Bord('1'), ])	,	Chem([Sub('11'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('8'), Bord('2'), Bord('1'), ])	,	Chem([Sub('9'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('9'), Bord('4'), Bord('1'), ])	,	Chem([Sub('11'), Bord('0'), Bord('1'), ])),
		]
	
	
	etat0.space = []
	
	etat0.initMat[Chem([Sub('0')])] = FMat([
		[Coef('Var'  ,-3.94695     ), Coef('Var'  ,-3.77333     ), Coef('Var'  ,-3.11112     ), Coef('Var'  ,-2.64745     ), Coef('Var'  ,-1.56898     ), Coef('Var'  ,-1.87316     ), Coef('Var'  ,-1.46635     ), Coef('Var'  ,-2.55641     ), Coef('Var'  ,-2.98307     ), Coef('Var'  ,-3.74027     ), ], 
		[Coef('Var'  , 0.44216     ), Coef('Var'  , 1.75714     ), Coef('Var'  , 2.81207     ), Coef('Var'  , 3.22015     ), Coef('Var'  , 3.46513     ), Coef('Var'  , 2.55627     ), Coef('Var'  , 1.42224     ), Coef('Var'  , 0.677476    ), Coef('Var'  ,-0.430252    ), Coef('Var'  , 0.203763    ), ], 
		[Coef('Var'  , 3.05039     ), Coef('Var'  , 2.99331     ), Coef('Var'  , 3.44564     ), Coef('Var'  , 2.27143     ), Coef('Var'  , 1.53914     ), Coef('Var'  , 0.64499     ), Coef('Var'  , 0.136545    ), Coef('Var'  , 0.281559    ), Coef('Var'  , 0.883902    ), Coef('Var'  , 1.76495     ), ], 
		[Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), ], ])
	etat0.initMat[Chem([Sub('1')])] = FMat([
		[Coef('Var'  ,-3.22578     ), Coef('Var'  ,-3.08244     ), Coef('Var'  ,-2.24927     ), Coef('Var'  ,-2.68527     ), Coef('Var'  ,-2.38819     ), Coef('Var'  ,-3.25039     ), Coef('Var'  ,-3.42177     ), Coef('Var'  ,-3.99229     ), Coef('Var'  ,-3.94695     ), Coef('Var'  ,-3.88754     ), ], 
		[Coef('Var'  ,-1.99473     ), Coef('Var'  ,-2.38415     ), Coef('Var'  ,-2.68093     ), Coef('Var'  ,-1.75947     ), Coef('Var'  ,-0.699971    ), Coef('Var'  , 0.117       ), Coef('Var'  , 1.23434     ), Coef('Var'  , 0.665515    ), Coef('Var'  , 0.44216     ), Coef('Var'  ,-0.880485    ), ], 
		[Coef('Var'  , 2.85562     ), Coef('Var'  , 4.11507     ), Coef('Var'  , 5.10191     ), Coef('Var'  , 5.95035     ), Coef('Var'  , 6.69508     ), Coef('Var'  , 6.10457     ), Coef('Var'  , 5.41578     ), Coef('Var'  , 4.35832     ), Coef('Var'  , 3.05039     ), Coef('Var'  , 3.13793     ), ], 
		[Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), ], ])
	etat0.initMat[Chem([Sub('2')])] = FMat([
		[Coef('Var'  , 1.66651     ), Coef('Var'  , 1.19685     ), Coef('Var'  , 0.949305    ), Coef('Var'  ,-0.361799    ), Coef('Var'  ,-1.56266     ), Coef('Var'  ,-1.96355     ), Coef('Var'  ,-2.38819     ), Coef('Var'  ,-1.40642     ), Coef('Var'  ,-0.39386     ), Coef('Var'  , 0.544203    ), ], 
		[Coef('Var'  ,-0.848564    ), Coef('Var'  , 0.300131    ), Coef('Var'  , 1.57273     ), Coef('Var'  , 1.51554     ), Coef('Var'  , 1.66679     ), Coef('Var'  , 0.410999    ), Coef('Var'  ,-0.699971    ), Coef('Var'  ,-1.47125     ), Coef('Var'  ,-2.25453     ), Coef('Var'  ,-1.5398      ), ], 
		[Coef('Var'  , 7.25449     ), Coef('Var'  , 7.71546     ), Coef('Var'  , 7.44181     ), Coef('Var'  , 7.64069     ), Coef('Var'  , 7.09677     ), Coef('Var'  , 7.27523     ), Coef('Var'  , 6.69508     ), Coef('Var'  , 7.13264     ), Coef('Var'  , 6.79015     ), Coef('Var'  , 7.39475     ), ], 
		[Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), ], ])
	etat0.initMat[Chem([Sub('3')])] = FMat([
		[Coef('Var'  , 1.30573     ), Coef('Var'  , 1.10633     ), Coef('Var'  , 0.360726    ), Coef('Var'  , 1.35547     ), Coef('Var'  , 1.83617     ), Coef('Var'  , 2.98347     ), Coef('Var'  , 3.72083     ), Coef('Var'  , 3.69828     ), Coef('Var'  , 3.36372     ), Coef('Var'  , 2.54061     ), ], 
		[Coef('Var'  ,-3.64327     ), Coef('Var'  ,-3.55994     ), Coef('Var'  ,-3.01727     ), Coef('Var'  ,-2.35644     ), Coef('Var'  ,-1.14118     ), Coef('Var'  ,-1.21644     ), Coef('Var'  ,-0.66175     ), Coef('Var'  ,-1.73205     ), Coef('Var'  ,-2.22539     ), Coef('Var'  ,-3.15412     ), ], 
		[Coef('Var'  , 3.29193     ), Coef('Var'  , 1.98798     ), Coef('Var'  , 1.03561     ), Coef('Var'  , 0.437936    ), Coef('Var'  , 0.219807    ), Coef('Var'  , 0.828145    ), Coef('Var'  , 1.77141     ), Coef('Var'  , 2.55303     ), Coef('Var'  , 3.73977     ), Coef('Var'  , 3.27945     ), ], 
		[Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), ], ])
	etat0.initMat[Chem([Sub('4')])] = FMat([
		[Coef('Var'  , 1.80357     ), Coef('Var'  , 2.87858     ), Coef('Var'  , 3.36372     ), Coef('Var'  , 4.02385     ), Coef('Var'  , 4.19073     ), Coef('Var'  , 3.91784     ), Coef('Var'  , 3.13589     ), Coef('Var'  , 2.71216     ), Coef('Var'  , 1.66651     ), Coef('Var'  , 2.07118     ), ], 
		[Coef('Var'  ,-2.83001     ), Coef('Var'  ,-2.59289     ), Coef('Var'  ,-2.22539     ), Coef('Var'  ,-1.17782     ), Coef('Var'  , 0.133407    ), Coef('Var'  , 0.368002    ), Coef('Var'  , 0.989947    ), Coef('Var'  ,-0.10156     ), Coef('Var'  ,-0.848564    ), Coef('Var'  ,-1.94016     ), ], 
		[Coef('Var'  , 5.65755     ), Coef('Var'  , 4.9191      ), Coef('Var'  , 3.73977     ), Coef('Var'  , 4.19429     ), Coef('Var'  , 4.13537     ), Coef('Var'  , 5.41847     ), Coef('Var'  , 6.29173     ), Coef('Var'  , 6.91364     ), Coef('Var'  , 7.25449     ), Coef('Var'  , 6.60855     ), ], 
		[Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), ], ])
	etat0.initMat[Chem([Sub('5')])] = FMat([
		[Coef('Var'  , 0.360726    ), Coef('Var'  ,-0.6481      ), Coef('Var'  ,-1.21079     ), Coef('Var'  ,-2.36309     ), Coef('Var'  ,-3.22578     ), Coef('Var'  ,-3.25161     ), Coef('Var'  ,-2.98307     ), Coef('Var'  ,-2.03347     ), Coef('Var'  ,-0.72935     ), Coef('Var'  ,-0.426978    ), ], 
		[Coef('Var'  ,-3.01727     ), Coef('Var'  ,-3.50086     ), Coef('Var'  ,-3.55364     ), Coef('Var'  ,-2.9735      ), Coef('Var'  ,-1.99473     ), Coef('Var'  ,-1.49818     ), Coef('Var'  ,-0.430252    ), Coef('Var'  ,-1.0367      ), Coef('Var'  ,-1.02981     ), Coef('Var'  ,-2.2832      ), ], 
		[Coef('Var'  , 1.03561     ), Coef('Var'  , 1.7473      ), Coef('Var'  , 2.94696     ), Coef('Var'  , 2.61666     ), Coef('Var'  , 2.85562     ), Coef('Var'  , 1.62385     ), Coef('Var'  , 0.883902    ), Coef('Var'  , 0.195537    ), Coef('Var'  , 0.018834    ), Coef('Var'  , 0.273138    ), ], 
		[Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), ], ])
	etat0.initMat[Chem([Sub('6')])] = FMat([
		[Coef('Var'  , 1.83617     ), Coef('Var'  , 0.569052    ), Coef('Var'  ,-0.72935     ), Coef('Var'  ,-0.90251     ), Coef('Var'  ,-1.46635     ), Coef('Var'  ,-0.325727    ), Coef('Var'  , 0.639405    ), Coef('Var'  , 1.64497     ), Coef('Var'  , 2.64489     ), Coef('Var'  , 2.19513     ), ], 
		[Coef('Var'  ,-1.14118     ), Coef('Var'  ,-0.893482    ), Coef('Var'  ,-1.02981     ), Coef('Var'  , 0.261561    ), Coef('Var'  , 1.42224     ), Coef('Var'  , 2.06608     ), Coef('Var'  , 2.83427     ), Coef('Var'  , 2.03958     ), Coef('Var'  , 1.26838     ), Coef('Var'  , 0.123078    ), ], 
		[Coef('Var'  , 0.219807    ), Coef('Var'  , 9.11887e-09 ), Coef('Var'  , 0.018834    ), Coef('Var'  , 9.11352e-09 ), Coef('Var'  , 0.136545    ), Coef('Var'  , 1.33246e-08 ), Coef('Var'  , 0.434512    ), Coef('Var'  , 0.0570655   ), Coef('Var'  , 0.490662    ), Coef('Var'  , 1.18148e-08 ), ], 
		[Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), ], ])
	etat0.initMat[Chem([Sub('7')])] = FMat([
		[Coef('Var'  ,-0.0851737   ), Coef('Var'  ,-0.82719     ), Coef('Var'  ,-1.04327     ), Coef('Var'  ,-2.27241     ), Coef('Var'  ,-3.11112     ), Coef('Var'  ,-3.41555     ), Coef('Var'  ,-3.42177     ), Coef('Var'  ,-2.68136     ), Coef('Var'  ,-1.56266     ), Coef('Var'  ,-1.07372     ), ], 
		[Coef('Var'  , 3.49012     ), Coef('Var'  , 4.05947     ), Coef('Var'  , 4.21534     ), Coef('Var'  , 3.73044     ), Coef('Var'  , 2.81207     ), Coef('Var'  , 2.30493     ), Coef('Var'  , 1.23434     ), Coef('Var'  , 1.7576      ), Coef('Var'  , 1.66679     ), Coef('Var'  , 2.83855     ), ], 
		[Coef('Var'  , 6.13112     ), Coef('Var'  , 5.19026     ), Coef('Var'  , 3.8903      ), Coef('Var'  , 3.90298     ), Coef('Var'  , 3.44564     ), Coef('Var'  , 4.63392     ), Coef('Var'  , 5.41578     ), Coef('Var'  , 6.38518     ), Coef('Var'  , 7.09677     ), Coef('Var'  , 6.7211      ), ], 
		[Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), ], ])
	etat0.initMat[Chem([Sub('8')])] = FMat([
		[Coef('Var'  , 3.72083     ), Coef('Var'  , 3.53444     ), Coef('Var'  , 2.64489     ), Coef('Var'  , 2.95677     ), Coef('Var'  , 2.51911     ), Coef('Var'  , 3.34495     ), Coef('Var'  , 3.46006     ), Coef('Var'  , 4.14499     ), Coef('Var'  , 4.19073     ), Coef('Var'  , 4.26976     ), ], 
		[Coef('Var'  ,-0.66175     ), Coef('Var'  , 0.450366    ), Coef('Var'  , 1.26838     ), Coef('Var'  , 2.33991     ), Coef('Var'  , 3.25694     ), Coef('Var'  , 2.94301     ), Coef('Var'  , 2.54838     ), Coef('Var'  , 1.4515      ), Coef('Var'  , 0.133407    ), Coef('Var'  ,-0.092904    ), ], 
		[Coef('Var'  , 1.77141     ), Coef('Var'  , 1.05978     ), Coef('Var'  , 0.490662    ), Coef('Var'  , 1.19793     ), Coef('Var'  , 2.04293     ), Coef('Var'  , 3.03376     ), Coef('Var'  , 4.2977      ), Coef('Var'  , 4.04078     ), Coef('Var'  , 4.13537     ), Coef('Var'  , 2.83623     ), ], 
		[Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), ], ])
	etat0.initMat[Chem([Sub('9')])] = FMat([
		[Coef('Var'  , 1.46496     ), Coef('Var'  , 0.914339    ), Coef('Var'  ,-0.0851737   ), Coef('Var'  , 0.665869    ), Coef('Var'  , 0.949305    ), Coef('Var'  , 2.21489     ), Coef('Var'  , 3.13589     ), Coef('Var'  , 3.4056      ), Coef('Var'  , 3.46006     ), Coef('Var'  , 2.6158      ), ], 
		[Coef('Var'  , 4.09795     ), Coef('Var'  , 3.96977     ), Coef('Var'  , 3.49012     ), Coef('Var'  , 2.77961     ), Coef('Var'  , 1.57273     ), Coef('Var'  , 1.57724     ), Coef('Var'  , 0.989947    ), Coef('Var'  , 2.04123     ), Coef('Var'  , 2.54838     ), Coef('Var'  , 3.5351      ), ], 
		[Coef('Var'  , 4.20204     ), Coef('Var'  , 5.40536     ), Coef('Var'  , 6.13112     ), Coef('Var'  , 6.9632      ), Coef('Var'  , 7.44181     ), Coef('Var'  , 7.04271     ), Coef('Var'  , 6.29173     ), Coef('Var'  , 5.52758     ), Coef('Var'  , 4.2977      ), Coef('Var'  , 4.52945     ), ], 
		[Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), ], ])
	etat0.initMat[Chem([Sub('10')])] = FMat([
		[Coef('Var'  ,-1.21079     ), Coef('Var'  , 0.00798086  ), Coef('Var'  , 1.30573     ), Coef('Var'  , 1.45549     ), Coef('Var'  , 1.80357     ), Coef('Var'  , 0.643234    ), Coef('Var'  ,-0.39386     ), Coef('Var'  ,-1.30164     ), Coef('Var'  ,-2.24927     ), Coef('Var'  ,-1.69804     ), ], 
		[Coef('Var'  ,-3.55364     ), Coef('Var'  ,-3.90734     ), Coef('Var'  ,-3.64327     ), Coef('Var'  ,-3.56659     ), Coef('Var'  ,-2.83001     ), Coef('Var'  ,-2.91168     ), Coef('Var'  ,-2.25453     ), Coef('Var'  ,-2.83616     ), Coef('Var'  ,-2.68093     ), Coef('Var'  ,-3.4592      ), ], 
		[Coef('Var'  , 2.94696     ), Coef('Var'  , 3.31631     ), Coef('Var'  , 3.29193     ), Coef('Var'  , 4.61105     ), Coef('Var'  , 5.65755     ), Coef('Var'  , 6.28918     ), Coef('Var'  , 6.79015     ), Coef('Var'  , 6.01603     ), Coef('Var'  , 5.10191     ), Coef('Var'  , 4.18097     ), ], 
		[Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), ], ])
	etat0.initMat[Chem([Sub('11')])] = FMat([
		[Coef('Var'  ,-1.04327     ), Coef('Var'  , 0.25182     ), Coef('Var'  , 1.46496     ), Coef('Var'  , 1.95807     ), Coef('Var'  , 2.51911     ), Coef('Var'  , 1.57077     ), Coef('Var'  , 0.639405    ), Coef('Var'  ,-0.402589    ), Coef('Var'  ,-1.56898     ), Coef('Var'  ,-1.21134     ), ], 
		[Coef('Var'  , 4.21534     ), Coef('Var'  , 4.48238     ), Coef('Var'  , 4.09795     ), Coef('Var'  , 4.02272     ), Coef('Var'  , 3.25694     ), Coef('Var'  , 3.42806     ), Coef('Var'  , 2.83427     ), Coef('Var'  , 3.53524     ), Coef('Var'  , 3.46513     ), Coef('Var'  , 4.19644     ), ], 
		[Coef('Var'  , 3.8903      ), Coef('Var'  , 3.85853     ), Coef('Var'  , 4.20204     ), Coef('Var'  , 2.97155     ), Coef('Var'  , 2.04293     ), Coef('Var'  , 1.14664     ), Coef('Var'  , 0.434512    ), Coef('Var'  , 0.892433    ), Coef('Var'  , 1.53914     ), Coef('Var'  , 2.57566     ), ], 
		[Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), ], ])
	
	
	
	etat1.bords   = {Bord('0'): etat13, Bord('1'): etat13, Bord('2'): etat13, Bord('3'): etat13, Bord('4'): etat13, }
	etat1.permuts = {}
	etat1.interns = {Intern('_'): etat1, }
	etat1.subs    = {Sub('0'): etat2, Sub('1'): etat3, Sub('2'): etat4, Sub('3'): etat5, Sub('G', True): Etat.etatPoint, Sub('4'): etat6, Sub('5'): etat7, Sub('6'): etat8, Sub('7'): etat9, Sub('8'): etat10, Sub('9'): etat11, Sub('10'): etat12, }
	
	etat1.buildIntern()
	
	
	etat1.eqs = [
		(Chem([Bord('0'), Sub('0'), Permut('0'), ])	,	Chem([Sub('0'), Bord('3'), ])),
		(Chem([Bord('4'), Sub('1'), Permut('0'), ])	,	Chem([Sub('0'), Bord('4'), ])),
		(Chem([Bord('4'), Sub('0'), Permut('0'), ])	,	Chem([Sub('4'), Bord('2'), ])),
		(Chem([Bord('3'), Sub('1'), Permut('0'), ])	,	Chem([Sub('4'), Bord('3'), ])),
		(Chem([Bord('3'), Sub('0'), Permut('0'), ])	,	Chem([Sub('5'), Bord('1'), ])),
		(Chem([Bord('2'), Sub('1'), Permut('0'), ])	,	Chem([Sub('5'), Bord('2'), ])),
		(Chem([Bord('1'), Sub('0'), Permut('0'), ])	,	Chem([Sub('6'), Bord('1'), ])),
		(Chem([Bord('0'), Sub('1'), Permut('0'), ])	,	Chem([Sub('6'), Bord('2'), ])),
		(Chem([Bord('2'), Sub('0'), Permut('0'), ])	,	Chem([Sub('10'), Bord('3'), ])),
		(Chem([Bord('1'), Sub('1'), Permut('0'), ])	,	Chem([Sub('10'), Bord('4'), ])),
		(Chem([Sub('0'), Bord('0'), Bord('1'), ])	,	Chem([Sub('9'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('1'), Bord('1'), ])	,	Chem([Sub('1'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('2'), Bord('1'), ])	,	Chem([Sub('6'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('4'), Bord('1'), ])	,	Chem([Sub('4'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('0'), Bord('1'), ])	,	Chem([Sub('8'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('1'), Bord('1'), ])	,	Chem([Sub('6'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('3'), Bord('1'), ])	,	Chem([Sub('9'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('4'), Bord('1'), ])	,	Chem([Sub('3'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('0'), Bord('1'), ])	,	Chem([Sub('4'), Bord('4'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('1'), Bord('1'), ])	,	Chem([Sub('5'), Bord('4'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('2'), Bord('1'), ])	,	Chem([Sub('7'), Bord('4'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('3'), Bord('1'), ])	,	Chem([Sub('3'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('4'), Bord('1'), ])	,	Chem([Sub('9'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('3'), Bord('1'), Bord('1'), ])	,	Chem([Sub('7'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('3'), Bord('2'), Bord('1'), ])	,	Chem([Sub('8'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('3'), Bord('4'), Bord('1'), ])	,	Chem([Sub('9'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('4'), Bord('0'), Bord('1'), ])	,	Chem([Sub('9'), Bord('4'), Bord('1'), ])),
		(Chem([Sub('4'), Bord('3'), Bord('1'), ])	,	Chem([Sub('5'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('5'), Bord('2'), Bord('1'), ])	,	Chem([Sub('10'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('5'), Bord('3'), Bord('1'), ])	,	Chem([Sub('7'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('6'), Bord('0'), Bord('1'), ])	,	Chem([Sub('10'), Bord('4'), Bord('1'), ])),
		(Chem([Sub('6'), Bord('4'), Bord('1'), ])	,	Chem([Sub('8'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('7'), Bord('1'), Bord('1'), ])	,	Chem([Sub('10'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('7'), Bord('2'), Bord('1'), ])	,	Chem([Sub('8'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('8'), Bord('4'), Bord('1'), ])	,	Chem([Sub('10'), Bord('0'), Bord('1'), ])),
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
		[Coef('Const', 0.25        ), Coef('Var'  , 0.212828    ), Coef('Var'  , 0.176913    ), Coef('Var'  , 0.175553    ), Coef('Var'  , 0.176658    ), Coef('Var'  , 0.212725    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0536173   ), Coef('Var'  , 0.10814     ), Coef('Var'  , 0.174663    ), Coef('Var'  , 0.243688    ), Coef('Var'  , 0.371045    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0424091   ), Coef('Var'  , 0.0846196   ), Coef('Var'  , 0.121699    ), Coef('Var'  , 0.158904    ), Coef('Var'  , 0.20429     ), Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0225659   ), Coef('Var'  , 0.04428     ), Coef('Var'  , 0.0506841   ), Coef('Var'  , 0.0559962   ), Coef('Var'  , 0.0281182   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0229811   ), Coef('Var'  , 0.0446111   ), Coef('Var'  , 0.0481686   ), Coef('Var'  , 0.0495145   ), Coef('Var'  , 0.0251874   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0217391   ), Coef('Var'  , 0.0418742   ), Coef('Var'  , 0.0435484   ), Coef('Var'  , 0.0420289   ), Coef('Var'  , 0.0218094   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.021851    ), Coef('Var'  , 0.0434645   ), Coef('Var'  , 0.0415334   ), Coef('Var'  , 0.0387113   ), Coef('Var'  , 0.0196825   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0302835   ), Coef('Var'  , 0.0602434   ), Coef('Var'  , 0.0542431   ), Coef('Var'  , 0.0471697   ), Coef('Var'  , 0.0239597   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.25        ), Coef('Var'  , 0.199888    ), Coef('Var'  , 0.150329    ), Coef('Var'  , 0.113994    ), Coef('Var'  , 0.0779219   ), Coef('Var'  , 0.0391068   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.5         ), Coef('Var'  , 0.371837    ), Coef('Var'  , 0.245525    ), Coef('Var'  , 0.175914    ), Coef('Var'  , 0.109407    ), Coef('Var'  , 0.0540764   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), ], ])
	etat1.initMat[Chem([Sub('1')])] = FMat([
		[Coef('Var'  , 0.112687    ), Coef('Var'  , 0.109662    ), Coef('Var'  , 0.108638    ), Coef('Var'  , 0.129381    ), Coef('Var'  , 0.151612    ), Coef('Var'  , 0.163173    ), Coef('Var'  , 0.176658    ), Coef('Var'  , 0.157387    ), Coef('Var'  , 0.140933    ), Coef('Var'  , 0.125391    ), ], 
		[Coef('Var'  , 0.117763    ), Coef('Var'  , 0.126386    ), Coef('Var'  , 0.137501    ), Coef('Var'  , 0.188268    ), Coef('Var'  , 0.242299    ), Coef('Var'  , 0.241322    ), Coef('Var'  , 0.243688    ), Coef('Var'  , 0.190478    ), Coef('Var'  , 0.140104    ), Coef('Var'  , 0.127826    ), ], 
		[Coef('Var'  , 0.127213    ), Coef('Var'  , 0.13924     ), Coef('Var'  , 0.152185    ), Coef('Var'  , 0.166634    ), Coef('Var'  , 0.183168    ), Coef('Var'  , 0.170318    ), Coef('Var'  , 0.158904    ), Coef('Var'  , 0.139841    ), Coef('Var'  , 0.120829    ), Coef('Var'  , 0.124186    ), ], 
		[Coef('Var'  , 0.10003     ), Coef('Var'  , 0.117044    ), Coef('Var'  , 0.136111    ), Coef('Var'  , 0.119355    ), Coef('Var'  , 0.105425    ), Coef('Var'  , 0.0802462   ), Coef('Var'  , 0.0559962   ), Coef('Var'  , 0.0645597   ), Coef('Var'  , 0.0721882   ), Coef('Var'  , 0.0862583   ), ], 
		[Coef('Var'  , 0.0910364   ), Coef('Var'  , 0.0967076   ), Coef('Var'  , 0.103082    ), Coef('Var'  , 0.0882802   ), Coef('Var'  , 0.0745156   ), Coef('Var'  , 0.062311    ), Coef('Var'  , 0.0495145   ), Coef('Var'  , 0.0608767   ), Coef('Var'  , 0.0702079   ), Coef('Var'  , 0.0812403   ), ], 
		[Coef('Var'  , 0.07918     ), Coef('Var'  , 0.0758574   ), Coef('Var'  , 0.0710875   ), Coef('Var'  , 0.0593091   ), Coef('Var'  , 0.0455124   ), Coef('Var'  , 0.0451886   ), Coef('Var'  , 0.0420289   ), Coef('Var'  , 0.0547388   ), Coef('Var'  , 0.0643668   ), Coef('Var'  , 0.0728569   ), ], 
		[Coef('Var'  , 0.079083    ), Coef('Var'  , 0.0747742   ), Coef('Var'  , 0.0683352   ), Coef('Var'  , 0.0561651   ), Coef('Var'  , 0.0415958   ), Coef('Var'  , 0.0410231   ), Coef('Var'  , 0.0387113   ), Coef('Var'  , 0.0514367   ), Coef('Var'  , 0.063016    ), Coef('Var'  , 0.0717039   ), ], 
		[Coef('Var'  , 0.0881704   ), Coef('Var'  , 0.0796752   ), Coef('Var'  , 0.0692666   ), Coef('Var'  , 0.0573795   ), Coef('Var'  , 0.0430738   ), Coef('Var'  , 0.0460836   ), Coef('Var'  , 0.0471697   ), Coef('Var'  , 0.0630615   ), Coef('Var'  , 0.0776704   ), Coef('Var'  , 0.0835216   ), ], 
		[Coef('Var'  , 0.0944686   ), Coef('Var'  , 0.0843511   ), Coef('Var'  , 0.0723416   ), Coef('Var'  , 0.0631276   ), Coef('Var'  , 0.0514857   ), Coef('Var'  , 0.0653882   ), Coef('Var'  , 0.0779219   ), Coef('Var'  , 0.0927462   ), Coef('Var'  , 0.107365    ), Coef('Var'  , 0.101144    ), ], 
		[Coef('Var'  , 0.110368    ), Coef('Var'  , 0.0963033   ), Coef('Var'  , 0.0814506   ), Coef('Var'  , 0.0721006   ), Coef('Var'  , 0.0613125   ), Coef('Var'  , 0.0849468   ), Coef('Var'  , 0.109407    ), Coef('Var'  , 0.124874    ), Coef('Var'  , 0.14332     ), Coef('Var'  , 0.125871    ), ], ])
	etat1.initMat[Chem([Sub('2')])] = FMat([
		[Coef('Var'  , 0.11161     ), Coef('Var'  , 0.0960427   ), Coef('Var'  , 0.0808751   ), Coef('Var'  , 0.0701705   ), Coef('Var'  , 0.0578717   ), Coef('Var'  , 0.0717788   ), Coef('Var'  , 0.0821299   ), Coef('Var'  , 0.0936008   ), Coef('Var'  , 0.1024      ), Coef('Var'  , 0.107097    ), ], 
		[Coef('Var'  , 0.0748395   ), Coef('Var'  , 0.0610818   ), Coef('Var'  , 0.0455896   ), Coef('Var'  , 0.0439806   ), Coef('Var'  , 0.0403471   ), Coef('Var'  , 0.0536219   ), Coef('Var'  , 0.0645334   ), Coef('Var'  , 0.0751098   ), Coef('Var'  , 0.0835469   ), Coef('Var'  , 0.0800597   ), ], 
		[Coef('Var'  , 0.0822292   ), Coef('Var'  , 0.067457    ), Coef('Var'  , 0.0503572   ), Coef('Var'  , 0.0518324   ), Coef('Var'  , 0.050833    ), Coef('Var'  , 0.0680611   ), Coef('Var'  , 0.0824904   ), Coef('Var'  , 0.0921089   ), Coef('Var'  , 0.0990545   ), Coef('Var'  , 0.0918575   ), ], 
		[Coef('Var'  , 0.0646717   ), Coef('Var'  , 0.0539641   ), Coef('Var'  , 0.0407608   ), Coef('Var'  , 0.0440904   ), Coef('Var'  , 0.0451979   ), Coef('Var'  , 0.0598903   ), Coef('Var'  , 0.0728744   ), Coef('Var'  , 0.0780856   ), Coef('Var'  , 0.0818683   ), Coef('Var'  , 0.0742724   ), ], 
		[Coef('Var'  , 0.0711783   ), Coef('Var'  , 0.0619677   ), Coef('Var'  , 0.0504713   ), Coef('Var'  , 0.0634399   ), Coef('Var'  , 0.0755719   ), Coef('Var'  , 0.0895818   ), Coef('Var'  , 0.104362    ), Coef('Var'  , 0.0980426   ), Coef('Var'  , 0.0921287   ), Coef('Var'  , 0.0824082   ), ], 
		[Coef('Var'  , 0.0696364   ), Coef('Var'  , 0.062943    ), Coef('Var'  , 0.0550443   ), Coef('Var'  , 0.0780335   ), Coef('Var'  , 0.101896    ), Coef('Var'  , 0.113766    ), Coef('Var'  , 0.12925     ), Coef('Var'  , 0.109865    ), Coef('Var'  , 0.0936838   ), Coef('Var'  , 0.0815543   ), ], 
		[Coef('Var'  , 0.0980826   ), Coef('Var'  , 0.11986     ), Coef('Var'  , 0.143695    ), Coef('Var'  , 0.154962    ), Coef('Var'  , 0.169326    ), Coef('Var'  , 0.149043    ), Coef('Var'  , 0.132433    ), Coef('Var'  , 0.116315    ), Coef('Var'  , 0.102885    ), Coef('Var'  , 0.0996017   ), ], 
		[Coef('Var'  , 0.147305    ), Coef('Var'  , 0.19755     ), Coef('Var'  , 0.249646    ), Coef('Var'  , 0.248007    ), Coef('Var'  , 0.248717    ), Coef('Var'  , 0.19608     ), Coef('Var'  , 0.14598     ), Coef('Var'  , 0.13495     ), Coef('Var'  , 0.12594     ), Coef('Var'  , 0.135819    ), ], 
		[Coef('Var'  , 0.133937    ), Coef('Var'  , 0.150496    ), Coef('Var'  , 0.171025    ), Coef('Var'  , 0.157703    ), Coef('Var'  , 0.147151    ), Coef('Var'  , 0.124392    ), Coef('Var'  , 0.103072    ), Coef('Var'  , 0.103829    ), Coef('Var'  , 0.106197    ), Coef('Var'  , 0.118484    ), ], 
		[Coef('Var'  , 0.14651     ), Coef('Var'  , 0.128637    ), Coef('Var'  , 0.112536    ), Coef('Var'  , 0.0877802   ), Coef('Var'  , 0.0630886   ), Coef('Var'  , 0.0737854   ), Coef('Var'  , 0.0828751   ), Coef('Var'  , 0.0980928   ), Coef('Var'  , 0.112296    ), Coef('Var'  , 0.128846    ), ], ])
	etat1.initMat[Chem([Sub('3')])] = FMat([
		[Coef('Var'  , 0.114406    ), Coef('Var'  , 0.108241    ), Coef('Var'  , 0.1024      ), Coef('Var'  , 0.0994694   ), Coef('Var'  , 0.0944848   ), Coef('Var'  , 0.097633    ), Coef('Var'  , 0.0992428   ), Coef('Var'  , 0.105416    ), Coef('Var'  , 0.112687    ), Coef('Var'  , 0.112446    ), ], 
		[Coef('Var'  , 0.103793    ), Coef('Var'  , 0.0940876   ), Coef('Var'  , 0.0835469   ), Coef('Var'  , 0.0832906   ), Coef('Var'  , 0.0814887   ), Coef('Var'  , 0.0911041   ), Coef('Var'  , 0.100522    ), Coef('Var'  , 0.108431    ), Coef('Var'  , 0.117763    ), Coef('Var'  , 0.110258    ), ], 
		[Coef('Var'  , 0.109695    ), Coef('Var'  , 0.105421    ), Coef('Var'  , 0.0990545   ), Coef('Var'  , 0.104499    ), Coef('Var'  , 0.108079    ), Coef('Var'  , 0.117173    ), Coef('Var'  , 0.125811    ), Coef('Var'  , 0.126448    ), Coef('Var'  , 0.127213    ), Coef('Var'  , 0.118915    ), ], 
		[Coef('Var'  , 0.0818196   ), Coef('Var'  , 0.0826161   ), Coef('Var'  , 0.0818683   ), Coef('Var'  , 0.0911496   ), Coef('Var'  , 0.100225    ), Coef('Var'  , 0.106503    ), Coef('Var'  , 0.114669    ), Coef('Var'  , 0.106467    ), Coef('Var'  , 0.10003     ), Coef('Var'  , 0.0911359   ), ], 
		[Coef('Var'  , 0.0836041   ), Coef('Var'  , 0.0884383   ), Coef('Var'  , 0.0921287   ), Coef('Var'  , 0.0992403   ), Coef('Var'  , 0.107137    ), Coef('Var'  , 0.105768    ), Coef('Var'  , 0.106486    ), Coef('Var'  , 0.0982492   ), Coef('Var'  , 0.0910364   ), Coef('Var'  , 0.0878188   ), ], 
		[Coef('Var'  , 0.0784324   ), Coef('Var'  , 0.085907    ), Coef('Var'  , 0.0936838   ), Coef('Var'  , 0.0991285   ), Coef('Var'  , 0.107446    ), Coef('Var'  , 0.100106    ), Coef('Var'  , 0.0954312   ), Coef('Var'  , 0.0872773   ), Coef('Var'  , 0.07918     ), Coef('Var'  , 0.0794626   ), ], 
		[Coef('Var'  , 0.085407    ), Coef('Var'  , 0.0936287   ), Coef('Var'  , 0.102885    ), Coef('Var'  , 0.103755    ), Coef('Var'  , 0.106033    ), Coef('Var'  , 0.0986001   ), Coef('Var'  , 0.09099     ), Coef('Var'  , 0.0857824   ), Coef('Var'  , 0.079083    ), Coef('Var'  , 0.0825904   ), ], 
		[Coef('Var'  , 0.109407    ), Coef('Var'  , 0.117208    ), Coef('Var'  , 0.12594     ), Coef('Var'  , 0.117236    ), Coef('Var'  , 0.109515    ), Coef('Var'  , 0.0993768   ), Coef('Var'  , 0.0886744   ), Coef('Var'  , 0.0891339   ), Coef('Var'  , 0.0881704   ), Coef('Var'  , 0.0990549   ), ], 
		[Coef('Var'  , 0.108122    ), Coef('Var'  , 0.106185    ), Coef('Var'  , 0.106197    ), Coef('Var'  , 0.0982672   ), Coef('Var'  , 0.0912053   ), Coef('Var'  , 0.088496    ), Coef('Var'  , 0.0845436   ), Coef('Var'  , 0.0902975   ), Coef('Var'  , 0.0944686   ), Coef('Var'  , 0.101126    ), ], 
		[Coef('Var'  , 0.125313    ), Coef('Var'  , 0.118267    ), Coef('Var'  , 0.112296    ), Coef('Var'  , 0.103964    ), Coef('Var'  , 0.0943873   ), Coef('Var'  , 0.0952403   ), Coef('Var'  , 0.0936302   ), Coef('Var'  , 0.102498    ), Coef('Var'  , 0.110368    ), Coef('Var'  , 0.117192    ), ], ])
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
	etat1.initMat[Chem([Sub('4')])] = FMat([
		[Coef('Var'  , 0.0808751   ), Coef('Var'  , 0.116673    ), Coef('Var'  , 0.153119    ), Coef('Var'  , 0.201204    ), Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0404689   ), ], 
		[Coef('Var'  , 0.0455896   ), Coef('Var'  , 0.0524679   ), Coef('Var'  , 0.0580585   ), Coef('Var'  , 0.0292226   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0232454   ), ], 
		[Coef('Var'  , 0.0503572   ), Coef('Var'  , 0.0543535   ), Coef('Var'  , 0.0564456   ), Coef('Var'  , 0.0286136   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0257399   ), ], 
		[Coef('Var'  , 0.0407608   ), Coef('Var'  , 0.0418106   ), Coef('Var'  , 0.0404802   ), Coef('Var'  , 0.0208219   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0209887   ), ], 
		[Coef('Var'  , 0.0504713   ), Coef('Var'  , 0.0490118   ), Coef('Var'  , 0.0451405   ), Coef('Var'  , 0.0232817   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0257301   ), ], 
		[Coef('Var'  , 0.0550443   ), Coef('Var'  , 0.0507145   ), Coef('Var'  , 0.0446541   ), Coef('Var'  , 0.0229538   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0277607   ), ], 
		[Coef('Var'  , 0.143695    ), Coef('Var'  , 0.105853    ), Coef('Var'  , 0.0697721   ), Coef('Var'  , 0.0346067   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.196246    ), ], 
		[Coef('Var'  , 0.249646    ), Coef('Var'  , 0.180527    ), Coef('Var'  , 0.11295     ), Coef('Var'  , 0.0562227   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.374304    ), ], 
		[Coef('Var'  , 0.171025    ), Coef('Var'  , 0.169597    ), Coef('Var'  , 0.171836    ), Coef('Var'  , 0.210021    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.209576    ), ], 
		[Coef('Var'  , 0.112536    ), Coef('Var'  , 0.178992    ), Coef('Var'  , 0.247545    ), Coef('Var'  , 0.373053    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0559391   ), ], ])
	etat1.initMat[Chem([Sub('5')])] = FMat([
		[Coef('Var'  , 0.0578717   ), Coef('Var'  , 0.0297016   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0274295   ), Coef('Var'  , 0.0528718   ), Coef('Var'  , 0.0571311   ), ], 
		[Coef('Var'  , 0.0403471   ), Coef('Var'  , 0.0207353   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0202924   ), Coef('Var'  , 0.0395338   ), Coef('Var'  , 0.0410276   ), ], 
		[Coef('Var'  , 0.050833    ), Coef('Var'  , 0.0260925   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.028862    ), Coef('Var'  , 0.0566664   ), Coef('Var'  , 0.0549545   ), ], 
		[Coef('Var'  , 0.0451979   ), Coef('Var'  , 0.0231017   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0288806   ), Coef('Var'  , 0.0572767   ), Coef('Var'  , 0.0519823   ), ], 
		[Coef('Var'  , 0.0755719   ), Coef('Var'  , 0.0377098   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.199115    ), Coef('Var'  , 0.149009    ), Coef('Var'  , 0.111825    ), ], 
		[Coef('Var'  , 0.101896    ), Coef('Var'  , 0.0502728   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.367667    ), Coef('Var'  , 0.237374    ), Coef('Var'  , 0.16794     ), ], 
		[Coef('Var'  , 0.169326    ), Coef('Var'  , 0.208716    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.209174    ), Coef('Var'  , 0.1702      ), Coef('Var'  , 0.16789     ), ], 
		[Coef('Var'  , 0.248717    ), Coef('Var'  , 0.373703    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.055608    ), Coef('Var'  , 0.112015    ), Coef('Var'  , 0.179311    ), ], 
		[Coef('Var'  , 0.147151    ), Coef('Var'  , 0.198126    ), Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0368859   ), Coef('Var'  , 0.0739664   ), Coef('Var'  , 0.110012    ), ], 
		[Coef('Var'  , 0.0630886   ), Coef('Var'  , 0.0318411   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0260856   ), Coef('Var'  , 0.0510862   ), Coef('Var'  , 0.0579267   ), ], ])
	etat1.initMat[Chem([Sub('6')])] = FMat([
		[Coef('Var'  , 0.0786555   ), Coef('Var'  , 0.0392914   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.200448    ), Coef('Var'  , 0.151612    ), Coef('Var'  , 0.114739    ), ], 
		[Coef('Var'  , 0.105383    ), Coef('Var'  , 0.0520803   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.370276    ), Coef('Var'  , 0.242299    ), Coef('Var'  , 0.172357    ), ], 
		[Coef('Var'  , 0.18238     ), Coef('Var'  , 0.215555    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.216029    ), Coef('Var'  , 0.183168    ), Coef('Var'  , 0.181584    ), ], 
		[Coef('Var'  , 0.241578    ), Coef('Var'  , 0.369918    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.052128    ), Coef('Var'  , 0.105425    ), Coef('Var'  , 0.172046    ), ], 
		[Coef('Var'  , 0.148225    ), Coef('Var'  , 0.198701    ), Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0371236   ), Coef('Var'  , 0.0745156   ), Coef('Var'  , 0.110824    ), ], 
		[Coef('Var'  , 0.0566775   ), Coef('Var'  , 0.0286512   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0233792   ), Coef('Var'  , 0.0455124   ), Coef('Var'  , 0.0520305   ), ], 
		[Coef('Var'  , 0.0483462   ), Coef('Var'  , 0.0246059   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0213406   ), Coef('Var'  , 0.0415958   ), Coef('Var'  , 0.0459465   ), ], 
		[Coef('Var'  , 0.0436489   ), Coef('Var'  , 0.0224782   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0221239   ), Coef('Var'  , 0.0430738   ), Coef('Var'  , 0.0446021   ), ], 
		[Coef('Var'  , 0.0447638   ), Coef('Var'  , 0.0229702   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0262815   ), Coef('Var'  , 0.0514857   ), Coef('Var'  , 0.0492517   ), ], 
		[Coef('Var'  , 0.0503424   ), Coef('Var'  , 0.0257491   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0308704   ), Coef('Var'  , 0.0613125   ), Coef('Var'  , 0.0566195   ), ], ])
	etat1.initMat[Chem([Sub('7')])] = FMat([
		[Coef('Var'  , 0.0821299   ), Coef('Var'  , 0.0695067   ), Coef('Var'  , 0.0528718   ), Coef('Var'  , 0.0539089   ), Coef('Var'  , 0.0512302   ), Coef('Var'  , 0.0667577   ), Coef('Var'  , 0.0790491   ), Coef('Var'  , 0.088224    ), Coef('Var'  , 0.0944848   ), Coef('Var'  , 0.0900229   ), ], 
		[Coef('Var'  , 0.0645334   ), Coef('Var'  , 0.0531789   ), Coef('Var'  , 0.0395338   ), Coef('Var'  , 0.0417595   ), Coef('Var'  , 0.0423891   ), Coef('Var'  , 0.0568121   ), Coef('Var'  , 0.0703938   ), Coef('Var'  , 0.0764124   ), Coef('Var'  , 0.0814887   ), Coef('Var'  , 0.0739539   ), ], 
		[Coef('Var'  , 0.0824904   ), Coef('Var'  , 0.0708306   ), Coef('Var'  , 0.0566664   ), Coef('Var'  , 0.0701632   ), Coef('Var'  , 0.0826407   ), Coef('Var'  , 0.100029    ), Coef('Var'  , 0.117703    ), Coef('Var'  , 0.113087    ), Coef('Var'  , 0.108079    ), Coef('Var'  , 0.0963277   ), ], 
		[Coef('Var'  , 0.0728744   ), Coef('Var'  , 0.0656692   ), Coef('Var'  , 0.0572767   ), Coef('Var'  , 0.0818067   ), Coef('Var'  , 0.106742    ), Coef('Var'  , 0.120616    ), Coef('Var'  , 0.13693     ), Coef('Var'  , 0.117542    ), Coef('Var'  , 0.100225    ), Coef('Var'  , 0.0866412   ), ], 
		[Coef('Var'  , 0.104362    ), Coef('Var'  , 0.125987    ), Coef('Var'  , 0.149009    ), Coef('Var'  , 0.160474    ), Coef('Var'  , 0.173982    ), Coef('Var'  , 0.153718    ), Coef('Var'  , 0.13626     ), Coef('Var'  , 0.120429    ), Coef('Var'  , 0.107137    ), Coef('Var'  , 0.104942    ), ], 
		[Coef('Var'  , 0.12925     ), Coef('Var'  , 0.18116     ), Coef('Var'  , 0.237374    ), Coef('Var'  , 0.236315    ), Coef('Var'  , 0.239013    ), Coef('Var'  , 0.183708    ), Coef('Var'  , 0.131889    ), Coef('Var'  , 0.117817    ), Coef('Var'  , 0.107446    ), Coef('Var'  , 0.11625     ), ], 
		[Coef('Var'  , 0.132433    ), Coef('Var'  , 0.149501    ), Coef('Var'  , 0.1702      ), Coef('Var'  , 0.157447    ), Coef('Var'  , 0.147478    ), Coef('Var'  , 0.125236    ), Coef('Var'  , 0.10414     ), Coef('Var'  , 0.10473     ), Coef('Var'  , 0.106033    ), Coef('Var'  , 0.118094    ), ], 
		[Coef('Var'  , 0.14598     ), Coef('Var'  , 0.127985    ), Coef('Var'  , 0.112015    ), Coef('Var'  , 0.0865461   ), Coef('Var'  , 0.0613301   ), Coef('Var'  , 0.071002    ), Coef('Var'  , 0.079266    ), Coef('Var'  , 0.0947265   ), Coef('Var'  , 0.109515    ), Coef('Var'  , 0.12704     ), ], 
		[Coef('Var'  , 0.103072    ), Coef('Var'  , 0.0881512   ), Coef('Var'  , 0.0739664   ), Coef('Var'  , 0.0612203   ), Coef('Var'  , 0.0480701   ), Coef('Var'  , 0.0593931   ), Coef('Var'  , 0.0691759   ), Coef('Var'  , 0.0807622   ), Coef('Var'  , 0.0912053   ), Coef('Var'  , 0.0969689   ), ], 
		[Coef('Var'  , 0.0828751   ), Coef('Var'  , 0.06803     ), Coef('Var'  , 0.0510862   ), Coef('Var'  , 0.0503594   ), Coef('Var'  , 0.0471251   ), Coef('Var'  , 0.0627288   ), Coef('Var'  , 0.0751934   ), Coef('Var'  , 0.0862703   ), Coef('Var'  , 0.0943873   ), Coef('Var'  , 0.0897597   ), ], ])
	etat1.initMat[Chem([Sub('8')])] = FMat([
		[Coef('Var'  , 0.0552626   ), Coef('Var'  , 0.067517    ), Coef('Var'  , 0.0786555   ), Coef('Var'  , 0.0932243   ), Coef('Var'  , 0.108638    ), Coef('Var'  , 0.10362     ), Coef('Var'  , 0.0992428   ), Coef('Var'  , 0.0899655   ), Coef('Var'  , 0.0790491   ), Coef('Var'  , 0.0685039   ), ], 
		[Coef('Var'  , 0.0543034   ), Coef('Var'  , 0.0791993   ), Coef('Var'  , 0.105383    ), Coef('Var'  , 0.120072    ), Coef('Var'  , 0.137501    ), Coef('Var'  , 0.118028    ), Coef('Var'  , 0.100522    ), Coef('Var'  , 0.0853817   ), Coef('Var'  , 0.0703938   ), Coef('Var'  , 0.062464    ), ], 
		[Coef('Var'  , 0.156392    ), Coef('Var'  , 0.168368    ), Coef('Var'  , 0.18238     ), Coef('Var'  , 0.16616     ), Coef('Var'  , 0.152185    ), Coef('Var'  , 0.138419    ), Coef('Var'  , 0.125811    ), Coef('Var'  , 0.121541    ), Coef('Var'  , 0.117703    ), Coef('Var'  , 0.13654     ), ], 
		[Coef('Var'  , 0.242251    ), Coef('Var'  , 0.24024     ), Coef('Var'  , 0.241578    ), Coef('Var'  , 0.187145    ), Coef('Var'  , 0.136111    ), Coef('Var'  , 0.123877    ), Coef('Var'  , 0.114669    ), Coef('Var'  , 0.12434     ), Coef('Var'  , 0.13693     ), Coef('Var'  , 0.188012    ), ], 
		[Coef('Var'  , 0.173826    ), Coef('Var'  , 0.159989    ), Coef('Var'  , 0.148225    ), Coef('Var'  , 0.124857    ), Coef('Var'  , 0.103082    ), Coef('Var'  , 0.103855    ), Coef('Var'  , 0.106486    ), Coef('Var'  , 0.120058    ), Coef('Var'  , 0.13626     ), Coef('Var'  , 0.153648    ), ], 
		[Coef('Var'  , 0.104465    ), Coef('Var'  , 0.0804407   ), Coef('Var'  , 0.0566775   ), Coef('Var'  , 0.0645811   ), Coef('Var'  , 0.0710875   ), Coef('Var'  , 0.0832796   ), Coef('Var'  , 0.0954312   ), Coef('Var'  , 0.11241     ), Coef('Var'  , 0.131889    ), Coef('Var'  , 0.11685     ), ], 
		[Coef('Var'  , 0.0746784   ), Coef('Var'  , 0.0618788   ), Coef('Var'  , 0.0483462   ), Coef('Var'  , 0.0594304   ), Coef('Var'  , 0.0683352   ), Coef('Var'  , 0.0806572   ), Coef('Var'  , 0.09099     ), Coef('Var'  , 0.0977948   ), Coef('Var'  , 0.10414     ), Coef('Var'  , 0.089235    ), ], 
		[Coef('Var'  , 0.0488362   ), Coef('Var'  , 0.0474598   ), Coef('Var'  , 0.0436489   ), Coef('Var'  , 0.0577337   ), Coef('Var'  , 0.0692666   ), Coef('Var'  , 0.0799697   ), Coef('Var'  , 0.0886744   ), Coef('Var'  , 0.0847781   ), Coef('Var'  , 0.079266    ), Coef('Var'  , 0.0650455   ), ], 
		[Coef('Var'  , 0.0429362   ), Coef('Var'  , 0.0448973   ), Coef('Var'  , 0.0447638   ), Coef('Var'  , 0.0598163   ), Coef('Var'  , 0.0723416   ), Coef('Var'  , 0.0796386   ), Coef('Var'  , 0.0845436   ), Coef('Var'  , 0.0778511   ), Coef('Var'  , 0.0691759   ), Coef('Var'  , 0.0569857   ), ], 
		[Coef('Var'  , 0.0470489   ), Coef('Var'  , 0.0500105   ), Coef('Var'  , 0.0503424   ), Coef('Var'  , 0.0669793   ), Coef('Var'  , 0.0814506   ), Coef('Var'  , 0.0886552   ), Coef('Var'  , 0.0936302   ), Coef('Var'  , 0.08588     ), Coef('Var'  , 0.0751934   ), Coef('Var'  , 0.0627164   ), ], ])
	etat1.initMat[Chem([Sub('9')])] = FMat([
		[Coef('Var'  , 0.153119    ), Coef('Var'  , 0.131778    ), Coef('Var'  , 0.11161     ), Coef('Var'  , 0.112291    ), Coef('Var'  , 0.114406    ), Coef('Var'  , 0.126379    ), Coef('Var'  , 0.140933    ), Coef('Var'  , 0.157491    ), Coef('Var'  , 0.176913    ), Coef('Var'  , 0.164032    ), ], 
		[Coef('Var'  , 0.0580585   ), Coef('Var'  , 0.067059    ), Coef('Var'  , 0.0748395   ), Coef('Var'  , 0.0897008   ), Coef('Var'  , 0.103793    ), Coef('Var'  , 0.121297    ), Coef('Var'  , 0.140104    ), Coef('Var'  , 0.12305     ), Coef('Var'  , 0.10814     ), Coef('Var'  , 0.0828398   ), ], 
		[Coef('Var'  , 0.0564456   ), Coef('Var'  , 0.0703308   ), Coef('Var'  , 0.0822292   ), Coef('Var'  , 0.0969982   ), Coef('Var'  , 0.109695    ), Coef('Var'  , 0.115833    ), Coef('Var'  , 0.120829    ), Coef('Var'  , 0.102961    ), Coef('Var'  , 0.0846196   ), Coef('Var'  , 0.0710227   ), ], 
		[Coef('Var'  , 0.0404802   ), Coef('Var'  , 0.0537974   ), Coef('Var'  , 0.0646717   ), Coef('Var'  , 0.0742945   ), Coef('Var'  , 0.0818196   ), Coef('Var'  , 0.0777605   ), Coef('Var'  , 0.0721882   ), Coef('Var'  , 0.0590073   ), Coef('Var'  , 0.04428     ), Coef('Var'  , 0.0433878   ), ], 
		[Coef('Var'  , 0.0451405   ), Coef('Var'  , 0.0595193   ), Coef('Var'  , 0.0711783   ), Coef('Var'  , 0.0785053   ), Coef('Var'  , 0.0836041   ), Coef('Var'  , 0.077957    ), Coef('Var'  , 0.0702079   ), Coef('Var'  , 0.0586704   ), Coef('Var'  , 0.0446111   ), Coef('Var'  , 0.0462628   ), ], 
		[Coef('Var'  , 0.0446541   ), Coef('Var'  , 0.0581362   ), Coef('Var'  , 0.0696364   ), Coef('Var'  , 0.0747175   ), Coef('Var'  , 0.0784324   ), Coef('Var'  , 0.0724645   ), Coef('Var'  , 0.0643668   ), Coef('Var'  , 0.0546685   ), Coef('Var'  , 0.0418742   ), Coef('Var'  , 0.0446929   ), ], 
		[Coef('Var'  , 0.0697721   ), Coef('Var'  , 0.0832203   ), Coef('Var'  , 0.0980826   ), Coef('Var'  , 0.0912543   ), Coef('Var'  , 0.085407    ), Coef('Var'  , 0.0743949   ), Coef('Var'  , 0.063016    ), Coef('Var'  , 0.0536052   ), Coef('Var'  , 0.0434645   ), Coef('Var'  , 0.0564577   ), ], 
		[Coef('Var'  , 0.11295     ), Coef('Var'  , 0.129469    ), Coef('Var'  , 0.147305    ), Coef('Var'  , 0.127881    ), Coef('Var'  , 0.109407    ), Coef('Var'  , 0.093737    ), Coef('Var'  , 0.0776704   ), Coef('Var'  , 0.0693853   ), Coef('Var'  , 0.0602434   ), Coef('Var'  , 0.0865062   ), ], 
		[Coef('Var'  , 0.171836    ), Coef('Var'  , 0.150941    ), Coef('Var'  , 0.133937    ), Coef('Var'  , 0.119541    ), Coef('Var'  , 0.108122    ), Coef('Var'  , 0.10726     ), Coef('Var'  , 0.107365    ), Coef('Var'  , 0.128527    ), Coef('Var'  , 0.150329    ), Coef('Var'  , 0.159908    ), ], 
		[Coef('Var'  , 0.247545    ), Coef('Var'  , 0.19575     ), Coef('Var'  , 0.14651     ), Coef('Var'  , 0.134817    ), Coef('Var'  , 0.125313    ), Coef('Var'  , 0.132917    ), Coef('Var'  , 0.14332     ), Coef('Var'  , 0.192635    ), Coef('Var'  , 0.245525    ), Coef('Var'  , 0.24489     ), ], ])
	etat1.initMat[Chem([Sub('10')])] = FMat([
		[Coef('Const', 0           ), Coef('Var'  , 0.0282257   ), Coef('Var'  , 0.0552626   ), Coef('Var'  , 0.0547051   ), Coef('Var'  , 0.0512302   ), Coef('Var'  , 0.0264794   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.027119    ), Coef('Var'  , 0.0543034   ), Coef('Var'  , 0.0485861   ), Coef('Var'  , 0.0423891   ), Coef('Var'  , 0.0214671   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.25        ), Coef('Var'  , 0.202813    ), Coef('Var'  , 0.156392    ), Coef('Var'  , 0.119114    ), Coef('Var'  , 0.0826407   ), Coef('Var'  , 0.0413011   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.5         ), Coef('Var'  , 0.370322    ), Coef('Var'  , 0.242251    ), Coef('Var'  , 0.173249    ), Coef('Var'  , 0.106742    ), Coef('Var'  , 0.0529261   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0.25        ), Coef('Var'  , 0.211288    ), Coef('Var'  , 0.173826    ), Coef('Var'  , 0.172646    ), Coef('Var'  , 0.173982    ), Coef('Var'  , 0.211359    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0517895   ), Coef('Var'  , 0.104465    ), Coef('Var'  , 0.170437    ), Coef('Var'  , 0.239013    ), Coef('Var'  , 0.368648    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0372729   ), Coef('Var'  , 0.0746784   ), Coef('Var'  , 0.110546    ), Coef('Var'  , 0.147478    ), Coef('Var'  , 0.198274    ), Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0249816   ), Coef('Var'  , 0.0488362   ), Coef('Var'  , 0.0559197   ), Coef('Var'  , 0.0613301   ), Coef('Var'  , 0.0309381   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0219271   ), Coef('Var'  , 0.0429362   ), Coef('Var'  , 0.0462615   ), Coef('Var'  , 0.0480701   ), Coef('Var'  , 0.0243345   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0242614   ), Coef('Var'  , 0.0470489   ), Coef('Var'  , 0.0485352   ), Coef('Var'  , 0.0471251   ), Coef('Var'  , 0.0242738   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], ])
	
	
	
	etat2.bords   = {Bord('0'): etat13, Bord('1'): etat13, Bord('2'): etat13, Bord('3'): etat13, Bord('4'): etat13, }
	etat2.permuts = {}
	etat2.interns = {Intern('_'): etat2, }
	etat2.subs    = {Sub('0'): etat1, Sub('1'): etat3, Sub('2'): etat4, Sub('3'): etat5, Sub('G', True): Etat.etatPoint, Sub('4'): etat6, Sub('5'): etat7, Sub('6'): etat8, Sub('7'): etat9, Sub('8'): etat10, Sub('9'): etat11, Sub('10'): etat12, }
	
	etat2.buildIntern()
	
	
	etat2.eqs = [
		(Chem([Bord('3'), Sub('1'), Permut('0'), ])	,	Chem([Sub('0'), Bord('0'), ])),
		(Chem([Bord('4'), Sub('0'), Permut('0'), ])	,	Chem([Sub('0'), Bord('4'), ])),
		(Chem([Bord('2'), Sub('0'), Permut('0'), ])	,	Chem([Sub('1'), Bord('2'), ])),
		(Chem([Bord('1'), Sub('1'), Permut('0'), ])	,	Chem([Sub('1'), Bord('3'), ])),
		(Chem([Bord('0'), Sub('0'), Permut('0'), ])	,	Chem([Sub('4'), Bord('1'), ])),
		(Chem([Bord('4'), Sub('1'), Permut('0'), ])	,	Chem([Sub('4'), Bord('2'), ])),
		(Chem([Bord('3'), Sub('0'), Permut('0'), ])	,	Chem([Sub('6'), Bord('2'), ])),
		(Chem([Bord('2'), Sub('1'), Permut('0'), ])	,	Chem([Sub('6'), Bord('3'), ])),
		(Chem([Bord('1'), Sub('0'), Permut('0'), ])	,	Chem([Sub('9'), Bord('3'), ])),
		(Chem([Bord('0'), Sub('1'), Permut('0'), ])	,	Chem([Sub('9'), Bord('4'), ])),
		(Chem([Sub('0'), Bord('0'), Bord('1'), ])	,	Chem([Sub('6'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('1'), Bord('1'), ])	,	Chem([Sub('10'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('2'), Bord('1'), ])	,	Chem([Sub('5'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('3'), Bord('1'), ])	,	Chem([Sub('4'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('0'), Bord('1'), ])	,	Chem([Sub('8'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('1'), Bord('1'), ])	,	Chem([Sub('6'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('3'), Bord('1'), ])	,	Chem([Sub('9'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('4'), Bord('1'), ])	,	Chem([Sub('3'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('0'), Bord('1'), ])	,	Chem([Sub('4'), Bord('4'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('1'), Bord('1'), ])	,	Chem([Sub('5'), Bord('4'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('2'), Bord('1'), ])	,	Chem([Sub('7'), Bord('4'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('3'), Bord('1'), ])	,	Chem([Sub('3'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('4'), Bord('1'), ])	,	Chem([Sub('9'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('3'), Bord('1'), Bord('1'), ])	,	Chem([Sub('7'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('3'), Bord('2'), Bord('1'), ])	,	Chem([Sub('8'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('3'), Bord('4'), Bord('1'), ])	,	Chem([Sub('9'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('4'), Bord('0'), Bord('1'), ])	,	Chem([Sub('9'), Bord('4'), Bord('1'), ])),
		(Chem([Sub('4'), Bord('3'), Bord('1'), ])	,	Chem([Sub('5'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('5'), Bord('2'), Bord('1'), ])	,	Chem([Sub('10'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('5'), Bord('3'), Bord('1'), ])	,	Chem([Sub('7'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('6'), Bord('0'), Bord('1'), ])	,	Chem([Sub('10'), Bord('4'), Bord('1'), ])),
		(Chem([Sub('6'), Bord('4'), Bord('1'), ])	,	Chem([Sub('8'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('7'), Bord('1'), Bord('1'), ])	,	Chem([Sub('10'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('7'), Bord('2'), Bord('1'), ])	,	Chem([Sub('8'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('8'), Bord('4'), Bord('1'), ])	,	Chem([Sub('10'), Bord('0'), Bord('1'), ])),
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
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.039682    ), Coef('Var'  , 0.0794675   ), Coef('Var'  , 0.11557     ), Coef('Var'  , 0.152598    ), Coef('Var'  , 0.200888    ), Coef('Const', 0.25        ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.023556    ), Coef('Var'  , 0.0463443   ), Coef('Var'  , 0.0518631   ), Coef('Var'  , 0.0566139   ), Coef('Var'  , 0.0283071   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0246478   ), Coef('Var'  , 0.0477676   ), Coef('Var'  , 0.0520405   ), Coef('Var'  , 0.0535527   ), Coef('Var'  , 0.0273927   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0221876   ), Coef('Var'  , 0.042892    ), Coef('Var'  , 0.0444361   ), Coef('Var'  , 0.042972    ), Coef('Var'  , 0.0222485   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0246475   ), Coef('Var'  , 0.0481751   ), Coef('Var'  , 0.0462822   ), Coef('Var'  , 0.0418925   ), Coef('Var'  , 0.0216347   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0285205   ), Coef('Var'  , 0.0570352   ), Coef('Var'  , 0.0524257   ), Coef('Var'  , 0.0469625   ), Coef('Var'  , 0.0239052   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.198061    ), Coef('Var'  , 0.146762    ), Coef('Var'  , 0.109189    ), Coef('Var'  , 0.0724024   ), Coef('Var'  , 0.0361286   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.370247    ), Coef('Var'  , 0.24238     ), Coef('Var'  , 0.173549    ), Coef('Var'  , 0.107778    ), Coef('Var'  , 0.0533019   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.211063    ), Coef('Var'  , 0.173784    ), Coef('Var'  , 0.172564    ), Coef('Var'  , 0.17454     ), Coef('Var'  , 0.211501    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0573877   ), Coef('Var'  , 0.115393    ), Coef('Var'  , 0.18208     ), Coef('Var'  , 0.250689    ), Coef('Var'  , 0.374692    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), ], ])
	etat2.initMat[Chem([Sub('1')])] = FMat([
		[Coef('Var'  , 0.0503847   ), Coef('Var'  , 0.0487951   ), Coef('Var'  , 0.0456239   ), Coef('Var'  , 0.0233139   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0254813   ), ], 
		[Coef('Var'  , 0.0603594   ), Coef('Var'  , 0.0557685   ), Coef('Var'  , 0.0495513   ), Coef('Var'  , 0.0253557   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0304128   ), ], 
		[Coef('Var'  , 0.151191    ), Coef('Var'  , 0.11415     ), Coef('Var'  , 0.0778267   ), Coef('Var'  , 0.0389106   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.20024     ), ], 
		[Coef('Var'  , 0.243725    ), Coef('Var'  , 0.174657    ), Coef('Var'  , 0.107875    ), Coef('Var'  , 0.0535219   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.371135    ), ], 
		[Coef('Var'  , 0.169897    ), Coef('Var'  , 0.168665    ), Coef('Var'  , 0.17046     ), Coef('Var'  , 0.209482    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.209183    ), ], 
		[Coef('Var'  , 0.107327    ), Coef('Var'  , 0.173074    ), Coef('Var'  , 0.241924    ), Coef('Var'  , 0.369986    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0530874   ), ], 
		[Coef('Var'  , 0.07376     ), Coef('Var'  , 0.109979    ), Coef('Var'  , 0.147124    ), Coef('Var'  , 0.198156    ), Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0368236   ), ], 
		[Coef('Var'  , 0.0456625   ), Coef('Var'  , 0.0512481   ), Coef('Var'  , 0.0560896   ), Coef('Var'  , 0.0280488   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0231994   ), ], 
		[Coef('Var'  , 0.049221    ), Coef('Var'  , 0.053014    ), Coef('Var'  , 0.0539242   ), Coef('Var'  , 0.027579    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0254351   ), ], 
		[Coef('Var'  , 0.048472    ), Coef('Var'  , 0.0506486   ), Coef('Var'  , 0.0496016   ), Coef('Var'  , 0.0256461   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0250025   ), ], ])
	etat2.initMat[Chem([Sub('2')])] = FMat([
		[Coef('Var'  , 0.15041     ), Coef('Var'  , 0.162312    ), Coef('Var'  , 0.176451    ), Coef('Var'  , 0.158052    ), Coef('Var'  , 0.142346    ), Coef('Var'  , 0.127115    ), Coef('Var'  , 0.113939    ), Coef('Var'  , 0.110194    ), Coef('Var'  , 0.107809    ), Coef('Var'  , 0.12835     ), ], 
		[Coef('Var'  , 0.242118    ), Coef('Var'  , 0.239401    ), Coef('Var'  , 0.24068     ), Coef('Var'  , 0.186743    ), Coef('Var'  , 0.13681     ), Coef('Var'  , 0.125782    ), Coef('Var'  , 0.118032    ), Coef('Var'  , 0.127218    ), Coef('Var'  , 0.139392    ), Coef('Var'  , 0.188985    ), ], 
		[Coef('Var'  , 0.176005    ), Coef('Var'  , 0.162987    ), Coef('Var'  , 0.15197     ), Coef('Var'  , 0.130064    ), Coef('Var'  , 0.109163    ), Coef('Var'  , 0.110248    ), Coef('Var'  , 0.11251     ), Coef('Var'  , 0.125168    ), Coef('Var'  , 0.140146    ), Coef('Var'  , 0.156626    ), ], 
		[Coef('Var'  , 0.10724     ), Coef('Var'  , 0.0823181   ), Coef('Var'  , 0.0578898   ), Coef('Var'  , 0.0664111   ), Coef('Var'  , 0.0738153   ), Coef('Var'  , 0.087515    ), Coef('Var'  , 0.10115     ), Coef('Var'  , 0.118336    ), Coef('Var'  , 0.137736    ), Coef('Var'  , 0.121206    ), ], 
		[Coef('Var'  , 0.0701531   ), Coef('Var'  , 0.0571598   ), Coef('Var'  , 0.0441552   ), Coef('Var'  , 0.0538378   ), Coef('Var'  , 0.0624427   ), Coef('Var'  , 0.0730828   ), Coef('Var'  , 0.0832938   ), Coef('Var'  , 0.0896324   ), Coef('Var'  , 0.0970301   ), Coef('Var'  , 0.082946    ), ], 
		[Coef('Var'  , 0.0497032   ), Coef('Var'  , 0.0497755   ), Coef('Var'  , 0.0468244   ), Coef('Var'  , 0.0619552   ), Coef('Var'  , 0.0733429   ), Coef('Var'  , 0.0834413   ), Coef('Var'  , 0.0903088   ), Coef('Var'  , 0.0858284   ), Coef('Var'  , 0.0791073   ), Coef('Var'  , 0.0655294   ), ], 
		[Coef('Var'  , 0.0411829   ), Coef('Var'  , 0.0410871   ), Coef('Var'  , 0.0391209   ), Coef('Var'  , 0.0517285   ), Coef('Var'  , 0.0630954   ), Coef('Var'  , 0.0708718   ), Coef('Var'  , 0.0774558   ), Coef('Var'  , 0.0729324   ), Coef('Var'  , 0.0665229   ), Coef('Var'  , 0.0550316   ), ], 
		[Coef('Var'  , 0.0470501   ), Coef('Var'  , 0.0506724   ), Coef('Var'  , 0.0509748   ), Coef('Var'  , 0.0671596   ), Coef('Var'  , 0.0805675   ), Coef('Var'  , 0.0867721   ), Coef('Var'  , 0.0903061   ), Coef('Var'  , 0.0831439   ), Coef('Var'  , 0.0726606   ), Coef('Var'  , 0.0617534   ), ], 
		[Coef('Var'  , 0.054536    ), Coef('Var'  , 0.0676898   ), Coef('Var'  , 0.0796166   ), Coef('Var'  , 0.0949803   ), Coef('Var'  , 0.110382    ), Coef('Var'  , 0.105166    ), Coef('Var'  , 0.0995046   ), Coef('Var'  , 0.0896626   ), Coef('Var'  , 0.0776822   ), Coef('Var'  , 0.0674159   ), ], 
		[Coef('Var'  , 0.0616014   ), Coef('Var'  , 0.0865968   ), Coef('Var'  , 0.112317    ), Coef('Var'  , 0.129069    ), Coef('Var'  , 0.148035    ), Coef('Var'  , 0.130006    ), Coef('Var'  , 0.113499    ), Coef('Var'  , 0.0978841   ), Coef('Var'  , 0.0819131   ), Coef('Var'  , 0.0721566   ), ], ])
	etat2.initMat[Chem([Sub('3')])] = FMat([
		[Coef('Var'  , 0.0763047   ), Coef('Var'  , 0.0915771   ), Coef('Var'  , 0.107809    ), Coef('Var'  , 0.102251    ), Coef('Var'  , 0.0971339   ), Coef('Var'  , 0.0859354   ), Coef('Var'  , 0.0735795   ), Coef('Var'  , 0.0627505   ), Coef('Var'  , 0.0503847   ), Coef('Var'  , 0.0634739   ), ], 
		[Coef('Var'  , 0.10756     ), Coef('Var'  , 0.122095    ), Coef('Var'  , 0.139392    ), Coef('Var'  , 0.122184    ), Coef('Var'  , 0.106716    ), Coef('Var'  , 0.0937182   ), Coef('Var'  , 0.0797313   ), Coef('Var'  , 0.0708284   ), Coef('Var'  , 0.0603594   ), Coef('Var'  , 0.0836266   ), ], 
		[Coef('Var'  , 0.175791    ), Coef('Var'  , 0.156502    ), Coef('Var'  , 0.140146    ), Coef('Var'  , 0.125035    ), Coef('Var'  , 0.112215    ), Coef('Var'  , 0.109673    ), Coef('Var'  , 0.108304    ), Coef('Var'  , 0.129189    ), Coef('Var'  , 0.151191    ), Coef('Var'  , 0.16243     ), ], 
		[Coef('Var'  , 0.243259    ), Coef('Var'  , 0.188913    ), Coef('Var'  , 0.137736    ), Coef('Var'  , 0.125384    ), Coef('Var'  , 0.116053    ), Coef('Var'  , 0.125868    ), Coef('Var'  , 0.138534    ), Coef('Var'  , 0.189679    ), Coef('Var'  , 0.243725    ), Coef('Var'  , 0.241988    ), ], 
		[Coef('Var'  , 0.144188    ), Coef('Var'  , 0.119687    ), Coef('Var'  , 0.0970301   ), Coef('Var'  , 0.0974594   ), Coef('Var'  , 0.099902    ), Coef('Var'  , 0.113878    ), Coef('Var'  , 0.130758    ), Coef('Var'  , 0.148689    ), Coef('Var'  , 0.169897    ), Coef('Var'  , 0.155783    ), ], 
		[Coef('Var'  , 0.060201    ), Coef('Var'  , 0.0703904   ), Coef('Var'  , 0.0791073   ), Coef('Var'  , 0.0929136   ), Coef('Var'  , 0.105988    ), Coef('Var'  , 0.121544    ), Coef('Var'  , 0.139027    ), Coef('Var'  , 0.121766    ), Coef('Var'  , 0.107327    ), Coef('Var'  , 0.0834298   ), ], 
		[Coef('Var'  , 0.0476553   ), Coef('Var'  , 0.0581585   ), Coef('Var'  , 0.0665229   ), Coef('Var'  , 0.0778689   ), Coef('Var'  , 0.0877568   ), Coef('Var'  , 0.0945188   ), Coef('Var'  , 0.101563    ), Coef('Var'  , 0.0873404   ), Coef('Var'  , 0.07376     ), Coef('Var'  , 0.0611153   ), ], 
		[Coef('Var'  , 0.045561    ), Coef('Var'  , 0.0609007   ), Coef('Var'  , 0.0726606   ), Coef('Var'  , 0.0812926   ), Coef('Var'  , 0.0870663   ), Coef('Var'  , 0.0808965   ), Coef('Var'  , 0.0735046   ), Coef('Var'  , 0.0601095   ), Coef('Var'  , 0.0456625   ), Coef('Var'  , 0.0467939   ), ], 
		[Coef('Var'  , 0.0493245   ), Coef('Var'  , 0.0650288   ), Coef('Var'  , 0.0776822   ), Coef('Var'  , 0.0858473   ), Coef('Var'  , 0.0912169   ), Coef('Var'  , 0.085482    ), Coef('Var'  , 0.0769104   ), Coef('Var'  , 0.0646714   ), Coef('Var'  , 0.049221    ), Coef('Var'  , 0.0508623   ), ], 
		[Coef('Var'  , 0.0501565   ), Coef('Var'  , 0.066747    ), Coef('Var'  , 0.0819131   ), Coef('Var'  , 0.0897645   ), Coef('Var'  , 0.0959523   ), Coef('Var'  , 0.088486    ), Coef('Var'  , 0.0780883   ), Coef('Var'  , 0.064977    ), Coef('Var'  , 0.048472    ), Coef('Var'  , 0.0504966   ), ], ])
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
	etat2.initMat[Chem([Sub('4')])] = FMat([
		[Coef('Var'  , 0.176451    ), Coef('Var'  , 0.212546    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.212745    ), Coef('Var'  , 0.176875    ), Coef('Var'  , 0.175291    ), ], 
		[Coef('Var'  , 0.24068     ), Coef('Var'  , 0.369298    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0516183   ), Coef('Var'  , 0.104722    ), Coef('Var'  , 0.170916    ), ], 
		[Coef('Var'  , 0.15197     ), Coef('Var'  , 0.200672    ), Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0395768   ), Coef('Var'  , 0.0790001   ), Coef('Var'  , 0.115249    ), ], 
		[Coef('Var'  , 0.0578898   ), Coef('Var'  , 0.0291718   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.023755    ), Coef('Var'  , 0.0463969   ), Coef('Var'  , 0.0529268   ), ], 
		[Coef('Var'  , 0.0441552   ), Coef('Var'  , 0.0223006   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0202393   ), Coef('Var'  , 0.0395251   ), Coef('Var'  , 0.04254     ), ], 
		[Coef('Var'  , 0.0468244   ), Coef('Var'  , 0.0242942   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0238297   ), Coef('Var'  , 0.0460272   ), Coef('Var'  , 0.0481239   ), ], 
		[Coef('Var'  , 0.0391209   ), Coef('Var'  , 0.0199224   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0225209   ), Coef('Var'  , 0.0446583   ), Coef('Var'  , 0.0424432   ), ], 
		[Coef('Var'  , 0.0509748   ), Coef('Var'  , 0.0262252   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0310356   ), Coef('Var'  , 0.0614295   ), Coef('Var'  , 0.0572608   ), ], 
		[Coef('Var'  , 0.0796166   ), Coef('Var'  , 0.0398755   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.200807    ), Coef('Var'  , 0.152176    ), Coef('Var'  , 0.115683    ), ], 
		[Coef('Var'  , 0.112317    ), Coef('Var'  , 0.0556932   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.373872    ), Coef('Var'  , 0.24919     ), Coef('Var'  , 0.179566    ), ], ])
	etat2.initMat[Chem([Sub('5')])] = FMat([
		[Coef('Var'  , 0.142346    ), Coef('Var'  , 0.15825     ), Coef('Var'  , 0.176875    ), Coef('Var'  , 0.163633    ), Coef('Var'  , 0.152598    ), Coef('Var'  , 0.131669    ), Coef('Var'  , 0.111811    ), Coef('Var'  , 0.113664    ), Coef('Var'  , 0.116177    ), Coef('Var'  , 0.128388    ), ], 
		[Coef('Var'  , 0.13681     ), Coef('Var'  , 0.119063    ), Coef('Var'  , 0.104722    ), Coef('Var'  , 0.0799254   ), Coef('Var'  , 0.0566139   ), Coef('Var'  , 0.0663786   ), Coef('Var'  , 0.0755225   ), Coef('Var'  , 0.089714    ), Coef('Var'  , 0.103709    ), Coef('Var'  , 0.119088    ), ], 
		[Coef('Var'  , 0.109163    ), Coef('Var'  , 0.0939684   ), Coef('Var'  , 0.0790001   ), Coef('Var'  , 0.0669695   ), Coef('Var'  , 0.0535527   ), Coef('Var'  , 0.0656744   ), Coef('Var'  , 0.0751963   ), Coef('Var'  , 0.0869343   ), Coef('Var'  , 0.0970432   ), Coef('Var'  , 0.103044    ), ], 
		[Coef('Var'  , 0.0738153   ), Coef('Var'  , 0.0609944   ), Coef('Var'  , 0.0463969   ), Coef('Var'  , 0.0460035   ), Coef('Var'  , 0.042972    ), Coef('Var'  , 0.0565037   ), Coef('Var'  , 0.0670408   ), Coef('Var'  , 0.0762063   ), Coef('Var'  , 0.0832294   ), Coef('Var'  , 0.0791904   ), ], 
		[Coef('Var'  , 0.0624427   ), Coef('Var'  , 0.0517765   ), Coef('Var'  , 0.0395251   ), Coef('Var'  , 0.041874    ), Coef('Var'  , 0.0418925   ), Coef('Var'  , 0.0554071   ), Coef('Var'  , 0.0662866   ), Coef('Var'  , 0.0721668   ), Coef('Var'  , 0.0761808   ), Coef('Var'  , 0.0699316   ), ], 
		[Coef('Var'  , 0.0733429   ), Coef('Var'  , 0.0614908   ), Coef('Var'  , 0.0460272   ), Coef('Var'  , 0.0477349   ), Coef('Var'  , 0.0469625   ), Coef('Var'  , 0.062277    ), Coef('Var'  , 0.0760754   ), Coef('Var'  , 0.0835879   ), Coef('Var'  , 0.0892207   ), Coef('Var'  , 0.0828772   ), ], 
		[Coef('Var'  , 0.0630954   ), Coef('Var'  , 0.054327    ), Coef('Var'  , 0.0446583   ), Coef('Var'  , 0.0586494   ), Coef('Var'  , 0.0724024   ), Coef('Var'  , 0.0859731   ), Coef('Var'  , 0.10022     ), Coef('Var'  , 0.0925222   ), Coef('Var'  , 0.0854711   ), Coef('Var'  , 0.0744839   ), ], 
		[Coef('Var'  , 0.0805675   ), Coef('Var'  , 0.07197     ), Coef('Var'  , 0.0614295   ), Coef('Var'  , 0.0843376   ), Coef('Var'  , 0.107778    ), Coef('Var'  , 0.121967    ), Coef('Var'  , 0.139048    ), Coef('Var'  , 0.121816    ), Coef('Var'  , 0.106421    ), Coef('Var'  , 0.0940862   ), ], 
		[Coef('Var'  , 0.110382    ), Coef('Var'  , 0.130912    ), Coef('Var'  , 0.152176    ), Coef('Var'  , 0.162309    ), Coef('Var'  , 0.17454     ), Coef('Var'  , 0.154505    ), Coef('Var'  , 0.137893    ), Coef('Var'  , 0.123713    ), Coef('Var'  , 0.112272    ), Coef('Var'  , 0.110814    ), ], 
		[Coef('Var'  , 0.148035    ), Coef('Var'  , 0.197248    ), Coef('Var'  , 0.24919     ), Coef('Var'  , 0.248565    ), Coef('Var'  , 0.250689    ), Coef('Var'  , 0.199646    ), Coef('Var'  , 0.150906    ), Coef('Var'  , 0.139676    ), Coef('Var'  , 0.130277    ), Coef('Var'  , 0.138098    ), ], ])
	etat2.initMat[Chem([Sub('6')])] = FMat([
		[Coef('Var'  , 0.0479544   ), Coef('Var'  , 0.0522715   ), Coef('Var'  , 0.0541139   ), Coef('Var'  , 0.0276019   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0246696   ), ], 
		[Coef('Var'  , 0.0461897   ), Coef('Var'  , 0.0472973   ), Coef('Var'  , 0.0453293   ), Coef('Var'  , 0.0234066   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0238907   ), ], 
		[Coef('Var'  , 0.0520746   ), Coef('Var'  , 0.0506397   ), Coef('Var'  , 0.0468985   ), Coef('Var'  , 0.0241259   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0265138   ), ], 
		[Coef('Var'  , 0.0580631   ), Coef('Var'  , 0.052927    ), Coef('Var'  , 0.0463211   ), Coef('Var'  , 0.0236776   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0292494   ), ], 
		[Coef('Var'  , 0.146564    ), Coef('Var'  , 0.109676    ), Coef('Var'  , 0.073619    ), Coef('Var'  , 0.0367935   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.197882    ), ], 
		[Coef('Var'  , 0.24085     ), Coef('Var'  , 0.171149    ), Coef('Var'  , 0.105031    ), Coef('Var'  , 0.0517701   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.369379    ), ], 
		[Coef('Var'  , 0.171441    ), Coef('Var'  , 0.169999    ), Coef('Var'  , 0.171502    ), Coef('Var'  , 0.210036    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.209964    ), ], 
		[Coef('Var'  , 0.105371    ), Coef('Var'  , 0.171911    ), Coef('Var'  , 0.241489    ), Coef('Var'  , 0.369835    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0520759   ), ], 
		[Coef('Var'  , 0.0772253   ), Coef('Var'  , 0.112863    ), Coef('Var'  , 0.149538    ), Coef('Var'  , 0.1993      ), Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0385627   ), ], 
		[Coef('Var'  , 0.0542656   ), Coef('Var'  , 0.0612662   ), Coef('Var'  , 0.066158    ), Coef('Var'  , 0.0334534   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0278128   ), ], ])
	etat2.initMat[Chem([Sub('7')])] = FMat([
		[Coef('Var'  , 0.113939    ), Coef('Var'  , 0.114493    ), Coef('Var'  , 0.116177    ), Coef('Var'  , 0.108957    ), Coef('Var'  , 0.101304    ), Coef('Var'  , 0.0970728   ), Coef('Var'  , 0.0907565   ), Coef('Var'  , 0.0946645   ), Coef('Var'  , 0.0971339   ), Coef('Var'  , 0.105276    ), ], 
		[Coef('Var'  , 0.118032    ), Coef('Var'  , 0.109979    ), Coef('Var'  , 0.103709    ), Coef('Var'  , 0.0968523   ), Coef('Var'  , 0.0891563   ), Coef('Var'  , 0.0914486   ), Coef('Var'  , 0.091019    ), Coef('Var'  , 0.0995414   ), Coef('Var'  , 0.106716    ), Coef('Var'  , 0.111639    ), ], 
		[Coef('Var'  , 0.11251     ), Coef('Var'  , 0.104509    ), Coef('Var'  , 0.0970432   ), Coef('Var'  , 0.0931514   ), Coef('Var'  , 0.0881108   ), Coef('Var'  , 0.0927898   ), Coef('Var'  , 0.0963353   ), Coef('Var'  , 0.104014    ), Coef('Var'  , 0.112215    ), Coef('Var'  , 0.11158     ), ], 
		[Coef('Var'  , 0.10115     ), Coef('Var'  , 0.0922267   ), Coef('Var'  , 0.0832294   ), Coef('Var'  , 0.0840211   ), Coef('Var'  , 0.083437    ), Coef('Var'  , 0.0926659   ), Coef('Var'  , 0.101689    ), Coef('Var'  , 0.10792     ), Coef('Var'  , 0.116053    ), Coef('Var'  , 0.1076      ), ], 
		[Coef('Var'  , 0.0832938   ), Coef('Var'  , 0.07994     ), Coef('Var'  , 0.0761808   ), Coef('Var'  , 0.0815761   ), Coef('Var'  , 0.0862713   ), Coef('Var'  , 0.0933508   ), Coef('Var'  , 0.101403    ), Coef('Var'  , 0.0995417   ), Coef('Var'  , 0.099902    ), Coef('Var'  , 0.0909182   ), ], 
		[Coef('Var'  , 0.0903088   ), Coef('Var'  , 0.0909964   ), Coef('Var'  , 0.0892207   ), Coef('Var'  , 0.0972103   ), Coef('Var'  , 0.10429     ), Coef('Var'  , 0.110438    ), Coef('Var'  , 0.118173    ), Coef('Var'  , 0.11131     ), Coef('Var'  , 0.105988    ), Coef('Var'  , 0.0986458   ), ], 
		[Coef('Var'  , 0.0774558   ), Coef('Var'  , 0.0817433   ), Coef('Var'  , 0.0854711   ), Coef('Var'  , 0.0933588   ), Coef('Var'  , 0.102451    ), Coef('Var'  , 0.101868    ), Coef('Var'  , 0.103371    ), Coef('Var'  , 0.0951887   ), Coef('Var'  , 0.0877568   ), Coef('Var'  , 0.0830676   ), ], 
		[Coef('Var'  , 0.0903061   ), Coef('Var'  , 0.0989895   ), Coef('Var'  , 0.106421    ), Coef('Var'  , 0.111031    ), Coef('Var'  , 0.117195    ), Coef('Var'  , 0.108443    ), Coef('Var'  , 0.101823    ), Coef('Var'  , 0.0945502   ), Coef('Var'  , 0.0870663   ), Coef('Var'  , 0.0898242   ), ], 
		[Coef('Var'  , 0.0995046   ), Coef('Var'  , 0.10577     ), Coef('Var'  , 0.112272    ), Coef('Var'  , 0.110362    ), Coef('Var'  , 0.110466    ), Coef('Var'  , 0.103286    ), Coef('Var'  , 0.0970301   ), Coef('Var'  , 0.0948781   ), Coef('Var'  , 0.0912169   ), Coef('Var'  , 0.0963067   ), ], 
		[Coef('Var'  , 0.113499    ), Coef('Var'  , 0.121353    ), Coef('Var'  , 0.130277    ), Coef('Var'  , 0.12348     ), Coef('Var'  , 0.117319    ), Coef('Var'  , 0.108638    ), Coef('Var'  , 0.0984005   ), Coef('Var'  , 0.0983915   ), Coef('Var'  , 0.0959523   ), Coef('Var'  , 0.105143    ), ], ])
	etat2.initMat[Chem([Sub('8')])] = FMat([
		[Coef('Var'  , 0.0778422   ), Coef('Var'  , 0.0644301   ), Coef('Var'  , 0.0479544   ), Coef('Var'  , 0.0479835   ), Coef('Var'  , 0.0456239   ), Coef('Var'  , 0.0605832   ), Coef('Var'  , 0.0735795   ), Coef('Var'  , 0.0832677   ), Coef('Var'  , 0.0907565   ), Coef('Var'  , 0.0857588   ), ], 
		[Coef('Var'  , 0.0731338   ), Coef('Var'  , 0.0614423   ), Coef('Var'  , 0.0461897   ), Coef('Var'  , 0.0492464   ), Coef('Var'  , 0.0495513   ), Coef('Var'  , 0.0657713   ), Coef('Var'  , 0.0797313   ), Coef('Var'  , 0.0866544   ), Coef('Var'  , 0.091019    ), Coef('Var'  , 0.0837904   ), ], 
		[Coef('Var'  , 0.0739144   ), Coef('Var'  , 0.0640455   ), Coef('Var'  , 0.0520746   ), Coef('Var'  , 0.0654244   ), Coef('Var'  , 0.0778267   ), Coef('Var'  , 0.09286     ), Coef('Var'  , 0.108304    ), Coef('Var'  , 0.10224     ), Coef('Var'  , 0.0963353   ), Coef('Var'  , 0.0858227   ), ], 
		[Coef('Var'  , 0.0740269   ), Coef('Var'  , 0.066591    ), Coef('Var'  , 0.0580631   ), Coef('Var'  , 0.0827713   ), Coef('Var'  , 0.107875    ), Coef('Var'  , 0.122066    ), Coef('Var'  , 0.138534    ), Coef('Var'  , 0.11914     ), Coef('Var'  , 0.101689    ), Coef('Var'  , 0.0879376   ), ], 
		[Coef('Var'  , 0.100345    ), Coef('Var'  , 0.122748    ), Coef('Var'  , 0.146564    ), Coef('Var'  , 0.157365    ), Coef('Var'  , 0.17046     ), Coef('Var'  , 0.148988    ), Coef('Var'  , 0.130758    ), Coef('Var'  , 0.114675    ), Coef('Var'  , 0.101403    ), Coef('Var'  , 0.100035    ), ], 
		[Coef('Var'  , 0.137344    ), Coef('Var'  , 0.187144    ), Coef('Var'  , 0.24085     ), Coef('Var'  , 0.239365    ), Coef('Var'  , 0.241924    ), Coef('Var'  , 0.188665    ), Coef('Var'  , 0.139027    ), Coef('Var'  , 0.127123    ), Coef('Var'  , 0.118173    ), Coef('Var'  , 0.126209    ), ], 
		[Coef('Var'  , 0.13256     ), Coef('Var'  , 0.150356    ), Coef('Var'  , 0.171441    ), Coef('Var'  , 0.158119    ), Coef('Var'  , 0.147124    ), Coef('Var'  , 0.123672    ), Coef('Var'  , 0.101563    ), Coef('Var'  , 0.101703    ), Coef('Var'  , 0.103371    ), Coef('Var'  , 0.116579    ), ], 
		[Coef('Var'  , 0.1368      ), Coef('Var'  , 0.119591    ), Coef('Var'  , 0.105371    ), Coef('Var'  , 0.0801247   ), Coef('Var'  , 0.0560896   ), Coef('Var'  , 0.0649588   ), Coef('Var'  , 0.0735046   ), Coef('Var'  , 0.0874738   ), Coef('Var'  , 0.101823    ), Coef('Var'  , 0.118079    ), ], 
		[Coef('Var'  , 0.106693    ), Coef('Var'  , 0.0915431   ), Coef('Var'  , 0.0772253   ), Coef('Var'  , 0.0661416   ), Coef('Var'  , 0.0539242   ), Coef('Var'  , 0.0668153   ), Coef('Var'  , 0.0769104   ), Coef('Var'  , 0.0878687   ), Coef('Var'  , 0.0970301   ), Coef('Var'  , 0.101613    ), ], 
		[Coef('Var'  , 0.087341    ), Coef('Var'  , 0.0721095   ), Coef('Var'  , 0.0542656   ), Coef('Var'  , 0.0534589   ), Coef('Var'  , 0.0496016   ), Coef('Var'  , 0.0656205   ), Coef('Var'  , 0.0780883   ), Coef('Var'  , 0.0898544   ), Coef('Var'  , 0.0984005   ), Coef('Var'  , 0.0941767   ), ], ])
	etat2.initMat[Chem([Sub('9')])] = FMat([
		[Coef('Const', 0.25        ), Coef('Var'  , 0.199766    ), Coef('Var'  , 0.15041     ), Coef('Var'  , 0.112759    ), Coef('Var'  , 0.0763047   ), Coef('Var'  , 0.0379926   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.5         ), Coef('Var'  , 0.370103    ), Coef('Var'  , 0.242118    ), Coef('Var'  , 0.173317    ), Coef('Var'  , 0.10756     ), Coef('Var'  , 0.0532138   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0.25        ), Coef('Var'  , 0.212314    ), Coef('Var'  , 0.176005    ), Coef('Var'  , 0.174505    ), Coef('Var'  , 0.175791    ), Coef('Var'  , 0.212191    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0531463   ), Coef('Var'  , 0.10724     ), Coef('Var'  , 0.173999    ), Coef('Var'  , 0.243259    ), Coef('Var'  , 0.370853    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0348592   ), Coef('Var'  , 0.0701531   ), Coef('Var'  , 0.106459    ), Coef('Var'  , 0.144188    ), Coef('Var'  , 0.1966      ), Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0254813   ), Coef('Var'  , 0.0497032   ), Coef('Var'  , 0.0558236   ), Coef('Var'  , 0.060201    ), Coef('Var'  , 0.0303423   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0211647   ), Coef('Var'  , 0.0411829   ), Coef('Var'  , 0.0454563   ), Coef('Var'  , 0.0476553   ), Coef('Var'  , 0.0242916   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0244472   ), Coef('Var'  , 0.0470501   ), Coef('Var'  , 0.0480418   ), Coef('Var'  , 0.045561    ), Coef('Var'  , 0.0235946   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0278143   ), Coef('Var'  , 0.054536    ), Coef('Var'  , 0.0532415   ), Coef('Var'  , 0.0493245   ), Coef('Var'  , 0.0254272   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0309036   ), Coef('Var'  , 0.0616014   ), Coef('Var'  , 0.0563976   ), Coef('Var'  , 0.0501565   ), Coef('Var'  , 0.0254941   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], ])
	etat2.initMat[Chem([Sub('10')])] = FMat([
		[Coef('Var'  , 0.0541139   ), Coef('Var'  , 0.0673624   ), Coef('Var'  , 0.0778422   ), Coef('Var'  , 0.0908349   ), Coef('Var'  , 0.101304    ), Coef('Var'  , 0.106855    ), Coef('Var'  , 0.111811    ), Coef('Var'  , 0.095463    ), Coef('Var'  , 0.0794675   ), Coef('Var'  , 0.067284    ), ], 
		[Coef('Var'  , 0.0453293   ), Coef('Var'  , 0.0609582   ), Coef('Var'  , 0.0731338   ), Coef('Var'  , 0.0827614   ), Coef('Var'  , 0.0891563   ), Coef('Var'  , 0.0832813   ), Coef('Var'  , 0.0755225   ), Coef('Var'  , 0.0616275   ), Coef('Var'  , 0.0463443   ), Coef('Var'  , 0.0469626   ), ], 
		[Coef('Var'  , 0.0468985   ), Coef('Var'  , 0.0616576   ), Coef('Var'  , 0.0739144   ), Coef('Var'  , 0.0820305   ), Coef('Var'  , 0.0881108   ), Coef('Var'  , 0.0827805   ), Coef('Var'  , 0.0751963   ), Coef('Var'  , 0.0629296   ), Coef('Var'  , 0.0477676   ), Coef('Var'  , 0.0487737   ), ], 
		[Coef('Var'  , 0.0463211   ), Coef('Var'  , 0.0610193   ), Coef('Var'  , 0.0740269   ), Coef('Var'  , 0.0794117   ), Coef('Var'  , 0.083437    ), Coef('Var'  , 0.0763252   ), Coef('Var'  , 0.0670408   ), Coef('Var'  , 0.0564428   ), Coef('Var'  , 0.042892    ), Coef('Var'  , 0.0458652   ), ], 
		[Coef('Var'  , 0.073619    ), Coef('Var'  , 0.0866596   ), Coef('Var'  , 0.100345    ), Coef('Var'  , 0.0930478   ), Coef('Var'  , 0.0862713   ), Coef('Var'  , 0.0769542   ), Coef('Var'  , 0.0662866   ), Coef('Var'  , 0.05842     ), Coef('Var'  , 0.0481751   ), Coef('Var'  , 0.061441    ), ], 
		[Coef('Var'  , 0.105031    ), Coef('Var'  , 0.119535    ), Coef('Var'  , 0.137344    ), Coef('Var'  , 0.119759    ), Coef('Var'  , 0.10429     ), Coef('Var'  , 0.0903659   ), Coef('Var'  , 0.0760754   ), Coef('Var'  , 0.0668923   ), Coef('Var'  , 0.0570352   ), Coef('Var'  , 0.0802907   ), ], 
		[Coef('Var'  , 0.171502    ), Coef('Var'  , 0.150427    ), Coef('Var'  , 0.13256     ), Coef('Var'  , 0.116073    ), Coef('Var'  , 0.102451    ), Coef('Var'  , 0.100526    ), Coef('Var'  , 0.10022     ), Coef('Var'  , 0.122905    ), Coef('Var'  , 0.146762    ), Coef('Var'  , 0.158096    ), ], 
		[Coef('Var'  , 0.241489    ), Coef('Var'  , 0.18735     ), Coef('Var'  , 0.1368      ), Coef('Var'  , 0.125394    ), Coef('Var'  , 0.117195    ), Coef('Var'  , 0.126543    ), Coef('Var'  , 0.139048    ), Coef('Var'  , 0.188912    ), Coef('Var'  , 0.24238     ), Coef('Var'  , 0.240082    ), ], 
		[Coef('Var'  , 0.149538    ), Coef('Var'  , 0.127281    ), Coef('Var'  , 0.106693    ), Coef('Var'  , 0.107634    ), Coef('Var'  , 0.110466    ), Coef('Var'  , 0.122657    ), Coef('Var'  , 0.137893    ), Coef('Var'  , 0.154067    ), Coef('Var'  , 0.173784    ), Coef('Var'  , 0.160363    ), ], 
		[Coef('Var'  , 0.066158    ), Coef('Var'  , 0.0777501   ), Coef('Var'  , 0.087341    ), Coef('Var'  , 0.103055    ), Coef('Var'  , 0.117319    ), Coef('Var'  , 0.133711    ), Coef('Var'  , 0.150906    ), Coef('Var'  , 0.132341    ), Coef('Var'  , 0.115393    ), Coef('Var'  , 0.0908411   ), ], ])
	
	
	
	etat3.bords   = {Bord('0'): etat13, Bord('1'): etat13, Bord('2'): etat13, Bord('3'): etat13, Bord('4'): etat13, }
	etat3.permuts = {}
	etat3.interns = {Intern('_'): etat3, }
	etat3.subs    = {Sub('0'): etat1, Sub('1'): etat2, Sub('2'): etat4, Sub('3'): etat5, Sub('G', True): Etat.etatPoint, Sub('4'): etat6, Sub('5'): etat7, Sub('6'): etat8, Sub('7'): etat9, Sub('8'): etat10, Sub('9'): etat11, Sub('10'): etat12, }
	
	etat3.buildIntern()
	
	
	etat3.eqs = [
		(Chem([Bord('3'), Sub('0'), Permut('0'), ])	,	Chem([Sub('1'), Bord('1'), ])),
		(Chem([Bord('2'), Sub('1'), Permut('0'), ])	,	Chem([Sub('1'), Bord('2'), ])),
		(Chem([Bord('0'), Sub('0'), Permut('0'), ])	,	Chem([Sub('3'), Bord('3'), ])),
		(Chem([Bord('4'), Sub('1'), Permut('0'), ])	,	Chem([Sub('3'), Bord('4'), ])),
		(Chem([Bord('2'), Sub('0'), Permut('0'), ])	,	Chem([Sub('6'), Bord('3'), ])),
		(Chem([Bord('1'), Sub('1'), Permut('0'), ])	,	Chem([Sub('6'), Bord('4'), ])),
		(Chem([Bord('1'), Sub('0'), Permut('0'), ])	,	Chem([Sub('8'), Bord('1'), ])),
		(Chem([Bord('0'), Sub('1'), Permut('0'), ])	,	Chem([Sub('8'), Bord('2'), ])),
		(Chem([Bord('4'), Sub('0'), Permut('0'), ])	,	Chem([Sub('9'), Bord('2'), ])),
		(Chem([Bord('3'), Sub('1'), Permut('0'), ])	,	Chem([Sub('9'), Bord('3'), ])),
		(Chem([Sub('0'), Bord('0'), Bord('1'), ])	,	Chem([Sub('6'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('1'), Bord('1'), ])	,	Chem([Sub('10'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('2'), Bord('1'), ])	,	Chem([Sub('5'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('3'), Bord('1'), ])	,	Chem([Sub('4'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('4'), Bord('1'), ])	,	Chem([Sub('1'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('0'), Bord('1'), ])	,	Chem([Sub('9'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('2'), Bord('1'), ])	,	Chem([Sub('6'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('4'), Bord('1'), ])	,	Chem([Sub('4'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('0'), Bord('1'), ])	,	Chem([Sub('4'), Bord('4'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('1'), Bord('1'), ])	,	Chem([Sub('5'), Bord('4'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('2'), Bord('1'), ])	,	Chem([Sub('7'), Bord('4'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('3'), Bord('1'), ])	,	Chem([Sub('3'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('4'), Bord('1'), ])	,	Chem([Sub('9'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('3'), Bord('1'), Bord('1'), ])	,	Chem([Sub('7'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('3'), Bord('2'), Bord('1'), ])	,	Chem([Sub('8'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('3'), Bord('4'), Bord('1'), ])	,	Chem([Sub('9'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('4'), Bord('0'), Bord('1'), ])	,	Chem([Sub('9'), Bord('4'), Bord('1'), ])),
		(Chem([Sub('4'), Bord('3'), Bord('1'), ])	,	Chem([Sub('5'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('5'), Bord('2'), Bord('1'), ])	,	Chem([Sub('10'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('5'), Bord('3'), Bord('1'), ])	,	Chem([Sub('7'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('6'), Bord('0'), Bord('1'), ])	,	Chem([Sub('10'), Bord('4'), Bord('1'), ])),
		(Chem([Sub('6'), Bord('4'), Bord('1'), ])	,	Chem([Sub('8'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('7'), Bord('1'), Bord('1'), ])	,	Chem([Sub('10'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('7'), Bord('2'), Bord('1'), ])	,	Chem([Sub('8'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('8'), Bord('4'), Bord('1'), ])	,	Chem([Sub('10'), Bord('0'), Bord('1'), ])),
		(Chem([Bord('0'), Bord('1'), ])	,	Chem([Bord('1'), Bord('0'), ])),
		(Chem([Bord('1'), Bord('1'), ])	,	Chem([Bord('2'), Bord('0'), ])),
		(Chem([Bord('2'), Bord('1'), ])	,	Chem([Bord('3'), Bord('0'), ])),
		(Chem([Bord('3'), Bord('1'), ])	,	Chem([Bord('4'), Bord('0'), ])),
		(Chem([Bord('4'), Bord('1'), ])	,	Chem([Bord('0'), Bord('0'), ])),
		]
	
	
	etat3.prim.elems = [Figure(2, [Chem([Bord('0'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('0'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('0'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('0'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('1'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('1'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('1'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('1'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('2'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('2'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('2'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('2'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('3'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('3'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('3'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('3'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('4'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('4'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('4'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('4'), Sub('1'), Sub('1'), Bord('0'), ]), ])]
	etat3.grid.elems = [
		Figure(1, [Chem([Bord('1'), Bord('0'), ]), Chem([Bord('1'), Intern(''), ]), Chem([Bord('1'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('4'), Bord('0'), ]), Chem([Bord('4'), Intern(''), ]), Chem([Bord('4'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('2'), Bord('0'), ]), Chem([Bord('2'), Intern(''), ]), Chem([Bord('2'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('0'), Bord('0'), ]), Chem([Bord('0'), Intern(''), ]), Chem([Bord('0'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('3'), Bord('0'), ]), Chem([Bord('3'), Intern(''), ]), Chem([Bord('3'), Bord('1'), ]), ]), ]
	
	
	etat3.space = [Chem([Bord('4'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('2'), Intern('0'), Intern('0'), ]), Chem([Bord('2'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('3'), Intern('0'), Intern('0'), ]), Chem([Bord('4'), Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('4'), Intern('0'), Intern('0'), ]), ]
	
	etat3.initMat[Chem([Sub('0')])] = FMat([
		[Coef('Var'  , 0.0472779   ), Coef('Var'  , 0.047802    ), Coef('Var'  , 0.0459415   ), Coef('Var'  , 0.0611746   ), Coef('Var'  , 0.0742107   ), Coef('Var'  , 0.0833462   ), Coef('Var'  , 0.0902059   ), Coef('Var'  , 0.0846063   ), Coef('Var'  , 0.0764147   ), Coef('Var'  , 0.0632113   ), ], 
		[Coef('Var'  , 0.0391242   ), Coef('Var'  , 0.0423409   ), Coef('Var'  , 0.0432689   ), Coef('Var'  , 0.0572372   ), Coef('Var'  , 0.0692937   ), Coef('Var'  , 0.0742543   ), Coef('Var'  , 0.0774888   ), Coef('Var'  , 0.0705564   ), Coef('Var'  , 0.0614521   ), Coef('Var'  , 0.0515602   ), ], 
		[Coef('Var'  , 0.0570696   ), Coef('Var'  , 0.0698414   ), Coef('Var'  , 0.0811861   ), Coef('Var'  , 0.0970971   ), Coef('Var'  , 0.113206    ), Coef('Var'  , 0.108836    ), Coef('Var'  , 0.104129    ), Coef('Var'  , 0.0942876   ), Coef('Var'  , 0.0820378   ), Coef('Var'  , 0.0710868   ), ], 
		[Coef('Var'  , 0.0535371   ), Coef('Var'  , 0.0777359   ), Coef('Var'  , 0.103324    ), Coef('Var'  , 0.116948    ), Coef('Var'  , 0.133856    ), Coef('Var'  , 0.114256    ), Coef('Var'  , 0.0973027   ), Coef('Var'  , 0.0829254   ), Coef('Var'  , 0.0689956   ), Coef('Var'  , 0.061414    ), ], 
		[Coef('Var'  , 0.154854    ), Coef('Var'  , 0.166405    ), Coef('Var'  , 0.179114    ), Coef('Var'  , 0.160279    ), Coef('Var'  , 0.143541    ), Coef('Var'  , 0.128796    ), Coef('Var'  , 0.115539    ), Coef('Var'  , 0.113725    ), Coef('Var'  , 0.112162    ), Coef('Var'  , 0.133472    ), ], 
		[Coef('Var'  , 0.242041    ), Coef('Var'  , 0.240928    ), Coef('Var'  , 0.243286    ), Coef('Var'  , 0.18955     ), Coef('Var'  , 0.138934    ), Coef('Var'  , 0.126118    ), Coef('Var'  , 0.116371    ), Coef('Var'  , 0.124901    ), Coef('Var'  , 0.13691     ), Coef('Var'  , 0.187579    ), ], 
		[Coef('Var'  , 0.178398    ), Coef('Var'  , 0.165802    ), Coef('Var'  , 0.154854    ), Coef('Var'  , 0.133906    ), Coef('Var'  , 0.113531    ), Coef('Var'  , 0.114578    ), Coef('Var'  , 0.116384    ), Coef('Var'  , 0.128607    ), Coef('Var'  , 0.142917    ), Coef('Var'  , 0.159346    ), ], 
		[Coef('Var'  , 0.107993    ), Coef('Var'  , 0.0832246   ), Coef('Var'  , 0.0591283   ), Coef('Var'  , 0.068749    ), Coef('Var'  , 0.0772423   ), Coef('Var'  , 0.0916893   ), Coef('Var'  , 0.105602    ), Coef('Var'  , 0.122071    ), Coef('Var'  , 0.14023     ), Coef('Var'  , 0.122873    ), ], 
		[Coef('Var'  , 0.0719936   ), Coef('Var'  , 0.0592911   ), Coef('Var'  , 0.0468036   ), Coef('Var'  , 0.0581075   ), Coef('Var'  , 0.068156    ), Coef('Var'  , 0.0797031   ), Coef('Var'  , 0.0903854   ), Coef('Var'  , 0.0955536   ), Coef('Var'  , 0.10159     ), Coef('Var'  , 0.0860185   ), ], 
		[Coef('Var'  , 0.0477128   ), Coef('Var'  , 0.0466299   ), Coef('Var'  , 0.0430936   ), Coef('Var'  , 0.0569522   ), Coef('Var'  , 0.0680292   ), Coef('Var'  , 0.0784232   ), Coef('Var'  , 0.0865919   ), Coef('Var'  , 0.0827661   ), Coef('Var'  , 0.0772909   ), Coef('Var'  , 0.0634394   ), ], ])
	etat3.initMat[Chem([Sub('1')])] = FMat([
		[Coef('Var'  , 0.0533778   ), Coef('Var'  , 0.0272065   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0242893   ), Coef('Var'  , 0.0472779   ), Coef('Var'  , 0.0514958   ), ], 
		[Coef('Var'  , 0.0387927   ), Coef('Var'  , 0.019997    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0201808   ), Coef('Var'  , 0.0391242   ), Coef('Var'  , 0.0401778   ), ], 
		[Coef('Var'  , 0.0516998   ), Coef('Var'  , 0.0266572   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0291897   ), Coef('Var'  , 0.0570696   ), Coef('Var'  , 0.0558469   ), ], 
		[Coef('Var'  , 0.0424024   ), Coef('Var'  , 0.0215446   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0267666   ), Coef('Var'  , 0.0535371   ), Coef('Var'  , 0.0483112   ), ], 
		[Coef('Var'  , 0.0801103   ), Coef('Var'  , 0.040209    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.202334    ), Coef('Var'  , 0.154854    ), Coef('Var'  , 0.117543    ), ], 
		[Coef('Var'  , 0.106577    ), Coef('Var'  , 0.0527199   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.370087    ), Coef('Var'  , 0.242041    ), Coef('Var'  , 0.172807    ), ], 
		[Coef('Var'  , 0.177805    ), Coef('Var'  , 0.213313    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.213606    ), Coef('Var'  , 0.178398    ), Coef('Var'  , 0.176919    ), ], 
		[Coef('Var'  , 0.243261    ), Coef('Var'  , 0.370745    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0534835   ), Coef('Var'  , 0.107993    ), Coef('Var'  , 0.174229    ), ], 
		[Coef('Var'  , 0.146088    ), Coef('Var'  , 0.197442    ), Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0356758   ), Coef('Var'  , 0.0719936   ), Coef('Var'  , 0.108118    ), ], 
		[Coef('Var'  , 0.0598863   ), Coef('Var'  , 0.0301651   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0243871   ), Coef('Var'  , 0.0477128   ), Coef('Var'  , 0.0545522   ), ], ])
	etat3.initMat[Chem([Sub('2')])] = FMat([
		[Coef('Var'  , 0.152207    ), Coef('Var'  , 0.131145    ), Coef('Var'  , 0.111009    ), Coef('Var'  , 0.112616    ), Coef('Var'  , 0.114949    ), Coef('Var'  , 0.126876    ), Coef('Var'  , 0.14087     ), Coef('Var'  , 0.156694    ), Coef('Var'  , 0.175638    ), Coef('Var'  , 0.162781    ), ], 
		[Coef('Var'  , 0.0531233   ), Coef('Var'  , 0.0606203   ), Coef('Var'  , 0.0672533   ), Coef('Var'  , 0.079681    ), Coef('Var'  , 0.09237     ), Coef('Var'  , 0.108998    ), Coef('Var'  , 0.128522    ), Coef('Var'  , 0.113087    ), Coef('Var'  , 0.10102     ), Coef('Var'  , 0.0765764   ), ], 
		[Coef('Var'  , 0.0563662   ), Coef('Var'  , 0.0700088   ), Coef('Var'  , 0.0811343   ), Coef('Var'  , 0.0938754   ), Coef('Var'  , 0.104486    ), Coef('Var'  , 0.109915    ), Coef('Var'  , 0.11469     ), Coef('Var'  , 0.0985203   ), Coef('Var'  , 0.0820985   ), Coef('Var'  , 0.0698991   ), ], 
		[Coef('Var'  , 0.0417741   ), Coef('Var'  , 0.0547236   ), Coef('Var'  , 0.0649464   ), Coef('Var'  , 0.0751388   ), Coef('Var'  , 0.0831221   ), Coef('Var'  , 0.0803293   ), Coef('Var'  , 0.0756345   ), Coef('Var'  , 0.0626168   ), Coef('Var'  , 0.0473212   ), Coef('Var'  , 0.0458685   ), ], 
		[Coef('Var'  , 0.0429726   ), Coef('Var'  , 0.0579704   ), Coef('Var'  , 0.0712428   ), Coef('Var'  , 0.0787857   ), Coef('Var'  , 0.0846808   ), Coef('Var'  , 0.0774269   ), Coef('Var'  , 0.0687083   ), Coef('Var'  , 0.0558521   ), Coef('Var'  , 0.0415727   ), Coef('Var'  , 0.0430319   ), ], 
		[Coef('Var'  , 0.0482298   ), Coef('Var'  , 0.0633515   ), Coef('Var'  , 0.0762346   ), Coef('Var'  , 0.0820723   ), Coef('Var'  , 0.0861068   ), Coef('Var'  , 0.0791335   ), Coef('Var'  , 0.069732    ), Coef('Var'  , 0.0587766   ), Coef('Var'  , 0.0447101   ), Coef('Var'  , 0.0479014   ), ], 
		[Coef('Var'  , 0.0779653   ), Coef('Var'  , 0.093088    ), Coef('Var'  , 0.108854    ), Coef('Var'  , 0.102851    ), Coef('Var'  , 0.0973852   ), Coef('Var'  , 0.086528    ), Coef('Var'  , 0.0746724   ), Coef('Var'  , 0.064222    ), Coef('Var'  , 0.0520241   ), Coef('Var'  , 0.065343    ), ], 
		[Coef('Var'  , 0.106826    ), Coef('Var'  , 0.121439    ), Coef('Var'  , 0.13903     ), Coef('Var'  , 0.121052    ), Coef('Var'  , 0.105074    ), Coef('Var'  , 0.0913449   ), Coef('Var'  , 0.0770813   ), Coef('Var'  , 0.0684741   ), Coef('Var'  , 0.0587124   ), Coef('Var'  , 0.0822924   ), ], 
		[Coef('Var'  , 0.174163    ), Coef('Var'  , 0.154256    ), Coef('Var'  , 0.137251    ), Coef('Var'  , 0.122722    ), Coef('Var'  , 0.110269    ), Coef('Var'  , 0.108659    ), Coef('Var'  , 0.107878    ), Coef('Var'  , 0.128902    ), Coef('Var'  , 0.150828    ), Coef('Var'  , 0.16146     ), ], 
		[Coef('Var'  , 0.246373    ), Coef('Var'  , 0.193398    ), Coef('Var'  , 0.143044    ), Coef('Var'  , 0.131205    ), Coef('Var'  , 0.121557    ), Coef('Var'  , 0.13079     ), Coef('Var'  , 0.142212    ), Coef('Var'  , 0.192855    ), Coef('Var'  , 0.246076    ), Coef('Var'  , 0.244847    ), ], ])
	etat3.initMat[Chem([Sub('3')])] = FMat([
		[Coef('Const', 0.25        ), Coef('Var'  , 0.212035    ), Coef('Var'  , 0.175638    ), Coef('Var'  , 0.173762    ), Coef('Var'  , 0.175096    ), Coef('Var'  , 0.211727    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0498631   ), Coef('Var'  , 0.10102     ), Coef('Var'  , 0.166916    ), Coef('Var'  , 0.236196    ), Coef('Var'  , 0.367053    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0411857   ), Coef('Var'  , 0.0820985   ), Coef('Var'  , 0.118335    ), Coef('Var'  , 0.154754    ), Coef('Var'  , 0.202149    ), Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0242857   ), Coef('Var'  , 0.0473212   ), Coef('Var'  , 0.0543448   ), Coef('Var'  , 0.0594282   ), Coef('Var'  , 0.0300592   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0211362   ), Coef('Var'  , 0.0415727   ), Coef('Var'  , 0.0450202   ), Coef('Var'  , 0.0473728   ), Coef('Var'  , 0.023884    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0231326   ), Coef('Var'  , 0.0447101   ), Coef('Var'  , 0.0462369   ), Coef('Var'  , 0.0446932   ), Coef('Var'  , 0.0231042   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0264      ), Coef('Var'  , 0.0520241   ), Coef('Var'  , 0.0507449   ), Coef('Var'  , 0.0474288   ), Coef('Var'  , 0.0243449   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.029517    ), Coef('Var'  , 0.0587124   ), Coef('Var'  , 0.0540368   ), Coef('Var'  , 0.0479452   ), Coef('Var'  , 0.0245198   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.25        ), Coef('Var'  , 0.200084    ), Coef('Var'  , 0.150828    ), Coef('Var'  , 0.114001    ), Coef('Var'  , 0.0777761   ), Coef('Var'  , 0.0389163   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.5         ), Coef('Var'  , 0.37236     ), Coef('Var'  , 0.246076    ), Coef('Var'  , 0.176603    ), Coef('Var'  , 0.109309    ), Coef('Var'  , 0.0542424   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), ], ])
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
	etat3.initMat[Chem([Sub('4')])] = FMat([
		[Coef('Var'  , 0.111009    ), Coef('Var'  , 0.0950431   ), Coef('Var'  , 0.079249    ), Coef('Var'  , 0.0668504   ), Coef('Var'  , 0.0533778   ), Coef('Var'  , 0.0661285   ), Coef('Var'  , 0.0764147   ), Coef('Var'  , 0.0891295   ), Coef('Var'  , 0.0997967   ), Coef('Var'  , 0.105607    ), ], 
		[Coef('Var'  , 0.0672533   ), Coef('Var'  , 0.055358    ), Coef('Var'  , 0.0419913   ), Coef('Var'  , 0.0414479   ), Coef('Var'  , 0.0387927   ), Coef('Var'  , 0.0513763   ), Coef('Var'  , 0.0614521   ), Coef('Var'  , 0.0699117   ), Coef('Var'  , 0.0763947   ), Coef('Var'  , 0.0724394   ), ], 
		[Coef('Var'  , 0.0811343   ), Coef('Var'  , 0.0674962   ), Coef('Var'  , 0.0510037   ), Coef('Var'  , 0.0528581   ), Coef('Var'  , 0.0516998   ), Coef('Var'  , 0.0685543   ), Coef('Var'  , 0.0820378   ), Coef('Var'  , 0.0910557   ), Coef('Var'  , 0.0968701   ), Coef('Var'  , 0.0904539   ), ], 
		[Coef('Var'  , 0.0649464   ), Coef('Var'  , 0.0539984   ), Coef('Var'  , 0.0404772   ), Coef('Var'  , 0.0424022   ), Coef('Var'  , 0.0424024   ), Coef('Var'  , 0.056192    ), Coef('Var'  , 0.0689956   ), Coef('Var'  , 0.0749773   ), Coef('Var'  , 0.0801049   ), Coef('Var'  , 0.0734706   ), ], 
		[Coef('Var'  , 0.0712428   ), Coef('Var'  , 0.0616931   ), Coef('Var'  , 0.0504937   ), Coef('Var'  , 0.0658274   ), Coef('Var'  , 0.0801103   ), Coef('Var'  , 0.0963467   ), Coef('Var'  , 0.112162    ), Coef('Var'  , 0.10492     ), Coef('Var'  , 0.0971176   ), Coef('Var'  , 0.0848571   ), ], 
		[Coef('Var'  , 0.0762346   ), Coef('Var'  , 0.0684694   ), Coef('Var'  , 0.0591529   ), Coef('Var'  , 0.0826066   ), Coef('Var'  , 0.106577    ), Coef('Var'  , 0.120212    ), Coef('Var'  , 0.13691     ), Coef('Var'  , 0.11836     ), Coef('Var'  , 0.102342    ), Coef('Var'  , 0.0894513   ), ], 
		[Coef('Var'  , 0.108854    ), Coef('Var'  , 0.129864    ), Coef('Var'  , 0.152042    ), Coef('Var'  , 0.164032    ), Coef('Var'  , 0.177805    ), Coef('Var'  , 0.159053    ), Coef('Var'  , 0.142917    ), Coef('Var'  , 0.127226    ), Coef('Var'  , 0.113925    ), Coef('Var'  , 0.110631    ), ], 
		[Coef('Var'  , 0.13903     ), Coef('Var'  , 0.188925    ), Coef('Var'  , 0.242469    ), Coef('Var'  , 0.241007    ), Coef('Var'  , 0.243261    ), Coef('Var'  , 0.190135    ), Coef('Var'  , 0.14023     ), Coef('Var'  , 0.128469    ), Coef('Var'  , 0.119318    ), Coef('Var'  , 0.127743    ), ], 
		[Coef('Var'  , 0.137251    ), Coef('Var'  , 0.153554    ), Coef('Var'  , 0.17291     ), Coef('Var'  , 0.158116    ), Coef('Var'  , 0.146088    ), Coef('Var'  , 0.122785    ), Coef('Var'  , 0.10159     ), Coef('Var'  , 0.10365     ), Coef('Var'  , 0.107469    ), Coef('Var'  , 0.121189    ), ], 
		[Coef('Var'  , 0.143044    ), Coef('Var'  , 0.125598    ), Coef('Var'  , 0.110211    ), Coef('Var'  , 0.0848528   ), Coef('Var'  , 0.0598863   ), Coef('Var'  , 0.0692174   ), Coef('Var'  , 0.0772909   ), Coef('Var'  , 0.0923003   ), Coef('Var'  , 0.106663    ), Coef('Var'  , 0.124159    ), ], ])
	etat3.initMat[Chem([Sub('5')])] = FMat([
		[Coef('Var'  , 0.114949    ), Coef('Var'  , 0.107425    ), Coef('Var'  , 0.0997967   ), Coef('Var'  , 0.0958918   ), Coef('Var'  , 0.0902059   ), Coef('Var'  , 0.0948289   ), Coef('Var'  , 0.0978424   ), Coef('Var'  , 0.105783    ), Coef('Var'  , 0.113862    ), Coef('Var'  , 0.113855    ), ], 
		[Coef('Var'  , 0.09237     ), Coef('Var'  , 0.0843063   ), Coef('Var'  , 0.0763947   ), Coef('Var'  , 0.0777095   ), Coef('Var'  , 0.0774888   ), Coef('Var'  , 0.0859036   ), Coef('Var'  , 0.093995    ), Coef('Var'  , 0.0989761   ), Coef('Var'  , 0.106273    ), Coef('Var'  , 0.0980235   ), ], 
		[Coef('Var'  , 0.104486    ), Coef('Var'  , 0.101739    ), Coef('Var'  , 0.0968701   ), Coef('Var'  , 0.101549    ), Coef('Var'  , 0.104129    ), Coef('Var'  , 0.110635    ), Coef('Var'  , 0.117317    ), Coef('Var'  , 0.116824    ), Coef('Var'  , 0.117882    ), Coef('Var'  , 0.11116     ), ], 
		[Coef('Var'  , 0.0831221   ), Coef('Var'  , 0.082328    ), Coef('Var'  , 0.0801049   ), Coef('Var'  , 0.0886079   ), Coef('Var'  , 0.0973027   ), Coef('Var'  , 0.104811    ), Coef('Var'  , 0.11439     ), Coef('Var'  , 0.107605    ), Coef('Var'  , 0.102333    ), Coef('Var'  , 0.0930703   ), ], 
		[Coef('Var'  , 0.0846808   ), Coef('Var'  , 0.0914933   ), Coef('Var'  , 0.0971176   ), Coef('Var'  , 0.10637     ), Coef('Var'  , 0.115539    ), Coef('Var'  , 0.113939    ), Coef('Var'  , 0.113282    ), Coef('Var'  , 0.103297    ), Coef('Var'  , 0.0937262   ), Coef('Var'  , 0.0896568   ), ], 
		[Coef('Var'  , 0.0861068   ), Coef('Var'  , 0.0943581   ), Coef('Var'  , 0.102342    ), Coef('Var'  , 0.108278    ), Coef('Var'  , 0.116371    ), Coef('Var'  , 0.108998    ), Coef('Var'  , 0.103598    ), Coef('Var'  , 0.0953336   ), Coef('Var'  , 0.0865854   ), Coef('Var'  , 0.0872345   ), ], 
		[Coef('Var'  , 0.0973852   ), Coef('Var'  , 0.105192    ), Coef('Var'  , 0.113925    ), Coef('Var'  , 0.114353    ), Coef('Var'  , 0.116384    ), Coef('Var'  , 0.109164    ), Coef('Var'  , 0.101923    ), Coef('Var'  , 0.0974337   ), Coef('Var'  , 0.0912245   ), Coef('Var'  , 0.0948425   ), ], 
		[Coef('Var'  , 0.105074    ), Coef('Var'  , 0.111467    ), Coef('Var'  , 0.119318    ), Coef('Var'  , 0.11176     ), Coef('Var'  , 0.105602    ), Coef('Var'  , 0.097347    ), Coef('Var'  , 0.0883236   ), Coef('Var'  , 0.0892798   ), Coef('Var'  , 0.0882035   ), Coef('Var'  , 0.097002    ), ], 
		[Coef('Var'  , 0.110269    ), Coef('Var'  , 0.108149    ), Coef('Var'  , 0.107469    ), Coef('Var'  , 0.0985187   ), Coef('Var'  , 0.0903854   ), Coef('Var'  , 0.0877197   ), Coef('Var'  , 0.0840923   ), Coef('Var'  , 0.090342    ), Coef('Var'  , 0.0951378   ), Coef('Var'  , 0.102675    ), ], 
		[Coef('Var'  , 0.121557    ), Coef('Var'  , 0.113543    ), Coef('Var'  , 0.106663    ), Coef('Var'  , 0.0969619   ), Coef('Var'  , 0.0865919   ), Coef('Var'  , 0.0866541   ), Coef('Var'  , 0.0852357   ), Coef('Var'  , 0.0951259   ), Coef('Var'  , 0.104772    ), Coef('Var'  , 0.112481    ), ], ])
	etat3.initMat[Chem([Sub('6')])] = FMat([
		[Coef('Const', 0           ), Coef('Var'  , 0.0258132   ), Coef('Var'  , 0.0509611   ), Coef('Var'  , 0.0493259   ), Coef('Var'  , 0.0459415   ), Coef('Var'  , 0.0235127   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0273757   ), Coef('Var'  , 0.0543625   ), Coef('Var'  , 0.0495357   ), Coef('Var'  , 0.0432689   ), Coef('Var'  , 0.02216     ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.25        ), Coef('Var'  , 0.20131     ), Coef('Var'  , 0.153369    ), Coef('Var'  , 0.116961    ), Coef('Var'  , 0.0811861   ), Coef('Var'  , 0.0406516   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.5         ), Coef('Var'  , 0.369144    ), Coef('Var'  , 0.240199    ), Coef('Var'  , 0.170114    ), Coef('Var'  , 0.103324    ), Coef('Var'  , 0.0509693   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0.25        ), Coef('Var'  , 0.213328    ), Coef('Var'  , 0.177829    ), Coef('Var'  , 0.177399    ), Coef('Var'  , 0.179114    ), Coef('Var'  , 0.214071    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.053804    ), Coef('Var'  , 0.108404    ), Coef('Var'  , 0.174644    ), Coef('Var'  , 0.243286    ), Coef('Var'  , 0.37084     ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0410958   ), Coef('Var'  , 0.0819208   ), Coef('Var'  , 0.118292    ), Coef('Var'  , 0.154854    ), Coef('Var'  , 0.202196    ), Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0244669   ), Coef('Var'  , 0.0479193   ), Coef('Var'  , 0.054208    ), Coef('Var'  , 0.0591283   ), Coef('Var'  , 0.0297411   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0218185   ), Coef('Var'  , 0.0426234   ), Coef('Var'  , 0.0454339   ), Coef('Var'  , 0.0468036   ), Coef('Var'  , 0.0236153   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0218436   ), Coef('Var'  , 0.0424118   ), Coef('Var'  , 0.0440864   ), Coef('Var'  , 0.0430936   ), Coef('Var'  , 0.0222428   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], ])
	etat3.initMat[Chem([Sub('7')])] = FMat([
		[Coef('Var'  , 0.14087     ), Coef('Var'  , 0.126298    ), Coef('Var'  , 0.113862    ), Coef('Var'  , 0.110645    ), Coef('Var'  , 0.108458    ), Coef('Var'  , 0.128632    ), Coef('Var'  , 0.1502      ), Coef('Var'  , 0.161352    ), Coef('Var'  , 0.175096    ), Coef('Var'  , 0.156387    ), ], 
		[Coef('Var'  , 0.128522    ), Coef('Var'  , 0.115473    ), Coef('Var'  , 0.106273    ), Coef('Var'  , 0.115889    ), Coef('Var'  , 0.129293    ), Coef('Var'  , 0.1808      ), Coef('Var'  , 0.236436    ), Coef('Var'  , 0.234213    ), Coef('Var'  , 0.236196    ), Coef('Var'  , 0.180277    ), ], 
		[Coef('Var'  , 0.11469     ), Coef('Var'  , 0.115914    ), Coef('Var'  , 0.117882    ), Coef('Var'  , 0.128927    ), Coef('Var'  , 0.142537    ), Coef('Var'  , 0.158077    ), Coef('Var'  , 0.17703     ), Coef('Var'  , 0.164878    ), Coef('Var'  , 0.154754    ), Coef('Var'  , 0.134483    ), ], 
		[Coef('Var'  , 0.0756345   ), Coef('Var'  , 0.0894034   ), Coef('Var'  , 0.102333    ), Coef('Var'  , 0.11963     ), Coef('Var'  , 0.138436    ), Coef('Var'  , 0.122257    ), Coef('Var'  , 0.108159    ), Coef('Var'  , 0.0837585   ), Coef('Var'  , 0.0594282   ), Coef('Var'  , 0.0683904   ), ], 
		[Coef('Var'  , 0.0687083   ), Coef('Var'  , 0.0816618   ), Coef('Var'  , 0.0937262   ), Coef('Var'  , 0.100016    ), Coef('Var'  , 0.106687    ), Coef('Var'  , 0.0904738   ), Coef('Var'  , 0.075171    ), Coef('Var'  , 0.0612876   ), Coef('Var'  , 0.0473728   ), Coef('Var'  , 0.0585999   ), ], 
		[Coef('Var'  , 0.069732    ), Coef('Var'  , 0.079389    ), Coef('Var'  , 0.0865854   ), Coef('Var'  , 0.0826892   ), Coef('Var'  , 0.0769717   ), Coef('Var'  , 0.0637903   ), Coef('Var'  , 0.0484712   ), Coef('Var'  , 0.0479503   ), Coef('Var'  , 0.0446932   ), Coef('Var'  , 0.0587482   ), ], 
		[Coef('Var'  , 0.0746724   ), Coef('Var'  , 0.0839585   ), Coef('Var'  , 0.0912245   ), Coef('Var'  , 0.0866967   ), Coef('Var'  , 0.0793855   ), Coef('Var'  , 0.0664329   ), Coef('Var'  , 0.0500624   ), Coef('Var'  , 0.0502177   ), Coef('Var'  , 0.0474288   ), Coef('Var'  , 0.0621669   ), ], 
		[Coef('Var'  , 0.0770813   ), Coef('Var'  , 0.0835712   ), Coef('Var'  , 0.0882035   ), Coef('Var'  , 0.0810549   ), Coef('Var'  , 0.0711887   ), Coef('Var'  , 0.0597695   ), Coef('Var'  , 0.0450877   ), Coef('Var'  , 0.0478486   ), Coef('Var'  , 0.0479452   ), Coef('Var'  , 0.0634769   ), ], 
		[Coef('Var'  , 0.107878    ), Coef('Var'  , 0.101651    ), Coef('Var'  , 0.0951378   ), Coef('Var'  , 0.0849259   ), Coef('Var'  , 0.0727563   ), Coef('Var'  , 0.0635201   ), Coef('Var'  , 0.051748    ), Coef('Var'  , 0.0653438   ), Coef('Var'  , 0.0777761   ), Coef('Var'  , 0.0927337   ), ], 
		[Coef('Var'  , 0.142212    ), Coef('Var'  , 0.12268     ), Coef('Var'  , 0.104772    ), Coef('Var'  , 0.0895252   ), Coef('Var'  , 0.0742876   ), Coef('Var'  , 0.0662471   ), Coef('Var'  , 0.0576352   ), Coef('Var'  , 0.0831499   ), Coef('Var'  , 0.109309    ), Coef('Var'  , 0.124737    ), ], ])
	etat3.initMat[Chem([Sub('8')])] = FMat([
		[Coef('Var'  , 0.0767042   ), Coef('Var'  , 0.0382146   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.199625    ), Coef('Var'  , 0.1502      ), Coef('Var'  , 0.112839    ), ], 
		[Coef('Var'  , 0.101552    ), Coef('Var'  , 0.050107    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.36716     ), Coef('Var'  , 0.236436    ), Coef('Var'  , 0.167267    ), ], 
		[Coef('Var'  , 0.176564    ), Coef('Var'  , 0.212444    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.212729    ), Coef('Var'  , 0.17703     ), Coef('Var'  , 0.175174    ), ], 
		[Coef('Var'  , 0.242765    ), Coef('Var'  , 0.370598    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0536994   ), Coef('Var'  , 0.108159    ), Coef('Var'  , 0.174298    ), ], 
		[Coef('Var'  , 0.15035     ), Coef('Var'  , 0.19976     ), Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0374037   ), Coef('Var'  , 0.075171    ), Coef('Var'  , 0.112164    ), ], 
		[Coef('Var'  , 0.0599932   ), Coef('Var'  , 0.0303241   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0248461   ), Coef('Var'  , 0.0484712   ), Coef('Var'  , 0.0551702   ), ], 
		[Coef('Var'  , 0.0563942   ), Coef('Var'  , 0.028896    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0258728   ), Coef('Var'  , 0.0500624   ), Coef('Var'  , 0.0547687   ), ], 
		[Coef('Var'  , 0.0450205   ), Coef('Var'  , 0.0232758   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0233288   ), Coef('Var'  , 0.0450877   ), Coef('Var'  , 0.0466046   ), ], 
		[Coef('Var'  , 0.0452724   ), Coef('Var'  , 0.023331    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0264274   ), Coef('Var'  , 0.051748    ), Coef('Var'  , 0.0497584   ), ], 
		[Coef('Var'  , 0.0453841   ), Coef('Var'  , 0.0230487   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0289076   ), Coef('Var'  , 0.0576352   ), Coef('Var'  , 0.0519562   ), ], ])
	etat3.initMat[Chem([Sub('9')])] = FMat([
		[Coef('Var'  , 0.079249    ), Coef('Var'  , 0.115389    ), Coef('Var'  , 0.152207    ), Coef('Var'  , 0.200745    ), Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.039644    ), ], 
		[Coef('Var'  , 0.0419913   ), Coef('Var'  , 0.0481642   ), Coef('Var'  , 0.0531233   ), Coef('Var'  , 0.0267132   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.021451    ), ], 
		[Coef('Var'  , 0.0510037   ), Coef('Var'  , 0.0549143   ), Coef('Var'  , 0.0563662   ), Coef('Var'  , 0.0287134   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0262009   ), ], 
		[Coef('Var'  , 0.0404772   ), Coef('Var'  , 0.0424405   ), Coef('Var'  , 0.0417741   ), Coef('Var'  , 0.0215828   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0208577   ), ], 
		[Coef('Var'  , 0.0504937   ), Coef('Var'  , 0.047514    ), Coef('Var'  , 0.0429726   ), Coef('Var'  , 0.0218957   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0256183   ), ], 
		[Coef('Var'  , 0.0591529   ), Coef('Var'  , 0.0546555   ), Coef('Var'  , 0.0482298   ), Coef('Var'  , 0.0247688   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0298867   ), ], 
		[Coef('Var'  , 0.152042    ), Coef('Var'  , 0.114662    ), Coef('Var'  , 0.0779653   ), Coef('Var'  , 0.038943    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.200719    ), ], 
		[Coef('Var'  , 0.242469    ), Coef('Var'  , 0.173037    ), Coef('Var'  , 0.106826    ), Coef('Var'  , 0.0527753   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.370262    ), ], 
		[Coef('Var'  , 0.17291     ), Coef('Var'  , 0.172049    ), Coef('Var'  , 0.174163    ), Coef('Var'  , 0.211375    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.210673    ), ], 
		[Coef('Var'  , 0.110211    ), Coef('Var'  , 0.177175    ), Coef('Var'  , 0.246373    ), Coef('Var'  , 0.372487    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0546877   ), ], ])
	etat3.initMat[Chem([Sub('10')])] = FMat([
		[Coef('Var'  , 0.0509611   ), Coef('Var'  , 0.0640279   ), Coef('Var'  , 0.0767042   ), Coef('Var'  , 0.0922217   ), Coef('Var'  , 0.108458    ), Coef('Var'  , 0.103152    ), Coef('Var'  , 0.0978424   ), Coef('Var'  , 0.0868065   ), Coef('Var'  , 0.0742107   ), Coef('Var'  , 0.0634752   ), ], 
		[Coef('Var'  , 0.0543625   ), Coef('Var'  , 0.0774828   ), Coef('Var'  , 0.101552    ), Coef('Var'  , 0.113747    ), Coef('Var'  , 0.129293    ), Coef('Var'  , 0.110366    ), Coef('Var'  , 0.093995    ), Coef('Var'  , 0.0818037   ), Coef('Var'  , 0.0692937   ), Coef('Var'  , 0.0624529   ), ], 
		[Coef('Var'  , 0.153369    ), Coef('Var'  , 0.163754    ), Coef('Var'  , 0.176564    ), Coef('Var'  , 0.157792    ), Coef('Var'  , 0.142537    ), Coef('Var'  , 0.128592    ), Coef('Var'  , 0.117317    ), Coef('Var'  , 0.11469     ), Coef('Var'  , 0.113206    ), Coef('Var'  , 0.132755    ), ], 
		[Coef('Var'  , 0.240199    ), Coef('Var'  , 0.239743    ), Coef('Var'  , 0.242765    ), Coef('Var'  , 0.189156    ), Coef('Var'  , 0.138436    ), Coef('Var'  , 0.125091    ), Coef('Var'  , 0.11439     ), Coef('Var'  , 0.122511    ), Coef('Var'  , 0.133856    ), Coef('Var'  , 0.185123    ), ], 
		[Coef('Var'  , 0.177829    ), Coef('Var'  , 0.163088    ), Coef('Var'  , 0.15035     ), Coef('Var'  , 0.127831    ), Coef('Var'  , 0.106687    ), Coef('Var'  , 0.109421    ), Coef('Var'  , 0.113282    ), Coef('Var'  , 0.127559    ), Coef('Var'  , 0.143541    ), Coef('Var'  , 0.159536    ), ], 
		[Coef('Var'  , 0.108404    ), Coef('Var'  , 0.0841281   ), Coef('Var'  , 0.0599932   ), Coef('Var'  , 0.0692683   ), Coef('Var'  , 0.0769717   ), Coef('Var'  , 0.0905328   ), Coef('Var'  , 0.103598    ), Coef('Var'  , 0.120298    ), Coef('Var'  , 0.138934    ), Coef('Var'  , 0.122513    ), ], 
		[Coef('Var'  , 0.0819208   ), Coef('Var'  , 0.0699918   ), Coef('Var'  , 0.0563942   ), Coef('Var'  , 0.0694562   ), Coef('Var'  , 0.0793855   ), Coef('Var'  , 0.0918574   ), Coef('Var'  , 0.101923    ), Coef('Var'  , 0.108007    ), Coef('Var'  , 0.113531    ), Coef('Var'  , 0.0978061   ), ], 
		[Coef('Var'  , 0.0479193   ), Coef('Var'  , 0.0477427   ), Coef('Var'  , 0.0450205   ), Coef('Var'  , 0.0597165   ), Coef('Var'  , 0.0711887   ), Coef('Var'  , 0.0811063   ), Coef('Var'  , 0.0883236   ), Coef('Var'  , 0.0836736   ), Coef('Var'  , 0.0772423   ), Coef('Var'  , 0.0634748   ), ], 
		[Coef('Var'  , 0.0426234   ), Coef('Var'  , 0.0451495   ), Coef('Var'  , 0.0452724   ), Coef('Var'  , 0.0604237   ), Coef('Var'  , 0.0727563   ), Coef('Var'  , 0.0796015   ), Coef('Var'  , 0.0840923   ), Coef('Var'  , 0.077001    ), Coef('Var'  , 0.068156    ), Coef('Var'  , 0.0563107   ), ], 
		[Coef('Var'  , 0.0424118   ), Coef('Var'  , 0.0448923   ), Coef('Var'  , 0.0453841   ), Coef('Var'  , 0.0603882   ), Coef('Var'  , 0.0742876   ), Coef('Var'  , 0.0802798   ), Coef('Var'  , 0.0852357   ), Coef('Var'  , 0.0776497   ), Coef('Var'  , 0.0680292   ), Coef('Var'  , 0.056553    ), ], ])
	
	
	
	etat4.bords   = {Bord('0'): etat13, Bord('1'): etat13, Bord('2'): etat13, Bord('3'): etat13, Bord('4'): etat13, }
	etat4.permuts = {}
	etat4.interns = {Intern('_'): etat4, }
	etat4.subs    = {Sub('0'): etat1, Sub('1'): etat2, Sub('2'): etat3, Sub('3'): etat5, Sub('G', True): Etat.etatPoint, Sub('4'): etat6, Sub('5'): etat7, Sub('6'): etat8, Sub('7'): etat9, Sub('8'): etat10, Sub('9'): etat11, Sub('10'): etat12, }
	
	etat4.buildIntern()
	
	
	etat4.eqs = [
		(Chem([Bord('4'), Sub('0'), Permut('0'), ])	,	Chem([Sub('3'), Bord('0'), ])),
		(Chem([Bord('3'), Sub('1'), Permut('0'), ])	,	Chem([Sub('3'), Bord('1'), ])),
		(Chem([Bord('0'), Sub('1'), Permut('0'), ])	,	Chem([Sub('4'), Bord('0'), ])),
		(Chem([Bord('1'), Sub('0'), Permut('0'), ])	,	Chem([Sub('4'), Bord('4'), ])),
		(Chem([Bord('1'), Sub('1'), Permut('0'), ])	,	Chem([Sub('5'), Bord('0'), ])),
		(Chem([Bord('2'), Sub('0'), Permut('0'), ])	,	Chem([Sub('5'), Bord('4'), ])),
		(Chem([Bord('2'), Sub('1'), Permut('0'), ])	,	Chem([Sub('7'), Bord('0'), ])),
		(Chem([Bord('3'), Sub('0'), Permut('0'), ])	,	Chem([Sub('7'), Bord('4'), ])),
		(Chem([Bord('0'), Sub('0'), Permut('0'), ])	,	Chem([Sub('9'), Bord('0'), ])),
		(Chem([Bord('4'), Sub('1'), Permut('0'), ])	,	Chem([Sub('9'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('0'), Bord('1'), ])	,	Chem([Sub('6'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('1'), Bord('1'), ])	,	Chem([Sub('10'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('2'), Bord('1'), ])	,	Chem([Sub('5'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('3'), Bord('1'), ])	,	Chem([Sub('4'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('4'), Bord('1'), ])	,	Chem([Sub('1'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('0'), Bord('1'), ])	,	Chem([Sub('9'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('1'), Bord('1'), ])	,	Chem([Sub('2'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('2'), Bord('1'), ])	,	Chem([Sub('6'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('4'), Bord('1'), ])	,	Chem([Sub('4'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('0'), Bord('1'), ])	,	Chem([Sub('8'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('1'), Bord('1'), ])	,	Chem([Sub('6'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('3'), Bord('1'), ])	,	Chem([Sub('9'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('4'), Bord('1'), ])	,	Chem([Sub('3'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('3'), Bord('1'), Bord('1'), ])	,	Chem([Sub('7'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('3'), Bord('2'), Bord('1'), ])	,	Chem([Sub('8'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('3'), Bord('4'), Bord('1'), ])	,	Chem([Sub('9'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('4'), Bord('0'), Bord('1'), ])	,	Chem([Sub('9'), Bord('4'), Bord('1'), ])),
		(Chem([Sub('4'), Bord('3'), Bord('1'), ])	,	Chem([Sub('5'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('5'), Bord('2'), Bord('1'), ])	,	Chem([Sub('10'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('5'), Bord('3'), Bord('1'), ])	,	Chem([Sub('7'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('6'), Bord('0'), Bord('1'), ])	,	Chem([Sub('10'), Bord('4'), Bord('1'), ])),
		(Chem([Sub('6'), Bord('4'), Bord('1'), ])	,	Chem([Sub('8'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('7'), Bord('1'), Bord('1'), ])	,	Chem([Sub('10'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('7'), Bord('2'), Bord('1'), ])	,	Chem([Sub('8'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('8'), Bord('4'), Bord('1'), ])	,	Chem([Sub('10'), Bord('0'), Bord('1'), ])),
		(Chem([Bord('0'), Bord('1'), ])	,	Chem([Bord('1'), Bord('0'), ])),
		(Chem([Bord('1'), Bord('1'), ])	,	Chem([Bord('2'), Bord('0'), ])),
		(Chem([Bord('2'), Bord('1'), ])	,	Chem([Bord('3'), Bord('0'), ])),
		(Chem([Bord('3'), Bord('1'), ])	,	Chem([Bord('4'), Bord('0'), ])),
		(Chem([Bord('4'), Bord('1'), ])	,	Chem([Bord('0'), Bord('0'), ])),
		]
	
	
	etat4.prim.elems = [Figure(2, [Chem([Bord('0'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('0'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('0'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('0'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('1'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('1'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('1'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('1'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('2'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('2'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('2'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('2'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('3'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('3'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('3'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('3'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('4'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('4'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('4'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('4'), Sub('1'), Sub('1'), Bord('0'), ]), ])]
	etat4.grid.elems = [
		Figure(1, [Chem([Bord('1'), Bord('0'), ]), Chem([Bord('1'), Intern(''), ]), Chem([Bord('1'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('4'), Bord('0'), ]), Chem([Bord('4'), Intern(''), ]), Chem([Bord('4'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('2'), Bord('0'), ]), Chem([Bord('2'), Intern(''), ]), Chem([Bord('2'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('0'), Bord('0'), ]), Chem([Bord('0'), Intern(''), ]), Chem([Bord('0'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('3'), Bord('0'), ]), Chem([Bord('3'), Intern(''), ]), Chem([Bord('3'), Bord('1'), ]), ]), ]
	
	
	etat4.space = [Chem([Bord('4'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('2'), Intern('0'), Intern('0'), ]), Chem([Bord('2'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('3'), Intern('0'), Intern('0'), ]), Chem([Bord('4'), Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('4'), Intern('0'), Intern('0'), ]), ]
	
	etat4.initMat[Chem([Sub('0')])] = FMat([
		[Coef('Var'  , 0.102266    ), Coef('Var'  , 0.0956376   ), Coef('Var'  , 0.089757    ), Coef('Var'  , 0.079532    ), Coef('Var'  , 0.0682307   ), Coef('Var'  , 0.0590236   ), Coef('Var'  , 0.0480221   ), Coef('Var'  , 0.0610073   ), Coef('Var'  , 0.0735723   ), Coef('Var'  , 0.0873577   ), ], 
		[Coef('Var'  , 0.142873    ), Coef('Var'  , 0.126539    ), Coef('Var'  , 0.111224    ), Coef('Var'  , 0.0979166   ), Coef('Var'  , 0.0830957   ), Coef('Var'  , 0.0734673   ), Coef('Var'  , 0.06213     ), Coef('Var'  , 0.0854639   ), Coef('Var'  , 0.109368    ), Coef('Var'  , 0.124953    ), ], 
		[Coef('Var'  , 0.136206    ), Coef('Var'  , 0.121153    ), Coef('Var'  , 0.109025    ), Coef('Var'  , 0.106477    ), Coef('Var'  , 0.105739    ), Coef('Var'  , 0.126447    ), Coef('Var'  , 0.148819    ), Coef('Var'  , 0.15952     ), Coef('Var'  , 0.172778    ), Coef('Var'  , 0.152766    ), ], 
		[Coef('Var'  , 0.139733    ), Coef('Var'  , 0.129224    ), Coef('Var'  , 0.121271    ), Coef('Var'  , 0.131163    ), Coef('Var'  , 0.143175    ), Coef('Var'  , 0.192859    ), Coef('Var'  , 0.245306    ), Coef('Var'  , 0.24251     ), Coef('Var'  , 0.243201    ), Coef('Var'  , 0.189709    ), ], 
		[Coef('Var'  , 0.10105     ), Coef('Var'  , 0.101069    ), Coef('Var'  , 0.102978    ), Coef('Var'  , 0.11629     ), Coef('Var'  , 0.132459    ), Coef('Var'  , 0.150415    ), Coef('Var'  , 0.171492    ), Coef('Var'  , 0.157983    ), Coef('Var'  , 0.146778    ), Coef('Var'  , 0.123094    ), ], 
		[Coef('Var'  , 0.0667504   ), Coef('Var'  , 0.0792847   ), Coef('Var'  , 0.0920307   ), Coef('Var'  , 0.109634    ), Coef('Var'  , 0.129796    ), Coef('Var'  , 0.114614    ), Coef('Var'  , 0.102371    ), Coef('Var'  , 0.0775879   ), Coef('Var'  , 0.0535962   ), Coef('Var'  , 0.0606132   ), ], 
		[Coef('Var'  , 0.075753    ), Coef('Var'  , 0.0876936   ), Coef('Var'  , 0.0985969   ), Coef('Var'  , 0.104404    ), Coef('Var'  , 0.110685    ), Coef('Var'  , 0.0949807   ), Coef('Var'  , 0.079626    ), Coef('Var'  , 0.067109    ), Coef('Var'  , 0.0534542   ), Coef('Var'  , 0.0656312   ), ], 
		[Coef('Var'  , 0.0702934   ), Coef('Var'  , 0.0798456   ), Coef('Var'  , 0.0865748   ), Coef('Var'  , 0.082521    ), Coef('Var'  , 0.0764101   ), Coef('Var'  , 0.0633591   ), Coef('Var'  , 0.0481132   ), Coef('Var'  , 0.0481347   ), Coef('Var'  , 0.0452556   ), Coef('Var'  , 0.0594914   ), ], 
		[Coef('Var'  , 0.0758234   ), Coef('Var'  , 0.0830155   ), Coef('Var'  , 0.087854    ), Coef('Var'  , 0.0800033   ), Coef('Var'  , 0.0705878   ), Coef('Var'  , 0.0578073   ), Coef('Var'  , 0.0435408   ), Coef('Var'  , 0.046177    ), Coef('Var'  , 0.0466599   ), Coef('Var'  , 0.0626343   ), ], 
		[Coef('Var'  , 0.089252    ), Coef('Var'  , 0.0965372   ), Coef('Var'  , 0.100689    ), Coef('Var'  , 0.0920588   ), Coef('Var'  , 0.0798224   ), Coef('Var'  , 0.0670259   ), Coef('Var'  , 0.0505795   ), Coef('Var'  , 0.0545079   ), Coef('Var'  , 0.0553373   ), Coef('Var'  , 0.07375     ), ], ])
	etat4.initMat[Chem([Sub('1')])] = FMat([
		[Coef('Var'  , 0.147512    ), Coef('Var'  , 0.159437    ), Coef('Var'  , 0.1736      ), Coef('Var'  , 0.153658    ), Coef('Var'  , 0.136474    ), Coef('Var'  , 0.120216    ), Coef('Var'  , 0.106362    ), Coef('Var'  , 0.10344     ), Coef('Var'  , 0.102266    ), Coef('Var'  , 0.124034    ), ], 
		[Coef('Var'  , 0.243097    ), Coef('Var'  , 0.23912     ), Coef('Var'  , 0.239647    ), Coef('Var'  , 0.186009    ), Coef('Var'  , 0.137127    ), Coef('Var'  , 0.12766     ), Coef('Var'  , 0.121467    ), Coef('Var'  , 0.13099     ), Coef('Var'  , 0.142873    ), Coef('Var'  , 0.19136     ), ], 
		[Coef('Var'  , 0.172774    ), Coef('Var'  , 0.159674    ), Coef('Var'  , 0.149312    ), Coef('Var'  , 0.127242    ), Coef('Var'  , 0.10694     ), Coef('Var'  , 0.107455    ), Coef('Var'  , 0.109729    ), Coef('Var'  , 0.121527    ), Coef('Var'  , 0.136206    ), Coef('Var'  , 0.152729    ), ], 
		[Coef('Var'  , 0.106468    ), Coef('Var'  , 0.0808842   ), Coef('Var'  , 0.0566205   ), Coef('Var'  , 0.0659424   ), Coef('Var'  , 0.0746329   ), Coef('Var'  , 0.0898211   ), Coef('Var'  , 0.104682    ), Coef('Var'  , 0.12127     ), Coef('Var'  , 0.139733    ), Coef('Var'  , 0.121613    ), ], 
		[Coef('Var'  , 0.0737085   ), Coef('Var'  , 0.061957    ), Coef('Var'  , 0.0494663   ), Coef('Var'  , 0.0604183   ), Coef('Var'  , 0.0691911   ), Coef('Var'  , 0.0795508   ), Coef('Var'  , 0.0886662   ), Coef('Var'  , 0.0945073   ), Coef('Var'  , 0.10105     ), Coef('Var'  , 0.0868889   ), ], 
		[Coef('Var'  , 0.0423374   ), Coef('Var'  , 0.0417265   ), Coef('Var'  , 0.0384567   ), Coef('Var'  , 0.0501815   ), Coef('Var'  , 0.0589532   ), Coef('Var'  , 0.0673541   ), Coef('Var'  , 0.0738438   ), Coef('Var'  , 0.0708254   ), Coef('Var'  , 0.0667504   ), Coef('Var'  , 0.0553636   ), ], 
		[Coef('Var'  , 0.0483342   ), Coef('Var'  , 0.0507541   ), Coef('Var'  , 0.0502336   ), Coef('Var'  , 0.066268    ), Coef('Var'  , 0.0792806   ), Coef('Var'  , 0.0864963   ), Coef('Var'  , 0.0914656   ), Coef('Var'  , 0.0845308   ), Coef('Var'  , 0.075753    ), Coef('Var'  , 0.0632442   ), ], 
		[Coef('Var'  , 0.0451235   ), Coef('Var'  , 0.0476077   ), Coef('Var'  , 0.0470738   ), Coef('Var'  , 0.0617187   ), Coef('Var'  , 0.0742506   ), Coef('Var'  , 0.0806721   ), Coef('Var'  , 0.0853228   ), Coef('Var'  , 0.0791474   ), Coef('Var'  , 0.0702934   ), Coef('Var'  , 0.0594541   ), ], 
		[Coef('Var'  , 0.0538428   ), Coef('Var'  , 0.0681883   ), Coef('Var'  , 0.0811566   ), Coef('Var'  , 0.0972083   ), Coef('Var'  , 0.113162    ), Coef('Var'  , 0.106802    ), Coef('Var'  , 0.0999956   ), Coef('Var'  , 0.088917    ), Coef('Var'  , 0.0758234   ), Coef('Var'  , 0.066142    ), ], 
		[Coef('Var'  , 0.0668031   ), Coef('Var'  , 0.090651    ), Coef('Var'  , 0.114433    ), Coef('Var'  , 0.131353    ), Coef('Var'  , 0.149988    ), Coef('Var'  , 0.133972    ), Coef('Var'  , 0.118466    ), Coef('Var'  , 0.104845    ), Coef('Var'  , 0.089252    ), Coef('Var'  , 0.0791722   ), ], ])
	etat4.initMat[Chem([Sub('2')])] = FMat([
		[Coef('Var'  , 0.148939    ), Coef('Var'  , 0.125992    ), Coef('Var'  , 0.104297    ), Coef('Var'  , 0.105168    ), Coef('Var'  , 0.107354    ), Coef('Var'  , 0.120788    ), Coef('Var'  , 0.136474    ), Coef('Var'  , 0.153879    ), Coef('Var'  , 0.173989    ), Coef('Var'  , 0.160461    ), ], 
		[Coef('Var'  , 0.0568249   ), Coef('Var'  , 0.0675985   ), Coef('Var'  , 0.0777032   ), Coef('Var'  , 0.0923184   ), Coef('Var'  , 0.106399    ), Coef('Var'  , 0.120532    ), Coef('Var'  , 0.137127    ), Coef('Var'  , 0.118205    ), Coef('Var'  , 0.103477    ), Coef('Var'  , 0.0790976   ), ], 
		[Coef('Var'  , 0.0561851   ), Coef('Var'  , 0.0695273   ), Coef('Var'  , 0.0793009   ), Coef('Var'  , 0.0898447   ), Coef('Var'  , 0.0979623   ), Coef('Var'  , 0.102316    ), Coef('Var'  , 0.10694     ), Coef('Var'  , 0.0919867   ), Coef('Var'  , 0.0778619   ), Coef('Var'  , 0.0677602   ), ], 
		[Coef('Var'  , 0.042331    ), Coef('Var'  , 0.0567535   ), Coef('Var'  , 0.0686934   ), Coef('Var'  , 0.0786075   ), Coef('Var'  , 0.0863413   ), Coef('Var'  , 0.0812057   ), Coef('Var'  , 0.0746329   ), Coef('Var'  , 0.0605618   ), Coef('Var'  , 0.0451826   ), Coef('Var'  , 0.0446911   ), ], 
		[Coef('Var'  , 0.0457575   ), Coef('Var'  , 0.0594165   ), Coef('Var'  , 0.0698943   ), Coef('Var'  , 0.076557    ), Coef('Var'  , 0.0810622   ), Coef('Var'  , 0.0761105   ), Coef('Var'  , 0.0691911   ), Coef('Var'  , 0.0585255   ), Coef('Var'  , 0.0450669   ), Coef('Var'  , 0.0471018   ), ], 
		[Coef('Var'  , 0.0379926   ), Coef('Var'  , 0.0501367   ), Coef('Var'  , 0.0620057   ), Coef('Var'  , 0.0672018   ), Coef('Var'  , 0.072109    ), Coef('Var'  , 0.0664157   ), Coef('Var'  , 0.0589532   ), Coef('Var'  , 0.0493865   ), Coef('Var'  , 0.0371217   ), Coef('Var'  , 0.0383899   ), ], 
		[Coef('Var'  , 0.0846008   ), Coef('Var'  , 0.101019    ), Coef('Var'  , 0.11652     ), Coef('Var'  , 0.110061    ), Coef('Var'  , 0.102896    ), Coef('Var'  , 0.092057    ), Coef('Var'  , 0.0792806   ), Coef('Var'  , 0.0696641   ), Coef('Var'  , 0.0571636   ), Coef('Var'  , 0.0719554   ), ], 
		[Coef('Var'  , 0.102442    ), Coef('Var'  , 0.115563    ), Coef('Var'  , 0.132616    ), Coef('Var'  , 0.114816    ), Coef('Var'  , 0.0998597   ), Coef('Var'  , 0.0871777   ), Coef('Var'  , 0.0742506   ), Coef('Var'  , 0.0660066   ), Coef('Var'  , 0.0566068   ), Coef('Var'  , 0.078841    ), ], 
		[Coef('Var'  , 0.180186    ), Coef('Var'  , 0.161693    ), Coef('Var'  , 0.145063    ), Coef('Var'  , 0.13031     ), Coef('Var'  , 0.117017    ), Coef('Var'  , 0.114807    ), Coef('Var'  , 0.113162    ), Coef('Var'  , 0.133985    ), Coef('Var'  , 0.155281    ), Coef('Var'  , 0.167127    ), ], 
		[Coef('Var'  , 0.244741    ), Coef('Var'  , 0.192301    ), Coef('Var'  , 0.143907    ), Coef('Var'  , 0.135115    ), Coef('Var'  , 0.128998    ), Coef('Var'  , 0.138591    ), Coef('Var'  , 0.149988    ), Coef('Var'  , 0.197799    ), Coef('Var'  , 0.248249    ), Coef('Var'  , 0.244575    ), ], ])
	etat4.initMat[Chem([Sub('3')])] = FMat([
		[Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0374188   ), Coef('Var'  , 0.0750262   ), Coef('Var'  , 0.111516    ), Coef('Var'  , 0.148939    ), Coef('Var'  , 0.199097    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0241201   ), Coef('Var'  , 0.0473949   ), Coef('Var'  , 0.052472    ), Coef('Var'  , 0.0568249   ), Coef('Var'  , 0.0283519   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.026917    ), Coef('Var'  , 0.0516907   ), Coef('Var'  , 0.0558029   ), Coef('Var'  , 0.0561851   ), Coef('Var'  , 0.0288859   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0223159   ), Coef('Var'  , 0.0433451   ), Coef('Var'  , 0.0440564   ), Coef('Var'  , 0.042331    ), Coef('Var'  , 0.0217405   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0258955   ), Coef('Var'  , 0.0505034   ), Coef('Var'  , 0.0496686   ), Coef('Var'  , 0.0457575   ), Coef('Var'  , 0.0237731   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0244618   ), Coef('Var'  , 0.0492505   ), Coef('Var'  , 0.0436388   ), Coef('Var'  , 0.0379926   ), Coef('Var'  , 0.019177    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.203923    ), Coef('Var'  , 0.157862    ), Coef('Var'  , 0.121576    ), Coef('Var'  , 0.0846008   ), Coef('Var'  , 0.0426532   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.367563    ), Coef('Var'  , 0.237575    ), Coef('Var'  , 0.167942    ), Coef('Var'  , 0.102442    ), Coef('Var'  , 0.0503793   ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.214111    ), Coef('Var'  , 0.179172    ), Coef('Var'  , 0.178776    ), Coef('Var'  , 0.180186    ), Coef('Var'  , 0.214665    ), ], 
		[Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0532747   ), Coef('Var'  , 0.10818     ), Coef('Var'  , 0.174551    ), Coef('Var'  , 0.244741    ), Coef('Var'  , 0.371276    ), ], ])
	etat4.initMat[Chem([Sub('G')])] = FMat([
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
	etat4.initMat[Chem([Sub('4')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.198294    ), Coef('Var'  , 0.147512    ), Coef('Var'  , 0.109912    ), Coef('Var'  , 0.0735723   ), Coef('Var'  , 0.0366179   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.37057     ), Coef('Var'  , 0.243097    ), Coef('Var'  , 0.174734    ), Coef('Var'  , 0.109368    ), Coef('Var'  , 0.0541632   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.210544    ), Coef('Var'  , 0.172774    ), Coef('Var'  , 0.171126    ), Coef('Var'  , 0.172778    ), Coef('Var'  , 0.210582    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.052553    ), Coef('Var'  , 0.106468    ), Coef('Var'  , 0.173202    ), Coef('Var'  , 0.243201    ), Coef('Var'  , 0.370649    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0367356   ), Coef('Var'  , 0.0737085   ), Coef('Var'  , 0.109677    ), Coef('Var'  , 0.146778    ), Coef('Var'  , 0.197941    ), Coef('Const', 0.25        ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0217186   ), Coef('Var'  , 0.0423374   ), Coef('Var'  , 0.0486868   ), Coef('Var'  , 0.0535962   ), Coef('Var'  , 0.0269682   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0248479   ), Coef('Var'  , 0.0483342   ), Coef('Var'  , 0.0520827   ), Coef('Var'  , 0.0534542   ), Coef('Var'  , 0.0272348   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0234339   ), Coef('Var'  , 0.0451235   ), Coef('Var'  , 0.0469051   ), Coef('Var'  , 0.0452556   ), Coef('Var'  , 0.0234712   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0275035   ), Coef('Var'  , 0.0538428   ), Coef('Var'  , 0.0514994   ), Coef('Var'  , 0.0466599   ), Coef('Var'  , 0.0239959   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.033799    ), Coef('Var'  , 0.0668031   ), Coef('Var'  , 0.0621758   ), Coef('Var'  , 0.0553373   ), Coef('Var'  , 0.0283768   ), Coef('Const', 0           ), Coef('Const', 0           ), ], ])
	etat4.initMat[Chem([Sub('5')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0243894   ), Coef('Var'  , 0.0480221   ), Coef('Var'  , 0.0463573   ), Coef('Var'  , 0.0427653   ), Coef('Var'  , 0.0219679   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0313007   ), Coef('Var'  , 0.06213     ), Coef('Var'  , 0.0574418   ), Coef('Var'  , 0.0511444   ), Coef('Var'  , 0.0261411   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.198938    ), Coef('Var'  , 0.148819    ), Coef('Var'  , 0.112043    ), Coef('Var'  , 0.0764359   ), Coef('Var'  , 0.0381046   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.37186     ), Coef('Var'  , 0.245306    ), Coef('Var'  , 0.176724    ), Coef('Var'  , 0.11048     ), Coef('Var'  , 0.054864    ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.210042    ), Coef('Var'  , 0.171492    ), Coef('Var'  , 0.170061    ), Coef('Var'  , 0.171435    ), Coef('Var'  , 0.21002     ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0506197   ), Coef('Var'  , 0.102371    ), Coef('Var'  , 0.168702    ), Coef('Var'  , 0.237922    ), Coef('Var'  , 0.368083    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0398741   ), Coef('Var'  , 0.079626    ), Coef('Var'  , 0.116384    ), Coef('Var'  , 0.15355     ), Coef('Var'  , 0.20151     ), Coef('Const', 0.25        ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0246635   ), Coef('Var'  , 0.0481132   ), Coef('Var'  , 0.0541719   ), Coef('Var'  , 0.0585693   ), Coef('Var'  , 0.0295084   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0221811   ), Coef('Var'  , 0.0435408   ), Coef('Var'  , 0.0465229   ), Coef('Var'  , 0.048364    ), Coef('Var'  , 0.0243419   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0261311   ), Coef('Var'  , 0.0505795   ), Coef('Var'  , 0.0515909   ), Coef('Var'  , 0.0493338   ), Coef('Var'  , 0.0254598   ), Coef('Const', 0           ), Coef('Const', 0           ), ], ])
	etat4.initMat[Chem([Sub('6')])] = FMat([
		[Coef('Var'  , 0.0912252   ), Coef('Var'  , 0.0870266   ), Coef('Var'  , 0.0817482   ), Coef('Var'  , 0.0861866   ), Coef('Var'  , 0.089757    ), Coef('Var'  , 0.0975983   ), Coef('Var'  , 0.106362    ), Coef('Var'  , 0.105973    ), Coef('Var'  , 0.107354    ), Coef('Var'  , 0.0990106   ), ], 
		[Coef('Var'  , 0.0924326   ), Coef('Var'  , 0.0952235   ), Coef('Var'  , 0.0949616   ), Coef('Var'  , 0.104046    ), Coef('Var'  , 0.111224    ), Coef('Var'  , 0.115951    ), Coef('Var'  , 0.121467    ), Coef('Var'  , 0.113272    ), Coef('Var'  , 0.106399    ), Coef('Var'  , 0.0999989   ), ], 
		[Coef('Var'  , 0.0909398   ), Coef('Var'  , 0.0943057   ), Coef('Var'  , 0.096198    ), Coef('Var'  , 0.102175    ), Coef('Var'  , 0.109025    ), Coef('Var'  , 0.108311    ), Coef('Var'  , 0.109729    ), Coef('Var'  , 0.103546    ), Coef('Var'  , 0.0979623   ), Coef('Var'  , 0.0953023   ), ], 
		[Coef('Var'  , 0.0882061   ), Coef('Var'  , 0.0985143   ), Coef('Var'  , 0.107883    ), Coef('Var'  , 0.114093    ), Coef('Var'  , 0.121271    ), Coef('Var'  , 0.112374    ), Coef('Var'  , 0.104682    ), Coef('Var'  , 0.0958045   ), Coef('Var'  , 0.0863413   ), Coef('Var'  , 0.0881803   ), ], 
		[Coef('Var'  , 0.0880794   ), Coef('Var'  , 0.0944847   ), Coef('Var'  , 0.102379    ), Coef('Var'  , 0.101438    ), Coef('Var'  , 0.102978    ), Coef('Var'  , 0.0952699   ), Coef('Var'  , 0.0886662   ), Coef('Var'  , 0.0852676   ), Coef('Var'  , 0.0810622   ), Coef('Var'  , 0.0848759   ), ], 
		[Coef('Var'  , 0.0898025   ), Coef('Var'  , 0.0966115   ), Coef('Var'  , 0.105808    ), Coef('Var'  , 0.0977642   ), Coef('Var'  , 0.0920307   ), Coef('Var'  , 0.0828202   ), Coef('Var'  , 0.0738438   ), Coef('Var'  , 0.0734225   ), Coef('Var'  , 0.072109    ), Coef('Var'  , 0.0807292   ), ], 
		[Coef('Var'  , 0.118551    ), Coef('Var'  , 0.116453    ), Coef('Var'  , 0.11588     ), Coef('Var'  , 0.106779    ), Coef('Var'  , 0.0985969   ), Coef('Var'  , 0.0954318   ), Coef('Var'  , 0.0914656   ), Coef('Var'  , 0.0978297   ), Coef('Var'  , 0.102896    ), Coef('Var'  , 0.110667    ), ], 
		[Coef('Var'  , 0.113764    ), Coef('Var'  , 0.107304    ), Coef('Var'  , 0.102486    ), Coef('Var'  , 0.0949661   ), Coef('Var'  , 0.0865748   ), Coef('Var'  , 0.0869526   ), Coef('Var'  , 0.0853228   ), Coef('Var'  , 0.0927601   ), Coef('Var'  , 0.0998597   ), Coef('Var'  , 0.105796    ), ], 
		[Coef('Var'  , 0.114482    ), Coef('Var'  , 0.104618    ), Coef('Var'  , 0.0953441   ), Coef('Var'  , 0.0920851   ), Coef('Var'  , 0.087854    ), Coef('Var'  , 0.0946556   ), Coef('Var'  , 0.0999956   ), Coef('Var'  , 0.108562    ), Coef('Var'  , 0.117017    ), Coef('Var'  , 0.115193    ), ], 
		[Coef('Var'  , 0.112517    ), Coef('Var'  , 0.105458    ), Coef('Var'  , 0.0973128   ), Coef('Var'  , 0.100467    ), Coef('Var'  , 0.100689    ), Coef('Var'  , 0.110636    ), Coef('Var'  , 0.118466    ), Coef('Var'  , 0.123562    ), Coef('Var'  , 0.128998    ), Coef('Var'  , 0.120246    ), ], ])
	etat4.initMat[Chem([Sub('7')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.022126    ), Coef('Var'  , 0.0430863   ), Coef('Var'  , 0.0468915   ), Coef('Var'  , 0.0487585   ), Coef('Var'  , 0.0247654   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0244952   ), Coef('Var'  , 0.047448    ), Coef('Var'  , 0.0485209   ), Coef('Var'  , 0.0465625   ), Coef('Var'  , 0.0240257   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0272757   ), Coef('Var'  , 0.0534808   ), Coef('Var'  , 0.0531233   ), Coef('Var'  , 0.0499154   ), Coef('Var'  , 0.0258476   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0309518   ), Coef('Var'  , 0.0612391   ), Coef('Var'  , 0.0559979   ), Coef('Var'  , 0.0489088   ), Coef('Var'  , 0.0250461   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.197772    ), Coef('Var'  , 0.146471    ), Coef('Var'  , 0.109589    ), Coef('Var'  , 0.0738042   ), Coef('Var'  , 0.036817    ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.367839    ), Coef('Var'  , 0.237387    ), Coef('Var'  , 0.167456    ), Coef('Var'  , 0.1005      ), Coef('Var'  , 0.0496162   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.214135    ), Coef('Var'  , 0.179418    ), Coef('Var'  , 0.178914    ), Coef('Var'  , 0.180566    ), Coef('Var'  , 0.214779    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0521275   ), Coef('Var'  , 0.105441    ), Coef('Var'  , 0.170845    ), Coef('Var'  , 0.239519    ), Coef('Var'  , 0.368717    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0376754   ), Coef('Var'  , 0.075764    ), Coef('Var'  , 0.11292     ), Coef('Var'  , 0.151234    ), Coef('Var'  , 0.200245    ), Coef('Const', 0.25        ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0256023   ), Coef('Var'  , 0.0502648   ), Coef('Var'  , 0.0557433   ), Coef('Var'  , 0.0602315   ), Coef('Var'  , 0.030141    ), Coef('Const', 0           ), Coef('Const', 0           ), ], ])
	etat4.initMat[Chem([Sub('8')])] = FMat([
		[Coef('Var'  , 0.0690278   ), Coef('Var'  , 0.0807979   ), Coef('Var'  , 0.0912252   ), Coef('Var'  , 0.097633    ), Coef('Var'  , 0.104297    ), Coef('Var'  , 0.0893139   ), Coef('Var'  , 0.0750262   ), Coef('Var'  , 0.0621842   ), Coef('Var'  , 0.0487585   ), Coef('Var'  , 0.0598255   ), ], 
		[Coef('Var'  , 0.0756757   ), Coef('Var'  , 0.0857545   ), Coef('Var'  , 0.0924326   ), Coef('Var'  , 0.0861736   ), Coef('Var'  , 0.0777032   ), Coef('Var'  , 0.0633666   ), Coef('Var'  , 0.0473949   ), Coef('Var'  , 0.0481458   ), Coef('Var'  , 0.0465625   ), Coef('Var'  , 0.0628531   ), ], 
		[Coef('Var'  , 0.0764657   ), Coef('Var'  , 0.0850498   ), Coef('Var'  , 0.0909398   ), Coef('Var'  , 0.0867406   ), Coef('Var'  , 0.0793009   ), Coef('Var'  , 0.0675585   ), Coef('Var'  , 0.0516907   ), Coef('Var'  , 0.0527647   ), Coef('Var'  , 0.0499154   ), Coef('Var'  , 0.0647984   ), ], 
		[Coef('Var'  , 0.0792098   ), Coef('Var'  , 0.0847084   ), Coef('Var'  , 0.0882061   ), Coef('Var'  , 0.0795987   ), Coef('Var'  , 0.0686934   ), Coef('Var'  , 0.0573288   ), Coef('Var'  , 0.0433451   ), Coef('Var'  , 0.047362    ), Coef('Var'  , 0.0489088   ), Coef('Var'  , 0.0651687   ), ], 
		[Coef('Var'  , 0.1002      ), Coef('Var'  , 0.0935741   ), Coef('Var'  , 0.0880794   ), Coef('Var'  , 0.0796056   ), Coef('Var'  , 0.0698943   ), Coef('Var'  , 0.0615388   ), Coef('Var'  , 0.0505034   ), Coef('Var'  , 0.0627125   ), Coef('Var'  , 0.0738042   ), Coef('Var'  , 0.0864288   ), ], 
		[Coef('Var'  , 0.128767    ), Coef('Var'  , 0.108024    ), Coef('Var'  , 0.0898025   ), Coef('Var'  , 0.0754468   ), Coef('Var'  , 0.0620057   ), Coef('Var'  , 0.0554215   ), Coef('Var'  , 0.0492505   ), Coef('Var'  , 0.0740781   ), Coef('Var'  , 0.1005      ), Coef('Var'  , 0.113153    ), ], 
		[Coef('Var'  , 0.145076    ), Coef('Var'  , 0.130818    ), Coef('Var'  , 0.118551    ), Coef('Var'  , 0.117337    ), Coef('Var'  , 0.11652     ), Coef('Var'  , 0.137288    ), Coef('Var'  , 0.157862    ), Coef('Var'  , 0.168702    ), Coef('Var'  , 0.180566    ), Coef('Var'  , 0.161625    ), ], 
		[Coef('Var'  , 0.135935    ), Coef('Var'  , 0.123311    ), Coef('Var'  , 0.113764    ), Coef('Var'  , 0.121347    ), Coef('Var'  , 0.132616    ), Coef('Var'  , 0.182746    ), Coef('Var'  , 0.237575    ), Coef('Var'  , 0.23628     ), Coef('Var'  , 0.239519    ), Coef('Var'  , 0.185864    ), ], 
		[Coef('Var'  , 0.107594    ), Coef('Var'  , 0.110398    ), Coef('Var'  , 0.114482    ), Coef('Var'  , 0.128937    ), Coef('Var'  , 0.145063    ), Coef('Var'  , 0.161138    ), Coef('Var'  , 0.179172    ), Coef('Var'  , 0.164355    ), Coef('Var'  , 0.151234    ), Coef('Var'  , 0.128733    ), ], 
		[Coef('Var'  , 0.0820498   ), Coef('Var'  , 0.0975645   ), Coef('Var'  , 0.112517    ), Coef('Var'  , 0.12718     ), Coef('Var'  , 0.143907    ), Coef('Var'  , 0.124299    ), Coef('Var'  , 0.10818     ), Coef('Var'  , 0.0834156   ), Coef('Var'  , 0.0602315   ), Coef('Var'  , 0.07155     ), ], ])
	etat4.initMat[Chem([Sub('9')])] = FMat([
		[Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.211364    ), Coef('Var'  , 0.173989    ), Coef('Var'  , 0.172507    ), Coef('Var'  , 0.1736      ), Coef('Var'  , 0.211143    ), ], 
		[Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0507457   ), Coef('Var'  , 0.103477    ), Coef('Var'  , 0.169295    ), Coef('Var'  , 0.239647    ), Coef('Var'  , 0.368549    ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0388743   ), Coef('Var'  , 0.0778619   ), Coef('Var'  , 0.113004    ), Coef('Var'  , 0.149312    ), Coef('Var'  , 0.19913     ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0229506   ), Coef('Var'  , 0.0451826   ), Coef('Var'  , 0.0512818   ), Coef('Var'  , 0.0566205   ), Coef('Var'  , 0.0283312   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0233286   ), Coef('Var'  , 0.0450669   ), Coef('Var'  , 0.0485501   ), Coef('Var'  , 0.0494663   ), Coef('Var'  , 0.0252214   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0192128   ), Coef('Var'  , 0.0371217   ), Coef('Var'  , 0.0392207   ), Coef('Var'  , 0.0384567   ), Coef('Var'  , 0.0200079   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0293022   ), Coef('Var'  , 0.0571636   ), Coef('Var'  , 0.0552085   ), Coef('Var'  , 0.0502336   ), Coef('Var'  , 0.0259062   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0284617   ), Coef('Var'  , 0.0566068   ), Coef('Var'  , 0.0526355   ), Coef('Var'  , 0.0470738   ), Coef('Var'  , 0.0241738   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.202462    ), Coef('Var'  , 0.155281    ), Coef('Var'  , 0.118146    ), Coef('Var'  , 0.0811566   ), Coef('Var'  , 0.0406847   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.373298    ), Coef('Var'  , 0.248249    ), Coef('Var'  , 0.18015     ), Coef('Var'  , 0.114433    ), Coef('Var'  , 0.056852    ), ], ])
	etat4.initMat[Chem([Sub('10')])] = FMat([
		[Coef('Var'  , 0.0817482   ), Coef('Var'  , 0.076349    ), Coef('Var'  , 0.0690278   ), Coef('Var'  , 0.0571862   ), Coef('Var'  , 0.0430863   ), Coef('Var'  , 0.0440939   ), Coef('Var'  , 0.0427653   ), Coef('Var'  , 0.0566021   ), Coef('Var'  , 0.0682307   ), Coef('Var'  , 0.0759231   ), ], 
		[Coef('Var'  , 0.0949616   ), Coef('Var'  , 0.0871238   ), Coef('Var'  , 0.0756757   ), Coef('Var'  , 0.0633227   ), Coef('Var'  , 0.047448    ), Coef('Var'  , 0.0506364   ), Coef('Var'  , 0.0511444   ), Coef('Var'  , 0.0683078   ), Coef('Var'  , 0.0830957   ), Coef('Var'  , 0.0904631   ), ], 
		[Coef('Var'  , 0.096198    ), Coef('Var'  , 0.0871574   ), Coef('Var'  , 0.0764657   ), Coef('Var'  , 0.0662264   ), Coef('Var'  , 0.0534808   ), Coef('Var'  , 0.0653803   ), Coef('Var'  , 0.0764359   ), Coef('Var'  , 0.0906136   ), Coef('Var'  , 0.105739    ), Coef('Var'  , 0.100716    ), ], 
		[Coef('Var'  , 0.107883    ), Coef('Var'  , 0.0940512   ), Coef('Var'  , 0.0792098   ), Coef('Var'  , 0.0710744   ), Coef('Var'  , 0.0612391   ), Coef('Var'  , 0.0858158   ), Coef('Var'  , 0.11048     ), Coef('Var'  , 0.125863    ), Coef('Var'  , 0.143175    ), Coef('Var'  , 0.124927    ), ], 
		[Coef('Var'  , 0.102379    ), Coef('Var'  , 0.100134    ), Coef('Var'  , 0.1002      ), Coef('Var'  , 0.122384    ), Coef('Var'  , 0.146471    ), Coef('Var'  , 0.157792    ), Coef('Var'  , 0.171435    ), Coef('Var'  , 0.150394    ), Coef('Var'  , 0.132459    ), Coef('Var'  , 0.115896    ), ], 
		[Coef('Var'  , 0.105808    ), Coef('Var'  , 0.115662    ), Coef('Var'  , 0.128767    ), Coef('Var'  , 0.181377    ), Coef('Var'  , 0.237387    ), Coef('Var'  , 0.235922    ), Coef('Var'  , 0.237922    ), Coef('Var'  , 0.182077    ), Coef('Var'  , 0.129796    ), Coef('Var'  , 0.116119    ), ], 
		[Coef('Var'  , 0.11588     ), Coef('Var'  , 0.129327    ), Coef('Var'  , 0.145076    ), Coef('Var'  , 0.160981    ), Coef('Var'  , 0.179418    ), Coef('Var'  , 0.165645    ), Coef('Var'  , 0.15355     ), Coef('Var'  , 0.131616    ), Coef('Var'  , 0.110685    ), Coef('Var'  , 0.112588    ), ], 
		[Coef('Var'  , 0.102486    ), Coef('Var'  , 0.118288    ), Coef('Var'  , 0.135935    ), Coef('Var'  , 0.119275    ), Coef('Var'  , 0.105441    ), Coef('Var'  , 0.0816359   ), Coef('Var'  , 0.0585693   ), Coef('Var'  , 0.068204    ), Coef('Var'  , 0.0764101   ), Coef('Var'  , 0.0898363   ), ], 
		[Coef('Var'  , 0.0953441   ), Coef('Var'  , 0.101196    ), Coef('Var'  , 0.107594    ), Coef('Var'  , 0.0911634   ), Coef('Var'  , 0.075764    ), Coef('Var'  , 0.0620172   ), Coef('Var'  , 0.048364    ), Coef('Var'  , 0.0599681   ), Coef('Var'  , 0.0705878   ), Coef('Var'  , 0.0833342   ), ], 
		[Coef('Var'  , 0.0973128   ), Coef('Var'  , 0.0907116   ), Coef('Var'  , 0.0820498   ), Coef('Var'  , 0.0670113   ), Coef('Var'  , 0.0502648   ), Coef('Var'  , 0.0510621   ), Coef('Var'  , 0.0493338   ), Coef('Var'  , 0.0663546   ), Coef('Var'  , 0.0798224   ), Coef('Var'  , 0.0901973   ), ], ])
	
	
	
	etat5.bords   = {Bord('0'): etat13, Bord('1'): etat13, Bord('2'): etat13, Bord('3'): etat13, Bord('4'): etat13, }
	etat5.permuts = {}
	etat5.interns = {Intern('_'): etat5, }
	etat5.subs    = {Sub('0'): etat1, Sub('1'): etat2, Sub('2'): etat3, Sub('3'): etat4, Sub('G', True): Etat.etatPoint, Sub('4'): etat6, Sub('5'): etat7, Sub('6'): etat8, Sub('7'): etat9, Sub('8'): etat10, Sub('9'): etat11, Sub('10'): etat12, }
	
	etat5.buildIntern()
	
	
	etat5.eqs = [
		(Chem([Bord('3'), Sub('1'), Permut('0'), ])	,	Chem([Sub('2'), Bord('0'), ])),
		(Chem([Bord('4'), Sub('0'), Permut('0'), ])	,	Chem([Sub('2'), Bord('4'), ])),
		(Chem([Bord('1'), Sub('0'), Permut('0'), ])	,	Chem([Sub('3'), Bord('3'), ])),
		(Chem([Bord('0'), Sub('1'), Permut('0'), ])	,	Chem([Sub('3'), Bord('4'), ])),
		(Chem([Bord('2'), Sub('0'), Permut('0'), ])	,	Chem([Sub('7'), Bord('3'), ])),
		(Chem([Bord('1'), Sub('1'), Permut('0'), ])	,	Chem([Sub('7'), Bord('4'), ])),
		(Chem([Bord('3'), Sub('0'), Permut('0'), ])	,	Chem([Sub('8'), Bord('2'), ])),
		(Chem([Bord('2'), Sub('1'), Permut('0'), ])	,	Chem([Sub('8'), Bord('3'), ])),
		(Chem([Bord('0'), Sub('0'), Permut('0'), ])	,	Chem([Sub('9'), Bord('1'), ])),
		(Chem([Bord('4'), Sub('1'), Permut('0'), ])	,	Chem([Sub('9'), Bord('2'), ])),
		(Chem([Sub('0'), Bord('0'), Bord('1'), ])	,	Chem([Sub('6'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('1'), Bord('1'), ])	,	Chem([Sub('10'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('2'), Bord('1'), ])	,	Chem([Sub('5'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('3'), Bord('1'), ])	,	Chem([Sub('4'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('4'), Bord('1'), ])	,	Chem([Sub('1'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('0'), Bord('1'), ])	,	Chem([Sub('9'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('1'), Bord('1'), ])	,	Chem([Sub('2'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('2'), Bord('1'), ])	,	Chem([Sub('6'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('4'), Bord('1'), ])	,	Chem([Sub('4'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('0'), Bord('1'), ])	,	Chem([Sub('8'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('1'), Bord('1'), ])	,	Chem([Sub('6'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('3'), Bord('1'), ])	,	Chem([Sub('9'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('3'), Bord('0'), Bord('1'), ])	,	Chem([Sub('4'), Bord('4'), Bord('1'), ])),
		(Chem([Sub('3'), Bord('1'), Bord('1'), ])	,	Chem([Sub('5'), Bord('4'), Bord('1'), ])),
		(Chem([Sub('3'), Bord('2'), Bord('1'), ])	,	Chem([Sub('7'), Bord('4'), Bord('1'), ])),
		(Chem([Sub('3'), Bord('4'), Bord('1'), ])	,	Chem([Sub('9'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('4'), Bord('0'), Bord('1'), ])	,	Chem([Sub('9'), Bord('4'), Bord('1'), ])),
		(Chem([Sub('4'), Bord('3'), Bord('1'), ])	,	Chem([Sub('5'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('5'), Bord('2'), Bord('1'), ])	,	Chem([Sub('10'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('5'), Bord('3'), Bord('1'), ])	,	Chem([Sub('7'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('6'), Bord('0'), Bord('1'), ])	,	Chem([Sub('10'), Bord('4'), Bord('1'), ])),
		(Chem([Sub('6'), Bord('4'), Bord('1'), ])	,	Chem([Sub('8'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('7'), Bord('1'), Bord('1'), ])	,	Chem([Sub('10'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('7'), Bord('2'), Bord('1'), ])	,	Chem([Sub('8'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('8'), Bord('4'), Bord('1'), ])	,	Chem([Sub('10'), Bord('0'), Bord('1'), ])),
		(Chem([Bord('0'), Bord('1'), ])	,	Chem([Bord('1'), Bord('0'), ])),
		(Chem([Bord('1'), Bord('1'), ])	,	Chem([Bord('2'), Bord('0'), ])),
		(Chem([Bord('2'), Bord('1'), ])	,	Chem([Bord('3'), Bord('0'), ])),
		(Chem([Bord('3'), Bord('1'), ])	,	Chem([Bord('4'), Bord('0'), ])),
		(Chem([Bord('4'), Bord('1'), ])	,	Chem([Bord('0'), Bord('0'), ])),
		]
	
	
	etat5.prim.elems = [Figure(2, [Chem([Bord('0'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('0'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('0'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('0'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('1'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('1'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('1'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('1'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('2'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('2'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('2'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('2'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('3'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('3'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('3'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('3'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('4'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('4'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('4'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('4'), Sub('1'), Sub('1'), Bord('0'), ]), ])]
	etat5.grid.elems = [
		Figure(1, [Chem([Bord('1'), Bord('0'), ]), Chem([Bord('1'), Intern(''), ]), Chem([Bord('1'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('4'), Bord('0'), ]), Chem([Bord('4'), Intern(''), ]), Chem([Bord('4'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('2'), Bord('0'), ]), Chem([Bord('2'), Intern(''), ]), Chem([Bord('2'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('0'), Bord('0'), ]), Chem([Bord('0'), Intern(''), ]), Chem([Bord('0'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('3'), Bord('0'), ]), Chem([Bord('3'), Intern(''), ]), Chem([Bord('3'), Bord('1'), ]), ]), ]
	
	
	etat5.space = [Chem([Bord('4'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('2'), Intern('0'), Intern('0'), ]), Chem([Bord('2'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('3'), Intern('0'), Intern('0'), ]), Chem([Bord('4'), Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('4'), Intern('0'), Intern('0'), ]), ]
	
	etat5.initMat[Chem([Sub('0')])] = FMat([
		[Coef('Var'  , 0.11774     ), Coef('Var'  , 0.111481    ), Coef('Var'  , 0.10486     ), Coef('Var'  , 0.101374    ), Coef('Var'  , 0.0956337   ), Coef('Var'  , 0.0991163   ), Coef('Var'  , 0.10081     ), Coef('Var'  , 0.107754    ), Coef('Var'  , 0.115117    ), Coef('Var'  , 0.115783    ), ], 
		[Coef('Var'  , 0.0977332   ), Coef('Var'  , 0.0903161   ), Coef('Var'  , 0.0826859   ), Coef('Var'  , 0.0843696   ), Coef('Var'  , 0.0839841   ), Coef('Var'  , 0.0919094   ), Coef('Var'  , 0.0992076   ), Coef('Var'  , 0.104197    ), Coef('Var'  , 0.111397    ), Coef('Var'  , 0.103363    ), ], 
		[Coef('Var'  , 0.101077    ), Coef('Var'  , 0.0969661   ), Coef('Var'  , 0.0918856   ), Coef('Var'  , 0.0983857   ), Coef('Var'  , 0.103463    ), Coef('Var'  , 0.112828    ), Coef('Var'  , 0.121879    ), Coef('Var'  , 0.120784    ), Coef('Var'  , 0.12048     ), Coef('Var'  , 0.110578    ), ], 
		[Coef('Var'  , 0.0736629   ), Coef('Var'  , 0.0727862   ), Coef('Var'  , 0.0711049   ), Coef('Var'  , 0.0805723   ), Coef('Var'  , 0.0904639   ), Coef('Var'  , 0.0983836   ), Coef('Var'  , 0.108235    ), Coef('Var'  , 0.100503    ), Coef('Var'  , 0.0943745   ), Coef('Var'  , 0.08409     ), ], 
		[Coef('Var'  , 0.0887316   ), Coef('Var'  , 0.0924357   ), Coef('Var'  , 0.0948327   ), Coef('Var'  , 0.102303    ), Coef('Var'  , 0.110613    ), Coef('Var'  , 0.111106    ), Coef('Var'  , 0.113283    ), Coef('Var'  , 0.10605     ), Coef('Var'  , 0.0988952   ), Coef('Var'  , 0.0946889   ), ], 
		[Coef('Var'  , 0.0906921   ), Coef('Var'  , 0.0996045   ), Coef('Var'  , 0.107512    ), Coef('Var'  , 0.113333    ), Coef('Var'  , 0.120662    ), Coef('Var'  , 0.112669    ), Coef('Var'  , 0.106395    ), Coef('Var'  , 0.0987076   ), Coef('Var'  , 0.0902838   ), Coef('Var'  , 0.0916683   ), ], 
		[Coef('Var'  , 0.0957991   ), Coef('Var'  , 0.104457    ), Coef('Var'  , 0.113562    ), Coef('Var'  , 0.113463    ), Coef('Var'  , 0.114518    ), Coef('Var'  , 0.10595     ), Coef('Var'  , 0.0974678   ), Coef('Var'  , 0.0926768   ), Coef('Var'  , 0.0866936   ), Coef('Var'  , 0.0917253   ), ], 
		[Coef('Var'  , 0.0982836   ), Coef('Var'  , 0.102616    ), Coef('Var'  , 0.108856    ), Coef('Var'  , 0.0985748   ), Coef('Var'  , 0.0910603   ), Coef('Var'  , 0.0828028   ), Coef('Var'  , 0.0753262   ), Coef('Var'  , 0.0781094   ), Coef('Var'  , 0.0796594   ), Coef('Var'  , 0.0892574   ), ], 
		[Coef('Var'  , 0.11346     ), Coef('Var'  , 0.113663    ), Coef('Var'  , 0.115143    ), Coef('Var'  , 0.106915    ), Coef('Var'  , 0.0987883   ), Coef('Var'  , 0.0943456   ), Coef('Var'  , 0.088454    ), Coef('Var'  , 0.0930486   ), Coef('Var'  , 0.0963749   ), Coef('Var'  , 0.104694    ), ], 
		[Coef('Var'  , 0.122822    ), Coef('Var'  , 0.115675    ), Coef('Var'  , 0.109559    ), Coef('Var'  , 0.100709    ), Coef('Var'  , 0.0908131   ), Coef('Var'  , 0.0908906   ), Coef('Var'  , 0.0889425   ), Coef('Var'  , 0.0981699   ), Coef('Var'  , 0.106724    ), Coef('Var'  , 0.114152    ), ], ])
	etat5.initMat[Chem([Sub('1')])] = FMat([
		[Coef('Var'  , 0.141774    ), Coef('Var'  , 0.157416    ), Coef('Var'  , 0.176299    ), Coef('Var'  , 0.164177    ), Coef('Var'  , 0.15427     ), Coef('Var'  , 0.134133    ), Coef('Var'  , 0.114664    ), Coef('Var'  , 0.115936    ), Coef('Var'  , 0.11774     ), Coef('Var'  , 0.128689    ), ], 
		[Coef('Var'  , 0.133435    ), Coef('Var'  , 0.117266    ), Coef('Var'  , 0.103996    ), Coef('Var'  , 0.0790215   ), Coef('Var'  , 0.0550431   ), Coef('Var'  , 0.0632866   ), Coef('Var'  , 0.0709948   ), Coef('Var'  , 0.0842151   ), Coef('Var'  , 0.0977332   ), Coef('Var'  , 0.114338    ), ], 
		[Coef('Var'  , 0.113965    ), Coef('Var'  , 0.0974048   ), Coef('Var'  , 0.0810601   ), Coef('Var'  , 0.0675706   ), Coef('Var'  , 0.0531341   ), Coef('Var'  , 0.0653927   ), Coef('Var'  , 0.0758606   ), Coef('Var'  , 0.0890051   ), Coef('Var'  , 0.101077    ), Coef('Var'  , 0.107424    ), ], 
		[Coef('Var'  , 0.0675914   ), Coef('Var'  , 0.0554319   ), Coef('Var'  , 0.0416344   ), Coef('Var'  , 0.0396297   ), Coef('Var'  , 0.0356223   ), Coef('Var'  , 0.046838    ), Coef('Var'  , 0.0560801   ), Coef('Var'  , 0.0655945   ), Coef('Var'  , 0.0736629   ), Coef('Var'  , 0.0712302   ), ], 
		[Coef('Var'  , 0.0759512   ), Coef('Var'  , 0.0630585   ), Coef('Var'  , 0.047376    ), Coef('Var'  , 0.0479323   ), Coef('Var'  , 0.0458988   ), Coef('Var'  , 0.0607078   ), Coef('Var'  , 0.073082    ), Coef('Var'  , 0.0820782   ), Coef('Var'  , 0.0887316   ), Coef('Var'  , 0.0836332   ), ], 
		[Coef('Var'  , 0.073241    ), Coef('Var'  , 0.0613377   ), Coef('Var'  , 0.0460507   ), Coef('Var'  , 0.0486128   ), Coef('Var'  , 0.04871     ), Coef('Var'  , 0.0646605   ), Coef('Var'  , 0.0788614   ), Coef('Var'  , 0.0857853   ), Coef('Var'  , 0.0906921   ), Coef('Var'  , 0.0835007   ), ], 
		[Coef('Var'  , 0.0716869   ), Coef('Var'  , 0.0618376   ), Coef('Var'  , 0.0503708   ), Coef('Var'  , 0.0645128   ), Coef('Var'  , 0.0778663   ), Coef('Var'  , 0.0933175   ), Coef('Var'  , 0.109       ), Coef('Var'  , 0.102356    ), Coef('Var'  , 0.0957991   ), Coef('Var'  , 0.0842778   ), ], 
		[Coef('Var'  , 0.0731      ), Coef('Var'  , 0.0664493   ), Coef('Var'  , 0.0581307   ), Coef('Var'  , 0.0823086   ), Coef('Var'  , 0.106542    ), Coef('Var'  , 0.119708    ), Coef('Var'  , 0.134973    ), Coef('Var'  , 0.115798    ), Coef('Var'  , 0.0982836   ), Coef('Var'  , 0.0860429   ), ], 
		[Coef('Var'  , 0.107535    ), Coef('Var'  , 0.12823     ), Coef('Var'  , 0.150465    ), Coef('Var'  , 0.162659    ), Coef('Var'  , 0.177035    ), Coef('Var'  , 0.158501    ), Coef('Var'  , 0.142539    ), Coef('Var'  , 0.12699     ), Coef('Var'  , 0.11346     ), Coef('Var'  , 0.10982     ), ], 
		[Coef('Var'  , 0.14172     ), Coef('Var'  , 0.191568    ), Coef('Var'  , 0.244617    ), Coef('Var'  , 0.243576    ), Coef('Var'  , 0.245878    ), Coef('Var'  , 0.193455    ), Coef('Var'  , 0.143945    ), Coef('Var'  , 0.132241    ), Coef('Var'  , 0.122822    ), Coef('Var'  , 0.131044    ), ], ])
	etat5.initMat[Chem([Sub('2')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0411822   ), Coef('Var'  , 0.0821628   ), Coef('Var'  , 0.118006    ), Coef('Var'  , 0.15427     ), Coef('Var'  , 0.201823    ), Coef('Const', 0.25        ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0225293   ), Coef('Var'  , 0.0442781   ), Coef('Var'  , 0.050112    ), Coef('Var'  , 0.0550431   ), Coef('Var'  , 0.0275827   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0241203   ), Coef('Var'  , 0.047111    ), Coef('Var'  , 0.0511089   ), Coef('Var'  , 0.0531341   ), Coef('Var'  , 0.0269886   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0175107   ), Coef('Var'  , 0.0341899   ), Coef('Var'  , 0.0358465   ), Coef('Var'  , 0.0356223   ), Coef('Var'  , 0.0183358   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0256258   ), Coef('Var'  , 0.0504759   ), Coef('Var'  , 0.0491941   ), Coef('Var'  , 0.0458988   ), Coef('Var'  , 0.0235683   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0302218   ), Coef('Var'  , 0.0601044   ), Coef('Var'  , 0.0550473   ), Coef('Var'  , 0.04871     ), Coef('Var'  , 0.0248255   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.200683    ), Coef('Var'  , 0.151947    ), Coef('Var'  , 0.11464     ), Coef('Var'  , 0.0778663   ), Coef('Var'  , 0.038957    ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.369673    ), Coef('Var'  , 0.240852    ), Coef('Var'  , 0.17258     ), Coef('Var'  , 0.106542    ), Coef('Var'  , 0.0529064   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.213464    ), Coef('Var'  , 0.178044    ), Coef('Var'  , 0.176344    ), Coef('Var'  , 0.177035    ), Coef('Var'  , 0.21288     ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0549893   ), Coef('Var'  , 0.110834    ), Coef('Var'  , 0.177122    ), Coef('Var'  , 0.245878    ), Coef('Var'  , 0.372133    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), ], ])
	etat5.initMat[Chem([Sub('3')])] = FMat([
		[Coef('Const', 0.25        ), Coef('Var'  , 0.199351    ), Coef('Var'  , 0.149888    ), Coef('Var'  , 0.112829    ), Coef('Var'  , 0.0773354   ), Coef('Var'  , 0.0384784   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.5         ), Coef('Var'  , 0.368567    ), Coef('Var'  , 0.239127    ), Coef('Var'  , 0.16983     ), Coef('Var'  , 0.103872    ), Coef('Var'  , 0.0512628   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0.25        ), Coef('Var'  , 0.216249    ), Coef('Var'  , 0.183178    ), Coef('Var'  , 0.182552    ), Coef('Var'  , 0.183328    ), Coef('Var'  , 0.216303    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0514355   ), Coef('Var'  , 0.103866    ), Coef('Var'  , 0.170138    ), Coef('Var'  , 0.239132    ), Coef('Var'  , 0.368702    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0401614   ), Coef('Var'  , 0.080098    ), Coef('Var'  , 0.116608    ), Coef('Var'  , 0.15331     ), Coef('Var'  , 0.201446    ), Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0250124   ), Coef('Var'  , 0.0489091   ), Coef('Var'  , 0.0550772   ), Coef('Var'  , 0.0597505   ), Coef('Var'  , 0.0300648   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0232006   ), Coef('Var'  , 0.045269    ), Coef('Var'  , 0.0495746   ), Coef('Var'  , 0.0518217   ), Coef('Var'  , 0.026374    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0213715   ), Coef('Var'  , 0.0411571   ), Coef('Var'  , 0.0417838   ), Coef('Var'  , 0.0394263   ), Coef('Var'  , 0.0204123   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0256689   ), Coef('Var'  , 0.0506095   ), Coef('Var'  , 0.0489951   ), Coef('Var'  , 0.0454889   ), Coef('Var'  , 0.0233261   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0289826   ), Coef('Var'  , 0.057898    ), Coef('Var'  , 0.0526127   ), Coef('Var'  , 0.0465337   ), Coef('Var'  , 0.0236301   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], ])
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
	etat5.initMat[Chem([Sub('4')])] = FMat([
		[Coef('Var'  , 0.149888    ), Coef('Var'  , 0.161022    ), Coef('Var'  , 0.175099    ), Coef('Var'  , 0.156734    ), Coef('Var'  , 0.141774    ), Coef('Var'  , 0.127219    ), Coef('Var'  , 0.115117    ), Coef('Var'  , 0.111206    ), Coef('Var'  , 0.10886     ), Coef('Var'  , 0.1284      ), ], 
		[Coef('Var'  , 0.239127    ), Coef('Var'  , 0.23745     ), Coef('Var'  , 0.239547    ), Coef('Var'  , 0.184709    ), Coef('Var'  , 0.133435    ), Coef('Var'  , 0.120679    ), Coef('Var'  , 0.111397    ), Coef('Var'  , 0.120438    ), Coef('Var'  , 0.133192    ), Coef('Var'  , 0.184153    ), ], 
		[Coef('Var'  , 0.183178    ), Coef('Var'  , 0.169184    ), Coef('Var'  , 0.156201    ), Coef('Var'  , 0.134758    ), Coef('Var'  , 0.113965    ), Coef('Var'  , 0.1168      ), Coef('Var'  , 0.12048     ), Coef('Var'  , 0.134664    ), Coef('Var'  , 0.150167    ), Coef('Var'  , 0.165936    ), ], 
		[Coef('Var'  , 0.103866    ), Coef('Var'  , 0.0787118   ), Coef('Var'  , 0.054151    ), Coef('Var'  , 0.0614143   ), Coef('Var'  , 0.0675914   ), Coef('Var'  , 0.0811358   ), Coef('Var'  , 0.0943745   ), Coef('Var'  , 0.112523    ), Coef('Var'  , 0.132518    ), Coef('Var'  , 0.116961    ), ], 
		[Coef('Var'  , 0.080098    ), Coef('Var'  , 0.0675289   ), Coef('Var'  , 0.0536556   ), Coef('Var'  , 0.0660619   ), Coef('Var'  , 0.0759512   ), Coef('Var'  , 0.0884447   ), Coef('Var'  , 0.0988952   ), Coef('Var'  , 0.10529     ), Coef('Var'  , 0.111165    ), Coef('Var'  , 0.0957013   ), ], 
		[Coef('Var'  , 0.0489091   ), Coef('Var'  , 0.0489317   ), Coef('Var'  , 0.046228    ), Coef('Var'  , 0.0614698   ), Coef('Var'  , 0.073241    ), Coef('Var'  , 0.0832685   ), Coef('Var'  , 0.0902838   ), Coef('Var'  , 0.0853758   ), Coef('Var'  , 0.078475    ), Coef('Var'  , 0.0646701   ), ], 
		[Coef('Var'  , 0.045269    ), Coef('Var'  , 0.0459206   ), Coef('Var'  , 0.0444288   ), Coef('Var'  , 0.0590018   ), Coef('Var'  , 0.0716869   ), Coef('Var'  , 0.0800112   ), Coef('Var'  , 0.0866936   ), Coef('Var'  , 0.0809027   ), Coef('Var'  , 0.0732395   ), Coef('Var'  , 0.060374    ), ], 
		[Coef('Var'  , 0.0411571   ), Coef('Var'  , 0.0451838   ), Coef('Var'  , 0.0463307   ), Coef('Var'  , 0.0608595   ), Coef('Var'  , 0.0731      ), Coef('Var'  , 0.0773087   ), Coef('Var'  , 0.0796594   ), Coef('Var'  , 0.072385    ), Coef('Var'  , 0.0627648   ), Coef('Var'  , 0.0534949   ), ], 
		[Coef('Var'  , 0.0506095   ), Coef('Var'  , 0.0636536   ), Coef('Var'  , 0.0763125   ), Coef('Var'  , 0.0914357   ), Coef('Var'  , 0.107535    ), Coef('Var'  , 0.101776    ), Coef('Var'  , 0.0963749   ), Coef('Var'  , 0.085486    ), Coef('Var'  , 0.0731813   ), Coef('Var'  , 0.0628298   ), ], 
		[Coef('Var'  , 0.057898    ), Coef('Var'  , 0.0824138   ), Coef('Var'  , 0.108046    ), Coef('Var'  , 0.123556    ), Coef('Var'  , 0.14172     ), Coef('Var'  , 0.123357    ), Coef('Var'  , 0.106724    ), Coef('Var'  , 0.0917296   ), Coef('Var'  , 0.076438    ), Coef('Var'  , 0.0674799   ), ], ])
	etat5.initMat[Chem([Sub('5')])] = FMat([
		[Coef('Var'  , 0.0773354   ), Coef('Var'  , 0.0925277   ), Coef('Var'  , 0.10886     ), Coef('Var'  , 0.104647    ), Coef('Var'  , 0.10081     ), Coef('Var'  , 0.0909867   ), Coef('Var'  , 0.0792758   ), Coef('Var'  , 0.0680741   ), Coef('Var'  , 0.0543545   ), Coef('Var'  , 0.0661632   ), ], 
		[Coef('Var'  , 0.103872    ), Coef('Var'  , 0.116848    ), Coef('Var'  , 0.133192    ), Coef('Var'  , 0.11493     ), Coef('Var'  , 0.0992076   ), Coef('Var'  , 0.0867612   ), Coef('Var'  , 0.0739279   ), Coef('Var'  , 0.0660916   ), Coef('Var'  , 0.0569743   ), Coef('Var'  , 0.079938    ), ], 
		[Coef('Var'  , 0.183328    ), Coef('Var'  , 0.16599     ), Coef('Var'  , 0.150167    ), Coef('Var'  , 0.135494    ), Coef('Var'  , 0.121879    ), Coef('Var'  , 0.118895    ), Coef('Var'  , 0.116204    ), Coef('Var'  , 0.136511    ), Coef('Var'  , 0.157191    ), Coef('Var'  , 0.169726    ), ], 
		[Coef('Var'  , 0.239132    ), Coef('Var'  , 0.184228    ), Coef('Var'  , 0.132518    ), Coef('Var'  , 0.119031    ), Coef('Var'  , 0.108235    ), Coef('Var'  , 0.117371    ), Coef('Var'  , 0.129452    ), Coef('Var'  , 0.181629    ), Coef('Var'  , 0.237419    ), Coef('Var'  , 0.236466    ), ], 
		[Coef('Var'  , 0.15331     ), Coef('Var'  , 0.131986    ), Coef('Var'  , 0.111165    ), Coef('Var'  , 0.111839    ), Coef('Var'  , 0.113283    ), Coef('Var'  , 0.125386    ), Coef('Var'  , 0.13973     ), Coef('Var'  , 0.156581    ), Coef('Var'  , 0.176259    ), Coef('Var'  , 0.163941    ), ], 
		[Coef('Var'  , 0.0597505   ), Coef('Var'  , 0.0697226   ), Coef('Var'  , 0.078475    ), Coef('Var'  , 0.0926473   ), Coef('Var'  , 0.106395    ), Coef('Var'  , 0.122283    ), Coef('Var'  , 0.140329    ), Coef('Var'  , 0.122737    ), Coef('Var'  , 0.108046    ), Coef('Var'  , 0.0835081   ), ], 
		[Coef('Var'  , 0.0518217   ), Coef('Var'  , 0.0635473   ), Coef('Var'  , 0.0732395   ), Coef('Var'  , 0.0861208   ), Coef('Var'  , 0.0974678   ), Coef('Var'  , 0.104343    ), Coef('Var'  , 0.110869    ), Coef('Var'  , 0.0951835   ), Coef('Var'  , 0.0793893   ), Coef('Var'  , 0.0661624   ), ], 
		[Coef('Var'  , 0.0394263   ), Coef('Var'  , 0.0525358   ), Coef('Var'  , 0.0627648   ), Coef('Var'  , 0.0699712   ), Coef('Var'  , 0.0753262   ), Coef('Var'  , 0.0697339   ), Coef('Var'  , 0.063816    ), Coef('Var'  , 0.0519919   ), Coef('Var'  , 0.0396488   ), Coef('Var'  , 0.0405181   ), ], 
		[Coef('Var'  , 0.0454889   ), Coef('Var'  , 0.060487    ), Coef('Var'  , 0.0731813   ), Coef('Var'  , 0.0818844   ), Coef('Var'  , 0.088454    ), Coef('Var'  , 0.082703    ), Coef('Var'  , 0.0747629   ), Coef('Var'  , 0.0617506   ), Coef('Var'  , 0.04634     ), Coef('Var'  , 0.0470973   ), ], 
		[Coef('Var'  , 0.0465337   ), Coef('Var'  , 0.0621274   ), Coef('Var'  , 0.076438    ), Coef('Var'  , 0.0834348   ), Coef('Var'  , 0.0889425   ), Coef('Var'  , 0.0815381   ), Coef('Var'  , 0.0716335   ), Coef('Var'  , 0.0594498   ), Coef('Var'  , 0.0443774   ), Coef('Var'  , 0.0464793   ), ], ])
	etat5.initMat[Chem([Sub('6')])] = FMat([
		[Coef('Var'  , 0.0575053   ), Coef('Var'  , 0.0714043   ), Coef('Var'  , 0.0822067   ), Coef('Var'  , 0.0948465   ), Coef('Var'  , 0.10486     ), Coef('Var'  , 0.110165    ), Coef('Var'  , 0.114664    ), Coef('Var'  , 0.0984919   ), Coef('Var'  , 0.0821628   ), Coef('Var'  , 0.070595    ), ], 
		[Coef('Var'  , 0.0431046   ), Coef('Var'  , 0.0573891   ), Coef('Var'  , 0.0682617   ), Coef('Var'  , 0.0768673   ), Coef('Var'  , 0.0826859   ), Coef('Var'  , 0.0775089   ), Coef('Var'  , 0.0709948   ), Coef('Var'  , 0.0582333   ), Coef('Var'  , 0.0442781   ), Coef('Var'  , 0.0448561   ), ], 
		[Coef('Var'  , 0.0479228   ), Coef('Var'  , 0.0640205   ), Coef('Var'  , 0.07766     ), Coef('Var'  , 0.085812    ), Coef('Var'  , 0.0918856   ), Coef('Var'  , 0.0847692   ), Coef('Var'  , 0.0758606   ), Coef('Var'  , 0.0625244   ), Coef('Var'  , 0.047111    ), Coef('Var'  , 0.048694    ), ], 
		[Coef('Var'  , 0.0365722   ), Coef('Var'  , 0.0490853   ), Coef('Var'  , 0.0614029   ), Coef('Var'  , 0.0663715   ), Coef('Var'  , 0.0711049   ), Coef('Var'  , 0.0641962   ), Coef('Var'  , 0.0560801   ), Coef('Var'  , 0.046013    ), Coef('Var'  , 0.0341899   ), Coef('Var'  , 0.0359185   ), ], 
		[Coef('Var'  , 0.0750564   ), Coef('Var'  , 0.0894876   ), Coef('Var'  , 0.105156    ), Coef('Var'  , 0.0996564   ), Coef('Var'  , 0.0948327   ), Coef('Var'  , 0.0846365   ), Coef('Var'  , 0.073082    ), Coef('Var'  , 0.0627653   ), Coef('Var'  , 0.0504759   ), Coef('Var'  , 0.062954    ), ], 
		[Coef('Var'  , 0.109453    ), Coef('Var'  , 0.12463     ), Coef('Var'  , 0.142069    ), Coef('Var'  , 0.124005    ), Coef('Var'  , 0.107512    ), Coef('Var'  , 0.0934893   ), Coef('Var'  , 0.0788614   ), Coef('Var'  , 0.0700569   ), Coef('Var'  , 0.0601044   ), Coef('Var'  , 0.0845017   ), ], 
		[Coef('Var'  , 0.176896    ), Coef('Var'  , 0.158008    ), Coef('Var'  , 0.141895    ), Coef('Var'  , 0.126697    ), Coef('Var'  , 0.113562    ), Coef('Var'  , 0.110821    ), Coef('Var'  , 0.109       ), Coef('Var'  , 0.130044    ), Coef('Var'  , 0.151947    ), Coef('Var'  , 0.163454    ), ], 
		[Coef('Var'  , 0.237318    ), Coef('Var'  , 0.180852    ), Coef('Var'  , 0.128549    ), Coef('Var'  , 0.116797    ), Coef('Var'  , 0.108856    ), Coef('Var'  , 0.120422    ), Coef('Var'  , 0.134973    ), Coef('Var'  , 0.186475    ), Coef('Var'  , 0.240852    ), Coef('Var'  , 0.237348    ), ], 
		[Coef('Var'  , 0.153971    ), Coef('Var'  , 0.132597    ), Coef('Var'  , 0.111716    ), Coef('Var'  , 0.113098    ), Coef('Var'  , 0.115143    ), Coef('Var'  , 0.127914    ), Coef('Var'  , 0.142539    ), Coef('Var'  , 0.159085    ), Coef('Var'  , 0.178044    ), Coef('Var'  , 0.165257    ), ], 
		[Coef('Var'  , 0.0621999   ), Coef('Var'  , 0.0725258   ), Coef('Var'  , 0.081084    ), Coef('Var'  , 0.0958495   ), Coef('Var'  , 0.109559    ), Coef('Var'  , 0.126078    ), Coef('Var'  , 0.143945    ), Coef('Var'  , 0.126311    ), Coef('Var'  , 0.110834    ), Coef('Var'  , 0.0864214   ), ], ])
	etat5.initMat[Chem([Sub('7')])] = FMat([
		[Coef('Const', 0           ), Coef('Var'  , 0.0276848   ), Coef('Var'  , 0.0543545   ), Coef('Var'  , 0.053702    ), Coef('Var'  , 0.0504454   ), Coef('Var'  , 0.0260172   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0286752   ), Coef('Var'  , 0.0569743   ), Coef('Var'  , 0.052577    ), Coef('Var'  , 0.046624    ), Coef('Var'  , 0.0239018   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.25        ), Coef('Var'  , 0.203424    ), Coef('Var'  , 0.157191    ), Coef('Var'  , 0.119658    ), Coef('Var'  , 0.0823432   ), Coef('Var'  , 0.0412346   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.5         ), Coef('Var'  , 0.367764    ), Coef('Var'  , 0.237419    ), Coef('Var'  , 0.167125    ), Coef('Var'  , 0.10015     ), Coef('Var'  , 0.0493613   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0.25        ), Coef('Var'  , 0.212495    ), Coef('Var'  , 0.176259    ), Coef('Var'  , 0.17427     ), Coef('Var'  , 0.174992    ), Coef('Var'  , 0.211775    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0534433   ), Coef('Var'  , 0.108046    ), Coef('Var'  , 0.174552    ), Coef('Var'  , 0.243965    ), Coef('Var'  , 0.371109    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0397885   ), Coef('Var'  , 0.0793893   ), Coef('Var'  , 0.116118    ), Coef('Var'  , 0.153144    ), Coef('Var'  , 0.201329    ), Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0201058   ), Coef('Var'  , 0.0396488   ), Coef('Var'  , 0.0450529   ), Coef('Var'  , 0.0501241   ), Coef('Var'  , 0.0249471   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0237712   ), Coef('Var'  , 0.04634     ), Coef('Var'  , 0.0505988   ), Coef('Var'  , 0.052716    ), Coef('Var'  , 0.0268276   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0228492   ), Coef('Var'  , 0.0443774   ), Coef('Var'  , 0.0463465   ), Coef('Var'  , 0.0454952   ), Coef('Var'  , 0.0234973   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], ])
	etat5.initMat[Chem([Sub('8')])] = FMat([
		[Coef('Var'  , 0.0519498   ), Coef('Var'  , 0.0562447   ), Coef('Var'  , 0.0575053   ), Coef('Var'  , 0.0294128   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0268319   ), ], 
		[Coef('Var'  , 0.0438149   ), Coef('Var'  , 0.0450722   ), Coef('Var'  , 0.0431046   ), Coef('Var'  , 0.0223267   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0227455   ), ], 
		[Coef('Var'  , 0.0543896   ), Coef('Var'  , 0.0522337   ), Coef('Var'  , 0.0479228   ), Coef('Var'  , 0.0245737   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0276601   ), ], 
		[Coef('Var'  , 0.0485194   ), Coef('Var'  , 0.0424872   ), Coef('Var'  , 0.0365722   ), Coef('Var'  , 0.0184078   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0240794   ), ], 
		[Coef('Var'  , 0.148704    ), Coef('Var'  , 0.111168    ), Coef('Var'  , 0.0750564   ), Coef('Var'  , 0.0373281   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.198839    ), ], 
		[Coef('Var'  , 0.244997    ), Coef('Var'  , 0.176014    ), Coef('Var'  , 0.109453    ), Coef('Var'  , 0.0542799   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.371734    ), ], 
		[Coef('Var'  , 0.177182    ), Coef('Var'  , 0.175695    ), Coef('Var'  , 0.176896    ), Coef('Var'  , 0.212771    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.212924    ), ], 
		[Coef('Var'  , 0.099952    ), Coef('Var'  , 0.166875    ), Coef('Var'  , 0.237318    ), Coef('Var'  , 0.367675    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0491999   ), ], 
		[Coef('Var'  , 0.0800648   ), Coef('Var'  , 0.11692     ), Coef('Var'  , 0.153971    ), Coef('Var'  , 0.201793    ), Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0401276   ), ], 
		[Coef('Var'  , 0.0504266   ), Coef('Var'  , 0.0572908   ), Coef('Var'  , 0.0621999   ), Coef('Var'  , 0.0314321   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0258587   ), ], ])
	etat5.initMat[Chem([Sub('9')])] = FMat([
		[Coef('Var'  , 0.175099    ), Coef('Var'  , 0.211671    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.212354    ), Coef('Var'  , 0.176299    ), Coef('Var'  , 0.174025    ), ], 
		[Coef('Var'  , 0.239547    ), Coef('Var'  , 0.368882    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0514388   ), Coef('Var'  , 0.103996    ), Coef('Var'  , 0.170321    ), ], 
		[Coef('Var'  , 0.156201    ), Coef('Var'  , 0.202935    ), Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.040582    ), Coef('Var'  , 0.0810601   ), Coef('Var'  , 0.118517    ), ], 
		[Coef('Var'  , 0.054151    ), Coef('Var'  , 0.0272763   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.021294    ), Coef('Var'  , 0.0416344   ), Coef('Var'  , 0.0485703   ), ], 
		[Coef('Var'  , 0.0536556   ), Coef('Var'  , 0.0273674   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.024364    ), Coef('Var'  , 0.047376    ), Coef('Var'  , 0.0517314   ), ], 
		[Coef('Var'  , 0.046228    ), Coef('Var'  , 0.0239193   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0237873   ), Coef('Var'  , 0.0460507   ), Coef('Var'  , 0.0477066   ), ], 
		[Coef('Var'  , 0.0444288   ), Coef('Var'  , 0.02272     ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0255558   ), Coef('Var'  , 0.0503708   ), Coef('Var'  , 0.0482758   ), ], 
		[Coef('Var'  , 0.0463307   ), Coef('Var'  , 0.0238124   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0294022   ), Coef('Var'  , 0.0581307   ), Coef('Var'  , 0.0532146   ), ], 
		[Coef('Var'  , 0.0763125   ), Coef('Var'  , 0.0379846   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.199779    ), Coef('Var'  , 0.150465    ), Coef('Var'  , 0.112764    ), ], 
		[Coef('Var'  , 0.108046    ), Coef('Var'  , 0.0534313   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.371443    ), Coef('Var'  , 0.244617    ), Coef('Var'  , 0.174874    ), ], ])
	etat5.initMat[Chem([Sub('10')])] = FMat([
		[Coef('Var'  , 0.0822067   ), Coef('Var'  , 0.0688235   ), Coef('Var'  , 0.0519498   ), Coef('Var'  , 0.0528491   ), Coef('Var'  , 0.0504454   ), Coef('Var'  , 0.0664066   ), Coef('Var'  , 0.0792758   ), Coef('Var'  , 0.0889082   ), Coef('Var'  , 0.0956337   ), Coef('Var'  , 0.0905105   ), ], 
		[Coef('Var'  , 0.0682617   ), Coef('Var'  , 0.0578079   ), Coef('Var'  , 0.0438149   ), Coef('Var'  , 0.0466473   ), Coef('Var'  , 0.046624    ), Coef('Var'  , 0.0613182   ), Coef('Var'  , 0.0739279   ), Coef('Var'  , 0.0799811   ), Coef('Var'  , 0.0839841   ), Coef('Var'  , 0.0776271   ), ], 
		[Coef('Var'  , 0.07766     ), Coef('Var'  , 0.067107    ), Coef('Var'  , 0.0543896   ), Coef('Var'  , 0.0688947   ), Coef('Var'  , 0.0823432   ), Coef('Var'  , 0.0993222   ), Coef('Var'  , 0.116204    ), Coef('Var'  , 0.110108    ), Coef('Var'  , 0.103463    ), Coef('Var'  , 0.0914674   ), ], 
		[Coef('Var'  , 0.0614029   ), Coef('Var'  , 0.0547569   ), Coef('Var'  , 0.0485194   ), Coef('Var'  , 0.0734407   ), Coef('Var'  , 0.10015     ), Coef('Var'  , 0.113227    ), Coef('Var'  , 0.129452    ), Coef('Var'  , 0.108744    ), Coef('Var'  , 0.0904639   ), Coef('Var'  , 0.0755558   ), ], 
		[Coef('Var'  , 0.105156    ), Coef('Var'  , 0.125999    ), Coef('Var'  , 0.148704    ), Coef('Var'  , 0.160614    ), Coef('Var'  , 0.174992    ), Coef('Var'  , 0.155861    ), Coef('Var'  , 0.13973     ), Coef('Var'  , 0.123893    ), Coef('Var'  , 0.110613    ), Coef('Var'  , 0.106966    ), ], 
		[Coef('Var'  , 0.142069    ), Coef('Var'  , 0.192085    ), Coef('Var'  , 0.244997    ), Coef('Var'  , 0.242843    ), Coef('Var'  , 0.243965    ), Coef('Var'  , 0.190402    ), Coef('Var'  , 0.140329    ), Coef('Var'  , 0.128972    ), Coef('Var'  , 0.120662    ), Coef('Var'  , 0.13003     ), ], 
		[Coef('Var'  , 0.141895    ), Coef('Var'  , 0.15816     ), Coef('Var'  , 0.177182    ), Coef('Var'  , 0.164253    ), Coef('Var'  , 0.153144    ), Coef('Var'  , 0.131724    ), Coef('Var'  , 0.110869    ), Coef('Var'  , 0.112397    ), Coef('Var'  , 0.114518    ), Coef('Var'  , 0.127239    ), ], 
		[Coef('Var'  , 0.128549    ), Coef('Var'  , 0.112377    ), Coef('Var'  , 0.099952    ), Coef('Var'  , 0.074147    ), Coef('Var'  , 0.0501241   ), Coef('Var'  , 0.0568332   ), Coef('Var'  , 0.063816    ), Coef('Var'  , 0.0768411   ), Coef('Var'  , 0.0910603   ), Coef('Var'  , 0.108132    ), ], 
		[Coef('Var'  , 0.111716    ), Coef('Var'  , 0.0959322   ), Coef('Var'  , 0.0800648   ), Coef('Var'  , 0.0669552   ), Coef('Var'  , 0.052716    ), Coef('Var'  , 0.064807    ), Coef('Var'  , 0.0747629   ), Coef('Var'  , 0.0876015   ), Coef('Var'  , 0.0987883   ), Coef('Var'  , 0.105427    ), ], 
		[Coef('Var'  , 0.081084    ), Coef('Var'  , 0.0669523   ), Coef('Var'  , 0.0504266   ), Coef('Var'  , 0.049356    ), Coef('Var'  , 0.0454952   ), Coef('Var'  , 0.0600979   ), Coef('Var'  , 0.0716335   ), Coef('Var'  , 0.0825536   ), Coef('Var'  , 0.0908131   ), Coef('Var'  , 0.0870467   ), ], ])
	
	
	
	etat6.bords   = {Bord('0'): etat13, Bord('1'): etat13, Bord('2'): etat13, Bord('3'): etat13, Bord('4'): etat13, }
	etat6.permuts = {}
	etat6.interns = {Intern('_'): etat6, }
	etat6.subs    = {Sub('0'): etat1, Sub('1'): etat2, Sub('2'): etat3, Sub('3'): etat4, Sub('G', True): Etat.etatPoint, Sub('4'): etat5, Sub('5'): etat7, Sub('6'): etat8, Sub('7'): etat9, Sub('8'): etat10, Sub('9'): etat11, Sub('10'): etat12, }
	
	etat6.buildIntern()
	
	
	etat6.eqs = [
		(Chem([Bord('3'), Sub('0'), Permut('0'), ])	,	Chem([Sub('0'), Bord('3'), ])),
		(Chem([Bord('2'), Sub('1'), Permut('0'), ])	,	Chem([Sub('0'), Bord('4'), ])),
		(Chem([Bord('1'), Sub('1'), Permut('0'), ])	,	Chem([Sub('1'), Bord('0'), ])),
		(Chem([Bord('2'), Sub('0'), Permut('0'), ])	,	Chem([Sub('1'), Bord('4'), ])),
		(Chem([Bord('0'), Sub('0'), Permut('0'), ])	,	Chem([Sub('3'), Bord('0'), ])),
		(Chem([Bord('4'), Sub('1'), Permut('0'), ])	,	Chem([Sub('3'), Bord('1'), ])),
		(Chem([Bord('4'), Sub('0'), Permut('0'), ])	,	Chem([Sub('5'), Bord('0'), ])),
		(Chem([Bord('3'), Sub('1'), Permut('0'), ])	,	Chem([Sub('5'), Bord('1'), ])),
		(Chem([Bord('0'), Sub('1'), Permut('0'), ])	,	Chem([Sub('9'), Bord('0'), ])),
		(Chem([Bord('1'), Sub('0'), Permut('0'), ])	,	Chem([Sub('9'), Bord('4'), ])),
		(Chem([Sub('0'), Bord('0'), Bord('1'), ])	,	Chem([Sub('6'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('1'), Bord('1'), ])	,	Chem([Sub('10'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('2'), Bord('1'), ])	,	Chem([Sub('5'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('4'), Bord('1'), ])	,	Chem([Sub('1'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('0'), Bord('1'), ])	,	Chem([Sub('9'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('1'), Bord('1'), ])	,	Chem([Sub('2'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('2'), Bord('1'), ])	,	Chem([Sub('6'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('0'), Bord('1'), ])	,	Chem([Sub('8'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('1'), Bord('1'), ])	,	Chem([Sub('6'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('3'), Bord('1'), ])	,	Chem([Sub('9'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('4'), Bord('1'), ])	,	Chem([Sub('4'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('3'), Bord('1'), Bord('1'), ])	,	Chem([Sub('5'), Bord('4'), Bord('1'), ])),
		(Chem([Sub('3'), Bord('2'), Bord('1'), ])	,	Chem([Sub('7'), Bord('4'), Bord('1'), ])),
		(Chem([Sub('3'), Bord('3'), Bord('1'), ])	,	Chem([Sub('4'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('3'), Bord('4'), Bord('1'), ])	,	Chem([Sub('9'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('4'), Bord('1'), Bord('1'), ])	,	Chem([Sub('7'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('4'), Bord('2'), Bord('1'), ])	,	Chem([Sub('8'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('4'), Bord('4'), Bord('1'), ])	,	Chem([Sub('9'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('5'), Bord('2'), Bord('1'), ])	,	Chem([Sub('10'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('5'), Bord('3'), Bord('1'), ])	,	Chem([Sub('7'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('6'), Bord('0'), Bord('1'), ])	,	Chem([Sub('10'), Bord('4'), Bord('1'), ])),
		(Chem([Sub('6'), Bord('4'), Bord('1'), ])	,	Chem([Sub('8'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('7'), Bord('1'), Bord('1'), ])	,	Chem([Sub('10'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('7'), Bord('2'), Bord('1'), ])	,	Chem([Sub('8'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('8'), Bord('4'), Bord('1'), ])	,	Chem([Sub('10'), Bord('0'), Bord('1'), ])),
		(Chem([Bord('0'), Bord('1'), ])	,	Chem([Bord('1'), Bord('0'), ])),
		(Chem([Bord('1'), Bord('1'), ])	,	Chem([Bord('2'), Bord('0'), ])),
		(Chem([Bord('2'), Bord('1'), ])	,	Chem([Bord('3'), Bord('0'), ])),
		(Chem([Bord('3'), Bord('1'), ])	,	Chem([Bord('4'), Bord('0'), ])),
		(Chem([Bord('4'), Bord('1'), ])	,	Chem([Bord('0'), Bord('0'), ])),
		]
	
	
	etat6.prim.elems = [Figure(2, [Chem([Bord('0'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('0'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('0'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('0'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('1'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('1'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('1'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('1'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('2'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('2'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('2'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('2'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('3'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('3'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('3'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('3'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('4'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('4'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('4'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('4'), Sub('1'), Sub('1'), Bord('0'), ]), ])]
	etat6.grid.elems = [
		Figure(1, [Chem([Bord('1'), Bord('0'), ]), Chem([Bord('1'), Intern(''), ]), Chem([Bord('1'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('4'), Bord('0'), ]), Chem([Bord('4'), Intern(''), ]), Chem([Bord('4'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('2'), Bord('0'), ]), Chem([Bord('2'), Intern(''), ]), Chem([Bord('2'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('0'), Bord('0'), ]), Chem([Bord('0'), Intern(''), ]), Chem([Bord('0'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('3'), Bord('0'), ]), Chem([Bord('3'), Intern(''), ]), Chem([Bord('3'), Bord('1'), ]), ]), ]
	
	
	etat6.space = [Chem([Bord('4'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('2'), Intern('0'), Intern('0'), ]), Chem([Bord('2'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('3'), Intern('0'), Intern('0'), ]), Chem([Bord('4'), Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('4'), Intern('0'), Intern('0'), ]), ]
	
	etat6.initMat[Chem([Sub('0')])] = FMat([
		[Coef('Const', 0           ), Coef('Var'  , 0.0275138   ), Coef('Var'  , 0.0534203   ), Coef('Var'  , 0.0573223   ), Coef('Var'  , 0.0584279   ), Coef('Var'  , 0.0298085   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0219457   ), Coef('Var'  , 0.0422851   ), Coef('Var'  , 0.0440404   ), Coef('Var'  , 0.0425726   ), Coef('Var'  , 0.0220947   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0248032   ), Coef('Var'  , 0.0490911   ), Coef('Var'  , 0.0467618   ), Coef('Var'  , 0.0430754   ), Coef('Var'  , 0.0219585   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.027173    ), Coef('Var'  , 0.0540411   ), Coef('Var'  , 0.0498151   ), Coef('Var'  , 0.0441347   ), Coef('Var'  , 0.0226421   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.25        ), Coef('Var'  , 0.202594    ), Coef('Var'  , 0.155581    ), Coef('Var'  , 0.118862    ), Coef('Var'  , 0.0822794   ), Coef('Var'  , 0.0412674   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.5         ), Coef('Var'  , 0.367967    ), Coef('Var'  , 0.237824    ), Coef('Var'  , 0.168322    ), Coef('Var'  , 0.101956    ), Coef('Var'  , 0.0503548   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0.25        ), Coef('Var'  , 0.214763    ), Coef('Var'  , 0.180594    ), Coef('Var'  , 0.179125    ), Coef('Var'  , 0.179923    ), Coef('Var'  , 0.214362    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0506587   ), Coef('Var'  , 0.102873    ), Coef('Var'  , 0.169269    ), Coef('Var'  , 0.239348    ), Coef('Var'  , 0.36861     ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.039515    ), Coef('Var'  , 0.0790744   ), Coef('Var'  , 0.114829    ), Coef('Var'  , 0.15142     ), Coef('Var'  , 0.200314    ), Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0230656   ), Coef('Var'  , 0.0452157   ), Coef('Var'  , 0.0516542   ), Coef('Var'  , 0.0568632   ), Coef('Var'  , 0.0285886   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], ])
	etat6.initMat[Chem([Sub('1')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0301739   ), Coef('Var'  , 0.0591206   ), Coef('Var'  , 0.0577779   ), Coef('Var'  , 0.0536245   ), Coef('Var'  , 0.027604    ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0268398   ), Coef('Var'  , 0.0535667   ), Coef('Var'  , 0.0491622   ), Coef('Var'  , 0.0436825   ), Coef('Var'  , 0.0223224   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.200892    ), Coef('Var'  , 0.152547    ), Coef('Var'  , 0.114343    ), Coef('Var'  , 0.0771924   ), Coef('Var'  , 0.0384508   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.366009    ), Coef('Var'  , 0.234438    ), Coef('Var'  , 0.165071    ), Coef('Var'  , 0.0997507   ), Coef('Var'  , 0.0490621   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.213362    ), Coef('Var'  , 0.177989    ), Coef('Var'  , 0.177304    ), Coef('Var'  , 0.179029    ), Coef('Var'  , 0.213941    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0506949   ), Coef('Var'  , 0.102487    ), Coef('Var'  , 0.168914    ), Coef('Var'  , 0.23822     ), Coef('Var'  , 0.368219    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0417945   ), Coef('Var'  , 0.083256    ), Coef('Var'  , 0.120131    ), Coef('Var'  , 0.156914    ), Coef('Var'  , 0.203337    ), Coef('Const', 0.25        ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0229284   ), Coef('Var'  , 0.044901    ), Coef('Var'  , 0.0505201   ), Coef('Var'  , 0.0550466   ), Coef('Var'  , 0.0275918   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0258606   ), Coef('Var'  , 0.0500094   ), Coef('Var'  , 0.0540454   ), Coef('Var'  , 0.055144    ), Coef('Var'  , 0.0281848   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0214441   ), Coef('Var'  , 0.041685    ), Coef('Var'  , 0.0427317   ), Coef('Var'  , 0.0413968   ), Coef('Var'  , 0.0212876   ), Coef('Const', 0           ), Coef('Const', 0           ), ], ])
	etat6.initMat[Chem([Sub('2')])] = FMat([
		[Coef('Var'  , 0.118722    ), Coef('Var'  , 0.11442     ), Coef('Var'  , 0.109383    ), Coef('Var'  , 0.0986214   ), Coef('Var'  , 0.0853871   ), Coef('Var'  , 0.0737143   ), Coef('Var'  , 0.0591206   ), Coef('Var'  , 0.0725986   ), Coef('Var'  , 0.0845834   ), Coef('Var'  , 0.101764    ), ], 
		[Coef('Var'  , 0.128769    ), Coef('Var'  , 0.11009     ), Coef('Var'  , 0.0944367   ), Coef('Var'  , 0.0818333   ), Coef('Var'  , 0.0694068   ), Coef('Var'  , 0.0618395   ), Coef('Var'  , 0.0535667   ), Coef('Var'  , 0.0762869   ), Coef('Var'  , 0.10048     ), Coef('Var'  , 0.112703    ), ], 
		[Coef('Var'  , 0.147564    ), Coef('Var'  , 0.132064    ), Coef('Var'  , 0.11758     ), Coef('Var'  , 0.113427    ), Coef('Var'  , 0.109966    ), Coef('Var'  , 0.13066     ), Coef('Var'  , 0.152547    ), Coef('Var'  , 0.165582    ), Coef('Var'  , 0.180378    ), Coef('Var'  , 0.163095    ), ], 
		[Coef('Var'  , 0.128197    ), Coef('Var'  , 0.114981    ), Coef('Var'  , 0.105688    ), Coef('Var'  , 0.114391    ), Coef('Var'  , 0.127284    ), Coef('Var'  , 0.178479    ), Coef('Var'  , 0.234438    ), Coef('Var'  , 0.232423    ), Coef('Var'  , 0.23507     ), Coef('Var'  , 0.179475    ), ], 
		[Coef('Var'  , 0.109334    ), Coef('Var'  , 0.111687    ), Coef('Var'  , 0.115544    ), Coef('Var'  , 0.128766    ), Coef('Var'  , 0.14417     ), Coef('Var'  , 0.159772    ), Coef('Var'  , 0.177989    ), Coef('Var'  , 0.163749    ), Coef('Var'  , 0.151623    ), Coef('Var'  , 0.129718    ), ], 
		[Coef('Var'  , 0.0659673   ), Coef('Var'  , 0.0791283   ), Coef('Var'  , 0.0925593   ), Coef('Var'  , 0.110414    ), Coef('Var'  , 0.130649    ), Coef('Var'  , 0.115173    ), Coef('Var'  , 0.102487    ), Coef('Var'  , 0.0771666   ), Coef('Var'  , 0.0527232   ), Coef('Var'  , 0.0596637   ), ], 
		[Coef('Var'  , 0.0807419   ), Coef('Var'  , 0.0938875   ), Coef('Var'  , 0.105027    ), Coef('Var'  , 0.11101     ), Coef('Var'  , 0.116379    ), Coef('Var'  , 0.0999878   ), Coef('Var'  , 0.083256    ), Coef('Var'  , 0.0705335   ), Coef('Var'  , 0.0564118   ), Coef('Var'  , 0.0698099   ), ], 
		[Coef('Var'  , 0.0696447   ), Coef('Var'  , 0.0781381   ), Coef('Var'  , 0.0841384   ), Coef('Var'  , 0.0785515   ), Coef('Var'  , 0.0717272   ), Coef('Var'  , 0.0590156   ), Coef('Var'  , 0.044901    ), Coef('Var'  , 0.045534    ), Coef('Var'  , 0.0436971   ), Coef('Var'  , 0.0582796   ), ], 
		[Coef('Var'  , 0.0759768   ), Coef('Var'  , 0.0850449   ), Coef('Var'  , 0.0913501   ), Coef('Var'  , 0.08661     ), Coef('Var'  , 0.0787476   ), Coef('Var'  , 0.0661226   ), Coef('Var'  , 0.0500094   ), Coef('Var'  , 0.0509817   ), Coef('Var'  , 0.0486694   ), Coef('Var'  , 0.063818    ), ], 
		[Coef('Var'  , 0.0750844   ), Coef('Var'  , 0.0805587   ), Coef('Var'  , 0.0842925   ), Coef('Var'  , 0.0763761   ), Coef('Var'  , 0.066283    ), Coef('Var'  , 0.0552361   ), Coef('Var'  , 0.041685    ), Coef('Var'  , 0.0451438   ), Coef('Var'  , 0.0463642   ), Coef('Var'  , 0.0616743   ), ], ])
	etat6.initMat[Chem([Sub('3')])] = FMat([
		[Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.214748    ), Coef('Var'  , 0.180759    ), Coef('Var'  , 0.179773    ), Coef('Var'  , 0.181235    ), Coef('Var'  , 0.215026    ), ], 
		[Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0507132   ), Coef('Var'  , 0.102654    ), Coef('Var'  , 0.168341    ), Coef('Var'  , 0.237259    ), Coef('Var'  , 0.367628    ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0401594   ), Coef('Var'  , 0.0802164   ), Coef('Var'  , 0.117685    ), Coef('Var'  , 0.155402    ), Coef('Var'  , 0.202526    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.02198     ), Coef('Var'  , 0.0430693   ), Coef('Var'  , 0.0487721   ), Coef('Var'  , 0.0534076   ), Coef('Var'  , 0.0267921   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0246674   ), Coef('Var'  , 0.0480319   ), Coef('Var'  , 0.0514238   ), Coef('Var'  , 0.0526778   ), Coef('Var'  , 0.0267564   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0191409   ), Coef('Var'  , 0.0371203   ), Coef('Var'  , 0.0382136   ), Coef('Var'  , 0.0370089   ), Coef('Var'  , 0.0190726   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0285357   ), Coef('Var'  , 0.0559459   ), Coef('Var'  , 0.0544911   ), Coef('Var'  , 0.0504658   ), Coef('Var'  , 0.0259554   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0306823   ), Coef('Var'  , 0.0607446   ), Coef('Var'  , 0.0558682   ), Coef('Var'  , 0.0491726   ), Coef('Var'  , 0.0251859   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.19888     ), Coef('Var'  , 0.148769    ), Coef('Var'  , 0.111702    ), Coef('Var'  , 0.075956    ), Coef('Var'  , 0.0378218   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.370494    ), Coef('Var'  , 0.24269     ), Coef('Var'  , 0.17373     ), Coef('Var'  , 0.107414    ), Coef('Var'  , 0.0532365   ), ], ])
	etat6.initMat[Chem([Sub('G')])] = FMat([
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
	etat6.initMat[Chem([Sub('4')])] = FMat([
		[Coef('Var'  , 0.157666    ), Coef('Var'  , 0.168664    ), Coef('Var'  , 0.181235    ), Coef('Var'  , 0.163555    ), Coef('Var'  , 0.148465    ), Coef('Var'  , 0.134959    ), Coef('Var'  , 0.123427    ), Coef('Var'  , 0.120769    ), Coef('Var'  , 0.118722    ), Coef('Var'  , 0.137977    ), ], 
		[Coef('Var'  , 0.23597     ), Coef('Var'  , 0.234496    ), Coef('Var'  , 0.237259    ), Coef('Var'  , 0.182118    ), Coef('Var'  , 0.13089     ), Coef('Var'  , 0.117449    ), Coef('Var'  , 0.107718    ), Coef('Var'  , 0.116215    ), Coef('Var'  , 0.128769    ), Coef('Var'  , 0.180125    ), ], 
		[Coef('Var'  , 0.181196    ), Coef('Var'  , 0.16769     ), Coef('Var'  , 0.155402    ), Coef('Var'  , 0.134293    ), Coef('Var'  , 0.113516    ), Coef('Var'  , 0.116266    ), Coef('Var'  , 0.119094    ), Coef('Var'  , 0.132904    ), Coef('Var'  , 0.147564    ), Coef('Var'  , 0.163569    ), ], 
		[Coef('Var'  , 0.100421    ), Coef('Var'  , 0.0762916   ), Coef('Var'  , 0.0534076   ), Coef('Var'  , 0.0615304   ), Coef('Var'  , 0.0688417   ), Coef('Var'  , 0.0812301   ), Coef('Var'  , 0.0936292   ), Coef('Var'  , 0.109553    ), Coef('Var'  , 0.128197    ), Coef('Var'  , 0.11256     ), ], 
		[Coef('Var'  , 0.0777462   ), Coef('Var'  , 0.0654992   ), Coef('Var'  , 0.0526778   ), Coef('Var'  , 0.0655518   ), Coef('Var'  , 0.0763789   ), Coef('Var'  , 0.0884982   ), Coef('Var'  , 0.0991864   ), Coef('Var'  , 0.104034    ), Coef('Var'  , 0.109334    ), Coef('Var'  , 0.0930736   ), ], 
		[Coef('Var'  , 0.0408369   ), Coef('Var'  , 0.0398893   ), Coef('Var'  , 0.0370089   ), Coef('Var'  , 0.0488468   ), Coef('Var'  , 0.0584593   ), Coef('Var'  , 0.0669737   ), Coef('Var'  , 0.0739612   ), Coef('Var'  , 0.0703916   ), Coef('Var'  , 0.0659673   ), Coef('Var'  , 0.0540088   ), ], 
		[Coef('Var'  , 0.0504501   ), Coef('Var'  , 0.0518541   ), Coef('Var'  , 0.0504658   ), Coef('Var'  , 0.0669828   ), Coef('Var'  , 0.0805344   ), Coef('Var'  , 0.0896768   ), Coef('Var'  , 0.0960106   ), Coef('Var'  , 0.0897204   ), Coef('Var'  , 0.0807419   ), Coef('Var'  , 0.0669697   ), ], 
		[Coef('Var'  , 0.0446147   ), Coef('Var'  , 0.0482484   ), Coef('Var'  , 0.0491726   ), Coef('Var'  , 0.0652388   ), Coef('Var'  , 0.0788891   ), Coef('Var'  , 0.0846827   ), Coef('Var'  , 0.0879467   ), Coef('Var'  , 0.0803037   ), Coef('Var'  , 0.0696447   ), Coef('Var'  , 0.0587365   ), ], 
		[Coef('Var'  , 0.0527224   ), Coef('Var'  , 0.0646885   ), Coef('Var'  , 0.075956    ), Coef('Var'  , 0.0901725   ), Coef('Var'  , 0.105578    ), Coef('Var'  , 0.100572    ), Coef('Var'  , 0.0962875   ), Coef('Var'  , 0.0869185   ), Coef('Var'  , 0.0759768   ), Coef('Var'  , 0.0655636   ), ], 
		[Coef('Var'  , 0.0583764   ), Coef('Var'  , 0.0826791   ), Coef('Var'  , 0.107414    ), Coef('Var'  , 0.121711    ), Coef('Var'  , 0.138447    ), Coef('Var'  , 0.119693    ), Coef('Var'  , 0.10274     ), Coef('Var'  , 0.0891923   ), Coef('Var'  , 0.0750844   ), Coef('Var'  , 0.0674172   ), ], ])
	etat6.initMat[Chem([Sub('5')])] = FMat([
		[Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0414934   ), Coef('Var'  , 0.082958    ), Coef('Var'  , 0.119196    ), Coef('Var'  , 0.156052    ), Coef('Var'  , 0.202703    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0229975   ), Coef('Var'  , 0.0449456   ), Coef('Var'  , 0.0508704   ), Coef('Var'  , 0.0554263   ), Coef('Var'  , 0.027873    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0223499   ), Coef('Var'  , 0.0438206   ), Coef('Var'  , 0.0480942   ), Coef('Var'  , 0.0508238   ), Coef('Var'  , 0.0257442   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0215223   ), Coef('Var'  , 0.0415001   ), Coef('Var'  , 0.0427956   ), Coef('Var'  , 0.0411074   ), Coef('Var'  , 0.0212733   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0285805   ), Coef('Var'  , 0.0559715   ), Coef('Var'  , 0.0541747   ), Coef('Var'  , 0.0497092   ), Coef('Var'  , 0.0255942   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0265141   ), Coef('Var'  , 0.0528017   ), Coef('Var'  , 0.0475301   ), Coef('Var'  , 0.0411615   ), Coef('Var'  , 0.021016    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.202066    ), Coef('Var'  , 0.154746    ), Coef('Var'  , 0.117733    ), Coef('Var'  , 0.081279    ), Coef('Var'  , 0.0406664   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.370584    ), Coef('Var'  , 0.242785    ), Coef('Var'  , 0.174507    ), Coef('Var'  , 0.108654    ), Coef('Var'  , 0.0539228   ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.211493    ), Coef('Var'  , 0.174506    ), Coef('Var'  , 0.172667    ), Coef('Var'  , 0.173892    ), Coef('Var'  , 0.211174    ), ], 
		[Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0523989   ), Coef('Var'  , 0.105965    ), Coef('Var'  , 0.172432    ), Coef('Var'  , 0.241894    ), Coef('Var'  , 0.370033    ), ], ])
	etat6.initMat[Chem([Sub('6')])] = FMat([
		[Coef('Var'  , 0.101269    ), Coef('Var'  , 0.0947517   ), Coef('Var'  , 0.084941    ), Coef('Var'  , 0.070848    ), Coef('Var'  , 0.0534203   ), Coef('Var'  , 0.0551177   ), Coef('Var'  , 0.0536245   ), Coef('Var'  , 0.0711444   ), Coef('Var'  , 0.0853871   ), Coef('Var'  , 0.0949579   ), ], 
		[Coef('Var'  , 0.0803251   ), Coef('Var'  , 0.0747208   ), Coef('Var'  , 0.0663459   ), Coef('Var'  , 0.0560253   ), Coef('Var'  , 0.0422851   ), Coef('Var'  , 0.0442681   ), Coef('Var'  , 0.0436825   ), Coef('Var'  , 0.057322    ), Coef('Var'  , 0.0694068   ), Coef('Var'  , 0.0756409   ), ], 
		[Coef('Var'  , 0.0968776   ), Coef('Var'  , 0.0843891   ), Coef('Var'  , 0.0709299   ), Coef('Var'  , 0.0606476   ), Coef('Var'  , 0.0490911   ), Coef('Var'  , 0.063254    ), Coef('Var'  , 0.0771924   ), Coef('Var'  , 0.0932186   ), Coef('Var'  , 0.109966    ), Coef('Var'  , 0.103312    ), ], 
		[Coef('Var'  , 0.0936252   ), Coef('Var'  , 0.08178     ), Coef('Var'  , 0.0697926   ), Coef('Var'  , 0.0624861   ), Coef('Var'  , 0.0540411   ), Coef('Var'  , 0.0762351   ), Coef('Var'  , 0.0997507   ), Coef('Var'  , 0.111532    ), Coef('Var'  , 0.127284    ), Coef('Var'  , 0.108937    ), ], 
		[Coef('Var'  , 0.118111    ), Coef('Var'  , 0.116203    ), Coef('Var'  , 0.114818    ), Coef('Var'  , 0.134997    ), Coef('Var'  , 0.155581    ), Coef('Var'  , 0.166536    ), Coef('Var'  , 0.179029    ), Coef('Var'  , 0.160351    ), Coef('Var'  , 0.14417     ), Coef('Var'  , 0.13021     ), ], 
		[Coef('Var'  , 0.107368    ), Coef('Var'  , 0.117087    ), Coef('Var'  , 0.130143    ), Coef('Var'  , 0.182124    ), Coef('Var'  , 0.237824    ), Coef('Var'  , 0.236186    ), Coef('Var'  , 0.23822     ), Coef('Var'  , 0.182696    ), Coef('Var'  , 0.130649    ), Coef('Var'  , 0.117407    ), ], 
		[Coef('Var'  , 0.120188    ), Coef('Var'  , 0.132293    ), Coef('Var'  , 0.146427    ), Coef('Var'  , 0.162278    ), Coef('Var'  , 0.180594    ), Coef('Var'  , 0.1681      ), Coef('Var'  , 0.156914    ), Coef('Var'  , 0.13653     ), Coef('Var'  , 0.116379    ), Coef('Var'  , 0.117971    ), ], 
		[Coef('Var'  , 0.098611    ), Coef('Var'  , 0.114262    ), Coef('Var'  , 0.133148    ), Coef('Var'  , 0.11609     ), Coef('Var'  , 0.102873    ), Coef('Var'  , 0.0782505   ), Coef('Var'  , 0.0550466   ), Coef('Var'  , 0.063679    ), Coef('Var'  , 0.0717272   ), Coef('Var'  , 0.0849186   ), ], 
		[Coef('Var'  , 0.0999885   ), Coef('Var'  , 0.105134    ), Coef('Var'  , 0.109886    ), Coef('Var'  , 0.0942916   ), Coef('Var'  , 0.0790744   ), Coef('Var'  , 0.0676998   ), Coef('Var'  , 0.055144    ), Coef('Var'  , 0.0684468   ), Coef('Var'  , 0.0787476   ), Coef('Var'  , 0.0906196   ), ], 
		[Coef('Var'  , 0.0836365   ), Coef('Var'  , 0.0793791   ), Coef('Var'  , 0.0735689   ), Coef('Var'  , 0.0602121   ), Coef('Var'  , 0.0452157   ), Coef('Var'  , 0.0443532   ), Coef('Var'  , 0.0413968   ), Coef('Var'  , 0.0550796   ), Coef('Var'  , 0.066283    ), Coef('Var'  , 0.0760246   ), ], ])
	etat6.initMat[Chem([Sub('7')])] = FMat([
		[Coef('Var'  , 0.180759    ), Coef('Var'  , 0.16745     ), Coef('Var'  , 0.156052    ), Coef('Var'  , 0.13597     ), Coef('Var'  , 0.116835    ), Coef('Var'  , 0.119282    ), Coef('Var'  , 0.122678    ), Coef('Var'  , 0.134544    ), Coef('Var'  , 0.148465    ), Coef('Var'  , 0.163276    ), ], 
		[Coef('Var'  , 0.102654    ), Coef('Var'  , 0.0785861   ), Coef('Var'  , 0.0554263   ), Coef('Var'  , 0.0638647   ), Coef('Var'  , 0.0712482   ), Coef('Var'  , 0.0837662   ), Coef('Var'  , 0.0961348   ), Coef('Var'  , 0.112265    ), Coef('Var'  , 0.13089     ), Coef('Var'  , 0.115204    ), ], 
		[Coef('Var'  , 0.0802164   ), Coef('Var'  , 0.0659037   ), Coef('Var'  , 0.0508238   ), Coef('Var'  , 0.0623686   ), Coef('Var'  , 0.0723981   ), Coef('Var'  , 0.0863979   ), Coef('Var'  , 0.0991144   ), Coef('Var'  , 0.106541    ), Coef('Var'  , 0.113516    ), Coef('Var'  , 0.0969264   ), ], 
		[Coef('Var'  , 0.0430693   ), Coef('Var'  , 0.0432533   ), Coef('Var'  , 0.0411074   ), Coef('Var'  , 0.0545085   ), Coef('Var'  , 0.0647827   ), Coef('Var'  , 0.0733151   ), Coef('Var'  , 0.0791909   ), Coef('Var'  , 0.0748182   ), Coef('Var'  , 0.0688417   ), Coef('Var'  , 0.0567183   ), ], 
		[Coef('Var'  , 0.0480319   ), Coef('Var'  , 0.0502616   ), Coef('Var'  , 0.0497092   ), Coef('Var'  , 0.0661703   ), Coef('Var'  , 0.0795834   ), Coef('Var'  , 0.0875837   ), Coef('Var'  , 0.0928271   ), Coef('Var'  , 0.085803    ), Coef('Var'  , 0.0763789   ), Coef('Var'  , 0.0634628   ), ], 
		[Coef('Var'  , 0.0371203   ), Coef('Var'  , 0.0401569   ), Coef('Var'  , 0.0411615   ), Coef('Var'  , 0.0544771   ), Coef('Var'  , 0.0663924   ), Coef('Var'  , 0.0707981   ), Coef('Var'  , 0.0741727   ), Coef('Var'  , 0.0671112   ), Coef('Var'  , 0.0584593   ), Coef('Var'  , 0.0489151   ), ], 
		[Coef('Var'  , 0.0559459   ), Coef('Var'  , 0.0692021   ), Coef('Var'  , 0.081279    ), Coef('Var'  , 0.0974201   ), Coef('Var'  , 0.113871    ), Coef('Var'  , 0.108899    ), Coef('Var'  , 0.103791    ), Coef('Var'  , 0.0931726   ), Coef('Var'  , 0.0805344   ), Coef('Var'  , 0.0695631   ), ], 
		[Coef('Var'  , 0.0607446   ), Coef('Var'  , 0.0846051   ), Coef('Var'  , 0.108654    ), Coef('Var'  , 0.123037    ), Coef('Var'  , 0.139528    ), Coef('Var'  , 0.121821    ), Coef('Var'  , 0.105363    ), Coef('Var'  , 0.0927595   ), Coef('Var'  , 0.0788891   ), Coef('Var'  , 0.0707352   ), ], 
		[Coef('Var'  , 0.148769    ), Coef('Var'  , 0.160054    ), Coef('Var'  , 0.173892    ), Coef('Var'  , 0.154428    ), Coef('Var'  , 0.138233    ), Coef('Var'  , 0.122782    ), Coef('Var'  , 0.110186    ), Coef('Var'  , 0.10688     ), Coef('Var'  , 0.105578    ), Coef('Var'  , 0.126231    ), ], 
		[Coef('Var'  , 0.24269     ), Coef('Var'  , 0.240527    ), Coef('Var'  , 0.241894    ), Coef('Var'  , 0.187755    ), Coef('Var'  , 0.137128    ), Coef('Var'  , 0.125354    ), Coef('Var'  , 0.116542    ), Coef('Var'  , 0.126107    ), Coef('Var'  , 0.138447    ), Coef('Var'  , 0.188968    ), ], ])
	etat6.initMat[Chem([Sub('8')])] = FMat([
		[Coef('Var'  , 0.108391    ), Coef('Var'  , 0.105967    ), Coef('Var'  , 0.101269    ), Coef('Var'  , 0.106498    ), Coef('Var'  , 0.109383    ), Coef('Var'  , 0.116511    ), Coef('Var'  , 0.123427    ), Coef('Var'  , 0.122444    ), Coef('Var'  , 0.122678    ), Coef('Var'  , 0.115564    ), ], 
		[Coef('Var'  , 0.0811906   ), Coef('Var'  , 0.0817481   ), Coef('Var'  , 0.0803251   ), Coef('Var'  , 0.0874748   ), Coef('Var'  , 0.0944367   ), Coef('Var'  , 0.0997919   ), Coef('Var'  , 0.107718    ), Coef('Var'  , 0.100733    ), Coef('Var'  , 0.0961348   ), Coef('Var'  , 0.0888813   ), ], 
		[Coef('Var'  , 0.0866659   ), Coef('Var'  , 0.0922024   ), Coef('Var'  , 0.0968776   ), Coef('Var'  , 0.107204    ), Coef('Var'  , 0.11758     ), Coef('Var'  , 0.118159    ), Coef('Var'  , 0.119094    ), Coef('Var'  , 0.109273    ), Coef('Var'  , 0.0991144   ), Coef('Var'  , 0.0934312   ), ], 
		[Coef('Var'  , 0.0794692   ), Coef('Var'  , 0.0867086   ), Coef('Var'  , 0.0936252   ), Coef('Var'  , 0.0983875   ), Coef('Var'  , 0.105688    ), Coef('Var'  , 0.0984123   ), Coef('Var'  , 0.0936292   ), Coef('Var'  , 0.0865716   ), Coef('Var'  , 0.0791909   ), Coef('Var'  , 0.0803216   ), ], 
		[Coef('Var'  , 0.10328     ), Coef('Var'  , 0.110801    ), Coef('Var'  , 0.118111    ), Coef('Var'  , 0.116157    ), Coef('Var'  , 0.115544    ), Coef('Var'  , 0.107059    ), Coef('Var'  , 0.0991864   ), Coef('Var'  , 0.0967104   ), Coef('Var'  , 0.0928271   ), Coef('Var'  , 0.0990084   ), ], 
		[Coef('Var'  , 0.0926617   ), Coef('Var'  , 0.0989343   ), Coef('Var'  , 0.107368    ), Coef('Var'  , 0.098866    ), Coef('Var'  , 0.0925593   ), Coef('Var'  , 0.0831357   ), Coef('Var'  , 0.0739612   ), Coef('Var'  , 0.0745365   ), Coef('Var'  , 0.0741727   ), Coef('Var'  , 0.0833416   ), ], 
		[Coef('Var'  , 0.119174    ), Coef('Var'  , 0.118985    ), Coef('Var'  , 0.120188    ), Coef('Var'  , 0.112595    ), Coef('Var'  , 0.105027    ), Coef('Var'  , 0.101466    ), Coef('Var'  , 0.0960106   ), Coef('Var'  , 0.100795    ), Coef('Var'  , 0.103791    ), Coef('Var'  , 0.111352    ), ], 
		[Coef('Var'  , 0.115149    ), Coef('Var'  , 0.105649    ), Coef('Var'  , 0.098611    ), Coef('Var'  , 0.0912956   ), Coef('Var'  , 0.0841384   ), Coef('Var'  , 0.087094    ), Coef('Var'  , 0.0879467   ), Coef('Var'  , 0.0973363   ), Coef('Var'  , 0.105363    ), Coef('Var'  , 0.109524    ), ], 
		[Coef('Var'  , 0.112457    ), Coef('Var'  , 0.106197    ), Coef('Var'  , 0.0999885   ), Coef('Var'  , 0.0967055   ), Coef('Var'  , 0.0913501   ), Coef('Var'  , 0.0945696   ), Coef('Var'  , 0.0962875   ), Coef('Var'  , 0.10275     ), Coef('Var'  , 0.110186    ), Coef('Var'  , 0.110369    ), ], 
		[Coef('Var'  , 0.101561    ), Coef('Var'  , 0.0928069   ), Coef('Var'  , 0.0836365   ), Coef('Var'  , 0.0848168   ), Coef('Var'  , 0.0842925   ), Coef('Var'  , 0.0938019   ), Coef('Var'  , 0.10274     ), Coef('Var'  , 0.10885     ), Coef('Var'  , 0.116542    ), Coef('Var'  , 0.108206    ), ], ])
	etat6.initMat[Chem([Sub('9')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.203638    ), Coef('Var'  , 0.157666    ), Coef('Var'  , 0.121063    ), Coef('Var'  , 0.0845834   ), Coef('Var'  , 0.0424247   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.366868    ), Coef('Var'  , 0.23597     ), Coef('Var'  , 0.166315    ), Coef('Var'  , 0.10048     ), Coef('Var'  , 0.0494471   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.215164    ), Coef('Var'  , 0.181196    ), Coef('Var'  , 0.179855    ), Coef('Var'  , 0.180378    ), Coef('Var'  , 0.21469     ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0494995   ), Coef('Var'  , 0.100421    ), Coef('Var'  , 0.165914    ), Coef('Var'  , 0.23507     ), Coef('Var'  , 0.366414    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0387428   ), Coef('Var'  , 0.0777462   ), Coef('Var'  , 0.11413     ), Coef('Var'  , 0.151623    ), Coef('Var'  , 0.200387    ), Coef('Const', 0.25        ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0208167   ), Coef('Var'  , 0.0408369   ), Coef('Var'  , 0.0472883   ), Coef('Var'  , 0.0527232   ), Coef('Var'  , 0.0264717   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0258987   ), Coef('Var'  , 0.0504501   ), Coef('Var'  , 0.0546376   ), Coef('Var'  , 0.0564118   ), Coef('Var'  , 0.0287389   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0230626   ), Coef('Var'  , 0.0446147   ), Coef('Var'  , 0.0456682   ), Coef('Var'  , 0.0436971   ), Coef('Var'  , 0.0226056   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0268667   ), Coef('Var'  , 0.0527224   ), Coef('Var'  , 0.0519877   ), Coef('Var'  , 0.0486694   ), Coef('Var'  , 0.0251211   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0294426   ), Coef('Var'  , 0.0583764   ), Coef('Var'  , 0.0531423   ), Coef('Var'  , 0.0463642   ), Coef('Var'  , 0.0236997   ), Coef('Const', 0           ), Coef('Const', 0           ), ], ])
	etat6.initMat[Chem([Sub('10')])] = FMat([
		[Coef('Var'  , 0.084941    ), Coef('Var'  , 0.0978839   ), Coef('Var'  , 0.108391    ), Coef('Var'  , 0.112817    ), Coef('Var'  , 0.116835    ), Coef('Var'  , 0.0997609   ), Coef('Var'  , 0.082958    ), Coef('Var'  , 0.0713019   ), Coef('Var'  , 0.0584279   ), Coef('Var'  , 0.0731428   ), ], 
		[Coef('Var'  , 0.0663459   ), Coef('Var'  , 0.0751865   ), Coef('Var'  , 0.0811906   ), Coef('Var'  , 0.0770986   ), Coef('Var'  , 0.0712482   ), Coef('Var'  , 0.0589892   ), Coef('Var'  , 0.0449456   ), Coef('Var'  , 0.0450922   ), Coef('Var'  , 0.0425726   ), Coef('Var'  , 0.0561743   ), ], 
		[Coef('Var'  , 0.0709299   ), Coef('Var'  , 0.0795021   ), Coef('Var'  , 0.0866659   ), Coef('Var'  , 0.080282    ), Coef('Var'  , 0.0723981   ), Coef('Var'  , 0.0589742   ), Coef('Var'  , 0.0438206   ), Coef('Var'  , 0.0443084   ), Coef('Var'  , 0.0430754   ), Coef('Var'  , 0.0578029   ), ], 
		[Coef('Var'  , 0.0697926   ), Coef('Var'  , 0.0755548   ), Coef('Var'  , 0.0794692   ), Coef('Var'  , 0.0734769   ), Coef('Var'  , 0.0647827   ), Coef('Var'  , 0.0547575   ), Coef('Var'  , 0.0415001   ), Coef('Var'  , 0.0441643   ), Coef('Var'  , 0.0441347   ), Coef('Var'  , 0.0579552   ), ], 
		[Coef('Var'  , 0.114818    ), Coef('Var'  , 0.109404    ), Coef('Var'  , 0.10328     ), Coef('Var'  , 0.0925768   ), Coef('Var'  , 0.0795834   ), Coef('Var'  , 0.0691566   ), Coef('Var'  , 0.0559715   ), Coef('Var'  , 0.0698479   ), Coef('Var'  , 0.0822794   ), Coef('Var'  , 0.0986703   ), ], 
		[Coef('Var'  , 0.130143    ), Coef('Var'  , 0.110161    ), Coef('Var'  , 0.0926617   ), Coef('Var'  , 0.0794656   ), Coef('Var'  , 0.0663924   ), Coef('Var'  , 0.0599752   ), Coef('Var'  , 0.0528017   ), Coef('Var'  , 0.0768689   ), Coef('Var'  , 0.101956    ), Coef('Var'  , 0.114512    ), ], 
		[Coef('Var'  , 0.146427    ), Coef('Var'  , 0.131722    ), Coef('Var'  , 0.119174    ), Coef('Var'  , 0.115961    ), Coef('Var'  , 0.113871    ), Coef('Var'  , 0.13382     ), Coef('Var'  , 0.154746    ), Coef('Var'  , 0.166428    ), Coef('Var'  , 0.179923    ), Coef('Var'  , 0.161877    ), ], 
		[Coef('Var'  , 0.133148    ), Coef('Var'  , 0.122249    ), Coef('Var'  , 0.115149    ), Coef('Var'  , 0.125932    ), Coef('Var'  , 0.139528    ), Coef('Var'  , 0.189698    ), Coef('Var'  , 0.242785    ), Coef('Var'  , 0.239194    ), Coef('Var'  , 0.239348    ), Coef('Var'  , 0.184041    ), ], 
		[Coef('Var'  , 0.109886    ), Coef('Var'  , 0.110616    ), Coef('Var'  , 0.112457    ), Coef('Var'  , 0.124093    ), Coef('Var'  , 0.138233    ), Coef('Var'  , 0.154747    ), Coef('Var'  , 0.174506    ), Coef('Var'  , 0.161807    ), Coef('Var'  , 0.15142     ), Coef('Var'  , 0.13009     ), ], 
		[Coef('Var'  , 0.0735689   ), Coef('Var'  , 0.0877207   ), Coef('Var'  , 0.101561    ), Coef('Var'  , 0.118297    ), Coef('Var'  , 0.137128    ), Coef('Var'  , 0.120121    ), Coef('Var'  , 0.105965    ), Coef('Var'  , 0.0809875   ), Coef('Var'  , 0.0568632   ), Coef('Var'  , 0.0657351   ), ], ])
	
	
	
	etat7.bords   = {Bord('0'): etat13, Bord('1'): etat13, Bord('2'): etat13, Bord('3'): etat13, Bord('4'): etat13, }
	etat7.permuts = {}
	etat7.interns = {Intern('_'): etat7, }
	etat7.subs    = {Sub('0'): etat1, Sub('1'): etat2, Sub('2'): etat3, Sub('3'): etat4, Sub('G', True): Etat.etatPoint, Sub('4'): etat5, Sub('5'): etat6, Sub('6'): etat8, Sub('7'): etat9, Sub('8'): etat10, Sub('9'): etat11, Sub('10'): etat12, }
	
	etat7.buildIntern()
	
	
	etat7.eqs = [
		(Chem([Bord('2'), Sub('0'), Permut('0'), ])	,	Chem([Sub('0'), Bord('2'), ])),
		(Chem([Bord('1'), Sub('1'), Permut('0'), ])	,	Chem([Sub('0'), Bord('3'), ])),
		(Chem([Bord('0'), Sub('0'), Permut('0'), ])	,	Chem([Sub('3'), Bord('1'), ])),
		(Chem([Bord('4'), Sub('1'), Permut('0'), ])	,	Chem([Sub('3'), Bord('2'), ])),
		(Chem([Bord('1'), Sub('0'), Permut('0'), ])	,	Chem([Sub('5'), Bord('3'), ])),
		(Chem([Bord('0'), Sub('1'), Permut('0'), ])	,	Chem([Sub('5'), Bord('4'), ])),
		(Chem([Bord('4'), Sub('0'), Permut('0'), ])	,	Chem([Sub('7'), Bord('0'), ])),
		(Chem([Bord('3'), Sub('1'), Permut('0'), ])	,	Chem([Sub('7'), Bord('1'), ])),
		(Chem([Bord('3'), Sub('0'), Permut('0'), ])	,	Chem([Sub('10'), Bord('2'), ])),
		(Chem([Bord('2'), Sub('1'), Permut('0'), ])	,	Chem([Sub('10'), Bord('3'), ])),
		(Chem([Sub('0'), Bord('0'), Bord('1'), ])	,	Chem([Sub('6'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('1'), Bord('1'), ])	,	Chem([Sub('10'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('3'), Bord('1'), ])	,	Chem([Sub('5'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('4'), Bord('1'), ])	,	Chem([Sub('1'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('0'), Bord('1'), ])	,	Chem([Sub('9'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('1'), Bord('1'), ])	,	Chem([Sub('2'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('2'), Bord('1'), ])	,	Chem([Sub('6'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('4'), Bord('1'), ])	,	Chem([Sub('5'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('0'), Bord('1'), ])	,	Chem([Sub('8'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('1'), Bord('1'), ])	,	Chem([Sub('6'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('3'), Bord('1'), ])	,	Chem([Sub('9'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('4'), Bord('1'), ])	,	Chem([Sub('4'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('3'), Bord('0'), Bord('1'), ])	,	Chem([Sub('5'), Bord('4'), Bord('1'), ])),
		(Chem([Sub('3'), Bord('2'), Bord('1'), ])	,	Chem([Sub('7'), Bord('4'), Bord('1'), ])),
		(Chem([Sub('3'), Bord('3'), Bord('1'), ])	,	Chem([Sub('4'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('3'), Bord('4'), Bord('1'), ])	,	Chem([Sub('9'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('4'), Bord('1'), Bord('1'), ])	,	Chem([Sub('7'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('4'), Bord('2'), Bord('1'), ])	,	Chem([Sub('8'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('4'), Bord('4'), Bord('1'), ])	,	Chem([Sub('9'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('5'), Bord('0'), Bord('1'), ])	,	Chem([Sub('9'), Bord('4'), Bord('1'), ])),
		(Chem([Sub('6'), Bord('0'), Bord('1'), ])	,	Chem([Sub('10'), Bord('4'), Bord('1'), ])),
		(Chem([Sub('6'), Bord('4'), Bord('1'), ])	,	Chem([Sub('8'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('7'), Bord('1'), Bord('1'), ])	,	Chem([Sub('10'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('7'), Bord('2'), Bord('1'), ])	,	Chem([Sub('8'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('8'), Bord('4'), Bord('1'), ])	,	Chem([Sub('10'), Bord('0'), Bord('1'), ])),
		(Chem([Bord('0'), Bord('1'), ])	,	Chem([Bord('1'), Bord('0'), ])),
		(Chem([Bord('1'), Bord('1'), ])	,	Chem([Bord('2'), Bord('0'), ])),
		(Chem([Bord('2'), Bord('1'), ])	,	Chem([Bord('3'), Bord('0'), ])),
		(Chem([Bord('3'), Bord('1'), ])	,	Chem([Bord('4'), Bord('0'), ])),
		(Chem([Bord('4'), Bord('1'), ])	,	Chem([Bord('0'), Bord('0'), ])),
		]
	
	
	etat7.prim.elems = [Figure(2, [Chem([Bord('0'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('0'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('0'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('0'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('1'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('1'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('1'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('1'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('2'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('2'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('2'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('2'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('3'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('3'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('3'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('3'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('4'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('4'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('4'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('4'), Sub('1'), Sub('1'), Bord('0'), ]), ])]
	etat7.grid.elems = [
		Figure(1, [Chem([Bord('1'), Bord('0'), ]), Chem([Bord('1'), Intern(''), ]), Chem([Bord('1'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('4'), Bord('0'), ]), Chem([Bord('4'), Intern(''), ]), Chem([Bord('4'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('2'), Bord('0'), ]), Chem([Bord('2'), Intern(''), ]), Chem([Bord('2'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('0'), Bord('0'), ]), Chem([Bord('0'), Intern(''), ]), Chem([Bord('0'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('3'), Bord('0'), ]), Chem([Bord('3'), Intern(''), ]), Chem([Bord('3'), Bord('1'), ]), ]), ]
	
	
	etat7.space = [Chem([Bord('4'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('2'), Intern('0'), Intern('0'), ]), Chem([Bord('2'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('3'), Intern('0'), Intern('0'), ]), Chem([Bord('4'), Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('4'), Intern('0'), Intern('0'), ]), ]
	
	etat7.initMat[Chem([Sub('0')])] = FMat([
		[Coef('Var'  , 0.049709    ), Coef('Var'  , 0.0482598   ), Coef('Var'  , 0.0450785   ), Coef('Var'  , 0.0230899   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0251699   ), ], 
		[Coef('Var'  , 0.0601097   ), Coef('Var'  , 0.0548842   ), Coef('Var'  , 0.0478888   ), Coef('Var'  , 0.0245359   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0303483   ), ], 
		[Coef('Var'  , 0.147462    ), Coef('Var'  , 0.110059    ), Coef('Var'  , 0.0739349   ), Coef('Var'  , 0.0368096   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.198249    ), ], 
		[Coef('Var'  , 0.241898    ), Coef('Var'  , 0.173665    ), Coef('Var'  , 0.107986    ), Coef('Var'  , 0.0535671   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.370098    ), ], 
		[Coef('Var'  , 0.175986    ), Coef('Var'  , 0.174719    ), Coef('Var'  , 0.176168    ), Coef('Var'  , 0.212399    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.212319    ), ], 
		[Coef('Var'  , 0.1081      ), Coef('Var'  , 0.174314    ), Coef('Var'  , 0.243395    ), Coef('Var'  , 0.370828    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0534862   ), ], 
		[Coef('Var'  , 0.080938    ), Coef('Var'  , 0.117155    ), Coef('Var'  , 0.153407    ), Coef('Var'  , 0.201501    ), Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0406537   ), ], 
		[Coef('Var'  , 0.0479312   ), Coef('Var'  , 0.0538011   ), Coef('Var'  , 0.0578643   ), Coef('Var'  , 0.0291667   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0246344   ), ], 
		[Coef('Var'  , 0.0398885   ), Coef('Var'  , 0.0429476   ), Coef('Var'  , 0.0449197   ), Coef('Var'  , 0.0226194   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0203282   ), ], 
		[Coef('Var'  , 0.047977    ), Coef('Var'  , 0.0501958   ), Coef('Var'  , 0.0493577   ), Coef('Var'  , 0.0254829   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0247129   ), ], ])
	etat7.initMat[Chem([Sub('1')])] = FMat([
		[Coef('Var'  , 0.0751071   ), Coef('Var'  , 0.0899642   ), Coef('Var'  , 0.106238    ), Coef('Var'  , 0.100424    ), Coef('Var'  , 0.0954741   ), Coef('Var'  , 0.0844312   ), Coef('Var'  , 0.0723584   ), Coef('Var'  , 0.0618458   ), Coef('Var'  , 0.049709    ), Coef('Var'  , 0.0624652   ), ], 
		[Coef('Var'  , 0.109504    ), Coef('Var'  , 0.124351    ), Coef('Var'  , 0.141301    ), Coef('Var'  , 0.122652    ), Coef('Var'  , 0.105391    ), Coef('Var'  , 0.0918082   ), Coef('Var'  , 0.0773196   ), Coef('Var'  , 0.0695146   ), Coef('Var'  , 0.0601097   ), Coef('Var'  , 0.0846897   ), ], 
		[Coef('Var'  , 0.173301    ), Coef('Var'  , 0.15328     ), Coef('Var'  , 0.136204    ), Coef('Var'  , 0.119993    ), Coef('Var'  , 0.106389    ), Coef('Var'  , 0.103453    ), Coef('Var'  , 0.102413    ), Coef('Var'  , 0.124035    ), Coef('Var'  , 0.147462    ), Coef('Var'  , 0.159204    ), ], 
		[Coef('Var'  , 0.23939     ), Coef('Var'  , 0.18407     ), Coef('Var'  , 0.132992    ), Coef('Var'  , 0.121303    ), Coef('Var'  , 0.113598    ), Coef('Var'  , 0.123873    ), Coef('Var'  , 0.137551    ), Coef('Var'  , 0.188056    ), Coef('Var'  , 0.241898    ), Coef('Var'  , 0.238779    ), ], 
		[Coef('Var'  , 0.150086    ), Coef('Var'  , 0.127853    ), Coef('Var'  , 0.106983    ), Coef('Var'  , 0.109243    ), Coef('Var'  , 0.112552    ), Coef('Var'  , 0.126014    ), Coef('Var'  , 0.141246    ), Coef('Var'  , 0.157325    ), Coef('Var'  , 0.175986    ), Coef('Var'  , 0.161937    ), ], 
		[Coef('Var'  , 0.0605091   ), Coef('Var'  , 0.0708698   ), Coef('Var'  , 0.0796181   ), Coef('Var'  , 0.093617    ), Coef('Var'  , 0.106647    ), Coef('Var'  , 0.122355    ), Coef('Var'  , 0.139901    ), Coef('Var'  , 0.122599    ), Coef('Var'  , 0.1081      ), Coef('Var'  , 0.0839809   ), ], 
		[Coef('Var'  , 0.0551461   ), Coef('Var'  , 0.0676589   ), Coef('Var'  , 0.0773959   ), Coef('Var'  , 0.089485    ), Coef('Var'  , 0.0994804   ), Coef('Var'  , 0.105833    ), Coef('Var'  , 0.111603    ), Coef('Var'  , 0.0964536   ), Coef('Var'  , 0.080938    ), Coef('Var'  , 0.0688607   ), ], 
		[Coef('Var'  , 0.0450026   ), Coef('Var'  , 0.0591884   ), Coef('Var'  , 0.069415    ), Coef('Var'  , 0.0790396   ), Coef('Var'  , 0.0852219   ), Coef('Var'  , 0.0815336   ), Coef('Var'  , 0.0754076   ), Coef('Var'  , 0.0628787   ), Coef('Var'  , 0.0479312   ), Coef('Var'  , 0.0480724   ), ], 
		[Coef('Var'  , 0.0417824   ), Coef('Var'  , 0.0560882   ), Coef('Var'  , 0.0683998   ), Coef('Var'  , 0.075221    ), Coef('Var'  , 0.0803299   ), Coef('Var'  , 0.073407    ), Coef('Var'  , 0.0650945   ), Coef('Var'  , 0.0532188   ), Coef('Var'  , 0.0398885   ), Coef('Var'  , 0.0417118   ), ], 
		[Coef('Var'  , 0.0501709   ), Coef('Var'  , 0.0666761   ), Coef('Var'  , 0.0814529   ), Coef('Var'  , 0.0890214   ), Coef('Var'  , 0.0949156   ), Coef('Var'  , 0.0872928   ), Coef('Var'  , 0.0771053   ), Coef('Var'  , 0.0640737   ), Coef('Var'  , 0.047977    ), Coef('Var'  , 0.0502994   ), ], ])
	etat7.initMat[Chem([Sub('2')])] = FMat([
		[Coef('Var'  , 0.118103    ), Coef('Var'  , 0.110081    ), Coef('Var'  , 0.10174     ), Coef('Var'  , 0.0961546   ), Coef('Var'  , 0.0889958   ), Coef('Var'  , 0.0927091   ), Coef('Var'  , 0.0954741   ), Coef('Var'  , 0.104256    ), Coef('Var'  , 0.11384     ), Coef('Var'  , 0.115381    ), ], 
		[Coef('Var'  , 0.101037    ), Coef('Var'  , 0.0918953   ), Coef('Var'  , 0.0826777   ), Coef('Var'  , 0.0849648   ), Coef('Var'  , 0.085619    ), Coef('Var'  , 0.0959456   ), Coef('Var'  , 0.105391    ), Coef('Var'  , 0.111369    ), Coef('Var'  , 0.118566    ), Coef('Var'  , 0.108962    ), ], 
		[Coef('Var'  , 0.0923042   ), Coef('Var'  , 0.0882586   ), Coef('Var'  , 0.0830655   ), Coef('Var'  , 0.0872491   ), Coef('Var'  , 0.0905193   ), Coef('Var'  , 0.0979463   ), Coef('Var'  , 0.106389    ), Coef('Var'  , 0.106098    ), Coef('Var'  , 0.107709    ), Coef('Var'  , 0.0997187   ), ], 
		[Coef('Var'  , 0.085384    ), Coef('Var'  , 0.0879654   ), Coef('Var'  , 0.0884827   ), Coef('Var'  , 0.0965866   ), Coef('Var'  , 0.103823    ), Coef('Var'  , 0.107654    ), Coef('Var'  , 0.113598    ), Coef('Var'  , 0.104773    ), Coef('Var'  , 0.0986728   ), Coef('Var'  , 0.0919768   ), ], 
		[Coef('Var'  , 0.0861691   ), Coef('Var'  , 0.0919602   ), Coef('Var'  , 0.096465    ), Coef('Var'  , 0.104943    ), Coef('Var'  , 0.113429    ), Coef('Var'  , 0.112503    ), Coef('Var'  , 0.112552    ), Coef('Var'  , 0.103499    ), Coef('Var'  , 0.0947707   ), Coef('Var'  , 0.0910026   ), ], 
		[Coef('Var'  , 0.0883645   ), Coef('Var'  , 0.0963673   ), Coef('Var'  , 0.103847    ), Coef('Var'  , 0.110206    ), Coef('Var'  , 0.118557    ), Coef('Var'  , 0.111802    ), Coef('Var'  , 0.106647    ), Coef('Var'  , 0.0991328   ), Coef('Var'  , 0.0903822   ), Coef('Var'  , 0.0906127   ), ], 
		[Coef('Var'  , 0.0953146   ), Coef('Var'  , 0.102187    ), Coef('Var'  , 0.110085    ), Coef('Var'  , 0.110552    ), Coef('Var'  , 0.112882    ), Coef('Var'  , 0.106101    ), Coef('Var'  , 0.0994804   ), Coef('Var'  , 0.0954174   ), Coef('Var'  , 0.0896962   ), Coef('Var'  , 0.0930868   ), ], 
		[Coef('Var'  , 0.0949232   ), Coef('Var'  , 0.100868    ), Coef('Var'  , 0.109301    ), Coef('Var'  , 0.103459    ), Coef('Var'  , 0.0996468   ), Coef('Var'  , 0.0929474   ), Coef('Var'  , 0.0852219   ), Coef('Var'  , 0.0849156   ), Coef('Var'  , 0.0822056   ), Coef('Var'  , 0.088693    ), ], 
		[Coef('Var'  , 0.109644    ), Coef('Var'  , 0.107739    ), Coef('Var'  , 0.107184    ), Coef('Var'  , 0.0973454   ), Coef('Var'  , 0.0883025   ), Coef('Var'  , 0.0846622   ), Coef('Var'  , 0.0803299   ), Coef('Var'  , 0.0867609   ), Coef('Var'  , 0.0921741   ), Coef('Var'  , 0.100784    ), ], 
		[Coef('Var'  , 0.128756    ), Coef('Var'  , 0.122678    ), Coef('Var'  , 0.117152    ), Coef('Var'  , 0.108538    ), Coef('Var'  , 0.0982261   ), Coef('Var'  , 0.0977288   ), Coef('Var'  , 0.0949156   ), Coef('Var'  , 0.103778    ), Coef('Var'  , 0.111983    ), Coef('Var'  , 0.119783    ), ], ])
	etat7.initMat[Chem([Sub('3')])] = FMat([
		[Coef('Var'  , 0.177911    ), Coef('Var'  , 0.213336    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.214583    ), Coef('Var'  , 0.180093    ), Coef('Var'  , 0.17792     ), ], 
		[Coef('Var'  , 0.243562    ), Coef('Var'  , 0.371015    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0526195   ), Coef('Var'  , 0.106313    ), Coef('Var'  , 0.173634    ), ], 
		[Coef('Var'  , 0.149589    ), Coef('Var'  , 0.199463    ), Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0379649   ), Coef('Var'  , 0.075996    ), Coef('Var'  , 0.112428    ), ], 
		[Coef('Var'  , 0.0558271   ), Coef('Var'  , 0.0279909   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0236632   ), Coef('Var'  , 0.0462855   ), Coef('Var'  , 0.0516541   ), ], 
		[Coef('Var'  , 0.0493361   ), Coef('Var'  , 0.0249781   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0225681   ), Coef('Var'  , 0.0440815   ), Coef('Var'  , 0.0475462   ), ], 
		[Coef('Var'  , 0.045845    ), Coef('Var'  , 0.0237092   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0232219   ), Coef('Var'  , 0.0449904   ), Coef('Var'  , 0.0469312   ), ], 
		[Coef('Var'  , 0.0479317   ), Coef('Var'  , 0.0247323   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0266748   ), Coef('Var'  , 0.0522995   ), Coef('Var'  , 0.0514071   ), ], 
		[Coef('Var'  , 0.042398    ), Coef('Var'  , 0.0214968   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0256688   ), Coef('Var'  , 0.0516553   ), Coef('Var'  , 0.0471656   ), ], 
		[Coef('Var'  , 0.0769764   ), Coef('Var'  , 0.0385328   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.200426    ), Coef('Var'  , 0.151302    ), Coef('Var'  , 0.113959    ), ], 
		[Coef('Var'  , 0.110624    ), Coef('Var'  , 0.054746    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.372609    ), Coef('Var'  , 0.246984    ), Coef('Var'  , 0.177355    ), ], ])
	etat7.initMat[Chem([Sub('G')])] = FMat([
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
	etat7.initMat[Chem([Sub('4')])] = FMat([
		[Coef('Var'  , 0.144355    ), Coef('Var'  , 0.161155    ), Coef('Var'  , 0.180093    ), Coef('Var'  , 0.168342    ), Coef('Var'  , 0.157487    ), Coef('Var'  , 0.137006    ), Coef('Var'  , 0.116128    ), Coef('Var'  , 0.117128    ), Coef('Var'  , 0.118103    ), Coef('Var'  , 0.130452    ), ], 
		[Coef('Var'  , 0.138505    ), Coef('Var'  , 0.121141    ), Coef('Var'  , 0.106313    ), Coef('Var'  , 0.079803    ), Coef('Var'  , 0.0544868   ), Coef('Var'  , 0.0625403   ), Coef('Var'  , 0.0705632   ), Coef('Var'  , 0.0855911   ), Coef('Var'  , 0.101037    ), Coef('Var'  , 0.118755    ), ], 
		[Coef('Var'  , 0.105268    ), Coef('Var'  , 0.09039     ), Coef('Var'  , 0.075996    ), Coef('Var'  , 0.0633269   ), Coef('Var'  , 0.0498657   ), Coef('Var'  , 0.061113    ), Coef('Var'  , 0.0703637   ), Coef('Var'  , 0.0820393   ), Coef('Var'  , 0.0923042   ), Coef('Var'  , 0.0987134   ), ], 
		[Coef('Var'  , 0.0726521   ), Coef('Var'  , 0.0602137   ), Coef('Var'  , 0.0462855   ), Coef('Var'  , 0.0478216   ), Coef('Var'  , 0.0464219   ), Coef('Var'  , 0.0613678   ), Coef('Var'  , 0.072374    ), Coef('Var'  , 0.0803277   ), Coef('Var'  , 0.085384    ), Coef('Var'  , 0.0796688   ), ], 
		[Coef('Var'  , 0.071017    ), Coef('Var'  , 0.0585313   ), Coef('Var'  , 0.0440815   ), Coef('Var'  , 0.045821    ), Coef('Var'  , 0.0452481   ), Coef('Var'  , 0.0603717   ), Coef('Var'  , 0.0730009   ), Coef('Var'  , 0.0806308   ), Coef('Var'  , 0.0861691   ), Coef('Var'  , 0.0794751   ), ], 
		[Coef('Var'  , 0.0723547   ), Coef('Var'  , 0.0603378   ), Coef('Var'  , 0.0449904   ), Coef('Var'  , 0.0468368   ), Coef('Var'  , 0.046459    ), Coef('Var'  , 0.0615597   ), Coef('Var'  , 0.0753789   ), Coef('Var'  , 0.0826665   ), Coef('Var'  , 0.0883645   ), Coef('Var'  , 0.0818376   ), ], 
		[Coef('Var'  , 0.0747617   ), Coef('Var'  , 0.0647178   ), Coef('Var'  , 0.0522995   ), Coef('Var'  , 0.0645739   ), Coef('Var'  , 0.0760241   ), Coef('Var'  , 0.0902324   ), Coef('Var'  , 0.105474    ), Coef('Var'  , 0.100036    ), Coef('Var'  , 0.0953146   ), Coef('Var'  , 0.0857455   ), ], 
		[Coef('Var'  , 0.0684066   ), Coef('Var'  , 0.0600024   ), Coef('Var'  , 0.0516553   ), Coef('Var'  , 0.074367    ), Coef('Var'  , 0.0992124   ), Coef('Var'  , 0.111867    ), Coef('Var'  , 0.128634    ), Coef('Var'  , 0.110235    ), Coef('Var'  , 0.0949232   ), Coef('Var'  , 0.0814002   ), ], 
		[Coef('Var'  , 0.106971    ), Coef('Var'  , 0.128806    ), Coef('Var'  , 0.151302    ), Coef('Var'  , 0.162808    ), Coef('Var'  , 0.175831    ), Coef('Var'  , 0.156044    ), Coef('Var'  , 0.138537    ), Coef('Var'  , 0.123202    ), Coef('Var'  , 0.109644    ), Coef('Var'  , 0.10792     ), ], 
		[Coef('Var'  , 0.145708    ), Coef('Var'  , 0.194705    ), Coef('Var'  , 0.246984    ), Coef('Var'  , 0.2463      ), Coef('Var'  , 0.248964    ), Coef('Var'  , 0.197898    ), Coef('Var'  , 0.149547    ), Coef('Var'  , 0.138144    ), Coef('Var'  , 0.128756    ), Coef('Var'  , 0.136033    ), ], ])
	etat7.initMat[Chem([Sub('5')])] = FMat([
		[Coef('Const', 0.25        ), Coef('Var'  , 0.199312    ), Coef('Var'  , 0.149678    ), Coef('Var'  , 0.111607    ), Coef('Var'  , 0.0751071   ), Coef('Var'  , 0.0372953   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.5         ), Coef('Var'  , 0.371739    ), Coef('Var'  , 0.244946    ), Coef('Var'  , 0.17608     ), Coef('Var'  , 0.109504    ), Coef('Var'  , 0.0543414   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0.25        ), Coef('Var'  , 0.211292    ), Coef('Var'  , 0.173893    ), Coef('Var'  , 0.172246    ), Coef('Var'  , 0.173301    ), Coef('Var'  , 0.210955    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0509256   ), Coef('Var'  , 0.103292    ), Coef('Var'  , 0.169607    ), Coef('Var'  , 0.23939     ), Coef('Var'  , 0.368681    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0378006   ), Coef('Var'  , 0.0758837   ), Coef('Var'  , 0.112418    ), Coef('Var'  , 0.150086    ), Coef('Var'  , 0.199618    ), Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0253632   ), Coef('Var'  , 0.0495351   ), Coef('Var'  , 0.0558579   ), Coef('Var'  , 0.0605091   ), Coef('Var'  , 0.0304947   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0253935   ), Coef('Var'  , 0.049197    ), Coef('Var'  , 0.0536005   ), Coef('Var'  , 0.0551461   ), Coef('Var'  , 0.0282071   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0225488   ), Coef('Var'  , 0.0434545   ), Coef('Var'  , 0.0459868   ), Coef('Var'  , 0.0450026   ), Coef('Var'  , 0.023438    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0248266   ), Coef('Var'  , 0.0488378   ), Coef('Var'  , 0.0462102   ), Coef('Var'  , 0.0417824   ), Coef('Var'  , 0.0213836   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0307992   ), Coef('Var'  , 0.0612825   ), Coef('Var'  , 0.0563858   ), Coef('Var'  , 0.0501709   ), Coef('Var'  , 0.0255865   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], ])
	etat7.initMat[Chem([Sub('6')])] = FMat([
		[Coef('Var'  , 0.0764396   ), Coef('Var'  , 0.0630157   ), Coef('Var'  , 0.0471566   ), Coef('Var'  , 0.0472717   ), Coef('Var'  , 0.0450785   ), Coef('Var'  , 0.0597658   ), Coef('Var'  , 0.0723584   ), Coef('Var'  , 0.0816297   ), Coef('Var'  , 0.0889958   ), Coef('Var'  , 0.0837876   ), ], 
		[Coef('Var'  , 0.0665621   ), Coef('Var'  , 0.0558243   ), Coef('Var'  , 0.0423161   ), Coef('Var'  , 0.0463767   ), Coef('Var'  , 0.0478888   ), Coef('Var'  , 0.0637022   ), Coef('Var'  , 0.0773196   ), Coef('Var'  , 0.08247     ), Coef('Var'  , 0.085619    ), Coef('Var'  , 0.0772872   ), ], 
		[Coef('Var'  , 0.0697329   ), Coef('Var'  , 0.0604934   ), Coef('Var'  , 0.0491724   ), Coef('Var'  , 0.0618454   ), Coef('Var'  , 0.0739349   ), Coef('Var'  , 0.0875954   ), Coef('Var'  , 0.102413    ), Coef('Var'  , 0.0960646   ), Coef('Var'  , 0.0905193   ), Coef('Var'  , 0.0807364   ), ], 
		[Coef('Var'  , 0.0792777   ), Coef('Var'  , 0.0714096   ), Coef('Var'  , 0.0615398   ), Coef('Var'  , 0.0847404   ), Coef('Var'  , 0.107986    ), Coef('Var'  , 0.121525    ), Coef('Var'  , 0.137551    ), Coef('Var'  , 0.119698    ), Coef('Var'  , 0.103823    ), Coef('Var'  , 0.0919759   ), ], 
		[Coef('Var'  , 0.108673    ), Coef('Var'  , 0.129279    ), Coef('Var'  , 0.151081    ), Coef('Var'  , 0.162526    ), Coef('Var'  , 0.176168    ), Coef('Var'  , 0.157404    ), Coef('Var'  , 0.141246    ), Coef('Var'  , 0.1265      ), Coef('Var'  , 0.113429    ), Coef('Var'  , 0.110647    ), ], 
		[Coef('Var'  , 0.138788    ), Coef('Var'  , 0.189272    ), Coef('Var'  , 0.243065    ), Coef('Var'  , 0.241535    ), Coef('Var'  , 0.243395    ), Coef('Var'  , 0.189941    ), Coef('Var'  , 0.139901    ), Coef('Var'  , 0.127673    ), Coef('Var'  , 0.118557    ), Coef('Var'  , 0.127125    ), ], 
		[Coef('Var'  , 0.138433    ), Coef('Var'  , 0.155213    ), Coef('Var'  , 0.17525     ), Coef('Var'  , 0.163392    ), Coef('Var'  , 0.153407    ), Coef('Var'  , 0.132301    ), Coef('Var'  , 0.111603    ), Coef('Var'  , 0.111867    ), Coef('Var'  , 0.112882    ), Coef('Var'  , 0.12439     ), ], 
		[Coef('Var'  , 0.132438    ), Coef('Var'  , 0.116367    ), Coef('Var'  , 0.103534    ), Coef('Var'  , 0.0802758   ), Coef('Var'  , 0.0578643   ), Coef('Var'  , 0.0674111   ), Coef('Var'  , 0.0754076   ), Coef('Var'  , 0.0879025   ), Coef('Var'  , 0.0996468   ), Coef('Var'  , 0.114916    ), ], 
		[Coef('Var'  , 0.101053    ), Coef('Var'  , 0.0855099   ), Coef('Var'  , 0.0714941   ), Coef('Var'  , 0.0580448   ), Coef('Var'  , 0.0449197   ), Coef('Var'  , 0.0555101   ), Coef('Var'  , 0.0650945   ), Coef('Var'  , 0.0770365   ), Coef('Var'  , 0.0883025   ), Coef('Var'  , 0.0942304   ), ], 
		[Coef('Var'  , 0.0886026   ), Coef('Var'  , 0.0736155   ), Coef('Var'  , 0.0553913   ), Coef('Var'  , 0.053992    ), Coef('Var'  , 0.0493577   ), Coef('Var'  , 0.0648438   ), Coef('Var'  , 0.0771053   ), Coef('Var'  , 0.0891578   ), Coef('Var'  , 0.0982261   ), Coef('Var'  , 0.0949033   ), ], ])
	etat7.initMat[Chem([Sub('7')])] = FMat([
		[Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0420422   ), Coef('Var'  , 0.0834996   ), Coef('Var'  , 0.1208      ), Coef('Var'  , 0.157487    ), Coef('Var'  , 0.203758    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0214835   ), Coef('Var'  , 0.0425454   ), Coef('Var'  , 0.048667    ), Coef('Var'  , 0.0544868   ), Coef('Var'  , 0.0271834   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0227734   ), Coef('Var'  , 0.0442882   ), Coef('Var'  , 0.0481354   ), Coef('Var'  , 0.0498657   ), Coef('Var'  , 0.025362    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0248226   ), Coef('Var'  , 0.0476314   ), Coef('Var'  , 0.048981    ), Coef('Var'  , 0.0464219   ), Coef('Var'  , 0.0241584   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0260952   ), Coef('Var'  , 0.0512595   ), Coef('Var'  , 0.0493481   ), Coef('Var'  , 0.0452481   ), Coef('Var'  , 0.0232529   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0288363   ), Coef('Var'  , 0.0575247   ), Coef('Var'  , 0.0524512   ), Coef('Var'  , 0.046459    ), Coef('Var'  , 0.0236149   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.19892     ), Coef('Var'  , 0.148835    ), Coef('Var'  , 0.111819    ), Coef('Var'  , 0.0760241   ), Coef('Var'  , 0.0378991   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.366456    ), Coef('Var'  , 0.235282    ), Coef('Var'  , 0.165154    ), Coef('Var'  , 0.0992124   ), Coef('Var'  , 0.0486982   ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.211609    ), Coef('Var'  , 0.174485    ), Coef('Var'  , 0.173992    ), Coef('Var'  , 0.175831    ), Coef('Var'  , 0.212382    ), ], 
		[Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.056962    ), Coef('Var'  , 0.114648    ), Coef('Var'  , 0.180653    ), Coef('Var'  , 0.248964    ), Coef('Var'  , 0.373691    ), ], ])
	etat7.initMat[Chem([Sub('8')])] = FMat([
		[Coef('Var'  , 0.0545528   ), Coef('Var'  , 0.0666431   ), Coef('Var'  , 0.0764396   ), Coef('Var'  , 0.0900347   ), Coef('Var'  , 0.10174     ), Coef('Var'  , 0.109448    ), Coef('Var'  , 0.116128    ), Coef('Var'  , 0.10029     ), Coef('Var'  , 0.0834996   ), Coef('Var'  , 0.0698515   ), ], 
		[Coef('Var'  , 0.0407878   ), Coef('Var'  , 0.0549388   ), Coef('Var'  , 0.0665621   ), Coef('Var'  , 0.0756446   ), Coef('Var'  , 0.0826777   ), Coef('Var'  , 0.077018    ), Coef('Var'  , 0.0705632   ), Coef('Var'  , 0.0568404   ), Coef('Var'  , 0.0425454   ), Coef('Var'  , 0.0424388   ), ], 
		[Coef('Var'  , 0.0441217   ), Coef('Var'  , 0.0581839   ), Coef('Var'  , 0.0697329   ), Coef('Var'  , 0.0774279   ), Coef('Var'  , 0.0830655   ), Coef('Var'  , 0.0777213   ), Coef('Var'  , 0.0703637   ), Coef('Var'  , 0.0585244   ), Coef('Var'  , 0.0442882   ), Coef('Var'  , 0.0454997   ), ], 
		[Coef('Var'  , 0.0510221   ), Coef('Var'  , 0.0665212   ), Coef('Var'  , 0.0792777   ), Coef('Var'  , 0.0850834   ), Coef('Var'  , 0.0884827   ), Coef('Var'  , 0.0820564   ), Coef('Var'  , 0.072374    ), Coef('Var'  , 0.062032    ), Coef('Var'  , 0.0476314   ), Coef('Var'  , 0.0511075   ), ], 
		[Coef('Var'  , 0.0774527   ), Coef('Var'  , 0.0928145   ), Coef('Var'  , 0.108673    ), Coef('Var'  , 0.1026      ), Coef('Var'  , 0.096465    ), Coef('Var'  , 0.0855671   ), Coef('Var'  , 0.0730009   ), Coef('Var'  , 0.0632141   ), Coef('Var'  , 0.0512595   ), Coef('Var'  , 0.0647576   ), ], 
		[Coef('Var'  , 0.107007    ), Coef('Var'  , 0.121533    ), Coef('Var'  , 0.138788    ), Coef('Var'  , 0.12021     ), Coef('Var'  , 0.103847    ), Coef('Var'  , 0.0895904   ), Coef('Var'  , 0.0753789   ), Coef('Var'  , 0.0667811   ), Coef('Var'  , 0.0575247   ), Coef('Var'  , 0.0818042   ), ], 
		[Coef('Var'  , 0.174011    ), Coef('Var'  , 0.154516    ), Coef('Var'  , 0.138433    ), Coef('Var'  , 0.122808    ), Coef('Var'  , 0.110085    ), Coef('Var'  , 0.106818    ), Coef('Var'  , 0.105474    ), Coef('Var'  , 0.126253    ), Coef('Var'  , 0.148835    ), Coef('Var'  , 0.160112    ), ], 
		[Coef('Var'  , 0.23738     ), Coef('Var'  , 0.182875    ), Coef('Var'  , 0.132438    ), Coef('Var'  , 0.119059    ), Coef('Var'  , 0.109301    ), Coef('Var'  , 0.11697     ), Coef('Var'  , 0.128634    ), Coef('Var'  , 0.179625    ), Coef('Var'  , 0.235282    ), Coef('Var'  , 0.234072    ), ], 
		[Coef('Var'  , 0.146499    ), Coef('Var'  , 0.122783    ), Coef('Var'  , 0.101053    ), Coef('Var'  , 0.103284    ), Coef('Var'  , 0.107184    ), Coef('Var'  , 0.121861    ), Coef('Var'  , 0.138537    ), Coef('Var'  , 0.155271    ), Coef('Var'  , 0.174485    ), Coef('Var'  , 0.159308    ), ], 
		[Coef('Var'  , 0.0671663   ), Coef('Var'  , 0.0791922   ), Coef('Var'  , 0.0886026   ), Coef('Var'  , 0.103848    ), Coef('Var'  , 0.117152    ), Coef('Var'  , 0.132949    ), Coef('Var'  , 0.149547    ), Coef('Var'  , 0.13117     ), Coef('Var'  , 0.114648    ), Coef('Var'  , 0.0910478   ), ], ])
	etat7.initMat[Chem([Sub('9')])] = FMat([
		[Coef('Var'  , 0.149678    ), Coef('Var'  , 0.162648    ), Coef('Var'  , 0.177911    ), Coef('Var'  , 0.159908    ), Coef('Var'  , 0.144355    ), Coef('Var'  , 0.128072    ), Coef('Var'  , 0.11384     ), Coef('Var'  , 0.109169    ), Coef('Var'  , 0.106238    ), Coef('Var'  , 0.126981    ), ], 
		[Coef('Var'  , 0.244946    ), Coef('Var'  , 0.242754    ), Coef('Var'  , 0.243562    ), Coef('Var'  , 0.189536    ), Coef('Var'  , 0.138505    ), Coef('Var'  , 0.127248    ), Coef('Var'  , 0.118566    ), Coef('Var'  , 0.128737    ), Coef('Var'  , 0.141301    ), Coef('Var'  , 0.191749    ), ], 
		[Coef('Var'  , 0.173893    ), Coef('Var'  , 0.160755    ), Coef('Var'  , 0.149589    ), Coef('Var'  , 0.126888    ), Coef('Var'  , 0.105268    ), Coef('Var'  , 0.105856    ), Coef('Var'  , 0.107709    ), Coef('Var'  , 0.120756    ), Coef('Var'  , 0.136204    ), Coef('Var'  , 0.153617    ), ], 
		[Coef('Var'  , 0.103292    ), Coef('Var'  , 0.0789165   ), Coef('Var'  , 0.0558271   ), Coef('Var'  , 0.0645414   ), Coef('Var'  , 0.0726521   ), Coef('Var'  , 0.085409    ), Coef('Var'  , 0.0986728   ), Coef('Var'  , 0.114247    ), Coef('Var'  , 0.132992    ), Coef('Var'  , 0.116314    ), ], 
		[Coef('Var'  , 0.0758837   ), Coef('Var'  , 0.0627787   ), Coef('Var'  , 0.0493361   ), Coef('Var'  , 0.0609413   ), Coef('Var'  , 0.071017    ), Coef('Var'  , 0.0834538   ), Coef('Var'  , 0.0947707   ), Coef('Var'  , 0.100726    ), Coef('Var'  , 0.106983    ), Coef('Var'  , 0.0910357   ), ], 
		[Coef('Var'  , 0.0495351   ), Coef('Var'  , 0.0490724   ), Coef('Var'  , 0.045845    ), Coef('Var'  , 0.0608252   ), Coef('Var'  , 0.0723547   ), Coef('Var'  , 0.0830069   ), Coef('Var'  , 0.0903822   ), Coef('Var'  , 0.0862662   ), Coef('Var'  , 0.0796181   ), Coef('Var'  , 0.0657384   ), ], 
		[Coef('Var'  , 0.049197    ), Coef('Var'  , 0.0501257   ), Coef('Var'  , 0.0479317   ), Coef('Var'  , 0.0627752   ), Coef('Var'  , 0.0747617   ), Coef('Var'  , 0.0834272   ), Coef('Var'  , 0.0896962   ), Coef('Var'  , 0.0848361   ), Coef('Var'  , 0.0773959   ), Coef('Var'  , 0.0648453   ), ], 
		[Coef('Var'  , 0.0434545   ), Coef('Var'  , 0.0440456   ), Coef('Var'  , 0.042398    ), Coef('Var'  , 0.0558304   ), Coef('Var'  , 0.0684066   ), Coef('Var'  , 0.0759601   ), Coef('Var'  , 0.0822056   ), Coef('Var'  , 0.0773768   ), Coef('Var'  , 0.069415    ), Coef('Var'  , 0.0582992   ), ], 
		[Coef('Var'  , 0.0488378   ), Coef('Var'  , 0.0633594   ), Coef('Var'  , 0.0769764   ), Coef('Var'  , 0.0919126   ), Coef('Var'  , 0.106971    ), Coef('Var'  , 0.0996244   ), Coef('Var'  , 0.0921741   ), Coef('Var'  , 0.0809492   ), Coef('Var'  , 0.0683998   ), Coef('Var'  , 0.0595312   ), ], 
		[Coef('Var'  , 0.0612825   ), Coef('Var'  , 0.0855452   ), Coef('Var'  , 0.110624    ), Coef('Var'  , 0.126842    ), Coef('Var'  , 0.145708    ), Coef('Var'  , 0.127943    ), Coef('Var'  , 0.111983    ), Coef('Var'  , 0.096936    ), Coef('Var'  , 0.0814529   ), Coef('Var'  , 0.0718888   ), ], ])
	etat7.initMat[Chem([Sub('10')])] = FMat([
		[Coef('Var'  , 0.0471566   ), Coef('Var'  , 0.0519911   ), Coef('Var'  , 0.0545528   ), Coef('Var'  , 0.0278093   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0241818   ), ], 
		[Coef('Var'  , 0.0423161   ), Coef('Var'  , 0.0427961   ), Coef('Var'  , 0.0407878   ), Coef('Var'  , 0.0209553   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0218408   ), ], 
		[Coef('Var'  , 0.0491724   ), Coef('Var'  , 0.0477622   ), Coef('Var'  , 0.0441217   ), Coef('Var'  , 0.0227264   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0250358   ), ], 
		[Coef('Var'  , 0.0615398   ), Coef('Var'  , 0.0574582   ), Coef('Var'  , 0.0510221   ), Coef('Var'  , 0.0262849   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0311733   ), ], 
		[Coef('Var'  , 0.151081    ), Coef('Var'  , 0.113789    ), Coef('Var'  , 0.0774527   ), Coef('Var'  , 0.0386624   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.200127    ), ], 
		[Coef('Var'  , 0.243065    ), Coef('Var'  , 0.173675    ), Coef('Var'  , 0.107007    ), Coef('Var'  , 0.0529679   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.370707    ), ], 
		[Coef('Var'  , 0.17525     ), Coef('Var'  , 0.173083    ), Coef('Var'  , 0.174011    ), Coef('Var'  , 0.211193    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.211891    ), ], 
		[Coef('Var'  , 0.103534    ), Coef('Var'  , 0.168726    ), Coef('Var'  , 0.23738     ), Coef('Var'  , 0.367617    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0511091   ), ], 
		[Coef('Var'  , 0.0714941   ), Coef('Var'  , 0.108124    ), Coef('Var'  , 0.146499    ), Coef('Var'  , 0.197699    ), Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0354254   ), ], 
		[Coef('Var'  , 0.0553913   ), Coef('Var'  , 0.0625949   ), Coef('Var'  , 0.0671663   ), Coef('Var'  , 0.0340858   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0285091   ), ], ])
	
	
	
	etat8.bords   = {Bord('0'): etat13, Bord('1'): etat13, Bord('2'): etat13, Bord('3'): etat13, Bord('4'): etat13, }
	etat8.permuts = {}
	etat8.interns = {Intern('_'): etat8, }
	etat8.subs    = {Sub('0'): etat1, Sub('1'): etat2, Sub('2'): etat3, Sub('3'): etat4, Sub('G', True): Etat.etatPoint, Sub('4'): etat5, Sub('5'): etat6, Sub('6'): etat7, Sub('7'): etat9, Sub('8'): etat10, Sub('9'): etat11, Sub('10'): etat12, }
	
	etat8.buildIntern()
	
	
	etat8.eqs = [
		(Chem([Bord('2'), Sub('0'), Permut('0'), ])	,	Chem([Sub('0'), Bord('0'), ])),
		(Chem([Bord('1'), Sub('1'), Permut('0'), ])	,	Chem([Sub('0'), Bord('1'), ])),
		(Chem([Bord('3'), Sub('0'), Permut('0'), ])	,	Chem([Sub('1'), Bord('2'), ])),
		(Chem([Bord('2'), Sub('1'), Permut('0'), ])	,	Chem([Sub('1'), Bord('3'), ])),
		(Chem([Bord('4'), Sub('0'), Permut('0'), ])	,	Chem([Sub('2'), Bord('1'), ])),
		(Chem([Bord('3'), Sub('1'), Permut('0'), ])	,	Chem([Sub('2'), Bord('2'), ])),
		(Chem([Bord('0'), Sub('0'), Permut('0'), ])	,	Chem([Sub('8'), Bord('0'), ])),
		(Chem([Bord('4'), Sub('1'), Permut('0'), ])	,	Chem([Sub('8'), Bord('1'), ])),
		(Chem([Bord('0'), Sub('1'), Permut('0'), ])	,	Chem([Sub('10'), Bord('0'), ])),
		(Chem([Bord('1'), Sub('0'), Permut('0'), ])	,	Chem([Sub('10'), Bord('4'), ])),
		(Chem([Sub('0'), Bord('1'), Bord('1'), ])	,	Chem([Sub('10'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('2'), Bord('1'), ])	,	Chem([Sub('6'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('3'), Bord('1'), ])	,	Chem([Sub('5'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('4'), Bord('1'), ])	,	Chem([Sub('1'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('0'), Bord('1'), ])	,	Chem([Sub('9'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('1'), Bord('1'), ])	,	Chem([Sub('2'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('4'), Bord('1'), ])	,	Chem([Sub('5'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('0'), Bord('1'), ])	,	Chem([Sub('8'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('3'), Bord('1'), ])	,	Chem([Sub('9'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('4'), Bord('1'), ])	,	Chem([Sub('4'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('3'), Bord('0'), Bord('1'), ])	,	Chem([Sub('5'), Bord('4'), Bord('1'), ])),
		(Chem([Sub('3'), Bord('1'), Bord('1'), ])	,	Chem([Sub('6'), Bord('4'), Bord('1'), ])),
		(Chem([Sub('3'), Bord('2'), Bord('1'), ])	,	Chem([Sub('7'), Bord('4'), Bord('1'), ])),
		(Chem([Sub('3'), Bord('3'), Bord('1'), ])	,	Chem([Sub('4'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('3'), Bord('4'), Bord('1'), ])	,	Chem([Sub('9'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('4'), Bord('1'), Bord('1'), ])	,	Chem([Sub('7'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('4'), Bord('2'), Bord('1'), ])	,	Chem([Sub('8'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('4'), Bord('4'), Bord('1'), ])	,	Chem([Sub('9'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('5'), Bord('0'), Bord('1'), ])	,	Chem([Sub('9'), Bord('4'), Bord('1'), ])),
		(Chem([Sub('5'), Bord('3'), Bord('1'), ])	,	Chem([Sub('6'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('6'), Bord('2'), Bord('1'), ])	,	Chem([Sub('10'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('6'), Bord('3'), Bord('1'), ])	,	Chem([Sub('7'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('7'), Bord('1'), Bord('1'), ])	,	Chem([Sub('10'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('7'), Bord('2'), Bord('1'), ])	,	Chem([Sub('8'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('8'), Bord('4'), Bord('1'), ])	,	Chem([Sub('10'), Bord('0'), Bord('1'), ])),
		(Chem([Bord('0'), Bord('1'), ])	,	Chem([Bord('1'), Bord('0'), ])),
		(Chem([Bord('1'), Bord('1'), ])	,	Chem([Bord('2'), Bord('0'), ])),
		(Chem([Bord('2'), Bord('1'), ])	,	Chem([Bord('3'), Bord('0'), ])),
		(Chem([Bord('3'), Bord('1'), ])	,	Chem([Bord('4'), Bord('0'), ])),
		(Chem([Bord('4'), Bord('1'), ])	,	Chem([Bord('0'), Bord('0'), ])),
		]
	
	
	etat8.prim.elems = [Figure(2, [Chem([Bord('0'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('0'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('0'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('0'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('1'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('1'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('1'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('1'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('2'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('2'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('2'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('2'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('3'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('3'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('3'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('3'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('4'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('4'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('4'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('4'), Sub('1'), Sub('1'), Bord('0'), ]), ])]
	etat8.grid.elems = [
		Figure(1, [Chem([Bord('1'), Bord('0'), ]), Chem([Bord('1'), Intern(''), ]), Chem([Bord('1'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('4'), Bord('0'), ]), Chem([Bord('4'), Intern(''), ]), Chem([Bord('4'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('2'), Bord('0'), ]), Chem([Bord('2'), Intern(''), ]), Chem([Bord('2'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('0'), Bord('0'), ]), Chem([Bord('0'), Intern(''), ]), Chem([Bord('0'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('3'), Bord('0'), ]), Chem([Bord('3'), Intern(''), ]), Chem([Bord('3'), Bord('1'), ]), ]), ]
	
	
	etat8.space = [Chem([Bord('4'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('2'), Intern('0'), Intern('0'), ]), Chem([Bord('2'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('3'), Intern('0'), Intern('0'), ]), Chem([Bord('4'), Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('4'), Intern('0'), Intern('0'), ]), ]
	
	etat8.initMat[Chem([Sub('0')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0242585   ), Coef('Var'  , 0.0477904   ), Coef('Var'  , 0.0465574   ), Coef('Var'  , 0.043416    ), Coef('Var'  , 0.0222989   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0282484   ), Coef('Var'  , 0.056424    ), Coef('Var'  , 0.050381    ), Coef('Var'  , 0.0437357   ), Coef('Var'  , 0.0221326   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.198717    ), Coef('Var'  , 0.148037    ), Coef('Var'  , 0.110625    ), Coef('Var'  , 0.0738506   ), Coef('Var'  , 0.036908    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.372283    ), Coef('Var'  , 0.246069    ), Coef('Var'  , 0.176988    ), Coef('Var'  , 0.110239    ), Coef('Var'  , 0.0547047   ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.212321    ), Coef('Var'  , 0.175683    ), Coef('Var'  , 0.174773    ), Coef('Var'  , 0.175896    ), Coef('Var'  , 0.212452    ), ], 
		[Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0542222   ), Coef('Var'  , 0.109717    ), Coef('Var'  , 0.176237    ), Coef('Var'  , 0.245874    ), Coef('Var'  , 0.372015    ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0382556   ), Coef('Var'  , 0.0765673   ), Coef('Var'  , 0.11362     ), Coef('Var'  , 0.151244    ), Coef('Var'  , 0.200365    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0274007   ), Coef('Var'  , 0.0538081   ), Coef('Var'  , 0.0592516   ), Coef('Var'  , 0.0635827   ), Coef('Var'  , 0.0318509   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0203964   ), Coef('Var'  , 0.0395885   ), Coef('Var'  , 0.0437928   ), Coef('Var'  , 0.0458493   ), Coef('Var'  , 0.0233964   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0238971   ), Coef('Var'  , 0.0463152   ), Coef('Var'  , 0.0477738   ), Coef('Var'  , 0.0463126   ), Coef('Var'  , 0.0238768   ), ], ])
	etat8.initMat[Chem([Sub('1')])] = FMat([
		[Coef('Var'  , 0.0454857   ), Coef('Var'  , 0.0498564   ), Coef('Var'  , 0.0516837   ), Coef('Var'  , 0.0264079   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0234486   ), ], 
		[Coef('Var'  , 0.0393575   ), Coef('Var'  , 0.040624    ), Coef('Var'  , 0.0401489   ), Coef('Var'  , 0.0205546   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0200693   ), ], 
		[Coef('Var'  , 0.0463039   ), Coef('Var'  , 0.0440532   ), Coef('Var'  , 0.0402      ), Coef('Var'  , 0.0205662   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.023487    ), ], 
		[Coef('Var'  , 0.0604591   ), Coef('Var'  , 0.0553764   ), Coef('Var'  , 0.0487524   ), Coef('Var'  , 0.0249108   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0304656   ), ], 
		[Coef('Var'  , 0.148756    ), Coef('Var'  , 0.110401    ), Coef('Var'  , 0.0730021   ), Coef('Var'  , 0.0363541   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.199047    ), ], 
		[Coef('Var'  , 0.247321    ), Coef('Var'  , 0.178536    ), Coef('Var'  , 0.11225     ), Coef('Var'  , 0.0556799   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.372856    ), ], 
		[Coef('Var'  , 0.177098    ), Coef('Var'  , 0.176023    ), Coef('Var'  , 0.177113    ), Coef('Var'  , 0.213001    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.213022    ), ], 
		[Coef('Var'  , 0.11316     ), Coef('Var'  , 0.180549    ), Coef('Var'  , 0.250747    ), Coef('Var'  , 0.37457     ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0559783   ), ], 
		[Coef('Var'  , 0.0717788   ), Coef('Var'  , 0.107806    ), Coef('Var'  , 0.144556    ), Coef('Var'  , 0.196916    ), Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0358899   ), ], 
		[Coef('Var'  , 0.0502797   ), Coef('Var'  , 0.0567754   ), Coef('Var'  , 0.0615479   ), Coef('Var'  , 0.031039    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0257364   ), ], ])
	etat8.initMat[Chem([Sub('2')])] = FMat([
		[Coef('Var'  , 0.149752    ), Coef('Var'  , 0.199575    ), Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0387077   ), Coef('Var'  , 0.0772633   ), Coef('Var'  , 0.113283    ), ], 
		[Coef('Var'  , 0.0584284   ), Coef('Var'  , 0.0294464   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.023556    ), Coef('Var'  , 0.0460881   ), Coef('Var'  , 0.0530024   ), ], 
		[Coef('Var'  , 0.0468307   ), Coef('Var'  , 0.0237898   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0207788   ), Coef('Var'  , 0.0405641   ), Coef('Var'  , 0.0445687   ), ], 
		[Coef('Var'  , 0.0457627   ), Coef('Var'  , 0.023655    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.023462    ), Coef('Var'  , 0.0454361   ), Coef('Var'  , 0.0471171   ), ], 
		[Coef('Var'  , 0.036741    ), Coef('Var'  , 0.0186168   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0218797   ), Coef('Var'  , 0.0434975   ), Coef('Var'  , 0.0404965   ), ], 
		[Coef('Var'  , 0.0522155   ), Coef('Var'  , 0.0267096   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0320392   ), Coef('Var'  , 0.0635537   ), Coef('Var'  , 0.0587487   ), ], 
		[Coef('Var'  , 0.0776568   ), Coef('Var'  , 0.0388417   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.200559    ), Coef('Var'  , 0.151706    ), Coef('Var'  , 0.114401    ), ], 
		[Coef('Var'  , 0.121825    ), Coef('Var'  , 0.0608154   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.377081    ), Coef('Var'  , 0.255239    ), Coef('Var'  , 0.187896    ), ], 
		[Coef('Var'  , 0.165935    ), Coef('Var'  , 0.207058    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.207698    ), Coef('Var'  , 0.167063    ), Coef('Var'  , 0.164756    ), ], 
		[Coef('Var'  , 0.244853    ), Coef('Var'  , 0.371492    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0542383   ), Coef('Var'  , 0.10959     ), Coef('Var'  , 0.17573     ), ], ])
	etat8.initMat[Chem([Sub('3')])] = FMat([
		[Coef('Var'  , 0.0935089   ), Coef('Var'  , 0.0892224   ), Coef('Var'  , 0.083343    ), Coef('Var'  , 0.0863256   ), Coef('Var'  , 0.0884036   ), Coef('Var'  , 0.0951411   ), Coef('Var'  , 0.103336    ), Coef('Var'  , 0.103778    ), Coef('Var'  , 0.10648     ), Coef('Var'  , 0.0998212   ), ], 
		[Coef('Var'  , 0.0847807   ), Coef('Var'  , 0.0853417   ), Coef('Var'  , 0.0842141   ), Coef('Var'  , 0.0947957   ), Coef('Var'  , 0.104559    ), Coef('Var'  , 0.111991    ), Coef('Var'  , 0.120276    ), Coef('Var'  , 0.112066    ), Coef('Var'  , 0.104839    ), Coef('Var'  , 0.0951664   ), ], 
		[Coef('Var'  , 0.0773792   ), Coef('Var'  , 0.0823069   ), Coef('Var'  , 0.0868147   ), Coef('Var'  , 0.0950291   ), Coef('Var'  , 0.104297    ), Coef('Var'  , 0.103536    ), Coef('Var'  , 0.104655    ), Coef('Var'  , 0.0956567   ), Coef('Var'  , 0.0875045   ), Coef('Var'  , 0.0827199   ), ], 
		[Coef('Var'  , 0.0892777   ), Coef('Var'  , 0.0986413   ), Coef('Var'  , 0.107509    ), Coef('Var'  , 0.114344    ), Coef('Var'  , 0.122613    ), Coef('Var'  , 0.114859    ), Coef('Var'  , 0.108395    ), Coef('Var'  , 0.0995729   ), Coef('Var'  , 0.0899847   ), Coef('Var'  , 0.0905242   ), ], 
		[Coef('Var'  , 0.0868745   ), Coef('Var'  , 0.0970935   ), Coef('Var'  , 0.10779     ), Coef('Var'  , 0.107327    ), Coef('Var'  , 0.107777    ), Coef('Var'  , 0.097229    ), Coef('Var'  , 0.0870332   ), Coef('Var'  , 0.081444    ), Coef('Var'  , 0.0753818   ), Coef('Var'  , 0.0813158   ), ], 
		[Coef('Var'  , 0.113966    ), Coef('Var'  , 0.120076    ), Coef('Var'  , 0.126948    ), Coef('Var'  , 0.118829    ), Coef('Var'  , 0.111722    ), Coef('Var'  , 0.103878    ), Coef('Var'  , 0.0949569   ), Coef('Var'  , 0.0968341   ), Coef('Var'  , 0.09619     ), Coef('Var'  , 0.105799    ), ], 
		[Coef('Var'  , 0.111646    ), Coef('Var'  , 0.110583    ), Coef('Var'  , 0.110991    ), Coef('Var'  , 0.101583    ), Coef('Var'  , 0.0929108   ), Coef('Var'  , 0.088748    ), Coef('Var'  , 0.0838747   ), Coef('Var'  , 0.089573    ), Coef('Var'  , 0.0943527   ), Coef('Var'  , 0.102771    ), ], 
		[Coef('Var'  , 0.136657    ), Coef('Var'  , 0.126672    ), Coef('Var'  , 0.118113    ), Coef('Var'  , 0.111289    ), Coef('Var'  , 0.103881    ), Coef('Var'  , 0.108427    ), Coef('Var'  , 0.110029    ), Coef('Var'  , 0.120295    ), Coef('Var'  , 0.128094    ), Coef('Var'  , 0.132247    ), ], 
		[Coef('Var'  , 0.0960297   ), Coef('Var'  , 0.0884907   ), Coef('Var'  , 0.082107    ), Coef('Var'  , 0.0774451   ), Coef('Var'  , 0.0720908   ), Coef('Var'  , 0.0752316   ), Coef('Var'  , 0.0781207   ), Coef('Var'  , 0.0849069   ), Coef('Var'  , 0.0935599   ), Coef('Var'  , 0.0934153   ), ], 
		[Coef('Var'  , 0.10988     ), Coef('Var'  , 0.101572    ), Coef('Var'  , 0.0921696   ), Coef('Var'  , 0.0930321   ), Coef('Var'  , 0.0917446   ), Coef('Var'  , 0.100959    ), Coef('Var'  , 0.109324    ), Coef('Var'  , 0.115875    ), Coef('Var'  , 0.123614    ), Coef('Var'  , 0.11622     ), ], ])
	etat8.initMat[Chem([Sub('G')])] = FMat([
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
	etat8.initMat[Chem([Sub('4')])] = FMat([
		[Coef('Var'  , 0.10616     ), Coef('Var'  , 0.105763    ), Coef('Var'  , 0.10648     ), Coef('Var'  , 0.118269    ), Coef('Var'  , 0.132941    ), Coef('Var'  , 0.150576    ), Coef('Var'  , 0.171767    ), Coef('Var'  , 0.159662    ), Coef('Var'  , 0.149752    ), Coef('Var'  , 0.127558    ), ], 
		[Coef('Var'  , 0.0758294   ), Coef('Var'  , 0.0907326   ), Coef('Var'  , 0.104839    ), Coef('Var'  , 0.12168     ), Coef('Var'  , 0.140186    ), Coef('Var'  , 0.122577    ), Coef('Var'  , 0.107635    ), Coef('Var'  , 0.0826913   ), Coef('Var'  , 0.0584284   ), Coef('Var'  , 0.0678317   ), ], 
		[Coef('Var'  , 0.0652495   ), Coef('Var'  , 0.0768312   ), Coef('Var'  , 0.0875045   ), Coef('Var'  , 0.0947326   ), Coef('Var'  , 0.102341    ), Coef('Var'  , 0.0879972   ), Coef('Var'  , 0.0741293   ), Coef('Var'  , 0.060836    ), Coef('Var'  , 0.0468307   ), Coef('Var'  , 0.0568394   ), ], 
		[Coef('Var'  , 0.0717898   ), Coef('Var'  , 0.082136    ), Coef('Var'  , 0.0899847   ), Coef('Var'  , 0.0859012   ), Coef('Var'  , 0.0798792   ), Coef('Var'  , 0.0659721   ), Coef('Var'  , 0.0498398   ), Coef('Var'  , 0.0491965   ), Coef('Var'  , 0.0457627   ), Coef('Var'  , 0.0603205   ), ], 
		[Coef('Var'  , 0.0616911   ), Coef('Var'  , 0.0689352   ), Coef('Var'  , 0.0753818   ), Coef('Var'  , 0.0691505   ), Coef('Var'  , 0.0620062   ), Coef('Var'  , 0.0499795   ), Coef('Var'  , 0.0368843   ), Coef('Var'  , 0.037328    ), Coef('Var'  , 0.036741    ), Coef('Var'  , 0.0496698   ), ], 
		[Coef('Var'  , 0.0843743   ), Coef('Var'  , 0.0914931   ), Coef('Var'  , 0.09619     ), Coef('Var'  , 0.0881619   ), Coef('Var'  , 0.0769676   ), Coef('Var'  , 0.0645184   ), Coef('Var'  , 0.0485922   ), Coef('Var'  , 0.0518199   ), Coef('Var'  , 0.0522155   ), Coef('Var'  , 0.0694488   ), ], 
		[Coef('Var'  , 0.107888    ), Coef('Var'  , 0.101057    ), Coef('Var'  , 0.0943527   ), Coef('Var'  , 0.0835591   ), Coef('Var'  , 0.0713684   ), Coef('Var'  , 0.0621646   ), Coef('Var'  , 0.0508273   ), Coef('Var'  , 0.0647449   ), Coef('Var'  , 0.0776568   ), Coef('Var'  , 0.0926013   ), ], 
		[Coef('Var'  , 0.158828    ), Coef('Var'  , 0.143444    ), Coef('Var'  , 0.128094    ), Coef('Var'  , 0.115157    ), Coef('Var'  , 0.0995533   ), Coef('Var'  , 0.0889809   ), Coef('Var'  , 0.074946    ), Coef('Var'  , 0.0990045   ), Coef('Var'  , 0.121825    ), Coef('Var'  , 0.139894    ), ], 
		[Coef('Var'  , 0.125047    ), Coef('Var'  , 0.107489    ), Coef('Var'  , 0.0935599   ), Coef('Var'  , 0.0912574   ), Coef('Var'  , 0.0916255   ), Coef('Var'  , 0.11482     ), Coef('Var'  , 0.140407    ), Coef('Var'  , 0.151643    ), Coef('Var'  , 0.165935    ), Coef('Var'  , 0.143524    ), ], 
		[Coef('Var'  , 0.143143    ), Coef('Var'  , 0.132119    ), Coef('Var'  , 0.123614    ), Coef('Var'  , 0.132131    ), Coef('Var'  , 0.143131    ), Coef('Var'  , 0.192414    ), Coef('Var'  , 0.244973    ), Coef('Var'  , 0.243073    ), Coef('Var'  , 0.244853    ), Coef('Var'  , 0.192313    ), ], ])
	etat8.initMat[Chem([Sub('5')])] = FMat([
		[Coef('Var'  , 0.083343    ), Coef('Var'  , 0.0791185   ), Coef('Var'  , 0.0723757   ), Coef('Var'  , 0.0603855   ), Coef('Var'  , 0.0454857   ), Coef('Var'  , 0.0457475   ), Coef('Var'  , 0.043416    ), Coef('Var'  , 0.0569723   ), Coef('Var'  , 0.0683442   ), Coef('Var'  , 0.076855    ), ], 
		[Coef('Var'  , 0.0842141   ), Coef('Var'  , 0.0755272   ), Coef('Var'  , 0.0649822   ), Coef('Var'  , 0.0530739   ), Coef('Var'  , 0.0393575   ), Coef('Var'  , 0.0422019   ), Coef('Var'  , 0.0437357   ), Coef('Var'  , 0.0592833   ), Coef('Var'  , 0.0737019   ), Coef('Var'  , 0.0796733   ), ], 
		[Coef('Var'  , 0.0868147   ), Coef('Var'  , 0.0760074   ), Coef('Var'  , 0.0645535   ), Coef('Var'  , 0.0561258   ), Coef('Var'  , 0.0463039   ), Coef('Var'  , 0.060395    ), Coef('Var'  , 0.0738506   ), Coef('Var'  , 0.0875964   ), Coef('Var'  , 0.101868    ), Coef('Var'  , 0.094057    ), ], 
		[Coef('Var'  , 0.107509    ), Coef('Var'  , 0.0931642   ), Coef('Var'  , 0.0784115   ), Coef('Var'  , 0.0700422   ), Coef('Var'  , 0.0604591   ), Coef('Var'  , 0.0851703   ), Coef('Var'  , 0.110239    ), Coef('Var'  , 0.125592    ), Coef('Var'  , 0.143118    ), Coef('Var'  , 0.124475    ), ], 
		[Coef('Var'  , 0.10779     ), Coef('Var'  , 0.104859    ), Coef('Var'  , 0.10286     ), Coef('Var'  , 0.125246    ), Coef('Var'  , 0.148756    ), Coef('Var'  , 0.161499    ), Coef('Var'  , 0.175896    ), Coef('Var'  , 0.156611    ), Coef('Var'  , 0.13925     ), Coef('Var'  , 0.122819    ), ], 
		[Coef('Var'  , 0.126948    ), Coef('Var'  , 0.135971    ), Coef('Var'  , 0.147064    ), Coef('Var'  , 0.195795    ), Coef('Var'  , 0.247321    ), Coef('Var'  , 0.244871    ), Coef('Var'  , 0.245874    ), Coef('Var'  , 0.193541    ), Coef('Var'  , 0.144605    ), Coef('Var'  , 0.134556    ), ], 
		[Coef('Var'  , 0.110991    ), Coef('Var'  , 0.124927    ), Coef('Var'  , 0.140897    ), Coef('Var'  , 0.157839    ), Coef('Var'  , 0.177098    ), Coef('Var'  , 0.163387    ), Coef('Var'  , 0.151244    ), Coef('Var'  , 0.128546    ), Coef('Var'  , 0.106787    ), Coef('Var'  , 0.108292    ), ], 
		[Coef('Var'  , 0.118113    ), Coef('Var'  , 0.133214    ), Coef('Var'  , 0.150503    ), Coef('Var'  , 0.130402    ), Coef('Var'  , 0.11316     ), Coef('Var'  , 0.0878292   ), Coef('Var'  , 0.0635827   ), Coef('Var'  , 0.0752      ), Coef('Var'  , 0.0862155   ), Coef('Var'  , 0.10214     ), ], 
		[Coef('Var'  , 0.082107    ), Coef('Var'  , 0.0893938   ), Coef('Var'  , 0.0971169   ), Coef('Var'  , 0.0841859   ), Coef('Var'  , 0.0717788   ), Coef('Var'  , 0.0592863   ), Coef('Var'  , 0.0458493   ), Coef('Var'  , 0.0552908   ), Coef('Var'  , 0.0626873   ), Coef('Var'  , 0.0729923   ), ], 
		[Coef('Var'  , 0.0921696   ), Coef('Var'  , 0.0878185   ), Coef('Var'  , 0.0812361   ), Coef('Var'  , 0.0669049   ), Coef('Var'  , 0.0502797   ), Coef('Var'  , 0.0496132   ), Coef('Var'  , 0.0463126   ), Coef('Var'  , 0.0613678   ), Coef('Var'  , 0.0734235   ), Coef('Var'  , 0.084141    ), ], ])
	etat8.initMat[Chem([Sub('6')])] = FMat([
		[Coef('Var'  , 0.0884036   ), Coef('Var'  , 0.0788174   ), Coef('Var'  , 0.0683442   ), Coef('Var'  , 0.0589319   ), Coef('Var'  , 0.0477904   ), Coef('Var'  , 0.0601528   ), Coef('Var'  , 0.0721628   ), Coef('Var'  , 0.0852792   ), Coef('Var'  , 0.0997385   ), Coef('Var'  , 0.0935288   ), ], 
		[Coef('Var'  , 0.104559    ), Coef('Var'  , 0.0894239   ), Coef('Var'  , 0.0737019   ), Coef('Var'  , 0.0653992   ), Coef('Var'  , 0.056424    ), Coef('Var'  , 0.0815585   ), Coef('Var'  , 0.107659    ), Coef('Var'  , 0.12319     ), Coef('Var'  , 0.14094     ), Coef('Var'  , 0.122153    ), ], 
		[Coef('Var'  , 0.104297    ), Coef('Var'  , 0.102349    ), Coef('Var'  , 0.101868    ), Coef('Var'  , 0.124405    ), Coef('Var'  , 0.148037    ), Coef('Var'  , 0.159511    ), Coef('Var'  , 0.172923    ), Coef('Var'  , 0.152224    ), Coef('Var'  , 0.13447     ), Coef('Var'  , 0.11809     ), ], 
		[Coef('Var'  , 0.122613    ), Coef('Var'  , 0.131644    ), Coef('Var'  , 0.143118    ), Coef('Var'  , 0.193171    ), Coef('Var'  , 0.246069    ), Coef('Var'  , 0.244445    ), Coef('Var'  , 0.245919    ), Coef('Var'  , 0.193025    ), Coef('Var'  , 0.143146    ), Coef('Var'  , 0.13162     ), ], 
		[Coef('Var'  , 0.107777    ), Coef('Var'  , 0.122826    ), Coef('Var'  , 0.13925     ), Coef('Var'  , 0.15648     ), Coef('Var'  , 0.175683    ), Coef('Var'  , 0.160991    ), Coef('Var'  , 0.148145    ), Coef('Var'  , 0.12463     ), Coef('Var'  , 0.102449    ), Coef('Var'  , 0.104628    ), ], 
		[Coef('Var'  , 0.111722    ), Coef('Var'  , 0.127323    ), Coef('Var'  , 0.144605    ), Coef('Var'  , 0.125747    ), Coef('Var'  , 0.109717    ), Coef('Var'  , 0.0848708   ), Coef('Var'  , 0.0610572   ), Coef('Var'  , 0.0719407   ), Coef('Var'  , 0.0817299   ), Coef('Var'  , 0.0970903   ), ], 
		[Coef('Var'  , 0.0929108   ), Coef('Var'  , 0.0996541   ), Coef('Var'  , 0.106787    ), Coef('Var'  , 0.091437    ), Coef('Var'  , 0.0765673   ), Coef('Var'  , 0.0630805   ), Coef('Var'  , 0.0489977   ), Coef('Var'  , 0.059916    ), Coef('Var'  , 0.0693933   ), Coef('Var'  , 0.0815637   ), ], 
		[Coef('Var'  , 0.103881    ), Coef('Var'  , 0.0958476   ), Coef('Var'  , 0.0862155   ), Coef('Var'  , 0.0707499   ), Coef('Var'  , 0.0538081   ), Coef('Var'  , 0.0560751   ), Coef('Var'  , 0.0552941   ), Coef('Var'  , 0.0739518   ), Coef('Var'  , 0.0881802   ), Coef('Var'  , 0.0977758   ), ], 
		[Coef('Var'  , 0.0720908   ), Coef('Var'  , 0.0682417   ), Coef('Var'  , 0.0626873   ), Coef('Var'  , 0.0522908   ), Coef('Var'  , 0.0395885   ), Coef('Var'  , 0.0397754   ), Coef('Var'  , 0.037766    ), Coef('Var'  , 0.049413    ), Coef('Var'  , 0.0593485   ), Coef('Var'  , 0.0663813   ), ], 
		[Coef('Var'  , 0.0917446   ), Coef('Var'  , 0.083873    ), Coef('Var'  , 0.0734235   ), Coef('Var'  , 0.061388    ), Coef('Var'  , 0.0463152   ), Coef('Var'  , 0.0495402   ), Coef('Var'  , 0.0500756   ), Coef('Var'  , 0.0664301   ), Coef('Var'  , 0.0806045   ), Coef('Var'  , 0.087169    ), ], ])
	etat8.initMat[Chem([Sub('7')])] = FMat([
		[Coef('Var'  , 0.103336    ), Coef('Var'  , 0.100382    ), Coef('Var'  , 0.0997385   ), Coef('Var'  , 0.121533    ), Coef('Var'  , 0.145358    ), Coef('Var'  , 0.156623    ), Coef('Var'  , 0.17065     ), Coef('Var'  , 0.149963    ), Coef('Var'  , 0.132941    ), Coef('Var'  , 0.116486    ), ], 
		[Coef('Var'  , 0.120276    ), Coef('Var'  , 0.129598    ), Coef('Var'  , 0.14094     ), Coef('Var'  , 0.190985    ), Coef('Var'  , 0.243879    ), Coef('Var'  , 0.241886    ), Coef('Var'  , 0.243411    ), Coef('Var'  , 0.190113    ), Coef('Var'  , 0.140186    ), Coef('Var'  , 0.129051    ), ], 
		[Coef('Var'  , 0.104655    ), Coef('Var'  , 0.118305    ), Coef('Var'  , 0.13447     ), Coef('Var'  , 0.152165    ), Coef('Var'  , 0.172859    ), Coef('Var'  , 0.159442    ), Coef('Var'  , 0.148088    ), Coef('Var'  , 0.124657    ), Coef('Var'  , 0.102341    ), Coef('Var'  , 0.102826    ), ], 
		[Coef('Var'  , 0.108395    ), Coef('Var'  , 0.124966    ), Coef('Var'  , 0.143146    ), Coef('Var'  , 0.125495    ), Coef('Var'  , 0.11021     ), Coef('Var'  , 0.0855834   ), Coef('Var'  , 0.061341    ), Coef('Var'  , 0.0713826   ), Coef('Var'  , 0.0798792   ), Coef('Var'  , 0.0945331   ), ], 
		[Coef('Var'  , 0.0870332   ), Coef('Var'  , 0.0945227   ), Coef('Var'  , 0.102449    ), Coef('Var'  , 0.0869763   ), Coef('Var'  , 0.0724583   ), Coef('Var'  , 0.0578972   ), Coef('Var'  , 0.0434957   ), Coef('Var'  , 0.0531501   ), Coef('Var'  , 0.0620062   ), Coef('Var'  , 0.0748301   ), ], 
		[Coef('Var'  , 0.0949569   ), Coef('Var'  , 0.0893723   ), Coef('Var'  , 0.0817299   ), Coef('Var'  , 0.0669925   ), Coef('Var'  , 0.0503601   ), Coef('Var'  , 0.0505751   ), Coef('Var'  , 0.048148    ), Coef('Var'  , 0.0642827   ), Coef('Var'  , 0.0769676   ), Coef('Var'  , 0.0874882   ), ], 
		[Coef('Var'  , 0.0838747   ), Coef('Var'  , 0.0773665   ), Coef('Var'  , 0.0693933   ), Coef('Var'  , 0.0572779   ), Coef('Var'  , 0.0433427   ), Coef('Var'  , 0.0450814   ), Coef('Var'  , 0.04453     ), Coef('Var'  , 0.0591561   ), Coef('Var'  , 0.0713684   ), Coef('Var'  , 0.0785369   ), ], 
		[Coef('Var'  , 0.110029    ), Coef('Var'  , 0.101206    ), Coef('Var'  , 0.0881802   ), Coef('Var'  , 0.0754015   ), Coef('Var'  , 0.0578838   ), Coef('Var'  , 0.0629862   ), Coef('Var'  , 0.0635879   ), Coef('Var'  , 0.0836538   ), Coef('Var'  , 0.0995533   ), Coef('Var'  , 0.106721    ), ], 
		[Coef('Var'  , 0.0781207   ), Coef('Var'  , 0.0689184   ), Coef('Var'  , 0.0593485   ), Coef('Var'  , 0.0514331   ), Coef('Var'  , 0.0422767   ), Coef('Var'  , 0.0546188   ), Coef('Var'  , 0.0670075   ), Coef('Var'  , 0.0784546   ), Coef('Var'  , 0.0916255   ), Coef('Var'  , 0.0841192   ), ], 
		[Coef('Var'  , 0.109324    ), Coef('Var'  , 0.0953634   ), Coef('Var'  , 0.0806045   ), Coef('Var'  , 0.0717399   ), Coef('Var'  , 0.0613719   ), Coef('Var'  , 0.0853073   ), Coef('Var'  , 0.10974     ), Coef('Var'  , 0.125187    ), Coef('Var'  , 0.143131    ), Coef('Var'  , 0.125409    ), ], ])
	etat8.initMat[Chem([Sub('8')])] = FMat([
		[Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.210087    ), Coef('Var'  , 0.171767    ), Coef('Var'  , 0.169562    ), Coef('Var'  , 0.17065     ), Coef('Var'  , 0.209475    ), ], 
		[Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0532449   ), Coef('Var'  , 0.107635    ), Coef('Var'  , 0.174025    ), Coef('Var'  , 0.243411    ), Coef('Var'  , 0.37078     ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0370462   ), Coef('Var'  , 0.0741293   ), Coef('Var'  , 0.110752    ), Coef('Var'  , 0.148088    ), Coef('Var'  , 0.198706    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0255414   ), Coef('Var'  , 0.0498398   ), Coef('Var'  , 0.0564933   ), Coef('Var'  , 0.061341    ), Coef('Var'  , 0.0309519   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0187112   ), Coef('Var'  , 0.0368843   ), Coef('Var'  , 0.040593    ), Coef('Var'  , 0.0434957   ), Coef('Var'  , 0.0218818   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0251104   ), Coef('Var'  , 0.0485922   ), Coef('Var'  , 0.049985    ), Coef('Var'  , 0.048148    ), Coef('Var'  , 0.0248746   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0259031   ), Coef('Var'  , 0.0508273   ), Coef('Var'  , 0.0487977   ), Coef('Var'  , 0.04453     ), Coef('Var'  , 0.0228946   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0381892   ), Coef('Var'  , 0.074946    ), Coef('Var'  , 0.0710513   ), Coef('Var'  , 0.0635879   ), Coef('Var'  , 0.0328621   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.194585    ), Coef('Var'  , 0.140407    ), Coef('Var'  , 0.102805    ), Coef('Var'  , 0.0670075   ), Coef('Var'  , 0.0332198   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.371581    ), Coef('Var'  , 0.244973    ), Coef('Var'  , 0.175935    ), Coef('Var'  , 0.10974     ), Coef('Var'  , 0.0543543   ), ], ])
	etat8.initMat[Chem([Sub('9')])] = FMat([
		[Coef('Var'  , 0.0723757   ), Coef('Var'  , 0.0839777   ), Coef('Var'  , 0.0935089   ), Coef('Var'  , 0.100023    ), Coef('Var'  , 0.10616     ), Coef('Var'  , 0.0916902   ), Coef('Var'  , 0.0772633   ), Coef('Var'  , 0.0651156   ), Coef('Var'  , 0.0516837   ), Coef('Var'  , 0.0633448   ), ], 
		[Coef('Var'  , 0.0649822   ), Coef('Var'  , 0.0758237   ), Coef('Var'  , 0.0847807   ), Coef('Var'  , 0.0812044   ), Coef('Var'  , 0.0758294   ), Coef('Var'  , 0.0619413   ), Coef('Var'  , 0.0460881   ), Coef('Var'  , 0.0441106   ), Coef('Var'  , 0.0401489   ), Coef('Var'  , 0.0535592   ), ], 
		[Coef('Var'  , 0.0645535   ), Coef('Var'  , 0.071577    ), Coef('Var'  , 0.0773792   ), Coef('Var'  , 0.0719879   ), Coef('Var'  , 0.0652495   ), Coef('Var'  , 0.0538284   ), Coef('Var'  , 0.0405641   ), Coef('Var'  , 0.041345    ), Coef('Var'  , 0.0402      ), Coef('Var'  , 0.0532049   ), ], 
		[Coef('Var'  , 0.0784115   ), Coef('Var'  , 0.0846303   ), Coef('Var'  , 0.0892777   ), Coef('Var'  , 0.0817191   ), Coef('Var'  , 0.0717898   ), Coef('Var'  , 0.0601275   ), Coef('Var'  , 0.0454361   ), Coef('Var'  , 0.0483728   ), Coef('Var'  , 0.0487524   ), Coef('Var'  , 0.0644874   ), ], 
		[Coef('Var'  , 0.10286     ), Coef('Var'  , 0.0946331   ), Coef('Var'  , 0.0868745   ), Coef('Var'  , 0.0744866   ), Coef('Var'  , 0.0616911   ), Coef('Var'  , 0.0529327   ), Coef('Var'  , 0.0434975   ), Coef('Var'  , 0.0582338   ), Coef('Var'  , 0.0730021   ), Coef('Var'  , 0.0875536   ), ], 
		[Coef('Var'  , 0.147064    ), Coef('Var'  , 0.129985    ), Coef('Var'  , 0.113966    ), Coef('Var'  , 0.0997846   ), Coef('Var'  , 0.0843743   ), Coef('Var'  , 0.0747784   ), Coef('Var'  , 0.0635537   ), Coef('Var'  , 0.0877191   ), Coef('Var'  , 0.11225     ), Coef('Var'  , 0.128619    ), ], 
		[Coef('Var'  , 0.140897    ), Coef('Var'  , 0.125289    ), Coef('Var'  , 0.111646    ), Coef('Var'  , 0.109233    ), Coef('Var'  , 0.107888    ), Coef('Var'  , 0.129319    ), Coef('Var'  , 0.151706    ), Coef('Var'  , 0.16356     ), Coef('Var'  , 0.177113    ), Coef('Var'  , 0.157817    ), ], 
		[Coef('Var'  , 0.150503    ), Coef('Var'  , 0.142305    ), Coef('Var'  , 0.136657    ), Coef('Var'  , 0.14696     ), Coef('Var'  , 0.158828    ), Coef('Var'  , 0.206159    ), Coef('Var'  , 0.255239    ), Coef('Var'  , 0.251651    ), Coef('Var'  , 0.250747    ), Coef('Var'  , 0.198994    ), ], 
		[Coef('Var'  , 0.0971169   ), Coef('Var'  , 0.0956888   ), Coef('Var'  , 0.0960297   ), Coef('Var'  , 0.108859    ), Coef('Var'  , 0.125047    ), Coef('Var'  , 0.144164    ), Coef('Var'  , 0.167063    ), Coef('Var'  , 0.154614    ), Coef('Var'  , 0.144556    ), Coef('Var'  , 0.120212    ), ], 
		[Coef('Var'  , 0.0812361   ), Coef('Var'  , 0.0960901   ), Coef('Var'  , 0.10988     ), Coef('Var'  , 0.125743    ), Coef('Var'  , 0.143143    ), Coef('Var'  , 0.125059    ), Coef('Var'  , 0.10959     ), Coef('Var'  , 0.0852773   ), Coef('Var'  , 0.0615479   ), Coef('Var'  , 0.0722075   ), ], ])
	etat8.initMat[Chem([Sub('10')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.197149    ), Coef('Var'  , 0.145358    ), Coef('Var'  , 0.108043    ), Coef('Var'  , 0.0721628   ), Coef('Var'  , 0.0358944   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.371105    ), Coef('Var'  , 0.243879    ), Coef('Var'  , 0.174416    ), Coef('Var'  , 0.107659    ), Coef('Var'  , 0.0533101   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.210736    ), Coef('Var'  , 0.172859    ), Coef('Var'  , 0.17153     ), Coef('Var'  , 0.172923    ), Coef('Var'  , 0.210794    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0546315   ), Coef('Var'  , 0.11021     ), Coef('Var'  , 0.176793    ), Coef('Var'  , 0.245919    ), Coef('Var'  , 0.372161    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0360154   ), Coef('Var'  , 0.0724583   ), Coef('Var'  , 0.109685    ), Coef('Var'  , 0.148145    ), Coef('Var'  , 0.19867     ), Coef('Const', 0.25        ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0257004   ), Coef('Var'  , 0.0503601   ), Coef('Var'  , 0.056349    ), Coef('Var'  , 0.0610572   ), Coef('Var'  , 0.0306486   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0221868   ), Coef('Var'  , 0.0433427   ), Coef('Var'  , 0.0470117   ), Coef('Var'  , 0.0489977   ), Coef('Var'  , 0.0248249   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0301241   ), Coef('Var'  , 0.0578838   ), Coef('Var'  , 0.0587986   ), Coef('Var'  , 0.0552941   ), Coef('Var'  , 0.0286745   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.021399    ), Coef('Var'  , 0.0422767   ), Coef('Var'  , 0.040778    ), Coef('Var'  , 0.037766    ), Coef('Var'  , 0.019379    ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0309529   ), Coef('Var'  , 0.0613719   ), Coef('Var'  , 0.0565961   ), Coef('Var'  , 0.0500756   ), Coef('Var'  , 0.0256432   ), Coef('Const', 0           ), Coef('Const', 0           ), ], ])
	
	
	
	etat9.bords   = {Bord('0'): etat13, Bord('1'): etat13, Bord('2'): etat13, Bord('3'): etat13, Bord('4'): etat13, }
	etat9.permuts = {}
	etat9.interns = {Intern('_'): etat9, }
	etat9.subs    = {Sub('0'): etat1, Sub('1'): etat2, Sub('2'): etat3, Sub('3'): etat4, Sub('G', True): Etat.etatPoint, Sub('4'): etat5, Sub('5'): etat6, Sub('6'): etat7, Sub('7'): etat8, Sub('8'): etat10, Sub('9'): etat11, Sub('10'): etat12, }
	
	etat9.buildIntern()
	
	
	etat9.eqs = [
		(Chem([Bord('0'), Sub('0'), Permut('0'), ])	,	Chem([Sub('3'), Bord('2'), ])),
		(Chem([Bord('4'), Sub('1'), Permut('0'), ])	,	Chem([Sub('3'), Bord('3'), ])),
		(Chem([Bord('4'), Sub('0'), Permut('0'), ])	,	Chem([Sub('4'), Bord('1'), ])),
		(Chem([Bord('3'), Sub('1'), Permut('0'), ])	,	Chem([Sub('4'), Bord('2'), ])),
		(Chem([Bord('1'), Sub('0'), Permut('0'), ])	,	Chem([Sub('6'), Bord('3'), ])),
		(Chem([Bord('0'), Sub('1'), Permut('0'), ])	,	Chem([Sub('6'), Bord('4'), ])),
		(Chem([Bord('3'), Sub('0'), Permut('0'), ])	,	Chem([Sub('8'), Bord('3'), ])),
		(Chem([Bord('2'), Sub('1'), Permut('0'), ])	,	Chem([Sub('8'), Bord('4'), ])),
		(Chem([Bord('2'), Sub('0'), Permut('0'), ])	,	Chem([Sub('10'), Bord('1'), ])),
		(Chem([Bord('1'), Sub('1'), Permut('0'), ])	,	Chem([Sub('10'), Bord('2'), ])),
		(Chem([Sub('0'), Bord('0'), Bord('1'), ])	,	Chem([Sub('7'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('1'), Bord('1'), ])	,	Chem([Sub('10'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('2'), Bord('1'), ])	,	Chem([Sub('6'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('3'), Bord('1'), ])	,	Chem([Sub('5'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('4'), Bord('1'), ])	,	Chem([Sub('1'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('0'), Bord('1'), ])	,	Chem([Sub('9'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('1'), Bord('1'), ])	,	Chem([Sub('2'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('2'), Bord('1'), ])	,	Chem([Sub('7'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('4'), Bord('1'), ])	,	Chem([Sub('5'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('0'), Bord('1'), ])	,	Chem([Sub('8'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('1'), Bord('1'), ])	,	Chem([Sub('7'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('3'), Bord('1'), ])	,	Chem([Sub('9'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('4'), Bord('1'), ])	,	Chem([Sub('4'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('3'), Bord('0'), Bord('1'), ])	,	Chem([Sub('5'), Bord('4'), Bord('1'), ])),
		(Chem([Sub('3'), Bord('1'), Bord('1'), ])	,	Chem([Sub('6'), Bord('4'), Bord('1'), ])),
		(Chem([Sub('3'), Bord('3'), Bord('1'), ])	,	Chem([Sub('4'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('3'), Bord('4'), Bord('1'), ])	,	Chem([Sub('9'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('4'), Bord('2'), Bord('1'), ])	,	Chem([Sub('8'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('4'), Bord('4'), Bord('1'), ])	,	Chem([Sub('9'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('5'), Bord('0'), Bord('1'), ])	,	Chem([Sub('9'), Bord('4'), Bord('1'), ])),
		(Chem([Sub('5'), Bord('3'), Bord('1'), ])	,	Chem([Sub('6'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('6'), Bord('2'), Bord('1'), ])	,	Chem([Sub('10'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('7'), Bord('0'), Bord('1'), ])	,	Chem([Sub('10'), Bord('4'), Bord('1'), ])),
		(Chem([Sub('7'), Bord('4'), Bord('1'), ])	,	Chem([Sub('8'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('8'), Bord('4'), Bord('1'), ])	,	Chem([Sub('10'), Bord('0'), Bord('1'), ])),
		(Chem([Bord('0'), Bord('1'), ])	,	Chem([Bord('1'), Bord('0'), ])),
		(Chem([Bord('1'), Bord('1'), ])	,	Chem([Bord('2'), Bord('0'), ])),
		(Chem([Bord('2'), Bord('1'), ])	,	Chem([Bord('3'), Bord('0'), ])),
		(Chem([Bord('3'), Bord('1'), ])	,	Chem([Bord('4'), Bord('0'), ])),
		(Chem([Bord('4'), Bord('1'), ])	,	Chem([Bord('0'), Bord('0'), ])),
		]
	
	
	etat9.prim.elems = [Figure(2, [Chem([Bord('0'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('0'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('0'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('0'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('1'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('1'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('1'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('1'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('2'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('2'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('2'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('2'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('3'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('3'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('3'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('3'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('4'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('4'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('4'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('4'), Sub('1'), Sub('1'), Bord('0'), ]), ])]
	etat9.grid.elems = [
		Figure(1, [Chem([Bord('1'), Bord('0'), ]), Chem([Bord('1'), Intern(''), ]), Chem([Bord('1'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('4'), Bord('0'), ]), Chem([Bord('4'), Intern(''), ]), Chem([Bord('4'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('2'), Bord('0'), ]), Chem([Bord('2'), Intern(''), ]), Chem([Bord('2'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('0'), Bord('0'), ]), Chem([Bord('0'), Intern(''), ]), Chem([Bord('0'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('3'), Bord('0'), ]), Chem([Bord('3'), Intern(''), ]), Chem([Bord('3'), Bord('1'), ]), ]), ]
	
	
	etat9.space = [Chem([Bord('4'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('2'), Intern('0'), Intern('0'), ]), Chem([Bord('2'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('3'), Intern('0'), Intern('0'), ]), Chem([Bord('4'), Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('4'), Intern('0'), Intern('0'), ]), ]
	
	etat9.initMat[Chem([Sub('0')])] = FMat([
		[Coef('Var'  , 0.0898271   ), Coef('Var'  , 0.080451    ), Coef('Var'  , 0.069782    ), Coef('Var'  , 0.0609706   ), Coef('Var'  , 0.0499571   ), Coef('Var'  , 0.0629466   ), Coef('Var'  , 0.0749111   ), Coef('Var'  , 0.0884534   ), Coef('Var'  , 0.102517    ), Coef('Var'  , 0.0959639   ), ], 
		[Coef('Var'  , 0.104663    ), Coef('Var'  , 0.0910157   ), Coef('Var'  , 0.0770574   ), Coef('Var'  , 0.0674476   ), Coef('Var'  , 0.05722     ), Coef('Var'  , 0.0800261   ), Coef('Var'  , 0.104364    ), Coef('Var'  , 0.118704    ), Coef('Var'  , 0.136428    ), Coef('Var'  , 0.119437    ), ], 
		[Coef('Var'  , 0.113619    ), Coef('Var'  , 0.111208    ), Coef('Var'  , 0.109445    ), Coef('Var'  , 0.129625    ), Coef('Var'  , 0.150813    ), Coef('Var'  , 0.161319    ), Coef('Var'  , 0.174426    ), Coef('Var'  , 0.155298    ), Coef('Var'  , 0.139626    ), Coef('Var'  , 0.125537    ), ], 
		[Coef('Var'  , 0.117399    ), Coef('Var'  , 0.125712    ), Coef('Var'  , 0.137526    ), Coef('Var'  , 0.187932    ), Coef('Var'  , 0.242179    ), Coef('Var'  , 0.241017    ), Coef('Var'  , 0.243409    ), Coef('Var'  , 0.189874    ), Coef('Var'  , 0.139566    ), Coef('Var'  , 0.126921    ), ], 
		[Coef('Var'  , 0.105855    ), Coef('Var'  , 0.117913    ), Coef('Var'  , 0.132775    ), Coef('Var'  , 0.150771    ), Coef('Var'  , 0.172088    ), Coef('Var'  , 0.160207    ), Coef('Var'  , 0.150238    ), Coef('Var'  , 0.127812    ), Coef('Var'  , 0.106019    ), Coef('Var'  , 0.105377    ), ], 
		[Coef('Var'  , 0.0959332   ), Coef('Var'  , 0.111967    ), Coef('Var'  , 0.130818    ), Coef('Var'  , 0.115       ), Coef('Var'  , 0.102557    ), Coef('Var'  , 0.0785984   ), Coef('Var'  , 0.0555395   ), Coef('Var'  , 0.0638908   ), Coef('Var'  , 0.0711132   ), Coef('Var'  , 0.083516    ), ], 
		[Coef('Var'  , 0.100807    ), Coef('Var'  , 0.108865    ), Coef('Var'  , 0.115861    ), Coef('Var'  , 0.0995612   ), Coef('Var'  , 0.0824724   ), Coef('Var'  , 0.0680618   ), Coef('Var'  , 0.0524112   ), Coef('Var'  , 0.0641201   ), Coef('Var'  , 0.0739687   ), Coef('Var'  , 0.0882563   ), ], 
		[Coef('Var'  , 0.0854966   ), Coef('Var'  , 0.0806135   ), Coef('Var'  , 0.0742819   ), Coef('Var'  , 0.0609535   ), Coef('Var'  , 0.0460864   ), Coef('Var'  , 0.0460823   ), Coef('Var'  , 0.0437426   ), Coef('Var'  , 0.0580463   ), Coef('Var'  , 0.069396    ), Coef('Var'  , 0.0786281   ), ], 
		[Coef('Var'  , 0.0920159   ), Coef('Var'  , 0.0861217   ), Coef('Var'  , 0.0776343   ), Coef('Var'  , 0.0651343   ), Coef('Var'  , 0.0494939   ), Coef('Var'  , 0.0510524   ), Coef('Var'  , 0.0494594   ), Coef('Var'  , 0.0651928   ), Coef('Var'  , 0.0780399   ), Coef('Var'  , 0.0862654   ), ], 
		[Coef('Var'  , 0.0943835   ), Coef('Var'  , 0.0861319   ), Coef('Var'  , 0.0748199   ), Coef('Var'  , 0.0626045   ), Coef('Var'  , 0.0471337   ), Coef('Var'  , 0.0506894   ), Coef('Var'  , 0.0514992   ), Coef('Var'  , 0.0686087   ), Coef('Var'  , 0.0833254   ), Coef('Var'  , 0.0900976   ), ], ])
	etat9.initMat[Chem([Sub('1')])] = FMat([
		[Coef('Var'  , 0.103777    ), Coef('Var'  , 0.102525    ), Coef('Var'  , 0.103678    ), Coef('Var'  , 0.0961516   ), Coef('Var'  , 0.0897994   ), Coef('Var'  , 0.0863879   ), Coef('Var'  , 0.0821167   ), Coef('Var'  , 0.0864292   ), Coef('Var'  , 0.0898271   ), Coef('Var'  , 0.0962693   ), ], 
		[Coef('Var'  , 0.117137    ), Coef('Var'  , 0.110834    ), Coef('Var'  , 0.106007    ), Coef('Var'  , 0.100222    ), Coef('Var'  , 0.0928226   ), Coef('Var'  , 0.093887    ), Coef('Var'  , 0.091725    ), Coef('Var'  , 0.0987799   ), Coef('Var'  , 0.104663    ), Coef('Var'  , 0.110047    ), ], 
		[Coef('Var'  , 0.113146    ), Coef('Var'  , 0.104906    ), Coef('Var'  , 0.0968451   ), Coef('Var'  , 0.0932196   ), Coef('Var'  , 0.088112    ), Coef('Var'  , 0.093844    ), Coef('Var'  , 0.0978456   ), Coef('Var'  , 0.105824    ), Coef('Var'  , 0.113619    ), Coef('Var'  , 0.112848    ), ], 
		[Coef('Var'  , 0.105208    ), Coef('Var'  , 0.0975186   ), Coef('Var'  , 0.0892517   ), Coef('Var'  , 0.089867    ), Coef('Var'  , 0.0885688   ), Coef('Var'  , 0.0962941   ), Coef('Var'  , 0.103715    ), Coef('Var'  , 0.10947     ), Coef('Var'  , 0.117399    ), Coef('Var'  , 0.11032     ), ], 
		[Coef('Var'  , 0.0924137   ), Coef('Var'  , 0.0878054   ), Coef('Var'  , 0.0818232   ), Coef('Var'  , 0.08476     ), Coef('Var'  , 0.0868628   ), Coef('Var'  , 0.0939093   ), Coef('Var'  , 0.10236     ), Coef('Var'  , 0.102989    ), Coef('Var'  , 0.105855    ), Coef('Var'  , 0.0988797   ), ], 
		[Coef('Var'  , 0.0809729   ), Coef('Var'  , 0.0823266   ), Coef('Var'  , 0.082041    ), Coef('Var'  , 0.0898296   ), Coef('Var'  , 0.0974045   ), Coef('Var'  , 0.101958    ), Coef('Var'  , 0.109022    ), Coef('Var'  , 0.101179    ), Coef('Var'  , 0.0959332   ), Coef('Var'  , 0.088467    ), ], 
		[Coef('Var'  , 0.0869584   ), Coef('Var'  , 0.0914408   ), Coef('Var'  , 0.0952921   ), Coef('Var'  , 0.105145    ), Coef('Var'  , 0.115741    ), Coef('Var'  , 0.117068    ), Coef('Var'  , 0.119239    ), Coef('Var'  , 0.110284    ), Coef('Var'  , 0.100807    ), Coef('Var'  , 0.0945816   ), ], 
		[Coef('Var'  , 0.0869906   ), Coef('Var'  , 0.0958778   ), Coef('Var'  , 0.104082    ), Coef('Var'  , 0.10957     ), Coef('Var'  , 0.116745    ), Coef('Var'  , 0.108557    ), Coef('Var'  , 0.102195    ), Coef('Var'  , 0.09403     ), Coef('Var'  , 0.0854966   ), Coef('Var'  , 0.0871588   ), ], 
		[Coef('Var'  , 0.101101    ), Coef('Var'  , 0.108645    ), Coef('Var'  , 0.11625     ), Coef('Var'  , 0.114796    ), Coef('Var'  , 0.114735    ), Coef('Var'  , 0.106647    ), Coef('Var'  , 0.099146    ), Coef('Var'  , 0.0962475   ), Coef('Var'  , 0.0920159   ), Coef('Var'  , 0.0973611   ), ], 
		[Coef('Var'  , 0.112296    ), Coef('Var'  , 0.118121    ), Coef('Var'  , 0.124729    ), Coef('Var'  , 0.116439    ), Coef('Var'  , 0.109209    ), Coef('Var'  , 0.101448    ), Coef('Var'  , 0.0926354   ), Coef('Var'  , 0.0947676   ), Coef('Var'  , 0.0943835   ), Coef('Var'  , 0.104068    ), ], ])
	etat9.initMat[Chem([Sub('2')])] = FMat([
		[Coef('Var'  , 0.0751973   ), Coef('Var'  , 0.0634832   ), Coef('Var'  , 0.0505369   ), Coef('Var'  , 0.0615851   ), Coef('Var'  , 0.0702031   ), Coef('Var'  , 0.0806618   ), Coef('Var'  , 0.0897994   ), Coef('Var'  , 0.095875    ), Coef('Var'  , 0.102475    ), Coef('Var'  , 0.0885801   ), ], 
		[Coef('Var'  , 0.0492486   ), Coef('Var'  , 0.0501907   ), Coef('Var'  , 0.0482054   ), Coef('Var'  , 0.0644416   ), Coef('Var'  , 0.0764145   ), Coef('Var'  , 0.0866785   ), Coef('Var'  , 0.0928226   ), Coef('Var'  , 0.0874166   ), Coef('Var'  , 0.0792654   ), Coef('Var'  , 0.065302    ), ], 
		[Coef('Var'  , 0.0443822   ), Coef('Var'  , 0.0455711   ), Coef('Var'  , 0.0448676   ), Coef('Var'  , 0.0603551   ), Coef('Var'  , 0.0736385   ), Coef('Var'  , 0.0820161   ), Coef('Var'  , 0.088112    ), Coef('Var'  , 0.0813977   ), Coef('Var'  , 0.0726257   ), Coef('Var'  , 0.0594484   ), ], 
		[Coef('Var'  , 0.0475288   ), Coef('Var'  , 0.0502832   ), Coef('Var'  , 0.0497268   ), Coef('Var'  , 0.0648739   ), Coef('Var'  , 0.0777156   ), Coef('Var'  , 0.0840537   ), Coef('Var'  , 0.0885688   ), Coef('Var'  , 0.0823019   ), Coef('Var'  , 0.0732462   ), Coef('Var'  , 0.0622729   ), ], 
		[Coef('Var'  , 0.0462838   ), Coef('Var'  , 0.0583126   ), Coef('Var'  , 0.0703999   ), Coef('Var'  , 0.0833041   ), Coef('Var'  , 0.0979458   ), Coef('Var'  , 0.0917949   ), Coef('Var'  , 0.0868628   ), Coef('Var'  , 0.0772186   ), Coef('Var'  , 0.0667347   ), Coef('Var'  , 0.057267    ), ], 
		[Coef('Var'  , 0.0580422   ), Coef('Var'  , 0.0807401   ), Coef('Var'  , 0.103845    ), Coef('Var'  , 0.116138    ), Coef('Var'  , 0.13169     ), Coef('Var'  , 0.11318     ), Coef('Var'  , 0.0974045   ), Coef('Var'  , 0.08585     ), Coef('Var'  , 0.0738669   ), Coef('Var'  , 0.0668827   ), ], 
		[Coef('Var'  , 0.152447    ), Coef('Var'  , 0.165515    ), Coef('Var'  , 0.180154    ), Coef('Var'  , 0.162354    ), Coef('Var'  , 0.146551    ), Coef('Var'  , 0.130302    ), Coef('Var'  , 0.115741    ), Coef('Var'  , 0.11164     ), Coef('Var'  , 0.108745    ), Coef('Var'  , 0.130033    ), ], 
		[Coef('Var'  , 0.241981    ), Coef('Var'  , 0.239998    ), Coef('Var'  , 0.241771    ), Coef('Var'  , 0.187848    ), Coef('Var'  , 0.137392    ), Coef('Var'  , 0.125568    ), Coef('Var'  , 0.116745    ), Coef('Var'  , 0.125804    ), Coef('Var'  , 0.137996    ), Coef('Var'  , 0.188143    ), ], 
		[Coef('Var'  , 0.177272    ), Coef('Var'  , 0.163273    ), Coef('Var'  , 0.151485    ), Coef('Var'  , 0.129537    ), Coef('Var'  , 0.1092      ), Coef('Var'  , 0.1112      ), Coef('Var'  , 0.114735    ), Coef('Var'  , 0.127789    ), Coef('Var'  , 0.143006    ), Coef('Var'  , 0.158814    ), ], 
		[Coef('Var'  , 0.107617    ), Coef('Var'  , 0.082633    ), Coef('Var'  , 0.0590095   ), Coef('Var'  , 0.0695632   ), Coef('Var'  , 0.0792503   ), Coef('Var'  , 0.0945459   ), Coef('Var'  , 0.109209    ), Coef('Var'  , 0.124707    ), Coef('Var'  , 0.142039    ), Coef('Var'  , 0.123257    ), ], ])
	etat9.initMat[Chem([Sub('3')])] = FMat([
		[Coef('Var'  , 0.170697    ), Coef('Var'  , 0.168988    ), Coef('Var'  , 0.170682    ), Coef('Var'  , 0.20949     ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.209498    ), ], 
		[Coef('Var'  , 0.104202    ), Coef('Var'  , 0.169573    ), Coef('Var'  , 0.239032    ), Coef('Var'  , 0.368323    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0512494   ), ], 
		[Coef('Var'  , 0.0776403   ), Coef('Var'  , 0.114033    ), Coef('Var'  , 0.151073    ), Coef('Var'  , 0.200196    ), Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0388366   ), ], 
		[Coef('Var'  , 0.0503363   ), Coef('Var'  , 0.056703    ), Coef('Var'  , 0.0610488   ), Coef('Var'  , 0.0308491   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0258539   ), ], 
		[Coef('Var'  , 0.0449264   ), Coef('Var'  , 0.0495625   ), Coef('Var'  , 0.0515663   ), Coef('Var'  , 0.0263921   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0231704   ), ], 
		[Coef('Var'  , 0.0434228   ), Coef('Var'  , 0.0446625   ), Coef('Var'  , 0.0427303   ), Coef('Var'  , 0.0221301   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0225324   ), ], 
		[Coef('Var'  , 0.0486786   ), Coef('Var'  , 0.0463117   ), Coef('Var'  , 0.0427146   ), Coef('Var'  , 0.0217215   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0245901   ), ], 
		[Coef('Var'  , 0.0603159   ), Coef('Var'  , 0.0558762   ), Coef('Var'  , 0.0492847   ), Coef('Var'  , 0.0253586   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0305176   ), ], 
		[Coef('Var'  , 0.153861    ), Coef('Var'  , 0.116984    ), Coef('Var'  , 0.0805599   ), Coef('Var'  , 0.0403334   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.20165     ), ], 
		[Coef('Var'  , 0.245919    ), Coef('Var'  , 0.177308    ), Coef('Var'  , 0.111308    ), Coef('Var'  , 0.0552062   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.372101    ), ], ])
	etat9.initMat[Chem([Sub('G')])] = FMat([
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
	etat9.initMat[Chem([Sub('4')])] = FMat([
		[Coef('Var'  , 0.147581    ), Coef('Var'  , 0.198408    ), Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0376325   ), Coef('Var'  , 0.0751973   ), Coef('Var'  , 0.11104     ), ], 
		[Coef('Var'  , 0.0584658   ), Coef('Var'  , 0.0292802   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0251565   ), Coef('Var'  , 0.0492486   ), Coef('Var'  , 0.0544367   ), ], 
		[Coef('Var'  , 0.0504659   ), Coef('Var'  , 0.025583    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0226414   ), Coef('Var'  , 0.0443822   ), Coef('Var'  , 0.0482244   ), ], 
		[Coef('Var'  , 0.0476123   ), Coef('Var'  , 0.0247447   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.024717    ), Coef('Var'  , 0.0475288   ), Coef('Var'  , 0.0494617   ), ], 
		[Coef('Var'  , 0.042314    ), Coef('Var'  , 0.0217139   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0234259   ), Coef('Var'  , 0.0462838   ), Coef('Var'  , 0.0451398   ), ], 
		[Coef('Var'  , 0.0474798   ), Coef('Var'  , 0.0244875   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0294076   ), Coef('Var'  , 0.0580422   ), Coef('Var'  , 0.0538951   ), ], 
		[Coef('Var'  , 0.0770261   ), Coef('Var'  , 0.0384438   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.200928    ), Coef('Var'  , 0.152447    ), Coef('Var'  , 0.114371    ), ], 
		[Coef('Var'  , 0.107225    ), Coef('Var'  , 0.0530532   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.370028    ), Coef('Var'  , 0.241981    ), Coef('Var'  , 0.173081    ), ], 
		[Coef('Var'  , 0.177927    ), Coef('Var'  , 0.21335     ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.212981    ), Coef('Var'  , 0.177272    ), Coef('Var'  , 0.176331    ), ], 
		[Coef('Var'  , 0.243903    ), Coef('Var'  , 0.370936    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0530828   ), Coef('Var'  , 0.107617    ), Coef('Var'  , 0.174018    ), ], ])
	etat9.initMat[Chem([Sub('5')])] = FMat([
		[Coef('Var'  , 0.170682    ), Coef('Var'  , 0.149393    ), Coef('Var'  , 0.131858    ), Coef('Var'  , 0.116203    ), Coef('Var'  , 0.103777    ), Coef('Var'  , 0.102296    ), Coef('Var'  , 0.102517    ), Coef('Var'  , 0.124366    ), Coef('Var'  , 0.14751     ), Coef('Var'  , 0.157861    ), ], 
		[Coef('Var'  , 0.239032    ), Coef('Var'  , 0.185502    ), Coef('Var'  , 0.136378    ), Coef('Var'  , 0.125061    ), Coef('Var'  , 0.117137    ), Coef('Var'  , 0.125156    ), Coef('Var'  , 0.136428    ), Coef('Var'  , 0.185823    ), Coef('Var'  , 0.239329    ), Coef('Var'  , 0.236873    ), ], 
		[Coef('Var'  , 0.151073    ), Coef('Var'  , 0.129625    ), Coef('Var'  , 0.109061    ), Coef('Var'  , 0.110706    ), Coef('Var'  , 0.113146    ), Coef('Var'  , 0.125243    ), Coef('Var'  , 0.139626    ), Coef('Var'  , 0.15542     ), Coef('Var'  , 0.174598    ), Coef('Var'  , 0.16165     ), ], 
		[Coef('Var'  , 0.0610488   ), Coef('Var'  , 0.0707919   ), Coef('Var'  , 0.0789247   ), Coef('Var'  , 0.0923404   ), Coef('Var'  , 0.105208    ), Coef('Var'  , 0.121396    ), Coef('Var'  , 0.139566    ), Coef('Var'  , 0.122904    ), Coef('Var'  , 0.108688    ), Coef('Var'  , 0.0847546   ), ], 
		[Coef('Var'  , 0.0515663   ), Coef('Var'  , 0.0628098   ), Coef('Var'  , 0.0714023   ), Coef('Var'  , 0.0828406   ), Coef('Var'  , 0.0924137   ), Coef('Var'  , 0.0993432   ), Coef('Var'  , 0.106019    ), Coef('Var'  , 0.0918944   ), Coef('Var'  , 0.0776479   ), Coef('Var'  , 0.0653662   ), ], 
		[Coef('Var'  , 0.0427303   ), Coef('Var'  , 0.0561352   ), Coef('Var'  , 0.0664671   ), Coef('Var'  , 0.0748768   ), Coef('Var'  , 0.0809729   ), Coef('Var'  , 0.0767925   ), Coef('Var'  , 0.0711132   ), Coef('Var'  , 0.0590355   ), Coef('Var'  , 0.0451023   ), Coef('Var'  , 0.0452448   ), ], 
		[Coef('Var'  , 0.0427146   ), Coef('Var'  , 0.0570499   ), Coef('Var'  , 0.0700468   ), Coef('Var'  , 0.0791589   ), Coef('Var'  , 0.0869584   ), Coef('Var'  , 0.0813358   ), Coef('Var'  , 0.0739687   ), Coef('Var'  , 0.0602605   ), Coef('Var'  , 0.0446193   ), Coef('Var'  , 0.0444767   ), ], 
		[Coef('Var'  , 0.0492847   ), Coef('Var'  , 0.0649522   ), Coef('Var'  , 0.0780317   ), Coef('Var'  , 0.0835905   ), Coef('Var'  , 0.0869906   ), Coef('Var'  , 0.0794629   ), Coef('Var'  , 0.069396    ), Coef('Var'  , 0.0585956   ), Coef('Var'  , 0.0446851   ), Coef('Var'  , 0.0484881   ), ], 
		[Coef('Var'  , 0.0805599   ), Coef('Var'  , 0.0964506   ), Coef('Var'  , 0.112436    ), Coef('Var'  , 0.106922    ), Coef('Var'  , 0.101101    ), Coef('Var'  , 0.0905142   ), Coef('Var'  , 0.0780399   ), Coef('Var'  , 0.0676541   ), Coef('Var'  , 0.0548088   ), Coef('Var'  , 0.0682782   ), ], 
		[Coef('Var'  , 0.111308    ), Coef('Var'  , 0.127291    ), Coef('Var'  , 0.145394    ), Coef('Var'  , 0.1283      ), Coef('Var'  , 0.112296    ), Coef('Var'  , 0.0984598   ), Coef('Var'  , 0.0833254   ), Coef('Var'  , 0.074046    ), Coef('Var'  , 0.0630119   ), Coef('Var'  , 0.0870074   ), ], ])
	etat9.initMat[Chem([Sub('6')])] = FMat([
		[Coef('Const', 0.25        ), Coef('Var'  , 0.198371    ), Coef('Var'  , 0.14751     ), Coef('Var'  , 0.110829    ), Coef('Var'  , 0.0749111   ), Coef('Var'  , 0.0374582   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.5         ), Coef('Var'  , 0.36855     ), Coef('Var'  , 0.239329    ), Coef('Var'  , 0.16998     ), Coef('Var'  , 0.104364    ), Coef('Var'  , 0.0514302   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0.25        ), Coef('Var'  , 0.211454    ), Coef('Var'  , 0.174598    ), Coef('Var'  , 0.172785    ), Coef('Var'  , 0.174426    ), Coef('Var'  , 0.211331    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0539055   ), Coef('Var'  , 0.108688    ), Coef('Var'  , 0.174781    ), Coef('Var'  , 0.243409    ), Coef('Var'  , 0.370876    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.038974    ), Coef('Var'  , 0.0776479   ), Coef('Var'  , 0.113866    ), Coef('Var'  , 0.150238    ), Coef('Var'  , 0.199892    ), Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0231147   ), Coef('Var'  , 0.0451023   ), Coef('Var'  , 0.0510848   ), Coef('Var'  , 0.0555395   ), Coef('Var'  , 0.0279701   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0227552   ), Coef('Var'  , 0.0446193   ), Coef('Var'  , 0.04937     ), Coef('Var'  , 0.0524112   ), Coef('Var'  , 0.0266148   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0231295   ), Coef('Var'  , 0.0446851   ), Coef('Var'  , 0.0457098   ), Coef('Var'  , 0.0437426   ), Coef('Var'  , 0.0225803   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0279448   ), Coef('Var'  , 0.0548088   ), Coef('Var'  , 0.0534284   ), Coef('Var'  , 0.0494594   ), Coef('Var'  , 0.0254836   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0318012   ), Coef('Var'  , 0.0630119   ), Coef('Var'  , 0.0581651   ), Coef('Var'  , 0.0514992   ), Coef('Var'  , 0.0263639   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], ])
	etat9.initMat[Chem([Sub('7')])] = FMat([
		[Coef('Var'  , 0.0452119   ), Coef('Var'  , 0.0465143   ), Coef('Var'  , 0.0448623   ), Coef('Var'  , 0.058631    ), Coef('Var'  , 0.069782    ), Coef('Var'  , 0.0769428   ), Coef('Var'  , 0.0821167   ), Coef('Var'  , 0.0771949   ), Coef('Var'  , 0.0702031   ), Coef('Var'  , 0.0590999   ), ], 
		[Coef('Var'  , 0.0477556   ), Coef('Var'  , 0.049032    ), Coef('Var'  , 0.0476883   ), Coef('Var'  , 0.0631095   ), Coef('Var'  , 0.0770574   ), Coef('Var'  , 0.0854676   ), Coef('Var'  , 0.091725    ), Coef('Var'  , 0.0860233   ), Coef('Var'  , 0.0764145   ), Coef('Var'  , 0.0641816   ), ], 
		[Coef('Var'  , 0.0510106   ), Coef('Var'  , 0.0646555   ), Coef('Var'  , 0.0776105   ), Coef('Var'  , 0.0934051   ), Coef('Var'  , 0.109445    ), Coef('Var'  , 0.103891    ), Coef('Var'  , 0.0978456   ), Coef('Var'  , 0.0866787   ), Coef('Var'  , 0.0736385   ), Coef('Var'  , 0.0633134   ), ], 
		[Coef('Var'  , 0.0598482   ), Coef('Var'  , 0.082991    ), Coef('Var'  , 0.106784    ), Coef('Var'  , 0.120577    ), Coef('Var'  , 0.137526    ), Coef('Var'  , 0.119338    ), Coef('Var'  , 0.103715    ), Coef('Var'  , 0.0908558   ), Coef('Var'  , 0.0777156   ), Coef('Var'  , 0.0695118   ), ], 
		[Coef('Var'  , 0.143943    ), Coef('Var'  , 0.155683    ), Coef('Var'  , 0.170371    ), Coef('Var'  , 0.149798    ), Coef('Var'  , 0.132775    ), Coef('Var'  , 0.115988    ), Coef('Var'  , 0.10236     ), Coef('Var'  , 0.0989492   ), Coef('Var'  , 0.0979458   ), Coef('Var'  , 0.119759    ), ], 
		[Coef('Var'  , 0.238022    ), Coef('Var'  , 0.235696    ), Coef('Var'  , 0.237552    ), Coef('Var'  , 0.182101    ), Coef('Var'  , 0.130818    ), Coef('Var'  , 0.117955    ), Coef('Var'  , 0.109022    ), Coef('Var'  , 0.118389    ), Coef('Var'  , 0.13169     ), Coef('Var'  , 0.182772    ), ], 
		[Coef('Var'  , 0.181404    ), Coef('Var'  , 0.168903    ), Coef('Var'  , 0.157315    ), Coef('Var'  , 0.136742    ), Coef('Var'  , 0.115861    ), Coef('Var'  , 0.117647    ), Coef('Var'  , 0.119239    ), Coef('Var'  , 0.132299    ), Coef('Var'  , 0.146551    ), Coef('Var'  , 0.163042    ), ], 
		[Coef('Var'  , 0.106129    ), Coef('Var'  , 0.0812108   ), Coef('Var'  , 0.0571745   ), Coef('Var'  , 0.0661644   ), Coef('Var'  , 0.0742819   ), Coef('Var'  , 0.0883195   ), Coef('Var'  , 0.102195    ), Coef('Var'  , 0.118747    ), Coef('Var'  , 0.137392    ), Coef('Var'  , 0.120377    ), ], 
		[Coef('Var'  , 0.0783514   ), Coef('Var'  , 0.0668728   ), Coef('Var'  , 0.0543561   ), Coef('Var'  , 0.0673444   ), Coef('Var'  , 0.0776343   ), Coef('Var'  , 0.0892568   ), Coef('Var'  , 0.099146    ), Coef('Var'  , 0.103935    ), Coef('Var'  , 0.1092      ), Coef('Var'  , 0.0933381   ), ], 
		[Coef('Var'  , 0.0483252   ), Coef('Var'  , 0.0484413   ), Coef('Var'  , 0.0462869   ), Coef('Var'  , 0.0621273   ), Coef('Var'  , 0.0748199   ), Coef('Var'  , 0.0851937   ), Coef('Var'  , 0.0926354   ), Coef('Var'  , 0.0869278   ), Coef('Var'  , 0.0792503   ), Coef('Var'  , 0.0646061   ), ], ])
	etat9.initMat[Chem([Sub('8')])] = FMat([
		[Coef('Const', 0           ), Coef('Var'  , 0.0233656   ), Coef('Var'  , 0.0452119   ), Coef('Var'  , 0.0492163   ), Coef('Var'  , 0.0505369   ), Coef('Var'  , 0.0258507   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0247742   ), Coef('Var'  , 0.0477556   ), Coef('Var'  , 0.0498084   ), Coef('Var'  , 0.0482054   ), Coef('Var'  , 0.0250342   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0258879   ), Coef('Var'  , 0.0510106   ), Coef('Var'  , 0.0488177   ), Coef('Var'  , 0.0448676   ), Coef('Var'  , 0.0229297   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0302041   ), Coef('Var'  , 0.0598482   ), Coef('Var'  , 0.0557703   ), Coef('Var'  , 0.0497268   ), Coef('Var'  , 0.0255662   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.25        ), Coef('Var'  , 0.196341    ), Coef('Var'  , 0.143943    ), Coef('Var'  , 0.106228    ), Coef('Var'  , 0.0703999   ), Coef('Var'  , 0.0348867   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.5         ), Coef('Var'  , 0.367967    ), Coef('Var'  , 0.238022    ), Coef('Var'  , 0.169299    ), Coef('Var'  , 0.103845    ), Coef('Var'  , 0.0513325   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0.25        ), Coef('Var'  , 0.215275    ), Coef('Var'  , 0.181404    ), Coef('Var'  , 0.179863    ), Coef('Var'  , 0.180154    ), Coef('Var'  , 0.214588    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0524979   ), Coef('Var'  , 0.106129    ), Coef('Var'  , 0.172468    ), Coef('Var'  , 0.241771    ), Coef('Var'  , 0.36997     ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0390939   ), Coef('Var'  , 0.0783514   ), Coef('Var'  , 0.114386    ), Coef('Var'  , 0.151485    ), Coef('Var'  , 0.200292    ), Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.024593    ), Coef('Var'  , 0.0483252   ), Coef('Var'  , 0.0541431   ), Coef('Var'  , 0.0590095   ), Coef('Var'  , 0.0295502   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], ])
	etat9.initMat[Chem([Sub('9')])] = FMat([
		[Coef('Var'  , 0.131858    ), Coef('Var'  , 0.1494      ), Coef('Var'  , 0.170697    ), Coef('Var'  , 0.157905    ), Coef('Var'  , 0.147581    ), Coef('Var'  , 0.124355    ), Coef('Var'  , 0.102475    ), Coef('Var'  , 0.102172    ), Coef('Var'  , 0.103678    ), Coef('Var'  , 0.116127    ), ], 
		[Coef('Var'  , 0.136378    ), Coef('Var'  , 0.118428    ), Coef('Var'  , 0.104202    ), Coef('Var'  , 0.0805296   ), Coef('Var'  , 0.0584658   ), Coef('Var'  , 0.0694257   ), Coef('Var'  , 0.0792654   ), Coef('Var'  , 0.0930964   ), Coef('Var'  , 0.106007    ), Coef('Var'  , 0.120129    ), ], 
		[Coef('Var'  , 0.109061    ), Coef('Var'  , 0.0932658   ), Coef('Var'  , 0.0776403   ), Coef('Var'  , 0.0644197   ), Coef('Var'  , 0.0504659   ), Coef('Var'  , 0.06239     ), Coef('Var'  , 0.0726257   ), Coef('Var'  , 0.0854359   ), Coef('Var'  , 0.0968451   ), Coef('Var'  , 0.103058    ), ], 
		[Coef('Var'  , 0.0789247   ), Coef('Var'  , 0.0657967   ), Coef('Var'  , 0.0503363   ), Coef('Var'  , 0.0505986   ), Coef('Var'  , 0.0476123   ), Coef('Var'  , 0.0623006   ), Coef('Var'  , 0.0732462   ), Coef('Var'  , 0.0826769   ), Coef('Var'  , 0.0892517   ), Coef('Var'  , 0.0850638   ), ], 
		[Coef('Var'  , 0.0714023   ), Coef('Var'  , 0.0595881   ), Coef('Var'  , 0.0449264   ), Coef('Var'  , 0.0448843   ), Coef('Var'  , 0.042314    ), Coef('Var'  , 0.055555    ), Coef('Var'  , 0.0667347   ), Coef('Var'  , 0.0752236   ), Coef('Var'  , 0.0818232   ), Coef('Var'  , 0.0778002   ), ], 
		[Coef('Var'  , 0.0664671   ), Coef('Var'  , 0.0565375   ), Coef('Var'  , 0.0434228   ), Coef('Var'  , 0.0470199   ), Coef('Var'  , 0.0474798   ), Coef('Var'  , 0.0619627   ), Coef('Var'  , 0.0738669   ), Coef('Var'  , 0.07893     ), Coef('Var'  , 0.082041    ), Coef('Var'  , 0.0754599   ), ], 
		[Coef('Var'  , 0.0700468   ), Coef('Var'  , 0.0599185   ), Coef('Var'  , 0.0486786   ), Coef('Var'  , 0.063034    ), Coef('Var'  , 0.0770261   ), Coef('Var'  , 0.0925488   ), Coef('Var'  , 0.108745    ), Coef('Var'  , 0.101715    ), Coef('Var'  , 0.0952921   ), Coef('Var'  , 0.0829386   ), ], 
		[Coef('Var'  , 0.0780317   ), Coef('Var'  , 0.0701113   ), Coef('Var'  , 0.0603159   ), Coef('Var'  , 0.0835709   ), Coef('Var'  , 0.107225    ), Coef('Var'  , 0.121169    ), Coef('Var'  , 0.137996    ), Coef('Var'  , 0.119996    ), Coef('Var'  , 0.104082    ), Coef('Var'  , 0.0914746   ), ], 
		[Coef('Var'  , 0.112436    ), Coef('Var'  , 0.132768    ), Coef('Var'  , 0.153861    ), Coef('Var'  , 0.165001    ), Coef('Var'  , 0.177927    ), Coef('Var'  , 0.159184    ), Coef('Var'  , 0.143006    ), Coef('Var'  , 0.128674    ), Coef('Var'  , 0.11625     ), Coef('Var'  , 0.113958    ), ], 
		[Coef('Var'  , 0.145394    ), Coef('Var'  , 0.194186    ), Coef('Var'  , 0.245919    ), Coef('Var'  , 0.243037    ), Coef('Var'  , 0.243903    ), Coef('Var'  , 0.19111     ), Coef('Var'  , 0.142039    ), Coef('Var'  , 0.13208     ), Coef('Var'  , 0.124729    ), Coef('Var'  , 0.133991    ), ], ])
	etat9.initMat[Chem([Sub('10')])] = FMat([
		[Coef('Var'  , 0.0448623   ), Coef('Var'  , 0.0231487   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0254884   ), Coef('Var'  , 0.0499571   ), Coef('Var'  , 0.0486371   ), ], 
		[Coef('Var'  , 0.0476883   ), Coef('Var'  , 0.0242578   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0285959   ), Coef('Var'  , 0.05722     ), Coef('Var'  , 0.0528537   ), ], 
		[Coef('Var'  , 0.0776105   ), Coef('Var'  , 0.0387676   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.199988    ), Coef('Var'  , 0.150813    ), Coef('Var'  , 0.113756    ), ], 
		[Coef('Var'  , 0.106784    ), Coef('Var'  , 0.0527869   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.370142    ), Coef('Var'  , 0.242179    ), Coef('Var'  , 0.172929    ), ], 
		[Coef('Var'  , 0.170371    ), Coef('Var'  , 0.209342    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.210315    ), Coef('Var'  , 0.172088    ), Coef('Var'  , 0.169656    ), ], 
		[Coef('Var'  , 0.237552    ), Coef('Var'  , 0.36773     ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0506283   ), Coef('Var'  , 0.102557    ), Coef('Var'  , 0.168358    ), ], 
		[Coef('Var'  , 0.157315    ), Coef('Var'  , 0.203628    ), Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.041447    ), Coef('Var'  , 0.0824724   ), Coef('Var'  , 0.120075    ), ], 
		[Coef('Var'  , 0.0571745   ), Coef('Var'  , 0.0287129   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.023502    ), Coef('Var'  , 0.0460864   ), Coef('Var'  , 0.0522149   ), ], 
		[Coef('Var'  , 0.0543561   ), Coef('Var'  , 0.0277789   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0255688   ), Coef('Var'  , 0.0494939   ), Coef('Var'  , 0.0533477   ), ], 
		[Coef('Var'  , 0.0462869   ), Coef('Var'  , 0.0238483   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0243255   ), Coef('Var'  , 0.0471337   ), Coef('Var'  , 0.0481737   ), ], ])
	
	
	
	etat10.bords   = {Bord('0'): etat13, Bord('1'): etat13, Bord('2'): etat13, Bord('3'): etat13, Bord('4'): etat13, }
	etat10.permuts = {}
	etat10.interns = {Intern('_'): etat10, }
	etat10.subs    = {Sub('0'): etat1, Sub('1'): etat2, Sub('2'): etat3, Sub('3'): etat4, Sub('G', True): Etat.etatPoint, Sub('4'): etat5, Sub('5'): etat6, Sub('6'): etat7, Sub('7'): etat8, Sub('8'): etat9, Sub('9'): etat11, Sub('10'): etat12, }
	
	etat10.buildIntern()
	
	
	etat10.eqs = [
		(Chem([Bord('2'), Sub('0'), Permut('0'), ])	,	Chem([Sub('2'), Bord('0'), ])),
		(Chem([Bord('1'), Sub('1'), Permut('0'), ])	,	Chem([Sub('2'), Bord('1'), ])),
		(Chem([Bord('3'), Sub('0'), Permut('0'), ])	,	Chem([Sub('4'), Bord('2'), ])),
		(Chem([Bord('2'), Sub('1'), Permut('0'), ])	,	Chem([Sub('4'), Bord('3'), ])),
		(Chem([Bord('0'), Sub('1'), Permut('0'), ])	,	Chem([Sub('7'), Bord('0'), ])),
		(Chem([Bord('1'), Sub('0'), Permut('0'), ])	,	Chem([Sub('7'), Bord('4'), ])),
		(Chem([Bord('4'), Sub('0'), Permut('0'), ])	,	Chem([Sub('8'), Bord('2'), ])),
		(Chem([Bord('3'), Sub('1'), Permut('0'), ])	,	Chem([Sub('8'), Bord('3'), ])),
		(Chem([Bord('0'), Sub('0'), Permut('0'), ])	,	Chem([Sub('10'), Bord('0'), ])),
		(Chem([Bord('4'), Sub('1'), Permut('0'), ])	,	Chem([Sub('10'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('0'), Bord('1'), ])	,	Chem([Sub('7'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('1'), Bord('1'), ])	,	Chem([Sub('10'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('2'), Bord('1'), ])	,	Chem([Sub('6'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('3'), Bord('1'), ])	,	Chem([Sub('5'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('4'), Bord('1'), ])	,	Chem([Sub('1'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('0'), Bord('1'), ])	,	Chem([Sub('9'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('1'), Bord('1'), ])	,	Chem([Sub('2'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('2'), Bord('1'), ])	,	Chem([Sub('7'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('4'), Bord('1'), ])	,	Chem([Sub('5'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('1'), Bord('1'), ])	,	Chem([Sub('7'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('3'), Bord('1'), ])	,	Chem([Sub('9'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('4'), Bord('1'), ])	,	Chem([Sub('4'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('3'), Bord('0'), Bord('1'), ])	,	Chem([Sub('5'), Bord('4'), Bord('1'), ])),
		(Chem([Sub('3'), Bord('1'), Bord('1'), ])	,	Chem([Sub('6'), Bord('4'), Bord('1'), ])),
		(Chem([Sub('3'), Bord('2'), Bord('1'), ])	,	Chem([Sub('8'), Bord('4'), Bord('1'), ])),
		(Chem([Sub('3'), Bord('3'), Bord('1'), ])	,	Chem([Sub('4'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('3'), Bord('4'), Bord('1'), ])	,	Chem([Sub('9'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('4'), Bord('1'), Bord('1'), ])	,	Chem([Sub('8'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('4'), Bord('4'), Bord('1'), ])	,	Chem([Sub('9'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('5'), Bord('0'), Bord('1'), ])	,	Chem([Sub('9'), Bord('4'), Bord('1'), ])),
		(Chem([Sub('5'), Bord('3'), Bord('1'), ])	,	Chem([Sub('6'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('6'), Bord('2'), Bord('1'), ])	,	Chem([Sub('10'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('6'), Bord('3'), Bord('1'), ])	,	Chem([Sub('8'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('7'), Bord('0'), Bord('1'), ])	,	Chem([Sub('10'), Bord('4'), Bord('1'), ])),
		(Chem([Sub('8'), Bord('1'), Bord('1'), ])	,	Chem([Sub('10'), Bord('1'), Bord('1'), ])),
		(Chem([Bord('0'), Bord('1'), ])	,	Chem([Bord('1'), Bord('0'), ])),
		(Chem([Bord('1'), Bord('1'), ])	,	Chem([Bord('2'), Bord('0'), ])),
		(Chem([Bord('2'), Bord('1'), ])	,	Chem([Bord('3'), Bord('0'), ])),
		(Chem([Bord('3'), Bord('1'), ])	,	Chem([Bord('4'), Bord('0'), ])),
		(Chem([Bord('4'), Bord('1'), ])	,	Chem([Bord('0'), Bord('0'), ])),
		]
	
	
	etat10.prim.elems = [Figure(2, [Chem([Bord('0'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('0'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('0'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('0'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('1'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('1'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('1'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('1'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('2'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('2'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('2'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('2'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('3'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('3'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('3'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('3'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('4'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('4'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('4'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('4'), Sub('1'), Sub('1'), Bord('0'), ]), ])]
	etat10.grid.elems = [
		Figure(1, [Chem([Bord('1'), Bord('0'), ]), Chem([Bord('1'), Intern(''), ]), Chem([Bord('1'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('4'), Bord('0'), ]), Chem([Bord('4'), Intern(''), ]), Chem([Bord('4'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('2'), Bord('0'), ]), Chem([Bord('2'), Intern(''), ]), Chem([Bord('2'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('0'), Bord('0'), ]), Chem([Bord('0'), Intern(''), ]), Chem([Bord('0'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('3'), Bord('0'), ]), Chem([Bord('3'), Intern(''), ]), Chem([Bord('3'), Bord('1'), ]), ]), ]
	
	
	etat10.space = [Chem([Bord('4'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('2'), Intern('0'), Intern('0'), ]), Chem([Bord('2'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('3'), Intern('0'), Intern('0'), ]), Chem([Bord('4'), Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('4'), Intern('0'), Intern('0'), ]), ]
	
	etat10.initMat[Chem([Sub('0')])] = FMat([
		[Coef('Var'  , 0.105949    ), Coef('Var'  , 0.126998    ), Coef('Var'  , 0.149211    ), Coef('Var'  , 0.159799    ), Coef('Var'  , 0.172922    ), Coef('Var'  , 0.15296     ), Coef('Var'  , 0.136494    ), Coef('Var'  , 0.121555    ), Coef('Var'  , 0.109132    ), Coef('Var'  , 0.106993    ), ], 
		[Coef('Var'  , 0.131313    ), Coef('Var'  , 0.183001    ), Coef('Var'  , 0.238446    ), Coef('Var'  , 0.237228    ), Coef('Var'  , 0.239625    ), Coef('Var'  , 0.184778    ), Coef('Var'  , 0.133193    ), Coef('Var'  , 0.12        ), Coef('Var'  , 0.109778    ), Coef('Var'  , 0.118914    ), ], 
		[Coef('Var'  , 0.129803    ), Coef('Var'  , 0.148194    ), Coef('Var'  , 0.16992     ), Coef('Var'  , 0.156465    ), Coef('Var'  , 0.145362    ), Coef('Var'  , 0.120837    ), Coef('Var'  , 0.0980416   ), Coef('Var'  , 0.0975503   ), Coef('Var'  , 0.0992837   ), Coef('Var'  , 0.112943    ), ], 
		[Coef('Var'  , 0.14351     ), Coef('Var'  , 0.126215    ), Coef('Var'  , 0.110986    ), Coef('Var'  , 0.0863901   ), Coef('Var'  , 0.0619229   ), Coef('Var'  , 0.0719635   ), Coef('Var'  , 0.080211    ), Coef('Var'  , 0.0948356   ), Coef('Var'  , 0.108371    ), Coef('Var'  , 0.125282    ), ], 
		[Coef('Var'  , 0.109805    ), Coef('Var'  , 0.0940044   ), Coef('Var'  , 0.0787368   ), Coef('Var'  , 0.067588    ), Coef('Var'  , 0.0552987   ), Coef('Var'  , 0.06912     ), Coef('Var'  , 0.0797845   ), Coef('Var'  , 0.0917784   ), Coef('Var'  , 0.10105     ), Coef('Var'  , 0.105618    ), ], 
		[Coef('Var'  , 0.076613    ), Coef('Var'  , 0.0638089   ), Coef('Var'  , 0.0487044   ), Coef('Var'  , 0.0488078   ), Coef('Var'  , 0.0458915   ), Coef('Var'  , 0.0603379   ), Coef('Var'  , 0.0715042   ), Coef('Var'  , 0.0806443   ), Coef('Var'  , 0.0872794   ), Coef('Var'  , 0.082849    ), ], 
		[Coef('Var'  , 0.075821    ), Coef('Var'  , 0.0629188   ), Coef('Var'  , 0.047356    ), Coef('Var'  , 0.0485382   ), Coef('Var'  , 0.0470872   ), Coef('Var'  , 0.0626027   ), Coef('Var'  , 0.075504    ), Coef('Var'  , 0.0841253   ), Coef('Var'  , 0.090286    ), Coef('Var'  , 0.0842876   ), ], 
		[Coef('Var'  , 0.0759338   ), Coef('Var'  , 0.0630471   ), Coef('Var'  , 0.0467288   ), Coef('Var'  , 0.047665    ), Coef('Var'  , 0.0464643   ), Coef('Var'  , 0.0617468   ), Coef('Var'  , 0.0761344   ), Coef('Var'  , 0.0844362   ), Coef('Var'  , 0.0914949   ), Coef('Var'  , 0.0851534   ), ], 
		[Coef('Var'  , 0.0751972   ), Coef('Var'  , 0.0642794   ), Coef('Var'  , 0.0521634   ), Coef('Var'  , 0.0669118   ), Coef('Var'  , 0.0808746   ), Coef('Var'  , 0.0974574   ), Coef('Var'  , 0.113906    ), Coef('Var'  , 0.107479    ), Coef('Var'  , 0.101008    ), Coef('Var'  , 0.0884913   ), ], 
		[Coef('Var'  , 0.0760549   ), Coef('Var'  , 0.0675334   ), Coef('Var'  , 0.0577474   ), Coef('Var'  , 0.0806072   ), Coef('Var'  , 0.104552    ), Coef('Var'  , 0.118196    ), Coef('Var'  , 0.135227    ), Coef('Var'  , 0.117596    ), Coef('Var'  , 0.102318    ), Coef('Var'  , 0.0894692   ), ], ])
	etat10.initMat[Chem([Sub('1')])] = FMat([
		[Coef('Var'  , 0.0932806   ), Coef('Var'  , 0.0827503   ), Coef('Var'  , 0.0707049   ), Coef('Var'  , 0.0613567   ), Coef('Var'  , 0.0499303   ), Coef('Var'  , 0.0634909   ), Coef('Var'  , 0.0761563   ), Coef('Var'  , 0.0908674   ), Coef('Var'  , 0.105949    ), Coef('Var'  , 0.0996143   ), ], 
		[Coef('Var'  , 0.0943202   ), Coef('Var'  , 0.0805818   ), Coef('Var'  , 0.0670357   ), Coef('Var'  , 0.0600363   ), Coef('Var'  , 0.05256     ), Coef('Var'  , 0.0766627   ), Coef('Var'  , 0.102081    ), Coef('Var'  , 0.115093    ), Coef('Var'  , 0.131313    ), Coef('Var'  , 0.11158     ), ], 
		[Coef('Var'  , 0.0996916   ), Coef('Var'  , 0.0982083   ), Coef('Var'  , 0.0986695   ), Coef('Var'  , 0.121411    ), Coef('Var'  , 0.145672    ), Coef('Var'  , 0.156698    ), Coef('Var'  , 0.17001     ), Coef('Var'  , 0.148246    ), Coef('Var'  , 0.129803    ), Coef('Var'  , 0.113207    ), ], 
		[Coef('Var'  , 0.121241    ), Coef('Var'  , 0.129906    ), Coef('Var'  , 0.141164    ), Coef('Var'  , 0.191904    ), Coef('Var'  , 0.245494    ), Coef('Var'  , 0.244564    ), Coef('Var'  , 0.246475    ), Coef('Var'  , 0.193644    ), Coef('Var'  , 0.14351     ), Coef('Var'  , 0.131158    ), ], 
		[Coef('Var'  , 0.113034    ), Coef('Var'  , 0.124162    ), Coef('Var'  , 0.138084    ), Coef('Var'  , 0.153966    ), Coef('Var'  , 0.173574    ), Coef('Var'  , 0.160773    ), Coef('Var'  , 0.150696    ), Coef('Var'  , 0.129566    ), Coef('Var'  , 0.109805    ), Coef('Var'  , 0.110779    ), ], 
		[Coef('Var'  , 0.102409    ), Coef('Var'  , 0.117804    ), Coef('Var'  , 0.135984    ), Coef('Var'  , 0.119039    ), Coef('Var'  , 0.105541    ), Coef('Var'  , 0.0818998   ), Coef('Var'  , 0.0590049   ), Coef('Var'  , 0.0685673   ), Coef('Var'  , 0.076613    ), Coef('Var'  , 0.0896408   ), ], 
		[Coef('Var'  , 0.0988076   ), Coef('Var'  , 0.104333    ), Coef('Var'  , 0.109838    ), Coef('Var'  , 0.0938712   ), Coef('Var'  , 0.0783982   ), Coef('Var'  , 0.0660656   ), Coef('Var'  , 0.0528541   ), Coef('Var'  , 0.0654821   ), Coef('Var'  , 0.075821    ), Coef('Var'  , 0.0881909   ), ], 
		[Coef('Var'  , 0.0963587   ), Coef('Var'  , 0.0929806   ), Coef('Var'  , 0.0865562   ), Coef('Var'  , 0.0717679   ), Coef('Var'  , 0.0540024   ), Coef('Var'  , 0.0529697   ), Coef('Var'  , 0.0487089   ), Coef('Var'  , 0.0641511   ), Coef('Var'  , 0.0759338   ), Coef('Var'  , 0.0878773   ), ], 
		[Coef('Var'  , 0.0934116   ), Coef('Var'  , 0.0884664   ), Coef('Var'  , 0.0808966   ), Coef('Var'  , 0.0669427   ), Coef('Var'  , 0.0498892   ), Coef('Var'  , 0.0493795   ), Coef('Var'  , 0.0465909   ), Coef('Var'  , 0.0616343   ), Coef('Var'  , 0.0751972   ), Coef('Var'  , 0.0851063   ), ], 
		[Coef('Var'  , 0.0874451   ), Coef('Var'  , 0.0808068   ), Coef('Var'  , 0.0710667   ), Coef('Var'  , 0.0597041   ), Coef('Var'  , 0.044939    ), Coef('Var'  , 0.0474975   ), Coef('Var'  , 0.0474221   ), Coef('Var'  , 0.0627498   ), Coef('Var'  , 0.0760549   ), Coef('Var'  , 0.0828457   ), ], ])
	etat10.initMat[Chem([Sub('2')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0254221   ), Coef('Var'  , 0.0499303   ), Coef('Var'  , 0.047865    ), Coef('Var'  , 0.0437498   ), Coef('Var'  , 0.0224429   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0263023   ), Coef('Var'  , 0.05256     ), Coef('Var'  , 0.0472185   ), Coef('Var'  , 0.0411079   ), Coef('Var'  , 0.0209162   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.197431    ), Coef('Var'  , 0.145672    ), Coef('Var'  , 0.108607    ), Coef('Var'  , 0.0724904   ), Coef('Var'  , 0.0361756   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.372038    ), Coef('Var'  , 0.245494    ), Coef('Var'  , 0.175968    ), Coef('Var'  , 0.108737    ), Coef('Var'  , 0.0539302   ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.210895    ), Coef('Var'  , 0.173574    ), Coef('Var'  , 0.171789    ), Coef('Var'  , 0.173526    ), Coef('Var'  , 0.210894    ), ], 
		[Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0521044   ), Coef('Var'  , 0.105541    ), Coef('Var'  , 0.171491    ), Coef('Var'  , 0.240871    ), Coef('Var'  , 0.369386    ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0391563   ), Coef('Var'  , 0.0783982   ), Coef('Var'  , 0.114648    ), Coef('Var'  , 0.151747    ), Coef('Var'  , 0.200492    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0277416   ), Coef('Var'  , 0.0540024   ), Coef('Var'  , 0.0608963   ), Coef('Var'  , 0.0655091   ), Coef('Var'  , 0.0331547   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0256639   ), Coef('Var'  , 0.0498892   ), Coef('Var'  , 0.0550193   ), Coef('Var'  , 0.057326    ), Coef('Var'  , 0.0293555   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0232454   ), Coef('Var'  , 0.044939    ), Coef('Var'  , 0.0464975   ), Coef('Var'  , 0.044936    ), Coef('Var'  , 0.0232522   ), ], ])
	etat10.initMat[Chem([Sub('3')])] = FMat([
		[Coef('Var'  , 0.0693038   ), Coef('Var'  , 0.0816003   ), Coef('Var'  , 0.0927622   ), Coef('Var'  , 0.0994075   ), Coef('Var'  , 0.106017    ), Coef('Var'  , 0.0908212   ), Coef('Var'  , 0.0758931   ), Coef('Var'  , 0.0625537   ), Coef('Var'  , 0.0486163   ), Coef('Var'  , 0.0596954   ), ], 
		[Coef('Var'  , 0.0605272   ), Coef('Var'  , 0.0697002   ), Coef('Var'  , 0.0770258   ), Coef('Var'  , 0.0734893   ), Coef('Var'  , 0.0687479   ), Coef('Var'  , 0.0562612   ), Coef('Var'  , 0.0423818   ), Coef('Var'  , 0.0412699   ), Coef('Var'  , 0.0381731   ), Coef('Var'  , 0.0505292   ), ], 
		[Coef('Var'  , 0.065257    ), Coef('Var'  , 0.0715688   ), Coef('Var'  , 0.0763831   ), Coef('Var'  , 0.0718665   ), Coef('Var'  , 0.0657247   ), Coef('Var'  , 0.0556397   ), Coef('Var'  , 0.042867    ), Coef('Var'  , 0.0441382   ), Coef('Var'  , 0.0424089   ), Coef('Var'  , 0.0550471   ), ], 
		[Coef('Var'  , 0.0743856   ), Coef('Var'  , 0.0808191   ), Coef('Var'  , 0.0862876   ), Coef('Var'  , 0.0793017   ), Coef('Var'  , 0.0701422   ), Coef('Var'  , 0.05847     ), Coef('Var'  , 0.0438571   ), Coef('Var'  , 0.0459883   ), Coef('Var'  , 0.0459269   ), Coef('Var'  , 0.0607134   ), ], 
		[Coef('Var'  , 0.108393    ), Coef('Var'  , 0.103714    ), Coef('Var'  , 0.0989781   ), Coef('Var'  , 0.0887463   ), Coef('Var'  , 0.0767026   ), Coef('Var'  , 0.0656316   ), Coef('Var'  , 0.0525118   ), Coef('Var'  , 0.0651699   ), Coef('Var'  , 0.077263    ), Coef('Var'  , 0.0925114   ), ], 
		[Coef('Var'  , 0.139394    ), Coef('Var'  , 0.121517    ), Coef('Var'  , 0.105408    ), Coef('Var'  , 0.0928988   ), Coef('Var'  , 0.0794595   ), Coef('Var'  , 0.0714526   ), Coef('Var'  , 0.0614903   ), Coef('Var'  , 0.0850485   ), Coef('Var'  , 0.108675    ), Coef('Var'  , 0.122845    ), ], 
		[Coef('Var'  , 0.14164     ), Coef('Var'  , 0.127017    ), Coef('Var'  , 0.114361    ), Coef('Var'  , 0.111228    ), Coef('Var'  , 0.109133    ), Coef('Var'  , 0.129316    ), Coef('Var'  , 0.150891    ), Coef('Var'  , 0.16228     ), Coef('Var'  , 0.176054    ), Coef('Var'  , 0.157419    ), ], 
		[Coef('Var'  , 0.147293    ), Coef('Var'  , 0.135038    ), Coef('Var'  , 0.124799    ), Coef('Var'  , 0.131398    ), Coef('Var'  , 0.14079     ), Coef('Var'  , 0.190378    ), Coef('Var'  , 0.243747    ), Coef('Var'  , 0.243724    ), Coef('Var'  , 0.247221    ), Coef('Var'  , 0.195956    ), ], 
		[Coef('Var'  , 0.118042    ), Coef('Var'  , 0.119833    ), Coef('Var'  , 0.121765    ), Coef('Var'  , 0.133762    ), Coef('Var'  , 0.14745     ), Coef('Var'  , 0.163015    ), Coef('Var'  , 0.181105    ), Coef('Var'  , 0.168699    ), Coef('Var'  , 0.157777    ), Coef('Var'  , 0.137872    ), ], 
		[Coef('Var'  , 0.0757645   ), Coef('Var'  , 0.0891938   ), Coef('Var'  , 0.10223     ), Coef('Var'  , 0.117901    ), Coef('Var'  , 0.135833    ), Coef('Var'  , 0.119015    ), Coef('Var'  , 0.105255    ), Coef('Var'  , 0.081128    ), Coef('Var'  , 0.0578854   ), Coef('Var'  , 0.067412    ), ], ])
	etat10.initMat[Chem([Sub('G')])] = FMat([
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
	etat10.initMat[Chem([Sub('4')])] = FMat([
		[Coef('Var'  , 0.0428168   ), Coef('Var'  , 0.046486    ), Coef('Var'  , 0.0486163   ), Coef('Var'  , 0.0246175   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0218685   ), ], 
		[Coef('Var'  , 0.0378743   ), Coef('Var'  , 0.0391706   ), Coef('Var'  , 0.0381731   ), Coef('Var'  , 0.0196635   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.019507    ), ], 
		[Coef('Var'  , 0.04734     ), Coef('Var'  , 0.0460547   ), Coef('Var'  , 0.0424089   ), Coef('Var'  , 0.0219216   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.024133    ), ], 
		[Coef('Var'  , 0.0576665   ), Coef('Var'  , 0.0522891   ), Coef('Var'  , 0.0459269   ), Coef('Var'  , 0.0233571   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.028932    ), ], 
		[Coef('Var'  , 0.150094    ), Coef('Var'  , 0.113164    ), Coef('Var'  , 0.077263    ), Coef('Var'  , 0.0385412   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.199623    ), ], 
		[Coef('Var'  , 0.242824    ), Coef('Var'  , 0.174444    ), Coef('Var'  , 0.108675    ), Coef('Var'  , 0.0539113   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.370533    ), ], 
		[Coef('Var'  , 0.176336    ), Coef('Var'  , 0.174768    ), Coef('Var'  , 0.176054    ), Coef('Var'  , 0.212298    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.21247     ), ], 
		[Coef('Var'  , 0.113175    ), Coef('Var'  , 0.179049    ), Coef('Var'  , 0.247221    ), Coef('Var'  , 0.372831    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0562174   ), ], 
		[Coef('Var'  , 0.0845348   ), Coef('Var'  , 0.121255    ), Coef('Var'  , 0.157777    ), Coef('Var'  , 0.203743    ), Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0425118   ), ], 
		[Coef('Var'  , 0.0473389   ), Coef('Var'  , 0.0533208   ), Coef('Var'  , 0.0578854   ), Coef('Var'  , 0.029116    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0242048   ), ], ])
	etat10.initMat[Chem([Sub('5')])] = FMat([
		[Coef('Var'  , 0.0927622   ), Coef('Var'  , 0.0888385   ), Coef('Var'  , 0.0837941   ), Coef('Var'  , 0.0891318   ), Coef('Var'  , 0.0932806   ), Coef('Var'  , 0.10101     ), Coef('Var'  , 0.109132    ), Coef('Var'  , 0.108378    ), Coef('Var'  , 0.109082    ), Coef('Var'  , 0.100706    ), ], 
		[Coef('Var'  , 0.0770258   ), Coef('Var'  , 0.0772821   ), Coef('Var'  , 0.0762889   ), Coef('Var'  , 0.0852954   ), Coef('Var'  , 0.0943202   ), Coef('Var'  , 0.101029    ), Coef('Var'  , 0.109778    ), Coef('Var'  , 0.101809    ), Coef('Var'  , 0.0957581   ), Coef('Var'  , 0.0864618   ), ], 
		[Coef('Var'  , 0.0763831   ), Coef('Var'  , 0.0806959   ), Coef('Var'  , 0.0846353   ), Coef('Var'  , 0.0914806   ), Coef('Var'  , 0.0996916   ), Coef('Var'  , 0.0981919   ), Coef('Var'  , 0.0992837   ), Coef('Var'  , 0.0909546   ), Coef('Var'  , 0.0842369   ), Coef('Var'  , 0.0804342   ), ], 
		[Coef('Var'  , 0.0862876   ), Coef('Var'  , 0.095229    ), Coef('Var'  , 0.104169    ), Coef('Var'  , 0.111806    ), Coef('Var'  , 0.121241    ), Coef('Var'  , 0.114205    ), Coef('Var'  , 0.108371    ), Coef('Var'  , 0.0992623   ), Coef('Var'  , 0.0891247   ), Coef('Var'  , 0.088561    ), ], 
		[Coef('Var'  , 0.0989781   ), Coef('Var'  , 0.105371    ), Coef('Var'  , 0.112176    ), Coef('Var'  , 0.111719    ), Coef('Var'  , 0.113034    ), Coef('Var'  , 0.107021    ), Coef('Var'  , 0.10105     ), Coef('Var'  , 0.0983419   ), Coef('Var'  , 0.0932534   ), Coef('Var'  , 0.0971555   ), ], 
		[Coef('Var'  , 0.105408    ), Coef('Var'  , 0.110159    ), Coef('Var'  , 0.116701    ), Coef('Var'  , 0.108445    ), Coef('Var'  , 0.102409    ), Coef('Var'  , 0.0949462   ), Coef('Var'  , 0.0872794   ), Coef('Var'  , 0.0890158   ), Coef('Var'  , 0.0888204   ), Coef('Var'  , 0.097522    ), ], 
		[Coef('Var'  , 0.114361    ), Coef('Var'  , 0.113836    ), Coef('Var'  , 0.114493    ), Coef('Var'  , 0.106559    ), Coef('Var'  , 0.0988076   ), Coef('Var'  , 0.0953329   ), Coef('Var'  , 0.090286    ), Coef('Var'  , 0.0952788   ), Coef('Var'  , 0.0986275   ), Coef('Var'  , 0.106459    ), ], 
		[Coef('Var'  , 0.124799    ), Coef('Var'  , 0.119493    ), Coef('Var'  , 0.114758    ), Coef('Var'  , 0.106534    ), Coef('Var'  , 0.0963587   ), Coef('Var'  , 0.0951846   ), Coef('Var'  , 0.0914949   ), Coef('Var'  , 0.0993848   ), Coef('Var'  , 0.106864    ), Coef('Var'  , 0.115068    ), ], 
		[Coef('Var'  , 0.121765    ), Coef('Var'  , 0.113997    ), Coef('Var'  , 0.105749    ), Coef('Var'  , 0.100481    ), Coef('Var'  , 0.0934116   ), Coef('Var'  , 0.0977601   ), Coef('Var'  , 0.101008    ), Coef('Var'  , 0.109968    ), Coef('Var'  , 0.119426    ), Coef('Var'  , 0.120099    ), ], 
		[Coef('Var'  , 0.10223     ), Coef('Var'  , 0.0950992   ), Coef('Var'  , 0.0872357   ), Coef('Var'  , 0.0885495   ), Coef('Var'  , 0.0874451   ), Coef('Var'  , 0.0953196   ), Coef('Var'  , 0.102318    ), Coef('Var'  , 0.107608    ), Coef('Var'  , 0.114807    ), Coef('Var'  , 0.107534    ), ], ])
	etat10.initMat[Chem([Sub('6')])] = FMat([
		[Coef('Var'  , 0.106017    ), Coef('Var'  , 0.107069    ), Coef('Var'  , 0.109082    ), Coef('Var'  , 0.121545    ), Coef('Var'  , 0.136494    ), Coef('Var'  , 0.153071    ), Coef('Var'  , 0.17308     ), Coef('Var'  , 0.160117    ), Coef('Var'  , 0.149487    ), Coef('Var'  , 0.127292    ), ], 
		[Coef('Var'  , 0.0687479   ), Coef('Var'  , 0.0822822   ), Coef('Var'  , 0.0957581   ), Coef('Var'  , 0.113446    ), Coef('Var'  , 0.133193    ), Coef('Var'  , 0.117388    ), Coef('Var'  , 0.104144    ), Coef('Var'  , 0.0789222   ), Coef('Var'  , 0.0544196   ), Coef('Var'  , 0.0620077   ), ], 
		[Coef('Var'  , 0.0657247   ), Coef('Var'  , 0.0754139   ), Coef('Var'  , 0.0842369   ), Coef('Var'  , 0.0905773   ), Coef('Var'  , 0.0980416   ), Coef('Var'  , 0.0847825   ), Coef('Var'  , 0.0724908   ), Coef('Var'  , 0.0607731   ), Coef('Var'  , 0.048018    ), Coef('Var'  , 0.0580002   ), ], 
		[Coef('Var'  , 0.0701422   ), Coef('Var'  , 0.0809368   ), Coef('Var'  , 0.0891247   ), Coef('Var'  , 0.0857694   ), Coef('Var'  , 0.080211    ), Coef('Var'  , 0.0662862   ), Coef('Var'  , 0.049964    ), Coef('Var'  , 0.0488233   ), Coef('Var'  , 0.0449058   ), Coef('Var'  , 0.0590473   ), ], 
		[Coef('Var'  , 0.0767026   ), Coef('Var'  , 0.0864148   ), Coef('Var'  , 0.0932534   ), Coef('Var'  , 0.0882604   ), Coef('Var'  , 0.0797845   ), Coef('Var'  , 0.0665777   ), Coef('Var'  , 0.0498692   ), Coef('Var'  , 0.0503359   ), Coef('Var'  , 0.0480013   ), Coef('Var'  , 0.0636095   ), ], 
		[Coef('Var'  , 0.0794595   ), Coef('Var'  , 0.085254    ), Coef('Var'  , 0.0888204   ), Coef('Var'  , 0.0815057   ), Coef('Var'  , 0.0715042   ), Coef('Var'  , 0.060486    ), Coef('Var'  , 0.0462067   ), Coef('Var'  , 0.049786    ), Coef('Var'  , 0.0503249   ), Coef('Var'  , 0.0661825   ), ], 
		[Coef('Var'  , 0.109133    ), Coef('Var'  , 0.103897    ), Coef('Var'  , 0.0986275   ), Coef('Var'  , 0.0879746   ), Coef('Var'  , 0.075504    ), Coef('Var'  , 0.0649339   ), Coef('Var'  , 0.0521996   ), Coef('Var'  , 0.065112    ), Coef('Var'  , 0.0774394   ), Coef('Var'  , 0.0929214   ), ], 
		[Coef('Var'  , 0.14079     ), Coef('Var'  , 0.122639    ), Coef('Var'  , 0.106864    ), Coef('Var'  , 0.0913602   ), Coef('Var'  , 0.0761344   ), Coef('Var'  , 0.0664868   ), Coef('Var'  , 0.0567535   ), Coef('Var'  , 0.0807828   ), Coef('Var'  , 0.106504    ), Coef('Var'  , 0.121987    ), ], 
		[Coef('Var'  , 0.14745     ), Coef('Var'  , 0.132454    ), Coef('Var'  , 0.119426    ), Coef('Var'  , 0.116301    ), Coef('Var'  , 0.113906    ), Coef('Var'  , 0.134605    ), Coef('Var'  , 0.155645    ), Coef('Var'  , 0.167524    ), Coef('Var'  , 0.180769    ), Coef('Var'  , 0.162884    ), ], 
		[Coef('Var'  , 0.135833    ), Coef('Var'  , 0.123639    ), Coef('Var'  , 0.114807    ), Coef('Var'  , 0.123261    ), Coef('Var'  , 0.135227    ), Coef('Var'  , 0.185384    ), Coef('Var'  , 0.239647    ), Coef('Var'  , 0.237823    ), Coef('Var'  , 0.240131    ), Coef('Var'  , 0.186068    ), ], ])
	etat10.initMat[Chem([Sub('7')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.1992      ), Coef('Var'  , 0.149211    ), Coef('Var'  , 0.112268    ), Coef('Var'  , 0.0761563   ), Coef('Var'  , 0.0380688   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.368268    ), Coef('Var'  , 0.238446    ), Coef('Var'  , 0.168628    ), Coef('Var'  , 0.102081    ), Coef('Var'  , 0.0503604   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.209214    ), Coef('Var'  , 0.16992     ), Coef('Var'  , 0.168481    ), Coef('Var'  , 0.17001     ), Coef('Var'  , 0.209266    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.055098    ), Coef('Var'  , 0.110986    ), Coef('Var'  , 0.177624    ), Coef('Var'  , 0.246475    ), Coef('Var'  , 0.372526    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0393164   ), Coef('Var'  , 0.0787368   ), Coef('Var'  , 0.114194    ), Coef('Var'  , 0.150696    ), Coef('Var'  , 0.199878    ), Coef('Const', 0.25        ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0250371   ), Coef('Var'  , 0.0487044   ), Coef('Var'  , 0.0548325   ), Coef('Var'  , 0.0590049   ), Coef('Var'  , 0.0297954   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.024346    ), Coef('Var'  , 0.047356    ), Coef('Var'  , 0.0512554   ), Coef('Var'  , 0.0528541   ), Coef('Var'  , 0.0269093   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0241241   ), Coef('Var'  , 0.0467288   ), Coef('Var'  , 0.0493523   ), Coef('Var'  , 0.0487089   ), Coef('Var'  , 0.0252281   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0263607   ), Coef('Var'  , 0.0521634   ), Coef('Var'  , 0.0500763   ), Coef('Var'  , 0.0465909   ), Coef('Var'  , 0.0237156   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0290357   ), Coef('Var'  , 0.0577474   ), Coef('Var'  , 0.0532878   ), Coef('Var'  , 0.0474221   ), Coef('Var'  , 0.0242521   ), Coef('Const', 0           ), Coef('Const', 0           ), ], ])
	etat10.initMat[Chem([Sub('8')])] = FMat([
		[Coef('Var'  , 0.0758931   ), Coef('Var'  , 0.112343    ), Coef('Var'  , 0.149487    ), Coef('Var'  , 0.199407    ), Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0379361   ), ], 
		[Coef('Var'  , 0.0423818   ), Coef('Var'  , 0.0489592   ), Coef('Var'  , 0.0544196   ), Coef('Var'  , 0.0273528   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0216063   ), ], 
		[Coef('Var'  , 0.042867    ), Coef('Var'  , 0.0467937   ), Coef('Var'  , 0.048018    ), Coef('Var'  , 0.0245771   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0222166   ), ], 
		[Coef('Var'  , 0.0438571   ), Coef('Var'  , 0.0458397   ), Coef('Var'  , 0.0449058   ), Coef('Var'  , 0.0232085   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0226312   ), ], 
		[Coef('Var'  , 0.0525118   ), Coef('Var'  , 0.0512354   ), Coef('Var'  , 0.0480013   ), Coef('Var'  , 0.0246067   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0266287   ), ], 
		[Coef('Var'  , 0.0614903   ), Coef('Var'  , 0.0570043   ), Coef('Var'  , 0.0503249   ), Coef('Var'  , 0.0258671   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0311372   ), ], 
		[Coef('Var'  , 0.150891    ), Coef('Var'  , 0.113571    ), Coef('Var'  , 0.0774394   ), Coef('Var'  , 0.0385886   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.199983    ), ], 
		[Coef('Var'  , 0.243747    ), Coef('Var'  , 0.173395    ), Coef('Var'  , 0.106504    ), Coef('Var'  , 0.0525018   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.370893    ), ], 
		[Coef('Var'  , 0.181105    ), Coef('Var'  , 0.179782    ), Coef('Var'  , 0.180769    ), Coef('Var'  , 0.214826    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.214956    ), ], 
		[Coef('Var'  , 0.105255    ), Coef('Var'  , 0.171077    ), Coef('Var'  , 0.240131    ), Coef('Var'  , 0.369065    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.052012    ), ], ])
	etat10.initMat[Chem([Sub('9')])] = FMat([
		[Coef('Var'  , 0.0837941   ), Coef('Var'  , 0.0773939   ), Coef('Var'  , 0.0693038   ), Coef('Var'  , 0.0569463   ), Coef('Var'  , 0.0428168   ), Coef('Var'  , 0.0443114   ), Coef('Var'  , 0.0437498   ), Coef('Var'  , 0.0583775   ), Coef('Var'  , 0.0707049   ), Coef('Var'  , 0.0782507   ), ], 
		[Coef('Var'  , 0.0762889   ), Coef('Var'  , 0.0693134   ), Coef('Var'  , 0.0605272   ), Coef('Var'  , 0.0503727   ), Coef('Var'  , 0.0378743   ), Coef('Var'  , 0.0404232   ), Coef('Var'  , 0.0411079   ), Coef('Var'  , 0.0546503   ), Coef('Var'  , 0.0670357   ), Coef('Var'  , 0.0721817   ), ], 
		[Coef('Var'  , 0.0846353   ), Coef('Var'  , 0.075378    ), Coef('Var'  , 0.065257    ), Coef('Var'  , 0.0572585   ), Coef('Var'  , 0.04734     ), Coef('Var'  , 0.0603086   ), Coef('Var'  , 0.0724904   ), Coef('Var'  , 0.0851558   ), Coef('Var'  , 0.0986695   ), Coef('Var'  , 0.0912327   ), ], 
		[Coef('Var'  , 0.104169    ), Coef('Var'  , 0.0891223   ), Coef('Var'  , 0.0743856   ), Coef('Var'  , 0.0662882   ), Coef('Var'  , 0.0576665   ), Coef('Var'  , 0.0828622   ), Coef('Var'  , 0.108737    ), Coef('Var'  , 0.123796    ), Coef('Var'  , 0.141164    ), Coef('Var'  , 0.121632    ), ], 
		[Coef('Var'  , 0.112176    ), Coef('Var'  , 0.109598    ), Coef('Var'  , 0.108393    ), Coef('Var'  , 0.128593    ), Coef('Var'  , 0.150094    ), Coef('Var'  , 0.160517    ), Coef('Var'  , 0.173526    ), Coef('Var'  , 0.153966    ), Coef('Var'  , 0.138084    ), Coef('Var'  , 0.123699    ), ], 
		[Coef('Var'  , 0.116701    ), Coef('Var'  , 0.126509    ), Coef('Var'  , 0.139394    ), Coef('Var'  , 0.189466    ), Coef('Var'  , 0.242824    ), Coef('Var'  , 0.239919    ), Coef('Var'  , 0.240871    ), Coef('Var'  , 0.186322    ), Coef('Var'  , 0.135984    ), Coef('Var'  , 0.124511    ), ], 
		[Coef('Var'  , 0.114493    ), Coef('Var'  , 0.127062    ), Coef('Var'  , 0.14164     ), Coef('Var'  , 0.157592    ), Coef('Var'  , 0.176336    ), Coef('Var'  , 0.162962    ), Coef('Var'  , 0.151747    ), Coef('Var'  , 0.130207    ), Coef('Var'  , 0.109838    ), Coef('Var'  , 0.111656    ), ], 
		[Coef('Var'  , 0.114758    ), Coef('Var'  , 0.130704    ), Coef('Var'  , 0.147293    ), Coef('Var'  , 0.129342    ), Coef('Var'  , 0.113175    ), Coef('Var'  , 0.089372    ), Coef('Var'  , 0.0655091   ), Coef('Var'  , 0.077181    ), Coef('Var'  , 0.0865562   ), Coef('Var'  , 0.101606    ), ], 
		[Coef('Var'  , 0.105749    ), Coef('Var'  , 0.112422    ), Coef('Var'  , 0.118042    ), Coef('Var'  , 0.101641    ), Coef('Var'  , 0.0845348   ), Coef('Var'  , 0.0718673   ), Coef('Var'  , 0.057326    ), Coef('Var'  , 0.0706343   ), Coef('Var'  , 0.0808966   ), Coef('Var'  , 0.094572    ), ], 
		[Coef('Var'  , 0.0872357   ), Coef('Var'  , 0.0824975   ), Coef('Var'  , 0.0757645   ), Coef('Var'  , 0.0625009   ), Coef('Var'  , 0.0473389   ), Coef('Var'  , 0.047457    ), Coef('Var'  , 0.044936    ), Coef('Var'  , 0.0597109   ), Coef('Var'  , 0.0710667   ), Coef('Var'  , 0.0806602   ), ], ])
	etat10.initMat[Chem([Sub('10')])] = FMat([
		[Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.21071     ), Coef('Var'  , 0.17308     ), Coef('Var'  , 0.171309    ), Coef('Var'  , 0.172922    ), Coef('Var'  , 0.210599    ), ], 
		[Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0515694   ), Coef('Var'  , 0.104144    ), Coef('Var'  , 0.170529    ), Coef('Var'  , 0.239625    ), Coef('Var'  , 0.36896     ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.036196    ), Coef('Var'  , 0.0724908   ), Coef('Var'  , 0.108446    ), Coef('Var'  , 0.145362    ), Coef('Var'  , 0.19725     ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0256148   ), Coef('Var'  , 0.049964    ), Coef('Var'  , 0.0569068   ), Coef('Var'  , 0.0619229   ), Coef('Var'  , 0.0312921   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0257292   ), Coef('Var'  , 0.0498692   ), Coef('Var'  , 0.0540008   ), Coef('Var'  , 0.0552987   ), Coef('Var'  , 0.0282716   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0239189   ), Coef('Var'  , 0.0462067   ), Coef('Var'  , 0.0476897   ), Coef('Var'  , 0.0458915   ), Coef('Var'  , 0.0237708   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0265234   ), Coef('Var'  , 0.0521996   ), Coef('Var'  , 0.0507155   ), Coef('Var'  , 0.0470872   ), Coef('Var'  , 0.0241921   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0282809   ), Coef('Var'  , 0.0567535   ), Coef('Var'  , 0.0518219   ), Coef('Var'  , 0.0464643   ), Coef('Var'  , 0.0235409   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.202699    ), Coef('Var'  , 0.155645    ), Coef('Var'  , 0.11825     ), Coef('Var'  , 0.0808746   ), Coef('Var'  , 0.0405512   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.368759    ), Coef('Var'  , 0.239647    ), Coef('Var'  , 0.17033     ), Coef('Var'  , 0.104552    ), Coef('Var'  , 0.0515715   ), ], ])
	
	
	
	etat11.bords   = {Bord('0'): etat13, Bord('1'): etat13, Bord('2'): etat13, Bord('3'): etat13, Bord('4'): etat13, }
	etat11.permuts = {}
	etat11.interns = {Intern('_'): etat11, }
	etat11.subs    = {Sub('0'): etat1, Sub('1'): etat2, Sub('2'): etat3, Sub('3'): etat4, Sub('G', True): Etat.etatPoint, Sub('4'): etat5, Sub('5'): etat6, Sub('6'): etat7, Sub('7'): etat8, Sub('8'): etat9, Sub('9'): etat10, Sub('10'): etat12, }
	
	etat11.buildIntern()
	
	
	etat11.eqs = [
		(Chem([Bord('4'), Sub('0'), Permut('0'), ])	,	Chem([Sub('1'), Bord('0'), ])),
		(Chem([Bord('3'), Sub('1'), Permut('0'), ])	,	Chem([Sub('1'), Bord('1'), ])),
		(Chem([Bord('3'), Sub('0'), Permut('0'), ])	,	Chem([Sub('2'), Bord('3'), ])),
		(Chem([Bord('2'), Sub('1'), Permut('0'), ])	,	Chem([Sub('2'), Bord('4'), ])),
		(Chem([Bord('0'), Sub('1'), Permut('0'), ])	,	Chem([Sub('3'), Bord('0'), ])),
		(Chem([Bord('1'), Sub('0'), Permut('0'), ])	,	Chem([Sub('3'), Bord('4'), ])),
		(Chem([Bord('1'), Sub('1'), Permut('0'), ])	,	Chem([Sub('4'), Bord('0'), ])),
		(Chem([Bord('2'), Sub('0'), Permut('0'), ])	,	Chem([Sub('4'), Bord('4'), ])),
		(Chem([Bord('0'), Sub('0'), Permut('0'), ])	,	Chem([Sub('5'), Bord('0'), ])),
		(Chem([Bord('4'), Sub('1'), Permut('0'), ])	,	Chem([Sub('5'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('0'), Bord('1'), ])	,	Chem([Sub('7'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('1'), Bord('1'), ])	,	Chem([Sub('10'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('2'), Bord('1'), ])	,	Chem([Sub('6'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('3'), Bord('1'), ])	,	Chem([Sub('5'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('4'), Bord('1'), ])	,	Chem([Sub('1'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('1'), Bord('1'), ])	,	Chem([Sub('2'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('2'), Bord('1'), ])	,	Chem([Sub('7'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('4'), Bord('1'), ])	,	Chem([Sub('5'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('0'), Bord('1'), ])	,	Chem([Sub('9'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('1'), Bord('1'), ])	,	Chem([Sub('7'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('4'), Bord('1'), ])	,	Chem([Sub('4'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('3'), Bord('0'), Bord('1'), ])	,	Chem([Sub('5'), Bord('4'), Bord('1'), ])),
		(Chem([Sub('3'), Bord('1'), Bord('1'), ])	,	Chem([Sub('6'), Bord('4'), Bord('1'), ])),
		(Chem([Sub('3'), Bord('2'), Bord('1'), ])	,	Chem([Sub('8'), Bord('4'), Bord('1'), ])),
		(Chem([Sub('3'), Bord('3'), Bord('1'), ])	,	Chem([Sub('4'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('4'), Bord('1'), Bord('1'), ])	,	Chem([Sub('8'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('4'), Bord('2'), Bord('1'), ])	,	Chem([Sub('9'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('5'), Bord('3'), Bord('1'), ])	,	Chem([Sub('6'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('6'), Bord('2'), Bord('1'), ])	,	Chem([Sub('10'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('6'), Bord('3'), Bord('1'), ])	,	Chem([Sub('8'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('7'), Bord('0'), Bord('1'), ])	,	Chem([Sub('10'), Bord('4'), Bord('1'), ])),
		(Chem([Sub('7'), Bord('4'), Bord('1'), ])	,	Chem([Sub('9'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('8'), Bord('1'), Bord('1'), ])	,	Chem([Sub('10'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('8'), Bord('2'), Bord('1'), ])	,	Chem([Sub('9'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('9'), Bord('4'), Bord('1'), ])	,	Chem([Sub('10'), Bord('0'), Bord('1'), ])),
		(Chem([Bord('0'), Bord('1'), ])	,	Chem([Bord('1'), Bord('0'), ])),
		(Chem([Bord('1'), Bord('1'), ])	,	Chem([Bord('2'), Bord('0'), ])),
		(Chem([Bord('2'), Bord('1'), ])	,	Chem([Bord('3'), Bord('0'), ])),
		(Chem([Bord('3'), Bord('1'), ])	,	Chem([Bord('4'), Bord('0'), ])),
		(Chem([Bord('4'), Bord('1'), ])	,	Chem([Bord('0'), Bord('0'), ])),
		]
	
	
	etat11.prim.elems = [Figure(2, [Chem([Bord('0'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('0'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('0'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('0'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('1'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('1'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('1'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('1'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('2'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('2'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('2'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('2'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('3'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('3'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('3'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('3'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('4'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('4'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('4'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('4'), Sub('1'), Sub('1'), Bord('0'), ]), ])]
	etat11.grid.elems = [
		Figure(1, [Chem([Bord('1'), Bord('0'), ]), Chem([Bord('1'), Intern(''), ]), Chem([Bord('1'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('4'), Bord('0'), ]), Chem([Bord('4'), Intern(''), ]), Chem([Bord('4'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('2'), Bord('0'), ]), Chem([Bord('2'), Intern(''), ]), Chem([Bord('2'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('0'), Bord('0'), ]), Chem([Bord('0'), Intern(''), ]), Chem([Bord('0'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('3'), Bord('0'), ]), Chem([Bord('3'), Intern(''), ]), Chem([Bord('3'), Bord('1'), ]), ]), ]
	
	
	etat11.space = [Chem([Bord('4'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('2'), Intern('0'), Intern('0'), ]), Chem([Bord('2'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('3'), Intern('0'), Intern('0'), ]), Chem([Bord('4'), Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('4'), Intern('0'), Intern('0'), ]), ]
	
	etat11.initMat[Chem([Sub('0')])] = FMat([
		[Coef('Var'  , 0.15212     ), Coef('Var'  , 0.130722    ), Coef('Var'  , 0.109656    ), Coef('Var'  , 0.110951    ), Coef('Var'  , 0.112612    ), Coef('Var'  , 0.124865    ), Coef('Var'  , 0.139202    ), Coef('Var'  , 0.155515    ), Coef('Var'  , 0.175025    ), Coef('Var'  , 0.162578    ), ], 
		[Coef('Var'  , 0.061145    ), Coef('Var'  , 0.0714643   ), Coef('Var'  , 0.0806461   ), Coef('Var'  , 0.0956677   ), Coef('Var'  , 0.110076    ), Coef('Var'  , 0.126481    ), Coef('Var'  , 0.1443      ), Coef('Var'  , 0.12649     ), Coef('Var'  , 0.110729    ), Coef('Var'  , 0.0857169   ), ], 
		[Coef('Var'  , 0.0461033   ), Coef('Var'  , 0.0562545   ), Coef('Var'  , 0.0652419   ), Coef('Var'  , 0.0768273   ), Coef('Var'  , 0.0879491   ), Coef('Var'  , 0.0945984   ), Coef('Var'  , 0.102065    ), Coef('Var'  , 0.0872705   ), Coef('Var'  , 0.0733467   ), Coef('Var'  , 0.0598883   ), ], 
		[Coef('Var'  , 0.0454518   ), Coef('Var'  , 0.059728    ), Coef('Var'  , 0.0706488   ), Coef('Var'  , 0.0809608   ), Coef('Var'  , 0.0882064   ), Coef('Var'  , 0.084805    ), Coef('Var'  , 0.0787319   ), Coef('Var'  , 0.0655646   ), Coef('Var'  , 0.0496298   ), Coef('Var'  , 0.049063    ), ], 
		[Coef('Var'  , 0.0463999   ), Coef('Var'  , 0.0605391   ), Coef('Var'  , 0.0719661   ), Coef('Var'  , 0.0804103   ), Coef('Var'  , 0.086454    ), Coef('Var'  , 0.0823336   ), Coef('Var'  , 0.0753685   ), Coef('Var'  , 0.0636202   ), Coef('Var'  , 0.0484175   ), Coef('Var'  , 0.0490081   ), ], 
		[Coef('Var'  , 0.0451942   ), Coef('Var'  , 0.0599768   ), Coef('Var'  , 0.0735342   ), Coef('Var'  , 0.0799636   ), Coef('Var'  , 0.0850129   ), Coef('Var'  , 0.0781523   ), Coef('Var'  , 0.0687592   ), Coef('Var'  , 0.0574209   ), Coef('Var'  , 0.0430496   ), Coef('Var'  , 0.045189    ), ], 
		[Coef('Var'  , 0.0774698   ), Coef('Var'  , 0.0930311   ), Coef('Var'  , 0.109169    ), Coef('Var'  , 0.102919    ), Coef('Var'  , 0.0969756   ), Coef('Var'  , 0.085379    ), Coef('Var'  , 0.0728551   ), Coef('Var'  , 0.062456    ), Coef('Var'  , 0.0506237   ), Coef('Var'  , 0.0642831   ), ], 
		[Coef('Var'  , 0.104781    ), Coef('Var'  , 0.119476    ), Coef('Var'  , 0.13694     ), Coef('Var'  , 0.117102    ), Coef('Var'  , 0.0992985   ), Coef('Var'  , 0.0836938   ), Coef('Var'  , 0.0684698   ), Coef('Var'  , 0.0606057   ), Coef('Var'  , 0.0528324   ), Coef('Var'  , 0.0780749   ), ], 
		[Coef('Var'  , 0.17803     ), Coef('Var'  , 0.15962     ), Coef('Var'  , 0.143828    ), Coef('Var'  , 0.12961     ), Coef('Var'  , 0.117277    ), Coef('Var'  , 0.114528    ), Coef('Var'  , 0.112638    ), Coef('Var'  , 0.132574    ), Coef('Var'  , 0.153526    ), Coef('Var'  , 0.164781    ), ], 
		[Coef('Var'  , 0.243305    ), Coef('Var'  , 0.189188    ), Coef('Var'  , 0.138369    ), Coef('Var'  , 0.125588    ), Coef('Var'  , 0.116139    ), Coef('Var'  , 0.125163    ), Coef('Var'  , 0.137611    ), Coef('Var'  , 0.188483    ), Coef('Var'  , 0.24282     ), Coef('Var'  , 0.241418    ), ], ])
	etat11.initMat[Chem([Sub('1')])] = FMat([
		[Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.039249    ), Coef('Var'  , 0.0782543   ), Coef('Var'  , 0.115098    ), Coef('Var'  , 0.15212     ), Coef('Var'  , 0.200849    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.025273    ), Coef('Var'  , 0.0496333   ), Coef('Var'  , 0.0560252   ), Coef('Var'  , 0.061145    ), Coef('Var'  , 0.0307522   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0207033   ), Coef('Var'  , 0.0405464   ), Coef('Var'  , 0.044025    ), Coef('Var'  , 0.0461033   ), Coef('Var'  , 0.0233217   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0230198   ), Coef('Var'  , 0.0445438   ), Coef('Var'  , 0.0465552   ), Coef('Var'  , 0.0454518   ), Coef('Var'  , 0.0235353   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0256258   ), Coef('Var'  , 0.0503329   ), Coef('Var'  , 0.0495509   ), Coef('Var'  , 0.0463999   ), Coef('Var'  , 0.0239251   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0283679   ), Coef('Var'  , 0.0566326   ), Coef('Var'  , 0.0513347   ), Coef('Var'  , 0.0451942   ), Coef('Var'  , 0.0229668   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.200535    ), Coef('Var'  , 0.151779    ), Coef('Var'  , 0.114194    ), Coef('Var'  , 0.0774698   ), Coef('Var'  , 0.038659    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.370258    ), Coef('Var'  , 0.242206    ), Coef('Var'  , 0.172026    ), Coef('Var'  , 0.104781    ), Coef('Var'  , 0.0517685   ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.213228    ), Coef('Var'  , 0.177742    ), Coef('Var'  , 0.1766      ), Coef('Var'  , 0.17803     ), Coef('Var'  , 0.213373    ), ], 
		[Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0537407   ), Coef('Var'  , 0.10833     ), Coef('Var'  , 0.17459     ), Coef('Var'  , 0.243305    ), Coef('Var'  , 0.370849    ), ], ])
	etat11.initMat[Chem([Sub('2')])] = FMat([
		[Coef('Const', 0           ), Coef('Var'  , 0.0214579   ), Coef('Var'  , 0.0422061   ), Coef('Var'  , 0.0463938   ), Coef('Var'  , 0.0492431   ), Coef('Var'  , 0.0249359   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0246493   ), Coef('Var'  , 0.0476807   ), Coef('Var'  , 0.0489785   ), Coef('Var'  , 0.0471731   ), Coef('Var'  , 0.0243292   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0250572   ), Coef('Var'  , 0.0492342   ), Coef('Var'  , 0.0466699   ), Coef('Var'  , 0.0421787   ), Coef('Var'  , 0.0216127   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0287463   ), Coef('Var'  , 0.0571189   ), Coef('Var'  , 0.0524042   ), Coef('Var'  , 0.0463305   ), Coef('Var'  , 0.0236579   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.25        ), Coef('Var'  , 0.197394    ), Coef('Var'  , 0.145899    ), Coef('Var'  , 0.109066    ), Coef('Var'  , 0.0736383   ), Coef('Var'  , 0.0366717   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.5         ), Coef('Var'  , 0.370763    ), Coef('Var'  , 0.24309     ), Coef('Var'  , 0.173677    ), Coef('Var'  , 0.106854    ), Coef('Var'  , 0.0529137   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0.25        ), Coef('Var'  , 0.213672    ), Coef('Var'  , 0.178611    ), Coef('Var'  , 0.176872    ), Coef('Var'  , 0.177732    ), Coef('Var'  , 0.2132      ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0536634   ), Coef('Var'  , 0.108203    ), Coef('Var'  , 0.174917    ), Coef('Var'  , 0.243996    ), Coef('Var'  , 0.371254    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0390825   ), Coef('Var'  , 0.0783749   ), Coef('Var'  , 0.114789    ), Coef('Var'  , 0.152196    ), Coef('Var'  , 0.200707    ), Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0255145   ), Coef('Var'  , 0.0495829   ), Coef('Var'  , 0.0562325   ), Coef('Var'  , 0.0606589   ), Coef('Var'  , 0.030718    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], ])
	etat11.initMat[Chem([Sub('3')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.199257    ), Coef('Var'  , 0.149392    ), Coef('Var'  , 0.111917    ), Coef('Var'  , 0.0755101   ), Coef('Var'  , 0.0376594   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.37122     ), Coef('Var'  , 0.244386    ), Coef('Var'  , 0.17484     ), Coef('Var'  , 0.108613    ), Coef('Var'  , 0.05362     ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.211388    ), Coef('Var'  , 0.174124    ), Coef('Var'  , 0.173346    ), Coef('Var'  , 0.175126    ), Coef('Var'  , 0.211958    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0522322   ), Coef('Var'  , 0.1058      ), Coef('Var'  , 0.171359    ), Coef('Var'  , 0.240356    ), Coef('Var'  , 0.369127    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0391079   ), Coef('Var'  , 0.0779609   ), Coef('Var'  , 0.113445    ), Coef('Var'  , 0.149379    ), Coef('Var'  , 0.199337    ), Coef('Const', 0.25        ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0243452   ), Coef('Var'  , 0.0475359   ), Coef('Var'  , 0.0540052   ), Coef('Var'  , 0.0588458   ), Coef('Var'  , 0.02966     ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0248144   ), Coef('Var'  , 0.0481601   ), Coef('Var'  , 0.0530059   ), Coef('Var'  , 0.0550916   ), Coef('Var'  , 0.0281915   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0194122   ), Coef('Var'  , 0.0379473   ), Coef('Var'  , 0.039397    ), Coef('Var'  , 0.0389773   ), Coef('Var'  , 0.0199848   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0281084   ), Coef('Var'  , 0.0550897   ), Coef('Var'  , 0.053515    ), Coef('Var'  , 0.0493357   ), Coef('Var'  , 0.0254067   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0301141   ), Coef('Var'  , 0.0596053   ), Coef('Var'  , 0.0551701   ), Coef('Var'  , 0.0487654   ), Coef('Var'  , 0.025056    ), Coef('Const', 0           ), Coef('Const', 0           ), ], ])
	etat11.initMat[Chem([Sub('G')])] = FMat([
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
	etat11.initMat[Chem([Sub('4')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0243463   ), Coef('Var'  , 0.0481366   ), Coef('Var'  , 0.0456955   ), Coef('Var'  , 0.0419363   ), Coef('Var'  , 0.0213492   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0309729   ), Coef('Var'  , 0.0615087   ), Coef('Var'  , 0.0571063   ), Coef('Var'  , 0.0510007   ), Coef('Var'  , 0.0261334   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.200597    ), Coef('Var'  , 0.15153     ), Coef('Var'  , 0.114483    ), Coef('Var'  , 0.0775266   ), Coef('Var'  , 0.0388862   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.369203    ), Coef('Var'  , 0.240323    ), Coef('Var'  , 0.171259    ), Coef('Var'  , 0.105206    ), Coef('Var'  , 0.0520558   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.209431    ), Coef('Var'  , 0.170689    ), Coef('Var'  , 0.168349    ), Coef('Var'  , 0.16977     ), Coef('Var'  , 0.208918    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0531591   ), Coef('Var'  , 0.10737     ), Coef('Var'  , 0.173831    ), Coef('Var'  , 0.243018    ), Coef('Var'  , 0.370672    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0413015   ), Coef('Var'  , 0.0821852   ), Coef('Var'  , 0.118808    ), Coef('Var'  , 0.155378    ), Coef('Var'  , 0.202506    ), Coef('Const', 0.25        ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.022659    ), Coef('Var'  , 0.0445539   ), Coef('Var'  , 0.0514869   ), Coef('Var'  , 0.0573804   ), Coef('Var'  , 0.0288279   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0246112   ), Coef('Var'  , 0.0479762   ), Coef('Var'  , 0.051423    ), Coef('Var'  , 0.0528411   ), Coef('Var'  , 0.0268118   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0237188   ), Coef('Var'  , 0.0457275   ), Coef('Var'  , 0.0475586   ), Coef('Var'  , 0.0459444   ), Coef('Var'  , 0.0238398   ), Coef('Const', 0           ), Coef('Const', 0           ), ], ])
	etat11.initMat[Chem([Sub('5')])] = FMat([
		[Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.211728    ), Coef('Var'  , 0.175025    ), Coef('Var'  , 0.172974    ), Coef('Var'  , 0.174204    ), Coef('Var'  , 0.211245    ), ], 
		[Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0549647   ), Coef('Var'  , 0.110729    ), Coef('Var'  , 0.177211    ), Coef('Var'  , 0.246006    ), Coef('Var'  , 0.372246    ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0365666   ), Coef('Var'  , 0.0733467   ), Coef('Var'  , 0.1101      ), Coef('Var'  , 0.147847    ), Coef('Var'  , 0.198533    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0255277   ), Coef('Var'  , 0.0496298   ), Coef('Var'  , 0.0558807   ), Coef('Var'  , 0.0600709   ), Coef('Var'  , 0.030353    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.025083    ), Coef('Var'  , 0.0484175   ), Coef('Var'  , 0.0528736   ), Coef('Var'  , 0.0541122   ), Coef('Var'  , 0.0277907   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0222222   ), Coef('Var'  , 0.0430496   ), Coef('Var'  , 0.044867    ), Coef('Var'  , 0.0437657   ), Coef('Var'  , 0.0226448   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0256241   ), Coef('Var'  , 0.0506237   ), Coef('Var'  , 0.049013    ), Coef('Var'  , 0.0456877   ), Coef('Var'  , 0.0233889   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0263064   ), Coef('Var'  , 0.0528324   ), Coef('Var'  , 0.0467706   ), Coef('Var'  , 0.0406075   ), Coef('Var'  , 0.0204642   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.201408    ), Coef('Var'  , 0.153526    ), Coef('Var'  , 0.116548    ), Coef('Var'  , 0.0803066   ), Coef('Var'  , 0.0401399   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.370569    ), Coef('Var'  , 0.24282     ), Coef('Var'  , 0.173763    ), Coef('Var'  , 0.107392    ), Coef('Var'  , 0.0531941   ), ], ])
	etat11.initMat[Chem([Sub('6')])] = FMat([
		[Coef('Var'  , 0.149392    ), Coef('Var'  , 0.160503    ), Coef('Var'  , 0.174204    ), Coef('Var'  , 0.155032    ), Coef('Var'  , 0.139202    ), Coef('Var'  , 0.124264    ), Coef('Var'  , 0.111506    ), Coef('Var'  , 0.108639    ), Coef('Var'  , 0.106642    ), Coef('Var'  , 0.127419    ), ], 
		[Coef('Var'  , 0.244386    ), Coef('Var'  , 0.243466    ), Coef('Var'  , 0.246006    ), Coef('Var'  , 0.193771    ), Coef('Var'  , 0.1443      ), Coef('Var'  , 0.132726    ), Coef('Var'  , 0.123573    ), Coef('Var'  , 0.131344    ), Coef('Var'  , 0.142106    ), Coef('Var'  , 0.191364    ), ], 
		[Coef('Var'  , 0.174124    ), Coef('Var'  , 0.159921    ), Coef('Var'  , 0.147847    ), Coef('Var'  , 0.124237    ), Coef('Var'  , 0.102065    ), Coef('Var'  , 0.103383    ), Coef('Var'  , 0.10633     ), Coef('Var'  , 0.120496    ), Coef('Var'  , 0.137143    ), Coef('Var'  , 0.154205    ), ], 
		[Coef('Var'  , 0.1058      ), Coef('Var'  , 0.0825852   ), Coef('Var'  , 0.0600709   ), Coef('Var'  , 0.0703899   ), Coef('Var'  , 0.0787319   ), Coef('Var'  , 0.0918637   ), Coef('Var'  , 0.103837    ), Coef('Var'  , 0.118949    ), Coef('Var'  , 0.136186    ), Coef('Var'  , 0.119355    ), ], 
		[Coef('Var'  , 0.0779609   ), Coef('Var'  , 0.0668986   ), Coef('Var'  , 0.0541122   ), Coef('Var'  , 0.0663279   ), Coef('Var'  , 0.0753685   ), Coef('Var'  , 0.0861311   ), Coef('Var'  , 0.0947589   ), Coef('Var'  , 0.10048     ), Coef('Var'  , 0.106137    ), Coef('Var'  , 0.0919944   ), ], 
		[Coef('Var'  , 0.0475359   ), Coef('Var'  , 0.04699     ), Coef('Var'  , 0.0437657   ), Coef('Var'  , 0.0578434   ), Coef('Var'  , 0.0687592   ), Coef('Var'  , 0.078644    ), Coef('Var'  , 0.0859067   ), Coef('Var'  , 0.0819028   ), Coef('Var'  , 0.0760535   ), Coef('Var'  , 0.0628026   ), ], 
		[Coef('Var'  , 0.0481601   ), Coef('Var'  , 0.0482033   ), Coef('Var'  , 0.0456877   ), Coef('Var'  , 0.0602208   ), Coef('Var'  , 0.0728551   ), Coef('Var'  , 0.0818492   ), Coef('Var'  , 0.0892471   ), Coef('Var'  , 0.0842496   ), Coef('Var'  , 0.0770662   ), Coef('Var'  , 0.0640467   ), ], 
		[Coef('Var'  , 0.0379473   ), Coef('Var'  , 0.0398764   ), Coef('Var'  , 0.0406075   ), Coef('Var'  , 0.0547636   ), Coef('Var'  , 0.0684698   ), Coef('Var'  , 0.0746094   ), Coef('Var'  , 0.0799933   ), Coef('Var'  , 0.0724195   ), Coef('Var'  , 0.0630264   ), Coef('Var'  , 0.0515216   ), ], 
		[Coef('Var'  , 0.0550897   ), Coef('Var'  , 0.0682482   ), Coef('Var'  , 0.0803066   ), Coef('Var'  , 0.0963056   ), Coef('Var'  , 0.112638    ), Coef('Var'  , 0.107653    ), Coef('Var'  , 0.102309    ), Coef('Var'  , 0.0918642   ), Coef('Var'  , 0.0791409   ), Coef('Var'  , 0.0684851   ), ], 
		[Coef('Var'  , 0.0596053   ), Coef('Var'  , 0.0833082   ), Coef('Var'  , 0.107392    ), Coef('Var'  , 0.121108    ), Coef('Var'  , 0.137611    ), Coef('Var'  , 0.118877    ), Coef('Var'  , 0.102539    ), Coef('Var'  , 0.0896556   ), Coef('Var'  , 0.0764977   ), Coef('Var'  , 0.068807    ), ], ])
	etat11.initMat[Chem([Sub('7')])] = FMat([
		[Coef('Var'  , 0.069993    ), Coef('Var'  , 0.0832785   ), Coef('Var'  , 0.0953188   ), Coef('Var'  , 0.102754    ), Coef('Var'  , 0.109656    ), Coef('Var'  , 0.0941215   ), Coef('Var'  , 0.0782543   ), Coef('Var'  , 0.0641848   ), Coef('Var'  , 0.0492431   ), Coef('Var'  , 0.0603332   ), ], 
		[Coef('Var'  , 0.0756154   ), Coef('Var'  , 0.0860778   ), Coef('Var'  , 0.0934359   ), Coef('Var'  , 0.0880442   ), Coef('Var'  , 0.0806461   ), Coef('Var'  , 0.0659851   ), Coef('Var'  , 0.0496333   ), Coef('Var'  , 0.0496021   ), Coef('Var'  , 0.0471731   ), Coef('Var'  , 0.0630749   ), ], 
		[Coef('Var'  , 0.0683295   ), Coef('Var'  , 0.0748515   ), Coef('Var'  , 0.0798249   ), Coef('Var'  , 0.0731214   ), Coef('Var'  , 0.0652419   ), Coef('Var'  , 0.053636    ), Coef('Var'  , 0.0405464   ), Coef('Var'  , 0.042316    ), Coef('Var'  , 0.0421787   ), Coef('Var'  , 0.0562756   ), ], 
		[Coef('Var'  , 0.0738552   ), Coef('Var'  , 0.0805174   ), Coef('Var'  , 0.0857213   ), Coef('Var'  , 0.0794943   ), Coef('Var'  , 0.0706488   ), Coef('Var'  , 0.0592125   ), Coef('Var'  , 0.0445438   ), Coef('Var'  , 0.0466778   ), Coef('Var'  , 0.0463305   ), Coef('Var'  , 0.0608737   ), ], 
		[Coef('Var'  , 0.101639    ), Coef('Var'  , 0.0961896   ), Coef('Var'  , 0.0914365   ), Coef('Var'  , 0.082394    ), Coef('Var'  , 0.0719661   ), Coef('Var'  , 0.0622397   ), Coef('Var'  , 0.0503329   ), Coef('Var'  , 0.0622975   ), Coef('Var'  , 0.0736383   ), Coef('Var'  , 0.0870813   ), ], 
		[Coef('Var'  , 0.138434    ), Coef('Var'  , 0.119428    ), Coef('Var'  , 0.102321    ), Coef('Var'  , 0.0879564   ), Coef('Var'  , 0.0735342   ), Coef('Var'  , 0.0653779   ), Coef('Var'  , 0.0566326   ), Coef('Var'  , 0.0812816   ), Coef('Var'  , 0.106854    ), Coef('Var'  , 0.121396    ), ], 
		[Coef('Var'  , 0.143784    ), Coef('Var'  , 0.128467    ), Coef('Var'  , 0.115106    ), Coef('Var'  , 0.111613    ), Coef('Var'  , 0.109169    ), Coef('Var'  , 0.129907    ), Coef('Var'  , 0.151779    ), Coef('Var'  , 0.163735    ), Coef('Var'  , 0.177732    ), Coef('Var'  , 0.159427    ), ], 
		[Coef('Var'  , 0.140363    ), Coef('Var'  , 0.127885    ), Coef('Var'  , 0.117453    ), Coef('Var'  , 0.125969    ), Coef('Var'  , 0.13694     ), Coef('Var'  , 0.187966    ), Coef('Var'  , 0.242206    ), Coef('Var'  , 0.241511    ), Coef('Var'  , 0.243996    ), Coef('Var'  , 0.190877    ), ], 
		[Coef('Var'  , 0.110513    ), Coef('Var'  , 0.112775    ), Coef('Var'  , 0.116194    ), Coef('Var'  , 0.129012    ), Coef('Var'  , 0.143828    ), Coef('Var'  , 0.159475    ), Coef('Var'  , 0.177742    ), Coef('Var'  , 0.163935    ), Coef('Var'  , 0.152196    ), Coef('Var'  , 0.130718    ), ], 
		[Coef('Var'  , 0.0774739   ), Coef('Var'  , 0.0905297   ), Coef('Var'  , 0.103188    ), Coef('Var'  , 0.119642    ), Coef('Var'  , 0.138369    ), Coef('Var'  , 0.12208     ), Coef('Var'  , 0.10833     ), Coef('Var'  , 0.0844588   ), Coef('Var'  , 0.0606589   ), Coef('Var'  , 0.0699445   ), ], ])
	etat11.initMat[Chem([Sub('8')])] = FMat([
		[Coef('Var'  , 0.0755101   ), Coef('Var'  , 0.090821    ), Coef('Var'  , 0.106642    ), Coef('Var'  , 0.100325    ), Coef('Var'  , 0.0939318   ), Coef('Var'  , 0.0823353   ), Coef('Var'  , 0.0694422   ), Coef('Var'  , 0.0595184   ), Coef('Var'  , 0.0481366   ), Coef('Var'  , 0.0620057   ), ], 
		[Coef('Var'  , 0.108613    ), Coef('Var'  , 0.123764    ), Coef('Var'  , 0.142106    ), Coef('Var'  , 0.125127    ), Coef('Var'  , 0.110096    ), Coef('Var'  , 0.0966198   ), Coef('Var'  , 0.0820993   ), Coef('Var'  , 0.0726094   ), Coef('Var'  , 0.0615087   ), Coef('Var'  , 0.0845928   ), ], 
		[Coef('Var'  , 0.175126    ), Coef('Var'  , 0.154775    ), Coef('Var'  , 0.137143    ), Coef('Var'  , 0.121803    ), Coef('Var'  , 0.108667    ), Coef('Var'  , 0.107491    ), Coef('Var'  , 0.107083    ), Coef('Var'  , 0.129102    ), Coef('Var'  , 0.15153     ), Coef('Var'  , 0.162555    ), ], 
		[Coef('Var'  , 0.240356    ), Coef('Var'  , 0.186249    ), Coef('Var'  , 0.136186    ), Coef('Var'  , 0.123636    ), Coef('Var'  , 0.114645    ), Coef('Var'  , 0.123193    ), Coef('Var'  , 0.135235    ), Coef('Var'  , 0.185882    ), Coef('Var'  , 0.240323    ), Coef('Var'  , 0.238329    ), ], 
		[Coef('Var'  , 0.149379    ), Coef('Var'  , 0.127223    ), Coef('Var'  , 0.106137    ), Coef('Var'  , 0.105525    ), Coef('Var'  , 0.106393    ), Coef('Var'  , 0.117632    ), Coef('Var'  , 0.132161    ), Coef('Var'  , 0.149425    ), Coef('Var'  , 0.170689    ), Coef('Var'  , 0.158768    ), ], 
		[Coef('Var'  , 0.0588458   ), Coef('Var'  , 0.0681174   ), Coef('Var'  , 0.0760535   ), Coef('Var'  , 0.0898868   ), Coef('Var'  , 0.10328     ), Coef('Var'  , 0.119812    ), Coef('Var'  , 0.138427    ), Coef('Var'  , 0.121541    ), Coef('Var'  , 0.10737     ), Coef('Var'  , 0.0828191   ), ], 
		[Coef('Var'  , 0.0550916   ), Coef('Var'  , 0.0674238   ), Coef('Var'  , 0.0770662   ), Coef('Var'  , 0.090004    ), Coef('Var'  , 0.100997    ), Coef('Var'  , 0.107893    ), Coef('Var'  , 0.11417     ), Coef('Var'  , 0.0984229   ), Coef('Var'  , 0.0821852   ), Coef('Var'  , 0.069493    ), ], 
		[Coef('Var'  , 0.0389773   ), Coef('Var'  , 0.0520942   ), Coef('Var'  , 0.0630264   ), Coef('Var'  , 0.0739094   ), Coef('Var'  , 0.082638    ), Coef('Var'  , 0.0792113   ), Coef('Var'  , 0.0740309   ), Coef('Var'  , 0.0600703   ), Coef('Var'  , 0.0445539   ), Coef('Var'  , 0.0426438   ), ], 
		[Coef('Var'  , 0.0493357   ), Coef('Var'  , 0.0657833   ), Coef('Var'  , 0.0791409   ), Coef('Var'  , 0.0875354   ), Coef('Var'  , 0.0930429   ), Coef('Var'  , 0.0861681   ), Coef('Var'  , 0.0767951   ), Coef('Var'  , 0.0636206   ), Coef('Var'  , 0.0479762   ), Coef('Var'  , 0.0500179   ), ], 
		[Coef('Var'  , 0.0487654   ), Coef('Var'  , 0.0637489   ), Coef('Var'  , 0.0764977   ), Coef('Var'  , 0.0822482   ), Coef('Var'  , 0.0863102   ), Coef('Var'  , 0.0796445   ), Coef('Var'  , 0.0705567   ), Coef('Var'  , 0.059808    ), Coef('Var'  , 0.0457275   ), Coef('Var'  , 0.0487748   ), ], ])
	etat11.initMat[Chem([Sub('9')])] = FMat([
		[Coef('Var'  , 0.0843857   ), Coef('Var'  , 0.0780002   ), Coef('Var'  , 0.069993    ), Coef('Var'  , 0.0568553   ), Coef('Var'  , 0.0422061   ), Coef('Var'  , 0.0428072   ), Coef('Var'  , 0.0419363   ), Coef('Var'  , 0.0565213   ), Coef('Var'  , 0.0694422   ), Coef('Var'  , 0.0777749   ), ], 
		[Coef('Var'  , 0.0940294   ), Coef('Var'  , 0.086462    ), Coef('Var'  , 0.0756154   ), Coef('Var'  , 0.0633951   ), Coef('Var'  , 0.0476807   ), Coef('Var'  , 0.0507827   ), Coef('Var'  , 0.0510007   ), Coef('Var'  , 0.0677699   ), Coef('Var'  , 0.0820993   ), Coef('Var'  , 0.0893527   ), ], 
		[Coef('Var'  , 0.091741    ), Coef('Var'  , 0.080685    ), Coef('Var'  , 0.0683295   ), Coef('Var'  , 0.05972     ), Coef('Var'  , 0.0492342   ), Coef('Var'  , 0.0639434   ), Coef('Var'  , 0.0775266   ), Coef('Var'  , 0.0923914   ), Coef('Var'  , 0.107083    ), Coef('Var'  , 0.0995273   ), ], 
		[Coef('Var'  , 0.100435    ), Coef('Var'  , 0.0870567   ), Coef('Var'  , 0.0738552   ), Coef('Var'  , 0.065962    ), Coef('Var'  , 0.0571189   ), Coef('Var'  , 0.0808021   ), Coef('Var'  , 0.105206    ), Coef('Var'  , 0.118735    ), Coef('Var'  , 0.135235    ), Coef('Var'  , 0.11652     ), ], 
		[Coef('Var'  , 0.104456    ), Coef('Var'  , 0.102       ), Coef('Var'  , 0.101639    ), Coef('Var'  , 0.122804    ), Coef('Var'  , 0.145899    ), Coef('Var'  , 0.156312    ), Coef('Var'  , 0.16977     ), Coef('Var'  , 0.148911    ), Coef('Var'  , 0.132161    ), Coef('Var'  , 0.116584    ), ], 
		[Coef('Var'  , 0.117064    ), Coef('Var'  , 0.126346    ), Coef('Var'  , 0.138434    ), Coef('Var'  , 0.189245    ), Coef('Var'  , 0.24309     ), Coef('Var'  , 0.241435    ), Coef('Var'  , 0.243018    ), Coef('Var'  , 0.189055    ), Coef('Var'  , 0.138427    ), Coef('Var'  , 0.126246    ), ], 
		[Coef('Var'  , 0.117388    ), Coef('Var'  , 0.129717    ), Coef('Var'  , 0.143784    ), Coef('Var'  , 0.159898    ), Coef('Var'  , 0.178611    ), Coef('Var'  , 0.166178    ), Coef('Var'  , 0.155378    ), Coef('Var'  , 0.134627    ), Coef('Var'  , 0.11417     ), Coef('Var'  , 0.115612    ), ], 
		[Coef('Var'  , 0.103575    ), Coef('Var'  , 0.121428    ), Coef('Var'  , 0.140363    ), Coef('Var'  , 0.123287    ), Coef('Var'  , 0.108203    ), Coef('Var'  , 0.0824912   ), Coef('Var'  , 0.0573804   ), Coef('Var'  , 0.0662392   ), Coef('Var'  , 0.0740309   ), Coef('Var'  , 0.0892154   ), ], 
		[Coef('Var'  , 0.100241    ), Coef('Var'  , 0.105328    ), Coef('Var'  , 0.110513    ), Coef('Var'  , 0.0940931   ), Coef('Var'  , 0.0783749   ), Coef('Var'  , 0.0658943   ), Coef('Var'  , 0.0528411   ), Coef('Var'  , 0.0658212   ), Coef('Var'  , 0.0767951   ), Coef('Var'  , 0.089327    ), ], 
		[Coef('Var'  , 0.0866857   ), Coef('Var'  , 0.0829776   ), Coef('Var'  , 0.0774739   ), Coef('Var'  , 0.0647409   ), Coef('Var'  , 0.0495829   ), Coef('Var'  , 0.0493543   ), Coef('Var'  , 0.0459444   ), Coef('Var'  , 0.059929    ), Coef('Var'  , 0.0705567   ), Coef('Var'  , 0.0798404   ), ], ])
	etat11.initMat[Chem([Sub('10')])] = FMat([
		[Coef('Var'  , 0.0953188   ), Coef('Var'  , 0.0904839   ), Coef('Var'  , 0.0843857   ), Coef('Var'  , 0.089766    ), Coef('Var'  , 0.0939318   ), Coef('Var'  , 0.10264     ), Coef('Var'  , 0.111506    ), Coef('Var'  , 0.111556    ), Coef('Var'  , 0.112612    ), Coef('Var'  , 0.10396     ), ], 
		[Coef('Var'  , 0.0934359   ), Coef('Var'  , 0.0950483   ), Coef('Var'  , 0.0940294   ), Coef('Var'  , 0.1027      ), Coef('Var'  , 0.110096    ), Coef('Var'  , 0.116184    ), Coef('Var'  , 0.123573    ), Coef('Var'  , 0.116156    ), Coef('Var'  , 0.110076    ), Coef('Var'  , 0.102288    ), ], 
		[Coef('Var'  , 0.0798249   ), Coef('Var'  , 0.0862107   ), Coef('Var'  , 0.091741    ), Coef('Var'  , 0.100008    ), Coef('Var'  , 0.108667    ), Coef('Var'  , 0.106665    ), Coef('Var'  , 0.10633     ), Coef('Var'  , 0.0965734   ), Coef('Var'  , 0.0879491   ), Coef('Var'  , 0.0840831   ), ], 
		[Coef('Var'  , 0.0857213   ), Coef('Var'  , 0.0931426   ), Coef('Var'  , 0.100435    ), Coef('Var'  , 0.106355    ), Coef('Var'  , 0.114645    ), Coef('Var'  , 0.108341    ), Coef('Var'  , 0.103837    ), Coef('Var'  , 0.096595    ), Coef('Var'  , 0.0882064   ), Coef('Var'  , 0.0880699   ), ], 
		[Coef('Var'  , 0.0914365   ), Coef('Var'  , 0.0973708   ), Coef('Var'  , 0.104456    ), Coef('Var'  , 0.104229    ), Coef('Var'  , 0.106393    ), Coef('Var'  , 0.100232    ), Coef('Var'  , 0.0947589   ), Coef('Var'  , 0.0913902   ), Coef('Var'  , 0.086454    ), Coef('Var'  , 0.0895764   ), ], 
		[Coef('Var'  , 0.102321    ), Coef('Var'  , 0.10881     ), Coef('Var'  , 0.117064    ), Coef('Var'  , 0.109293    ), Coef('Var'  , 0.10328     ), Coef('Var'  , 0.0948748   ), Coef('Var'  , 0.0859067   ), Coef('Var'  , 0.086399    ), Coef('Var'  , 0.0850129   ), Coef('Var'  , 0.0939      ), ], 
		[Coef('Var'  , 0.115106    ), Coef('Var'  , 0.115732    ), Coef('Var'  , 0.117388    ), Coef('Var'  , 0.109262    ), Coef('Var'  , 0.100997    ), Coef('Var'  , 0.095789    ), Coef('Var'  , 0.0892471   ), Coef('Var'  , 0.0935644   ), Coef('Var'  , 0.0969756   ), Coef('Var'  , 0.105788    ), ], 
		[Coef('Var'  , 0.117453    ), Coef('Var'  , 0.110066    ), Coef('Var'  , 0.103575    ), Coef('Var'  , 0.093604    ), Coef('Var'  , 0.082638    ), Coef('Var'  , 0.08211     ), Coef('Var'  , 0.0799933   ), Coef('Var'  , 0.0897045   ), Coef('Var'  , 0.0992985   ), Coef('Var'  , 0.107656    ), ], 
		[Coef('Var'  , 0.116194    ), Coef('Var'  , 0.108082    ), Coef('Var'  , 0.100241    ), Coef('Var'  , 0.0974764   ), Coef('Var'  , 0.0930429   ), Coef('Var'  , 0.0986463   ), Coef('Var'  , 0.102309    ), Coef('Var'  , 0.10985     ), Coef('Var'  , 0.117277    ), Coef('Var'  , 0.116127    ), ], 
		[Coef('Var'  , 0.103188    ), Coef('Var'  , 0.0950545   ), Coef('Var'  , 0.0866857   ), Coef('Var'  , 0.0873065   ), Coef('Var'  , 0.0863102   ), Coef('Var'  , 0.094518    ), Coef('Var'  , 0.102539    ), Coef('Var'  , 0.108211    ), Coef('Var'  , 0.116139    ), Coef('Var'  , 0.108552    ), ], ])
	
	
	
	etat12.bords   = {Bord('0'): etat13, Bord('1'): etat13, Bord('2'): etat13, Bord('3'): etat13, Bord('4'): etat13, }
	etat12.permuts = {}
	etat12.interns = {Intern('_'): etat12, }
	etat12.subs    = {Sub('0'): etat1, Sub('1'): etat2, Sub('2'): etat3, Sub('3'): etat4, Sub('G', True): Etat.etatPoint, Sub('4'): etat5, Sub('5'): etat6, Sub('6'): etat7, Sub('7'): etat8, Sub('8'): etat9, Sub('9'): etat10, Sub('10'): etat11, }
	
	etat12.buildIntern()
	
	
	etat12.eqs = [
		(Chem([Bord('4'), Sub('0'), Permut('0'), ])	,	Chem([Sub('0'), Bord('1'), ])),
		(Chem([Bord('3'), Sub('1'), Permut('0'), ])	,	Chem([Sub('0'), Bord('2'), ])),
		(Chem([Bord('3'), Sub('0'), Permut('0'), ])	,	Chem([Sub('6'), Bord('2'), ])),
		(Chem([Bord('2'), Sub('1'), Permut('0'), ])	,	Chem([Sub('6'), Bord('3'), ])),
		(Chem([Bord('0'), Sub('0'), Permut('0'), ])	,	Chem([Sub('7'), Bord('0'), ])),
		(Chem([Bord('4'), Sub('1'), Permut('0'), ])	,	Chem([Sub('7'), Bord('1'), ])),
		(Chem([Bord('2'), Sub('0'), Permut('0'), ])	,	Chem([Sub('8'), Bord('1'), ])),
		(Chem([Bord('1'), Sub('1'), Permut('0'), ])	,	Chem([Sub('8'), Bord('2'), ])),
		(Chem([Bord('0'), Sub('1'), Permut('0'), ])	,	Chem([Sub('9'), Bord('0'), ])),
		(Chem([Bord('1'), Sub('0'), Permut('0'), ])	,	Chem([Sub('9'), Bord('4'), ])),
		(Chem([Sub('0'), Bord('0'), Bord('1'), ])	,	Chem([Sub('7'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('2'), Bord('1'), ])	,	Chem([Sub('6'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('3'), Bord('1'), ])	,	Chem([Sub('5'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('4'), Bord('1'), ])	,	Chem([Sub('1'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('0'), Bord('1'), ])	,	Chem([Sub('10'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('1'), Bord('1'), ])	,	Chem([Sub('2'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('2'), Bord('1'), ])	,	Chem([Sub('7'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('4'), Bord('1'), ])	,	Chem([Sub('5'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('0'), Bord('1'), ])	,	Chem([Sub('9'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('1'), Bord('1'), ])	,	Chem([Sub('7'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('3'), Bord('1'), ])	,	Chem([Sub('10'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('4'), Bord('1'), ])	,	Chem([Sub('4'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('3'), Bord('0'), Bord('1'), ])	,	Chem([Sub('5'), Bord('4'), Bord('1'), ])),
		(Chem([Sub('3'), Bord('1'), Bord('1'), ])	,	Chem([Sub('6'), Bord('4'), Bord('1'), ])),
		(Chem([Sub('3'), Bord('2'), Bord('1'), ])	,	Chem([Sub('8'), Bord('4'), Bord('1'), ])),
		(Chem([Sub('3'), Bord('3'), Bord('1'), ])	,	Chem([Sub('4'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('3'), Bord('4'), Bord('1'), ])	,	Chem([Sub('10'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('4'), Bord('1'), Bord('1'), ])	,	Chem([Sub('8'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('4'), Bord('2'), Bord('1'), ])	,	Chem([Sub('9'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('4'), Bord('4'), Bord('1'), ])	,	Chem([Sub('10'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('5'), Bord('0'), Bord('1'), ])	,	Chem([Sub('10'), Bord('4'), Bord('1'), ])),
		(Chem([Sub('5'), Bord('3'), Bord('1'), ])	,	Chem([Sub('6'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('6'), Bord('3'), Bord('1'), ])	,	Chem([Sub('8'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('7'), Bord('4'), Bord('1'), ])	,	Chem([Sub('9'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('8'), Bord('2'), Bord('1'), ])	,	Chem([Sub('9'), Bord('3'), Bord('1'), ])),
		(Chem([Bord('0'), Bord('1'), ])	,	Chem([Bord('1'), Bord('0'), ])),
		(Chem([Bord('1'), Bord('1'), ])	,	Chem([Bord('2'), Bord('0'), ])),
		(Chem([Bord('2'), Bord('1'), ])	,	Chem([Bord('3'), Bord('0'), ])),
		(Chem([Bord('3'), Bord('1'), ])	,	Chem([Bord('4'), Bord('0'), ])),
		(Chem([Bord('4'), Bord('1'), ])	,	Chem([Bord('0'), Bord('0'), ])),
		]
	
	
	etat12.prim.elems = [Figure(2, [Chem([Bord('0'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('0'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('0'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('0'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('1'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('1'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('1'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('1'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('2'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('2'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('2'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('2'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('3'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('3'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('3'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('3'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('4'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('4'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('4'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('4'), Sub('1'), Sub('1'), Bord('0'), ]), ])]
	etat12.grid.elems = [
		Figure(1, [Chem([Bord('1'), Bord('0'), ]), Chem([Bord('1'), Intern(''), ]), Chem([Bord('1'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('4'), Bord('0'), ]), Chem([Bord('4'), Intern(''), ]), Chem([Bord('4'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('2'), Bord('0'), ]), Chem([Bord('2'), Intern(''), ]), Chem([Bord('2'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('0'), Bord('0'), ]), Chem([Bord('0'), Intern(''), ]), Chem([Bord('0'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('3'), Bord('0'), ]), Chem([Bord('3'), Intern(''), ]), Chem([Bord('3'), Bord('1'), ]), ]), ]
	
	
	etat12.space = [Chem([Bord('4'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('2'), Intern('0'), Intern('0'), ]), Chem([Bord('2'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('3'), Intern('0'), Intern('0'), ]), Chem([Bord('4'), Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('4'), Intern('0'), Intern('0'), ]), ]
	
	etat12.initMat[Chem([Sub('0')])] = FMat([
		[Coef('Var'  , 0.155775    ), Coef('Var'  , 0.202675    ), Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0408413   ), Coef('Var'  , 0.0815883   ), Coef('Var'  , 0.118516    ), ], 
		[Coef('Var'  , 0.0667423   ), Coef('Var'  , 0.033856    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.027507    ), Coef('Var'  , 0.0536876   ), Coef('Var'  , 0.061363    ), ], 
		[Coef('Var'  , 0.0399673   ), Coef('Var'  , 0.020047    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.018447    ), Coef('Var'  , 0.0361241   ), Coef('Var'  , 0.038494    ), ], 
		[Coef('Var'  , 0.0513903   ), Coef('Var'  , 0.0266677   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0261472   ), Coef('Var'  , 0.0504981   ), Coef('Var'  , 0.0528149   ), ], 
		[Coef('Var'  , 0.0537041   ), Coef('Var'  , 0.0278171   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.030698    ), Coef('Var'  , 0.0598196   ), Coef('Var'  , 0.058515    ), ], 
		[Coef('Var'  , 0.0460469   ), Coef('Var'  , 0.0234546   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0292913   ), Coef('Var'  , 0.0582825   ), Coef('Var'  , 0.0527459   ), ], 
		[Coef('Var'  , 0.0793583   ), Coef('Var'  , 0.0398021   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.200133    ), Coef('Var'  , 0.150977    ), Coef('Var'  , 0.114935    ), ], 
		[Coef('Var'  , 0.0994584   ), Coef('Var'  , 0.0488058   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.366663    ), Coef('Var'  , 0.235656    ), Coef('Var'  , 0.165469    ), ], 
		[Coef('Var'  , 0.16289     ), Coef('Var'  , 0.20526     ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.205618    ), Coef('Var'  , 0.163431    ), Coef('Var'  , 0.160878    ), ], 
		[Coef('Var'  , 0.244667    ), Coef('Var'  , 0.371615    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0546532   ), Coef('Var'  , 0.109936    ), Coef('Var'  , 0.176268    ), ], ])
	etat12.initMat[Chem([Sub('1')])] = FMat([
		[Coef('Var'  , 0.113831    ), Coef('Var'  , 0.116206    ), Coef('Var'  , 0.119977    ), Coef('Var'  , 0.133525    ), Coef('Var'  , 0.148978    ), Coef('Var'  , 0.164651    ), Coef('Var'  , 0.182179    ), Coef('Var'  , 0.168364    ), Coef('Var'  , 0.155775    ), Coef('Var'  , 0.134318    ), ], 
		[Coef('Var'  , 0.0865421   ), Coef('Var'  , 0.102195    ), Coef('Var'  , 0.116209    ), Coef('Var'  , 0.133714    ), Coef('Var'  , 0.15148     ), Coef('Var'  , 0.13386     ), Coef('Var'  , 0.116961    ), Coef('Var'  , 0.0922693   ), Coef('Var'  , 0.0667423   ), Coef('Var'  , 0.0777835   ), ], 
		[Coef('Var'  , 0.0576052   ), Coef('Var'  , 0.0674767   ), Coef('Var'  , 0.077158    ), Coef('Var'  , 0.0827497   ), Coef('Var'  , 0.0900308   ), Coef('Var'  , 0.076277    ), Coef('Var'  , 0.0648149   ), Coef('Var'  , 0.0519768   ), Coef('Var'  , 0.0399673   ), Coef('Var'  , 0.049121    ), ], 
		[Coef('Var'  , 0.0790314   ), Coef('Var'  , 0.0897562   ), Coef('Var'  , 0.0972722   ), Coef('Var'  , 0.0934381   ), Coef('Var'  , 0.0869318   ), Coef('Var'  , 0.072925    ), Coef('Var'  , 0.0557284   ), Coef('Var'  , 0.0554194   ), Coef('Var'  , 0.0513903   ), Coef('Var'  , 0.067159    ), ], 
		[Coef('Var'  , 0.0850238   ), Coef('Var'  , 0.0927822   ), Coef('Var'  , 0.0971004   ), Coef('Var'  , 0.0893188   ), Coef('Var'  , 0.0789631   ), Coef('Var'  , 0.0659864   ), Coef('Var'  , 0.0503576   ), Coef('Var'  , 0.0537217   ), Coef('Var'  , 0.0537041   ), Coef('Var'  , 0.0713623   ), ], 
		[Coef('Var'  , 0.0754618   ), Coef('Var'  , 0.0811946   ), Coef('Var'  , 0.0854156   ), Coef('Var'  , 0.0772728   ), Coef('Var'  , 0.0670167   ), Coef('Var'  , 0.0556534   ), Coef('Var'  , 0.041803    ), Coef('Var'  , 0.0449529   ), Coef('Var'  , 0.0460469   ), Coef('Var'  , 0.0615314   ), ], 
		[Coef('Var'  , 0.108962    ), Coef('Var'  , 0.10365     ), Coef('Var'  , 0.0982239   ), Coef('Var'  , 0.089063    ), Coef('Var'  , 0.0777844   ), Coef('Var'  , 0.0681167   ), Coef('Var'  , 0.0553328   ), Coef('Var'  , 0.0681899   ), Coef('Var'  , 0.0793583   ), Coef('Var'  , 0.0941185   ), ], 
		[Coef('Var'  , 0.129229    ), Coef('Var'  , 0.110863    ), Coef('Var'  , 0.0949864   ), Coef('Var'  , 0.0815564   ), Coef('Var'  , 0.0679698   ), Coef('Var'  , 0.0598636   ), Coef('Var'  , 0.0514872   ), Coef('Var'  , 0.0744107   ), Coef('Var'  , 0.0994584   ), Coef('Var'  , 0.112371    ), ], 
		[Coef('Var'  , 0.122956    ), Coef('Var'  , 0.107487    ), Coef('Var'  , 0.0956548   ), Coef('Var'  , 0.0935779   ), Coef('Var'  , 0.0939561   ), Coef('Var'  , 0.115186    ), Coef('Var'  , 0.139375    ), Coef('Var'  , 0.149059    ), Coef('Var'  , 0.16289     ), Coef('Var'  , 0.140555    ), ], 
		[Coef('Var'  , 0.141358    ), Coef('Var'  , 0.12839     ), Coef('Var'  , 0.118002    ), Coef('Var'  , 0.125785    ), Coef('Var'  , 0.136889    ), Coef('Var'  , 0.187481    ), Coef('Var'  , 0.241961    ), Coef('Var'  , 0.241636    ), Coef('Var'  , 0.244667    ), Coef('Var'  , 0.19168     ), ], ])
	etat12.initMat[Chem([Sub('2')])] = FMat([
		[Coef('Var'  , 0.117531    ), Coef('Var'  , 0.137247    ), Coef('Var'  , 0.157445    ), Coef('Var'  , 0.169289    ), Coef('Var'  , 0.182438    ), Coef('Var'  , 0.164744    ), Coef('Var'  , 0.148978    ), Coef('Var'  , 0.134884    ), Coef('Var'  , 0.122265    ), Coef('Var'  , 0.119662    ), ], 
		[Coef('Var'  , 0.143686    ), Coef('Var'  , 0.193501    ), Coef('Var'  , 0.246837    ), Coef('Var'  , 0.247727    ), Coef('Var'  , 0.251346    ), Coef('Var'  , 0.200621    ), Coef('Var'  , 0.15148     ), Coef('Var'  , 0.138799    ), Coef('Var'  , 0.127646    ), Coef('Var'  , 0.134299    ), ], 
		[Coef('Var'  , 0.125858    ), Coef('Var'  , 0.14418     ), Coef('Var'  , 0.166152    ), Coef('Var'  , 0.151062    ), Coef('Var'  , 0.139086    ), Coef('Var'  , 0.11319     ), Coef('Var'  , 0.0900308   ), Coef('Var'  , 0.090375    ), Coef('Var'  , 0.0934965   ), Coef('Var'  , 0.107989    ), ], 
		[Coef('Var'  , 0.146483    ), Coef('Var'  , 0.129135    ), Coef('Var'  , 0.11388     ), Coef('Var'  , 0.0906158   ), Coef('Var'  , 0.0668421   ), Coef('Var'  , 0.0781508   ), Coef('Var'  , 0.0869318   ), Coef('Var'  , 0.1007      ), Coef('Var'  , 0.113348    ), Coef('Var'  , 0.129023    ), ], 
		[Coef('Var'  , 0.110022    ), Coef('Var'  , 0.0934054   ), Coef('Var'  , 0.0779015   ), Coef('Var'  , 0.0661092   ), Coef('Var'  , 0.0538866   ), Coef('Var'  , 0.0674213   ), Coef('Var'  , 0.0789631   ), Coef('Var'  , 0.0908922   ), Coef('Var'  , 0.101431    ), Coef('Var'  , 0.105446    ), ], 
		[Coef('Var'  , 0.0748888   ), Coef('Var'  , 0.0610714   ), Coef('Var'  , 0.0457027   ), Coef('Var'  , 0.0447532   ), Coef('Var'  , 0.0417394   ), Coef('Var'  , 0.0556233   ), Coef('Var'  , 0.0670167   ), Coef('Var'  , 0.0771231   ), Coef('Var'  , 0.0851239   ), Coef('Var'  , 0.0807545   ), ], 
		[Coef('Var'  , 0.0756435   ), Coef('Var'  , 0.0633425   ), Coef('Var'  , 0.0483261   ), Coef('Var'  , 0.0506175   ), Coef('Var'  , 0.0497466   ), Coef('Var'  , 0.0654657   ), Coef('Var'  , 0.0777844   ), Coef('Var'  , 0.0854781   ), Coef('Var'  , 0.090351    ), Coef('Var'  , 0.0842108   ), ], 
		[Coef('Var'  , 0.0635407   ), Coef('Var'  , 0.052929    ), Coef('Var'  , 0.0394132   ), Coef('Var'  , 0.0412902   ), Coef('Var'  , 0.0412643   ), Coef('Var'  , 0.0552007   ), Coef('Var'  , 0.0679698   ), Coef('Var'  , 0.074365    ), Coef('Var'  , 0.0791194   ), Coef('Var'  , 0.0726869   ), ], 
		[Coef('Var'  , 0.0681033   ), Coef('Var'  , 0.0591552   ), Coef('Var'  , 0.0475261   ), Coef('Var'  , 0.057983    ), Coef('Var'  , 0.0682396   ), Coef('Var'  , 0.0801085   ), Coef('Var'  , 0.0939561   ), Coef('Var'  , 0.0890971   ), Coef('Var'  , 0.0850302   ), Coef('Var'  , 0.0776049   ), ], 
		[Coef('Var'  , 0.0742441   ), Coef('Var'  , 0.066033    ), Coef('Var'  , 0.0568172   ), Coef('Var'  , 0.0805519   ), Coef('Var'  , 0.105411    ), Coef('Var'  , 0.119475    ), Coef('Var'  , 0.136889    ), Coef('Var'  , 0.118288    ), Coef('Var'  , 0.10219     ), Coef('Var'  , 0.0883237   ), ], ])
	etat12.initMat[Chem([Sub('3')])] = FMat([
		[Coef('Var'  , 0.0964527   ), Coef('Var'  , 0.0894619   ), Coef('Var'  , 0.0800123   ), Coef('Var'  , 0.0668505   ), Coef('Var'  , 0.0508894   ), Coef('Var'  , 0.0530828   ), Coef('Var'  , 0.0521046   ), Coef('Var'  , 0.0691175   ), Coef('Var'  , 0.0827811   ), Coef('Var'  , 0.0910583   ), ], 
		[Coef('Var'  , 0.0917184   ), Coef('Var'  , 0.084372    ), Coef('Var'  , 0.074643    ), Coef('Var'  , 0.0620494   ), Coef('Var'  , 0.0464231   ), Coef('Var'  , 0.048624    ), Coef('Var'  , 0.0484178   ), Coef('Var'  , 0.0642227   ), Coef('Var'  , 0.0785206   ), Coef('Var'  , 0.0857964   ), ], 
		[Coef('Var'  , 0.0828491   ), Coef('Var'  , 0.0737085   ), Coef('Var'  , 0.0631045   ), Coef('Var'  , 0.0556488   ), Coef('Var'  , 0.045983    ), Coef('Var'  , 0.0593887   ), Coef('Var'  , 0.071884    ), Coef('Var'  , 0.0844656   ), Coef('Var'  , 0.0976366   ), Coef('Var'  , 0.0900912   ), ], 
		[Coef('Var'  , 0.111128    ), Coef('Var'  , 0.0974588   ), Coef('Var'  , 0.0832788   ), Coef('Var'  , 0.0742137   ), Coef('Var'  , 0.0635115   ), Coef('Var'  , 0.087565    ), Coef('Var'  , 0.111794    ), Coef('Var'  , 0.127079    ), Coef('Var'  , 0.144809    ), Coef('Var'  , 0.126929    ), ], 
		[Coef('Var'  , 0.120738    ), Coef('Var'  , 0.118994    ), Coef('Var'  , 0.117572    ), Coef('Var'  , 0.136753    ), Coef('Var'  , 0.15641     ), Coef('Var'  , 0.16657     ), Coef('Var'  , 0.178661    ), Coef('Var'  , 0.160238    ), Coef('Var'  , 0.144674    ), Coef('Var'  , 0.131782    ), ], 
		[Coef('Var'  , 0.120134    ), Coef('Var'  , 0.129677    ), Coef('Var'  , 0.141426    ), Coef('Var'  , 0.191692    ), Coef('Var'  , 0.244731    ), Coef('Var'  , 0.242762    ), Coef('Var'  , 0.244006    ), Coef('Var'  , 0.19057     ), Coef('Var'  , 0.140273    ), Coef('Var'  , 0.12899     ), ], 
		[Coef('Var'  , 0.110401    ), Coef('Var'  , 0.121836    ), Coef('Var'  , 0.136324    ), Coef('Var'  , 0.152505    ), Coef('Var'  , 0.172647    ), Coef('Var'  , 0.160038    ), Coef('Var'  , 0.150071    ), Coef('Var'  , 0.128406    ), Coef('Var'  , 0.107845    ), Coef('Var'  , 0.108477    ), ], 
		[Coef('Var'  , 0.0955007   ), Coef('Var'  , 0.112312    ), Coef('Var'  , 0.131383    ), Coef('Var'  , 0.115374    ), Coef('Var'  , 0.102297    ), Coef('Var'  , 0.0772827   ), Coef('Var'  , 0.0533984   ), Coef('Var'  , 0.0613056   ), Coef('Var'  , 0.0686822   ), Coef('Var'  , 0.0820471   ), ], 
		[Coef('Var'  , 0.0839289   ), Coef('Var'  , 0.0885673   ), Coef('Var'  , 0.0942814   ), Coef('Var'  , 0.0808571   ), Coef('Var'  , 0.069064    ), Coef('Var'  , 0.0581931   ), Coef('Var'  , 0.0469495   ), Coef('Var'  , 0.0579236   ), Coef('Var'  , 0.0666905   ), Coef('Var'  , 0.0759841   ), ], 
		[Coef('Var'  , 0.0871497   ), Coef('Var'  , 0.0836129   ), Coef('Var'  , 0.0779746   ), Coef('Var'  , 0.0640559   ), Coef('Var'  , 0.0480436   ), Coef('Var'  , 0.0464936   ), Coef('Var'  , 0.0427125   ), Coef('Var'  , 0.0566715   ), Coef('Var'  , 0.0680879   ), Coef('Var'  , 0.0788455   ), ], ])
	etat12.initMat[Chem([Sub('G')])] = FMat([
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
	etat12.initMat[Chem([Sub('4')])] = FMat([
		[Coef('Var'  , 0.106909    ), Coef('Var'  , 0.0961007   ), Coef('Var'  , 0.0827811   ), Coef('Var'  , 0.0717814   ), Coef('Var'  , 0.0578535   ), Coef('Var'  , 0.0714636   ), Coef('Var'  , 0.0837005   ), Coef('Var'  , 0.100663    ), Coef('Var'  , 0.117531    ), Coef('Var'  , 0.1126      ), ], 
		[Coef('Var'  , 0.108981    ), Coef('Var'  , 0.0937405   ), Coef('Var'  , 0.0785206   ), Coef('Var'  , 0.0693635   ), Coef('Var'  , 0.0594498   ), Coef('Var'  , 0.083797    ), Coef('Var'  , 0.109235    ), Coef('Var'  , 0.124917    ), Coef('Var'  , 0.143686    ), Coef('Var'  , 0.125152    ), ], 
		[Coef('Var'  , 0.0968692   ), Coef('Var'  , 0.0964292   ), Coef('Var'  , 0.0976366   ), Coef('Var'  , 0.120551    ), Coef('Var'  , 0.14477     ), Coef('Var'  , 0.155011    ), Coef('Var'  , 0.167603    ), Coef('Var'  , 0.144975    ), Coef('Var'  , 0.125858    ), Coef('Var'  , 0.109836    ), ], 
		[Coef('Var'  , 0.125118    ), Coef('Var'  , 0.133395    ), Coef('Var'  , 0.144809    ), Coef('Var'  , 0.19468     ), Coef('Var'  , 0.24761     ), Coef('Var'  , 0.246668    ), Coef('Var'  , 0.248542    ), Coef('Var'  , 0.196084    ), Coef('Var'  , 0.146483    ), Coef('Var'  , 0.134293    ), ], 
		[Coef('Var'  , 0.117032    ), Coef('Var'  , 0.129706    ), Coef('Var'  , 0.144674    ), Coef('Var'  , 0.159595    ), Coef('Var'  , 0.17745     ), Coef('Var'  , 0.163178    ), Coef('Var'  , 0.151355    ), Coef('Var'  , 0.129823    ), Coef('Var'  , 0.110022    ), Coef('Var'  , 0.112737    ), ], 
		[Coef('Var'  , 0.104369    ), Coef('Var'  , 0.121464    ), Coef('Var'  , 0.140273    ), Coef('Var'  , 0.122671    ), Coef('Var'  , 0.107647    ), Coef('Var'  , 0.0821833   ), Coef('Var'  , 0.0575988   ), Coef('Var'  , 0.0667053   ), Coef('Var'  , 0.0748888   ), Coef('Var'  , 0.0898437   ), ], 
		[Coef('Var'  , 0.0970647   ), Coef('Var'  , 0.102478    ), Coef('Var'  , 0.107845    ), Coef('Var'  , 0.0926832   ), Coef('Var'  , 0.0777937   ), Coef('Var'  , 0.0659383   ), Coef('Var'  , 0.053026    ), Coef('Var'  , 0.0654742   ), Coef('Var'  , 0.0756435   ), Coef('Var'  , 0.0871821   ), ], 
		[Coef('Var'  , 0.0791196   ), Coef('Var'  , 0.0745857   ), Coef('Var'  , 0.0686822   ), Coef('Var'  , 0.0560012   ), Coef('Var'  , 0.042179    ), Coef('Var'  , 0.0418848   ), Coef('Var'  , 0.0396158   ), Coef('Var'  , 0.0530299   ), Coef('Var'  , 0.0635407   ), Coef('Var'  , 0.0726008   ), ], 
		[Coef('Var'  , 0.0791719   ), Coef('Var'  , 0.0742165   ), Coef('Var'  , 0.0666905   ), Coef('Var'  , 0.0562822   ), Coef('Var'  , 0.0430855   ), Coef('Var'  , 0.0449871   ), Coef('Var'  , 0.0437794   ), Coef('Var'  , 0.0576013   ), Coef('Var'  , 0.0681033   ), Coef('Var'  , 0.0751085   ), ], 
		[Coef('Var'  , 0.0853663   ), Coef('Var'  , 0.077885    ), Coef('Var'  , 0.0680879   ), Coef('Var'  , 0.056391    ), Coef('Var'  , 0.0421613   ), Coef('Var'  , 0.0448885   ), Coef('Var'  , 0.0455452   ), Coef('Var'  , 0.0607267   ), Coef('Var'  , 0.0742441   ), Coef('Var'  , 0.0806478   ), ], ])
	etat12.initMat[Chem([Sub('5')])] = FMat([
		[Coef('Var'  , 0.0800123   ), Coef('Var'  , 0.0922192   ), Coef('Var'  , 0.103067    ), Coef('Var'  , 0.108218    ), Coef('Var'  , 0.113831    ), Coef('Var'  , 0.0974842   ), Coef('Var'  , 0.0815883   ), Coef('Var'  , 0.069367    ), Coef('Var'  , 0.0559371   ), Coef('Var'  , 0.0691701   ), ], 
		[Coef('Var'  , 0.074643    ), Coef('Var'  , 0.0865558   ), Coef('Var'  , 0.0956619   ), Coef('Var'  , 0.0923715   ), Coef('Var'  , 0.0865421   ), Coef('Var'  , 0.0714345   ), Coef('Var'  , 0.0536876   ), Coef('Var'  , 0.0520577   ), Coef('Var'  , 0.047615    ), Coef('Var'  , 0.0626626   ), ], 
		[Coef('Var'  , 0.0631045   ), Coef('Var'  , 0.0684729   ), Coef('Var'  , 0.0718996   ), Coef('Var'  , 0.0653754   ), Coef('Var'  , 0.0576052   ), Coef('Var'  , 0.0475211   ), Coef('Var'  , 0.0361241   ), Coef('Var'  , 0.0387047   ), Coef('Var'  , 0.0393054   ), Coef('Var'  , 0.0524292   ), ], 
		[Coef('Var'  , 0.0832788   ), Coef('Var'  , 0.0905901   ), Coef('Var'  , 0.0957953   ), Coef('Var'  , 0.0889525   ), Coef('Var'  , 0.0790314   ), Coef('Var'  , 0.0666386   ), Coef('Var'  , 0.0504981   ), Coef('Var'  , 0.0531371   ), Coef('Var'  , 0.0526595   ), Coef('Var'  , 0.0691189   ), ], 
		[Coef('Var'  , 0.117572    ), Coef('Var'  , 0.113254    ), Coef('Var'  , 0.107851    ), Coef('Var'  , 0.097982    ), Coef('Var'  , 0.0850238   ), Coef('Var'  , 0.0742432   ), Coef('Var'  , 0.0598196   ), Coef('Var'  , 0.0730175   ), Coef('Var'  , 0.0843312   ), Coef('Var'  , 0.101136    ), ], 
		[Coef('Var'  , 0.141426    ), Coef('Var'  , 0.122552    ), Coef('Var'  , 0.105089    ), Coef('Var'  , 0.0905355   ), Coef('Var'  , 0.0754618   ), Coef('Var'  , 0.0673681   ), Coef('Var'  , 0.0582825   ), Coef('Var'  , 0.0832237   ), Coef('Var'  , 0.108774    ), Coef('Var'  , 0.124026    ), ], 
		[Coef('Var'  , 0.136324    ), Coef('Var'  , 0.122038    ), Coef('Var'  , 0.11084     ), Coef('Var'  , 0.109238    ), Coef('Var'  , 0.108962    ), Coef('Var'  , 0.12945     ), Coef('Var'  , 0.150977    ), Coef('Var'  , 0.160651    ), Coef('Var'  , 0.172875    ), Coef('Var'  , 0.152633    ), ], 
		[Coef('Var'  , 0.131383    ), Coef('Var'  , 0.118505    ), Coef('Var'  , 0.108789    ), Coef('Var'  , 0.117239    ), Coef('Var'  , 0.129229    ), Coef('Var'  , 0.180228    ), Coef('Var'  , 0.235656    ), Coef('Var'  , 0.234323    ), Coef('Var'  , 0.237296    ), Coef('Var'  , 0.18249     ), ], 
		[Coef('Var'  , 0.0942814   ), Coef('Var'  , 0.0935134   ), Coef('Var'  , 0.0952727   ), Coef('Var'  , 0.107223    ), Coef('Var'  , 0.122956    ), Coef('Var'  , 0.140914    ), Coef('Var'  , 0.163431    ), Coef('Var'  , 0.15024     ), Coef('Var'  , 0.140624    ), Coef('Var'  , 0.116207    ), ], 
		[Coef('Var'  , 0.0779746   ), Coef('Var'  , 0.0923003   ), Coef('Var'  , 0.105735    ), Coef('Var'  , 0.122865    ), Coef('Var'  , 0.141358    ), Coef('Var'  , 0.124718    ), Coef('Var'  , 0.109936    ), Coef('Var'  , 0.0852783   ), Coef('Var'  , 0.0605825   ), Coef('Var'  , 0.0701257   ), ], ])
	etat12.initMat[Chem([Sub('6')])] = FMat([
		[Coef('Var'  , 0.0508894   ), Coef('Var'  , 0.0547318   ), Coef('Var'  , 0.0559371   ), Coef('Var'  , 0.0285257   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0262061   ), ], 
		[Coef('Var'  , 0.0464231   ), Coef('Var'  , 0.0484883   ), Coef('Var'  , 0.047615    ), Coef('Var'  , 0.0245508   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0239376   ), ], 
		[Coef('Var'  , 0.045983    ), Coef('Var'  , 0.043735    ), Coef('Var'  , 0.0393054   ), Coef('Var'  , 0.0202577   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0234773   ), ], 
		[Coef('Var'  , 0.0635115   ), Coef('Var'  , 0.0590746   ), Coef('Var'  , 0.0526595   ), Coef('Var'  , 0.0269899   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0320847   ), ], 
		[Coef('Var'  , 0.15641     ), Coef('Var'  , 0.120256    ), Coef('Var'  , 0.0843312   ), Coef('Var'  , 0.0423196   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.202936    ), ], 
		[Coef('Var'  , 0.244731    ), Coef('Var'  , 0.175531    ), Coef('Var'  , 0.108774    ), Coef('Var'  , 0.0539324   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.371599    ), ], 
		[Coef('Var'  , 0.172647    ), Coef('Var'  , 0.170907    ), Coef('Var'  , 0.172875    ), Coef('Var'  , 0.210518    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.210389    ), ], 
		[Coef('Var'  , 0.102297    ), Coef('Var'  , 0.168202    ), Coef('Var'  , 0.237296    ), Coef('Var'  , 0.367659    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0505427   ), ], 
		[Coef('Var'  , 0.069064    ), Coef('Var'  , 0.103893    ), Coef('Var'  , 0.140624    ), Coef('Var'  , 0.194622    ), Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0342716   ), ], 
		[Coef('Var'  , 0.0480436   ), Coef('Var'  , 0.0551804   ), Coef('Var'  , 0.0605825   ), Coef('Var'  , 0.0306251   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0245553   ), ], ])
	etat12.initMat[Chem([Sub('7')])] = FMat([
		[Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.215689    ), Coef('Var'  , 0.182179    ), Coef('Var'  , 0.181472    ), Coef('Var'  , 0.182438    ), Coef('Var'  , 0.215783    ), ], 
		[Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0584133   ), Coef('Var'  , 0.116961    ), Coef('Var'  , 0.183587    ), Coef('Var'  , 0.251346    ), Coef('Var'  , 0.375174    ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0319299   ), Coef('Var'  , 0.0648149   ), Coef('Var'  , 0.100773    ), Coef('Var'  , 0.139086    ), Coef('Var'  , 0.193843    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0287518   ), Coef('Var'  , 0.0557284   ), Coef('Var'  , 0.0627292   ), Coef('Var'  , 0.0668421   ), Coef('Var'  , 0.0339775   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0259047   ), Coef('Var'  , 0.0503576   ), Coef('Var'  , 0.0532441   ), Coef('Var'  , 0.0538866   ), Coef('Var'  , 0.0273395   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0214983   ), Coef('Var'  , 0.041803    ), Coef('Var'  , 0.0429666   ), Coef('Var'  , 0.0417394   ), Coef('Var'  , 0.0214683   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0283878   ), Coef('Var'  , 0.0553328   ), Coef('Var'  , 0.0541245   ), Coef('Var'  , 0.0497466   ), Coef('Var'  , 0.0257367   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0256048   ), Coef('Var'  , 0.0514872   ), Coef('Var'  , 0.0465467   ), Coef('Var'  , 0.0412643   ), Coef('Var'  , 0.0209419   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.193799    ), Coef('Var'  , 0.139375    ), Coef('Var'  , 0.102521    ), Coef('Var'  , 0.0682396   ), Coef('Var'  , 0.0337221   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.370021    ), Coef('Var'  , 0.241961    ), Coef('Var'  , 0.172036    ), Coef('Var'  , 0.105411    ), Coef('Var'  , 0.0520149   ), ], ])
	etat12.initMat[Chem([Sub('8')])] = FMat([
		[Coef('Var'  , 0.0521046   ), Coef('Var'  , 0.0268767   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0295406   ), Coef('Var'  , 0.0578535   ), Coef('Var'  , 0.0564173   ), ], 
		[Coef('Var'  , 0.0484178   ), Coef('Var'  , 0.0246864   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0298272   ), Coef('Var'  , 0.0594498   ), Coef('Var'  , 0.0545136   ), ], 
		[Coef('Var'  , 0.071884    ), Coef('Var'  , 0.0359114   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.196997    ), Coef('Var'  , 0.14477     ), Coef('Var'  , 0.107908    ), ], 
		[Coef('Var'  , 0.111794    ), Coef('Var'  , 0.0554803   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.373081    ), Coef('Var'  , 0.24761     ), Coef('Var'  , 0.178562    ), ], 
		[Coef('Var'  , 0.178661    ), Coef('Var'  , 0.213634    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.21299     ), Coef('Var'  , 0.17745     ), Coef('Var'  , 0.176624    ), ], 
		[Coef('Var'  , 0.244006    ), Coef('Var'  , 0.371164    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0532645   ), Coef('Var'  , 0.107647    ), Coef('Var'  , 0.174428    ), ], 
		[Coef('Var'  , 0.150071    ), Coef('Var'  , 0.199648    ), Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0389258   ), Coef('Var'  , 0.0777937   ), Coef('Var'  , 0.113574    ), ], 
		[Coef('Var'  , 0.0533984   ), Coef('Var'  , 0.02674     ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0214356   ), Coef('Var'  , 0.042179    ), Coef('Var'  , 0.0481756   ), ], 
		[Coef('Var'  , 0.0469495   ), Coef('Var'  , 0.0239214   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.02228     ), Coef('Var'  , 0.0430855   ), Coef('Var'  , 0.0462015   ), ], 
		[Coef('Var'  , 0.0427125   ), Coef('Var'  , 0.0219383   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0216578   ), Coef('Var'  , 0.0421613   ), Coef('Var'  , 0.0435961   ), ], ])
	etat12.initMat[Chem([Sub('9')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.203507    ), Coef('Var'  , 0.157445    ), Coef('Var'  , 0.12043     ), Coef('Var'  , 0.0837005   ), Coef('Var'  , 0.041923    ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.372553    ), Coef('Var'  , 0.246837    ), Coef('Var'  , 0.176523    ), Coef('Var'  , 0.109235    ), Coef('Var'  , 0.0539698   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.20722     ), Coef('Var'  , 0.166152    ), Coef('Var'  , 0.165234    ), Coef('Var'  , 0.167603    ), Coef('Var'  , 0.208014    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0566383   ), Coef('Var'  , 0.11388     ), Coef('Var'  , 0.180225    ), Coef('Var'  , 0.248542    ), Coef('Var'  , 0.373587    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0387698   ), Coef('Var'  , 0.0779015   ), Coef('Var'  , 0.113957    ), Coef('Var'  , 0.151355    ), Coef('Var'  , 0.200188    ), Coef('Const', 0.25        ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0232849   ), Coef('Var'  , 0.0457027   ), Coef('Var'  , 0.0522038   ), Coef('Var'  , 0.0575988   ), Coef('Var'  , 0.0289188   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0248808   ), Coef('Var'  , 0.0483261   ), Coef('Var'  , 0.0518933   ), Coef('Var'  , 0.053026    ), Coef('Var'  , 0.0270126   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0203483   ), Coef('Var'  , 0.0394132   ), Coef('Var'  , 0.0407976   ), Coef('Var'  , 0.0396158   ), Coef('Var'  , 0.0204492   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.024261    ), Coef('Var'  , 0.0475261   ), Coef('Var'  , 0.046968    ), Coef('Var'  , 0.0437794   ), Coef('Var'  , 0.022707    ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.028537    ), Coef('Var'  , 0.0568172   ), Coef('Var'  , 0.0517677   ), Coef('Var'  , 0.0455452   ), Coef('Var'  , 0.0232307   ), Coef('Const', 0           ), Coef('Const', 0           ), ], ])
	etat12.initMat[Chem([Sub('10')])] = FMat([
		[Coef('Var'  , 0.103067    ), Coef('Var'  , 0.100392    ), Coef('Var'  , 0.0964527   ), Coef('Var'  , 0.102677    ), Coef('Var'  , 0.106909    ), Coef('Var'  , 0.114782    ), Coef('Var'  , 0.122265    ), Coef('Var'  , 0.120485    ), Coef('Var'  , 0.119977    ), Coef('Var'  , 0.111138    ), ], 
		[Coef('Var'  , 0.0956619   ), Coef('Var'  , 0.094704    ), Coef('Var'  , 0.0917184   ), Coef('Var'  , 0.100464    ), Coef('Var'  , 0.108981    ), Coef('Var'  , 0.117556    ), Coef('Var'  , 0.127646    ), Coef('Var'  , 0.121619    ), Coef('Var'  , 0.116209    ), Coef('Var'  , 0.106711    ), ], 
		[Coef('Var'  , 0.0718996   ), Coef('Var'  , 0.0778384   ), Coef('Var'  , 0.0828491   ), Coef('Var'  , 0.0894121   ), Coef('Var'  , 0.0968692   ), Coef('Var'  , 0.0939029   ), Coef('Var'  , 0.0934965   ), Coef('Var'  , 0.0844305   ), Coef('Var'  , 0.077158    ), Coef('Var'  , 0.074704    ), ], 
		[Coef('Var'  , 0.0957953   ), Coef('Var'  , 0.103791    ), Coef('Var'  , 0.111128    ), Coef('Var'  , 0.117126    ), Coef('Var'  , 0.125118    ), Coef('Var'  , 0.118322    ), Coef('Var'  , 0.113348    ), Coef('Var'  , 0.105791    ), Coef('Var'  , 0.0972722   ), Coef('Var'  , 0.0977259   ), ], 
		[Coef('Var'  , 0.107851    ), Coef('Var'  , 0.114614    ), Coef('Var'  , 0.120738    ), Coef('Var'  , 0.118278    ), Coef('Var'  , 0.117032    ), Coef('Var'  , 0.108912    ), Coef('Var'  , 0.101431    ), Coef('Var'  , 0.100047    ), Coef('Var'  , 0.0971004   ), Coef('Var'  , 0.103674    ), ], 
		[Coef('Var'  , 0.105089    ), Coef('Var'  , 0.112042    ), Coef('Var'  , 0.120134    ), Coef('Var'  , 0.11164     ), Coef('Var'  , 0.104369    ), Coef('Var'  , 0.0950252   ), Coef('Var'  , 0.0851239   ), Coef('Var'  , 0.0860858   ), Coef('Var'  , 0.0854156   ), Coef('Var'  , 0.0955764   ), ], 
		[Coef('Var'  , 0.11084     ), Coef('Var'  , 0.109642    ), Coef('Var'  , 0.110401    ), Coef('Var'  , 0.10344     ), Coef('Var'  , 0.0970647   ), Coef('Var'  , 0.0944696   ), Coef('Var'  , 0.090351    ), Coef('Var'  , 0.0950832   ), Coef('Var'  , 0.0982239   ), Coef('Var'  , 0.104256    ), ], 
		[Coef('Var'  , 0.108789    ), Coef('Var'  , 0.101155    ), Coef('Var'  , 0.0955007   ), Coef('Var'  , 0.0875015   ), Coef('Var'  , 0.0791196   ), Coef('Var'  , 0.0801263   ), Coef('Var'  , 0.0791194   ), Coef('Var'  , 0.0874038   ), Coef('Var'  , 0.0949864   ), Coef('Var'  , 0.100972    ), ], 
		[Coef('Var'  , 0.0952727   ), Coef('Var'  , 0.0889098   ), Coef('Var'  , 0.0839289   ), Coef('Var'  , 0.0821961   ), Coef('Var'  , 0.0791719   ), Coef('Var'  , 0.0829249   ), Coef('Var'  , 0.0850302   ), Coef('Var'  , 0.089902    ), Coef('Var'  , 0.0956548   ), Coef('Var'  , 0.0941193   ), ], 
		[Coef('Var'  , 0.105735    ), Coef('Var'  , 0.096912    ), Coef('Var'  , 0.0871497   ), Coef('Var'  , 0.0872641   ), Coef('Var'  , 0.0853663   ), Coef('Var'  , 0.0939795   ), Coef('Var'  , 0.10219     ), Coef('Var'  , 0.109152    ), Coef('Var'  , 0.118002    ), Coef('Var'  , 0.111124    ), ], ])
	
	
	
	etat13.bords   = {Bord('0'): etat14, Bord('1'): etat14, }
	etat13.permuts = {Permut('0'): etat13, }
	etat13.interns = {Intern('_'): etat13, }
	etat13.subs    = {Sub('0'): etat13, Sub('1'): etat13, Sub('G', True): Etat.etatPoint, }
	
	etat13.buildIntern()
	etat13.fm_[Permut('0')] = PMat(3, [2, 1, 0, ])
	
	
	etat13.eqs = [
		(Chem([Permut('0'), Bord('0'), ])	,	Chem([Bord('1')])),
		(Chem([Permut('0'), Bord('1'), ])	,	Chem([Bord('0')])),
		(Chem([Permut('0'), Intern(''), ])	,	Chem([Intern('')])),
		(Chem([Permut('0'), Sub('0'), ])	,	Chem([Sub('1'), Permut('0'), ])),
		(Chem([Permut('0'), Sub('1'), ])	,	Chem([Sub('0'), Permut('0'), ])),
		]
	
	
	etat13.prim.elems = [Figure(1, [Chem([Bord('0')]), Chem([Bord('1')]), ])]
	etat13.grid.elems = [Figure(1, [Chem([Bord('0')]), Chem([Intern('')]), Chem([Bord('1')]), ])]
	
	
	etat13.space = [Chem([Bord('0'), Intern('0'), Intern('0'), ]), Chem([Intern('0'), Intern('0'), ]), Chem([Bord('1'), Intern('0'), Intern('0'), ]), ]
	
	etat13.initMat[Chem([Sub('0')])] = FMat([
		[Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), ], ])
	etat13.initMat[Chem([Sub('1')])] = FMat([
		[Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), ], ])
	etat13.initMat[Chem([Sub('G')])] = FMat([
		[Coef('Const', 0           )], 
		[Coef('Const', 1           )], 
		[Coef('Const', 0           )], ])
	
	
	
	etat14.bords   = {}
	etat14.permuts = {}
	etat14.interns = {Intern('_'): etat14, }
	etat14.subs    = {Sub('0'): etat14, Sub('G', True): Etat.etatPoint, }
	
	etat14.buildIntern()
	
	
	etat14.eqs = [
		]
	
	
	etat14.prim.elems = []
	etat14.grid.elems = []
	
	
	etat14.space = [Chem([Intern('0'), Intern('0'), ])]
	
	etat14.initMat[Chem([Sub('0')])] = FMat([[Coef('Var'  , 1           )]])
	etat14.initMat[Chem([Sub('G')])] = FMat([[Coef('Const', 1           )]])
	
	
	
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
