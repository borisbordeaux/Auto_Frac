# -*- coding: utf-8 -*-

# Automatically generated, from file : unnamed.py, function : modele()

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
	etat4 = Etat('Cell_3',0)
	etat5 = Etat('Cell_4',0)
	etat6 = Etat('Cell_5',0)
	etat7 = Etat('Cell_6',0)
	etat8 = Etat('Cell_7',0)
	etat9 = Etat('Cell_8',0)
	etat10 = Etat('Cell_9',0)
	etat11 = Etat('Cell_10',0)
	etat12 = Etat('Cell_11',0)
	etat13 = Etat('Cell_12',0)
	etat14 = Etat('Cell_13',0)
	etat15 = Etat('Cell_14',0)
	etat16 = Etat('Cell_15',0)
	etat17 = Etat('Cell_16',0)
	etat18 = Etat('Cell_17',0)
	etat19 = Etat('B2',1)
	etat20 = Etat('B3',1)
	etat21 = Etat('B4',1)
	etat22 = Etat('B5',1)
	etat23 = Etat('s',1)
	
	
	etat0.subs   = {Sub('0'): etat1, Sub('1'): etat2, Sub('2'): etat3, Sub('3'): etat4, Sub('4'): etat5, Sub('5'): etat6, Sub('6'): etat7, Sub('7'): etat8, Sub('8'): etat9, Sub('9'): etat10, Sub('10'): etat11, Sub('11'): etat12, Sub('12'): etat13, Sub('13'): etat14, Sub('14'): etat15, Sub('15'): etat16, Sub('16'): etat17, Sub('17'): etat18, }
	
	etat0.eqs = [
		(Chem([Sub('0'), Bord('0'), Bord('1'), ])	,	Chem([Sub('12'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('1'), Bord('1'), ])	,	Chem([Sub('16'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('2'), Bord('1'), ])	,	Chem([Sub('3'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('3'), Bord('1'), ])	,	Chem([Sub('1'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('0'), Bord('1'), ])	,	Chem([Sub('12'), Bord('4'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('2'), Bord('1'), ])	,	Chem([Sub('3'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('3'), Bord('1'), ])	,	Chem([Sub('14'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('4'), Bord('1'), ])	,	Chem([Sub('9'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('0'), Bord('1'), ])	,	Chem([Sub('12'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('1'), Bord('1'), ])	,	Chem([Sub('10'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('2'), Bord('1'), ])	,	Chem([Sub('7'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('3'), Bord('1'), ])	,	Chem([Sub('17'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('4'), Bord('1'), ])	,	Chem([Sub('16'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('3'), Bord('1'), Bord('1'), ])	,	Chem([Sub('17'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('3'), Bord('2'), Bord('1'), ])	,	Chem([Sub('6'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('4'), Bord('0'), Bord('1'), ])	,	Chem([Sub('8'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('4'), Bord('1'), Bord('1'), ])	,	Chem([Sub('9'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('4'), Bord('2'), Bord('1'), ])	,	Chem([Sub('11'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('4'), Bord('3'), Bord('1'), ])	,	Chem([Sub('10'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('5'), Bord('0'), Bord('1'), ])	,	Chem([Sub('15'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('5'), Bord('1'), Bord('1'), ])	,	Chem([Sub('7'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('5'), Bord('2'), Bord('1'), ])	,	Chem([Sub('11'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('6'), Bord('0'), Bord('1'), ])	,	Chem([Sub('7'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('6'), Bord('1'), Bord('1'), ])	,	Chem([Sub('13'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('6'), Bord('3'), Bord('1'), ])	,	Chem([Sub('17'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('8'), Bord('0'), Bord('1'), ])	,	Chem([Sub('10'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('8'), Bord('1'), Bord('1'), ])	,	Chem([Sub('12'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('8'), Bord('2'), Bord('1'), ])	,	Chem([Sub('9'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('9'), Bord('2'), Bord('1'), ])	,	Chem([Sub('11'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('10'), Bord('0'), Bord('1'), ])	,	Chem([Sub('11'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('12'), Bord('2'), Bord('1'), ])	,	Chem([Sub('16'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('13'), Bord('0'), Bord('1'), ])	,	Chem([Sub('15'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('13'), Bord('1'), Bord('1'), ])	,	Chem([Sub('14'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('14'), Bord('1'), Bord('1'), ])	,	Chem([Sub('15'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('16'), Bord('2'), Bord('1'), ])	,	Chem([Sub('17'), Bord('0'), Bord('1'), ])),
		]
	
	
	etat0.space = []
	
	etat0.initMat[Chem([Sub('0')])] = FMat([
		[Coef('Var'  , 0.852012    ), Coef('Var'  , 1.67581     ), Coef('Var'  , 2.39063     ), Coef('Var'  , 3.50427     ), Coef('Var'  , 4.30543     ), Coef('Var'  , 3.71346     ), Coef('Var'  , 2.66094     ), Coef('Var'  , 1.90687     ), ], 
		[Coef('Var'  ,-2.49809     ), Coef('Var'  ,-3.4548      ), Coef('Var'  ,-3.56706     ), Coef('Var'  ,-3.11718     ), Coef('Var'  ,-2.05454     ), Coef('Var'  ,-1.53159     ), Coef('Var'  ,-0.840861    ), Coef('Var'  ,-1.88887     ), ], 
		[Coef('Var'  , 0.401981    ), Coef('Var'  , 0.782679    ), Coef('Var'  , 1.87914     ), Coef('Var'  , 1.31408     ), Coef('Var'  , 1.3917      ), Coef('Var'  , 0.35042     ), Coef('Var'  , 1.48523e-08 ), Coef('Var'  , 1.18488e-07 ), ], 
		[Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), ], ])
	etat0.initMat[Chem([Sub('1')])] = FMat([
		[Coef('Var'  ,-2.37048     ), Coef('Var'  ,-1.26411     ), Coef('Var'  ,-0.0450651   ), Coef('Var'  , 0.0326799   ), Coef('Var'  , 0.852012    ), Coef('Var'  , 0.178094    ), Coef('Var'  , 0.183117    ), Coef('Var'  ,-1.12128     ), Coef('Var'  ,-2.35742     ), Coef('Var'  ,-2.45428     ), ], 
		[Coef('Var'  ,-1.70357     ), Coef('Var'  ,-2.42549     ), Coef('Var'  ,-3.08607     ), Coef('Var'  ,-2.9134      ), Coef('Var'  ,-2.49809     ), Coef('Var'  ,-1.42648     ), Coef('Var'  ,-0.0943796   ), Coef('Var'  ,-0.029804    ), Coef('Var'  , 0.194218    ), Coef('Var'  ,-0.829982    ), ], 
		[Coef('Var'  , 3.18054     ), Coef('Var'  , 2.75523     ), Coef('Var'  , 2.61856     ), Coef('Var'  , 1.3248      ), Coef('Var'  , 0.401981    ), Coef('Var'  , 1.08516e-08 ), Coef('Var'  , 0.0686576   ), Coef('Var'  , 0.501571    ), Coef('Var'  , 1.06897     ), Coef('Var'  , 2.05579     ), ], 
		[Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), ], ])
	etat0.initMat[Chem([Sub('2')])] = FMat([
		[Coef('Var'  , 4.50547     ), Coef('Var'  , 3.58946     ), Coef('Var'  , 2.5062      ), Coef('Var'  , 1.81815     ), Coef('Var'  , 0.863103    ), Coef('Var'  , 1.19957     ), Coef('Var'  , 1.4093      ), Coef('Var'  , 2.69276     ), Coef('Var'  , 3.7569      ), Coef('Var'  , 4.21241     ), ], 
		[Coef('Var'  ,-0.446982    ), Coef('Var'  ,-0.869461    ), Coef('Var'  ,-1.60777     ), Coef('Var'  ,-0.639157    ), Coef('Var'  , 0.16669     ), Coef('Var'  , 1.33709     ), Coef('Var'  , 2.4092      ), Coef('Var'  , 2.19316     ), Coef('Var'  , 1.88971     ), Coef('Var'  , 0.850203    ), ], 
		[Coef('Var'  , 4.48491     ), Coef('Var'  , 5.32905     ), Coef('Var'  , 5.47653     ), Coef('Var'  , 6.17099     ), Coef('Var'  , 6.74344     ), Coef('Var'  , 6.00494     ), Coef('Var'  , 5.09847     ), Coef('Var'  , 4.67762     ), Coef('Var'  , 3.87002     ), Coef('Var'  , 4.56314     ), ], 
		[Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), ], ])
	etat0.initMat[Chem([Sub('3')])] = FMat([
		[Coef('Var'  , 0.183117    ), Coef('Var'  , 1.46778     ), Coef('Var'  , 2.66094     ), Coef('Var'  , 3.31803     ), Coef('Var'  , 3.66244     ), Coef('Var'  , 2.51106     ), Coef('Var'  , 1.30991     ), Coef('Var'  , 0.606152    ), ], 
		[Coef('Var'  ,-0.0943796   ), Coef('Var'  ,-0.297502    ), Coef('Var'  ,-0.840861    ), Coef('Var'  , 0.294474    ), Coef('Var'  , 1.48564     ), Coef('Var'  , 1.90003     ), Coef('Var'  , 2.38129     ), Coef('Var'  , 1.21479     ), ], 
		[Coef('Var'  , 0.0686576   ), Coef('Var'  , 3.95988e-08 ), Coef('Var'  , 1.48523e-08 ), Coef('Var'  , 4.55139e-08 ), Coef('Var'  , 0.436965    ), Coef('Var'  , 7.44472e-08 ), Coef('Var'  , 0.123499    ), Coef('Var'  , 1.82183e-08 ), ], 
		[Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), ], ])
	etat0.initMat[Chem([Sub('4')])] = FMat([
		[Coef('Var'  ,-1.85564     ), Coef('Var'  ,-2.23137     ), Coef('Var'  ,-2.22604     ), Coef('Var'  ,-3.48878     ), Coef('Var'  ,-4.07461     ), Coef('Var'  ,-4.36072     ), Coef('Var'  ,-3.71115     ), Coef('Var'  ,-3.09443     ), ], 
		[Coef('Var'  ,-1.26756     ), Coef('Var'  ,-2.52259     ), Coef('Var'  ,-3.31539     ), Coef('Var'  ,-3.15029     ), Coef('Var'  ,-2.40419     ), Coef('Var'  ,-1.50504     ), Coef('Var'  ,-0.416226    ), Coef('Var'  ,-0.880127    ), ], 
		[Coef('Var'  , 8.96777     ), Coef('Var'  , 8.80342     ), Coef('Var'  , 7.74785     ), Coef('Var'  , 7.44577     ), Coef('Var'  , 6.53731     ), Coef('Var'  , 7.44698     ), Coef('Var'  , 7.77294     ), Coef('Var'  , 8.83139     ), ], 
		[Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), ], ])
	etat0.initMat[Chem([Sub('5')])] = FMat([
		[Coef('Var'  ,-2.62931     ), Coef('Var'  ,-3.2745      ), Coef('Var'  ,-3.11302     ), Coef('Var'  ,-1.97798     ), Coef('Var'  ,-0.844254    ), Coef('Var'  ,-1.65374     ), ], 
		[Coef('Var'  , 2.09834     ), Coef('Var'  , 2.86001     ), Coef('Var'  , 3.48682     ), Coef('Var'  , 3.91586     ), Coef('Var'  , 3.63986     ), Coef('Var'  , 2.96067     ), ], 
		[Coef('Var'  , 5.66276     ), Coef('Var'  , 4.78535     ), Coef('Var'  , 3.63337     ), Coef('Var'  , 4.15781     ), Coef('Var'  , 4.79631     ), Coef('Var'  , 5.54521     ), ], 
		[Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), ], ])
	etat0.initMat[Chem([Sub('6')])] = FMat([
		[Coef('Var'  , 2.89054     ), Coef('Var'  , 1.9864      ), Coef('Var'  , 0.798224    ), Coef('Var'  , 0.0308688   ), Coef('Var'  ,-0.687303    ), Coef('Var'  , 0.334104    ), Coef('Var'  , 1.30991     ), Coef('Var'  , 2.04257     ), ], 
		[Coef('Var'  , 3.29127     ), Coef('Var'  , 4.0286      ), Coef('Var'  , 3.96355     ), Coef('Var'  , 4.05672     ), Coef('Var'  , 3.80049     ), Coef('Var'  , 3.26489     ), Coef('Var'  , 2.38129     ), Coef('Var'  , 3.19148     ), ], 
		[Coef('Var'  , 1.8427      ), Coef('Var'  , 2.46019     ), Coef('Var'  , 3.02209     ), Coef('Var'  , 1.883       ), Coef('Var'  , 0.742693    ), Coef('Var'  , 0.102614    ), Coef('Var'  , 0.123499    ), Coef('Var'  , 0.851719    ), ], 
		[Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), ], ])
	etat0.initMat[Chem([Sub('7')])] = FMat([
		[Coef('Var'  , 1.4093      ), Coef('Var'  , 0.273479    ), Coef('Var'  ,-0.844254    ), Coef('Var'  ,-0.0942746   ), Coef('Var'  , 0.798224    ), Coef('Var'  , 1.27863     ), ], 
		[Coef('Var'  , 2.4092      ), Coef('Var'  , 3.08942     ), Coef('Var'  , 3.63986     ), Coef('Var'  , 4.25793     ), Coef('Var'  , 3.96355     ), Coef('Var'  , 3.1896      ), ], 
		[Coef('Var'  , 5.09847     ), Coef('Var'  , 5.31192     ), Coef('Var'  , 4.79631     ), Coef('Var'  , 3.92125     ), Coef('Var'  , 3.02209     ), Coef('Var'  , 4.01094     ), ], 
		[Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), ], ])
	etat0.initMat[Chem([Sub('8')])] = FMat([
		[Coef('Var'  ,-2.22604     ), Coef('Var'  ,-0.927959    ), Coef('Var'  ,-0.0605472   ), Coef('Var'  , 0.259815    ), Coef('Var'  , 0.268108    ), Coef('Var'  ,-0.9948      ), Coef('Var'  ,-2.3155      ), Coef('Var'  ,-2.18625     ), ], 
		[Coef('Var'  ,-3.31539     ), Coef('Var'  ,-3.17123     ), Coef('Var'  ,-2.18477     ), Coef('Var'  ,-2.81256     ), Coef('Var'  ,-3.04357     ), Coef('Var'  ,-3.47104     ), Coef('Var'  ,-3.40053     ), Coef('Var'  ,-3.82766     ), ], 
		[Coef('Var'  , 7.74785     ), Coef('Var'  , 7.87054     ), Coef('Var'  , 7.69161     ), Coef('Var'  , 6.56792     ), Coef('Var'  , 5.25446     ), Coef('Var'  , 5.21599     ), Coef('Var'  , 5.27067     ), Coef('Var'  , 6.52879     ), ], 
		[Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), ], ])
	etat0.initMat[Chem([Sub('9')])] = FMat([
		[Coef('Var'  ,-4.07461     ), Coef('Var'  ,-3.55225     ), Coef('Var'  ,-2.3155      ), Coef('Var'  ,-2.48971     ), Coef('Var'  ,-2.37048     ), Coef('Var'  ,-3.08921     ), Coef('Var'  ,-3.65817     ), Coef('Var'  ,-4.25106     ), ], 
		[Coef('Var'  ,-2.40419     ), Coef('Var'  ,-3.20131     ), Coef('Var'  ,-3.40053     ), Coef('Var'  ,-2.72726     ), Coef('Var'  ,-1.70357     ), Coef('Var'  ,-0.929705    ), Coef('Var'  ,-0.35117     ), Coef('Var'  ,-1.47554     ), ], 
		[Coef('Var'  , 6.53731     ), Coef('Var'  , 5.64341     ), Coef('Var'  , 5.27067     ), Coef('Var'  , 4.08531     ), Coef('Var'  , 3.18054     ), Coef('Var'  , 4.10393     ), Coef('Var'  , 5.25823     ), Coef('Var'  , 5.61641     ), ], 
		[Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), ], ])
	etat0.initMat[Chem([Sub('10')])] = FMat([
		[Coef('Var'  ,-1.85564     ), Coef('Var'  ,-1.49928     ), Coef('Var'  ,-1.60011     ), Coef('Var'  ,-0.289228    ), Coef('Var'  , 0.863103    ), Coef('Var'  , 0.552735    ), Coef('Var'  ,-0.0605472   ), Coef('Var'  ,-0.637164    ), ], 
		[Coef('Var'  ,-1.26756     ), Coef('Var'  ,-0.00950172  ), Coef('Var'  , 0.841226    ), Coef('Var'  , 0.678873    ), Coef('Var'  , 0.16669     ), Coef('Var'  ,-1.00185     ), Coef('Var'  ,-2.18477     ), Coef('Var'  ,-1.69187     ), ], 
		[Coef('Var'  , 8.96777     ), Coef('Var'  , 8.75419     ), Coef('Var'  , 7.7445      ), Coef('Var'  , 7.31951     ), Coef('Var'  , 6.74344     ), Coef('Var'  , 7.39243     ), Coef('Var'  , 7.69161     ), Coef('Var'  , 8.7603      ), ], 
		[Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), ], ])
	etat0.initMat[Chem([Sub('11')])] = FMat([
		[Coef('Var'  ,-3.71115     ), Coef('Var'  ,-3.96903     ), Coef('Var'  ,-3.65817     ), Coef('Var'  ,-3.21636     ), Coef('Var'  ,-2.62931     ), Coef('Var'  ,-2.08757     ), Coef('Var'  ,-1.60011     ), Coef('Var'  ,-2.88226     ), ], 
		[Coef('Var'  ,-0.416226    ), Coef('Var'  ,-0.0910028   ), Coef('Var'  ,-0.35117     ), Coef('Var'  , 0.930966    ), Coef('Var'  , 2.09834     ), Coef('Var'  , 1.69456     ), Coef('Var'  , 0.841226    ), Coef('Var'  , 0.581049    ), ], 
		[Coef('Var'  , 7.77294     ), Coef('Var'  , 6.5271      ), Coef('Var'  , 5.25823     ), Coef('Var'  , 5.29607     ), Coef('Var'  , 5.66276     ), Coef('Var'  , 6.82917     ), Coef('Var'  , 7.7445      ), Coef('Var'  , 7.9355      ), ], 
		[Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), ], ])
	etat0.initMat[Chem([Sub('12')])] = FMat([
		[Coef('Var'  ,-0.0450651   ), Coef('Var'  , 0.184555    ), Coef('Var'  , 0.268108    ), Coef('Var'  , 1.46132     ), Coef('Var'  , 2.5062      ), Coef('Var'  , 3.20318     ), Coef('Var'  , 3.93955     ), Coef('Var'  , 3.13473     ), Coef('Var'  , 2.39063     ), Coef('Var'  , 1.17043     ), ], 
		[Coef('Var'  ,-3.08607     ), Coef('Var'  ,-3.19033     ), Coef('Var'  ,-3.04357     ), Coef('Var'  ,-2.43242     ), Coef('Var'  ,-1.60777     ), Coef('Var'  ,-2.48618     ), Coef('Var'  ,-2.69132     ), Coef('Var'  ,-3.50244     ), Coef('Var'  ,-3.56706     ), Coef('Var'  ,-3.64798     ), ], 
		[Coef('Var'  , 2.61856     ), Coef('Var'  , 3.92533     ), Coef('Var'  , 5.25446     ), Coef('Var'  , 5.34254     ), Coef('Var'  , 5.47653     ), Coef('Var'  , 4.74969     ), Coef('Var'  , 3.67653     ), Coef('Var'  , 2.98183     ), Coef('Var'  , 1.87914     ), Coef('Var'  , 2.42141     ), ], 
		[Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), ], ])
	etat0.initMat[Chem([Sub('13')])] = FMat([
		[Coef('Var'  ,-0.687303    ), Coef('Var'  ,-1.79504     ), Coef('Var'  ,-3.06945     ), Coef('Var'  ,-3.10082     ), Coef('Var'  ,-2.68719     ), Coef('Var'  ,-1.50948     ), ], 
		[Coef('Var'  , 3.80049     ), Coef('Var'  , 4.47646     ), Coef('Var'  , 4.19696     ), Coef('Var'  , 3.69906     ), Coef('Var'  , 2.46422     ), Coef('Var'  , 3.04443     ), ], 
		[Coef('Var'  , 0.742693    ), Coef('Var'  , 1.01784     ), Coef('Var'  , 1.27024     ), Coef('Var'  , 0.0700908   ), Coef('Var'  , 1.4514e-08  ), Coef('Var'  , 0.0266851   ), ], 
		[Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), ], ])
	etat0.initMat[Chem([Sub('14')])] = FMat([
		[Coef('Var'  ,-2.35742     ), Coef('Var'  ,-2.45209     ), Coef('Var'  ,-2.68719     ), Coef('Var'  ,-3.874       ), Coef('Var'  ,-3.93267     ), Coef('Var'  ,-3.3684      ), ], 
		[Coef('Var'  , 0.194218    ), Coef('Var'  , 1.16101     ), Coef('Var'  , 2.46422     ), Coef('Var'  , 2.13669     ), Coef('Var'  , 2.1736      ), Coef('Var'  , 0.944984    ), ], 
		[Coef('Var'  , 1.06897     ), Coef('Var'  , 0.13902     ), Coef('Var'  , 1.4514e-08  ), Coef('Var'  , 0.355318    ), Coef('Var'  , 1.63383     ), Coef('Var'  , 1.55784     ), ], 
		[Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), ], ])
	etat0.initMat[Chem([Sub('15')])] = FMat([
		[Coef('Var'  ,-3.11302     ), Coef('Var'  ,-3.75883     ), Coef('Var'  ,-3.93267     ), Coef('Var'  ,-4.12182     ), Coef('Var'  ,-3.06945     ), Coef('Var'  ,-3.14559     ), ], 
		[Coef('Var'  , 3.48682     ), Coef('Var'  , 2.61828     ), Coef('Var'  , 2.1736      ), Coef('Var'  , 3.4484      ), Coef('Var'  , 4.19696     ), Coef('Var'  , 4.30382     ), ], 
		[Coef('Var'  , 3.63337     ), Coef('Var'  , 2.86382     ), Coef('Var'  , 1.63383     ), Coef('Var'  , 1.4113      ), Coef('Var'  , 1.27024     ), Coef('Var'  , 2.58825     ), ], 
		[Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), ], ])
	etat0.initMat[Chem([Sub('16')])] = FMat([
		[Coef('Var'  , 4.30543     ), Coef('Var'  , 4.5832      ), Coef('Var'  , 3.93955     ), Coef('Var'  , 4.65696     ), Coef('Var'  , 4.50547     ), Coef('Var'  , 5.22083     ), Coef('Var'  , 4.96915     ), Coef('Var'  , 4.93107     ), ], 
		[Coef('Var'  ,-2.05454     ), Coef('Var'  ,-2.56637     ), Coef('Var'  ,-2.69132     ), Coef('Var'  ,-1.72668     ), Coef('Var'  ,-0.446982    ), Coef('Var'  ,-0.145795    ), Coef('Var'  , 0.332472    ), Coef('Var'  ,-0.893195    ), ], 
		[Coef('Var'  , 1.3917      ), Coef('Var'  , 2.54937     ), Coef('Var'  , 3.67653     ), Coef('Var'  , 4.21044     ), Coef('Var'  , 4.48491     ), Coef('Var'  , 3.42902     ), Coef('Var'  , 2.2412      ), Coef('Var'  , 1.67603     ), ], 
		[Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), ], ])
	etat0.initMat[Chem([Sub('17')])] = FMat([
		[Coef('Var'  , 3.66244     ), Coef('Var'  , 4.66307     ), Coef('Var'  , 4.96915     ), Coef('Var'  , 4.59559     ), Coef('Var'  , 3.7569      ), Coef('Var'  , 3.48146     ), Coef('Var'  , 2.89054     ), Coef('Var'  , 3.7023      ), ], 
		[Coef('Var'  , 1.48564     ), Coef('Var'  , 0.990088    ), Coef('Var'  , 0.332472    ), Coef('Var'  , 1.36914     ), Coef('Var'  , 1.88971     ), Coef('Var'  , 2.82333     ), Coef('Var'  , 3.29127     ), Coef('Var'  , 2.67243     ), ], 
		[Coef('Var'  , 0.436965    ), Coef('Var'  , 1.13769     ), Coef('Var'  , 2.2412      ), Coef('Var'  , 2.98222     ), Coef('Var'  , 3.87002     ), Coef('Var'  , 2.94896     ), Coef('Var'  , 1.8427      ), Coef('Var'  , 1.01227     ), ], 
		[Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), ], ])
	
	
	
	etat1.bords   = {Bord('0'): etat19, Bord('1'): etat19, Bord('2'): etat20, Bord('3'): etat19, }
	etat1.permuts = {}
	etat1.interns = {Intern('_'): etat1, }
	etat1.subs    = {Sub('0'): etat2, Sub('1'): etat3, Sub('2'): etat4, Sub('3'): etat5, Sub('4'): etat6, Sub('5'): etat7, Sub('6'): etat8, Sub('7'): etat9, Sub('G', True): Etat.etatPoint, Sub('8'): etat10, Sub('9'): etat11, Sub('10'): etat12, Sub('11'): etat13, Sub('12'): etat14, Sub('13'): etat15, Sub('14'): etat16, Sub('15'): etat17, Sub('16'): etat18, }
	
	etat1.buildIntern()
	
	
	etat1.eqs = [
		(Chem([Bord('0'), Sub('0'), Permut('0'), ])	,	Chem([Sub('0'), Bord('1'), ])),
		(Chem([Bord('3'), Sub('1'), Permut('0'), ])	,	Chem([Sub('0'), Bord('2'), ])),
		(Chem([Bord('3'), Sub('0'), Permut('0'), ])	,	Chem([Sub('2'), Bord('0'), ])),
		(Chem([Bord('2'), Sub('2'), Permut('0'), ])	,	Chem([Sub('2'), Bord('1'), ])),
		(Chem([Bord('1'), Sub('0'), Permut('0'), ])	,	Chem([Sub('11'), Bord('3'), ])),
		(Chem([Bord('0'), Sub('1'), Permut('0'), ])	,	Chem([Sub('11'), Bord('4'), ])),
		(Chem([Bord('1'), Sub('1'), Permut('0'), ])	,	Chem([Sub('15'), Bord('0'), ])),
		(Chem([Bord('2'), Sub('0'), Permut('0'), ])	,	Chem([Sub('15'), Bord('3'), ])),
		(Chem([Bord('2'), Sub('1'), Permut('0'), ])	,	Chem([Sub('16'), Bord('0'), ])),
		(Chem([Sub('0'), Bord('0'), Bord('1'), ])	,	Chem([Sub('11'), Bord('4'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('2'), Bord('1'), ])	,	Chem([Sub('2'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('3'), Bord('1'), ])	,	Chem([Sub('13'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('4'), Bord('1'), ])	,	Chem([Sub('8'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('0'), Bord('1'), ])	,	Chem([Sub('11'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('1'), Bord('1'), ])	,	Chem([Sub('9'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('2'), Bord('1'), ])	,	Chem([Sub('6'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('3'), Bord('1'), ])	,	Chem([Sub('16'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('4'), Bord('1'), ])	,	Chem([Sub('15'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('1'), Bord('1'), ])	,	Chem([Sub('16'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('2'), Bord('1'), ])	,	Chem([Sub('5'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('3'), Bord('0'), Bord('1'), ])	,	Chem([Sub('7'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('3'), Bord('1'), Bord('1'), ])	,	Chem([Sub('8'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('3'), Bord('2'), Bord('1'), ])	,	Chem([Sub('10'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('3'), Bord('3'), Bord('1'), ])	,	Chem([Sub('9'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('4'), Bord('0'), Bord('1'), ])	,	Chem([Sub('14'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('4'), Bord('1'), Bord('1'), ])	,	Chem([Sub('6'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('4'), Bord('2'), Bord('1'), ])	,	Chem([Sub('10'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('5'), Bord('0'), Bord('1'), ])	,	Chem([Sub('6'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('5'), Bord('1'), Bord('1'), ])	,	Chem([Sub('12'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('5'), Bord('3'), Bord('1'), ])	,	Chem([Sub('16'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('7'), Bord('0'), Bord('1'), ])	,	Chem([Sub('9'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('7'), Bord('1'), Bord('1'), ])	,	Chem([Sub('11'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('7'), Bord('2'), Bord('1'), ])	,	Chem([Sub('8'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('8'), Bord('2'), Bord('1'), ])	,	Chem([Sub('10'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('9'), Bord('0'), Bord('1'), ])	,	Chem([Sub('10'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('11'), Bord('2'), Bord('1'), ])	,	Chem([Sub('15'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('12'), Bord('0'), Bord('1'), ])	,	Chem([Sub('14'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('12'), Bord('1'), Bord('1'), ])	,	Chem([Sub('13'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('13'), Bord('1'), Bord('1'), ])	,	Chem([Sub('14'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('15'), Bord('2'), Bord('1'), ])	,	Chem([Sub('16'), Bord('0'), Bord('1'), ])),
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
		[Coef('Var'  , 0.18171     ), Coef('Var'  , 0.215618    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.216828    ), Coef('Var'  , 0.183977    ), Coef('Var'  , 0.182446    ), ], 
		[Coef('Var'  , 0.244207    ), Coef('Var'  , 0.371712    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0578187   ), Coef('Var'  , 0.1156      ), Coef('Var'  , 0.17953     ), ], 
		[Coef('Var'  , 0.163493    ), Coef('Var'  , 0.206663    ), Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.049402    ), Coef('Var'  , 0.0982181   ), Coef('Var'  , 0.131065    ), ], 
		[Coef('Var'  , 0.0757656   ), Coef('Var'  , 0.0382003   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.033657    ), Coef('Var'  , 0.0664516   ), Coef('Var'  , 0.0718573   ), ], 
		[Coef('Var'  , 0.0640787   ), Coef('Var'  , 0.0322138   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0302449   ), Coef('Var'  , 0.0601465   ), Coef('Var'  , 0.0624587   ), ], 
		[Coef('Var'  , 0.0630969   ), Coef('Var'  , 0.0317169   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.036541    ), Coef('Var'  , 0.0729725   ), Coef('Var'  , 0.0682578   ), ], 
		[Coef('Var'  , 0.0914023   ), Coef('Var'  , 0.0457344   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.203466    ), Coef('Var'  , 0.157919    ), Coef('Var'  , 0.124201    ), ], 
		[Coef('Var'  , 0.116247    ), Coef('Var'  , 0.0581421   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.372042    ), Coef('Var'  , 0.244715    ), Coef('Var'  , 0.180184    ), ], ])
	etat1.initMat[Chem([Sub('1')])] = FMat([
		[Coef('Var'  , 0.0325498   ), Coef('Var'  , 0.053639    ), Coef('Var'  , 0.0740756   ), Coef('Var'  , 0.0919891   ), Coef('Var'  , 0.109251    ), Coef('Var'  , 0.105231    ), Coef('Var'  , 0.0999836   ), Coef('Var'  , 0.0769617   ), Coef('Var'  , 0.0524044   ), Coef('Var'  , 0.0429975   ), ], 
		[Coef('Var'  , 0.035274    ), Coef('Var'  , 0.0663345   ), Coef('Var'  , 0.0975769   ), Coef('Var'  , 0.1086      ), Coef('Var'  , 0.12038     ), Coef('Var'  , 0.104718    ), Coef('Var'  , 0.088967    ), Coef('Var'  , 0.0662522   ), Coef('Var'  , 0.0425064   ), Coef('Var'  , 0.0391895   ), ], 
		[Coef('Var'  , 0.125425    ), Coef('Var'  , 0.150853    ), Coef('Var'  , 0.176306    ), Coef('Var'  , 0.161381    ), Coef('Var'  , 0.146599    ), Coef('Var'  , 0.129576    ), Coef('Var'  , 0.11179     ), Coef('Var'  , 0.0936575   ), Coef('Var'  , 0.0742619   ), Coef('Var'  , 0.100133    ), ], 
		[Coef('Var'  , 0.21094     ), Coef('Var'  , 0.22969     ), Coef('Var'  , 0.248789    ), Coef('Var'  , 0.204368    ), Coef('Var'  , 0.160164    ), Coef('Var'  , 0.138269    ), Coef('Var'  , 0.116116    ), Coef('Var'  , 0.1063      ), Coef('Var'  , 0.0961749   ), Coef('Var'  , 0.153501    ), ], 
		[Coef('Var'  , 0.28572     ), Coef('Var'  , 0.239882    ), Coef('Var'  , 0.19493     ), Coef('Var'  , 0.170449    ), Coef('Var'  , 0.147044    ), Coef('Var'  , 0.154258    ), Coef('Var'  , 0.163055    ), Coef('Var'  , 0.209673    ), Coef('Var'  , 0.257943    ), Coef('Var'  , 0.271264    ), ], 
		[Coef('Var'  , 0.203125    ), Coef('Var'  , 0.149855    ), Coef('Var'  , 0.0972333   ), Coef('Var'  , 0.108055    ), Coef('Var'  , 0.119617    ), Coef('Var'  , 0.149377    ), Coef('Var'  , 0.180804    ), Coef('Var'  , 0.226834    ), Coef('Var'  , 0.274895    ), Coef('Var'  , 0.23839     ), ], 
		[Coef('Var'  , 0.0806459   ), Coef('Var'  , 0.0724994   ), Coef('Var'  , 0.0641074   ), Coef('Var'  , 0.0856822   ), Coef('Var'  , 0.10667     ), Coef('Var'  , 0.124567    ), Coef('Var'  , 0.14286     ), Coef('Var'  , 0.144763    ), Coef('Var'  , 0.147841    ), Coef('Var'  , 0.113992    ), ], 
		[Coef('Var'  , 0.0263211   ), Coef('Var'  , 0.0372471   ), Coef('Var'  , 0.0469815   ), Coef('Var'  , 0.0694749   ), Coef('Var'  , 0.0902747   ), Coef('Var'  , 0.0940031   ), Coef('Var'  , 0.0964246   ), Coef('Var'  , 0.0755591   ), Coef('Var'  , 0.0539724   ), Coef('Var'  , 0.0405344   ), ], ])
	etat1.initMat[Chem([Sub('2')])] = FMat([
		[Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0569271   ), Coef('Var'  , 0.113516    ), Coef('Var'  , 0.181927    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0164202   ), Coef('Var'  , 0.0323739   ), Coef('Var'  , 0.0164202   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.019562    ), Coef('Var'  , 0.0385316   ), Coef('Var'  , 0.0195619   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0178472   ), Coef('Var'  , 0.0353449   ), Coef('Var'  , 0.0178471   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.111111    ), Coef('Var'  , 0.0997478   ), Coef('Var'  , 0.0885965   ), Coef('Var'  , 0.0441922   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.333333    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.332115    ), Coef('Var'  , 0.2203      ), Coef('Var'  , 0.109893    ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.666667    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.363746    ), Coef('Var'  , 0.283872    ), Coef('Var'  , 0.266524    ), ], 
		[Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0936352   ), Coef('Var'  , 0.187466    ), Coef('Var'  , 0.343635    ), ], ])
	etat1.initMat[Chem([Sub('3')])] = FMat([
		[Coef('Var'  , 0.131988    ), Coef('Var'  , 0.134416    ), Coef('Var'  , 0.137734    ), Coef('Var'  , 0.138708    ), Coef('Var'  , 0.140865    ), Coef('Var'  , 0.137394    ), Coef('Var'  , 0.135119    ), Coef('Var'  , 0.133102    ), ], 
		[Coef('Var'  , 0.150355    ), Coef('Var'  , 0.156611    ), Coef('Var'  , 0.165979    ), Coef('Var'  , 0.164954    ), Coef('Var'  , 0.167224    ), Coef('Var'  , 0.157865    ), Coef('Var'  , 0.151599    ), Coef('Var'  , 0.149523    ), ], 
		[Coef('Var'  , 0.14699     ), Coef('Var'  , 0.14833     ), Coef('Var'  , 0.150975    ), Coef('Var'  , 0.14925     ), Coef('Var'  , 0.148941    ), Coef('Var'  , 0.14634     ), Coef('Var'  , 0.144956    ), Coef('Var'  , 0.14542     ), ], 
		[Coef('Var'  , 0.134497    ), Coef('Var'  , 0.132209    ), Coef('Var'  , 0.129104    ), Coef('Var'  , 0.127061    ), Coef('Var'  , 0.123888    ), Coef('Var'  , 0.127226    ), Coef('Var'  , 0.129281    ), Coef('Var'  , 0.132374    ), ], 
		[Coef('Var'  , 0.113484    ), Coef('Var'  , 0.110792    ), Coef('Var'  , 0.107816    ), Coef('Var'  , 0.105884    ), Coef('Var'  , 0.103332    ), Coef('Var'  , 0.106455    ), Coef('Var'  , 0.109001    ), Coef('Var'  , 0.111363    ), ], 
		[Coef('Var'  , 0.100594    ), Coef('Var'  , 0.0976341   ), Coef('Var'  , 0.0940508   ), Coef('Var'  , 0.0944332   ), Coef('Var'  , 0.0939169   ), Coef('Var'  , 0.0975654   ), Coef('Var'  , 0.100461    ), Coef('Var'  , 0.100766    ), ], 
		[Coef('Var'  , 0.111916    ), Coef('Var'  , 0.110141    ), Coef('Var'  , 0.106617    ), Coef('Var'  , 0.108856    ), Coef('Var'  , 0.109403    ), Coef('Var'  , 0.112876    ), Coef('Var'  , 0.114703    ), Coef('Var'  , 0.114162    ), ], 
		[Coef('Var'  , 0.110175    ), Coef('Var'  , 0.109866    ), Coef('Var'  , 0.107725    ), Coef('Var'  , 0.110854    ), Coef('Var'  , 0.11243     ), Coef('Var'  , 0.114278    ), Coef('Var'  , 0.11488     ), Coef('Var'  , 0.113291    ), ], ])
	etat1.initMat[Chem([Sub('4')])] = FMat([
		[Coef('Var'  , 0.133441    ), Coef('Var'  , 0.13611     ), Coef('Var'  , 0.138672    ), Coef('Var'  , 0.130457    ), Coef('Var'  , 0.121549    ), Coef('Var'  , 0.127802    ), ], 
		[Coef('Var'  , 0.130548    ), Coef('Var'  , 0.12266     ), Coef('Var'  , 0.114606    ), Coef('Var'  , 0.110526    ), Coef('Var'  , 0.10546     ), Coef('Var'  , 0.118143    ), ], 
		[Coef('Var'  , 0.134535    ), Coef('Var'  , 0.129853    ), Coef('Var'  , 0.12366     ), Coef('Var'  , 0.122754    ), Coef('Var'  , 0.119765    ), Coef('Var'  , 0.127858    ), ], 
		[Coef('Var'  , 0.120206    ), Coef('Var'  , 0.115161    ), Coef('Var'  , 0.108234    ), Coef('Var'  , 0.110779    ), Coef('Var'  , 0.111514    ), Coef('Var'  , 0.116623    ), ], 
		[Coef('Var'  , 0.111209    ), Coef('Var'  , 0.107584    ), Coef('Var'  , 0.104291    ), Coef('Var'  , 0.114611    ), Coef('Var'  , 0.12572     ), Coef('Var'  , 0.118018    ), ], 
		[Coef('Var'  , 0.11915     ), Coef('Var'  , 0.121933    ), Coef('Var'  , 0.125634    ), Coef('Var'  , 0.137602    ), Coef('Var'  , 0.151123    ), Coef('Var'  , 0.134416    ), ], 
		[Coef('Var'  , 0.126766    ), Coef('Var'  , 0.131659    ), Coef('Var'  , 0.138197    ), Coef('Var'  , 0.140034    ), Coef('Var'  , 0.144232    ), Coef('Var'  , 0.13485     ), ], 
		[Coef('Var'  , 0.124146    ), Coef('Var'  , 0.135039    ), Coef('Var'  , 0.146705    ), Coef('Var'  , 0.133237    ), Coef('Var'  , 0.120639    ), Coef('Var'  , 0.12229     ), ], ])
	etat1.initMat[Chem([Sub('5')])] = FMat([
		[Coef('Var'  , 0.0700989   ), Coef('Var'  , 0.0896392   ), Coef('Var'  , 0.107702    ), Coef('Var'  , 0.119636    ), Coef('Var'  , 0.130425    ), Coef('Var'  , 0.122298    ), Coef('Var'  , 0.113516    ), Coef('Var'  , 0.0923011   ), ], 
		[Coef('Var'  , 0.040854    ), Coef('Var'  , 0.0621548   ), Coef('Var'  , 0.0819824   ), Coef('Var'  , 0.083636    ), Coef('Var'  , 0.0836525   ), Coef('Var'  , 0.0586406   ), Coef('Var'  , 0.0323739   ), Coef('Var'  , 0.0371595   ), ], 
		[Coef('Var'  , 0.0545416   ), Coef('Var'  , 0.0771202   ), Coef('Var'  , 0.0978936   ), Coef('Var'  , 0.0966645   ), Coef('Var'  , 0.0930657   ), Coef('Var'  , 0.0667188   ), Coef('Var'  , 0.0385316   ), Coef('Var'  , 0.0471746   ), ], 
		[Coef('Var'  , 0.0568899   ), Coef('Var'  , 0.0753683   ), Coef('Var'  , 0.0929917   ), Coef('Var'  , 0.0875418   ), Coef('Var'  , 0.0805544   ), Coef('Var'  , 0.0585967   ), Coef('Var'  , 0.0353449   ), Coef('Var'  , 0.0464232   ), ], 
		[Coef('Var'  , 0.145804    ), Coef('Var'  , 0.138013    ), Coef('Var'  , 0.131549    ), Coef('Var'  , 0.115232    ), Coef('Var'  , 0.0998112   ), Coef('Var'  , 0.0940317   ), Coef('Var'  , 0.0885965   ), Coef('Var'  , 0.116813    ), ], 
		[Coef('Var'  , 0.280137    ), Coef('Var'  , 0.234136    ), Coef('Var'  , 0.190247    ), Coef('Var'  , 0.175234    ), Coef('Var'  , 0.162122    ), Coef('Var'  , 0.190616    ), Coef('Var'  , 0.2203      ), Coef('Var'  , 0.249519    ), ], 
		[Coef('Var'  , 0.261972    ), Coef('Var'  , 0.220265    ), Coef('Var'  , 0.180679    ), Coef('Var'  , 0.182816    ), Coef('Var'  , 0.188015    ), Coef('Var'  , 0.234648    ), Coef('Var'  , 0.283872    ), Coef('Var'  , 0.272097    ), ], 
		[Coef('Var'  , 0.0897023   ), Coef('Var'  , 0.103303    ), Coef('Var'  , 0.116955    ), Coef('Var'  , 0.13924     ), Coef('Var'  , 0.162355    ), Coef('Var'  , 0.17445     ), Coef('Var'  , 0.187466    ), Coef('Var'  , 0.138513    ), ], ])
	etat1.initMat[Chem([Sub('6')])] = FMat([
		[Coef('Var'  , 0.0999836   ), Coef('Var'  , 0.111497    ), Coef('Var'  , 0.121549    ), Coef('Var'  , 0.11534     ), Coef('Var'  , 0.107702    ), Coef('Var'  , 0.104688    ), ], 
		[Coef('Var'  , 0.088967    ), Coef('Var'  , 0.0977617   ), Coef('Var'  , 0.10546     ), Coef('Var'  , 0.0944198   ), Coef('Var'  , 0.0819824   ), Coef('Var'  , 0.0861729   ), ], 
		[Coef('Var'  , 0.11179     ), Coef('Var'  , 0.116665    ), Coef('Var'  , 0.119765    ), Coef('Var'  , 0.109887    ), Coef('Var'  , 0.0978936   ), Coef('Var'  , 0.105793    ), ], 
		[Coef('Var'  , 0.116116    ), Coef('Var'  , 0.114315    ), Coef('Var'  , 0.111514    ), Coef('Var'  , 0.102913    ), Coef('Var'  , 0.0929917   ), Coef('Var'  , 0.104987    ), ], 
		[Coef('Var'  , 0.163055    ), Coef('Var'  , 0.143573    ), Coef('Var'  , 0.12572     ), Coef('Var'  , 0.127915    ), Coef('Var'  , 0.131549    ), Coef('Var'  , 0.146442    ), ], 
		[Coef('Var'  , 0.180804    ), Coef('Var'  , 0.164853    ), Coef('Var'  , 0.151123    ), Coef('Var'  , 0.169553    ), Coef('Var'  , 0.190247    ), Coef('Var'  , 0.184321    ), ], 
		[Coef('Var'  , 0.14286     ), Coef('Var'  , 0.14269     ), Coef('Var'  , 0.144232    ), Coef('Var'  , 0.161304    ), Coef('Var'  , 0.180679    ), Coef('Var'  , 0.16077     ), ], 
		[Coef('Var'  , 0.0964246   ), Coef('Var'  , 0.108644    ), Coef('Var'  , 0.120639    ), Coef('Var'  , 0.118669    ), Coef('Var'  , 0.116955    ), Coef('Var'  , 0.106825    ), ], ])
	etat1.initMat[Chem([Sub('7')])] = FMat([
		[Coef('Var'  , 0.137734    ), Coef('Var'  , 0.134675    ), Coef('Var'  , 0.13226     ), Coef('Var'  , 0.141891    ), Coef('Var'  , 0.151722    ), Coef('Var'  , 0.151324    ), Coef('Var'  , 0.151535    ), Coef('Var'  , 0.144108    ), ], 
		[Coef('Var'  , 0.165979    ), Coef('Var'  , 0.164153    ), Coef('Var'  , 0.165211    ), Coef('Var'  , 0.20068     ), Coef('Var'  , 0.238238    ), Coef('Var'  , 0.217889    ), Coef('Var'  , 0.19985     ), Coef('Var'  , 0.181363    ), ], 
		[Coef('Var'  , 0.150975    ), Coef('Var'  , 0.15277     ), Coef('Var'  , 0.155814    ), Coef('Var'  , 0.169676    ), Coef('Var'  , 0.184473    ), Coef('Var'  , 0.171831    ), Coef('Var'  , 0.160242    ), Coef('Var'  , 0.154924    ), ], 
		[Coef('Var'  , 0.129104    ), Coef('Var'  , 0.133734    ), Coef('Var'  , 0.1378      ), Coef('Var'  , 0.131754    ), Coef('Var'  , 0.125575    ), Coef('Var'  , 0.12056     ), Coef('Var'  , 0.11502     ), Coef('Var'  , 0.122539    ), ], 
		[Coef('Var'  , 0.107816    ), Coef('Var'  , 0.112482    ), Coef('Var'  , 0.11706     ), Coef('Var'  , 0.109146    ), Coef('Var'  , 0.101485    ), Coef('Var'  , 0.0983545   ), Coef('Var'  , 0.095004    ), Coef('Var'  , 0.10169     ), ], 
		[Coef('Var'  , 0.0940508   ), Coef('Var'  , 0.0952866   ), Coef('Var'  , 0.0960199   ), Coef('Var'  , 0.0825649   ), Coef('Var'  , 0.0689109   ), Coef('Var'  , 0.0753653   ), Coef('Var'  , 0.0812323   ), Coef('Var'  , 0.0880871   ), ], 
		[Coef('Var'  , 0.106617    ), Coef('Var'  , 0.104095    ), Coef('Var'  , 0.0999559   ), Coef('Var'  , 0.0837166   ), Coef('Var'  , 0.0662264   ), Coef('Var'  , 0.0813156   ), Coef('Var'  , 0.0952501   ), Coef('Var'  , 0.101694    ), ], 
		[Coef('Var'  , 0.107725    ), Coef('Var'  , 0.102805    ), Coef('Var'  , 0.0958798   ), Coef('Var'  , 0.0805706   ), Coef('Var'  , 0.063369    ), Coef('Var'  , 0.0833603   ), Coef('Var'  , 0.101867    ), Coef('Var'  , 0.105595    ), ], ])
	etat1.initMat[Chem([Sub('G')])] = FMat([
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], ])
	etat1.initMat[Chem([Sub('8')])] = FMat([
		[Coef('Var'  , 0.140865    ), Coef('Var'  , 0.145597    ), Coef('Var'  , 0.151535    ), Coef('Var'  , 0.166116    ), Coef('Var'  , 0.18171     ), Coef('Var'  , 0.16352     ), Coef('Var'  , 0.14634     ), Coef('Var'  , 0.143       ), ], 
		[Coef('Var'  , 0.167224    ), Coef('Var'  , 0.18199     ), Coef('Var'  , 0.19985     ), Coef('Var'  , 0.220911    ), Coef('Var'  , 0.244207    ), Coef('Var'  , 0.206148    ), Coef('Var'  , 0.170051    ), Coef('Var'  , 0.167227    ), ], 
		[Coef('Var'  , 0.148941    ), Coef('Var'  , 0.153929    ), Coef('Var'  , 0.160242    ), Coef('Var'  , 0.161464    ), Coef('Var'  , 0.163493    ), Coef('Var'  , 0.155063    ), Coef('Var'  , 0.147123    ), Coef('Var'  , 0.147527    ), ], 
		[Coef('Var'  , 0.123888    ), Coef('Var'  , 0.120048    ), Coef('Var'  , 0.11502     ), Coef('Var'  , 0.0959631   ), Coef('Var'  , 0.0757656   ), Coef('Var'  , 0.0958389   ), Coef('Var'  , 0.114494    ), Coef('Var'  , 0.119923    ), ], 
		[Coef('Var'  , 0.103332    ), Coef('Var'  , 0.0995214   ), Coef('Var'  , 0.095004    ), Coef('Var'  , 0.0798775   ), Coef('Var'  , 0.0640787   ), Coef('Var'  , 0.0811458   ), Coef('Var'  , 0.0975925   ), Coef('Var'  , 0.10079     ), ], 
		[Coef('Var'  , 0.0939169   ), Coef('Var'  , 0.0880527   ), Coef('Var'  , 0.0812323   ), Coef('Var'  , 0.0725701   ), Coef('Var'  , 0.0630969   ), Coef('Var'  , 0.0792561   ), Coef('Var'  , 0.0948181   ), Coef('Var'  , 0.0947387   ), ], 
		[Coef('Var'  , 0.109403    ), Coef('Var'  , 0.103062    ), Coef('Var'  , 0.0952501   ), Coef('Var'  , 0.0936847   ), Coef('Var'  , 0.0914023   ), Coef('Var'  , 0.101879    ), Coef('Var'  , 0.111822    ), Coef('Var'  , 0.111256    ), ], 
		[Coef('Var'  , 0.11243     ), Coef('Var'  , 0.107801    ), Coef('Var'  , 0.101867    ), Coef('Var'  , 0.109413    ), Coef('Var'  , 0.116247    ), Coef('Var'  , 0.117149    ), Coef('Var'  , 0.11776     ), Coef('Var'  , 0.115537    ), ], ])
	etat1.initMat[Chem([Sub('9')])] = FMat([
		[Coef('Var'  , 0.131988    ), Coef('Var'  , 0.129276    ), Coef('Var'  , 0.127066    ), Coef('Var'  , 0.118278    ), Coef('Var'  , 0.109251    ), Coef('Var'  , 0.120874    ), Coef('Var'  , 0.13226     ), Coef('Var'  , 0.131872    ), ], 
		[Coef('Var'  , 0.150355    ), Coef('Var'  , 0.141675    ), Coef('Var'  , 0.135411    ), Coef('Var'  , 0.127187    ), Coef('Var'  , 0.12038     ), Coef('Var'  , 0.14195     ), Coef('Var'  , 0.165211    ), Coef('Var'  , 0.156438    ), ], 
		[Coef('Var'  , 0.14699     ), Coef('Var'  , 0.144454    ), Coef('Var'  , 0.142696    ), Coef('Var'  , 0.144536    ), Coef('Var'  , 0.146599    ), Coef('Var'  , 0.150937    ), Coef('Var'  , 0.155814    ), Coef('Var'  , 0.150854    ), ], 
		[Coef('Var'  , 0.134497    ), Coef('Var'  , 0.136266    ), Coef('Var'  , 0.137274    ), Coef('Var'  , 0.148907    ), Coef('Var'  , 0.160164    ), Coef('Var'  , 0.149031    ), Coef('Var'  , 0.1378      ), Coef('Var'  , 0.13639     ), ], 
		[Coef('Var'  , 0.113484    ), Coef('Var'  , 0.116488    ), Coef('Var'  , 0.119646    ), Coef('Var'  , 0.13293     ), Coef('Var'  , 0.147044    ), Coef('Var'  , 0.131663    ), Coef('Var'  , 0.11706     ), Coef('Var'  , 0.115221    ), ], 
		[Coef('Var'  , 0.100594    ), Coef('Var'  , 0.105141    ), Coef('Var'  , 0.109608    ), Coef('Var'  , 0.114307    ), Coef('Var'  , 0.119617    ), Coef('Var'  , 0.107619    ), Coef('Var'  , 0.0960199   ), Coef('Var'  , 0.0984532   ), ], 
		[Coef('Var'  , 0.111916    ), Coef('Var'  , 0.114942    ), Coef('Var'  , 0.116526    ), Coef('Var'  , 0.112034    ), Coef('Var'  , 0.10667     ), Coef('Var'  , 0.103841    ), Coef('Var'  , 0.0999559   ), Coef('Var'  , 0.106748    ), ], 
		[Coef('Var'  , 0.110175    ), Coef('Var'  , 0.111759    ), Coef('Var'  , 0.111772    ), Coef('Var'  , 0.10182     ), Coef('Var'  , 0.0902747   ), Coef('Var'  , 0.0940843   ), Coef('Var'  , 0.0958798   ), Coef('Var'  , 0.104023    ), ], ])
	etat1.initMat[Chem([Sub('10')])] = FMat([
		[Coef('Var'  , 0.135119    ), Coef('Var'  , 0.140198    ), Coef('Var'  , 0.14634     ), Coef('Var'  , 0.139629    ), Coef('Var'  , 0.133441    ), Coef('Var'  , 0.130197    ), Coef('Var'  , 0.127066    ), Coef('Var'  , 0.130766    ), ], 
		[Coef('Var'  , 0.151599    ), Coef('Var'  , 0.159512    ), Coef('Var'  , 0.170051    ), Coef('Var'  , 0.149576    ), Coef('Var'  , 0.130548    ), Coef('Var'  , 0.132366    ), Coef('Var'  , 0.135411    ), Coef('Var'  , 0.142302    ), ], 
		[Coef('Var'  , 0.144956    ), Coef('Var'  , 0.145612    ), Coef('Var'  , 0.147123    ), Coef('Var'  , 0.140878    ), Coef('Var'  , 0.134535    ), Coef('Var'  , 0.138725    ), Coef('Var'  , 0.142696    ), Coef('Var'  , 0.143459    ), ], 
		[Coef('Var'  , 0.129281    ), Coef('Var'  , 0.12258     ), Coef('Var'  , 0.114494    ), Coef('Var'  , 0.118141    ), Coef('Var'  , 0.120206    ), Coef('Var'  , 0.129335    ), Coef('Var'  , 0.137274    ), Coef('Var'  , 0.133774    ), ], 
		[Coef('Var'  , 0.109001    ), Coef('Var'  , 0.103529    ), Coef('Var'  , 0.0975925   ), Coef('Var'  , 0.104427    ), Coef('Var'  , 0.111209    ), Coef('Var'  , 0.115217    ), Coef('Var'  , 0.119646    ), Coef('Var'  , 0.114319    ), ], 
		[Coef('Var'  , 0.100461    ), Coef('Var'  , 0.0979052   ), Coef('Var'  , 0.0948181   ), Coef('Var'  , 0.106913    ), Coef('Var'  , 0.11915     ), Coef('Var'  , 0.114114    ), Coef('Var'  , 0.109608    ), Coef('Var'  , 0.105107    ), ], 
		[Coef('Var'  , 0.114703    ), Coef('Var'  , 0.113909    ), Coef('Var'  , 0.111822    ), Coef('Var'  , 0.119383    ), Coef('Var'  , 0.126766    ), Coef('Var'  , 0.121783    ), Coef('Var'  , 0.116526    ), Coef('Var'  , 0.116309    ), ], 
		[Coef('Var'  , 0.11488     ), Coef('Var'  , 0.116755    ), Coef('Var'  , 0.11776     ), Coef('Var'  , 0.121053    ), Coef('Var'  , 0.124146    ), Coef('Var'  , 0.118263    ), Coef('Var'  , 0.111772    ), Coef('Var'  , 0.113965    ), ], ])
	etat1.initMat[Chem([Sub('11')])] = FMat([
		[Coef('Const', 0.25        ), Coef('Var'  , 0.200826    ), Coef('Var'  , 0.151722    ), Coef('Var'  , 0.113006    ), Coef('Var'  , 0.0740756   ), Coef('Var'  , 0.0371805   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.5         ), Coef('Var'  , 0.36869     ), Coef('Var'  , 0.238238    ), Coef('Var'  , 0.16733     ), Coef('Var'  , 0.0975769   ), Coef('Var'  , 0.0486398   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0.25        ), Coef('Var'  , 0.217029    ), Coef('Var'  , 0.184473    ), Coef('Var'  , 0.180121    ), Coef('Var'  , 0.176306    ), Coef('Var'  , 0.213091    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.062797    ), Coef('Var'  , 0.125575    ), Coef('Var'  , 0.187091    ), Coef('Var'  , 0.248789    ), Coef('Var'  , 0.374294    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0506909   ), Coef('Var'  , 0.101485    ), Coef('Var'  , 0.147932    ), Coef('Var'  , 0.19493     ), Coef('Var'  , 0.222241    ), Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.034512    ), Coef('Var'  , 0.0689109   ), Coef('Var'  , 0.0830008   ), Coef('Var'  , 0.0972333   ), Coef('Var'  , 0.0484888   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0333654   ), Coef('Var'  , 0.0662264   ), Coef('Var'  , 0.065558    ), Coef('Var'  , 0.0641074   ), Coef('Var'  , 0.0321926   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0320893   ), Coef('Var'  , 0.063369    ), Coef('Var'  , 0.0559612   ), Coef('Var'  , 0.0469815   ), Coef('Var'  , 0.0238718   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], ])
	etat1.initMat[Chem([Sub('12')])] = FMat([
		[Coef('Var'  , 0.130425    ), Coef('Var'  , 0.137407    ), Coef('Var'  , 0.144102    ), Coef('Var'  , 0.148437    ), Coef('Var'  , 0.152938    ), Coef('Var'  , 0.141772    ), ], 
		[Coef('Var'  , 0.0836525   ), Coef('Var'  , 0.09546     ), Coef('Var'  , 0.105819    ), Coef('Var'  , 0.106421    ), Coef('Var'  , 0.105804    ), Coef('Var'  , 0.0954021   ), ], 
		[Coef('Var'  , 0.0930657   ), Coef('Var'  , 0.104619    ), Coef('Var'  , 0.113597    ), Coef('Var'  , 0.112195    ), Coef('Var'  , 0.108252    ), Coef('Var'  , 0.10189     ), ], 
		[Coef('Var'  , 0.0805544   ), Coef('Var'  , 0.0892554   ), Coef('Var'  , 0.0957829   ), Coef('Var'  , 0.0927622   ), Coef('Var'  , 0.0873241   ), Coef('Var'  , 0.0850058   ), ], 
		[Coef('Var'  , 0.0998112   ), Coef('Var'  , 0.0972416   ), Coef('Var'  , 0.094646    ), Coef('Var'  , 0.0905706   ), Coef('Var'  , 0.0860626   ), Coef('Var'  , 0.0930079   ), ], 
		[Coef('Var'  , 0.162122    ), Coef('Var'  , 0.144471    ), Coef('Var'  , 0.127852    ), Coef('Var'  , 0.122471    ), Coef('Var'  , 0.11765     ), Coef('Var'  , 0.139448    ), ], 
		[Coef('Var'  , 0.188015    ), Coef('Var'  , 0.167915    ), Coef('Var'  , 0.151502    ), Coef('Var'  , 0.151677    ), Coef('Var'  , 0.155622    ), Coef('Var'  , 0.17001     ), ], 
		[Coef('Var'  , 0.162355    ), Coef('Var'  , 0.16363     ), Coef('Var'  , 0.166698    ), Coef('Var'  , 0.175465    ), Coef('Var'  , 0.186346    ), Coef('Var'  , 0.173465    ), ], ])
	etat1.initMat[Chem([Sub('13')])] = FMat([
		[Coef('Var'  , 0.183977    ), Coef('Var'  , 0.168229    ), Coef('Var'  , 0.152938    ), Coef('Var'  , 0.153534    ), Coef('Var'  , 0.154463    ), Coef('Var'  , 0.168961    ), ], 
		[Coef('Var'  , 0.1156      ), Coef('Var'  , 0.111       ), Coef('Var'  , 0.105804    ), Coef('Var'  , 0.109322    ), Coef('Var'  , 0.111809    ), Coef('Var'  , 0.113959    ), ], 
		[Coef('Var'  , 0.0982181   ), Coef('Var'  , 0.104135    ), Coef('Var'  , 0.108252    ), Coef('Var'  , 0.112452    ), Coef('Var'  , 0.114275    ), Coef('Var'  , 0.107121    ), ], 
		[Coef('Var'  , 0.0664516   ), Coef('Var'  , 0.0779133   ), Coef('Var'  , 0.0873241   ), Coef('Var'  , 0.0913235   ), Coef('Var'  , 0.0929224   ), Coef('Var'  , 0.0807242   ), ], 
		[Coef('Var'  , 0.0601465   ), Coef('Var'  , 0.0734134   ), Coef('Var'  , 0.0860626   ), Coef('Var'  , 0.0867882   ), Coef('Var'  , 0.0869643   ), Coef('Var'  , 0.0738646   ), ], 
		[Coef('Var'  , 0.0729725   ), Coef('Var'  , 0.0952647   ), Coef('Var'  , 0.11765     ), Coef('Var'  , 0.11387     ), Coef('Var'  , 0.110447    ), Coef('Var'  , 0.0916874   ), ], 
		[Coef('Var'  , 0.157919    ), Coef('Var'  , 0.155352    ), Coef('Var'  , 0.155622    ), Coef('Var'  , 0.148975    ), Coef('Var'  , 0.145901    ), Coef('Var'  , 0.150555    ), ], 
		[Coef('Var'  , 0.244715    ), Coef('Var'  , 0.214692    ), Coef('Var'  , 0.186346    ), Coef('Var'  , 0.183735    ), Coef('Var'  , 0.183218    ), Coef('Var'  , 0.213127    ), ], ])
	etat1.initMat[Chem([Sub('14')])] = FMat([
		[Coef('Var'  , 0.138672    ), Coef('Var'  , 0.146515    ), Coef('Var'  , 0.154463    ), Coef('Var'  , 0.149169    ), Coef('Var'  , 0.144102    ), Coef('Var'  , 0.141419    ), ], 
		[Coef('Var'  , 0.114606    ), Coef('Var'  , 0.113662    ), Coef('Var'  , 0.111809    ), Coef('Var'  , 0.10938     ), Coef('Var'  , 0.105819    ), Coef('Var'  , 0.110761    ), ], 
		[Coef('Var'  , 0.12366     ), Coef('Var'  , 0.120093    ), Coef('Var'  , 0.114275    ), Coef('Var'  , 0.115181    ), Coef('Var'  , 0.113597    ), Coef('Var'  , 0.119837    ), ], 
		[Coef('Var'  , 0.108234    ), Coef('Var'  , 0.101726    ), Coef('Var'  , 0.0929224   ), Coef('Var'  , 0.0955731   ), Coef('Var'  , 0.0957829   ), Coef('Var'  , 0.103165    ), ], 
		[Coef('Var'  , 0.104291    ), Coef('Var'  , 0.095708    ), Coef('Var'  , 0.0869643   ), Coef('Var'  , 0.0910219   ), Coef('Var'  , 0.094646    ), Coef('Var'  , 0.0994904   ), ], 
		[Coef('Var'  , 0.125634    ), Coef('Var'  , 0.117706    ), Coef('Var'  , 0.110447    ), Coef('Var'  , 0.118894    ), Coef('Var'  , 0.127852    ), Coef('Var'  , 0.126307    ), ], 
		[Coef('Var'  , 0.138197    ), Coef('Var'  , 0.140511    ), Coef('Var'  , 0.145901    ), Coef('Var'  , 0.14688     ), Coef('Var'  , 0.151502    ), Coef('Var'  , 0.143212    ), ], 
		[Coef('Var'  , 0.146705    ), Coef('Var'  , 0.164079    ), Coef('Var'  , 0.183218    ), Coef('Var'  , 0.1739      ), Coef('Var'  , 0.166698    ), Coef('Var'  , 0.155808    ), ], ])
	etat1.initMat[Chem([Sub('15')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0164585   ), Coef('Var'  , 0.0325498   ), Coef('Var'  , 0.0164586   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0176947   ), Coef('Var'  , 0.035274    ), Coef('Var'  , 0.0176948   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.187761    ), Coef('Var'  , 0.125425    ), Coef('Var'  , 0.0627613   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.355396    ), Coef('Var'  , 0.21094     ), Coef('Var'  , 0.105396    ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.267641    ), Coef('Var'  , 0.28572     ), Coef('Var'  , 0.364863    ), Coef('Const', 0.444444    ), Coef('Const', 0.666667    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.101367    ), Coef('Var'  , 0.203125    ), Coef('Var'  , 0.323589    ), Coef('Const', 0.444444    ), Coef('Const', 0.333333    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0403068   ), Coef('Var'  , 0.0806459   ), Coef('Var'  , 0.0958624   ), Coef('Const', 0.111111    ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0133753   ), Coef('Var'  , 0.0263211   ), Coef('Var'  , 0.0133754   ), Coef('Const', 0           ), Coef('Const', 0           ), ], ])
	etat1.initMat[Chem([Sub('16')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.026539    ), Coef('Var'  , 0.0524044   ), Coef('Var'  , 0.0619131   ), Coef('Var'  , 0.0700989   ), Coef('Var'  , 0.0353742   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0214949   ), Coef('Var'  , 0.0425064   ), Coef('Var'  , 0.0422341   ), Coef('Var'  , 0.040854    ), Coef('Var'  , 0.0207394   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0373718   ), Coef('Var'  , 0.0742619   ), Coef('Var'  , 0.0649844   ), Coef('Var'  , 0.0545416   ), Coef('Var'  , 0.0276127   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0481049   ), Coef('Var'  , 0.0961749   ), Coef('Var'  , 0.0766809   ), Coef('Var'  , 0.0568899   ), Coef('Var'  , 0.0285761   ), ], 
		[Coef('Const', 0.111111    ), Coef('Const', 0.222222    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.350845    ), Coef('Var'  , 0.257943    ), Coef('Var'  , 0.201243    ), Coef('Var'  , 0.145804    ), Coef('Var'  , 0.128176    ), ], 
		[Coef('Const', 0.444444    ), Coef('Const', 0.555556    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.359245    ), Coef('Var'  , 0.274895    ), Coef('Var'  , 0.276649    ), Coef('Var'  , 0.280137    ), Coef('Var'  , 0.361848    ), ], 
		[Coef('Const', 0.444444    ), Coef('Const', 0.222222    ), Coef('Const', 0.111111    ), Coef('Var'  , 0.129241    ), Coef('Var'  , 0.147841    ), Coef('Var'  , 0.204258    ), Coef('Var'  , 0.261972    ), Coef('Var'  , 0.352795    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0271591   ), Coef('Var'  , 0.0539724   ), Coef('Var'  , 0.0720371   ), Coef('Var'  , 0.0897023   ), Coef('Var'  , 0.0448781   ), ], ])
	
	
	
	etat2.bords   = {Bord('0'): etat20, Bord('1'): etat19, Bord('2'): etat19, Bord('3'): etat21, Bord('4'): etat22, }
	etat2.permuts = {}
	etat2.interns = {Intern('_'): etat2, }
	etat2.subs    = {Sub('0'): etat1, Sub('1'): etat3, Sub('2'): etat4, Sub('3'): etat5, Sub('4'): etat6, Sub('5'): etat7, Sub('6'): etat8, Sub('7'): etat9, Sub('G', True): Etat.etatPoint, Sub('8'): etat10, Sub('9'): etat11, Sub('10'): etat12, Sub('11'): etat13, Sub('12'): etat14, Sub('13'): etat15, Sub('14'): etat16, Sub('15'): etat17, Sub('16'): etat18, }
	
	etat2.buildIntern()
	
	
	etat2.eqs = [
		(Chem([Bord('1'), Sub('1'), Permut('0'), ])	,	Chem([Sub('0'), Bord('0'), ])),
		(Chem([Bord('2'), Sub('0'), Permut('0'), ])	,	Chem([Sub('0'), Bord('3'), ])),
		(Chem([Bord('2'), Sub('1'), Permut('0'), ])	,	Chem([Sub('2'), Bord('0'), ])),
		(Chem([Bord('3'), Sub('0'), Permut('0'), ])	,	Chem([Sub('2'), Bord('3'), ])),
		(Chem([Bord('4'), Sub('2'), Permut('0'), ])	,	Chem([Sub('4'), Bord('0'), ])),
		(Chem([Bord('3'), Sub('1'), Permut('0'), ])	,	Chem([Sub('5'), Bord('2'), ])),
		(Chem([Bord('0'), Sub('1'), Permut('0'), ])	,	Chem([Sub('7'), Bord('2'), ])),
		(Chem([Bord('0'), Sub('0'), Permut('0'), ])	,	Chem([Sub('8'), Bord('1'), ])),
		(Chem([Bord('4'), Sub('4'), Permut('0'), ])	,	Chem([Sub('8'), Bord('2'), ])),
		(Chem([Bord('4'), Sub('3'), Permut('0'), ])	,	Chem([Sub('10'), Bord('1'), ])),
		(Chem([Bord('0'), Sub('2'), Permut('0'), ])	,	Chem([Sub('11'), Bord('0'), ])),
		(Chem([Bord('1'), Sub('0'), Permut('0'), ])	,	Chem([Sub('11'), Bord('4'), ])),
		(Chem([Bord('3'), Sub('2'), Permut('0'), ])	,	Chem([Sub('12'), Bord('2'), ])),
		(Chem([Bord('3'), Sub('3'), Permut('0'), ])	,	Chem([Sub('13'), Bord('0'), ])),
		(Chem([Bord('4'), Sub('0'), Permut('0'), ])	,	Chem([Sub('13'), Bord('2'), ])),
		(Chem([Bord('4'), Sub('1'), Permut('0'), ])	,	Chem([Sub('14'), Bord('0'), ])),
		(Chem([Sub('0'), Bord('0'), Bord('1'), ])	,	Chem([Sub('11'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('1'), Bord('1'), ])	,	Chem([Sub('15'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('2'), Bord('1'), ])	,	Chem([Sub('2'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('0'), Bord('1'), ])	,	Chem([Sub('11'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('1'), Bord('1'), ])	,	Chem([Sub('9'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('2'), Bord('1'), ])	,	Chem([Sub('6'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('3'), Bord('1'), ])	,	Chem([Sub('16'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('4'), Bord('1'), ])	,	Chem([Sub('15'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('1'), Bord('1'), ])	,	Chem([Sub('16'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('2'), Bord('1'), ])	,	Chem([Sub('5'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('3'), Bord('0'), Bord('1'), ])	,	Chem([Sub('7'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('3'), Bord('1'), Bord('1'), ])	,	Chem([Sub('8'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('3'), Bord('2'), Bord('1'), ])	,	Chem([Sub('10'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('3'), Bord('3'), Bord('1'), ])	,	Chem([Sub('9'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('4'), Bord('0'), Bord('1'), ])	,	Chem([Sub('14'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('4'), Bord('1'), Bord('1'), ])	,	Chem([Sub('6'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('4'), Bord('2'), Bord('1'), ])	,	Chem([Sub('10'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('5'), Bord('0'), Bord('1'), ])	,	Chem([Sub('6'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('5'), Bord('1'), Bord('1'), ])	,	Chem([Sub('12'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('5'), Bord('3'), Bord('1'), ])	,	Chem([Sub('16'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('7'), Bord('0'), Bord('1'), ])	,	Chem([Sub('9'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('7'), Bord('1'), Bord('1'), ])	,	Chem([Sub('11'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('7'), Bord('2'), Bord('1'), ])	,	Chem([Sub('8'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('8'), Bord('2'), Bord('1'), ])	,	Chem([Sub('10'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('9'), Bord('0'), Bord('1'), ])	,	Chem([Sub('10'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('11'), Bord('2'), Bord('1'), ])	,	Chem([Sub('15'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('12'), Bord('0'), Bord('1'), ])	,	Chem([Sub('14'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('12'), Bord('1'), Bord('1'), ])	,	Chem([Sub('13'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('13'), Bord('1'), Bord('1'), ])	,	Chem([Sub('14'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('15'), Bord('2'), Bord('1'), ])	,	Chem([Sub('16'), Bord('0'), Bord('1'), ])),
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
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0125814   ), Coef('Var'  , 0.0250001   ), Coef('Var'  , 0.0125814   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0183441   ), Coef('Var'  , 0.0365429   ), Coef('Var'  , 0.0183441   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.192994    ), Coef('Var'  , 0.136245    ), Coef('Var'  , 0.067994    ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.358398    ), Coef('Var'  , 0.216867    ), Coef('Var'  , 0.108398    ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.223066    ), Coef('Var'  , 0.196269    ), Coef('Var'  , 0.223066    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0893446   ), Coef('Var'  , 0.178712    ), Coef('Var'  , 0.339345    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0636136   ), Coef('Var'  , 0.127792    ), Coef('Var'  , 0.188614    ), Coef('Const', 0.25        ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0184777   ), Coef('Var'  , 0.0369667   ), Coef('Var'  , 0.0184777   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0118098   ), Coef('Var'  , 0.0232578   ), Coef('Var'  , 0.0118098   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0113712   ), Coef('Var'  , 0.0223484   ), Coef('Var'  , 0.0113712   ), Coef('Const', 0           ), Coef('Const', 0           ), ], ])
	etat2.initMat[Chem([Sub('1')])] = FMat([
		[Coef('Var'  , 0.0693385   ), Coef('Var'  , 0.0861995   ), Coef('Var'  , 0.10366     ), Coef('Var'  , 0.146509    ), Coef('Var'  , 0.192378    ), Coef('Var'  , 0.161613    ), Coef('Var'  , 0.133968    ), Coef('Var'  , 0.104243    ), Coef('Var'  , 0.0751999   ), Coef('Var'  , 0.0723318   ), ], 
		[Coef('Var'  , 0.103892    ), Coef('Var'  , 0.151441    ), Coef('Var'  , 0.198861    ), Coef('Var'  , 0.180739    ), Coef('Var'  , 0.163334    ), Coef('Var'  , 0.118888    ), Coef('Var'  , 0.0747293   ), Coef('Var'  , 0.0724001   ), Coef('Var'  , 0.0692507   ), Coef('Var'  , 0.0869625   ), ], 
		[Coef('Var'  , 0.155226    ), Coef('Var'  , 0.193907    ), Coef('Var'  , 0.233658    ), Coef('Var'  , 0.190465    ), Coef('Var'  , 0.148491    ), Coef('Var'  , 0.112581    ), Coef('Var'  , 0.0773243   ), Coef('Var'  , 0.0859531   ), Coef('Var'  , 0.0947103   ), Coef('Var'  , 0.124673    ), ], 
		[Coef('Var'  , 0.143849    ), Coef('Var'  , 0.128501    ), Coef('Var'  , 0.112777    ), Coef('Var'  , 0.0873329   ), Coef('Var'  , 0.0605144   ), Coef('Var'  , 0.0587162   ), Coef('Var'  , 0.0548295   ), Coef('Var'  , 0.0746012   ), Coef('Var'  , 0.0929127   ), Coef('Var'  , 0.118681    ), ], 
		[Coef('Var'  , 0.113553    ), Coef('Var'  , 0.0973087   ), Coef('Var'  , 0.0809913   ), Coef('Var'  , 0.0652614   ), Coef('Var'  , 0.0484327   ), Coef('Var'  , 0.0497159   ), Coef('Var'  , 0.0494107   ), Coef('Var'  , 0.0687662   ), Coef('Var'  , 0.0873071   ), Coef('Var'  , 0.100479    ), ], 
		[Coef('Var'  , 0.08983     ), Coef('Var'  , 0.0722746   ), Coef('Var'  , 0.0541496   ), Coef('Var'  , 0.0484139   ), Coef('Var'  , 0.041144    ), Coef('Var'  , 0.0462474   ), Coef('Var'  , 0.0495312   ), Coef('Var'  , 0.0693446   ), Coef('Var'  , 0.088206    ), Coef('Var'  , 0.0892285   ), ], 
		[Coef('Var'  , 0.127063    ), Coef('Var'  , 0.0962597   ), Coef('Var'  , 0.0668585   ), Coef('Var'  , 0.0661527   ), Coef('Var'  , 0.0654041   ), Coef('Var'  , 0.0966479   ), Coef('Var'  , 0.128221    ), Coef('Var'  , 0.156021    ), Coef('Var'  , 0.185849    ), Coef('Var'  , 0.15525     ), ], 
		[Coef('Var'  , 0.0818168   ), Coef('Var'  , 0.0635663   ), Coef('Var'  , 0.0452813   ), Coef('Var'  , 0.0512725   ), Coef('Var'  , 0.0568421   ), Coef('Var'  , 0.0923229   ), Coef('Var'  , 0.12803     ), Coef('Var'  , 0.131143    ), Coef('Var'  , 0.135253    ), Coef('Var'  , 0.108232    ), ], 
		[Coef('Var'  , 0.0568951   ), Coef('Var'  , 0.0509763   ), Coef('Var'  , 0.0438649   ), Coef('Var'  , 0.0626283   ), Coef('Var'  , 0.0803851   ), Coef('Var'  , 0.109102    ), Coef('Var'  , 0.137239    ), Coef('Var'  , 0.112616    ), Coef('Var'  , 0.0874783   ), Coef('Var'  , 0.0727157   ), ], 
		[Coef('Var'  , 0.0585367   ), Coef('Var'  , 0.0595662   ), Coef('Var'  , 0.0598996   ), Coef('Var'  , 0.101225    ), Coef('Var'  , 0.143075    ), Coef('Var'  , 0.154167    ), Coef('Var'  , 0.166718    ), Coef('Var'  , 0.124912    ), Coef('Var'  , 0.083833    ), Coef('Var'  , 0.0714467   ), ], ])
	etat2.initMat[Chem([Sub('2')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0125345   ), Coef('Var'  , 0.0248511   ), Coef('Var'  , 0.0125345   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0122108   ), Coef('Var'  , 0.0240908   ), Coef('Var'  , 0.0122108   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0185072   ), Coef('Var'  , 0.0369787   ), Coef('Var'  , 0.0185072   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0212589   ), Coef('Var'  , 0.0423505   ), Coef('Var'  , 0.0212589   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.179324    ), Coef('Var'  , 0.108626    ), Coef('Var'  , 0.0543245   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.338831    ), Coef('Var'  , 0.177657    ), Coef('Var'  , 0.0888309   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.287933    ), Coef('Var'  , 0.326653    ), Coef('Var'  , 0.444183    ), Coef('Const', 0.5625      ), Coef('Const', 0.75        ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0883984   ), Coef('Var'  , 0.177087    ), Coef('Var'  , 0.275898    ), Coef('Const', 0.375       ), Coef('Const', 0.25        ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0270848   ), Coef('Var'  , 0.0539718   ), Coef('Var'  , 0.0583348   ), Coef('Const', 0.0625      ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0139165   ), Coef('Var'  , 0.0277341   ), Coef('Var'  , 0.0139165   ), Coef('Const', 0           ), Coef('Const', 0           ), ], ])
	etat2.initMat[Chem([Sub('3')])] = FMat([
		[Coef('Var'  , 0.325919    ), Coef('Var'  , 0.339486    ), Coef('Var'  , 0.360072    ), Coef('Var'  , 0.40899     ), Coef('Var'  , 0.462946    ), Coef('Var'  , 0.443347    ), Coef('Var'  , 0.428793    ), Coef('Var'  , 0.373843    ), ], 
		[Coef('Var'  , 0.194232    ), Coef('Var'  , 0.234168    ), Coef('Var'  , 0.276408    ), Coef('Var'  , 0.242651    ), Coef('Var'  , 0.210556    ), Coef('Var'  , 0.168659    ), Coef('Var'  , 0.12838     ), Coef('Var'  , 0.160176    ), ], 
		[Coef('Var'  , 0.118806    ), Coef('Var'  , 0.122038    ), Coef('Var'  , 0.126663    ), Coef('Var'  , 0.100506    ), Coef('Var'  , 0.0753078   ), Coef('Var'  , 0.0709093   ), Coef('Var'  , 0.0674511   ), Coef('Var'  , 0.092441    ), ], 
		[Coef('Var'  , 0.0301398   ), Coef('Var'  , 0.0270091   ), Coef('Var'  , 0.0213593   ), Coef('Var'  , 0.0178512   ), Coef('Var'  , 0.0125627   ), Coef('Var'  , 0.01784     ), Coef('Var'  , 0.0213432   ), Coef('Var'  , 0.026998    ), ], 
		[Coef('Var'  , 0.026558    ), Coef('Var'  , 0.0239973   ), Coef('Var'  , 0.0189495   ), Coef('Var'  , 0.016048    ), Coef('Var'  , 0.0113759   ), Coef('Var'  , 0.0160721   ), Coef('Var'  , 0.0189845   ), Coef('Var'  , 0.0240215   ), ], 
		[Coef('Var'  , 0.0252494   ), Coef('Var'  , 0.0229855   ), Coef('Var'  , 0.0181296   ), Coef('Var'  , 0.01547     ), Coef('Var'  , 0.0109874   ), Coef('Var'  , 0.0154547   ), Coef('Var'  , 0.0181073   ), Coef('Var'  , 0.0229701   ), ], 
		[Coef('Var'  , 0.0297301   ), Coef('Var'  , 0.0265232   ), Coef('Var'  , 0.0210034   ), Coef('Var'  , 0.0174794   ), Coef('Var'  , 0.0122887   ), Coef('Var'  , 0.0174877   ), Coef('Var'  , 0.0210154   ), Coef('Var'  , 0.0265315   ), ], 
		[Coef('Var'  , 0.0230394   ), Coef('Var'  , 0.0203196   ), Coef('Var'  , 0.0161321   ), Coef('Var'  , 0.0132016   ), Coef('Var'  , 0.00920184  ), Coef('Var'  , 0.0131858   ), Coef('Var'  , 0.0161091   ), Coef('Var'  , 0.0203038   ), ], 
		[Coef('Var'  , 0.0585185   ), Coef('Var'  , 0.0475564   ), Coef('Var'  , 0.0355426   ), Coef('Var'  , 0.0350964   ), Coef('Var'  , 0.0339018   ), Coef('Var'  , 0.0457643   ), Coef('Var'  , 0.0568777   ), Coef('Var'  , 0.0582243   ), ], 
		[Coef('Var'  , 0.167808    ), Coef('Var'  , 0.135917    ), Coef('Var'  , 0.105741    ), Coef('Var'  , 0.132707    ), Coef('Var'  , 0.160871    ), Coef('Var'  , 0.19128     ), Coef('Var'  , 0.222939    ), Coef('Var'  , 0.194491    ), ], ])
	etat2.initMat[Chem([Sub('4')])] = FMat([
		[Coef('Const', 0.36        ), Coef('Const', 0.24        ), Coef('Const', 0.16        ), Coef('Var'  , 0.17269     ), Coef('Var'  , 0.185617    ), Coef('Var'  , 0.27269     ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0142758   ), Coef('Var'  , 0.0282419   ), Coef('Var'  , 0.0142758   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0146035   ), Coef('Var'  , 0.0290605   ), Coef('Var'  , 0.0146035   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0119596   ), Coef('Var'  , 0.0233187   ), Coef('Var'  , 0.0119596   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0110315   ), Coef('Var'  , 0.0216846   ), Coef('Var'  , 0.0110315   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0116569   ), Coef('Var'  , 0.0229456   ), Coef('Var'  , 0.0116569   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0389998   ), Coef('Var'  , 0.0784689   ), Coef('Var'  , 0.0389998   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.044645    ), Coef('Var'  , 0.0897321   ), Coef('Var'  , 0.044645    ), ], 
		[Coef('Const', 0.16        ), Coef('Const', 0.24        ), Coef('Const', 0.36        ), Coef('Var'  , 0.283572    ), Coef('Var'  , 0.207227    ), Coef('Var'  , 0.183572    ), ], 
		[Coef('Const', 0.48        ), Coef('Const', 0.52        ), Coef('Const', 0.48        ), Coef('Var'  , 0.396566    ), Coef('Var'  , 0.313704    ), Coef('Var'  , 0.396566    ), ], ])
	etat2.initMat[Chem([Sub('5')])] = FMat([
		[Coef('Var'  , 0.0481016   ), Coef('Var'  , 0.0696887   ), Coef('Var'  , 0.0913268   ), Coef('Var'  , 0.0455708   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0241179   ), ], 
		[Coef('Var'  , 0.0333791   ), Coef('Var'  , 0.0347523   ), Coef('Var'  , 0.0351915   ), Coef('Var'  , 0.017818    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0169342   ), ], 
		[Coef('Var'  , 0.0426479   ), Coef('Var'  , 0.0403549   ), Coef('Var'  , 0.0376977   ), Coef('Var'  , 0.0189536   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0214012   ), ], 
		[Coef('Var'  , 0.0430915   ), Coef('Var'  , 0.0382328   ), Coef('Var'  , 0.0321892   ), Coef('Var'  , 0.0164554   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0217774   ), ], 
		[Coef('Var'  , 0.0578913   ), Coef('Var'  , 0.0459584   ), Coef('Var'  , 0.033379    ), Coef('Var'  , 0.0169068   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0290516   ), ], 
		[Coef('Var'  , 0.0765617   ), Coef('Var'  , 0.0577392   ), Coef('Var'  , 0.038341    ), Coef('Var'  , 0.0193718   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0383673   ), ], 
		[Coef('Var'  , 0.313814    ), Coef('Var'  , 0.251384    ), Coef('Var'  , 0.190685    ), Coef('Var'  , 0.219976    ), Coef('Const', 0.25        ), Coef('Const', 0.375       ), Coef('Const', 0.5625      ), Coef('Var'  , 0.437659    ), ], 
		[Coef('Var'  , 0.229318    ), Coef('Var'  , 0.231744    ), Coef('Var'  , 0.235294    ), Coef('Var'  , 0.367351    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0.375       ), Coef('Var'  , 0.301894    ), ], 
		[Coef('Var'  , 0.0943958   ), Coef('Var'  , 0.1333      ), Coef('Var'  , 0.172155    ), Coef('Var'  , 0.211045    ), Coef('Const', 0.25        ), Coef('Const', 0.125       ), Coef('Const', 0.0625      ), Coef('Var'  , 0.0785051   ), ], 
		[Coef('Var'  , 0.0607993   ), Coef('Var'  , 0.0968455   ), Coef('Var'  , 0.133741    ), Coef('Var'  , 0.0665527   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0302929   ), ], ])
	etat2.initMat[Chem([Sub('6')])] = FMat([
		[Coef('Var'  , 0.133968    ), Coef('Var'  , 0.159297    ), Coef('Var'  , 0.185617    ), Coef('Var'  , 0.138261    ), Coef('Var'  , 0.0913268   ), Coef('Var'  , 0.112178    ), ], 
		[Coef('Var'  , 0.0747293   ), Coef('Var'  , 0.0517894   ), Coef('Var'  , 0.0282419   ), Coef('Var'  , 0.0320939   ), Coef('Var'  , 0.0351915   ), Coef('Var'  , 0.0553316   ), ], 
		[Coef('Var'  , 0.0773243   ), Coef('Var'  , 0.0532548   ), Coef('Var'  , 0.0290605   ), Coef('Var'  , 0.0335572   ), Coef('Var'  , 0.0376977   ), Coef('Var'  , 0.0576048   ), ], 
		[Coef('Var'  , 0.0548295   ), Coef('Var'  , 0.0398619   ), Coef('Var'  , 0.0233187   ), Coef('Var'  , 0.028415    ), Coef('Var'  , 0.0321892   ), Coef('Var'  , 0.0443578   ), ], 
		[Coef('Var'  , 0.0494107   ), Coef('Var'  , 0.0360567   ), Coef('Var'  , 0.0216846   ), Coef('Var'  , 0.0279383   ), Coef('Var'  , 0.033379    ), Coef('Var'  , 0.041932    ), ], 
		[Coef('Var'  , 0.0495312   ), Coef('Var'  , 0.036769    ), Coef('Var'  , 0.0229456   ), Coef('Var'  , 0.0310287   ), Coef('Var'  , 0.038341    ), Coef('Var'  , 0.0444839   ), ], 
		[Coef('Var'  , 0.128221    ), Coef('Var'  , 0.102763    ), Coef('Var'  , 0.0784689   ), Coef('Var'  , 0.133975    ), Coef('Var'  , 0.190685    ), Coef('Var'  , 0.158738    ), ], 
		[Coef('Var'  , 0.12803     ), Coef('Var'  , 0.108409    ), Coef('Var'  , 0.0897321   ), Coef('Var'  , 0.161996    ), Coef('Var'  , 0.235294    ), Coef('Var'  , 0.181115    ), ], 
		[Coef('Var'  , 0.137239    ), Coef('Var'  , 0.172247    ), Coef('Var'  , 0.207227    ), Coef('Var'  , 0.189617    ), Coef('Var'  , 0.172155    ), Coef('Var'  , 0.15472     ), ], 
		[Coef('Var'  , 0.166718    ), Coef('Var'  , 0.239552    ), Coef('Var'  , 0.313704    ), Coef('Var'  , 0.223118    ), Coef('Var'  , 0.133741    ), Coef('Var'  , 0.14954     ), ], ])
	etat2.initMat[Chem([Sub('7')])] = FMat([
		[Coef('Var'  , 0.360072    ), Coef('Var'  , 0.296575    ), Coef('Var'  , 0.23915     ), Coef('Var'  , 0.173601    ), Coef('Const', 0.111111    ), Coef('Const', 0.222222    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.400752    ), ], 
		[Coef('Var'  , 0.276408    ), Coef('Var'  , 0.270713    ), Coef('Var'  , 0.267004    ), Coef('Var'  , 0.355232    ), Coef('Const', 0.444444    ), Coef('Const', 0.555556    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.359925    ), ], 
		[Coef('Var'  , 0.126663    ), Coef('Var'  , 0.16661     ), Coef('Var'  , 0.207816    ), Coef('Var'  , 0.325797    ), Coef('Const', 0.444444    ), Coef('Const', 0.222222    ), Coef('Const', 0.111111    ), Coef('Var'  , 0.118591    ), ], 
		[Coef('Var'  , 0.0213593   ), Coef('Var'  , 0.0273768   ), Coef('Var'  , 0.0311532   ), Coef('Var'  , 0.016159    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0112179   ), ], 
		[Coef('Var'  , 0.0189495   ), Coef('Var'  , 0.0237966   ), Coef('Var'  , 0.0264747   ), Coef('Var'  , 0.0137913   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0100053   ), ], 
		[Coef('Var'  , 0.0181296   ), Coef('Var'  , 0.0224072   ), Coef('Var'  , 0.0243748   ), Coef('Var'  , 0.0127895   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.00961777  ), ], 
		[Coef('Var'  , 0.0210034   ), Coef('Var'  , 0.0272049   ), Coef('Var'  , 0.0314796   ), Coef('Var'  , 0.0162064   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0109986   ), ], 
		[Coef('Var'  , 0.0161321   ), Coef('Var'  , 0.0214683   ), Coef('Var'  , 0.0255736   ), Coef('Var'  , 0.0130841   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.00838431  ), ], 
		[Coef('Var'  , 0.0355426   ), Coef('Var'  , 0.0406939   ), Coef('Var'  , 0.0449162   ), Coef('Var'  , 0.0226977   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0179963   ), ], 
		[Coef('Var'  , 0.105741    ), Coef('Var'  , 0.103154    ), Coef('Var'  , 0.102057    ), Coef('Var'  , 0.0506417   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0525127   ), ], ])
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
	etat2.initMat[Chem([Sub('8')])] = FMat([
		[Coef('Var'  , 0.462946    ), Coef('Var'  , 0.452682    ), Coef('Const', 0.444444    ), Coef('Const', 0.666667    ), Coef('Const', 1           ), Coef('Const', 0.8         ), Coef('Const', 0.64        ), Coef('Var'  , 0.55046     ), ], 
		[Coef('Var'  , 0.210556    ), Coef('Var'  , 0.32717     ), Coef('Const', 0.444444    ), Coef('Const', 0.333333    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.104948    ), ], 
		[Coef('Var'  , 0.0753078   ), Coef('Var'  , 0.0930265   ), Coef('Const', 0.111111    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.037471    ), ], 
		[Coef('Var'  , 0.0125627   ), Coef('Var'  , 0.00663336  ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.00663331  ), ], 
		[Coef('Var'  , 0.0113759   ), Coef('Var'  , 0.00604274  ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.00604269  ), ], 
		[Coef('Var'  , 0.0109874   ), Coef('Var'  , 0.00585236  ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.00585231  ), ], 
		[Coef('Var'  , 0.0122887   ), Coef('Var'  , 0.00648088  ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.00648083  ), ], 
		[Coef('Var'  , 0.00920184  ), Coef('Var'  , 0.00481739  ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.00481734  ), ], 
		[Coef('Var'  , 0.0339018   ), Coef('Var'  , 0.0171002   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.04        ), Coef('Var'  , 0.0371002   ), ], 
		[Coef('Var'  , 0.160871    ), Coef('Var'  , 0.080194    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.2         ), Coef('Const', 0.32        ), Coef('Var'  , 0.240194    ), ], ])
	etat2.initMat[Chem([Sub('9')])] = FMat([
		[Coef('Var'  , 0.325919    ), Coef('Var'  , 0.318693    ), Coef('Var'  , 0.318539    ), Coef('Var'  , 0.252742    ), Coef('Var'  , 0.192378    ), Coef('Var'  , 0.213052    ), Coef('Var'  , 0.23915     ), Coef('Var'  , 0.279002    ), ], 
		[Coef('Var'  , 0.194232    ), Coef('Var'  , 0.155484    ), Coef('Var'  , 0.118976    ), Coef('Var'  , 0.140393    ), Coef('Var'  , 0.163334    ), Coef('Var'  , 0.214384    ), Coef('Var'  , 0.267004    ), Coef('Var'  , 0.229475    ), ], 
		[Coef('Var'  , 0.118806    ), Coef('Var'  , 0.0996471   ), Coef('Var'  , 0.0819378   ), Coef('Var'  , 0.114574    ), Coef('Var'  , 0.148491    ), Coef('Var'  , 0.177504    ), Coef('Var'  , 0.207816    ), Coef('Var'  , 0.162577    ), ], 
		[Coef('Var'  , 0.0301398   ), Coef('Var'  , 0.0319392   ), Coef('Var'  , 0.0311371   ), Coef('Var'  , 0.0469617   ), Coef('Var'  , 0.0605144   ), Coef('Var'  , 0.0469728   ), Coef('Var'  , 0.0311532   ), Coef('Var'  , 0.0319502   ), ], 
		[Coef('Var'  , 0.026558    ), Coef('Var'  , 0.0278074   ), Coef('Var'  , 0.0265097   ), Coef('Var'  , 0.0385061   ), Coef('Var'  , 0.0484327   ), Coef('Var'  , 0.038482    ), Coef('Var'  , 0.0264747   ), Coef('Var'  , 0.0277833   ), ], 
		[Coef('Var'  , 0.0252494   ), Coef('Var'  , 0.0261419   ), Coef('Var'  , 0.0243526   ), Coef('Var'  , 0.0339095   ), Coef('Var'  , 0.041144    ), Coef('Var'  , 0.0339248   ), Coef('Var'  , 0.0243748   ), Coef('Var'  , 0.0261573   ), ], 
		[Coef('Var'  , 0.0297301   ), Coef('Var'  , 0.0317392   ), Coef('Var'  , 0.0314916   ), Coef('Var'  , 0.0490995   ), Coef('Var'  , 0.0654041   ), Coef('Var'  , 0.0490913   ), Coef('Var'  , 0.0314796   ), Coef('Var'  , 0.031731    ), ], 
		[Coef('Var'  , 0.0230394   ), Coef('Var'  , 0.0250036   ), Coef('Var'  , 0.0255506   ), Coef('Var'  , 0.041627    ), Coef('Var'  , 0.0568421   ), Coef('Var'  , 0.0416428   ), Coef('Var'  , 0.0255736   ), Coef('Var'  , 0.0250194   ), ], 
		[Coef('Var'  , 0.0585185   ), Coef('Var'  , 0.0749257   ), Coef('Var'  , 0.0902512   ), Coef('Var'  , 0.0857925   ), Coef('Var'  , 0.0803851   ), Coef('Var'  , 0.0631247   ), Coef('Var'  , 0.0449162   ), Coef('Var'  , 0.0522579   ), ], 
		[Coef('Var'  , 0.167808    ), Coef('Var'  , 0.208619    ), Coef('Var'  , 0.251255    ), Coef('Var'  , 0.196395    ), Coef('Var'  , 0.143075    ), Coef('Var'  , 0.121822    ), Coef('Var'  , 0.102057    ), Coef('Var'  , 0.134046    ), ], ])
	etat2.initMat[Chem([Sub('10')])] = FMat([
		[Coef('Var'  , 0.428793    ), Coef('Var'  , 0.532887    ), Coef('Const', 0.64        ), Coef('Const', 0.48        ), Coef('Const', 0.36        ), Coef('Var'  , 0.337736    ), Coef('Var'  , 0.318539    ), Coef('Var'  , 0.370623    ), ], 
		[Coef('Var'  , 0.12838     ), Coef('Var'  , 0.0637109   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0590186   ), Coef('Var'  , 0.118976    ), Coef('Var'  , 0.122729    ), ], 
		[Coef('Var'  , 0.0674511   ), Coef('Var'  , 0.0334383   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0406444   ), Coef('Var'  , 0.0819378   ), Coef('Var'  , 0.0740828   ), ], 
		[Coef('Var'  , 0.0213432   ), Coef('Var'  , 0.0112067   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0161479   ), Coef('Var'  , 0.0311371   ), Coef('Var'  , 0.0273546   ), ], 
		[Coef('Var'  , 0.0189845   ), Coef('Var'  , 0.0100294   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0138154   ), Coef('Var'  , 0.0265097   ), Coef('Var'  , 0.0238448   ), ], 
		[Coef('Var'  , 0.0181073   ), Coef('Var'  , 0.00960236  ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0127742   ), Coef('Var'  , 0.0243526   ), Coef('Var'  , 0.0223765   ), ], 
		[Coef('Var'  , 0.0210154   ), Coef('Var'  , 0.0110069   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0162146   ), Coef('Var'  , 0.0314916   ), Coef('Var'  , 0.0272214   ), ], 
		[Coef('Var'  , 0.0161091   ), Coef('Var'  , 0.00836843  ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0130682   ), Coef('Var'  , 0.0255506   ), Coef('Var'  , 0.0214366   ), ], 
		[Coef('Var'  , 0.0568777   ), Coef('Var'  , 0.0486641   ), Coef('Const', 0.04        ), Coef('Const', 0.08        ), Coef('Const', 0.16        ), Coef('Var'  , 0.125366    ), Coef('Var'  , 0.0902512   ), Coef('Var'  , 0.0740296   ), ], 
		[Coef('Var'  , 0.222939    ), Coef('Var'  , 0.271086    ), Coef('Const', 0.32        ), Coef('Const', 0.44        ), Coef('Const', 0.48        ), Coef('Var'  , 0.365215    ), Coef('Var'  , 0.251255    ), Coef('Var'  , 0.236301    ), ], ])
	etat2.initMat[Chem([Sub('11')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.111111    ), Coef('Var'  , 0.107059    ), Coef('Var'  , 0.10366     ), Coef('Var'  , 0.0761318   ), Coef('Var'  , 0.0492925   ), Coef('Var'  , 0.0246282   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.333333    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.321587    ), Coef('Var'  , 0.198861    ), Coef('Var'  , 0.141892    ), Coef('Var'  , 0.0850027   ), Coef('Var'  , 0.0425273   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 1           ), Coef('Const', 0.666667    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.338758    ), Coef('Var'  , 0.233658    ), Coef('Var'  , 0.212547    ), Coef('Var'  , 0.192518    ), Coef('Var'  , 0.221011    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0565191   ), Coef('Var'  , 0.112777    ), Coef('Var'  , 0.178203    ), Coef('Var'  , 0.243409    ), Coef('Var'  , 0.371684    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0405707   ), Coef('Var'  , 0.0809913   ), Coef('Var'  , 0.120497    ), Coef('Var'  , 0.159977    ), Coef('Var'  , 0.204926    ), Coef('Const', 0.25        ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0272786   ), Coef('Var'  , 0.0541496   ), Coef('Var'  , 0.0678552   ), Coef('Var'  , 0.0810417   ), Coef('Var'  , 0.0405766   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0332678   ), Coef('Var'  , 0.0668585   ), Coef('Var'  , 0.0724005   ), Coef('Var'  , 0.0788305   ), Coef('Var'  , 0.0391327   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0227137   ), Coef('Var'  , 0.0452813   ), Coef('Var'  , 0.0433398   ), Coef('Var'  , 0.0411659   ), Coef('Var'  , 0.0206261   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0222013   ), Coef('Var'  , 0.0438649   ), Coef('Var'  , 0.0386645   ), Coef('Var'  , 0.0323993   ), Coef('Var'  , 0.0164632   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0300446   ), Coef('Var'  , 0.0598996   ), Coef('Var'  , 0.0484688   ), Coef('Var'  , 0.0363638   ), Coef('Var'  , 0.0184242   ), Coef('Const', 0           ), Coef('Const', 0           ), ], ])
	etat2.initMat[Chem([Sub('12')])] = FMat([
		[Coef('Const', 0           ), Coef('Var'  , 0.0250018   ), Coef('Var'  , 0.0500022   ), Coef('Var'  , 0.0250018   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 2.66847e-06 ), Coef('Var'  , 3.29841e-06 ), Coef('Var'  , 2.66847e-06 ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 3.63498e-06 ), Coef('Var'  , 4.49308e-06 ), Coef('Var'  , 3.63498e-06 ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 2.34923e-06 ), Coef('Var'  , 2.90381e-06 ), Coef('Var'  , 2.34923e-06 ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 4.01981e-06 ), Coef('Var'  , 4.96876e-06 ), Coef('Var'  , 4.01981e-06 ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 2.12294e-06 ), Coef('Var'  , 2.6241e-06  ), Coef('Var'  , 2.12294e-06 ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.25        ), Coef('Var'  , 0.164063    ), Coef('Var'  , 0.0781255   ), Coef('Var'  , 0.0703129   ), Coef('Const', 0.0625      ), Coef('Const', 0.125       ), ], 
		[Coef('Const', 0.5         ), Coef('Var'  , 0.359372    ), Coef('Var'  , 0.218746    ), Coef('Var'  , 0.296872    ), Coef('Const', 0.375       ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0.25        ), Coef('Var'  , 0.351552    ), Coef('Var'  , 0.453112    ), Coef('Var'  , 0.507802    ), Coef('Const', 0.5625      ), Coef('Const', 0.375       ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0999962   ), Coef('Var'  , 0.199995    ), Coef('Var'  , 0.0999962   ), Coef('Const', 0           ), Coef('Const', 0           ), ], ])
	etat2.initMat[Chem([Sub('13')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.02        ), Coef('Const', 0.04        ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  ,-1.95936e-18 ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  ,-1.99251e-18 ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  ,-2.02115e-18 ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  ,-2.01589e-18 ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  ,-1.99099e-18 ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.0625      ), Coef('Var'  , 0.03125     ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Const', 0.375       ), Coef('Var'  , 0.1875      ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 1           ), Coef('Const', 0.75        ), Coef('Const', 0.5625      ), Coef('Var'  , 0.60125     ), Coef('Const', 0.64        ), Coef('Const', 0.8         ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.16        ), Coef('Const', 0.32        ), Coef('Const', 0.2         ), ], ])
	etat2.initMat[Chem([Sub('14')])] = FMat([
		[Coef('Const', 0.16        ), Coef('Const', 0.08        ), Coef('Const', 0.04        ), Coef('Var'  , 0.0450018   ), Coef('Var'  , 0.0500022   ), Coef('Var'  , 0.105002    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 2.66847e-06 ), Coef('Var'  , 3.29841e-06 ), Coef('Var'  , 2.66847e-06 ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 3.63498e-06 ), Coef('Var'  , 4.49308e-06 ), Coef('Var'  , 3.63498e-06 ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 2.34923e-06 ), Coef('Var'  , 2.90381e-06 ), Coef('Var'  , 2.34923e-06 ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 4.01981e-06 ), Coef('Var'  , 4.96876e-06 ), Coef('Var'  , 4.01981e-06 ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 2.12294e-06 ), Coef('Var'  , 2.6241e-06  ), Coef('Var'  , 2.12294e-06 ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0390629   ), Coef('Var'  , 0.0781255   ), Coef('Var'  , 0.0390629   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.109372    ), Coef('Var'  , 0.218746    ), Coef('Var'  , 0.109372    ), ], 
		[Coef('Const', 0.36        ), Coef('Const', 0.48        ), Coef('Const', 0.64        ), Coef('Var'  , 0.546552    ), Coef('Var'  , 0.453112    ), Coef('Var'  , 0.406552    ), ], 
		[Coef('Const', 0.48        ), Coef('Const', 0.44        ), Coef('Const', 0.32        ), Coef('Var'  , 0.259996    ), Coef('Var'  , 0.199995    ), Coef('Var'  , 0.339996    ), ], ])
	etat2.initMat[Chem([Sub('15')])] = FMat([
		[Coef('Var'  , 0.0250001   ), Coef('Var'  , 0.0372096   ), Coef('Var'  , 0.0492925   ), Coef('Var'  , 0.0593241   ), Coef('Var'  , 0.0693385   ), Coef('Var'  , 0.0594834   ), Coef('Var'  , 0.0492707   ), Coef('Var'  , 0.0373689   ), ], 
		[Coef('Var'  , 0.0365429   ), Coef('Var'  , 0.0608714   ), Coef('Var'  , 0.0850027   ), Coef('Var'  , 0.0946033   ), Coef('Var'  , 0.103892    ), Coef('Var'  , 0.0820713   ), Coef('Var'  , 0.0595676   ), Coef('Var'  , 0.0483394   ), ], 
		[Coef('Var'  , 0.136245    ), Coef('Var'  , 0.164005    ), Coef('Var'  , 0.192518    ), Coef('Var'  , 0.173382    ), Coef('Var'  , 0.155226    ), Coef('Var'  , 0.129823    ), Coef('Var'  , 0.105135    ), Coef('Var'  , 0.120446    ), ], 
		[Coef('Var'  , 0.216867    ), Coef('Var'  , 0.230082    ), Coef('Var'  , 0.243409    ), Coef('Var'  , 0.193666    ), Coef('Var'  , 0.143849    ), Coef('Var'  , 0.134252    ), Coef('Var'  , 0.124423    ), Coef('Var'  , 0.170668    ), ], 
		[Coef('Var'  , 0.196269    ), Coef('Var'  , 0.177992    ), Coef('Var'  , 0.159977    ), Coef('Var'  , 0.136664    ), Coef('Var'  , 0.113553    ), Coef('Var'  , 0.119839    ), Coef('Var'  , 0.12629     ), Coef('Var'  , 0.161167    ), ], 
		[Coef('Var'  , 0.178712    ), Coef('Var'  , 0.129921    ), Coef('Var'  , 0.0810417   ), Coef('Var'  , 0.0855726   ), Coef('Var'  , 0.08983     ), Coef('Var'  , 0.111893    ), Coef('Var'  , 0.133773    ), Coef('Var'  , 0.156242    ), ], 
		[Coef('Var'  , 0.127792    ), Coef('Var'  , 0.102746    ), Coef('Var'  , 0.0788305   ), Coef('Var'  , 0.102125    ), Coef('Var'  , 0.127063    ), Coef('Var'  , 0.156628    ), Coef('Var'  , 0.188516    ), Coef('Var'  , 0.15725     ), ], 
		[Coef('Var'  , 0.0369667   ), Coef('Var'  , 0.0391038   ), Coef('Var'  , 0.0411659   ), Coef('Var'  , 0.0614787   ), Coef('Var'  , 0.0818168   ), Coef('Var'  , 0.0942305   ), Coef('Var'  , 0.107027    ), Coef('Var'  , 0.0718556   ), ], 
		[Coef('Var'  , 0.0232578   ), Coef('Var'  , 0.028273    ), Coef('Var'  , 0.0323993   ), Coef('Var'  , 0.0452382   ), Coef('Var'  , 0.0568951   ), Coef('Var'  , 0.0574481   ), Coef('Var'  , 0.0568183   ), Coef('Var'  , 0.0404829   ), ], 
		[Coef('Var'  , 0.0223484   ), Coef('Var'  , 0.0297955   ), Coef('Var'  , 0.0363638   ), Coef('Var'  , 0.0479459   ), Coef('Var'  , 0.0585367   ), Coef('Var'  , 0.0543317   ), Coef('Var'  , 0.0491808   ), Coef('Var'  , 0.0361812   ), ], ])
	etat2.initMat[Chem([Sub('16')])] = FMat([
		[Coef('Var'  , 0.0248511   ), Coef('Var'  , 0.037322    ), Coef('Var'  , 0.0492707   ), Coef('Var'  , 0.0624234   ), Coef('Var'  , 0.0751999   ), Coef('Var'  , 0.0617538   ), Coef('Var'  , 0.0481016   ), Coef('Var'  , 0.0366524   ), ], 
		[Coef('Var'  , 0.0240908   ), Coef('Var'  , 0.0422061   ), Coef('Var'  , 0.0595676   ), Coef('Var'  , 0.0648818   ), Coef('Var'  , 0.0692507   ), Coef('Var'  , 0.0518207   ), Coef('Var'  , 0.0333791   ), Coef('Var'  , 0.029145    ), ], 
		[Coef('Var'  , 0.0369787   ), Coef('Var'  , 0.0709593   ), Coef('Var'  , 0.105135    ), Coef('Var'  , 0.099754    ), Coef('Var'  , 0.0947103   ), Coef('Var'  , 0.0687031   ), Coef('Var'  , 0.0426479   ), Coef('Var'  , 0.0399085   ), ], 
		[Coef('Var'  , 0.0423505   ), Coef('Var'  , 0.0835286   ), Coef('Var'  , 0.124423    ), Coef('Var'  , 0.108969    ), Coef('Var'  , 0.0929127   ), Coef('Var'  , 0.0684763   ), Coef('Var'  , 0.0430915   ), Coef('Var'  , 0.0430363   ), ], 
		[Coef('Var'  , 0.108626    ), Coef('Var'  , 0.117426    ), Coef('Var'  , 0.12629     ), Coef('Var'  , 0.106842    ), Coef('Var'  , 0.0873071   ), Coef('Var'  , 0.0727927   ), Coef('Var'  , 0.0578913   ), Coef('Var'  , 0.0833761   ), ], 
		[Coef('Var'  , 0.177657    ), Coef('Var'  , 0.155728    ), Coef('Var'  , 0.133773    ), Coef('Var'  , 0.111129    ), Coef('Var'  , 0.088206    ), Coef('Var'  , 0.0825998   ), Coef('Var'  , 0.0765617   ), Coef('Var'  , 0.127198    ), ], 
		[Coef('Var'  , 0.326653    ), Coef('Var'  , 0.25657     ), Coef('Var'  , 0.188516    ), Coef('Var'  , 0.185894    ), Coef('Var'  , 0.185849    ), Coef('Var'  , 0.248667    ), Coef('Var'  , 0.313814    ), Coef('Var'  , 0.319342    ), ], 
		[Coef('Var'  , 0.177087    ), Coef('Var'  , 0.141776    ), Coef('Var'  , 0.107027    ), Coef('Var'  , 0.120757    ), Coef('Var'  , 0.135253    ), Coef('Var'  , 0.181773    ), Coef('Var'  , 0.229318    ), Coef('Var'  , 0.202792    ), ], 
		[Coef('Var'  , 0.0539718   ), Coef('Var'  , 0.0557579   ), Coef('Var'  , 0.0568183   ), Coef('Var'  , 0.0726139   ), Coef('Var'  , 0.0874783   ), Coef('Var'  , 0.0911958   ), Coef('Var'  , 0.0943958   ), Coef('Var'  , 0.0743399   ), ], 
		[Coef('Var'  , 0.0277341   ), Coef('Var'  , 0.0387265   ), Coef('Var'  , 0.0491808   ), Coef('Var'  , 0.066735    ), Coef('Var'  , 0.083833    ), Coef('Var'  , 0.0722179   ), Coef('Var'  , 0.0607993   ), Coef('Var'  , 0.0442093   ), ], ])
	
	
	
	etat3.bords   = {Bord('0'): etat19, Bord('1'): etat20, Bord('2'): etat21, Bord('3'): etat20, Bord('4'): etat19, }
	etat3.permuts = {}
	etat3.interns = {Intern('_'): etat3, }
	etat3.subs    = {Sub('0'): etat1, Sub('1'): etat2, Sub('2'): etat4, Sub('3'): etat5, Sub('4'): etat6, Sub('5'): etat7, Sub('6'): etat8, Sub('7'): etat9, Sub('G', True): Etat.etatPoint, Sub('8'): etat10, Sub('9'): etat11, Sub('10'): etat12, Sub('11'): etat13, Sub('12'): etat14, Sub('13'): etat15, Sub('14'): etat16, Sub('15'): etat17, Sub('16'): etat18, }
	
	etat3.buildIntern()
	
	
	etat3.eqs = [
		(Chem([Bord('2'), Sub('2'), Permut('0'), ])	,	Chem([Sub('4'), Bord('2'), ])),
		(Chem([Bord('3'), Sub('1'), Permut('0'), ])	,	Chem([Sub('5'), Bord('0'), ])),
		(Chem([Bord('2'), Sub('3'), Permut('0'), ])	,	Chem([Sub('6'), Bord('0'), ])),
		(Chem([Bord('3'), Sub('0'), Permut('0'), ])	,	Chem([Sub('6'), Bord('2'), ])),
		(Chem([Bord('1'), Sub('1'), Permut('0'), ])	,	Chem([Sub('7'), Bord('1'), ])),
		(Chem([Bord('2'), Sub('0'), Permut('0'), ])	,	Chem([Sub('9'), Bord('1'), ])),
		(Chem([Bord('1'), Sub('2'), Permut('0'), ])	,	Chem([Sub('9'), Bord('2'), ])),
		(Chem([Bord('2'), Sub('1'), Permut('0'), ])	,	Chem([Sub('10'), Bord('2'), ])),
		(Chem([Bord('1'), Sub('0'), Permut('0'), ])	,	Chem([Sub('11'), Bord('1'), ])),
		(Chem([Bord('0'), Sub('1'), Permut('0'), ])	,	Chem([Sub('11'), Bord('2'), ])),
		(Chem([Bord('0'), Sub('0'), Permut('0'), ])	,	Chem([Sub('15'), Bord('1'), ])),
		(Chem([Bord('4'), Sub('1'), Permut('0'), ])	,	Chem([Sub('15'), Bord('2'), ])),
		(Chem([Bord('4'), Sub('0'), Permut('0'), ])	,	Chem([Sub('16'), Bord('1'), ])),
		(Chem([Bord('3'), Sub('2'), Permut('0'), ])	,	Chem([Sub('16'), Bord('2'), ])),
		(Chem([Sub('0'), Bord('0'), Bord('1'), ])	,	Chem([Sub('11'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('1'), Bord('1'), ])	,	Chem([Sub('15'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('2'), Bord('1'), ])	,	Chem([Sub('2'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('3'), Bord('1'), ])	,	Chem([Sub('1'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('0'), Bord('1'), ])	,	Chem([Sub('11'), Bord('4'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('2'), Bord('1'), ])	,	Chem([Sub('2'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('3'), Bord('1'), ])	,	Chem([Sub('13'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('4'), Bord('1'), ])	,	Chem([Sub('8'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('1'), Bord('1'), ])	,	Chem([Sub('16'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('2'), Bord('1'), ])	,	Chem([Sub('5'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('3'), Bord('0'), Bord('1'), ])	,	Chem([Sub('7'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('3'), Bord('1'), Bord('1'), ])	,	Chem([Sub('8'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('3'), Bord('2'), Bord('1'), ])	,	Chem([Sub('10'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('3'), Bord('3'), Bord('1'), ])	,	Chem([Sub('9'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('4'), Bord('0'), Bord('1'), ])	,	Chem([Sub('14'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('4'), Bord('1'), Bord('1'), ])	,	Chem([Sub('6'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('4'), Bord('2'), Bord('1'), ])	,	Chem([Sub('10'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('5'), Bord('0'), Bord('1'), ])	,	Chem([Sub('6'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('5'), Bord('1'), Bord('1'), ])	,	Chem([Sub('12'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('5'), Bord('3'), Bord('1'), ])	,	Chem([Sub('16'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('7'), Bord('0'), Bord('1'), ])	,	Chem([Sub('9'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('7'), Bord('1'), Bord('1'), ])	,	Chem([Sub('11'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('7'), Bord('2'), Bord('1'), ])	,	Chem([Sub('8'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('8'), Bord('2'), Bord('1'), ])	,	Chem([Sub('10'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('9'), Bord('0'), Bord('1'), ])	,	Chem([Sub('10'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('11'), Bord('2'), Bord('1'), ])	,	Chem([Sub('15'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('12'), Bord('0'), Bord('1'), ])	,	Chem([Sub('14'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('12'), Bord('1'), Bord('1'), ])	,	Chem([Sub('13'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('13'), Bord('1'), Bord('1'), ])	,	Chem([Sub('14'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('15'), Bord('2'), Bord('1'), ])	,	Chem([Sub('16'), Bord('0'), Bord('1'), ])),
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
		[Coef('Var'  , 0.11776     ), Coef('Var'  , 0.139587    ), Coef('Var'  , 0.161841    ), Coef('Var'  , 0.179471    ), Coef('Var'  , 0.197535    ), Coef('Var'  , 0.163704    ), Coef('Var'  , 0.130301    ), Coef('Var'  , 0.12382     ), ], 
		[Coef('Var'  , 0.140104    ), Coef('Var'  , 0.189655    ), Coef('Var'  , 0.240107    ), Coef('Var'  , 0.226892    ), Coef('Var'  , 0.214465    ), Coef('Var'  , 0.167472    ), Coef('Var'  , 0.121255    ), Coef('Var'  , 0.130235    ), ], 
		[Coef('Var'  , 0.161716    ), Coef('Var'  , 0.178408    ), Coef('Var'  , 0.196081    ), Coef('Var'  , 0.166929    ), Coef('Var'  , 0.138537    ), Coef('Var'  , 0.124429    ), Coef('Var'  , 0.110843    ), Coef('Var'  , 0.135908    ), ], 
		[Coef('Var'  , 0.104843    ), Coef('Var'  , 0.0948399   ), Coef('Var'  , 0.0848847   ), Coef('Var'  , 0.0607082   ), Coef('Var'  , 0.0365612   ), Coef('Var'  , 0.0488062   ), Coef('Var'  , 0.0607399   ), Coef('Var'  , 0.0829378   ), ], 
		[Coef('Var'  , 0.0625875   ), Coef('Var'  , 0.054375    ), Coef('Var'  , 0.0455819   ), Coef('Var'  , 0.0345877   ), Coef('Var'  , 0.0230895   ), Coef('Var'  , 0.033832    ), Coef('Var'  , 0.0436861   ), Coef('Var'  , 0.0536193   ), ], 
		[Coef('Var'  , 0.0583379   ), Coef('Var'  , 0.04902     ), Coef('Var'  , 0.0377434   ), Coef('Var'  , 0.0312806   ), Coef('Var'  , 0.0233175   ), Coef('Var'  , 0.036757    ), Coef('Var'  , 0.0483854   ), Coef('Var'  , 0.0544964   ), ], 
		[Coef('Var'  , 0.0678586   ), Coef('Var'  , 0.0536831   ), Coef('Var'  , 0.0384248   ), Coef('Var'  , 0.033776    ), Coef('Var'  , 0.0282022   ), Coef('Var'  , 0.0498372   ), Coef('Var'  , 0.0707841   ), Coef('Var'  , 0.0697444   ), ], 
		[Coef('Var'  , 0.0838048   ), Coef('Var'  , 0.0625539   ), Coef('Var'  , 0.0416599   ), Coef('Var'  , 0.0400169   ), Coef('Var'  , 0.0385497   ), Coef('Var'  , 0.0760538   ), Coef('Var'  , 0.114218    ), Coef('Var'  , 0.0985908   ), ], 
		[Coef('Var'  , 0.109926    ), Coef('Var'  , 0.0901788   ), Coef('Var'  , 0.0713455   ), Coef('Var'  , 0.0953931   ), Coef('Var'  , 0.120086    ), Coef('Var'  , 0.140863    ), Coef('Var'  , 0.162778    ), Coef('Var'  , 0.135648    ), ], 
		[Coef('Var'  , 0.0930626   ), Coef('Var'  , 0.0876995   ), Coef('Var'  , 0.0823308   ), Coef('Var'  , 0.130945    ), Coef('Var'  , 0.179656    ), Coef('Var'  , 0.158246    ), Coef('Var'  , 0.137009    ), Coef('Var'  , 0.115001    ), ], ])
	etat3.initMat[Chem([Sub('1')])] = FMat([
		[Coef('Var'  , 0.0553407   ), Coef('Var'  , 0.0701786   ), Coef('Var'  , 0.0840117   ), Coef('Var'  , 0.100813    ), Coef('Var'  , 0.11776     ), Coef('Var'  , 0.107127    ), Coef('Var'  , 0.0965225   ), Coef('Var'  , 0.0844071   ), Coef('Var'  , 0.0709676   ), Coef('Var'  , 0.0641983   ), ], 
		[Coef('Var'  , 0.0611342   ), Coef('Var'  , 0.0858771   ), Coef('Var'  , 0.110029    ), Coef('Var'  , 0.124755    ), Coef('Var'  , 0.140104    ), Coef('Var'  , 0.116562    ), Coef('Var'  , 0.0935095   ), Coef('Var'  , 0.0815193   ), Coef('Var'  , 0.0685769   ), Coef('Var'  , 0.065714    ), ], 
		[Coef('Var'  , 0.159477    ), Coef('Var'  , 0.198789    ), Coef('Var'  , 0.239064    ), Coef('Var'  , 0.199876    ), Coef('Var'  , 0.161716    ), Coef('Var'  , 0.13354     ), Coef('Var'  , 0.105889    ), Coef('Var'  , 0.104425    ), Coef('Var'  , 0.102586    ), Coef('Var'  , 0.131024    ), ], 
		[Coef('Var'  , 0.165743    ), Coef('Var'  , 0.18176     ), Coef('Var'  , 0.199067    ), Coef('Var'  , 0.151801    ), Coef('Var'  , 0.104843    ), Coef('Var'  , 0.0897101   ), Coef('Var'  , 0.0741954   ), Coef('Var'  , 0.0833305   ), Coef('Var'  , 0.0918282   ), Coef('Var'  , 0.128465    ), ], 
		[Coef('Var'  , 0.164707    ), Coef('Var'  , 0.128641    ), Coef('Var'  , 0.0949208   ), Coef('Var'  , 0.0787647   ), Coef('Var'  , 0.0625875   ), Coef('Var'  , 0.0629438   ), Coef('Var'  , 0.062501    ), Coef('Var'  , 0.0832775   ), Coef('Var'  , 0.104052    ), Coef('Var'  , 0.133184    ), ], 
		[Coef('Var'  , 0.141543    ), Coef('Var'  , 0.101155    ), Coef('Var'  , 0.0607552   ), Coef('Var'  , 0.0603777   ), Coef('Var'  , 0.0583379   ), Coef('Var'  , 0.0674089   ), Coef('Var'  , 0.074606    ), Coef('Var'  , 0.105162    ), Coef('Var'  , 0.135696    ), Coef('Var'  , 0.138011    ), ], 
		[Coef('Var'  , 0.0973614   ), Coef('Var'  , 0.0749606   ), Coef('Var'  , 0.0520785   ), Coef('Var'  , 0.0604726   ), Coef('Var'  , 0.0678586   ), Coef('Var'  , 0.0866713   ), Coef('Var'  , 0.105289    ), Coef('Var'  , 0.127718    ), Coef('Var'  , 0.152285    ), Coef('Var'  , 0.123915    ), ], 
		[Coef('Var'  , 0.0534126   ), Coef('Var'  , 0.0495062   ), Coef('Var'  , 0.0449746   ), Coef('Var'  , 0.0642916   ), Coef('Var'  , 0.0838048   ), Coef('Var'  , 0.110412    ), Coef('Var'  , 0.138109    ), Coef('Var'  , 0.122443    ), Coef('Var'  , 0.10839     ), Coef('Var'  , 0.0807284   ), ], 
		[Coef('Var'  , 0.054395    ), Coef('Var'  , 0.0568182   ), Coef('Var'  , 0.0587097   ), Coef('Var'  , 0.083979    ), Coef('Var'  , 0.109926    ), Coef('Var'  , 0.131036    ), Coef('Var'  , 0.153523    ), Coef('Var'  , 0.12525     ), Coef('Var'  , 0.0978745   ), Coef('Var'  , 0.0763608   ), ], 
		[Coef('Var'  , 0.0468873   ), Coef('Var'  , 0.0523144   ), Coef('Var'  , 0.056389    ), Coef('Var'  , 0.0748696   ), Coef('Var'  , 0.0930626   ), Coef('Var'  , 0.094589    ), Coef('Var'  , 0.0958559   ), Coef('Var'  , 0.0824676   ), Coef('Var'  , 0.0677438   ), Coef('Var'  , 0.0583991   ), ], ])
	etat3.initMat[Chem([Sub('2')])] = FMat([
		[Coef('Var'  , 0.0965225   ), Coef('Var'  , 0.113394    ), Coef('Var'  , 0.130301    ), Coef('Var'  , 0.120613    ), Coef('Var'  , 0.111174    ), Coef('Var'  , 0.0879756   ), Coef('Var'  , 0.0645405   ), Coef('Var'  , 0.0807561   ), ], 
		[Coef('Var'  , 0.0935095   ), Coef('Var'  , 0.107162    ), Coef('Var'  , 0.121255    ), Coef('Var'  , 0.0808656   ), Coef('Var'  , 0.0410119   ), Coef('Var'  , 0.0424798   ), Coef('Var'  , 0.0438869   ), Coef('Var'  , 0.0687764   ), ], 
		[Coef('Var'  , 0.105889    ), Coef('Var'  , 0.108221    ), Coef('Var'  , 0.110843    ), Coef('Var'  , 0.0752819   ), Coef('Var'  , 0.0399461   ), Coef('Var'  , 0.0444899   ), Coef('Var'  , 0.0487443   ), Coef('Var'  , 0.0774292   ), ], 
		[Coef('Var'  , 0.0741954   ), Coef('Var'  , 0.0677621   ), Coef('Var'  , 0.0607399   ), Coef('Var'  , 0.0430064   ), Coef('Var'  , 0.0247701   ), Coef('Var'  , 0.0306006   ), Coef('Var'  , 0.0357346   ), Coef('Var'  , 0.0553562   ), ], 
		[Coef('Var'  , 0.062501    ), Coef('Var'  , 0.0535891   ), Coef('Var'  , 0.0436861   ), Coef('Var'  , 0.032693    ), Coef('Var'  , 0.0207618   ), Coef('Var'  , 0.0285952   ), Coef('Var'  , 0.0356859   ), Coef('Var'  , 0.0494912   ), ], 
		[Coef('Var'  , 0.074606    ), Coef('Var'  , 0.0624253   ), Coef('Var'  , 0.0483854   ), Coef('Var'  , 0.0378504   ), Coef('Var'  , 0.0256429   ), Coef('Var'  , 0.0375748   ), Coef('Var'  , 0.0486674   ), Coef('Var'  , 0.0621497   ), ], 
		[Coef('Var'  , 0.105289    ), Coef('Var'  , 0.0880353   ), Coef('Var'  , 0.0707841   ), Coef('Var'  , 0.0750053   ), Coef('Var'  , 0.0789413   ), Coef('Var'  , 0.106413    ), Coef('Var'  , 0.134595    ), Coef('Var'  , 0.119443    ), ], 
		[Coef('Var'  , 0.138109    ), Coef('Var'  , 0.12552     ), Coef('Var'  , 0.114218    ), Coef('Var'  , 0.157679    ), Coef('Var'  , 0.202102    ), Coef('Var'  , 0.227652    ), Coef('Var'  , 0.254417    ), Coef('Var'  , 0.195493    ), ], 
		[Coef('Var'  , 0.153523    ), Coef('Var'  , 0.157377    ), Coef('Var'  , 0.162778    ), Coef('Var'  , 0.218645    ), Coef('Var'  , 0.275825    ), Coef('Var'  , 0.263057    ), Coef('Var'  , 0.251417    ), Coef('Var'  , 0.20179     ), ], 
		[Coef('Var'  , 0.0958559   ), Coef('Var'  , 0.116514    ), Coef('Var'  , 0.137009    ), Coef('Var'  , 0.15836     ), Coef('Var'  , 0.179825    ), Coef('Var'  , 0.131162    ), Coef('Var'  , 0.0823114   ), Coef('Var'  , 0.0893156   ), ], ])
	etat3.initMat[Chem([Sub('3')])] = FMat([
		[Coef('Var'  , 0.0110912   ), Coef('Var'  , 0.0157863   ), Coef('Var'  , 0.018943    ), Coef('Var'  , 0.0239346   ), Coef('Var'  , 0.0267596   ), Coef('Var'  , 0.0239103   ), Coef('Var'  , 0.0189078   ), Coef('Var'  , 0.015762    ), ], 
		[Coef('Var'  , 0.0107089   ), Coef('Var'  , 0.0153341   ), Coef('Var'  , 0.0186493   ), Coef('Var'  , 0.0235333   ), Coef('Var'  , 0.0265711   ), Coef('Var'  , 0.0235204   ), Coef('Var'  , 0.0186307   ), Coef('Var'  , 0.0153212   ), ], 
		[Coef('Var'  , 0.0773794   ), Coef('Var'  , 0.10345     ), Coef('Var'  , 0.130214    ), Coef('Var'  , 0.12653     ), Coef('Var'  , 0.123867    ), Coef('Var'  , 0.0969539   ), Coef('Var'  , 0.0710326   ), Coef('Var'  , 0.0738739   ), ], 
		[Coef('Var'  , 0.208586    ), Coef('Var'  , 0.240002    ), Coef('Var'  , 0.273618    ), Coef('Var'  , 0.230566    ), Coef('Var'  , 0.1906      ), Coef('Var'  , 0.15656     ), Coef('Var'  , 0.125568    ), Coef('Var'  , 0.165996    ), ], 
		[Coef('Var'  , 0.42557     ), Coef('Var'  , 0.379056    ), Coef('Var'  , 0.337128    ), Coef('Var'  , 0.310078    ), Coef('Var'  , 0.289392    ), Coef('Var'  , 0.330425    ), Coef('Var'  , 0.377834    ), Coef('Var'  , 0.399403    ), ], 
		[Coef('Var'  , 0.184301    ), Coef('Var'  , 0.15008     ), Coef('Var'  , 0.117062    ), Coef('Var'  , 0.149235    ), Coef('Var'  , 0.18309     ), Coef('Var'  , 0.215855    ), Coef('Var'  , 0.250329    ), Coef('Var'  , 0.2167      ), ], 
		[Coef('Var'  , 0.0487578   ), Coef('Var'  , 0.048751    ), Coef('Var'  , 0.0479328   ), Coef('Var'  , 0.0647064   ), Coef('Var'  , 0.0803634   ), Coef('Var'  , 0.0813194   ), Coef('Var'  , 0.0811884   ), Coef('Var'  , 0.0653641   ), ], 
		[Coef('Var'  , 0.0115556   ), Coef('Var'  , 0.0163205   ), Coef('Var'  , 0.0193379   ), Coef('Var'  , 0.0244596   ), Coef('Var'  , 0.0271591   ), Coef('Var'  , 0.0244864   ), Coef('Var'  , 0.0193768   ), Coef('Var'  , 0.0163474   ), ], 
		[Coef('Var'  , 0.0110822   ), Coef('Var'  , 0.0157133   ), Coef('Var'  , 0.0187579   ), Coef('Var'  , 0.0237126   ), Coef('Var'  , 0.0264554   ), Coef('Var'  , 0.0237277   ), Coef('Var'  , 0.0187798   ), Coef('Var'  , 0.0157284   ), ], 
		[Coef('Var'  , 0.0109683   ), Coef('Var'  , 0.0155065   ), Coef('Var'  , 0.0183572   ), Coef('Var'  , 0.0232448   ), Coef('Var'  , 0.0257422   ), Coef('Var'  , 0.0232421   ), Coef('Var'  , 0.0183533   ), Coef('Var'  , 0.0155038   ), ], ])
	etat3.initMat[Chem([Sub('4')])] = FMat([
		[Coef('Const', 0           ), Coef('Var'  , 0.0154359   ), Coef('Var'  , 0.0300262   ), Coef('Var'  , 0.0154359   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0139796   ), Coef('Var'  , 0.0272026   ), Coef('Var'  , 0.0139796   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0169492   ), Coef('Var'  , 0.0332963   ), Coef('Var'  , 0.0169492   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0149688   ), Coef('Var'  , 0.0293916   ), Coef('Var'  , 0.0149688   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.25        ), Coef('Var'  , 0.189032    ), Coef('Var'  , 0.127993    ), Coef('Var'  , 0.0952821   ), Coef('Const', 0.0625      ), Coef('Const', 0.125       ), ], 
		[Coef('Const', 0.5         ), Coef('Var'  , 0.403902    ), Coef('Var'  , 0.308673    ), Coef('Var'  , 0.341402    ), Coef('Const', 0.375       ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0.25        ), Coef('Var'  , 0.280463    ), Coef('Var'  , 0.312782    ), Coef('Var'  , 0.436713    ), Coef('Const', 0.5625      ), Coef('Const', 0.375       ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0287323   ), Coef('Var'  , 0.0582343   ), Coef('Var'  , 0.0287323   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0216787   ), Coef('Var'  , 0.0434041   ), Coef('Var'  , 0.0216787   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.014859    ), Coef('Var'  , 0.0289968   ), Coef('Var'  , 0.014859    ), Coef('Const', 0           ), Coef('Const', 0           ), ], ])
	etat3.initMat[Chem([Sub('5')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0240814   ), Coef('Var'  , 0.0472453   ), Coef('Var'  , 0.0564869   ), Coef('Var'  , 0.0645405   ), Coef('Var'  , 0.0324056   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0198792   ), Coef('Var'  , 0.0389389   ), Coef('Var'  , 0.041911    ), Coef('Var'  , 0.0438869   ), Coef('Var'  , 0.0220318   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0235897   ), Coef('Var'  , 0.0464567   ), Coef('Var'  , 0.0480921   ), Coef('Var'  , 0.0487443   ), Coef('Var'  , 0.0245025   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0199978   ), Coef('Var'  , 0.0392822   ), Coef('Var'  , 0.0380868   ), Coef('Var'  , 0.0357346   ), Coef('Var'  , 0.0180891   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0279137   ), Coef('Var'  , 0.0555973   ), Coef('Var'  , 0.045948    ), Coef('Var'  , 0.0356859   ), Coef('Var'  , 0.0180344   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0454986   ), Coef('Var'  , 0.0916865   ), Coef('Var'  , 0.0699793   ), Coef('Var'  , 0.0486674   ), Coef('Var'  , 0.0244809   ), ], 
		[Coef('Const', 0.111111    ), Coef('Const', 0.222222    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.346563    ), Coef('Var'  , 0.250732    ), Coef('Var'  , 0.191303    ), Coef('Var'  , 0.134595    ), Coef('Var'  , 0.122517    ), ], 
		[Coef('Const', 0.444444    ), Coef('Const', 0.555556    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.342286    ), Coef('Var'  , 0.241222    ), Coef('Var'  , 0.246886    ), Coef('Var'  , 0.254417    ), Coef('Var'  , 0.349045    ), ], 
		[Coef('Const', 0.444444    ), Coef('Const', 0.222222    ), Coef('Const', 0.111111    ), Coef('Var'  , 0.124407    ), Coef('Var'  , 0.138031    ), Coef('Var'  , 0.194259    ), Coef('Var'  , 0.251417    ), Coef('Var'  , 0.347629    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0257845   ), Coef('Var'  , 0.0508085   ), Coef('Var'  , 0.0670489   ), Coef('Var'  , 0.0823114   ), Coef('Var'  , 0.0412645   ), ], ])
	etat3.initMat[Chem([Sub('6')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 5e-08       ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 5e-08       ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 5e-08       ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 5e-08       ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.0625      ), Coef('Var'  , 0.03125     ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Const', 0.375       ), Coef('Var'  , 0.1875      ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 1           ), Coef('Const', 0.75        ), Coef('Const', 0.5625      ), Coef('Var'  , 0.503472    ), Coef('Const', 0.444444    ), Coef('Const', 0.666667    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.222222    ), Coef('Const', 0.444444    ), Coef('Const', 0.333333    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0555555   ), Coef('Const', 0.111111    ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 5e-08       ), Coef('Const', 0           ), Coef('Const', 0           ), ], ])
	etat3.initMat[Chem([Sub('7')])] = FMat([
		[Coef('Var'  , 0.018943    ), Coef('Var'  , 0.00993636  ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0144708   ), Coef('Var'  , 0.0279492   ), Coef('Var'  , 0.0244071   ), ], 
		[Coef('Var'  , 0.0186493   ), Coef('Var'  , 0.00972011  ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0148378   ), Coef('Var'  , 0.0288411   ), Coef('Var'  , 0.0245578   ), ], 
		[Coef('Var'  , 0.130214    ), Coef('Var'  , 0.120445    ), Coef('Const', 0.111111    ), Coef('Const', 0.222222    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.328569    ), Coef('Var'  , 0.213191    ), Coef('Var'  , 0.171236    ), ], 
		[Coef('Var'  , 0.273618    ), Coef('Var'  , 0.358365    ), Coef('Const', 0.444444    ), Coef('Const', 0.555556    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.354046    ), Coef('Var'  , 0.265004    ), Coef('Var'  , 0.267968    ), ], 
		[Coef('Var'  , 0.337128    ), Coef('Var'  , 0.389419    ), Coef('Const', 0.444444    ), Coef('Const', 0.222222    ), Coef('Const', 0.111111    ), Coef('Var'  , 0.163317    ), Coef('Var'  , 0.218255    ), Coef('Var'  , 0.274959    ), ], 
		[Coef('Var'  , 0.117062    ), Coef('Var'  , 0.0581735   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.053898    ), Coef('Var'  , 0.108508    ), Coef('Var'  , 0.112071    ), ], 
		[Coef('Var'  , 0.0479328   ), Coef('Var'  , 0.0242112   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0289714   ), Coef('Var'  , 0.0575078   ), Coef('Var'  , 0.0531824   ), ], 
		[Coef('Var'  , 0.0193379   ), Coef('Var'  , 0.0101884   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0143004   ), Coef('Var'  , 0.0276063   ), Coef('Var'  , 0.0244887   ), ], 
		[Coef('Var'  , 0.0187579   ), Coef('Var'  , 0.00985276  ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0141678   ), Coef('Var'  , 0.0273975   ), Coef('Var'  , 0.0240205   ), ], 
		[Coef('Var'  , 0.0183572   ), Coef('Var'  , 0.00968857  ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0134217   ), Coef('Var'  , 0.0257398   ), Coef('Var'  , 0.0231101   ), ], ])
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
	etat3.initMat[Chem([Sub('8')])] = FMat([
		[Coef('Var'  , 0.0267596   ), Coef('Var'  , 0.0284691   ), Coef('Var'  , 0.0279492   ), Coef('Var'  , 0.0426125   ), Coef('Var'  , 0.0553407   ), Coef('Var'  , 0.0425882   ), Coef('Var'  , 0.0279139   ), Coef('Var'  , 0.0284447   ), ], 
		[Coef('Var'  , 0.0265711   ), Coef('Var'  , 0.028651    ), Coef('Var'  , 0.0288411   ), Coef('Var'  , 0.0457771   ), Coef('Var'  , 0.0611342   ), Coef('Var'  , 0.0457642   ), Coef('Var'  , 0.0288224   ), Coef('Var'  , 0.0286381   ), ], 
		[Coef('Var'  , 0.123867    ), Coef('Var'  , 0.167988    ), Coef('Var'  , 0.213191    ), Coef('Var'  , 0.185873    ), Coef('Var'  , 0.159477    ), Coef('Var'  , 0.122964    ), Coef('Var'  , 0.0873427   ), Coef('Var'  , 0.105078    ), ], 
		[Coef('Var'  , 0.1906      ), Coef('Var'  , 0.226247    ), Coef('Var'  , 0.265004    ), Coef('Var'  , 0.214226    ), Coef('Var'  , 0.165743    ), Coef('Var'  , 0.14022     ), Coef('Var'  , 0.116955    ), Coef('Var'  , 0.152241    ), ], 
		[Coef('Var'  , 0.289392    ), Coef('Var'  , 0.250643    ), Coef('Var'  , 0.218255    ), Coef('Var'  , 0.189125    ), Coef('Var'  , 0.164707    ), Coef('Var'  , 0.211554    ), Coef('Var'  , 0.263127    ), Coef('Var'  , 0.273072    ), ], 
		[Coef('Var'  , 0.18309     ), Coef('Var'  , 0.144959    ), Coef('Var'  , 0.108508    ), Coef('Var'  , 0.124416    ), Coef('Var'  , 0.141543    ), Coef('Var'  , 0.203536    ), Coef('Var'  , 0.266775    ), Coef('Var'  , 0.22408     ), ], 
		[Coef('Var'  , 0.0803634   ), Coef('Var'  , 0.0694666   ), Coef('Var'  , 0.0575078   ), Coef('Var'  , 0.0776495   ), Coef('Var'  , 0.0973614   ), Coef('Var'  , 0.113012    ), Coef('Var'  , 0.128263    ), Coef('Var'  , 0.10483     ), ], 
		[Coef('Var'  , 0.0271591   ), Coef('Var'  , 0.0285716   ), Coef('Var'  , 0.0276063   ), Coef('Var'  , 0.0412565   ), Coef('Var'  , 0.0534126   ), Coef('Var'  , 0.0412833   ), Coef('Var'  , 0.0276451   ), Coef('Var'  , 0.0285984   ), ], 
		[Coef('Var'  , 0.0264554   ), Coef('Var'  , 0.0280277   ), Coef('Var'  , 0.0273975   ), Coef('Var'  , 0.0416606   ), Coef('Var'  , 0.054395    ), Coef('Var'  , 0.0416757   ), Coef('Var'  , 0.0274194   ), Coef('Var'  , 0.0280428   ), ], 
		[Coef('Var'  , 0.0257422   ), Coef('Var'  , 0.0269779   ), Coef('Var'  , 0.0257398   ), Coef('Var'  , 0.0374043   ), Coef('Var'  , 0.0468873   ), Coef('Var'  , 0.0374016   ), Coef('Var'  , 0.0257359   ), Coef('Var'  , 0.0269752   ), ], ])
	etat3.initMat[Chem([Sub('9')])] = FMat([
		[Coef('Var'  , 0.0110912   ), Coef('Var'  , 0.00585001  ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.00585006  ), ], 
		[Coef('Var'  , 0.0107089   ), Coef('Var'  , 0.00561403  ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.00561408  ), ], 
		[Coef('Var'  , 0.0773794   ), Coef('Var'  , 0.038561    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.111111    ), Coef('Var'  , 0.0941165   ), ], 
		[Coef('Var'  , 0.208586    ), Coef('Var'  , 0.103859    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.333333    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.326081    ), ], 
		[Coef('Var'  , 0.42557     ), Coef('Var'  , 0.493109    ), Coef('Const', 0.5625      ), Coef('Const', 0.75        ), Coef('Const', 1           ), Coef('Const', 0.666667    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.434081    ), ], 
		[Coef('Var'  , 0.184301    ), Coef('Var'  , 0.279406    ), Coef('Const', 0.375       ), Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0919063   ), ], 
		[Coef('Var'  , 0.0487578   ), Coef('Var'  , 0.0557899   ), Coef('Const', 0.0625      ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.02454     ), ], 
		[Coef('Var'  , 0.0115556   ), Coef('Var'  , 0.00613221  ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.00613226  ), ], 
		[Coef('Var'  , 0.0110822   ), Coef('Var'  , 0.00586063  ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.00586068  ), ], 
		[Coef('Var'  , 0.0109683   ), Coef('Var'  , 0.00581801  ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.00581806  ), ], ])
	etat3.initMat[Chem([Sub('10')])] = FMat([
		[Coef('Var'  , 0.0189078   ), Coef('Var'  , 0.0243584   ), Coef('Var'  , 0.0279139   ), Coef('Var'  , 0.0144465   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.00991198  ), ], 
		[Coef('Var'  , 0.0186307   ), Coef('Var'  , 0.024532    ), Coef('Var'  , 0.0288224   ), Coef('Var'  , 0.0148249   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.00970719  ), ], 
		[Coef('Var'  , 0.0710326   ), Coef('Var'  , 0.0787502   ), Coef('Var'  , 0.0873427   ), Coef('Var'  , 0.0434373   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0353129   ), ], 
		[Coef('Var'  , 0.125568    ), Coef('Var'  , 0.119956    ), Coef('Var'  , 0.116955    ), Coef('Var'  , 0.0578186   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0621375   ), ], 
		[Coef('Var'  , 0.377834    ), Coef('Var'  , 0.317734    ), Coef('Var'  , 0.263127    ), Coef('Var'  , 0.255191    ), Coef('Const', 0.25        ), Coef('Const', 0.375       ), Coef('Const', 0.5625      ), Coef('Var'  , 0.468793    ), ], 
		[Coef('Var'  , 0.250329    ), Coef('Var'  , 0.257813    ), Coef('Var'  , 0.266775    ), Coef('Var'  , 0.383019    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0.375       ), Coef('Var'  , 0.312294    ), ], 
		[Coef('Var'  , 0.0811884   ), Coef('Var'  , 0.105158    ), Coef('Var'  , 0.128263    ), Coef('Var'  , 0.189334    ), Coef('Const', 0.25        ), Coef('Const', 0.125       ), Coef('Const', 0.0625      ), Coef('Var'  , 0.0720741   ), ], 
		[Coef('Var'  , 0.0193768   ), Coef('Var'  , 0.0245423   ), Coef('Var'  , 0.0276451   ), Coef('Var'  , 0.0143271   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0102152   ), ], 
		[Coef('Var'  , 0.0187798   ), Coef('Var'  , 0.0240507   ), Coef('Var'  , 0.0274194   ), Coef('Var'  , 0.0141829   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.00986781  ), ], 
		[Coef('Var'  , 0.0183533   ), Coef('Var'  , 0.0231047   ), Coef('Var'  , 0.0257359   ), Coef('Var'  , 0.0134189   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0096858   ), ], ])
	etat3.initMat[Chem([Sub('11')])] = FMat([
		[Coef('Var'  , 0.0840117   ), Coef('Var'  , 0.0420369   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.205811    ), Coef('Var'  , 0.161841    ), Coef('Var'  , 0.122847    ), ], 
		[Coef('Var'  , 0.110029    ), Coef('Var'  , 0.0549377   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.369837    ), Coef('Var'  , 0.240107    ), Coef('Var'  , 0.174775    ), ], 
		[Coef('Var'  , 0.239064    ), Coef('Var'  , 0.341484    ), Coef('Const', 0.444444    ), Coef('Const', 0.666667    ), Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.222795    ), Coef('Var'  , 0.196081    ), Coef('Var'  , 0.217057    ), ], 
		[Coef('Var'  , 0.199067    ), Coef('Var'  , 0.32158     ), Coef('Const', 0.444444    ), Coef('Const', 0.333333    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0423969   ), Coef('Var'  , 0.0848847   ), Coef('Var'  , 0.141755    ), ], 
		[Coef('Var'  , 0.0949208   ), Coef('Var'  , 0.102833    ), Coef('Const', 0.111111    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.022888    ), Coef('Var'  , 0.0455819   ), Coef('Var'  , 0.0701658   ), ], 
		[Coef('Var'  , 0.0607552   ), Coef('Var'  , 0.0306377   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.01928     ), Coef('Var'  , 0.0377434   ), Coef('Var'  , 0.0499177   ), ], 
		[Coef('Var'  , 0.0520785   ), Coef('Var'  , 0.0262825   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.019493    ), Coef('Var'  , 0.0384248   ), Coef('Var'  , 0.0457754   ), ], 
		[Coef('Var'  , 0.0449746   ), Coef('Var'  , 0.0225501   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0208124   ), Coef('Var'  , 0.0416599   ), Coef('Var'  , 0.0433624   ), ], 
		[Coef('Var'  , 0.0587097   ), Coef('Var'  , 0.0293254   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0355252   ), Coef('Var'  , 0.0713455   ), Coef('Var'  , 0.0648506   ), ], 
		[Coef('Var'  , 0.056389    ), Coef('Var'  , 0.0283318   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0411616   ), Coef('Var'  , 0.0823308   ), Coef('Var'  , 0.0694933   ), ], ])
	etat3.initMat[Chem([Sub('12')])] = FMat([
		[Coef('Var'  , 0.0472453   ), Coef('Var'  , 0.0512412   ), Coef('Var'  , 0.0529334   ), Coef('Var'  , 0.0585126   ), Coef('Var'  , 0.0612625   ), Coef('Var'  , 0.0554342   ), ], 
		[Coef('Var'  , 0.0389389   ), Coef('Var'  , 0.0441017   ), Coef('Var'  , 0.0471961   ), Coef('Var'  , 0.0526629   ), Coef('Var'  , 0.0555816   ), Coef('Var'  , 0.0483195   ), ], 
		[Coef('Var'  , 0.0464567   ), Coef('Var'  , 0.0529818   ), Coef('Var'  , 0.0577749   ), Coef('Var'  , 0.0656345   ), Coef('Var'  , 0.0715268   ), Coef('Var'  , 0.059832    ), ], 
		[Coef('Var'  , 0.0392822   ), Coef('Var'  , 0.0457938   ), Coef('Var'  , 0.0506698   ), Coef('Var'  , 0.0577312   ), Coef('Var'  , 0.0630174   ), Coef('Var'  , 0.0519328   ), ], 
		[Coef('Var'  , 0.0555973   ), Coef('Var'  , 0.0753464   ), Coef('Var'  , 0.0947111   ), Coef('Var'  , 0.0922977   ), Coef('Var'  , 0.0896815   ), Coef('Var'  , 0.0727786   ), ], 
		[Coef('Var'  , 0.0916865   ), Coef('Var'  , 0.134895    ), Coef('Var'  , 0.180123    ), Coef('Var'  , 0.161574    ), Coef('Var'  , 0.145629    ), Coef('Var'  , 0.117676    ), ], 
		[Coef('Var'  , 0.250732    ), Coef('Var'  , 0.242454    ), Coef('Var'  , 0.239266    ), Coef('Var'  , 0.220225    ), Coef('Var'  , 0.207222    ), Coef('Var'  , 0.226453    ), ], 
		[Coef('Var'  , 0.241222    ), Coef('Var'  , 0.186385    ), Coef('Var'  , 0.133997    ), Coef('Var'  , 0.13763     ), Coef('Var'  , 0.143988    ), Coef('Var'  , 0.191371    ), ], 
		[Coef('Var'  , 0.138031    ), Coef('Var'  , 0.114327    ), Coef('Var'  , 0.0911247   ), Coef('Var'  , 0.096353    ), Coef('Var'  , 0.101961    ), Coef('Var'  , 0.119729    ), ], 
		[Coef('Var'  , 0.0508085   ), Coef('Var'  , 0.0524743   ), Coef('Var'  , 0.0522043   ), Coef('Var'  , 0.057379    ), Coef('Var'  , 0.06013     ), Coef('Var'  , 0.0564736   ), ], ])
	etat3.initMat[Chem([Sub('13')])] = FMat([
		[Coef('Var'  , 0.0709676   ), Coef('Var'  , 0.0674094   ), Coef('Var'  , 0.0612625   ), Coef('Var'  , 0.0609597   ), Coef('Var'  , 0.0577847   ), Coef('Var'  , 0.0656635   ), ], 
		[Coef('Var'  , 0.0685769   ), Coef('Var'  , 0.0632149   ), Coef('Var'  , 0.0555816   ), Coef('Var'  , 0.0556802   ), Coef('Var'  , 0.0531987   ), Coef('Var'  , 0.0620145   ), ], 
		[Coef('Var'  , 0.102586    ), Coef('Var'  , 0.0877405   ), Coef('Var'  , 0.0715268   ), Coef('Var'  , 0.0711155   ), Coef('Var'  , 0.0688244   ), Coef('Var'  , 0.0863713   ), ], 
		[Coef('Var'  , 0.0918282   ), Coef('Var'  , 0.0779984   ), Coef('Var'  , 0.0630174   ), Coef('Var'  , 0.0628151   ), Coef('Var'  , 0.0609496   ), Coef('Var'  , 0.0769433   ), ], 
		[Coef('Var'  , 0.104052    ), Coef('Var'  , 0.0966857   ), Coef('Var'  , 0.0896815   ), Coef('Var'  , 0.096904    ), Coef('Var'  , 0.104073    ), Coef('Var'  , 0.10386     ), ], 
		[Coef('Var'  , 0.135696    ), Coef('Var'  , 0.139671    ), Coef('Var'  , 0.145629    ), Coef('Var'  , 0.165966    ), Coef('Var'  , 0.188913    ), Coef('Var'  , 0.161282    ), ], 
		[Coef('Var'  , 0.152285    ), Coef('Var'  , 0.177349    ), Coef('Var'  , 0.207222    ), Coef('Var'  , 0.210496    ), Coef('Var'  , 0.219727    ), Coef('Var'  , 0.183621    ), ], 
		[Coef('Var'  , 0.10839     ), Coef('Var'  , 0.12508     ), Coef('Var'  , 0.143988    ), Coef('Var'  , 0.124458    ), Coef('Var'  , 0.107577    ), Coef('Var'  , 0.106922    ), ], 
		[Coef('Var'  , 0.0978745   ), Coef('Var'  , 0.0997456   ), Coef('Var'  , 0.101961    ), Coef('Var'  , 0.0924175   ), Coef('Var'  , 0.0832005   ), Coef('Var'  , 0.0904078   ), ], 
		[Coef('Var'  , 0.0677438   ), Coef('Var'  , 0.0651057   ), Coef('Var'  , 0.06013     ), Coef('Var'  , 0.0591878   ), Coef('Var'  , 0.0557529   ), Coef('Var'  , 0.0629152   ), ], ])
	etat3.initMat[Chem([Sub('14')])] = FMat([
		[Coef('Var'  , 0.0300262   ), Coef('Var'  , 0.0450428   ), Coef('Var'  , 0.0577847   ), Coef('Var'  , 0.0567667   ), Coef('Var'  , 0.0529334   ), Coef('Var'  , 0.0425957   ), ], 
		[Coef('Var'  , 0.0272026   ), Coef('Var'  , 0.0412196   ), Coef('Var'  , 0.0531987   ), Coef('Var'  , 0.0514625   ), Coef('Var'  , 0.0471961   ), Coef('Var'  , 0.0382022   ), ], 
		[Coef('Var'  , 0.0332963   ), Coef('Var'  , 0.0518224   ), Coef('Var'  , 0.0688244   ), Coef('Var'  , 0.0642653   ), Coef('Var'  , 0.0577749   ), Coef('Var'  , 0.0463414   ), ], 
		[Coef('Var'  , 0.0293916   ), Coef('Var'  , 0.0458488   ), Coef('Var'  , 0.0609496   ), Coef('Var'  , 0.0566761   ), Coef('Var'  , 0.0506698   ), Coef('Var'  , 0.0407649   ), ], 
		[Coef('Var'  , 0.127993    ), Coef('Var'  , 0.116071    ), Coef('Var'  , 0.104073    ), Coef('Var'  , 0.0994717   ), Coef('Var'  , 0.0947111   ), Coef('Var'  , 0.111465    ), ], 
		[Coef('Var'  , 0.308673    ), Coef('Var'  , 0.24769     ), Coef('Var'  , 0.188913    ), Coef('Var'  , 0.183185    ), Coef('Var'  , 0.180123    ), Coef('Var'  , 0.243298    ), ], 
		[Coef('Var'  , 0.312782    ), Coef('Var'  , 0.263847    ), Coef('Var'  , 0.219727    ), Coef('Var'  , 0.226497    ), Coef('Var'  , 0.239266    ), Coef('Var'  , 0.273576    ), ], 
		[Coef('Var'  , 0.0582343   ), Coef('Var'  , 0.0818824   ), Coef('Var'  , 0.107577    ), Coef('Var'  , 0.119472    ), Coef('Var'  , 0.133997    ), Coef('Var'  , 0.0950543   ), ], 
		[Coef('Var'  , 0.0434041   ), Coef('Var'  , 0.0632185   ), Coef('Var'  , 0.0832005   ), Coef('Var'  , 0.0870151   ), Coef('Var'  , 0.0911247   ), Coef('Var'  , 0.067154    ), ], 
		[Coef('Var'  , 0.0289968   ), Coef('Var'  , 0.0433576   ), Coef('Var'  , 0.0557529   ), Coef('Var'  , 0.0551885   ), Coef('Var'  , 0.0522043   ), Coef('Var'  , 0.0415488   ), ], ])
	etat3.initMat[Chem([Sub('15')])] = FMat([
		[Coef('Var'  , 0.197535    ), Coef('Var'  , 0.22366     ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.22366     ), ], 
		[Coef('Var'  , 0.214465    ), Coef('Var'  , 0.357055    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.107055    ), ], 
		[Coef('Var'  , 0.138537    ), Coef('Var'  , 0.194135    ), Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0691346   ), ], 
		[Coef('Var'  , 0.0365612   ), Coef('Var'  , 0.0183113   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0183113   ), ], 
		[Coef('Var'  , 0.0230895   ), Coef('Var'  , 0.0116997   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0116997   ), ], 
		[Coef('Var'  , 0.0233175   ), Coef('Var'  , 0.0120005   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0120005   ), ], 
		[Coef('Var'  , 0.0282022   ), Coef('Var'  , 0.014283    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.014283    ), ], 
		[Coef('Var'  , 0.0385497   ), Coef('Var'  , 0.0192045   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0192045   ), ], 
		[Coef('Var'  , 0.120086    ), Coef('Var'  , 0.0598678   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.184868    ), ], 
		[Coef('Var'  , 0.179656    ), Coef('Var'  , 0.0897834   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.339783    ), ], ])
	etat3.initMat[Chem([Sub('16')])] = FMat([
		[Coef('Var'  , 0.111174    ), Coef('Var'  , 0.18057     ), Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0555701   ), ], 
		[Coef('Var'  , 0.0410119   ), Coef('Var'  , 0.020448    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0204481   ), ], 
		[Coef('Var'  , 0.0399461   ), Coef('Var'  , 0.0199875   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0199875   ), ], 
		[Coef('Var'  , 0.0247701   ), Coef('Var'  , 0.0125115   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0125116   ), ], 
		[Coef('Var'  , 0.0207618   ), Coef('Var'  , 0.0105608   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0105608   ), ], 
		[Coef('Var'  , 0.0256429   ), Coef('Var'  , 0.013094    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.013094    ), ], 
		[Coef('Var'  , 0.0789413   ), Coef('Var'  , 0.0394511   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.111111    ), Coef('Var'  , 0.0950067   ), ], 
		[Coef('Var'  , 0.202102    ), Coef('Var'  , 0.100829    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.333333    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.323051    ), ], 
		[Coef('Var'  , 0.275825    ), Coef('Var'  , 0.26265     ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.666667    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.359872    ), ], 
		[Coef('Var'  , 0.179825    ), Coef('Var'  , 0.339897    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0898975   ), ], ])
	
	
	
	etat4.bords   = {Bord('0'): etat19, Bord('1'): etat20, Bord('2'): etat19, Bord('3'): etat21, }
	etat4.permuts = {}
	etat4.interns = {Intern('_'): etat4, }
	etat4.subs    = {Sub('0'): etat1, Sub('1'): etat2, Sub('2'): etat3, Sub('3'): etat5, Sub('4'): etat6, Sub('5'): etat7, Sub('6'): etat8, Sub('7'): etat9, Sub('G', True): Etat.etatPoint, Sub('8'): etat10, Sub('9'): etat11, Sub('10'): etat12, Sub('11'): etat13, Sub('12'): etat14, Sub('13'): etat15, Sub('14'): etat16, Sub('15'): etat17, Sub('16'): etat18, }
	
	etat4.buildIntern()
	
	
	etat4.eqs = [
		(Chem([Bord('1'), Sub('0'), Permut('0'), ])	,	Chem([Sub('0'), Bord('2'), ])),
		(Chem([Bord('0'), Sub('1'), Permut('0'), ])	,	Chem([Sub('0'), Bord('3'), ])),
		(Chem([Bord('0'), Sub('0'), Permut('0'), ])	,	Chem([Sub('1'), Bord('2'), ])),
		(Chem([Bord('3'), Sub('3'), Permut('0'), ])	,	Chem([Sub('1'), Bord('3'), ])),
		(Chem([Bord('3'), Sub('0'), Permut('0'), ])	,	Chem([Sub('5'), Bord('2'), ])),
		(Chem([Bord('2'), Sub('1'), Permut('0'), ])	,	Chem([Sub('5'), Bord('3'), ])),
		(Chem([Bord('3'), Sub('1'), Permut('0'), ])	,	Chem([Sub('12'), Bord('2'), ])),
		(Chem([Bord('3'), Sub('2'), Permut('0'), ])	,	Chem([Sub('13'), Bord('0'), ])),
		(Chem([Bord('1'), Sub('1'), Permut('0'), ])	,	Chem([Sub('15'), Bord('3'), ])),
		(Chem([Bord('1'), Sub('2'), Permut('0'), ])	,	Chem([Sub('16'), Bord('0'), ])),
		(Chem([Bord('2'), Sub('0'), Permut('0'), ])	,	Chem([Sub('16'), Bord('3'), ])),
		(Chem([Sub('0'), Bord('0'), Bord('1'), ])	,	Chem([Sub('11'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('1'), Bord('1'), ])	,	Chem([Sub('15'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('3'), Bord('1'), ])	,	Chem([Sub('1'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('0'), Bord('1'), ])	,	Chem([Sub('11'), Bord('4'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('3'), Bord('1'), ])	,	Chem([Sub('13'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('4'), Bord('1'), ])	,	Chem([Sub('8'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('0'), Bord('1'), ])	,	Chem([Sub('11'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('1'), Bord('1'), ])	,	Chem([Sub('9'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('2'), Bord('1'), ])	,	Chem([Sub('6'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('3'), Bord('1'), ])	,	Chem([Sub('16'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('4'), Bord('1'), ])	,	Chem([Sub('15'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('3'), Bord('0'), Bord('1'), ])	,	Chem([Sub('7'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('3'), Bord('1'), Bord('1'), ])	,	Chem([Sub('8'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('3'), Bord('2'), Bord('1'), ])	,	Chem([Sub('10'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('3'), Bord('3'), Bord('1'), ])	,	Chem([Sub('9'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('4'), Bord('0'), Bord('1'), ])	,	Chem([Sub('14'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('4'), Bord('1'), Bord('1'), ])	,	Chem([Sub('6'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('4'), Bord('2'), Bord('1'), ])	,	Chem([Sub('10'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('5'), Bord('0'), Bord('1'), ])	,	Chem([Sub('6'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('5'), Bord('1'), Bord('1'), ])	,	Chem([Sub('12'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('5'), Bord('3'), Bord('1'), ])	,	Chem([Sub('16'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('7'), Bord('0'), Bord('1'), ])	,	Chem([Sub('9'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('7'), Bord('1'), Bord('1'), ])	,	Chem([Sub('11'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('7'), Bord('2'), Bord('1'), ])	,	Chem([Sub('8'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('8'), Bord('2'), Bord('1'), ])	,	Chem([Sub('10'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('9'), Bord('0'), Bord('1'), ])	,	Chem([Sub('10'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('11'), Bord('2'), Bord('1'), ])	,	Chem([Sub('15'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('12'), Bord('0'), Bord('1'), ])	,	Chem([Sub('14'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('12'), Bord('1'), Bord('1'), ])	,	Chem([Sub('13'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('13'), Bord('1'), Bord('1'), ])	,	Chem([Sub('14'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('15'), Bord('2'), Bord('1'), ])	,	Chem([Sub('16'), Bord('0'), Bord('1'), ])),
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
		[Coef('Const', 0.25        ), Coef('Var'  , 0.189324    ), Coef('Var'  , 0.12876     ), Coef('Var'  , 0.0643245   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.5         ), Coef('Var'  , 0.354973    ), Coef('Var'  , 0.209912    ), Coef('Var'  , 0.104973    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0.25        ), Coef('Var'  , 0.270032    ), Coef('Var'  , 0.290499    ), Coef('Var'  , 0.367254    ), Coef('Const', 0.444444    ), Coef('Const', 0.666667    ), Coef('Const', 1           ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.102921    ), Coef('Var'  , 0.206266    ), Coef('Var'  , 0.325143    ), Coef('Const', 0.444444    ), Coef('Const', 0.333333    ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0413289   ), Coef('Var'  , 0.0827097   ), Coef('Var'  , 0.0968844   ), Coef('Const', 0.111111    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0123363   ), Coef('Var'  , 0.024324    ), Coef('Var'  , 0.0123363   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0129111   ), Coef('Var'  , 0.0254329   ), Coef('Var'  , 0.0129112   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0161731   ), Coef('Var'  , 0.0320968   ), Coef('Var'  , 0.0161732   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], ])
	etat4.initMat[Chem([Sub('1')])] = FMat([
		[Coef('Var'  , 0.275852    ), Coef('Var'  , 0.236347    ), Coef('Var'  , 0.198639    ), Coef('Var'  , 0.223994    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.75        ), Coef('Const', 0.5625      ), Coef('Var'  , 0.418603    ), ], 
		[Coef('Var'  , 0.121996    ), Coef('Var'  , 0.183792    ), Coef('Var'  , 0.245678    ), Coef('Var'  , 0.372807    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0609851   ), ], 
		[Coef('Var'  , 0.114516    ), Coef('Var'  , 0.15896     ), Coef('Var'  , 0.203927    ), Coef('Var'  , 0.226754    ), Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0572065   ), ], 
		[Coef('Var'  , 0.07295     ), Coef('Var'  , 0.0869192   ), Coef('Var'  , 0.101415    ), Coef('Var'  , 0.050509    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0364102   ), ], 
		[Coef('Var'  , 0.0671734   ), Coef('Var'  , 0.0670163   ), Coef('Var'  , 0.066332    ), Coef('Var'  , 0.033246    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0337703   ), ], 
		[Coef('Var'  , 0.0631224   ), Coef('Var'  , 0.0551245   ), Coef('Var'  , 0.0454811   ), Coef('Var'  , 0.0231003   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0320242   ), ], 
		[Coef('Var'  , 0.0886617   ), Coef('Var'  , 0.0712809   ), Coef('Var'  , 0.0530001   ), Coef('Var'  , 0.0267662   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.0625      ), Coef('Var'  , 0.0757647   ), ], 
		[Coef('Var'  , 0.19573     ), Coef('Var'  , 0.14056     ), Coef('Var'  , 0.085528    ), Coef('Var'  , 0.0428233   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Const', 0.375       ), Coef('Var'  , 0.285236    ), ], ])
	etat4.initMat[Chem([Sub('2')])] = FMat([
		[Coef('Var'  , 0.0486784   ), Coef('Var'  , 0.0706034   ), Coef('Var'  , 0.092315    ), Coef('Var'  , 0.0995002   ), Coef('Var'  , 0.107167    ), Coef('Var'  , 0.0935356   ), Coef('Var'  , 0.0805207   ), Coef('Var'  , 0.0565231   ), Coef('Var'  , 0.0325614   ), Coef('Var'  , 0.0408195   ), ], 
		[Coef('Var'  , 0.0579175   ), Coef('Var'  , 0.0806037   ), Coef('Var'  , 0.102295    ), Coef('Var'  , 0.102329    ), Coef('Var'  , 0.100998    ), Coef('Var'  , 0.081353    ), Coef('Var'  , 0.0596246   ), Coef('Var'  , 0.0461879   ), Coef('Var'  , 0.0309275   ), Coef('Var'  , 0.044951    ), ], 
		[Coef('Var'  , 0.161416    ), Coef('Var'  , 0.170647    ), Coef('Var'  , 0.180841    ), Coef('Var'  , 0.157504    ), Coef('Var'  , 0.134467    ), Coef('Var'  , 0.111222    ), Coef('Var'  , 0.0870019   ), Coef('Var'  , 0.0889806   ), Coef('Var'  , 0.0901274   ), Coef('Var'  , 0.125596    ), ], 
		[Coef('Var'  , 0.284677    ), Coef('Var'  , 0.244889    ), Coef('Var'  , 0.20673     ), Coef('Var'  , 0.171399    ), Coef('Var'  , 0.137357    ), Coef('Var'  , 0.127992    ), Coef('Var'  , 0.118964    ), Coef('Var'  , 0.165056    ), Coef('Var'  , 0.211361    ), Coef('Var'  , 0.247525    ), ], 
		[Coef('Var'  , 0.259787    ), Coef('Var'  , 0.212584    ), Coef('Var'  , 0.16632     ), Coef('Var'  , 0.153821    ), Coef('Var'  , 0.142109    ), Coef('Var'  , 0.153845    ), Coef('Var'  , 0.166355    ), Coef('Var'  , 0.222361    ), Coef('Var'  , 0.279196    ), Coef('Var'  , 0.269056    ), ], 
		[Coef('Var'  , 0.0799852   ), Coef('Var'  , 0.0827301   ), Coef('Var'  , 0.0848036   ), Coef('Var'  , 0.102194    ), Coef('Var'  , 0.118733    ), Coef('Var'  , 0.139141    ), Coef('Var'  , 0.159274    ), Coef('Var'  , 0.171951    ), Coef('Var'  , 0.184768    ), Coef('Var'  , 0.132446    ), ], 
		[Coef('Var'  , 0.0647615   ), Coef('Var'  , 0.0752243   ), Coef('Var'  , 0.0850297   ), Coef('Var'  , 0.109531    ), Coef('Var'  , 0.133904    ), Coef('Var'  , 0.163558    ), Coef('Var'  , 0.194442    ), Coef('Var'  , 0.159963    ), Coef('Var'  , 0.126674    ), Coef('Var'  , 0.0957264   ), ], 
		[Coef('Var'  , 0.0427764   ), Coef('Var'  , 0.0627185   ), Coef('Var'  , 0.0816662   ), Coef('Var'  , 0.10372     ), Coef('Var'  , 0.125265    ), Coef('Var'  , 0.129353    ), Coef('Var'  , 0.133817    ), Coef('Var'  , 0.0889787   ), Coef('Var'  , 0.0443848   ), Coef('Var'  , 0.0438786   ), ], ])
	etat4.initMat[Chem([Sub('3')])] = FMat([
		[Coef('Var'  , 0.134382    ), Coef('Var'  , 0.138463    ), Coef('Var'  , 0.145306    ), Coef('Var'  , 0.14936     ), Coef('Var'  , 0.1566      ), Coef('Var'  , 0.149534    ), Coef('Var'  , 0.145676    ), Coef('Var'  , 0.138637    ), ], 
		[Coef('Var'  , 0.119365    ), Coef('Var'  , 0.12197     ), Coef('Var'  , 0.124138    ), Coef('Var'  , 0.12272     ), Coef('Var'  , 0.121095    ), Coef('Var'  , 0.118947    ), Coef('Var'  , 0.116322    ), Coef('Var'  , 0.118197    ), ], 
		[Coef('Var'  , 0.13388     ), Coef('Var'  , 0.135193    ), Coef('Var'  , 0.136073    ), Coef('Var'  , 0.133455    ), Coef('Var'  , 0.130503    ), Coef('Var'  , 0.129745    ), Coef('Var'  , 0.128311    ), Coef('Var'  , 0.131483    ), ], 
		[Coef('Var'  , 0.108891    ), Coef('Var'  , 0.107785    ), Coef('Var'  , 0.107012    ), Coef('Var'  , 0.103434    ), Coef('Var'  , 0.100109    ), Coef('Var'  , 0.101085    ), Coef('Var'  , 0.101989    ), Coef('Var'  , 0.105436    ), ], 
		[Coef('Var'  , 0.116187    ), Coef('Var'  , 0.114568    ), Coef('Var'  , 0.112345    ), Coef('Var'  , 0.109971    ), Coef('Var'  , 0.106742    ), Coef('Var'  , 0.109111    ), Coef('Var'  , 0.110584    ), Coef('Var'  , 0.113709    ), ], 
		[Coef('Var'  , 0.115009    ), Coef('Var'  , 0.113802    ), Coef('Var'  , 0.11062     ), Coef('Var'  , 0.110771    ), Coef('Var'  , 0.108596    ), Coef('Var'  , 0.111887    ), Coef('Var'  , 0.112985    ), Coef('Var'  , 0.114918    ), ], 
		[Coef('Var'  , 0.126828    ), Coef('Var'  , 0.123273    ), Coef('Var'  , 0.119398    ), Coef('Var'  , 0.120752    ), Coef('Var'  , 0.121547    ), Coef('Var'  , 0.125322    ), Coef('Var'  , 0.128977    ), Coef('Var'  , 0.127844    ), ], 
		[Coef('Var'  , 0.145457    ), Coef('Var'  , 0.144946    ), Coef('Var'  , 0.145109    ), Coef('Var'  , 0.149538    ), Coef('Var'  , 0.154807    ), Coef('Var'  , 0.154369    ), Coef('Var'  , 0.155155    ), Coef('Var'  , 0.149777    ), ], ])
	etat4.initMat[Chem([Sub('4')])] = FMat([
		[Coef('Var'  , 0.151455    ), Coef('Var'  , 0.169751    ), Coef('Var'  , 0.190098    ), Coef('Var'  , 0.154242    ), Coef('Var'  , 0.119909    ), Coef('Var'  , 0.134762    ), ], 
		[Coef('Var'  , 0.0858293   ), Coef('Var'  , 0.068785    ), Coef('Var'  , 0.0493259   ), Coef('Var'  , 0.0564095   ), Coef('Var'  , 0.0607786   ), Coef('Var'  , 0.0746235   ), ], 
		[Coef('Var'  , 0.0962764   ), Coef('Var'  , 0.0772274   ), Coef('Var'  , 0.0559194   ), Coef('Var'  , 0.0659334   ), Coef('Var'  , 0.0735562   ), Coef('Var'  , 0.0860806   ), ], 
		[Coef('Var'  , 0.0830225   ), Coef('Var'  , 0.0676746   ), Coef('Var'  , 0.0510527   ), Coef('Var'  , 0.0646978   ), Coef('Var'  , 0.0770858   ), Coef('Var'  , 0.0806159   ), ], 
		[Coef('Var'  , 0.0998547   ), Coef('Var'  , 0.0831137   ), Coef('Var'  , 0.0658802   ), Coef('Var'  , 0.0909851   ), Coef('Var'  , 0.115935    ), Coef('Var'  , 0.10797     ), ], 
		[Coef('Var'  , 0.108186    ), Coef('Var'  , 0.0917027   ), Coef('Var'  , 0.0744168   ), Coef('Var'  , 0.105077    ), Coef('Var'  , 0.135387    ), Coef('Var'  , 0.122074    ), ], 
		[Coef('Var'  , 0.176567    ), Coef('Var'  , 0.200547    ), Coef('Var'  , 0.226827    ), Coef('Var'  , 0.223134    ), Coef('Var'  , 0.222065    ), Coef('Var'  , 0.198088    ), ], 
		[Coef('Var'  , 0.198809    ), Coef('Var'  , 0.241198    ), Coef('Var'  , 0.28648     ), Coef('Var'  , 0.239521    ), Coef('Var'  , 0.195283    ), Coef('Var'  , 0.195785    ), ], ])
	etat4.initMat[Chem([Sub('5')])] = FMat([
		[Coef('Const', 0           ), Coef('Var'  , 0.0324859   ), Coef('Var'  , 0.0651525   ), Coef('Var'  , 0.0637359   ), Coef('Const', 0.0625      ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0166908   ), Coef('Var'  , 0.032489    ), Coef('Var'  , 0.0166908   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0213024   ), Coef('Var'  , 0.0419266   ), Coef('Var'  , 0.0213024   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0248942   ), Coef('Var'  , 0.0495723   ), Coef('Var'  , 0.0248942   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.25        ), Coef('Var'  , 0.191141    ), Coef('Var'  , 0.132512    ), Coef('Var'  , 0.0661408   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.5         ), Coef('Var'  , 0.349174    ), Coef('Var'  , 0.198463    ), Coef('Var'  , 0.0991737   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0.25        ), Coef('Var'  , 0.277142    ), Coef('Var'  , 0.305105    ), Coef('Var'  , 0.433392    ), Coef('Const', 0.5625      ), Coef('Const', 0.75        ), Coef('Const', 1           ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0871705   ), Coef('Var'  , 0.17478     ), Coef('Var'  , 0.274671    ), Coef('Const', 0.375       ), Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), ], ])
	etat4.initMat[Chem([Sub('6')])] = FMat([
		[Coef('Var'  , 0.0805207   ), Coef('Var'  , 0.0997976   ), Coef('Var'  , 0.119909    ), Coef('Var'  , 0.0921124   ), Coef('Var'  , 0.0651525   ), Coef('Var'  , 0.0726571   ), ], 
		[Coef('Var'  , 0.0596246   ), Coef('Var'  , 0.0615562   ), Coef('Var'  , 0.0607786   ), Coef('Var'  , 0.0478148   ), Coef('Var'  , 0.032489    ), Coef('Var'  , 0.047123    ), ], 
		[Coef('Var'  , 0.0870019   ), Coef('Var'  , 0.0812677   ), Coef('Var'  , 0.0735562   ), Coef('Var'  , 0.0586957   ), Coef('Var'  , 0.0419266   ), Coef('Var'  , 0.0651768   ), ], 
		[Coef('Var'  , 0.118964    ), Coef('Var'  , 0.0983257   ), Coef('Var'  , 0.0770858   ), Coef('Var'  , 0.0637138   ), Coef('Var'  , 0.0495723   ), Coef('Var'  , 0.0844004   ), ], 
		[Coef('Var'  , 0.166355    ), Coef('Var'  , 0.140876    ), Coef('Var'  , 0.115935    ), Coef('Var'  , 0.124062    ), Coef('Var'  , 0.132512    ), Coef('Var'  , 0.149097    ), ], 
		[Coef('Var'  , 0.159274    ), Coef('Var'  , 0.147315    ), Coef('Var'  , 0.135387    ), Coef('Var'  , 0.166898    ), Coef('Var'  , 0.198463    ), Coef('Var'  , 0.178764    ), ], 
		[Coef('Var'  , 0.194442    ), Coef('Var'  , 0.207081    ), Coef('Var'  , 0.222065    ), Coef('Var'  , 0.262479    ), Coef('Var'  , 0.305105    ), Coef('Var'  , 0.248886    ), ], 
		[Coef('Var'  , 0.133817    ), Coef('Var'  , 0.16378     ), Coef('Var'  , 0.195283    ), Coef('Var'  , 0.184225    ), Coef('Var'  , 0.17478     ), Coef('Var'  , 0.153896    ), ], ])
	etat4.initMat[Chem([Sub('7')])] = FMat([
		[Coef('Var'  , 0.145306    ), Coef('Var'  , 0.136642    ), Coef('Var'  , 0.130462    ), Coef('Var'  , 0.137849    ), Coef('Var'  , 0.147099    ), Coef('Var'  , 0.160857    ), Coef('Var'  , 0.176979    ), Coef('Var'  , 0.15965     ), ], 
		[Coef('Var'  , 0.124138    ), Coef('Var'  , 0.12472     ), Coef('Var'  , 0.124888    ), Coef('Var'  , 0.138188    ), Coef('Var'  , 0.151053    ), Coef('Var'  , 0.140361    ), Coef('Var'  , 0.129598    ), Coef('Var'  , 0.126893    ), ], 
		[Coef('Var'  , 0.136073    ), Coef('Var'  , 0.139308    ), Coef('Var'  , 0.142413    ), Coef('Var'  , 0.153387    ), Coef('Var'  , 0.164771    ), Coef('Var'  , 0.150199    ), Coef('Var'  , 0.136188    ), Coef('Var'  , 0.13612     ), ], 
		[Coef('Var'  , 0.107012    ), Coef('Var'  , 0.113104    ), Coef('Var'  , 0.11984     ), Coef('Var'  , 0.124734    ), Coef('Var'  , 0.130698    ), Coef('Var'  , 0.115797    ), Coef('Var'  , 0.10185     ), Coef('Var'  , 0.104168    ), ], 
		[Coef('Var'  , 0.112345    ), Coef('Var'  , 0.117042    ), Coef('Var'  , 0.121332    ), Coef('Var'  , 0.117668    ), Coef('Var'  , 0.113908    ), Coef('Var'  , 0.107749    ), Coef('Var'  , 0.10114     ), Coef('Var'  , 0.107123    ), ], 
		[Coef('Var'  , 0.11062     ), Coef('Var'  , 0.1114      ), Coef('Var'  , 0.110246    ), Coef('Var'  , 0.0993739   ), Coef('Var'  , 0.0867275   ), Coef('Var'  , 0.0923108   ), Coef('Var'  , 0.0957151   ), Coef('Var'  , 0.104337    ), ], 
		[Coef('Var'  , 0.119398    ), Coef('Var'  , 0.11935     ), Coef('Var'  , 0.118753    ), Coef('Var'  , 0.106063    ), Coef('Var'  , 0.0925336   ), Coef('Var'  , 0.10033     ), Coef('Var'  , 0.10696     ), Coef('Var'  , 0.113617    ), ], 
		[Coef('Var'  , 0.145109    ), Coef('Var'  , 0.138434    ), Coef('Var'  , 0.132066    ), Coef('Var'  , 0.122738    ), Coef('Var'  , 0.113211    ), Coef('Var'  , 0.132396    ), Coef('Var'  , 0.15157     ), Coef('Var'  , 0.148092    ), ], ])
	etat4.initMat[Chem([Sub('G')])] = FMat([
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], ])
	etat4.initMat[Chem([Sub('8')])] = FMat([
		[Coef('Var'  , 0.1566      ), Coef('Var'  , 0.165185    ), Coef('Var'  , 0.176979    ), Coef('Var'  , 0.22509     ), Coef('Var'  , 0.275852    ), Coef('Var'  , 0.225512    ), Coef('Var'  , 0.177906    ), Coef('Var'  , 0.165607    ), ], 
		[Coef('Var'  , 0.121095    ), Coef('Var'  , 0.125381    ), Coef('Var'  , 0.129598    ), Coef('Var'  , 0.125762    ), Coef('Var'  , 0.121996    ), Coef('Var'  , 0.117427    ), Coef('Var'  , 0.112497    ), Coef('Var'  , 0.117047    ), ], 
		[Coef('Var'  , 0.130503    ), Coef('Var'  , 0.133396    ), Coef('Var'  , 0.136188    ), Coef('Var'  , 0.125237    ), Coef('Var'  , 0.114516    ), Coef('Var'  , 0.116805    ), Coef('Var'  , 0.118733    ), Coef('Var'  , 0.124964    ), ], 
		[Coef('Var'  , 0.100109    ), Coef('Var'  , 0.100818    ), Coef('Var'  , 0.10185     ), Coef('Var'  , 0.0871862   ), Coef('Var'  , 0.07295     ), Coef('Var'  , 0.0815379   ), Coef('Var'  , 0.0900426   ), Coef('Var'  , 0.0951699   ), ], 
		[Coef('Var'  , 0.106742    ), Coef('Var'  , 0.104394    ), Coef('Var'  , 0.10114     ), Coef('Var'  , 0.0845437   ), Coef('Var'  , 0.0671734   ), Coef('Var'  , 0.0827029   ), Coef('Var'  , 0.0973869   ), Coef('Var'  , 0.102554    ), ], 
		[Coef('Var'  , 0.108596    ), Coef('Var'  , 0.10338     ), Coef('Var'  , 0.0957151   ), Coef('Var'  , 0.0804968   ), Coef('Var'  , 0.0631224   ), Coef('Var'  , 0.0831175   ), Coef('Var'  , 0.101154    ), Coef('Var'  , 0.106       ), ], 
		[Coef('Var'  , 0.121547    ), Coef('Var'  , 0.114642    ), Coef('Var'  , 0.10696     ), Coef('Var'  , 0.0982681   ), Coef('Var'  , 0.0886617   ), Coef('Var'  , 0.108692    ), Coef('Var'  , 0.128501    ), Coef('Var'  , 0.125065    ), ], 
		[Coef('Var'  , 0.154807    ), Coef('Var'  , 0.152803    ), Coef('Var'  , 0.15157     ), Coef('Var'  , 0.173415    ), Coef('Var'  , 0.19573     ), Coef('Var'  , 0.184205    ), Coef('Var'  , 0.17378     ), Coef('Var'  , 0.163593    ), ], ])
	etat4.initMat[Chem([Sub('9')])] = FMat([
		[Coef('Var'  , 0.134382    ), Coef('Var'  , 0.131701    ), Coef('Var'  , 0.131388    ), Coef('Var'  , 0.118515    ), Coef('Var'  , 0.107167    ), Coef('Var'  , 0.118094    ), Coef('Var'  , 0.130462    ), Coef('Var'  , 0.131281    ), ], 
		[Coef('Var'  , 0.119365    ), Coef('Var'  , 0.114122    ), Coef('Var'  , 0.107786    ), Coef('Var'  , 0.105189    ), Coef('Var'  , 0.100998    ), Coef('Var'  , 0.113525    ), Coef('Var'  , 0.124888    ), Coef('Var'  , 0.122458    ), ], 
		[Coef('Var'  , 0.13388     ), Coef('Var'  , 0.129889    ), Coef('Var'  , 0.124957    ), Coef('Var'  , 0.130132    ), Coef('Var'  , 0.134467    ), Coef('Var'  , 0.138566    ), Coef('Var'  , 0.142413    ), Coef('Var'  , 0.138322    ), ], 
		[Coef('Var'  , 0.108891    ), Coef('Var'  , 0.108455    ), Coef('Var'  , 0.10803     ), Coef('Var'  , 0.122548    ), Coef('Var'  , 0.137357    ), Coef('Var'  , 0.128198    ), Coef('Var'  , 0.11984     ), Coef('Var'  , 0.114105    ), ], 
		[Coef('Var'  , 0.116187    ), Coef('Var'  , 0.117072    ), Coef('Var'  , 0.117581    ), Coef('Var'  , 0.129743    ), Coef('Var'  , 0.142109    ), Coef('Var'  , 0.131582    ), Coef('Var'  , 0.121332    ), Coef('Var'  , 0.118911    ), ], 
		[Coef('Var'  , 0.115009    ), Coef('Var'  , 0.116094    ), Coef('Var'  , 0.115685    ), Coef('Var'  , 0.117707    ), Coef('Var'  , 0.118733    ), Coef('Var'  , 0.115086    ), Coef('Var'  , 0.110246    ), Coef('Var'  , 0.113473    ), ], 
		[Coef('Var'  , 0.126828    ), Coef('Var'  , 0.133319    ), Coef('Var'  , 0.140293    ), Coef('Var'  , 0.136724    ), Coef('Var'  , 0.133904    ), Coef('Var'  , 0.126301    ), Coef('Var'  , 0.118753    ), Coef('Var'  , 0.122896    ), ], 
		[Coef('Var'  , 0.145457    ), Coef('Var'  , 0.149348    ), Coef('Var'  , 0.154281    ), Coef('Var'  , 0.139443    ), Coef('Var'  , 0.125265    ), Coef('Var'  , 0.128649    ), Coef('Var'  , 0.132066    ), Coef('Var'  , 0.138554    ), ], ])
	etat4.initMat[Chem([Sub('10')])] = FMat([
		[Coef('Var'  , 0.145676    ), Coef('Var'  , 0.160246    ), Coef('Var'  , 0.177906    ), Coef('Var'  , 0.163295    ), Coef('Var'  , 0.151455    ), Coef('Var'  , 0.140286    ), Coef('Var'  , 0.131388    ), Coef('Var'  , 0.137236    ), ], 
		[Coef('Var'  , 0.116322    ), Coef('Var'  , 0.114785    ), Coef('Var'  , 0.112497    ), Coef('Var'  , 0.0999418   ), Coef('Var'  , 0.0858293   ), Coef('Var'  , 0.0977679   ), Coef('Var'  , 0.107786    ), Coef('Var'  , 0.112611    ), ], 
		[Coef('Var'  , 0.128311    ), Coef('Var'  , 0.123979    ), Coef('Var'  , 0.118733    ), Coef('Var'  , 0.108286    ), Coef('Var'  , 0.0962764   ), Coef('Var'  , 0.111473    ), Coef('Var'  , 0.124957    ), Coef('Var'  , 0.127165    ), ], 
		[Coef('Var'  , 0.101989    ), Coef('Var'  , 0.0961709   ), Coef('Var'  , 0.0900426   ), Coef('Var'  , 0.0869241   ), Coef('Var'  , 0.0830225   ), Coef('Var'  , 0.0958583   ), Coef('Var'  , 0.10803     ), Coef('Var'  , 0.105105    ), ], 
		[Coef('Var'  , 0.110584    ), Coef('Var'  , 0.104423    ), Coef('Var'  , 0.0973869   ), Coef('Var'  , 0.0989819   ), Coef('Var'  , 0.0998547   ), Coef('Var'  , 0.108903    ), Coef('Var'  , 0.117581    ), Coef('Var'  , 0.114344    ), ], 
		[Coef('Var'  , 0.112985    ), Coef('Var'  , 0.108074    ), Coef('Var'  , 0.101154    ), Coef('Var'  , 0.105443    ), Coef('Var'  , 0.108186    ), Coef('Var'  , 0.112506    ), Coef('Var'  , 0.115685    ), Coef('Var'  , 0.115137    ), ], 
		[Coef('Var'  , 0.128977    ), Coef('Var'  , 0.128611    ), Coef('Var'  , 0.128501    ), Coef('Var'  , 0.151928    ), Coef('Var'  , 0.176567    ), Coef('Var'  , 0.15766     ), Coef('Var'  , 0.140293    ), Coef('Var'  , 0.134343    ), ], 
		[Coef('Var'  , 0.155155    ), Coef('Var'  , 0.163713    ), Coef('Var'  , 0.17378     ), Coef('Var'  , 0.1852      ), Coef('Var'  , 0.198809    ), Coef('Var'  , 0.175546    ), Coef('Var'  , 0.154281    ), Coef('Var'  , 0.154059    ), ], ])
	etat4.initMat[Chem([Sub('11')])] = FMat([
		[Coef('Var'  , 0.198639    ), Coef('Var'  , 0.172113    ), Coef('Var'  , 0.147099    ), Coef('Var'  , 0.119255    ), Coef('Var'  , 0.092315    ), Coef('Var'  , 0.0801087   ), Coef('Var'  , 0.0677674   ), Coef('Var'  , 0.0982973   ), Coef('Var'  , 0.12876     ), Coef('Var'  , 0.163319    ), ], 
		[Coef('Var'  , 0.245678    ), Coef('Var'  , 0.198391    ), Coef('Var'  , 0.151053    ), Coef('Var'  , 0.126992    ), Coef('Var'  , 0.102295    ), Coef('Var'  , 0.0982682   ), Coef('Var'  , 0.0934024   ), Coef('Var'  , 0.151833    ), Coef('Var'  , 0.209912    ), Coef('Var'  , 0.22778     ), ], 
		[Coef('Var'  , 0.203927    ), Coef('Var'  , 0.183922    ), Coef('Var'  , 0.164771    ), Coef('Var'  , 0.172325    ), Coef('Var'  , 0.180841    ), Coef('Var'  , 0.22379     ), Coef('Var'  , 0.267856    ), Coef('Var'  , 0.278665    ), Coef('Var'  , 0.290499    ), Coef('Var'  , 0.246786    ), ], 
		[Coef('Var'  , 0.101415    ), Coef('Var'  , 0.115531    ), Coef('Var'  , 0.130698    ), Coef('Var'  , 0.167935    ), Coef('Var'  , 0.20673     ), Coef('Var'  , 0.244316    ), Coef('Var'  , 0.283572    ), Coef('Var'  , 0.244324    ), Coef('Var'  , 0.206266    ), Coef('Var'  , 0.15343     ), ], 
		[Coef('Var'  , 0.066332    ), Coef('Var'  , 0.0902216   ), Coef('Var'  , 0.113908    ), Coef('Var'  , 0.139908    ), Coef('Var'  , 0.16632     ), Coef('Var'  , 0.15976     ), Coef('Var'  , 0.15403     ), Coef('Var'  , 0.118157    ), Coef('Var'  , 0.0827097   ), Coef('Var'  , 0.0745749   ), ], 
		[Coef('Var'  , 0.0454811   ), Coef('Var'  , 0.0669384   ), Coef('Var'  , 0.0867275   ), Coef('Var'  , 0.0864819   ), Coef('Var'  , 0.0848036   ), Coef('Var'  , 0.0668619   ), Coef('Var'  , 0.0481291   ), Coef('Var'  , 0.0365544   ), Coef('Var'  , 0.024324    ), Coef('Var'  , 0.0354365   ), ], 
		[Coef('Var'  , 0.0530001   ), Coef('Var'  , 0.0733427   ), Coef('Var'  , 0.0925336   ), Coef('Var'  , 0.0892935   ), Coef('Var'  , 0.0850297   ), Coef('Var'  , 0.0653635   ), Coef('Var'  , 0.0448653   ), Coef('Var'  , 0.0355577   ), Coef('Var'  , 0.0254329   ), Coef('Var'  , 0.0396773   ), ], 
		[Coef('Var'  , 0.085528    ), Coef('Var'  , 0.09954     ), Coef('Var'  , 0.113211    ), Coef('Var'  , 0.0978095   ), Coef('Var'  , 0.0816662   ), Coef('Var'  , 0.0615315   ), Coef('Var'  , 0.0403785   ), Coef('Var'  , 0.0366118   ), Coef('Var'  , 0.0320968   ), Coef('Var'  , 0.0589964   ), ], ])
	etat4.initMat[Chem([Sub('12')])] = FMat([
		[Coef('Const', 0.0625      ), Coef('Var'  , 0.130641    ), Coef('Var'  , 0.199246    ), Coef('Var'  , 0.224391    ), Coef('Const', 0.25        ), Coef('Const', 0.125       ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.00961977  ), Coef('Var'  , 0.0186269   ), Coef('Var'  , 0.00961977  ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0106552   ), Coef('Var'  , 0.0207222   ), Coef('Var'  , 0.0106552   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.00941267  ), Coef('Var'  , 0.018417    ), Coef('Var'  , 0.00941267  ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0114341   ), Coef('Var'  , 0.0226499   ), Coef('Var'  , 0.0114341   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0128194   ), Coef('Var'  , 0.0254459   ), Coef('Var'  , 0.0128194   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.5625      ), Coef('Var'  , 0.436395    ), Coef('Var'  , 0.31091     ), Coef('Var'  , 0.280145    ), Coef('Const', 0.25        ), Coef('Const', 0.375       ), ], 
		[Coef('Const', 0.375       ), Coef('Var'  , 0.379023    ), Coef('Var'  , 0.383982    ), Coef('Var'  , 0.441523    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), ], ])
	etat4.initMat[Chem([Sub('13')])] = FMat([
		[Coef('Const', 0.5625      ), Coef('Const', 0.375       ), Coef('Const', 0.25        ), Coef('Var'  , 0.274391    ), Coef('Var'  , 0.299246    ), Coef('Var'  , 0.430641    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.00961983  ), Coef('Var'  , 0.0186269   ), Coef('Var'  , 0.00961983  ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0106552   ), Coef('Var'  , 0.0207222   ), Coef('Var'  , 0.0106552   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.00941267  ), Coef('Var'  , 0.018417    ), Coef('Var'  , 0.00941267  ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0114341   ), Coef('Var'  , 0.0226499   ), Coef('Var'  , 0.0114341   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0128194   ), Coef('Var'  , 0.0254459   ), Coef('Var'  , 0.0128194   ), ], 
		[Coef('Const', 0.0625      ), Coef('Const', 0.125       ), Coef('Const', 0.25        ), Coef('Var'  , 0.230145    ), Coef('Var'  , 0.21091     ), Coef('Var'  , 0.136395    ), ], 
		[Coef('Const', 0.375       ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.441523    ), Coef('Var'  , 0.383982    ), Coef('Var'  , 0.379023    ), ], ])
	etat4.initMat[Chem([Sub('14')])] = FMat([
		[Coef('Var'  , 0.190098    ), Coef('Var'  , 0.244006    ), Coef('Var'  , 0.299246    ), Coef('Var'  , 0.248782    ), Coef('Var'  , 0.199246    ), Coef('Var'  , 0.194006    ), ], 
		[Coef('Var'  , 0.0493259   ), Coef('Var'  , 0.0349053   ), Coef('Var'  , 0.0186269   ), Coef('Var'  , 0.0192396   ), Coef('Var'  , 0.0186269   ), Coef('Var'  , 0.0349053   ), ], 
		[Coef('Var'  , 0.0559194   ), Coef('Var'  , 0.0391953   ), Coef('Var'  , 0.0207222   ), Coef('Var'  , 0.0213105   ), Coef('Var'  , 0.0207222   ), Coef('Var'  , 0.0391953   ), ], 
		[Coef('Var'  , 0.0510527   ), Coef('Var'  , 0.0352909   ), Coef('Var'  , 0.018417    ), Coef('Var'  , 0.0188253   ), Coef('Var'  , 0.018417    ), Coef('Var'  , 0.0352909   ), ], 
		[Coef('Var'  , 0.0658802   ), Coef('Var'  , 0.0444985   ), Coef('Var'  , 0.0226499   ), Coef('Var'  , 0.0228682   ), Coef('Var'  , 0.0226499   ), Coef('Var'  , 0.0444985   ), ], 
		[Coef('Var'  , 0.0744168   ), Coef('Var'  , 0.0501723   ), Coef('Var'  , 0.0254459   ), Coef('Var'  , 0.0256388   ), Coef('Var'  , 0.0254459   ), Coef('Var'  , 0.0501723   ), ], 
		[Coef('Var'  , 0.226827    ), Coef('Var'  , 0.217942    ), Coef('Var'  , 0.21091     ), Coef('Var'  , 0.26029     ), Coef('Var'  , 0.31091     ), Coef('Var'  , 0.267942    ), ], 
		[Coef('Var'  , 0.28648     ), Coef('Var'  , 0.33399     ), Coef('Var'  , 0.383982    ), Coef('Var'  , 0.383046    ), Coef('Var'  , 0.383982    ), Coef('Var'  , 0.33399     ), ], ])
	etat4.initMat[Chem([Sub('15')])] = FMat([
		[Coef('Const', 0           ), Coef('Var'  , 0.033973    ), Coef('Var'  , 0.0677674   ), Coef('Var'  , 0.0584406   ), Coef('Var'  , 0.0486784   ), Coef('Var'  , 0.0244677   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0468599   ), Coef('Var'  , 0.0934024   ), Coef('Var'  , 0.0760551   ), Coef('Var'  , 0.0579175   ), Coef('Var'  , 0.0291954   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.444444    ), Coef('Var'  , 0.355855    ), Coef('Var'  , 0.267856    ), Coef('Var'  , 0.214123    ), Coef('Var'  , 0.161416    ), Coef('Var'  , 0.136046    ), Coef('Const', 0.111111    ), Coef('Const', 0.222222    ), ], 
		[Coef('Const', 0.444444    ), Coef('Var'  , 0.363625    ), Coef('Var'  , 0.283572    ), Coef('Var'  , 0.283379    ), Coef('Var'  , 0.284677    ), Coef('Var'  , 0.364198    ), Coef('Const', 0.444444    ), Coef('Const', 0.555556    ), ], 
		[Coef('Const', 0.111111    ), Coef('Var'  , 0.132383    ), Coef('Var'  , 0.15403     ), Coef('Var'  , 0.206479    ), Coef('Var'  , 0.259787    ), Coef('Var'  , 0.351874    ), Coef('Const', 0.444444    ), Coef('Const', 0.222222    ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0242182   ), Coef('Var'  , 0.0481291   ), Coef('Var'  , 0.0643044   ), Coef('Var'  , 0.0799852   ), Coef('Var'  , 0.0400864   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0226466   ), Coef('Var'  , 0.0448653   ), Coef('Var'  , 0.0551539   ), Coef('Var'  , 0.0647615   ), Coef('Var'  , 0.0325074   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0204388   ), Coef('Var'  , 0.0403785   ), Coef('Var'  , 0.0420645   ), Coef('Var'  , 0.0427764   ), Coef('Var'  , 0.0216258   ), Coef('Const', 0           ), Coef('Const', 0           ), ], ])
	etat4.initMat[Chem([Sub('16')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.016352    ), Coef('Var'  , 0.0325614   ), Coef('Var'  , 0.0163519   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0157558   ), Coef('Var'  , 0.0309275   ), Coef('Var'  , 0.0157557   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.111111    ), Coef('Var'  , 0.100662    ), Coef('Var'  , 0.0901274   ), Coef('Var'  , 0.0451061   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.333333    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.327772    ), Coef('Var'  , 0.211361    ), Coef('Var'  , 0.105549    ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 1           ), Coef('Const', 0.666667    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.361627    ), Coef('Var'  , 0.279196    ), Coef('Var'  , 0.264405    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0923601   ), Coef('Var'  , 0.184768    ), Coef('Var'  , 0.34236     ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0632191   ), Coef('Var'  , 0.126674    ), Coef('Var'  , 0.188219    ), Coef('Const', 0.25        ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0222529   ), Coef('Var'  , 0.0443848   ), Coef('Var'  , 0.0222529   ), Coef('Const', 0           ), Coef('Const', 0           ), ], ])
	
	
	
	etat5.bords   = {Bord('0'): etat19, Bord('1'): etat19, Bord('2'): etat19, Bord('3'): etat19, }
	etat5.permuts = {}
	etat5.interns = {Intern('_'): etat5, }
	etat5.subs    = {Sub('0'): etat1, Sub('1'): etat2, Sub('2'): etat3, Sub('3'): etat4, Sub('4'): etat6, Sub('5'): etat7, Sub('6'): etat8, Sub('7'): etat9, Sub('G', True): Etat.etatPoint, Sub('8'): etat10, Sub('9'): etat11, Sub('10'): etat12, Sub('11'): etat13, Sub('12'): etat14, Sub('13'): etat15, Sub('14'): etat16, Sub('15'): etat17, Sub('16'): etat18, }
	
	etat5.buildIntern()
	
	
	etat5.eqs = [
		(Chem([Bord('0'), Sub('1'), Permut('0'), ])	,	Chem([Sub('7'), Bord('0'), ])),
		(Chem([Bord('1'), Sub('0'), Permut('0'), ])	,	Chem([Sub('7'), Bord('3'), ])),
		(Chem([Bord('1'), Sub('1'), Permut('0'), ])	,	Chem([Sub('8'), Bord('0'), ])),
		(Chem([Bord('2'), Sub('0'), Permut('0'), ])	,	Chem([Sub('8'), Bord('3'), ])),
		(Chem([Bord('3'), Sub('1'), Permut('0'), ])	,	Chem([Sub('9'), Bord('0'), ])),
		(Chem([Bord('0'), Sub('0'), Permut('0'), ])	,	Chem([Sub('9'), Bord('3'), ])),
		(Chem([Bord('2'), Sub('1'), Permut('0'), ])	,	Chem([Sub('10'), Bord('0'), ])),
		(Chem([Bord('3'), Sub('0'), Permut('0'), ])	,	Chem([Sub('10'), Bord('3'), ])),
		(Chem([Sub('0'), Bord('0'), Bord('1'), ])	,	Chem([Sub('11'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('1'), Bord('1'), ])	,	Chem([Sub('15'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('2'), Bord('1'), ])	,	Chem([Sub('3'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('3'), Bord('1'), ])	,	Chem([Sub('1'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('0'), Bord('1'), ])	,	Chem([Sub('11'), Bord('4'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('2'), Bord('1'), ])	,	Chem([Sub('3'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('3'), Bord('1'), ])	,	Chem([Sub('13'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('4'), Bord('1'), ])	,	Chem([Sub('8'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('0'), Bord('1'), ])	,	Chem([Sub('11'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('1'), Bord('1'), ])	,	Chem([Sub('9'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('2'), Bord('1'), ])	,	Chem([Sub('6'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('3'), Bord('1'), ])	,	Chem([Sub('16'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('4'), Bord('1'), ])	,	Chem([Sub('15'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('3'), Bord('1'), Bord('1'), ])	,	Chem([Sub('16'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('3'), Bord('2'), Bord('1'), ])	,	Chem([Sub('5'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('4'), Bord('0'), Bord('1'), ])	,	Chem([Sub('14'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('4'), Bord('1'), Bord('1'), ])	,	Chem([Sub('6'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('4'), Bord('2'), Bord('1'), ])	,	Chem([Sub('10'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('5'), Bord('0'), Bord('1'), ])	,	Chem([Sub('6'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('5'), Bord('1'), Bord('1'), ])	,	Chem([Sub('12'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('5'), Bord('3'), Bord('1'), ])	,	Chem([Sub('16'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('7'), Bord('0'), Bord('1'), ])	,	Chem([Sub('9'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('7'), Bord('1'), Bord('1'), ])	,	Chem([Sub('11'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('7'), Bord('2'), Bord('1'), ])	,	Chem([Sub('8'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('8'), Bord('2'), Bord('1'), ])	,	Chem([Sub('10'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('9'), Bord('0'), Bord('1'), ])	,	Chem([Sub('10'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('11'), Bord('2'), Bord('1'), ])	,	Chem([Sub('15'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('12'), Bord('0'), Bord('1'), ])	,	Chem([Sub('14'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('12'), Bord('1'), Bord('1'), ])	,	Chem([Sub('13'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('13'), Bord('1'), Bord('1'), ])	,	Chem([Sub('14'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('15'), Bord('2'), Bord('1'), ])	,	Chem([Sub('16'), Bord('0'), Bord('1'), ])),
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
		[Coef('Var'  , 0.114042    ), Coef('Var'  , 0.116162    ), Coef('Var'  , 0.118142    ), Coef('Var'  , 0.121647    ), Coef('Var'  , 0.125114    ), Coef('Var'  , 0.122772    ), Coef('Var'  , 0.12029     ), Coef('Var'  , 0.117288    ), ], 
		[Coef('Var'  , 0.131624    ), Coef('Var'  , 0.135314    ), Coef('Var'  , 0.138874    ), Coef('Var'  , 0.139574    ), Coef('Var'  , 0.140333    ), Coef('Var'  , 0.13606     ), Coef('Var'  , 0.131685    ), Coef('Var'  , 0.1318      ), ], 
		[Coef('Var'  , 0.131516    ), Coef('Var'  , 0.131938    ), Coef('Var'  , 0.132919    ), Coef('Var'  , 0.128998    ), Coef('Var'  , 0.125917    ), Coef('Var'  , 0.124704    ), Coef('Var'  , 0.124227    ), Coef('Var'  , 0.127645    ), ], 
		[Coef('Var'  , 0.148424    ), Coef('Var'  , 0.147441    ), Coef('Var'  , 0.147604    ), Coef('Var'  , 0.142235    ), Coef('Var'  , 0.137722    ), Coef('Var'  , 0.137845    ), Coef('Var'  , 0.13862     ), Coef('Var'  , 0.14305     ), ], 
		[Coef('Var'  , 0.120778    ), Coef('Var'  , 0.119132    ), Coef('Var'  , 0.11831     ), Coef('Var'  , 0.114653    ), Coef('Var'  , 0.111373    ), Coef('Var'  , 0.112501    ), Coef('Var'  , 0.114139    ), Coef('Var'  , 0.11698     ), ], 
		[Coef('Var'  , 0.12491     ), Coef('Var'  , 0.121311    ), Coef('Var'  , 0.117253    ), Coef('Var'  , 0.11674     ), Coef('Var'  , 0.115693    ), Coef('Var'  , 0.120549    ), Coef('Var'  , 0.124904    ), Coef('Var'  , 0.12512     ), ], 
		[Coef('Var'  , 0.129727    ), Coef('Var'  , 0.129232    ), Coef('Var'  , 0.127348    ), Coef('Var'  , 0.130918    ), Coef('Var'  , 0.13315     ), Coef('Var'  , 0.135126    ), Coef('Var'  , 0.136016    ), Coef('Var'  , 0.13344     ), ], 
		[Coef('Var'  , 0.0989786   ), Coef('Var'  , 0.0994703   ), Coef('Var'  , 0.0995496   ), Coef('Var'  , 0.105234    ), Coef('Var'  , 0.110698    ), Coef('Var'  , 0.110442    ), Coef('Var'  , 0.11012     ), Coef('Var'  , 0.104678    ), ], ])
	etat5.initMat[Chem([Sub('1')])] = FMat([
		[Coef('Var'  , 0.0503878   ), Coef('Var'  , 0.0761995   ), Coef('Var'  , 0.101899    ), Coef('Var'  , 0.108048    ), Coef('Var'  , 0.114042    ), Coef('Var'  , 0.114455    ), Coef('Var'  , 0.114591    ), Coef('Var'  , 0.1069      ), Coef('Var'  , 0.0988669   ), Coef('Var'  , 0.0747552   ), ], 
		[Coef('Var'  , 0.0576356   ), Coef('Var'  , 0.0952049   ), Coef('Var'  , 0.132625    ), Coef('Var'  , 0.132213    ), Coef('Var'  , 0.131624    ), Coef('Var'  , 0.126908    ), Coef('Var'  , 0.121789    ), Coef('Var'  , 0.109512    ), Coef('Var'  , 0.0966044   ), Coef('Var'  , 0.0773636   ), ], 
		[Coef('Var'  , 0.129992    ), Coef('Var'  , 0.138724    ), Coef('Var'  , 0.147507    ), Coef('Var'  , 0.13934     ), Coef('Var'  , 0.131516    ), Coef('Var'  , 0.127527    ), Coef('Var'  , 0.123735    ), Coef('Var'  , 0.122797    ), Coef('Var'  , 0.121453    ), Coef('Var'  , 0.125977    ), ], 
		[Coef('Var'  , 0.20435     ), Coef('Var'  , 0.188661    ), Coef('Var'  , 0.173839    ), Coef('Var'  , 0.16056     ), Coef('Var'  , 0.148424    ), Coef('Var'  , 0.143744    ), Coef('Var'  , 0.140045    ), Coef('Var'  , 0.143094    ), Coef('Var'  , 0.146888    ), Coef('Var'  , 0.17528     ), ], 
		[Coef('Var'  , 0.192833    ), Coef('Var'  , 0.164558    ), Coef('Var'  , 0.13699     ), Coef('Var'  , 0.128412    ), Coef('Var'  , 0.120778    ), Coef('Var'  , 0.119586    ), Coef('Var'  , 0.119489    ), Coef('Var'  , 0.128004    ), Coef('Var'  , 0.137556    ), Coef('Var'  , 0.164799    ), ], 
		[Coef('Var'  , 0.193805    ), Coef('Var'  , 0.157872    ), Coef('Var'  , 0.121862    ), Coef('Var'  , 0.123559    ), Coef('Var'  , 0.12491     ), Coef('Var'  , 0.129265    ), Coef('Var'  , 0.133348    ), Coef('Var'  , 0.143571    ), Coef('Var'  , 0.154056    ), Coef('Var'  , 0.17373     ), ], 
		[Coef('Var'  , 0.125399    ), Coef('Var'  , 0.118799    ), Coef('Var'  , 0.111403    ), Coef('Var'  , 0.121194    ), Coef('Var'  , 0.129727    ), Coef('Var'  , 0.133817    ), Coef('Var'  , 0.136936    ), Coef('Var'  , 0.137712    ), Coef('Var'  , 0.138238    ), Coef('Var'  , 0.131876    ), ], 
		[Coef('Var'  , 0.0455981   ), Coef('Var'  , 0.0599818   ), Coef('Var'  , 0.0738748   ), Coef('Var'  , 0.0866735   ), Coef('Var'  , 0.0989786   ), Coef('Var'  , 0.104696    ), Coef('Var'  , 0.110066    ), Coef('Var'  , 0.108411    ), Coef('Var'  , 0.106336    ), Coef('Var'  , 0.0762194   ), ], ])
	etat5.initMat[Chem([Sub('2')])] = FMat([
		[Coef('Var'  , 0.135897    ), Coef('Var'  , 0.141354    ), Coef('Var'  , 0.147178    ), Coef('Var'  , 0.172891    ), Coef('Var'  , 0.198954    ), Coef('Var'  , 0.174378    ), Coef('Var'  , 0.150122    ), Coef('Var'  , 0.143027    ), Coef('Var'  , 0.136239    ), Coef('Var'  , 0.135917    ), ], 
		[Coef('Var'  , 0.151089    ), Coef('Var'  , 0.163391    ), Coef('Var'  , 0.176246    ), Coef('Var'  , 0.189755    ), Coef('Var'  , 0.203721    ), Coef('Var'  , 0.171888    ), Coef('Var'  , 0.140379    ), Coef('Var'  , 0.139848    ), Coef('Var'  , 0.139662    ), Coef('Var'  , 0.145141    ), ], 
		[Coef('Var'  , 0.126882    ), Coef('Var'  , 0.135037    ), Coef('Var'  , 0.144151    ), Coef('Var'  , 0.134756    ), Coef('Var'  , 0.125888    ), Coef('Var'  , 0.118215    ), Coef('Var'  , 0.110578    ), Coef('Var'  , 0.113892    ), Coef('Var'  , 0.117465    ), Coef('Var'  , 0.121738    ), ], 
		[Coef('Var'  , 0.131112    ), Coef('Var'  , 0.131423    ), Coef('Var'  , 0.131585    ), Coef('Var'  , 0.0949786   ), Coef('Var'  , 0.0581037   ), Coef('Var'  , 0.0785336   ), Coef('Var'  , 0.0978198   ), Coef('Var'  , 0.1112      ), Coef('Var'  , 0.123129    ), Coef('Var'  , 0.127497    ), ], 
		[Coef('Var'  , 0.103598    ), Coef('Var'  , 0.0994861   ), Coef('Var'  , 0.094906    ), Coef('Var'  , 0.0709288   ), Coef('Var'  , 0.0466375   ), Coef('Var'  , 0.0686467   ), Coef('Var'  , 0.0904082   ), Coef('Var'  , 0.0966232   ), Coef('Var'  , 0.102498    ), Coef('Var'  , 0.103294    ), ], 
		[Coef('Var'  , 0.10202     ), Coef('Var'  , 0.089252    ), Coef('Var'  , 0.0759882   ), Coef('Var'  , 0.0611039   ), Coef('Var'  , 0.0459432   ), Coef('Var'  , 0.0766456   ), Coef('Var'  , 0.10752     ), Coef('Var'  , 0.109625    ), Coef('Var'  , 0.111845    ), Coef('Var'  , 0.107103    ), ], 
		[Coef('Var'  , 0.128863    ), Coef('Var'  , 0.120319    ), Coef('Var'  , 0.110907    ), Coef('Var'  , 0.118903    ), Coef('Var'  , 0.126346    ), Coef('Var'  , 0.13487     ), Coef('Var'  , 0.143482    ), Coef('Var'  , 0.140438    ), Coef('Var'  , 0.137484    ), Coef('Var'  , 0.133424    ), ], 
		[Coef('Var'  , 0.120539    ), Coef('Var'  , 0.119739    ), Coef('Var'  , 0.119037    ), Coef('Var'  , 0.156683    ), Coef('Var'  , 0.194407    ), Coef('Var'  , 0.176823    ), Coef('Var'  , 0.159692    ), Coef('Var'  , 0.145346    ), Coef('Var'  , 0.131678    ), Coef('Var'  , 0.125887    ), ], ])
	etat5.initMat[Chem([Sub('3')])] = FMat([
		[Coef('Var'  , 0.114591    ), Coef('Var'  , 0.117583    ), Coef('Var'  , 0.12029     ), Coef('Var'  , 0.123296    ), Coef('Var'  , 0.126136    ), Coef('Var'  , 0.124847    ), Coef('Var'  , 0.123464    ), Coef('Var'  , 0.119135    ), ], 
		[Coef('Var'  , 0.121789    ), Coef('Var'  , 0.12694     ), Coef('Var'  , 0.131685    ), Coef('Var'  , 0.131677    ), Coef('Var'  , 0.131474    ), Coef('Var'  , 0.128053    ), Coef('Var'  , 0.124422    ), Coef('Var'  , 0.123316    ), ], 
		[Coef('Var'  , 0.123735    ), Coef('Var'  , 0.123848    ), Coef('Var'  , 0.124227    ), Coef('Var'  , 0.121219    ), Coef('Var'  , 0.118758    ), Coef('Var'  , 0.118159    ), Coef('Var'  , 0.117881    ), Coef('Var'  , 0.120788    ), ], 
		[Coef('Var'  , 0.140045    ), Coef('Var'  , 0.138965    ), Coef('Var'  , 0.13862     ), Coef('Var'  , 0.135266    ), Coef('Var'  , 0.132069    ), Coef('Var'  , 0.131381    ), Coef('Var'  , 0.130328    ), Coef('Var'  , 0.13508     ), ], 
		[Coef('Var'  , 0.119489    ), Coef('Var'  , 0.116331    ), Coef('Var'  , 0.114139    ), Coef('Var'  , 0.111515    ), Coef('Var'  , 0.109442    ), Coef('Var'  , 0.110232    ), Coef('Var'  , 0.111416    ), Coef('Var'  , 0.115048    ), ], 
		[Coef('Var'  , 0.133348    ), Coef('Var'  , 0.129274    ), Coef('Var'  , 0.124904    ), Coef('Var'  , 0.124247    ), Coef('Var'  , 0.123164    ), Coef('Var'  , 0.126134    ), Coef('Var'  , 0.12883     ), Coef('Var'  , 0.131161    ), ], 
		[Coef('Var'  , 0.136936    ), Coef('Var'  , 0.13688     ), Coef('Var'  , 0.136016    ), Coef('Var'  , 0.137675    ), Coef('Var'  , 0.138675    ), Coef('Var'  , 0.139523    ), Coef('Var'  , 0.140186    ), Coef('Var'  , 0.138728    ), ], 
		[Coef('Var'  , 0.110066    ), Coef('Var'  , 0.110178    ), Coef('Var'  , 0.11012     ), Coef('Var'  , 0.115105    ), Coef('Var'  , 0.120282    ), Coef('Var'  , 0.121672    ), Coef('Var'  , 0.123473    ), Coef('Var'  , 0.116745    ), ], ])
	etat5.initMat[Chem([Sub('4')])] = FMat([
		[Coef('Var'  , 0.126709    ), Coef('Var'  , 0.125157    ), Coef('Var'  , 0.123541    ), Coef('Var'  , 0.128427    ), Coef('Var'  , 0.133324    ), Coef('Var'  , 0.129976    ), ], 
		[Coef('Var'  , 0.0468989   ), Coef('Var'  , 0.0674072   ), Coef('Var'  , 0.087533    ), Coef('Var'  , 0.0934286   ), Coef('Var'  , 0.098993    ), Coef('Var'  , 0.0730146   ), ], 
		[Coef('Var'  , 0.0462248   ), Coef('Var'  , 0.0691927   ), Coef('Var'  , 0.091207    ), Coef('Var'  , 0.091176    ), Coef('Var'  , 0.0901183   ), Coef('Var'  , 0.0685394   ), ], 
		[Coef('Var'  , 0.0472744   ), Coef('Var'  , 0.0713512   ), Coef('Var'  , 0.0945871   ), Coef('Var'  , 0.0928922   ), Coef('Var'  , 0.0899332   ), Coef('Var'  , 0.0692502   ), ], 
		[Coef('Var'  , 0.118002    ), Coef('Var'  , 0.116652    ), Coef('Var'  , 0.115506    ), Coef('Var'  , 0.111168    ), Coef('Var'  , 0.106998    ), Coef('Var'  , 0.112476    ), ], 
		[Coef('Var'  , 0.200302    ), Coef('Var'  , 0.1788      ), Coef('Var'  , 0.158372    ), Coef('Var'  , 0.152124    ), Coef('Var'  , 0.147058    ), Coef('Var'  , 0.173229    ), ], 
		[Coef('Var'  , 0.206722    ), Coef('Var'  , 0.185736    ), Coef('Var'  , 0.16559     ), Coef('Var'  , 0.164639    ), Coef('Var'  , 0.164644    ), Coef('Var'  , 0.185314    ), ], 
		[Coef('Var'  , 0.207868    ), Coef('Var'  , 0.185704    ), Coef('Var'  , 0.163663    ), Coef('Var'  , 0.166145    ), Coef('Var'  , 0.168931    ), Coef('Var'  , 0.188201    ), ], ])
	etat5.initMat[Chem([Sub('5')])] = FMat([
		[Coef('Var'  , 0.12976     ), Coef('Var'  , 0.131668    ), Coef('Var'  , 0.13373     ), Coef('Var'  , 0.128212    ), Coef('Var'  , 0.122756    ), Coef('Var'  , 0.123158    ), Coef('Var'  , 0.123464    ), Coef('Var'  , 0.126614    ), ], 
		[Coef('Var'  , 0.129005    ), Coef('Var'  , 0.124773    ), Coef('Var'  , 0.120554    ), Coef('Var'  , 0.117215    ), Coef('Var'  , 0.113594    ), Coef('Var'  , 0.119227    ), Coef('Var'  , 0.124422    ), Coef('Var'  , 0.126785    ), ], 
		[Coef('Var'  , 0.115175    ), Coef('Var'  , 0.111682    ), Coef('Var'  , 0.108111    ), Coef('Var'  , 0.111431    ), Coef('Var'  , 0.114141    ), Coef('Var'  , 0.116189    ), Coef('Var'  , 0.117881    ), Coef('Var'  , 0.11644     ), ], 
		[Coef('Var'  , 0.125674    ), Coef('Var'  , 0.119022    ), Coef('Var'  , 0.110968    ), Coef('Var'  , 0.116792    ), Coef('Var'  , 0.121545    ), Coef('Var'  , 0.126144    ), Coef('Var'  , 0.130328    ), Coef('Var'  , 0.128374    ), ], 
		[Coef('Var'  , 0.106801    ), Coef('Var'  , 0.105502    ), Coef('Var'  , 0.104227    ), Coef('Var'  , 0.108442    ), Coef('Var'  , 0.112873    ), Coef('Var'  , 0.11191     ), Coef('Var'  , 0.111416    ), Coef('Var'  , 0.108969    ), ], 
		[Coef('Var'  , 0.122965    ), Coef('Var'  , 0.12511     ), Coef('Var'  , 0.127455    ), Coef('Var'  , 0.131108    ), Coef('Var'  , 0.135357    ), Coef('Var'  , 0.131965    ), Coef('Var'  , 0.12883     ), Coef('Var'  , 0.125967    ), ], 
		[Coef('Var'  , 0.140845    ), Coef('Var'  , 0.143945    ), Coef('Var'  , 0.147405    ), Coef('Var'  , 0.145408    ), Coef('Var'  , 0.144066    ), Coef('Var'  , 0.14196     ), Coef('Var'  , 0.140186    ), Coef('Var'  , 0.140497    ), ], 
		[Coef('Var'  , 0.129775    ), Coef('Var'  , 0.138298    ), Coef('Var'  , 0.14755     ), Coef('Var'  , 0.141392    ), Coef('Var'  , 0.135668    ), Coef('Var'  , 0.129447    ), Coef('Var'  , 0.123473    ), Coef('Var'  , 0.126353    ), ], ])
	etat5.initMat[Chem([Sub('6')])] = FMat([
		[Coef('Var'  , 0.150122    ), Coef('Var'  , 0.141599    ), Coef('Var'  , 0.133324    ), Coef('Var'  , 0.133436    ), Coef('Var'  , 0.13373     ), Coef('Var'  , 0.141788    ), ], 
		[Coef('Var'  , 0.140379    ), Coef('Var'  , 0.119634    ), Coef('Var'  , 0.098993    ), Coef('Var'  , 0.109797    ), Coef('Var'  , 0.120554    ), Coef('Var'  , 0.130395    ), ], 
		[Coef('Var'  , 0.110578    ), Coef('Var'  , 0.100586    ), Coef('Var'  , 0.0901183   ), Coef('Var'  , 0.0994269   ), Coef('Var'  , 0.108111    ), Coef('Var'  , 0.10949     ), ], 
		[Coef('Var'  , 0.0978198   ), Coef('Var'  , 0.094736    ), Coef('Var'  , 0.0899332   ), Coef('Var'  , 0.101294    ), Coef('Var'  , 0.110968    ), Coef('Var'  , 0.105239    ), ], 
		[Coef('Var'  , 0.0904082   ), Coef('Var'  , 0.0987626   ), Coef('Var'  , 0.106998    ), Coef('Var'  , 0.105607    ), Coef('Var'  , 0.104227    ), Coef('Var'  , 0.0973784   ), ], 
		[Coef('Var'  , 0.10752     ), Coef('Var'  , 0.126935    ), Coef('Var'  , 0.147058    ), Coef('Var'  , 0.136871    ), Coef('Var'  , 0.127455    ), Coef('Var'  , 0.117252    ), ], 
		[Coef('Var'  , 0.143482    ), Coef('Var'  , 0.153758    ), Coef('Var'  , 0.164644    ), Coef('Var'  , 0.155655    ), Coef('Var'  , 0.147405    ), Coef('Var'  , 0.145197    ), ], 
		[Coef('Var'  , 0.159692    ), Coef('Var'  , 0.163989    ), Coef('Var'  , 0.168931    ), Coef('Var'  , 0.157913    ), Coef('Var'  , 0.14755     ), Coef('Var'  , 0.153261    ), ], ])
	etat5.initMat[Chem([Sub('7')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.187255    ), Coef('Var'  , 0.124587    ), Coef('Var'  , 0.0622552   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.350925    ), Coef('Var'  , 0.201958    ), Coef('Var'  , 0.100925    ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.223637    ), Coef('Var'  , 0.197444    ), Coef('Var'  , 0.223637    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.100325    ), Coef('Var'  , 0.200844    ), Coef('Var'  , 0.350325    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0601199   ), Coef('Var'  , 0.120301    ), Coef('Var'  , 0.18512     ), Coef('Const', 0.25        ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0249733   ), Coef('Var'  , 0.0498135   ), Coef('Var'  , 0.0249733   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0284339   ), Coef('Var'  , 0.056517    ), Coef('Var'  , 0.0284339   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0243304   ), Coef('Var'  , 0.0485352   ), Coef('Var'  , 0.0243304   ), Coef('Const', 0           ), Coef('Const', 0           ), ], ])
	etat5.initMat[Chem([Sub('G')])] = FMat([
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], ])
	etat5.initMat[Chem([Sub('8')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0252309   ), Coef('Var'  , 0.0503878   ), Coef('Var'  , 0.0252309   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0288758   ), Coef('Var'  , 0.0576356   ), Coef('Var'  , 0.0288758   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.190046    ), Coef('Var'  , 0.129992    ), Coef('Var'  , 0.0650455   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.352016    ), Coef('Var'  , 0.20435     ), Coef('Var'  , 0.102016    ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.221264    ), Coef('Var'  , 0.192833    ), Coef('Var'  , 0.221264    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0968685   ), Coef('Var'  , 0.193805    ), Coef('Var'  , 0.346868    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0627927   ), Coef('Var'  , 0.125399    ), Coef('Var'  , 0.187793    ), Coef('Const', 0.25        ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0229065   ), Coef('Var'  , 0.0455981   ), Coef('Var'  , 0.0229065   ), Coef('Const', 0           ), Coef('Const', 0           ), ], ])
	etat5.initMat[Chem([Sub('9')])] = FMat([
		[Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.224402    ), Coef('Var'  , 0.198954    ), Coef('Var'  , 0.224402    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.101773    ), Coef('Var'  , 0.203721    ), Coef('Var'  , 0.351773    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.06289     ), Coef('Var'  , 0.125888    ), Coef('Var'  , 0.18789     ), Coef('Const', 0.25        ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0291931   ), Coef('Var'  , 0.0581037   ), Coef('Var'  , 0.0291931   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0233798   ), Coef('Var'  , 0.0466375   ), Coef('Var'  , 0.0233798   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0229876   ), Coef('Var'  , 0.0459432   ), Coef('Var'  , 0.0229876   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.18822     ), Coef('Var'  , 0.126346    ), Coef('Var'  , 0.0632204   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.347154    ), Coef('Var'  , 0.194407    ), Coef('Var'  , 0.0971543   ), Coef('Const', 0           ), Coef('Const', 0           ), ], ])
	etat5.initMat[Chem([Sub('10')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0633533   ), Coef('Var'  , 0.126709    ), Coef('Var'  , 0.188353    ), Coef('Const', 0.25        ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0234966   ), Coef('Var'  , 0.0468989   ), Coef('Var'  , 0.0234966   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.023278    ), Coef('Var'  , 0.0462248   ), Coef('Var'  , 0.023278    ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0238546   ), Coef('Var'  , 0.0472744   ), Coef('Var'  , 0.0238546   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.18398     ), Coef('Var'  , 0.118002    ), Coef('Var'  , 0.0589803   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.349952    ), Coef('Var'  , 0.200302    ), Coef('Var'  , 0.0999521   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.228205    ), Coef('Var'  , 0.206722    ), Coef('Var'  , 0.228205    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.10388     ), Coef('Var'  , 0.207868    ), Coef('Var'  , 0.35388     ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), ], ])
	etat5.initMat[Chem([Sub('11')])] = FMat([
		[Coef('Var'  , 0.101899    ), Coef('Var'  , 0.113224    ), Coef('Var'  , 0.124587    ), Coef('Var'  , 0.135744    ), Coef('Var'  , 0.147178    ), Coef('Var'  , 0.139074    ), Coef('Var'  , 0.131283    ), Coef('Var'  , 0.124667    ), Coef('Var'  , 0.118142    ), Coef('Var'  , 0.110051    ), ], 
		[Coef('Var'  , 0.132625    ), Coef('Var'  , 0.167254    ), Coef('Var'  , 0.201958    ), Coef('Var'  , 0.188908    ), Coef('Var'  , 0.176246    ), Coef('Var'  , 0.16343     ), Coef('Var'  , 0.151097    ), Coef('Var'  , 0.144878    ), Coef('Var'  , 0.138874    ), Coef('Var'  , 0.135759    ), ], 
		[Coef('Var'  , 0.147507    ), Coef('Var'  , 0.172316    ), Coef('Var'  , 0.197444    ), Coef('Var'  , 0.170504    ), Coef('Var'  , 0.144151    ), Coef('Var'  , 0.137089    ), Coef('Var'  , 0.13098     ), Coef('Var'  , 0.131499    ), Coef('Var'  , 0.132919    ), Coef('Var'  , 0.139954    ), ], 
		[Coef('Var'  , 0.173839    ), Coef('Var'  , 0.18697     ), Coef('Var'  , 0.200844    ), Coef('Var'  , 0.16611     ), Coef('Var'  , 0.131585    ), Coef('Var'  , 0.133846    ), Coef('Var'  , 0.136365    ), Coef('Var'  , 0.141586    ), Coef('Var'  , 0.147604    ), Coef('Var'  , 0.160171    ), ], 
		[Coef('Var'  , 0.13699     ), Coef('Var'  , 0.128414    ), Coef('Var'  , 0.120301    ), Coef('Var'  , 0.107669    ), Coef('Var'  , 0.094906    ), Coef('Var'  , 0.101215    ), Coef('Var'  , 0.107236    ), Coef('Var'  , 0.11268     ), Coef('Var'  , 0.11831     ), Coef('Var'  , 0.127308    ), ], 
		[Coef('Var'  , 0.121862    ), Coef('Var'  , 0.0859768   ), Coef('Var'  , 0.0498135   ), Coef('Var'  , 0.0630895   ), Coef('Var'  , 0.0759882   ), Coef('Var'  , 0.0900639   ), Coef('Var'  , 0.10359     ), Coef('Var'  , 0.110703    ), Coef('Var'  , 0.117253    ), Coef('Var'  , 0.119759    ), ], 
		[Coef('Var'  , 0.111403    ), Coef('Var'  , 0.08444     ), Coef('Var'  , 0.056517    ), Coef('Var'  , 0.0841168   ), Coef('Var'  , 0.110907    ), Coef('Var'  , 0.119433    ), Coef('Var'  , 0.126863    ), Coef('Var'  , 0.127794    ), Coef('Var'  , 0.127348    ), Coef('Var'  , 0.12005     ), ], 
		[Coef('Var'  , 0.0738748   ), Coef('Var'  , 0.0614057   ), Coef('Var'  , 0.0485352   ), Coef('Var'  , 0.0838591   ), Coef('Var'  , 0.119037    ), Coef('Var'  , 0.115849    ), Coef('Var'  , 0.112587    ), Coef('Var'  , 0.106192    ), Coef('Var'  , 0.0995496   ), Coef('Var'  , 0.0869474   ), ], ])
	etat5.initMat[Chem([Sub('12')])] = FMat([
		[Coef('Var'  , 0.122756    ), Coef('Var'  , 0.120989    ), Coef('Var'  , 0.119057    ), Coef('Var'  , 0.116757    ), Coef('Var'  , 0.114184    ), Coef('Var'  , 0.118567    ), ], 
		[Coef('Var'  , 0.113594    ), Coef('Var'  , 0.108228    ), Coef('Var'  , 0.102169    ), Coef('Var'  , 0.103523    ), Coef('Var'  , 0.104025    ), Coef('Var'  , 0.109166    ), ], 
		[Coef('Var'  , 0.114141    ), Coef('Var'  , 0.11262     ), Coef('Var'  , 0.110062    ), Coef('Var'  , 0.113655    ), Coef('Var'  , 0.116002    ), Coef('Var'  , 0.115565    ), ], 
		[Coef('Var'  , 0.121545    ), Coef('Var'  , 0.118921    ), Coef('Var'  , 0.115987    ), Coef('Var'  , 0.120977    ), Coef('Var'  , 0.12603     ), Coef('Var'  , 0.123843    ), ], 
		[Coef('Var'  , 0.112873    ), Coef('Var'  , 0.11475     ), Coef('Var'  , 0.117101    ), Coef('Var'  , 0.118909    ), Coef('Var'  , 0.121331    ), Coef('Var'  , 0.11682     ), ], 
		[Coef('Var'  , 0.135357    ), Coef('Var'  , 0.139654    ), Coef('Var'  , 0.144894    ), Coef('Var'  , 0.143986    ), Coef('Var'  , 0.144218    ), Coef('Var'  , 0.139361    ), ], 
		[Coef('Var'  , 0.144066    ), Coef('Var'  , 0.146054    ), Coef('Var'  , 0.148891    ), Coef('Var'  , 0.145833    ), Coef('Var'  , 0.143666    ), Coef('Var'  , 0.143501    ), ], 
		[Coef('Var'  , 0.135668    ), Coef('Var'  , 0.138783    ), Coef('Var'  , 0.14184     ), Coef('Var'  , 0.13636     ), Coef('Var'  , 0.130544    ), Coef('Var'  , 0.133177    ), ], ])
	etat5.initMat[Chem([Sub('13')])] = FMat([
		[Coef('Var'  , 0.0988669   ), Coef('Var'  , 0.106692    ), Coef('Var'  , 0.114184    ), Coef('Var'  , 0.114432    ), Coef('Var'  , 0.114362    ), Coef('Var'  , 0.106788    ), ], 
		[Coef('Var'  , 0.0966044   ), Coef('Var'  , 0.100718    ), Coef('Var'  , 0.104025    ), Coef('Var'  , 0.101863    ), Coef('Var'  , 0.0988233   ), Coef('Var'  , 0.0981206   ), ], 
		[Coef('Var'  , 0.121453    ), Coef('Var'  , 0.119232    ), Coef('Var'  , 0.116002    ), Coef('Var'  , 0.114406    ), Coef('Var'  , 0.111547    ), Coef('Var'  , 0.117037    ), ], 
		[Coef('Var'  , 0.146888    ), Coef('Var'  , 0.136214    ), Coef('Var'  , 0.12603     ), Coef('Var'  , 0.12328     ), Coef('Var'  , 0.120739    ), Coef('Var'  , 0.133595    ), ], 
		[Coef('Var'  , 0.137556    ), Coef('Var'  , 0.129025    ), Coef('Var'  , 0.121331    ), Coef('Var'  , 0.121256    ), Coef('Var'  , 0.121878    ), Coef('Var'  , 0.129302    ), ], 
		[Coef('Var'  , 0.154056    ), Coef('Var'  , 0.148708    ), Coef('Var'  , 0.144218    ), Coef('Var'  , 0.145836    ), Coef('Var'  , 0.148613    ), Coef('Var'  , 0.150851    ), ], 
		[Coef('Var'  , 0.138238    ), Coef('Var'  , 0.140723    ), Coef('Var'  , 0.143666    ), Coef('Var'  , 0.145352    ), Coef('Var'  , 0.147865    ), Coef('Var'  , 0.142795    ), ], 
		[Coef('Var'  , 0.106336    ), Coef('Var'  , 0.11869     ), Coef('Var'  , 0.130544    ), Coef('Var'  , 0.133575    ), Coef('Var'  , 0.136173    ), Coef('Var'  , 0.121512    ), ], ])
	etat5.initMat[Chem([Sub('14')])] = FMat([
		[Coef('Var'  , 0.123541    ), Coef('Var'  , 0.119067    ), Coef('Var'  , 0.114362    ), Coef('Var'  , 0.116853    ), Coef('Var'  , 0.119057    ), Coef('Var'  , 0.121393    ), ], 
		[Coef('Var'  , 0.087533    ), Coef('Var'  , 0.0935434   ), Coef('Var'  , 0.0988233   ), Coef('Var'  , 0.100925    ), Coef('Var'  , 0.102169    ), Coef('Var'  , 0.0952031   ), ], 
		[Coef('Var'  , 0.091207    ), Coef('Var'  , 0.102021    ), Coef('Var'  , 0.111547    ), Coef('Var'  , 0.111461    ), Coef('Var'  , 0.110062    ), Coef('Var'  , 0.101269    ), ], 
		[Coef('Var'  , 0.0945871   ), Coef('Var'  , 0.107827    ), Coef('Var'  , 0.120739    ), Coef('Var'  , 0.118359    ), Coef('Var'  , 0.115987    ), Coef('Var'  , 0.105524    ), ], 
		[Coef('Var'  , 0.115506    ), Coef('Var'  , 0.118439    ), Coef('Var'  , 0.121878    ), Coef('Var'  , 0.119186    ), Coef('Var'  , 0.117101    ), Coef('Var'  , 0.116091    ), ], 
		[Coef('Var'  , 0.158372    ), Coef('Var'  , 0.152837    ), Coef('Var'  , 0.148613    ), Coef('Var'  , 0.146129    ), Coef('Var'  , 0.144894    ), Coef('Var'  , 0.150987    ), ], 
		[Coef('Var'  , 0.16559     ), Coef('Var'  , 0.156243    ), Coef('Var'  , 0.147865    ), Coef('Var'  , 0.147905    ), Coef('Var'  , 0.148891    ), Coef('Var'  , 0.156724    ), ], 
		[Coef('Var'  , 0.163663    ), Coef('Var'  , 0.150023    ), Coef('Var'  , 0.136173    ), Coef('Var'  , 0.139182    ), Coef('Var'  , 0.14184     ), Coef('Var'  , 0.152807    ), ], ])
	etat5.initMat[Chem([Sub('15')])] = FMat([
		[Coef('Var'  , 0.125114    ), Coef('Var'  , 0.128149    ), Coef('Var'  , 0.131283    ), Coef('Var'  , 0.13345     ), Coef('Var'  , 0.135897    ), Coef('Var'  , 0.133173    ), Coef('Var'  , 0.130671    ), Coef('Var'  , 0.127873    ), ], 
		[Coef('Var'  , 0.140333    ), Coef('Var'  , 0.145592    ), Coef('Var'  , 0.151097    ), Coef('Var'  , 0.150856    ), Coef('Var'  , 0.151089    ), Coef('Var'  , 0.145467    ), Coef('Var'  , 0.140255    ), Coef('Var'  , 0.140203    ), ], 
		[Coef('Var'  , 0.125917    ), Coef('Var'  , 0.127945    ), Coef('Var'  , 0.13098     ), Coef('Var'  , 0.128394    ), Coef('Var'  , 0.126882    ), Coef('Var'  , 0.123373    ), Coef('Var'  , 0.120896    ), Coef('Var'  , 0.122925    ), ], 
		[Coef('Var'  , 0.137722    ), Coef('Var'  , 0.13677     ), Coef('Var'  , 0.136365    ), Coef('Var'  , 0.133698    ), Coef('Var'  , 0.131112    ), Coef('Var'  , 0.131525    ), Coef('Var'  , 0.131568    ), Coef('Var'  , 0.134597    ), ], 
		[Coef('Var'  , 0.111373    ), Coef('Var'  , 0.109304    ), Coef('Var'  , 0.107236    ), Coef('Var'  , 0.105603    ), Coef('Var'  , 0.103598    ), Coef('Var'  , 0.105535    ), Coef('Var'  , 0.107053    ), Coef('Var'  , 0.109237    ), ], 
		[Coef('Var'  , 0.115693    ), Coef('Var'  , 0.109933    ), Coef('Var'  , 0.10359     ), Coef('Var'  , 0.103083    ), Coef('Var'  , 0.10202     ), Coef('Var'  , 0.108161    ), Coef('Var'  , 0.113827    ), Coef('Var'  , 0.115011    ), ], 
		[Coef('Var'  , 0.13315     ), Coef('Var'  , 0.130625    ), Coef('Var'  , 0.126863    ), Coef('Var'  , 0.128386    ), Coef('Var'  , 0.128863    ), Coef('Var'  , 0.132532    ), Coef('Var'  , 0.135483    ), Coef('Var'  , 0.134771    ), ], 
		[Coef('Var'  , 0.110698    ), Coef('Var'  , 0.111682    ), Coef('Var'  , 0.112587    ), Coef('Var'  , 0.11653     ), Coef('Var'  , 0.120539    ), Coef('Var'  , 0.120233    ), Coef('Var'  , 0.120248    ), Coef('Var'  , 0.115385    ), ], ])
	etat5.initMat[Chem([Sub('16')])] = FMat([
		[Coef('Var'  , 0.126136    ), Coef('Var'  , 0.128396    ), Coef('Var'  , 0.130671    ), Coef('Var'  , 0.13336     ), Coef('Var'  , 0.136239    ), Coef('Var'  , 0.132907    ), Coef('Var'  , 0.12976     ), Coef('Var'  , 0.127943    ), ], 
		[Coef('Var'  , 0.131474    ), Coef('Var'  , 0.13582     ), Coef('Var'  , 0.140255    ), Coef('Var'  , 0.139791    ), Coef('Var'  , 0.139662    ), Coef('Var'  , 0.134226    ), Coef('Var'  , 0.129005    ), Coef('Var'  , 0.130255    ), ], 
		[Coef('Var'  , 0.118758    ), Coef('Var'  , 0.119439    ), Coef('Var'  , 0.120896    ), Coef('Var'  , 0.11877     ), Coef('Var'  , 0.117465    ), Coef('Var'  , 0.116084    ), Coef('Var'  , 0.115175    ), Coef('Var'  , 0.116753    ), ], 
		[Coef('Var'  , 0.132069    ), Coef('Var'  , 0.132018    ), Coef('Var'  , 0.131568    ), Coef('Var'  , 0.127748    ), Coef('Var'  , 0.123129    ), Coef('Var'  , 0.124984    ), Coef('Var'  , 0.125674    ), Coef('Var'  , 0.129254    ), ], 
		[Coef('Var'  , 0.109442    ), Coef('Var'  , 0.108251    ), Coef('Var'  , 0.107053    ), Coef('Var'  , 0.104954    ), Coef('Var'  , 0.102498    ), Coef('Var'  , 0.104747    ), Coef('Var'  , 0.106801    ), Coef('Var'  , 0.108043    ), ], 
		[Coef('Var'  , 0.123164    ), Coef('Var'  , 0.118709    ), Coef('Var'  , 0.113827    ), Coef('Var'  , 0.112993    ), Coef('Var'  , 0.111845    ), Coef('Var'  , 0.117483    ), Coef('Var'  , 0.122965    ), Coef('Var'  , 0.123199    ), ], 
		[Coef('Var'  , 0.138675    ), Coef('Var'  , 0.13732     ), Coef('Var'  , 0.135483    ), Coef('Var'  , 0.136684    ), Coef('Var'  , 0.137484    ), Coef('Var'  , 0.139186    ), Coef('Var'  , 0.140845    ), Coef('Var'  , 0.139822    ), ], 
		[Coef('Var'  , 0.120282    ), Coef('Var'  , 0.120048    ), Coef('Var'  , 0.120248    ), Coef('Var'  , 0.125701    ), Coef('Var'  , 0.131678    ), Coef('Var'  , 0.130383    ), Coef('Var'  , 0.129775    ), Coef('Var'  , 0.12473     ), ], ])
	
	
	
	etat6.bords   = {Bord('0'): etat22, Bord('1'): etat21, Bord('2'): etat21, }
	etat6.permuts = {}
	etat6.interns = {Intern('_'): etat6, }
	etat6.subs    = {Sub('0'): etat1, Sub('1'): etat2, Sub('2'): etat3, Sub('3'): etat4, Sub('4'): etat5, Sub('5'): etat7, Sub('6'): etat8, Sub('7'): etat9, Sub('G', True): Etat.etatPoint, Sub('8'): etat10, Sub('9'): etat11, Sub('10'): etat12, Sub('11'): etat13, Sub('12'): etat14, Sub('13'): etat15, Sub('14'): etat16, Sub('15'): etat17, Sub('16'): etat18, }
	
	etat6.buildIntern()
	
	
	etat6.eqs = [
		(Chem([Bord('0'), Sub('2'), Permut('0'), ])	,	Chem([Sub('1'), Bord('4'), ])),
		(Chem([Bord('2'), Sub('1'), Permut('0'), ])	,	Chem([Sub('2'), Bord('2'), ])),
		(Chem([Bord('1'), Sub('2'), Permut('0'), ])	,	Chem([Sub('5'), Bord('1'), ])),
		(Chem([Bord('2'), Sub('0'), Permut('0'), ])	,	Chem([Sub('6'), Bord('0'), ])),
		(Chem([Bord('1'), Sub('3'), Permut('0'), ])	,	Chem([Sub('6'), Bord('1'), ])),
		(Chem([Bord('0'), Sub('1'), Permut('0'), ])	,	Chem([Sub('8'), Bord('2'), ])),
		(Chem([Bord('2'), Sub('2'), Permut('0'), ])	,	Chem([Sub('9'), Bord('1'), ])),
		(Chem([Bord('0'), Sub('0'), Permut('0'), ])	,	Chem([Sub('10'), Bord('1'), ])),
		(Chem([Bord('2'), Sub('3'), Permut('0'), ])	,	Chem([Sub('10'), Bord('2'), ])),
		(Chem([Bord('1'), Sub('1'), Permut('0'), ])	,	Chem([Sub('12'), Bord('0'), ])),
		(Chem([Bord('0'), Sub('3'), Permut('0'), ])	,	Chem([Sub('13'), Bord('2'), ])),
		(Chem([Bord('0'), Sub('4'), Permut('0'), ])	,	Chem([Sub('14'), Bord('0'), ])),
		(Chem([Bord('1'), Sub('0'), Permut('0'), ])	,	Chem([Sub('14'), Bord('2'), ])),
		(Chem([Sub('0'), Bord('0'), Bord('1'), ])	,	Chem([Sub('11'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('1'), Bord('1'), ])	,	Chem([Sub('15'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('2'), Bord('1'), ])	,	Chem([Sub('3'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('3'), Bord('1'), ])	,	Chem([Sub('1'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('0'), Bord('1'), ])	,	Chem([Sub('11'), Bord('4'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('2'), Bord('1'), ])	,	Chem([Sub('3'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('3'), Bord('1'), ])	,	Chem([Sub('13'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('4'), Bord('1'), ])	,	Chem([Sub('8'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('0'), Bord('1'), ])	,	Chem([Sub('11'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('1'), Bord('1'), ])	,	Chem([Sub('9'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('2'), Bord('1'), ])	,	Chem([Sub('6'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('3'), Bord('1'), ])	,	Chem([Sub('16'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('4'), Bord('1'), ])	,	Chem([Sub('15'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('3'), Bord('1'), Bord('1'), ])	,	Chem([Sub('16'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('3'), Bord('2'), Bord('1'), ])	,	Chem([Sub('5'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('4'), Bord('0'), Bord('1'), ])	,	Chem([Sub('7'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('4'), Bord('1'), Bord('1'), ])	,	Chem([Sub('8'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('4'), Bord('2'), Bord('1'), ])	,	Chem([Sub('10'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('4'), Bord('3'), Bord('1'), ])	,	Chem([Sub('9'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('5'), Bord('0'), Bord('1'), ])	,	Chem([Sub('6'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('5'), Bord('1'), Bord('1'), ])	,	Chem([Sub('12'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('5'), Bord('3'), Bord('1'), ])	,	Chem([Sub('16'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('7'), Bord('0'), Bord('1'), ])	,	Chem([Sub('9'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('7'), Bord('1'), Bord('1'), ])	,	Chem([Sub('11'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('7'), Bord('2'), Bord('1'), ])	,	Chem([Sub('8'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('8'), Bord('2'), Bord('1'), ])	,	Chem([Sub('10'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('9'), Bord('0'), Bord('1'), ])	,	Chem([Sub('10'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('11'), Bord('2'), Bord('1'), ])	,	Chem([Sub('15'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('12'), Bord('0'), Bord('1'), ])	,	Chem([Sub('14'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('12'), Bord('1'), Bord('1'), ])	,	Chem([Sub('13'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('13'), Bord('1'), Bord('1'), ])	,	Chem([Sub('14'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('15'), Bord('2'), Bord('1'), ])	,	Chem([Sub('16'), Bord('0'), Bord('1'), ])),
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
		[Coef('Var'  , 0.190016    ), Coef('Var'  , 0.194016    ), Coef('Var'  , 0.199321    ), Coef('Var'  , 0.185089    ), Coef('Var'  , 0.171938    ), Coef('Var'  , 0.165411    ), Coef('Var'  , 0.158943    ), Coef('Var'  , 0.174338    ), ], 
		[Coef('Var'  , 0.240318    ), Coef('Var'  , 0.227419    ), Coef('Var'  , 0.215255    ), Coef('Var'  , 0.197673    ), Coef('Var'  , 0.18029     ), Coef('Var'  , 0.193176    ), Coef('Var'  , 0.205943    ), Coef('Var'  , 0.222921    ), ], 
		[Coef('Var'  , 0.184525    ), Coef('Var'  , 0.172839    ), Coef('Var'  , 0.159731    ), Coef('Var'  , 0.158406    ), Coef('Var'  , 0.155455    ), Coef('Var'  , 0.170661    ), Coef('Var'  , 0.18464     ), Coef('Var'  , 0.185095    ), ], 
		[Coef('Var'  , 0.136361    ), Coef('Var'  , 0.135577    ), Coef('Var'  , 0.132005    ), Coef('Var'  , 0.14306     ), Coef('Var'  , 0.151168    ), Coef('Var'  , 0.158604    ), Coef('Var'  , 0.164056    ), Coef('Var'  , 0.151122    ), ], 
		[Coef('Var'  , 0.130717    ), Coef('Var'  , 0.136197    ), Coef('Var'  , 0.143967    ), Coef('Var'  , 0.159287    ), Coef('Var'  , 0.177665    ), Coef('Var'  , 0.169105    ), Coef('Var'  , 0.164098    ), Coef('Var'  , 0.146015    ), ], 
		[Coef('Var'  , 0.118063    ), Coef('Var'  , 0.133952    ), Coef('Var'  , 0.14972     ), Coef('Var'  , 0.156484    ), Coef('Var'  , 0.163483    ), Coef('Var'  , 0.143043    ), Coef('Var'  , 0.122321    ), Coef('Var'  , 0.12051     ), ], ])
	etat6.initMat[Chem([Sub('1')])] = FMat([
		[Coef('Const', 0.36        ), Coef('Var'  , 0.307743    ), Coef('Var'  , 0.256708    ), Coef('Var'  , 0.222512    ), Coef('Var'  , 0.190016    ), Coef('Var'  , 0.170105    ), Coef('Var'  , 0.15045     ), Coef('Var'  , 0.155335    ), Coef('Const', 0.16        ), Coef('Const', 0.24        ), ], 
		[Coef('Const', 0.48        ), Coef('Var'  , 0.380569    ), Coef('Var'  , 0.281706    ), Coef('Var'  , 0.26052     ), Coef('Var'  , 0.240318    ), Coef('Var'  , 0.251124    ), Coef('Var'  , 0.262427    ), Coef('Var'  , 0.371172    ), Coef('Const', 0.48        ), Coef('Const', 0.52        ), ], 
		[Coef('Const', 0.16        ), Coef('Var'  , 0.158039    ), Coef('Var'  , 0.155295    ), Coef('Var'  , 0.17059     ), Coef('Var'  , 0.184525    ), Coef('Var'  , 0.208418    ), Coef('Var'  , 0.231488    ), Coef('Var'  , 0.295867    ), Coef('Const', 0.36        ), Coef('Const', 0.24        ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0459485   ), Coef('Var'  , 0.0903128   ), Coef('Var'  , 0.114703    ), Coef('Var'  , 0.136361    ), Coef('Var'  , 0.141803    ), Coef('Var'  , 0.145747    ), Coef('Var'  , 0.0730482   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0492786   ), Coef('Var'  , 0.0989732   ), Coef('Var'  , 0.114095    ), Coef('Var'  , 0.130717    ), Coef('Var'  , 0.12876     ), Coef('Var'  , 0.129055    ), Coef('Var'  , 0.063943    ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0584227   ), Coef('Var'  , 0.117004    ), Coef('Var'  , 0.117579    ), Coef('Var'  , 0.118063    ), Coef('Var'  , 0.0997913   ), Coef('Var'  , 0.0808335   ), Coef('Var'  , 0.0406352   ), Coef('Const', 0           ), Coef('Const', 0           ), ], ])
	etat6.initMat[Chem([Sub('2')])] = FMat([
		[Coef('Var'  , 0.166498    ), Coef('Var'  , 0.193013    ), Coef('Var'  , 0.220807    ), Coef('Var'  , 0.23487     ), Coef('Const', 0.25        ), Coef('Const', 0.125       ), Coef('Const', 0.0625      ), Coef('Var'  , 0.0891785   ), Coef('Var'  , 0.115436    ), Coef('Var'  , 0.141072    ), ], 
		[Coef('Var'  , 0.129024    ), Coef('Var'  , 0.125677    ), Coef('Var'  , 0.121865    ), Coef('Var'  , 0.0609155   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0455833   ), Coef('Var'  , 0.0905526   ), Coef('Var'  , 0.110345    ), ], 
		[Coef('Var'  , 0.116777    ), Coef('Var'  , 0.105469    ), Coef('Var'  , 0.0923251   ), Coef('Var'  , 0.046641    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.048487    ), Coef('Var'  , 0.096497    ), Coef('Var'  , 0.107314    ), ], 
		[Coef('Var'  , 0.134112    ), Coef('Var'  , 0.11346     ), Coef('Var'  , 0.0898503   ), Coef('Var'  , 0.0457577   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0693976   ), Coef('Var'  , 0.13833     ), Coef('Var'  , 0.1371      ), ], 
		[Coef('Var'  , 0.234172    ), Coef('Var'  , 0.213525    ), Coef('Var'  , 0.195818    ), Coef('Var'  , 0.222434    ), Coef('Const', 0.25        ), Coef('Const', 0.375       ), Coef('Const', 0.5625      ), Coef('Var'  , 0.449848    ), Coef('Var'  , 0.33905     ), Coef('Var'  , 0.284689    ), ], 
		[Coef('Var'  , 0.219418    ), Coef('Var'  , 0.248856    ), Coef('Var'  , 0.279335    ), Coef('Var'  , 0.389382    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0.375       ), Coef('Var'  , 0.297506    ), Coef('Var'  , 0.220134    ), Coef('Var'  , 0.21948     ), ], ])
	etat6.initMat[Chem([Sub('3')])] = FMat([
		[Coef('Var'  , 0.15045     ), Coef('Var'  , 0.154902    ), Coef('Var'  , 0.158943    ), Coef('Var'  , 0.140813    ), Coef('Var'  , 0.121666    ), Coef('Var'  , 0.107006    ), Coef('Var'  , 0.0908055   ), Coef('Var'  , 0.121096    ), ], 
		[Coef('Var'  , 0.262427    ), Coef('Var'  , 0.234141    ), Coef('Var'  , 0.205943    ), Coef('Var'  , 0.173513    ), Coef('Var'  , 0.140578    ), Coef('Var'  , 0.132766    ), Coef('Var'  , 0.124129    ), Coef('Var'  , 0.193395    ), ], 
		[Coef('Var'  , 0.231488    ), Coef('Var'  , 0.208411    ), Coef('Var'  , 0.18464     ), Coef('Var'  , 0.173472    ), Coef('Var'  , 0.161524    ), Coef('Var'  , 0.177792    ), Coef('Var'  , 0.193575    ), Coef('Var'  , 0.21273     ), ], 
		[Coef('Var'  , 0.145747    ), Coef('Var'  , 0.155415    ), Coef('Var'  , 0.164056    ), Coef('Var'  , 0.189687    ), Coef('Var'  , 0.214507    ), Coef('Var'  , 0.246236    ), Coef('Var'  , 0.277927    ), Coef('Var'  , 0.211965    ), ], 
		[Coef('Var'  , 0.129055    ), Coef('Var'  , 0.145141    ), Coef('Var'  , 0.164098    ), Coef('Var'  , 0.199449    ), Coef('Var'  , 0.238684    ), Coef('Var'  , 0.234961    ), Coef('Var'  , 0.234954    ), Coef('Var'  , 0.180653    ), ], 
		[Coef('Var'  , 0.0808335   ), Coef('Var'  , 0.101989    ), Coef('Var'  , 0.122321    ), Coef('Var'  , 0.123067    ), Coef('Var'  , 0.123041    ), Coef('Var'  , 0.101239    ), Coef('Var'  , 0.0786092   ), Coef('Var'  , 0.0801611   ), ], ])
	etat6.initMat[Chem([Sub('4')])] = FMat([
		[Coef('Var'  , 0.450051    ), Coef('Var'  , 0.421945    ), Coef('Var'  , 0.40042     ), Coef('Var'  , 0.435909    ), Coef('Var'  , 0.477998    ), Coef('Var'  , 0.500458    ), Coef('Var'  , 0.52763     ), Coef('Var'  , 0.486495    ), ], 
		[Coef('Var'  , 0.115609    ), Coef('Var'  , 0.148236    ), Coef('Var'  , 0.182555    ), Coef('Var'  , 0.206799    ), Coef('Var'  , 0.232792    ), Coef('Var'  , 0.19871     ), Coef('Var'  , 0.165845    ), Coef('Var'  , 0.140146    ), ], 
		[Coef('Var'  , 0.0484213   ), Coef('Var'  , 0.0638937   ), Coef('Var'  , 0.0764139   ), Coef('Var'  , 0.0745595   ), Coef('Var'  , 0.0697532   ), Coef('Var'  , 0.0568005   ), Coef('Var'  , 0.0417606   ), Coef('Var'  , 0.0461347   ), ], 
		[Coef('Var'  , 0.035061    ), Coef('Var'  , 0.0445054   ), Coef('Var'  , 0.0487859   ), Coef('Var'  , 0.0445001   ), Coef('Var'  , 0.0350534   ), Coef('Var'  , 0.029988    ), Coef('Var'  , 0.0213286   ), Coef('Var'  , 0.0299932   ), ], 
		[Coef('Var'  , 0.0891426   ), Coef('Var'  , 0.0913178   ), Coef('Var'  , 0.0917558   ), Coef('Var'  , 0.0746895   ), Coef('Var'  , 0.0558649   ), Coef('Var'  , 0.0552036   ), Coef('Var'  , 0.0532517   ), Coef('Var'  , 0.0718319   ), ], 
		[Coef('Var'  , 0.261715    ), Coef('Var'  , 0.230102    ), Coef('Var'  , 0.200069    ), Coef('Var'  , 0.163543    ), Coef('Var'  , 0.128538    ), Coef('Var'  , 0.15884     ), Coef('Var'  , 0.190184    ), Coef('Var'  , 0.225399    ), ], ])
	etat6.initMat[Chem([Sub('5')])] = FMat([
		[Coef('Var'  , 0.083917    ), Coef('Var'  , 0.0423455   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0457613   ), Coef('Var'  , 0.0908055   ), Coef('Var'  , 0.0881067   ), ], 
		[Coef('Var'  , 0.0901503   ), Coef('Var'  , 0.0453324   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.062223    ), Coef('Var'  , 0.124129    ), Coef('Var'  , 0.107555    ), ], 
		[Coef('Var'  , 0.129209    ), Coef('Var'  , 0.0959634   ), Coef('Const', 0.0625      ), Coef('Const', 0.125       ), Coef('Const', 0.25        ), Coef('Var'  , 0.221863    ), Coef('Var'  , 0.193575    ), Coef('Var'  , 0.161577    ), ], 
		[Coef('Var'  , 0.251511    ), Coef('Var'  , 0.313225    ), Coef('Const', 0.375       ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.388916    ), Coef('Var'  , 0.277927    ), Coef('Var'  , 0.264642    ), ], 
		[Coef('Var'  , 0.339064    ), Coef('Var'  , 0.449918    ), Coef('Const', 0.5625      ), Coef('Const', 0.375       ), Coef('Const', 0.25        ), Coef('Var'  , 0.24171     ), Coef('Var'  , 0.234954    ), Coef('Var'  , 0.285378    ), ], 
		[Coef('Var'  , 0.106149    ), Coef('Var'  , 0.0532155   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0395259   ), Coef('Var'  , 0.0786092   ), Coef('Var'  , 0.0927414   ), ], ])
	etat6.initMat[Chem([Sub('6')])] = FMat([
		[Coef('Const', 0.0625      ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.03125     ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  ,-9.27245e-18 ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.0625      ), Coef('Var'  , 0.03125     ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Const', 0.375       ), Coef('Var'  , 0.1875      ), ], 
		[Coef('Const', 0.5625      ), Coef('Const', 0.75        ), Coef('Const', 1           ), Coef('Const', 0.75        ), Coef('Const', 0.5625      ), Coef('Var'  , 0.5625      ), ], 
		[Coef('Const', 0.375       ), Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.1875      ), ], ])
	etat6.initMat[Chem([Sub('7')])] = FMat([
		[Coef('Var'  , 0.40042     ), Coef('Var'  , 0.366774    ), Coef('Var'  , 0.339851    ), Coef('Var'  , 0.312573    ), Coef('Var'  , 0.290849    ), Coef('Var'  , 0.329786    ), Coef('Var'  , 0.374298    ), Coef('Var'  , 0.383988    ), ], 
		[Coef('Var'  , 0.182555    ), Coef('Var'  , 0.151228    ), Coef('Var'  , 0.121677    ), Coef('Var'  , 0.158581    ), Coef('Var'  , 0.197025    ), Coef('Var'  , 0.233144    ), Coef('Var'  , 0.27086     ), Coef('Var'  , 0.225791    ), ], 
		[Coef('Var'  , 0.0764139   ), Coef('Var'  , 0.070705    ), Coef('Var'  , 0.0619312   ), Coef('Var'  , 0.0863291   ), Coef('Var'  , 0.107983    ), Coef('Var'  , 0.108995    ), Coef('Var'  , 0.107263    ), Coef('Var'  , 0.0933706   ), ], 
		[Coef('Var'  , 0.0487859   ), Coef('Var'  , 0.0503211   ), Coef('Var'  , 0.0464264   ), Coef('Var'  , 0.0633231   ), Coef('Var'  , 0.0752147   ), Coef('Var'  , 0.0633179   ), Coef('Var'  , 0.0464188   ), Coef('Var'  , 0.0503159   ), ], 
		[Coef('Var'  , 0.0917558   ), Coef('Var'  , 0.117299    ), Coef('Var'  , 0.141181    ), Coef('Var'  , 0.134424    ), Coef('Var'  , 0.126844    ), Coef('Var'  , 0.0990456   ), Coef('Var'  , 0.0704038   ), Coef('Var'  , 0.0819211   ), ], 
		[Coef('Var'  , 0.200069    ), Coef('Var'  , 0.243672    ), Coef('Var'  , 0.288933    ), Coef('Var'  , 0.24477     ), Coef('Var'  , 0.202085    ), Coef('Var'  , 0.165711    ), Coef('Var'  , 0.130756    ), Coef('Var'  , 0.164613    ), ], ])
	etat6.initMat[Chem([Sub('G')])] = FMat([
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], ])
	etat6.initMat[Chem([Sub('8')])] = FMat([
		[Coef('Var'  , 0.477998    ), Coef('Var'  , 0.423244    ), Coef('Var'  , 0.374298    ), Coef('Var'  , 0.365662    ), Coef('Const', 0.36        ), Coef('Const', 0.48        ), Coef('Const', 0.64        ), Coef('Var'  , 0.557583    ), ], 
		[Coef('Var'  , 0.232792    ), Coef('Var'  , 0.251028    ), Coef('Var'  , 0.27086     ), Coef('Var'  , 0.37501     ), Coef('Const', 0.48        ), Coef('Const', 0.44        ), Coef('Const', 0.32        ), Coef('Var'  , 0.276018    ), ], 
		[Coef('Var'  , 0.0697532   ), Coef('Var'  , 0.089824    ), Coef('Var'  , 0.107263    ), Coef('Var'  , 0.134318    ), Coef('Const', 0.16        ), Coef('Const', 0.08        ), Coef('Const', 0.04        ), Coef('Var'  , 0.0555064   ), ], 
		[Coef('Var'  , 0.0350534   ), Coef('Var'  , 0.0430572   ), Coef('Var'  , 0.0464188   ), Coef('Var'  , 0.0244365   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0186207   ), ], 
		[Coef('Var'  , 0.0558649   ), Coef('Var'  , 0.063864    ), Coef('Var'  , 0.0704038   ), Coef('Var'  , 0.0355478   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0283162   ), ], 
		[Coef('Var'  , 0.128538    ), Coef('Var'  , 0.128982    ), Coef('Var'  , 0.130756    ), Coef('Var'  , 0.0650261   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.063956    ), ], ])
	etat6.initMat[Chem([Sub('9')])] = FMat([
		[Coef('Var'  , 0.450051    ), Coef('Var'  , 0.504869    ), Coef('Const', 0.5625      ), Coef('Const', 0.375       ), Coef('Const', 0.25        ), Coef('Var'  , 0.293448    ), Coef('Var'  , 0.339851    ), Coef('Var'  , 0.392067    ), ], 
		[Coef('Var'  , 0.115609    ), Coef('Var'  , 0.0574547   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.060447    ), Coef('Var'  , 0.121677    ), Coef('Var'  , 0.117902    ), ], 
		[Coef('Var'  , 0.0484213   ), Coef('Var'  , 0.0248407   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0316519   ), Coef('Var'  , 0.0619312   ), Coef('Var'  , 0.0564926   ), ], 
		[Coef('Var'  , 0.035061    ), Coef('Var'  , 0.0186259   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0244417   ), Coef('Var'  , 0.0464264   ), Coef('Var'  , 0.0430677   ), ], 
		[Coef('Var'  , 0.0891426   ), Coef('Var'  , 0.0761945   ), Coef('Const', 0.0625      ), Coef('Const', 0.125       ), Coef('Const', 0.25        ), Coef('Var'  , 0.195926    ), Coef('Var'  , 0.141181    ), Coef('Var'  , 0.115871    ), ], 
		[Coef('Var'  , 0.261715    ), Coef('Var'  , 0.318015    ), Coef('Const', 0.375       ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.394085    ), Coef('Var'  , 0.288933    ), Coef('Var'  , 0.2746      ), ], ])
	etat6.initMat[Chem([Sub('10')])] = FMat([
		[Coef('Var'  , 0.52763     ), Coef('Var'  , 0.582875    ), Coef('Const', 0.64        ), Coef('Const', 0.8         ), Coef('Const', 1           ), Coef('Const', 0.75        ), Coef('Const', 0.5625      ), Coef('Var'  , 0.544125    ), ], 
		[Coef('Var'  , 0.165845    ), Coef('Var'  , 0.242692    ), Coef('Const', 0.32        ), Coef('Const', 0.2         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0826915   ), ], 
		[Coef('Var'  , 0.0417606   ), Coef('Var'  , 0.0412941   ), Coef('Const', 0.04        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0212941   ), ], 
		[Coef('Var'  , 0.0213286   ), Coef('Var'  , 0.0113672   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0113672   ), ], 
		[Coef('Var'  , 0.0532517   ), Coef('Var'  , 0.0268874   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.0625      ), Coef('Var'  , 0.0581374   ), ], 
		[Coef('Var'  , 0.190184    ), Coef('Var'  , 0.0948843   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Const', 0.375       ), Coef('Var'  , 0.282384    ), ], ])
	etat6.initMat[Chem([Sub('11')])] = FMat([
		[Coef('Var'  , 0.256708    ), Coef('Var'  , 0.271867    ), Coef('Var'  , 0.290849    ), Coef('Var'  , 0.253995    ), Coef('Var'  , 0.220807    ), Coef('Var'  , 0.203355    ), Coef('Var'  , 0.187678    ), Coef('Var'  , 0.192732    ), Coef('Var'  , 0.199321    ), Coef('Var'  , 0.226989    ), ], 
		[Coef('Var'  , 0.281706    ), Coef('Var'  , 0.238702    ), Coef('Var'  , 0.197025    ), Coef('Var'  , 0.159049    ), Coef('Var'  , 0.121865    ), Coef('Var'  , 0.141891    ), Coef('Var'  , 0.161855    ), Coef('Var'  , 0.188442    ), Coef('Var'  , 0.215255    ), Coef('Var'  , 0.248036    ), ], 
		[Coef('Var'  , 0.155295    ), Coef('Var'  , 0.132716    ), Coef('Var'  , 0.107983    ), Coef('Var'  , 0.101318    ), Coef('Var'  , 0.0923251   ), Coef('Var'  , 0.114061    ), Coef('Var'  , 0.133859    ), Coef('Var'  , 0.147708    ), Coef('Var'  , 0.159731    ), Coef('Var'  , 0.158327    ), ], 
		[Coef('Var'  , 0.0903128   ), Coef('Var'  , 0.08483     ), Coef('Var'  , 0.0752147   ), Coef('Var'  , 0.0846391   ), Coef('Var'  , 0.0898503   ), Coef('Var'  , 0.112405    ), Coef('Var'  , 0.13159     ), Coef('Var'  , 0.13347     ), Coef('Var'  , 0.132005    ), Coef('Var'  , 0.112771    ), ], 
		[Coef('Var'  , 0.0989732   ), Coef('Var'  , 0.112776    ), Coef('Var'  , 0.126844    ), Coef('Var'  , 0.160931    ), Coef('Var'  , 0.195818    ), Coef('Var'  , 0.188224    ), Coef('Var'  , 0.183203    ), Coef('Var'  , 0.162171    ), Coef('Var'  , 0.143967    ), Coef('Var'  , 0.120659    ), ], 
		[Coef('Var'  , 0.117004    ), Coef('Var'  , 0.159108    ), Coef('Var'  , 0.202085    ), Coef('Var'  , 0.240067    ), Coef('Var'  , 0.279335    ), Coef('Var'  , 0.240064    ), Coef('Var'  , 0.201815    ), Coef('Var'  , 0.175478    ), Coef('Var'  , 0.14972     ), Coef('Var'  , 0.133218    ), ], ])
	etat6.initMat[Chem([Sub('12')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.025003    ), Coef('Var'  , 0.0500037   ), Coef('Var'  , 0.025003    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0999982   ), Coef('Var'  , 0.199998    ), Coef('Var'  , 0.0999982   ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0.375       ), Coef('Const', 0.5625      ), Coef('Var'  , 0.507805    ), Coef('Var'  , 0.453115    ), Coef('Var'  , 0.351555    ), ], 
		[Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0.375       ), Coef('Var'  , 0.296874    ), Coef('Var'  , 0.218749    ), Coef('Var'  , 0.359374    ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0.125       ), Coef('Const', 0.0625      ), Coef('Var'  , 0.0703147   ), Coef('Var'  , 0.0781277   ), Coef('Var'  , 0.164065    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 5.46372e-06 ), Coef('Var'  , 6.75353e-06 ), Coef('Var'  , 5.46372e-06 ), ], ])
	etat6.initMat[Chem([Sub('13')])] = FMat([
		[Coef('Const', 0.16        ), Coef('Var'  , 0.105003    ), Coef('Var'  , 0.0500037   ), Coef('Var'  , 0.045003    ), Coef('Const', 0.04        ), Coef('Const', 0.08        ), ], 
		[Coef('Const', 0.48        ), Coef('Var'  , 0.339998    ), Coef('Var'  , 0.199998    ), Coef('Var'  , 0.259998    ), Coef('Const', 0.32        ), Coef('Const', 0.44        ), ], 
		[Coef('Const', 0.36        ), Coef('Var'  , 0.406555    ), Coef('Var'  , 0.453115    ), Coef('Var'  , 0.546555    ), Coef('Const', 0.64        ), Coef('Const', 0.48        ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.109374    ), Coef('Var'  , 0.218749    ), Coef('Var'  , 0.109374    ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0390647   ), Coef('Var'  , 0.0781277   ), Coef('Var'  , 0.0390647   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 5.46372e-06 ), Coef('Var'  , 6.75353e-06 ), Coef('Var'  , 5.46372e-06 ), Coef('Const', 0           ), Coef('Const', 0           ), ], ])
	etat6.initMat[Chem([Sub('14')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.04        ), Coef('Var'  , 0.02        ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.2         ), Coef('Const', 0.32        ), Coef('Var'  , 0.16        ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 1           ), Coef('Const', 0.8         ), Coef('Const', 0.64        ), Coef('Var'  , 0.60125     ), Coef('Const', 0.5625      ), Coef('Const', 0.75        ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.1875      ), Coef('Const', 0.375       ), Coef('Const', 0.25        ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.03125     ), Coef('Const', 0.0625      ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 9.07222e-18 ), Coef('Const', 0           ), Coef('Const', 0           ), ], ])
	etat6.initMat[Chem([Sub('15')])] = FMat([
		[Coef('Var'  , 0.171938    ), Coef('Var'  , 0.179329    ), Coef('Var'  , 0.187678    ), Coef('Var'  , 0.176629    ), Coef('Var'  , 0.166498    ), Coef('Var'  , 0.15572     ), Coef('Var'  , 0.144774    ), Coef('Var'  , 0.15842     ), ], 
		[Coef('Var'  , 0.18029     ), Coef('Var'  , 0.171181    ), Coef('Var'  , 0.161855    ), Coef('Var'  , 0.145737    ), Coef('Var'  , 0.129024    ), Coef('Var'  , 0.133457    ), Coef('Var'  , 0.136752    ), Coef('Var'  , 0.158901    ), ], 
		[Coef('Var'  , 0.155455    ), Coef('Var'  , 0.145537    ), Coef('Var'  , 0.133859    ), Coef('Var'  , 0.126247    ), Coef('Var'  , 0.116777    ), Coef('Var'  , 0.126399    ), Coef('Var'  , 0.134484    ), Coef('Var'  , 0.145689    ), ], 
		[Coef('Var'  , 0.151168    ), Coef('Var'  , 0.142884    ), Coef('Var'  , 0.13159     ), Coef('Var'  , 0.134349    ), Coef('Var'  , 0.134112    ), Coef('Var'  , 0.149045    ), Coef('Var'  , 0.161902    ), Coef('Var'  , 0.15758     ), ], 
		[Coef('Var'  , 0.177665    ), Coef('Var'  , 0.178698    ), Coef('Var'  , 0.183203    ), Coef('Var'  , 0.206882    ), Coef('Var'  , 0.234172    ), Coef('Var'  , 0.235366    ), Coef('Var'  , 0.240882    ), Coef('Var'  , 0.207182    ), ], 
		[Coef('Var'  , 0.163483    ), Coef('Var'  , 0.182371    ), Coef('Var'  , 0.201815    ), Coef('Var'  , 0.210156    ), Coef('Var'  , 0.219418    ), Coef('Var'  , 0.200014    ), Coef('Var'  , 0.181206    ), Coef('Var'  , 0.172229    ), ], ])
	etat6.initMat[Chem([Sub('16')])] = FMat([
		[Coef('Var'  , 0.121666    ), Coef('Var'  , 0.133821    ), Coef('Var'  , 0.144774    ), Coef('Var'  , 0.130505    ), Coef('Var'  , 0.115436    ), Coef('Var'  , 0.100274    ), Coef('Var'  , 0.083917    ), Coef('Var'  , 0.10359     ), ], 
		[Coef('Var'  , 0.140578    ), Coef('Var'  , 0.139238    ), Coef('Var'  , 0.136752    ), Coef('Var'  , 0.114278    ), Coef('Var'  , 0.0905526   ), Coef('Var'  , 0.0909157   ), Coef('Var'  , 0.0901503   ), Coef('Var'  , 0.115876    ), ], 
		[Coef('Var'  , 0.161524    ), Coef('Var'  , 0.1485      ), Coef('Var'  , 0.134484    ), Coef('Var'  , 0.116058    ), Coef('Var'  , 0.096497    ), Coef('Var'  , 0.1132      ), Coef('Var'  , 0.129209    ), Coef('Var'  , 0.145642    ), ], 
		[Coef('Var'  , 0.214507    ), Coef('Var'  , 0.188662    ), Coef('Var'  , 0.161902    ), Coef('Var'  , 0.15074     ), Coef('Var'  , 0.13833     ), Coef('Var'  , 0.195123    ), Coef('Var'  , 0.251511    ), Coef('Var'  , 0.233045    ), ], 
		[Coef('Var'  , 0.238684    ), Coef('Var'  , 0.237526    ), Coef('Var'  , 0.240882    ), Coef('Var'  , 0.287873    ), Coef('Var'  , 0.33905     ), Coef('Var'  , 0.337266    ), Coef('Var'  , 0.339064    ), Coef('Var'  , 0.286919    ), ], 
		[Coef('Var'  , 0.123041    ), Coef('Var'  , 0.152253    ), Coef('Var'  , 0.181206    ), Coef('Var'  , 0.200546    ), Coef('Var'  , 0.220134    ), Coef('Var'  , 0.163221    ), Coef('Var'  , 0.106149    ), Coef('Var'  , 0.114929    ), ], ])
	
	
	
	etat7.bords   = {Bord('0'): etat20, Bord('1'): etat21, Bord('2'): etat21, Bord('3'): etat19, }
	etat7.permuts = {}
	etat7.interns = {Intern('_'): etat7, }
	etat7.subs    = {Sub('0'): etat1, Sub('1'): etat2, Sub('2'): etat3, Sub('3'): etat4, Sub('4'): etat5, Sub('5'): etat6, Sub('6'): etat8, Sub('7'): etat9, Sub('G', True): Etat.etatPoint, Sub('8'): etat10, Sub('9'): etat11, Sub('10'): etat12, Sub('11'): etat13, Sub('12'): etat14, Sub('13'): etat15, Sub('14'): etat16, Sub('15'): etat17, Sub('16'): etat18, }
	
	etat7.buildIntern()
	
	
	etat7.eqs = [
		(Chem([Bord('2'), Sub('2'), Permut('0'), ])	,	Chem([Sub('1'), Bord('3'), ])),
		(Chem([Bord('0'), Sub('1'), Permut('0'), ])	,	Chem([Sub('2'), Bord('3'), ])),
		(Chem([Bord('3'), Sub('0'), Permut('0'), ])	,	Chem([Sub('3'), Bord('2'), ])),
		(Chem([Bord('2'), Sub('3'), Permut('0'), ])	,	Chem([Sub('3'), Bord('3'), ])),
		(Chem([Bord('1'), Sub('1'), Permut('0'), ])	,	Chem([Sub('5'), Bord('1'), ])),
		(Chem([Bord('1'), Sub('0'), Permut('0'), ])	,	Chem([Sub('6'), Bord('1'), ])),
		(Chem([Bord('0'), Sub('2'), Permut('0'), ])	,	Chem([Sub('6'), Bord('2'), ])),
		(Chem([Bord('1'), Sub('3'), Permut('0'), ])	,	Chem([Sub('12'), Bord('0'), ])),
		(Chem([Bord('2'), Sub('0'), Permut('0'), ])	,	Chem([Sub('12'), Bord('2'), ])),
		(Chem([Bord('2'), Sub('1'), Permut('0'), ])	,	Chem([Sub('13'), Bord('0'), ])),
		(Chem([Bord('1'), Sub('2'), Permut('0'), ])	,	Chem([Sub('14'), Bord('2'), ])),
		(Chem([Bord('0'), Sub('0'), Permut('0'), ])	,	Chem([Sub('16'), Bord('2'), ])),
		(Chem([Bord('3'), Sub('1'), Permut('0'), ])	,	Chem([Sub('16'), Bord('3'), ])),
		(Chem([Sub('0'), Bord('0'), Bord('1'), ])	,	Chem([Sub('11'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('1'), Bord('1'), ])	,	Chem([Sub('15'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('2'), Bord('1'), ])	,	Chem([Sub('3'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('3'), Bord('1'), ])	,	Chem([Sub('1'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('0'), Bord('1'), ])	,	Chem([Sub('11'), Bord('4'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('2'), Bord('1'), ])	,	Chem([Sub('3'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('3'), Bord('1'), ])	,	Chem([Sub('13'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('4'), Bord('1'), ])	,	Chem([Sub('8'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('0'), Bord('1'), ])	,	Chem([Sub('11'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('1'), Bord('1'), ])	,	Chem([Sub('9'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('2'), Bord('1'), ])	,	Chem([Sub('6'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('3'), Bord('1'), ])	,	Chem([Sub('16'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('4'), Bord('1'), ])	,	Chem([Sub('15'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('3'), Bord('1'), Bord('1'), ])	,	Chem([Sub('16'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('4'), Bord('0'), Bord('1'), ])	,	Chem([Sub('7'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('4'), Bord('1'), Bord('1'), ])	,	Chem([Sub('8'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('4'), Bord('2'), Bord('1'), ])	,	Chem([Sub('10'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('4'), Bord('3'), Bord('1'), ])	,	Chem([Sub('9'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('5'), Bord('0'), Bord('1'), ])	,	Chem([Sub('14'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('5'), Bord('1'), Bord('1'), ])	,	Chem([Sub('6'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('5'), Bord('2'), Bord('1'), ])	,	Chem([Sub('10'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('7'), Bord('0'), Bord('1'), ])	,	Chem([Sub('9'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('7'), Bord('1'), Bord('1'), ])	,	Chem([Sub('11'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('7'), Bord('2'), Bord('1'), ])	,	Chem([Sub('8'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('8'), Bord('2'), Bord('1'), ])	,	Chem([Sub('10'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('9'), Bord('0'), Bord('1'), ])	,	Chem([Sub('10'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('11'), Bord('2'), Bord('1'), ])	,	Chem([Sub('15'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('12'), Bord('0'), Bord('1'), ])	,	Chem([Sub('14'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('12'), Bord('1'), Bord('1'), ])	,	Chem([Sub('13'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('13'), Bord('1'), Bord('1'), ])	,	Chem([Sub('14'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('15'), Bord('2'), Bord('1'), ])	,	Chem([Sub('16'), Bord('0'), Bord('1'), ])),
		(Chem([Bord('0'), Bord('1'), ])	,	Chem([Bord('1'), Bord('0'), ])),
		(Chem([Bord('1'), Bord('1'), ])	,	Chem([Bord('2'), Bord('0'), ])),
		(Chem([Bord('2'), Bord('1'), ])	,	Chem([Bord('3'), Bord('0'), ])),
		(Chem([Bord('3'), Bord('1'), ])	,	Chem([Bord('0'), Bord('0'), ])),
		]
	
	
	etat7.prim.elems = [Figure(2, [Chem([Bord('0'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('0'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('0'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('0'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('1'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('1'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('1'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('1'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('2'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('2'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('2'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('2'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('3'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('3'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('3'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('3'), Sub('1'), Sub('1'), Bord('0'), ]), ])]
	etat7.grid.elems = [
		Figure(1, [Chem([Bord('1'), Bord('0'), ]), Chem([Bord('1'), Intern(''), ]), Chem([Bord('1'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('2'), Bord('0'), ]), Chem([Bord('2'), Intern(''), ]), Chem([Bord('2'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('0'), Bord('0'), ]), Chem([Bord('0'), Intern(''), ]), Chem([Bord('0'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('3'), Bord('0'), ]), Chem([Bord('3'), Intern(''), ]), Chem([Bord('3'), Bord('1'), ]), ]), ]
	
	
	etat7.space = [Chem([Bord('0'), Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('2'), Intern('0'), Intern('0'), ]), Chem([Bord('2'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('3'), Intern('0'), Intern('0'), ]), ]
	
	etat7.initMat[Chem([Sub('0')])] = FMat([
		[Coef('Var'  , 0.0960448   ), Coef('Var'  , 0.11986     ), Coef('Var'  , 0.144863    ), Coef('Var'  , 0.165019    ), Coef('Var'  , 0.186925    ), Coef('Var'  , 0.158839    ), Coef('Var'  , 0.132113    ), Coef('Var'  , 0.113681    ), ], 
		[Coef('Var'  , 0.0761735   ), Coef('Var'  , 0.103978    ), Coef('Var'  , 0.131406    ), Coef('Var'  , 0.138962    ), Coef('Var'  , 0.146539    ), Coef('Var'  , 0.101214    ), Coef('Var'  , 0.0559049   ), Coef('Var'  , 0.0662307   ), ], 
		[Coef('Var'  , 0.0565929   ), Coef('Var'  , 0.0728115   ), Coef('Var'  , 0.0877384   ), Coef('Var'  , 0.0841531   ), Coef('Var'  , 0.0791134   ), Coef('Var'  , 0.0576663   ), Coef('Var'  , 0.0350737   ), Coef('Var'  , 0.0463247   ), ], 
		[Coef('Var'  , 0.0391827   ), Coef('Var'  , 0.0484089   ), Coef('Var'  , 0.0552464   ), Coef('Var'  , 0.0501517   ), Coef('Var'  , 0.0423232   ), Coef('Var'  , 0.0333307   ), Coef('Var'  , 0.0223188   ), Coef('Var'  , 0.0315879   ), ], 
		[Coef('Var'  , 0.0825043   ), Coef('Var'  , 0.0867557   ), Coef('Var'  , 0.0888925   ), Coef('Var'  , 0.0790116   ), Coef('Var'  , 0.0665218   ), Coef('Var'  , 0.0615297   ), Coef('Var'  , 0.0546197   ), Coef('Var'  , 0.0692737   ), ], 
		[Coef('Var'  , 0.223311    ), Coef('Var'  , 0.190095    ), Coef('Var'  , 0.158257    ), Coef('Var'  , 0.139322    ), Coef('Var'  , 0.121515    ), Coef('Var'  , 0.149878    ), Coef('Var'  , 0.179009    ), Coef('Var'  , 0.200652    ), ], 
		[Coef('Var'  , 0.323973    ), Coef('Var'  , 0.267048    ), Coef('Var'  , 0.214044    ), Coef('Var'  , 0.205925    ), Coef('Var'  , 0.201992    ), Coef('Var'  , 0.265249    ), Coef('Var'  , 0.33155     ), Coef('Var'  , 0.326372    ), ], 
		[Coef('Var'  , 0.102217    ), Coef('Var'  , 0.111041    ), Coef('Var'  , 0.119553    ), Coef('Var'  , 0.137456    ), Coef('Var'  , 0.155071    ), Coef('Var'  , 0.172293    ), Coef('Var'  , 0.189411    ), Coef('Var'  , 0.145879    ), ], ])
	etat7.initMat[Chem([Sub('1')])] = FMat([
		[Coef('Var'  , 0.0773465   ), Coef('Var'  , 0.0945982   ), Coef('Var'  , 0.111652    ), Coef('Var'  , 0.10356     ), Coef('Var'  , 0.0960448   ), Coef('Var'  , 0.047829    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.038867    ), ], 
		[Coef('Var'  , 0.0895656   ), Coef('Var'  , 0.102567    ), Coef('Var'  , 0.11482     ), Coef('Var'  , 0.0958048   ), Coef('Var'  , 0.0761735   ), Coef('Var'  , 0.0382253   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0449878   ), ], 
		[Coef('Var'  , 0.104643    ), Coef('Var'  , 0.101242    ), Coef('Var'  , 0.0980182   ), Coef('Var'  , 0.0777053   ), Coef('Var'  , 0.0565929   ), Coef('Var'  , 0.0285685   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0521052   ), ], 
		[Coef('Var'  , 0.0831669   ), Coef('Var'  , 0.0763846   ), Coef('Var'  , 0.0686826   ), Coef('Var'  , 0.0548729   ), Coef('Var'  , 0.0391827   ), Coef('Var'  , 0.0200723   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.041584    ), ], 
		[Coef('Var'  , 0.162782    ), Coef('Var'  , 0.139457    ), Coef('Var'  , 0.11491     ), Coef('Var'  , 0.09955     ), Coef('Var'  , 0.0825043   ), Coef('Var'  , 0.0729013   ), Coef('Const', 0.0625      ), Coef('Const', 0.125       ), Coef('Const', 0.25        ), Coef('Var'  , 0.206558    ), ], 
		[Coef('Var'  , 0.243427    ), Coef('Var'  , 0.214925    ), Coef('Var'  , 0.187972    ), Coef('Var'  , 0.204876    ), Coef('Var'  , 0.223311    ), Coef('Var'  , 0.298824    ), Coef('Const', 0.375       ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.371374    ), ], 
		[Coef('Var'  , 0.171229    ), Coef('Var'  , 0.187212    ), Coef('Var'  , 0.205734    ), Coef('Var'  , 0.263123    ), Coef('Var'  , 0.323973    ), Coef('Var'  , 0.442411    ), Coef('Const', 0.5625      ), Coef('Const', 0.375       ), Coef('Const', 0.25        ), Coef('Var'  , 0.21025     ), ], 
		[Coef('Var'  , 0.0678402   ), Coef('Var'  , 0.0836138   ), Coef('Var'  , 0.0982116   ), Coef('Var'  , 0.100508    ), Coef('Var'  , 0.102217    ), Coef('Var'  , 0.0511684   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0342742   ), ], ])
	etat7.initMat[Chem([Sub('2')])] = FMat([
		[Coef('Var'  , 0.274209    ), Coef('Var'  , 0.226392    ), Coef('Var'  , 0.180046    ), Coef('Var'  , 0.153943    ), Coef('Var'  , 0.128429    ), Coef('Var'  , 0.119801    ), Coef('Const', 0.111111    ), Coef('Const', 0.222222    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.358916    ), ], 
		[Coef('Var'  , 0.263035    ), Coef('Var'  , 0.237091    ), Coef('Var'  , 0.212145    ), Coef('Var'  , 0.227894    ), Coef('Var'  , 0.244509    ), Coef('Var'  , 0.344306    ), Coef('Const', 0.444444    ), Coef('Const', 0.555556    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.353503    ), ], 
		[Coef('Var'  , 0.113091    ), Coef('Var'  , 0.132816    ), Coef('Var'  , 0.152446    ), Coef('Var'  , 0.199736    ), Coef('Var'  , 0.248094    ), Coef('Var'  , 0.345812    ), Coef('Const', 0.444444    ), Coef('Const', 0.222222    ), Coef('Const', 0.111111    ), Coef('Var'  , 0.112225    ), ], 
		[Coef('Var'  , 0.0390363   ), Coef('Var'  , 0.0547617   ), Coef('Var'  , 0.068667    ), Coef('Var'  , 0.0765342   ), Coef('Var'  , 0.0834397   ), Coef('Var'  , 0.0417487   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0199763   ), ], 
		[Coef('Var'  , 0.0511677   ), Coef('Var'  , 0.0689753   ), Coef('Var'  , 0.0845196   ), Coef('Var'  , 0.083979    ), Coef('Var'  , 0.0817311   ), Coef('Var'  , 0.0411282   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0261244   ), ], 
		[Coef('Var'  , 0.0616857   ), Coef('Var'  , 0.0778832   ), Coef('Var'  , 0.0942528   ), Coef('Var'  , 0.0836791   ), Coef('Var'  , 0.0732023   ), Coef('Var'  , 0.0366156   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0308197   ), ], 
		[Coef('Var'  , 0.0947033   ), Coef('Var'  , 0.10049     ), Coef('Var'  , 0.108731    ), Coef('Var'  , 0.0895622   ), Coef('Var'  , 0.0719279   ), Coef('Var'  , 0.0358329   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0467603   ), ], 
		[Coef('Var'  , 0.103073    ), Coef('Var'  , 0.101591    ), Coef('Var'  , 0.0991924   ), Coef('Var'  , 0.0846729   ), Coef('Var'  , 0.0686675   ), Coef('Var'  , 0.0347561   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0516739   ), ], ])
	etat7.initMat[Chem([Sub('3')])] = FMat([
		[Coef('Const', 0           ), Coef('Var'  , 0.0658516   ), Coef('Var'  , 0.132113    ), Coef('Var'  , 0.190852    ), Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0280054   ), Coef('Var'  , 0.0559049   ), Coef('Var'  , 0.0280054   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0177563   ), Coef('Var'  , 0.0350737   ), Coef('Var'  , 0.0177563   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0115156   ), Coef('Var'  , 0.0223188   ), Coef('Var'  , 0.0115156   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.0625      ), Coef('Var'  , 0.0588724   ), Coef('Var'  , 0.0546197   ), Coef('Var'  , 0.0276224   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.375       ), Coef('Var'  , 0.276827    ), Coef('Var'  , 0.179009    ), Coef('Var'  , 0.0893274   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), ], 
		[Coef('Const', 0.5625      ), Coef('Var'  , 0.446461    ), Coef('Var'  , 0.33155     ), Coef('Var'  , 0.290211    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.75        ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0947102   ), Coef('Var'  , 0.189411    ), Coef('Var'  , 0.34471     ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), ], ])
	etat7.initMat[Chem([Sub('4')])] = FMat([
		[Coef('Var'  , 0.111685    ), Coef('Var'  , 0.113519    ), Coef('Var'  , 0.113895    ), Coef('Var'  , 0.110225    ), Coef('Var'  , 0.10498     ), Coef('Var'  , 0.104744    ), Coef('Var'  , 0.10277     ), Coef('Var'  , 0.108038    ), ], 
		[Coef('Var'  , 0.152241    ), Coef('Var'  , 0.150523    ), Coef('Var'  , 0.148656    ), Coef('Var'  , 0.140507    ), Coef('Var'  , 0.13183     ), Coef('Var'  , 0.133919    ), Coef('Var'  , 0.135415    ), Coef('Var'  , 0.143936    ), ], 
		[Coef('Var'  , 0.183301    ), Coef('Var'  , 0.171261    ), Coef('Var'  , 0.162495    ), Coef('Var'  , 0.16184     ), Coef('Var'  , 0.164148    ), Coef('Var'  , 0.172976    ), Coef('Var'  , 0.184954    ), Coef('Var'  , 0.182397    ), ], 
		[Coef('Var'  , 0.12858     ), Coef('Var'  , 0.120899    ), Coef('Var'  , 0.114323    ), Coef('Var'  , 0.120716    ), Coef('Var'  , 0.128281    ), Coef('Var'  , 0.134618    ), Coef('Var'  , 0.142538    ), Coef('Var'  , 0.134801    ), ], 
		[Coef('Var'  , 0.125502    ), Coef('Var'  , 0.127823    ), Coef('Var'  , 0.129546    ), Coef('Var'  , 0.133434    ), Coef('Var'  , 0.136779    ), Coef('Var'  , 0.134932    ), Coef('Var'  , 0.132735    ), Coef('Var'  , 0.129321    ), ], 
		[Coef('Var'  , 0.109599    ), Coef('Var'  , 0.117685    ), Coef('Var'  , 0.126323    ), Coef('Var'  , 0.128772    ), Coef('Var'  , 0.132166    ), Coef('Var'  , 0.123392    ), Coef('Var'  , 0.115442    ), Coef('Var'  , 0.112305    ), ], 
		[Coef('Var'  , 0.0984522   ), Coef('Var'  , 0.104312    ), Coef('Var'  , 0.110132    ), Coef('Var'  , 0.110753    ), Coef('Var'  , 0.111568    ), Coef('Var'  , 0.105833    ), Coef('Var'  , 0.099888    ), Coef('Var'  , 0.0993924   ), ], 
		[Coef('Var'  , 0.0906393   ), Coef('Var'  , 0.0939776   ), Coef('Var'  , 0.0946299   ), Coef('Var'  , 0.0937535   ), Coef('Var'  , 0.0902475   ), Coef('Var'  , 0.0895848   ), Coef('Var'  , 0.0862568   ), Coef('Var'  , 0.0898089   ), ], ])
	etat7.initMat[Chem([Sub('5')])] = FMat([
		[Coef('Var'  , 0.047327    ), Coef('Var'  , 0.0238806   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0238806   ), ], 
		[Coef('Var'  , 0.0640818   ), Coef('Var'  , 0.0320926   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0320926   ), ], 
		[Coef('Var'  , 0.303771    ), Coef('Var'  , 0.276481    ), Coef('Const', 0.25        ), Coef('Const', 0.375       ), Coef('Const', 0.5625      ), Coef('Var'  , 0.432731    ), ], 
		[Coef('Var'  , 0.298206    ), Coef('Var'  , 0.39887     ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0.375       ), Coef('Var'  , 0.33637     ), ], 
		[Coef('Var'  , 0.144963    ), Coef('Var'  , 0.197501    ), Coef('Const', 0.25        ), Coef('Const', 0.125       ), Coef('Const', 0.0625      ), Coef('Var'  , 0.103751    ), ], 
		[Coef('Var'  , 0.0555106   ), Coef('Var'  , 0.0276975   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0276975   ), ], 
		[Coef('Var'  , 0.047179    ), Coef('Var'  , 0.0236732   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0236732   ), ], 
		[Coef('Var'  , 0.0389621   ), Coef('Var'  , 0.0198046   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0198046   ), ], ])
	etat7.initMat[Chem([Sub('6')])] = FMat([
		[Coef('Const', 0.111111    ), Coef('Var'  , 0.0555556   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.444444    ), Coef('Var'  , 0.222222    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.333333    ), ], 
		[Coef('Const', 0.444444    ), Coef('Var'  , 0.503472    ), Coef('Const', 0.5625      ), Coef('Const', 0.75        ), Coef('Const', 1           ), Coef('Const', 0.666667    ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.1875      ), Coef('Const', 0.375       ), Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0312501   ), Coef('Const', 0.0625      ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 6.25e-08    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 6.25e-08    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 6.25e-08    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], ])
	etat7.initMat[Chem([Sub('7')])] = FMat([
		[Coef('Var'  , 0.113895    ), Coef('Var'  , 0.118688    ), Coef('Var'  , 0.122358    ), Coef('Var'  , 0.126724    ), Coef('Var'  , 0.130669    ), Coef('Var'  , 0.119797    ), Coef('Var'  , 0.108338    ), Coef('Var'  , 0.111762    ), ], 
		[Coef('Var'  , 0.148656    ), Coef('Var'  , 0.162207    ), Coef('Var'  , 0.175753    ), Coef('Var'  , 0.167228    ), Coef('Var'  , 0.158884    ), Coef('Var'  , 0.146114    ), Coef('Var'  , 0.133061    ), Coef('Var'  , 0.141093    ), ], 
		[Coef('Var'  , 0.162495    ), Coef('Var'  , 0.169774    ), Coef('Var'  , 0.179907    ), Coef('Var'  , 0.159502    ), Coef('Var'  , 0.140977    ), Coef('Var'  , 0.139775    ), Coef('Var'  , 0.140102    ), Coef('Var'  , 0.150047    ), ], 
		[Coef('Var'  , 0.114323    ), Coef('Var'  , 0.108374    ), Coef('Var'  , 0.103005    ), Coef('Var'  , 0.0952748   ), Coef('Var'  , 0.0871397   ), Coef('Var'  , 0.0950979   ), Coef('Var'  , 0.102715    ), Coef('Var'  , 0.108197    ), ], 
		[Coef('Var'  , 0.129546    ), Coef('Var'  , 0.122434    ), Coef('Var'  , 0.114481    ), Coef('Var'  , 0.115493    ), Coef('Var'  , 0.115177    ), Coef('Var'  , 0.126874    ), Coef('Var'  , 0.137332    ), Coef('Var'  , 0.133814    ), ], 
		[Coef('Var'  , 0.126323    ), Coef('Var'  , 0.118169    ), Coef('Var'  , 0.110622    ), Coef('Var'  , 0.123006    ), Coef('Var'  , 0.136124    ), Coef('Var'  , 0.146302    ), Coef('Var'  , 0.15768     ), Coef('Var'  , 0.141465    ), ], 
		[Coef('Var'  , 0.110132    ), Coef('Var'  , 0.106113    ), Coef('Var'  , 0.102535    ), Coef('Var'  , 0.11728     ), Coef('Var'  , 0.133482    ), Coef('Var'  , 0.130832    ), Coef('Var'  , 0.129928    ), Coef('Var'  , 0.119665    ), ], 
		[Coef('Var'  , 0.0946299   ), Coef('Var'  , 0.0942412   ), Coef('Var'  , 0.0913389   ), Coef('Var'  , 0.095493    ), Coef('Var'  , 0.0975471   ), Coef('Var'  , 0.0952072   ), Coef('Var'  , 0.0908435   ), Coef('Var'  , 0.0939554   ), ], ])
	etat7.initMat[Chem([Sub('G')])] = FMat([
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], ])
	etat7.initMat[Chem([Sub('8')])] = FMat([
		[Coef('Var'  , 0.10498     ), Coef('Var'  , 0.107375    ), Coef('Var'  , 0.108338    ), Coef('Var'  , 0.0933226   ), Coef('Var'  , 0.0773465   ), Coef('Var'  , 0.0818902   ), Coef('Var'  , 0.0852632   ), Coef('Var'  , 0.0959422   ), ], 
		[Coef('Var'  , 0.13183     ), Coef('Var'  , 0.132791    ), Coef('Var'  , 0.133061    ), Coef('Var'  , 0.111677    ), Coef('Var'  , 0.0895656   ), Coef('Var'  , 0.0983128   ), Coef('Var'  , 0.106253    ), Coef('Var'  , 0.119427    ), ], 
		[Coef('Var'  , 0.164148    ), Coef('Var'  , 0.150905    ), Coef('Var'  , 0.140102    ), Coef('Var'  , 0.121661    ), Coef('Var'  , 0.104643    ), Coef('Var'  , 0.144464    ), Coef('Var'  , 0.185917    ), Coef('Var'  , 0.173708    ), ], 
		[Coef('Var'  , 0.128281    ), Coef('Var'  , 0.115057    ), Coef('Var'  , 0.102715    ), Coef('Var'  , 0.0928531   ), Coef('Var'  , 0.0831669   ), Coef('Var'  , 0.121837    ), Coef('Var'  , 0.161204    ), Coef('Var'  , 0.14404     ), ], 
		[Coef('Var'  , 0.136779    ), Coef('Var'  , 0.137369    ), Coef('Var'  , 0.137332    ), Coef('Var'  , 0.150433    ), Coef('Var'  , 0.162782    ), Coef('Var'  , 0.153996    ), Coef('Var'  , 0.144755    ), Coef('Var'  , 0.140931    ), ], 
		[Coef('Var'  , 0.132166    ), Coef('Var'  , 0.144319    ), Coef('Var'  , 0.15768     ), Coef('Var'  , 0.19988     ), Coef('Var'  , 0.243427    ), Coef('Var'  , 0.188769    ), Coef('Var'  , 0.13528     ), Coef('Var'  , 0.133208    ), ], 
		[Coef('Var'  , 0.111568    ), Coef('Var'  , 0.120426    ), Coef('Var'  , 0.129928    ), Coef('Var'  , 0.149919    ), Coef('Var'  , 0.171229    ), Coef('Var'  , 0.138906    ), Coef('Var'  , 0.107325    ), Coef('Var'  , 0.109413    ), ], 
		[Coef('Var'  , 0.0902475   ), Coef('Var'  , 0.091759    ), Coef('Var'  , 0.0908435   ), Coef('Var'  , 0.0802546   ), Coef('Var'  , 0.0678402   ), Coef('Var'  , 0.0718262   ), Coef('Var'  , 0.0740023   ), Coef('Var'  , 0.0833306   ), ], ])
	etat7.initMat[Chem([Sub('9')])] = FMat([
		[Coef('Var'  , 0.111685    ), Coef('Var'  , 0.106165    ), Coef('Var'  , 0.0992866   ), Coef('Var'  , 0.114197    ), Coef('Var'  , 0.128429    ), Coef('Var'  , 0.125627    ), Coef('Var'  , 0.122358    ), Coef('Var'  , 0.117594    ), ], 
		[Coef('Var'  , 0.152241    ), Coef('Var'  , 0.150558    ), Coef('Var'  , 0.148945    ), Coef('Var'  , 0.196523    ), Coef('Var'  , 0.244509    ), Coef('Var'  , 0.209886    ), Coef('Var'  , 0.175753    ), Coef('Var'  , 0.163921    ), ], 
		[Coef('Var'  , 0.183301    ), Coef('Var'  , 0.202857    ), Coef('Var'  , 0.225723    ), Coef('Var'  , 0.235677    ), Coef('Var'  , 0.248094    ), Coef('Var'  , 0.212873    ), Coef('Var'  , 0.179907    ), Coef('Var'  , 0.180053    ), ], 
		[Coef('Var'  , 0.12858     ), Coef('Var'  , 0.144401    ), Coef('Var'  , 0.161495    ), Coef('Var'  , 0.122179    ), Coef('Var'  , 0.0834397   ), Coef('Var'  , 0.0931947   ), Coef('Var'  , 0.103005    ), Coef('Var'  , 0.115417    ), ], 
		[Coef('Var'  , 0.125502    ), Coef('Var'  , 0.123936    ), Coef('Var'  , 0.121899    ), Coef('Var'  , 0.10218     ), Coef('Var'  , 0.0817311   ), Coef('Var'  , 0.0986217   ), Coef('Var'  , 0.114481    ), Coef('Var'  , 0.120377    ), ], 
		[Coef('Var'  , 0.109599    ), Coef('Var'  , 0.0988243   ), Coef('Var'  , 0.088222    ), Coef('Var'  , 0.0807139   ), Coef('Var'  , 0.0732023   ), Coef('Var'  , 0.0918255   ), Coef('Var'  , 0.110622    ), Coef('Var'  , 0.109936    ), ], 
		[Coef('Var'  , 0.0984522   ), Coef('Var'  , 0.0894195   ), Coef('Var'  , 0.0799329   ), Coef('Var'  , 0.0759365   ), Coef('Var'  , 0.0719279   ), Coef('Var'  , 0.0869495   ), Coef('Var'  , 0.102535    ), Coef('Var'  , 0.100433    ), ], 
		[Coef('Var'  , 0.0906393   ), Coef('Var'  , 0.0838396   ), Coef('Var'  , 0.0744968   ), Coef('Var'  , 0.072593    ), Coef('Var'  , 0.0686675   ), Coef('Var'  , 0.0810222   ), Coef('Var'  , 0.0913389   ), Coef('Var'  , 0.0922688   ), ], ])
	etat7.initMat[Chem([Sub('10')])] = FMat([
		[Coef('Var'  , 0.10277     ), Coef('Var'  , 0.0948485   ), Coef('Var'  , 0.0852632   ), Coef('Var'  , 0.0669039   ), Coef('Var'  , 0.047327    ), Coef('Var'  , 0.0738326   ), Coef('Var'  , 0.0992866   ), Coef('Var'  , 0.101777    ), ], 
		[Coef('Var'  , 0.135415    ), Coef('Var'  , 0.121142    ), Coef('Var'  , 0.106253    ), Coef('Var'  , 0.0854176   ), Coef('Var'  , 0.0640818   ), Coef('Var'  , 0.106532    ), Coef('Var'  , 0.148945    ), Coef('Var'  , 0.142256    ), ], 
		[Coef('Var'  , 0.184954    ), Coef('Var'  , 0.183986    ), Coef('Var'  , 0.185917    ), Coef('Var'  , 0.24384     ), Coef('Var'  , 0.303771    ), Coef('Var'  , 0.263568    ), Coef('Var'  , 0.225723    ), Coef('Var'  , 0.203715    ), ], 
		[Coef('Var'  , 0.142538    ), Coef('Var'  , 0.151083    ), Coef('Var'  , 0.161204    ), Coef('Var'  , 0.229122    ), Coef('Var'  , 0.298206    ), Coef('Var'  , 0.2293      ), Coef('Var'  , 0.161495    ), Coef('Var'  , 0.151261    ), ], 
		[Coef('Var'  , 0.132735    ), Coef('Var'  , 0.138875    ), Coef('Var'  , 0.144755    ), Coef('Var'  , 0.144938    ), Coef('Var'  , 0.144963    ), Coef('Var'  , 0.133553    ), Coef('Var'  , 0.121899    ), Coef('Var'  , 0.12749     ), ], 
		[Coef('Var'  , 0.115442    ), Coef('Var'  , 0.124974    ), Coef('Var'  , 0.13528     ), Coef('Var'  , 0.0950925   ), Coef('Var'  , 0.0555106   ), Coef('Var'  , 0.0717959   ), Coef('Var'  , 0.088222    ), Coef('Var'  , 0.101678    ), ], 
		[Coef('Var'  , 0.099888    ), Coef('Var'  , 0.103732    ), Coef('Var'  , 0.107325    ), Coef('Var'  , 0.0773291   ), Coef('Var'  , 0.047179    ), Coef('Var'  , 0.0637769   ), Coef('Var'  , 0.0799329   ), Coef('Var'  , 0.0901801   ), ], 
		[Coef('Var'  , 0.0862568   ), Coef('Var'  , 0.0813582   ), Coef('Var'  , 0.0740023   ), Coef('Var'  , 0.0573566   ), Coef('Var'  , 0.0389621   ), Coef('Var'  , 0.0576417   ), Coef('Var'  , 0.0744968   ), Coef('Var'  , 0.0816433   ), ], ])
	etat7.initMat[Chem([Sub('11')])] = FMat([
		[Coef('Var'  , 0.111652    ), Coef('Var'  , 0.121073    ), Coef('Var'  , 0.130669    ), Coef('Var'  , 0.155039    ), Coef('Var'  , 0.180046    ), Coef('Var'  , 0.185977    ), Coef('Var'  , 0.193639    ), Coef('Var'  , 0.168311    ), Coef('Var'  , 0.144863    ), Coef('Var'  , 0.127763    ), ], 
		[Coef('Var'  , 0.11482     ), Coef('Var'  , 0.137005    ), Coef('Var'  , 0.158884    ), Coef('Var'  , 0.185235    ), Coef('Var'  , 0.212145    ), Coef('Var'  , 0.19926     ), Coef('Var'  , 0.187291    ), Coef('Var'  , 0.159203    ), Coef('Var'  , 0.131406    ), Coef('Var'  , 0.123333    ), ], 
		[Coef('Var'  , 0.0980182   ), Coef('Var'  , 0.119356    ), Coef('Var'  , 0.140977    ), Coef('Var'  , 0.146365    ), Coef('Var'  , 0.152446    ), Coef('Var'  , 0.131178    ), Coef('Var'  , 0.10952     ), Coef('Var'  , 0.0992749   ), Coef('Var'  , 0.0877384   ), Coef('Var'  , 0.0933799   ), ], 
		[Coef('Var'  , 0.0686826   ), Coef('Var'  , 0.0786294   ), Coef('Var'  , 0.0871397   ), Coef('Var'  , 0.0786143   ), Coef('Var'  , 0.068667    ), Coef('Var'  , 0.0630729   ), Coef('Var'  , 0.0551723   ), Coef('Var'  , 0.0566241   ), Coef('Var'  , 0.0552464   ), Coef('Var'  , 0.0631372   ), ], 
		[Coef('Var'  , 0.11491     ), Coef('Var'  , 0.115898    ), Coef('Var'  , 0.115177    ), Coef('Var'  , 0.10085     ), Coef('Var'  , 0.0845196   ), Coef('Var'  , 0.082047    ), Coef('Var'  , 0.0768939   ), Coef('Var'  , 0.0843004   ), Coef('Var'  , 0.0888925   ), Coef('Var'  , 0.103003    ), ], 
		[Coef('Var'  , 0.187972    ), Coef('Var'  , 0.161348    ), Coef('Var'  , 0.136124    ), Coef('Var'  , 0.11486     ), Coef('Var'  , 0.0942528   ), Coef('Var'  , 0.100903    ), Coef('Var'  , 0.107985    ), Coef('Var'  , 0.132611    ), Coef('Var'  , 0.158257    ), Coef('Var'  , 0.172323    ), ], 
		[Coef('Var'  , 0.205734    ), Coef('Var'  , 0.168125    ), Coef('Var'  , 0.133482    ), Coef('Var'  , 0.119892    ), Coef('Var'  , 0.108731    ), Coef('Var'  , 0.127439    ), Coef('Var'  , 0.149383    ), Coef('Var'  , 0.179597    ), Coef('Var'  , 0.214044    ), Coef('Var'  , 0.207849    ), ], 
		[Coef('Var'  , 0.0982116   ), Coef('Var'  , 0.0985664   ), Coef('Var'  , 0.0975471   ), Coef('Var'  , 0.0991436   ), Coef('Var'  , 0.0991924   ), Coef('Var'  , 0.110122    ), Coef('Var'  , 0.120116    ), Coef('Var'  , 0.120079    ), Coef('Var'  , 0.119553    ), Coef('Var'  , 0.109213    ), ], ])
	etat7.initMat[Chem([Sub('12')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 6.98338e-18 ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 6.88921e-18 ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.0625      ), Coef('Var'  , 0.03125     ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Const', 0.375       ), Coef('Var'  , 0.1875      ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 1           ), Coef('Const', 0.75        ), Coef('Const', 0.5625      ), Coef('Var'  , 0.5625      ), Coef('Const', 0.5625      ), Coef('Const', 0.75        ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.1875      ), Coef('Const', 0.375       ), Coef('Const', 0.25        ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.03125     ), Coef('Const', 0.0625      ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 6.92873e-18 ), Coef('Const', 0           ), Coef('Const', 0           ), ], ])
	etat7.initMat[Chem([Sub('13')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 5.73373e-06 ), Coef('Var'  , 7.08728e-06 ), Coef('Var'  , 5.73373e-06 ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 4.19876e-06 ), Coef('Var'  , 5.18995e-06 ), Coef('Var'  , 4.19876e-06 ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0390629   ), Coef('Var'  , 0.0781255   ), Coef('Var'  , 0.0390629   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.10937     ), Coef('Var'  , 0.218744    ), Coef('Var'  , 0.10937     ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0.375       ), Coef('Const', 0.5625      ), Coef('Var'  , 0.484366    ), Coef('Var'  , 0.406238    ), Coef('Var'  , 0.328116    ), ], 
		[Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0.375       ), Coef('Var'  , 0.296873    ), Coef('Var'  , 0.218748    ), Coef('Var'  , 0.359373    ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0.125       ), Coef('Const', 0.0625      ), Coef('Var'  , 0.0703143   ), Coef('Var'  , 0.0781272   ), Coef('Var'  , 0.164064    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 3.50025e-06 ), Coef('Var'  , 4.32654e-06 ), Coef('Var'  , 3.50025e-06 ), ], ])
	etat7.initMat[Chem([Sub('14')])] = FMat([
		[Coef('Const', 0           ), Coef('Var'  , 5.73373e-06 ), Coef('Var'  , 7.08728e-06 ), Coef('Var'  , 5.73373e-06 ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 4.19876e-06 ), Coef('Var'  , 5.18995e-06 ), Coef('Var'  , 4.19876e-06 ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.25        ), Coef('Var'  , 0.164063    ), Coef('Var'  , 0.0781255   ), Coef('Var'  , 0.0703129   ), Coef('Const', 0.0625      ), Coef('Const', 0.125       ), ], 
		[Coef('Const', 0.5         ), Coef('Var'  , 0.35937     ), Coef('Var'  , 0.218744    ), Coef('Var'  , 0.29687     ), Coef('Const', 0.375       ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0.25        ), Coef('Var'  , 0.328116    ), Coef('Var'  , 0.406238    ), Coef('Var'  , 0.484366    ), Coef('Const', 0.5625      ), Coef('Const', 0.375       ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.109373    ), Coef('Var'  , 0.218748    ), Coef('Var'  , 0.109373    ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0390643   ), Coef('Var'  , 0.0781272   ), Coef('Var'  , 0.0390643   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 3.50025e-06 ), Coef('Var'  , 4.32654e-06 ), Coef('Var'  , 3.50025e-06 ), Coef('Const', 0           ), Coef('Const', 0           ), ], ])
	etat7.initMat[Chem([Sub('15')])] = FMat([
		[Coef('Var'  , 0.186925    ), Coef('Var'  , 0.189267    ), Coef('Var'  , 0.193639    ), Coef('Var'  , 0.232974    ), Coef('Var'  , 0.274209    ), Coef('Var'  , 0.280031    ), Coef('Var'  , 0.287285    ), Coef('Var'  , 0.236324    ), ], 
		[Coef('Var'  , 0.146539    ), Coef('Var'  , 0.166658    ), Coef('Var'  , 0.187291    ), Coef('Var'  , 0.224731    ), Coef('Var'  , 0.263035    ), Coef('Var'  , 0.237627    ), Coef('Var'  , 0.212922    ), Coef('Var'  , 0.179554    ), ], 
		[Coef('Var'  , 0.0791134   ), Coef('Var'  , 0.0949418   ), Coef('Var'  , 0.10952     ), Coef('Var'  , 0.111702    ), Coef('Var'  , 0.113091    ), Coef('Var'  , 0.0951713   ), Coef('Var'  , 0.0766818   ), Coef('Var'  , 0.0784115   ), ], 
		[Coef('Var'  , 0.0423232   ), Coef('Var'  , 0.0501025   ), Coef('Var'  , 0.0551723   ), Coef('Var'  , 0.0482637   ), Coef('Var'  , 0.0390363   ), Coef('Var'  , 0.031426    ), Coef('Var'  , 0.0222173   ), Coef('Var'  , 0.0332649   ), ], 
		[Coef('Var'  , 0.0665218   ), Coef('Var'  , 0.0731033   ), Coef('Var'  , 0.0768939   ), Coef('Var'  , 0.0653204   ), Coef('Var'  , 0.0511677   ), Coef('Var'  , 0.042241    ), Coef('Var'  , 0.0314752   ), Coef('Var'  , 0.0500239   ), ], 
		[Coef('Var'  , 0.121515    ), Coef('Var'  , 0.114391    ), Coef('Var'  , 0.107985    ), Coef('Var'  , 0.0846595   ), Coef('Var'  , 0.0616857   ), Coef('Var'  , 0.0535316   ), Coef('Var'  , 0.0455071   ), Coef('Var'  , 0.0832627   ), ], 
		[Coef('Var'  , 0.201992    ), Coef('Var'  , 0.173748    ), Coef('Var'  , 0.149383    ), Coef('Var'  , 0.12047     ), Coef('Var'  , 0.0947033   ), Coef('Var'  , 0.113362    ), Coef('Var'  , 0.134117    ), Coef('Var'  , 0.166639    ), ], 
		[Coef('Var'  , 0.155071    ), Coef('Var'  , 0.137788    ), Coef('Var'  , 0.120116    ), Coef('Var'  , 0.111879    ), Coef('Var'  , 0.103073    ), Coef('Var'  , 0.146611    ), Coef('Var'  , 0.189794    ), Coef('Var'  , 0.17252     ), ], ])
	etat7.initMat[Chem([Sub('16')])] = FMat([
		[Coef('Const', 0.25        ), Coef('Var'  , 0.268336    ), Coef('Var'  , 0.287285    ), Coef('Var'  , 0.365558    ), Coef('Const', 0.444444    ), Coef('Const', 0.666667    ), Coef('Const', 1           ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.106345    ), Coef('Var'  , 0.212922    ), Coef('Var'  , 0.328567    ), Coef('Const', 0.444444    ), Coef('Const', 0.333333    ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0385015   ), Coef('Var'  , 0.0766818   ), Coef('Var'  , 0.094057    ), Coef('Const', 0.111111    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0114498   ), Coef('Var'  , 0.0222173   ), Coef('Var'  , 0.0114498   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0161167   ), Coef('Var'  , 0.0314752   ), Coef('Var'  , 0.0161167   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0227119   ), Coef('Var'  , 0.0455071   ), Coef('Var'  , 0.022712    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.25        ), Coef('Var'  , 0.191601    ), Coef('Var'  , 0.134117    ), Coef('Var'  , 0.0666014   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.5         ), Coef('Var'  , 0.344937    ), Coef('Var'  , 0.189794    ), Coef('Var'  , 0.0949373   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), ], ])
	
	
	
	etat8.bords   = {Bord('0'): etat21, Bord('1'): etat21, Bord('2'): etat20, }
	etat8.permuts = {}
	etat8.interns = {Intern('_'): etat8, }
	etat8.subs    = {Sub('0'): etat1, Sub('1'): etat2, Sub('2'): etat3, Sub('3'): etat4, Sub('4'): etat5, Sub('5'): etat6, Sub('6'): etat7, Sub('7'): etat9, Sub('G', True): Etat.etatPoint, Sub('8'): etat10, Sub('9'): etat11, Sub('10'): etat12, Sub('11'): etat13, Sub('12'): etat14, Sub('13'): etat15, Sub('14'): etat16, Sub('15'): etat17, Sub('16'): etat18, }
	
	etat8.buildIntern()
	
	
	etat8.eqs = [
		(Chem([Bord('0'), Sub('0'), Permut('0'), ])	,	Chem([Sub('2'), Bord('2'), ])),
		(Chem([Bord('2'), Sub('2'), Permut('0'), ])	,	Chem([Sub('2'), Bord('3'), ])),
		(Chem([Bord('1'), Sub('0'), Permut('0'), ])	,	Chem([Sub('5'), Bord('1'), ])),
		(Chem([Bord('0'), Sub('3'), Permut('0'), ])	,	Chem([Sub('5'), Bord('2'), ])),
		(Chem([Bord('2'), Sub('0'), Permut('0'), ])	,	Chem([Sub('6'), Bord('0'), ])),
		(Chem([Bord('1'), Sub('3'), Permut('0'), ])	,	Chem([Sub('6'), Bord('1'), ])),
		(Chem([Bord('0'), Sub('1'), Permut('0'), ])	,	Chem([Sub('9'), Bord('1'), ])),
		(Chem([Bord('0'), Sub('2'), Permut('0'), ])	,	Chem([Sub('10'), Bord('2'), ])),
		(Chem([Bord('1'), Sub('2'), Permut('0'), ])	,	Chem([Sub('12'), Bord('0'), ])),
		(Chem([Bord('1'), Sub('1'), Permut('0'), ])	,	Chem([Sub('14'), Bord('2'), ])),
		(Chem([Bord('2'), Sub('1'), Permut('0'), ])	,	Chem([Sub('16'), Bord('2'), ])),
		(Chem([Sub('0'), Bord('0'), Bord('1'), ])	,	Chem([Sub('11'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('1'), Bord('1'), ])	,	Chem([Sub('15'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('2'), Bord('1'), ])	,	Chem([Sub('3'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('3'), Bord('1'), ])	,	Chem([Sub('1'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('0'), Bord('1'), ])	,	Chem([Sub('11'), Bord('4'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('2'), Bord('1'), ])	,	Chem([Sub('3'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('3'), Bord('1'), ])	,	Chem([Sub('13'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('4'), Bord('1'), ])	,	Chem([Sub('8'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('0'), Bord('1'), ])	,	Chem([Sub('11'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('1'), Bord('1'), ])	,	Chem([Sub('9'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('3'), Bord('1'), ])	,	Chem([Sub('16'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('4'), Bord('1'), ])	,	Chem([Sub('15'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('3'), Bord('1'), Bord('1'), ])	,	Chem([Sub('16'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('3'), Bord('2'), Bord('1'), ])	,	Chem([Sub('6'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('4'), Bord('0'), Bord('1'), ])	,	Chem([Sub('7'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('4'), Bord('1'), Bord('1'), ])	,	Chem([Sub('8'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('4'), Bord('2'), Bord('1'), ])	,	Chem([Sub('10'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('4'), Bord('3'), Bord('1'), ])	,	Chem([Sub('9'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('5'), Bord('0'), Bord('1'), ])	,	Chem([Sub('14'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('5'), Bord('2'), Bord('1'), ])	,	Chem([Sub('10'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('6'), Bord('1'), Bord('1'), ])	,	Chem([Sub('12'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('6'), Bord('3'), Bord('1'), ])	,	Chem([Sub('16'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('7'), Bord('0'), Bord('1'), ])	,	Chem([Sub('9'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('7'), Bord('1'), Bord('1'), ])	,	Chem([Sub('11'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('7'), Bord('2'), Bord('1'), ])	,	Chem([Sub('8'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('8'), Bord('2'), Bord('1'), ])	,	Chem([Sub('10'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('9'), Bord('0'), Bord('1'), ])	,	Chem([Sub('10'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('11'), Bord('2'), Bord('1'), ])	,	Chem([Sub('15'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('12'), Bord('0'), Bord('1'), ])	,	Chem([Sub('14'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('12'), Bord('1'), Bord('1'), ])	,	Chem([Sub('13'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('13'), Bord('1'), Bord('1'), ])	,	Chem([Sub('14'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('15'), Bord('2'), Bord('1'), ])	,	Chem([Sub('16'), Bord('0'), Bord('1'), ])),
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
		[Coef('Var'  , 0.181513    ), Coef('Var'  , 0.199997    ), Coef('Var'  , 0.221913    ), Coef('Var'  , 0.229023    ), Coef('Var'  , 0.240053    ), Coef('Var'  , 0.20805     ), Coef('Var'  , 0.178995    ), Coef('Var'  , 0.179025    ), ], 
		[Coef('Var'  , 0.139119    ), Coef('Var'  , 0.147032    ), Coef('Var'  , 0.152991    ), Coef('Var'  , 0.141294    ), Coef('Var'  , 0.127558    ), Coef('Var'  , 0.120619    ), Coef('Var'  , 0.110897    ), Coef('Var'  , 0.126357    ), ], 
		[Coef('Var'  , 0.157409    ), Coef('Var'  , 0.155531    ), Coef('Var'  , 0.150464    ), Coef('Var'  , 0.139199    ), Coef('Var'  , 0.124297    ), Coef('Var'  , 0.12957     ), Coef('Var'  , 0.131157    ), Coef('Var'  , 0.145902    ), ], 
		[Coef('Var'  , 0.144461    ), Coef('Var'  , 0.135315    ), Coef('Var'  , 0.123896    ), Coef('Var'  , 0.117773    ), Coef('Var'  , 0.108859    ), Coef('Var'  , 0.122147    ), Coef('Var'  , 0.133301    ), Coef('Var'  , 0.139689    ), ], 
		[Coef('Var'  , 0.18493     ), Coef('Var'  , 0.166139    ), Coef('Var'  , 0.150354    ), Coef('Var'  , 0.155233    ), Coef('Var'  , 0.162947    ), Coef('Var'  , 0.189227    ), Coef('Var'  , 0.219079    ), Coef('Var'  , 0.200133    ), ], 
		[Coef('Var'  , 0.192568    ), Coef('Var'  , 0.195986    ), Coef('Var'  , 0.200383    ), Coef('Var'  , 0.21748     ), Coef('Var'  , 0.236285    ), Coef('Var'  , 0.230387    ), Coef('Var'  , 0.22657     ), Coef('Var'  , 0.208893    ), ], ])
	etat8.initMat[Chem([Sub('1')])] = FMat([
		[Coef('Var'  , 0.164244    ), Coef('Var'  , 0.183014    ), Coef('Var'  , 0.204754    ), Coef('Var'  , 0.191534    ), Coef('Var'  , 0.181513    ), Coef('Var'  , 0.15825     ), Coef('Var'  , 0.136882    ), Coef('Var'  , 0.113246    ), Coef('Var'  , 0.0901638   ), Coef('Var'  , 0.126608    ), ], 
		[Coef('Var'  , 0.201017    ), Coef('Var'  , 0.190182    ), Coef('Var'  , 0.180994    ), Coef('Var'  , 0.160472    ), Coef('Var'  , 0.139119    ), Coef('Var'  , 0.120538    ), Coef('Var'  , 0.0994876   ), Coef('Var'  , 0.0964047   ), Coef('Var'  , 0.0916382   ), Coef('Var'  , 0.145825    ), ], 
		[Coef('Var'  , 0.235721    ), Coef('Var'  , 0.208047    ), Coef('Var'  , 0.180002    ), Coef('Var'  , 0.169834    ), Coef('Var'  , 0.157409    ), Coef('Var'  , 0.155481    ), Coef('Var'  , 0.150905    ), Coef('Var'  , 0.190311    ), Coef('Var'  , 0.228555    ), Coef('Var'  , 0.231954    ), ], 
		[Coef('Var'  , 0.148161    ), Coef('Var'  , 0.140864    ), Coef('Var'  , 0.131593    ), Coef('Var'  , 0.139066    ), Coef('Var'  , 0.144461    ), Coef('Var'  , 0.162025    ), Coef('Var'  , 0.178544    ), Coef('Var'  , 0.22487     ), Coef('Var'  , 0.271382    ), Coef('Var'  , 0.20997     ), ], 
		[Coef('Var'  , 0.134551    ), Coef('Var'  , 0.137428    ), Coef('Var'  , 0.140489    ), Coef('Var'  , 0.161594    ), Coef('Var'  , 0.18493     ), Coef('Var'  , 0.215076    ), Coef('Var'  , 0.248756    ), Coef('Var'  , 0.235125    ), Coef('Var'  , 0.224105    ), Coef('Var'  , 0.179102    ), ], 
		[Coef('Var'  , 0.116305    ), Coef('Var'  , 0.140465    ), Coef('Var'  , 0.162167    ), Coef('Var'  , 0.1775      ), Coef('Var'  , 0.192568    ), Coef('Var'  , 0.188631    ), Coef('Var'  , 0.185424    ), Coef('Var'  , 0.140043    ), Coef('Var'  , 0.094156    ), Coef('Var'  , 0.106541    ), ], ])
	etat8.initMat[Chem([Sub('2')])] = FMat([
		[Coef('Var'  , 0.341757    ), Coef('Var'  , 0.349221    ), Coef('Var'  , 0.360223    ), Coef('Var'  , 0.460424    ), Coef('Const', 0.5625      ), Coef('Const', 0.75        ), Coef('Const', 1           ), Coef('Const', 0.666667    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.392269    ), ], 
		[Coef('Var'  , 0.114073    ), Coef('Var'  , 0.166627    ), Coef('Var'  , 0.219036    ), Coef('Var'  , 0.296904    ), Coef('Const', 0.375       ), Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.057223    ), ], 
		[Coef('Var'  , 0.0794783   ), Coef('Var'  , 0.0959741   ), Coef('Var'  , 0.11025     ), Coef('Var'  , 0.0868571   ), Coef('Const', 0.0625      ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0403671   ), ], 
		[Coef('Var'  , 0.060693    ), Coef('Var'  , 0.0648965   ), Coef('Var'  , 0.0664755   ), Coef('Var'  , 0.0339251   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0309715   ), ], 
		[Coef('Var'  , 0.122739    ), Coef('Var'  , 0.104367    ), Coef('Var'  , 0.0867084   ), Coef('Var'  , 0.043277    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.111111    ), Coef('Var'  , 0.116646    ), ], 
		[Coef('Var'  , 0.281261    ), Coef('Var'  , 0.218915    ), Coef('Var'  , 0.157307    ), Coef('Var'  , 0.0786127   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.333333    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.362524    ), ], ])
	etat8.initMat[Chem([Sub('3')])] = FMat([
		[Coef('Var'  , 0.136882    ), Coef('Var'  , 0.157142    ), Coef('Var'  , 0.178995    ), Coef('Var'  , 0.173934    ), Coef('Var'  , 0.170577    ), Coef('Var'  , 0.136827    ), Coef('Var'  , 0.103912    ), Coef('Var'  , 0.120035    ), ], 
		[Coef('Var'  , 0.0994876   ), Coef('Var'  , 0.106647    ), Coef('Var'  , 0.110897    ), Coef('Var'  , 0.0870886   ), Coef('Var'  , 0.0606294   ), Coef('Var'  , 0.0523803   ), Coef('Var'  , 0.0422187   ), Coef('Var'  , 0.0719383   ), ], 
		[Coef('Var'  , 0.150905    ), Coef('Var'  , 0.142472    ), Coef('Var'  , 0.131157    ), Coef('Var'  , 0.103406    ), Coef('Var'  , 0.0727037   ), Coef('Var'  , 0.0741002   ), Coef('Var'  , 0.0735429   ), Coef('Var'  , 0.113166    ), ], 
		[Coef('Var'  , 0.178544    ), Coef('Var'  , 0.156388    ), Coef('Var'  , 0.133301    ), Coef('Var'  , 0.113485    ), Coef('Var'  , 0.0923791   ), Coef('Var'  , 0.127513    ), Coef('Var'  , 0.161964    ), Coef('Var'  , 0.170416    ), ], 
		[Coef('Var'  , 0.248756    ), Coef('Var'  , 0.231991    ), Coef('Var'  , 0.219079    ), Coef('Var'  , 0.25874     ), Coef('Var'  , 0.301795    ), Coef('Var'  , 0.342939    ), Coef('Var'  , 0.386521    ), Coef('Var'  , 0.316189    ), ], 
		[Coef('Var'  , 0.185424    ), Coef('Var'  , 0.20536     ), Coef('Var'  , 0.22657     ), Coef('Var'  , 0.263347    ), Coef('Var'  , 0.301916    ), Coef('Var'  , 0.266241    ), Coef('Var'  , 0.231842    ), Coef('Var'  , 0.208255    ), ], ])
	etat8.initMat[Chem([Sub('4')])] = FMat([
		[Coef('Var'  , 0.257269    ), Coef('Var'  , 0.250909    ), Coef('Var'  , 0.247565    ), Coef('Var'  , 0.224718    ), Coef('Var'  , 0.205177    ), Coef('Var'  , 0.208749    ), Coef('Var'  , 0.21488     ), Coef('Var'  , 0.23494     ), ], 
		[Coef('Var'  , 0.357827    ), Coef('Var'  , 0.322295    ), Coef('Var'  , 0.292222    ), Coef('Var'  , 0.288118    ), Coef('Var'  , 0.290213    ), Coef('Var'  , 0.320366    ), Coef('Var'  , 0.355819    ), Coef('Var'  , 0.354544    ), ], 
		[Coef('Var'  , 0.218764    ), Coef('Var'  , 0.213255    ), Coef('Var'  , 0.20903     ), Coef('Var'  , 0.227986    ), Coef('Var'  , 0.248679    ), Coef('Var'  , 0.252673    ), Coef('Var'  , 0.258413    ), Coef('Var'  , 0.237943    ), ], 
		[Coef('Var'  , 0.0521852   ), Coef('Var'  , 0.0674561   ), Coef('Var'  , 0.079948    ), Coef('Var'  , 0.0830028   ), Coef('Var'  , 0.0829782   ), Coef('Var'  , 0.0703438   ), Coef('Var'  , 0.0552154   ), Coef('Var'  , 0.0547971   ), ], 
		[Coef('Var'  , 0.0504775   ), Coef('Var'  , 0.0649898   ), Coef('Var'  , 0.0767491   ), Coef('Var'  , 0.0795681   ), Coef('Var'  , 0.0792426   ), Coef('Var'  , 0.0674799   ), Coef('Var'  , 0.052971    ), Coef('Var'  , 0.0529016   ), ], 
		[Coef('Var'  , 0.0634776   ), Coef('Var'  , 0.081094    ), Coef('Var'  , 0.0944858   ), Coef('Var'  , 0.096607    ), Coef('Var'  , 0.0937099   ), Coef('Var'  , 0.0803875   ), Coef('Var'  , 0.0627017   ), Coef('Var'  , 0.0648745   ), ], ])
	etat8.initMat[Chem([Sub('5')])] = FMat([
		[Coef('Const', 0.0625      ), Coef('Var'  , 0.03125     ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.375       ), Coef('Var'  , 0.1875      ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), ], 
		[Coef('Const', 0.5625      ), Coef('Var'  , 0.5625      ), Coef('Const', 0.5625      ), Coef('Const', 0.75        ), Coef('Const', 1           ), Coef('Const', 0.75        ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.1875      ), Coef('Const', 0.375       ), Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.03125     ), Coef('Const', 0.0625      ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  ,-4.26059e-18 ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], ])
	etat8.initMat[Chem([Sub('6')])] = FMat([
		[Coef('Const', 0.111111    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0518512   ), Coef('Var'  , 0.103912    ), Coef('Var'  , 0.107407    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0215248   ), Coef('Var'  , 0.0422187   ), Coef('Var'  , 0.0215249   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.0625      ), Coef('Var'  , 0.0683906   ), Coef('Var'  , 0.0735429   ), Coef('Var'  , 0.0371407   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Const', 0.375       ), Coef('Var'  , 0.268555    ), Coef('Var'  , 0.161964    ), Coef('Var'  , 0.0810549   ), ], 
		[Coef('Const', 0.444444    ), Coef('Const', 0.666667    ), Coef('Const', 1           ), Coef('Const', 0.75        ), Coef('Const', 0.5625      ), Coef('Var'  , 0.473972    ), Coef('Var'  , 0.386521    ), Coef('Var'  , 0.414944    ), ], 
		[Coef('Const', 0.444444    ), Coef('Const', 0.333333    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.115706    ), Coef('Var'  , 0.231842    ), Coef('Var'  , 0.337928    ), ], ])
	etat8.initMat[Chem([Sub('7')])] = FMat([
		[Coef('Var'  , 0.247565    ), Coef('Var'  , 0.287485    ), Coef('Var'  , 0.330692    ), Coef('Var'  , 0.299722    ), Coef('Var'  , 0.272361    ), Coef('Var'  , 0.242763    ), Coef('Var'  , 0.217092    ), Coef('Var'  , 0.230526    ), ], 
		[Coef('Var'  , 0.292222    ), Coef('Var'  , 0.297849    ), Coef('Var'  , 0.308804    ), Coef('Var'  , 0.269602    ), Coef('Var'  , 0.234269    ), Coef('Var'  , 0.23828     ), Coef('Var'  , 0.24674     ), Coef('Var'  , 0.266527    ), ], 
		[Coef('Var'  , 0.20903     ), Coef('Var'  , 0.18577     ), Coef('Var'  , 0.163559    ), Coef('Var'  , 0.165417    ), Coef('Var'  , 0.167381    ), Coef('Var'  , 0.190172    ), Coef('Var'  , 0.213444    ), Coef('Var'  , 0.210526    ), ], 
		[Coef('Var'  , 0.079948    ), Coef('Var'  , 0.0717035   ), Coef('Var'  , 0.0605506   ), Coef('Var'  , 0.0795207   ), Coef('Var'  , 0.0956108   ), Coef('Var'  , 0.10239     ), Coef('Var'  , 0.106048    ), Coef('Var'  , 0.0945732   ), ], 
		[Coef('Var'  , 0.0767491   ), Coef('Var'  , 0.0693208   ), Coef('Var'  , 0.0592662   ), Coef('Var'  , 0.0796379   ), Coef('Var'  , 0.0983558   ), Coef('Var'  , 0.100491    ), Coef('Var'  , 0.100734    ), Coef('Var'  , 0.0901736   ), ], 
		[Coef('Var'  , 0.0944858   ), Coef('Var'  , 0.087872    ), Coef('Var'  , 0.0771278   ), Coef('Var'  , 0.1061      ), Coef('Var'  , 0.132022    ), Coef('Var'  , 0.125903    ), Coef('Var'  , 0.115942    ), Coef('Var'  , 0.107675    ), ], ])
	etat8.initMat[Chem([Sub('G')])] = FMat([
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], ])
	etat8.initMat[Chem([Sub('8')])] = FMat([
		[Coef('Var'  , 0.205177    ), Coef('Var'  , 0.209446    ), Coef('Var'  , 0.217092    ), Coef('Var'  , 0.189173    ), Coef('Var'  , 0.164244    ), Coef('Var'  , 0.160499    ), Coef('Var'  , 0.158865    ), Coef('Var'  , 0.180773    ), ], 
		[Coef('Var'  , 0.290213    ), Coef('Var'  , 0.265562    ), Coef('Var'  , 0.24674     ), Coef('Var'  , 0.221819    ), Coef('Var'  , 0.201017    ), Coef('Var'  , 0.248828    ), Coef('Var'  , 0.299979    ), Coef('Var'  , 0.292571    ), ], 
		[Coef('Var'  , 0.248679    ), Coef('Var'  , 0.230234    ), Coef('Var'  , 0.213444    ), Coef('Var'  , 0.224056    ), Coef('Var'  , 0.235721    ), Coef('Var'  , 0.279447    ), Coef('Var'  , 0.324332    ), Coef('Var'  , 0.285626    ), ], 
		[Coef('Var'  , 0.0829782   ), Coef('Var'  , 0.096017    ), Coef('Var'  , 0.106048    ), Coef('Var'  , 0.128255    ), Coef('Var'  , 0.148161    ), Coef('Var'  , 0.111988    ), Coef('Var'  , 0.0741605   ), Coef('Var'  , 0.0797496   ), ], 
		[Coef('Var'  , 0.0792426   ), Coef('Var'  , 0.0914186   ), Coef('Var'  , 0.100734    ), Coef('Var'  , 0.118456    ), Coef('Var'  , 0.134551    ), Coef('Var'  , 0.102614    ), Coef('Var'  , 0.0693566   ), Coef('Var'  , 0.0755769   ), ], 
		[Coef('Var'  , 0.0937099   ), Coef('Var'  , 0.107322    ), Coef('Var'  , 0.115942    ), Coef('Var'  , 0.118242    ), Coef('Var'  , 0.116305    ), Coef('Var'  , 0.0966243   ), Coef('Var'  , 0.0733068   ), Coef('Var'  , 0.0857039   ), ], ])
	etat8.initMat[Chem([Sub('9')])] = FMat([
		[Coef('Var'  , 0.257269    ), Coef('Var'  , 0.25301     ), Coef('Const', 0.25        ), Coef('Const', 0.375       ), Coef('Const', 0.5625      ), Coef('Var'  , 0.445836    ), Coef('Var'  , 0.330692    ), Coef('Var'  , 0.292596    ), ], 
		[Coef('Var'  , 0.357827    ), Coef('Var'  , 0.427754    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0.375       ), Coef('Var'  , 0.340807    ), Coef('Var'  , 0.308804    ), Coef('Var'  , 0.331061    ), ], 
		[Coef('Var'  , 0.218764    ), Coef('Var'  , 0.234117    ), Coef('Const', 0.25        ), Coef('Const', 0.125       ), Coef('Const', 0.0625      ), Coef('Var'  , 0.112882    ), Coef('Var'  , 0.163559    ), Coef('Var'  , 0.190749    ), ], 
		[Coef('Var'  , 0.0521852   ), Coef('Var'  , 0.0266766   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.030924    ), Coef('Var'  , 0.0605506   ), Coef('Var'  , 0.0576006   ), ], 
		[Coef('Var'  , 0.0504775   ), Coef('Var'  , 0.0258283   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0301592   ), Coef('Var'  , 0.0592662   ), Coef('Var'  , 0.0559875   ), ], 
		[Coef('Var'  , 0.0634776   ), Coef('Var'  , 0.0326139   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0393918   ), Coef('Var'  , 0.0771278   ), Coef('Var'  , 0.0720057   ), ], ])
	etat8.initMat[Chem([Sub('10')])] = FMat([
		[Coef('Var'  , 0.21488     ), Coef('Var'  , 0.185884    ), Coef('Var'  , 0.158865    ), Coef('Var'  , 0.110204    ), Coef('Const', 0.0625      ), Coef('Const', 0.125       ), Coef('Const', 0.25        ), Coef('Var'  , 0.23193     ), ], 
		[Coef('Var'  , 0.355819    ), Coef('Var'  , 0.325783    ), Coef('Var'  , 0.299979    ), Coef('Var'  , 0.336494    ), Coef('Const', 0.375       ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.42679     ), ], 
		[Coef('Var'  , 0.258413    ), Coef('Var'  , 0.290605    ), Coef('Var'  , 0.324332    ), Coef('Var'  , 0.443029    ), Coef('Const', 0.5625      ), Coef('Const', 0.375       ), Coef('Const', 0.25        ), Coef('Var'  , 0.253826    ), ], 
		[Coef('Var'  , 0.0552154   ), Coef('Var'  , 0.0656468   ), Coef('Var'  , 0.0741605   ), Coef('Var'  , 0.0375263   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0281205   ), ], 
		[Coef('Var'  , 0.052971    ), Coef('Var'  , 0.0622436   ), Coef('Var'  , 0.0693566   ), Coef('Var'  , 0.0351703   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0270733   ), ], 
		[Coef('Var'  , 0.0627017   ), Coef('Var'  , 0.0698376   ), Coef('Var'  , 0.0733068   ), Coef('Var'  , 0.037577    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0322606   ), ], ])
	etat8.initMat[Chem([Sub('11')])] = FMat([
		[Coef('Var'  , 0.204754    ), Coef('Var'  , 0.236604    ), Coef('Var'  , 0.272361    ), Coef('Var'  , 0.31431     ), Coef('Var'  , 0.360223    ), Coef('Var'  , 0.320428    ), Coef('Var'  , 0.284756    ), Coef('Var'  , 0.251184    ), Coef('Var'  , 0.221913    ), Coef('Var'  , 0.211399    ), ], 
		[Coef('Var'  , 0.180994    ), Coef('Var'  , 0.206643    ), Coef('Var'  , 0.234269    ), Coef('Var'  , 0.225699    ), Coef('Var'  , 0.219036    ), Coef('Var'  , 0.187331    ), Coef('Var'  , 0.155212    ), Coef('Var'  , 0.154835    ), Coef('Var'  , 0.152991    ), Coef('Var'  , 0.167256    ), ], 
		[Coef('Var'  , 0.180002    ), Coef('Var'  , 0.174164    ), Coef('Var'  , 0.167381    ), Coef('Var'  , 0.139392    ), Coef('Var'  , 0.11025     ), Coef('Var'  , 0.116963    ), Coef('Var'  , 0.120972    ), Coef('Var'  , 0.137431    ), Coef('Var'  , 0.150464    ), Coef('Var'  , 0.166454    ), ], 
		[Coef('Var'  , 0.131593    ), Coef('Var'  , 0.115       ), Coef('Var'  , 0.0956108   ), Coef('Var'  , 0.0825218   ), Coef('Var'  , 0.0664755   ), Coef('Var'  , 0.0819879   ), Coef('Var'  , 0.0944973   ), Coef('Var'  , 0.110715    ), Coef('Var'  , 0.123896    ), Coef('Var'  , 0.129055    ), ], 
		[Coef('Var'  , 0.140489    ), Coef('Var'  , 0.119463    ), Coef('Var'  , 0.0983558   ), Coef('Var'  , 0.0927557   ), Coef('Var'  , 0.0867084   ), Coef('Var'  , 0.10679     ), Coef('Var'  , 0.127955    ), Coef('Var'  , 0.138043    ), Coef('Var'  , 0.150354    ), Coef('Var'  , 0.144514    ), ], 
		[Coef('Var'  , 0.162167    ), Coef('Var'  , 0.148126    ), Coef('Var'  , 0.132022    ), Coef('Var'  , 0.145321    ), Coef('Var'  , 0.157307    ), Coef('Var'  , 0.186501    ), Coef('Var'  , 0.216608    ), Coef('Var'  , 0.207792    ), Coef('Var'  , 0.200383    ), Coef('Var'  , 0.181322    ), ], ])
	etat8.initMat[Chem([Sub('12')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0154679   ), Coef('Var'  , 0.0306894   ), Coef('Var'  , 0.0154679   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0158951   ), Coef('Var'  , 0.0314918   ), Coef('Var'  , 0.0158951   ), ], 
		[Coef('Const', 0.0625      ), Coef('Const', 0.125       ), Coef('Const', 0.25        ), Coef('Var'  , 0.231635    ), Coef('Var'  , 0.213385    ), Coef('Var'  , 0.137885    ), ], 
		[Coef('Const', 0.375       ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.440076    ), Coef('Var'  , 0.380649    ), Coef('Var'  , 0.377576    ), ], 
		[Coef('Const', 0.5625      ), Coef('Const', 0.375       ), Coef('Const', 0.25        ), Coef('Var'  , 0.280154    ), Coef('Var'  , 0.31073     ), Coef('Var'  , 0.436404    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0167716   ), Coef('Var'  , 0.0330545   ), Coef('Var'  , 0.0167716   ), ], ])
	etat8.initMat[Chem([Sub('13')])] = FMat([
		[Coef('Var'  , 0.0901638   ), Coef('Var'  , 0.0605299   ), Coef('Var'  , 0.0306894   ), Coef('Var'  , 0.0309357   ), Coef('Var'  , 0.0306894   ), Coef('Var'  , 0.0605299   ), ], 
		[Coef('Var'  , 0.0916382   ), Coef('Var'  , 0.0618863   ), Coef('Var'  , 0.0314918   ), Coef('Var'  , 0.0317902   ), Coef('Var'  , 0.0314918   ), Coef('Var'  , 0.0618863   ), ], 
		[Coef('Var'  , 0.228555    ), Coef('Var'  , 0.22092     ), Coef('Var'  , 0.213385    ), Coef('Var'  , 0.26327     ), Coef('Var'  , 0.313385    ), Coef('Var'  , 0.27092     ), ], 
		[Coef('Var'  , 0.271382    ), Coef('Var'  , 0.325585    ), Coef('Var'  , 0.380649    ), Coef('Var'  , 0.380152    ), Coef('Var'  , 0.380649    ), Coef('Var'  , 0.325585    ), ], 
		[Coef('Var'  , 0.224105    ), Coef('Var'  , 0.266813    ), Coef('Var'  , 0.31073     ), Coef('Var'  , 0.260309    ), Coef('Var'  , 0.21073     ), Coef('Var'  , 0.216813    ), ], 
		[Coef('Var'  , 0.094156    ), Coef('Var'  , 0.0642654   ), Coef('Var'  , 0.0330545   ), Coef('Var'  , 0.0335432   ), Coef('Var'  , 0.0330546   ), Coef('Var'  , 0.0642655   ), ], ])
	etat8.initMat[Chem([Sub('14')])] = FMat([
		[Coef('Const', 0           ), Coef('Var'  , 0.0154679   ), Coef('Var'  , 0.0306894   ), Coef('Var'  , 0.0154679   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0158951   ), Coef('Var'  , 0.0314918   ), Coef('Var'  , 0.0158951   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.5625      ), Coef('Var'  , 0.437885    ), Coef('Var'  , 0.313385    ), Coef('Var'  , 0.281635    ), Coef('Const', 0.25        ), Coef('Const', 0.375       ), ], 
		[Coef('Const', 0.375       ), Coef('Var'  , 0.377576    ), Coef('Var'  , 0.380649    ), Coef('Var'  , 0.440076    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0.0625      ), Coef('Var'  , 0.136405    ), Coef('Var'  , 0.21073     ), Coef('Var'  , 0.230155    ), Coef('Const', 0.25        ), Coef('Const', 0.125       ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0167716   ), Coef('Var'  , 0.0330546   ), Coef('Var'  , 0.0167716   ), Coef('Const', 0           ), Coef('Const', 0           ), ], ])
	etat8.initMat[Chem([Sub('15')])] = FMat([
		[Coef('Var'  , 0.240053    ), Coef('Var'  , 0.260345    ), Coef('Var'  , 0.284756    ), Coef('Var'  , 0.3113      ), Coef('Var'  , 0.341757    ), Coef('Var'  , 0.317339    ), Coef('Var'  , 0.2958      ), Coef('Var'  , 0.266385    ), ], 
		[Coef('Var'  , 0.127558    ), Coef('Var'  , 0.142312    ), Coef('Var'  , 0.155212    ), Coef('Var'  , 0.13515     ), Coef('Var'  , 0.114073    ), Coef('Var'  , 0.0965827   ), Coef('Var'  , 0.0778695   ), Coef('Var'  , 0.103745    ), ], 
		[Coef('Var'  , 0.124297    ), Coef('Var'  , 0.124479    ), Coef('Var'  , 0.120972    ), Coef('Var'  , 0.101722    ), Coef('Var'  , 0.0794783   ), Coef('Var'  , 0.0774996   ), Coef('Var'  , 0.0728872   ), Coef('Var'  , 0.100256    ), ], 
		[Coef('Var'  , 0.108859    ), Coef('Var'  , 0.103184    ), Coef('Var'  , 0.0944973   ), Coef('Var'  , 0.0790342   ), Coef('Var'  , 0.060693    ), Coef('Var'  , 0.0655457   ), Coef('Var'  , 0.0681693   ), Coef('Var'  , 0.0896951   ), ], 
		[Coef('Var'  , 0.162947    ), Coef('Var'  , 0.144216    ), Coef('Var'  , 0.127955    ), Coef('Var'  , 0.124604    ), Coef('Var'  , 0.122739    ), Coef('Var'  , 0.146439    ), Coef('Var'  , 0.171747    ), Coef('Var'  , 0.166052    ), ], 
		[Coef('Var'  , 0.236285    ), Coef('Var'  , 0.225464    ), Coef('Var'  , 0.216608    ), Coef('Var'  , 0.24819     ), Coef('Var'  , 0.281261    ), Coef('Var'  , 0.296594    ), Coef('Var'  , 0.313527    ), Coef('Var'  , 0.273867    ), ], ])
	etat8.initMat[Chem([Sub('16')])] = FMat([
		[Coef('Var'  , 0.170577    ), Coef('Var'  , 0.232268    ), Coef('Var'  , 0.2958      ), Coef('Var'  , 0.369515    ), Coef('Const', 0.444444    ), Coef('Const', 0.222222    ), Coef('Const', 0.111111    ), Coef('Var'  , 0.140531    ), ], 
		[Coef('Var'  , 0.0606294   ), Coef('Var'  , 0.0702153   ), Coef('Var'  , 0.0778695   ), Coef('Var'  , 0.0393599   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0308556   ), ], 
		[Coef('Var'  , 0.0727037   ), Coef('Var'  , 0.0740921   ), Coef('Var'  , 0.0728872   ), Coef('Var'  , 0.0371327   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0369597   ), ], 
		[Coef('Var'  , 0.0923791   ), Coef('Var'  , 0.0810327   ), Coef('Var'  , 0.0681693   ), Coef('Var'  , 0.0345743   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0464585   ), ], 
		[Coef('Var'  , 0.301795    ), Coef('Var'  , 0.235565    ), Coef('Var'  , 0.171747    ), Coef('Var'  , 0.140904    ), Coef('Const', 0.111111    ), Coef('Const', 0.222222    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.372438    ), ], 
		[Coef('Var'  , 0.301916    ), Coef('Var'  , 0.306826    ), Coef('Var'  , 0.313527    ), Coef('Var'  , 0.378514    ), Coef('Const', 0.444444    ), Coef('Const', 0.555556    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.372757    ), ], ])
	
	
	
	etat9.bords   = {Bord('0'): etat19, Bord('1'): etat20, Bord('2'): etat20, Bord('3'): etat19, }
	etat9.permuts = {}
	etat9.interns = {Intern('_'): etat9, }
	etat9.subs    = {Sub('0'): etat1, Sub('1'): etat2, Sub('2'): etat3, Sub('3'): etat4, Sub('4'): etat5, Sub('5'): etat6, Sub('6'): etat7, Sub('7'): etat8, Sub('G', True): Etat.etatPoint, Sub('8'): etat10, Sub('9'): etat11, Sub('10'): etat12, Sub('11'): etat13, Sub('12'): etat14, Sub('13'): etat15, Sub('14'): etat16, Sub('15'): etat17, Sub('16'): etat18, }
	
	etat9.buildIntern()
	
	
	etat9.eqs = [
		(Chem([Bord('2'), Sub('1'), Permut('0'), ])	,	Chem([Sub('1'), Bord('0'), ])),
		(Chem([Bord('1'), Sub('1'), Permut('0'), ])	,	Chem([Sub('2'), Bord('1'), ])),
		(Chem([Bord('0'), Sub('0'), Permut('0'), ])	,	Chem([Sub('4'), Bord('0'), ])),
		(Chem([Bord('3'), Sub('1'), Permut('0'), ])	,	Chem([Sub('4'), Bord('1'), ])),
		(Chem([Bord('3'), Sub('0'), Permut('0'), ])	,	Chem([Sub('8'), Bord('0'), ])),
		(Chem([Bord('2'), Sub('2'), Permut('0'), ])	,	Chem([Sub('8'), Bord('1'), ])),
		(Chem([Bord('1'), Sub('0'), Permut('0'), ])	,	Chem([Sub('9'), Bord('2'), ])),
		(Chem([Bord('0'), Sub('1'), Permut('0'), ])	,	Chem([Sub('9'), Bord('3'), ])),
		(Chem([Bord('2'), Sub('0'), Permut('0'), ])	,	Chem([Sub('11'), Bord('0'), ])),
		(Chem([Bord('1'), Sub('2'), Permut('0'), ])	,	Chem([Sub('11'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('0'), Bord('1'), ])	,	Chem([Sub('11'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('1'), Bord('1'), ])	,	Chem([Sub('15'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('2'), Bord('1'), ])	,	Chem([Sub('3'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('3'), Bord('1'), ])	,	Chem([Sub('1'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('0'), Bord('1'), ])	,	Chem([Sub('11'), Bord('4'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('2'), Bord('1'), ])	,	Chem([Sub('3'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('3'), Bord('1'), ])	,	Chem([Sub('13'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('4'), Bord('1'), ])	,	Chem([Sub('8'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('0'), Bord('1'), ])	,	Chem([Sub('11'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('1'), Bord('1'), ])	,	Chem([Sub('9'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('2'), Bord('1'), ])	,	Chem([Sub('7'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('3'), Bord('1'), ])	,	Chem([Sub('16'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('4'), Bord('1'), ])	,	Chem([Sub('15'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('3'), Bord('1'), Bord('1'), ])	,	Chem([Sub('16'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('3'), Bord('2'), Bord('1'), ])	,	Chem([Sub('6'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('4'), Bord('1'), Bord('1'), ])	,	Chem([Sub('8'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('4'), Bord('2'), Bord('1'), ])	,	Chem([Sub('10'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('4'), Bord('3'), Bord('1'), ])	,	Chem([Sub('9'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('5'), Bord('0'), Bord('1'), ])	,	Chem([Sub('14'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('5'), Bord('1'), Bord('1'), ])	,	Chem([Sub('7'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('5'), Bord('2'), Bord('1'), ])	,	Chem([Sub('10'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('6'), Bord('0'), Bord('1'), ])	,	Chem([Sub('7'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('6'), Bord('1'), Bord('1'), ])	,	Chem([Sub('12'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('6'), Bord('3'), Bord('1'), ])	,	Chem([Sub('16'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('8'), Bord('2'), Bord('1'), ])	,	Chem([Sub('10'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('9'), Bord('0'), Bord('1'), ])	,	Chem([Sub('10'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('11'), Bord('2'), Bord('1'), ])	,	Chem([Sub('15'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('12'), Bord('0'), Bord('1'), ])	,	Chem([Sub('14'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('12'), Bord('1'), Bord('1'), ])	,	Chem([Sub('13'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('13'), Bord('1'), Bord('1'), ])	,	Chem([Sub('14'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('15'), Bord('2'), Bord('1'), ])	,	Chem([Sub('16'), Bord('0'), Bord('1'), ])),
		(Chem([Bord('0'), Bord('1'), ])	,	Chem([Bord('1'), Bord('0'), ])),
		(Chem([Bord('1'), Bord('1'), ])	,	Chem([Bord('2'), Bord('0'), ])),
		(Chem([Bord('2'), Bord('1'), ])	,	Chem([Bord('3'), Bord('0'), ])),
		(Chem([Bord('3'), Bord('1'), ])	,	Chem([Bord('0'), Bord('0'), ])),
		]
	
	
	etat9.prim.elems = [Figure(2, [Chem([Bord('0'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('0'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('0'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('0'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('1'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('1'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('1'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('1'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('2'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('2'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('2'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('2'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('3'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('3'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('3'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('3'), Sub('1'), Sub('1'), Bord('0'), ]), ])]
	etat9.grid.elems = [
		Figure(1, [Chem([Bord('1'), Bord('0'), ]), Chem([Bord('1'), Intern(''), ]), Chem([Bord('1'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('2'), Bord('0'), ]), Chem([Bord('2'), Intern(''), ]), Chem([Bord('2'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('0'), Bord('0'), ]), Chem([Bord('0'), Intern(''), ]), Chem([Bord('0'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('3'), Bord('0'), ]), Chem([Bord('3'), Intern(''), ]), Chem([Bord('3'), Bord('1'), ]), ]), ]
	
	
	etat9.space = [Chem([Bord('0'), Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('2'), Intern('0'), Intern('0'), ]), Chem([Bord('2'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('3'), Intern('0'), Intern('0'), ]), ]
	
	etat9.initMat[Chem([Sub('0')])] = FMat([
		[Coef('Var'  , 0.0508918   ), Coef('Var'  , 0.0474799   ), Coef('Var'  , 0.0417011   ), Coef('Var'  , 0.0530082   ), Coef('Var'  , 0.0615859   ), Coef('Var'  , 0.0689704   ), Coef('Var'  , 0.073108    ), Coef('Var'  , 0.063442    ), ], 
		[Coef('Var'  , 0.0553486   ), Coef('Var'  , 0.0516279   ), Coef('Var'  , 0.0454182   ), Coef('Var'  , 0.057824    ), Coef('Var'  , 0.0673411   ), Coef('Var'  , 0.0752961   ), Coef('Var'  , 0.0798238   ), Coef('Var'  , 0.0690999   ), ], 
		[Coef('Var'  , 0.061906    ), Coef('Var'  , 0.0642682   ), Coef('Var'  , 0.0656259   ), Coef('Var'  , 0.0812685   ), Coef('Var'  , 0.0958324   ), Coef('Var'  , 0.0940444   ), Coef('Var'  , 0.0911211   ), Coef('Var'  , 0.0770441   ), ], 
		[Coef('Var'  , 0.0812216   ), Coef('Var'  , 0.099038    ), Coef('Var'  , 0.118916    ), Coef('Var'  , 0.139442    ), Coef('Var'  , 0.162891    ), Coef('Var'  , 0.138644    ), Coef('Var'  , 0.11757     ), Coef('Var'  , 0.0982407   ), ], 
		[Coef('Var'  , 0.300393    ), Coef('Var'  , 0.313489    ), Coef('Var'  , 0.331218    ), Coef('Var'  , 0.300562    ), Coef('Var'  , 0.275582    ), Coef('Var'  , 0.254005    ), Coef('Var'  , 0.238774    ), Coef('Var'  , 0.266932    ), ], 
		[Coef('Var'  , 0.274867    ), Coef('Var'  , 0.262203    ), Coef('Var'  , 0.251757    ), Coef('Var'  , 0.211102    ), Coef('Var'  , 0.172622    ), Coef('Var'  , 0.184774    ), Coef('Var'  , 0.199637    ), Coef('Var'  , 0.235874    ), ], 
		[Coef('Var'  , 0.121491    ), Coef('Var'  , 0.111364    ), Coef('Var'  , 0.100561    ), Coef('Var'  , 0.0996003   ), Coef('Var'  , 0.0974675   ), Coef('Var'  , 0.110183    ), Coef('Var'  , 0.121864    ), Coef('Var'  , 0.121946    ), ], 
		[Coef('Var'  , 0.0538807   ), Coef('Var'  , 0.05053     ), Coef('Var'  , 0.0448035   ), Coef('Var'  , 0.0571924   ), Coef('Var'  , 0.0666781   ), Coef('Var'  , 0.0740833   ), Coef('Var'  , 0.0781025   ), Coef('Var'  , 0.0674209   ), ], ])
	etat9.initMat[Chem([Sub('1')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0260565   ), Coef('Var'  , 0.0508918   ), Coef('Var'  , 0.0642508   ), Coef('Var'  , 0.0749248   ), Coef('Var'  , 0.0726565   ), Coef('Var'  , 0.0680023   ), Coef('Var'  , 0.0344622   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0283133   ), Coef('Var'  , 0.0553486   ), Coef('Var'  , 0.0699037   ), Coef('Var'  , 0.0816506   ), Coef('Var'  , 0.0788697   ), Coef('Var'  , 0.0736412   ), Coef('Var'  , 0.0372793   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0312032   ), Coef('Var'  , 0.061906    ), Coef('Var'  , 0.0742021   ), Coef('Var'  , 0.0856118   ), Coef('Var'  , 0.0790161   ), Coef('Var'  , 0.0720417   ), Coef('Var'  , 0.0360172   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0401629   ), Coef('Var'  , 0.0812216   ), Coef('Var'  , 0.0892202   ), Coef('Var'  , 0.099009    ), Coef('Var'  , 0.0885142   ), Coef('Var'  , 0.0790089   ), Coef('Var'  , 0.0394568   ), ], 
		[Coef('Const', 0.111111    ), Coef('Const', 0.222222    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.371299    ), Coef('Var'  , 0.300393    ), Coef('Var'  , 0.25411     ), Coef('Var'  , 0.212281    ), Coef('Var'  , 0.181574    ), Coef('Var'  , 0.153597    ), Coef('Var'  , 0.132097    ), ], 
		[Coef('Const', 0.444444    ), Coef('Const', 0.555556    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.359035    ), Coef('Var'  , 0.274867    ), Coef('Var'  , 0.244677    ), Coef('Var'  , 0.217258    ), Coef('Var'  , 0.233536    ), Coef('Var'  , 0.252526    ), Coef('Var'  , 0.347895    ), ], 
		[Coef('Const', 0.444444    ), Coef('Const', 0.222222    ), Coef('Const', 0.111111    ), Coef('Var'  , 0.1164      ), Coef('Var'  , 0.121491    ), Coef('Var'  , 0.13588     ), Coef('Var'  , 0.150216    ), Coef('Var'  , 0.190118    ), Coef('Var'  , 0.23099     ), Coef('Var'  , 0.337304    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0275301   ), Coef('Var'  , 0.0538807   ), Coef('Var'  , 0.0677565   ), Coef('Var'  , 0.079048    ), Coef('Var'  , 0.075715    ), Coef('Var'  , 0.0701921   ), Coef('Var'  , 0.0354886   ), ], ])
	etat9.initMat[Chem([Sub('2')])] = FMat([
		[Coef('Var'  , 0.0499162   ), Coef('Var'  , 0.0255194   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0339189   ), Coef('Var'  , 0.0672125   ), Coef('Var'  , 0.0711829   ), Coef('Var'  , 0.0732662   ), Coef('Var'  , 0.0627834   ), ], 
		[Coef('Var'  , 0.0552294   ), Coef('Var'  , 0.0282393   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0378976   ), Coef('Var'  , 0.0748423   ), Coef('Var'  , 0.0794433   ), Coef('Var'  , 0.0815724   ), Coef('Var'  , 0.069785    ), ], 
		[Coef('Var'  , 0.120798    ), Coef('Var'  , 0.116019    ), Coef('Const', 0.111111    ), Coef('Const', 0.222222    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.33573     ), Coef('Var'  , 0.227725    ), Coef('Var'  , 0.188488    ), Coef('Var'  , 0.1502      ), Coef('Var'  , 0.135444    ), ], 
		[Coef('Var'  , 0.267763    ), Coef('Var'  , 0.355279    ), Coef('Const', 0.444444    ), Coef('Const', 0.555556    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.344148    ), Coef('Var'  , 0.244925    ), Coef('Var'  , 0.225928    ), Coef('Var'  , 0.209957    ), Coef('Var'  , 0.237059    ), ], 
		[Coef('Var'  , 0.299461    ), Coef('Var'  , 0.37079     ), Coef('Const', 0.444444    ), Coef('Const', 0.222222    ), Coef('Const', 0.111111    ), Coef('Var'  , 0.130397    ), Coef('Var'  , 0.150309    ), Coef('Var'  , 0.178932    ), Coef('Var'  , 0.210486    ), Coef('Var'  , 0.252658    ), ], 
		[Coef('Var'  , 0.0879471   ), Coef('Var'  , 0.043716    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0413335   ), Coef('Var'  , 0.0828416   ), Coef('Var'  , 0.0938318   ), Coef('Var'  , 0.105485    ), Coef('Var'  , 0.0962143   ), ], 
		[Coef('Var'  , 0.063706    ), Coef('Var'  , 0.0321647   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0395929   ), Coef('Var'  , 0.0791188   ), Coef('Var'  , 0.0839677   ), Coef('Var'  , 0.0881814   ), Coef('Var'  , 0.0765396   ), ], 
		[Coef('Var'  , 0.0551803   ), Coef('Var'  , 0.0282724   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0369824   ), Coef('Var'  , 0.0730254   ), Coef('Var'  , 0.078226    ), Coef('Var'  , 0.0808509   ), Coef('Var'  , 0.069516    ), ], ])
	etat9.initMat[Chem([Sub('3')])] = FMat([
		[Coef('Var'  , 0.0749248   ), Coef('Var'  , 0.0755799   ), Coef('Var'  , 0.073108    ), Coef('Var'  , 0.0812402   ), Coef('Var'  , 0.0860733   ), Coef('Var'  , 0.0900452   ), Coef('Var'  , 0.0909243   ), Coef('Var'  , 0.0843849   ), ], 
		[Coef('Var'  , 0.0816506   ), Coef('Var'  , 0.082377    ), Coef('Var'  , 0.0798238   ), Coef('Var'  , 0.0891435   ), Coef('Var'  , 0.0949131   ), Coef('Var'  , 0.0992506   ), Coef('Var'  , 0.100157    ), Coef('Var'  , 0.0924841   ), ], 
		[Coef('Var'  , 0.0856118   ), Coef('Var'  , 0.0888399   ), Coef('Var'  , 0.0911211   ), Coef('Var'  , 0.103541    ), Coef('Var'  , 0.115242    ), Coef('Var'  , 0.114409    ), Coef('Var'  , 0.113459    ), Coef('Var'  , 0.0997082   ), ], 
		[Coef('Var'  , 0.099009    ), Coef('Var'  , 0.107135    ), Coef('Var'  , 0.11757     ), Coef('Var'  , 0.129037    ), Coef('Var'  , 0.143718    ), Coef('Var'  , 0.134883    ), Coef('Var'  , 0.129157    ), Coef('Var'  , 0.112982    ), ], 
		[Coef('Var'  , 0.212281    ), Coef('Var'  , 0.222888    ), Coef('Var'  , 0.238774    ), Coef('Var'  , 0.217126    ), Coef('Var'  , 0.201437    ), Coef('Var'  , 0.189059    ), Coef('Var'  , 0.181646    ), Coef('Var'  , 0.194821    ), ], 
		[Coef('Var'  , 0.217258    ), Coef('Var'  , 0.206924    ), Coef('Var'  , 0.199637    ), Coef('Var'  , 0.173842    ), Coef('Var'  , 0.150701    ), Coef('Var'  , 0.153706    ), Coef('Var'  , 0.159047    ), Coef('Var'  , 0.186788    ), ], 
		[Coef('Var'  , 0.150216    ), Coef('Var'  , 0.136139    ), Coef('Var'  , 0.121864    ), Coef('Var'  , 0.118544    ), Coef('Var'  , 0.114493    ), Coef('Var'  , 0.121385    ), Coef('Var'  , 0.127975    ), Coef('Var'  , 0.138979    ), ], 
		[Coef('Var'  , 0.079048    ), Coef('Var'  , 0.0801172   ), Coef('Var'  , 0.0781025   ), Coef('Var'  , 0.0875265   ), Coef('Var'  , 0.0934218   ), Coef('Var'  , 0.097262    ), Coef('Var'  , 0.097634    ), Coef('Var'  , 0.0898528   ), ], ])
	etat9.initMat[Chem([Sub('4')])] = FMat([
		[Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.222873    ), Coef('Var'  , 0.195826    ), Coef('Var'  , 0.222873    ), ], 
		[Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0984453   ), Coef('Var'  , 0.196921    ), Coef('Var'  , 0.348445    ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0707763   ), Coef('Var'  , 0.141714    ), Coef('Var'  , 0.195776    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.024943    ), Coef('Var'  , 0.0497628   ), Coef('Var'  , 0.024943    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0157224   ), Coef('Var'  , 0.0311954   ), Coef('Var'  , 0.0157224   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0238899   ), Coef('Var'  , 0.0476807   ), Coef('Var'  , 0.0238899   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.195327    ), Coef('Var'  , 0.140754    ), Coef('Var'  , 0.0703268   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.348023    ), Coef('Var'  , 0.196146    ), Coef('Var'  , 0.0980229   ), ], ])
	etat9.initMat[Chem([Sub('5')])] = FMat([
		[Coef('Var'  , 0.122289    ), Coef('Var'  , 0.114103    ), Coef('Var'  , 0.105197    ), Coef('Var'  , 0.101996    ), Coef('Var'  , 0.0977496   ), Coef('Var'  , 0.110329    ), ], 
		[Coef('Var'  , 0.12806     ), Coef('Var'  , 0.121272    ), Coef('Var'  , 0.113402    ), Coef('Var'  , 0.110758    ), Coef('Var'  , 0.106561    ), Coef('Var'  , 0.117894    ), ], 
		[Coef('Var'  , 0.151397    ), Coef('Var'  , 0.14013     ), Coef('Var'  , 0.130372    ), Coef('Var'  , 0.146548    ), Coef('Var'  , 0.164503    ), Coef('Var'  , 0.157086    ), ], 
		[Coef('Var'  , 0.123045    ), Coef('Var'  , 0.126108    ), Coef('Var'  , 0.129177    ), Coef('Var'  , 0.147064    ), Coef('Var'  , 0.165537    ), Coef('Var'  , 0.144004    ), ], 
		[Coef('Var'  , 0.0988446   ), Coef('Var'  , 0.116513    ), Coef('Var'  , 0.133013    ), Coef('Var'  , 0.133987    ), Coef('Var'  , 0.134183    ), Coef('Var'  , 0.116923    ), ], 
		[Coef('Var'  , 0.109326    ), Coef('Var'  , 0.123233    ), Coef('Var'  , 0.137874    ), Coef('Var'  , 0.124034    ), Coef('Var'  , 0.111069    ), Coef('Var'  , 0.110047    ), ], 
		[Coef('Var'  , 0.142084    ), Coef('Var'  , 0.141446    ), Coef('Var'  , 0.142243    ), Coef('Var'  , 0.129104    ), Coef('Var'  , 0.117326    ), Coef('Var'  , 0.129278    ), ], 
		[Coef('Var'  , 0.124955    ), Coef('Var'  , 0.117196    ), Coef('Var'  , 0.108722    ), Coef('Var'  , 0.106509    ), Coef('Var'  , 0.103071    ), Coef('Var'  , 0.114439    ), ], ])
	etat9.initMat[Chem([Sub('6')])] = FMat([
		[Coef('Var'  , 0.0891086   ), Coef('Var'  , 0.0907647   ), Coef('Var'  , 0.0902259   ), Coef('Var'  , 0.0943274   ), Coef('Var'  , 0.0965201   ), Coef('Var'  , 0.0949835   ), Coef('Var'  , 0.0909243   ), Coef('Var'  , 0.0914208   ), ], 
		[Coef('Var'  , 0.098967    ), Coef('Var'  , 0.10098     ), Coef('Var'  , 0.100151    ), Coef('Var'  , 0.104281    ), Coef('Var'  , 0.105956    ), Coef('Var'  , 0.104492    ), Coef('Var'  , 0.100157    ), Coef('Var'  , 0.101191    ), ], 
		[Coef('Var'  , 0.133696    ), Coef('Var'  , 0.145894    ), Coef('Var'  , 0.159237    ), Coef('Var'  , 0.138909    ), Coef('Var'  , 0.119894    ), Coef('Var'  , 0.116416    ), Coef('Var'  , 0.113459    ), Coef('Var'  , 0.123401    ), ], 
		[Coef('Var'  , 0.158706    ), Coef('Var'  , 0.163812    ), Coef('Var'  , 0.171764    ), Coef('Var'  , 0.150337    ), Coef('Var'  , 0.13062     ), Coef('Var'  , 0.128937    ), Coef('Var'  , 0.129157    ), Coef('Var'  , 0.142411    ), ], 
		[Coef('Var'  , 0.180564    ), Coef('Var'  , 0.16555     ), Coef('Var'  , 0.153284    ), Coef('Var'  , 0.154275    ), Coef('Var'  , 0.156438    ), Coef('Var'  , 0.167742    ), Coef('Var'  , 0.181646    ), Coef('Var'  , 0.179016    ), ], 
		[Coef('Var'  , 0.130822    ), Coef('Var'  , 0.123568    ), Coef('Var'  , 0.117532    ), Coef('Var'  , 0.133702    ), Coef('Var'  , 0.151386    ), Coef('Var'  , 0.154087    ), Coef('Var'  , 0.159047    ), Coef('Var'  , 0.143953    ), ], 
		[Coef('Var'  , 0.110932    ), Coef('Var'  , 0.110765    ), Coef('Var'  , 0.110545    ), Coef('Var'  , 0.123409    ), Coef('Var'  , 0.13727     ), Coef('Var'  , 0.132175    ), Coef('Var'  , 0.127975    ), Coef('Var'  , 0.119532    ), ], 
		[Coef('Var'  , 0.0972046   ), Coef('Var'  , 0.0986665   ), Coef('Var'  , 0.0972596   ), Coef('Var'  , 0.10076     ), Coef('Var'  , 0.101915    ), Coef('Var'  , 0.101168    ), Coef('Var'  , 0.097634    ), Coef('Var'  , 0.0990745   ), ], ])
	etat9.initMat[Chem([Sub('7')])] = FMat([
		[Coef('Var'  , 0.0672125   ), Coef('Var'  , 0.0830301   ), Coef('Var'  , 0.0977496   ), Coef('Var'  , 0.0946457   ), Coef('Var'  , 0.0902259   ), Coef('Var'  , 0.0794533   ), ], 
		[Coef('Var'  , 0.0748423   ), Coef('Var'  , 0.0915877   ), Coef('Var'  , 0.106561    ), Coef('Var'  , 0.104372    ), Coef('Var'  , 0.100151    ), Coef('Var'  , 0.0885799   ), ], 
		[Coef('Var'  , 0.227725    ), Coef('Var'  , 0.195259    ), Coef('Var'  , 0.164503    ), Coef('Var'  , 0.160955    ), Coef('Var'  , 0.159237    ), Coef('Var'  , 0.19271     ), ], 
		[Coef('Var'  , 0.244925    ), Coef('Var'  , 0.204406    ), Coef('Var'  , 0.165537    ), Coef('Var'  , 0.167805    ), Coef('Var'  , 0.171764    ), Coef('Var'  , 0.207251    ), ], 
		[Coef('Var'  , 0.150309    ), Coef('Var'  , 0.142039    ), Coef('Var'  , 0.134183    ), Coef('Var'  , 0.143519    ), Coef('Var'  , 0.153284    ), Coef('Var'  , 0.151163    ), ], 
		[Coef('Var'  , 0.0828416   ), Coef('Var'  , 0.0967575   ), Coef('Var'  , 0.111069    ), Coef('Var'  , 0.113964    ), Coef('Var'  , 0.117532    ), Coef('Var'  , 0.0998733   ), ], 
		[Coef('Var'  , 0.0791188   ), Coef('Var'  , 0.0980608   ), Coef('Var'  , 0.117326    ), Coef('Var'  , 0.113644    ), Coef('Var'  , 0.110545    ), Coef('Var'  , 0.0947693   ), ], 
		[Coef('Var'  , 0.0730254   ), Coef('Var'  , 0.0888587   ), Coef('Var'  , 0.103071    ), Coef('Var'  , 0.101095    ), Coef('Var'  , 0.0972596   ), Coef('Var'  , 0.0862008   ), ], ])
	etat9.initMat[Chem([Sub('G')])] = FMat([
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], ])
	etat9.initMat[Chem([Sub('8')])] = FMat([
		[Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0709653   ), Coef('Var'  , 0.141976    ), Coef('Var'  , 0.195965    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0407183   ), Coef('Var'  , 0.0814047   ), Coef('Var'  , 0.0407182   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0361299   ), Coef('Var'  , 0.0725302   ), Coef('Var'  , 0.0361298   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.021765    ), Coef('Var'  , 0.043422    ), Coef('Var'  , 0.0217649   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.111111    ), Coef('Var'  , 0.0862808   ), Coef('Var'  , 0.0611208   ), Coef('Var'  , 0.0307252   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.333333    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.297503    ), Coef('Var'  , 0.150489    ), Coef('Var'  , 0.0752807   ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.666667    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.344069    ), Coef('Var'  , 0.243859    ), Coef('Var'  , 0.246847    ), ], 
		[Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.102569    ), Coef('Var'  , 0.205198    ), Coef('Var'  , 0.352568    ), ], ])
	etat9.initMat[Chem([Sub('9')])] = FMat([
		[Coef('Const', 0.25        ), Coef('Var'  , 0.195965    ), Coef('Var'  , 0.141976    ), Coef('Var'  , 0.0709652   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.5         ), Coef('Var'  , 0.353215    ), Coef('Var'  , 0.206401    ), Coef('Var'  , 0.103216    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0.25        ), Coef('Var'  , 0.247929    ), Coef('Var'  , 0.246134    ), Coef('Var'  , 0.345152    ), Coef('Const', 0.444444    ), Coef('Const', 0.666667    ), Coef('Const', 1           ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0773168   ), Coef('Var'  , 0.154529    ), Coef('Var'  , 0.299539    ), Coef('Const', 0.444444    ), Coef('Const', 0.333333    ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0307261   ), Coef('Var'  , 0.0611218   ), Coef('Var'  , 0.0862816   ), Coef('Const', 0.111111    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0197282   ), Coef('Var'  , 0.0393815   ), Coef('Var'  , 0.0197283   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0350463   ), Coef('Var'  , 0.0702534   ), Coef('Var'  , 0.0350463   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0400727   ), Coef('Var'  , 0.0802034   ), Coef('Var'  , 0.0400727   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], ])
	etat9.initMat[Chem([Sub('10')])] = FMat([
		[Coef('Var'  , 0.195826    ), Coef('Var'  , 0.168838    ), Coef('Var'  , 0.141976    ), Coef('Var'  , 0.132183    ), Coef('Var'  , 0.122289    ), Coef('Var'  , 0.132183    ), Coef('Var'  , 0.141976    ), Coef('Var'  , 0.168838    ), ], 
		[Coef('Var'  , 0.196921    ), Coef('Var'  , 0.139164    ), Coef('Var'  , 0.0814047   ), Coef('Var'  , 0.104922    ), Coef('Var'  , 0.12806     ), Coef('Var'  , 0.167419    ), Coef('Var'  , 0.206401    ), Coef('Var'  , 0.201661    ), ], 
		[Coef('Var'  , 0.141714    ), Coef('Var'  , 0.106906    ), Coef('Var'  , 0.0725302   ), Coef('Var'  , 0.111464    ), Coef('Var'  , 0.151397    ), Coef('Var'  , 0.198263    ), Coef('Var'  , 0.246134    ), Coef('Var'  , 0.193706    ), ], 
		[Coef('Var'  , 0.0497628   ), Coef('Var'  , 0.0467079   ), Coef('Var'  , 0.043422    ), Coef('Var'  , 0.0832886   ), Coef('Var'  , 0.123045    ), Coef('Var'  , 0.138841    ), Coef('Var'  , 0.154529    ), Coef('Var'  , 0.10226     ), ], 
		[Coef('Var'  , 0.0311954   ), Coef('Var'  , 0.0464476   ), Coef('Var'  , 0.0611208   ), Coef('Var'  , 0.08045     ), Coef('Var'  , 0.0988446   ), Coef('Var'  , 0.0804508   ), Coef('Var'  , 0.0611218   ), Coef('Var'  , 0.0464485   ), ], 
		[Coef('Var'  , 0.0476807   ), Coef('Var'  , 0.0991706   ), Coef('Var'  , 0.150489    ), Coef('Var'  , 0.129904    ), Coef('Var'  , 0.109326    ), Coef('Var'  , 0.074351    ), Coef('Var'  , 0.0393815   ), Coef('Var'  , 0.0436181   ), ], 
		[Coef('Var'  , 0.140754    ), Coef('Var'  , 0.192174    ), Coef('Var'  , 0.243859    ), Coef('Var'  , 0.192657    ), Coef('Var'  , 0.142084    ), Coef('Var'  , 0.105856    ), Coef('Var'  , 0.0702534   ), Coef('Var'  , 0.105373    ), ], 
		[Coef('Var'  , 0.196146    ), Coef('Var'  , 0.200591    ), Coef('Var'  , 0.205198    ), Coef('Var'  , 0.165131    ), Coef('Var'  , 0.124955    ), Coef('Var'  , 0.102636    ), Coef('Var'  , 0.0802034   ), Coef('Var'  , 0.138096    ), ], ])
	etat9.initMat[Chem([Sub('11')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0212898   ), Coef('Var'  , 0.0414559   ), Coef('Var'  , 0.0427131   ), Coef('Var'  , 0.0417011   ), Coef('Var'  , 0.0214235   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0232876   ), Coef('Var'  , 0.0453751   ), Coef('Var'  , 0.0466021   ), Coef('Var'  , 0.0454182   ), Coef('Var'  , 0.0233146   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.111111    ), Coef('Var'  , 0.105475    ), Coef('Var'  , 0.0994278   ), Coef('Var'  , 0.0829843   ), Coef('Var'  , 0.0656259   ), Coef('Var'  , 0.0330651   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.333333    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.343878    ), Coef('Var'  , 0.244688    ), Coef('Var'  , 0.180531    ), Coef('Var'  , 0.118916    ), Coef('Var'  , 0.0588753   ), ], 
		[Coef('Const', 0.444444    ), Coef('Const', 0.666667    ), Coef('Const', 1           ), Coef('Const', 0.666667    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.386501    ), Coef('Var'  , 0.330978    ), Coef('Var'  , 0.328691    ), Coef('Var'  , 0.331218    ), Coef('Var'  , 0.386634    ), ], 
		[Coef('Const', 0.444444    ), Coef('Const', 0.333333    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0625584   ), Coef('Var'  , 0.125893    ), Coef('Var'  , 0.187948    ), Coef('Var'  , 0.251757    ), Coef('Var'  , 0.347612    ), ], 
		[Coef('Const', 0.111111    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0338008   ), Coef('Var'  , 0.0670125   ), Coef('Var'  , 0.0843205   ), Coef('Var'  , 0.100561    ), Coef('Var'  , 0.106075    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.02321     ), Coef('Var'  , 0.0451697   ), Coef('Var'  , 0.0462098   ), Coef('Var'  , 0.0448035   ), Coef('Var'  , 0.023       ), ], ])
	etat9.initMat[Chem([Sub('12')])] = FMat([
		[Coef('Var'  , 0.0965201   ), Coef('Var'  , 0.0991115   ), Coef('Var'  , 0.0997316   ), Coef('Var'  , 0.0970607   ), Coef('Var'  , 0.0924854   ), Coef('Var'  , 0.095535    ), ], 
		[Coef('Var'  , 0.105956    ), Coef('Var'  , 0.108242    ), Coef('Var'  , 0.108312    ), Coef('Var'  , 0.105391    ), Coef('Var'  , 0.100467    ), Coef('Var'  , 0.104346    ), ], 
		[Coef('Var'  , 0.119894    ), Coef('Var'  , 0.115352    ), Coef('Var'  , 0.111808    ), Coef('Var'  , 0.105762    ), Coef('Var'  , 0.100555    ), Coef('Var'  , 0.109823    ), ], 
		[Coef('Var'  , 0.13062     ), Coef('Var'  , 0.124729    ), Coef('Var'  , 0.119444    ), Coef('Var'  , 0.114387    ), Coef('Var'  , 0.109369    ), Coef('Var'  , 0.119683    ), ], 
		[Coef('Var'  , 0.156438    ), Coef('Var'  , 0.151613    ), Coef('Var'  , 0.147093    ), Coef('Var'  , 0.148961    ), Coef('Var'  , 0.150641    ), Coef('Var'  , 0.153255    ), ], 
		[Coef('Var'  , 0.151386    ), Coef('Var'  , 0.154302    ), Coef('Var'  , 0.15942     ), Coef('Var'  , 0.169526    ), Coef('Var'  , 0.182057    ), Coef('Var'  , 0.165548    ), ], 
		[Coef('Var'  , 0.13727     ), Coef('Var'  , 0.143064    ), Coef('Var'  , 0.150929    ), Coef('Var'  , 0.158574    ), Coef('Var'  , 0.168733    ), Coef('Var'  , 0.151974    ), ], 
		[Coef('Var'  , 0.101915    ), Coef('Var'  , 0.103587    ), Coef('Var'  , 0.103263    ), Coef('Var'  , 0.100338    ), Coef('Var'  , 0.0956925   ), Coef('Var'  , 0.0998355   ), ], ])
	etat9.initMat[Chem([Sub('13')])] = FMat([
		[Coef('Var'  , 0.0680023   ), Coef('Var'  , 0.0812043   ), Coef('Var'  , 0.0924854   ), Coef('Var'  , 0.0941791   ), Coef('Var'  , 0.0939785   ), Coef('Var'  , 0.0818991   ), ], 
		[Coef('Var'  , 0.0736412   ), Coef('Var'  , 0.0880271   ), Coef('Var'  , 0.100467    ), Coef('Var'  , 0.102056    ), Coef('Var'  , 0.1017      ), Coef('Var'  , 0.0885874   ), ], 
		[Coef('Var'  , 0.0720417   ), Coef('Var'  , 0.0861338   ), Coef('Var'  , 0.100555    ), Coef('Var'  , 0.101167    ), Coef('Var'  , 0.102494    ), Coef('Var'  , 0.0870671   ), ], 
		[Coef('Var'  , 0.0790089   ), Coef('Var'  , 0.0941275   ), Coef('Var'  , 0.109369    ), Coef('Var'  , 0.109416    ), Coef('Var'  , 0.109382    ), Coef('Var'  , 0.0942022   ), ], 
		[Coef('Var'  , 0.153597    ), Coef('Var'  , 0.151842    ), Coef('Var'  , 0.150641    ), Coef('Var'  , 0.148659    ), Coef('Var'  , 0.14651     ), Coef('Var'  , 0.1499      ), ], 
		[Coef('Var'  , 0.252526    ), Coef('Var'  , 0.216059    ), Coef('Var'  , 0.182057    ), Coef('Var'  , 0.179567    ), Coef('Var'  , 0.179558    ), Coef('Var'  , 0.214854    ), ], 
		[Coef('Var'  , 0.23099     ), Coef('Var'  , 0.198823    ), Coef('Var'  , 0.168733    ), Coef('Var'  , 0.167923    ), Coef('Var'  , 0.169647    ), Coef('Var'  , 0.199263    ), ], 
		[Coef('Var'  , 0.0701921   ), Coef('Var'  , 0.0837821   ), Coef('Var'  , 0.0956925   ), Coef('Var'  , 0.0970333   ), Coef('Var'  , 0.0967313   ), Coef('Var'  , 0.0842284   ), ], ])
	etat9.initMat[Chem([Sub('14')])] = FMat([
		[Coef('Var'  , 0.105197    ), Coef('Var'  , 0.100321    ), Coef('Var'  , 0.0939785   ), Coef('Var'  , 0.0977555   ), Coef('Var'  , 0.0997316   ), Coef('Var'  , 0.103203    ), ], 
		[Coef('Var'  , 0.113402    ), Coef('Var'  , 0.108376    ), Coef('Var'  , 0.1017      ), Coef('Var'  , 0.105951    ), Coef('Var'  , 0.108312    ), Coef('Var'  , 0.111711    ), ], 
		[Coef('Var'  , 0.130372    ), Coef('Var'  , 0.115846    ), Coef('Var'  , 0.102494    ), Coef('Var'  , 0.106696    ), Coef('Var'  , 0.111808    ), Coef('Var'  , 0.120442    ), ], 
		[Coef('Var'  , 0.129177    ), Coef('Var'  , 0.119329    ), Coef('Var'  , 0.109382    ), Coef('Var'  , 0.114462    ), Coef('Var'  , 0.119444    ), Coef('Var'  , 0.124301    ), ], 
		[Coef('Var'  , 0.133013    ), Coef('Var'  , 0.140147    ), Coef('Var'  , 0.14651     ), Coef('Var'  , 0.147018    ), Coef('Var'  , 0.147093    ), Coef('Var'  , 0.140448    ), ], 
		[Coef('Var'  , 0.137874    ), Coef('Var'  , 0.157791    ), Coef('Var'  , 0.179558    ), Coef('Var'  , 0.168321    ), Coef('Var'  , 0.15942     ), Coef('Var'  , 0.14775     ), ], 
		[Coef('Var'  , 0.142243    ), Coef('Var'  , 0.154817    ), Coef('Var'  , 0.169647    ), Coef('Var'  , 0.159013    ), Coef('Var'  , 0.150929    ), Coef('Var'  , 0.145468    ), ], 
		[Coef('Var'  , 0.108722    ), Coef('Var'  , 0.103372    ), Coef('Var'  , 0.0967313   ), Coef('Var'  , 0.100785    ), Coef('Var'  , 0.103263    ), Coef('Var'  , 0.106678    ), ], ])
	etat9.initMat[Chem([Sub('15')])] = FMat([
		[Coef('Var'  , 0.0615859   ), Coef('Var'  , 0.0528745   ), Coef('Var'  , 0.0414559   ), Coef('Var'  , 0.046809    ), Coef('Var'  , 0.0499162   ), Coef('Var'  , 0.0623998   ), Coef('Var'  , 0.0721921   ), Coef('Var'  , 0.0684653   ), ], 
		[Coef('Var'  , 0.0673411   ), Coef('Var'  , 0.057797    ), Coef('Var'  , 0.0453751   ), Coef('Var'  , 0.0515268   ), Coef('Var'  , 0.0552294   ), Coef('Var'  , 0.0689619   ), Coef('Var'  , 0.0797205   ), Coef('Var'  , 0.0752321   ), ], 
		[Coef('Var'  , 0.0958324   ), Coef('Var'  , 0.0981227   ), Coef('Var'  , 0.0994278   ), Coef('Var'  , 0.110383    ), Coef('Var'  , 0.120798    ), Coef('Var'  , 0.12111     ), Coef('Var'  , 0.12108     ), Coef('Var'  , 0.10885     ), ], 
		[Coef('Var'  , 0.162891    ), Coef('Var'  , 0.202222    ), Coef('Var'  , 0.244688    ), Coef('Var'  , 0.254713    ), Coef('Var'  , 0.267763    ), Coef('Var'  , 0.227098    ), Coef('Var'  , 0.190188    ), Coef('Var'  , 0.174607    ), ], 
		[Coef('Var'  , 0.275582    ), Coef('Var'  , 0.300429    ), Coef('Var'  , 0.330978    ), Coef('Var'  , 0.312847    ), Coef('Var'  , 0.299461    ), Coef('Var'  , 0.265951    ), Coef('Var'  , 0.237907    ), Coef('Var'  , 0.253533    ), ], 
		[Coef('Var'  , 0.172622    ), Coef('Var'  , 0.148271    ), Coef('Var'  , 0.125893    ), Coef('Var'  , 0.106274    ), Coef('Var'  , 0.0879471   ), Coef('Var'  , 0.106624    ), Coef('Var'  , 0.126663    ), Coef('Var'  , 0.148621    ), ], 
		[Coef('Var'  , 0.0974675   ), Coef('Var'  , 0.0828813   ), Coef('Var'  , 0.0670125   ), Coef('Var'  , 0.0659654   ), Coef('Var'  , 0.063706    ), Coef('Var'  , 0.0790099   ), Coef('Var'  , 0.0929513   ), Coef('Var'  , 0.0959258   ), ], 
		[Coef('Var'  , 0.0666781   ), Coef('Var'  , 0.0574024   ), Coef('Var'  , 0.0451697   ), Coef('Var'  , 0.0514822   ), Coef('Var'  , 0.0551803   ), Coef('Var'  , 0.0688455   ), Coef('Var'  , 0.0792979   ), Coef('Var'  , 0.0747656   ), ], ])
	etat9.initMat[Chem([Sub('16')])] = FMat([
		[Coef('Var'  , 0.0860733   ), Coef('Var'  , 0.0807351   ), Coef('Var'  , 0.0721921   ), Coef('Var'  , 0.0741445   ), Coef('Var'  , 0.0732662   ), Coef('Var'  , 0.0824943   ), Coef('Var'  , 0.0891086   ), Coef('Var'  , 0.0890848   ), ], 
		[Coef('Var'  , 0.0949131   ), Coef('Var'  , 0.0890796   ), Coef('Var'  , 0.0797205   ), Coef('Var'  , 0.0822684   ), Coef('Var'  , 0.0815724   ), Coef('Var'  , 0.0918433   ), Coef('Var'  , 0.098967    ), Coef('Var'  , 0.0986545   ), ], 
		[Coef('Var'  , 0.115242    ), Coef('Var'  , 0.118346    ), Coef('Var'  , 0.12108     ), Coef('Var'  , 0.135627    ), Coef('Var'  , 0.1502      ), Coef('Var'  , 0.141672    ), Coef('Var'  , 0.133696    ), Coef('Var'  , 0.124392    ), ], 
		[Coef('Var'  , 0.143718    ), Coef('Var'  , 0.165       ), Coef('Var'  , 0.190188    ), Coef('Var'  , 0.198043    ), Coef('Var'  , 0.209957    ), Coef('Var'  , 0.18249     ), Coef('Var'  , 0.158706    ), Coef('Var'  , 0.149446    ), ], 
		[Coef('Var'  , 0.201437    ), Coef('Var'  , 0.216654    ), Coef('Var'  , 0.237907    ), Coef('Var'  , 0.221474    ), Coef('Var'  , 0.210486    ), Coef('Var'  , 0.193319    ), Coef('Var'  , 0.180564    ), Coef('Var'  , 0.188499    ), ], 
		[Coef('Var'  , 0.150701    ), Coef('Var'  , 0.137689    ), Coef('Var'  , 0.126663    ), Coef('Var'  , 0.115407    ), Coef('Var'  , 0.105485    ), Coef('Var'  , 0.117527    ), Coef('Var'  , 0.130822    ), Coef('Var'  , 0.139809    ), ], 
		[Coef('Var'  , 0.114493    ), Coef('Var'  , 0.104287    ), Coef('Var'  , 0.0929513   ), Coef('Var'  , 0.0912202   ), Coef('Var'  , 0.0881814   ), Coef('Var'  , 0.0999636   ), Coef('Var'  , 0.110932    ), Coef('Var'  , 0.113031    ), ], 
		[Coef('Var'  , 0.0934218   ), Coef('Var'  , 0.0882088   ), Coef('Var'  , 0.0792979   ), Coef('Var'  , 0.0818167   ), Coef('Var'  , 0.0808509   ), Coef('Var'  , 0.0906917   ), Coef('Var'  , 0.0972046   ), Coef('Var'  , 0.0970838   ), ], ])
	
	
	
	etat10.bords   = {Bord('0'): etat19, Bord('1'): etat20, Bord('2'): etat22, Bord('3'): etat19, }
	etat10.permuts = {}
	etat10.interns = {Intern('_'): etat10, }
	etat10.subs    = {Sub('0'): etat1, Sub('1'): etat2, Sub('2'): etat3, Sub('3'): etat4, Sub('4'): etat5, Sub('5'): etat6, Sub('6'): etat7, Sub('7'): etat8, Sub('G', True): Etat.etatPoint, Sub('8'): etat9, Sub('9'): etat11, Sub('10'): etat12, Sub('11'): etat13, Sub('12'): etat14, Sub('13'): etat15, Sub('14'): etat16, Sub('15'): etat17, Sub('16'): etat18, }
	
	etat10.buildIntern()
	
	
	etat10.eqs = [
		(Chem([Bord('1'), Sub('2'), Permut('0'), ])	,	Chem([Sub('1'), Bord('0'), ])),
		(Chem([Bord('2'), Sub('0'), Permut('0'), ])	,	Chem([Sub('1'), Bord('4'), ])),
		(Chem([Bord('0'), Sub('0'), Permut('0'), ])	,	Chem([Sub('4'), Bord('1'), ])),
		(Chem([Bord('3'), Sub('1'), Permut('0'), ])	,	Chem([Sub('4'), Bord('2'), ])),
		(Chem([Bord('2'), Sub('3'), Permut('0'), ])	,	Chem([Sub('5'), Bord('0'), ])),
		(Chem([Bord('1'), Sub('0'), Permut('0'), ])	,	Chem([Sub('8'), Bord('2'), ])),
		(Chem([Bord('0'), Sub('1'), Permut('0'), ])	,	Chem([Sub('8'), Bord('3'), ])),
		(Chem([Bord('3'), Sub('0'), Permut('0'), ])	,	Chem([Sub('10'), Bord('0'), ])),
		(Chem([Bord('2'), Sub('4'), Permut('0'), ])	,	Chem([Sub('10'), Bord('1'), ])),
		(Chem([Bord('1'), Sub('1'), Permut('0'), ])	,	Chem([Sub('11'), Bord('0'), ])),
		(Chem([Bord('2'), Sub('1'), Permut('0'), ])	,	Chem([Sub('13'), Bord('2'), ])),
		(Chem([Bord('2'), Sub('2'), Permut('0'), ])	,	Chem([Sub('14'), Bord('0'), ])),
		(Chem([Sub('0'), Bord('0'), Bord('1'), ])	,	Chem([Sub('11'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('1'), Bord('1'), ])	,	Chem([Sub('15'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('2'), Bord('1'), ])	,	Chem([Sub('3'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('3'), Bord('1'), ])	,	Chem([Sub('1'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('0'), Bord('1'), ])	,	Chem([Sub('11'), Bord('4'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('2'), Bord('1'), ])	,	Chem([Sub('3'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('3'), Bord('1'), ])	,	Chem([Sub('13'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('0'), Bord('1'), ])	,	Chem([Sub('11'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('1'), Bord('1'), ])	,	Chem([Sub('9'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('2'), Bord('1'), ])	,	Chem([Sub('7'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('3'), Bord('1'), ])	,	Chem([Sub('16'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('4'), Bord('1'), ])	,	Chem([Sub('15'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('3'), Bord('1'), Bord('1'), ])	,	Chem([Sub('16'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('3'), Bord('2'), Bord('1'), ])	,	Chem([Sub('6'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('4'), Bord('0'), Bord('1'), ])	,	Chem([Sub('8'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('4'), Bord('2'), Bord('1'), ])	,	Chem([Sub('10'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('4'), Bord('3'), Bord('1'), ])	,	Chem([Sub('9'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('5'), Bord('0'), Bord('1'), ])	,	Chem([Sub('14'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('5'), Bord('1'), Bord('1'), ])	,	Chem([Sub('7'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('5'), Bord('2'), Bord('1'), ])	,	Chem([Sub('10'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('6'), Bord('0'), Bord('1'), ])	,	Chem([Sub('7'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('6'), Bord('1'), Bord('1'), ])	,	Chem([Sub('12'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('6'), Bord('3'), Bord('1'), ])	,	Chem([Sub('16'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('8'), Bord('0'), Bord('1'), ])	,	Chem([Sub('9'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('8'), Bord('1'), Bord('1'), ])	,	Chem([Sub('11'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('9'), Bord('0'), Bord('1'), ])	,	Chem([Sub('10'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('11'), Bord('2'), Bord('1'), ])	,	Chem([Sub('15'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('12'), Bord('0'), Bord('1'), ])	,	Chem([Sub('14'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('12'), Bord('1'), Bord('1'), ])	,	Chem([Sub('13'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('13'), Bord('1'), Bord('1'), ])	,	Chem([Sub('14'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('15'), Bord('2'), Bord('1'), ])	,	Chem([Sub('16'), Bord('0'), Bord('1'), ])),
		(Chem([Bord('0'), Bord('1'), ])	,	Chem([Bord('1'), Bord('0'), ])),
		(Chem([Bord('1'), Bord('1'), ])	,	Chem([Bord('2'), Bord('0'), ])),
		(Chem([Bord('2'), Bord('1'), ])	,	Chem([Bord('3'), Bord('0'), ])),
		(Chem([Bord('3'), Bord('1'), ])	,	Chem([Bord('0'), Bord('0'), ])),
		]
	
	
	etat10.prim.elems = [Figure(2, [Chem([Bord('0'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('0'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('0'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('0'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('1'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('1'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('1'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('1'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('2'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('2'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('2'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('2'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('3'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('3'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('3'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('3'), Sub('1'), Sub('1'), Bord('0'), ]), ])]
	etat10.grid.elems = [
		Figure(1, [Chem([Bord('1'), Bord('0'), ]), Chem([Bord('1'), Intern(''), ]), Chem([Bord('1'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('2'), Bord('0'), ]), Chem([Bord('2'), Intern(''), ]), Chem([Bord('2'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('0'), Bord('0'), ]), Chem([Bord('0'), Intern(''), ]), Chem([Bord('0'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('3'), Bord('0'), ]), Chem([Bord('3'), Intern(''), ]), Chem([Bord('3'), Bord('1'), ]), ]), ]
	
	
	etat10.space = [Chem([Bord('0'), Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('2'), Intern('0'), Intern('0'), ]), Chem([Bord('2'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('3'), Intern('0'), Intern('0'), ]), ]
	
	etat10.initMat[Chem([Sub('0')])] = FMat([
		[Coef('Var'  , 0.0486558   ), Coef('Var'  , 0.0539873   ), Coef('Var'  , 0.0567163   ), Coef('Var'  , 0.0707161   ), Coef('Var'  , 0.0814229   ), Coef('Var'  , 0.0785598   ), Coef('Var'  , 0.0720676   ), Coef('Var'  , 0.061831    ), ], 
		[Coef('Var'  , 0.0509313   ), Coef('Var'  , 0.0560831   ), Coef('Var'  , 0.0586647   ), Coef('Var'  , 0.0732857   ), Coef('Var'  , 0.0846766   ), Coef('Var'  , 0.0820876   ), Coef('Var'  , 0.0758469   ), Coef('Var'  , 0.064885    ), ], 
		[Coef('Var'  , 0.110055    ), Coef('Var'  , 0.121112    ), Coef('Var'  , 0.131907    ), Coef('Var'  , 0.135125    ), Coef('Var'  , 0.138378    ), Coef('Var'  , 0.125869    ), Coef('Var'  , 0.112823    ), Coef('Var'  , 0.111856    ), ], 
		[Coef('Var'  , 0.255876    ), Coef('Var'  , 0.265191    ), Coef('Var'  , 0.277278    ), Coef('Var'  , 0.239076    ), Coef('Var'  , 0.204604    ), Coef('Var'  , 0.190406    ), Coef('Var'  , 0.179716    ), Coef('Var'  , 0.216521    ), ], 
		[Coef('Var'  , 0.336391    ), Coef('Var'  , 0.312107    ), Coef('Var'  , 0.29298     ), Coef('Var'  , 0.255874    ), Coef('Var'  , 0.224537    ), Coef('Var'  , 0.245292    ), Coef('Var'  , 0.273116    ), Coef('Var'  , 0.301525    ), ], 
		[Coef('Var'  , 0.0944414   ), Coef('Var'  , 0.0824016   ), Coef('Var'  , 0.0708321   ), Coef('Var'  , 0.0862831   ), Coef('Var'  , 0.10208     ), Coef('Var'  , 0.115481    ), Coef('Var'  , 0.130012    ), Coef('Var'  , 0.111599    ), ], 
		[Coef('Var'  , 0.059147    ), Coef('Var'  , 0.0604371   ), Coef('Var'  , 0.0608199   ), Coef('Var'  , 0.0761093   ), Coef('Var'  , 0.0905795   ), Coef('Var'  , 0.0906053   ), Coef('Var'  , 0.0897842   ), Coef('Var'  , 0.0749331   ), ], 
		[Coef('Var'  , 0.0445036   ), Coef('Var'  , 0.048681    ), Coef('Var'  , 0.0508016   ), Coef('Var'  , 0.0635304   ), Coef('Var'  , 0.0737221   ), Coef('Var'  , 0.0716992   ), Coef('Var'  , 0.0666347   ), Coef('Var'  , 0.0568498   ), ], ])
	etat10.initMat[Chem([Sub('1')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0249373   ), Coef('Var'  , 0.0486558   ), Coef('Var'  , 0.0515175   ), Coef('Var'  , 0.0519014   ), Coef('Var'  , 0.0265803   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0260788   ), Coef('Var'  , 0.0509313   ), Coef('Var'  , 0.0543033   ), Coef('Var'  , 0.0551085   ), Coef('Var'  , 0.0282246   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.111111    ), Coef('Var'  , 0.110741    ), Coef('Var'  , 0.110055    ), Coef('Var'  , 0.0959112   ), Coef('Var'  , 0.0808511   ), Coef('Var'  , 0.0407259   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.333333    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.349594    ), Coef('Var'  , 0.255876    ), Coef('Var'  , 0.194337    ), Coef('Var'  , 0.134679    ), Coef('Var'  , 0.0669645   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 1           ), Coef('Const', 0.666667    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.389059    ), Coef('Var'  , 0.336391    ), Coef('Var'  , 0.348014    ), Coef('Var'  , 0.365345    ), Coef('Var'  , 0.501176    ), Coef('Const', 0.64        ), Coef('Const', 0.8         ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0470096   ), Coef('Var'  , 0.0944414   ), Coef('Var'  , 0.137625    ), Coef('Var'  , 0.182179    ), Coef('Var'  , 0.250615    ), Coef('Const', 0.32        ), Coef('Const', 0.2         ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0298146   ), Coef('Var'  , 0.059147    ), Coef('Var'  , 0.0705705   ), Coef('Var'  , 0.0812238   ), Coef('Var'  , 0.060756    ), Coef('Const', 0.04        ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0227654   ), Coef('Var'  , 0.0445036   ), Coef('Var'  , 0.0477221   ), Coef('Var'  , 0.0487118   ), Coef('Var'  , 0.0249568   ), Coef('Const', 0           ), Coef('Const', 0           ), ], ])
	etat10.initMat[Chem([Sub('2')])] = FMat([
		[Coef('Var'  , 0.0910917   ), Coef('Var'  , 0.0842858   ), Coef('Var'  , 0.0743668   ), Coef('Var'  , 0.0937894   ), Coef('Var'  , 0.111174    ), Coef('Var'  , 0.097351    ), Coef('Var'  , 0.0814376   ), Coef('Var'  , 0.0889485   ), Coef('Var'  , 0.0933123   ), Coef('Var'  , 0.0940705   ), ], 
		[Coef('Var'  , 0.0948633   ), Coef('Var'  , 0.0871398   ), Coef('Var'  , 0.0763235   ), Coef('Var'  , 0.0956234   ), Coef('Var'  , 0.112944    ), Coef('Var'  , 0.100624    ), Coef('Var'  , 0.08601     ), Coef('Var'  , 0.0941254   ), Coef('Var'  , 0.0987001   ), Coef('Var'  , 0.0987463   ), ], 
		[Coef('Var'  , 0.169135    ), Coef('Var'  , 0.202771    ), Coef('Var'  , 0.236929    ), Coef('Var'  , 0.202616    ), Coef('Var'  , 0.16879     ), Coef('Var'  , 0.139377    ), Coef('Var'  , 0.109772    ), Coef('Var'  , 0.121662    ), Coef('Var'  , 0.132906    ), Coef('Var'  , 0.151071    ), ], 
		[Coef('Var'  , 0.186417    ), Coef('Var'  , 0.21351     ), Coef('Var'  , 0.243729    ), Coef('Var'  , 0.189081    ), Coef('Var'  , 0.136017    ), Coef('Var'  , 0.117609    ), Coef('Var'  , 0.0996209   ), Coef('Var'  , 0.118208    ), Coef('Var'  , 0.138003    ), Coef('Var'  , 0.160738    ), ], 
		[Coef('Var'  , 0.156558    ), Coef('Var'  , 0.142843    ), Coef('Var'  , 0.132981    ), Coef('Var'  , 0.108771    ), Coef('Var'  , 0.0864286   ), Coef('Var'  , 0.105874    ), Coef('Var'  , 0.127356    ), Coef('Var'  , 0.137995    ), Coef('Var'  , 0.152856    ), Coef('Var'  , 0.152107    ), ], 
		[Coef('Var'  , 0.106519    ), Coef('Var'  , 0.0901296   ), Coef('Var'  , 0.0742311   ), Coef('Var'  , 0.0887462   ), Coef('Var'  , 0.103598    ), Coef('Var'  , 0.147589    ), Coef('Var'  , 0.19334     ), Coef('Var'  , 0.16828     ), Coef('Var'  , 0.14602     ), Coef('Var'  , 0.125379    ), ], 
		[Coef('Var'  , 0.111915    ), Coef('Var'  , 0.102       ), Coef('Var'  , 0.0926892   ), Coef('Var'  , 0.132234    ), Coef('Var'  , 0.173035    ), Coef('Var'  , 0.197297    ), Coef('Var'  , 0.223822    ), Coef('Var'  , 0.18607     ), Coef('Var'  , 0.150439    ), Coef('Var'  , 0.130637    ), ], 
		[Coef('Var'  , 0.0835004   ), Coef('Var'  , 0.0773198   ), Coef('Var'  , 0.0687515   ), Coef('Var'  , 0.0891394   ), Coef('Var'  , 0.108013    ), Coef('Var'  , 0.0942805   ), Coef('Var'  , 0.0786417   ), Coef('Var'  , 0.084711    ), Coef('Var'  , 0.0877642   ), Coef('Var'  , 0.0872506   ), ], ])
	etat10.initMat[Chem([Sub('3')])] = FMat([
		[Coef('Var'  , 0.0519014   ), Coef('Var'  , 0.0634741   ), Coef('Var'  , 0.0720676   ), Coef('Var'  , 0.0810643   ), Coef('Var'  , 0.0864355   ), Coef('Var'  , 0.0811818   ), Coef('Var'  , 0.0723733   ), Coef('Var'  , 0.0635915   ), ], 
		[Coef('Var'  , 0.0551085   ), Coef('Var'  , 0.0670309   ), Coef('Var'  , 0.0758469   ), Coef('Var'  , 0.0859394   ), Coef('Var'  , 0.0921764   ), Coef('Var'  , 0.0871786   ), Coef('Var'  , 0.0781743   ), Coef('Var'  , 0.0682701   ), ], 
		[Coef('Var'  , 0.0808511   ), Coef('Var'  , 0.0973967   ), Coef('Var'  , 0.112823    ), Coef('Var'  , 0.115189    ), Coef('Var'  , 0.116223    ), Coef('Var'  , 0.106046    ), Coef('Var'  , 0.0939768   ), Coef('Var'  , 0.0882534   ), ], 
		[Coef('Var'  , 0.134679    ), Coef('Var'  , 0.156113    ), Coef('Var'  , 0.179716    ), Coef('Var'  , 0.158534    ), Coef('Var'  , 0.139722    ), Coef('Var'  , 0.125187    ), Coef('Var'  , 0.111832    ), Coef('Var'  , 0.122767    ), ], 
		[Coef('Var'  , 0.365345    ), Coef('Var'  , 0.315864    ), Coef('Var'  , 0.273116    ), Coef('Var'  , 0.236916    ), Coef('Var'  , 0.208357    ), Coef('Var'  , 0.223043    ), Coef('Var'  , 0.245288    ), Coef('Var'  , 0.301991    ), ], 
		[Coef('Var'  , 0.182179    ), Coef('Var'  , 0.155205    ), Coef('Var'  , 0.130012    ), Coef('Var'  , 0.139435    ), Coef('Var'  , 0.151383    ), Coef('Var'  , 0.171337    ), Coef('Var'  , 0.195159    ), Coef('Var'  , 0.187107    ), ], 
		[Coef('Var'  , 0.0812238   ), Coef('Var'  , 0.0858745   ), Coef('Var'  , 0.0897842   ), Coef('Var'  , 0.106961    ), Coef('Var'  , 0.123864    ), Coef('Var'  , 0.128308    ), Coef('Var'  , 0.133311    ), Coef('Var'  , 0.107222    ), ], 
		[Coef('Var'  , 0.0487118   ), Coef('Var'  , 0.0590413   ), Coef('Var'  , 0.0666347   ), Coef('Var'  , 0.0759617   ), Coef('Var'  , 0.0818397   ), Coef('Var'  , 0.0777191   ), Coef('Var'  , 0.0698864   ), Coef('Var'  , 0.0607987   ), ], ])
	etat10.initMat[Chem([Sub('4')])] = FMat([
		[Coef('Var'  , 0.195216    ), Coef('Var'  , 0.22266     ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.22266     ), ], 
		[Coef('Var'  , 0.195198    ), Coef('Var'  , 0.347613    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0976128   ), ], 
		[Coef('Var'  , 0.144708    ), Coef('Var'  , 0.197305    ), Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0723052   ), ], 
		[Coef('Var'  , 0.0512781   ), Coef('Var'  , 0.0256759   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0256759   ), ], 
		[Coef('Var'  , 0.0233915   ), Coef('Var'  , 0.0117642   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0117642   ), ], 
		[Coef('Var'  , 0.0378663   ), Coef('Var'  , 0.0189836   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0189836   ), ], 
		[Coef('Var'  , 0.157863    ), Coef('Var'  , 0.0787354   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.203735    ), ], 
		[Coef('Var'  , 0.194478    ), Coef('Var'  , 0.0972631   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.347263    ), ], ])
	etat10.initMat[Chem([Sub('5')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0199828   ), Coef('Var'  , 0.0392355   ), Coef('Var'  , 0.0199828   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0216168   ), Coef('Var'  , 0.0423079   ), Coef('Var'  , 0.0216168   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0248787   ), Coef('Var'  , 0.0494009   ), Coef('Var'  , 0.0248787   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0228313   ), Coef('Var'  , 0.045493    ), Coef('Var'  , 0.0228313   ), ], 
		[Coef('Const', 0.04        ), Coef('Const', 0.08        ), Coef('Const', 0.16        ), Coef('Var'  , 0.140029    ), Coef('Var'  , 0.120988    ), Coef('Var'  , 0.0800292   ), ], 
		[Coef('Const', 0.32        ), Coef('Const', 0.44        ), Coef('Const', 0.48        ), Coef('Var'  , 0.391518    ), Coef('Var'  , 0.304188    ), Coef('Var'  , 0.311518    ), ], 
		[Coef('Const', 0.64        ), Coef('Const', 0.48        ), Coef('Const', 0.36        ), Coef('Var'  , 0.359581    ), Coef('Var'  , 0.360052    ), Coef('Var'  , 0.499581    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0195619   ), Coef('Var'  , 0.0383337   ), Coef('Var'  , 0.0195619   ), ], ])
	etat10.initMat[Chem([Sub('6')])] = FMat([
		[Coef('Var'  , 0.0850575   ), Coef('Var'  , 0.0776595   ), Coef('Var'  , 0.0671013   ), Coef('Var'  , 0.0582849   ), Coef('Var'  , 0.0469382   ), Coef('Var'  , 0.0610628   ), Coef('Var'  , 0.0723733   ), Coef('Var'  , 0.0804374   ), ], 
		[Coef('Var'  , 0.0915202   ), Coef('Var'  , 0.0840412   ), Coef('Var'  , 0.072759    ), Coef('Var'  , 0.0638644   ), Coef('Var'  , 0.0517683   ), Coef('Var'  , 0.0666741   ), Coef('Var'  , 0.0781743   ), Coef('Var'  , 0.0868508   ), ], 
		[Coef('Var'  , 0.109284    ), Coef('Var'  , 0.0974559   ), Coef('Var'  , 0.0838684   ), Coef('Var'  , 0.0718088   ), Coef('Var'  , 0.0578672   ), Coef('Var'  , 0.0769825   ), Coef('Var'  , 0.0939768   ), Coef('Var'  , 0.10263     ), ], 
		[Coef('Var'  , 0.116365    ), Coef('Var'  , 0.0986378   ), Coef('Var'  , 0.0809761   ), Coef('Var'  , 0.0709732   ), Coef('Var'  , 0.0601325   ), Coef('Var'  , 0.0861372   ), Coef('Var'  , 0.111832    ), Coef('Var'  , 0.113802    ), ], 
		[Coef('Var'  , 0.183776    ), Coef('Var'  , 0.172984    ), Coef('Var'  , 0.167804    ), Coef('Var'  , 0.214076    ), Coef('Var'  , 0.265068    ), Coef('Var'  , 0.252104    ), Coef('Var'  , 0.245288    ), Coef('Var'  , 0.211012    ), ], 
		[Coef('Var'  , 0.176022    ), Coef('Var'  , 0.203811    ), Coef('Var'  , 0.236036    ), Coef('Var'  , 0.263275    ), Coef('Var'  , 0.29512     ), Coef('Var'  , 0.242873    ), Coef('Var'  , 0.195159    ), Coef('Var'  , 0.183409    ), ], 
		[Coef('Var'  , 0.156153    ), Coef('Var'  , 0.189932    ), Coef('Var'  , 0.225765    ), Coef('Var'  , 0.200101    ), Coef('Var'  , 0.176461    ), Coef('Var'  , 0.154315    ), Coef('Var'  , 0.133311    ), Coef('Var'  , 0.144146    ), ], 
		[Coef('Var'  , 0.0818219   ), Coef('Var'  , 0.0754792   ), Coef('Var'  , 0.0656894   ), Coef('Var'  , 0.0576164   ), Coef('Var'  , 0.0466448   ), Coef('Var'  , 0.0598509   ), Coef('Var'  , 0.0698864   ), Coef('Var'  , 0.0777137   ), ], ])
	etat10.initMat[Chem([Sub('7')])] = FMat([
		[Coef('Var'  , 0.0814376   ), Coef('Var'  , 0.0613455   ), Coef('Var'  , 0.0392355   ), Coef('Var'  , 0.0542162   ), Coef('Var'  , 0.0671013   ), Coef('Var'  , 0.075596    ), ], 
		[Coef('Var'  , 0.08601     ), Coef('Var'  , 0.0653763   ), Coef('Var'  , 0.0423079   ), Coef('Var'  , 0.0588527   ), Coef('Var'  , 0.072759    ), Coef('Var'  , 0.0809954   ), ], 
		[Coef('Var'  , 0.109772    ), Coef('Var'  , 0.0799406   ), Coef('Var'  , 0.0494009   ), Coef('Var'  , 0.0672325   ), Coef('Var'  , 0.0838684   ), Coef('Var'  , 0.0974156   ), ], 
		[Coef('Var'  , 0.0996209   ), Coef('Var'  , 0.0725851   ), Coef('Var'  , 0.045493    ), Coef('Var'  , 0.0634694   ), Coef('Var'  , 0.0809761   ), Coef('Var'  , 0.0903918   ), ], 
		[Coef('Var'  , 0.127356    ), Coef('Var'  , 0.122946    ), Coef('Var'  , 0.120988    ), Coef('Var'  , 0.142816    ), Coef('Var'  , 0.167804    ), Coef('Var'  , 0.145703    ), ], 
		[Coef('Var'  , 0.19334     ), Coef('Var'  , 0.247455    ), Coef('Var'  , 0.304188    ), Coef('Var'  , 0.268412    ), Coef('Var'  , 0.236036    ), Coef('Var'  , 0.21283     ), ], 
		[Coef('Var'  , 0.223822    ), Coef('Var'  , 0.290829    ), Coef('Var'  , 0.360052    ), Coef('Var'  , 0.291833    ), Coef('Var'  , 0.225765    ), Coef('Var'  , 0.2235      ), ], 
		[Coef('Var'  , 0.0786417   ), Coef('Var'  , 0.0595225   ), Coef('Var'  , 0.0383337   ), Coef('Var'  , 0.0531692   ), Coef('Var'  , 0.0656894   ), Coef('Var'  , 0.0735679   ), ], ])
	etat10.initMat[Chem([Sub('G')])] = FMat([
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], ])
	etat10.initMat[Chem([Sub('8')])] = FMat([
		[Coef('Const', 0.25        ), Coef('Var'  , 0.195005    ), Coef('Var'  , 0.139781    ), Coef('Var'  , 0.0700051   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.5         ), Coef('Var'  , 0.351372    ), Coef('Var'  , 0.20258     ), Coef('Var'  , 0.101372    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0.25        ), Coef('Var'  , 0.250791    ), Coef('Var'  , 0.251701    ), Coef('Var'  , 0.348013    ), Coef('Const', 0.444444    ), Coef('Const', 0.666667    ), Coef('Const', 1           ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.078933    ), Coef('Var'  , 0.157862    ), Coef('Var'  , 0.301155    ), Coef('Const', 0.444444    ), Coef('Const', 0.333333    ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.027603    ), Coef('Var'  , 0.0551679   ), Coef('Var'  , 0.0831586   ), Coef('Const', 0.111111    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0176952   ), Coef('Var'  , 0.0353566   ), Coef('Var'  , 0.0176953   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0404774   ), Coef('Var'  , 0.081453    ), Coef('Var'  , 0.0404774   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0381241   ), Coef('Var'  , 0.0760983   ), Coef('Var'  , 0.0381242   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], ])
	etat10.initMat[Chem([Sub('9')])] = FMat([
		[Coef('Var'  , 0.195216    ), Coef('Var'  , 0.167666    ), Coef('Var'  , 0.139783    ), Coef('Var'  , 0.125994    ), Coef('Var'  , 0.111174    ), Coef('Var'  , 0.125993    ), Coef('Var'  , 0.139781    ), Coef('Var'  , 0.167665    ), ], 
		[Coef('Var'  , 0.195198    ), Coef('Var'  , 0.136489    ), Coef('Var'  , 0.0775855   ), Coef('Var'  , 0.0957402   ), Coef('Var'  , 0.112944    ), Coef('Var'  , 0.158236    ), Coef('Var'  , 0.20258     ), Coef('Var'  , 0.198984    ), ], 
		[Coef('Var'  , 0.144708    ), Coef('Var'  , 0.111294    ), Coef('Var'  , 0.0780941   ), Coef('Var'  , 0.123304    ), Coef('Var'  , 0.16879     ), Coef('Var'  , 0.210106    ), Coef('Var'  , 0.251701    ), Coef('Var'  , 0.198096    ), ], 
		[Coef('Var'  , 0.0512781   ), Coef('Var'  , 0.0490551   ), Coef('Var'  , 0.0467531   ), Coef('Var'  , 0.091234    ), Coef('Var'  , 0.136017    ), Coef('Var'  , 0.146788    ), Coef('Var'  , 0.157862    ), Coef('Var'  , 0.104609    ), ], 
		[Coef('Var'  , 0.0233915   ), Coef('Var'  , 0.0304791   ), Coef('Var'  , 0.0373909   ), Coef('Var'  , 0.0616713   ), Coef('Var'  , 0.0864286   ), Coef('Var'  , 0.0705595   ), Coef('Var'  , 0.0551679   ), Coef('Var'  , 0.0393673   ), ], 
		[Coef('Var'  , 0.0378663   ), Coef('Var'  , 0.0766771   ), Coef('Var'  , 0.115354    ), Coef('Var'  , 0.109346    ), Coef('Var'  , 0.103598    ), Coef('Var'  , 0.0693478   ), Coef('Var'  , 0.0353566   ), Coef('Var'  , 0.0366789   ), ], 
		[Coef('Var'  , 0.157863    ), Coef('Var'  , 0.230456    ), Coef('Var'  , 0.303945    ), Coef('Var'  , 0.237769    ), Coef('Var'  , 0.173035    ), Coef('Var'  , 0.126526    ), Coef('Var'  , 0.081453    ), Coef('Var'  , 0.119213    ), ], 
		[Coef('Var'  , 0.194478    ), Coef('Var'  , 0.197884    ), Coef('Var'  , 0.201095    ), Coef('Var'  , 0.154941    ), Coef('Var'  , 0.108013    ), Coef('Var'  , 0.092444    ), Coef('Var'  , 0.0760983   ), Coef('Var'  , 0.135387    ), ], ])
	etat10.initMat[Chem([Sub('10')])] = FMat([
		[Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0700061   ), Coef('Var'  , 0.139783    ), Coef('Var'  , 0.195006    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0388762   ), Coef('Var'  , 0.0775855   ), Coef('Var'  , 0.0388762   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0389884   ), Coef('Var'  , 0.0780941   ), Coef('Var'  , 0.0389884   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0233792   ), Coef('Var'  , 0.0467531   ), Coef('Var'  , 0.0233792   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.04        ), Coef('Var'  , 0.0387148   ), Coef('Var'  , 0.0373909   ), Coef('Var'  , 0.0187148   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.2         ), Coef('Const', 0.32        ), Coef('Var'  , 0.217693    ), Coef('Var'  , 0.115354    ), Coef('Var'  , 0.0576934   ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.8         ), Coef('Const', 0.64        ), Coef('Var'  , 0.471721    ), Coef('Var'  , 0.303945    ), Coef('Var'  , 0.276721    ), ], 
		[Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.100621    ), Coef('Var'  , 0.201095    ), Coef('Var'  , 0.350621    ), ], ])
	etat10.initMat[Chem([Sub('11')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0378012   ), Coef('Var'  , 0.0743668   ), Coef('Var'  , 0.0792007   ), Coef('Var'  , 0.081012    ), Coef('Var'  , 0.0704497   ), Coef('Var'  , 0.0567163   ), Coef('Var'  , 0.0290502   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0387594   ), Coef('Var'  , 0.0763235   ), Coef('Var'  , 0.0814429   ), Coef('Var'  , 0.0836314   ), Coef('Var'  , 0.072688    ), Coef('Var'  , 0.0586647   ), Coef('Var'  , 0.0300044   ), ], 
		[Coef('Const', 0.111111    ), Coef('Const', 0.222222    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.340522    ), Coef('Var'  , 0.236929    ), Coef('Var'  , 0.202348    ), Coef('Var'  , 0.168398    ), Coef('Var'  , 0.149974    ), Coef('Var'  , 0.131907    ), Coef('Var'  , 0.121482    ), ], 
		[Coef('Const', 0.444444    ), Coef('Const', 0.555556    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.343448    ), Coef('Var'  , 0.243729    ), Coef('Var'  , 0.231282    ), Coef('Var'  , 0.222217    ), Coef('Var'  , 0.247874    ), Coef('Var'  , 0.277278    ), Coef('Var'  , 0.36004     ), ], 
		[Coef('Const', 0.444444    ), Coef('Const', 0.222222    ), Coef('Const', 0.111111    ), Coef('Var'  , 0.12137     ), Coef('Var'  , 0.132981    ), Coef('Var'  , 0.161675    ), Coef('Var'  , 0.194285    ), Coef('Var'  , 0.241131    ), Coef('Var'  , 0.29298     ), Coef('Var'  , 0.367492    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0370937   ), Coef('Var'  , 0.0742311   ), Coef('Var'  , 0.0811425   ), Coef('Var'  , 0.0881115   ), Coef('Var'  , 0.0794409   ), Coef('Var'  , 0.0708321   ), Coef('Var'  , 0.0353921   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0461857   ), Coef('Var'  , 0.0926892   ), Coef('Var'  , 0.0909371   ), Coef('Var'  , 0.089341    ), Coef('Var'  , 0.075374    ), Coef('Var'  , 0.0608199   ), Coef('Var'  , 0.0306226   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0348196   ), Coef('Var'  , 0.0687515   ), Coef('Var'  , 0.0719717   ), Coef('Var'  , 0.0730035   ), Coef('Var'  , 0.0630678   ), Coef('Var'  , 0.0508016   ), Coef('Var'  , 0.0259157   ), ], ])
	etat10.initMat[Chem([Sub('12')])] = FMat([
		[Coef('Var'  , 0.0469382   ), Coef('Var'  , 0.0330894   ), Coef('Var'  , 0.0175537   ), Coef('Var'  , 0.0180757   ), Coef('Var'  , 0.0175537   ), Coef('Var'  , 0.0330894   ), ], 
		[Coef('Var'  , 0.0517683   ), Coef('Var'  , 0.0368593   ), Coef('Var'  , 0.0197669   ), Coef('Var'  , 0.0204614   ), Coef('Var'  , 0.0197669   ), Coef('Var'  , 0.0368593   ), ], 
		[Coef('Var'  , 0.0578672   ), Coef('Var'  , 0.0403909   ), Coef('Var'  , 0.0212928   ), Coef('Var'  , 0.0218717   ), Coef('Var'  , 0.0212928   ), Coef('Var'  , 0.0403909   ), ], 
		[Coef('Var'  , 0.0601325   ), Coef('Var'  , 0.0412765   ), Coef('Var'  , 0.0214455   ), Coef('Var'  , 0.0218829   ), Coef('Var'  , 0.0214456   ), Coef('Var'  , 0.0412766   ), ], 
		[Coef('Var'  , 0.265068    ), Coef('Var'  , 0.275389    ), Coef('Var'  , 0.289396    ), Coef('Var'  , 0.336198    ), Coef('Var'  , 0.385396    ), Coef('Var'  , 0.323389    ), ], 
		[Coef('Var'  , 0.29512     ), Coef('Var'  , 0.347317    ), Coef('Var'  , 0.40318     ), Coef('Var'  , 0.385872    ), Coef('Var'  , 0.37118     ), Coef('Var'  , 0.331317    ), ], 
		[Coef('Var'  , 0.176461    ), Coef('Var'  , 0.192418    ), Coef('Var'  , 0.209504    ), Coef('Var'  , 0.177137    ), Coef('Var'  , 0.145504    ), Coef('Var'  , 0.160418    ), ], 
		[Coef('Var'  , 0.0466448   ), Coef('Var'  , 0.0332595   ), Coef('Var'  , 0.0178613   ), Coef('Var'  , 0.0185008   ), Coef('Var'  , 0.0178613   ), Coef('Var'  , 0.0332594   ), ], ])
	etat10.initMat[Chem([Sub('13')])] = FMat([
		[Coef('Const', 0           ), Coef('Var'  , 0.00903783  ), Coef('Var'  , 0.0175537   ), Coef('Var'  , 0.00903783  ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0102307   ), Coef('Var'  , 0.0197669   ), Coef('Var'  , 0.0102307   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0109359   ), Coef('Var'  , 0.0212928   ), Coef('Var'  , 0.0109359   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0109414   ), Coef('Var'  , 0.0214456   ), Coef('Var'  , 0.0109414   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.64        ), Coef('Var'  , 0.512099    ), Coef('Var'  , 0.385396    ), Coef('Var'  , 0.372099    ), Coef('Const', 0.36        ), Coef('Const', 0.48        ), ], 
		[Coef('Const', 0.32        ), Coef('Var'  , 0.344936    ), Coef('Var'  , 0.37118     ), Coef('Var'  , 0.424936    ), Coef('Const', 0.48        ), Coef('Const', 0.44        ), ], 
		[Coef('Const', 0.04        ), Coef('Var'  , 0.0925686   ), Coef('Var'  , 0.145504    ), Coef('Var'  , 0.152569    ), Coef('Const', 0.16        ), Coef('Const', 0.08        ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.00925038  ), Coef('Var'  , 0.0178613   ), Coef('Var'  , 0.00925038  ), Coef('Const', 0           ), Coef('Const', 0           ), ], ])
	etat10.initMat[Chem([Sub('14')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.00903785  ), Coef('Var'  , 0.0175537   ), Coef('Var'  , 0.00903785  ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0102307   ), Coef('Var'  , 0.0197669   ), Coef('Var'  , 0.0102307   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0109359   ), Coef('Var'  , 0.0212928   ), Coef('Var'  , 0.0109359   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0109414   ), Coef('Var'  , 0.0214455   ), Coef('Var'  , 0.0109414   ), ], 
		[Coef('Const', 0.16        ), Coef('Const', 0.24        ), Coef('Const', 0.36        ), Coef('Var'  , 0.324099    ), Coef('Var'  , 0.289396    ), Coef('Var'  , 0.224099    ), ], 
		[Coef('Const', 0.48        ), Coef('Const', 0.52        ), Coef('Const', 0.48        ), Coef('Var'  , 0.440936    ), Coef('Var'  , 0.40318     ), Coef('Var'  , 0.440936    ), ], 
		[Coef('Const', 0.36        ), Coef('Const', 0.24        ), Coef('Const', 0.16        ), Coef('Var'  , 0.184569    ), Coef('Var'  , 0.209504    ), Coef('Var'  , 0.284569    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0092504   ), Coef('Var'  , 0.0178613   ), Coef('Var'  , 0.0092504   ), ], ])
	etat10.initMat[Chem([Sub('15')])] = FMat([
		[Coef('Var'  , 0.0814229   ), Coef('Var'  , 0.0830656   ), Coef('Var'  , 0.081012    ), Coef('Var'  , 0.0878843   ), Coef('Var'  , 0.0910917   ), Coef('Var'  , 0.094473    ), Coef('Var'  , 0.0939541   ), Coef('Var'  , 0.0896544   ), ], 
		[Coef('Var'  , 0.0846766   ), Coef('Var'  , 0.0859649   ), Coef('Var'  , 0.0836314   ), Coef('Var'  , 0.0910641   ), Coef('Var'  , 0.0948633   ), Coef('Var'  , 0.0987969   ), Coef('Var'  , 0.0987355   ), Coef('Var'  , 0.0936977   ), ], 
		[Coef('Var'  , 0.138378    ), Coef('Var'  , 0.153246    ), Coef('Var'  , 0.168398    ), Coef('Var'  , 0.168519    ), Coef('Var'  , 0.169135    ), Coef('Var'  , 0.154456    ), Coef('Var'  , 0.139783    ), Coef('Var'  , 0.139184    ), ], 
		[Coef('Var'  , 0.204604    ), Coef('Var'  , 0.211313    ), Coef('Var'  , 0.222217    ), Coef('Var'  , 0.20234     ), Coef('Var'  , 0.186417    ), Coef('Var'  , 0.172574    ), Coef('Var'  , 0.16231     ), Coef('Var'  , 0.181548    ), ], 
		[Coef('Var'  , 0.224537    ), Coef('Var'  , 0.206465    ), Coef('Var'  , 0.194285    ), Coef('Var'  , 0.17289     ), Coef('Var'  , 0.156558    ), Coef('Var'  , 0.163381    ), Coef('Var'  , 0.175977    ), Coef('Var'  , 0.196956    ), ], 
		[Coef('Var'  , 0.10208     ), Coef('Var'  , 0.0949399   ), Coef('Var'  , 0.0881115   ), Coef('Var'  , 0.0970848   ), Coef('Var'  , 0.106519    ), Coef('Var'  , 0.114462    ), Coef('Var'  , 0.123748    ), Coef('Var'  , 0.112317    ), ], 
		[Coef('Var'  , 0.0905795   ), Coef('Var'  , 0.0902382   ), Coef('Var'  , 0.089341    ), Coef('Var'  , 0.100566    ), Coef('Var'  , 0.111915    ), Coef('Var'  , 0.115029    ), Coef('Var'  , 0.118609    ), Coef('Var'  , 0.104701    ), ], 
		[Coef('Var'  , 0.0737221   ), Coef('Var'  , 0.0747669   ), Coef('Var'  , 0.0730035   ), Coef('Var'  , 0.0796524   ), Coef('Var'  , 0.0835004   ), Coef('Var'  , 0.0868283   ), Coef('Var'  , 0.0868824   ), Coef('Var'  , 0.0819428   ), ], ])
	etat10.initMat[Chem([Sub('16')])] = FMat([
		[Coef('Var'  , 0.0864355   ), Coef('Var'  , 0.0921589   ), Coef('Var'  , 0.0939541   ), Coef('Var'  , 0.0955742   ), Coef('Var'  , 0.0933123   ), Coef('Var'  , 0.091012    ), Coef('Var'  , 0.0850575   ), Coef('Var'  , 0.0875967   ), ], 
		[Coef('Var'  , 0.0921764   ), Coef('Var'  , 0.0975495   ), Coef('Var'  , 0.0987355   ), Coef('Var'  , 0.100782    ), Coef('Var'  , 0.0987001   ), Coef('Var'  , 0.0971712   ), Coef('Var'  , 0.0915202   ), Coef('Var'  , 0.0939383   ), ], 
		[Coef('Var'  , 0.116223    ), Coef('Var'  , 0.128503    ), Coef('Var'  , 0.139783    ), Coef('Var'  , 0.136585    ), Coef('Var'  , 0.132906    ), Coef('Var'  , 0.121702    ), Coef('Var'  , 0.109284    ), Coef('Var'  , 0.11362     ), ], 
		[Coef('Var'  , 0.139722    ), Coef('Var'  , 0.149675    ), Coef('Var'  , 0.16231     ), Coef('Var'  , 0.148744    ), Coef('Var'  , 0.138003    ), Coef('Var'  , 0.126454    ), Coef('Var'  , 0.116365    ), Coef('Var'  , 0.127385    ), ], 
		[Coef('Var'  , 0.208357    ), Coef('Var'  , 0.188581    ), Coef('Var'  , 0.175977    ), Coef('Var'  , 0.16143     ), Coef('Var'  , 0.152856    ), Coef('Var'  , 0.165276    ), Coef('Var'  , 0.183776    ), Coef('Var'  , 0.192426    ), ], 
		[Coef('Var'  , 0.151383    ), Coef('Var'  , 0.136271    ), Coef('Var'  , 0.123748    ), Coef('Var'  , 0.133769    ), Coef('Var'  , 0.14602     ), Coef('Var'  , 0.159261    ), Coef('Var'  , 0.176022    ), Coef('Var'  , 0.161762    ), ], 
		[Coef('Var'  , 0.123864    ), Coef('Var'  , 0.121056    ), Coef('Var'  , 0.118609    ), Coef('Var'  , 0.134036    ), Coef('Var'  , 0.150439    ), Coef('Var'  , 0.152502    ), Coef('Var'  , 0.156153    ), Coef('Var'  , 0.139523    ), ], 
		[Coef('Var'  , 0.0818397   ), Coef('Var'  , 0.0862052   ), Coef('Var'  , 0.0868824   ), Coef('Var'  , 0.0890784   ), Coef('Var'  , 0.0877642   ), Coef('Var'  , 0.0866222   ), Coef('Var'  , 0.0818219   ), Coef('Var'  , 0.083749    ), ], ])
	
	
	
	etat11.bords   = {Bord('0'): etat19, Bord('1'): etat21, Bord('2'): etat20, Bord('3'): etat19, }
	etat11.permuts = {}
	etat11.interns = {Intern('_'): etat11, }
	etat11.subs    = {Sub('0'): etat1, Sub('1'): etat2, Sub('2'): etat3, Sub('3'): etat4, Sub('4'): etat5, Sub('5'): etat6, Sub('6'): etat7, Sub('7'): etat8, Sub('G', True): Etat.etatPoint, Sub('8'): etat9, Sub('9'): etat10, Sub('10'): etat12, Sub('11'): etat13, Sub('12'): etat14, Sub('13'): etat15, Sub('14'): etat16, Sub('15'): etat17, Sub('16'): etat18, }
	
	etat11.buildIntern()
	
	
	etat11.eqs = [
		(Chem([Bord('2'), Sub('0'), Permut('0'), ])	,	Chem([Sub('2'), Bord('1'), ])),
		(Chem([Bord('1'), Sub('3'), Permut('0'), ])	,	Chem([Sub('2'), Bord('2'), ])),
		(Chem([Bord('3'), Sub('1'), Permut('0'), ])	,	Chem([Sub('4'), Bord('0'), ])),
		(Chem([Bord('0'), Sub('0'), Permut('0'), ])	,	Chem([Sub('4'), Bord('3'), ])),
		(Chem([Bord('1'), Sub('1'), Permut('0'), ])	,	Chem([Sub('5'), Bord('2'), ])),
		(Chem([Bord('1'), Sub('2'), Permut('0'), ])	,	Chem([Sub('7'), Bord('0'), ])),
		(Chem([Bord('3'), Sub('0'), Permut('0'), ])	,	Chem([Sub('8'), Bord('0'), ])),
		(Chem([Bord('2'), Sub('2'), Permut('0'), ])	,	Chem([Sub('8'), Bord('1'), ])),
		(Chem([Bord('1'), Sub('0'), Permut('0'), ])	,	Chem([Sub('10'), Bord('2'), ])),
		(Chem([Bord('0'), Sub('1'), Permut('0'), ])	,	Chem([Sub('10'), Bord('3'), ])),
		(Chem([Bord('2'), Sub('1'), Permut('0'), ])	,	Chem([Sub('11'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('0'), Bord('1'), ])	,	Chem([Sub('11'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('1'), Bord('1'), ])	,	Chem([Sub('15'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('2'), Bord('1'), ])	,	Chem([Sub('3'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('3'), Bord('1'), ])	,	Chem([Sub('1'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('0'), Bord('1'), ])	,	Chem([Sub('11'), Bord('4'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('2'), Bord('1'), ])	,	Chem([Sub('3'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('3'), Bord('1'), ])	,	Chem([Sub('13'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('4'), Bord('1'), ])	,	Chem([Sub('9'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('0'), Bord('1'), ])	,	Chem([Sub('11'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('2'), Bord('1'), ])	,	Chem([Sub('7'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('3'), Bord('1'), ])	,	Chem([Sub('16'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('4'), Bord('1'), ])	,	Chem([Sub('15'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('3'), Bord('1'), Bord('1'), ])	,	Chem([Sub('16'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('3'), Bord('2'), Bord('1'), ])	,	Chem([Sub('6'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('4'), Bord('0'), Bord('1'), ])	,	Chem([Sub('8'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('4'), Bord('1'), Bord('1'), ])	,	Chem([Sub('9'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('4'), Bord('2'), Bord('1'), ])	,	Chem([Sub('10'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('5'), Bord('0'), Bord('1'), ])	,	Chem([Sub('14'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('5'), Bord('1'), Bord('1'), ])	,	Chem([Sub('7'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('5'), Bord('2'), Bord('1'), ])	,	Chem([Sub('10'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('6'), Bord('0'), Bord('1'), ])	,	Chem([Sub('7'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('6'), Bord('1'), Bord('1'), ])	,	Chem([Sub('12'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('6'), Bord('3'), Bord('1'), ])	,	Chem([Sub('16'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('8'), Bord('1'), Bord('1'), ])	,	Chem([Sub('11'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('8'), Bord('2'), Bord('1'), ])	,	Chem([Sub('9'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('9'), Bord('2'), Bord('1'), ])	,	Chem([Sub('10'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('11'), Bord('2'), Bord('1'), ])	,	Chem([Sub('15'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('12'), Bord('0'), Bord('1'), ])	,	Chem([Sub('14'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('12'), Bord('1'), Bord('1'), ])	,	Chem([Sub('13'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('13'), Bord('1'), Bord('1'), ])	,	Chem([Sub('14'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('15'), Bord('2'), Bord('1'), ])	,	Chem([Sub('16'), Bord('0'), Bord('1'), ])),
		(Chem([Bord('0'), Bord('1'), ])	,	Chem([Bord('1'), Bord('0'), ])),
		(Chem([Bord('1'), Bord('1'), ])	,	Chem([Bord('2'), Bord('0'), ])),
		(Chem([Bord('2'), Bord('1'), ])	,	Chem([Bord('3'), Bord('0'), ])),
		(Chem([Bord('3'), Bord('1'), ])	,	Chem([Bord('0'), Bord('0'), ])),
		]
	
	
	etat11.prim.elems = [Figure(2, [Chem([Bord('0'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('0'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('0'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('0'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('1'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('1'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('1'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('1'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('2'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('2'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('2'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('2'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('3'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('3'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('3'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('3'), Sub('1'), Sub('1'), Bord('0'), ]), ])]
	etat11.grid.elems = [
		Figure(1, [Chem([Bord('1'), Bord('0'), ]), Chem([Bord('1'), Intern(''), ]), Chem([Bord('1'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('2'), Bord('0'), ]), Chem([Bord('2'), Intern(''), ]), Chem([Bord('2'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('0'), Bord('0'), ]), Chem([Bord('0'), Intern(''), ]), Chem([Bord('0'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('3'), Bord('0'), ]), Chem([Bord('3'), Intern(''), ]), Chem([Bord('3'), Bord('1'), ]), ]), ]
	
	
	etat11.space = [Chem([Bord('0'), Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('2'), Intern('0'), Intern('0'), ]), Chem([Bord('2'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('3'), Intern('0'), Intern('0'), ]), ]
	
	etat11.initMat[Chem([Sub('0')])] = FMat([
		[Coef('Var'  , 0.097865    ), Coef('Var'  , 0.0930308   ), Coef('Var'  , 0.0848843   ), Coef('Var'  , 0.0869492   ), Coef('Var'  , 0.0856241   ), Coef('Var'  , 0.0954901   ), Coef('Var'  , 0.101571    ), Coef('Var'  , 0.101572    ), ], 
		[Coef('Var'  , 0.0825668   ), Coef('Var'  , 0.0778435   ), Coef('Var'  , 0.0706453   ), Coef('Var'  , 0.0713653   ), Coef('Var'  , 0.0696748   ), Coef('Var'  , 0.0783553   ), Coef('Var'  , 0.0842747   ), Coef('Var'  , 0.0848335   ), ], 
		[Coef('Var'  , 0.0970444   ), Coef('Var'  , 0.0895821   ), Coef('Var'  , 0.0811358   ), Coef('Var'  , 0.0825363   ), Coef('Var'  , 0.0825997   ), Coef('Var'  , 0.092995    ), Coef('Var'  , 0.102282    ), Coef('Var'  , 0.100041    ), ], 
		[Coef('Var'  , 0.105635    ), Coef('Var'  , 0.0979639   ), Coef('Var'  , 0.0905045   ), Coef('Var'  , 0.0989345   ), Coef('Var'  , 0.107514    ), Coef('Var'  , 0.11592     ), Coef('Var'  , 0.1254      ), Coef('Var'  , 0.11495     ), ], 
		[Coef('Var'  , 0.165955    ), Coef('Var'  , 0.180693    ), Coef('Var'  , 0.200424    ), Coef('Var'  , 0.212663    ), Coef('Var'  , 0.230655    ), Coef('Var'  , 0.205886    ), Coef('Var'  , 0.187494    ), Coef('Var'  , 0.173915    ), ], 
		[Coef('Var'  , 0.194969    ), Coef('Var'  , 0.210899    ), Coef('Var'  , 0.22998     ), Coef('Var'  , 0.218747    ), Coef('Var'  , 0.210923    ), Coef('Var'  , 0.188405    ), Coef('Var'  , 0.169167    ), Coef('Var'  , 0.180557    ), ], 
		[Coef('Var'  , 0.163217    ), Coef('Var'  , 0.1622      ), Coef('Var'  , 0.162382    ), Coef('Var'  , 0.146857    ), Coef('Var'  , 0.132121    ), Coef('Var'  , 0.132586    ), Coef('Var'  , 0.133331    ), Coef('Var'  , 0.147929    ), ], 
		[Coef('Var'  , 0.0927477   ), Coef('Var'  , 0.0877877   ), Coef('Var'  , 0.0800448   ), Coef('Var'  , 0.0819481   ), Coef('Var'  , 0.0808886   ), Coef('Var'  , 0.0903628   ), Coef('Var'  , 0.0964795   ), Coef('Var'  , 0.0962024   ), ], ])
	etat11.initMat[Chem([Sub('1')])] = FMat([
		[Coef('Var'  , 0.119411    ), Coef('Var'  , 0.0998984   ), Coef('Var'  , 0.078628    ), Coef('Var'  , 0.0896332   ), Coef('Var'  , 0.097865    ), Coef('Var'  , 0.103834    ), Coef('Var'  , 0.106159    ), Coef('Var'  , 0.108159    ), Coef('Var'  , 0.106662    ), Coef('Var'  , 0.11418     ), ], 
		[Coef('Var'  , 0.113725    ), Coef('Var'  , 0.0922423   ), Coef('Var'  , 0.069201    ), Coef('Var'  , 0.0769692   ), Coef('Var'  , 0.0825668   ), Coef('Var'  , 0.0880079   ), Coef('Var'  , 0.0905593   ), Coef('Var'  , 0.0950065   ), Coef('Var'  , 0.096415    ), Coef('Var'  , 0.106168    ), ], 
		[Coef('Var'  , 0.146313    ), Coef('Var'  , 0.113914    ), Coef('Var'  , 0.0816872   ), Coef('Var'  , 0.0896571   ), Coef('Var'  , 0.0970444   ), Coef('Var'  , 0.108249    ), Coef('Var'  , 0.119323    ), Coef('Var'  , 0.137649    ), Coef('Var'  , 0.15757     ), Coef('Var'  , 0.151062    ), ], 
		[Coef('Var'  , 0.0976415   ), Coef('Var'  , 0.0853732   ), Coef('Var'  , 0.0733841   ), Coef('Var'  , 0.0893898   ), Coef('Var'  , 0.105635    ), Coef('Var'  , 0.121004    ), Coef('Var'  , 0.138087    ), Coef('Var'  , 0.146863    ), Coef('Var'  , 0.159196    ), Coef('Var'  , 0.127159    ), ], 
		[Coef('Var'  , 0.0929606   ), Coef('Var'  , 0.114823    ), Coef('Var'  , 0.138533    ), Coef('Var'  , 0.150338    ), Coef('Var'  , 0.165955    ), Coef('Var'  , 0.163767    ), Coef('Var'  , 0.166631    ), Coef('Var'  , 0.150086    ), Coef('Var'  , 0.137541    ), Coef('Var'  , 0.114297    ), ], 
		[Coef('Var'  , 0.143419    ), Coef('Var'  , 0.196344    ), Coef('Var'  , 0.250451    ), Coef('Var'  , 0.221474    ), Coef('Var'  , 0.194969    ), Coef('Var'  , 0.169785    ), Coef('Var'  , 0.147057    ), Coef('Var'  , 0.131546    ), Coef('Var'  , 0.116875    ), Coef('Var'  , 0.130109    ), ], 
		[Coef('Var'  , 0.168831    ), Coef('Var'  , 0.200264    ), Coef('Var'  , 0.232969    ), Coef('Var'  , 0.197453    ), Coef('Var'  , 0.163217    ), Coef('Var'  , 0.146298    ), Coef('Var'  , 0.129989    ), Coef('Var'  , 0.124972    ), Coef('Var'  , 0.119837    ), Coef('Var'  , 0.14412     ), ], 
		[Coef('Var'  , 0.117699    ), Coef('Var'  , 0.0971409   ), Coef('Var'  , 0.0751475   ), Coef('Var'  , 0.085086    ), Coef('Var'  , 0.0927477   ), Coef('Var'  , 0.0990531   ), Coef('Var'  , 0.102193    ), Coef('Var'  , 0.105718    ), Coef('Var'  , 0.105904    ), Coef('Var'  , 0.112906    ), ], ])
	etat11.initMat[Chem([Sub('2')])] = FMat([
		[Coef('Var'  , 0.0509474   ), Coef('Var'  , 0.02608     ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0280052   ), Coef('Var'  , 0.0547101   ), Coef('Var'  , 0.0540851   ), ], 
		[Coef('Var'  , 0.0406091   ), Coef('Var'  , 0.0207146   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0224206   ), Coef('Var'  , 0.0439265   ), Coef('Var'  , 0.0431351   ), ], 
		[Coef('Var'  , 0.0560935   ), Coef('Var'  , 0.0282966   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.0625      ), Coef('Var'  , 0.0712784   ), Coef('Var'  , 0.0796862   ), Coef('Var'  , 0.068325    ), ], 
		[Coef('Var'  , 0.104817    ), Coef('Var'  , 0.0521953   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Const', 0.375       ), Coef('Var'  , 0.290286    ), Coef('Var'  , 0.206406    ), Coef('Var'  , 0.154981    ), ], 
		[Coef('Var'  , 0.33503     ), Coef('Var'  , 0.388477    ), Coef('Const', 0.444444    ), Coef('Const', 0.666667    ), Coef('Const', 1           ), Coef('Const', 0.75        ), Coef('Const', 0.5625      ), Coef('Var'  , 0.456049    ), Coef('Var'  , 0.352277    ), Coef('Var'  , 0.341054    ), ], 
		[Coef('Var'  , 0.257759    ), Coef('Var'  , 0.350566    ), Coef('Const', 0.444444    ), Coef('Const', 0.333333    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0667828   ), Coef('Var'  , 0.134471    ), Coef('Var'  , 0.195127    ), ], 
		[Coef('Var'  , 0.106188    ), Coef('Var'  , 0.1088      ), Coef('Const', 0.111111    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0382889   ), Coef('Var'  , 0.0760252   ), Coef('Var'  , 0.0915333   ), ], 
		[Coef('Var'  , 0.0485567   ), Coef('Var'  , 0.0248705   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0268894   ), Coef('Var'  , 0.0524979   ), Coef('Var'  , 0.0517598   ), ], ])
	etat11.initMat[Chem([Sub('3')])] = FMat([
		[Coef('Var'  , 0.106159    ), Coef('Var'  , 0.105816    ), Coef('Var'  , 0.101571    ), Coef('Var'  , 0.099522    ), Coef('Var'  , 0.0934803   ), Coef('Var'  , 0.0967592   ), Coef('Var'  , 0.0960241   ), Coef('Var'  , 0.103053    ), ], 
		[Coef('Var'  , 0.0905593   ), Coef('Var'  , 0.0889456   ), Coef('Var'  , 0.0842747   ), Coef('Var'  , 0.0820245   ), Coef('Var'  , 0.0767686   ), Coef('Var'  , 0.0802907   ), Coef('Var'  , 0.080706    ), Coef('Var'  , 0.0872118   ), ], 
		[Coef('Var'  , 0.119323    ), Coef('Var'  , 0.110884    ), Coef('Var'  , 0.102282    ), Coef('Var'  , 0.104504    ), Coef('Var'  , 0.106073    ), Coef('Var'  , 0.114596    ), Coef('Var'  , 0.123209    ), Coef('Var'  , 0.120976    ), ], 
		[Coef('Var'  , 0.138087    ), Coef('Var'  , 0.130638    ), Coef('Var'  , 0.1254      ), Coef('Var'  , 0.141765    ), Coef('Var'  , 0.160474    ), Coef('Var'  , 0.167739    ), Coef('Var'  , 0.178679    ), Coef('Var'  , 0.156612    ), ], 
		[Coef('Var'  , 0.166631    ), Coef('Var'  , 0.17419     ), Coef('Var'  , 0.187494    ), Coef('Var'  , 0.202171    ), Coef('Var'  , 0.223588    ), Coef('Var'  , 0.211609    ), Coef('Var'  , 0.206324    ), Coef('Var'  , 0.183629    ), ], 
		[Coef('Var'  , 0.147057    ), Coef('Var'  , 0.156865    ), Coef('Var'  , 0.169167    ), Coef('Var'  , 0.153779    ), Coef('Var'  , 0.141096    ), Coef('Var'  , 0.128822    ), Coef('Var'  , 0.118367    ), Coef('Var'  , 0.131908    ), ], 
		[Coef('Var'  , 0.129989    ), Coef('Var'  , 0.131593    ), Coef('Var'  , 0.133331    ), Coef('Var'  , 0.121383    ), Coef('Var'  , 0.108917    ), Coef('Var'  , 0.106888    ), Coef('Var'  , 0.103501    ), Coef('Var'  , 0.117098    ), ], 
		[Coef('Var'  , 0.102193    ), Coef('Var'  , 0.101069    ), Coef('Var'  , 0.0964795   ), Coef('Var'  , 0.0948523   ), Coef('Var'  , 0.0896033   ), Coef('Var'  , 0.0932951   ), Coef('Var'  , 0.0931906   ), Coef('Var'  , 0.0995123   ), ], ])
	etat11.initMat[Chem([Sub('4')])] = FMat([
		[Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.223056    ), Coef('Var'  , 0.196081    ), Coef('Var'  , 0.223056    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0978114   ), Coef('Var'  , 0.195522    ), Coef('Var'  , 0.347811    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0749182   ), Coef('Var'  , 0.149911    ), Coef('Var'  , 0.199918    ), Coef('Const', 0.25        ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0205473   ), Coef('Var'  , 0.0409801   ), Coef('Var'  , 0.0205473   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0130171   ), Coef('Var'  , 0.0259067   ), Coef('Var'  , 0.0130171   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0261576   ), Coef('Var'  , 0.0522741   ), Coef('Var'  , 0.0261576   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.196716    ), Coef('Var'  , 0.143745    ), Coef('Var'  , 0.0717156   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.347777    ), Coef('Var'  , 0.195581    ), Coef('Var'  , 0.0977771   ), Coef('Const', 0           ), Coef('Const', 0           ), ], ])
	etat11.initMat[Chem([Sub('5')])] = FMat([
		[Coef('Const', 0           ), Coef('Var'  , 0.0229577   ), Coef('Var'  , 0.0450292   ), Coef('Var'  , 0.0229577   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0207669   ), Coef('Var'  , 0.0406666   ), Coef('Var'  , 0.0207669   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.5625      ), Coef('Var'  , 0.431646    ), Coef('Var'  , 0.302002    ), Coef('Var'  , 0.275396    ), Coef('Const', 0.25        ), Coef('Const', 0.375       ), ], 
		[Coef('Const', 0.375       ), Coef('Var'  , 0.35098     ), Coef('Var'  , 0.328751    ), Coef('Var'  , 0.41348     ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0.0625      ), Coef('Var'  , 0.107832    ), Coef('Var'  , 0.153882    ), Coef('Var'  , 0.201582    ), Coef('Const', 0.25        ), Coef('Const', 0.125       ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0209745   ), Coef('Var'  , 0.0414934   ), Coef('Var'  , 0.0209745   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0212572   ), Coef('Var'  , 0.0420505   ), Coef('Var'  , 0.0212572   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0235855   ), Coef('Var'  , 0.0461254   ), Coef('Var'  , 0.0235855   ), Coef('Const', 0           ), Coef('Const', 0           ), ], ])
	etat11.initMat[Chem([Sub('6')])] = FMat([
		[Coef('Var'  , 0.0767887   ), Coef('Var'  , 0.0612843   ), Coef('Var'  , 0.0430859   ), Coef('Var'  , 0.0651231   ), Coef('Var'  , 0.0844173   ), Coef('Var'  , 0.0921076   ), Coef('Var'  , 0.0960241   ), Coef('Var'  , 0.0882687   ), ], 
		[Coef('Var'  , 0.0632572   ), Coef('Var'  , 0.0509268   ), Coef('Var'  , 0.036501    ), Coef('Var'  , 0.0562623   ), Coef('Var'  , 0.073685    ), Coef('Var'  , 0.0787696   ), Coef('Var'  , 0.080706    ), Coef('Var'  , 0.0734341   ), ], 
		[Coef('Var'  , 0.113465    ), Coef('Var'  , 0.129       ), Coef('Var'  , 0.144906    ), Coef('Var'  , 0.150609    ), Coef('Var'  , 0.158107    ), Coef('Var'  , 0.139782    ), Coef('Var'  , 0.123209    ), Coef('Var'  , 0.118172    ), ], 
		[Coef('Var'  , 0.212851    ), Coef('Var'  , 0.26742     ), Coef('Var'  , 0.325065    ), Coef('Var'  , 0.274225    ), Coef('Var'  , 0.227647    ), Coef('Var'  , 0.200641    ), Coef('Var'  , 0.178679    ), Coef('Var'  , 0.193836    ), ], 
		[Coef('Var'  , 0.265951    ), Coef('Var'  , 0.289031    ), Coef('Var'  , 0.316676    ), Coef('Var'  , 0.259047    ), Coef('Var'  , 0.204981    ), Coef('Var'  , 0.203054    ), Coef('Var'  , 0.206324    ), Coef('Var'  , 0.233038    ), ], 
		[Coef('Var'  , 0.108346    ), Coef('Var'  , 0.0777797   ), Coef('Var'  , 0.0480041   ), Coef('Var'  , 0.0664621   ), Coef('Var'  , 0.0846992   ), Coef('Var'  , 0.101355    ), Coef('Var'  , 0.118367    ), Coef('Var'  , 0.112673    ), ], 
		[Coef('Var'  , 0.0851198   ), Coef('Var'  , 0.064891    ), Coef('Var'  , 0.0432836   ), Coef('Var'  , 0.0633727   ), Coef('Var'  , 0.0819994   ), Coef('Var'  , 0.0935686   ), Coef('Var'  , 0.103501    ), Coef('Var'  , 0.0950868   ), ], 
		[Coef('Var'  , 0.0742212   ), Coef('Var'  , 0.059667    ), Coef('Var'  , 0.0424781   ), Coef('Var'  , 0.0648978   ), Coef('Var'  , 0.0844651   ), Coef('Var'  , 0.0907219   ), Coef('Var'  , 0.0931906   ), Coef('Var'  , 0.0854911   ), ], ])
	etat11.initMat[Chem([Sub('7')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0220294   ), Coef('Var'  , 0.0430859   ), Coef('Var'  , 0.0220294   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0186445   ), Coef('Var'  , 0.036501    ), Coef('Var'  , 0.0186445   ), ], 
		[Coef('Const', 0.0625      ), Coef('Const', 0.125       ), Coef('Const', 0.25        ), Coef('Var'  , 0.197258    ), Coef('Var'  , 0.144906    ), Coef('Var'  , 0.103508    ), ], 
		[Coef('Const', 0.375       ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.41185     ), Coef('Var'  , 0.325065    ), Coef('Var'  , 0.34935     ), ], 
		[Coef('Const', 0.5625      ), Coef('Const', 0.375       ), Coef('Const', 0.25        ), Coef('Var'  , 0.282601    ), Coef('Var'  , 0.316676    ), Coef('Var'  , 0.438851    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0239687   ), Coef('Var'  , 0.0480041   ), Coef('Var'  , 0.0239687   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0219208   ), Coef('Var'  , 0.0432836   ), Coef('Var'  , 0.0219208   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0217281   ), Coef('Var'  , 0.0424781   ), Coef('Var'  , 0.0217281   ), ], ])
	etat11.initMat[Chem([Sub('G')])] = FMat([
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], ])
	etat11.initMat[Chem([Sub('8')])] = FMat([
		[Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0710055   ), Coef('Var'  , 0.141865    ), Coef('Var'  , 0.196005    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0390704   ), Coef('Var'  , 0.0779321   ), Coef('Var'  , 0.0390703   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0367801   ), Coef('Var'  , 0.0736875   ), Coef('Var'  , 0.0367801   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0173471   ), Coef('Var'  , 0.0346484   ), Coef('Var'  , 0.0173471   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.111111    ), Coef('Var'  , 0.0842829   ), Coef('Var'  , 0.0574225   ), Coef('Var'  , 0.0287274   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.333333    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.302205    ), Coef('Var'  , 0.159972    ), Coef('Var'  , 0.0799834   ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.666667    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.34745     ), Coef('Var'  , 0.250834    ), Coef('Var'  , 0.250228    ), ], 
		[Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.101858    ), Coef('Var'  , 0.203639    ), Coef('Var'  , 0.351858    ), ], ])
	etat11.initMat[Chem([Sub('9')])] = FMat([
		[Coef('Var'  , 0.196081    ), Coef('Var'  , 0.169061    ), Coef('Var'  , 0.141865    ), Coef('Var'  , 0.131066    ), Coef('Var'  , 0.119411    ), Coef('Var'  , 0.131064    ), Coef('Var'  , 0.141862    ), Coef('Var'  , 0.169059    ), ], 
		[Coef('Var'  , 0.195522    ), Coef('Var'  , 0.136882    ), Coef('Var'  , 0.0779321   ), Coef('Var'  , 0.0962913   ), Coef('Var'  , 0.113725    ), Coef('Var'  , 0.158788    ), Coef('Var'  , 0.202928    ), Coef('Var'  , 0.199379    ), ], 
		[Coef('Var'  , 0.149911    ), Coef('Var'  , 0.111698    ), Coef('Var'  , 0.0736875   ), Coef('Var'  , 0.10974     ), Coef('Var'  , 0.146313    ), Coef('Var'  , 0.211294    ), Coef('Var'  , 0.276802    ), Coef('Var'  , 0.213252    ), ], 
		[Coef('Var'  , 0.0409801   ), Coef('Var'  , 0.0378944   ), Coef('Var'  , 0.0346484   ), Coef('Var'  , 0.0659887   ), Coef('Var'  , 0.0976415   ), Coef('Var'  , 0.112861    ), Coef('Var'  , 0.128396    ), Coef('Var'  , 0.084767    ), ], 
		[Coef('Var'  , 0.0259067   ), Coef('Var'  , 0.0417445   ), Coef('Var'  , 0.0574225   ), Coef('Var'  , 0.0749584   ), Coef('Var'  , 0.0929606   ), Coef('Var'  , 0.0688847   ), Coef('Var'  , 0.0452731   ), Coef('Var'  , 0.0356708   ), ], 
		[Coef('Var'  , 0.0522741   ), Coef('Var'  , 0.106141    ), Coef('Var'  , 0.159972    ), Coef('Var'  , 0.151593    ), Coef('Var'  , 0.143419    ), Coef('Var'  , 0.0960409   ), Coef('Var'  , 0.048865    ), Coef('Var'  , 0.0505887   ), ], 
		[Coef('Var'  , 0.143745    ), Coef('Var'  , 0.196944    ), Coef('Var'  , 0.250834    ), Coef('Var'  , 0.209357    ), Coef('Var'  , 0.168831    ), Coef('Var'  , 0.122557    ), Coef('Var'  , 0.0772292   ), Coef('Var'  , 0.110144    ), ], 
		[Coef('Var'  , 0.195581    ), Coef('Var'  , 0.199635    ), Coef('Var'  , 0.203639    ), Coef('Var'  , 0.161006    ), Coef('Var'  , 0.117699    ), Coef('Var'  , 0.0985104   ), Coef('Var'  , 0.0786448   ), Coef('Var'  , 0.13714     ), ], ])
	etat11.initMat[Chem([Sub('10')])] = FMat([
		[Coef('Const', 0.25        ), Coef('Var'  , 0.196004    ), Coef('Var'  , 0.141862    ), Coef('Var'  , 0.0710036   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.5         ), Coef('Var'  , 0.351567    ), Coef('Var'  , 0.202928    ), Coef('Var'  , 0.101567    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0.25        ), Coef('Var'  , 0.263334    ), Coef('Var'  , 0.276802    ), Coef('Var'  , 0.419584    ), Coef('Const', 0.5625      ), Coef('Const', 0.75        ), Coef('Const', 1           ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0642197   ), Coef('Var'  , 0.128396    ), Coef('Var'  , 0.25172     ), Coef('Const', 0.375       ), Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0226537   ), Coef('Var'  , 0.0452731   ), Coef('Var'  , 0.0539037   ), Coef('Const', 0.0625      ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0244311   ), Coef('Var'  , 0.048865    ), Coef('Var'  , 0.0244311   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0384282   ), Coef('Var'  , 0.0772292   ), Coef('Var'  , 0.0384282   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0393624   ), Coef('Var'  , 0.0786448   ), Coef('Var'  , 0.0393624   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], ])
	etat11.initMat[Chem([Sub('11')])] = FMat([
		[Coef('Var'  , 0.078628    ), Coef('Var'  , 0.0398382   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0301567   ), Coef('Var'  , 0.0590321   ), Coef('Var'  , 0.0733924   ), Coef('Var'  , 0.0848843   ), Coef('Var'  , 0.0830739   ), ], 
		[Coef('Var'  , 0.069201    ), Coef('Var'  , 0.0350214   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0243148   ), Coef('Var'  , 0.0477592   ), Coef('Var'  , 0.0602103   ), Coef('Var'  , 0.0706453   ), Coef('Var'  , 0.070917    ), ], 
		[Coef('Var'  , 0.0816872   ), Coef('Var'  , 0.040954    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0285713   ), Coef('Var'  , 0.0565522   ), Coef('Var'  , 0.0694502   ), Coef('Var'  , 0.0811358   ), Coef('Var'  , 0.0818329   ), ], 
		[Coef('Var'  , 0.0733841   ), Coef('Var'  , 0.0367317   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0377264   ), Coef('Var'  , 0.0754763   ), Coef('Var'  , 0.083032    ), Coef('Var'  , 0.0905045   ), Coef('Var'  , 0.0820374   ), ], 
		[Coef('Var'  , 0.138533    ), Coef('Var'  , 0.124148    ), Coef('Const', 0.111111    ), Coef('Const', 0.222222    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.369015    ), Coef('Var'  , 0.295948    ), Coef('Var'  , 0.24574     ), Coef('Var'  , 0.200424    ), Coef('Var'  , 0.167539    ), ], 
		[Coef('Var'  , 0.250451    ), Coef('Var'  , 0.346957    ), Coef('Const', 0.444444    ), Coef('Const', 0.555556    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.362575    ), Coef('Var'  , 0.282049    ), Coef('Var'  , 0.254514    ), Coef('Var'  , 0.22998     ), Coef('Var'  , 0.238895    ), ], 
		[Coef('Var'  , 0.232969    ), Coef('Var'  , 0.338358    ), Coef('Const', 0.444444    ), Coef('Const', 0.222222    ), Coef('Const', 0.111111    ), Coef('Var'  , 0.119213    ), Coef('Var'  , 0.127493    ), Coef('Var'  , 0.14454     ), Coef('Var'  , 0.162382    ), Coef('Var'  , 0.197018    ), ], 
		[Coef('Var'  , 0.0751475   ), Coef('Var'  , 0.037993    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0284267   ), Coef('Var'  , 0.0556908   ), Coef('Var'  , 0.0691212   ), Coef('Var'  , 0.0800448   ), Coef('Var'  , 0.0786875   ), ], ])
	etat11.initMat[Chem([Sub('12')])] = FMat([
		[Coef('Var'  , 0.0844173   ), Coef('Var'  , 0.085307    ), Coef('Var'  , 0.0827696   ), Coef('Var'  , 0.0908226   ), Coef('Var'  , 0.0954258   ), Coef('Var'  , 0.091703    ), ], 
		[Coef('Var'  , 0.073685    ), Coef('Var'  , 0.0754619   ), Coef('Var'  , 0.074123    ), Coef('Var'  , 0.0814674   ), Coef('Var'  , 0.0855626   ), Coef('Var'  , 0.0812412   ), ], 
		[Coef('Var'  , 0.158107    ), Coef('Var'  , 0.179594    ), Coef('Var'  , 0.204478    ), Coef('Var'  , 0.187993    ), Coef('Var'  , 0.175523    ), Coef('Var'  , 0.165103    ), ], 
		[Coef('Var'  , 0.227647    ), Coef('Var'  , 0.229143    ), Coef('Var'  , 0.236706    ), Coef('Var'  , 0.216476    ), Coef('Var'  , 0.20264     ), Coef('Var'  , 0.212084    ), ], 
		[Coef('Var'  , 0.204981    ), Coef('Var'  , 0.181859    ), Coef('Var'  , 0.162318    ), Coef('Var'  , 0.158987    ), Coef('Var'  , 0.15875     ), Coef('Var'  , 0.180021    ), ], 
		[Coef('Var'  , 0.0846992   ), Coef('Var'  , 0.0815389   ), Coef('Var'  , 0.0773941   ), Coef('Var'  , 0.0855098   ), Coef('Var'  , 0.0923044   ), Coef('Var'  , 0.0889576   ), ], 
		[Coef('Var'  , 0.0819994   ), Coef('Var'  , 0.0808668   ), Coef('Var'  , 0.077977    ), Coef('Var'  , 0.0864665   ), Coef('Var'  , 0.0933469   ), Coef('Var'  , 0.0885035   ), ], 
		[Coef('Var'  , 0.0844651   ), Coef('Var'  , 0.0862299   ), Coef('Var'  , 0.0842339   ), Coef('Var'  , 0.092277    ), Coef('Var'  , 0.0964472   ), Coef('Var'  , 0.0923864   ), ], ])
	etat11.initMat[Chem([Sub('13')])] = FMat([
		[Coef('Var'  , 0.106662    ), Coef('Var'  , 0.102729    ), Coef('Var'  , 0.0954258   ), Coef('Var'  , 0.0929587   ), Coef('Var'  , 0.0871028   ), Coef('Var'  , 0.0984695   ), ], 
		[Coef('Var'  , 0.096415    ), Coef('Var'  , 0.0925699   ), Coef('Var'  , 0.0855626   ), Coef('Var'  , 0.0837052   ), Coef('Var'  , 0.0786233   ), Coef('Var'  , 0.0890284   ), ], 
		[Coef('Var'  , 0.15757     ), Coef('Var'  , 0.164854    ), Coef('Var'  , 0.175523    ), Coef('Var'  , 0.187954    ), Coef('Var'  , 0.204391    ), Coef('Var'  , 0.179306    ), ], 
		[Coef('Var'  , 0.159196    ), Coef('Var'  , 0.178226    ), Coef('Var'  , 0.20264     ), Coef('Var'  , 0.209935    ), Coef('Var'  , 0.223424    ), Coef('Var'  , 0.188743    ), ], 
		[Coef('Var'  , 0.137541    ), Coef('Var'  , 0.14664     ), Coef('Var'  , 0.15875     ), Coef('Var'  , 0.152534    ), Coef('Var'  , 0.149217    ), Coef('Var'  , 0.142025    ), ], 
		[Coef('Var'  , 0.116875    ), Coef('Var'  , 0.104964    ), Coef('Var'  , 0.0923044   ), Coef('Var'  , 0.0886628   ), Coef('Var'  , 0.0837416   ), Coef('Var'  , 0.100698    ), ], 
		[Coef('Var'  , 0.119837    ), Coef('Var'  , 0.107043    ), Coef('Var'  , 0.0933469   ), Coef('Var'  , 0.0899423   ), Coef('Var'  , 0.0851289   ), Coef('Var'  , 0.102882    ), ], 
		[Coef('Var'  , 0.105904    ), Coef('Var'  , 0.102974    ), Coef('Var'  , 0.0964472   ), Coef('Var'  , 0.0943076   ), Coef('Var'  , 0.088371    ), Coef('Var'  , 0.0988484   ), ], ])
	etat11.initMat[Chem([Sub('14')])] = FMat([
		[Coef('Var'  , 0.0450292   ), Coef('Var'  , 0.0673071   ), Coef('Var'  , 0.0871028   ), Coef('Var'  , 0.0865627   ), Coef('Var'  , 0.0827696   ), Coef('Var'  , 0.065171    ), ], 
		[Coef('Var'  , 0.0406666   ), Coef('Var'  , 0.0608488   ), Coef('Var'  , 0.0786233   ), Coef('Var'  , 0.077926    ), Coef('Var'  , 0.074123    ), Coef('Var'  , 0.058611    ), ], 
		[Coef('Var'  , 0.302002    ), Coef('Var'  , 0.251599    ), Coef('Var'  , 0.204391    ), Coef('Var'  , 0.202445    ), Coef('Var'  , 0.204478    ), Coef('Var'  , 0.251638    ), ], 
		[Coef('Var'  , 0.328751    ), Coef('Var'  , 0.273707    ), Coef('Var'  , 0.223424    ), Coef('Var'  , 0.226994    ), Coef('Var'  , 0.236706    ), Coef('Var'  , 0.280247    ), ], 
		[Coef('Var'  , 0.153882    ), Coef('Var'  , 0.150541    ), Coef('Var'  , 0.149217    ), Coef('Var'  , 0.154372    ), Coef('Var'  , 0.162318    ), Coef('Var'  , 0.156995    ), ], 
		[Coef('Var'  , 0.0414934   ), Coef('Var'  , 0.0631732   ), Coef('Var'  , 0.0837416   ), Coef('Var'  , 0.0812441   ), Coef('Var'  , 0.0773941   ), Coef('Var'  , 0.0600201   ), ], 
		[Coef('Var'  , 0.0420505   ), Coef('Var'  , 0.0641479   ), Coef('Var'  , 0.0851289   ), Coef('Var'  , 0.0823056   ), Coef('Var'  , 0.077977    ), Coef('Var'  , 0.0606721   ), ], 
		[Coef('Var'  , 0.0461254   ), Coef('Var'  , 0.0686764   ), Coef('Var'  , 0.088371    ), Coef('Var'  , 0.0881511   ), Coef('Var'  , 0.0842339   ), Coef('Var'  , 0.0666458   ), ], ])
	etat11.initMat[Chem([Sub('15')])] = FMat([
		[Coef('Var'  , 0.0856241   ), Coef('Var'  , 0.0738701   ), Coef('Var'  , 0.0590321   ), Coef('Var'  , 0.0562365   ), Coef('Var'  , 0.0509474   ), Coef('Var'  , 0.0650527   ), Coef('Var'  , 0.0762029   ), Coef('Var'  , 0.0826863   ), ], 
		[Coef('Var'  , 0.0696748   ), Coef('Var'  , 0.0597844   ), Coef('Var'  , 0.0477592   ), Coef('Var'  , 0.0450292   ), Coef('Var'  , 0.0406091   ), Coef('Var'  , 0.0519645   ), Coef('Var'  , 0.0612802   ), Coef('Var'  , 0.0667197   ), ], 
		[Coef('Var'  , 0.0825997   ), Coef('Var'  , 0.0702286   ), Coef('Var'  , 0.0565522   ), Coef('Var'  , 0.0568678   ), Coef('Var'  , 0.0560935   ), Coef('Var'  , 0.0699597   ), Coef('Var'  , 0.0827265   ), Coef('Var'  , 0.0833204   ), ], 
		[Coef('Var'  , 0.107514    ), Coef('Var'  , 0.091355    ), Coef('Var'  , 0.0754763   ), Coef('Var'  , 0.0899216   ), Coef('Var'  , 0.104817    ), Coef('Var'  , 0.123014    ), Coef('Var'  , 0.142444    ), Coef('Var'  , 0.124448    ), ], 
		[Coef('Var'  , 0.230655    ), Coef('Var'  , 0.26051     ), Coef('Var'  , 0.295948    ), Coef('Var'  , 0.313048    ), Coef('Var'  , 0.33503     ), Coef('Var'  , 0.302312    ), Coef('Var'  , 0.275592    ), Coef('Var'  , 0.249773    ), ], 
		[Coef('Var'  , 0.210923    ), Coef('Var'  , 0.24494     ), Coef('Var'  , 0.282049    ), Coef('Var'  , 0.268697    ), Coef('Var'  , 0.257759    ), Coef('Var'  , 0.21868     ), Coef('Var'  , 0.182081    ), Coef('Var'  , 0.194923    ), ], 
		[Coef('Var'  , 0.132121    ), Coef('Var'  , 0.129632    ), Coef('Var'  , 0.127493    ), Coef('Var'  , 0.116902    ), Coef('Var'  , 0.106188    ), Coef('Var'  , 0.106979    ), Coef('Var'  , 0.107011    ), Coef('Var'  , 0.119709    ), ], 
		[Coef('Var'  , 0.0808886   ), Coef('Var'  , 0.0696801   ), Coef('Var'  , 0.0556908   ), Coef('Var'  , 0.053297    ), Coef('Var'  , 0.0485567   ), Coef('Var'  , 0.0620381   ), Coef('Var'  , 0.0726622   ), Coef('Var'  , 0.0784211   ), ], ])
	etat11.initMat[Chem([Sub('16')])] = FMat([
		[Coef('Var'  , 0.0934803   ), Coef('Var'  , 0.0867181   ), Coef('Var'  , 0.0762029   ), Coef('Var'  , 0.0669781   ), Coef('Var'  , 0.0547101   ), Coef('Var'  , 0.0672601   ), Coef('Var'  , 0.0767887   ), Coef('Var'  , 0.0870002   ), ], 
		[Coef('Var'  , 0.0767686   ), Coef('Var'  , 0.0703889   ), Coef('Var'  , 0.0612802   ), Coef('Var'  , 0.0536707   ), Coef('Var'  , 0.0439265   ), Coef('Var'  , 0.0547029   ), Coef('Var'  , 0.0632572   ), Coef('Var'  , 0.0714212   ), ], 
		[Coef('Var'  , 0.106073    ), Coef('Var'  , 0.0948293   ), Coef('Var'  , 0.0827265   ), Coef('Var'  , 0.0816915   ), Coef('Var'  , 0.0796862   ), Coef('Var'  , 0.0967706   ), Coef('Var'  , 0.113465    ), Coef('Var'  , 0.109908    ), ], 
		[Coef('Var'  , 0.160474    ), Coef('Var'  , 0.150293    ), Coef('Var'  , 0.142444    ), Coef('Var'  , 0.173605    ), Coef('Var'  , 0.206406    ), Coef('Var'  , 0.208356    ), Coef('Var'  , 0.212851    ), Coef('Var'  , 0.185044    ), ], 
		[Coef('Var'  , 0.223588    ), Coef('Var'  , 0.246058    ), Coef('Var'  , 0.275592    ), Coef('Var'  , 0.310856    ), Coef('Var'  , 0.352277    ), Coef('Var'  , 0.306229    ), Coef('Var'  , 0.265951    ), Coef('Var'  , 0.241432    ), ], 
		[Coef('Var'  , 0.141096    ), Coef('Var'  , 0.160297    ), Coef('Var'  , 0.182081    ), Coef('Var'  , 0.157119    ), Coef('Var'  , 0.134471    ), Coef('Var'  , 0.120594    ), Coef('Var'  , 0.108346    ), Coef('Var'  , 0.123772    ), ], 
		[Coef('Var'  , 0.108917    ), Coef('Var'  , 0.108506    ), Coef('Var'  , 0.107011    ), Coef('Var'  , 0.0920235   ), Coef('Var'  , 0.0760252   ), Coef('Var'  , 0.0812591   ), Coef('Var'  , 0.0851198   ), Coef('Var'  , 0.0977414   ), ], 
		[Coef('Var'  , 0.0896033   ), Coef('Var'  , 0.0829106   ), Coef('Var'  , 0.0726622   ), Coef('Var'  , 0.064057    ), Coef('Var'  , 0.0524979   ), Coef('Var'  , 0.0648282   ), Coef('Var'  , 0.0742212   ), Coef('Var'  , 0.0836818   ), ], ])
	
	
	
	etat12.bords   = {Bord('0'): etat19, Bord('1'): etat22, Bord('2'): etat21, Bord('3'): etat19, }
	etat12.permuts = {}
	etat12.interns = {Intern('_'): etat12, }
	etat12.subs    = {Sub('0'): etat1, Sub('1'): etat2, Sub('2'): etat3, Sub('3'): etat4, Sub('4'): etat5, Sub('5'): etat6, Sub('6'): etat7, Sub('7'): etat8, Sub('G', True): Etat.etatPoint, Sub('8'): etat9, Sub('9'): etat10, Sub('10'): etat11, Sub('11'): etat13, Sub('12'): etat14, Sub('13'): etat15, Sub('14'): etat16, Sub('15'): etat17, Sub('16'): etat18, }
	
	etat12.buildIntern()
	
	
	etat12.eqs = [
		(Chem([Bord('1'), Sub('1'), Permut('0'), ])	,	Chem([Sub('1'), Bord('4'), ])),
		(Chem([Bord('2'), Sub('2'), Permut('0'), ])	,	Chem([Sub('2'), Bord('2'), ])),
		(Chem([Bord('0'), Sub('0'), Permut('0'), ])	,	Chem([Sub('4'), Bord('2'), ])),
		(Chem([Bord('3'), Sub('1'), Permut('0'), ])	,	Chem([Sub('4'), Bord('3'), ])),
		(Chem([Bord('1'), Sub('4'), Permut('0'), ])	,	Chem([Sub('5'), Bord('0'), ])),
		(Chem([Bord('2'), Sub('0'), Permut('0'), ])	,	Chem([Sub('5'), Bord('2'), ])),
		(Chem([Bord('2'), Sub('1'), Permut('0'), ])	,	Chem([Sub('7'), Bord('0'), ])),
		(Chem([Bord('1'), Sub('0'), Permut('0'), ])	,	Chem([Sub('9'), Bord('2'), ])),
		(Chem([Bord('0'), Sub('1'), Permut('0'), ])	,	Chem([Sub('9'), Bord('3'), ])),
		(Chem([Bord('3'), Sub('0'), Permut('0'), ])	,	Chem([Sub('10'), Bord('0'), ])),
		(Chem([Bord('2'), Sub('3'), Permut('0'), ])	,	Chem([Sub('10'), Bord('1'), ])),
		(Chem([Bord('1'), Sub('2'), Permut('0'), ])	,	Chem([Sub('13'), Bord('2'), ])),
		(Chem([Bord('1'), Sub('3'), Permut('0'), ])	,	Chem([Sub('14'), Bord('0'), ])),
		(Chem([Sub('0'), Bord('0'), Bord('1'), ])	,	Chem([Sub('11'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('1'), Bord('1'), ])	,	Chem([Sub('15'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('2'), Bord('1'), ])	,	Chem([Sub('3'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('3'), Bord('1'), ])	,	Chem([Sub('1'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('0'), Bord('1'), ])	,	Chem([Sub('11'), Bord('4'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('2'), Bord('1'), ])	,	Chem([Sub('3'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('3'), Bord('1'), ])	,	Chem([Sub('13'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('4'), Bord('1'), ])	,	Chem([Sub('9'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('0'), Bord('1'), ])	,	Chem([Sub('11'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('1'), Bord('1'), ])	,	Chem([Sub('10'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('2'), Bord('1'), ])	,	Chem([Sub('7'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('3'), Bord('1'), ])	,	Chem([Sub('16'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('4'), Bord('1'), ])	,	Chem([Sub('15'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('3'), Bord('1'), Bord('1'), ])	,	Chem([Sub('16'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('3'), Bord('2'), Bord('1'), ])	,	Chem([Sub('6'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('4'), Bord('0'), Bord('1'), ])	,	Chem([Sub('8'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('4'), Bord('1'), Bord('1'), ])	,	Chem([Sub('9'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('4'), Bord('3'), Bord('1'), ])	,	Chem([Sub('10'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('5'), Bord('0'), Bord('1'), ])	,	Chem([Sub('14'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('5'), Bord('1'), Bord('1'), ])	,	Chem([Sub('7'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('6'), Bord('0'), Bord('1'), ])	,	Chem([Sub('7'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('6'), Bord('1'), Bord('1'), ])	,	Chem([Sub('12'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('6'), Bord('3'), Bord('1'), ])	,	Chem([Sub('16'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('8'), Bord('0'), Bord('1'), ])	,	Chem([Sub('10'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('8'), Bord('1'), Bord('1'), ])	,	Chem([Sub('11'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('8'), Bord('2'), Bord('1'), ])	,	Chem([Sub('9'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('11'), Bord('2'), Bord('1'), ])	,	Chem([Sub('15'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('12'), Bord('0'), Bord('1'), ])	,	Chem([Sub('14'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('12'), Bord('1'), Bord('1'), ])	,	Chem([Sub('13'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('13'), Bord('1'), Bord('1'), ])	,	Chem([Sub('14'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('15'), Bord('2'), Bord('1'), ])	,	Chem([Sub('16'), Bord('0'), Bord('1'), ])),
		(Chem([Bord('0'), Bord('1'), ])	,	Chem([Bord('1'), Bord('0'), ])),
		(Chem([Bord('1'), Bord('1'), ])	,	Chem([Bord('2'), Bord('0'), ])),
		(Chem([Bord('2'), Bord('1'), ])	,	Chem([Bord('3'), Bord('0'), ])),
		(Chem([Bord('3'), Bord('1'), ])	,	Chem([Bord('0'), Bord('0'), ])),
		]
	
	
	etat12.prim.elems = [Figure(2, [Chem([Bord('0'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('0'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('0'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('0'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('1'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('1'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('1'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('1'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('2'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('2'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('2'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('2'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('3'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('3'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('3'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('3'), Sub('1'), Sub('1'), Bord('0'), ]), ])]
	etat12.grid.elems = [
		Figure(1, [Chem([Bord('1'), Bord('0'), ]), Chem([Bord('1'), Intern(''), ]), Chem([Bord('1'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('2'), Bord('0'), ]), Chem([Bord('2'), Intern(''), ]), Chem([Bord('2'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('0'), Bord('0'), ]), Chem([Bord('0'), Intern(''), ]), Chem([Bord('0'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('3'), Bord('0'), ]), Chem([Bord('3'), Intern(''), ]), Chem([Bord('3'), Bord('1'), ]), ]), ]
	
	
	etat12.space = [Chem([Bord('0'), Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('2'), Intern('0'), Intern('0'), ]), Chem([Bord('2'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('3'), Intern('0'), Intern('0'), ]), ]
	
	etat12.initMat[Chem([Sub('0')])] = FMat([
		[Coef('Var'  , 0.082022    ), Coef('Var'  , 0.0866509   ), Coef('Var'  , 0.0879773   ), Coef('Var'  , 0.0914416   ), Coef('Var'  , 0.0914614   ), Coef('Var'  , 0.0902323   ), Coef('Var'  , 0.0852131   ), Coef('Var'  , 0.0854417   ), ], 
		[Coef('Var'  , 0.0821625   ), Coef('Var'  , 0.0867953   ), Coef('Var'  , 0.0883001   ), Coef('Var'  , 0.0920551   ), Coef('Var'  , 0.0924473   ), Coef('Var'  , 0.0910928   ), Coef('Var'  , 0.0859485   ), Coef('Var'  , 0.0858331   ), ], 
		[Coef('Var'  , 0.217596    ), Coef('Var'  , 0.204888    ), Coef('Var'  , 0.196668    ), Coef('Var'  , 0.170743    ), Coef('Var'  , 0.148785    ), Coef('Var'  , 0.158567    ), Coef('Var'  , 0.172166    ), Coef('Var'  , 0.192712    ), ], 
		[Coef('Var'  , 0.209621    ), Coef('Var'  , 0.191536    ), Coef('Var'  , 0.174586    ), Coef('Var'  , 0.165608    ), Coef('Var'  , 0.157494    ), Coef('Var'  , 0.177079    ), Coef('Var'  , 0.198039    ), Coef('Var'  , 0.203007    ), ], 
		[Coef('Var'  , 0.121573    ), Coef('Var'  , 0.116733    ), Coef('Var'  , 0.112581    ), Coef('Var'  , 0.120892    ), Coef('Var'  , 0.129898    ), Coef('Var'  , 0.135189    ), Coef('Var'  , 0.142101    ), Coef('Var'  , 0.131029    ), ], 
		[Coef('Var'  , 0.108787    ), Coef('Var'  , 0.118099    ), Coef('Var'  , 0.128782    ), Coef('Var'  , 0.140196    ), Coef('Var'  , 0.153836    ), Coef('Var'  , 0.140388    ), Coef('Var'  , 0.129352    ), Coef('Var'  , 0.118291    ), ], 
		[Coef('Var'  , 0.103183    ), Coef('Var'  , 0.115922    ), Coef('Var'  , 0.130309    ), Coef('Var'  , 0.13543     ), Coef('Var'  , 0.14264     ), Coef('Var'  , 0.125399    ), Coef('Var'  , 0.109839    ), Coef('Var'  , 0.105892    ), ], 
		[Coef('Var'  , 0.0750556   ), Coef('Var'  , 0.0793758   ), Coef('Var'  , 0.0807968   ), Coef('Var'  , 0.083634    ), Coef('Var'  , 0.0834389   ), Coef('Var'  , 0.0820531   ), Coef('Var'  , 0.0773416   ), Coef('Var'  , 0.0777949   ), ], ])
	etat12.initMat[Chem([Sub('1')])] = FMat([
		[Coef('Const', 0           ), Coef('Var'  , 0.0366363   ), Coef('Var'  , 0.0722293   ), Coef('Var'  , 0.0784894   ), Coef('Var'  , 0.082022    ), Coef('Var'  , 0.0742241   ), Coef('Var'  , 0.0631453   ), Coef('Var'  , 0.0323709   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0365807   ), Coef('Var'  , 0.0721996   ), Coef('Var'  , 0.0784602   ), Coef('Var'  , 0.0821625   ), Coef('Var'  , 0.0744285   ), Coef('Var'  , 0.0635276   ), Coef('Var'  , 0.032549    ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.64        ), Coef('Var'  , 0.473687    ), Coef('Var'  , 0.309135    ), Coef('Var'  , 0.261324    ), Coef('Var'  , 0.217596    ), Coef('Var'  , 0.215808    ), Coef('Var'  , 0.217957    ), Coef('Var'  , 0.28817     ), Coef('Const', 0.36        ), Coef('Const', 0.48        ), ], 
		[Coef('Const', 0.32        ), Coef('Var'  , 0.26158     ), Coef('Var'  , 0.203421    ), Coef('Var'  , 0.206025    ), Coef('Var'  , 0.209621    ), Coef('Var'  , 0.239303    ), Coef('Var'  , 0.270627    ), Coef('Var'  , 0.374859    ), Coef('Const', 0.48        ), Coef('Const', 0.44        ), ], 
		[Coef('Const', 0.04        ), Coef('Var'  , 0.0619038   ), Coef('Var'  , 0.0837922   ), Coef('Var'  , 0.102424    ), Coef('Var'  , 0.121573    ), Coef('Var'  , 0.137205    ), Coef('Var'  , 0.15448     ), Coef('Var'  , 0.156685    ), Coef('Const', 0.16        ), Coef('Const', 0.08        ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0441283   ), Coef('Var'  , 0.0884978   ), Coef('Var'  , 0.098255    ), Coef('Var'  , 0.108787    ), Coef('Var'  , 0.10168     ), Coef('Var'  , 0.0957439   ), Coef('Var'  , 0.0475534   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0511532   ), Coef('Var'  , 0.103001    ), Coef('Var'  , 0.102427    ), Coef('Var'  , 0.103183    ), Coef('Var'  , 0.0897733   ), Coef('Var'  , 0.0772873   ), Coef('Var'  , 0.0384998   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0343305   ), Coef('Var'  , 0.067725    ), Coef('Var'  , 0.0725958   ), Coef('Var'  , 0.0750556   ), Coef('Var'  , 0.067578    ), Coef('Var'  , 0.0572316   ), Coef('Var'  , 0.0293126   ), Coef('Const', 0           ), Coef('Const', 0           ), ], ])
	etat12.initMat[Chem([Sub('2')])] = FMat([
		[Coef('Var'  , 0.0803421   ), Coef('Var'  , 0.077058    ), Coef('Var'  , 0.0713607   ), Coef('Var'  , 0.0361477   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0313677   ), Coef('Var'  , 0.0613428   ), Coef('Var'  , 0.072278    ), ], 
		[Coef('Var'  , 0.0819551   ), Coef('Var'  , 0.0783533   ), Coef('Var'  , 0.0721692   ), Coef('Var'  , 0.0365724   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0322246   ), Coef('Var'  , 0.0629066   ), Coef('Var'  , 0.0740055   ), ], 
		[Coef('Var'  , 0.105546    ), Coef('Var'  , 0.105939    ), Coef('Var'  , 0.108006    ), Coef('Var'  , 0.0535627   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0384569   ), Coef('Var'  , 0.0773347   ), Coef('Var'  , 0.0908329   ), ], 
		[Coef('Var'  , 0.11103     ), Coef('Var'  , 0.100114    ), Coef('Var'  , 0.0891795   ), Coef('Var'  , 0.0446388   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0466421   ), Coef('Var'  , 0.0936222   ), Coef('Var'  , 0.102117    ), ], 
		[Coef('Var'  , 0.136694    ), Coef('Var'  , 0.115328    ), Coef('Var'  , 0.0944765   ), Coef('Var'  , 0.0784925   ), Coef('Const', 0.0625      ), Coef('Const', 0.125       ), Coef('Const', 0.25        ), Coef('Var'  , 0.217987    ), Coef('Var'  , 0.187012    ), Coef('Var'  , 0.161072    ), ], 
		[Coef('Var'  , 0.212712    ), Coef('Var'  , 0.213918    ), Coef('Var'  , 0.217846    ), Coef('Var'  , 0.295949    ), Coef('Const', 0.375       ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.388841    ), Coef('Var'  , 0.279299    ), Coef('Var'  , 0.244309    ), ], 
		[Coef('Var'  , 0.197883    ), Coef('Var'  , 0.237732    ), Coef('Var'  , 0.279869    ), Coef('Var'  , 0.420663    ), Coef('Const', 0.5625      ), Coef('Const', 0.375       ), Coef('Const', 0.25        ), Coef('Var'  , 0.215927    ), Coef('Var'  , 0.182627    ), Coef('Var'  , 0.189246    ), ], 
		[Coef('Var'  , 0.0738373   ), Coef('Var'  , 0.0715589   ), Coef('Var'  , 0.0670931   ), Coef('Var'  , 0.0339739   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0285541   ), Coef('Var'  , 0.0558563   ), Coef('Var'  , 0.0661391   ), ], ])
	etat12.initMat[Chem([Sub('3')])] = FMat([
		[Coef('Var'  , 0.0631453   ), Coef('Var'  , 0.0759595   ), Coef('Var'  , 0.0852131   ), Coef('Var'  , 0.0853901   ), Coef('Var'  , 0.0814497   ), Coef('Var'  , 0.0763726   ), Coef('Var'  , 0.0670471   ), Coef('Var'  , 0.066942    ), ], 
		[Coef('Var'  , 0.0635276   ), Coef('Var'  , 0.0765026   ), Coef('Var'  , 0.0859485   ), Coef('Var'  , 0.0865437   ), Coef('Var'  , 0.0829184   ), Coef('Var'  , 0.0776314   ), Coef('Var'  , 0.067954    ), Coef('Var'  , 0.0675904   ), ], 
		[Coef('Var'  , 0.217957    ), Coef('Var'  , 0.193245    ), Coef('Var'  , 0.172166    ), Coef('Var'  , 0.147977    ), Coef('Var'  , 0.126981    ), Coef('Var'  , 0.132381    ), Coef('Var'  , 0.139985    ), Coef('Var'  , 0.177648    ), ], 
		[Coef('Var'  , 0.270627    ), Coef('Var'  , 0.233421    ), Coef('Var'  , 0.198039    ), Coef('Var'  , 0.180388    ), Coef('Var'  , 0.164695    ), Coef('Var'  , 0.183593    ), Coef('Var'  , 0.204854    ), Coef('Var'  , 0.236627    ), ], 
		[Coef('Var'  , 0.15448     ), Coef('Var'  , 0.147193    ), Coef('Var'  , 0.142101    ), Coef('Var'  , 0.157123    ), Coef('Var'  , 0.175153    ), Coef('Var'  , 0.1889      ), Coef('Var'  , 0.206861    ), Coef('Var'  , 0.17897     ), ], 
		[Coef('Var'  , 0.0957439   ), Coef('Var'  , 0.111718    ), Coef('Var'  , 0.129352    ), Coef('Var'  , 0.14908     ), Coef('Var'  , 0.171468    ), Coef('Var'  , 0.160707    ), Coef('Var'  , 0.152828    ), Coef('Var'  , 0.123345    ), ], 
		[Coef('Var'  , 0.0772873   ), Coef('Var'  , 0.0931184   ), Coef('Var'  , 0.109839    ), Coef('Var'  , 0.116174    ), Coef('Var'  , 0.123648    ), Coef('Var'  , 0.111438    ), Coef('Var'  , 0.0999524   ), Coef('Var'  , 0.0883819   ), ], 
		[Coef('Var'  , 0.0572316   ), Coef('Var'  , 0.0688421   ), Coef('Var'  , 0.0773416   ), Coef('Var'  , 0.0773232   ), Coef('Var'  , 0.073687    ), Coef('Var'  , 0.0689773   ), Coef('Var'  , 0.0605186   ), Coef('Var'  , 0.0604962   ), ], ])
	etat12.initMat[Chem([Sub('4')])] = FMat([
		[Coef('Const', 0.25        ), Coef('Var'  , 0.222197    ), Coef('Var'  , 0.194333    ), Coef('Var'  , 0.222197    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0972286   ), Coef('Var'  , 0.194387    ), Coef('Var'  , 0.347229    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0807745   ), Coef('Var'  , 0.161917    ), Coef('Var'  , 0.205774    ), Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0197994   ), Coef('Var'  , 0.0394666   ), Coef('Var'  , 0.0197994   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.00847035  ), Coef('Var'  , 0.0167864   ), Coef('Var'  , 0.00847035  ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0222491   ), Coef('Var'  , 0.0443581   ), Coef('Var'  , 0.0222491   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.25        ), Coef('Var'  , 0.202199    ), Coef('Var'  , 0.154682    ), Coef('Var'  , 0.0771986   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.5         ), Coef('Var'  , 0.347082    ), Coef('Var'  , 0.19407     ), Coef('Var'  , 0.0970824   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), ], ])
	etat12.initMat[Chem([Sub('5')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 1.31758e-17 ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 1.31405e-17 ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.04        ), Coef('Var'  , 0.02        ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.2         ), Coef('Const', 0.32        ), Coef('Var'  , 0.16        ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 1           ), Coef('Const', 0.8         ), Coef('Const', 0.64        ), Coef('Var'  , 0.60125     ), Coef('Const', 0.5625      ), Coef('Const', 0.75        ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.1875      ), Coef('Const', 0.375       ), Coef('Const', 0.25        ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.03125     ), Coef('Const', 0.0625      ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 1.31328e-17 ), Coef('Const', 0           ), Coef('Const', 0           ), ], ])
	etat12.initMat[Chem([Sub('6')])] = FMat([
		[Coef('Var'  , 0.0648589   ), Coef('Var'  , 0.0478795   ), Coef('Var'  , 0.0279273   ), Coef('Var'  , 0.0328529   ), Coef('Var'  , 0.0351772   ), Coef('Var'  , 0.0529291   ), Coef('Var'  , 0.0670471   ), Coef('Var'  , 0.0679557   ), ], 
		[Coef('Var'  , 0.066207    ), Coef('Var'  , 0.0487859   ), Coef('Var'  , 0.0282868   ), Coef('Var'  , 0.033021    ), Coef('Var'  , 0.0352269   ), Coef('Var'  , 0.0533882   ), Coef('Var'  , 0.067954    ), Coef('Var'  , 0.0691531   ), ], 
		[Coef('Var'  , 0.0980631   ), Coef('Var'  , 0.0766027   ), Coef('Var'  , 0.0560101   ), Coef('Var'  , 0.0921459   ), Coef('Var'  , 0.128936    ), Coef('Var'  , 0.133734    ), Coef('Var'  , 0.139985    ), Coef('Var'  , 0.118191    ), ], 
		[Coef('Var'  , 0.137397    ), Coef('Var'  , 0.116649    ), Coef('Var'  , 0.0976368   ), Coef('Var'  , 0.178365    ), Coef('Var'  , 0.261119    ), Coef('Var'  , 0.231684    ), Coef('Var'  , 0.204854    ), Coef('Var'  , 0.169968    ), ], 
		[Coef('Var'  , 0.219095    ), Coef('Var'  , 0.272821    ), Coef('Var'  , 0.33004     ), Coef('Var'  , 0.315063    ), Coef('Var'  , 0.303675    ), Coef('Var'  , 0.253039    ), Coef('Var'  , 0.206861    ), Coef('Var'  , 0.210797    ), ], 
		[Coef('Var'  , 0.223227    ), Coef('Var'  , 0.263764    ), Coef('Var'  , 0.30651     ), Coef('Var'  , 0.220164    ), Coef('Var'  , 0.135111    ), Coef('Var'  , 0.14303     ), Coef('Var'  , 0.152828    ), Coef('Var'  , 0.18663     ), ], 
		[Coef('Var'  , 0.132536    ), Coef('Var'  , 0.130273    ), Coef('Var'  , 0.1284      ), Coef('Var'  , 0.0987639   ), Coef('Var'  , 0.0690263   ), Coef('Var'  , 0.0844562   ), Coef('Var'  , 0.0999524   ), Coef('Var'  , 0.115965    ), ], 
		[Coef('Var'  , 0.0586175   ), Coef('Var'  , 0.0432246   ), Coef('Var'  , 0.02519     ), Coef('Var'  , 0.0296245   ), Coef('Var'  , 0.0317284   ), Coef('Var'  , 0.047739    ), Coef('Var'  , 0.0605186   ), Coef('Var'  , 0.0613392   ), ], ])
	etat12.initMat[Chem([Sub('7')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0144948   ), Coef('Var'  , 0.0279273   ), Coef('Var'  , 0.0144948   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0146742   ), Coef('Var'  , 0.0282868   ), Coef('Var'  , 0.0146742   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0278893   ), Coef('Var'  , 0.0560101   ), Coef('Var'  , 0.0278893   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0484483   ), Coef('Var'  , 0.0976368   ), Coef('Var'  , 0.0484483   ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0.375       ), Coef('Const', 0.5625      ), Coef('Var'  , 0.445559    ), Coef('Var'  , 0.33004     ), Coef('Var'  , 0.289309    ), ], 
		[Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0.375       ), Coef('Var'  , 0.340426    ), Coef('Var'  , 0.30651     ), Coef('Var'  , 0.402926    ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0.125       ), Coef('Const', 0.0625      ), Coef('Var'  , 0.0954398   ), Coef('Var'  , 0.1284      ), Coef('Var'  , 0.18919     ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0130691   ), Coef('Var'  , 0.02519     ), Coef('Var'  , 0.0130691   ), ], ])
	etat12.initMat[Chem([Sub('G')])] = FMat([
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], ])
	etat12.initMat[Chem([Sub('8')])] = FMat([
		[Coef('Var'  , 0.194333    ), Coef('Var'  , 0.166401    ), Coef('Var'  , 0.138252    ), Coef('Var'  , 0.122885    ), Coef('Var'  , 0.106772    ), Coef('Var'  , 0.122886    ), Coef('Var'  , 0.138253    ), Coef('Var'  , 0.166402    ), ], 
		[Coef('Var'  , 0.194387    ), Coef('Var'  , 0.135222    ), Coef('Var'  , 0.0758262   ), Coef('Var'  , 0.0917724   ), Coef('Var'  , 0.106976    ), Coef('Var'  , 0.15427     ), Coef('Var'  , 0.200824    ), Coef('Var'  , 0.19772     ), ], 
		[Coef('Var'  , 0.161917    ), Coef('Var'  , 0.125267    ), Coef('Var'  , 0.0894983   ), Coef('Var'  , 0.144674    ), Coef('Var'  , 0.201516    ), Coef('Var'  , 0.255918    ), Coef('Var'  , 0.311991    ), Coef('Var'  , 0.236511    ), ], 
		[Coef('Var'  , 0.0394666   ), Coef('Var'  , 0.0390256   ), Coef('Var'  , 0.0383164   ), Coef('Var'  , 0.0755657   ), Coef('Var'  , 0.112553    ), Coef('Var'  , 0.115563    ), Coef('Var'  , 0.118314    ), Coef('Var'  , 0.0790233   ), ], 
		[Coef('Var'  , 0.0167864   ), Coef('Var'  , 0.0263769   ), Coef('Var'  , 0.0356324   ), Coef('Var'  , 0.0487843   ), Coef('Var'  , 0.061511    ), Coef('Var'  , 0.0459714   ), Coef('Var'  , 0.0300068   ), Coef('Var'  , 0.023564    ), ], 
		[Coef('Var'  , 0.0443581   ), Coef('Var'  , 0.0897967   ), Coef('Var'  , 0.135004    ), Coef('Var'  , 0.127507    ), Coef('Var'  , 0.120067    ), Coef('Var'  , 0.0806344   ), Coef('Var'  , 0.041257    ), Coef('Var'  , 0.0429242   ), ], 
		[Coef('Var'  , 0.154682    ), Coef('Var'  , 0.220696    ), Coef('Var'  , 0.287385    ), Coef('Var'  , 0.236302    ), Coef('Var'  , 0.18643     ), Coef('Var'  , 0.134747    ), Coef('Var'  , 0.0842693   ), Coef('Var'  , 0.119141    ), ], 
		[Coef('Var'  , 0.19407     ), Coef('Var'  , 0.197215    ), Coef('Var'  , 0.200085    ), Coef('Var'  , 0.152509    ), Coef('Var'  , 0.104175    ), Coef('Var'  , 0.0900091   ), Coef('Var'  , 0.0750856   ), Coef('Var'  , 0.134715    ), ], ])
	etat12.initMat[Chem([Sub('9')])] = FMat([
		[Coef('Const', 0.25        ), Coef('Var'  , 0.194204    ), Coef('Var'  , 0.138253    ), Coef('Var'  , 0.0692044   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.5         ), Coef('Var'  , 0.350491    ), Coef('Var'  , 0.200824    ), Coef('Var'  , 0.100491    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0.25        ), Coef('Var'  , 0.280736    ), Coef('Var'  , 0.311991    ), Coef('Var'  , 0.475736    ), Coef('Const', 0.64        ), Coef('Const', 0.8         ), Coef('Const', 1           ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0592239   ), Coef('Var'  , 0.118314    ), Coef('Var'  , 0.219224    ), Coef('Const', 0.32        ), Coef('Const', 0.2         ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0150936   ), Coef('Var'  , 0.0300068   ), Coef('Var'  , 0.0350936   ), Coef('Const', 0.04        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0206751   ), Coef('Var'  , 0.041257    ), Coef('Var'  , 0.0206751   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0419421   ), Coef('Var'  , 0.0842693   ), Coef('Var'  , 0.0419421   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.037633    ), Coef('Var'  , 0.0750856   ), Coef('Var'  , 0.037633    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], ])
	etat12.initMat[Chem([Sub('10')])] = FMat([
		[Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0692037   ), Coef('Var'  , 0.138252    ), Coef('Var'  , 0.194204    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0379935   ), Coef('Var'  , 0.0758262   ), Coef('Var'  , 0.0379935   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0444927   ), Coef('Var'  , 0.0894983   ), Coef('Var'  , 0.0444927   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0192262   ), Coef('Var'  , 0.0383164   ), Coef('Var'  , 0.0192262   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.0625      ), Coef('Var'  , 0.0491566   ), Coef('Var'  , 0.0356324   ), Coef('Var'  , 0.0179066   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Const', 0.375       ), Coef('Var'  , 0.255048    ), Coef('Var'  , 0.135004    ), Coef('Var'  , 0.0675477   ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.75        ), Coef('Const', 0.5625      ), Coef('Var'  , 0.424747    ), Coef('Var'  , 0.287385    ), Coef('Var'  , 0.268497    ), ], 
		[Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.100132    ), Coef('Var'  , 0.200085    ), Coef('Var'  , 0.350132    ), ], ])
	etat12.initMat[Chem([Sub('11')])] = FMat([
		[Coef('Var'  , 0.0722293   ), Coef('Var'  , 0.090318    ), Coef('Var'  , 0.106772    ), Coef('Var'  , 0.0898295   ), Coef('Var'  , 0.0713607   ), Coef('Var'  , 0.0805607   ), Coef('Var'  , 0.087293    ), Coef('Var'  , 0.0892108   ), Coef('Var'  , 0.0879773   ), Coef('Var'  , 0.0814341   ), ], 
		[Coef('Var'  , 0.0721996   ), Coef('Var'  , 0.0903596   ), Coef('Var'  , 0.106976    ), Coef('Var'  , 0.0903512   ), Coef('Var'  , 0.0721692   ), Coef('Var'  , 0.0814779   ), Coef('Var'  , 0.0882694   ), Coef('Var'  , 0.0898214   ), Coef('Var'  , 0.0883001   ), Coef('Var'  , 0.0814966   ), ], 
		[Coef('Var'  , 0.309135    ), Coef('Var'  , 0.253869    ), Coef('Var'  , 0.201516    ), Coef('Var'  , 0.153744    ), Coef('Var'  , 0.108006    ), Coef('Var'  , 0.120523    ), Coef('Var'  , 0.135402    ), Coef('Var'  , 0.164212    ), Coef('Var'  , 0.196668    ), Coef('Var'  , 0.250938    ), ], 
		[Coef('Var'  , 0.203421    ), Coef('Var'  , 0.15792     ), Coef('Var'  , 0.112553    ), Coef('Var'  , 0.100978    ), Coef('Var'  , 0.0891795   ), Coef('Var'  , 0.110872    ), Coef('Var'  , 0.132587    ), Coef('Var'  , 0.153325    ), Coef('Var'  , 0.174586    ), Coef('Var'  , 0.188672    ), ], 
		[Coef('Var'  , 0.0837922   ), Coef('Var'  , 0.0727815   ), Coef('Var'  , 0.061511    ), Coef('Var'  , 0.0781203   ), Coef('Var'  , 0.0944765   ), Coef('Var'  , 0.106031    ), Coef('Var'  , 0.117738    ), Coef('Var'  , 0.115       ), Coef('Var'  , 0.112581    ), Coef('Var'  , 0.0981159   ), ], 
		[Coef('Var'  , 0.0884978   ), Coef('Var'  , 0.104088    ), Coef('Var'  , 0.120067    ), Coef('Var'  , 0.168409    ), Coef('Var'  , 0.217846    ), Coef('Var'  , 0.194921    ), Coef('Var'  , 0.174332    ), Coef('Var'  , 0.150444    ), Coef('Var'  , 0.128782    ), Coef('Var'  , 0.1081      ), ], 
		[Coef('Var'  , 0.103001    ), Coef('Var'  , 0.143958    ), Coef('Var'  , 0.18643     ), Coef('Var'  , 0.232218    ), Coef('Var'  , 0.279869    ), Coef('Var'  , 0.23081     ), Coef('Var'  , 0.184078    ), Coef('Var'  , 0.156046    ), Coef('Var'  , 0.130309    ), Coef('Var'  , 0.115802    ), ], 
		[Coef('Var'  , 0.067725    ), Coef('Var'  , 0.0867066   ), Coef('Var'  , 0.104175    ), Coef('Var'  , 0.08635     ), Coef('Var'  , 0.0670931   ), Coef('Var'  , 0.0748047   ), Coef('Var'  , 0.0803004   ), Coef('Var'  , 0.0819412   ), Coef('Var'  , 0.0807968   ), Coef('Var'  , 0.0754409   ), ], ])
	etat12.initMat[Chem([Sub('12')])] = FMat([
		[Coef('Var'  , 0.0351772   ), Coef('Var'  , 0.026044    ), Coef('Var'  , 0.0145628   ), Coef('Var'  , 0.0153718   ), Coef('Var'  , 0.0145628   ), Coef('Var'  , 0.0260439   ), ], 
		[Coef('Var'  , 0.0352269   ), Coef('Var'  , 0.0258868   ), Coef('Var'  , 0.0143466   ), Coef('Var'  , 0.01508     ), Coef('Var'  , 0.0143466   ), Coef('Var'  , 0.0258868   ), ], 
		[Coef('Var'  , 0.128936    ), Coef('Var'  , 0.129346    ), Coef('Var'  , 0.130345    ), Coef('Var'  , 0.162178    ), Coef('Var'  , 0.194345    ), Coef('Var'  , 0.161345    ), ], 
		[Coef('Var'  , 0.261119    ), Coef('Var'  , 0.310369    ), Coef('Var'  , 0.361696    ), Coef('Var'  , 0.376904    ), Coef('Var'  , 0.393696    ), Coef('Var'  , 0.326369    ), ], 
		[Coef('Var'  , 0.303675    ), Coef('Var'  , 0.349256    ), Coef('Var'  , 0.398258    ), Coef('Var'  , 0.349003    ), Coef('Var'  , 0.302258    ), Coef('Var'  , 0.301256    ), ], 
		[Coef('Var'  , 0.135111    ), Coef('Var'  , 0.0892408   ), Coef('Var'  , 0.044209    ), Coef('Var'  , 0.0440047   ), Coef('Var'  , 0.0442091   ), Coef('Var'  , 0.0892408   ), ], 
		[Coef('Var'  , 0.0690263   ), Coef('Var'  , 0.0463571   ), Coef('Var'  , 0.0234285   ), Coef('Var'  , 0.0235662   ), Coef('Var'  , 0.0234285   ), Coef('Var'  , 0.0463572   ), ], 
		[Coef('Var'  , 0.0317284   ), Coef('Var'  , 0.0235016   ), Coef('Var'  , 0.0131543   ), Coef('Var'  , 0.0138924   ), Coef('Var'  , 0.0131544   ), Coef('Var'  , 0.0235016   ), ], ])
	etat12.initMat[Chem([Sub('13')])] = FMat([
		[Coef('Const', 0           ), Coef('Var'  , 0.00768589  ), Coef('Var'  , 0.0145628   ), Coef('Var'  , 0.00768589  ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.00753999  ), Coef('Var'  , 0.0143466   ), Coef('Var'  , 0.00753999  ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.36        ), Coef('Var'  , 0.277089    ), Coef('Var'  , 0.194345    ), Coef('Var'  , 0.177089    ), Coef('Const', 0.16        ), Coef('Const', 0.24        ), ], 
		[Coef('Const', 0.48        ), Coef('Var'  , 0.436452    ), Coef('Var'  , 0.393696    ), Coef('Var'  , 0.436452    ), Coef('Const', 0.48        ), Coef('Const', 0.52        ), ], 
		[Coef('Const', 0.16        ), Coef('Var'  , 0.230502    ), Coef('Var'  , 0.302258    ), Coef('Var'  , 0.330502    ), Coef('Const', 0.36        ), Coef('Const', 0.24        ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0220024   ), Coef('Var'  , 0.0442091   ), Coef('Var'  , 0.0220024   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0117831   ), Coef('Var'  , 0.0234285   ), Coef('Var'  , 0.0117831   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0069462   ), Coef('Var'  , 0.0131544   ), Coef('Var'  , 0.0069462   ), Coef('Const', 0           ), Coef('Const', 0           ), ], ])
	etat12.initMat[Chem([Sub('14')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.00768592  ), Coef('Var'  , 0.0145628   ), Coef('Var'  , 0.00768592  ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.00754001  ), Coef('Var'  , 0.0143466   ), Coef('Var'  , 0.00754001  ), ], 
		[Coef('Const', 0.04        ), Coef('Const', 0.08        ), Coef('Const', 0.16        ), Coef('Var'  , 0.145089    ), Coef('Var'  , 0.130345    ), Coef('Var'  , 0.085089    ), ], 
		[Coef('Const', 0.32        ), Coef('Const', 0.44        ), Coef('Const', 0.48        ), Coef('Var'  , 0.420452    ), Coef('Var'  , 0.361696    ), Coef('Var'  , 0.340452    ), ], 
		[Coef('Const', 0.64        ), Coef('Const', 0.48        ), Coef('Const', 0.36        ), Coef('Var'  , 0.378502    ), Coef('Var'  , 0.398258    ), Coef('Var'  , 0.518502    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0220023   ), Coef('Var'  , 0.044209    ), Coef('Var'  , 0.0220023   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0117831   ), Coef('Var'  , 0.0234285   ), Coef('Var'  , 0.0117831   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.00694617  ), Coef('Var'  , 0.0131543   ), Coef('Var'  , 0.00694617  ), ], ])
	etat12.initMat[Chem([Sub('15')])] = FMat([
		[Coef('Var'  , 0.0914614   ), Coef('Var'  , 0.0910568   ), Coef('Var'  , 0.087293    ), Coef('Var'  , 0.0853233   ), Coef('Var'  , 0.0803421   ), Coef('Var'  , 0.0837915   ), Coef('Var'  , 0.0839515   ), Coef('Var'  , 0.089525    ), ], 
		[Coef('Var'  , 0.0924473   ), Coef('Var'  , 0.0920447   ), Coef('Var'  , 0.0882694   ), Coef('Var'  , 0.0866864   ), Coef('Var'  , 0.0819551   ), Coef('Var'  , 0.0856301   ), Coef('Var'  , 0.085738    ), Coef('Var'  , 0.0909884   ), ], 
		[Coef('Var'  , 0.148785    ), Coef('Var'  , 0.140453    ), Coef('Var'  , 0.135402    ), Coef('Var'  , 0.119337    ), Coef('Var'  , 0.105546    ), Coef('Var'  , 0.10776     ), Coef('Var'  , 0.111704    ), Coef('Var'  , 0.128877    ), ], 
		[Coef('Var'  , 0.157494    ), Coef('Var'  , 0.144749    ), Coef('Var'  , 0.132587    ), Coef('Var'  , 0.121708    ), Coef('Var'  , 0.11103     ), Coef('Var'  , 0.120425    ), Coef('Var'  , 0.130338    ), Coef('Var'  , 0.143466    ), ], 
		[Coef('Var'  , 0.129898    ), Coef('Var'  , 0.123468    ), Coef('Var'  , 0.117738    ), Coef('Var'  , 0.126873    ), Coef('Var'  , 0.136694    ), Coef('Var'  , 0.144581    ), Coef('Var'  , 0.154063    ), Coef('Var'  , 0.141176    ), ], 
		[Coef('Var'  , 0.153836    ), Coef('Var'  , 0.162696    ), Coef('Var'  , 0.174332    ), Coef('Var'  , 0.19194     ), Coef('Var'  , 0.212712    ), Coef('Var'  , 0.204018    ), Coef('Var'  , 0.199009    ), Coef('Var'  , 0.174773    ), ], 
		[Coef('Var'  , 0.14264     ), Coef('Var'  , 0.162178    ), Coef('Var'  , 0.184078    ), Coef('Var'  , 0.189716    ), Coef('Var'  , 0.197883    ), Coef('Var'  , 0.177184    ), Coef('Var'  , 0.158765    ), Coef('Var'  , 0.149646    ), ], 
		[Coef('Var'  , 0.0834389   ), Coef('Var'  , 0.0833545   ), Coef('Var'  , 0.0803004   ), Coef('Var'  , 0.0784158   ), Coef('Var'  , 0.0738373   ), Coef('Var'  , 0.0766101   ), Coef('Var'  , 0.0764326   ), Coef('Var'  , 0.0815488   ), ], ])
	etat12.initMat[Chem([Sub('16')])] = FMat([
		[Coef('Var'  , 0.0814497   ), Coef('Var'  , 0.0846827   ), Coef('Var'  , 0.0839515   ), Coef('Var'  , 0.0742489   ), Coef('Var'  , 0.0613428   ), Coef('Var'  , 0.0647523   ), Coef('Var'  , 0.0648589   ), Coef('Var'  , 0.0751862   ), ], 
		[Coef('Var'  , 0.0829184   ), Coef('Var'  , 0.0864393   ), Coef('Var'  , 0.085738    ), Coef('Var'  , 0.0760738   ), Coef('Var'  , 0.0629066   ), Coef('Var'  , 0.0663364   ), Coef('Var'  , 0.066207    ), Coef('Var'  , 0.0767019   ), ], 
		[Coef('Var'  , 0.126981    ), Coef('Var'  , 0.118287    ), Coef('Var'  , 0.111704    ), Coef('Var'  , 0.0938412   ), Coef('Var'  , 0.0773347   ), Coef('Var'  , 0.0871703   ), Coef('Var'  , 0.0980631   ), Coef('Var'  , 0.111616    ), ], 
		[Coef('Var'  , 0.164695    ), Coef('Var'  , 0.146775    ), Coef('Var'  , 0.130338    ), Coef('Var'  , 0.111592    ), Coef('Var'  , 0.0936222   ), Coef('Var'  , 0.114843    ), Coef('Var'  , 0.137397    ), Coef('Var'  , 0.150026    ), ], 
		[Coef('Var'  , 0.175153    ), Coef('Var'  , 0.163111    ), Coef('Var'  , 0.154063    ), Coef('Var'  , 0.169483    ), Coef('Var'  , 0.187012    ), Coef('Var'  , 0.201499    ), Coef('Var'  , 0.219095    ), Coef('Var'  , 0.195127    ), ], 
		[Coef('Var'  , 0.171468    ), Coef('Var'  , 0.183465    ), Coef('Var'  , 0.199009    ), Coef('Var'  , 0.23739     ), Coef('Var'  , 0.279299    ), Coef('Var'  , 0.249679    ), Coef('Var'  , 0.223227    ), Coef('Var'  , 0.195754    ), ], 
		[Coef('Var'  , 0.123648    ), Coef('Var'  , 0.140421    ), Coef('Var'  , 0.158765    ), Coef('Var'  , 0.169793    ), Coef('Var'  , 0.182627    ), Coef('Var'  , 0.15701     ), Coef('Var'  , 0.132536    ), Coef('Var'  , 0.127639    ), ], 
		[Coef('Var'  , 0.073687    ), Coef('Var'  , 0.0768189   ), Coef('Var'  , 0.0764326   ), Coef('Var'  , 0.0675792   ), Coef('Var'  , 0.0558563   ), Coef('Var'  , 0.0587096   ), Coef('Var'  , 0.0586175   ), Coef('Var'  , 0.0679493   ), ], ])
	
	
	
	etat13.bords   = {Bord('0'): etat20, Bord('1'): etat20, Bord('2'): etat19, Bord('3'): etat19, Bord('4'): etat19, }
	etat13.permuts = {}
	etat13.interns = {Intern('_'): etat13, }
	etat13.subs    = {Sub('0'): etat1, Sub('1'): etat2, Sub('2'): etat3, Sub('3'): etat4, Sub('4'): etat5, Sub('5'): etat6, Sub('6'): etat7, Sub('7'): etat8, Sub('G', True): Etat.etatPoint, Sub('8'): etat9, Sub('9'): etat10, Sub('10'): etat11, Sub('11'): etat12, Sub('12'): etat14, Sub('13'): etat15, Sub('14'): etat16, Sub('15'): etat17, Sub('16'): etat18, }
	
	etat13.buildIntern()
	
	
	etat13.eqs = [
		(Chem([Bord('4'), Sub('0'), Permut('0'), ])	,	Chem([Sub('0'), Bord('0'), ])),
		(Chem([Bord('3'), Sub('1'), Permut('0'), ])	,	Chem([Sub('0'), Bord('1'), ])),
		(Chem([Bord('0'), Sub('0'), Permut('0'), ])	,	Chem([Sub('1'), Bord('0'), ])),
		(Chem([Bord('4'), Sub('1'), Permut('0'), ])	,	Chem([Sub('1'), Bord('1'), ])),
		(Chem([Bord('2'), Sub('0'), Permut('0'), ])	,	Chem([Sub('2'), Bord('0'), ])),
		(Chem([Bord('1'), Sub('2'), Permut('0'), ])	,	Chem([Sub('2'), Bord('1'), ])),
		(Chem([Bord('1'), Sub('0'), Permut('0'), ])	,	Chem([Sub('8'), Bord('1'), ])),
		(Chem([Bord('0'), Sub('2'), Permut('0'), ])	,	Chem([Sub('8'), Bord('2'), ])),
		(Chem([Bord('0'), Sub('1'), Permut('0'), ])	,	Chem([Sub('9'), Bord('1'), ])),
		(Chem([Bord('1'), Sub('1'), Permut('0'), ])	,	Chem([Sub('10'), Bord('2'), ])),
		(Chem([Bord('3'), Sub('0'), Permut('0'), ])	,	Chem([Sub('15'), Bord('0'), ])),
		(Chem([Bord('2'), Sub('1'), Permut('0'), ])	,	Chem([Sub('15'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('1'), Bord('1'), ])	,	Chem([Sub('15'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('2'), Bord('1'), ])	,	Chem([Sub('3'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('3'), Bord('1'), ])	,	Chem([Sub('1'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('2'), Bord('1'), ])	,	Chem([Sub('3'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('3'), Bord('1'), ])	,	Chem([Sub('13'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('4'), Bord('1'), ])	,	Chem([Sub('9'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('1'), Bord('1'), ])	,	Chem([Sub('10'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('2'), Bord('1'), ])	,	Chem([Sub('7'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('3'), Bord('1'), ])	,	Chem([Sub('16'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('4'), Bord('1'), ])	,	Chem([Sub('15'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('3'), Bord('1'), Bord('1'), ])	,	Chem([Sub('16'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('3'), Bord('2'), Bord('1'), ])	,	Chem([Sub('6'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('4'), Bord('0'), Bord('1'), ])	,	Chem([Sub('8'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('4'), Bord('1'), Bord('1'), ])	,	Chem([Sub('9'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('4'), Bord('2'), Bord('1'), ])	,	Chem([Sub('11'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('4'), Bord('3'), Bord('1'), ])	,	Chem([Sub('10'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('5'), Bord('0'), Bord('1'), ])	,	Chem([Sub('14'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('5'), Bord('1'), Bord('1'), ])	,	Chem([Sub('7'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('5'), Bord('2'), Bord('1'), ])	,	Chem([Sub('11'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('6'), Bord('0'), Bord('1'), ])	,	Chem([Sub('7'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('6'), Bord('1'), Bord('1'), ])	,	Chem([Sub('12'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('6'), Bord('3'), Bord('1'), ])	,	Chem([Sub('16'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('8'), Bord('0'), Bord('1'), ])	,	Chem([Sub('10'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('8'), Bord('2'), Bord('1'), ])	,	Chem([Sub('9'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('9'), Bord('2'), Bord('1'), ])	,	Chem([Sub('11'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('10'), Bord('0'), Bord('1'), ])	,	Chem([Sub('11'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('12'), Bord('0'), Bord('1'), ])	,	Chem([Sub('14'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('12'), Bord('1'), Bord('1'), ])	,	Chem([Sub('13'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('13'), Bord('1'), Bord('1'), ])	,	Chem([Sub('14'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('15'), Bord('2'), Bord('1'), ])	,	Chem([Sub('16'), Bord('0'), Bord('1'), ])),
		(Chem([Bord('0'), Bord('1'), ])	,	Chem([Bord('1'), Bord('0'), ])),
		(Chem([Bord('1'), Bord('1'), ])	,	Chem([Bord('2'), Bord('0'), ])),
		(Chem([Bord('2'), Bord('1'), ])	,	Chem([Bord('3'), Bord('0'), ])),
		(Chem([Bord('3'), Bord('1'), ])	,	Chem([Bord('4'), Bord('0'), ])),
		(Chem([Bord('4'), Bord('1'), ])	,	Chem([Bord('0'), Bord('0'), ])),
		]
	
	
	etat13.prim.elems = [Figure(2, [Chem([Bord('0'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('0'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('0'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('0'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('1'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('1'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('1'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('1'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('2'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('2'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('2'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('2'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('3'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('3'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('3'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('3'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('4'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('4'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('4'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('4'), Sub('1'), Sub('1'), Bord('0'), ]), ])]
	etat13.grid.elems = [
		Figure(1, [Chem([Bord('1'), Bord('0'), ]), Chem([Bord('1'), Intern(''), ]), Chem([Bord('1'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('4'), Bord('0'), ]), Chem([Bord('4'), Intern(''), ]), Chem([Bord('4'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('2'), Bord('0'), ]), Chem([Bord('2'), Intern(''), ]), Chem([Bord('2'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('0'), Bord('0'), ]), Chem([Bord('0'), Intern(''), ]), Chem([Bord('0'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('3'), Bord('0'), ]), Chem([Bord('3'), Intern(''), ]), Chem([Bord('3'), Bord('1'), ]), ]), ]
	
	
	etat13.space = [Chem([Bord('4'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('2'), Intern('0'), Intern('0'), ]), Chem([Bord('2'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('3'), Intern('0'), Intern('0'), ]), Chem([Bord('4'), Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('4'), Intern('0'), Intern('0'), ]), ]
	
	etat13.initMat[Chem([Sub('0')])] = FMat([
		[Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0736445   ), Coef('Var'  , 0.14616     ), Coef('Var'  , 0.198645    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0155525   ), Coef('Var'  , 0.0309066   ), Coef('Var'  , 0.0155525   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.00416087  ), Coef('Var'  , 0.00905222  ), Coef('Var'  , 0.00416087  ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.00528681  ), Coef('Var'  , 0.0113369   ), Coef('Var'  , 0.00528681  ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0275237   ), Coef('Var'  , 0.0536808   ), Coef('Var'  , 0.0275237   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0258087   ), Coef('Var'  , 0.0510846   ), Coef('Var'  , 0.0258087   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.179556    ), Coef('Var'  , 0.109579    ), Coef('Var'  , 0.0545564   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.343445    ), Coef('Var'  , 0.186672    ), Coef('Var'  , 0.0934445   ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.207777    ), Coef('Var'  , 0.168103    ), Coef('Var'  , 0.207777    ), ], 
		[Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.117245    ), Coef('Var'  , 0.233423    ), Coef('Var'  , 0.367245    ), ], ])
	etat13.initMat[Chem([Sub('1')])] = FMat([
		[Coef('Const', 0.444444    ), Coef('Const', 0.666667    ), Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.223156    ), Coef('Var'  , 0.19622     ), Coef('Var'  , 0.216005    ), Coef('Var'  , 0.237159    ), Coef('Var'  , 0.340071    ), ], 
		[Coef('Const', 0.444444    ), Coef('Const', 0.333333    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0374554   ), Coef('Var'  , 0.0749045   ), Coef('Var'  , 0.136005    ), Coef('Var'  , 0.197789    ), Coef('Var'  , 0.320771    ), ], 
		[Coef('Const', 0.111111    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.015659    ), Coef('Var'  , 0.0312865   ), Coef('Var'  , 0.0576563   ), Coef('Var'  , 0.0833353   ), Coef('Var'  , 0.0975529   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0134441   ), Coef('Var'  , 0.0269421   ), Coef('Var'  , 0.0396802   ), Coef('Var'  , 0.0518994   ), Coef('Var'  , 0.0262361   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0316306   ), Coef('Var'  , 0.0627107   ), Coef('Var'  , 0.0614197   ), Coef('Var'  , 0.060193    ), Coef('Var'  , 0.0297892   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0283289   ), Coef('Var'  , 0.0563336   ), Coef('Var'  , 0.0549292   ), Coef('Var'  , 0.0530088   ), Coef('Var'  , 0.0266003   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0332508   ), Coef('Var'  , 0.066619    ), Coef('Var'  , 0.0633383   ), Coef('Var'  , 0.0595528   ), Coef('Var'  , 0.0300876   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0461724   ), Coef('Var'  , 0.0921267   ), Coef('Var'  , 0.078732    ), Coef('Var'  , 0.0646766   ), Coef('Var'  , 0.0325596   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.19106     ), Coef('Var'  , 0.133487    ), Coef('Var'  , 0.101982    ), Coef('Var'  , 0.0712477   ), Coef('Var'  , 0.0359224   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.379843    ), Coef('Var'  , 0.25937     ), Coef('Var'  , 0.190253    ), Coef('Var'  , 0.121138    ), Coef('Var'  , 0.06041     ), ], ])
	etat13.initMat[Chem([Sub('2')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0377708   ), Coef('Var'  , 0.0746623   ), Coef('Var'  , 0.0743102   ), Coef('Var'  , 0.0701549   ), Coef('Var'  , 0.0365395   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0261768   ), Coef('Var'  , 0.0522175   ), Coef('Var'  , 0.0433245   ), Coef('Var'  , 0.0339143   ), Coef('Var'  , 0.0171477   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.111111    ), Coef('Var'  , 0.0907347   ), Coef('Var'  , 0.0711586   ), Coef('Var'  , 0.0441282   ), Coef('Var'  , 0.020153    ), Coef('Var'  , 0.00894908  ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.333333    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.315983    ), Coef('Var'  , 0.188598    ), Coef('Var'  , 0.122385    ), Coef('Var'  , 0.0596304   ), Coef('Var'  , 0.0286249   ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.666667    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.350597    ), Coef('Var'  , 0.256234    ), Coef('Var'  , 0.237901    ), Coef('Var'  , 0.216275    ), Coef('Var'  , 0.234527    ), ], 
		[Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0595557   ), Coef('Var'  , 0.118729    ), Coef('Var'  , 0.187243    ), Coef('Var'  , 0.254313    ), Coef('Var'  , 0.377687    ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0415753   ), Coef('Var'  , 0.0833186   ), Coef('Var'  , 0.120363    ), Coef('Var'  , 0.158566    ), Coef('Var'  , 0.203787    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0324237   ), Coef('Var'  , 0.0643808   ), Coef('Var'  , 0.0791538   ), Coef('Var'  , 0.0928552   ), Coef('Var'  , 0.0467302   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.00799854  ), Coef('Var'  , 0.0177572   ), Coef('Var'  , 0.0137239   ), Coef('Var'  , 0.0166488   ), Coef('Var'  , 0.00572541  ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0371853   ), Coef('Var'  , 0.0729429   ), Coef('Var'  , 0.0774669   ), Coef('Var'  , 0.0774893   ), Coef('Var'  , 0.0402816   ), ], ])
	etat13.initMat[Chem([Sub('3')])] = FMat([
		[Coef('Var'  , 0.19622     ), Coef('Var'  , 0.171801    ), Coef('Var'  , 0.14616     ), Coef('Var'  , 0.138496    ), Coef('Var'  , 0.12647     ), Coef('Var'  , 0.140297    ), Coef('Var'  , 0.149508    ), Coef('Var'  , 0.173602    ), ], 
		[Coef('Var'  , 0.0749045   ), Coef('Var'  , 0.0530079   ), Coef('Var'  , 0.0309066   ), Coef('Var'  , 0.0391637   ), Coef('Var'  , 0.0467101   ), Coef('Var'  , 0.0593238   ), Coef('Var'  , 0.0710848   ), Coef('Var'  , 0.0731681   ), ], 
		[Coef('Var'  , 0.0312865   ), Coef('Var'  , 0.0198199   ), Coef('Var'  , 0.00905222  ), Coef('Var'  , 0.00941442  ), Coef('Var'  , 0.0127812   ), Coef('Var'  , 0.021722    ), Coef('Var'  , 0.0337013   ), Coef('Var'  , 0.0321275   ), ], 
		[Coef('Var'  , 0.0269421   ), Coef('Var'  , 0.018731    ), Coef('Var'  , 0.0113369   ), Coef('Var'  , 0.0174646   ), Coef('Var'  , 0.0267258   ), Coef('Var'  , 0.0349322   ), Coef('Var'  , 0.0464862   ), Coef('Var'  , 0.0361986   ), ], 
		[Coef('Var'  , 0.0627107   ), Coef('Var'  , 0.0591543   ), Coef('Var'  , 0.0536808   ), Coef('Var'  , 0.0980398   ), Coef('Var'  , 0.137593    ), Coef('Var'  , 0.136364    ), Coef('Var'  , 0.129988    ), Coef('Var'  , 0.0974781   ), ], 
		[Coef('Var'  , 0.0563336   ), Coef('Var'  , 0.0541377   ), Coef('Var'  , 0.0510846   ), Coef('Var'  , 0.0976095   ), Coef('Var'  , 0.14233     ), Coef('Var'  , 0.130737    ), Coef('Var'  , 0.117184    ), Coef('Var'  , 0.0872649   ), ], 
		[Coef('Var'  , 0.066619    ), Coef('Var'  , 0.0878072   ), Coef('Var'  , 0.109579    ), Coef('Var'  , 0.117243    ), Coef('Var'  , 0.126607    ), Coef('Var'  , 0.111758    ), Coef('Var'  , 0.0987905   ), Coef('Var'  , 0.0823227   ), ], 
		[Coef('Var'  , 0.0921267   ), Coef('Var'  , 0.139617    ), Coef('Var'  , 0.186672    ), Coef('Var'  , 0.169759    ), Coef('Var'  , 0.152033    ), Coef('Var'  , 0.133648    ), Coef('Var'  , 0.114228    ), Coef('Var'  , 0.103507    ), ], 
		[Coef('Var'  , 0.133487    ), Coef('Var'  , 0.148837    ), Coef('Var'  , 0.168103    ), Coef('Var'  , 0.112696    ), Coef('Var'  , 0.0661673   ), Coef('Var'  , 0.0587255   ), Coef('Var'  , 0.0613598   ), Coef('Var'  , 0.0948668   ), ], 
		[Coef('Var'  , 0.25937     ), Coef('Var'  , 0.247088    ), Coef('Var'  , 0.233423    ), Coef('Var'  , 0.200115    ), Coef('Var'  , 0.162582    ), Coef('Var'  , 0.172493    ), Coef('Var'  , 0.17767     ), Coef('Var'  , 0.219465    ), ], ])
	etat13.initMat[Chem([Sub('4')])] = FMat([
		[Coef('Var'  , 0.0650907   ), Coef('Var'  , 0.0696112   ), Coef('Var'  , 0.0746117   ), Coef('Var'  , 0.099181    ), Coef('Var'  , 0.124263    ), Coef('Var'  , 0.119097    ), Coef('Var'  , 0.114742    ), Coef('Var'  , 0.089527    ), ], 
		[Coef('Var'  , 0.121436    ), Coef('Var'  , 0.162972    ), Coef('Var'  , 0.206589    ), Coef('Var'  , 0.236944    ), Coef('Var'  , 0.269436    ), Coef('Var'  , 0.225357    ), Coef('Var'  , 0.184283    ), Coef('Var'  , 0.151385    ), ], 
		[Coef('Var'  , 0.309845    ), Coef('Var'  , 0.339774    ), Coef('Var'  , 0.373303    ), Coef('Var'  , 0.339798    ), Coef('Var'  , 0.30988     ), Coef('Var'  , 0.275681    ), Coef('Var'  , 0.246422    ), Coef('Var'  , 0.275657    ), ], 
		[Coef('Var'  , 0.27216     ), Coef('Var'  , 0.238887    ), Coef('Var'  , 0.207835    ), Coef('Var'  , 0.164887    ), Coef('Var'  , 0.12412     ), Coef('Var'  , 0.154749    ), Coef('Var'  , 0.188444    ), Coef('Var'  , 0.228749    ), ], 
		[Coef('Var'  , 0.128147    ), Coef('Var'  , 0.102168    ), Coef('Var'  , 0.0766269   ), Coef('Var'  , 0.0725815   ), Coef('Var'  , 0.0689508   ), Coef('Var'  , 0.094358    ), Coef('Var'  , 0.120471    ), Coef('Var'  , 0.123944    ), ], 
		[Coef('Var'  , 0.0193235   ), Coef('Var'  , 0.0160156   ), Coef('Var'  , 0.0112295   ), Coef('Var'  , 0.0160012   ), Coef('Var'  , 0.0193026   ), Coef('Var'  , 0.0243753   ), Coef('Var'  , 0.0273966   ), Coef('Var'  , 0.0243897   ), ], 
		[Coef('Var'  , 0.0233261   ), Coef('Var'  , 0.0195972   ), Coef('Var'  , 0.0138302   ), Coef('Var'  , 0.0196089   ), Coef('Var'  , 0.023343    ), Coef('Var'  , 0.0295463   ), Coef('Var'  , 0.0328389   ), Coef('Var'  , 0.0295346   ), ], 
		[Coef('Var'  , 0.0174348   ), Coef('Var'  , 0.0144645   ), Coef('Var'  , 0.0101485   ), Coef('Var'  , 0.0144694   ), Coef('Var'  , 0.0174419   ), Coef('Var'  , 0.0220412   ), Coef('Var'  , 0.0247282   ), Coef('Var'  , 0.0220362   ), ], 
		[Coef('Var'  , 0.0222143   ), Coef('Var'  , 0.0190116   ), Coef('Var'  , 0.0135286   ), Coef('Var'  , 0.0190352   ), Coef('Var'  , 0.0222485   ), Coef('Var'  , 0.0282443   ), Coef('Var'  , 0.0309341   ), Coef('Var'  , 0.0282207   ), ], 
		[Coef('Var'  , 0.0210233   ), Coef('Var'  , 0.0175      ), Coef('Var'  , 0.0122972   ), Coef('Var'  , 0.0174935   ), Coef('Var'  , 0.0210139   ), Coef('Var'  , 0.0265505   ), Coef('Var'  , 0.02974     ), Coef('Var'  , 0.026557    ), ], ])
	etat13.initMat[Chem([Sub('5')])] = FMat([
		[Coef('Var'  , 0.124665    ), Coef('Var'  , 0.124885    ), Coef('Var'  , 0.128167    ), Coef('Var'  , 0.116704    ), Coef('Var'  , 0.1079      ), Coef('Var'  , 0.11536     ), ], 
		[Coef('Var'  , 0.142218    ), Coef('Var'  , 0.130978    ), Coef('Var'  , 0.122306    ), Coef('Var'  , 0.108679    ), Coef('Var'  , 0.0968279   ), Coef('Var'  , 0.118583    ), ], 
		[Coef('Var'  , 0.14642     ), Coef('Var'  , 0.126577    ), Coef('Var'  , 0.107998    ), Coef('Var'  , 0.102105    ), Coef('Var'  , 0.0965168   ), Coef('Var'  , 0.120628    ), ], 
		[Coef('Var'  , 0.158234    ), Coef('Var'  , 0.139994    ), Coef('Var'  , 0.122801    ), Coef('Var'  , 0.133519    ), Coef('Var'  , 0.144867    ), Coef('Var'  , 0.150758    ), ], 
		[Coef('Var'  , 0.144443    ), Coef('Var'  , 0.133492    ), Coef('Var'  , 0.125144    ), Coef('Var'  , 0.148855    ), Coef('Var'  , 0.175       ), Coef('Var'  , 0.158672    ), ], 
		[Coef('Var'  , 0.06053     ), Coef('Var'  , 0.07076     ), Coef('Var'  , 0.0799214   ), Coef('Var'  , 0.0882229   ), Coef('Var'  , 0.0958637   ), Coef('Var'  , 0.0786916   ), ], 
		[Coef('Var'  , 0.0619299   ), Coef('Var'  , 0.0735087   ), Coef('Var'  , 0.0822633   ), Coef('Var'  , 0.0834274   ), Coef('Var'  , 0.0824714   ), Coef('Var'  , 0.0733334   ), ], 
		[Coef('Var'  , 0.0523435   ), Coef('Var'  , 0.064338    ), Coef('Var'  , 0.074474    ), Coef('Var'  , 0.0739073   ), Coef('Var'  , 0.071755    ), Coef('Var'  , 0.0628832   ), ], 
		[Coef('Var'  , 0.0458288   ), Coef('Var'  , 0.0562534   ), Coef('Var'  , 0.062885    ), Coef('Var'  , 0.0533185   ), Coef('Var'  , 0.041193    ), Coef('Var'  , 0.0448383   ), ], 
		[Coef('Var'  , 0.0633883   ), Coef('Var'  , 0.0792129   ), Coef('Var'  , 0.0940396   ), Coef('Var'  , 0.0912629   ), Coef('Var'  , 0.0876051   ), Coef('Var'  , 0.0762532   ), ], ])
	etat13.initMat[Chem([Sub('6')])] = FMat([
		[Coef('Var'  , 0.121445    ), Coef('Var'  , 0.117922    ), Coef('Var'  , 0.111501    ), Coef('Var'  , 0.124392    ), Coef('Var'  , 0.138261    ), Coef('Var'  , 0.143973    ), Coef('Var'  , 0.149508    ), Coef('Var'  , 0.137503    ), ], 
		[Coef('Var'  , 0.0586554   ), Coef('Var'  , 0.0683175   ), Coef('Var'  , 0.0772774   ), Coef('Var'  , 0.0889452   ), Coef('Var'  , 0.100893    ), Coef('Var'  , 0.0859554   ), Coef('Var'  , 0.0710848   ), Coef('Var'  , 0.0653278   ), ], 
		[Coef('Var'  , 0.0283995   ), Coef('Var'  , 0.046196    ), Coef('Var'  , 0.0659253   ), Coef('Var'  , 0.0691491   ), Coef('Var'  , 0.0718563   ), Coef('Var'  , 0.0527471   ), Coef('Var'  , 0.0337013   ), Coef('Var'  , 0.0297939   ), ], 
		[Coef('Var'  , 0.0571186   ), Coef('Var'  , 0.0859489   ), Coef('Var'  , 0.117353    ), Coef('Var'  , 0.102124    ), Coef('Var'  , 0.087078    ), Coef('Var'  , 0.0664901   ), Coef('Var'  , 0.0464862   ), Coef('Var'  , 0.050315    ), ], 
		[Coef('Var'  , 0.173803    ), Coef('Var'  , 0.179893    ), Coef('Var'  , 0.183381    ), Coef('Var'  , 0.154605    ), Coef('Var'  , 0.126476    ), Coef('Var'  , 0.128769    ), Coef('Var'  , 0.129988    ), Coef('Var'  , 0.154057    ), ], 
		[Coef('Var'  , 0.161164    ), Coef('Var'  , 0.141219    ), Coef('Var'  , 0.120088    ), Coef('Var'  , 0.110578    ), Coef('Var'  , 0.100704    ), Coef('Var'  , 0.109358    ), Coef('Var'  , 0.117184    ), Coef('Var'  , 0.139999    ), ], 
		[Coef('Var'  , 0.116698    ), Coef('Var'  , 0.104644    ), Coef('Var'  , 0.0936466   ), Coef('Var'  , 0.0931183   ), Coef('Var'  , 0.092145    ), Coef('Var'  , 0.0953716   ), Coef('Var'  , 0.0987905   ), Coef('Var'  , 0.106897    ), ], 
		[Coef('Var'  , 0.113293    ), Coef('Var'  , 0.100883    ), Coef('Var'  , 0.0874158   ), Coef('Var'  , 0.0911918   ), Coef('Var'  , 0.0939358   ), Coef('Var'  , 0.104575    ), Coef('Var'  , 0.114228    ), Coef('Var'  , 0.114266    ), ], 
		[Coef('Var'  , 0.0297609   ), Coef('Var'  , 0.0278622   ), Coef('Var'  , 0.0325594   ), Coef('Var'  , 0.0448775   ), Coef('Var'  , 0.0584434   ), Coef('Var'  , 0.0580263   ), Coef('Var'  , 0.0613598   ), Coef('Var'  , 0.041011    ), ], 
		[Coef('Var'  , 0.139661    ), Coef('Var'  , 0.127115    ), Coef('Var'  , 0.110853    ), Coef('Var'  , 0.121019    ), Coef('Var'  , 0.130207    ), Coef('Var'  , 0.154734    ), Coef('Var'  , 0.17767     ), Coef('Var'  , 0.16083     ), ], ])
	etat13.initMat[Chem([Sub('7')])] = FMat([
		[Coef('Var'  , 0.0746623   ), Coef('Var'  , 0.0913596   ), Coef('Var'  , 0.1079      ), Coef('Var'  , 0.109453    ), Coef('Var'  , 0.111501    ), Coef('Var'  , 0.0936354   ), ], 
		[Coef('Var'  , 0.0522175   ), Coef('Var'  , 0.0743186   ), Coef('Var'  , 0.0968279   ), Coef('Var'  , 0.0868443   ), Coef('Var'  , 0.0772774   ), Coef('Var'  , 0.0648793   ), ], 
		[Coef('Var'  , 0.0711586   ), Coef('Var'  , 0.0832569   ), Coef('Var'  , 0.0965168   ), Coef('Var'  , 0.0809484   ), Coef('Var'  , 0.0659253   ), Coef('Var'  , 0.0680497   ), ], 
		[Coef('Var'  , 0.188598    ), Coef('Var'  , 0.165902    ), Coef('Var'  , 0.144867    ), Coef('Var'  , 0.13053     ), Coef('Var'  , 0.117353    ), Coef('Var'  , 0.152149    ), ], 
		[Coef('Var'  , 0.256234    ), Coef('Var'  , 0.215392    ), Coef('Var'  , 0.175       ), Coef('Var'  , 0.178701    ), Coef('Var'  , 0.183381    ), Coef('Var'  , 0.220058    ), ], 
		[Coef('Var'  , 0.118729    ), Coef('Var'  , 0.107633    ), Coef('Var'  , 0.0958637   ), Coef('Var'  , 0.108233    ), Coef('Var'  , 0.120088    ), Coef('Var'  , 0.119711    ), ], 
		[Coef('Var'  , 0.0833186   ), Coef('Var'  , 0.0832013   ), Coef('Var'  , 0.0824714   ), Coef('Var'  , 0.0884445   ), Coef('Var'  , 0.0936466   ), Coef('Var'  , 0.0883937   ), ], 
		[Coef('Var'  , 0.0643808   ), Coef('Var'  , 0.0686499   ), Coef('Var'  , 0.071755    ), Coef('Var'  , 0.0801775   ), Coef('Var'  , 0.0874158   ), Coef('Var'  , 0.0763749   ), ], 
		[Coef('Var'  , 0.0177572   ), Coef('Var'  , 0.0289502   ), Coef('Var'  , 0.041193    ), Coef('Var'  , 0.0366099   ), Coef('Var'  , 0.0325594   ), Coef('Var'  , 0.0236567   ), ], 
		[Coef('Var'  , 0.0729429   ), Coef('Var'  , 0.0813368   ), Coef('Var'  , 0.0876051   ), Coef('Var'  , 0.100059    ), Coef('Var'  , 0.110853    ), Coef('Var'  , 0.0930925   ), ], ])
	etat13.initMat[Chem([Sub('G')])] = FMat([
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
	etat13.initMat[Chem([Sub('8')])] = FMat([
		[Coef('Var'  , 0.0746117   ), Coef('Var'  , 0.0372191   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.111111    ), Coef('Var'  , 0.0927746   ), ], 
		[Coef('Var'  , 0.206589    ), Coef('Var'  , 0.102876    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.333333    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.325098    ), ], 
		[Coef('Var'  , 0.373303    ), Coef('Var'  , 0.408144    ), Coef('Const', 0.444444    ), Coef('Const', 0.666667    ), Coef('Const', 1           ), Coef('Const', 0.666667    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.408144    ), ], 
		[Coef('Var'  , 0.207835    ), Coef('Var'  , 0.3257      ), Coef('Const', 0.444444    ), Coef('Const', 0.333333    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.103478    ), ], 
		[Coef('Var'  , 0.0766269   ), Coef('Var'  , 0.0937987   ), Coef('Const', 0.111111    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0382432   ), ], 
		[Coef('Var'  , 0.0112295   ), Coef('Var'  , 0.0059107   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0059107   ), ], 
		[Coef('Var'  , 0.0138302   ), Coef('Var'  , 0.0073172   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0073172   ), ], 
		[Coef('Var'  , 0.0101485   ), Coef('Var'  , 0.00534059  ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.00534059  ), ], 
		[Coef('Var'  , 0.0135286   ), Coef('Var'  , 0.00720951  ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.00720951  ), ], 
		[Coef('Var'  , 0.0122972   ), Coef('Var'  , 0.00648418  ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.00648418  ), ], ])
	etat13.initMat[Chem([Sub('9')])] = FMat([
		[Coef('Var'  , 0.124263    ), Coef('Var'  , 0.117517    ), Coef('Const', 0.111111    ), Coef('Const', 0.222222    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.322171    ), Coef('Var'  , 0.200455    ), Coef('Var'  , 0.16191     ), ], 
		[Coef('Var'  , 0.269436    ), Coef('Var'  , 0.35629     ), Coef('Const', 0.444444    ), Coef('Const', 0.555556    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.349688    ), Coef('Var'  , 0.256327    ), Coef('Var'  , 0.261534    ), ], 
		[Coef('Var'  , 0.30988     ), Coef('Var'  , 0.376098    ), Coef('Const', 0.444444    ), Coef('Const', 0.222222    ), Coef('Const', 0.111111    ), Coef('Var'  , 0.153503    ), Coef('Var'  , 0.19795     ), Coef('Var'  , 0.251823    ), ], 
		[Coef('Var'  , 0.12412     ), Coef('Var'  , 0.0614091   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0564149   ), Coef('Var'  , 0.114149    ), Coef('Var'  , 0.117824    ), ], 
		[Coef('Var'  , 0.0689508   ), Coef('Var'  , 0.0343384   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0407352   ), Coef('Var'  , 0.0819886   ), Coef('Var'  , 0.0750736   ), ], 
		[Coef('Var'  , 0.0193026   ), Coef('Var'  , 0.0100906   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0150441   ), Coef('Var'  , 0.0292008   ), Coef('Var'  , 0.0251346   ), ], 
		[Coef('Var'  , 0.023343    ), Coef('Var'  , 0.0122918   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0173419   ), Coef('Var'  , 0.0332989   ), Coef('Var'  , 0.0296336   ), ], 
		[Coef('Var'  , 0.0174419   ), Coef('Var'  , 0.00912894  ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0134939   ), Coef('Var'  , 0.0260876   ), Coef('Var'  , 0.0226227   ), ], 
		[Coef('Var'  , 0.0222485   ), Coef('Var'  , 0.0118258   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0154558   ), Coef('Var'  , 0.0292576   ), Coef('Var'  , 0.0272815   ), ], 
		[Coef('Var'  , 0.0210139   ), Coef('Var'  , 0.0110094   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0161527   ), Coef('Var'  , 0.0312859   ), Coef('Var'  , 0.027162    ), ], ])
	etat13.initMat[Chem([Sub('10')])] = FMat([
		[Coef('Var'  , 0.0650907   ), Coef('Var'  , 0.0694374   ), Coef('Var'  , 0.0746153   ), Coef('Var'  , 0.0370454   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0323921   ), ], 
		[Coef('Var'  , 0.121436    ), Coef('Var'  , 0.11359     ), Coef('Var'  , 0.108326    ), Coef('Var'  , 0.0534938   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0600961   ), ], 
		[Coef('Var'  , 0.309845    ), Coef('Var'  , 0.251774    ), Coef('Var'  , 0.197915    ), Coef('Var'  , 0.153478    ), Coef('Const', 0.111111    ), Coef('Const', 0.222222    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.376074    ), ], 
		[Coef('Var'  , 0.27216     ), Coef('Var'  , 0.265824    ), Coef('Var'  , 0.262189    ), Coef('Var'  , 0.352637    ), Coef('Const', 0.444444    ), Coef('Const', 0.555556    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.357631    ), ], 
		[Coef('Var'  , 0.128147    ), Coef('Var'  , 0.167579    ), Coef('Var'  , 0.207851    ), Coef('Var'  , 0.325877    ), Coef('Const', 0.444444    ), Coef('Const', 0.222222    ), Coef('Const', 0.111111    ), Coef('Var'  , 0.11948     ), ], 
		[Coef('Var'  , 0.0193235   ), Coef('Var'  , 0.0251633   ), Coef('Var'  , 0.0292217   ), Coef('Var'  , 0.0150585   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.010105    ), ], 
		[Coef('Var'  , 0.0233261   ), Coef('Var'  , 0.0296102   ), Coef('Var'  , 0.033282    ), Coef('Var'  , 0.0173303   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0122801   ), ], 
		[Coef('Var'  , 0.0174348   ), Coef('Var'  , 0.0226128   ), Coef('Var'  , 0.0260805   ), Coef('Var'  , 0.0134889   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.00912398  ), ], 
		[Coef('Var'  , 0.0222143   ), Coef('Var'  , 0.0272343   ), Coef('Var'  , 0.0292234   ), Coef('Var'  , 0.0154322   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0118022   ), ], 
		[Coef('Var'  , 0.0210233   ), Coef('Var'  , 0.027175    ), Coef('Var'  , 0.0312953   ), Coef('Var'  , 0.0161591   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0110159   ), ], ])
	etat13.initMat[Chem([Sub('11')])] = FMat([
		[Coef('Var'  , 0.114742    ), Coef('Var'  , 0.157083    ), Coef('Var'  , 0.200455    ), Coef('Var'  , 0.161719    ), Coef('Var'  , 0.124665    ), Coef('Var'  , 0.098816    ), Coef('Var'  , 0.0746153   ), Coef('Var'  , 0.0941803   ), ], 
		[Coef('Var'  , 0.184283    ), Coef('Var'  , 0.218755    ), Coef('Var'  , 0.256327    ), Coef('Var'  , 0.197907    ), Coef('Var'  , 0.142218    ), Coef('Var'  , 0.123935    ), Coef('Var'  , 0.108326    ), Coef('Var'  , 0.144782    ), ], 
		[Coef('Var'  , 0.246422    ), Coef('Var'  , 0.219753    ), Coef('Var'  , 0.19795     ), Coef('Var'  , 0.170497    ), Coef('Var'  , 0.14642     ), Coef('Var'  , 0.170473    ), Coef('Var'  , 0.197915    ), Coef('Var'  , 0.219728    ), ], 
		[Coef('Var'  , 0.188444    ), Coef('Var'  , 0.149755    ), Coef('Var'  , 0.114149    ), Coef('Var'  , 0.135032    ), Coef('Var'  , 0.158234    ), Coef('Var'  , 0.209032    ), Coef('Var'  , 0.262189    ), Coef('Var'  , 0.223755    ), ], 
		[Coef('Var'  , 0.120471    ), Coef('Var'  , 0.100755    ), Coef('Var'  , 0.0819886   ), Coef('Var'  , 0.112389    ), Coef('Var'  , 0.144443    ), Coef('Var'  , 0.175309    ), Coef('Var'  , 0.207851    ), Coef('Var'  , 0.163674    ), ], 
		[Coef('Var'  , 0.0273966   ), Coef('Var'  , 0.0293288   ), Coef('Var'  , 0.0292008   ), Coef('Var'  , 0.0456584   ), Coef('Var'  , 0.06053     ), Coef('Var'  , 0.0456728   ), Coef('Var'  , 0.0292217   ), Coef('Var'  , 0.0293432   ), ], 
		[Coef('Var'  , 0.0328389   ), Coef('Var'  , 0.0345964   ), Coef('Var'  , 0.0332989   ), Coef('Var'  , 0.0490493   ), Coef('Var'  , 0.0619299   ), Coef('Var'  , 0.0490376   ), Coef('Var'  , 0.033282    ), Coef('Var'  , 0.0345848   ), ], 
		[Coef('Var'  , 0.0247282   ), Coef('Var'  , 0.0264061   ), Coef('Var'  , 0.0260876   ), Coef('Var'  , 0.0401507   ), Coef('Var'  , 0.0523435   ), Coef('Var'  , 0.0401458   ), Coef('Var'  , 0.0260805   ), Coef('Var'  , 0.0264012   ), ], 
		[Coef('Var'  , 0.0309341   ), Coef('Var'  , 0.0318743   ), Coef('Var'  , 0.0292576   ), Coef('Var'  , 0.0393423   ), Coef('Var'  , 0.0458288   ), Coef('Var'  , 0.0393187   ), Coef('Var'  , 0.0292234   ), Coef('Var'  , 0.0318507   ), ], 
		[Coef('Var'  , 0.02974     ), Coef('Var'  , 0.0316938   ), Coef('Var'  , 0.0312859   ), Coef('Var'  , 0.0482542   ), Coef('Var'  , 0.0633883   ), Coef('Var'  , 0.0482607   ), Coef('Var'  , 0.0312953   ), Coef('Var'  , 0.0317002   ), ], ])
	etat13.initMat[Chem([Sub('12')])] = FMat([
		[Coef('Var'  , 0.138261    ), Coef('Var'  , 0.137866    ), Coef('Var'  , 0.141031    ), Coef('Var'  , 0.149715    ), Coef('Var'  , 0.163035    ), Coef('Var'  , 0.148904    ), ], 
		[Coef('Var'  , 0.100893    ), Coef('Var'  , 0.110885    ), Coef('Var'  , 0.122436    ), Coef('Var'  , 0.12902     ), Coef('Var'  , 0.137795    ), Coef('Var'  , 0.11862     ), ], 
		[Coef('Var'  , 0.0718563   ), Coef('Var'  , 0.0833445   ), Coef('Var'  , 0.0932744   ), Coef('Var'  , 0.0919043   ), Coef('Var'  , 0.0886658   ), Coef('Var'  , 0.081117    ), ], 
		[Coef('Var'  , 0.087078    ), Coef('Var'  , 0.0930169   ), Coef('Var'  , 0.0979075   ), Coef('Var'  , 0.0917331   ), Coef('Var'  , 0.0840758   ), Coef('Var'  , 0.0861875   ), ], 
		[Coef('Var'  , 0.126476    ), Coef('Var'  , 0.114846    ), Coef('Var'  , 0.10524     ), Coef('Var'  , 0.0976625   ), Coef('Var'  , 0.0926788   ), Coef('Var'  , 0.108659    ), ], 
		[Coef('Var'  , 0.100704    ), Coef('Var'  , 0.0926102   ), Coef('Var'  , 0.0841686   ), Coef('Var'  , 0.0816231   ), Coef('Var'  , 0.0787002   ), Coef('Var'  , 0.089858    ), ], 
		[Coef('Var'  , 0.092145    ), Coef('Var'  , 0.0908822   ), Coef('Var'  , 0.0880159   ), Coef('Var'  , 0.0866408   ), Coef('Var'  , 0.08312     ), Coef('Var'  , 0.0883581   ), ], 
		[Coef('Var'  , 0.0939358   ), Coef('Var'  , 0.0899935   ), Coef('Var'  , 0.0847215   ), Coef('Var'  , 0.0843645   ), Coef('Var'  , 0.0825377   ), Coef('Var'  , 0.0888522   ), ], 
		[Coef('Var'  , 0.0584434   ), Coef('Var'  , 0.0654346   ), Coef('Var'  , 0.0708767   ), Coef('Var'  , 0.0728266   ), Coef('Var'  , 0.0719329   ), Coef('Var'  , 0.0658306   ), ], 
		[Coef('Var'  , 0.130207    ), Coef('Var'  , 0.121121    ), Coef('Var'  , 0.112328    ), Coef('Var'  , 0.114511    ), Coef('Var'  , 0.117459    ), Coef('Var'  , 0.123613    ), ], ])
	etat13.initMat[Chem([Sub('13')])] = FMat([
		[Coef('Var'  , 0.237159    ), Coef('Var'  , 0.198225    ), Coef('Var'  , 0.163035    ), Coef('Var'  , 0.159565    ), Coef('Var'  , 0.160737    ), Coef('Var'  , 0.197038    ), ], 
		[Coef('Var'  , 0.197789    ), Coef('Var'  , 0.166926    ), Coef('Var'  , 0.137795    ), Coef('Var'  , 0.138579    ), Coef('Var'  , 0.141644    ), Coef('Var'  , 0.168751    ), ], 
		[Coef('Var'  , 0.0833353   ), Coef('Var'  , 0.0868357   ), Coef('Var'  , 0.0886658   ), Coef('Var'  , 0.0929597   ), Coef('Var'  , 0.0954702   ), Coef('Var'  , 0.0901186   ), ], 
		[Coef('Var'  , 0.0518994   ), Coef('Var'  , 0.0686879   ), Coef('Var'  , 0.0840758   ), Coef('Var'  , 0.0882161   ), Coef('Var'  , 0.0908965   ), Coef('Var'  , 0.0720003   ), ], 
		[Coef('Var'  , 0.060193    ), Coef('Var'  , 0.0755271   ), Coef('Var'  , 0.0926788   ), Coef('Var'  , 0.0911283   ), Coef('Var'  , 0.0920819   ), Coef('Var'  , 0.0751794   ), ], 
		[Coef('Var'  , 0.0530088   ), Coef('Var'  , 0.0660357   ), Coef('Var'  , 0.0787002   ), Coef('Var'  , 0.0769233   ), Coef('Var'  , 0.0747075   ), Coef('Var'  , 0.064088    ), ], 
		[Coef('Var'  , 0.0595528   ), Coef('Var'  , 0.0721459   ), Coef('Var'  , 0.08312     ), Coef('Var'  , 0.0834392   ), Coef('Var'  , 0.0815787   ), Coef('Var'  , 0.0714684   ), ], 
		[Coef('Var'  , 0.0646766   ), Coef('Var'  , 0.0741712   ), Coef('Var'  , 0.0825377   ), Coef('Var'  , 0.0814247   ), Coef('Var'  , 0.0788418   ), Coef('Var'  , 0.0723727   ), ], 
		[Coef('Var'  , 0.0712477   ), Coef('Var'  , 0.0725337   ), Coef('Var'  , 0.0719329   ), Coef('Var'  , 0.0742018   ), Coef('Var'  , 0.0736143   ), Coef('Var'  , 0.0735128   ), ], 
		[Coef('Var'  , 0.121138    ), Coef('Var'  , 0.118912    ), Coef('Var'  , 0.117459    ), Coef('Var'  , 0.113563    ), Coef('Var'  , 0.110428    ), Coef('Var'  , 0.115471    ), ], ])
	etat13.initMat[Chem([Sub('14')])] = FMat([
		[Coef('Var'  , 0.128167    ), Coef('Var'  , 0.142304    ), Coef('Var'  , 0.160737    ), Coef('Var'  , 0.148528    ), Coef('Var'  , 0.141031    ), Coef('Var'  , 0.132453    ), ], 
		[Coef('Var'  , 0.122306    ), Coef('Var'  , 0.130739    ), Coef('Var'  , 0.141644    ), Coef('Var'  , 0.130844    ), Coef('Var'  , 0.122436    ), Coef('Var'  , 0.12118     ), ], 
		[Coef('Var'  , 0.107998    ), Coef('Var'  , 0.102149    ), Coef('Var'  , 0.0954702   ), Coef('Var'  , 0.0951872   ), Coef('Var'  , 0.0932744   ), Coef('Var'  , 0.101093    ), ], 
		[Coef('Var'  , 0.122801    ), Coef('Var'  , 0.107142    ), Coef('Var'  , 0.0908965   ), Coef('Var'  , 0.0950454   ), Coef('Var'  , 0.0979075   ), Coef('Var'  , 0.110659    ), ], 
		[Coef('Var'  , 0.125144    ), Coef('Var'  , 0.107228    ), Coef('Var'  , 0.0920819   ), Coef('Var'  , 0.0973148   ), Coef('Var'  , 0.10524     ), Coef('Var'  , 0.113762    ), ], 
		[Coef('Var'  , 0.0799214   ), Coef('Var'  , 0.0776334   ), Coef('Var'  , 0.0747075   ), Coef('Var'  , 0.0796754   ), Coef('Var'  , 0.0841686   ), Coef('Var'  , 0.0823333   ), ], 
		[Coef('Var'  , 0.0822633   ), Coef('Var'  , 0.0831822   ), Coef('Var'  , 0.0815787   ), Coef('Var'  , 0.0859634   ), Coef('Var'  , 0.0880159   ), Coef('Var'  , 0.0863838   ), ], 
		[Coef('Var'  , 0.074474    ), Coef('Var'  , 0.0774942   ), Coef('Var'  , 0.0788418   ), Coef('Var'  , 0.082566    ), Coef('Var'  , 0.0847215   ), Coef('Var'  , 0.080434    ), ], 
		[Coef('Var'  , 0.062885    ), Coef('Var'  , 0.0699572   ), Coef('Var'  , 0.0736143   ), Coef('Var'  , 0.0738058   ), Coef('Var'  , 0.0708767   ), Coef('Var'  , 0.0685821   ), ], 
		[Coef('Var'  , 0.0940396   ), Coef('Var'  , 0.102172    ), Coef('Var'  , 0.110428    ), Coef('Var'  , 0.11107     ), Coef('Var'  , 0.112328    ), Coef('Var'  , 0.10312     ), ], ])
	etat13.initMat[Chem([Sub('15')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0296843   ), Coef('Var'  , 0.056293    ), Coef('Var'  , 0.0296843   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0106025   ), Coef('Var'  , 0.0209237   ), Coef('Var'  , 0.0106025   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.000104379 ), Coef('Var'  , 0.00266643  ), Coef('Var'  , 0.000104379 ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.00675068  ), Coef('Var'  , 0.015954    ), Coef('Var'  , 0.00675068  ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.20571     ), Coef('Var'  , 0.15826     ), Coef('Var'  , 0.0807097   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.364064    ), Coef('Var'  , 0.226925    ), Coef('Var'  , 0.114064    ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.221395    ), Coef('Var'  , 0.19383     ), Coef('Var'  , 0.221395    ), ], 
		[Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0940791   ), Coef('Var'  , 0.187579    ), Coef('Var'  , 0.344079    ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0324306   ), Coef('Var'  , 0.0703247   ), Coef('Var'  , 0.157431    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0351793   ), Coef('Var'  , 0.0672434   ), Coef('Var'  , 0.0351793   ), ], ])
	etat13.initMat[Chem([Sub('16')])] = FMat([
		[Coef('Var'  , 0.12647     ), Coef('Var'  , 0.0945354   ), Coef('Var'  , 0.056293    ), Coef('Var'  , 0.0662238   ), Coef('Var'  , 0.0701549   ), Coef('Var'  , 0.0985971   ), Coef('Var'  , 0.121445    ), Coef('Var'  , 0.126909    ), ], 
		[Coef('Var'  , 0.0467101   ), Coef('Var'  , 0.0342136   ), Coef('Var'  , 0.0209237   ), Coef('Var'  , 0.0277503   ), Coef('Var'  , 0.0339143   ), Coef('Var'  , 0.0467628   ), Coef('Var'  , 0.0586554   ), Coef('Var'  , 0.0532262   ), ], 
		[Coef('Var'  , 0.0127812   ), Coef('Var'  , 0.00535793  ), Coef('Var'  , 0.00266643  ), Coef('Var'  , 0.00905346  ), Coef('Var'  , 0.020153    ), Coef('Var'  , 0.0222745   ), Coef('Var'  , 0.0283995   ), Coef('Var'  , 0.018579    ), ], 
		[Coef('Var'  , 0.0267258   ), Coef('Var'  , 0.0189285   ), Coef('Var'  , 0.015954    ), Coef('Var'  , 0.0353756   ), Coef('Var'  , 0.0596304   ), Coef('Var'  , 0.0561856   ), Coef('Var'  , 0.0571186   ), Coef('Var'  , 0.0397384   ), ], 
		[Coef('Var'  , 0.137593    ), Coef('Var'  , 0.151226    ), Coef('Var'  , 0.15826     ), Coef('Var'  , 0.190236    ), Coef('Var'  , 0.216275    ), Coef('Var'  , 0.197736    ), Coef('Var'  , 0.173803    ), Coef('Var'  , 0.158726    ), ], 
		[Coef('Var'  , 0.14233     ), Coef('Var'  , 0.185865    ), Coef('Var'  , 0.226925    ), Coef('Var'  , 0.241752    ), Coef('Var'  , 0.254313    ), Coef('Var'  , 0.208751    ), Coef('Var'  , 0.161164    ), Coef('Var'  , 0.152864    ), ], 
		[Coef('Var'  , 0.126607    ), Coef('Var'  , 0.159082    ), Coef('Var'  , 0.19383     ), Coef('Var'  , 0.175182    ), Coef('Var'  , 0.158566    ), Coef('Var'  , 0.136613    ), Coef('Var'  , 0.116698    ), Coef('Var'  , 0.120512    ), ], 
		[Coef('Var'  , 0.152033    ), Coef('Var'  , 0.170393    ), Coef('Var'  , 0.187579    ), Coef('Var'  , 0.140809    ), Coef('Var'  , 0.0928552   ), Coef('Var'  , 0.103662    ), Coef('Var'  , 0.113293    ), Coef('Var'  , 0.133246    ), ], 
		[Coef('Var'  , 0.0661673   ), Coef('Var'  , 0.062349    ), Coef('Var'  , 0.0703247   ), Coef('Var'  , 0.038156    ), Coef('Var'  , 0.0166488   ), Coef('Var'  , 0.0179293   ), Coef('Var'  , 0.0297609   ), Coef('Var'  , 0.0421224   ), ], 
		[Coef('Var'  , 0.162582    ), Coef('Var'  , 0.11805     ), Coef('Var'  , 0.0672434   ), Coef('Var'  , 0.075461    ), Coef('Var'  , 0.0774893   ), Coef('Var'  , 0.11149     ), Coef('Var'  , 0.139661    ), Coef('Var'  , 0.154078    ), ], ])
	
	
	
	etat14.bords   = {Bord('0'): etat21, Bord('1'): etat19, Bord('2'): etat21, }
	etat14.permuts = {}
	etat14.interns = {Intern('_'): etat14, }
	etat14.subs    = {Sub('0'): etat1, Sub('1'): etat2, Sub('2'): etat3, Sub('3'): etat4, Sub('4'): etat5, Sub('5'): etat6, Sub('6'): etat7, Sub('7'): etat8, Sub('G', True): Etat.etatPoint, Sub('8'): etat9, Sub('9'): etat10, Sub('10'): etat11, Sub('11'): etat12, Sub('12'): etat13, Sub('13'): etat15, Sub('14'): etat16, Sub('15'): etat17, Sub('16'): etat18, }
	
	etat14.buildIntern()
	
	
	etat14.eqs = [
		(Chem([Bord('2'), Sub('1'), Permut('0'), ])	,	Chem([Sub('1'), Bord('3'), ])),
		(Chem([Bord('2'), Sub('2'), Permut('0'), ])	,	Chem([Sub('3'), Bord('3'), ])),
		(Chem([Bord('0'), Sub('2'), Permut('0'), ])	,	Chem([Sub('5'), Bord('1'), ])),
		(Chem([Bord('0'), Sub('0'), Permut('0'), ])	,	Chem([Sub('6'), Bord('1'), ])),
		(Chem([Bord('2'), Sub('3'), Permut('0'), ])	,	Chem([Sub('6'), Bord('2'), ])),
		(Chem([Bord('0'), Sub('1'), Permut('0'), ])	,	Chem([Sub('7'), Bord('1'), ])),
		(Chem([Bord('2'), Sub('0'), Permut('0'), ])	,	Chem([Sub('13'), Bord('0'), ])),
		(Chem([Bord('1'), Sub('1'), Permut('0'), ])	,	Chem([Sub('13'), Bord('1'), ])),
		(Chem([Bord('1'), Sub('0'), Permut('0'), ])	,	Chem([Sub('14'), Bord('1'), ])),
		(Chem([Bord('0'), Sub('3'), Permut('0'), ])	,	Chem([Sub('14'), Bord('2'), ])),
		(Chem([Sub('0'), Bord('0'), Bord('1'), ])	,	Chem([Sub('12'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('1'), Bord('1'), ])	,	Chem([Sub('15'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('2'), Bord('1'), ])	,	Chem([Sub('3'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('3'), Bord('1'), ])	,	Chem([Sub('1'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('0'), Bord('1'), ])	,	Chem([Sub('12'), Bord('4'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('2'), Bord('1'), ])	,	Chem([Sub('3'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('3'), Bord('1'), ])	,	Chem([Sub('13'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('4'), Bord('1'), ])	,	Chem([Sub('9'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('0'), Bord('1'), ])	,	Chem([Sub('12'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('1'), Bord('1'), ])	,	Chem([Sub('10'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('2'), Bord('1'), ])	,	Chem([Sub('7'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('3'), Bord('1'), ])	,	Chem([Sub('16'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('4'), Bord('1'), ])	,	Chem([Sub('15'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('3'), Bord('1'), Bord('1'), ])	,	Chem([Sub('16'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('3'), Bord('2'), Bord('1'), ])	,	Chem([Sub('6'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('4'), Bord('0'), Bord('1'), ])	,	Chem([Sub('8'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('4'), Bord('1'), Bord('1'), ])	,	Chem([Sub('9'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('4'), Bord('2'), Bord('1'), ])	,	Chem([Sub('11'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('4'), Bord('3'), Bord('1'), ])	,	Chem([Sub('10'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('5'), Bord('0'), Bord('1'), ])	,	Chem([Sub('14'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('5'), Bord('1'), Bord('1'), ])	,	Chem([Sub('7'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('5'), Bord('2'), Bord('1'), ])	,	Chem([Sub('11'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('6'), Bord('0'), Bord('1'), ])	,	Chem([Sub('7'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('6'), Bord('3'), Bord('1'), ])	,	Chem([Sub('16'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('8'), Bord('0'), Bord('1'), ])	,	Chem([Sub('10'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('8'), Bord('1'), Bord('1'), ])	,	Chem([Sub('12'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('8'), Bord('2'), Bord('1'), ])	,	Chem([Sub('9'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('9'), Bord('2'), Bord('1'), ])	,	Chem([Sub('11'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('10'), Bord('0'), Bord('1'), ])	,	Chem([Sub('11'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('12'), Bord('2'), Bord('1'), ])	,	Chem([Sub('15'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('13'), Bord('1'), Bord('1'), ])	,	Chem([Sub('14'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('15'), Bord('2'), Bord('1'), ])	,	Chem([Sub('16'), Bord('0'), Bord('1'), ])),
		(Chem([Bord('0'), Bord('1'), ])	,	Chem([Bord('1'), Bord('0'), ])),
		(Chem([Bord('1'), Bord('1'), ])	,	Chem([Bord('2'), Bord('0'), ])),
		(Chem([Bord('2'), Bord('1'), ])	,	Chem([Bord('0'), Bord('0'), ])),
		]
	
	
	etat14.prim.elems = [Figure(2, [Chem([Bord('0'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('0'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('0'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('0'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('1'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('1'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('1'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('1'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('2'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('2'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('2'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('2'), Sub('1'), Sub('1'), Bord('0'), ]), ])]
	etat14.grid.elems = [
		Figure(1, [Chem([Bord('1'), Bord('0'), ]), Chem([Bord('1'), Intern(''), ]), Chem([Bord('1'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('2'), Bord('0'), ]), Chem([Bord('2'), Intern(''), ]), Chem([Bord('2'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('0'), Bord('0'), ]), Chem([Bord('0'), Intern(''), ]), Chem([Bord('0'), Bord('1'), ]), ]), ]
	
	
	etat14.space = [Chem([Bord('2'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('2'), Intern('0'), Intern('0'), ]), ]
	
	etat14.initMat[Chem([Sub('0')])] = FMat([
		[Coef('Var'  , 0.218534    ), Coef('Var'  , 0.208246    ), Coef('Var'  , 0.202811    ), Coef('Var'  , 0.21534     ), Coef('Var'  , 0.234037    ), Coef('Var'  , 0.247524    ), Coef('Var'  , 0.266465    ), Coef('Var'  , 0.24043     ), ], 
		[Coef('Var'  , 0.0863357   ), Coef('Var'  , 0.107725    ), Coef('Var'  , 0.127367    ), Coef('Var'  , 0.13011     ), Coef('Var'  , 0.131194    ), Coef('Var'  , 0.107096    ), Coef('Var'  , 0.0816175   ), Coef('Var'  , 0.0847111   ), ], 
		[Coef('Var'  , 0.086072    ), Coef('Var'  , 0.107372    ), Coef('Var'  , 0.124967    ), Coef('Var'  , 0.124322    ), Coef('Var'  , 0.119528    ), Coef('Var'  , 0.0975973   ), Coef('Var'  , 0.0721295   ), Coef('Var'  , 0.0806466   ), ], 
		[Coef('Var'  , 0.0716946   ), Coef('Var'  , 0.0897427   ), Coef('Var'  , 0.104061    ), Coef('Var'  , 0.102792    ), Coef('Var'  , 0.0971969   ), Coef('Var'  , 0.0793559   ), Coef('Var'  , 0.0580221   ), Coef('Var'  , 0.0663067   ), ], 
		[Coef('Var'  , 0.209578    ), Coef('Var'  , 0.199542    ), Coef('Var'  , 0.189687    ), Coef('Var'  , 0.180741    ), Coef('Var'  , 0.171261    ), Coef('Var'  , 0.17988     ), Coef('Var'  , 0.187677    ), Coef('Var'  , 0.198681    ), ], 
		[Coef('Var'  , 0.327786    ), Coef('Var'  , 0.287372    ), Coef('Var'  , 0.251107    ), Coef('Var'  , 0.246694    ), Coef('Var'  , 0.246783    ), Coef('Var'  , 0.288546    ), Coef('Var'  , 0.334089    ), Coef('Var'  , 0.329224    ), ], ])
	etat14.initMat[Chem([Sub('1')])] = FMat([
		[Coef('Var'  , 0.134686    ), Coef('Var'  , 0.154622    ), Coef('Var'  , 0.177341    ), Coef('Var'  , 0.195973    ), Coef('Var'  , 0.218534    ), Coef('Var'  , 0.233281    ), Coef('Const', 0.25        ), Coef('Const', 0.125       ), Coef('Const', 0.0625      ), Coef('Var'  , 0.0981801   ), ], 
		[Coef('Var'  , 0.125676    ), Coef('Var'  , 0.12711     ), Coef('Var'  , 0.127964    ), Coef('Var'  , 0.107875    ), Coef('Var'  , 0.0863357   ), Coef('Var'  , 0.0435777   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0628126   ), ], 
		[Coef('Var'  , 0.127715    ), Coef('Var'  , 0.129723    ), Coef('Var'  , 0.129612    ), Coef('Var'  , 0.109436    ), Coef('Var'  , 0.086072    ), Coef('Var'  , 0.0438389   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0641262   ), ], 
		[Coef('Var'  , 0.0941943   ), Coef('Var'  , 0.102442    ), Coef('Var'  , 0.106972    ), Coef('Var'  , 0.0911271   ), Coef('Var'  , 0.0716946   ), Coef('Var'  , 0.0366178   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0479332   ), ], 
		[Coef('Var'  , 0.280765    ), Coef('Var'  , 0.246043    ), Coef('Var'  , 0.21239     ), Coef('Var'  , 0.210651    ), Coef('Var'  , 0.209578    ), Coef('Var'  , 0.229701    ), Coef('Const', 0.25        ), Coef('Const', 0.375       ), Coef('Const', 0.5625      ), Coef('Var'  , 0.421343    ), ], 
		[Coef('Var'  , 0.236964    ), Coef('Var'  , 0.24006     ), Coef('Var'  , 0.245721    ), Coef('Var'  , 0.284938    ), Coef('Var'  , 0.327786    ), Coef('Var'  , 0.412984    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0.375       ), Coef('Var'  , 0.305605    ), ], ])
	etat14.initMat[Chem([Sub('2')])] = FMat([
		[Coef('Var'  , 0.250093    ), Coef('Var'  , 0.226435    ), Coef('Var'  , 0.208537    ), Coef('Var'  , 0.21359     ), Coef('Var'  , 0.222297    ), Coef('Var'  , 0.278399    ), Coef('Var'  , 0.336833    ), Coef('Var'  , 0.329139    ), Coef('Var'  , 0.325327    ), Coef('Var'  , 0.284678    ), ], 
		[Coef('Var'  , 0.173571    ), Coef('Var'  , 0.177048    ), Coef('Var'  , 0.180914    ), Coef('Var'  , 0.206143    ), Coef('Var'  , 0.232694    ), Coef('Var'  , 0.279187    ), Coef('Var'  , 0.327164    ), Coef('Var'  , 0.266113    ), Coef('Var'  , 0.205768    ), Coef('Var'  , 0.189516    ), ], 
		[Coef('Var'  , 0.139377    ), Coef('Var'  , 0.15073     ), Coef('Var'  , 0.159378    ), Coef('Var'  , 0.170761    ), Coef('Var'  , 0.180683    ), Coef('Var'  , 0.168127    ), Coef('Var'  , 0.154928    ), Coef('Var'  , 0.13934     ), Coef('Var'  , 0.122251    ), Coef('Var'  , 0.132154    ), ], 
		[Coef('Var'  , 0.106569    ), Coef('Var'  , 0.117891    ), Coef('Var'  , 0.124679    ), Coef('Var'  , 0.122379    ), Coef('Var'  , 0.115682    ), Coef('Var'  , 0.0845359   ), Coef('Var'  , 0.0503049   ), Coef('Var'  , 0.0633998   ), Coef('Var'  , 0.0738437   ), Coef('Var'  , 0.0921306   ), ], 
		[Coef('Var'  , 0.141998    ), Coef('Var'  , 0.147126    ), Coef('Var'  , 0.150881    ), Coef('Var'  , 0.134711    ), Coef('Var'  , 0.11806     ), Coef('Var'  , 0.0877057   ), Coef('Var'  , 0.0568197   ), Coef('Var'  , 0.0815662   ), Coef('Var'  , 0.104814    ), Coef('Var'  , 0.124441    ), ], 
		[Coef('Var'  , 0.188393    ), Coef('Var'  , 0.18077     ), Coef('Var'  , 0.175612    ), Coef('Var'  , 0.152416    ), Coef('Var'  , 0.130584    ), Coef('Var'  , 0.102045    ), Coef('Var'  , 0.0739505   ), Coef('Var'  , 0.120442    ), Coef('Var'  , 0.167996    ), Coef('Var'  , 0.17708     ), ], ])
	etat14.initMat[Chem([Sub('3')])] = FMat([
		[Coef('Const', 0.25        ), Coef('Var'  , 0.257149    ), Coef('Var'  , 0.266465    ), Coef('Var'  , 0.324875    ), Coef('Var'  , 0.387601    ), Coef('Var'  , 0.473976    ), Coef('Const', 0.5625      ), Coef('Const', 0.375       ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0411334   ), Coef('Var'  , 0.0816175   ), Coef('Var'  , 0.0923666   ), Coef('Var'  , 0.102206    ), Coef('Var'  , 0.0512332   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0368076   ), Coef('Var'  , 0.0721295   ), Coef('Var'  , 0.0706884   ), Coef('Var'  , 0.066598    ), Coef('Var'  , 0.0338808   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0296889   ), Coef('Var'  , 0.0580221   ), Coef('Var'  , 0.0541255   ), Coef('Var'  , 0.0477122   ), Coef('Var'  , 0.0244366   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.25        ), Coef('Var'  , 0.218981    ), Coef('Var'  , 0.187677    ), Coef('Var'  , 0.152615    ), Coef('Var'  , 0.116601    ), Coef('Var'  , 0.0898844   ), Coef('Const', 0.0625      ), Coef('Const', 0.125       ), ], 
		[Coef('Const', 0.5         ), Coef('Var'  , 0.416241    ), Coef('Var'  , 0.334089    ), Coef('Var'  , 0.305329    ), Coef('Var'  , 0.279282    ), Coef('Var'  , 0.326589    ), Coef('Const', 0.375       ), Coef('Const', 0.5         ), ], ])
	etat14.initMat[Chem([Sub('4')])] = FMat([
		[Coef('Var'  , 0.170207    ), Coef('Var'  , 0.166846    ), Coef('Var'  , 0.1644      ), Coef('Var'  , 0.1606      ), Coef('Var'  , 0.157751    ), Coef('Var'  , 0.160286    ), Coef('Var'  , 0.163558    ), Coef('Var'  , 0.166531    ), ], 
		[Coef('Var'  , 0.202843    ), Coef('Var'  , 0.192898    ), Coef('Var'  , 0.185148    ), Coef('Var'  , 0.186388    ), Coef('Var'  , 0.189435    ), Coef('Var'  , 0.197221    ), Coef('Var'  , 0.20713     ), Coef('Var'  , 0.203731    ), ], 
		[Coef('Var'  , 0.197739    ), Coef('Var'  , 0.191034    ), Coef('Var'  , 0.184541    ), Coef('Var'  , 0.187555    ), Coef('Var'  , 0.190681    ), Coef('Var'  , 0.197047    ), Coef('Var'  , 0.20388     ), Coef('Var'  , 0.200526    ), ], 
		[Coef('Var'  , 0.144173    ), Coef('Var'  , 0.148259    ), Coef('Var'  , 0.14762     ), Coef('Var'  , 0.146477    ), Coef('Var'  , 0.140675    ), Coef('Var'  , 0.141333    ), Coef('Var'  , 0.137228    ), Coef('Var'  , 0.143116    ), ], 
		[Coef('Var'  , 0.140091    ), Coef('Var'  , 0.148679    ), Coef('Var'  , 0.158381    ), Coef('Var'  , 0.159626    ), Coef('Var'  , 0.162205    ), Coef('Var'  , 0.152454    ), Coef('Var'  , 0.143915    ), Coef('Var'  , 0.141507    ), ], 
		[Coef('Var'  , 0.144946    ), Coef('Var'  , 0.152285    ), Coef('Var'  , 0.159909    ), Coef('Var'  , 0.159353    ), Coef('Var'  , 0.159253    ), Coef('Var'  , 0.151658    ), Coef('Var'  , 0.14429     ), Coef('Var'  , 0.14459     ), ], ])
	etat14.initMat[Chem([Sub('5')])] = FMat([
		[Coef('Var'  , 0.160207    ), Coef('Var'  , 0.111272    ), Coef('Const', 0.0625      ), Coef('Const', 0.125       ), Coef('Const', 0.25        ), Coef('Var'  , 0.205022    ), ], 
		[Coef('Var'  , 0.329496    ), Coef('Var'  , 0.351919    ), Coef('Const', 0.375       ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.414419    ), ], 
		[Coef('Var'  , 0.310265    ), Coef('Var'  , 0.436284    ), Coef('Const', 0.5625      ), Coef('Const', 0.375       ), Coef('Const', 0.25        ), Coef('Var'  , 0.280034    ), ], 
		[Coef('Var'  , 0.0623985   ), Coef('Var'  , 0.031801    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.031801    ), ], 
		[Coef('Var'  , 0.0692503   ), Coef('Var'  , 0.0345216   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0345216   ), ], 
		[Coef('Var'  , 0.0683827   ), Coef('Var'  , 0.0342018   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0342018   ), ], ])
	etat14.initMat[Chem([Sub('6')])] = FMat([
		[Coef('Var'  , 0.455313    ), Coef('Var'  , 0.508145    ), Coef('Const', 0.5625      ), Coef('Const', 0.75        ), Coef('Const', 1           ), Coef('Const', 0.75        ), Coef('Const', 0.5625      ), Coef('Var'  , 0.508145    ), ], 
		[Coef('Var'  , 0.170712    ), Coef('Var'  , 0.272843    ), Coef('Const', 0.375       ), Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0853433   ), ], 
		[Coef('Var'  , 0.0647511   ), Coef('Var'  , 0.063969    ), Coef('Const', 0.0625      ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.032719    ), ], 
		[Coef('Var'  , 0.0326471   ), Coef('Var'  , 0.0167213   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0167213   ), ], 
		[Coef('Var'  , 0.0725752   ), Coef('Var'  , 0.0365933   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.0625      ), Coef('Var'  , 0.0678433   ), ], 
		[Coef('Var'  , 0.204002    ), Coef('Var'  , 0.101728    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Const', 0.375       ), Coef('Var'  , 0.289228    ), ], ])
	etat14.initMat[Chem([Sub('7')])] = FMat([
		[Coef('Var'  , 0.336833    ), Coef('Var'  , 0.292853    ), Coef('Const', 0.25        ), Coef('Const', 0.375       ), Coef('Const', 0.5625      ), Coef('Var'  , 0.449103    ), ], 
		[Coef('Var'  , 0.327164    ), Coef('Var'  , 0.413345    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0.375       ), Coef('Var'  , 0.350845    ), ], 
		[Coef('Var'  , 0.154928    ), Coef('Var'  , 0.202641    ), Coef('Const', 0.25        ), Coef('Const', 0.125       ), Coef('Const', 0.0625      ), Coef('Var'  , 0.108891    ), ], 
		[Coef('Var'  , 0.0503049   ), Coef('Var'  , 0.0256586   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0256586   ), ], 
		[Coef('Var'  , 0.0568197   ), Coef('Var'  , 0.0286228   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0286228   ), ], 
		[Coef('Var'  , 0.0739505   ), Coef('Var'  , 0.0368803   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0368803   ), ], ])
	etat14.initMat[Chem([Sub('G')])] = FMat([
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], ])
	etat14.initMat[Chem([Sub('8')])] = FMat([
		[Coef('Var'  , 0.1644      ), Coef('Var'  , 0.171834    ), Coef('Var'  , 0.18062     ), Coef('Var'  , 0.177126    ), Coef('Var'  , 0.175999    ), Coef('Var'  , 0.164719    ), Coef('Var'  , 0.155773    ), Coef('Var'  , 0.159427    ), ], 
		[Coef('Var'  , 0.185148    ), Coef('Var'  , 0.188638    ), Coef('Var'  , 0.194009    ), Coef('Var'  , 0.179574    ), Coef('Var'  , 0.166309    ), Coef('Var'  , 0.165432    ), Coef('Var'  , 0.16521     ), Coef('Var'  , 0.174496    ), ], 
		[Coef('Var'  , 0.184541    ), Coef('Var'  , 0.183387    ), Coef('Var'  , 0.182007    ), Coef('Var'  , 0.172709    ), Coef('Var'  , 0.162258    ), Coef('Var'  , 0.165459    ), Coef('Var'  , 0.167361    ), Coef('Var'  , 0.176137    ), ], 
		[Coef('Var'  , 0.14762     ), Coef('Var'  , 0.147237    ), Coef('Var'  , 0.142238    ), Coef('Var'  , 0.14044     ), Coef('Var'  , 0.134089    ), Coef('Var'  , 0.137076    ), Coef('Var'  , 0.135633    ), Coef('Var'  , 0.143874    ), ], 
		[Coef('Var'  , 0.158381    ), Coef('Var'  , 0.151963    ), Coef('Var'  , 0.146584    ), Coef('Var'  , 0.16006     ), Coef('Var'  , 0.17435     ), Coef('Var'  , 0.182589    ), Coef('Var'  , 0.19196     ), Coef('Var'  , 0.174492    ), ], 
		[Coef('Var'  , 0.159909    ), Coef('Var'  , 0.156941    ), Coef('Var'  , 0.154542    ), Coef('Var'  , 0.170092    ), Coef('Var'  , 0.186995    ), Coef('Var'  , 0.184725    ), Coef('Var'  , 0.184064    ), Coef('Var'  , 0.171574    ), ], ])
	etat14.initMat[Chem([Sub('9')])] = FMat([
		[Coef('Var'  , 0.157751    ), Coef('Var'  , 0.156147    ), Coef('Var'  , 0.155773    ), Coef('Var'  , 0.144417    ), Coef('Var'  , 0.134686    ), Coef('Var'  , 0.143149    ), Coef('Var'  , 0.152827    ), Coef('Var'  , 0.154879    ), ], 
		[Coef('Var'  , 0.189435    ), Coef('Var'  , 0.176658    ), Coef('Var'  , 0.16521     ), Coef('Var'  , 0.145195    ), Coef('Var'  , 0.125676    ), Coef('Var'  , 0.167758    ), Coef('Var'  , 0.210678    ), Coef('Var'  , 0.19922     ), ], 
		[Coef('Var'  , 0.190681    ), Coef('Var'  , 0.179144    ), Coef('Var'  , 0.167361    ), Coef('Var'  , 0.147989    ), Coef('Var'  , 0.127715    ), Coef('Var'  , 0.168001    ), Coef('Var'  , 0.207879    ), Coef('Var'  , 0.199156    ), ], 
		[Coef('Var'  , 0.140675    ), Coef('Var'  , 0.140411    ), Coef('Var'  , 0.135633    ), Coef('Var'  , 0.116837    ), Coef('Var'  , 0.0941943   ), Coef('Var'  , 0.106287    ), Coef('Var'  , 0.11463     ), Coef('Var'  , 0.12986     ), ], 
		[Coef('Var'  , 0.162205    ), Coef('Var'  , 0.17638     ), Coef('Var'  , 0.19196     ), Coef('Var'  , 0.235716    ), Coef('Var'  , 0.280765    ), Coef('Var'  , 0.221022    ), Coef('Var'  , 0.162425    ), Coef('Var'  , 0.161687    ), ], 
		[Coef('Var'  , 0.159253    ), Coef('Var'  , 0.171261    ), Coef('Var'  , 0.184064    ), Coef('Var'  , 0.209846    ), Coef('Var'  , 0.236964    ), Coef('Var'  , 0.193783    ), Coef('Var'  , 0.151561    ), Coef('Var'  , 0.155198    ), ], ])
	etat14.initMat[Chem([Sub('10')])] = FMat([
		[Coef('Var'  , 0.170207    ), Coef('Var'  , 0.173531    ), Coef('Var'  , 0.177673    ), Coef('Var'  , 0.212633    ), Coef('Var'  , 0.222297    ), Coef('Var'  , 0.20044     ), Coef('Var'  , 0.18062     ), Coef('Var'  , 0.174799    ), ], 
		[Coef('Var'  , 0.202843    ), Coef('Var'  , 0.21987     ), Coef('Var'  , 0.239475    ), Coef('Var'  , 0.223222    ), Coef('Var'  , 0.232694    ), Coef('Var'  , 0.212367    ), Coef('Var'  , 0.194009    ), Coef('Var'  , 0.197309    ), ], 
		[Coef('Var'  , 0.197739    ), Coef('Var'  , 0.209884    ), Coef('Var'  , 0.222525    ), Coef('Var'  , 0.205624    ), Coef('Var'  , 0.180683    ), Coef('Var'  , 0.181599    ), Coef('Var'  , 0.182007    ), Coef('Var'  , 0.189872    ), ], 
		[Coef('Var'  , 0.144173    ), Coef('Var'  , 0.135012    ), Coef('Var'  , 0.121242    ), Coef('Var'  , 0.123819    ), Coef('Var'  , 0.115682    ), Coef('Var'  , 0.131145    ), Coef('Var'  , 0.142238    ), Coef('Var'  , 0.145557    ), ], 
		[Coef('Var'  , 0.140091    ), Coef('Var'  , 0.128208    ), Coef('Var'  , 0.117047    ), Coef('Var'  , 0.10624     ), Coef('Var'  , 0.11806     ), Coef('Var'  , 0.132177    ), Coef('Var'  , 0.146584    ), Coef('Var'  , 0.142903    ), ], 
		[Coef('Var'  , 0.144946    ), Coef('Var'  , 0.133497    ), Coef('Var'  , 0.122039    ), Coef('Var'  , 0.128461    ), Coef('Var'  , 0.130584    ), Coef('Var'  , 0.142273    ), Coef('Var'  , 0.154542    ), Coef('Var'  , 0.149559    ), ], ])
	etat14.initMat[Chem([Sub('11')])] = FMat([
		[Coef('Var'  , 0.163558    ), Coef('Var'  , 0.157845    ), Coef('Var'  , 0.152827    ), Coef('Var'  , 0.156241    ), Coef('Var'  , 0.160207    ), Coef('Var'  , 0.168647    ), Coef('Var'  , 0.177673    ), Coef('Var'  , 0.170251    ), ], 
		[Coef('Var'  , 0.20713     ), Coef('Var'  , 0.207891    ), Coef('Var'  , 0.210678    ), Coef('Var'  , 0.269364    ), Coef('Var'  , 0.329496    ), Coef('Var'  , 0.283504    ), Coef('Var'  , 0.239475    ), Coef('Var'  , 0.222031    ), ], 
		[Coef('Var'  , 0.20388     ), Coef('Var'  , 0.205641    ), Coef('Var'  , 0.207879    ), Coef('Var'  , 0.258909    ), Coef('Var'  , 0.310265    ), Coef('Var'  , 0.266158    ), Coef('Var'  , 0.222525    ), Coef('Var'  , 0.21289     ), ], 
		[Coef('Var'  , 0.137228    ), Coef('Var'  , 0.12818     ), Coef('Var'  , 0.11463     ), Coef('Var'  , 0.0901545   ), Coef('Var'  , 0.0623985   ), Coef('Var'  , 0.0935232   ), Coef('Var'  , 0.121242    ), Coef('Var'  , 0.131548    ), ], 
		[Coef('Var'  , 0.143915    ), Coef('Var'  , 0.152627    ), Coef('Var'  , 0.162425    ), Coef('Var'  , 0.115451    ), Coef('Var'  , 0.0692503   ), Coef('Var'  , 0.0929199   ), Coef('Var'  , 0.117047    ), Coef('Var'  , 0.130095    ), ], 
		[Coef('Var'  , 0.14429     ), Coef('Var'  , 0.147816    ), Coef('Var'  , 0.151561    ), Coef('Var'  , 0.10988     ), Coef('Var'  , 0.0683827   ), Coef('Var'  , 0.0952471   ), Coef('Var'  , 0.122039    ), Coef('Var'  , 0.133184    ), ], ])
	etat14.initMat[Chem([Sub('12')])] = FMat([
		[Coef('Var'  , 0.177341    ), Coef('Var'  , 0.174924    ), Coef('Var'  , 0.175999    ), Coef('Var'  , 0.190277    ), Coef('Var'  , 0.208537    ), Coef('Var'  , 0.208662    ), Coef('Var'  , 0.214483    ), Coef('Var'  , 0.205583    ), Coef('Var'  , 0.202811    ), Coef('Var'  , 0.187656    ), ], 
		[Coef('Var'  , 0.127964    ), Coef('Var'  , 0.147347    ), Coef('Var'  , 0.166309    ), Coef('Var'  , 0.17335     ), Coef('Var'  , 0.180914    ), Coef('Var'  , 0.167679    ), Coef('Var'  , 0.154356    ), Coef('Var'  , 0.141526    ), Coef('Var'  , 0.127367    ), Coef('Var'  , 0.128445    ), ], 
		[Coef('Var'  , 0.129612    ), Coef('Var'  , 0.147193    ), Coef('Var'  , 0.162258    ), Coef('Var'  , 0.161871    ), Coef('Var'  , 0.159378    ), Coef('Var'  , 0.151812    ), Coef('Var'  , 0.141208    ), Coef('Var'  , 0.135069    ), Coef('Var'  , 0.124967    ), Coef('Var'  , 0.12913     ), ], 
		[Coef('Var'  , 0.106972    ), Coef('Var'  , 0.122682    ), Coef('Var'  , 0.134089    ), Coef('Var'  , 0.131674    ), Coef('Var'  , 0.124679    ), Coef('Var'  , 0.122188    ), Coef('Var'  , 0.115012    ), Coef('Var'  , 0.11181     ), Coef('Var'  , 0.104061    ), Coef('Var'  , 0.107634    ), ], 
		[Coef('Var'  , 0.21239     ), Coef('Var'  , 0.192916    ), Coef('Var'  , 0.17435     ), Coef('Var'  , 0.162593    ), Coef('Var'  , 0.150881    ), Coef('Var'  , 0.15839     ), Coef('Var'  , 0.164987    ), Coef('Var'  , 0.177604    ), Coef('Var'  , 0.189687    ), Coef('Var'  , 0.200792    ), ], 
		[Coef('Var'  , 0.245721    ), Coef('Var'  , 0.214938    ), Coef('Var'  , 0.186995    ), Coef('Var'  , 0.180235    ), Coef('Var'  , 0.175612    ), Coef('Var'  , 0.191269    ), Coef('Var'  , 0.209954    ), Coef('Var'  , 0.228407    ), Coef('Var'  , 0.251107    ), Coef('Var'  , 0.246343    ), ], ])
	etat14.initMat[Chem([Sub('13')])] = FMat([
		[Coef('Const', 0.0625      ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.03125     ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 1.96214e-17 ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.125       ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.25        ), ], 
		[Coef('Const', 0.5625      ), Coef('Const', 0.75        ), Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.40625     ), ], 
		[Coef('Const', 0.375       ), Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.1875      ), ], ])
	etat14.initMat[Chem([Sub('14')])] = FMat([
		[Coef('Const', 0.0625      ), Coef('Var'  , 0.03125     ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.375       ), Coef('Var'  , 0.1875      ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), ], 
		[Coef('Const', 0.5625      ), Coef('Var'  , 0.40625     ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.75        ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.25        ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.125       ), Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  ,-2.97843e-17 ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], ])
	etat14.initMat[Chem([Sub('15')])] = FMat([
		[Coef('Var'  , 0.234037    ), Coef('Var'  , 0.220994    ), Coef('Var'  , 0.214483    ), Coef('Var'  , 0.22901     ), Coef('Var'  , 0.250093    ), Coef('Var'  , 0.266629    ), Coef('Var'  , 0.289835    ), Coef('Var'  , 0.258613    ), ], 
		[Coef('Var'  , 0.131194    ), Coef('Var'  , 0.143342    ), Coef('Var'  , 0.154356    ), Coef('Var'  , 0.164127    ), Coef('Var'  , 0.173571    ), Coef('Var'  , 0.163683    ), Coef('Var'  , 0.153698    ), Coef('Var'  , 0.142898    ), ], 
		[Coef('Var'  , 0.119528    ), Coef('Var'  , 0.132326    ), Coef('Var'  , 0.141208    ), Coef('Var'  , 0.141991    ), Coef('Var'  , 0.139377    ), Coef('Var'  , 0.129613    ), Coef('Var'  , 0.116661    ), Coef('Var'  , 0.119948    ), ], 
		[Coef('Var'  , 0.0971969   ), Coef('Var'  , 0.108353    ), Coef('Var'  , 0.115012    ), Coef('Var'  , 0.113075    ), Coef('Var'  , 0.106569    ), Coef('Var'  , 0.0988514   ), Coef('Var'  , 0.0869695   ), Coef('Var'  , 0.0941291   ), ], 
		[Coef('Var'  , 0.171261    ), Coef('Var'  , 0.168662    ), Coef('Var'  , 0.164987    ), Coef('Var'  , 0.15426     ), Coef('Var'  , 0.141998    ), Coef('Var'  , 0.140325    ), Coef('Var'  , 0.136568    ), Coef('Var'  , 0.154727    ), ], 
		[Coef('Var'  , 0.246783    ), Coef('Var'  , 0.226323    ), Coef('Var'  , 0.209954    ), Coef('Var'  , 0.197537    ), Coef('Var'  , 0.188393    ), Coef('Var'  , 0.2009      ), Coef('Var'  , 0.216268    ), Coef('Var'  , 0.229686    ), ], ])
	etat14.initMat[Chem([Sub('16')])] = FMat([
		[Coef('Var'  , 0.387601    ), Coef('Var'  , 0.335964    ), Coef('Var'  , 0.289835    ), Coef('Var'  , 0.304524    ), Coef('Var'  , 0.325327    ), Coef('Var'  , 0.388182    ), Coef('Var'  , 0.455313    ), Coef('Var'  , 0.419621    ), ], 
		[Coef('Var'  , 0.102206    ), Coef('Var'  , 0.128168    ), Coef('Var'  , 0.153698    ), Coef('Var'  , 0.179703    ), Coef('Var'  , 0.205768    ), Coef('Var'  , 0.188111    ), Coef('Var'  , 0.170712    ), Coef('Var'  , 0.136577    ), ], 
		[Coef('Var'  , 0.066598    ), Coef('Var'  , 0.093039    ), Coef('Var'  , 0.116661    ), Coef('Var'  , 0.120858    ), Coef('Var'  , 0.122251    ), Coef('Var'  , 0.0944184   ), Coef('Var'  , 0.0647511   ), Coef('Var'  , 0.0665998   ), ], 
		[Coef('Var'  , 0.0477122   ), Coef('Var'  , 0.0688987   ), Coef('Var'  , 0.0869695   ), Coef('Var'  , 0.0822032   ), Coef('Var'  , 0.0738437   ), Coef('Var'  , 0.0544625   ), Coef('Var'  , 0.0326471   ), Coef('Var'  , 0.041158    ), ], 
		[Coef('Var'  , 0.116601    ), Coef('Var'  , 0.127461    ), Coef('Var'  , 0.136568    ), Coef('Var'  , 0.12177     ), Coef('Var'  , 0.104814    ), Coef('Var'  , 0.0895366   ), Coef('Var'  , 0.0725752   ), Coef('Var'  , 0.0952277   ), ], 
		[Coef('Var'  , 0.279282    ), Coef('Var'  , 0.246469    ), Coef('Var'  , 0.216268    ), Coef('Var'  , 0.190942    ), Coef('Var'  , 0.167996    ), Coef('Var'  , 0.18529     ), Coef('Var'  , 0.204002    ), Coef('Var'  , 0.240817    ), ], ])
	
	
	
	etat15.bords   = {Bord('0'): etat21, Bord('1'): etat19, Bord('2'): etat22, }
	etat15.permuts = {}
	etat15.interns = {Intern('_'): etat15, }
	etat15.subs    = {Sub('0'): etat1, Sub('1'): etat2, Sub('2'): etat3, Sub('3'): etat4, Sub('4'): etat5, Sub('5'): etat6, Sub('6'): etat7, Sub('7'): etat8, Sub('G', True): Etat.etatPoint, Sub('8'): etat9, Sub('9'): etat10, Sub('10'): etat11, Sub('11'): etat12, Sub('12'): etat13, Sub('13'): etat14, Sub('14'): etat16, Sub('15'): etat17, Sub('16'): etat18, }
	
	etat15.buildIntern()
	
	
	etat15.eqs = [
		(Chem([Bord('0'), Sub('0'), Permut('0'), ])	,	Chem([Sub('1'), Bord('3'), ])),
		(Chem([Bord('2'), Sub('4'), Permut('0'), ])	,	Chem([Sub('1'), Bord('4'), ])),
		(Chem([Bord('0'), Sub('1'), Permut('0'), ])	,	Chem([Sub('3'), Bord('3'), ])),
		(Chem([Bord('2'), Sub('1'), Permut('0'), ])	,	Chem([Sub('5'), Bord('0'), ])),
		(Chem([Bord('0'), Sub('2'), Permut('0'), ])	,	Chem([Sub('6'), Bord('2'), ])),
		(Chem([Bord('2'), Sub('3'), Permut('0'), ])	,	Chem([Sub('9'), Bord('2'), ])),
		(Chem([Bord('2'), Sub('2'), Permut('0'), ])	,	Chem([Sub('11'), Bord('1'), ])),
		(Chem([Bord('1'), Sub('0'), Permut('0'), ])	,	Chem([Sub('13'), Bord('1'), ])),
		(Chem([Bord('0'), Sub('3'), Permut('0'), ])	,	Chem([Sub('13'), Bord('2'), ])),
		(Chem([Bord('2'), Sub('0'), Permut('0'), ])	,	Chem([Sub('14'), Bord('0'), ])),
		(Chem([Bord('1'), Sub('1'), Permut('0'), ])	,	Chem([Sub('14'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('0'), Bord('1'), ])	,	Chem([Sub('12'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('1'), Bord('1'), ])	,	Chem([Sub('15'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('2'), Bord('1'), ])	,	Chem([Sub('3'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('3'), Bord('1'), ])	,	Chem([Sub('1'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('0'), Bord('1'), ])	,	Chem([Sub('12'), Bord('4'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('2'), Bord('1'), ])	,	Chem([Sub('3'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('4'), Bord('1'), ])	,	Chem([Sub('9'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('0'), Bord('1'), ])	,	Chem([Sub('12'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('1'), Bord('1'), ])	,	Chem([Sub('10'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('2'), Bord('1'), ])	,	Chem([Sub('7'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('3'), Bord('1'), ])	,	Chem([Sub('16'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('4'), Bord('1'), ])	,	Chem([Sub('15'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('3'), Bord('1'), Bord('1'), ])	,	Chem([Sub('16'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('3'), Bord('2'), Bord('1'), ])	,	Chem([Sub('6'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('4'), Bord('0'), Bord('1'), ])	,	Chem([Sub('8'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('4'), Bord('1'), Bord('1'), ])	,	Chem([Sub('9'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('4'), Bord('2'), Bord('1'), ])	,	Chem([Sub('11'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('4'), Bord('3'), Bord('1'), ])	,	Chem([Sub('10'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('5'), Bord('0'), Bord('1'), ])	,	Chem([Sub('14'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('5'), Bord('1'), Bord('1'), ])	,	Chem([Sub('7'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('5'), Bord('2'), Bord('1'), ])	,	Chem([Sub('11'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('6'), Bord('0'), Bord('1'), ])	,	Chem([Sub('7'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('6'), Bord('1'), Bord('1'), ])	,	Chem([Sub('13'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('6'), Bord('3'), Bord('1'), ])	,	Chem([Sub('16'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('8'), Bord('0'), Bord('1'), ])	,	Chem([Sub('10'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('8'), Bord('1'), Bord('1'), ])	,	Chem([Sub('12'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('8'), Bord('2'), Bord('1'), ])	,	Chem([Sub('9'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('9'), Bord('2'), Bord('1'), ])	,	Chem([Sub('11'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('10'), Bord('0'), Bord('1'), ])	,	Chem([Sub('11'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('12'), Bord('2'), Bord('1'), ])	,	Chem([Sub('15'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('13'), Bord('0'), Bord('1'), ])	,	Chem([Sub('14'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('15'), Bord('2'), Bord('1'), ])	,	Chem([Sub('16'), Bord('0'), Bord('1'), ])),
		(Chem([Bord('0'), Bord('1'), ])	,	Chem([Bord('1'), Bord('0'), ])),
		(Chem([Bord('1'), Bord('1'), ])	,	Chem([Bord('2'), Bord('0'), ])),
		(Chem([Bord('2'), Bord('1'), ])	,	Chem([Bord('0'), Bord('0'), ])),
		]
	
	
	etat15.prim.elems = [Figure(2, [Chem([Bord('0'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('0'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('0'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('0'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('1'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('1'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('1'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('1'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('2'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('2'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('2'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('2'), Sub('1'), Sub('1'), Bord('0'), ]), ])]
	etat15.grid.elems = [
		Figure(1, [Chem([Bord('1'), Bord('0'), ]), Chem([Bord('1'), Intern(''), ]), Chem([Bord('1'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('2'), Bord('0'), ]), Chem([Bord('2'), Intern(''), ]), Chem([Bord('2'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('0'), Bord('0'), ]), Chem([Bord('0'), Intern(''), ]), Chem([Bord('0'), Bord('1'), ]), ]), ]
	
	
	etat15.space = [Chem([Bord('2'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('2'), Intern('0'), Intern('0'), ]), ]
	
	etat15.initMat[Chem([Sub('0')])] = FMat([
		[Coef('Var'  , 0.413269    ), Coef('Var'  , 0.369571    ), Coef('Var'  , 0.332519    ), Coef('Var'  , 0.306638    ), Coef('Var'  , 0.288379    ), Coef('Var'  , 0.328176    ), Coef('Var'  , 0.374162    ), Coef('Var'  , 0.391109    ), ], 
		[Coef('Var'  , 0.249906    ), Coef('Var'  , 0.223361    ), Coef('Var'  , 0.199203    ), Coef('Var'  , 0.210957    ), Coef('Var'  , 0.226129    ), Coef('Var'  , 0.257619    ), Coef('Var'  , 0.292526    ), Coef('Var'  , 0.270023    ), ], 
		[Coef('Var'  , 0.101201    ), Coef('Var'  , 0.112531    ), Coef('Var'  , 0.122082    ), Coef('Var'  , 0.134633    ), Coef('Var'  , 0.145307    ), Coef('Var'  , 0.13721     ), Coef('Var'  , 0.127766    ), Coef('Var'  , 0.115108    ), ], 
		[Coef('Var'  , 0.0568657   ), Coef('Var'  , 0.074462    ), Coef('Var'  , 0.0881894   ), Coef('Var'  , 0.0940734   ), Coef('Var'  , 0.0950915   ), Coef('Var'  , 0.0780645   ), Coef('Var'  , 0.0568205   ), Coef('Var'  , 0.0584532   ), ], 
		[Coef('Var'  , 0.0707692   ), Coef('Var'  , 0.0909786   ), Coef('Var'  , 0.108212    ), Coef('Var'  , 0.113109    ), Coef('Var'  , 0.114489    ), Coef('Var'  , 0.0930944   ), Coef('Var'  , 0.0686693   ), Coef('Var'  , 0.070964    ), ], 
		[Coef('Var'  , 0.107988    ), Coef('Var'  , 0.129096    ), Coef('Var'  , 0.149795    ), Coef('Var'  , 0.14059     ), Coef('Var'  , 0.130605    ), Coef('Var'  , 0.105835    ), Coef('Var'  , 0.0800557   ), Coef('Var'  , 0.0943416   ), ], ])
	etat15.initMat[Chem([Sub('1')])] = FMat([
		[Coef('Const', 0.64        ), Coef('Var'  , 0.525899    ), Coef('Var'  , 0.414895    ), Coef('Var'  , 0.411149    ), Coef('Var'  , 0.413269    ), Coef('Var'  , 0.4865      ), Coef('Const', 0.5625      ), Coef('Const', 0.75        ), Coef('Const', 1           ), Coef('Const', 0.8         ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0716168   ), Coef('Var'  , 0.143612    ), Coef('Var'  , 0.196088    ), Coef('Var'  , 0.249906    ), Coef('Var'  , 0.311972    ), Coef('Const', 0.375       ), Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0425572   ), Coef('Var'  , 0.0841224   ), Coef('Var'  , 0.0935303   ), Coef('Var'  , 0.101201    ), Coef('Var'  , 0.0822231   ), Coef('Const', 0.0625      ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0330813   ), Coef('Var'  , 0.0643968   ), Coef('Var'  , 0.0622959   ), Coef('Var'  , 0.0568657   ), Coef('Var'  , 0.0292145   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.04        ), Coef('Var'  , 0.0667698   ), Coef('Var'  , 0.0924149   ), Coef('Var'  , 0.0827797   ), Coef('Var'  , 0.0707692   ), Coef('Var'  , 0.0360099   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.32        ), Coef('Var'  , 0.260076    ), Coef('Var'  , 0.200559    ), Coef('Var'  , 0.154157    ), Coef('Var'  , 0.107988    ), Coef('Var'  , 0.0540807   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.2         ), ], ])
	etat15.initMat[Chem([Sub('2')])] = FMat([
		[Coef('Var'  , 0.220261    ), Coef('Var'  , 0.224576    ), Coef('Var'  , 0.236378    ), Coef('Var'  , 0.217169    ), Coef('Var'  , 0.205205    ), Coef('Var'  , 0.179397    ), Coef('Var'  , 0.158749    ), Coef('Var'  , 0.175556    ), Coef('Var'  , 0.196763    ), Coef('Var'  , 0.205466    ), ], 
		[Coef('Var'  , 0.202018    ), Coef('Var'  , 0.181965    ), Coef('Var'  , 0.164231    ), Coef('Var'  , 0.150887    ), Coef('Var'  , 0.137265    ), Coef('Var'  , 0.156087    ), Coef('Var'  , 0.175108    ), Coef('Var'  , 0.200951    ), Coef('Var'  , 0.229747    ), Coef('Var'  , 0.213932    ), ], 
		[Coef('Var'  , 0.164804    ), Coef('Var'  , 0.152942    ), Coef('Var'  , 0.138831    ), Coef('Var'  , 0.134208    ), Coef('Var'  , 0.126736    ), Coef('Var'  , 0.152985    ), Coef('Var'  , 0.176953    ), Coef('Var'  , 0.183202    ), Coef('Var'  , 0.188046    ), Coef('Var'  , 0.177187    ), ], 
		[Coef('Var'  , 0.110462    ), Coef('Var'  , 0.113472    ), Coef('Var'  , 0.110462    ), Coef('Var'  , 0.105519    ), Coef('Var'  , 0.0946654   ), Coef('Var'  , 0.0858652   ), Coef('Var'  , 0.0718199   ), Coef('Var'  , 0.0837622   ), Coef('Var'  , 0.0906169   ), Coef('Var'  , 0.10342     ), ], 
		[Coef('Var'  , 0.145416    ), Coef('Var'  , 0.152105    ), Coef('Var'  , 0.156352    ), Coef('Var'  , 0.175558    ), Coef('Var'  , 0.193501    ), Coef('Var'  , 0.203463    ), Coef('Var'  , 0.213101    ), Coef('Var'  , 0.181185    ), Coef('Var'  , 0.148241    ), Coef('Var'  , 0.147981    ), ], 
		[Coef('Var'  , 0.157039    ), Coef('Var'  , 0.174941    ), Coef('Var'  , 0.193745    ), Coef('Var'  , 0.216659    ), Coef('Var'  , 0.242628    ), Coef('Var'  , 0.222203    ), Coef('Var'  , 0.20427     ), Coef('Var'  , 0.175343    ), Coef('Var'  , 0.146586    ), Coef('Var'  , 0.152015    ), ], ])
	etat15.initMat[Chem([Sub('3')])] = FMat([
		[Coef('Const', 0.5625      ), Coef('Var'  , 0.467109    ), Coef('Var'  , 0.374162    ), Coef('Var'  , 0.314913    ), Coef('Var'  , 0.260047    ), Coef('Var'  , 0.254054    ), Coef('Const', 0.25        ), Coef('Const', 0.375       ), ], 
		[Coef('Const', 0.375       ), Coef('Var'  , 0.333052    ), Coef('Var'  , 0.292526    ), Coef('Var'  , 0.31207     ), Coef('Var'  , 0.334686    ), Coef('Var'  , 0.416518    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0.0625      ), Coef('Var'  , 0.0953853   ), Coef('Var'  , 0.127766    ), Coef('Var'  , 0.16237     ), Coef('Var'  , 0.19615     ), Coef('Var'  , 0.223235    ), Coef('Const', 0.25        ), Coef('Const', 0.125       ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0292386   ), Coef('Var'  , 0.0568205   ), Coef('Var'  , 0.0583362   ), Coef('Var'  , 0.0564118   ), Coef('Var'  , 0.0290976   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0349541   ), Coef('Var'  , 0.0686693   ), Coef('Var'  , 0.0733469   ), Coef('Var'  , 0.0758027   ), Coef('Var'  , 0.0383928   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0402609   ), Coef('Var'  , 0.0800557   ), Coef('Var'  , 0.0789638   ), Coef('Var'  , 0.0769019   ), Coef('Var'  , 0.0387029   ), Coef('Const', 0           ), Coef('Const', 0           ), ], ])
	etat15.initMat[Chem([Sub('4')])] = FMat([
		[Coef('Var'  , 0.246532    ), Coef('Var'  , 0.262962    ), Coef('Var'  , 0.28716     ), Coef('Var'  , 0.299156    ), Coef('Var'  , 0.318013    ), Coef('Var'  , 0.294969    ), Coef('Var'  , 0.277385    ), Coef('Var'  , 0.258775    ), ], 
		[Coef('Var'  , 0.0986089   ), Coef('Var'  , 0.1011      ), Coef('Var'  , 0.0984306   ), Coef('Var'  , 0.084607    ), Coef('Var'  , 0.066184    ), Coef('Var'  , 0.0682081   ), Coef('Var'  , 0.0663623   ), Coef('Var'  , 0.0847012   ), ], 
		[Coef('Var'  , 0.0829874   ), Coef('Var'  , 0.0840519   ), Coef('Var'  , 0.0813453   ), Coef('Var'  , 0.0692283   ), Coef('Var'  , 0.0538498   ), Coef('Var'  , 0.0560205   ), Coef('Var'  , 0.0554919   ), Coef('Var'  , 0.0708441   ), ], 
		[Coef('Var'  , 0.0840962   ), Coef('Var'  , 0.0867881   ), Coef('Var'  , 0.0837805   ), Coef('Var'  , 0.0727436   ), Coef('Var'  , 0.0568929   ), Coef('Var'  , 0.0590362   ), Coef('Var'  , 0.0572087   ), Coef('Var'  , 0.0730806   ), ], 
		[Coef('Var'  , 0.18648     ), Coef('Var'  , 0.17351     ), Coef('Var'  , 0.160363    ), Coef('Var'  , 0.159129    ), Coef('Var'  , 0.157603    ), Coef('Var'  , 0.170708    ), Coef('Var'  , 0.18372     ), Coef('Var'  , 0.185089    ), ], 
		[Coef('Var'  , 0.301296    ), Coef('Var'  , 0.291588    ), Coef('Var'  , 0.28892     ), Coef('Var'  , 0.315136    ), Coef('Var'  , 0.347456    ), Coef('Var'  , 0.351058    ), Coef('Var'  , 0.359832    ), Coef('Var'  , 0.32751     ), ], ])
	etat15.initMat[Chem([Sub('5')])] = FMat([
		[Coef('Const', 0.16        ), Coef('Const', 0.08        ), Coef('Const', 0.04        ), Coef('Var'  , 0.0802561   ), Coef('Var'  , 0.121181    ), Coef('Var'  , 0.140256    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0508857   ), Coef('Var'  , 0.102385    ), Coef('Var'  , 0.0508857   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0566497   ), Coef('Var'  , 0.112959    ), Coef('Var'  , 0.0566497   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0165398   ), Coef('Var'  , 0.0319572   ), Coef('Var'  , 0.0165398   ), ], 
		[Coef('Const', 0.36        ), Coef('Const', 0.48        ), Coef('Const', 0.64        ), Coef('Var'  , 0.492077    ), Coef('Var'  , 0.344239    ), Coef('Var'  , 0.352077    ), ], 
		[Coef('Const', 0.48        ), Coef('Const', 0.44        ), Coef('Const', 0.32        ), Coef('Var'  , 0.303592    ), Coef('Var'  , 0.287278    ), Coef('Var'  , 0.383592    ), ], ])
	etat15.initMat[Chem([Sub('6')])] = FMat([
		[Coef('Var'  , 0.206066    ), Coef('Var'  , 0.168939    ), Coef('Var'  , 0.134199    ), Coef('Var'  , 0.0978672   ), Coef('Const', 0.0625      ), Coef('Const', 0.125       ), Coef('Const', 0.25        ), Coef('Var'  , 0.227322    ), ], 
		[Coef('Var'  , 0.322333    ), Coef('Var'  , 0.280458    ), Coef('Var'  , 0.24106     ), Coef('Var'  , 0.307539    ), Coef('Const', 0.375       ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.410419    ), ], 
		[Coef('Var'  , 0.227274    ), Coef('Var'  , 0.249515    ), Coef('Var'  , 0.271054    ), Coef('Var'  , 0.416974    ), Coef('Const', 0.5625      ), Coef('Const', 0.375       ), Coef('Const', 0.25        ), Coef('Var'  , 0.238791    ), ], 
		[Coef('Var'  , 0.052559    ), Coef('Var'  , 0.0496125   ), Coef('Var'  , 0.0433722   ), Coef('Var'  , 0.0224504   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.027162    ), ], 
		[Coef('Var'  , 0.0985859   ), Coef('Var'  , 0.131683    ), Coef('Var'  , 0.164222    ), Coef('Var'  , 0.0821275   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.049556    ), ], 
		[Coef('Var'  , 0.0931826   ), Coef('Var'  , 0.119792    ), Coef('Var'  , 0.146092    ), Coef('Var'  , 0.0730425   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0467496   ), ], ])
	etat15.initMat[Chem([Sub('7')])] = FMat([
		[Coef('Var'  , 0.158749    ), Coef('Var'  , 0.138703    ), Coef('Var'  , 0.121181    ), Coef('Var'  , 0.126873    ), Coef('Var'  , 0.134199    ), Coef('Var'  , 0.145064    ), ], 
		[Coef('Var'  , 0.175108    ), Coef('Var'  , 0.137977    ), Coef('Var'  , 0.102385    ), Coef('Var'  , 0.170924    ), Coef('Var'  , 0.24106     ), Coef('Var'  , 0.20713     ), ], 
		[Coef('Var'  , 0.176953    ), Coef('Var'  , 0.145517    ), Coef('Var'  , 0.112959    ), Coef('Var'  , 0.192373    ), Coef('Var'  , 0.271054    ), Coef('Var'  , 0.224591    ), ], 
		[Coef('Var'  , 0.0718199   ), Coef('Var'  , 0.0536201   ), Coef('Var'  , 0.0319572   ), Coef('Var'  , 0.0389903   ), Coef('Var'  , 0.0433722   ), Coef('Var'  , 0.0595306   ), ], 
		[Coef('Var'  , 0.213101    ), Coef('Var'  , 0.278684    ), Coef('Var'  , 0.344239    ), Coef('Var'  , 0.254204    ), Coef('Var'  , 0.164222    ), Coef('Var'  , 0.188734    ), ], 
		[Coef('Var'  , 0.20427     ), Coef('Var'  , 0.245499    ), Coef('Var'  , 0.287278    ), Coef('Var'  , 0.216634    ), Coef('Var'  , 0.146092    ), Coef('Var'  , 0.17495     ), ], ])
	etat15.initMat[Chem([Sub('G')])] = FMat([
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], ])
	etat15.initMat[Chem([Sub('8')])] = FMat([
		[Coef('Var'  , 0.28716     ), Coef('Var'  , 0.264417    ), Coef('Var'  , 0.249871    ), Coef('Var'  , 0.275153    ), Coef('Var'  , 0.308659    ), Coef('Var'  , 0.340508    ), Coef('Var'  , 0.379556    ), Coef('Var'  , 0.329772    ), ], 
		[Coef('Var'  , 0.0984306   ), Coef('Var'  , 0.112514    ), Coef('Var'  , 0.121846    ), Coef('Var'  , 0.127344    ), Coef('Var'  , 0.129712    ), Coef('Var'  , 0.105439    ), Coef('Var'  , 0.078396    ), Coef('Var'  , 0.0906098   ), ], 
		[Coef('Var'  , 0.0813453   ), Coef('Var'  , 0.0945022   ), Coef('Var'  , 0.103818    ), Coef('Var'  , 0.104726    ), Coef('Var'  , 0.102087    ), Coef('Var'  , 0.0841965   ), Coef('Var'  , 0.063291    ), Coef('Var'  , 0.0739723   ), ], 
		[Coef('Var'  , 0.0837805   ), Coef('Var'  , 0.0936828   ), Coef('Var'  , 0.0976174   ), Coef('Var'  , 0.097724    ), Coef('Var'  , 0.092       ), Coef('Var'  , 0.0804893   ), Coef('Var'  , 0.0641751   ), Coef('Var'  , 0.0764482   ), ], 
		[Coef('Var'  , 0.160363    ), Coef('Var'  , 0.165598    ), Coef('Var'  , 0.170424    ), Coef('Var'  , 0.154816    ), Coef('Var'  , 0.138205    ), Coef('Var'  , 0.132095    ), Coef('Var'  , 0.124912    ), Coef('Var'  , 0.142877    ), ], 
		[Coef('Var'  , 0.28892     ), Coef('Var'  , 0.269286    ), Coef('Var'  , 0.256423    ), Coef('Var'  , 0.240236    ), Coef('Var'  , 0.229338    ), Coef('Var'  , 0.257272    ), Coef('Var'  , 0.28967     ), Coef('Var'  , 0.286321    ), ], ])
	etat15.initMat[Chem([Sub('9')])] = FMat([
		[Coef('Var'  , 0.318013    ), Coef('Var'  , 0.345775    ), Coef('Var'  , 0.379556    ), Coef('Var'  , 0.508195    ), Coef('Const', 0.64        ), Coef('Const', 0.48        ), Coef('Const', 0.36        ), Coef('Var'  , 0.33758     ), ], 
		[Coef('Var'  , 0.066184    ), Coef('Var'  , 0.0741638   ), Coef('Var'  , 0.078396    ), Coef('Var'  , 0.0400833   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0340805   ), ], 
		[Coef('Var'  , 0.0538498   ), Coef('Var'  , 0.0599566   ), Coef('Var'  , 0.063291    ), Coef('Var'  , 0.0323504   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0276063   ), ], 
		[Coef('Var'  , 0.0568929   ), Coef('Var'  , 0.0625722   ), Coef('Var'  , 0.0641751   ), Coef('Var'  , 0.0331384   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0294338   ), ], 
		[Coef('Var'  , 0.157603    ), Coef('Var'  , 0.141475    ), Coef('Var'  , 0.124912    ), Coef('Var'  , 0.0826116   ), Coef('Const', 0.04        ), Coef('Const', 0.08        ), Coef('Const', 0.16        ), Coef('Var'  , 0.158864    ), ], 
		[Coef('Var'  , 0.347456    ), Coef('Var'  , 0.316057    ), Coef('Var'  , 0.28967     ), Coef('Var'  , 0.303621    ), Coef('Const', 0.32        ), Coef('Const', 0.44        ), Coef('Const', 0.48        ), Coef('Var'  , 0.412436    ), ], ])
	etat15.initMat[Chem([Sub('10')])] = FMat([
		[Coef('Var'  , 0.246532    ), Coef('Var'  , 0.227413    ), Coef('Var'  , 0.21468     ), Coef('Var'  , 0.206977    ), Coef('Var'  , 0.205205    ), Coef('Var'  , 0.22379     ), Coef('Var'  , 0.249871    ), Coef('Var'  , 0.244226    ), ], 
		[Coef('Var'  , 0.0986089   ), Coef('Var'  , 0.0913237   ), Coef('Var'  , 0.0799162   ), Coef('Var'  , 0.109745    ), Coef('Var'  , 0.137265    ), Coef('Var'  , 0.130983    ), Coef('Var'  , 0.121846    ), Coef('Var'  , 0.112561    ), ], 
		[Coef('Var'  , 0.0829874   ), Coef('Var'  , 0.0781622   ), Coef('Var'  , 0.0701176   ), Coef('Var'  , 0.0998503   ), Coef('Var'  , 0.126736    ), Coef('Var'  , 0.116998    ), Coef('Var'  , 0.103818    ), Coef('Var'  , 0.0953101   ), ], 
		[Coef('Var'  , 0.0840962   ), Coef('Var'  , 0.0771656   ), Coef('Var'  , 0.0652011   ), Coef('Var'  , 0.0824723   ), Coef('Var'  , 0.0946654   ), Coef('Var'  , 0.099158    ), Coef('Var'  , 0.0976174   ), Coef('Var'  , 0.0938513   ), ], 
		[Coef('Var'  , 0.18648     ), Coef('Var'  , 0.208671    ), Coef('Var'  , 0.230903    ), Coef('Var'  , 0.212281    ), Coef('Var'  , 0.193501    ), Coef('Var'  , 0.182189    ), Coef('Var'  , 0.170424    ), Coef('Var'  , 0.178578    ), ], 
		[Coef('Var'  , 0.301296    ), Coef('Var'  , 0.317265    ), Coef('Var'  , 0.339182    ), Coef('Var'  , 0.288674    ), Coef('Var'  , 0.242628    ), Coef('Var'  , 0.246882    ), Coef('Var'  , 0.256423    ), Coef('Var'  , 0.275473    ), ], ])
	etat15.initMat[Chem([Sub('11')])] = FMat([
		[Coef('Var'  , 0.277385    ), Coef('Var'  , 0.317389    ), Coef('Const', 0.36        ), Coef('Const', 0.24        ), Coef('Const', 0.16        ), Coef('Var'  , 0.186027    ), Coef('Var'  , 0.21468     ), Coef('Var'  , 0.243417    ), ], 
		[Coef('Var'  , 0.0663623   ), Coef('Var'  , 0.0341276   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0407501   ), Coef('Var'  , 0.0799162   ), Coef('Var'  , 0.0748777   ), ], 
		[Coef('Var'  , 0.0554919   ), Coef('Var'  , 0.0284142   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0357323   ), Coef('Var'  , 0.0701176   ), Coef('Var'  , 0.0641465   ), ], 
		[Coef('Var'  , 0.0572087   ), Coef('Var'  , 0.0296023   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0336874   ), Coef('Var'  , 0.0652011   ), Coef('Var'  , 0.0632897   ), ], 
		[Coef('Var'  , 0.18372     ), Coef('Var'  , 0.171844    ), Coef('Const', 0.16        ), Coef('Const', 0.24        ), Coef('Const', 0.36        ), Coef('Var'  , 0.295425    ), Coef('Var'  , 0.230903    ), Coef('Var'  , 0.207269    ), ], 
		[Coef('Var'  , 0.359832    ), Coef('Var'  , 0.418623    ), Coef('Const', 0.48        ), Coef('Const', 0.52        ), Coef('Const', 0.48        ), Coef('Var'  , 0.408378    ), Coef('Var'  , 0.339182    ), Coef('Var'  , 0.347       ), ], ])
	etat15.initMat[Chem([Sub('12')])] = FMat([
		[Coef('Var'  , 0.414895    ), Coef('Var'  , 0.358212    ), Coef('Var'  , 0.308659    ), Coef('Var'  , 0.268532    ), Coef('Var'  , 0.236378    ), Coef('Var'  , 0.242983    ), Coef('Var'  , 0.257585    ), Coef('Var'  , 0.291085    ), Coef('Var'  , 0.332519    ), Coef('Var'  , 0.37022     ), ], 
		[Coef('Var'  , 0.143612    ), Coef('Var'  , 0.136973    ), Coef('Var'  , 0.129712    ), Coef('Var'  , 0.147248    ), Coef('Var'  , 0.164231    ), Coef('Var'  , 0.177717    ), Coef('Var'  , 0.193275    ), Coef('Var'  , 0.194715    ), Coef('Var'  , 0.199203    ), Coef('Var'  , 0.170506    ), ], 
		[Coef('Var'  , 0.0841224   ), Coef('Var'  , 0.0944034   ), Coef('Var'  , 0.102087    ), Coef('Var'  , 0.121936    ), Coef('Var'  , 0.138831    ), Coef('Var'  , 0.143594    ), Coef('Var'  , 0.145929    ), Coef('Var'  , 0.135062    ), Coef('Var'  , 0.122082    ), Coef('Var'  , 0.104115    ), ], 
		[Coef('Var'  , 0.0643968   ), Coef('Var'  , 0.0804322   ), Coef('Var'  , 0.092       ), Coef('Var'  , 0.104085    ), Coef('Var'  , 0.110462    ), Coef('Var'  , 0.112851    ), Coef('Var'  , 0.109402    ), Coef('Var'  , 0.101365    ), Coef('Var'  , 0.0881894   ), Coef('Var'  , 0.0783288   ), ], 
		[Coef('Var'  , 0.0924149   ), Coef('Var'  , 0.116253    ), Coef('Var'  , 0.138205    ), Coef('Var'  , 0.148185    ), Coef('Var'  , 0.156352    ), Coef('Var'  , 0.147484    ), Coef('Var'  , 0.135892    ), Coef('Var'  , 0.123751    ), Coef('Var'  , 0.108212    ), Coef('Var'  , 0.101738    ), ], 
		[Coef('Var'  , 0.200559    ), Coef('Var'  , 0.213726    ), Coef('Var'  , 0.229338    ), Coef('Var'  , 0.210013    ), Coef('Var'  , 0.193745    ), Coef('Var'  , 0.175371    ), Coef('Var'  , 0.157917    ), Coef('Var'  , 0.154023    ), Coef('Var'  , 0.149795    ), Coef('Var'  , 0.175091    ), ], ])
	etat15.initMat[Chem([Sub('13')])] = FMat([
		[Coef('Const', 0.0625      ), Coef('Var'  , 0.03125     ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.375       ), Coef('Var'  , 0.1875      ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), ], 
		[Coef('Const', 0.5625      ), Coef('Var'  , 0.40625     ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.75        ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.25        ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.125       ), Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  ,-1.28762e-17 ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], ])
	etat15.initMat[Chem([Sub('14')])] = FMat([
		[Coef('Const', 0.04        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.02        ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  ,-6.26214e-18 ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.125       ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.25        ), ], 
		[Coef('Const', 0.64        ), Coef('Const', 0.8         ), Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.445       ), ], 
		[Coef('Const', 0.32        ), Coef('Const', 0.2         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.16        ), ], ])
	etat15.initMat[Chem([Sub('15')])] = FMat([
		[Coef('Var'  , 0.288379    ), Coef('Var'  , 0.269081    ), Coef('Var'  , 0.257585    ), Coef('Var'  , 0.23512     ), Coef('Var'  , 0.220261    ), Coef('Var'  , 0.222899    ), Coef('Var'  , 0.232217    ), Coef('Var'  , 0.25686     ), ], 
		[Coef('Var'  , 0.226129    ), Coef('Var'  , 0.207893    ), Coef('Var'  , 0.193275    ), Coef('Var'  , 0.195898    ), Coef('Var'  , 0.202018    ), Coef('Var'  , 0.219835    ), Coef('Var'  , 0.241815    ), Coef('Var'  , 0.231829    ), ], 
		[Coef('Var'  , 0.145307    ), Coef('Var'  , 0.146579    ), Coef('Var'  , 0.145929    ), Coef('Var'  , 0.156355    ), Coef('Var'  , 0.164804    ), Coef('Var'  , 0.170918    ), Coef('Var'  , 0.17551     ), Coef('Var'  , 0.161141    ), ], 
		[Coef('Var'  , 0.0950915   ), Coef('Var'  , 0.104943    ), Coef('Var'  , 0.109402    ), Coef('Var'  , 0.112855    ), Coef('Var'  , 0.110462    ), Coef('Var'  , 0.106189    ), Coef('Var'  , 0.0961313   ), Coef('Var'  , 0.0982772   ), ], 
		[Coef('Var'  , 0.114489    ), Coef('Var'  , 0.126923    ), Coef('Var'  , 0.135892    ), Coef('Var'  , 0.142185    ), Coef('Var'  , 0.145416    ), Coef('Var'  , 0.136689    ), Coef('Var'  , 0.125113    ), Coef('Var'  , 0.121427    ), ], 
		[Coef('Var'  , 0.130605    ), Coef('Var'  , 0.144582    ), Coef('Var'  , 0.157917    ), Coef('Var'  , 0.157586    ), Coef('Var'  , 0.157039    ), Coef('Var'  , 0.14347     ), Coef('Var'  , 0.129214    ), Coef('Var'  , 0.130466    ), ], ])
	etat15.initMat[Chem([Sub('16')])] = FMat([
		[Coef('Var'  , 0.260047    ), Coef('Var'  , 0.243596    ), Coef('Var'  , 0.232217    ), Coef('Var'  , 0.211652    ), Coef('Var'  , 0.196763    ), Coef('Var'  , 0.199431    ), Coef('Var'  , 0.206066    ), Coef('Var'  , 0.231376    ), ], 
		[Coef('Var'  , 0.334686    ), Coef('Var'  , 0.28628     ), Coef('Var'  , 0.241815    ), Coef('Var'  , 0.233622    ), Coef('Var'  , 0.229747    ), Coef('Var'  , 0.274279    ), Coef('Var'  , 0.322333    ), Coef('Var'  , 0.326937    ), ], 
		[Coef('Var'  , 0.19615     ), Coef('Var'  , 0.186301    ), Coef('Var'  , 0.17551     ), Coef('Var'  , 0.182401    ), Coef('Var'  , 0.188046    ), Coef('Var'  , 0.208127    ), Coef('Var'  , 0.227274    ), Coef('Var'  , 0.212026    ), ], 
		[Coef('Var'  , 0.0564118   ), Coef('Var'  , 0.0785489   ), Coef('Var'  , 0.0961313   ), Coef('Var'  , 0.0961333   ), Coef('Var'  , 0.0906169   ), Coef('Var'  , 0.073844    ), Coef('Var'  , 0.052559    ), Coef('Var'  , 0.0562597   ), ], 
		[Coef('Var'  , 0.0758027   ), Coef('Var'  , 0.101679    ), Coef('Var'  , 0.125113    ), Coef('Var'  , 0.137864    ), Coef('Var'  , 0.148241    ), Coef('Var'  , 0.124134    ), Coef('Var'  , 0.0985859   ), Coef('Var'  , 0.0879488   ), ], 
		[Coef('Var'  , 0.0769019   ), Coef('Var'  , 0.103595    ), Coef('Var'  , 0.129214    ), Coef('Var'  , 0.138328    ), Coef('Var'  , 0.146586    ), Coef('Var'  , 0.120186    ), Coef('Var'  , 0.0931826   ), Coef('Var'  , 0.0854525   ), ], ])
	
	
	
	etat16.bords   = {Bord('0'): etat22, Bord('1'): etat19, Bord('2'): etat21, }
	etat16.permuts = {}
	etat16.interns = {Intern('_'): etat16, }
	etat16.subs    = {Sub('0'): etat1, Sub('1'): etat2, Sub('2'): etat3, Sub('3'): etat4, Sub('4'): etat5, Sub('5'): etat6, Sub('6'): etat7, Sub('7'): etat8, Sub('G', True): Etat.etatPoint, Sub('8'): etat9, Sub('9'): etat10, Sub('10'): etat11, Sub('11'): etat12, Sub('12'): etat13, Sub('13'): etat14, Sub('14'): etat15, Sub('15'): etat17, Sub('16'): etat18, }
	
	etat16.buildIntern()
	
	
	etat16.eqs = [
		(Chem([Bord('0'), Sub('3'), Permut('0'), ])	,	Chem([Sub('1'), Bord('4'), ])),
		(Chem([Bord('0'), Sub('0'), Permut('0'), ])	,	Chem([Sub('5'), Bord('0'), ])),
		(Chem([Bord('2'), Sub('3'), Permut('0'), ])	,	Chem([Sub('5'), Bord('1'), ])),
		(Chem([Bord('2'), Sub('1'), Permut('0'), ])	,	Chem([Sub('6'), Bord('1'), ])),
		(Chem([Bord('2'), Sub('2'), Permut('0'), ])	,	Chem([Sub('7'), Bord('1'), ])),
		(Chem([Bord('0'), Sub('2'), Permut('0'), ])	,	Chem([Sub('9'), Bord('2'), ])),
		(Chem([Bord('0'), Sub('1'), Permut('0'), ])	,	Chem([Sub('11'), Bord('1'), ])),
		(Chem([Bord('2'), Sub('0'), Permut('0'), ])	,	Chem([Sub('13'), Bord('0'), ])),
		(Chem([Bord('1'), Sub('1'), Permut('0'), ])	,	Chem([Sub('13'), Bord('1'), ])),
		(Chem([Bord('1'), Sub('0'), Permut('0'), ])	,	Chem([Sub('14'), Bord('1'), ])),
		(Chem([Bord('0'), Sub('4'), Permut('0'), ])	,	Chem([Sub('14'), Bord('2'), ])),
		(Chem([Sub('0'), Bord('0'), Bord('1'), ])	,	Chem([Sub('12'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('1'), Bord('1'), ])	,	Chem([Sub('15'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('2'), Bord('1'), ])	,	Chem([Sub('3'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('3'), Bord('1'), ])	,	Chem([Sub('1'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('0'), Bord('1'), ])	,	Chem([Sub('12'), Bord('4'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('2'), Bord('1'), ])	,	Chem([Sub('3'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('3'), Bord('1'), ])	,	Chem([Sub('14'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('4'), Bord('1'), ])	,	Chem([Sub('9'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('0'), Bord('1'), ])	,	Chem([Sub('12'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('1'), Bord('1'), ])	,	Chem([Sub('10'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('2'), Bord('1'), ])	,	Chem([Sub('7'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('3'), Bord('1'), ])	,	Chem([Sub('16'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('4'), Bord('1'), ])	,	Chem([Sub('15'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('3'), Bord('1'), Bord('1'), ])	,	Chem([Sub('16'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('3'), Bord('2'), Bord('1'), ])	,	Chem([Sub('6'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('4'), Bord('0'), Bord('1'), ])	,	Chem([Sub('8'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('4'), Bord('1'), Bord('1'), ])	,	Chem([Sub('9'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('4'), Bord('2'), Bord('1'), ])	,	Chem([Sub('11'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('4'), Bord('3'), Bord('1'), ])	,	Chem([Sub('10'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('5'), Bord('1'), Bord('1'), ])	,	Chem([Sub('7'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('5'), Bord('2'), Bord('1'), ])	,	Chem([Sub('11'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('6'), Bord('0'), Bord('1'), ])	,	Chem([Sub('7'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('6'), Bord('1'), Bord('1'), ])	,	Chem([Sub('13'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('6'), Bord('3'), Bord('1'), ])	,	Chem([Sub('16'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('8'), Bord('0'), Bord('1'), ])	,	Chem([Sub('10'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('8'), Bord('1'), Bord('1'), ])	,	Chem([Sub('12'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('8'), Bord('2'), Bord('1'), ])	,	Chem([Sub('9'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('9'), Bord('2'), Bord('1'), ])	,	Chem([Sub('11'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('10'), Bord('0'), Bord('1'), ])	,	Chem([Sub('11'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('12'), Bord('2'), Bord('1'), ])	,	Chem([Sub('15'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('13'), Bord('1'), Bord('1'), ])	,	Chem([Sub('14'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('15'), Bord('2'), Bord('1'), ])	,	Chem([Sub('16'), Bord('0'), Bord('1'), ])),
		(Chem([Bord('0'), Bord('1'), ])	,	Chem([Bord('1'), Bord('0'), ])),
		(Chem([Bord('1'), Bord('1'), ])	,	Chem([Bord('2'), Bord('0'), ])),
		(Chem([Bord('2'), Bord('1'), ])	,	Chem([Bord('0'), Bord('0'), ])),
		]
	
	
	etat16.prim.elems = [Figure(2, [Chem([Bord('0'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('0'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('0'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('0'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('1'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('1'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('1'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('1'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('2'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('2'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('2'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('2'), Sub('1'), Sub('1'), Bord('0'), ]), ])]
	etat16.grid.elems = [
		Figure(1, [Chem([Bord('1'), Bord('0'), ]), Chem([Bord('1'), Intern(''), ]), Chem([Bord('1'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('2'), Bord('0'), ]), Chem([Bord('2'), Intern(''), ]), Chem([Bord('2'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('0'), Bord('0'), ]), Chem([Bord('0'), Intern(''), ]), Chem([Bord('0'), Bord('1'), ]), ]), ]
	
	
	etat16.space = [Chem([Bord('2'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('2'), Intern('0'), Intern('0'), ]), ]
	
	etat16.initMat[Chem([Sub('0')])] = FMat([
		[Coef('Var'  , 0.166584    ), Coef('Var'  , 0.176061    ), Coef('Var'  , 0.184876    ), Coef('Var'  , 0.187176    ), Coef('Var'  , 0.189157    ), Coef('Var'  , 0.178265    ), Coef('Var'  , 0.166872    ), Coef('Var'  , 0.167149    ), ], 
		[Coef('Var'  , 0.226516    ), Coef('Var'  , 0.223476    ), Coef('Var'  , 0.222918    ), Coef('Var'  , 0.204006    ), Coef('Var'  , 0.187248    ), Coef('Var'  , 0.186857    ), Coef('Var'  , 0.187968    ), Coef('Var'  , 0.206327    ), ], 
		[Coef('Var'  , 0.249907    ), Coef('Var'  , 0.232007    ), Coef('Var'  , 0.216038    ), Coef('Var'  , 0.203343    ), Coef('Var'  , 0.192303    ), Coef('Var'  , 0.208766    ), Coef('Var'  , 0.226566    ), Coef('Var'  , 0.23743     ), ], 
		[Coef('Var'  , 0.106224    ), Coef('Var'  , 0.116335    ), Coef('Var'  , 0.121402    ), Coef('Var'  , 0.128556    ), Coef('Var'  , 0.130243    ), Coef('Var'  , 0.123632    ), Coef('Var'  , 0.111446    ), Coef('Var'  , 0.111411    ), ], 
		[Coef('Var'  , 0.131117    ), Coef('Var'  , 0.131184    ), Coef('Var'  , 0.130944    ), Coef('Var'  , 0.141312    ), Coef('Var'  , 0.151503    ), Coef('Var'  , 0.154281    ), Coef('Var'  , 0.157544    ), Coef('Var'  , 0.144152    ), ], 
		[Coef('Var'  , 0.119651    ), Coef('Var'  , 0.120937    ), Coef('Var'  , 0.123821    ), Coef('Var'  , 0.135606    ), Coef('Var'  , 0.149546    ), Coef('Var'  , 0.148199    ), Coef('Var'  , 0.149604    ), Coef('Var'  , 0.13353     ), ], ])
	etat16.initMat[Chem([Sub('1')])] = FMat([
		[Coef('Const', 0.16        ), Coef('Var'  , 0.17023     ), Coef('Var'  , 0.180667    ), Coef('Var'  , 0.173745    ), Coef('Var'  , 0.166584    ), Coef('Var'  , 0.148667    ), Coef('Var'  , 0.129945    ), Coef('Var'  , 0.0851516   ), Coef('Const', 0.04        ), Coef('Const', 0.08        ), ], 
		[Coef('Const', 0.48        ), Coef('Var'  , 0.388506    ), Coef('Var'  , 0.298378    ), Coef('Var'  , 0.261181    ), Coef('Var'  , 0.226516    ), Coef('Var'  , 0.217268    ), Coef('Var'  , 0.209675    ), Coef('Var'  , 0.264593    ), Coef('Const', 0.32        ), Coef('Const', 0.44        ), ], 
		[Coef('Const', 0.36        ), Coef('Var'  , 0.306379    ), Coef('Var'  , 0.2536      ), Coef('Var'  , 0.250855    ), Coef('Var'  , 0.249907    ), Coef('Var'  , 0.2811      ), Coef('Var'  , 0.313751    ), Coef('Var'  , 0.476624    ), Coef('Const', 0.64        ), Coef('Const', 0.48        ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.044212    ), Coef('Var'  , 0.0864998   ), Coef('Var'  , 0.0985482   ), Coef('Var'  , 0.106224    ), Coef('Var'  , 0.0938108   ), Coef('Var'  , 0.076998    ), Coef('Var'  , 0.0394746   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0468804   ), Coef('Var'  , 0.0931652   ), Coef('Var'  , 0.112457    ), Coef('Var'  , 0.131117    ), Coef('Var'  , 0.136606    ), Coef('Var'  , 0.142384    ), Coef('Var'  , 0.071029    ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0437931   ), Coef('Var'  , 0.0876897   ), Coef('Var'  , 0.103214    ), Coef('Var'  , 0.119651    ), Coef('Var'  , 0.122548    ), Coef('Var'  , 0.127248    ), Coef('Var'  , 0.0631272   ), Coef('Const', 0           ), Coef('Const', 0           ), ], ])
	etat16.initMat[Chem([Sub('2')])] = FMat([
		[Coef('Var'  , 0.213715    ), Coef('Var'  , 0.218347    ), Coef('Var'  , 0.225478    ), Coef('Var'  , 0.255951    ), Coef('Var'  , 0.290522    ), Coef('Var'  , 0.309418    ), Coef('Var'  , 0.331789    ), Coef('Var'  , 0.282554    ), Coef('Var'  , 0.235088    ), Coef('Var'  , 0.22357     ), ], 
		[Coef('Var'  , 0.168993    ), Coef('Var'  , 0.188407    ), Coef('Var'  , 0.209549    ), Coef('Var'  , 0.208879    ), Coef('Var'  , 0.210861    ), Coef('Var'  , 0.146174    ), Coef('Var'  , 0.0830921   ), Coef('Var'  , 0.103841    ), Coef('Var'  , 0.124716    ), Coef('Var'  , 0.146675    ), ], 
		[Coef('Var'  , 0.153185    ), Coef('Var'  , 0.15714     ), Coef('Var'  , 0.161687    ), Coef('Var'  , 0.141669    ), Coef('Var'  , 0.122416    ), Coef('Var'  , 0.0913229   ), Coef('Var'  , 0.0604548   ), Coef('Var'  , 0.089867    ), Coef('Var'  , 0.11898     ), Coef('Var'  , 0.136122    ), ], 
		[Coef('Var'  , 0.125912    ), Coef('Var'  , 0.124293    ), Coef('Var'  , 0.117323    ), Coef('Var'  , 0.10355     ), Coef('Var'  , 0.0850356   ), Coef('Var'  , 0.0689908   ), Coef('Var'  , 0.0496084   ), Coef('Var'  , 0.0763028   ), Coef('Var'  , 0.099461    ), Coef('Var'  , 0.115236    ), ], 
		[Coef('Var'  , 0.158305    ), Coef('Var'  , 0.147142    ), Coef('Var'  , 0.134766    ), Coef('Var'  , 0.128578    ), Coef('Var'  , 0.11985     ), Coef('Var'  , 0.137612    ), Coef('Var'  , 0.153554    ), Coef('Var'  , 0.165816    ), Coef('Var'  , 0.177986    ), Coef('Var'  , 0.168106    ), ], 
		[Coef('Var'  , 0.179889    ), Coef('Var'  , 0.164671    ), Coef('Var'  , 0.151197    ), Coef('Var'  , 0.161373    ), Coef('Var'  , 0.171314    ), Coef('Var'  , 0.246483    ), Coef('Var'  , 0.321502    ), Coef('Var'  , 0.281619    ), Coef('Var'  , 0.243769    ), Coef('Var'  , 0.21029     ), ], ])
	etat16.initMat[Chem([Sub('3')])] = FMat([
		[Coef('Var'  , 0.129945    ), Coef('Var'  , 0.148786    ), Coef('Var'  , 0.166872    ), Coef('Var'  , 0.172627    ), Coef('Var'  , 0.178062    ), Coef('Var'  , 0.160403    ), Coef('Var'  , 0.142817    ), Coef('Var'  , 0.136562    ), ], 
		[Coef('Var'  , 0.209675    ), Coef('Var'  , 0.198246    ), Coef('Var'  , 0.187968    ), Coef('Var'  , 0.161731    ), Coef('Var'  , 0.1361      ), Coef('Var'  , 0.123017    ), Coef('Var'  , 0.109801    ), Coef('Var'  , 0.159532    ), ], 
		[Coef('Var'  , 0.313751    ), Coef('Var'  , 0.269578    ), Coef('Var'  , 0.226566    ), Coef('Var'  , 0.191727    ), Coef('Var'  , 0.157589    ), Coef('Var'  , 0.150791    ), Coef('Var'  , 0.144057    ), Coef('Var'  , 0.228641    ), ], 
		[Coef('Var'  , 0.076998    ), Coef('Var'  , 0.0965495   ), Coef('Var'  , 0.111446    ), Coef('Var'  , 0.108937    ), Coef('Var'  , 0.101103    ), Coef('Var'  , 0.0867767   ), Coef('Var'  , 0.0679612   ), Coef('Var'  , 0.0743887   ), ], 
		[Coef('Var'  , 0.142384    ), Coef('Var'  , 0.149605    ), Coef('Var'  , 0.157544    ), Coef('Var'  , 0.182839    ), Coef('Var'  , 0.209226    ), Coef('Var'  , 0.246116    ), Coef('Var'  , 0.284279    ), Coef('Var'  , 0.212882    ), ], 
		[Coef('Var'  , 0.127248    ), Coef('Var'  , 0.137236    ), Coef('Var'  , 0.149604    ), Coef('Var'  , 0.182139    ), Coef('Var'  , 0.217921    ), Coef('Var'  , 0.232896    ), Coef('Var'  , 0.251085    ), Coef('Var'  , 0.187993    ), ], ])
	etat16.initMat[Chem([Sub('4')])] = FMat([
		[Coef('Var'  , 0.292312    ), Coef('Var'  , 0.269406    ), Coef('Var'  , 0.253205    ), Coef('Var'  , 0.26508     ), Coef('Var'  , 0.282553    ), Coef('Var'  , 0.299718    ), Coef('Var'  , 0.32166     ), Coef('Var'  , 0.304044    ), ], 
		[Coef('Var'  , 0.305329    ), Coef('Var'  , 0.310735    ), Coef('Var'  , 0.320871    ), Coef('Var'  , 0.345602    ), Coef('Var'  , 0.37459     ), Coef('Var'  , 0.3651      ), Coef('Var'  , 0.359049    ), Coef('Var'  , 0.330234    ), ], 
		[Coef('Var'  , 0.146579    ), Coef('Var'  , 0.159818    ), Coef('Var'  , 0.174374    ), Coef('Var'  , 0.174201    ), Coef('Var'  , 0.175272    ), Coef('Var'  , 0.160882    ), Coef('Var'  , 0.147477    ), Coef('Var'  , 0.146498    ), ], 
		[Coef('Var'  , 0.0755246   ), Coef('Var'  , 0.0783153   ), Coef('Var'  , 0.0764124   ), Coef('Var'  , 0.0661275   ), Coef('Var'  , 0.0518151   ), Coef('Var'  , 0.053029    ), Coef('Var'  , 0.0509273   ), Coef('Var'  , 0.0652167   ), ], 
		[Coef('Var'  , 0.085097    ), Coef('Var'  , 0.0868424   ), Coef('Var'  , 0.0841415   ), Coef('Var'  , 0.0720992   ), Coef('Var'  , 0.0562122   ), Coef('Var'  , 0.0582724   ), Coef('Var'  , 0.0571677   ), Coef('Var'  , 0.0730156   ), ], 
		[Coef('Var'  , 0.0951581   ), Coef('Var'  , 0.0948826   ), Coef('Var'  , 0.0909955   ), Coef('Var'  , 0.0768901   ), Coef('Var'  , 0.0595572   ), Coef('Var'  , 0.0629988   ), Coef('Var'  , 0.0637197   ), Coef('Var'  , 0.0809913   ), ], ])
	etat16.initMat[Chem([Sub('5')])] = FMat([
		[Coef('Const', 0.64        ), Coef('Const', 0.8         ), Coef('Const', 1           ), Coef('Const', 0.75        ), Coef('Const', 0.5625      ), Coef('Var'  , 0.60125     ), ], 
		[Coef('Const', 0.32        ), Coef('Const', 0.2         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.16        ), ], 
		[Coef('Const', 0.04        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.02        ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  ,-2.51171e-17 ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.0625      ), Coef('Var'  , 0.03125     ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Const', 0.375       ), Coef('Var'  , 0.1875      ), ], ])
	etat16.initMat[Chem([Sub('6')])] = FMat([
		[Coef('Var'  , 0.200739    ), Coef('Var'  , 0.225228    ), Coef('Const', 0.25        ), Coef('Const', 0.125       ), Coef('Const', 0.0625      ), Coef('Var'  , 0.10266     ), Coef('Var'  , 0.142817    ), Coef('Var'  , 0.171638    ), ], 
		[Coef('Var'  , 0.093155    ), Coef('Var'  , 0.0467055   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0549389   ), Coef('Var'  , 0.109801    ), Coef('Var'  , 0.101644    ), ], 
		[Coef('Var'  , 0.105517    ), Coef('Var'  , 0.0528523   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0720171   ), Coef('Var'  , 0.144057    ), Coef('Var'  , 0.124869    ), ], 
		[Coef('Var'  , 0.0726301   ), Coef('Var'  , 0.0372821   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0349142   ), Coef('Var'  , 0.0679612   ), Coef('Var'  , 0.0721963   ), ], 
		[Coef('Var'  , 0.228933    ), Coef('Var'  , 0.239185    ), Coef('Const', 0.25        ), Coef('Const', 0.375       ), Coef('Const', 0.5625      ), Coef('Var'  , 0.423103    ), Coef('Var'  , 0.284279    ), Coef('Var'  , 0.256038    ), ], 
		[Coef('Var'  , 0.299027    ), Coef('Var'  , 0.398747    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0.375       ), Coef('Var'  , 0.312366    ), Coef('Var'  , 0.251085    ), Coef('Var'  , 0.273614    ), ], ])
	etat16.initMat[Chem([Sub('7')])] = FMat([
		[Coef('Var'  , 0.331789    ), Coef('Var'  , 0.446648    ), Coef('Const', 0.5625      ), Coef('Const', 0.375       ), Coef('Const', 0.25        ), Coef('Var'  , 0.290398    ), ], 
		[Coef('Var'  , 0.0830921   ), Coef('Var'  , 0.0414346   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0414346   ), ], 
		[Coef('Var'  , 0.0604548   ), Coef('Var'  , 0.030269    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.030269    ), ], 
		[Coef('Var'  , 0.0496084   ), Coef('Var'  , 0.0254006   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0254006   ), ], 
		[Coef('Var'  , 0.153554    ), Coef('Var'  , 0.108193    ), Coef('Const', 0.0625      ), Coef('Const', 0.125       ), Coef('Const', 0.25        ), Coef('Var'  , 0.201943    ), ], 
		[Coef('Var'  , 0.321502    ), Coef('Var'  , 0.348055    ), Coef('Const', 0.375       ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.410555    ), ], ])
	etat16.initMat[Chem([Sub('G')])] = FMat([
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], ])
	etat16.initMat[Chem([Sub('8')])] = FMat([
		[Coef('Var'  , 0.253205    ), Coef('Var'  , 0.250025    ), Coef('Var'  , 0.253409    ), Coef('Var'  , 0.231261    ), Coef('Var'  , 0.214422    ), Coef('Var'  , 0.215784    ), Coef('Var'  , 0.221359    ), Coef('Var'  , 0.234548    ), ], 
		[Coef('Var'  , 0.320871    ), Coef('Var'  , 0.294306    ), Coef('Var'  , 0.272501    ), Coef('Var'  , 0.273667    ), Coef('Var'  , 0.279129    ), Coef('Var'  , 0.316845    ), Coef('Var'  , 0.35843     ), Coef('Var'  , 0.337483    ), ], 
		[Coef('Var'  , 0.174374    ), Coef('Var'  , 0.165702    ), Coef('Var'  , 0.158382    ), Coef('Var'  , 0.177311    ), Coef('Var'  , 0.197627    ), Coef('Var'  , 0.210722    ), Coef('Var'  , 0.225158    ), Coef('Var'  , 0.199113    ), ], 
		[Coef('Var'  , 0.0764124   ), Coef('Var'  , 0.0858629   ), Coef('Var'  , 0.0904317   ), Coef('Var'  , 0.0954947   ), Coef('Var'  , 0.0956879   ), Coef('Var'  , 0.0804498   ), Coef('Var'  , 0.0610792   ), Coef('Var'  , 0.070818    ), ], 
		[Coef('Var'  , 0.0841415   ), Coef('Var'  , 0.0965464   ), Coef('Var'  , 0.104495    ), Coef('Var'  , 0.106196    ), Coef('Var'  , 0.104055    ), Coef('Var'  , 0.0864676   ), Coef('Var'  , 0.065629    ), Coef('Var'  , 0.0768178   ), ], 
		[Coef('Var'  , 0.0909955   ), Coef('Var'  , 0.107558    ), Coef('Var'  , 0.120782    ), Coef('Var'  , 0.11607     ), Coef('Var'  , 0.10908     ), Coef('Var'  , 0.0897319   ), Coef('Var'  , 0.0683449   ), Coef('Var'  , 0.0812197   ), ], ])
	etat16.initMat[Chem([Sub('9')])] = FMat([
		[Coef('Var'  , 0.282553    ), Coef('Var'  , 0.249704    ), Coef('Var'  , 0.221359    ), Coef('Var'  , 0.189586    ), Coef('Const', 0.16        ), Coef('Const', 0.24        ), Coef('Const', 0.36        ), Coef('Var'  , 0.320118    ), ], 
		[Coef('Var'  , 0.37459     ), Coef('Var'  , 0.364665    ), Coef('Var'  , 0.35843     ), Coef('Var'  , 0.418273    ), Coef('Const', 0.48        ), Coef('Const', 0.52        ), Coef('Const', 0.48        ), Coef('Var'  , 0.426392    ), ], 
		[Coef('Var'  , 0.175272    ), Coef('Var'  , 0.199645    ), Coef('Var'  , 0.225158    ), Coef('Var'  , 0.292278    ), Coef('Const', 0.36        ), Coef('Const', 0.24        ), Coef('Const', 0.16        ), Coef('Var'  , 0.167367    ), ], 
		[Coef('Var'  , 0.0518151   ), Coef('Var'  , 0.0581749   ), Coef('Var'  , 0.0610792   ), Coef('Var'  , 0.0314327   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0267422   ), ], 
		[Coef('Var'  , 0.0562122   ), Coef('Var'  , 0.0625328   ), Coef('Var'  , 0.065629    ), Coef('Var'  , 0.0336257   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0289071   ), ], 
		[Coef('Var'  , 0.0595572   ), Coef('Var'  , 0.0652778   ), Coef('Var'  , 0.0683449   ), Coef('Var'  , 0.0348037   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0304741   ), ], ])
	etat16.initMat[Chem([Sub('10')])] = FMat([
		[Coef('Var'  , 0.292312    ), Coef('Var'  , 0.332769    ), Coef('Var'  , 0.379157    ), Coef('Var'  , 0.332344    ), Coef('Var'  , 0.290522    ), Coef('Var'  , 0.269083    ), Coef('Var'  , 0.253409    ), Coef('Var'  , 0.269507    ), ], 
		[Coef('Var'  , 0.305329    ), Coef('Var'  , 0.298072    ), Coef('Var'  , 0.294575    ), Coef('Var'  , 0.251286    ), Coef('Var'  , 0.210861    ), Coef('Var'  , 0.239835    ), Coef('Var'  , 0.272501    ), Coef('Var'  , 0.286622    ), ], 
		[Coef('Var'  , 0.146579    ), Coef('Var'  , 0.129327    ), Coef('Var'  , 0.113053    ), Coef('Var'  , 0.117398    ), Coef('Var'  , 0.122416    ), Coef('Var'  , 0.139921    ), Coef('Var'  , 0.158382    ), Coef('Var'  , 0.151851    ), ], 
		[Coef('Var'  , 0.0755246   ), Coef('Var'  , 0.0686749   ), Coef('Var'  , 0.0577736   ), Coef('Var'  , 0.0733352   ), Coef('Var'  , 0.0850356   ), Coef('Var'  , 0.0900678   ), Coef('Var'  , 0.0904317   ), Coef('Var'  , 0.0854075   ), ], 
		[Coef('Var'  , 0.085097    ), Coef('Var'  , 0.0793317   ), Coef('Var'  , 0.0698314   ), Coef('Var'  , 0.0963505   ), Coef('Var'  , 0.11985     ), Coef('Var'  , 0.114023    ), Coef('Var'  , 0.104495    ), Coef('Var'  , 0.0970046   ), ], 
		[Coef('Var'  , 0.0951581   ), Coef('Var'  , 0.0918253   ), Coef('Var'  , 0.0856093   ), Coef('Var'  , 0.129287    ), Coef('Var'  , 0.171314    ), Coef('Var'  , 0.14707     ), Coef('Var'  , 0.120782    ), Coef('Var'  , 0.109608    ), ], ])
	etat16.initMat[Chem([Sub('11')])] = FMat([
		[Coef('Var'  , 0.32166     ), Coef('Var'  , 0.3396      ), Coef('Const', 0.36        ), Coef('Const', 0.48        ), Coef('Const', 0.64        ), Coef('Var'  , 0.508325    ), Coef('Var'  , 0.379157    ), Coef('Var'  , 0.347925    ), ], 
		[Coef('Var'  , 0.359049    ), Coef('Var'  , 0.418708    ), Coef('Const', 0.48        ), Coef('Const', 0.44        ), Coef('Const', 0.32        ), Coef('Var'  , 0.306546    ), Coef('Var'  , 0.294575    ), Coef('Var'  , 0.325254    ), ], 
		[Coef('Var'  , 0.147477    ), Coef('Var'  , 0.153515    ), Coef('Const', 0.16        ), Coef('Const', 0.08        ), Coef('Const', 0.04        ), Coef('Var'  , 0.076344    ), Coef('Var'  , 0.113053    ), Coef('Var'  , 0.129859    ), ], 
		[Coef('Var'  , 0.0509273   ), Coef('Var'  , 0.0262868   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.029745    ), Coef('Var'  , 0.0577736   ), Coef('Var'  , 0.0560318   ), ], 
		[Coef('Var'  , 0.0571677   ), Coef('Var'  , 0.0293653   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0356814   ), Coef('Var'  , 0.0698314   ), Coef('Var'  , 0.0650467   ), ], 
		[Coef('Var'  , 0.0637197   ), Coef('Var'  , 0.0325247   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0433587   ), Coef('Var'  , 0.0856093   ), Coef('Var'  , 0.0758834   ), ], ])
	etat16.initMat[Chem([Sub('12')])] = FMat([
		[Coef('Var'  , 0.180667    ), Coef('Var'  , 0.196428    ), Coef('Var'  , 0.214422    ), Coef('Var'  , 0.218129    ), Coef('Var'  , 0.225478    ), Coef('Var'  , 0.212614    ), Coef('Var'  , 0.20182     ), Coef('Var'  , 0.193228    ), Coef('Var'  , 0.184876    ), Coef('Var'  , 0.182775    ), ], 
		[Coef('Var'  , 0.298378    ), Coef('Var'  , 0.287077    ), Coef('Var'  , 0.279129    ), Coef('Var'  , 0.24271     ), Coef('Var'  , 0.209549    ), Coef('Var'  , 0.200703    ), Coef('Var'  , 0.194161    ), Coef('Var'  , 0.207365    ), Coef('Var'  , 0.222918    ), Coef('Var'  , 0.259308    ), ], 
		[Coef('Var'  , 0.2536      ), Coef('Var'  , 0.224823    ), Coef('Var'  , 0.197627    ), Coef('Var'  , 0.179059    ), Coef('Var'  , 0.161687    ), Coef('Var'  , 0.169795    ), Coef('Var'  , 0.178995    ), Coef('Var'  , 0.196711    ), Coef('Var'  , 0.216038    ), Coef('Var'  , 0.23391     ), ], 
		[Coef('Var'  , 0.0864998   ), Coef('Var'  , 0.0932291   ), Coef('Var'  , 0.0956879   ), Coef('Var'  , 0.108977    ), Coef('Var'  , 0.117323    ), Coef('Var'  , 0.127334    ), Coef('Var'  , 0.131966    ), Coef('Var'  , 0.129374    ), Coef('Var'  , 0.121402    ), Coef('Var'  , 0.106211    ), ], 
		[Coef('Var'  , 0.0931652   ), Coef('Var'  , 0.0997222   ), Coef('Var'  , 0.104055    ), Coef('Var'  , 0.120751    ), Coef('Var'  , 0.134766    ), Coef('Var'  , 0.140583    ), Coef('Var'  , 0.14497     ), Coef('Var'  , 0.138281    ), Coef('Var'  , 0.130944    ), Coef('Var'  , 0.112488    ), ], 
		[Coef('Var'  , 0.0876897   ), Coef('Var'  , 0.0987213   ), Coef('Var'  , 0.10908     ), Coef('Var'  , 0.130373    ), Coef('Var'  , 0.151197    ), Coef('Var'  , 0.148971    ), Coef('Var'  , 0.148087    ), Coef('Var'  , 0.135041    ), Coef('Var'  , 0.123821    ), Coef('Var'  , 0.105309    ), ], ])
	etat16.initMat[Chem([Sub('13')])] = FMat([
		[Coef('Const', 0.0625      ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.03125     ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  ,-1.43509e-17 ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.125       ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.25        ), ], 
		[Coef('Const', 0.5625      ), Coef('Const', 0.75        ), Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.40625     ), ], 
		[Coef('Const', 0.375       ), Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.1875      ), ], ])
	etat16.initMat[Chem([Sub('14')])] = FMat([
		[Coef('Const', 0.04        ), Coef('Var'  , 0.02        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.32        ), Coef('Var'  , 0.16        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.2         ), ], 
		[Coef('Const', 0.64        ), Coef('Var'  , 0.445       ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.8         ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.25        ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.125       ), Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  ,-6.20131e-18 ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], ])
	etat16.initMat[Chem([Sub('15')])] = FMat([
		[Coef('Var'  , 0.189157    ), Coef('Var'  , 0.195313    ), Coef('Var'  , 0.20182     ), Coef('Var'  , 0.207098    ), Coef('Var'  , 0.213715    ), Coef('Var'  , 0.207571    ), Coef('Var'  , 0.202743    ), Coef('Var'  , 0.195787    ), ], 
		[Coef('Var'  , 0.187248    ), Coef('Var'  , 0.189768    ), Coef('Var'  , 0.194161    ), Coef('Var'  , 0.180832    ), Coef('Var'  , 0.168993    ), Coef('Var'  , 0.16106     ), Coef('Var'  , 0.153695    ), Coef('Var'  , 0.169996    ), ], 
		[Coef('Var'  , 0.192303    ), Coef('Var'  , 0.184992    ), Coef('Var'  , 0.178995    ), Coef('Var'  , 0.165704    ), Coef('Var'  , 0.153185    ), Coef('Var'  , 0.154113    ), Coef('Var'  , 0.155222    ), Coef('Var'  , 0.1734      ), ], 
		[Coef('Var'  , 0.130243    ), Coef('Var'  , 0.133932    ), Coef('Var'  , 0.131966    ), Coef('Var'  , 0.131709    ), Coef('Var'  , 0.125912    ), Coef('Var'  , 0.126975    ), Coef('Var'  , 0.122443    ), Coef('Var'  , 0.129199    ), ], 
		[Coef('Var'  , 0.151503    ), Coef('Var'  , 0.148378    ), Coef('Var'  , 0.14497     ), Coef('Var'  , 0.151906    ), Coef('Var'  , 0.158305    ), Coef('Var'  , 0.165714    ), Coef('Var'  , 0.173339    ), Coef('Var'  , 0.162186    ), ], 
		[Coef('Var'  , 0.149546    ), Coef('Var'  , 0.147616    ), Coef('Var'  , 0.148087    ), Coef('Var'  , 0.162752    ), Coef('Var'  , 0.179889    ), Coef('Var'  , 0.184567    ), Coef('Var'  , 0.192557    ), Coef('Var'  , 0.169432    ), ], ])
	etat16.initMat[Chem([Sub('16')])] = FMat([
		[Coef('Var'  , 0.178062    ), Coef('Var'  , 0.190149    ), Coef('Var'  , 0.202743    ), Coef('Var'  , 0.218311    ), Coef('Var'  , 0.235088    ), Coef('Var'  , 0.217383    ), Coef('Var'  , 0.200739    ), Coef('Var'  , 0.189221    ), ], 
		[Coef('Var'  , 0.1361      ), Coef('Var'  , 0.14487     ), Coef('Var'  , 0.153695    ), Coef('Var'  , 0.139199    ), Coef('Var'  , 0.124716    ), Coef('Var'  , 0.109112    ), Coef('Var'  , 0.093155    ), Coef('Var'  , 0.114783    ), ], 
		[Coef('Var'  , 0.157589    ), Coef('Var'  , 0.156362    ), Coef('Var'  , 0.155222    ), Coef('Var'  , 0.137186    ), Coef('Var'  , 0.11898     ), Coef('Var'  , 0.11245     ), Coef('Var'  , 0.105517    ), Coef('Var'  , 0.131626    ), ], 
		[Coef('Var'  , 0.101103    ), Coef('Var'  , 0.114504    ), Coef('Var'  , 0.122443    ), Coef('Var'  , 0.113544    ), Coef('Var'  , 0.099461    ), Coef('Var'  , 0.0881843   ), Coef('Var'  , 0.0726301   ), Coef('Var'  , 0.0891445   ), ], 
		[Coef('Var'  , 0.209226    ), Coef('Var'  , 0.190745    ), Coef('Var'  , 0.173339    ), Coef('Var'  , 0.175355    ), Coef('Var'  , 0.177986    ), Coef('Var'  , 0.203058    ), Coef('Var'  , 0.228933    ), Coef('Var'  , 0.218448    ), ], 
		[Coef('Var'  , 0.217921    ), Coef('Var'  , 0.203371    ), Coef('Var'  , 0.192557    ), Coef('Var'  , 0.216406    ), Coef('Var'  , 0.243769    ), Coef('Var'  , 0.269812    ), Coef('Var'  , 0.299027    ), Coef('Var'  , 0.256777    ), ], ])
	
	
	
	etat17.bords   = {Bord('0'): etat19, Bord('1'): etat19, Bord('2'): etat19, Bord('3'): etat20, }
	etat17.permuts = {}
	etat17.interns = {Intern('_'): etat17, }
	etat17.subs    = {Sub('0'): etat1, Sub('1'): etat2, Sub('2'): etat3, Sub('3'): etat4, Sub('4'): etat5, Sub('5'): etat6, Sub('6'): etat7, Sub('7'): etat8, Sub('G', True): Etat.etatPoint, Sub('8'): etat9, Sub('9'): etat10, Sub('10'): etat11, Sub('11'): etat12, Sub('12'): etat13, Sub('13'): etat14, Sub('14'): etat15, Sub('15'): etat16, Sub('16'): etat18, }
	
	etat17.buildIntern()
	
	
	etat17.eqs = [
		(Chem([Bord('0'), Sub('0'), Permut('0'), ])	,	Chem([Sub('0'), Bord('1'), ])),
		(Chem([Bord('3'), Sub('2'), Permut('0'), ])	,	Chem([Sub('0'), Bord('2'), ])),
		(Chem([Bord('1'), Sub('1'), Permut('0'), ])	,	Chem([Sub('2'), Bord('0'), ])),
		(Chem([Bord('2'), Sub('0'), Permut('0'), ])	,	Chem([Sub('2'), Bord('4'), ])),
		(Chem([Bord('3'), Sub('1'), Permut('0'), ])	,	Chem([Sub('3'), Bord('1'), ])),
		(Chem([Bord('1'), Sub('0'), Permut('0'), ])	,	Chem([Sub('12'), Bord('2'), ])),
		(Chem([Bord('0'), Sub('1'), Permut('0'), ])	,	Chem([Sub('12'), Bord('3'), ])),
		(Chem([Bord('3'), Sub('0'), Permut('0'), ])	,	Chem([Sub('16'), Bord('0'), ])),
		(Chem([Bord('2'), Sub('1'), Permut('0'), ])	,	Chem([Sub('16'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('0'), Bord('1'), ])	,	Chem([Sub('12'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('2'), Bord('1'), ])	,	Chem([Sub('3'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('3'), Bord('1'), ])	,	Chem([Sub('1'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('0'), Bord('1'), ])	,	Chem([Sub('12'), Bord('4'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('2'), Bord('1'), ])	,	Chem([Sub('3'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('3'), Bord('1'), ])	,	Chem([Sub('14'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('4'), Bord('1'), ])	,	Chem([Sub('9'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('0'), Bord('1'), ])	,	Chem([Sub('12'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('1'), Bord('1'), ])	,	Chem([Sub('10'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('2'), Bord('1'), ])	,	Chem([Sub('7'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('3'), Bord('1'), ])	,	Chem([Sub('16'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('3'), Bord('1'), Bord('1'), ])	,	Chem([Sub('16'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('3'), Bord('2'), Bord('1'), ])	,	Chem([Sub('6'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('4'), Bord('0'), Bord('1'), ])	,	Chem([Sub('8'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('4'), Bord('1'), Bord('1'), ])	,	Chem([Sub('9'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('4'), Bord('2'), Bord('1'), ])	,	Chem([Sub('11'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('4'), Bord('3'), Bord('1'), ])	,	Chem([Sub('10'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('5'), Bord('0'), Bord('1'), ])	,	Chem([Sub('15'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('5'), Bord('1'), Bord('1'), ])	,	Chem([Sub('7'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('5'), Bord('2'), Bord('1'), ])	,	Chem([Sub('11'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('6'), Bord('0'), Bord('1'), ])	,	Chem([Sub('7'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('6'), Bord('1'), Bord('1'), ])	,	Chem([Sub('13'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('6'), Bord('3'), Bord('1'), ])	,	Chem([Sub('16'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('8'), Bord('0'), Bord('1'), ])	,	Chem([Sub('10'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('8'), Bord('1'), Bord('1'), ])	,	Chem([Sub('12'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('8'), Bord('2'), Bord('1'), ])	,	Chem([Sub('9'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('9'), Bord('2'), Bord('1'), ])	,	Chem([Sub('11'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('10'), Bord('0'), Bord('1'), ])	,	Chem([Sub('11'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('13'), Bord('0'), Bord('1'), ])	,	Chem([Sub('15'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('13'), Bord('1'), Bord('1'), ])	,	Chem([Sub('14'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('14'), Bord('1'), Bord('1'), ])	,	Chem([Sub('15'), Bord('0'), Bord('1'), ])),
		(Chem([Bord('0'), Bord('1'), ])	,	Chem([Bord('1'), Bord('0'), ])),
		(Chem([Bord('1'), Bord('1'), ])	,	Chem([Bord('2'), Bord('0'), ])),
		(Chem([Bord('2'), Bord('1'), ])	,	Chem([Bord('3'), Bord('0'), ])),
		(Chem([Bord('3'), Bord('1'), ])	,	Chem([Bord('0'), Bord('0'), ])),
		]
	
	
	etat17.prim.elems = [Figure(2, [Chem([Bord('0'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('0'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('0'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('0'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('1'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('1'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('1'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('1'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('2'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('2'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('2'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('2'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('3'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('3'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('3'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('3'), Sub('1'), Sub('1'), Bord('0'), ]), ])]
	etat17.grid.elems = [
		Figure(1, [Chem([Bord('1'), Bord('0'), ]), Chem([Bord('1'), Intern(''), ]), Chem([Bord('1'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('2'), Bord('0'), ]), Chem([Bord('2'), Intern(''), ]), Chem([Bord('2'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('0'), Bord('0'), ]), Chem([Bord('0'), Intern(''), ]), Chem([Bord('0'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('3'), Bord('0'), ]), Chem([Bord('3'), Intern(''), ]), Chem([Bord('3'), Bord('1'), ]), ]), ]
	
	
	etat17.space = [Chem([Bord('0'), Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('2'), Intern('0'), Intern('0'), ]), Chem([Bord('2'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('3'), Intern('0'), Intern('0'), ]), ]
	
	etat17.initMat[Chem([Sub('0')])] = FMat([
		[Coef('Var'  , 0.273913    ), Coef('Var'  , 0.261741    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.666667    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.358963    ), ], 
		[Coef('Var'  , 0.226775    ), Coef('Var'  , 0.363419    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.113419    ), ], 
		[Coef('Var'  , 0.126694    ), Coef('Var'  , 0.188366    ), Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0633657   ), ], 
		[Coef('Var'  , 0.0371609   ), Coef('Var'  , 0.0186117   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0186117   ), ], 
		[Coef('Var'  , 0.0266547   ), Coef('Var'  , 0.0134699   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.01347     ), ], 
		[Coef('Var'  , 0.0234699   ), Coef('Var'  , 0.0118868   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0118869   ), ], 
		[Coef('Var'  , 0.0842641   ), Coef('Var'  , 0.0421146   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.111111    ), Coef('Var'  , 0.0976702   ), ], 
		[Coef('Var'  , 0.201068    ), Coef('Var'  , 0.100392    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.333333    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.322614    ), ], ])
	etat17.initMat[Chem([Sub('1')])] = FMat([
		[Coef('Var'  , 0.0870061   ), Coef('Var'  , 0.119759    ), Coef('Var'  , 0.153492    ), Coef('Var'  , 0.212775    ), Coef('Var'  , 0.273913    ), Coef('Var'  , 0.26299     ), Coef('Var'  , 0.252516    ), Coef('Var'  , 0.201682    ), Coef('Var'  , 0.150333    ), Coef('Var'  , 0.119158    ), ], 
		[Coef('Var'  , 0.232888    ), Coef('Var'  , 0.265653    ), Coef('Var'  , 0.298153    ), Coef('Var'  , 0.263079    ), Coef('Var'  , 0.226775    ), Coef('Var'  , 0.16696     ), Coef('Var'  , 0.107474    ), Coef('Var'  , 0.125844    ), Coef('Var'  , 0.145606    ), Coef('Var'  , 0.188296    ), ], 
		[Coef('Var'  , 0.15507     ), Coef('Var'  , 0.168623    ), Coef('Var'  , 0.182642    ), Coef('Var'  , 0.154676    ), Coef('Var'  , 0.126694    ), Coef('Var'  , 0.100285    ), Coef('Var'  , 0.0736089   ), Coef('Var'  , 0.0938271   ), Coef('Var'  , 0.113659    ), Coef('Var'  , 0.134221    ), ], 
		[Coef('Var'  , 0.128642    ), Coef('Var'  , 0.115198    ), Coef('Var'  , 0.102827    ), Coef('Var'  , 0.0698921   ), Coef('Var'  , 0.0371609   ), Coef('Var'  , 0.0414281   ), Coef('Var'  , 0.0452619   ), Coef('Var'  , 0.0714363   ), Coef('Var'  , 0.0968674   ), Coef('Var'  , 0.112538    ), ], 
		[Coef('Var'  , 0.0843746   ), Coef('Var'  , 0.0714132   ), Coef('Var'  , 0.0578429   ), Coef('Var'  , 0.0423632   ), Coef('Var'  , 0.0266547   ), Coef('Var'  , 0.0368565   ), Coef('Var'  , 0.0461999   ), Coef('Var'  , 0.0673059   ), Coef('Var'  , 0.0868926   ), Coef('Var'  , 0.0864393   ), ], 
		[Coef('Var'  , 0.0768288   ), Coef('Var'  , 0.0575104   ), Coef('Var'  , 0.0369097   ), Coef('Var'  , 0.0305091   ), Coef('Var'  , 0.0234699   ), Coef('Var'  , 0.0390747   ), Coef('Var'  , 0.053978    ), Coef('Var'  , 0.0745048   ), Coef('Var'  , 0.0939188   ), Coef('Var'  , 0.0862051   ), ], 
		[Coef('Var'  , 0.126658    ), Coef('Var'  , 0.103014    ), Coef('Var'  , 0.0787458   ), Coef('Var'  , 0.0818139   ), Coef('Var'  , 0.0842641   ), Coef('Var'  , 0.115511    ), Coef('Var'  , 0.147496    ), Coef('Var'  , 0.141737    ), Coef('Var'  , 0.137931    ), Coef('Var'  , 0.131656    ), ], 
		[Coef('Var'  , 0.108533    ), Coef('Var'  , 0.0988287   ), Coef('Var'  , 0.0893877   ), Coef('Var'  , 0.144892    ), Coef('Var'  , 0.201068    ), Coef('Var'  , 0.236896    ), Coef('Var'  , 0.273465    ), Coef('Var'  , 0.223663    ), Coef('Var'  , 0.174792    ), Coef('Var'  , 0.141486    ), ], ])
	etat17.initMat[Chem([Sub('2')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  ,-0.0103486   ), Coef('Var'  ,-0.0161928   ), Coef('Var'  , 0.00367193  ), Coef('Var'  , 0.0289194   ), Coef('Var'  , 0.0140205   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0852285   ), Coef('Var'  , 0.164457    ), Coef('Var'  , 0.137205    ), Coef('Var'  , 0.101879    ), Coef('Var'  , 0.0519762   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.213068    ), Coef('Var'  , 0.175217    ), Coef('Var'  , 0.135799    ), Coef('Var'  , 0.0947069   ), Coef('Var'  , 0.0477312   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.376691    ), Coef('Var'  , 0.2534      ), Coef('Var'  , 0.18425     ), Coef('Var'  , 0.114919    ), Coef('Var'  , 0.0575597   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.198691    ), Coef('Var'  , 0.149555    ), Coef('Var'  , 0.153967    ), Coef('Var'  , 0.161293    ), Coef('Var'  , 0.205276    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0486991   ), Coef('Var'  , 0.0984624   ), Coef('Var'  , 0.165779    ), Coef('Var'  , 0.234861    ), Coef('Var'  , 0.36708     ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0643738   ), Coef('Var'  , 0.126893    ), Coef('Var'  , 0.158113    ), Coef('Var'  , 0.187647    ), Coef('Var'  , 0.21874     ), Coef('Const', 0.25        ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0235973   ), Coef('Var'  , 0.048209    ), Coef('Var'  , 0.0612141   ), Coef('Var'  , 0.0757745   ), Coef('Var'  , 0.0376168   ), Coef('Const', 0           ), Coef('Const', 0           ), ], ])
	etat17.initMat[Chem([Sub('3')])] = FMat([
		[Coef('Var'  , 0.252516    ), Coef('Var'  , 0.348471    ), Coef('Const', 0.444444    ), Coef('Const', 0.222222    ), Coef('Const', 0.111111    ), Coef('Var'  , 0.12622     ), Coef('Var'  , 0.14125     ), Coef('Var'  , 0.196913    ), ], 
		[Coef('Var'  , 0.107474    ), Coef('Var'  , 0.0535408   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0306912   ), Coef('Var'  , 0.0613995   ), Coef('Var'  , 0.0842319   ), ], 
		[Coef('Var'  , 0.0736089   ), Coef('Var'  , 0.036919    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0260586   ), Coef('Var'  , 0.0515658   ), Coef('Var'  , 0.0629775   ), ], 
		[Coef('Var'  , 0.0452619   ), Coef('Var'  , 0.0228165   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0218917   ), Coef('Var'  , 0.0432073   ), Coef('Var'  , 0.044708    ), ], 
		[Coef('Var'  , 0.0461999   ), Coef('Var'  , 0.0233866   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0328443   ), Coef('Var'  , 0.0653592   ), Coef('Var'  , 0.0562308   ), ], 
		[Coef('Var'  , 0.053978    ), Coef('Var'  , 0.027188    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0472493   ), Coef('Var'  , 0.0944351   ), Coef('Var'  , 0.0744371   ), ], 
		[Coef('Var'  , 0.147496    ), Coef('Var'  , 0.128952    ), Coef('Const', 0.111111    ), Coef('Const', 0.222222    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.353931    ), Coef('Var'  , 0.264431    ), Coef('Var'  , 0.205105    ), ], 
		[Coef('Var'  , 0.273465    ), Coef('Var'  , 0.358727    ), Coef('Const', 0.444444    ), Coef('Const', 0.555556    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.361115    ), Coef('Var'  , 0.278352    ), Coef('Var'  , 0.275397    ), ], ])
	etat17.initMat[Chem([Sub('4')])] = FMat([
		[Coef('Var'  ,-0.0381447   ), Coef('Var'  ,-0.0419353   ), Coef('Var'  ,-0.0338544   ), Coef('Var'  ,-0.0221932   ), Coef('Var'  ,-0.00363226  ), Coef('Var'  ,-0.00663683  ), Coef('Var'  ,-0.00792259  ), Coef('Var'  ,-0.026379    ), ], 
		[Coef('Var'  , 0.27997     ), Coef('Var'  , 0.290662    ), Coef('Var'  , 0.286587    ), Coef('Var'  , 0.279994    ), Coef('Var'  , 0.264797    ), Coef('Var'  , 0.262965    ), Coef('Var'  , 0.25818     ), Coef('Var'  , 0.273633    ), ], 
		[Coef('Var'  , 0.173419    ), Coef('Var'  , 0.175242    ), Coef('Var'  , 0.175765    ), Coef('Var'  , 0.170996    ), Coef('Var'  , 0.166023    ), Coef('Var'  , 0.164532    ), Coef('Var'  , 0.163677    ), Coef('Var'  , 0.168778    ), ], 
		[Coef('Var'  , 0.184826    ), Coef('Var'  , 0.18335     ), Coef('Var'  , 0.183444    ), Coef('Var'  , 0.172522    ), Coef('Var'  , 0.163938    ), Coef('Var'  , 0.163151    ), Coef('Var'  , 0.16532     ), Coef('Var'  , 0.173979    ), ], 
		[Coef('Var'  , 0.0895417   ), Coef('Var'  , 0.0854706   ), Coef('Var'  , 0.0867623   ), Coef('Var'  , 0.0865361   ), Coef('Var'  , 0.089444    ), Coef('Var'  , 0.090134    ), Coef('Var'  , 0.0922233   ), Coef('Var'  , 0.0890685   ), ], 
		[Coef('Var'  , 0.0818426   ), Coef('Var'  , 0.0781283   ), Coef('Var'  , 0.0758422   ), Coef('Var'  , 0.0801764   ), Coef('Var'  , 0.0845679   ), Coef('Var'  , 0.0879658   ), Coef('Var'  , 0.0905684   ), Coef('Var'  , 0.0859177   ), ], 
		[Coef('Var'  , 0.163043    ), Coef('Var'  , 0.164345    ), Coef('Var'  , 0.159583    ), Coef('Var'  , 0.15986     ), Coef('Var'  , 0.155859    ), Coef('Var'  , 0.158741    ), Coef('Var'  , 0.159319    ), Coef('Var'  , 0.163226    ), ], 
		[Coef('Var'  , 0.0655022   ), Coef('Var'  , 0.0647373   ), Coef('Var'  , 0.0658705   ), Coef('Var'  , 0.0721084   ), Coef('Var'  , 0.0790033   ), Coef('Var'  , 0.0791478   ), Coef('Var'  , 0.0786351   ), Coef('Var'  , 0.0717768   ), ], ])
	etat17.initMat[Chem([Sub('5')])] = FMat([
		[Coef('Var'  , 0.0506835   ), Coef('Var'  , 0.0747139   ), Coef('Var'  , 0.095099    ), Coef('Var'  , 0.0821495   ), Coef('Var'  , 0.0659942   ), Coef('Var'  , 0.0600392   ), ], 
		[Coef('Var'  , 0.180254    ), Coef('Var'  , 0.157548    ), Coef('Var'  , 0.136957    ), Coef('Var'  , 0.131631    ), Coef('Var'  , 0.127692    ), Coef('Var'  , 0.153261    ), ], 
		[Coef('Var'  , 0.136634    ), Coef('Var'  , 0.127994    ), Coef('Var'  , 0.119082    ), Coef('Var'  , 0.115141    ), Coef('Var'  , 0.110356    ), Coef('Var'  , 0.123701    ), ], 
		[Coef('Var'  , 0.138353    ), Coef('Var'  , 0.127685    ), Coef('Var'  , 0.11747     ), Coef('Var'  , 0.116429    ), Coef('Var'  , 0.115109    ), Coef('Var'  , 0.126397    ), ], 
		[Coef('Var'  , 0.111243    ), Coef('Var'  , 0.113213    ), Coef('Var'  , 0.114408    ), Coef('Var'  , 0.121622    ), Coef('Var'  , 0.128197    ), Coef('Var'  , 0.119891    ), ], 
		[Coef('Var'  , 0.124468    ), Coef('Var'  , 0.129694    ), Coef('Var'  , 0.134643    ), Coef('Var'  , 0.151096    ), Coef('Var'  , 0.167765    ), Coef('Var'  , 0.146055    ), ], 
		[Coef('Var'  , 0.153935    ), Coef('Var'  , 0.150513    ), Coef('Var'  , 0.149706    ), Coef('Var'  , 0.158603    ), Coef('Var'  , 0.170567    ), Coef('Var'  , 0.161145    ), ], 
		[Coef('Var'  , 0.104431    ), Coef('Var'  , 0.118639    ), Coef('Var'  , 0.132636    ), Coef('Var'  , 0.123329    ), Coef('Var'  , 0.114321    ), Coef('Var'  , 0.109512    ), ], ])
	etat17.initMat[Chem([Sub('6')])] = FMat([
		[Coef('Var'  , 0.082449    ), Coef('Var'  , 0.0791299   ), Coef('Var'  , 0.0750356   ), Coef('Var'  , 0.0967765   ), Coef('Var'  , 0.117619    ), Coef('Var'  , 0.129654    ), Coef('Var'  , 0.14125     ), Coef('Var'  , 0.112007    ), ], 
		[Coef('Var'  , 0.0390133   ), Coef('Var'  , 0.0664932   ), Coef('Var'  , 0.0934216   ), Coef('Var'  , 0.0967401   ), Coef('Var'  , 0.0995331   ), Coef('Var'  , 0.0804931   ), Coef('Var'  , 0.0613995   ), Coef('Var'  , 0.0502463   ), ], 
		[Coef('Var'  , 0.0354633   ), Coef('Var'  , 0.0610067   ), Coef('Var'  , 0.0852365   ), Coef('Var'  , 0.08918     ), Coef('Var'  , 0.091436    ), Coef('Var'  , 0.0722048   ), Coef('Var'  , 0.0515658   ), Coef('Var'  , 0.0440314   ), ], 
		[Coef('Var'  , 0.0340521   ), Coef('Var'  , 0.0620368   ), Coef('Var'  , 0.0891844   ), Coef('Var'  , 0.0890324   ), Coef('Var'  , 0.0875066   ), Coef('Var'  , 0.066095    ), Coef('Var'  , 0.0432073   ), Coef('Var'  , 0.0390994   ), ], 
		[Coef('Var'  , 0.1104      ), Coef('Var'  , 0.117816    ), Coef('Var'  , 0.125167    ), Coef('Var'  , 0.11337     ), Coef('Var'  , 0.101221    ), Coef('Var'  , 0.0836499   ), Coef('Var'  , 0.0653592   ), Coef('Var'  , 0.0880957   ), ], 
		[Coef('Var'  , 0.19332     ), Coef('Var'  , 0.186515    ), Coef('Var'  , 0.180291    ), Coef('Var'  , 0.154769    ), Coef('Var'  , 0.129713    ), Coef('Var'  , 0.112093    ), Coef('Var'  , 0.0944351   ), Coef('Var'  , 0.143838    ), ], 
		[Coef('Var'  , 0.288978    ), Coef('Var'  , 0.246094    ), Coef('Var'  , 0.205277    ), Coef('Var'  , 0.195051    ), Coef('Var'  , 0.18786     ), Coef('Var'  , 0.224766    ), Coef('Var'  , 0.264431    ), Coef('Var'  , 0.275809    ), ], 
		[Coef('Var'  , 0.216324    ), Coef('Var'  , 0.180909    ), Coef('Var'  , 0.146388    ), Coef('Var'  , 0.165081    ), Coef('Var'  , 0.185112    ), Coef('Var'  , 0.231045    ), Coef('Var'  , 0.278352    ), Coef('Var'  , 0.246873    ), ], ])
	etat17.initMat[Chem([Sub('7')])] = FMat([
		[Coef('Var'  , 0.0289194   ), Coef('Var'  , 0.047758    ), Coef('Var'  , 0.0659942   ), Coef('Var'  , 0.071524    ), Coef('Var'  , 0.0750356   ), Coef('Var'  , 0.0518071   ), ], 
		[Coef('Var'  , 0.101879    ), Coef('Var'  , 0.115648    ), Coef('Var'  , 0.127692    ), Coef('Var'  , 0.11061     ), Coef('Var'  , 0.0934216   ), Coef('Var'  , 0.0989143   ), ], 
		[Coef('Var'  , 0.0947069   ), Coef('Var'  , 0.103155    ), Coef('Var'  , 0.110356    ), Coef('Var'  , 0.0984581   ), Coef('Var'  , 0.0852365   ), Coef('Var'  , 0.090765    ), ], 
		[Coef('Var'  , 0.114919    ), Coef('Var'  , 0.11513     ), Coef('Var'  , 0.115109    ), Coef('Var'  , 0.1024      ), Coef('Var'  , 0.0891844   ), Coef('Var'  , 0.102389    ), ], 
		[Coef('Var'  , 0.161293    ), Coef('Var'  , 0.144426    ), Coef('Var'  , 0.128197    ), Coef('Var'  , 0.126715    ), Coef('Var'  , 0.125167    ), Coef('Var'  , 0.142841    ), ], 
		[Coef('Var'  , 0.234861    ), Coef('Var'  , 0.200808    ), Coef('Var'  , 0.167765    ), Coef('Var'  , 0.173654    ), Coef('Var'  , 0.180291    ), Coef('Var'  , 0.207006    ), ], 
		[Coef('Var'  , 0.187647    ), Coef('Var'  , 0.178357    ), Coef('Var'  , 0.170567    ), Coef('Var'  , 0.186611    ), Coef('Var'  , 0.205277    ), Coef('Var'  , 0.195733    ), ], 
		[Coef('Var'  , 0.0757745   ), Coef('Var'  , 0.0947177   ), Coef('Var'  , 0.114321    ), Coef('Var'  , 0.13003     ), Coef('Var'  , 0.146388    ), Coef('Var'  , 0.110546    ), ], ])
	etat17.initMat[Chem([Sub('G')])] = FMat([
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], ])
	etat17.initMat[Chem([Sub('8')])] = FMat([
		[Coef('Var'  ,-0.0338544   ), Coef('Var'  ,-0.0432061   ), Coef('Var'  ,-0.0382232   ), Coef('Var'  ,-0.0162375   ), Coef('Var'  , 0.018837    ), Coef('Var'  , 0.00983348  ), Coef('Var'  , 0.00848799  ), Coef('Var'  ,-0.0171351   ), ], 
		[Coef('Var'  , 0.286587    ), Coef('Var'  , 0.283501    ), Coef('Var'  , 0.263037    ), Coef('Var'  , 0.248829    ), Coef('Var'  , 0.219164    ), Coef('Var'  , 0.244195    ), Coef('Var'  , 0.260638    ), Coef('Var'  , 0.278867    ), ], 
		[Coef('Var'  , 0.175765    ), Coef('Var'  , 0.180654    ), Coef('Var'  , 0.183736    ), Coef('Var'  , 0.19214     ), Coef('Var'  , 0.198816    ), Coef('Var'  , 0.18663     ), Coef('Var'  , 0.173964    ), Coef('Var'  , 0.175144    ), ], 
		[Coef('Var'  , 0.183444    ), Coef('Var'  , 0.199588    ), Coef('Var'  , 0.216701    ), Coef('Var'  , 0.232452    ), Coef('Var'  , 0.248592    ), Coef('Var'  , 0.21285     ), Coef('Var'  , 0.178354    ), Coef('Var'  , 0.179986    ), ], 
		[Coef('Var'  , 0.0867623   ), Coef('Var'  , 0.0918467   ), Coef('Var'  , 0.102997    ), Coef('Var'  , 0.109747    ), Coef('Var'  , 0.121634    ), Coef('Var'  , 0.105799    ), Coef('Var'  , 0.0925639   ), Coef('Var'  , 0.0878984   ), ], 
		[Coef('Var'  , 0.0758422   ), Coef('Var'  , 0.0728573   ), Coef('Var'  , 0.0718166   ), Coef('Var'  , 0.0570197   ), Coef('Var'  , 0.0439861   ), Coef('Var'  , 0.057375    ), Coef('Var'  , 0.0709041   ), Coef('Var'  , 0.0732126   ), ], 
		[Coef('Var'  , 0.159583    ), Coef('Var'  , 0.156284    ), Coef('Var'  , 0.146171    ), Coef('Var'  , 0.124488    ), Coef('Var'  , 0.0968798   ), Coef('Var'  , 0.120341    ), Coef('Var'  , 0.139844    ), Coef('Var'  , 0.152138    ), ], 
		[Coef('Var'  , 0.0658705   ), Coef('Var'  , 0.0584758   ), Coef('Var'  , 0.0537652   ), Coef('Var'  , 0.0515626   ), Coef('Var'  , 0.052092    ), Coef('Var'  , 0.0629769   ), Coef('Var'  , 0.0752442   ), Coef('Var'  , 0.0698901   ), ], ])
	etat17.initMat[Chem([Sub('9')])] = FMat([
		[Coef('Var'  ,-0.00363226  ), Coef('Var'  , 0.000514141 ), Coef('Var'  , 0.00848799  ), Coef('Var'  , 0.0465112   ), Coef('Var'  , 0.0870061   ), Coef('Var'  , 0.0623319   ), Coef('Var'  , 0.0351511   ), Coef('Var'  , 0.0163349   ), ], 
		[Coef('Var'  , 0.264797    ), Coef('Var'  , 0.265018    ), Coef('Var'  , 0.260638    ), Coef('Var'  , 0.247938    ), Coef('Var'  , 0.232888    ), Coef('Var'  , 0.230573    ), Coef('Var'  , 0.231124    ), Coef('Var'  , 0.247653    ), ], 
		[Coef('Var'  , 0.166023    ), Coef('Var'  , 0.169789    ), Coef('Var'  , 0.173964    ), Coef('Var'  , 0.164282    ), Coef('Var'  , 0.15507     ), Coef('Var'  , 0.153835    ), Coef('Var'  , 0.153767    ), Coef('Var'  , 0.159342    ), ], 
		[Coef('Var'  , 0.163938    ), Coef('Var'  , 0.169886    ), Coef('Var'  , 0.178354    ), Coef('Var'  , 0.152593    ), Coef('Var'  , 0.128642    ), Coef('Var'  , 0.135705    ), Coef('Var'  , 0.145077    ), Coef('Var'  , 0.152998    ), ], 
		[Coef('Var'  , 0.089444    ), Coef('Var'  , 0.0902301   ), Coef('Var'  , 0.0925639   ), Coef('Var'  , 0.0883161   ), Coef('Var'  , 0.0843746   ), Coef('Var'  , 0.0903783   ), Coef('Var'  , 0.0951265   ), Coef('Var'  , 0.0922923   ), ], 
		[Coef('Var'  , 0.0845679   ), Coef('Var'  , 0.0781314   ), Coef('Var'  , 0.0709041   ), Coef('Var'  , 0.074472    ), Coef('Var'  , 0.0768288   ), Coef('Var'  , 0.0875029   ), Coef('Var'  , 0.0962973   ), Coef('Var'  , 0.0911623   ), ], 
		[Coef('Var'  , 0.155859    ), Coef('Var'  , 0.149336    ), Coef('Var'  , 0.139844    ), Coef('Var'  , 0.134121    ), Coef('Var'  , 0.126658    ), Coef('Var'  , 0.137713    ), Coef('Var'  , 0.149031    ), Coef('Var'  , 0.152928    ), ], 
		[Coef('Var'  , 0.0790033   ), Coef('Var'  , 0.0770954   ), Coef('Var'  , 0.0752442   ), Coef('Var'  , 0.0917668   ), Coef('Var'  , 0.108533    ), Coef('Var'  , 0.101961    ), Coef('Var'  , 0.0944273   ), Coef('Var'  , 0.0872891   ), ], ])
	etat17.initMat[Chem([Sub('10')])] = FMat([
		[Coef('Var'  ,-0.0381447   ), Coef('Var'  ,-0.0282409   ), Coef('Var'  ,-0.0100305   ), Coef('Var'  ,-0.0165754   ), Coef('Var'  ,-0.0161928   ), Coef('Var'  ,-0.0336335   ), Coef('Var'  ,-0.0382232   ), Coef('Var'  ,-0.045299    ), ], 
		[Coef('Var'  , 0.27997     ), Coef('Var'  , 0.261509    ), Coef('Var'  , 0.231736    ), Coef('Var'  , 0.202996    ), Coef('Var'  , 0.164457    ), Coef('Var'  , 0.221808    ), Coef('Var'  , 0.263037    ), Coef('Var'  , 0.28032     ), ], 
		[Coef('Var'  , 0.173419    ), Coef('Var'  , 0.168854    ), Coef('Var'  , 0.163236    ), Coef('Var'  , 0.169856    ), Coef('Var'  , 0.175217    ), Coef('Var'  , 0.180547    ), Coef('Var'  , 0.183736    ), Coef('Var'  , 0.179545    ), ], 
		[Coef('Var'  , 0.184826    ), Coef('Var'  , 0.183199    ), Coef('Var'  , 0.18314     ), Coef('Var'  , 0.21785     ), Coef('Var'  , 0.2534      ), Coef('Var'  , 0.234967    ), Coef('Var'  , 0.216701    ), Coef('Var'  , 0.200316    ), ], 
		[Coef('Var'  , 0.0895417   ), Coef('Var'  , 0.0956466   ), Coef('Var'  , 0.106143    ), Coef('Var'  , 0.12597     ), Coef('Var'  , 0.149555    ), Coef('Var'  , 0.123436    ), Coef('Var'  , 0.102997    ), Coef('Var'  , 0.0931128   ), ], 
		[Coef('Var'  , 0.0818426   ), Coef('Var'  , 0.0890662   ), Coef('Var'  , 0.0975896   ), Coef('Var'  , 0.0972658   ), Coef('Var'  , 0.0984624   ), Coef('Var'  , 0.0839276   ), Coef('Var'  , 0.0718166   ), Coef('Var'  , 0.075728    ), ], 
		[Coef('Var'  , 0.163043    ), Coef('Var'  , 0.161119    ), Coef('Var'  , 0.154815    ), Coef('Var'  , 0.142479    ), Coef('Var'  , 0.126893    ), Coef('Var'  , 0.139327    ), Coef('Var'  , 0.146171    ), Coef('Var'  , 0.157967    ), ], 
		[Coef('Var'  , 0.0655022   ), Coef('Var'  , 0.0688464   ), Coef('Var'  , 0.0733718   ), Coef('Var'  , 0.060158    ), Coef('Var'  , 0.048209    ), Coef('Var'  , 0.0496216   ), Coef('Var'  , 0.0537652   ), Coef('Var'  , 0.05831     ), ], ])
	etat17.initMat[Chem([Sub('11')])] = FMat([
		[Coef('Var'  ,-0.00792259  ), Coef('Var'  , 0.014242    ), Coef('Var'  , 0.0351511   ), Coef('Var'  , 0.0449086   ), Coef('Var'  , 0.0506835   ), Coef('Var'  , 0.020075    ), Coef('Var'  ,-0.0100305   ), Coef('Var'  ,-0.0105916   ), ], 
		[Coef('Var'  , 0.25818     ), Coef('Var'  , 0.244473    ), Coef('Var'  , 0.231124    ), Coef('Var'  , 0.204169    ), Coef('Var'  , 0.180254    ), Coef('Var'  , 0.207357    ), Coef('Var'  , 0.231736    ), Coef('Var'  , 0.24766     ), ], 
		[Coef('Var'  , 0.163677    ), Coef('Var'  , 0.158233    ), Coef('Var'  , 0.153767    ), Coef('Var'  , 0.144799    ), Coef('Var'  , 0.136634    ), Coef('Var'  , 0.150065    ), Coef('Var'  , 0.163236    ), Coef('Var'  , 0.163499    ), ], 
		[Coef('Var'  , 0.16532     ), Coef('Var'  , 0.153727    ), Coef('Var'  , 0.145077    ), Coef('Var'  , 0.140613    ), Coef('Var'  , 0.138353    ), Coef('Var'  , 0.159986    ), Coef('Var'  , 0.18314     ), Coef('Var'  , 0.173099    ), ], 
		[Coef('Var'  , 0.0922233   ), Coef('Var'  , 0.0935585   ), Coef('Var'  , 0.0951265   ), Coef('Var'  , 0.103599    ), Coef('Var'  , 0.111243    ), Coef('Var'  , 0.108019    ), Coef('Var'  , 0.106143    ), Coef('Var'  , 0.0979783   ), ], 
		[Coef('Var'  , 0.0905684   ), Coef('Var'  , 0.094033    ), Coef('Var'  , 0.0962973   ), Coef('Var'  , 0.110941    ), Coef('Var'  , 0.124468    ), Coef('Var'  , 0.110893    ), Coef('Var'  , 0.0975896   ), Coef('Var'  , 0.0939849   ), ], 
		[Coef('Var'  , 0.159319    ), Coef('Var'  , 0.15461     ), Coef('Var'  , 0.149031    ), Coef('Var'  , 0.150926    ), Coef('Var'  , 0.153935    ), Coef('Var'  , 0.154633    ), Coef('Var'  , 0.154815    ), Coef('Var'  , 0.158317    ), ], 
		[Coef('Var'  , 0.0786351   ), Coef('Var'  , 0.0871233   ), Coef('Var'  , 0.0944273   ), Coef('Var'  , 0.100043    ), Coef('Var'  , 0.104431    ), Coef('Var'  , 0.0889713   ), Coef('Var'  , 0.0733718   ), Coef('Var'  , 0.0760517   ), ], ])
	etat17.initMat[Chem([Sub('12')])] = FMat([
		[Coef('Var'  , 0.153492    ), Coef('Var'  , 0.0830818   ), Coef('Var'  , 0.018837    ), Coef('Var'  , 0.00704738  ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.201034    ), ], 
		[Coef('Var'  , 0.298153    ), Coef('Var'  , 0.26191     ), Coef('Var'  , 0.219164    ), Coef('Var'  , 0.11225     ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.39966     ), ], 
		[Coef('Var'  , 0.182642    ), Coef('Var'  , 0.190971    ), Coef('Var'  , 0.198816    ), Coef('Var'  , 0.224661    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.21631     ), ], 
		[Coef('Var'  , 0.102827    ), Coef('Var'  , 0.175456    ), Coef('Var'  , 0.248592    ), Coef('Var'  , 0.374175    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0512804   ), ], 
		[Coef('Var'  , 0.0578429   ), Coef('Var'  , 0.0888957   ), Coef('Var'  , 0.121634    ), Coef('Var'  , 0.185002    ), Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0288933   ), ], 
		[Coef('Var'  , 0.0369097   ), Coef('Var'  , 0.0404134   ), Coef('Var'  , 0.0439861   ), Coef('Var'  , 0.0217912   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0186223   ), ], 
		[Coef('Var'  , 0.0787458   ), Coef('Var'  , 0.0892337   ), Coef('Var'  , 0.0968798   ), Coef('Var'  , 0.0495345   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0396993   ), ], 
		[Coef('Var'  , 0.0893877   ), Coef('Var'  , 0.0700389   ), Coef('Var'  , 0.052092    ), Coef('Var'  , 0.0255384   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0445005   ), ], ])
	etat17.initMat[Chem([Sub('13')])] = FMat([
		[Coef('Var'  , 0.117619    ), Coef('Var'  , 0.11911     ), Coef('Var'  , 0.119512    ), Coef('Var'  , 0.125285    ), Coef('Var'  , 0.129912    ), Coef('Var'  , 0.124155    ), ], 
		[Coef('Var'  , 0.0995331   ), Coef('Var'  , 0.109999    ), Coef('Var'  , 0.120772    ), Coef('Var'  , 0.121261    ), Coef('Var'  , 0.12251     ), Coef('Var'  , 0.110866    ), ], 
		[Coef('Var'  , 0.091436    ), Coef('Var'  , 0.101696    ), Coef('Var'  , 0.110436    ), Coef('Var'  , 0.110486    ), Coef('Var'  , 0.109252    ), Coef('Var'  , 0.101082    ), ], 
		[Coef('Var'  , 0.0875066   ), Coef('Var'  , 0.0976196   ), Coef('Var'  , 0.105973    ), Coef('Var'  , 0.104828    ), Coef('Var'  , 0.101927    ), Coef('Var'  , 0.0956151   ), ], 
		[Coef('Var'  , 0.101221    ), Coef('Var'  , 0.104825    ), Coef('Var'  , 0.107455    ), Coef('Var'  , 0.105466    ), Coef('Var'  , 0.102188    ), Coef('Var'  , 0.102252    ), ], 
		[Coef('Var'  , 0.129713    ), Coef('Var'  , 0.127907    ), Coef('Var'  , 0.125964    ), Coef('Var'  , 0.122315    ), Coef('Var'  , 0.118168    ), Coef('Var'  , 0.124095    ), ], 
		[Coef('Var'  , 0.18786     ), Coef('Var'  , 0.167975    ), Coef('Var'  , 0.151753    ), Coef('Var'  , 0.148837    ), Coef('Var'  , 0.149646    ), Coef('Var'  , 0.166977    ), ], 
		[Coef('Var'  , 0.185112    ), Coef('Var'  , 0.170869    ), Coef('Var'  , 0.158135    ), Coef('Var'  , 0.161522    ), Coef('Var'  , 0.166397    ), Coef('Var'  , 0.174958    ), ], ])
	etat17.initMat[Chem([Sub('14')])] = FMat([
		[Coef('Var'  , 0.150333    ), Coef('Var'  , 0.140598    ), Coef('Var'  , 0.129912    ), Coef('Var'  , 0.128639    ), Coef('Var'  , 0.126164    ), Coef('Var'  , 0.138907    ), ], 
		[Coef('Var'  , 0.145606    ), Coef('Var'  , 0.133368    ), Coef('Var'  , 0.12251     ), Coef('Var'  , 0.125399    ), Coef('Var'  , 0.129364    ), Coef('Var'  , 0.136638    ), ], 
		[Coef('Var'  , 0.113659    ), Coef('Var'  , 0.111844    ), Coef('Var'  , 0.109252    ), Coef('Var'  , 0.112415    ), Coef('Var'  , 0.114488    ), Coef('Var'  , 0.114387    ), ], 
		[Coef('Var'  , 0.0968674   ), Coef('Var'  , 0.100032    ), Coef('Var'  , 0.101927    ), Coef('Var'  , 0.105562    ), Coef('Var'  , 0.107568    ), Coef('Var'  , 0.10277     ), ], 
		[Coef('Var'  , 0.0868926   ), Coef('Var'  , 0.095366    ), Coef('Var'  , 0.102188    ), Coef('Var'  , 0.104281    ), Coef('Var'  , 0.104916    ), Coef('Var'  , 0.0967534   ), ], 
		[Coef('Var'  , 0.0939188   ), Coef('Var'  , 0.106569    ), Coef('Var'  , 0.118168    ), Coef('Var'  , 0.119042    ), Coef('Var'  , 0.119216    ), Coef('Var'  , 0.107107    ), ], 
		[Coef('Var'  , 0.137931    ), Coef('Var'  , 0.14226     ), Coef('Var'  , 0.149646    ), Coef('Var'  , 0.144039    ), Coef('Var'  , 0.142032    ), Coef('Var'  , 0.138461    ), ], 
		[Coef('Var'  , 0.174792    ), Coef('Var'  , 0.169964    ), Coef('Var'  , 0.166397    ), Coef('Var'  , 0.160624    ), Coef('Var'  , 0.156252    ), Coef('Var'  , 0.164977    ), ], ])
	etat17.initMat[Chem([Sub('15')])] = FMat([
		[Coef('Var'  , 0.095099    ), Coef('Var'  , 0.111886    ), Coef('Var'  , 0.126164    ), Coef('Var'  , 0.123594    ), Coef('Var'  , 0.119512    ), Coef('Var'  , 0.108532    ), ], 
		[Coef('Var'  , 0.136957    ), Coef('Var'  , 0.132294    ), Coef('Var'  , 0.129364    ), Coef('Var'  , 0.124531    ), Coef('Var'  , 0.120772    ), Coef('Var'  , 0.128155    ), ], 
		[Coef('Var'  , 0.119082    ), Coef('Var'  , 0.117196    ), Coef('Var'  , 0.114488    ), Coef('Var'  , 0.113029    ), Coef('Var'  , 0.110436    ), Coef('Var'  , 0.115267    ), ], 
		[Coef('Var'  , 0.11747     ), Coef('Var'  , 0.113008    ), Coef('Var'  , 0.107568    ), Coef('Var'  , 0.107566    ), Coef('Var'  , 0.105973    ), Coef('Var'  , 0.112275    ), ], 
		[Coef('Var'  , 0.114408    ), Coef('Var'  , 0.110307    ), Coef('Var'  , 0.104916    ), Coef('Var'  , 0.106854    ), Coef('Var'  , 0.107455    ), Coef('Var'  , 0.111492    ), ], 
		[Coef('Var'  , 0.134643    ), Coef('Var'  , 0.127158    ), Coef('Var'  , 0.119216    ), Coef('Var'  , 0.122854    ), Coef('Var'  , 0.125964    ), Coef('Var'  , 0.130431    ), ], 
		[Coef('Var'  , 0.149706    ), Coef('Var'  , 0.144105    ), Coef('Var'  , 0.142032    ), Coef('Var'  , 0.145037    ), Coef('Var'  , 0.151753    ), Coef('Var'  , 0.148903    ), ], 
		[Coef('Var'  , 0.132636    ), Coef('Var'  , 0.144047    ), Coef('Var'  , 0.156252    ), Coef('Var'  , 0.156535    ), Coef('Var'  , 0.158135    ), Coef('Var'  , 0.144945    ), ], ])
	etat17.initMat[Chem([Sub('16')])] = FMat([
		[Coef('Const', 0.111111    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0413434   ), Coef('Var'  , 0.082449    ), Coef('Var'  , 0.0968989   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0195551   ), Coef('Var'  , 0.0390133   ), Coef('Var'  , 0.0195552   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0179729   ), Coef('Var'  , 0.0354633   ), Coef('Var'  , 0.0179729   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0172078   ), Coef('Var'  , 0.0340521   ), Coef('Var'  , 0.0172078   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.180251    ), Coef('Var'  , 0.1104      ), Coef('Var'  , 0.0552516   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.346589    ), Coef('Var'  , 0.19332     ), Coef('Var'  , 0.0965892   ), ], 
		[Coef('Const', 0.444444    ), Coef('Const', 0.666667    ), Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.2691      ), Coef('Var'  , 0.288978    ), Coef('Var'  , 0.366322    ), ], 
		[Coef('Const', 0.444444    ), Coef('Const', 0.333333    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.10798     ), Coef('Var'  , 0.216324    ), Coef('Var'  , 0.330202    ), ], ])
	
	
	
	etat18.bords   = {Bord('0'): etat20, Bord('1'): etat19, Bord('2'): etat20, Bord('3'): etat19, }
	etat18.permuts = {}
	etat18.interns = {Intern('_'): etat18, }
	etat18.subs    = {Sub('0'): etat1, Sub('1'): etat2, Sub('2'): etat3, Sub('3'): etat4, Sub('4'): etat5, Sub('5'): etat6, Sub('6'): etat7, Sub('7'): etat8, Sub('G', True): Etat.etatPoint, Sub('8'): etat9, Sub('9'): etat10, Sub('10'): etat11, Sub('11'): etat12, Sub('12'): etat13, Sub('13'): etat14, Sub('14'): etat15, Sub('15'): etat16, Sub('16'): etat17, }
	
	etat18.buildIntern()
	
	
	etat18.eqs = [
		(Chem([Bord('0'), Sub('1'), Permut('0'), ])	,	Chem([Sub('0'), Bord('2'), ])),
		(Chem([Bord('2'), Sub('0'), Permut('0'), ])	,	Chem([Sub('2'), Bord('3'), ])),
		(Chem([Bord('1'), Sub('1'), Permut('0'), ])	,	Chem([Sub('2'), Bord('4'), ])),
		(Chem([Bord('0'), Sub('0'), Permut('0'), ])	,	Chem([Sub('3'), Bord('1'), ])),
		(Chem([Bord('3'), Sub('1'), Permut('0'), ])	,	Chem([Sub('3'), Bord('2'), ])),
		(Chem([Bord('2'), Sub('2'), Permut('0'), ])	,	Chem([Sub('6'), Bord('0'), ])),
		(Chem([Bord('3'), Sub('0'), Permut('0'), ])	,	Chem([Sub('6'), Bord('3'), ])),
		(Chem([Bord('2'), Sub('1'), Permut('0'), ])	,	Chem([Sub('7'), Bord('2'), ])),
		(Chem([Bord('1'), Sub('0'), Permut('0'), ])	,	Chem([Sub('16'), Bord('2'), ])),
		(Chem([Bord('0'), Sub('2'), Permut('0'), ])	,	Chem([Sub('16'), Bord('3'), ])),
		(Chem([Sub('0'), Bord('0'), Bord('1'), ])	,	Chem([Sub('12'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('1'), Bord('1'), ])	,	Chem([Sub('16'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('2'), Bord('1'), ])	,	Chem([Sub('3'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('3'), Bord('1'), ])	,	Chem([Sub('1'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('0'), Bord('1'), ])	,	Chem([Sub('12'), Bord('4'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('2'), Bord('1'), ])	,	Chem([Sub('3'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('3'), Bord('1'), ])	,	Chem([Sub('14'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('4'), Bord('1'), ])	,	Chem([Sub('9'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('0'), Bord('1'), ])	,	Chem([Sub('12'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('1'), Bord('1'), ])	,	Chem([Sub('10'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('2'), Bord('1'), ])	,	Chem([Sub('7'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('4'), Bord('1'), ])	,	Chem([Sub('16'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('3'), Bord('2'), Bord('1'), ])	,	Chem([Sub('6'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('4'), Bord('0'), Bord('1'), ])	,	Chem([Sub('8'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('4'), Bord('1'), Bord('1'), ])	,	Chem([Sub('9'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('4'), Bord('2'), Bord('1'), ])	,	Chem([Sub('11'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('4'), Bord('3'), Bord('1'), ])	,	Chem([Sub('10'), Bord('3'), Bord('1'), ])),
		(Chem([Sub('5'), Bord('0'), Bord('1'), ])	,	Chem([Sub('15'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('5'), Bord('1'), Bord('1'), ])	,	Chem([Sub('7'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('5'), Bord('2'), Bord('1'), ])	,	Chem([Sub('11'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('6'), Bord('0'), Bord('1'), ])	,	Chem([Sub('7'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('6'), Bord('1'), Bord('1'), ])	,	Chem([Sub('13'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('8'), Bord('0'), Bord('1'), ])	,	Chem([Sub('10'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('8'), Bord('1'), Bord('1'), ])	,	Chem([Sub('12'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('8'), Bord('2'), Bord('1'), ])	,	Chem([Sub('9'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('9'), Bord('2'), Bord('1'), ])	,	Chem([Sub('11'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('10'), Bord('0'), Bord('1'), ])	,	Chem([Sub('11'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('12'), Bord('2'), Bord('1'), ])	,	Chem([Sub('16'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('13'), Bord('0'), Bord('1'), ])	,	Chem([Sub('15'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('13'), Bord('1'), Bord('1'), ])	,	Chem([Sub('14'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('14'), Bord('1'), Bord('1'), ])	,	Chem([Sub('15'), Bord('0'), Bord('1'), ])),
		(Chem([Bord('0'), Bord('1'), ])	,	Chem([Bord('1'), Bord('0'), ])),
		(Chem([Bord('1'), Bord('1'), ])	,	Chem([Bord('2'), Bord('0'), ])),
		(Chem([Bord('2'), Bord('1'), ])	,	Chem([Bord('3'), Bord('0'), ])),
		(Chem([Bord('3'), Bord('1'), ])	,	Chem([Bord('0'), Bord('0'), ])),
		]
	
	
	etat18.prim.elems = [Figure(2, [Chem([Bord('0'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('0'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('0'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('0'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('1'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('1'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('1'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('1'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('2'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('2'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('2'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('2'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('3'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('3'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('3'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('3'), Sub('1'), Sub('1'), Bord('0'), ]), ])]
	etat18.grid.elems = [
		Figure(1, [Chem([Bord('1'), Bord('0'), ]), Chem([Bord('1'), Intern(''), ]), Chem([Bord('1'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('2'), Bord('0'), ]), Chem([Bord('2'), Intern(''), ]), Chem([Bord('2'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('0'), Bord('0'), ]), Chem([Bord('0'), Intern(''), ]), Chem([Bord('0'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('3'), Bord('0'), ]), Chem([Bord('3'), Intern(''), ]), Chem([Bord('3'), Bord('1'), ]), ]), ]
	
	
	etat18.space = [Chem([Bord('0'), Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('2'), Intern('0'), Intern('0'), ]), Chem([Bord('2'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('3'), Intern('0'), Intern('0'), ]), ]
	
	etat18.initMat[Chem([Sub('0')])] = FMat([
		[Coef('Var'  , 0.260333    ), Coef('Var'  , 0.206871    ), Coef('Var'  , 0.154061    ), Coef('Var'  , 0.132442    ), Coef('Const', 0.111111    ), Coef('Const', 0.222222    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.352207    ), ], 
		[Coef('Var'  , 0.288025    ), Coef('Var'  , 0.286372    ), Coef('Var'  , 0.286537    ), Coef('Var'  , 0.365039    ), Coef('Const', 0.444444    ), Coef('Const', 0.555556    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.365777    ), ], 
		[Coef('Var'  , 0.164795    ), Coef('Var'  , 0.216922    ), Coef('Var'  , 0.270174    ), Coef('Var'  , 0.356994    ), Coef('Const', 0.444444    ), Coef('Const', 0.222222    ), Coef('Const', 0.111111    ), Coef('Var'  , 0.137706    ), ], 
		[Coef('Var'  , 0.0568827   ), Coef('Var'  , 0.0742513   ), Coef('Var'  , 0.0916893   ), Coef('Var'  , 0.0457944   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.028457    ), ], 
		[Coef('Var'  , 0.05116     ), Coef('Var'  , 0.0603458   ), Coef('Var'  , 0.0690071   ), Coef('Var'  , 0.0346132   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0257327   ), ], 
		[Coef('Var'  , 0.0434067   ), Coef('Var'  , 0.0433886   ), Coef('Var'  , 0.0416923   ), Coef('Var'  , 0.0212708   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0221179   ), ], 
		[Coef('Var'  , 0.0585251   ), Coef('Var'  , 0.0503446   ), Coef('Var'  , 0.0411877   ), Coef('Var'  , 0.0208694   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0294754   ), ], 
		[Coef('Var'  , 0.0768729   ), Coef('Var'  , 0.0615045   ), Coef('Var'  , 0.0456527   ), Coef('Var'  , 0.0229771   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0385276   ), ], ])
	etat18.initMat[Chem([Sub('1')])] = FMat([
		[Coef('Var'  , 0.140875    ), Coef('Var'  , 0.152876    ), Coef('Var'  , 0.165538    ), Coef('Var'  , 0.212567    ), Coef('Var'  , 0.260333    ), Coef('Var'  , 0.270326    ), Coef('Var'  , 0.280984    ), Coef('Var'  , 0.22623     ), Coef('Var'  , 0.172191    ), Coef('Var'  , 0.156183    ), ], 
		[Coef('Var'  , 0.150575    ), Coef('Var'  , 0.181746    ), Coef('Var'  , 0.214292    ), Coef('Var'  , 0.250202    ), Coef('Var'  , 0.288025    ), Coef('Var'  , 0.251352    ), Coef('Var'  , 0.216044    ), Coef('Var'  , 0.175789    ), Coef('Var'  , 0.136199    ), Coef('Var'  , 0.143091    ), ], 
		[Coef('Var'  , 0.144961    ), Coef('Var'  , 0.165231    ), Coef('Var'  , 0.18595     ), Coef('Var'  , 0.174818    ), Coef('Var'  , 0.164795    ), Coef('Var'  , 0.130581    ), Coef('Var'  , 0.0967748   ), Coef('Var'  , 0.103899    ), Coef('Var'  , 0.109938    ), Coef('Var'  , 0.128032    ), ], 
		[Coef('Var'  , 0.105748    ), Coef('Var'  , 0.104003    ), Coef('Var'  , 0.101704    ), Coef('Var'  , 0.0793121   ), Coef('Var'  , 0.0568827   ), Coef('Var'  , 0.0454298   ), Coef('Var'  , 0.0336176   ), Coef('Var'  , 0.0544625   ), Coef('Var'  , 0.0738366   ), Coef('Var'  , 0.0906379   ), ], 
		[Coef('Var'  , 0.116276    ), Coef('Var'  , 0.105979    ), Coef('Var'  , 0.0957557   ), Coef('Var'  , 0.0736601   ), Coef('Var'  , 0.05116     ), Coef('Var'  , 0.0444004   ), Coef('Var'  , 0.0370642   ), Coef('Var'  , 0.0660579   ), Coef('Var'  , 0.0944603   ), Coef('Var'  , 0.105441    ), ], 
		[Coef('Var'  , 0.120032    ), Coef('Var'  , 0.100868    ), Coef('Var'  , 0.0810722   ), Coef('Var'  , 0.0630492   ), Coef('Var'  , 0.0434067   ), Coef('Var'  , 0.0436497   ), Coef('Var'  , 0.0427536   ), Coef('Var'  , 0.0838069   ), Coef('Var'  , 0.124865    ), Coef('Var'  , 0.122211    ), ], 
		[Coef('Var'  , 0.112865    ), Coef('Var'  , 0.0947388   ), Coef('Var'  , 0.0761726   ), Coef('Var'  , 0.0678506   ), Coef('Var'  , 0.0585251   ), Coef('Var'  , 0.085706    ), Coef('Var'  , 0.112619    ), Coef('Var'  , 0.12765     ), Coef('Var'  , 0.144034    ), Coef('Var'  , 0.127783    ), ], 
		[Coef('Var'  , 0.108668    ), Coef('Var'  , 0.094558    ), Coef('Var'  , 0.0795155   ), Coef('Var'  , 0.0785413   ), Coef('Var'  , 0.0768729   ), Coef('Var'  , 0.128554    ), Coef('Var'  , 0.180143    ), Coef('Var'  , 0.162105    ), Coef('Var'  , 0.144477    ), Coef('Var'  , 0.126622    ), ], ])
	etat18.initMat[Chem([Sub('2')])] = FMat([
		[Coef('Const', 0           ), Coef('Var'  , 0.03223     ), Coef('Var'  , 0.0643644   ), Coef('Var'  , 0.0642028   ), Coef('Var'  , 0.0636234   ), Coef('Var'  , 0.0319729   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0535797   ), Coef('Var'  , 0.107408    ), Coef('Var'  , 0.0944392   ), Coef('Var'  , 0.0815925   ), Coef('Var'  , 0.0408595   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.25        ), Coef('Var'  , 0.228047    ), Coef('Var'  , 0.206482    ), Coef('Var'  , 0.162095    ), Coef('Var'  , 0.118121    ), Coef('Var'  , 0.0590483   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.5         ), Coef('Var'  , 0.372832    ), Coef('Var'  , 0.24587     ), Coef('Var'  , 0.184945    ), Coef('Var'  , 0.124192    ), Coef('Var'  , 0.0621122   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0.25        ), Coef('Var'  , 0.219935    ), Coef('Var'  , 0.190328    ), Coef('Var'  , 0.215971    ), Coef('Var'  , 0.24297     ), Coef('Var'  , 0.343257    ), Coef('Const', 0.444444    ), Coef('Const', 0.666667    ), Coef('Const', 1           ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0450593   ), Coef('Var'  , 0.0900259   ), Coef('Var'  , 0.151727    ), Coef('Var'  , 0.213968    ), Coef('Var'  , 0.328889    ), Coef('Const', 0.444444    ), Coef('Const', 0.333333    ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0268556   ), Coef('Var'  , 0.0532972   ), Coef('Var'  , 0.0759382   ), Coef('Var'  , 0.0979726   ), Coef('Var'  , 0.104638    ), Coef('Const', 0.111111    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0214603   ), Coef('Var'  , 0.0422259   ), Coef('Var'  , 0.0506827   ), Coef('Var'  , 0.0575593   ), Coef('Var'  , 0.0292224   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], ])
	etat18.initMat[Chem([Sub('3')])] = FMat([
		[Coef('Var'  , 0.280984    ), Coef('Var'  , 0.362563    ), Coef('Const', 0.444444    ), Coef('Const', 0.666667    ), Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.265341    ), ], 
		[Coef('Var'  , 0.216044    ), Coef('Var'  , 0.33002     ), Coef('Const', 0.444444    ), Coef('Const', 0.333333    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.107798    ), ], 
		[Coef('Var'  , 0.0967748   ), Coef('Var'  , 0.103987    ), Coef('Const', 0.111111    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.048431    ), ], 
		[Coef('Var'  , 0.0336176   ), Coef('Var'  , 0.0169729   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0169729   ), ], 
		[Coef('Var'  , 0.0370642   ), Coef('Var'  , 0.0186678   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0186678   ), ], 
		[Coef('Var'  , 0.0427536   ), Coef('Var'  , 0.021532    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0215319   ), ], 
		[Coef('Var'  , 0.112619    ), Coef('Var'  , 0.0562308   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.181231    ), ], 
		[Coef('Var'  , 0.180143    ), Coef('Var'  , 0.0900267   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.340027    ), ], ])
	etat18.initMat[Chem([Sub('4')])] = FMat([
		[Coef('Var'  , 0.100619    ), Coef('Var'  , 0.10394     ), Coef('Var'  , 0.10664     ), Coef('Var'  , 0.108693    ), Coef('Var'  , 0.110393    ), Coef('Var'  , 0.107654    ), Coef('Var'  , 0.104371    ), Coef('Var'  , 0.102901    ), ], 
		[Coef('Var'  , 0.115821    ), Coef('Var'  , 0.12016     ), Coef('Var'  , 0.123783    ), Coef('Var'  , 0.1247      ), Coef('Var'  , 0.12501     ), Coef('Var'  , 0.12145     ), Coef('Var'  , 0.117048    ), Coef('Var'  , 0.116911    ), ], 
		[Coef('Var'  , 0.136886    ), Coef('Var'  , 0.140064    ), Coef('Var'  , 0.142742    ), Coef('Var'  , 0.142009    ), Coef('Var'  , 0.140785    ), Coef('Var'  , 0.138285    ), Coef('Var'  , 0.134929    ), Coef('Var'  , 0.13634     ), ], 
		[Coef('Var'  , 0.126244    ), Coef('Var'  , 0.127738    ), Coef('Var'  , 0.128658    ), Coef('Var'  , 0.126793    ), Coef('Var'  , 0.124247    ), Coef('Var'  , 0.123586    ), Coef('Var'  , 0.121833    ), Coef('Var'  , 0.124531    ), ], 
		[Coef('Var'  , 0.157258    ), Coef('Var'  , 0.151088    ), Coef('Var'  , 0.147513    ), Coef('Var'  , 0.143034    ), Coef('Var'  , 0.140795    ), Coef('Var'  , 0.14449     ), Coef('Var'  , 0.15054     ), Coef('Var'  , 0.152543    ), ], 
		[Coef('Var'  , 0.149875    ), Coef('Var'  , 0.142503    ), Coef('Var'  , 0.137695    ), Coef('Var'  , 0.13646     ), Coef('Var'  , 0.137552    ), Coef('Var'  , 0.142215    ), Coef('Var'  , 0.149732    ), Coef('Var'  , 0.148257    ), ], 
		[Coef('Var'  , 0.113922    ), Coef('Var'  , 0.112352    ), Coef('Var'  , 0.110501    ), Coef('Var'  , 0.113174    ), Coef('Var'  , 0.115639    ), Coef('Var'  , 0.11726     ), Coef('Var'  , 0.11906     ), Coef('Var'  , 0.116437    ), ], 
		[Coef('Var'  , 0.0993753   ), Coef('Var'  , 0.102156    ), Coef('Var'  , 0.102467    ), Coef('Var'  , 0.105137    ), Coef('Var'  , 0.105579    ), Coef('Var'  , 0.10506     ), Coef('Var'  , 0.102487    ), Coef('Var'  , 0.102079    ), ], ])
	etat18.initMat[Chem([Sub('5')])] = FMat([
		[Coef('Var'  , 0.0881891   ), Coef('Var'  , 0.0937067   ), Coef('Var'  , 0.0985576   ), Coef('Var'  , 0.0732104   ), Coef('Var'  , 0.0473749   ), Coef('Var'  , 0.068152    ), ], 
		[Coef('Var'  , 0.0857747   ), Coef('Var'  , 0.0807996   ), Coef('Var'  , 0.0749074   ), Coef('Var'  , 0.0583035   ), Coef('Var'  , 0.0409787   ), Coef('Var'  , 0.0637768   ), ], 
		[Coef('Var'  , 0.100919    ), Coef('Var'  , 0.0953785   ), Coef('Var'  , 0.0873419   ), Coef('Var'  , 0.0693589   ), Coef('Var'  , 0.0491246   ), Coef('Var'  , 0.075881    ), ], 
		[Coef('Var'  , 0.0895611   ), Coef('Var'  , 0.0826991   ), Coef('Var'  , 0.0731799   ), Coef('Var'  , 0.0592189   ), Coef('Var'  , 0.0429118   ), Coef('Var'  , 0.0671974   ), ], 
		[Coef('Var'  , 0.171225    ), Coef('Var'  , 0.162807    ), Coef('Var'  , 0.155437    ), Coef('Var'  , 0.187259    ), Coef('Var'  , 0.219644    ), Coef('Var'  , 0.194854    ), ], 
		[Coef('Var'  , 0.215545    ), Coef('Var'  , 0.217152    ), Coef('Var'  , 0.22193     ), Coef('Var'  , 0.274131    ), Coef('Var'  , 0.328845    ), Coef('Var'  , 0.270851    ), ], 
		[Coef('Var'  , 0.161324    ), Coef('Var'  , 0.171446    ), Coef('Var'  , 0.184256    ), Coef('Var'  , 0.202374    ), Coef('Var'  , 0.22304     ), Coef('Var'  , 0.191302    ), ], 
		[Coef('Var'  , 0.0874621   ), Coef('Var'  , 0.0960119   ), Coef('Var'  , 0.10439     ), Coef('Var'  , 0.0761448   ), Coef('Var'  , 0.0480813   ), Coef('Var'  , 0.0679851   ), ], ])
	etat18.initMat[Chem([Sub('6')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0637873   ), Coef('Var'  , 0.127715    ), Coef('Var'  , 0.188787    ), Coef('Const', 0.25        ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0204249   ), Coef('Var'  , 0.040713    ), Coef('Var'  , 0.0204248   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0235892   ), Coef('Var'  , 0.0462001   ), Coef('Var'  , 0.0235891   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0186367   ), Coef('Var'  , 0.0363755   ), Coef('Var'  , 0.0186367   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.111111    ), Coef('Var'  , 0.0971747   ), Coef('Var'  , 0.0830484   ), Coef('Var'  , 0.0416191   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.333333    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.321185    ), Coef('Var'  , 0.198467    ), Coef('Var'  , 0.0989625   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 1           ), Coef('Const', 0.666667    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.355425    ), Coef('Var'  , 0.267581    ), Coef('Var'  , 0.258203    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0997773   ), Coef('Var'  , 0.1999      ), Coef('Var'  , 0.349777    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), ], ])
	etat18.initMat[Chem([Sub('7')])] = FMat([
		[Coef('Const', 0           ), Coef('Var'  , 0.0238279   ), Coef('Var'  , 0.0473749   ), Coef('Var'  , 0.0238279   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0206404   ), Coef('Var'  , 0.0409787   ), Coef('Var'  , 0.0206404   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0249308   ), Coef('Var'  , 0.0491246   ), Coef('Var'  , 0.0249308   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0218586   ), Coef('Var'  , 0.0429118   ), Coef('Var'  , 0.0218586   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.444444    ), Coef('Var'  , 0.331875    ), Coef('Var'  , 0.219644    ), Coef('Var'  , 0.165209    ), Coef('Const', 0.111111    ), Coef('Const', 0.222222    ), ], 
		[Coef('Const', 0.444444    ), Coef('Var'  , 0.386137    ), Coef('Var'  , 0.328845    ), Coef('Var'  , 0.386137    ), Coef('Const', 0.444444    ), Coef('Const', 0.555556    ), ], 
		[Coef('Const', 0.111111    ), Coef('Var'  , 0.166671    ), Coef('Var'  , 0.22304     ), Coef('Var'  , 0.333338    ), Coef('Const', 0.444444    ), Coef('Const', 0.222222    ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.024059    ), Coef('Var'  , 0.0480813   ), Coef('Var'  , 0.024059    ), Coef('Const', 0           ), Coef('Const', 0           ), ], ])
	etat18.initMat[Chem([Sub('G')])] = FMat([
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], ])
	etat18.initMat[Chem([Sub('8')])] = FMat([
		[Coef('Var'  , 0.10664     ), Coef('Var'  , 0.101631    ), Coef('Var'  , 0.0961491   ), Coef('Var'  , 0.103529    ), Coef('Var'  , 0.110677    ), Coef('Var'  , 0.113804    ), Coef('Var'  , 0.117043    ), Coef('Var'  , 0.111906    ), ], 
		[Coef('Var'  , 0.123783    ), Coef('Var'  , 0.120185    ), Coef('Var'  , 0.116188    ), Coef('Var'  , 0.129024    ), Coef('Var'  , 0.142161    ), Coef('Var'  , 0.138427    ), Coef('Var'  , 0.135195    ), Coef('Var'  , 0.129588    ), ], 
		[Coef('Var'  , 0.142742    ), Coef('Var'  , 0.142339    ), Coef('Var'  , 0.141827    ), Coef('Var'  , 0.155586    ), Coef('Var'  , 0.16985     ), Coef('Var'  , 0.159495    ), Coef('Var'  , 0.149618    ), Coef('Var'  , 0.146248    ), ], 
		[Coef('Var'  , 0.128658    ), Coef('Var'  , 0.130923    ), Coef('Var'  , 0.132959    ), Coef('Var'  , 0.142416    ), Coef('Var'  , 0.151998    ), Coef('Var'  , 0.140212    ), Coef('Var'  , 0.128365    ), Coef('Var'  , 0.128719    ), ], 
		[Coef('Var'  , 0.147513    ), Coef('Var'  , 0.157679    ), Coef('Var'  , 0.170192    ), Coef('Var'  , 0.157338    ), Coef('Var'  , 0.14623     ), Coef('Var'  , 0.14021     ), Coef('Var'  , 0.135495    ), Coef('Var'  , 0.140551    ), ], 
		[Coef('Var'  , 0.137695    ), Coef('Var'  , 0.143357    ), Coef('Var'  , 0.150927    ), Coef('Var'  , 0.130982    ), Coef('Var'  , 0.111768    ), Coef('Var'  , 0.118213    ), Coef('Var'  , 0.125093    ), Coef('Var'  , 0.130588    ), ], 
		[Coef('Var'  , 0.110501    ), Coef('Var'  , 0.10711     ), Coef('Var'  , 0.103141    ), Coef('Var'  , 0.0952296   ), Coef('Var'  , 0.0863845   ), Coef('Var'  , 0.0970879   ), Coef('Var'  , 0.106971    ), Coef('Var'  , 0.108968    ), ], 
		[Coef('Var'  , 0.102467    ), Coef('Var'  , 0.096777    ), Coef('Var'  , 0.0886169   ), Coef('Var'  , 0.0858949   ), Coef('Var'  , 0.0809313   ), Coef('Var'  , 0.09255     ), Coef('Var'  , 0.102221    ), Coef('Var'  , 0.103432    ), ], ])
	etat18.initMat[Chem([Sub('9')])] = FMat([
		[Coef('Var'  , 0.110393    ), Coef('Var'  , 0.113763    ), Coef('Var'  , 0.117043    ), Coef('Var'  , 0.128782    ), Coef('Var'  , 0.140875    ), Coef('Var'  , 0.126151    ), Coef('Var'  , 0.11152     ), Coef('Var'  , 0.111133    ), ], 
		[Coef('Var'  , 0.12501     ), Coef('Var'  , 0.130233    ), Coef('Var'  , 0.135195    ), Coef('Var'  , 0.14266     ), Coef('Var'  , 0.150575    ), Coef('Var'  , 0.135468    ), Coef('Var'  , 0.120432    ), Coef('Var'  , 0.123041    ), ], 
		[Coef('Var'  , 0.140785    ), Coef('Var'  , 0.145358    ), Coef('Var'  , 0.149618    ), Coef('Var'  , 0.147363    ), Coef('Var'  , 0.144961    ), Coef('Var'  , 0.138843    ), Coef('Var'  , 0.131998    ), Coef('Var'  , 0.136839    ), ], 
		[Coef('Var'  , 0.124247    ), Coef('Var'  , 0.126642    ), Coef('Var'  , 0.128365    ), Coef('Var'  , 0.117432    ), Coef('Var'  , 0.105748    ), Coef('Var'  , 0.109828    ), Coef('Var'  , 0.112574    ), Coef('Var'  , 0.119038    ), ], 
		[Coef('Var'  , 0.140795    ), Coef('Var'  , 0.137252    ), Coef('Var'  , 0.135495    ), Coef('Var'  , 0.125436    ), Coef('Var'  , 0.116276    ), Coef('Var'  , 0.128681    ), Coef('Var'  , 0.142134    ), Coef('Var'  , 0.140498    ), ], 
		[Coef('Var'  , 0.137552    ), Coef('Var'  , 0.130444    ), Coef('Var'  , 0.125093    ), Coef('Var'  , 0.122222    ), Coef('Var'  , 0.120032    ), Coef('Var'  , 0.135269    ), Coef('Var'  , 0.151974    ), Coef('Var'  , 0.143491    ), ], 
		[Coef('Var'  , 0.115639    ), Coef('Var'  , 0.111422    ), Coef('Var'  , 0.106971    ), Coef('Var'  , 0.109971    ), Coef('Var'  , 0.112865    ), Coef('Var'  , 0.119275    ), Coef('Var'  , 0.12619     ), Coef('Var'  , 0.120726    ), ], 
		[Coef('Var'  , 0.105579    ), Coef('Var'  , 0.104884    ), Coef('Var'  , 0.102221    ), Coef('Var'  , 0.106134    ), Coef('Var'  , 0.108668    ), Coef('Var'  , 0.106485    ), Coef('Var'  , 0.103178    ), Coef('Var'  , 0.105235    ), ], ])
	etat18.initMat[Chem([Sub('10')])] = FMat([
		[Coef('Var'  , 0.100619    ), Coef('Var'  , 0.096103    ), Coef('Var'  , 0.0906253   ), Coef('Var'  , 0.0775541   ), Coef('Var'  , 0.0636234   ), Coef('Var'  , 0.0801856   ), Coef('Var'  , 0.0961491   ), Coef('Var'  , 0.0987345   ), ], 
		[Coef('Var'  , 0.115821    ), Coef('Var'  , 0.109097    ), Coef('Var'  , 0.101424    ), Coef('Var'  , 0.0918232   ), Coef('Var'  , 0.0815925   ), Coef('Var'  , 0.0990169   ), Coef('Var'  , 0.116188    ), Coef('Var'  , 0.11629     ), ], 
		[Coef('Var'  , 0.136886    ), Coef('Var'  , 0.130986    ), Coef('Var'  , 0.124209    ), Coef('Var'  , 0.12142     ), Coef('Var'  , 0.118121    ), Coef('Var'  , 0.129938    ), Coef('Var'  , 0.141827    ), Coef('Var'  , 0.139505    ), ], 
		[Coef('Var'  , 0.126244    ), Coef('Var'  , 0.122188    ), Coef('Var'  , 0.117168    ), Coef('Var'  , 0.120996    ), Coef('Var'  , 0.124192    ), Coef('Var'  , 0.1286      ), Coef('Var'  , 0.132959    ), Coef('Var'  , 0.129792    ), ], 
		[Coef('Var'  , 0.157258    ), Coef('Var'  , 0.165678    ), Coef('Var'  , 0.17683     ), Coef('Var'  , 0.208792    ), Coef('Var'  , 0.24297     ), Coef('Var'  , 0.205547    ), Coef('Var'  , 0.170192    ), Coef('Var'  , 0.162433    ), ], 
		[Coef('Var'  , 0.149875    ), Coef('Var'  , 0.162301    ), Coef('Var'  , 0.177807    ), Coef('Var'  , 0.194768    ), Coef('Var'  , 0.213968    ), Coef('Var'  , 0.181722    ), Coef('Var'  , 0.150927    ), Coef('Var'  , 0.149256    ), ], 
		[Coef('Var'  , 0.113922    ), Coef('Var'  , 0.118048    ), Coef('Var'  , 0.122363    ), Coef('Var'  , 0.110139    ), Coef('Var'  , 0.0979726   ), Coef('Var'  , 0.100832    ), Coef('Var'  , 0.103141    ), Coef('Var'  , 0.108741    ), ], 
		[Coef('Var'  , 0.0993753   ), Coef('Var'  , 0.0955988   ), Coef('Var'  , 0.0895731   ), Coef('Var'  , 0.0745077   ), Coef('Var'  , 0.0575593   ), Coef('Var'  , 0.0741569   ), Coef('Var'  , 0.0886169   ), Coef('Var'  , 0.0952481   ), ], ])
	etat18.initMat[Chem([Sub('11')])] = FMat([
		[Coef('Var'  , 0.104371    ), Coef('Var'  , 0.108237    ), Coef('Var'  , 0.11152     ), Coef('Var'  , 0.100182    ), Coef('Var'  , 0.0881891   ), Coef('Var'  , 0.0899054   ), Coef('Var'  , 0.0906253   ), Coef('Var'  , 0.0979603   ), ], 
		[Coef('Var'  , 0.117048    ), Coef('Var'  , 0.119147    ), Coef('Var'  , 0.120432    ), Coef('Var'  , 0.103505    ), Coef('Var'  , 0.0857747   ), Coef('Var'  , 0.0941002   ), Coef('Var'  , 0.101424    ), Coef('Var'  , 0.109742    ), ], 
		[Coef('Var'  , 0.134929    ), Coef('Var'  , 0.134004    ), Coef('Var'  , 0.131998    ), Coef('Var'  , 0.117229    ), Coef('Var'  , 0.100919    ), Coef('Var'  , 0.113322    ), Coef('Var'  , 0.124209    ), Coef('Var'  , 0.130097    ), ], 
		[Coef('Var'  , 0.121833    ), Coef('Var'  , 0.117907    ), Coef('Var'  , 0.112574    ), Coef('Var'  , 0.102018    ), Coef('Var'  , 0.0895611   ), Coef('Var'  , 0.104223    ), Coef('Var'  , 0.117168    ), Coef('Var'  , 0.120112    ), ], 
		[Coef('Var'  , 0.15054     ), Coef('Var'  , 0.145252    ), Coef('Var'  , 0.142134    ), Coef('Var'  , 0.155831    ), Coef('Var'  , 0.171225    ), Coef('Var'  , 0.172959    ), Coef('Var'  , 0.17683     ), Coef('Var'  , 0.16238     ), ], 
		[Coef('Var'  , 0.149732    ), Coef('Var'  , 0.14939     ), Coef('Var'  , 0.151974    ), Coef('Var'  , 0.182269    ), Coef('Var'  , 0.215545    ), Coef('Var'  , 0.195037    ), Coef('Var'  , 0.177807    ), Coef('Var'  , 0.162157    ), ], 
		[Coef('Var'  , 0.11906     ), Coef('Var'  , 0.122357    ), Coef('Var'  , 0.12619     ), Coef('Var'  , 0.143099    ), Coef('Var'  , 0.161324    ), Coef('Var'  , 0.141243    ), Coef('Var'  , 0.122363    ), Coef('Var'  , 0.120502    ), ], 
		[Coef('Var'  , 0.102487    ), Coef('Var'  , 0.103706    ), Coef('Var'  , 0.103178    ), Coef('Var'  , 0.0958668   ), Coef('Var'  , 0.0874621   ), Coef('Var'  , 0.0892114   ), Coef('Var'  , 0.0895731   ), Coef('Var'  , 0.0970509   ), ], ])
	etat18.initMat[Chem([Sub('12')])] = FMat([
		[Coef('Var'  , 0.165538    ), Coef('Var'  , 0.137899    ), Coef('Var'  , 0.110677    ), Coef('Var'  , 0.0875463   ), Coef('Var'  , 0.0643644   ), Coef('Var'  , 0.0733162   ), Coef('Var'  , 0.0822277   ), Coef('Var'  , 0.117973    ), Coef('Var'  , 0.154061    ), Coef('Var'  , 0.159469    ), ], 
		[Coef('Var'  , 0.214292    ), Coef('Var'  , 0.177514    ), Coef('Var'  , 0.142161    ), Coef('Var'  , 0.124446    ), Coef('Var'  , 0.107408    ), Coef('Var'  , 0.157618    ), Coef('Var'  , 0.208504    ), Coef('Var'  , 0.246856    ), Coef('Var'  , 0.286537    ), Coef('Var'  , 0.249464    ), ], 
		[Coef('Var'  , 0.18595     ), Coef('Var'  , 0.177363    ), Coef('Var'  , 0.16985     ), Coef('Var'  , 0.187743    ), Coef('Var'  , 0.206482    ), Coef('Var'  , 0.248703    ), Coef('Var'  , 0.291734    ), Coef('Var'  , 0.280428    ), Coef('Var'  , 0.270174    ), Coef('Var'  , 0.227439    ), ], 
		[Coef('Var'  , 0.101704    ), Coef('Var'  , 0.126783    ), Coef('Var'  , 0.151998    ), Coef('Var'  , 0.19876     ), Coef('Var'  , 0.24587     ), Coef('Var'  , 0.227255    ), Coef('Var'  , 0.209011    ), Coef('Var'  , 0.150216    ), Coef('Var'  , 0.0916893   ), Coef('Var'  , 0.0966495   ), ], 
		[Coef('Var'  , 0.0957557   ), Coef('Var'  , 0.120754    ), Coef('Var'  , 0.14623     ), Coef('Var'  , 0.167762    ), Coef('Var'  , 0.190328    ), Coef('Var'  , 0.158503    ), Coef('Var'  , 0.12718     ), Coef('Var'  , 0.0981805   ), Coef('Var'  , 0.0690071   ), Coef('Var'  , 0.0825406   ), ], 
		[Coef('Var'  , 0.0810722   ), Coef('Var'  , 0.0968582   ), Coef('Var'  , 0.111768    ), Coef('Var'  , 0.100986    ), Coef('Var'  , 0.0900259   ), Coef('Var'  , 0.0622337   ), Coef('Var'  , 0.0339335   ), Coef('Var'  , 0.0384452   ), Coef('Var'  , 0.0416923   ), Coef('Var'  , 0.0622021   ), ], 
		[Coef('Var'  , 0.0761726   ), Coef('Var'  , 0.0818553   ), Coef('Var'  , 0.0863845   ), Coef('Var'  , 0.0703355   ), Coef('Var'  , 0.0532972   ), Coef('Var'  , 0.0393208   ), Coef('Var'  , 0.0245594   ), Coef('Var'  , 0.0333345   ), Coef('Var'  , 0.0411877   ), Coef('Var'  , 0.0592447   ), ], 
		[Coef('Var'  , 0.0795155   ), Coef('Var'  , 0.0809741   ), Coef('Var'  , 0.0809313   ), Coef('Var'  , 0.0624206   ), Coef('Var'  , 0.0422259   ), Coef('Var'  , 0.0330507   ), Coef('Var'  , 0.0228506   ), Coef('Var'  , 0.0345674   ), Coef('Var'  , 0.0456527   ), Coef('Var'  , 0.0629908   ), ], ])
	etat18.initMat[Chem([Sub('13')])] = FMat([
		[Coef('Var'  , 0.127715    ), Coef('Var'  , 0.125725    ), Coef('Var'  , 0.123997    ), Coef('Var'  , 0.130969    ), Coef('Var'  , 0.138364    ), Coef('Var'  , 0.132818    ), ], 
		[Coef('Var'  , 0.040713    ), Coef('Var'  , 0.0579397   ), Coef('Var'  , 0.074744    ), Coef('Var'  , 0.0809034   ), Coef('Var'  , 0.0866568   ), Coef('Var'  , 0.0638134   ), ], 
		[Coef('Var'  , 0.0462001   ), Coef('Var'  , 0.0668543   ), Coef('Var'  , 0.0848206   ), Coef('Var'  , 0.0885926   ), Coef('Var'  , 0.0890694   ), Coef('Var'  , 0.0689165   ), ], 
		[Coef('Var'  , 0.0363755   ), Coef('Var'  , 0.0533014   ), Coef('Var'  , 0.0677058   ), Coef('Var'  , 0.0692349   ), Coef('Var'  , 0.0676205   ), Coef('Var'  , 0.0532068   ), ], 
		[Coef('Var'  , 0.0830484   ), Coef('Var'  , 0.0994629   ), Coef('Var'  , 0.115493    ), Coef('Var'  , 0.10982     ), Coef('Var'  , 0.103605    ), Coef('Var'  , 0.093595    ), ], 
		[Coef('Var'  , 0.198467    ), Coef('Var'  , 0.191989    ), Coef('Var'  , 0.187183    ), Coef('Var'  , 0.176841    ), Coef('Var'  , 0.168432    ), Coef('Var'  , 0.182777    ), ], 
		[Coef('Var'  , 0.267581    ), Coef('Var'  , 0.231362    ), Coef('Var'  , 0.198352    ), Coef('Var'  , 0.192509    ), Coef('Var'  , 0.190599    ), Coef('Var'  , 0.227554    ), ], 
		[Coef('Var'  , 0.1999      ), Coef('Var'  , 0.173366    ), Coef('Var'  , 0.147705    ), Coef('Var'  , 0.151131    ), Coef('Var'  , 0.155652    ), Coef('Var'  , 0.17732     ), ], ])
	etat18.initMat[Chem([Sub('14')])] = FMat([
		[Coef('Var'  , 0.172191    ), Coef('Var'  , 0.15492     ), Coef('Var'  , 0.138364    ), Coef('Var'  , 0.135299    ), Coef('Var'  , 0.132736    ), Coef('Var'  , 0.152157    ), ], 
		[Coef('Var'  , 0.136199    ), Coef('Var'  , 0.11138     ), Coef('Var'  , 0.0866568   ), Coef('Var'  , 0.0903049   ), Coef('Var'  , 0.0936439   ), Coef('Var'  , 0.114908    ), ], 
		[Coef('Var'  , 0.109938    ), Coef('Var'  , 0.100795    ), Coef('Var'  , 0.0890694   ), Coef('Var'  , 0.0949639   ), Coef('Var'  , 0.0975681   ), Coef('Var'  , 0.105104    ), ], 
		[Coef('Var'  , 0.0738366   ), Coef('Var'  , 0.0720598   ), Coef('Var'  , 0.0676205   ), Coef('Var'  , 0.0730655   ), Coef('Var'  , 0.0753169   ), Coef('Var'  , 0.075985    ), ], 
		[Coef('Var'  , 0.0944603   ), Coef('Var'  , 0.099366    ), Coef('Var'  , 0.103605    ), Coef('Var'  , 0.111024    ), Coef('Var'  , 0.117858    ), Coef('Var'  , 0.106439    ), ], 
		[Coef('Var'  , 0.124865    ), Coef('Var'  , 0.146089    ), Coef('Var'  , 0.168432    ), Coef('Var'  , 0.169599    ), Coef('Var'  , 0.172613    ), Coef('Var'  , 0.148059    ), ], 
		[Coef('Var'  , 0.144034    ), Coef('Var'  , 0.16577     ), Coef('Var'  , 0.190599    ), Coef('Var'  , 0.180162    ), Coef('Var'  , 0.173648    ), Coef('Var'  , 0.15723     ), ], 
		[Coef('Var'  , 0.144477    ), Coef('Var'  , 0.14962     ), Coef('Var'  , 0.155652    ), Coef('Var'  , 0.145582    ), Coef('Var'  , 0.136616    ), Coef('Var'  , 0.140117    ), ], ])
	etat18.initMat[Chem([Sub('15')])] = FMat([
		[Coef('Var'  , 0.0985576   ), Coef('Var'  , 0.115651    ), Coef('Var'  , 0.132736    ), Coef('Var'  , 0.128206    ), Coef('Var'  , 0.123997    ), Coef('Var'  , 0.11132     ), ], 
		[Coef('Var'  , 0.0749074   ), Coef('Var'  , 0.0845795   ), Coef('Var'  , 0.0936439   ), Coef('Var'  , 0.0844312   ), Coef('Var'  , 0.074744    ), Coef('Var'  , 0.075178    ), ], 
		[Coef('Var'  , 0.0873419   ), Coef('Var'  , 0.0940646   ), Coef('Var'  , 0.0975681   ), Coef('Var'  , 0.0929017   ), Coef('Var'  , 0.0848206   ), Coef('Var'  , 0.0876934   ), ], 
		[Coef('Var'  , 0.0731799   ), Coef('Var'  , 0.0758557   ), Coef('Var'  , 0.0753169   ), Coef('Var'  , 0.0731601   ), Coef('Var'  , 0.0677058   ), Coef('Var'  , 0.0720251   ), ], 
		[Coef('Var'  , 0.155437    ), Coef('Var'  , 0.136654    ), Coef('Var'  , 0.117858    ), Coef('Var'  , 0.116892    ), Coef('Var'  , 0.115493    ), Coef('Var'  , 0.135449    ), ], 
		[Coef('Var'  , 0.22193     ), Coef('Var'  , 0.196       ), Coef('Var'  , 0.172613    ), Coef('Var'  , 0.178811    ), Coef('Var'  , 0.187183    ), Coef('Var'  , 0.203242    ), ], 
		[Coef('Var'  , 0.184256    ), Coef('Var'  , 0.17707     ), Coef('Var'  , 0.173648    ), Coef('Var'  , 0.18397     ), Coef('Var'  , 0.198352    ), Coef('Var'  , 0.189417    ), ], 
		[Coef('Var'  , 0.10439     ), Coef('Var'  , 0.120125    ), Coef('Var'  , 0.136616    ), Coef('Var'  , 0.141628    ), Coef('Var'  , 0.147705    ), Coef('Var'  , 0.125675    ), ], ])
	etat18.initMat[Chem([Sub('16')])] = FMat([
		[Coef('Const', 0.111111    ), Coef('Var'  , 0.0966418   ), Coef('Var'  , 0.0822277   ), Coef('Var'  , 0.0410862   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.444444    ), Coef('Var'  , 0.326261    ), Coef('Var'  , 0.208504    ), Coef('Var'  , 0.104039    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.333333    ), ], 
		[Coef('Const', 0.444444    ), Coef('Var'  , 0.367878    ), Coef('Var'  , 0.291734    ), Coef('Var'  , 0.270656    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.666667    ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.104422    ), Coef('Var'  , 0.209011    ), Coef('Var'  , 0.354422    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0635675   ), Coef('Var'  , 0.12718     ), Coef('Var'  , 0.188567    ), Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0171745   ), Coef('Var'  , 0.0339335   ), Coef('Var'  , 0.0171745   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0124653   ), Coef('Var'  , 0.0245594   ), Coef('Var'  , 0.0124652   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0115905   ), Coef('Var'  , 0.0228506   ), Coef('Var'  , 0.0115904   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], ])
	
	
	
	etat19.bords   = {Bord('0'): etat23, Bord('1'): etat23, }
	etat19.permuts = {Permut('0'): etat19, }
	etat19.interns = {Intern('_'): etat19, }
	etat19.subs    = {Sub('0'): etat19, Sub('1'): etat19, Sub('G', True): Etat.etatPoint, }
	
	etat19.buildIntern()
	etat19.fm_[Permut('0')] = PMat(3, [2, 1, 0, ])
	
	
	etat19.eqs = [
		(Chem([Permut('0'), Bord('0'), ])	,	Chem([Bord('1')])),
		(Chem([Permut('0'), Bord('1'), ])	,	Chem([Bord('0')])),
		(Chem([Permut('0'), Intern(''), ])	,	Chem([Intern('')])),
		(Chem([Permut('0'), Sub('0'), ])	,	Chem([Sub('1'), Permut('0'), ])),
		(Chem([Permut('0'), Sub('1'), ])	,	Chem([Sub('0'), Permut('0'), ])),
		]
	
	
	etat19.prim.elems = [Figure(1, [Chem([Bord('0')]), Chem([Bord('1')]), ])]
	etat19.grid.elems = [Figure(1, [Chem([Bord('0')]), Chem([Intern('')]), Chem([Bord('1')]), ])]
	
	
	etat19.space = [Chem([Bord('0'), Intern('0'), Intern('0'), ]), Chem([Intern('0'), Intern('0'), ]), Chem([Bord('1'), Intern('0'), Intern('0'), ]), ]
	
	etat19.initMat[Chem([Sub('0')])] = FMat([
		[Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), ], ])
	etat19.initMat[Chem([Sub('1')])] = FMat([
		[Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), ], ])
	etat19.initMat[Chem([Sub('G')])] = FMat([
		[Coef('Const', 0           )], 
		[Coef('Const', 1           )], 
		[Coef('Const', 0           )], ])
	
	
	
	etat20.bords   = {Bord('0'): etat23, Bord('1'): etat23, }
	etat20.permuts = {Permut('0'): etat20, }
	etat20.interns = {Intern('_'): etat20, }
	etat20.subs    = {Sub('0'): etat20, Sub('1'): etat20, Sub('2'): etat20, Sub('G', True): Etat.etatPoint, }
	
	etat20.buildIntern()
	etat20.fm_[Permut('0')] = PMat(3, [2, 1, 0, ])
	
	
	etat20.eqs = [
		(Chem([Permut('0'), Bord('0'), ])	,	Chem([Bord('1')])),
		(Chem([Permut('0'), Bord('1'), ])	,	Chem([Bord('0')])),
		(Chem([Permut('0'), Intern(''), ])	,	Chem([Intern('')])),
		(Chem([Permut('0'), Sub('0'), ])	,	Chem([Sub('2'), Permut('0'), ])),
		(Chem([Permut('0'), Sub('1'), ])	,	Chem([Sub('1'), Permut('0'), ])),
		(Chem([Permut('0'), Sub('2'), ])	,	Chem([Sub('0'), Permut('0'), ])),
		]
	
	
	etat20.prim.elems = [Figure(1, [Chem([Bord('0')]), Chem([Bord('1')]), ])]
	etat20.grid.elems = [Figure(1, [Chem([Bord('0')]), Chem([Intern('')]), Chem([Bord('1')]), ])]
	
	
	etat20.space = [Chem([Bord('0'), Intern('0'), Intern('0'), ]), Chem([Intern('0'), Intern('0'), ]), Chem([Bord('1'), Intern('0'), Intern('0'), ]), ]
	
	etat20.initMat[Chem([Sub('0')])] = FMat([
		[Coef('Const', 1           ), Coef('Const', 0.666667    ), Coef('Const', 0.444444    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.333333    ), Coef('Const', 0.444444    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.111111    ), ], ])
	etat20.initMat[Chem([Sub('1')])] = FMat([
		[Coef('Const', 0.444444    ), Coef('Const', 0.222222    ), Coef('Const', 0.111111    ), ], 
		[Coef('Const', 0.444444    ), Coef('Const', 0.555556    ), Coef('Const', 0.444444    ), ], 
		[Coef('Const', 0.111111    ), Coef('Const', 0.222222    ), Coef('Const', 0.444444    ), ], ])
	etat20.initMat[Chem([Sub('2')])] = FMat([
		[Coef('Const', 0.111111    ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.444444    ), Coef('Const', 0.333333    ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.444444    ), Coef('Const', 0.666667    ), Coef('Const', 1           ), ], ])
	etat20.initMat[Chem([Sub('G')])] = FMat([
		[Coef('Const', 0           )], 
		[Coef('Const', 1           )], 
		[Coef('Const', 0           )], ])
	
	
	
	etat21.bords   = {Bord('0'): etat23, Bord('1'): etat23, }
	etat21.permuts = {Permut('0'): etat21, }
	etat21.interns = {Intern('_'): etat21, }
	etat21.subs    = {Sub('0'): etat21, Sub('1'): etat21, Sub('2'): etat21, Sub('3'): etat21, Sub('G', True): Etat.etatPoint, }
	
	etat21.buildIntern()
	etat21.fm_[Permut('0')] = PMat(3, [2, 1, 0, ])
	
	
	etat21.eqs = [
		(Chem([Permut('0'), Bord('0'), ])	,	Chem([Bord('1')])),
		(Chem([Permut('0'), Bord('1'), ])	,	Chem([Bord('0')])),
		(Chem([Permut('0'), Intern(''), ])	,	Chem([Intern('')])),
		(Chem([Permut('0'), Sub('0'), ])	,	Chem([Sub('3'), Permut('0'), ])),
		(Chem([Permut('0'), Sub('1'), ])	,	Chem([Sub('2'), Permut('0'), ])),
		(Chem([Permut('0'), Sub('2'), ])	,	Chem([Sub('1'), Permut('0'), ])),
		(Chem([Permut('0'), Sub('3'), ])	,	Chem([Sub('0'), Permut('0'), ])),
		]
	
	
	etat21.prim.elems = [Figure(1, [Chem([Bord('0')]), Chem([Bord('1')]), ])]
	etat21.grid.elems = [Figure(1, [Chem([Bord('0')]), Chem([Intern('')]), Chem([Bord('1')]), ])]
	
	
	etat21.space = [Chem([Bord('0'), Intern('0'), Intern('0'), ]), Chem([Intern('0'), Intern('0'), ]), Chem([Bord('1'), Intern('0'), Intern('0'), ]), ]
	
	etat21.initMat[Chem([Sub('0')])] = FMat([
		[Coef('Const', 1           ), Coef('Const', 0.75        ), Coef('Const', 0.5625      ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Const', 0.375       ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.0625      ), ], ])
	etat21.initMat[Chem([Sub('1')])] = FMat([
		[Coef('Const', 0.5625      ), Coef('Const', 0.375       ), Coef('Const', 0.25        ), ], 
		[Coef('Const', 0.375       ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0.0625      ), Coef('Const', 0.125       ), Coef('Const', 0.25        ), ], ])
	etat21.initMat[Chem([Sub('2')])] = FMat([
		[Coef('Const', 0.25        ), Coef('Const', 0.125       ), Coef('Const', 0.0625      ), ], 
		[Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0.375       ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0.375       ), Coef('Const', 0.5625      ), ], ])
	etat21.initMat[Chem([Sub('3')])] = FMat([
		[Coef('Const', 0.0625      ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.375       ), Coef('Const', 0.25        ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.5625      ), Coef('Const', 0.75        ), Coef('Const', 1           ), ], ])
	etat21.initMat[Chem([Sub('G')])] = FMat([
		[Coef('Const', 0           )], 
		[Coef('Const', 1           )], 
		[Coef('Const', 0           )], ])
	
	
	
	etat22.bords   = {Bord('0'): etat23, Bord('1'): etat23, }
	etat22.permuts = {Permut('0'): etat22, }
	etat22.interns = {Intern('_'): etat22, }
	etat22.subs    = {Sub('0'): etat22, Sub('1'): etat22, Sub('2'): etat22, Sub('3'): etat22, Sub('4'): etat22, Sub('G', True): Etat.etatPoint, }
	
	etat22.buildIntern()
	etat22.fm_[Permut('0')] = PMat(3, [2, 1, 0, ])
	
	
	etat22.eqs = [
		(Chem([Permut('0'), Bord('0'), ])	,	Chem([Bord('1')])),
		(Chem([Permut('0'), Bord('1'), ])	,	Chem([Bord('0')])),
		(Chem([Permut('0'), Intern(''), ])	,	Chem([Intern('')])),
		(Chem([Permut('0'), Sub('0'), ])	,	Chem([Sub('4'), Permut('0'), ])),
		(Chem([Permut('0'), Sub('1'), ])	,	Chem([Sub('3'), Permut('0'), ])),
		(Chem([Permut('0'), Sub('2'), ])	,	Chem([Sub('2'), Permut('0'), ])),
		(Chem([Permut('0'), Sub('3'), ])	,	Chem([Sub('1'), Permut('0'), ])),
		(Chem([Permut('0'), Sub('4'), ])	,	Chem([Sub('0'), Permut('0'), ])),
		]
	
	
	etat22.prim.elems = [Figure(1, [Chem([Bord('0')]), Chem([Bord('1')]), ])]
	etat22.grid.elems = [Figure(1, [Chem([Bord('0')]), Chem([Intern('')]), Chem([Bord('1')]), ])]
	
	
	etat22.space = [Chem([Bord('0'), Intern('0'), Intern('0'), ]), Chem([Intern('0'), Intern('0'), ]), Chem([Bord('1'), Intern('0'), Intern('0'), ]), ]
	
	etat22.initMat[Chem([Sub('0')])] = FMat([
		[Coef('Const', 1           ), Coef('Const', 0.8         ), Coef('Const', 0.64        ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.2         ), Coef('Const', 0.32        ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.04        ), ], ])
	etat22.initMat[Chem([Sub('1')])] = FMat([
		[Coef('Const', 0.64        ), Coef('Const', 0.48        ), Coef('Const', 0.36        ), ], 
		[Coef('Const', 0.32        ), Coef('Const', 0.44        ), Coef('Const', 0.48        ), ], 
		[Coef('Const', 0.04        ), Coef('Const', 0.08        ), Coef('Const', 0.16        ), ], ])
	etat22.initMat[Chem([Sub('2')])] = FMat([
		[Coef('Const', 0.36        ), Coef('Const', 0.24        ), Coef('Const', 0.16        ), ], 
		[Coef('Const', 0.48        ), Coef('Const', 0.52        ), Coef('Const', 0.48        ), ], 
		[Coef('Const', 0.16        ), Coef('Const', 0.24        ), Coef('Const', 0.36        ), ], ])
	etat22.initMat[Chem([Sub('3')])] = FMat([
		[Coef('Const', 0.16        ), Coef('Const', 0.08        ), Coef('Const', 0.04        ), ], 
		[Coef('Const', 0.48        ), Coef('Const', 0.44        ), Coef('Const', 0.32        ), ], 
		[Coef('Const', 0.36        ), Coef('Const', 0.48        ), Coef('Const', 0.64        ), ], ])
	etat22.initMat[Chem([Sub('4')])] = FMat([
		[Coef('Const', 0.04        ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.32        ), Coef('Const', 0.2         ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.64        ), Coef('Const', 0.8         ), Coef('Const', 1           ), ], ])
	etat22.initMat[Chem([Sub('G')])] = FMat([
		[Coef('Const', 0           )], 
		[Coef('Const', 1           )], 
		[Coef('Const', 0           )], ])
	
	
	
	etat23.bords   = {}
	etat23.permuts = {}
	etat23.interns = {Intern('_'): etat23, }
	etat23.subs    = {Sub('0'): etat23, Sub('G', True): Etat.etatPoint, }
	
	etat23.buildIntern()
	
	
	etat23.eqs = [
		]
	
	
	etat23.prim.elems = []
	etat23.grid.elems = []
	
	
	etat23.space = [Chem([Intern('0'), Intern('0'), ])]
	
	etat23.initMat[Chem([Sub('0')])] = FMat([[Coef('Var'  , 1           )]])
	etat23.initMat[Chem([Sub('G')])] = FMat([[Coef('Const', 1           )]])
	
	
	
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
