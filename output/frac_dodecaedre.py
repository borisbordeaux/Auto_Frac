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
	
	
	etat0.subs   = {Sub('0'): etat1, Sub('1'): etat1, Sub('2'): etat1, Sub('3'): etat1, Sub('4'): etat1, Sub('5'): etat1, Sub('6'): etat1, Sub('7'): etat1, Sub('8'): etat1, Sub('9'): etat1, Sub('10'): etat1, Sub('11'): etat1, }
	
	etat0.eqs = [
		(Chem([Sub('0'), Bord('0'), Permut('0'), ])	,	Chem([Sub('4'), Bord('2'), ])),
		(Chem([Sub('0'), Bord('1'), Permut('0'), ])	,	Chem([Sub('10'), Bord('4'), ])),
		(Chem([Sub('0'), Bord('2'), Permut('0'), ])	,	Chem([Sub('1'), Bord('4'), ])),
		(Chem([Sub('0'), Bord('3'), Permut('0'), ])	,	Chem([Sub('11'), Bord('3'), ])),
		(Chem([Sub('0'), Bord('4'), Permut('0'), ])	,	Chem([Sub('5'), Bord('0'), ])),
		(Chem([Sub('1'), Bord('0'), Permut('0'), ])	,	Chem([Sub('10'), Bord('3'), ])),
		(Chem([Sub('1'), Bord('1'), Permut('0'), ])	,	Chem([Sub('8'), Bord('4'), ])),
		(Chem([Sub('1'), Bord('2'), Permut('0'), ])	,	Chem([Sub('9'), Bord('2'), ])),
		(Chem([Sub('1'), Bord('3'), Permut('0'), ])	,	Chem([Sub('11'), Bord('4'), ])),
		(Chem([Sub('2'), Bord('0'), Permut('0'), ])	,	Chem([Sub('10'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('1'), Permut('0'), ])	,	Chem([Sub('4'), Bord('0'), ])),
		(Chem([Sub('2'), Bord('2'), Permut('0'), ])	,	Chem([Sub('7'), Bord('0'), ])),
		(Chem([Sub('2'), Bord('3'), Permut('0'), ])	,	Chem([Sub('3'), Bord('4'), ])),
		(Chem([Sub('2'), Bord('4'), Permut('0'), ])	,	Chem([Sub('8'), Bord('1'), ])),
		(Chem([Sub('3'), Bord('0'), Permut('0'), ])	,	Chem([Sub('7'), Bord('4'), ])),
		(Chem([Sub('3'), Bord('1'), Permut('0'), ])	,	Chem([Sub('6'), Bord('2'), ])),
		(Chem([Sub('3'), Bord('2'), Permut('0'), ])	,	Chem([Sub('9'), Bord('4'), ])),
		(Chem([Sub('3'), Bord('3'), Permut('0'), ])	,	Chem([Sub('8'), Bord('2'), ])),
		(Chem([Sub('4'), Bord('1'), Permut('0'), ])	,	Chem([Sub('10'), Bord('0'), ])),
		(Chem([Sub('4'), Bord('3'), Permut('0'), ])	,	Chem([Sub('5'), Bord('4'), ])),
		(Chem([Sub('4'), Bord('4'), Permut('0'), ])	,	Chem([Sub('7'), Bord('1'), ])),
		(Chem([Sub('5'), Bord('1'), Permut('0'), ])	,	Chem([Sub('11'), Bord('2'), ])),
		(Chem([Sub('5'), Bord('2'), Permut('0'), ])	,	Chem([Sub('6'), Bord('4'), ])),
		(Chem([Sub('5'), Bord('3'), Permut('0'), ])	,	Chem([Sub('7'), Bord('2'), ])),
		(Chem([Sub('6'), Bord('0'), Permut('0'), ])	,	Chem([Sub('11'), Bord('1'), ])),
		(Chem([Sub('6'), Bord('1'), Permut('0'), ])	,	Chem([Sub('9'), Bord('0'), ])),
		(Chem([Sub('6'), Bord('3'), Permut('0'), ])	,	Chem([Sub('7'), Bord('3'), ])),
		(Chem([Sub('8'), Bord('0'), Permut('0'), ])	,	Chem([Sub('10'), Bord('2'), ])),
		(Chem([Sub('8'), Bord('3'), Permut('0'), ])	,	Chem([Sub('9'), Bord('3'), ])),
		(Chem([Sub('9'), Bord('1'), Permut('0'), ])	,	Chem([Sub('11'), Bord('0'), ])),
		]
	
	
	etat0.space = []
	
	etat0.initMat[Chem([Sub('0')])] = FMat([
		[Coef('Var'  ,-1.41618     ), Coef('Var'  ,-1.0985      ), Coef('Var'  ,-0.53518     ), Coef('Var'  , 0.728719    ), Coef('Var'  , 1.89907     ), Coef('Var'  , 2.46017     ), Coef('Var'  , 2.62178     ), Coef('Var'  , 1.68661     ), Coef('Var'  , 0.551911    ), Coef('Var'  ,-0.455157    ), ], 
		[Coef('Var'  ,-0.681332    ), Coef('Var'  ,-1.89362     ), Coef('Var'  ,-2.76865     ), Coef('Var'  ,-2.88513     ), Coef('Var'  ,-2.52482     ), Coef('Var'  ,-1.55402     ), Coef('Var'  ,-0.308983    ), Coef('Var'  , 0.323516    ), Coef('Var'  , 0.85979     ), Coef('Var'  , 0.112901    ), ], 
		[Coef('Var'  , 0.133249    ), Coef('Var'  , 0.27503     ), Coef('Var'  , 0.989828    ), Coef('Var'  , 0.950189    ), Coef('Var'  , 1.2796      ), Coef('Var'  , 0.686171    ), Coef('Var'  , 0.543355    ), Coef('Var'  , 3.14452e-09 ), Coef('Var'  , 1.72488e-08 ), Coef('Var'  , 3.0023e-08  ), ], 
		[Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), ], ])
	etat0.initMat[Chem([Sub('1')])] = FMat([
		[Coef('Var'  , 1.89907     ), Coef('Var'  , 2.29919     ), Coef('Var'  , 2.34447     ), Coef('Var'  , 3.06279     ), Coef('Var'  , 3.29764     ), Coef('Var'  , 3.66987     ), Coef('Var'  , 3.45872     ), Coef('Var'  , 3.32395     ), Coef('Var'  , 2.62178     ), Coef('Var'  , 2.46017     ), ], 
		[Coef('Var'  ,-2.52482     ), Coef('Var'  ,-2.76896     ), Coef('Var'  ,-2.54374     ), Coef('Var'  ,-1.5961      ), Coef('Var'  ,-0.37582     ), Coef('Var'  , 0.370339    ), Coef('Var'  , 1.05489     ), Coef('Var'  , 0.405047    ), Coef('Var'  ,-0.308983    ), Coef('Var'  ,-1.55402     ), ], 
		[Coef('Var'  , 1.2796      ), Coef('Var'  , 2.45685     ), Coef('Var'  , 3.70525     ), Coef('Var'  , 4.14392     ), Coef('Var'  , 4.3908      ), Coef('Var'  , 3.43797     ), Coef('Var'  , 2.39386     ), Coef('Var'  , 1.31722     ), Coef('Var'  , 0.543355    ), Coef('Var'  , 0.686171    ), ], 
		[Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), ], ])
	etat0.initMat[Chem([Sub('2')])] = FMat([
		[Coef('Var'  , 0.207053    ), Coef('Var'  ,-0.764739    ), Coef('Var'  ,-1.57809     ), Coef('Var'  ,-2.54535     ), Coef('Var'  ,-3.05943     ), Coef('Var'  ,-2.87288     ), Coef('Var'  ,-2.17358     ), Coef('Var'  ,-1.2978      ), Coef('Var'  ,-0.162036    ), Coef('Var'  , 0.0107846   ), ], 
		[Coef('Var'  ,-2.80662     ), Coef('Var'  ,-3.13202     ), Coef('Var'  ,-2.92344     ), Coef('Var'  ,-2.13303     ), Coef('Var'  ,-0.983432    ), Coef('Var'  ,-0.37006     ), Coef('Var'  , 0.316467    ), Coef('Var'  ,-0.274724    ), Coef('Var'  ,-0.820447    ), Coef('Var'  ,-1.98939     ), ], 
		[Coef('Var'  , 4.90681     ), Coef('Var'  , 4.16265     ), Coef('Var'  , 3.2139      ), Coef('Var'  , 3.4251      ), Coef('Var'  , 3.57365     ), Coef('Var'  , 4.66497     ), Coef('Var'  , 5.46876     ), Coef('Var'  , 6.16312     ), Coef('Var'  , 6.31126     ), Coef('Var'  , 5.85132     ), ], 
		[Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), ], ])
	etat0.initMat[Chem([Sub('3')])] = FMat([
		[Coef('Var'  ,-2.17358     ), Coef('Var'  ,-2.03194     ), Coef('Var'  ,-1.51849     ), Coef('Var'  ,-0.347057    ), Coef('Var'  , 0.916559    ), Coef('Var'  , 1.43876     ), Coef('Var'  , 1.74939     ), Coef('Var'  , 0.851312    ), Coef('Var'  ,-0.162036    ), Coef('Var'  ,-1.2978      ), ], 
		[Coef('Var'  , 0.316467    ), Coef('Var'  , 1.55231     ), Coef('Var'  , 2.52689     ), Coef('Var'  , 2.88259     ), Coef('Var'  , 2.75837     ), Coef('Var'  , 1.88316     ), Coef('Var'  , 0.688634    ), Coef('Var'  ,-0.0729101   ), Coef('Var'  ,-0.820447    ), Coef('Var'  ,-0.274724    ), ], 
		[Coef('Var'  , 5.46876     ), Coef('Var'  , 5.22924     ), Coef('Var'  , 4.6075      ), Coef('Var'  , 4.93382     ), Coef('Var'  , 4.93263     ), Coef('Var'  , 5.68686     ), Coef('Var'  , 5.98408     ), Coef('Var'  , 6.449       ), Coef('Var'  , 6.31126     ), Coef('Var'  , 6.16312     ), ], 
		[Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), ], ])
	etat0.initMat[Chem([Sub('4')])] = FMat([
		[Coef('Var'  ,-3.05943     ), Coef('Var'  ,-2.54535     ), Coef('Var'  ,-1.57809     ), Coef('Var'  ,-1.17182     ), Coef('Var'  ,-0.53518     ), Coef('Var'  ,-1.0985      ), Coef('Var'  ,-1.41618     ), Coef('Var'  ,-2.4494      ), Coef('Var'  ,-2.99449     ), Coef('Var'  ,-3.32993     ), ], 
		[Coef('Var'  ,-0.983432    ), Coef('Var'  ,-2.13303     ), Coef('Var'  ,-2.92344     ), Coef('Var'  ,-3.11632     ), Coef('Var'  ,-2.76865     ), Coef('Var'  ,-1.89362     ), Coef('Var'  ,-0.681332    ), Coef('Var'  ,-0.137438    ), Coef('Var'  , 0.451785    ), Coef('Var'  ,-0.296086    ), ], 
		[Coef('Var'  , 3.57365     ), Coef('Var'  , 3.4251      ), Coef('Var'  , 3.2139      ), Coef('Var'  , 2.02729     ), Coef('Var'  , 0.989828    ), Coef('Var'  , 0.27503     ), Coef('Var'  , 0.133249    ), Coef('Var'  , 0.602793    ), Coef('Var'  , 1.57861     ), Coef('Var'  , 2.54529     ), ], 
		[Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), ], ])
	etat0.initMat[Chem([Sub('5')])] = FMat([
		[Coef('Var'  ,-1.41618     ), Coef('Var'  ,-0.455157    ), Coef('Var'  , 0.551911    ), Coef('Var'  , 0.373159    ), Coef('Var'  , 0.147396    ), Coef('Var'  ,-1.04775     ), Coef('Var'  ,-2.01598     ), Coef('Var'  ,-2.74876     ), Coef('Var'  ,-2.99449     ), Coef('Var'  ,-2.4494      ), ], 
		[Coef('Var'  ,-0.681332    ), Coef('Var'  , 0.112901    ), Coef('Var'  , 0.85979     ), Coef('Var'  , 2.08173     ), Coef('Var'  , 2.95793     ), Coef('Var'  , 3.05224     ), Coef('Var'  , 2.62737     ), Coef('Var'  , 1.67875     ), Coef('Var'  , 0.451785    ), Coef('Var'  ,-0.137438    ), ], 
		[Coef('Var'  , 0.133249    ), Coef('Var'  , 3.0023e-08  ), Coef('Var'  , 1.72488e-08 ), Coef('Var'  , 0.216032    ), Coef('Var'  , 1.08493     ), Coef('Var'  , 1.49886     ), Coef('Var'  , 2.19901     ), Coef('Var'  , 1.77596     ), Coef('Var'  , 1.57861     ), Coef('Var'  , 0.602793    ), ], 
		[Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), ], ])
	etat0.initMat[Chem([Sub('6')])] = FMat([
		[Coef('Var'  , 0.147396    ), Coef('Var'  , 1.14697     ), Coef('Var'  , 1.97313     ), Coef('Var'  , 1.56274     ), Coef('Var'  , 0.916559    ), Coef('Var'  ,-0.347057    ), Coef('Var'  ,-1.51849     ), Coef('Var'  ,-1.94293     ), Coef('Var'  ,-2.01598     ), Coef('Var'  ,-1.04775     ), ], 
		[Coef('Var'  , 2.95793     ), Coef('Var'  , 3.26356     ), Coef('Var'  , 2.99942     ), Coef('Var'  , 3.13858     ), Coef('Var'  , 2.75837     ), Coef('Var'  , 2.88259     ), Coef('Var'  , 2.52689     ), Coef('Var'  , 2.81009     ), Coef('Var'  , 2.62737     ), Coef('Var'  , 3.05224     ), ], 
		[Coef('Var'  , 1.08493     ), Coef('Var'  , 1.79545     ), Coef('Var'  , 2.71651     ), Coef('Var'  , 3.90914     ), Coef('Var'  , 4.93263     ), Coef('Var'  , 4.93382     ), Coef('Var'  , 4.6075      ), Coef('Var'  , 3.44612     ), Coef('Var'  , 2.19901     ), Coef('Var'  , 1.49886     ), ], 
		[Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), ], ])
	etat0.initMat[Chem([Sub('7')])] = FMat([
		[Coef('Var'  ,-2.17358     ), Coef('Var'  ,-2.87288     ), Coef('Var'  ,-3.05943     ), Coef('Var'  ,-3.32993     ), Coef('Var'  ,-2.99449     ), Coef('Var'  ,-2.74876     ), Coef('Var'  ,-2.01598     ), Coef('Var'  ,-1.94293     ), Coef('Var'  ,-1.51849     ), Coef('Var'  ,-2.03194     ), ], 
		[Coef('Var'  , 0.316467    ), Coef('Var'  ,-0.37006     ), Coef('Var'  ,-0.983432    ), Coef('Var'  ,-0.296086    ), Coef('Var'  , 0.451785    ), Coef('Var'  , 1.67875     ), Coef('Var'  , 2.62737     ), Coef('Var'  , 2.81009     ), Coef('Var'  , 2.52689     ), Coef('Var'  , 1.55231     ), ], 
		[Coef('Var'  , 5.46876     ), Coef('Var'  , 4.66497     ), Coef('Var'  , 3.57365     ), Coef('Var'  , 2.54529     ), Coef('Var'  , 1.57861     ), Coef('Var'  , 1.77596     ), Coef('Var'  , 2.19901     ), Coef('Var'  , 3.44612     ), Coef('Var'  , 4.6075      ), Coef('Var'  , 5.22924     ), ], 
		[Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), ], ])
	etat0.initMat[Chem([Sub('8')])] = FMat([
		[Coef('Var'  , 2.34447     ), Coef('Var'  , 1.37874     ), Coef('Var'  , 0.207053    ), Coef('Var'  , 0.0107846   ), Coef('Var'  ,-0.162036    ), Coef('Var'  , 0.851312    ), Coef('Var'  , 1.74939     ), Coef('Var'  , 2.74142     ), Coef('Var'  , 3.29764     ), Coef('Var'  , 3.06279     ), ], 
		[Coef('Var'  ,-2.54374     ), Coef('Var'  ,-2.92174     ), Coef('Var'  ,-2.80662     ), Coef('Var'  ,-1.98939     ), Coef('Var'  ,-0.820447    ), Coef('Var'  ,-0.0729101   ), Coef('Var'  , 0.688634    ), Coef('Var'  , 0.164256    ), Coef('Var'  ,-0.37582     ), Coef('Var'  ,-1.5961      ), ], 
		[Coef('Var'  , 3.70525     ), Coef('Var'  , 4.42912     ), Coef('Var'  , 4.90681     ), Coef('Var'  , 5.85132     ), Coef('Var'  , 6.31126     ), Coef('Var'  , 6.449       ), Coef('Var'  , 5.98408     ), Coef('Var'  , 5.3948      ), Coef('Var'  , 4.3908      ), Coef('Var'  , 4.14392     ), ], 
		[Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), ], ])
	etat0.initMat[Chem([Sub('9')])] = FMat([
		[Coef('Var'  , 0.916559    ), Coef('Var'  , 1.56274     ), Coef('Var'  , 1.97313     ), Coef('Var'  , 2.94207     ), Coef('Var'  , 3.45872     ), Coef('Var'  , 3.66987     ), Coef('Var'  , 3.29764     ), Coef('Var'  , 2.74142     ), Coef('Var'  , 1.74939     ), Coef('Var'  , 1.43876     ), ], 
		[Coef('Var'  , 2.75837     ), Coef('Var'  , 3.13858     ), Coef('Var'  , 2.99942     ), Coef('Var'  , 2.20948     ), Coef('Var'  , 1.05489     ), Coef('Var'  , 0.370339    ), Coef('Var'  ,-0.37582     ), Coef('Var'  , 0.164256    ), Coef('Var'  , 0.688634    ), Coef('Var'  , 1.88316     ), ], 
		[Coef('Var'  , 4.93263     ), Coef('Var'  , 3.90914     ), Coef('Var'  , 2.71651     ), Coef('Var'  , 2.50516     ), Coef('Var'  , 2.39386     ), Coef('Var'  , 3.43797     ), Coef('Var'  , 4.3908      ), Coef('Var'  , 5.3948      ), Coef('Var'  , 5.98408     ), Coef('Var'  , 5.68686     ), ], 
		[Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), ], ])
	etat0.initMat[Chem([Sub('10')])] = FMat([
		[Coef('Var'  ,-0.53518     ), Coef('Var'  ,-1.17182     ), Coef('Var'  ,-1.57809     ), Coef('Var'  ,-0.764739    ), Coef('Var'  , 0.207053    ), Coef('Var'  , 1.37874     ), Coef('Var'  , 2.34447     ), Coef('Var'  , 2.29919     ), Coef('Var'  , 1.89907     ), Coef('Var'  , 0.728719    ), ], 
		[Coef('Var'  ,-2.76865     ), Coef('Var'  ,-3.11632     ), Coef('Var'  ,-2.92344     ), Coef('Var'  ,-3.13202     ), Coef('Var'  ,-2.80662     ), Coef('Var'  ,-2.92174     ), Coef('Var'  ,-2.54374     ), Coef('Var'  ,-2.76896     ), Coef('Var'  ,-2.52482     ), Coef('Var'  ,-2.88513     ), ], 
		[Coef('Var'  , 0.989828    ), Coef('Var'  , 2.02729     ), Coef('Var'  , 3.2139      ), Coef('Var'  , 4.16265     ), Coef('Var'  , 4.90681     ), Coef('Var'  , 4.42912     ), Coef('Var'  , 3.70525     ), Coef('Var'  , 2.45685     ), Coef('Var'  , 1.2796      ), Coef('Var'  , 0.950189    ), ], 
		[Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), ], ])
	etat0.initMat[Chem([Sub('11')])] = FMat([
		[Coef('Var'  , 3.45872     ), Coef('Var'  , 2.94207     ), Coef('Var'  , 1.97313     ), Coef('Var'  , 1.14697     ), Coef('Var'  , 0.147396    ), Coef('Var'  , 0.373159    ), Coef('Var'  , 0.551911    ), Coef('Var'  , 1.68661     ), Coef('Var'  , 2.62178     ), Coef('Var'  , 3.32395     ), ], 
		[Coef('Var'  , 1.05489     ), Coef('Var'  , 2.20948     ), Coef('Var'  , 2.99942     ), Coef('Var'  , 3.26356     ), Coef('Var'  , 2.95793     ), Coef('Var'  , 2.08173     ), Coef('Var'  , 0.85979     ), Coef('Var'  , 0.323516    ), Coef('Var'  ,-0.308983    ), Coef('Var'  , 0.405047    ), ], 
		[Coef('Var'  , 2.39386     ), Coef('Var'  , 2.50516     ), Coef('Var'  , 2.71651     ), Coef('Var'  , 1.79545     ), Coef('Var'  , 1.08493     ), Coef('Var'  , 0.216032    ), Coef('Var'  , 1.72488e-08 ), Coef('Var'  , 3.14452e-09 ), Coef('Var'  , 0.543355    ), Coef('Var'  , 1.31722     ), ], 
		[Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), ], ])
	
	
	
	etat1.bords   = {Bord('0'): etat2, Bord('1'): etat2, Bord('2'): etat2, Bord('3'): etat2, Bord('4'): etat2, }
	etat1.permuts = {}
	etat1.interns = {Intern('_'): etat1, }
	etat1.subs    = {Sub('0'): etat1, Sub('1'): etat1, Sub('2'): etat1, Sub('3'): etat1, Sub('4'): etat1, Sub('5'): etat1, Sub('6'): etat1, Sub('7'): etat1, Sub('8'): etat1, Sub('9'): etat1, Sub('10'): etat1, Sub('G', True): Etat.etatPoint, }
	
	etat1.buildIntern()
	
	
	etat1.eqs = [
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
	
	
	etat1.prim.elems = [Figure(2, [Chem([Bord('0'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('0'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('0'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('0'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('1'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('1'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('1'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('1'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('2'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('2'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('2'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('2'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('3'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('3'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('3'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('3'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('4'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('4'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('4'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('4'), Sub('1'), Sub('1'), Bord('0'), ]), ])]
	etat1.grid.elems = [
		Figure(1, [Chem([Bord('1'), Bord('0'), ]), Chem([Bord('1'), Intern(''), ]), Chem([Bord('1'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('4'), Bord('0'), ]), Chem([Bord('4'), Intern(''), ]), Chem([Bord('4'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('2'), Bord('0'), ]), Chem([Bord('2'), Intern(''), ]), Chem([Bord('2'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('0'), Bord('0'), ]), Chem([Bord('0'), Intern(''), ]), Chem([Bord('0'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('3'), Bord('0'), ]), Chem([Bord('3'), Intern(''), ]), Chem([Bord('3'), Bord('1'), ]), ]), ]
	
	
	etat1.space = [Chem([Bord('4'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('2'), Intern('0'), Intern('0'), ]), Chem([Bord('2'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('3'), Intern('0'), Intern('0'), ]), Chem([Bord('4'), Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('4'), Intern('0'), Intern('0'), ]), ]
	
	etat1.initMat[Chem([Sub('0')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0165713   ), Coef('Var'  , 0.0331414   ), Coef('Var'  , 0.0372792   ), Coef('Var'  , 0.0414391   ), Coef('Var'  , 0.0207079   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0168034   ), Coef('Var'  , 0.0334476   ), Coef('Var'  , 0.0336167   ), Coef('Var'  , 0.0334652   ), Coef('Var'  , 0.0168133   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.023139    ), Coef('Var'  , 0.0461793   ), Coef('Var'  , 0.0420984   ), Coef('Var'  , 0.0378048   ), Coef('Var'  , 0.0189594   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0275363   ), Coef('Var'  , 0.0550868   ), Coef('Var'  , 0.0467755   ), Coef('Var'  , 0.0384487   ), Coef('Var'  , 0.0192392   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.202803    ), Coef('Var'  , 0.155655    ), Coef('Var'  , 0.116584    ), Coef('Var'  , 0.0775631   ), Coef('Var'  , 0.0387804   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.377919    ), Coef('Var'  , 0.255935    ), Coef('Var'  , 0.186013    ), Coef('Var'  , 0.116253    ), Coef('Var'  , 0.0580938   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.218169    ), Coef('Var'  , 0.186409    ), Coef('Var'  , 0.18634     ), Coef('Var'  , 0.186411    ), Coef('Var'  , 0.218171    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0587094   ), Coef('Var'  , 0.11745     ), Coef('Var'  , 0.187278    ), Coef('Var'  , 0.257194    ), Coef('Var'  , 0.378568    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0386215   ), Coef('Var'  , 0.0772673   ), Coef('Var'  , 0.116288    ), Coef('Var'  , 0.155398    ), Coef('Var'  , 0.202666    ), Coef('Const', 0.25        ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0197279   ), Coef('Var'  , 0.0394288   ), Coef('Var'  , 0.0477287   ), Coef('Var'  , 0.0560234   ), Coef('Var'  , 0.0280008   ), Coef('Const', 0           ), Coef('Const', 0           ), ], ])
	etat1.initMat[Chem([Sub('1')])] = FMat([
		[Coef('Var'  , 0.0580463   ), Coef('Var'  , 0.0496531   ), Coef('Var'  , 0.0413539   ), Coef('Var'  , 0.0579701   ), Coef('Var'  , 0.0747291   ), Coef('Var'  , 0.0901878   ), Coef('Var'  , 0.105957    ), Coef('Var'  , 0.0960544   ), Coef('Var'  , 0.0865192   ), Coef('Var'  , 0.0721694   ), ], 
		[Coef('Var'  , 0.0724053   ), Coef('Var'  , 0.0651029   ), Coef('Var'  , 0.0576598   ), Coef('Var'  , 0.087141    ), Coef('Var'  , 0.116641    ), Coef('Var'  , 0.134836    ), Coef('Var'  , 0.153173    ), Coef('Var'  , 0.131239    ), Coef('Var'  , 0.109361    ), Coef('Var'  , 0.0909463   ), ], 
		[Coef('Var'  , 0.114415    ), Coef('Var'  , 0.136313    ), Coef('Var'  , 0.158103    ), Coef('Var'  , 0.172956    ), Coef('Var'  , 0.187776    ), Coef('Var'  , 0.171471    ), Coef('Var'  , 0.155139    ), Coef('Var'  , 0.138779    ), Coef('Var'  , 0.12232     ), Coef('Var'  , 0.118443    ), ], 
		[Coef('Var'  , 0.148872    ), Coef('Var'  , 0.201147    ), Coef('Var'  , 0.253748    ), Coef('Var'  , 0.253498    ), Coef('Var'  , 0.25356     ), Coef('Var'  , 0.200847    ), Coef('Var'  , 0.148522    ), Coef('Var'  , 0.13686     ), Coef('Var'  , 0.125633    ), Coef('Var'  , 0.137055    ), ], 
		[Coef('Var'  , 0.150735    ), Coef('Var'  , 0.167721    ), Coef('Var'  , 0.184973    ), Coef('Var'  , 0.170053    ), Coef('Var'  , 0.155337    ), Coef('Var'  , 0.132624    ), Coef('Var'  , 0.110083    ), Coef('Var'  , 0.113507    ), Coef('Var'  , 0.117132    ), Coef('Var'  , 0.133803    ), ], 
		[Coef('Var'  , 0.152565    ), Coef('Var'  , 0.13436     ), Coef('Var'  , 0.116303    ), Coef('Var'  , 0.0867803   ), Coef('Var'  , 0.0572815   ), Coef('Var'  , 0.0645613   ), Coef('Var'  , 0.0717216   ), Coef('Var'  , 0.0901784   ), Coef('Var'  , 0.108544    ), Coef('Var'  , 0.130513    ), ], 
		[Coef('Var'  , 0.112598    ), Coef('Var'  , 0.0957038   ), Coef('Var'  , 0.0787823   ), Coef('Var'  , 0.062149    ), Coef('Var'  , 0.0454007   ), Coef('Var'  , 0.0551587   ), Coef('Var'  , 0.0646746   ), Coef('Var'  , 0.0797352   ), Coef('Var'  , 0.0945646   ), Coef('Var'  , 0.103627    ), ], 
		[Coef('Var'  , 0.0735156   ), Coef('Var'  , 0.0577501   ), Coef('Var'  , 0.0417633   ), Coef('Var'  , 0.0380537   ), Coef('Var'  , 0.0340756   ), Coef('Var'  , 0.0465434   ), Coef('Var'  , 0.0586102   ), Coef('Var'  , 0.0703956   ), Coef('Var'  , 0.0817557   ), Coef('Var'  , 0.0777899   ), ], 
		[Coef('Var'  , 0.0620934   ), Coef('Var'  , 0.0488802   ), Coef('Var'  , 0.0355335   ), Coef('Var'  , 0.0355914   ), Coef('Var'  , 0.035514    ), Coef('Var'  , 0.0488491   ), Coef('Var'  , 0.0620575   ), Coef('Var'  , 0.0695257   ), Coef('Var'  , 0.076885    ), Coef('Var'  , 0.0695458   ), ], 
		[Coef('Var'  , 0.0547551   ), Coef('Var'  , 0.0433697   ), Coef('Var'  , 0.0317796   ), Coef('Var'  , 0.0358075   ), Coef('Var'  , 0.0396842   ), Coef('Var'  , 0.0549218   ), Coef('Var'  , 0.0700631   ), Coef('Var'  , 0.0737258   ), Coef('Var'  , 0.0772857   ), Coef('Var'  , 0.066107    ), ], ])
	etat1.initMat[Chem([Sub('2')])] = FMat([
		[Coef('Var'  , 0.0865192   ), Coef('Var'  , 0.0990403   ), Coef('Var'  , 0.111995    ), Coef('Var'  , 0.11176     ), Coef('Var'  , 0.112053    ), Coef('Var'  , 0.0991259   ), Coef('Var'  , 0.0866145   ), Coef('Var'  , 0.0791919   ), Coef('Var'  , 0.0720212   ), Coef('Var'  , 0.0791386   ), ], 
		[Coef('Var'  , 0.109361    ), Coef('Var'  , 0.120252    ), Coef('Var'  , 0.131173    ), Coef('Var'  , 0.120289    ), Coef('Var'  , 0.109428    ), Coef('Var'  , 0.0950127   ), Coef('Var'  , 0.0803963   ), Coef('Var'  , 0.0805407   ), Coef('Var'  , 0.0803546   ), Coef('Var'  , 0.094952    ), ], 
		[Coef('Var'  , 0.12232     ), Coef('Var'  , 0.122393    ), Coef('Var'  , 0.122317    ), Coef('Var'  , 0.109509    ), Coef('Var'  , 0.0964913   ), Coef('Var'  , 0.0892589   ), Coef('Var'  , 0.0817192   ), Coef('Var'  , 0.0892607   ), Coef('Var'  , 0.0964946   ), Coef('Var'  , 0.109512    ), ], 
		[Coef('Var'  , 0.125633    ), Coef('Var'  , 0.114388    ), Coef('Var'  , 0.103523    ), Coef('Var'  , 0.0888518   ), Coef('Var'  , 0.0743922   ), Coef('Var'  , 0.0744954   ), Coef('Var'  , 0.0746561   ), Coef('Var'  , 0.0892368   ), Coef('Var'  , 0.103948    ), Coef('Var'  , 0.114625    ), ], 
		[Coef('Var'  , 0.117132    ), Coef('Var'  , 0.104299    ), Coef('Var'  , 0.0915995   ), Coef('Var'  , 0.084424    ), Coef('Var'  , 0.0772063   ), Coef('Var'  , 0.0846038   ), Coef('Var'  , 0.0919216   ), Coef('Var'  , 0.10459     ), Coef('Var'  , 0.117331    ), Coef('Var'  , 0.117129    ), ], 
		[Coef('Var'  , 0.108544    ), Coef('Var'  , 0.0940574   ), Coef('Var'  , 0.0794322   ), Coef('Var'  , 0.0795436   ), Coef('Var'  , 0.0793956   ), Coef('Var'  , 0.0940039   ), Coef('Var'  , 0.108485    ), Coef('Var'  , 0.119376    ), Coef('Var'  , 0.130343    ), Coef('Var'  , 0.119409    ), ], 
		[Coef('Var'  , 0.0945646   ), Coef('Var'  , 0.0874122   ), Coef('Var'  , 0.0800269   ), Coef('Var'  , 0.087418    ), Coef('Var'  , 0.0945749   ), Coef('Var'  , 0.107334    ), Coef('Var'  , 0.120026    ), Coef('Var'  , 0.120004    ), Coef('Var'  , 0.12002     ), Coef('Var'  , 0.107325    ), ], 
		[Coef('Var'  , 0.0817557   ), Coef('Var'  , 0.0820349   ), Coef('Var'  , 0.0819153   ), Coef('Var'  , 0.0966768   ), Coef('Var'  , 0.111133    ), Coef('Var'  , 0.122057    ), Coef('Var'  , 0.132877    ), Coef('Var'  , 0.121914    ), Coef('Var'  , 0.110877    ), Coef('Var'  , 0.0964443   ), ], 
		[Coef('Var'  , 0.076885    ), Coef('Var'  , 0.0841819   ), Coef('Var'  , 0.0914439   ), Coef('Var'  , 0.104142    ), Coef('Var'  , 0.116964    ), Coef('Var'  , 0.116869    ), Coef('Var'  , 0.11699     ), Coef('Var'  , 0.104181    ), Coef('Var'  , 0.0914864   ), Coef('Var'  , 0.0842056   ), ], 
		[Coef('Var'  , 0.0772857   ), Coef('Var'  , 0.0919416   ), Coef('Var'  , 0.106575    ), Coef('Var'  , 0.117385    ), Coef('Var'  , 0.128361    ), Coef('Var'  , 0.117239    ), Coef('Var'  , 0.106314    ), Coef('Var'  , 0.0917057   ), Coef('Var'  , 0.0771247   ), Coef('Var'  , 0.0772591   ), ], ])
	etat1.initMat[Chem([Sub('3')])] = FMat([
		[Coef('Var'  , 0.152849    ), Coef('Var'  , 0.113658    ), Coef('Var'  , 0.0747291   ), Coef('Var'  , 0.0373099   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.201349    ), ], 
		[Coef('Var'  , 0.256304    ), Coef('Var'  , 0.186396    ), Coef('Var'  , 0.116641    ), Coef('Var'  , 0.0582911   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.378105    ), ], 
		[Coef('Var'  , 0.187774    ), Coef('Var'  , 0.187777    ), Coef('Var'  , 0.187776    ), Coef('Var'  , 0.218889    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.218888    ), ], 
		[Coef('Var'  , 0.113771    ), Coef('Var'  , 0.183508    ), Coef('Var'  , 0.25356     ), Coef('Var'  , 0.376696    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0568117   ), ], 
		[Coef('Var'  , 0.0771941   ), Coef('Var'  , 0.116201    ), Coef('Var'  , 0.155337    ), Coef('Var'  , 0.202626    ), Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0385745   ), ], 
		[Coef('Var'  , 0.0407182   ), Coef('Var'  , 0.0490611   ), Coef('Var'  , 0.0572815   ), Coef('Var'  , 0.0286583   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0204028   ), ], 
		[Coef('Var'  , 0.0371268   ), Coef('Var'  , 0.0413725   ), Coef('Var'  , 0.0454007   ), Coef('Var'  , 0.0227479   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0186246   ), ], 
		[Coef('Var'  , 0.0341433   ), Coef('Var'  , 0.0342791   ), Coef('Var'  , 0.0340756   ), Coef('Var'  , 0.0171206   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0171585   ), ], 
		[Coef('Var'  , 0.0437972   ), Coef('Var'  , 0.039709    ), Coef('Var'  , 0.035514    ), Coef('Var'  , 0.0177902   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0219188   ), ], 
		[Coef('Var'  , 0.0563218   ), Coef('Var'  , 0.0480377   ), Coef('Var'  , 0.0396842   ), Coef('Var'  , 0.0198704   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0281673   ), ], ])
	etat1.initMat[Chem([Sub('4')])] = FMat([
		[Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.216113    ), Coef('Var'  , 0.182419    ), Coef('Var'  , 0.182213    ), Coef('Var'  , 0.182395    ), Coef('Var'  , 0.2161      ), ], 
		[Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.058323    ), Coef('Var'  , 0.116698    ), Coef('Var'  , 0.186445    ), Coef('Var'  , 0.256334    ), Coef('Var'  , 0.378122    ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.039943    ), Coef('Var'  , 0.0798307   ), Coef('Var'  , 0.119006    ), Coef('Var'  , 0.158096    ), Coef('Var'  , 0.204063    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0190033   ), Coef('Var'  , 0.0380266   ), Coef('Var'  , 0.0462666   ), Coef('Var'  , 0.0545979   ), Coef('Var'  , 0.0272633   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0178483   ), Coef('Var'  , 0.035629    ), Coef('Var'  , 0.0397862   ), Coef('Var'  , 0.0438422   ), Coef('Var'  , 0.0219378   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0165327   ), Coef('Var'  , 0.0329278   ), Coef('Var'  , 0.0330741   ), Coef('Var'  , 0.0329432   ), Coef('Var'  , 0.0165413   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0227528   ), Coef('Var'  , 0.0454094   ), Coef('Var'  , 0.0413799   ), Coef('Var'  , 0.0371313   ), Coef('Var'  , 0.0186271   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0293559   ), Coef('Var'  , 0.0586263   ), Coef('Var'  , 0.050432    ), Coef('Var'  , 0.0420191   ), Coef('Var'  , 0.0210761   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.202643    ), Coef('Var'  , 0.155357    ), Coef('Var'  , 0.116238    ), Coef('Var'  , 0.0772189   ), Coef('Var'  , 0.0385945   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.377484    ), Coef('Var'  , 0.255076    ), Coef('Var'  , 0.18516     ), Coef('Var'  , 0.115422    ), Coef('Var'  , 0.0576753   ), ], ])
	etat1.initMat[Chem([Sub('5')])] = FMat([
		[Coef('Var'  , 0.182419    ), Coef('Var'  , 0.167513    ), Coef('Var'  , 0.15294     ), Coef('Var'  , 0.129347    ), Coef('Var'  , 0.106082    ), Coef('Var'  , 0.108844    ), Coef('Var'  , 0.112053    ), Coef('Var'  , 0.128978    ), Coef('Var'  , 0.146443    ), Coef('Var'  , 0.164195    ), ], 
		[Coef('Var'  , 0.116698    ), Coef('Var'  , 0.0872159   ), Coef('Var'  , 0.0577368   ), Coef('Var'  , 0.0651966   ), Coef('Var'  , 0.0724959   ), Coef('Var'  , 0.0910344   ), Coef('Var'  , 0.109428    ), Coef('Var'  , 0.131307    ), Coef('Var'  , 0.153228    ), Coef('Var'  , 0.134899    ), ], 
		[Coef('Var'  , 0.0798307   ), Coef('Var'  , 0.0630817   ), Coef('Var'  , 0.0461784   ), Coef('Var'  , 0.0562086   ), Coef('Var'  , 0.0659831   ), Coef('Var'  , 0.081383    ), Coef('Var'  , 0.0964913   ), Coef('Var'  , 0.105555    ), Coef('Var'  , 0.114408    ), Coef('Var'  , 0.0971846   ), ], 
		[Coef('Var'  , 0.0380266   ), Coef('Var'  , 0.0342177   ), Coef('Var'  , 0.0303809   ), Coef('Var'  , 0.0415233   ), Coef('Var'  , 0.0525726   ), Coef('Var'  , 0.0634829   ), Coef('Var'  , 0.0743922   ), Coef('Var'  , 0.0708337   ), Coef('Var'  , 0.0673999   ), Coef('Var'  , 0.052663    ), ], 
		[Coef('Var'  , 0.035629    ), Coef('Var'  , 0.0357772   ), Coef('Var'  , 0.0357733   ), Coef('Var'  , 0.0492149   ), Coef('Var'  , 0.0624821   ), Coef('Var'  , 0.0699201   ), Coef('Var'  , 0.0772063   ), Coef('Var'  , 0.0697708   ), Coef('Var'  , 0.0622148   ), Coef('Var'  , 0.0489851   ), ], 
		[Coef('Var'  , 0.0329278   ), Coef('Var'  , 0.036903    ), Coef('Var'  , 0.04066     ), Coef('Var'  , 0.056229    ), Coef('Var'  , 0.0716422   ), Coef('Var'  , 0.0756202   ), Coef('Var'  , 0.0793956   ), Coef('Var'  , 0.0681805   ), Coef('Var'  , 0.0566561   ), Coef('Var'  , 0.0449517   ), ], 
		[Coef('Var'  , 0.0454094   ), Coef('Var'  , 0.0621603   ), Coef('Var'  , 0.0787939   ), Coef('Var'  , 0.0957178   ), Coef('Var'  , 0.112612    ), Coef('Var'  , 0.10364     ), Coef('Var'  , 0.0945749   ), Coef('Var'  , 0.0797456   ), Coef('Var'  , 0.064683    ), Coef('Var'  , 0.0551683   ), ], 
		[Coef('Var'  , 0.0586263   ), Coef('Var'  , 0.0881885   ), Coef('Var'  , 0.117671    ), Coef('Var'  , 0.136202    ), Coef('Var'  , 0.154749    ), Coef('Var'  , 0.132985    ), Coef('Var'  , 0.111133    ), Coef('Var'  , 0.0926261   ), Coef('Var'  , 0.0738633   ), Coef('Var'  , 0.0663672   ), ], 
		[Coef('Var'  , 0.155357    ), Coef('Var'  , 0.170041    ), Coef('Var'  , 0.184908    ), Coef('Var'  , 0.167598    ), Coef('Var'  , 0.150551    ), Coef('Var'  , 0.133628    ), Coef('Var'  , 0.116964    ), Coef('Var'  , 0.11342     ), Coef('Var'  , 0.110055    ), Coef('Var'  , 0.132635    ), ], 
		[Coef('Var'  , 0.255076    ), Coef('Var'  , 0.254902    ), Coef('Var'  , 0.254957    ), Coef('Var'  , 0.202762    ), Coef('Var'  , 0.15083     ), Coef('Var'  , 0.139462    ), Coef('Var'  , 0.128361    ), Coef('Var'  , 0.139585    ), Coef('Var'  , 0.15105     ), Coef('Var'  , 0.202951    ), ], ])
	etat1.initMat[Chem([Sub('6')])] = FMat([
		[Coef('Var'  , 0.111995    ), Coef('Var'  , 0.108742    ), Coef('Var'  , 0.105957    ), Coef('Var'  , 0.129226    ), Coef('Var'  , 0.152849    ), Coef('Var'  , 0.167449    ), Coef('Var'  , 0.182395    ), Coef('Var'  , 0.164181    ), Coef('Var'  , 0.146443    ), Coef('Var'  , 0.128945    ), ], 
		[Coef('Var'  , 0.131173    ), Coef('Var'  , 0.142104    ), Coef('Var'  , 0.153173    ), Coef('Var'  , 0.204651    ), Coef('Var'  , 0.256304    ), Coef('Var'  , 0.256227    ), Coef('Var'  , 0.256334    ), Coef('Var'  , 0.204698    ), Coef('Var'  , 0.153228    ), Coef('Var'  , 0.142135    ), ], 
		[Coef('Var'  , 0.122317    ), Coef('Var'  , 0.138777    ), Coef('Var'  , 0.155139    ), Coef('Var'  , 0.171469    ), Coef('Var'  , 0.187774    ), Coef('Var'  , 0.172951    ), Coef('Var'  , 0.158096    ), Coef('Var'  , 0.136305    ), Coef('Var'  , 0.114408    ), Coef('Var'  , 0.118437    ), ], 
		[Coef('Var'  , 0.103523    ), Coef('Var'  , 0.125828    ), Coef('Var'  , 0.148522    ), Coef('Var'  , 0.130962    ), Coef('Var'  , 0.113771    ), Coef('Var'  , 0.084075    ), Coef('Var'  , 0.0545979   ), Coef('Var'  , 0.060923    ), Coef('Var'  , 0.0673999   ), Coef('Var'  , 0.0853376   ), ], 
		[Coef('Var'  , 0.0915995   ), Coef('Var'  , 0.100788    ), Coef('Var'  , 0.110083    ), Coef('Var'  , 0.0935724   ), Coef('Var'  , 0.0771941   ), Coef('Var'  , 0.0605123   ), Coef('Var'  , 0.0438422   ), Coef('Var'  , 0.0530746   ), Coef('Var'  , 0.0622148   ), Coef('Var'  , 0.0769268   ), ], 
		[Coef('Var'  , 0.0794322   ), Coef('Var'  , 0.0756851   ), Coef('Var'  , 0.0717216   ), Coef('Var'  , 0.0563059   ), Coef('Var'  , 0.0407182   ), Coef('Var'  , 0.0369441   ), Coef('Var'  , 0.0329432   ), Coef('Var'  , 0.0449603   ), Coef('Var'  , 0.0566561   ), Coef('Var'  , 0.068201    ), ], 
		[Coef('Var'  , 0.0800269   ), Coef('Var'  , 0.0724987   ), Coef('Var'  , 0.0646746   ), Coef('Var'  , 0.0510354   ), Coef('Var'  , 0.0371268   ), Coef('Var'  , 0.0372516   ), Coef('Var'  , 0.0371313   ), Coef('Var'  , 0.0510426   ), Coef('Var'  , 0.064683    ), Coef('Var'  , 0.0725034   ), ], 
		[Coef('Var'  , 0.0819153   ), Coef('Var'  , 0.0704848   ), Coef('Var'  , 0.0586102   ), Coef('Var'  , 0.0465813   ), Coef('Var'  , 0.0341433   ), Coef('Var'  , 0.0382346   ), Coef('Var'  , 0.0420191   ), Coef('Var'  , 0.0580873   ), Coef('Var'  , 0.0738633   ), Coef('Var'  , 0.0780733   ), ], 
		[Coef('Var'  , 0.0914439   ), Coef('Var'  , 0.0767741   ), Coef('Var'  , 0.0620575   ), Coef('Var'  , 0.0529777   ), Coef('Var'  , 0.0437972   ), Coef('Var'  , 0.0605133   ), Coef('Var'  , 0.0772189   ), Coef('Var'  , 0.0935867   ), Coef('Var'  , 0.110055    ), Coef('Var'  , 0.100707    ), ], 
		[Coef('Var'  , 0.106575    ), Coef('Var'  , 0.0883185   ), Coef('Var'  , 0.0700631   ), Coef('Var'  , 0.0632187   ), Coef('Var'  , 0.0563218   ), Coef('Var'  , 0.0858426   ), Coef('Var'  , 0.115422    ), Coef('Var'  , 0.133142    ), Coef('Var'  , 0.15105     ), Coef('Var'  , 0.128734    ), ], ])
	etat1.initMat[Chem([Sub('7')])] = FMat([
		[Coef('Var'  , 0.0331414   ), Coef('Var'  , 0.0331174   ), Coef('Var'  , 0.0330967   ), Coef('Var'  , 0.0455391   ), Coef('Var'  , 0.0580463   ), Coef('Var'  , 0.0649551   ), Coef('Var'  , 0.0720212   ), Coef('Var'  , 0.0650011   ), Coef('Var'  , 0.0581283   ), Coef('Var'  , 0.0456102   ), ], 
		[Coef('Var'  , 0.0334476   ), Coef('Var'  , 0.0374223   ), Coef('Var'  , 0.0411403   ), Coef('Var'  , 0.0568719   ), Coef('Var'  , 0.0724053   ), Coef('Var'  , 0.0765117   ), Coef('Var'  , 0.0803546   ), Coef('Var'  , 0.0691128   ), Coef('Var'  , 0.0574922   ), Coef('Var'  , 0.0456575   ), ], 
		[Coef('Var'  , 0.0461793   ), Coef('Var'  , 0.0630854   ), Coef('Var'  , 0.0798367   ), Coef('Var'  , 0.0971925   ), Coef('Var'  , 0.114415    ), Coef('Var'  , 0.105561    ), Coef('Var'  , 0.0964946   ), Coef('Var'  , 0.0813845   ), Coef('Var'  , 0.0659829   ), Coef('Var'  , 0.0562085   ), ], 
		[Coef('Var'  , 0.0550868   ), Coef('Var'  , 0.0845526   ), Coef('Var'  , 0.114138    ), Coef('Var'  , 0.131362    ), Coef('Var'  , 0.148872    ), Coef('Var'  , 0.126261    ), Coef('Var'  , 0.103948    ), Coef('Var'  , 0.085896    ), Coef('Var'  , 0.0679743   ), Coef('Var'  , 0.0615169   ), ], 
		[Coef('Var'  , 0.155655    ), Coef('Var'  , 0.170277    ), Coef('Var'  , 0.185056    ), Coef('Var'  , 0.167768    ), Coef('Var'  , 0.150735    ), Coef('Var'  , 0.133914    ), Coef('Var'  , 0.117331    ), Coef('Var'  , 0.11386     ), Coef('Var'  , 0.110515    ), Coef('Var'  , 0.133043    ), ], 
		[Coef('Var'  , 0.255935    ), Coef('Var'  , 0.255852    ), Coef('Var'  , 0.255961    ), Coef('Var'  , 0.204171    ), Coef('Var'  , 0.152565    ), Coef('Var'  , 0.141371    ), Coef('Var'  , 0.130343    ), Coef('Var'  , 0.141344    ), Coef('Var'  , 0.152516    ), Coef('Var'  , 0.204129    ), ], 
		[Coef('Var'  , 0.186409    ), Coef('Var'  , 0.171604    ), Coef('Var'  , 0.156893    ), Coef('Var'  , 0.134737    ), Coef('Var'  , 0.112598    ), Coef('Var'  , 0.116303    ), Coef('Var'  , 0.12002     ), Coef('Var'  , 0.136475    ), Coef('Var'  , 0.153027    ), Coef('Var'  , 0.169643    ), ], 
		[Coef('Var'  , 0.11745     ), Coef('Var'  , 0.0879001   ), Coef('Var'  , 0.0583305   ), Coef('Var'  , 0.0660077   ), Coef('Var'  , 0.0735156   ), Coef('Var'  , 0.0922885   ), Coef('Var'  , 0.110877    ), Coef('Var'  , 0.132724    ), Coef('Var'  , 0.154539    ), Coef('Var'  , 0.135962    ), ], 
		[Coef('Var'  , 0.0772673   ), Coef('Var'  , 0.0605613   ), Coef('Var'  , 0.0438346   ), Coef('Var'  , 0.0530188   ), Coef('Var'  , 0.0620934   ), Coef('Var'  , 0.0768179   ), Coef('Var'  , 0.0914864   ), Coef('Var'  , 0.100763    ), Coef('Var'  , 0.110111    ), Coef('Var'  , 0.0936452   ), ], 
		[Coef('Var'  , 0.0394288   ), Coef('Var'  , 0.0356276   ), Coef('Var'  , 0.0317125   ), Coef('Var'  , 0.0433322   ), Coef('Var'  , 0.0547551   ), Coef('Var'  , 0.0660172   ), Coef('Var'  , 0.0771247   ), Coef('Var'  , 0.0734411   ), Coef('Var'  , 0.0697139   ), Coef('Var'  , 0.0545845   ), ], ])
	etat1.initMat[Chem([Sub('8')])] = FMat([
		[Coef('Var'  , 0.0866145   ), Coef('Var'  , 0.0961776   ), Coef('Var'  , 0.106082    ), Coef('Var'  , 0.090318    ), Coef('Var'  , 0.074837    ), Coef('Var'  , 0.0580781   ), Coef('Var'  , 0.0414391   ), Coef('Var'  , 0.0497469   ), Coef('Var'  , 0.0581283   ), Coef('Var'  , 0.0722687   ), ], 
		[Coef('Var'  , 0.0803963   ), Coef('Var'  , 0.0765856   ), Coef('Var'  , 0.0724959   ), Coef('Var'  , 0.0569598   ), Coef('Var'  , 0.041207    ), Coef('Var'  , 0.0374694   ), Coef('Var'  , 0.0334652   ), Coef('Var'  , 0.0456674   ), Coef('Var'  , 0.0574922   ), Coef('Var'  , 0.0691361   ), ], 
		[Coef('Var'  , 0.0817192   ), Coef('Var'  , 0.0740156   ), Coef('Var'  , 0.0659831   ), Coef('Var'  , 0.0520297   ), Coef('Var'  , 0.0378053   ), Coef('Var'  , 0.0379192   ), Coef('Var'  , 0.0378048   ), Coef('Var'  , 0.0520289   ), Coef('Var'  , 0.0659829   ), Coef('Var'  , 0.0740152   ), ], 
		[Coef('Var'  , 0.0746561   ), Coef('Var'  , 0.0636304   ), Coef('Var'  , 0.0525726   ), Coef('Var'  , 0.0415857   ), Coef('Var'  , 0.0304926   ), Coef('Var'  , 0.0345159   ), Coef('Var'  , 0.0384487   ), Coef('Var'  , 0.0532198   ), Coef('Var'  , 0.0679743   ), Coef('Var'  , 0.071302    ), ], 
		[Coef('Var'  , 0.0919216   ), Coef('Var'  , 0.0772558   ), Coef('Var'  , 0.0624821   ), Coef('Var'  , 0.05338     ), Coef('Var'  , 0.0441219   ), Coef('Var'  , 0.0608745   ), Coef('Var'  , 0.0775631   ), Coef('Var'  , 0.0940199   ), Coef('Var'  , 0.110515    ), Coef('Var'  , 0.101209    ), ], 
		[Coef('Var'  , 0.108485    ), Coef('Var'  , 0.090101    ), Coef('Var'  , 0.0716422   ), Coef('Var'  , 0.0644793   ), Coef('Var'  , 0.0572141   ), Coef('Var'  , 0.0867144   ), Coef('Var'  , 0.116253    ), Coef('Var'  , 0.134304    ), Coef('Var'  , 0.152516    ), Coef('Var'  , 0.130453    ), ], 
		[Coef('Var'  , 0.120026    ), Coef('Var'  , 0.116314    ), Coef('Var'  , 0.112612    ), Coef('Var'  , 0.134751    ), Coef('Var'  , 0.156903    ), Coef('Var'  , 0.171611    ), Coef('Var'  , 0.186411    ), Coef('Var'  , 0.169645    ), Coef('Var'  , 0.153027    ), Coef('Var'  , 0.136478    ), ], 
		[Coef('Var'  , 0.132877    ), Coef('Var'  , 0.143812    ), Coef('Var'  , 0.154749    ), Coef('Var'  , 0.206001    ), Coef('Var'  , 0.257307    ), Coef('Var'  , 0.2572      ), Coef('Var'  , 0.257194    ), Coef('Var'  , 0.205821    ), Coef('Var'  , 0.154539    ), Coef('Var'  , 0.143695    ), ], 
		[Coef('Var'  , 0.11699     ), Coef('Var'  , 0.133643    ), Coef('Var'  , 0.150551    ), Coef('Var'  , 0.167604    ), Coef('Var'  , 0.184919    ), Coef('Var'  , 0.17007     ), Coef('Var'  , 0.155398    ), Coef('Var'  , 0.13269     ), Coef('Var'  , 0.110111    ), Coef('Var'  , 0.113466    ), ], 
		[Coef('Var'  , 0.106314    ), Coef('Var'  , 0.128465    ), Coef('Var'  , 0.15083     ), Coef('Var'  , 0.132891    ), Coef('Var'  , 0.115193    ), Coef('Var'  , 0.0855481   ), Coef('Var'  , 0.0560234   ), Coef('Var'  , 0.0628573   ), Coef('Var'  , 0.0697139   ), Coef('Var'  , 0.0879776   ), ], ])
	etat1.initMat[Chem([Sub('9')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0206602   ), Coef('Var'  , 0.0413539   ), Coef('Var'  , 0.0372063   ), Coef('Var'  , 0.0330967   ), Coef('Var'  , 0.0165461   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0288499   ), Coef('Var'  , 0.0576598   ), Coef('Var'  , 0.0494688   ), Coef('Var'  , 0.0411403   ), Coef('Var'  , 0.0206189   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.204067    ), Coef('Var'  , 0.158103    ), Coef('Var'  , 0.119013    ), Coef('Var'  , 0.0798367   ), Coef('Var'  , 0.0399464   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.376801    ), Coef('Var'  , 0.253748    ), Coef('Var'  , 0.183818    ), Coef('Var'  , 0.114138    ), Coef('Var'  , 0.0570163   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.217427    ), Coef('Var'  , 0.184973    ), Coef('Var'  , 0.184902    ), Coef('Var'  , 0.185056    ), Coef('Var'  , 0.217474    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.058122    ), Coef('Var'  , 0.116303    ), Coef('Var'  , 0.186055    ), Coef('Var'  , 0.255961    ), Coef('Var'  , 0.377933    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0394011   ), Coef('Var'  , 0.0787823   ), Coef('Var'  , 0.117836    ), Coef('Var'  , 0.156893    ), Coef('Var'  , 0.203435    ), Coef('Const', 0.25        ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0209331   ), Coef('Var'  , 0.0417633   ), Coef('Var'  , 0.0501238   ), Coef('Var'  , 0.0583305   ), Coef('Var'  , 0.0291907   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0178011   ), Coef('Var'  , 0.0355335   ), Coef('Var'  , 0.0397409   ), Coef('Var'  , 0.0438346   ), Coef('Var'  , 0.0219398   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0159371   ), Coef('Var'  , 0.0317796   ), Coef('Var'  , 0.0318367   ), Coef('Var'  , 0.0317125   ), Coef('Var'  , 0.0158996   ), Coef('Const', 0           ), Coef('Const', 0           ), ], ])
	etat1.initMat[Chem([Sub('10')])] = FMat([
		[Coef('Const', 0           ), Coef('Var'  , 0.0373701   ), Coef('Var'  , 0.074837    ), Coef('Var'  , 0.11377     ), Coef('Var'  , 0.15294     ), Coef('Var'  , 0.201399    ), Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0206561   ), Coef('Var'  , 0.041207    ), Coef('Var'  , 0.0495491   ), Coef('Var'  , 0.0577368   ), Coef('Var'  , 0.0288929   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0189599   ), Coef('Var'  , 0.0378053   ), Coef('Var'  , 0.0420986   ), Coef('Var'  , 0.0461784   ), Coef('Var'  , 0.0231387   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0152767   ), Coef('Var'  , 0.0304926   ), Coef('Var'  , 0.0304911   ), Coef('Var'  , 0.0303809   ), Coef('Var'  , 0.0152143   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.022094    ), Coef('Var'  , 0.0441219   ), Coef('Var'  , 0.0400229   ), Coef('Var'  , 0.0357733   ), Coef('Var'  , 0.0179289   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0286206   ), Coef('Var'  , 0.0572141   ), Coef('Var'  , 0.0489909   ), Coef('Var'  , 0.04066     ), Coef('Var'  , 0.0203703   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.25        ), Coef('Var'  , 0.20344     ), Coef('Var'  , 0.156903    ), Coef('Var'  , 0.117848    ), Coef('Var'  , 0.0787939   ), Coef('Var'  , 0.0394075   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.5         ), Coef('Var'  , 0.378631    ), Coef('Var'  , 0.257307    ), Coef('Var'  , 0.187464    ), Coef('Var'  , 0.117671    ), Coef('Var'  , 0.0588326   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0.25        ), Coef('Var'  , 0.217403    ), Coef('Var'  , 0.184919    ), Coef('Var'  , 0.184801    ), Coef('Var'  , 0.184908    ), Coef('Var'  , 0.217397    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Var'  , 0.0575474   ), Coef('Var'  , 0.115193    ), Coef('Var'  , 0.184965    ), Coef('Var'  , 0.254957    ), Coef('Var'  , 0.377418    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Const', 0           ), ], ])
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
