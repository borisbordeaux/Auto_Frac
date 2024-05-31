# -*- coding: utf-8 -*-

# Automatically generated, from file : result_g3.py, function : modele()

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
	etat4 = Etat('C2',0)
	etat5 = Etat('B3',1)
	etat6 = Etat('B2',1)
	etat7 = Etat('s',1)
	
	
	etat0.subs   = {Sub('0'): etat1, }
	
	etat0.eqs = [
		]
	
	
	etat0.space = []
	
	etat0.initMat[Chem([Sub('0')])] = FMat([
		[Coef('Var'  , 6           ), Coef('Var'  , 3           ), Coef('Var'  , 0           ), Coef('Var'  ,-3           ), Coef('Var'  ,-6           ), Coef('Var'  ,-3.24        ), Coef('Var'  ,-3           ), Coef('Var'  , 3           ), Coef('Var'  , 3.24        ), ], 
		[Coef('Var'  , 0.002222    ), Coef('Var'  , 5.19838     ), Coef('Var'  , 3.9         ), Coef('Var'  , 5.19838     ), Coef('Var'  , 0.002222    ), Coef('Var'  ,-1.87        ), Coef('Var'  ,-5.19393     ), Coef('Var'  ,-5.19393     ), Coef('Var'  ,-1.87        ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), ], ])
	
	
	
	etat1.bords   = {Bord('0'): etat4, Bord('1'): etat5, Bord('2'): etat4, Bord('3'): etat6, Bord('4'): etat4, Bord('5'): etat6, }
	etat1.permuts = {}
	etat1.interns = {Intern('_'): etat1, }
	etat1.subs    = {Sub('0'): etat1, Sub('1'): etat2, Sub('2'): etat1, Sub('3'): etat3, Sub('4'): etat3, Sub('5'): etat3, Sub('6'): etat3, Sub('G', True): Etat.etatPoint, }
	
	etat1.buildIntern()
	
	
	etat1.eqs = [
		(Chem([Bord('0'), Sub('1'), ])	,	Chem([Sub('0'), Bord('0'), ])),
		(Chem([Bord('1'), Sub('0'), ])	,	Chem([Sub('0'), Bord('1'), ])),
		(Chem([Bord('1'), Sub('1'), ])	,	Chem([Sub('1'), Bord('0'), ])),
		(Chem([Bord('1'), Sub('2'), ])	,	Chem([Sub('2'), Bord('1'), ])),
		(Chem([Bord('2'), Sub('0'), ])	,	Chem([Sub('2'), Bord('2'), ])),
		(Chem([Bord('2'), Sub('1'), ])	,	Chem([Sub('3'), Bord('0'), ])),
		(Chem([Bord('3'), Sub('0'), ])	,	Chem([Sub('3'), Bord('1'), ])),
		(Chem([Bord('3'), Sub('1'), ])	,	Chem([Sub('4'), Bord('5'), ])),
		(Chem([Bord('4'), Sub('0'), ])	,	Chem([Sub('4'), Bord('0'), ])),
		(Chem([Bord('4'), Sub('1'), ])	,	Chem([Sub('5'), Bord('0'), ])),
		(Chem([Bord('5'), Sub('0'), ])	,	Chem([Sub('5'), Bord('1'), ])),
		(Chem([Bord('5'), Sub('1'), ])	,	Chem([Sub('6'), Bord('5'), ])),
		(Chem([Bord('0'), Sub('0'), ])	,	Chem([Sub('6'), Bord('0'), ])),
		(Chem([Sub('0'), Bord('2'), Permut('0'), ])	,	Chem([Sub('1'), Bord('3'), ])),
		(Chem([Sub('1'), Bord('1'), Permut('0'), ])	,	Chem([Sub('2'), Bord('0'), ])),
		(Chem([Sub('2'), Bord('4'), Permut('0'), ])	,	Chem([Sub('3'), Bord('4'), ])),
		(Chem([Sub('3'), Bord('2'), Permut('0'), ])	,	Chem([Sub('4'), Bord('4'), ])),
		(Chem([Sub('4'), Bord('2'), Permut('0'), ])	,	Chem([Sub('5'), Bord('4'), ])),
		(Chem([Sub('5'), Bord('2'), Permut('0'), ])	,	Chem([Sub('6'), Bord('4'), ])),
		(Chem([Sub('6'), Bord('2'), Permut('0'), ])	,	Chem([Sub('0'), Bord('4'), ])),
		(Chem([Bord('0'), Bord('1'), ])	,	Chem([Bord('1'), Bord('0'), ])),
		(Chem([Bord('1'), Bord('1'), ])	,	Chem([Bord('2'), Bord('0'), ])),
		(Chem([Bord('2'), Bord('1'), ])	,	Chem([Bord('3'), Bord('0'), ])),
		(Chem([Bord('3'), Bord('1'), ])	,	Chem([Bord('4'), Bord('0'), ])),
		(Chem([Bord('4'), Bord('1'), ])	,	Chem([Bord('5'), Bord('0'), ])),
		(Chem([Bord('5'), Bord('1'), ])	,	Chem([Bord('0'), Bord('0'), ])),
		]
	
	
	etat1.prim.elems = [Figure(2, [Chem([Bord('0'), Bord('0'), ]), Chem([Bord('1'), Sub('0'), Bord('0'), ]), Chem([Bord('1'), Sub('1'), Bord('0'), ]), Chem([Bord('1'), Sub('2'), Bord('0'), ]), Chem([Bord('2'), Bord('0'), ]), Chem([Bord('3'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('3'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('3'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('3'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('4'), Bord('0'), ]), Chem([Bord('5'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('5'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('5'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('5'), Sub('1'), Sub('1'), Bord('0'), ]), ])]
	etat1.grid.elems = [
		Figure(1, [Chem([Bord('1'), Bord('0'), ]), Chem([Bord('1'), Intern(''), ]), Chem([Bord('1'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('2'), Bord('0'), ]), Chem([Bord('2'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('3'), Bord('0'), ]), Chem([Bord('3'), Intern(''), ]), Chem([Bord('3'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('4'), Bord('0'), ]), Chem([Bord('4'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('5'), Bord('0'), ]), Chem([Bord('5'), Intern(''), ]), Chem([Bord('5'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('0'), Bord('0'), ]), Chem([Bord('0'), Bord('1'), ]), ]), ]
	
	
	etat1.space = [Chem([Bord('5'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('2'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('3'), Intern('0'), Intern('0'), ]), Chem([Bord('3'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('4'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('5'), Intern('0'), Intern('0'), ]), ]
	
	etat1.initMat[Chem([Sub('0')])] = FMat([
		[Coef('Const', 0.333333    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.136155    ), Coef('Var'  , 0.169057    ), Coef('Var'  , 0.184914    ), Coef('Var'  , 0.276782    ), Coef('Var'  , 0.256003    ), ], 
		[Coef('Const', 0.666667    ), Coef('Const', 1           ), Coef('Const', 0.666667    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.230866    ), Coef('Var'  , 0.225903    ), Coef('Var'  , 0.189791    ), Coef('Var'  , 0.275513    ), Coef('Var'  , 0.296696    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.333333    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.191329    ), Coef('Var'  , 0.17531     ), Coef('Var'  , 0.142364    ), Coef('Var'  , 0.172129    ), Coef('Var'  , 0.195747    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.111111    ), Coef('Var'  , 0.20547     ), Coef('Var'  , 0.167675    ), Coef('Var'  , 0.115851    ), Coef('Var'  , 0.109574    ), Coef('Var'  , 0.151432    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0853631   ), Coef('Var'  , 0.0526016   ), Coef('Var'  , 0.0370339   ), Coef('Var'  ,-0.0550961   ), Coef('Var'  ,-0.0345236   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0583448   ), Coef('Var'  , 0.0484142   ), Coef('Var'  , 0.0559685   ), Coef('Var'  ,-0.00820144  ), Coef('Var'  ,-0.00853435  ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  ,-0.00934762  ), Coef('Var'  ,-0.00424471  ), Coef('Var'  , 0.0321571   ), Coef('Var'  ,-0.0538271   ), Coef('Var'  ,-0.0752164   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0160481   ), Coef('Var'  , 0.0539831   ), Coef('Var'  , 0.106097    ), Coef('Var'  , 0.112112    ), Coef('Var'  , 0.0700466   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0857722   ), Coef('Var'  , 0.1113      ), Coef('Var'  , 0.135824    ), Coef('Var'  , 0.171013    ), Coef('Var'  , 0.14835     ), ], ])
	etat1.initMat[Chem([Sub('1')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0754771   ), Coef('Var'  , 0.10673     ), Coef('Var'  , 0.136155    ), ], 
		[Coef('Const', 0.444444    ), Coef('Const', 0.222222    ), Coef('Const', 0.111111    ), Coef('Var'  , 0.199757    ), Coef('Var'  , 0.234487    ), Coef('Var'  , 0.230866    ), ], 
		[Coef('Const', 0.444444    ), Coef('Const', 0.555556    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.190753    ), Coef('Var'  , 0.205044    ), Coef('Var'  , 0.191329    ), ], 
		[Coef('Const', 0.111111    ), Coef('Const', 0.222222    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.235041    ), Coef('Var'  , 0.238456    ), Coef('Var'  , 0.20547     ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.146046    ), Coef('Var'  , 0.114668    ), Coef('Var'  , 0.0853631   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0913925   ), Coef('Var'  , 0.067525    ), Coef('Var'  , 0.0583448   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.021766    ), Coef('Var'  ,-0.0130891   ), Coef('Var'  ,-0.00934762  ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  ,-0.0135184   ), Coef('Var'  ,-0.0170582   ), Coef('Var'  , 0.0160481   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0532854   ), Coef('Var'  , 0.0632384   ), Coef('Var'  , 0.0857722   ), ], ])
	etat1.initMat[Chem([Sub('2')])] = FMat([
		[Coef('Var'  , 0.0754771   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  ,-0.0427192   ), Coef('Var'  ,-0.0614881   ), Coef('Var'  , 0.0262453   ), Coef('Var'  , 0.0446612   ), ], 
		[Coef('Var'  , 0.199757    ), Coef('Const', 0.111111    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.140267    ), Coef('Var'  , 0.0975502   ), Coef('Var'  , 0.110841    ), Coef('Var'  , 0.164269    ), ], 
		[Coef('Var'  , 0.190753    ), Coef('Const', 0.444444    ), Coef('Const', 0.333333    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.19046     ), Coef('Var'  , 0.165525    ), Coef('Var'  , 0.142652    ), Coef('Var'  , 0.175732    ), ], 
		[Coef('Var'  , 0.235041    ), Coef('Const', 0.444444    ), Coef('Const', 0.666667    ), Coef('Const', 1           ), Coef('Const', 0.666667    ), Coef('Var'  , 0.293749    ), Coef('Var'  , 0.26991     ), Coef('Var'  , 0.195569    ), Coef('Var'  , 0.230435    ), ], 
		[Coef('Var'  , 0.146046    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.333333    ), Coef('Var'  , 0.264245    ), Coef('Var'  , 0.283233    ), Coef('Var'  , 0.1957      ), Coef('Var'  , 0.176994    ), ], 
		[Coef('Var'  , 0.0913925   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.155362    ), Coef('Var'  , 0.177695    ), Coef('Var'  , 0.141509    ), Coef('Var'  , 0.115381    ), ], 
		[Coef('Var'  , 0.021766    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0812587   ), Coef('Var'  , 0.124194    ), Coef('Var'  , 0.111104    ), Coef('Var'  , 0.0573857   ), ], 
		[Coef('Var'  ,-0.0135184   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  ,-0.0722231   ), Coef('Var'  ,-0.0481659   ), Coef('Var'  , 0.0263766   ), Coef('Var'  ,-0.0087805   ), ], 
		[Coef('Var'  , 0.0532854   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  ,-0.0103986   ), Coef('Var'  ,-0.00845385  ), Coef('Var'  , 0.0500032   ), Coef('Var'  , 0.043922    ), ], ])
	etat1.initMat[Chem([Sub('3')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0327936   ), Coef('Var'  , 0.0100669   ), Coef('Var'  , 0.0262453   ), Coef('Var'  ,-0.0614881   ), Coef('Var'  ,-0.0821756   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.03634     ), Coef('Var'  , 0.0590207   ), Coef('Var'  , 0.110841    ), Coef('Var'  , 0.0975502   ), Coef('Var'  , 0.0515637   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0844703   ), Coef('Var'  , 0.109938    ), Coef('Var'  , 0.142652    ), Coef('Var'  , 0.165525    ), Coef('Var'  , 0.138862    ), ], 
		[Coef('Const', 0.333333    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.114775    ), Coef('Var'  , 0.16007     ), Coef('Var'  , 0.195569    ), Coef('Var'  , 0.26991     ), Coef('Var'  , 0.244729    ), ], 
		[Coef('Const', 0.666667    ), Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.189663    ), Coef('Var'  , 0.212166    ), Coef('Var'  , 0.1957      ), Coef('Var'  , 0.283233    ), Coef('Var'  , 0.304154    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.166435    ), Coef('Var'  , 0.166249    ), Coef('Var'  , 0.141509    ), Coef('Var'  , 0.177695    ), Coef('Var'  , 0.20191     ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.186116    ), Coef('Var'  , 0.163212    ), Coef('Var'  , 0.111104    ), Coef('Var'  , 0.124194    ), Coef('Var'  , 0.170415    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.107682    ), Coef('Var'  , 0.0621626   ), Coef('Var'  , 0.0263766   ), Coef('Var'  ,-0.0481659   ), Coef('Var'  ,-0.0227499   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0817258   ), Coef('Var'  , 0.0571156   ), Coef('Var'  , 0.0500032   ), Coef('Var'  ,-0.00845385  ), Coef('Var'  ,-0.00670774  ), ], ])
	etat1.initMat[Chem([Sub('4')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.068594    ), Coef('Var'  , 0.109968    ), Coef('Var'  , 0.110209    ), Coef('Var'  , 0.0563537   ), Coef('Var'  , 0.0327936   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  ,-0.0784635   ), Coef('Var'  ,-0.0643222   ), Coef('Var'  , 0.0430906   ), Coef('Var'  , 0.0167644   ), Coef('Var'  , 0.03634     ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  ,-0.014802    ), Coef('Var'  ,-0.0196985   ), Coef('Var'  , 0.0605639   ), Coef('Var'  , 0.061014    ), Coef('Var'  , 0.0844703   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  ,-0.0353937   ), Coef('Var'  ,-0.0626046   ), Coef('Var'  , 0.0442143   ), Coef('Var'  , 0.0717418   ), Coef('Var'  , 0.114775    ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.154734    ), Coef('Var'  , 0.113403    ), Coef('Var'  , 0.112457    ), Coef('Var'  , 0.166308    ), Coef('Var'  , 0.189663    ), Coef('Const', 0.25        ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.195667    ), Coef('Var'  , 0.175721    ), Coef('Var'  , 0.136326    ), Coef('Var'  , 0.165188    ), Coef('Var'  , 0.166435    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 1           ), Coef('Const', 0.666667    ), Coef('Var'  , 0.301791    ), Coef('Var'  , 0.287693    ), Coef('Var'  , 0.179575    ), Coef('Var'  , 0.205898    ), Coef('Var'  , 0.186116    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.333333    ), Coef('Var'  , 0.258722    ), Coef('Var'  , 0.285975    ), Coef('Var'  , 0.178452    ), Coef('Var'  , 0.15092     ), Coef('Var'  , 0.107682    ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.149152    ), Coef('Var'  , 0.173866    ), Coef('Var'  , 0.135112    ), Coef('Var'  , 0.105812    ), Coef('Var'  , 0.0817258   ), Coef('Const', 0           ), Coef('Const', 0           ), ], ])
	etat1.initMat[Chem([Sub('5')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.185171    ), Coef('Var'  , 0.16199     ), Coef('Var'  , 0.110209    ), Coef('Var'  , 0.109968    ), Coef('Var'  , 0.145049    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.111759    ), Coef('Var'  , 0.0695826   ), Coef('Var'  , 0.0430906   ), Coef('Var'  ,-0.0643222   ), Coef('Var'  ,-0.0533271   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0838942   ), Coef('Var'  , 0.061014    ), Coef('Var'  , 0.0605639   ), Coef('Var'  ,-0.0196985   ), Coef('Var'  ,-0.024595    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0378184   ), Coef('Var'  , 0.0189235   ), Coef('Var'  , 0.0442143   ), Coef('Var'  ,-0.0626046   ), Coef('Var'  ,-0.086669    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0372905   ), Coef('Var'  , 0.0606719   ), Coef('Var'  , 0.112457    ), Coef('Var'  , 0.113403    ), Coef('Var'  , 0.0783648   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0844332   ), Coef('Var'  , 0.108144    ), Coef('Var'  , 0.136326    ), Coef('Var'  , 0.175721    ), Coef('Var'  , 0.159172    ), ], 
		[Coef('Const', 0.333333    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.110703    ), Coef('Var'  , 0.153079    ), Coef('Var'  , 0.179575    ), Coef('Var'  , 0.287693    ), Coef('Var'  , 0.276741    ), ], 
		[Coef('Const', 0.666667    ), Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.184643    ), Coef('Var'  , 0.203739    ), Coef('Var'  , 0.178452    ), Coef('Var'  , 0.285975    ), Coef('Var'  , 0.310083    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.164289    ), Coef('Var'  , 0.162856    ), Coef('Var'  , 0.135112    ), Coef('Var'  , 0.173866    ), Coef('Var'  , 0.195182    ), ], ])
	etat1.initMat[Chem([Sub('6')])] = FMat([
		[Coef('Const', 1           ), Coef('Const', 0.666667    ), Coef('Var'  , 0.291243    ), Coef('Var'  , 0.276782    ), Coef('Var'  , 0.184914    ), Coef('Var'  , 0.205879    ), Coef('Var'  , 0.185171    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.333333    ), Coef('Var'  , 0.259257    ), Coef('Var'  , 0.275513    ), Coef('Var'  , 0.189791    ), Coef('Var'  , 0.154954    ), Coef('Var'  , 0.111759    ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.154559    ), Coef('Var'  , 0.172129    ), Coef('Var'  , 0.142364    ), Coef('Var'  , 0.108462    ), Coef('Var'  , 0.0838942   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0789342   ), Coef('Var'  , 0.109574    ), Coef('Var'  , 0.115851    ), Coef('Var'  , 0.060197    ), Coef('Var'  , 0.0378184   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  ,-0.0694022   ), Coef('Var'  ,-0.0550961   ), Coef('Var'  , 0.0370339   ), Coef('Var'  , 0.0163662   ), Coef('Var'  , 0.0372905   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  ,-0.00741485  ), Coef('Var'  ,-0.00820144  ), Coef('Var'  , 0.0559685   ), Coef('Var'  , 0.0612324   ), Coef('Var'  , 0.0844332   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  ,-0.0374161   ), Coef('Var'  ,-0.0538271   ), Coef('Var'  , 0.0321571   ), Coef('Var'  , 0.0672919   ), Coef('Var'  , 0.110703    ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.142906    ), Coef('Var'  , 0.112112    ), Coef('Var'  , 0.106097    ), Coef('Var'  , 0.162048    ), Coef('Var'  , 0.184643    ), Coef('Const', 0.25        ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.187334    ), Coef('Var'  , 0.171013    ), Coef('Var'  , 0.135824    ), Coef('Var'  , 0.163569    ), Coef('Var'  , 0.164289    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), ], ])
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
	
	
	
	etat2.bords   = {Bord('0'): etat5, Bord('1'): etat4, Bord('2'): etat6, Bord('3'): etat4, }
	etat2.permuts = {}
	etat2.interns = {Intern('_'): etat2, }
	etat2.subs    = {Sub('0'): etat2, Sub('1'): etat1, Sub('2'): etat3, Sub('3'): etat3, Sub('4'): etat1, Sub('G', True): Etat.etatPoint, }
	
	etat2.buildIntern()
	
	
	etat2.eqs = [
		(Chem([Bord('0'), Sub('1'), ])	,	Chem([Sub('0'), Bord('0'), ])),
		(Chem([Bord('0'), Sub('2'), ])	,	Chem([Sub('1'), Bord('1'), ])),
		(Chem([Bord('1'), Sub('0'), ])	,	Chem([Sub('1'), Bord('2'), ])),
		(Chem([Bord('1'), Sub('1'), ])	,	Chem([Sub('2'), Bord('0'), ])),
		(Chem([Bord('2'), Sub('0'), ])	,	Chem([Sub('2'), Bord('1'), ])),
		(Chem([Bord('2'), Sub('1'), ])	,	Chem([Sub('3'), Bord('5'), ])),
		(Chem([Bord('3'), Sub('0'), ])	,	Chem([Sub('3'), Bord('0'), ])),
		(Chem([Bord('3'), Sub('1'), ])	,	Chem([Sub('4'), Bord('0'), ])),
		(Chem([Bord('0'), Sub('0'), ])	,	Chem([Sub('4'), Bord('1'), ])),
		(Chem([Sub('0'), Bord('1'), Permut('0'), ])	,	Chem([Sub('1'), Bord('0'), ])),
		(Chem([Sub('1'), Bord('4'), Permut('0'), ])	,	Chem([Sub('2'), Bord('4'), ])),
		(Chem([Sub('2'), Bord('2'), Permut('0'), ])	,	Chem([Sub('3'), Bord('4'), ])),
		(Chem([Sub('3'), Bord('2'), Permut('0'), ])	,	Chem([Sub('4'), Bord('4'), ])),
		(Chem([Sub('4'), Bord('2'), Permut('0'), ])	,	Chem([Sub('0'), Bord('3'), ])),
		(Chem([Bord('0'), Bord('1'), ])	,	Chem([Bord('1'), Bord('0'), ])),
		(Chem([Bord('1'), Bord('1'), ])	,	Chem([Bord('2'), Bord('0'), ])),
		(Chem([Bord('2'), Bord('1'), ])	,	Chem([Bord('3'), Bord('0'), ])),
		(Chem([Bord('3'), Bord('1'), ])	,	Chem([Bord('0'), Bord('0'), ])),
		]
	
	
	etat2.prim.elems = [Figure(2, [Chem([Bord('0'), Sub('0'), Bord('0'), ]), Chem([Bord('0'), Sub('1'), Bord('0'), ]), Chem([Bord('0'), Sub('2'), Bord('0'), ]), Chem([Bord('1'), Bord('0'), ]), Chem([Bord('2'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('2'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('2'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('2'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('3'), Bord('0'), ]), ])]
	etat2.grid.elems = [
		Figure(1, [Chem([Bord('1'), Bord('0'), ]), Chem([Bord('1'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('2'), Bord('0'), ]), Chem([Bord('2'), Intern(''), ]), Chem([Bord('2'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('0'), Bord('0'), ]), Chem([Bord('0'), Intern(''), ]), Chem([Bord('0'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('3'), Bord('0'), ]), Chem([Bord('3'), Bord('1'), ]), ]), ]
	
	
	etat2.space = [Chem([Bord('0'), Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('2'), Intern('0'), Intern('0'), ]), Chem([Bord('2'), Bord('1'), Intern('0'), Intern('0'), ]), ]
	
	etat2.initMat[Chem([Sub('0')])] = FMat([
		[Coef('Const', 0.444444    ), Coef('Const', 0.222222    ), Coef('Const', 0.111111    ), Coef('Var'  , 0.213587    ), Coef('Var'  , 0.276165    ), Coef('Var'  , 0.289557    ), ], 
		[Coef('Const', 0.444444    ), Coef('Const', 0.555556    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.234401    ), Coef('Var'  , 0.254391    ), Coef('Var'  , 0.23474     ), ], 
		[Coef('Const', 0.111111    ), Coef('Const', 0.222222    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.281514    ), Coef('Var'  , 0.265731    ), Coef('Var'  , 0.204882    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0973869   ), Coef('Var'  , 0.0454752   ), Coef('Var'  , 0.0481372   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.118271    ), Coef('Var'  , 0.103739    ), Coef('Var'  , 0.117642    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0548407   ), Coef('Var'  , 0.0544991   ), Coef('Var'  , 0.105041    ), ], ])
	etat2.initMat[Chem([Sub('1')])] = FMat([
		[Coef('Var'  , 0.213587    ), Coef('Const', 0.111111    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  ,-0.0173212   ), Coef('Var'  ,-0.0490664   ), Coef('Var'  , 0.121997    ), Coef('Var'  , 0.153718    ), ], 
		[Coef('Var'  , 0.234401    ), Coef('Const', 0.444444    ), Coef('Const', 0.333333    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.209374    ), Coef('Var'  , 0.163386    ), Coef('Var'  , 0.175289    ), Coef('Var'  , 0.214024    ), ], 
		[Coef('Var'  , 0.281514    ), Coef('Const', 0.444444    ), Coef('Const', 0.666667    ), Coef('Const', 1           ), Coef('Const', 0.666667    ), Coef('Var'  , 0.456802    ), Coef('Var'  , 0.37871     ), Coef('Var'  , 0.232912    ), Coef('Var'  , 0.293605    ), ], 
		[Coef('Var'  , 0.0973869   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.333333    ), Coef('Var'  , 0.26089     ), Coef('Var'  , 0.307856    ), Coef('Var'  , 0.190548    ), Coef('Var'  , 0.147772    ), ], 
		[Coef('Var'  , 0.118271    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.137242    ), Coef('Var'  , 0.170101    ), Coef('Var'  , 0.160765    ), Coef('Var'  , 0.133064    ), ], 
		[Coef('Var'  , 0.0548407   ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  ,-0.0469873   ), Coef('Var'  , 0.0290139   ), Coef('Var'  , 0.11849     ), Coef('Var'  , 0.0578164   ), ], ])
	etat2.initMat[Chem([Sub('2')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.138734    ), Coef('Var'  , 0.0943942   ), Coef('Var'  , 0.121997    ), Coef('Var'  ,-0.0490664   ), Coef('Var'  ,-0.0858241   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.137658    ), Coef('Var'  , 0.138002    ), Coef('Var'  , 0.175289    ), Coef('Var'  , 0.163386    ), Coef('Var'  , 0.114373    ), ], 
		[Coef('Const', 0.333333    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.125469    ), Coef('Var'  , 0.171499    ), Coef('Var'  , 0.232912    ), Coef('Var'  , 0.37871     ), Coef('Var'  , 0.298467    ), ], 
		[Coef('Const', 0.666667    ), Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.201399    ), Coef('Var'  , 0.229831    ), Coef('Var'  , 0.190548    ), Coef('Var'  , 0.307856    ), Coef('Var'  , 0.359798    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.187434    ), Coef('Var'  , 0.187415    ), Coef('Var'  , 0.160765    ), Coef('Var'  , 0.170101    ), Coef('Var'  , 0.205134    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.209307    ), Coef('Var'  , 0.178859    ), Coef('Var'  , 0.11849     ), Coef('Var'  , 0.0290139   ), Coef('Var'  , 0.108051    ), ], ])
	etat2.initMat[Chem([Sub('3')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0.333333    ), Coef('Var'  , 0.317594    ), Coef('Var'  , 0.385027    ), Coef('Var'  , 0.24638     ), Coef('Var'  , 0.184594    ), Coef('Var'  , 0.138734    ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.120461    ), Coef('Var'  , 0.16361     ), Coef('Var'  , 0.177988    ), Coef('Var'  , 0.138405    ), Coef('Var'  , 0.137658    ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  ,-0.0981674   ), Coef('Var'  ,-0.0632792   ), Coef('Var'  , 0.112595    ), Coef('Var'  , 0.0805143   ), Coef('Var'  , 0.125469    ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0958045   ), Coef('Var'  , 0.0274285   ), Coef('Var'  , 0.108679    ), Coef('Var'  , 0.171356    ), Coef('Var'  , 0.201399    ), Coef('Const', 0.25        ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.198747    ), Coef('Var'  , 0.167726    ), Coef('Var'  , 0.158211    ), Coef('Var'  , 0.186668    ), Coef('Var'  , 0.187434    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 1           ), Coef('Const', 0.666667    ), Coef('Var'  , 0.365561    ), Coef('Var'  , 0.319488    ), Coef('Var'  , 0.196146    ), Coef('Var'  , 0.238462    ), Coef('Var'  , 0.209307    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), ], ])
	etat2.initMat[Chem([Sub('4')])] = FMat([
		[Coef('Const', 0.666667    ), Coef('Const', 1           ), Coef('Const', 0.666667    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.289557    ), Coef('Var'  , 0.304899    ), Coef('Var'  , 0.24638     ), Coef('Var'  , 0.385027    ), Coef('Var'  , 0.475195    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.333333    ), Coef('Const', 0.444444    ), Coef('Var'  , 0.23474     ), Coef('Var'  , 0.214212    ), Coef('Var'  , 0.177988    ), Coef('Var'  , 0.16361     ), Coef('Var'  , 0.217145    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.111111    ), Coef('Var'  , 0.204882    ), Coef('Var'  , 0.139941    ), Coef('Var'  , 0.112595    ), Coef('Var'  ,-0.0632792   ), Coef('Var'  ,-0.0266207   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0481372   ), Coef('Var'  , 0.0500454   ), Coef('Var'  , 0.108679    ), Coef('Var'  , 0.0274285   ), Coef('Var'  ,-0.0616042   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.117642    ), Coef('Var'  , 0.132158    ), Coef('Var'  , 0.158211    ), Coef('Var'  , 0.167726    ), Coef('Var'  , 0.129204    ), ], 
		[Coef('Const', 0.333333    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.105041    ), Coef('Var'  , 0.158745    ), Coef('Var'  , 0.196146    ), Coef('Var'  , 0.319488    ), Coef('Var'  , 0.266681    ), ], ])
	etat2.initMat[Chem([Sub('G')])] = FMat([
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], 
		[Coef('Const', 0.166667    )], ])
	
	
	
	etat3.bords   = {Bord('0'): etat4, Bord('1'): etat6, Bord('2'): etat4, Bord('3'): etat6, Bord('4'): etat4, Bord('5'): etat6, }
	etat3.permuts = {}
	etat3.interns = {Intern('_'): etat3, }
	etat3.subs    = {Sub('0'): etat3, Sub('1'): etat3, Sub('2'): etat3, Sub('3'): etat3, Sub('4'): etat3, Sub('5'): etat3, Sub('G', True): Etat.etatPoint, }
	
	etat3.buildIntern()
	
	
	etat3.eqs = [
		(Chem([Bord('0'), Sub('1'), ])	,	Chem([Sub('0'), Bord('0'), ])),
		(Chem([Bord('1'), Sub('0'), ])	,	Chem([Sub('0'), Bord('1'), ])),
		(Chem([Bord('1'), Sub('1'), ])	,	Chem([Sub('1'), Bord('5'), ])),
		(Chem([Bord('2'), Sub('0'), ])	,	Chem([Sub('1'), Bord('0'), ])),
		(Chem([Bord('2'), Sub('1'), ])	,	Chem([Sub('2'), Bord('0'), ])),
		(Chem([Bord('3'), Sub('0'), ])	,	Chem([Sub('2'), Bord('1'), ])),
		(Chem([Bord('3'), Sub('1'), ])	,	Chem([Sub('3'), Bord('5'), ])),
		(Chem([Bord('4'), Sub('0'), ])	,	Chem([Sub('3'), Bord('0'), ])),
		(Chem([Bord('4'), Sub('1'), ])	,	Chem([Sub('4'), Bord('0'), ])),
		(Chem([Bord('5'), Sub('0'), ])	,	Chem([Sub('4'), Bord('1'), ])),
		(Chem([Bord('5'), Sub('1'), ])	,	Chem([Sub('5'), Bord('5'), ])),
		(Chem([Bord('0'), Sub('0'), ])	,	Chem([Sub('5'), Bord('0'), ])),
		(Chem([Sub('0'), Bord('2'), Permut('0'), ])	,	Chem([Sub('1'), Bord('4'), ])),
		(Chem([Sub('1'), Bord('2'), Permut('0'), ])	,	Chem([Sub('2'), Bord('4'), ])),
		(Chem([Sub('2'), Bord('2'), Permut('0'), ])	,	Chem([Sub('3'), Bord('4'), ])),
		(Chem([Sub('3'), Bord('2'), Permut('0'), ])	,	Chem([Sub('4'), Bord('4'), ])),
		(Chem([Sub('4'), Bord('2'), Permut('0'), ])	,	Chem([Sub('5'), Bord('4'), ])),
		(Chem([Sub('5'), Bord('2'), Permut('0'), ])	,	Chem([Sub('0'), Bord('4'), ])),
		(Chem([Bord('0'), Bord('1'), ])	,	Chem([Bord('1'), Bord('0'), ])),
		(Chem([Bord('1'), Bord('1'), ])	,	Chem([Bord('2'), Bord('0'), ])),
		(Chem([Bord('2'), Bord('1'), ])	,	Chem([Bord('3'), Bord('0'), ])),
		(Chem([Bord('3'), Bord('1'), ])	,	Chem([Bord('4'), Bord('0'), ])),
		(Chem([Bord('4'), Bord('1'), ])	,	Chem([Bord('5'), Bord('0'), ])),
		(Chem([Bord('5'), Bord('1'), ])	,	Chem([Bord('0'), Bord('0'), ])),
		]
	
	
	etat3.prim.elems = [Figure(2, [Chem([Bord('0'), Bord('0'), ]), Chem([Bord('1'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('1'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('1'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('1'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('2'), Bord('0'), ]), Chem([Bord('3'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('3'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('3'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('3'), Sub('1'), Sub('1'), Bord('0'), ]), Chem([Bord('4'), Bord('0'), ]), Chem([Bord('5'), Sub('0'), Sub('0'), Bord('0'), ]), Chem([Bord('5'), Sub('0'), Sub('1'), Bord('0'), ]), Chem([Bord('5'), Sub('1'), Sub('0'), Bord('0'), ]), Chem([Bord('5'), Sub('1'), Sub('1'), Bord('0'), ]), ])]
	etat3.grid.elems = [
		Figure(1, [Chem([Bord('1'), Bord('0'), ]), Chem([Bord('1'), Intern(''), ]), Chem([Bord('1'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('2'), Bord('0'), ]), Chem([Bord('2'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('3'), Bord('0'), ]), Chem([Bord('3'), Intern(''), ]), Chem([Bord('3'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('4'), Bord('0'), ]), Chem([Bord('4'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('5'), Bord('0'), ]), Chem([Bord('5'), Intern(''), ]), Chem([Bord('5'), Bord('1'), ]), ]), 
		Figure(1, [Chem([Bord('0'), Bord('0'), ]), Chem([Bord('0'), Bord('1'), ]), ]), ]
	
	
	etat3.space = [Chem([Bord('5'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('2'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('3'), Intern('0'), Intern('0'), ]), Chem([Bord('3'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('4'), Bord('1'), Intern('0'), Intern('0'), ]), Chem([Bord('5'), Intern('0'), Intern('0'), ]), ]
	
	etat3.initMat[Chem([Sub('0')])] = FMat([
		[Coef('Const', 0.333333    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.129313    ), Coef('Var'  , 0.167462    ), Coef('Var'  , 0.181541    ), Coef('Var'  , 0.291526    ), Coef('Var'  , 0.285257    ), ], 
		[Coef('Const', 0.666667    ), Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.178749    ), Coef('Var'  , 0.190096    ), Coef('Var'  , 0.165373    ), Coef('Var'  , 0.248445    ), Coef('Var'  , 0.27338     ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.151299    ), Coef('Var'  , 0.151067    ), Coef('Var'  , 0.132258    ), Coef('Var'  , 0.164203    ), Coef('Var'  , 0.181598    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.1754      ), Coef('Var'  , 0.162782    ), Coef('Var'  , 0.125458    ), Coef('Var'  , 0.145982    ), Coef('Var'  , 0.178339    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.119062    ), Coef('Var'  , 0.0829689   ), Coef('Var'  , 0.0579533   ), Coef('Var'  ,-0.0257326   ), Coef('Var'  ,-0.00895879  ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0843565   ), Coef('Var'  , 0.0626812   ), Coef('Var'  , 0.0623079   ), Coef('Var'  ,-0.0134655   ), Coef('Var'  ,-0.0169724   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0509365   ), Coef('Var'  , 0.0279638   ), Coef('Var'  , 0.0423513   ), Coef('Var'  ,-0.0637089   ), Coef('Var'  ,-0.0811303   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0288674   ), Coef('Var'  , 0.0495527   ), Coef('Var'  , 0.0999839   ), Coef('Var'  , 0.0850714   ), Coef('Var'  , 0.0419979   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0820168   ), Coef('Var'  , 0.105427    ), Coef('Var'  , 0.132773    ), Coef('Var'  , 0.167679    ), Coef('Var'  , 0.14649     ), ], ])
	etat3.initMat[Chem([Sub('1')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0272288   ), Coef('Var'  ,-0.00697446  ), Coef('Var'  , 0.0554481   ), Coef('Var'  , 0.0946267   ), Coef('Var'  , 0.129313    ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.184398    ), Coef('Var'  , 0.148807    ), Coef('Var'  , 0.126266    ), Coef('Var'  , 0.169265    ), Coef('Var'  , 0.178749    ), Coef('Const', 0.25        ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.175241    ), Coef('Var'  , 0.158988    ), Coef('Var'  , 0.131986    ), Coef('Var'  , 0.152049    ), Coef('Var'  , 0.151299    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 1           ), Coef('Const', 0.666667    ), Coef('Var'  , 0.249856    ), Coef('Var'  , 0.232449    ), Coef('Var'  , 0.165353    ), Coef('Var'  , 0.187813    ), Coef('Var'  , 0.1754      ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.333333    ), Coef('Var'  , 0.230214    ), Coef('Var'  , 0.252291    ), Coef('Var'  , 0.176603    ), Coef('Var'  , 0.152216    ), Coef('Var'  , 0.119062    ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.132859    ), Coef('Var'  , 0.158996    ), Coef('Var'  , 0.134373    ), Coef('Var'  , 0.103844    ), Coef('Var'  , 0.0843565   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.083927    ), Coef('Var'  , 0.124626    ), Coef('Var'  , 0.11955     ), Coef('Var'  , 0.0711653   ), Coef('Var'  , 0.0509365   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  ,-0.0797946   ), Coef('Var'  ,-0.0607141   ), Coef('Var'  , 0.0339864   ), Coef('Var'  , 0.00882739  ), Coef('Var'  , 0.0288674   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  ,-0.00392861  ), Coef('Var'  ,-0.00847031  ), Coef('Var'  , 0.0564346   ), Coef('Var'  , 0.0601932   ), Coef('Var'  , 0.0820168   ), Coef('Const', 0           ), Coef('Const', 0           ), ], ])
	etat3.initMat[Chem([Sub('2')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.026215    ), Coef('Var'  , 0.0184256   ), Coef('Var'  , 0.0554481   ), Coef('Var'  ,-0.00697446  ), Coef('Var'  ,-0.0431053   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0571193   ), Coef('Var'  , 0.0836297   ), Coef('Var'  , 0.126266    ), Coef('Var'  , 0.148807    ), Coef('Var'  , 0.114867    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0930135   ), Coef('Var'  , 0.11173     ), Coef('Var'  , 0.131986    ), Coef('Var'  , 0.158988    ), Coef('Var'  , 0.144187    ), ], 
		[Coef('Const', 0.333333    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.106715    ), Coef('Var'  , 0.141865    ), Coef('Var'  , 0.165353    ), Coef('Var'  , 0.232449    ), Coef('Var'  , 0.218192    ), ], 
		[Coef('Const', 0.666667    ), Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.179805    ), Coef('Var'  , 0.198837    ), Coef('Var'  , 0.176603    ), Coef('Var'  , 0.252291    ), Coef('Var'  , 0.277092    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.166927    ), Coef('Var'  , 0.163749    ), Coef('Var'  , 0.134373    ), Coef('Var'  , 0.158996    ), Coef('Var'  , 0.185642    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.184966    ), Coef('Var'  , 0.166856    ), Coef('Var'  , 0.11955     ), Coef('Var'  , 0.124626    ), Coef('Var'  , 0.164728    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.107626    ), Coef('Var'  , 0.0607277   ), Coef('Var'  , 0.0339864   ), Coef('Var'  ,-0.0607141   ), Coef('Var'  ,-0.0459692   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.077613    ), Coef('Var'  , 0.0541797   ), Coef('Var'  , 0.0564346   ), Coef('Var'  ,-0.00847031  ), Coef('Var'  ,-0.0156332   ), ], ])
	etat3.initMat[Chem([Sub('3')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0087432   ), Coef('Var'  , 0.0585889   ), Coef('Var'  , 0.0863072   ), Coef('Var'  , 0.0333863   ), Coef('Var'  , 0.026215    ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  ,-0.0655069   ), Coef('Var'  ,-0.0577506   ), Coef('Var'  , 0.045979    ), Coef('Var'  , 0.0330673   ), Coef('Var'  , 0.0571193   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0170688   ), Coef('Var'  , 0.0121874   ), Coef('Var'  , 0.0738581   ), Coef('Var'  , 0.0760117   ), Coef('Var'  , 0.0930135   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  ,-0.0201937   ), Coef('Var'  ,-0.0446686   ), Coef('Var'  , 0.0540559   ), Coef('Var'  , 0.074756    ), Coef('Var'  , 0.106715    ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.14883     ), Coef('Var'  , 0.0988108   ), Coef('Var'  , 0.111214    ), Coef('Var'  , 0.162428    ), Coef('Var'  , 0.179805    ), Coef('Const', 0.25        ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.207829    ), Coef('Var'  , 0.181373    ), Coef('Var'  , 0.140438    ), Coef('Var'  , 0.16976     ), Coef('Var'  , 0.166927    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 1           ), Coef('Const', 0.666667    ), Coef('Var'  , 0.288363    ), Coef('Var'  , 0.263939    ), Coef('Var'  , 0.171727    ), Coef('Var'  , 0.201357    ), Coef('Var'  , 0.184966    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.333333    ), Coef('Var'  , 0.271988    ), Coef('Var'  , 0.309481    ), Coef('Var'  , 0.183159    ), Coef('Var'  , 0.150277    ), Coef('Var'  , 0.107626    ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.142877    ), Coef('Var'  , 0.178039    ), Coef('Var'  , 0.133262    ), Coef('Var'  , 0.0989572   ), Coef('Var'  , 0.077613    ), Coef('Const', 0           ), Coef('Const', 0           ), ], ])
	etat3.initMat[Chem([Sub('4')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.173282    ), Coef('Var'  , 0.141933    ), Coef('Var'  , 0.0863072   ), Coef('Var'  , 0.0585889   ), Coef('Var'  , 0.110341    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0999309   ), Coef('Var'  , 0.0615414   ), Coef('Var'  , 0.045979    ), Coef('Var'  ,-0.0577506   ), Coef('Var'  ,-0.0498014   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0915169   ), Coef('Var'  , 0.0728839   ), Coef('Var'  , 0.0738581   ), Coef('Var'  , 0.0121874   ), Coef('Var'  , 0.00705226  ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0570201   ), Coef('Var'  , 0.0345475   ), Coef('Var'  , 0.0540559   ), Coef('Var'  ,-0.0446686   ), Coef('Var'  ,-0.0701962   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0402866   ), Coef('Var'  , 0.0581889   ), Coef('Var'  , 0.111214    ), Coef('Var'  , 0.0988108   ), Coef('Var'  , 0.0468368   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0836141   ), Coef('Var'  , 0.109092    ), Coef('Var'  , 0.140438    ), Coef('Var'  , 0.181373    ), Coef('Var'  , 0.153933    ), ], 
		[Coef('Const', 0.333333    ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0971411   ), Coef('Var'  , 0.139007    ), Coef('Var'  , 0.171727    ), Coef('Var'  , 0.263939    ), Coef('Var'  , 0.238662    ), ], 
		[Coef('Const', 0.666667    ), Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.188746    ), Coef('Var'  , 0.214774    ), Coef('Var'  , 0.183159    ), Coef('Var'  , 0.309481    ), Coef('Var'  , 0.348561    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.168462    ), Coef('Var'  , 0.168032    ), Coef('Var'  , 0.133262    ), Coef('Var'  , 0.178039    ), Coef('Var'  , 0.214613    ), ], ])
	etat3.initMat[Chem([Sub('5')])] = FMat([
		[Coef('Const', 1           ), Coef('Const', 0.666667    ), Coef('Var'  , 0.299756    ), Coef('Var'  , 0.291526    ), Coef('Var'  , 0.181541    ), Coef('Var'  , 0.200444    ), Coef('Var'  , 0.173282    ), Coef('Const', 0.25        ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.333333    ), Coef('Var'  , 0.220177    ), Coef('Var'  , 0.248445    ), Coef('Var'  , 0.165373    ), Coef('Var'  , 0.134872    ), Coef('Var'  , 0.0999309   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.144262    ), Coef('Var'  , 0.164203    ), Coef('Var'  , 0.132258    ), Coef('Var'  , 0.108749    ), Coef('Var'  , 0.0915169   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.108554    ), Coef('Var'  , 0.145982    ), Coef('Var'  , 0.125458    ), Coef('Var'  , 0.078389    ), Coef('Var'  , 0.0570201   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  ,-0.0459443   ), Coef('Var'  ,-0.0257326   ), Coef('Var'  , 0.0579533   ), Coef('Var'  , 0.0254556   ), Coef('Var'  , 0.0402866   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  ,-0.0100396   ), Coef('Var'  ,-0.0134655   ), Coef('Var'  , 0.0623079   ), Coef('Var'  , 0.0610961   ), Coef('Var'  , 0.0836141   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  ,-0.0443718   ), Coef('Var'  ,-0.0637089   ), Coef('Var'  , 0.0423513   ), Coef('Var'  , 0.0595389   ), Coef('Var'  , 0.0971411   ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.135002    ), Coef('Var'  , 0.0850714   ), Coef('Var'  , 0.0999839   ), Coef('Var'  , 0.163708    ), Coef('Var'  , 0.188746    ), Coef('Const', 0.25        ), Coef('Const', 0           ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.192604    ), Coef('Var'  , 0.167679    ), Coef('Var'  , 0.132773    ), Coef('Var'  , 0.167748    ), Coef('Var'  , 0.168462    ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), ], ])
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
	
	
	
	etat4.bords   = {Bord('0'): etat7, Bord('1'): etat7, }
	etat4.permuts = {Permut('0'): etat4, }
	etat4.interns = {Intern('_'): etat4, }
	etat4.subs    = {Sub('0'): etat4, Sub('1'): etat4, Sub('G', True): Etat.etatPoint, }
	
	etat4.buildIntern()
	etat4.fm_[Permut('0')] = PMat(2, [1, 0, ])
	
	
	etat4.eqs = [
		(Chem([Permut('0'), Bord('0'), ])	,	Chem([Bord('1')])),
		(Chem([Permut('0'), Bord('1'), ])	,	Chem([Bord('0')])),
		(Chem([Permut('0'), Sub('0'), ])	,	Chem([Sub('1'), Permut('0'), ])),
		(Chem([Permut('0'), Sub('1'), ])	,	Chem([Sub('0'), Permut('0'), ])),
		(Chem([Bord('0'), Sub('0'), ])	,	Chem([Sub('0'), Bord('0'), ])),
		(Chem([Bord('1'), Sub('0'), ])	,	Chem([Sub('1'), Bord('1'), ])),
		]
	
	
	etat4.prim.elems = []
	etat4.grid.elems = [Figure(1, [Chem([Bord('0')]), Chem([Bord('1')]), ])]
	
	
	etat4.space = [Chem([Bord('0'), Intern('0'), Intern('0'), ]), Chem([Bord('1'), Intern('0'), Intern('0'), ]), ]
	
	etat4.initMat[Chem([Sub('0')])] = FMat([
		[Coef('Const', 1           ), Coef('Const', 0.666667    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.333333    ), ], ])
	etat4.initMat[Chem([Sub('1')])] = FMat([
		[Coef('Const', 0.333333    ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.666667    ), Coef('Const', 1           ), ], ])
	etat4.initMat[Chem([Sub('G')])] = FMat([
		[Coef('Const', 0.5         )], 
		[Coef('Const', 0.5         )], ])
	
	
	
	etat5.bords   = {Bord('0'): etat7, Bord('1'): etat7, }
	etat5.permuts = {Permut('0'): etat5, }
	etat5.interns = {Intern('_'): etat5, }
	etat5.subs    = {Sub('0'): etat5, Sub('1'): etat5, Sub('2'): etat5, Sub('G', True): Etat.etatPoint, }
	
	etat5.buildIntern()
	etat5.fm_[Permut('0')] = PMat(3, [2, 1, 0, ])
	
	
	etat5.eqs = [
		(Chem([Permut('0'), Bord('0'), ])	,	Chem([Bord('1')])),
		(Chem([Permut('0'), Bord('1'), ])	,	Chem([Bord('0')])),
		(Chem([Permut('0'), Intern(''), ])	,	Chem([Intern('')])),
		(Chem([Permut('0'), Sub('0'), ])	,	Chem([Sub('2'), Permut('0'), ])),
		(Chem([Permut('0'), Sub('1'), ])	,	Chem([Sub('1'), Permut('0'), ])),
		(Chem([Permut('0'), Sub('2'), ])	,	Chem([Sub('0'), Permut('0'), ])),
		]
	
	
	etat5.prim.elems = [Figure(1, [Chem([Bord('0')]), Chem([Bord('1')]), ])]
	etat5.grid.elems = [Figure(1, [Chem([Bord('0')]), Chem([Intern('')]), Chem([Bord('1')]), ])]
	
	
	etat5.space = [Chem([Bord('0'), Intern('0'), Intern('0'), ]), Chem([Intern('0'), Intern('0'), ]), Chem([Bord('1'), Intern('0'), Intern('0'), ]), ]
	
	etat5.initMat[Chem([Sub('0')])] = FMat([
		[Coef('Const', 1           ), Coef('Const', 0.666667    ), Coef('Const', 0.444444    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.333333    ), Coef('Const', 0.444444    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.111111    ), ], ])
	etat5.initMat[Chem([Sub('1')])] = FMat([
		[Coef('Const', 0.444444    ), Coef('Const', 0.222222    ), Coef('Const', 0.111111    ), ], 
		[Coef('Const', 0.444444    ), Coef('Const', 0.555556    ), Coef('Const', 0.444444    ), ], 
		[Coef('Const', 0.111111    ), Coef('Const', 0.222222    ), Coef('Const', 0.444444    ), ], ])
	etat5.initMat[Chem([Sub('2')])] = FMat([
		[Coef('Const', 0.111111    ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.444444    ), Coef('Const', 0.333333    ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.444444    ), Coef('Const', 0.666667    ), Coef('Const', 1           ), ], ])
	etat5.initMat[Chem([Sub('G')])] = FMat([
		[Coef('Const', 0           )], 
		[Coef('Const', 1           )], 
		[Coef('Const', 0           )], ])
	
	
	
	etat6.bords   = {Bord('0'): etat7, Bord('1'): etat7, }
	etat6.permuts = {Permut('0'): etat6, }
	etat6.interns = {Intern('_'): etat6, }
	etat6.subs    = {Sub('0'): etat6, Sub('1'): etat6, Sub('G', True): Etat.etatPoint, }
	
	etat6.buildIntern()
	etat6.fm_[Permut('0')] = PMat(3, [2, 1, 0, ])
	
	
	etat6.eqs = [
		(Chem([Permut('0'), Bord('0'), ])	,	Chem([Bord('1')])),
		(Chem([Permut('0'), Bord('1'), ])	,	Chem([Bord('0')])),
		(Chem([Permut('0'), Intern(''), ])	,	Chem([Intern('')])),
		(Chem([Permut('0'), Sub('0'), ])	,	Chem([Sub('1'), Permut('0'), ])),
		(Chem([Permut('0'), Sub('1'), ])	,	Chem([Sub('0'), Permut('0'), ])),
		]
	
	
	etat6.prim.elems = [Figure(1, [Chem([Bord('0')]), Chem([Bord('1')]), ])]
	etat6.grid.elems = [Figure(1, [Chem([Bord('0')]), Chem([Intern('')]), Chem([Bord('1')]), ])]
	
	
	etat6.space = [Chem([Bord('0'), Intern('0'), Intern('0'), ]), Chem([Intern('0'), Intern('0'), ]), Chem([Bord('1'), Intern('0'), Intern('0'), ]), ]
	
	etat6.initMat[Chem([Sub('0')])] = FMat([
		[Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), ], ])
	etat6.initMat[Chem([Sub('1')])] = FMat([
		[Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), ], ])
	etat6.initMat[Chem([Sub('G')])] = FMat([
		[Coef('Const', 0           )], 
		[Coef('Const', 1           )], 
		[Coef('Const', 0           )], ])
	
	
	
	etat7.bords   = {}
	etat7.permuts = {}
	etat7.interns = {Intern('_'): etat7, }
	etat7.subs    = {Sub('0'): etat7, Sub('G', True): Etat.etatPoint, }
	
	etat7.buildIntern()
	
	
	etat7.eqs = [
		]
	
	
	etat7.prim.elems = []
	etat7.grid.elems = []
	
	
	etat7.space = [Chem([Intern('0'), Intern('0'), ])]
	
	etat7.initMat[Chem([Sub('0')])] = FMat([[Coef('Const', 1           )]])
	etat7.initMat[Chem([Sub('G')])] = FMat([[Coef('Const', 1           )]])
	
	
	
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
