# -*- coding: utf-8 -*-

# Automatically generated, from file : dodecahedron.py, function : modele()

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
	
	
	etat0.subs   = {Sub('0'): etat1, Sub('1'): etat1, Sub('2'): etat1, Sub('3'): etat1, Sub('4'): etat1, Sub('5'): etat1, Sub('6'): etat1, Sub('7'): etat1, Sub('8'): etat1, Sub('9'): etat1, Sub('10'): etat1, Sub('11'): etat1, }
	
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
		[Coef('Var'  ,-2.50223     ), Coef('Var'  ,-3.37025     ), Coef('Var'  ,-3.84549     ), Coef('Var'  ,-3.56695     ), Coef('Var'  ,-2.89965     ), Coef('Var'  ,-2.18238     ), Coef('Var'  ,-0.979402    ), Coef('Var'  ,-1.14768     ), Coef('Var'  ,-0.725238    ), Coef('Var'  ,-1.87405     ), ], 
		[Coef('Var'  , 2.31847     ), Coef('Var'  , 2.27703     ), Coef('Var'  , 1.58803     ), Coef('Var'  , 2.49571     ), Coef('Var'  , 2.78392     ), Coef('Var'  , 3.77622     ), Coef('Var'  , 4.2967      ), Coef('Var'  , 4.39437     ), Coef('Var'  , 3.96713     ), Coef('Var'  , 3.41366     ), ], 
		[Coef('Var'  , 5.6633      ), Coef('Var'  , 4.6603      ), Coef('Var'  , 3.63565     ), Coef('Var'  , 2.70683     ), Coef('Var'  , 1.60258     ), Coef('Var'  , 2.1467      ), Coef('Var'  , 2.43543     ), Coef('Var'  , 3.7388      ), Coef('Var'  , 4.91665     ), Coef('Var'  , 5.26728     ), ], 
		[Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), ], ])
	etat0.initMat[Chem([Sub('1')])] = FMat([
		[Coef('Var'  ,-0.209482    ), Coef('Var'  ,-0.111001    ), Coef('Var'  , 0.426824    ), Coef('Var'  ,-0.726671    ), Coef('Var'  ,-1.48822     ), Coef('Var'  ,-2.49995     ), Coef('Var'  ,-3.29015     ), Coef('Var'  ,-2.99378     ), Coef('Var'  ,-2.50223     ), Coef('Var'  ,-1.51793     ), ], 
		[Coef('Var'  , 2.29684     ), Coef('Var'  , 1.09918     ), Coef('Var'  ,-0.109951    ), Coef('Var'  ,-0.761903    ), Coef('Var'  ,-1.58823     ), Coef('Var'  ,-0.743295    ), Coef('Var'  ,-0.0849399   ), Coef('Var'  , 1.12155     ), Coef('Var'  , 2.31847     ), Coef('Var'  , 2.26008     ), ], 
		[Coef('Var'  , 6.75072     ), Coef('Var'  , 7.30865     ), Coef('Var'  , 7.23128     ), Coef('Var'  , 7.16074     ), Coef('Var'  , 6.46053     ), Coef('Var'  , 6.31339     ), Coef('Var'  , 5.48073     ), Coef('Var'  , 5.9403      ), Coef('Var'  , 5.6633      ), Coef('Var'  , 6.54748     ), ], 
		[Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), ], ])
	etat0.initMat[Chem([Sub('2')])] = FMat([
		[Coef('Var'  , 1.0941      ), Coef('Var'  ,-0.177036    ), Coef('Var'  ,-1.22677     ), Coef('Var'  ,-2.04565     ), Coef('Var'  ,-2.83475     ), Coef('Var'  ,-2.19216     ), Coef('Var'  ,-1.48822     ), Coef('Var'  ,-0.381964    ), Coef('Var'  , 0.920139    ), Coef('Var'  , 0.860539    ), ], 
		[Coef('Var'  ,-3.63618     ), Coef('Var'  ,-3.87598     ), Coef('Var'  ,-3.60972     ), Coef('Var'  ,-3.28588     ), Coef('Var'  ,-2.37511     ), Coef('Var'  ,-2.33876     ), Coef('Var'  ,-1.58823     ), Coef('Var'  ,-2.31886     ), Coef('Var'  ,-2.35968     ), Coef('Var'  ,-3.31465     ), ], 
		[Coef('Var'  , 3.99553     ), Coef('Var'  , 3.68615     ), Coef('Var'  , 2.91618     ), Coef('Var'  , 3.91032     ), Coef('Var'  , 4.47012     ), Coef('Var'  , 5.62729     ), Coef('Var'  , 6.46053     ), Coef('Var'  , 6.41719     ), Coef('Var'  , 6.17081     ), Coef('Var'  , 5.25506     ), ], 
		[Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), ], ])
	etat0.initMat[Chem([Sub('3')])] = FMat([
		[Coef('Var'  , 3.78736     ), Coef('Var'  , 3.84238     ), Coef('Var'  , 3.18676     ), Coef('Var'  , 3.51543     ), Coef('Var'  , 3.03114     ), Coef('Var'  , 3.61264     ), Coef('Var'  , 3.46279     ), Coef('Var'  , 4.08395     ), Coef('Var'  , 3.99773     ), Coef('Var'  , 4.23638     ), ], 
		[Coef('Var'  , 0.305097    ), Coef('Var'  , 1.58349     ), Coef('Var'  , 2.727       ), Coef('Var'  , 2.90873     ), Coef('Var'  , 3.01365     ), Coef('Var'  , 1.91662     ), Coef('Var'  , 0.72128     ), Coef('Var'  , 0.0271401   ), Coef('Var'  ,-0.93506     ), Coef('Var'  ,-0.162863    ), ], 
		[Coef('Var'  , 4.88532     ), Coef('Var'  , 4.56305     ), Coef('Var'  , 4.43884     ), Coef('Var'  , 3.18591     ), Coef('Var'  , 1.93656     ), Coef('Var'  , 1.42333     ), Coef('Var'  , 0.821516    ), Coef('Var'  , 1.76692     ), Coef('Var'  , 2.68323     ), Coef('Var'  , 3.72882     ), ], 
		[Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), ], ])
	etat0.initMat[Chem([Sub('4')])] = FMat([
		[Coef('Var'  , 2.99389     ), Coef('Var'  , 3.67748     ), Coef('Var'  , 3.99773     ), Coef('Var'  , 3.58274     ), Coef('Var'  , 2.68561     ), Coef('Var'  , 2.08045     ), Coef('Var'  , 0.925806    ), Coef('Var'  , 1.31297     ), Coef('Var'  , 1.0941      ), Coef('Var'  , 2.29465     ), ], 
		[Coef('Var'  ,-2.10563     ), Coef('Var'  ,-1.83354     ), Coef('Var'  ,-0.93506     ), Coef('Var'  ,-1.67041     ), Coef('Var'  ,-1.74632     ), Coef('Var'  ,-2.89082     ), Coef('Var'  ,-3.47405     ), Coef('Var'  ,-3.84504     ), Coef('Var'  ,-3.63618     ), Coef('Var'  ,-3.12258     ), ], 
		[Coef('Var'  , 4.71241     ), Coef('Var'  , 3.60863     ), Coef('Var'  , 2.68323     ), Coef('Var'  , 1.6714      ), Coef('Var'  , 0.720914    ), Coef('Var'  , 1.11847     ), Coef('Var'  , 1.52075     ), Coef('Var'  , 2.71475     ), Coef('Var'  , 3.99553     ), Coef('Var'  , 4.23085     ), ], 
		[Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), ], ])
	etat0.initMat[Chem([Sub('5')])] = FMat([
		[Coef('Var'  , 3.18676     ), Coef('Var'  , 2.76928     ), Coef('Var'  , 2.19217     ), Coef('Var'  , 1.11553     ), Coef('Var'  ,-0.209482    ), Coef('Var'  ,-0.284313    ), Coef('Var'  ,-0.725238    ), Coef('Var'  , 0.470242    ), Coef('Var'  , 1.36038     ), Coef('Var'  , 2.33466     ), ], 
		[Coef('Var'  , 2.727       ), Coef('Var'  , 2.45252     ), Coef('Var'  , 1.52259     ), Coef('Var'  , 2.23108     ), Coef('Var'  , 2.29684     ), Coef('Var'  , 3.40706     ), Coef('Var'  , 3.96713     ), Coef('Var'  , 4.29878     ), Coef('Var'  , 4.20895     ), Coef('Var'  , 3.71776     ), ], 
		[Coef('Var'  , 4.43884     ), Coef('Var'  , 5.6357      ), Coef('Var'  , 6.45085     ), Coef('Var'  , 6.75254     ), Coef('Var'  , 6.75072     ), Coef('Var'  , 6.03265     ), Coef('Var'  , 4.91665     ), Coef('Var'  , 4.44922     ), Coef('Var'  , 3.46931     ), Coef('Var'  , 4.22152     ), ], 
		[Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), ], ])
	etat0.initMat[Chem([Sub('6')])] = FMat([
		[Coef('Var'  , 3.03114     ), Coef('Var'  , 2.21347     ), Coef('Var'  , 1.36038     ), Coef('Var'  , 0.302117    ), Coef('Var'  ,-0.979402    ), Coef('Var'  ,-0.739463    ), Coef('Var'  ,-0.767448    ), Coef('Var'  , 0.545019    ), Coef('Var'  , 1.66046     ), Coef('Var'  , 2.42353     ), ], 
		[Coef('Var'  , 3.01365     ), Coef('Var'  , 3.9213      ), Coef('Var'  , 4.20895     ), Coef('Var'  , 4.52552     ), Coef('Var'  , 4.2967      ), Coef('Var'  , 4.09382     ), Coef('Var'  , 3.12191     ), Coef('Var'  , 3.06728     ), Coef('Var'  , 2.30866     ), Coef('Var'  , 3.06025     ), ], 
		[Coef('Var'  , 1.93656     ), Coef('Var'  , 2.48396     ), Coef('Var'  , 3.46931     ), Coef('Var'  , 2.72762     ), Coef('Var'  , 2.43543     ), Coef('Var'  , 1.17187     ), Coef('Var'  , 0.315261    ), Coef('Var'  , 5.78127e-09 ), Coef('Var'  , 0.0686457   ), Coef('Var'  , 0.796296    ), ], 
		[Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), ], ])
	etat0.initMat[Chem([Sub('7')])] = FMat([
		[Coef('Var'  ,-3.14465     ), Coef('Var'  ,-3.78827     ), Coef('Var'  ,-3.74529     ), Coef('Var'  ,-4.16372     ), Coef('Var'  ,-3.84549     ), Coef('Var'  ,-3.90604     ), Coef('Var'  ,-3.29015     ), Coef('Var'  ,-3.43149     ), Coef('Var'  ,-2.83475     ), Coef('Var'  ,-3.3965      ), ], 
		[Coef('Var'  ,-2.14649     ), Coef('Var'  ,-0.968216    ), Coef('Var'  , 0.326565    ), Coef('Var'  , 0.827377    ), Coef('Var'  , 1.58803     ), Coef('Var'  , 0.605057    ), Coef('Var'  ,-0.0849399   ), Coef('Var'  ,-1.28317     ), Coef('Var'  ,-2.37511     ), Coef('Var'  ,-2.31525     ), ], 
		[Coef('Var'  , 2.00689     ), Coef('Var'  , 1.8422      ), Coef('Var'  , 1.4628      ), Coef('Var'  , 2.60241     ), Coef('Var'  , 3.63565     ), Coef('Var'  , 4.52733     ), Coef('Var'  , 5.48073     ), Coef('Var'  , 4.93464     ), Coef('Var'  , 4.47012     ), Coef('Var'  , 3.28175     ), ], 
		[Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), ], ])
	etat0.initMat[Chem([Sub('8')])] = FMat([
		[Coef('Var'  , 3.46279     ), Coef('Var'  , 2.70003     ), Coef('Var'  , 1.66046     ), Coef('Var'  , 0.837308    ), Coef('Var'  ,-0.284848    ), Coef('Var'  , 0.237198    ), Coef('Var'  , 0.294723    ), Coef('Var'  , 1.60911     ), Coef('Var'  , 2.68561     ), Coef('Var'  , 3.15094     ), ], 
		[Coef('Var'  , 0.72128     ), Coef('Var'  , 1.4594      ), Coef('Var'  , 2.30866     ), Coef('Var'  , 1.33421     ), Coef('Var'  , 0.705487    ), Coef('Var'  ,-0.46666     ), Coef('Var'  ,-1.74643     ), Coef('Var'  ,-1.69143     ), Coef('Var'  ,-1.74632     ), Coef('Var'  ,-0.519106    ), ], 
		[Coef('Var'  , 0.821516    ), Coef('Var'  , 0.0173293   ), Coef('Var'  , 0.0686457   ), Coef('Var'  , 8.65859e-09 ), Coef('Var'  , 9.9359e-09  ), Coef('Var'  , 2.34409e-08 ), Coef('Var'  , 1.86568e-09 ), Coef('Var'  , 3.89689e-08 ), Coef('Var'  , 0.720914    ), Coef('Var'  , 0.389151    ), ], 
		[Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), ], ])
	etat0.initMat[Chem([Sub('9')])] = FMat([
		[Coef('Var'  ,-2.14307     ), Coef('Var'  ,-2.77196     ), Coef('Var'  ,-3.14465     ), Coef('Var'  ,-2.24766     ), Coef('Var'  ,-1.22677     ), Coef('Var'  ,-0.306349    ), Coef('Var'  , 0.925806    ), Coef('Var'  , 0.436609    ), Coef('Var'  , 0.294723    ), Coef('Var'  ,-1.0311      ), ], 
		[Coef('Var'  ,-0.988915    ), Coef('Var'  ,-1.92849     ), Coef('Var'  ,-2.14649     ), Coef('Var'  ,-3.13078     ), Coef('Var'  ,-3.60972     ), Coef('Var'  ,-3.78395     ), Coef('Var'  ,-3.47405     ), Coef('Var'  ,-2.94903     ), Coef('Var'  ,-1.74643     ), Coef('Var'  ,-1.6819      ), ], 
		[Coef('Var'  , 0.169465    ), Coef('Var'  , 0.787423    ), Coef('Var'  , 2.00689     ), Coef('Var'  , 2.19615     ), Coef('Var'  , 2.91618     ), Coef('Var'  , 1.96379     ), Coef('Var'  , 1.52075     ), Coef('Var'  , 0.445354    ), Coef('Var'  , 1.86568e-09 ), Coef('Var'  , 6.92035e-08 ), ], 
		[Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), ], ])
	etat0.initMat[Chem([Sub('10')])] = FMat([
		[Coef('Var'  , 2.19217     ), Coef('Var'  , 3.15843     ), Coef('Var'  , 3.78736     ), Coef('Var'  , 3.54491     ), Coef('Var'  , 2.99389     ), Coef('Var'  , 2.17159     ), Coef('Var'  , 0.920139    ), Coef('Var'  , 0.940249    ), Coef('Var'  , 0.426824    ), Coef('Var'  , 1.55317     ), ], 
		[Coef('Var'  , 1.52259     ), Coef('Var'  , 0.755039    ), Coef('Var'  , 0.305097    ), Coef('Var'  ,-0.975372    ), Coef('Var'  ,-2.10563     ), Coef('Var'  ,-2.24497     ), Coef('Var'  ,-2.35968     ), Coef('Var'  ,-1.30046     ), Coef('Var'  ,-0.109951    ), Coef('Var'  , 0.56248     ), ], 
		[Coef('Var'  , 6.45085     ), Coef('Var'  , 5.95843     ), Coef('Var'  , 4.88532     ), Coef('Var'  , 5.13321     ), Coef('Var'  , 4.71241     ), Coef('Var'  , 5.74159     ), Coef('Var'  , 6.17081     ), Coef('Var'  , 6.96601     ), Coef('Var'  , 7.23128     ), Coef('Var'  , 7.08951     ), ], 
		[Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), ], ])
	etat0.initMat[Chem([Sub('11')])] = FMat([
		[Coef('Var'  ,-3.74529     ), Coef('Var'  ,-3.17409     ), Coef('Var'  ,-2.14307     ), Coef('Var'  ,-1.39521     ), Coef('Var'  ,-0.284848    ), Coef('Var'  ,-0.787262    ), Coef('Var'  ,-0.767448    ), Coef('Var'  ,-2.07824     ), Coef('Var'  ,-2.89965     ), Coef('Var'  ,-3.46005     ), ], 
		[Coef('Var'  , 0.326565    ), Coef('Var'  ,-0.205072    ), Coef('Var'  ,-0.988915    ), Coef('Var'  , 0.0502932   ), Coef('Var'  , 0.705487    ), Coef('Var'  , 1.88636     ), Coef('Var'  , 3.12191     ), Coef('Var'  , 3.03225     ), Coef('Var'  , 2.78392     ), Coef('Var'  , 1.62523     ), ], 
		[Coef('Var'  , 1.4628      ), Coef('Var'  , 0.408486    ), Coef('Var'  , 0.169465    ), Coef('Var'  , 1.87221e-08 ), Coef('Var'  , 9.9359e-09  ), Coef('Var'  , 2.54951e-08 ), Coef('Var'  , 0.315261    ), Coef('Var'  , 0.588209    ), Coef('Var'  , 1.60258     ), Coef('Var'  , 1.19055     ), ], 
		[Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), ], ])
	
	
	
	etat1.bords   = {Bord('0'): etat2, Bord('1'): etat2, Bord('2'): etat2, Bord('3'): etat2, Bord('4'): etat2, }
	etat1.permuts = {}
	etat1.interns = {Intern('_'): etat1, }
	etat1.subs    = {Sub('0'): etat1, Sub('1'): etat1, Sub('2'): etat1, Sub('3'): etat1, Sub('4'): etat1, Sub('5'): etat1, Sub('6'): etat1, Sub('7'): etat1, Sub('8'): etat1, Sub('9'): etat1, Sub('10'): etat1, Sub('G', True): Etat.etatPoint, }
	
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
		[Coef('Const', 0.25        ), Coef('Var'  , 0.214994    ), Coef('Var'  , 0.180586    ), Coef('Var'  , 0.180407    ), Coef('Var'  , 0.181335    ), Coef('Var'  , 0.215413    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0562657   ), Coef('Var'  , 0.112985    ), Coef('Var'  , 0.181355    ), Coef('Var'  , 0.250903    ), Coef('Var'  , 0.375089    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0396983   ), Coef('Var'  , 0.0794176   ), Coef('Var'  , 0.117612    ), Coef('Var'  , 0.156077    ), Coef('Var'  , 0.202914    ), Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0202137   ), Coef('Var'  , 0.0401128   ), Coef('Var'  , 0.0477924   ), Coef('Var'  , 0.055087    ), Coef('Var'  , 0.0275787   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.017374    ), Coef('Var'  , 0.0344006   ), Coef('Var'  , 0.038155    ), Coef('Var'  , 0.0413968   ), Coef('Var'  , 0.0207809   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0198273   ), Coef('Var'  , 0.0389741   ), Coef('Var'  , 0.0395225   ), Coef('Var'  , 0.0387397   ), Coef('Var'  , 0.0196952   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0242139   ), Coef('Var'  , 0.0480496   ), Coef('Var'  , 0.0443705   ), Coef('Var'  , 0.0398997   ), Coef('Var'  , 0.0201565   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0295062   ), Coef('Var'  , 0.0588067   ), Coef('Var'  , 0.0520832   ), Coef('Var'  , 0.0446055   ), Coef('Var'  , 0.0225771   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.25        ), Coef('Var'  , 0.201894    ), Coef('Var'  , 0.154094    ), Coef('Var'  , 0.115777    ), Coef('Var'  , 0.0777961   ), Coef('Var'  , 0.0388826   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.5         ), Coef('Var'  , 0.376013    ), Coef('Var'  , 0.252573    ), Coef('Var'  , 0.182926    ), Coef('Var'  , 0.114161    ), Coef('Var'  , 0.0569134   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), ], ])
	etat1.initMat[Chem([Sub('1')])] = FMat([
		[Coef('Var'  , 0.11449     ), Coef('Var'  , 0.112097    ), Coef('Var'  , 0.110019    ), Coef('Var'  , 0.132197    ), Coef('Var'  , 0.154517    ), Coef('Var'  , 0.167603    ), Coef('Var'  , 0.181335    ), Coef('Var'  , 0.162827    ), Coef('Var'  , 0.145507    ), Coef('Var'  , 0.129505    ), ], 
		[Coef('Var'  , 0.125463    ), Coef('Var'  , 0.135512    ), Coef('Var'  , 0.147017    ), Coef('Var'  , 0.198116    ), Coef('Var'  , 0.250745    ), Coef('Var'  , 0.250086    ), Coef('Var'  , 0.250903    ), Coef('Var'  , 0.198367    ), Coef('Var'  , 0.147291    ), Coef('Var'  , 0.135671    ), ], 
		[Coef('Var'  , 0.119953    ), Coef('Var'  , 0.135243    ), Coef('Var'  , 0.151327    ), Coef('Var'  , 0.167468    ), Coef('Var'  , 0.184525    ), Coef('Var'  , 0.169966    ), Coef('Var'  , 0.156077    ), Coef('Var'  , 0.134249    ), Coef('Var'  , 0.112853    ), Coef('Var'  , 0.116162    ), ], 
		[Coef('Var'  , 0.101568    ), Coef('Var'  , 0.122269    ), Coef('Var'  , 0.143884    ), Coef('Var'  , 0.126904    ), Coef('Var'  , 0.110999    ), Coef('Var'  , 0.0828704   ), Coef('Var'  , 0.055087    ), Coef('Var'  , 0.0619991   ), Coef('Var'  , 0.0686493   ), Coef('Var'  , 0.0850766   ), ], 
		[Coef('Var'  , 0.0827464   ), Coef('Var'  , 0.0911009   ), Coef('Var'  , 0.100235    ), Coef('Var'  , 0.0855571   ), Coef('Var'  , 0.0716998   ), Coef('Var'  , 0.0564958   ), Coef('Var'  , 0.0413968   ), Coef('Var'  , 0.0498852   ), Coef('Var'  , 0.0579701   ), Coef('Var'  , 0.0703628   ), ], 
		[Coef('Var'  , 0.0857281   ), Coef('Var'  , 0.0811784   ), Coef('Var'  , 0.0756733   ), Coef('Var'  , 0.0604052   ), Coef('Var'  , 0.0443686   ), Coef('Var'  , 0.0420816   ), Coef('Var'  , 0.0387397   ), Coef('Var'  , 0.0524722   ), Coef('Var'  , 0.0647043   ), Coef('Var'  , 0.0759366   ), ], 
		[Coef('Var'  , 0.0826325   ), Coef('Var'  , 0.0749711   ), Coef('Var'  , 0.0666234   ), Coef('Var'  , 0.0531764   ), Coef('Var'  , 0.0390854   ), Coef('Var'  , 0.0398619   ), Coef('Var'  , 0.0398997   ), Coef('Var'  , 0.0544641   ), Coef('Var'  , 0.0681342   ), Coef('Var'  , 0.0758075   ), ], 
		[Coef('Var'  , 0.0846159   ), Coef('Var'  , 0.0749634   ), Coef('Var'  , 0.0637218   ), Coef('Var'  , 0.0519866   ), Coef('Var'  , 0.0385893   ), Coef('Var'  , 0.0422465   ), Coef('Var'  , 0.0446055   ), Coef('Var'  , 0.0605439   ), Coef('Var'  , 0.0754178   ), Coef('Var'  , 0.0806129   ), ], 
		[Coef('Var'  , 0.0944263   ), Coef('Var'  , 0.0813784   ), Coef('Var'  , 0.0675634   ), Coef('Var'  , 0.0579603   ), Coef('Var'  , 0.0473806   ), Coef('Var'  , 0.0627706   ), Coef('Var'  , 0.0777961   ), Coef('Var'  , 0.0938123   ), Coef('Var'  , 0.110048    ), Coef('Var'  , 0.102236    ), ], 
		[Coef('Var'  , 0.108377    ), Coef('Var'  , 0.0912881   ), Coef('Var'  , 0.0739361   ), Coef('Var'  , 0.0662297   ), Coef('Var'  , 0.05809     ), Coef('Var'  , 0.0860187   ), Coef('Var'  , 0.114161    ), Coef('Var'  , 0.131381    ), Coef('Var'  , 0.149425    ), Coef('Var'  , 0.128631    ), ], ])
	etat1.initMat[Chem([Sub('2')])] = FMat([
		[Coef('Var'  , 0.106163    ), Coef('Var'  , 0.0901731   ), Coef('Var'  , 0.074909    ), Coef('Var'  , 0.0596796   ), Coef('Var'  , 0.0445389   ), Coef('Var'  , 0.0543873   ), Coef('Var'  , 0.063748    ), Coef('Var'  , 0.0770967   ), Coef('Var'  , 0.0902197   ), Coef('Var'  , 0.0979143   ), ], 
		[Coef('Var'  , 0.0745635   ), Coef('Var'  , 0.0598698   ), Coef('Var'  , 0.0442317   ), Coef('Var'  , 0.0420575   ), Coef('Var'  , 0.0385951   ), Coef('Var'  , 0.0519173   ), Coef('Var'  , 0.0635711   ), Coef('Var'  , 0.0744496   ), Coef('Var'  , 0.0838486   ), Coef('Var'  , 0.0797063   ), ], 
		[Coef('Var'  , 0.0701384   ), Coef('Var'  , 0.056576    ), Coef('Var'  , 0.041858    ), Coef('Var'  , 0.0427202   ), Coef('Var'  , 0.0423783   ), Coef('Var'  , 0.0573955   ), Coef('Var'  , 0.0711309   ), Coef('Var'  , 0.0791545   ), Coef('Var'  , 0.0859834   ), Coef('Var'  , 0.0786164   ), ], 
		[Coef('Var'  , 0.055956    ), Coef('Var'  , 0.0451662   ), Coef('Var'  , 0.0333915   ), Coef('Var'  , 0.0366601   ), Coef('Var'  , 0.0392462   ), Coef('Var'  , 0.0534668   ), Coef('Var'  , 0.0674323   ), Coef('Var'  , 0.0715605   ), Coef('Var'  , 0.0754684   ), Coef('Var'  , 0.0660603   ), ], 
		[Coef('Var'  , 0.0587734   ), Coef('Var'  , 0.050795    ), Coef('Var'  , 0.0421997   ), Coef('Var'  , 0.057457    ), Coef('Var'  , 0.0726166   ), Coef('Var'  , 0.0866581   ), Coef('Var'  , 0.101305    ), Coef('Var'  , 0.0921843   ), Coef('Var'  , 0.0836185   ), Coef('Var'  , 0.0713098   ), ], 
		[Coef('Var'  , 0.0768527   ), Coef('Var'  , 0.0687076   ), Coef('Var'  , 0.0598195   ), Coef('Var'  , 0.087234    ), Coef('Var'  , 0.114806    ), Coef('Var'  , 0.132147    ), Coef('Var'  , 0.150443    ), Coef('Var'  , 0.130334    ), Coef('Var'  , 0.11076     ), Coef('Var'  , 0.0940782   ), ], 
		[Coef('Var'  , 0.113808    ), Coef('Var'  , 0.135541    ), Coef('Var'  , 0.157167    ), Coef('Var'  , 0.170795    ), Coef('Var'  , 0.184754    ), Coef('Var'  , 0.167422    ), Coef('Var'  , 0.150813    ), Coef('Var'  , 0.135035    ), Coef('Var'  , 0.119761    ), Coef('Var'  , 0.116794    ), ], 
		[Coef('Var'  , 0.1478      ), Coef('Var'  , 0.198644    ), Coef('Var'  , 0.251001    ), Coef('Var'  , 0.250196    ), Coef('Var'  , 0.250897    ), Coef('Var'  , 0.198452    ), Coef('Var'  , 0.147444    ), Coef('Var'  , 0.136177    ), Coef('Var'  , 0.126207    ), Coef('Var'  , 0.136338    ), ], 
		[Coef('Var'  , 0.146973    ), Coef('Var'  , 0.163722    ), Coef('Var'  , 0.181771    ), Coef('Var'  , 0.167675    ), Coef('Var'  , 0.154403    ), Coef('Var'  , 0.1322      ), Coef('Var'  , 0.110369    ), Coef('Var'  , 0.112916    ), Coef('Var'  , 0.115961    ), Coef('Var'  , 0.130924    ), ], 
		[Coef('Var'  , 0.148973    ), Coef('Var'  , 0.130805    ), Coef('Var'  , 0.113651    ), Coef('Var'  , 0.0855263   ), Coef('Var'  , 0.0577645   ), Coef('Var'  , 0.0659529   ), Coef('Var'  , 0.0737453   ), Coef('Var'  , 0.0910925   ), Coef('Var'  , 0.108173    ), Coef('Var'  , 0.128259    ), ], ])
	etat1.initMat[Chem([Sub('3')])] = FMat([
		[Coef('Var'  , 0.112712    ), Coef('Var'  , 0.10116     ), Coef('Var'  , 0.0902197   ), Coef('Var'  , 0.0848751   ), Coef('Var'  , 0.0792414   ), Coef('Var'  , 0.0864645   ), Coef('Var'  , 0.0930634   ), Coef('Var'  , 0.103745    ), Coef('Var'  , 0.11449     ), Coef('Var'  , 0.113185    ), ], 
		[Coef('Var'  , 0.107392    ), Coef('Var'  , 0.0958302   ), Coef('Var'  , 0.0838486   ), Coef('Var'  , 0.084352    ), Coef('Var'  , 0.0837146   ), Coef('Var'  , 0.0956145   ), Coef('Var'  , 0.107142    ), Coef('Var'  , 0.115869    ), Coef('Var'  , 0.125463    ), Coef('Var'  , 0.11601     ), ], 
		[Coef('Var'  , 0.0977196   ), Coef('Var'  , 0.0922031   ), Coef('Var'  , 0.0859834   ), Coef('Var'  , 0.0929606   ), Coef('Var'  , 0.099091    ), Coef('Var'  , 0.110028    ), Coef('Var'  , 0.120853    ), Coef('Var'  , 0.120154    ), Coef('Var'  , 0.119953    ), Coef('Var'  , 0.10877     ), ], 
		[Coef('Var'  , 0.0760459   ), Coef('Var'  , 0.0759745   ), Coef('Var'  , 0.0754684   ), Coef('Var'  , 0.0879663   ), Coef('Var'  , 0.100657    ), Coef('Var'  , 0.11009     ), Coef('Var'  , 0.120557    ), Coef('Var'  , 0.110604    ), Coef('Var'  , 0.101568    ), Coef('Var'  , 0.0888068   ), ], 
		[Coef('Var'  , 0.071144    ), Coef('Var'  , 0.0774077   ), Coef('Var'  , 0.0836185   ), Coef('Var'  , 0.0938364   ), Coef('Var'  , 0.104874    ), Coef('Var'  , 0.103889    ), Coef('Var'  , 0.104362    ), Coef('Var'  , 0.09306     ), Coef('Var'  , 0.0827464   ), Coef('Var'  , 0.0769174   ), ], 
		[Coef('Var'  , 0.0862723   ), Coef('Var'  , 0.0988621   ), Coef('Var'  , 0.11076     ), Coef('Var'  , 0.119699    ), Coef('Var'  , 0.129068    ), Coef('Var'  , 0.119229    ), Coef('Var'  , 0.109921    ), Coef('Var'  , 0.0980849   ), Coef('Var'  , 0.0857281   ), Coef('Var'  , 0.0866261   ), ], 
		[Coef('Var'  , 0.0968365   ), Coef('Var'  , 0.108388    ), Coef('Var'  , 0.119761    ), Coef('Var'  , 0.119002    ), Coef('Var'  , 0.118579    ), Coef('Var'  , 0.106685    ), Coef('Var'  , 0.0949572   ), Coef('Var'  , 0.0890136   ), Coef('Var'  , 0.0826325   ), Coef('Var'  , 0.0900574   ), ], 
		[Coef('Var'  , 0.108377    ), Coef('Var'  , 0.11697     ), Coef('Var'  , 0.126207    ), Coef('Var'  , 0.116405    ), Coef('Var'  , 0.107361    ), Coef('Var'  , 0.0958081   ), Coef('Var'  , 0.0838514   ), Coef('Var'  , 0.0848568   ), Coef('Var'  , 0.0846159   ), Coef('Var'  , 0.0968086   ), ], 
		[Coef('Var'  , 0.115846    ), Coef('Var'  , 0.115526    ), Coef('Var'  , 0.115961    ), Coef('Var'  , 0.105142    ), Coef('Var'  , 0.0945054   ), Coef('Var'  , 0.0887627   ), Coef('Var'  , 0.082322    ), Coef('Var'  , 0.088723    ), Coef('Var'  , 0.0944263   ), Coef('Var'  , 0.105036    ), ], 
		[Coef('Var'  , 0.127654    ), Coef('Var'  , 0.117679    ), Coef('Var'  , 0.108173    ), Coef('Var'  , 0.0957614   ), Coef('Var'  , 0.0829088   ), Coef('Var'  , 0.083428    ), Coef('Var'  , 0.082972    ), Coef('Var'  , 0.0958899   ), Coef('Var'  , 0.108377    ), Coef('Var'  , 0.117783    ), ], ])
	etat1.initMat[Chem([Sub('4')])] = FMat([
		[Coef('Var'  , 0.074909    ), Coef('Var'  , 0.112933    ), Coef('Var'  , 0.15169     ), Coef('Var'  , 0.200609    ), Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0373239   ), ], 
		[Coef('Var'  , 0.0442317   ), Coef('Var'  , 0.0517009   ), Coef('Var'  , 0.0584454   ), Coef('Var'  , 0.0293242   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0223767   ), ], 
		[Coef('Var'  , 0.041858    ), Coef('Var'  , 0.0458795   ), Coef('Var'  , 0.0489113   ), Coef('Var'  , 0.0246601   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0212194   ), ], 
		[Coef('Var'  , 0.0333915   ), Coef('Var'  , 0.0339859   ), Coef('Var'  , 0.0336186   ), Coef('Var'  , 0.0170561   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0169298   ), ], 
		[Coef('Var'  , 0.0421997   ), Coef('Var'  , 0.0388606   ), Coef('Var'  , 0.0348439   ), Coef('Var'  , 0.0176264   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0212342   ), ], 
		[Coef('Var'  , 0.0598195   ), Coef('Var'  , 0.0529004   ), Coef('Var'  , 0.0452382   ), Coef('Var'  , 0.0228754   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.030025    ), ], 
		[Coef('Var'  , 0.157167    ), Coef('Var'  , 0.118775    ), Coef('Var'  , 0.0802162   ), Coef('Var'  , 0.0401979   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.203577    ), ], 
		[Coef('Var'  , 0.251001    ), Coef('Var'  , 0.181409    ), Coef('Var'  , 0.113107    ), Coef('Var'  , 0.0562951   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.375113    ), ], 
		[Coef('Var'  , 0.181771    ), Coef('Var'  , 0.181126    ), Coef('Var'  , 0.181668    ), Coef('Var'  , 0.215532    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.215594    ), ], 
		[Coef('Var'  , 0.113651    ), Coef('Var'  , 0.18243     ), Coef('Var'  , 0.252261    ), Coef('Var'  , 0.375824    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0566063   ), ], ])
	etat1.initMat[Chem([Sub('5')])] = FMat([
		[Coef('Var'  , 0.0445389   ), Coef('Var'  , 0.0223557   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0190773   ), Coef('Var'  , 0.0377777   ), Coef('Var'  , 0.041433    ), ], 
		[Coef('Var'  , 0.0385951   ), Coef('Var'  , 0.0196808   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0196618   ), Coef('Var'  , 0.0385577   ), Coef('Var'  , 0.0393427   ), ], 
		[Coef('Var'  , 0.0423783   ), Coef('Var'  , 0.0215008   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0252762   ), Coef('Var'  , 0.0500306   ), Coef('Var'  , 0.046777    ), ], 
		[Coef('Var'  , 0.0392462   ), Coef('Var'  , 0.0197303   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0270362   ), Coef('Var'  , 0.0541103   ), Coef('Var'  , 0.0467665   ), ], 
		[Coef('Var'  , 0.0726166   ), Coef('Var'  , 0.0362228   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.199234    ), Coef('Var'  , 0.148903    ), Coef('Var'  , 0.110456    ), ], 
		[Coef('Var'  , 0.114806    ), Coef('Var'  , 0.0572089   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.376102    ), Coef('Var'  , 0.252844    ), Coef('Var'  , 0.183311    ), ], 
		[Coef('Var'  , 0.184754    ), Coef('Var'  , 0.217218    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.216918    ), Coef('Var'  , 0.184222    ), Coef('Var'  , 0.184135    ), ], 
		[Coef('Var'  , 0.250897    ), Coef('Var'  , 0.375082    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0560743   ), Coef('Var'  , 0.11265     ), Coef('Var'  , 0.181157    ), ], 
		[Coef('Var'  , 0.154403    ), Coef('Var'  , 0.202081    ), Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0390169   ), Coef('Var'  , 0.0780247   ), Coef('Var'  , 0.116098    ), ], 
		[Coef('Var'  , 0.0577645   ), Coef('Var'  , 0.02892     ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.021604    ), Coef('Var'  , 0.0428801   ), Coef('Var'  , 0.050524    ), ], ])
	etat1.initMat[Chem([Sub('6')])] = FMat([
		[Coef('Var'  , 0.0781572   ), Coef('Var'  , 0.0391372   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.20219     ), Coef('Var'  , 0.154517    ), Coef('Var'  , 0.116327    ), ], 
		[Coef('Var'  , 0.112721    ), Coef('Var'  , 0.0561133   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.374997    ), Coef('Var'  , 0.250745    ), Coef('Var'  , 0.18111     ), ], 
		[Coef('Var'  , 0.184966    ), Coef('Var'  , 0.217304    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.217052    ), Coef('Var'  , 0.184525    ), Coef('Var'  , 0.184356    ), ], 
		[Coef('Var'  , 0.249389    ), Coef('Var'  , 0.374388    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0552917   ), Coef('Var'  , 0.110999    ), Coef('Var'  , 0.179679    ), ], 
		[Coef('Var'  , 0.148159    ), Coef('Var'  , 0.198825    ), Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0357148   ), Coef('Var'  , 0.0716998   ), Coef('Var'  , 0.10954     ), ], 
		[Coef('Var'  , 0.0588619   ), Coef('Var'  , 0.0294903   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0223864   ), Coef('Var'  , 0.0443686   ), Coef('Var'  , 0.0518767   ), ], 
		[Coef('Var'  , 0.0464215   ), Coef('Var'  , 0.0233074   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0197053   ), Coef('Var'  , 0.0390854   ), Coef('Var'  , 0.0430127   ), ], 
		[Coef('Var'  , 0.0381835   ), Coef('Var'  , 0.0194333   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0196694   ), Coef('Var'  , 0.0385893   ), Coef('Var'  , 0.0391027   ), ], 
		[Coef('Var'  , 0.0400974   ), Coef('Var'  , 0.0203125   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0238879   ), Coef('Var'  , 0.0473806   ), Coef('Var'  , 0.0442004   ), ], 
		[Coef('Var'  , 0.0430434   ), Coef('Var'  , 0.0216894   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0291053   ), Coef('Var'  , 0.05809     ), Coef('Var'  , 0.0507947   ), ], ])
	etat1.initMat[Chem([Sub('7')])] = FMat([
		[Coef('Var'  , 0.063748    ), Coef('Var'  , 0.0511089   ), Coef('Var'  , 0.0377777   ), Coef('Var'  , 0.0388265   ), Coef('Var'  , 0.0389891   ), Coef('Var'  , 0.0530472   ), Coef('Var'  , 0.0660256   ), Coef('Var'  , 0.073108    ), Coef('Var'  , 0.0792414   ), Coef('Var'  , 0.0718417   ), ], 
		[Coef('Var'  , 0.0635711   ), Coef('Var'  , 0.0518983   ), Coef('Var'  , 0.0385577   ), Coef('Var'  , 0.0419487   ), Coef('Var'  , 0.0440626   ), Coef('Var'  , 0.0596349   ), Coef('Var'  , 0.0742976   ), Coef('Var'  , 0.0794868   ), Coef('Var'  , 0.0837146   ), Coef('Var'  , 0.0743752   ), ], 
		[Coef('Var'  , 0.0711309   ), Coef('Var'  , 0.0611709   ), Coef('Var'  , 0.0500306   ), Coef('Var'  , 0.06596     ), Coef('Var'  , 0.0811678   ), Coef('Var'  , 0.0981704   ), Coef('Var'  , 0.114904    ), Coef('Var'  , 0.107187    ), Coef('Var'  , 0.099091    ), Coef('Var'  , 0.0855955   ), ], 
		[Coef('Var'  , 0.0674323   ), Coef('Var'  , 0.0607728   ), Coef('Var'  , 0.0541103   ), Coef('Var'  , 0.0819553   ), Coef('Var'  , 0.110319    ), Coef('Var'  , 0.126157    ), Coef('Var'  , 0.143208    ), Coef('Var'  , 0.12138     ), Coef('Var'  , 0.100657    ), Coef('Var'  , 0.0838789   ), ], 
		[Coef('Var'  , 0.101305    ), Coef('Var'  , 0.124669    ), Coef('Var'  , 0.148903    ), Coef('Var'  , 0.162049    ), Coef('Var'  , 0.176345    ), Coef('Var'  , 0.156286    ), Coef('Var'  , 0.137889    ), Coef('Var'  , 0.120557    ), Coef('Var'  , 0.104874    ), Coef('Var'  , 0.102523    ), ], 
		[Coef('Var'  , 0.150443    ), Coef('Var'  , 0.20104     ), Coef('Var'  , 0.252844    ), Coef('Var'  , 0.252043    ), Coef('Var'  , 0.252547    ), Coef('Var'  , 0.200555    ), Coef('Var'  , 0.14985     ), Coef('Var'  , 0.138918    ), Coef('Var'  , 0.129068    ), Coef('Var'  , 0.139242    ), ], 
		[Coef('Var'  , 0.150813    ), Coef('Var'  , 0.167123    ), Coef('Var'  , 0.184222    ), Coef('Var'  , 0.169385    ), Coef('Var'  , 0.15519     ), Coef('Var'  , 0.132961    ), Coef('Var'  , 0.111181    ), Coef('Var'  , 0.114666    ), Coef('Var'  , 0.118579    ), Coef('Var'  , 0.134377    ), ], 
		[Coef('Var'  , 0.147444    ), Coef('Var'  , 0.129444    ), Coef('Var'  , 0.11265     ), Coef('Var'  , 0.0848234   ), Coef('Var'  , 0.0574666   ), Coef('Var'  , 0.0657132   ), Coef('Var'  , 0.0736659   ), Coef('Var'  , 0.0905616   ), Coef('Var'  , 0.107361    ), Coef('Var'  , 0.126967    ), ], 
		[Coef('Var'  , 0.110369    ), Coef('Var'  , 0.0941367   ), Coef('Var'  , 0.0780247   ), Coef('Var'  , 0.0628389   ), Coef('Var'  , 0.0472882   ), Coef('Var'  , 0.0577916   ), Coef('Var'  , 0.0674137   ), Coef('Var'  , 0.0813153   ), Coef('Var'  , 0.0945054   ), Coef('Var'  , 0.102465    ), ], 
		[Coef('Var'  , 0.0737453   ), Coef('Var'  , 0.0586369   ), Coef('Var'  , 0.0428801   ), Coef('Var'  , 0.0401705   ), Coef('Var'  , 0.0366246   ), Coef('Var'  , 0.0496837   ), Coef('Var'  , 0.0615668   ), Coef('Var'  , 0.0728189   ), Coef('Var'  , 0.0829088   ), Coef('Var'  , 0.0787346   ), ], ])
	etat1.initMat[Chem([Sub('8')])] = FMat([
		[Coef('Var'  , 0.0469198   ), Coef('Var'  , 0.062816    ), Coef('Var'  , 0.0781572   ), Coef('Var'  , 0.0941438   ), Coef('Var'  , 0.110019    ), Coef('Var'  , 0.101661    ), Coef('Var'  , 0.0930634   ), Coef('Var'  , 0.0799525   ), Coef('Var'  , 0.0660256   ), Coef('Var'  , 0.0569767   ), ], 
		[Coef('Var'  , 0.0582066   ), Coef('Var'  , 0.0853064   ), Coef('Var'  , 0.112721    ), Coef('Var'  , 0.129232    ), Coef('Var'  , 0.147017    ), Coef('Var'  , 0.126594    ), Coef('Var'  , 0.107142    ), Coef('Var'  , 0.0908237   ), Coef('Var'  , 0.0742976   ), Coef('Var'  , 0.0665411   ), ], 
		[Coef('Var'  , 0.157669    ), Coef('Var'  , 0.17112     ), Coef('Var'  , 0.184966    ), Coef('Var'  , 0.16772     ), Coef('Var'  , 0.151327    ), Coef('Var'  , 0.135744    ), Coef('Var'  , 0.120853    ), Coef('Var'  , 0.117814    ), Coef('Var'  , 0.114904    ), Coef('Var'  , 0.136303    ), ], 
		[Coef('Var'  , 0.249046    ), Coef('Var'  , 0.248588    ), Coef('Var'  , 0.249389    ), Coef('Var'  , 0.196       ), Coef('Var'  , 0.143884    ), Coef('Var'  , 0.131561    ), Coef('Var'  , 0.120557    ), Coef('Var'  , 0.131186    ), Coef('Var'  , 0.143208    ), Coef('Var'  , 0.195438    ), ], 
		[Coef('Var'  , 0.176159    ), Coef('Var'  , 0.161539    ), Coef('Var'  , 0.148159    ), Coef('Var'  , 0.123667    ), Coef('Var'  , 0.100235    ), Coef('Var'  , 0.101644    ), Coef('Var'  , 0.104362    ), Coef('Var'  , 0.120271    ), Coef('Var'  , 0.137889    ), Coef('Var'  , 0.156184    ), ], 
		[Coef('Var'  , 0.114186    ), Coef('Var'  , 0.0863609   ), Coef('Var'  , 0.0588619   ), Coef('Var'  , 0.0675091   ), Coef('Var'  , 0.0756733   ), Coef('Var'  , 0.0929441   ), Coef('Var'  , 0.109921    ), Coef('Var'  , 0.129539    ), Coef('Var'  , 0.14985     ), Coef('Var'  , 0.131485    ), ], 
		[Coef('Var'  , 0.0779575   ), Coef('Var'  , 0.0622394   ), Coef('Var'  , 0.0464215   ), Coef('Var'  , 0.0567785   ), Coef('Var'  , 0.0666234   ), Coef('Var'  , 0.0809847   ), Coef('Var'  , 0.0949572   ), Coef('Var'  , 0.103008    ), Coef('Var'  , 0.111181    ), Coef('Var'  , 0.0944265   ), ], 
		[Coef('Var'  , 0.0432124   ), Coef('Var'  , 0.0412072   ), Coef('Var'  , 0.0381835   ), Coef('Var'  , 0.0517506   ), Coef('Var'  , 0.0637218   ), Coef('Var'  , 0.0745278   ), Coef('Var'  , 0.0838514   ), Coef('Var'  , 0.0791747   ), Coef('Var'  , 0.0736659   ), Coef('Var'  , 0.0587379   ), ], 
		[Coef('Var'  , 0.0399831   ), Coef('Var'  , 0.0405486   ), Coef('Var'  , 0.0400974   ), Coef('Var'  , 0.0543848   ), Coef('Var'  , 0.0675634   ), Coef('Var'  , 0.0754894   ), Coef('Var'  , 0.082322    ), Coef('Var'  , 0.0753867   ), Coef('Var'  , 0.0674137   ), Coef('Var'  , 0.0542058   ), ], 
		[Coef('Var'  , 0.0366602   ), Coef('Var'  , 0.0402741   ), Coef('Var'  , 0.0430434   ), Coef('Var'  , 0.0588138   ), Coef('Var'  , 0.0739361   ), Coef('Var'  , 0.0788506   ), Coef('Var'  , 0.082972    ), Coef('Var'  , 0.0728434   ), Coef('Var'  , 0.0615668   ), Coef('Var'  , 0.0497019   ), ], ])
	etat1.initMat[Chem([Sub('9')])] = FMat([
		[Coef('Var'  , 0.15169     ), Coef('Var'  , 0.128459    ), Coef('Var'  , 0.106163    ), Coef('Var'  , 0.108944    ), Coef('Var'  , 0.112712    ), Coef('Var'  , 0.12851     ), Coef('Var'  , 0.145507    ), Coef('Var'  , 0.162409    ), Coef('Var'  , 0.180586    ), Coef('Var'  , 0.165604    ), ], 
		[Coef('Var'  , 0.0584454   ), Coef('Var'  , 0.0668173   ), Coef('Var'  , 0.0745635   ), Coef('Var'  , 0.0911102   ), Coef('Var'  , 0.107392    ), Coef('Var'  , 0.126895    ), Coef('Var'  , 0.147291    ), Coef('Var'  , 0.129543    ), Coef('Var'  , 0.112985    ), Coef('Var'  , 0.0855899   ), ], 
		[Coef('Var'  , 0.0489113   ), Coef('Var'  , 0.0600167   ), Coef('Var'  , 0.0701384   ), Coef('Var'  , 0.0842999   ), Coef('Var'  , 0.0977196   ), Coef('Var'  , 0.105278    ), Coef('Var'  , 0.112853    ), Coef('Var'  , 0.0960333   ), Coef('Var'  , 0.0794176   ), Coef('Var'  , 0.0643584   ), ], 
		[Coef('Var'  , 0.0336186   ), Coef('Var'  , 0.0452924   ), Coef('Var'  , 0.055956    ), Coef('Var'  , 0.0663869   ), Coef('Var'  , 0.0760459   ), Coef('Var'  , 0.072571    ), Coef('Var'  , 0.0686493   ), Coef('Var'  , 0.0546341   ), Coef('Var'  , 0.0401128   ), Coef('Var'  , 0.0372698   ), ], 
		[Coef('Var'  , 0.0348439   ), Coef('Var'  , 0.0471873   ), Coef('Var'  , 0.0587734   ), Coef('Var'  , 0.0652196   ), Coef('Var'  , 0.071144    ), Coef('Var'  , 0.064763    ), Coef('Var'  , 0.0579701   ), Coef('Var'  , 0.0464783   ), Coef('Var'  , 0.0344006   ), Coef('Var'  , 0.0350005   ), ], 
		[Coef('Var'  , 0.0452382   ), Coef('Var'  , 0.061558    ), Coef('Var'  , 0.0768527   ), Coef('Var'  , 0.0821491   ), Coef('Var'  , 0.0862723   ), Coef('Var'  , 0.0762435   ), Coef('Var'  , 0.0647043   ), Coef('Var'  , 0.0526043   ), Coef('Var'  , 0.0389741   ), Coef('Var'  , 0.0427027   ), ], 
		[Coef('Var'  , 0.0802162   ), Coef('Var'  , 0.0971616   ), Coef('Var'  , 0.113808    ), Coef('Var'  , 0.105521    ), Coef('Var'  , 0.0968365   ), Coef('Var'  , 0.082865    ), Coef('Var'  , 0.0681342   ), Coef('Var'  , 0.0585215   ), Coef('Var'  , 0.0480496   ), Coef('Var'  , 0.0644118   ), ], 
		[Coef('Var'  , 0.113107    ), Coef('Var'  , 0.129825    ), Coef('Var'  , 0.1478      ), Coef('Var'  , 0.127693    ), Coef('Var'  , 0.108377    ), Coef('Var'  , 0.0921292   ), Coef('Var'  , 0.0754178   ), Coef('Var'  , 0.0674729   ), Coef('Var'  , 0.0588067   ), Coef('Var'  , 0.0858012   ), ], 
		[Coef('Var'  , 0.181668    ), Coef('Var'  , 0.16366     ), Coef('Var'  , 0.146973    ), Coef('Var'  , 0.130858    ), Coef('Var'  , 0.115846    ), Coef('Var'  , 0.11266     ), Coef('Var'  , 0.110048    ), Coef('Var'  , 0.131824    ), Coef('Var'  , 0.154094    ), Coef('Var'  , 0.167426    ), ], 
		[Coef('Var'  , 0.252261    ), Coef('Var'  , 0.200023    ), Coef('Var'  , 0.148973    ), Coef('Var'  , 0.137818    ), Coef('Var'  , 0.127654    ), Coef('Var'  , 0.138086    ), Coef('Var'  , 0.149425    ), Coef('Var'  , 0.20048     ), Coef('Var'  , 0.252573    ), Coef('Var'  , 0.251836    ), ], ])
	etat1.initMat[Chem([Sub('10')])] = FMat([
		[Coef('Const', 0           ), Coef('Var'  , 0.0236788   ), Coef('Var'  , 0.0469198   ), Coef('Var'  , 0.043428    ), Coef('Var'  , 0.0389891   ), Coef('Var'  , 0.0197492   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0291931   ), Coef('Var'  , 0.0582066   ), Coef('Var'  , 0.05148     ), Coef('Var'  , 0.0440626   ), Coef('Var'  , 0.0222869   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.25        ), Coef('Var'  , 0.203816    ), Coef('Var'  , 0.157669    ), Coef('Var'  , 0.1195      ), Coef('Var'  , 0.0811678   ), Coef('Var'  , 0.0406838   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.5         ), Coef('Var'  , 0.3742      ), Coef('Var'  , 0.249046    ), Coef('Var'  , 0.179119    ), Coef('Var'  , 0.110319    ), Coef('Var'  , 0.0549191   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0.25        ), Coef('Var'  , 0.212714    ), Coef('Var'  , 0.176159    ), Coef('Var'  , 0.17553     ), Coef('Var'  , 0.176345    ), Coef('Var'  , 0.212816    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0568705   ), Coef('Var'  , 0.114186    ), Coef('Var'  , 0.182812    ), Coef('Var'  , 0.252547    ), Coef('Var'  , 0.375941    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.038932    ), Coef('Var'  , 0.0779575   ), Coef('Var'  , 0.116399    ), Coef('Var'  , 0.15519     ), Coef('Var'  , 0.202467    ), Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0217738   ), Coef('Var'  , 0.0432124   ), Coef('Var'  , 0.050523    ), Coef('Var'  , 0.0574666   ), Coef('Var'  , 0.0287492   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0202361   ), Coef('Var'  , 0.0399831   ), Coef('Var'  , 0.044058    ), Coef('Var'  , 0.0472882   ), Coef('Var'  , 0.0238219   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0185848   ), Coef('Var'  , 0.0366602   ), Coef('Var'  , 0.0371513   ), Coef('Var'  , 0.0366246   ), Coef('Var'  , 0.0185665   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], ])
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
