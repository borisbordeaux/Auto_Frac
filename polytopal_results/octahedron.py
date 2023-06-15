# -*- coding: utf-8 -*-

# Automatically generated, from file : octahedron.py, function : modele()

from __future__ import division
import sys
if './../../../../../../python' not in sys.path:
	sys.path.append('./../../../../../../python')
from etat import *

def modele():
	
	etat0 = EtatInit()
	etat1 = Etat('Cell_0',0)
	etat2 = Etat('B3',1)
	etat3 = Etat('s',1)
	
	
	etat0.subs   = {Sub('0'): etat1, Sub('1'): etat1, Sub('2'): etat1, Sub('3'): etat1, Sub('4'): etat1, Sub('5'): etat1, Sub('6'): etat1, Sub('7'): etat1, }
	
	etat0.eqs = [
		(Chem([Sub('0'), Bord('0'), Bord('1'), ])	,	Chem([Sub('3'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('1'), Bord('1'), ])	,	Chem([Sub('4'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('2'), Bord('1'), ])	,	Chem([Sub('1'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('1'), Bord('1'), ])	,	Chem([Sub('5'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('1'), Bord('2'), Bord('1'), ])	,	Chem([Sub('2'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('1'), Bord('1'), ])	,	Chem([Sub('6'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('2'), Bord('2'), Bord('1'), ])	,	Chem([Sub('3'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('3'), Bord('1'), Bord('1'), ])	,	Chem([Sub('7'), Bord('0'), Bord('1'), ])),
		(Chem([Sub('4'), Bord('1'), Bord('1'), ])	,	Chem([Sub('7'), Bord('2'), Bord('1'), ])),
		(Chem([Sub('4'), Bord('2'), Bord('1'), ])	,	Chem([Sub('5'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('5'), Bord('2'), Bord('1'), ])	,	Chem([Sub('6'), Bord('1'), Bord('1'), ])),
		(Chem([Sub('6'), Bord('2'), Bord('1'), ])	,	Chem([Sub('7'), Bord('1'), Bord('1'), ])),
		]
	
	
	etat0.space = []
	
	etat0.initMat[Chem([Sub('0')])] = FMat([
		[Coef('Var'  , 1.89818     ), Coef('Var'  , 2.16451     ), Coef('Var'  , 2.58031     ), Coef('Var'  , 2.22462     ), Coef('Var'  , 1.7782      ), Coef('Var'  , 2.13173     ), ], 
		[Coef('Var'  , 0.528146    ), Coef('Var'  , 0.221909    ), Coef('Var'  ,-0.776514    ), Coef('Var'  , 0.367938    ), Coef('Var'  , 1.48159     ), Coef('Var'  , 0.413188    ), ], 
		[Coef('Var'  , 0.648748    ), Coef('Var'  , 1.84471     ), Coef('Var'  , 2.49012     ), Coef('Var'  , 2.01272     ), Coef('Var'  , 2.85383     ), Coef('Var'  , 1.81517     ), ], 
		[Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), ], ])
	etat0.initMat[Chem([Sub('1')])] = FMat([
		[Coef('Var'  , 0.281756    ), Coef('Var'  , 0.740345    ), Coef('Var'  , 1.89818     ), Coef('Var'  , 0.617213    ), Coef('Var'  ,-0.524876    ), Coef('Var'  , 0.404463    ), ], 
		[Coef('Var'  ,-1.25149     ), Coef('Var'  ,-0.0800974   ), Coef('Var'  , 0.528146    ), Coef('Var'  , 0.266518    ), Coef('Var'  , 1.08198     ), Coef('Var'  , 0.017855    ), ], 
		[Coef('Var'  , 0.0895609   ), Coef('Var'  , 0.30382     ), Coef('Var'  , 0.648748    ), Coef('Var'  , 0.351252    ), Coef('Var'  , 0.429521    ), Coef('Var'  , 0.340003    ), ], 
		[Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), ], ])
	etat0.initMat[Chem([Sub('2')])] = FMat([
		[Coef('Var'  , 1.03476     ), Coef('Var'  , 0.142849    ), Coef('Var'  , 0.281756    ), Coef('Var'  ,-0.307185    ), Coef('Var'  ,-1.33137     ), Coef('Var'  ,-0.132176    ), ], 
		[Coef('Var'  ,-2.55536     ), Coef('Var'  ,-2.02934     ), Coef('Var'  ,-1.25149     ), Coef('Var'  ,-1.93986     ), Coef('Var'  ,-2.04505     ), Coef('Var'  ,-2.1209      ), ], 
		[Coef('Var'  , 1.90272     ), Coef('Var'  , 1.15724     ), Coef('Var'  , 0.0895609   ), Coef('Var'  , 1.07839     ), Coef('Var'  , 1.63307     ), Coef('Var'  , 1.30111     ), ], 
		[Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), ], ])
	etat0.initMat[Chem([Sub('3')])] = FMat([
		[Coef('Var'  , 2.58031     ), Coef('Var'  , 1.66263     ), Coef('Var'  , 1.03476     ), Coef('Var'  , 1.37662     ), Coef('Var'  , 0.984294    ), Coef('Var'  , 1.66459     ), ], 
		[Coef('Var'  ,-0.776514    ), Coef('Var'  ,-1.70409     ), Coef('Var'  ,-2.55536     ), Coef('Var'  ,-1.92532     ), Coef('Var'  ,-1.59843     ), Coef('Var'  ,-1.51499     ), ], 
		[Coef('Var'  , 2.49012     ), Coef('Var'  , 2.73142     ), Coef('Var'  , 1.90272     ), Coef('Var'  , 3.04447     ), Coef('Var'  , 4.11713     ), Coef('Var'  , 3.04647     ), ], 
		[Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), ], ])
	etat0.initMat[Chem([Sub('4')])] = FMat([
		[Coef('Var'  ,-0.576357    ), Coef('Var'  , 0.536612    ), Coef('Var'  , 1.7782      ), Coef('Var'  , 0.542663    ), Coef('Var'  , 0.180707    ), Coef('Var'  , 0.330086    ), ], 
		[Coef('Var'  , 1.99577     ), Coef('Var'  , 1.45545     ), Coef('Var'  , 1.48159     ), Coef('Var'  , 1.24652     ), Coef('Var'  , 0.655687    ), Coef('Var'  , 1.32604     ), ], 
		[Coef('Var'  , 2.61525     ), Coef('Var'  , 3.28095     ), Coef('Var'  , 2.85383     ), Coef('Var'  , 3.52171     ), Coef('Var'  , 4.47347     ), Coef('Var'  , 3.44718     ), ], 
		[Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), ], ])
	etat0.initMat[Chem([Sub('5')])] = FMat([
		[Coef('Var'  ,-2.12757     ), Coef('Var'  ,-1.14205     ), Coef('Var'  ,-0.524876    ), Coef('Var'  ,-0.944738    ), Coef('Var'  ,-0.576357    ), Coef('Var'  ,-1.08223     ), ], 
		[Coef('Var'  , 0.231412    ), Coef('Var'  , 1.09165     ), Coef('Var'  , 1.08198     ), Coef('Var'  , 1.2641      ), Coef('Var'  , 1.99577     ), Coef('Var'  , 1.19066     ), ], 
		[Coef('Var'  , 1.98532     ), Coef('Var'  , 1.53383     ), Coef('Var'  , 0.429521    ), Coef('Var'  , 1.53955     ), Coef('Var'  , 2.61525     ), Coef('Var'  , 1.78427     ), ], 
		[Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), ], ])
	etat0.initMat[Chem([Sub('6')])] = FMat([
		[Coef('Var'  ,-1.37082     ), Coef('Var'  ,-1.59575     ), Coef('Var'  ,-1.33137     ), Coef('Var'  ,-1.69478     ), Coef('Var'  ,-2.12757     ), Coef('Var'  ,-1.7431      ), ], 
		[Coef('Var'  ,-1.10113     ), Coef('Var'  ,-1.20273     ), Coef('Var'  ,-2.04505     ), Coef('Var'  ,-1.02256     ), Coef('Var'  , 0.231412    ), Coef('Var'  ,-0.858901    ), ], 
		[Coef('Var'  , 3.85809     ), Coef('Var'  , 2.61812     ), Coef('Var'  , 1.63307     ), Coef('Var'  , 2.35915     ), Coef('Var'  , 1.98532     ), Coef('Var'  , 2.62568     ), ], 
		[Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), ], ])
	etat0.initMat[Chem([Sub('7')])] = FMat([
		[Coef('Var'  , 0.180707    ), Coef('Var'  , 0.123092    ), Coef('Var'  , 0.984294    ), Coef('Var'  ,-0.0726417   ), Coef('Var'  ,-1.37082     ), Coef('Var'  ,-0.171094    ), ], 
		[Coef('Var'  , 0.655687    ), Coef('Var'  ,-0.545293    ), Coef('Var'  ,-1.59843     ), Coef('Var'  ,-0.861459    ), Coef('Var'  ,-1.10113     ), Coef('Var'  ,-0.595935    ), ], 
		[Coef('Var'  , 4.47347     ), Coef('Var'  , 4.27545     ), Coef('Var'  , 4.11713     ), Coef('Var'  , 4.17307     ), Coef('Var'  , 3.85809     ), Coef('Var'  , 4.24908     ), ], 
		[Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), ], ])
	
	
	
	etat1.bords   = {Bord('0'): etat2, Bord('1'): etat2, Bord('2'): etat2, }
	etat1.permuts = {}
	etat1.interns = {Intern('_'): etat1, }
	etat1.subs    = {Sub('0'): etat1, Sub('1'): etat1, Sub('2'): etat1, Sub('3'): etat1, Sub('4'): etat1, Sub('5'): etat1, Sub('6'): etat1, Sub('G', True): Etat.etatPoint, }
	
	etat1.buildIntern()
	
	
	etat1.eqs = [
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
	
	
	etat1.prim.elems = [Figure(2, [Chem([Bord('0'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('0'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('0'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('0'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('1'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('1'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('1'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('1'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('2'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('2'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('2'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('2'), Sub('1'), Sub('1'), Bord('0'), ]), ])]
	etat1.grid.elems = [
		Figure(1, [Chem([Bord('1'), Bord('0'), ]), Chem([Bord('1'), Intern(''), ]), Chem([Bord('1'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('2'), Bord('0'), ]), Chem([Bord('2'), Intern(''), ]), Chem([Bord('2'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('0'), Bord('0'), ]), Chem([Bord('0'), Intern(''), ]), Chem([Bord('0'), Bord('1'), ]), ]), ]
	
	
	etat1.space = [Chem([Bord('2'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('2'), Intern('0'), Intern('0'), ]), ]
	
	etat1.initMat[Chem([Sub('0')])] = FMat([
		[Coef('Const', 0.444444    ), Coef('Const', 0.666667    ), Coef('Const', 1           ), Coef('Const', 0.666667    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.457468    ), ], 
		[Coef('Const', 0.444444    ), Coef('Const', 0.333333    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.331513    ), ], 
		[Coef('Const', 0.111111    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  ,-0.0309896   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  ,-0.035244    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.111111    ), Coef('Var'  ,-0.0443435   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.333333    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.321596    ), ], ])
	etat1.initMat[Chem([Sub('1')])] = FMat([
		[Coef('Const', 0.111111    ), Coef('Const', 0.222222    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.25859     ), Coef('Var'  , 0.210052    ), Coef('Var'  , 0.206686    ), ], 
		[Coef('Const', 0.444444    ), Coef('Const', 0.555556    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.223901    ), Coef('Var'  , 0.265231    ), Coef('Var'  , 0.240532    ), ], 
		[Coef('Const', 0.444444    ), Coef('Const', 0.222222    ), Coef('Const', 0.111111    ), Coef('Var'  , 0.205381    ), Coef('Var'  , 0.209858    ), Coef('Var'  , 0.216638    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.204251    ), Coef('Var'  , 0.103108    ), Coef('Var'  , 0.250149    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  ,-0.0583647   ), Coef('Var'  , 0.119913    ), Coef('Var'  ,-0.079325    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.16624     ), Coef('Var'  , 0.0918375   ), Coef('Var'  , 0.165321    ), ], ])
	etat1.initMat[Chem([Sub('2')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.111111    ), Coef('Var'  , 0.108987    ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.333333    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.206486    ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 1           ), Coef('Const', 0.666667    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.56368     ), Coef('Const', 0.444444    ), Coef('Const', 0.666667    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.183823    ), Coef('Const', 0.444444    ), Coef('Const', 0.333333    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0845869   ), Coef('Const', 0.111111    ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  ,-0.147563    ), Coef('Const', 0           ), Coef('Const', 0           ), ], ])
	etat1.initMat[Chem([Sub('3')])] = FMat([
		[Coef('Const', 0.111111    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0736405   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  ,-0.121801    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.111111    ), Coef('Var'  , 0.0680569   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.333333    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.21813     ), ], 
		[Coef('Const', 0.444444    ), Coef('Const', 0.666667    ), Coef('Const', 1           ), Coef('Const', 0.666667    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.53926     ), ], 
		[Coef('Const', 0.444444    ), Coef('Const', 0.333333    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.222713    ), ], ])
	etat1.initMat[Chem([Sub('4')])] = FMat([
		[Coef('Var'  , 0.210007    ), Coef('Var'  , 0.350175    ), Coef('Const', 0.444444    ), Coef('Const', 0.222222    ), Coef('Const', 0.111111    ), Coef('Var'  , 0.279783    ), ], 
		[Coef('Var'  , 0.0887497   ), Coef('Var'  , 0.133537    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0533943   ), ], 
		[Coef('Var'  , 0.100585    ), Coef('Var'  ,-0.0182245   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.035792    ), ], 
		[Coef('Var'  , 0.103001    ), Coef('Var'  , 0.124898    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0830859   ), ], 
		[Coef('Var'  , 0.231293    ), Coef('Var'  , 0.217944    ), Coef('Const', 0.111111    ), Coef('Const', 0.222222    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.375951    ), ], 
		[Coef('Var'  , 0.266364    ), Coef('Var'  , 0.19167     ), Coef('Const', 0.444444    ), Coef('Const', 0.555556    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.171994    ), ], ])
	etat1.initMat[Chem([Sub('5')])] = FMat([
		[Coef('Var'  , 0.100072    ), Coef('Var'  , 0.148989    ), Coef('Var'  , 0.210052    ), Coef('Var'  , 0.172653    ), Coef('Var'  , 0.210007    ), Coef('Var'  , 0.157672    ), ], 
		[Coef('Var'  , 0.0901383   ), Coef('Var'  , 0.171809    ), Coef('Var'  , 0.265231    ), Coef('Var'  , 0.152025    ), Coef('Var'  , 0.0887497   ), Coef('Var'  , 0.150891    ), ], 
		[Coef('Var'  , 0.209576    ), Coef('Var'  , 0.16246     ), Coef('Var'  , 0.209858    ), Coef('Var'  , 0.166604    ), Coef('Var'  , 0.100585    ), Coef('Var'  , 0.164779    ), ], 
		[Coef('Var'  , 0.278584    ), Coef('Var'  , 0.174208    ), Coef('Var'  , 0.103108    ), Coef('Var'  , 0.155989    ), Coef('Var'  , 0.103001    ), Coef('Var'  , 0.158677    ), ], 
		[Coef('Var'  , 0.230785    ), Coef('Var'  , 0.174058    ), Coef('Var'  , 0.119913    ), Coef('Var'  , 0.18823     ), Coef('Var'  , 0.231293    ), Coef('Var'  , 0.203036    ), ], 
		[Coef('Var'  , 0.0908455   ), Coef('Var'  , 0.168477    ), Coef('Var'  , 0.0918375   ), Coef('Var'  , 0.164498    ), Coef('Var'  , 0.266364    ), Coef('Var'  , 0.164945    ), ], ])
	etat1.initMat[Chem([Sub('6')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.00568531  ), Coef('Var'  , 0.100072    ), Coef('Var'  , 0.0309928   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.116606    ), Coef('Var'  , 0.0901383   ), Coef('Var'  , 0.0322718   ), ], 
		[Coef('Const', 0.111111    ), Coef('Const', 0.222222    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.316562    ), Coef('Var'  , 0.209576    ), Coef('Var'  , 0.316357    ), ], 
		[Coef('Const', 0.444444    ), Coef('Const', 0.555556    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.153807    ), Coef('Var'  , 0.278584    ), Coef('Var'  , 0.0942657   ), ], 
		[Coef('Const', 0.444444    ), Coef('Const', 0.222222    ), Coef('Const', 0.111111    ), Coef('Var'  , 0.271578    ), Coef('Var'  , 0.230785    ), Coef('Var'  , 0.402699    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.135761    ), Coef('Var'  , 0.0908455   ), Coef('Var'  , 0.123413    ), ], ])
	etat1.initMat[Chem([Sub('G')])] = FMat([
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], ])
	
	
	
	etat2.bords   = {Bord('0'): etat3, Bord('1'): etat3, }
	etat2.permuts = {Permut('0'): etat2, }
	etat2.interns = {Intern('_'): etat2, }
	etat2.subs    = {Sub('0'): etat2, Sub('1'): etat2, Sub('2'): etat2, Sub('G', True): Etat.etatPoint, }
	
	etat2.buildIntern()
	etat2.fm_[Permut('0')] = PMat(3, [2, 1, 0, ])
	
	
	etat2.eqs = [
		(Chem([Permut('0'), Bord('0'), ])	,	Chem([Bord('1')])),
		(Chem([Permut('0'), Bord('1'), ])	,	Chem([Bord('0')])),
		(Chem([Permut('0'), Intern(''), ])	,	Chem([Intern('')])),
		(Chem([Permut('0'), Sub('0'), ])	,	Chem([Sub('2'), Permut('0'), ])),
		(Chem([Permut('0'), Sub('1'), ])	,	Chem([Sub('1'), Permut('0'), ])),
		(Chem([Permut('0'), Sub('2'), ])	,	Chem([Sub('0'), Permut('0'), ])),
		]
	
	
	etat2.prim.elems = [Figure(1, [Chem([Bord('0')]), Chem([Bord('1')]), ])]
	etat2.grid.elems = [Figure(1, [Chem([Bord('0')]), Chem([Intern('')]), Chem([Bord('1')]), ])]
	
	
	etat2.space = [Chem([Bord('0'), Intern('0'), Intern('0'), ]), Chem([Intern('0'), Intern('0'), ]), Chem([Bord('1'), Intern('0'), Intern('0'), ]), ]
	
	etat2.initMat[Chem([Sub('0')])] = FMat([
		[Coef('Const', 1           ), Coef('Const', 0.666667    ), Coef('Const', 0.444444    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.333333    ), Coef('Const', 0.444444    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.111111    ), ], ])
	etat2.initMat[Chem([Sub('1')])] = FMat([
		[Coef('Const', 0.444444    ), Coef('Const', 0.222222    ), Coef('Const', 0.111111    ), ], 
		[Coef('Const', 0.444444    ), Coef('Const', 0.555556    ), Coef('Const', 0.444444    ), ], 
		[Coef('Const', 0.111111    ), Coef('Const', 0.222222    ), Coef('Const', 0.444444    ), ], ])
	etat2.initMat[Chem([Sub('2')])] = FMat([
		[Coef('Const', 0.111111    ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.444444    ), Coef('Const', 0.333333    ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.444444    ), Coef('Const', 0.666667    ), Coef('Const', 1           ), ], ])
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
