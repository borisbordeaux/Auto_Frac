# -*- coding: utf-8 -*-

# Automatically generated, from file : square_B2_full_B2_corner.py, function : modele()

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
		[Coef('Var'  ,-0.54068     ), Coef('Var'  , 0.478929    ), Coef('Var'  , 1.47691     ), Coef('Var'  , 1.01469     ), Coef('Var'  , 0.550932    ), Coef('Var'  ,-0.458656    ), Coef('Var'  ,-1.4667      ), Coef('Var'  ,-1.01355     ), ], 
		[Coef('Var'  , 1.47638     ), Coef('Var'  , 1.00797     ), Coef('Var'  , 0.550354    ), Coef('Var'  ,-0.455809    ), Coef('Var'  ,-1.46728     ), Coef('Var'  ,-0.996355    ), Coef('Var'  ,-0.541258    ), Coef('Var'  , 0.453075    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), ], 
		[Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), Coef('Var'  , 1           ), ], ])
	
	
	
	etat1.bords   = {Bord('0'): etat2, Bord('1'): etat2, Bord('2'): etat2, Bord('3'): etat2, }
	etat1.permuts = {}
	etat1.interns = {Intern('_'): etat1, }
	etat1.subs    = {Sub('0'): etat1, Sub('G', True): Etat.etatPoint, Sub('1'): etat1, Sub('2'): etat1, Sub('3'): etat1, Sub('4'): etat1, Sub('5'): etat1, Sub('6'): etat1, Sub('7'): etat1, }
	
	etat1.buildIntern()
	
	
	etat1.eqs = [
		(Chem([Bord('0'), Sub('0'), ])	,	Chem([Sub('0'), Bord('0'), ])),
		(Chem([Bord('0'), Sub('1'), ])	,	Chem([Sub('1'), Bord('0'), ])),
		(Chem([Bord('1'), Sub('0'), ])	,	Chem([Sub('2'), Bord('0'), ])),
		(Chem([Bord('1'), Sub('1'), ])	,	Chem([Sub('3'), Bord('0'), ])),
		(Chem([Bord('2'), Sub('0'), ])	,	Chem([Sub('4'), Bord('0'), ])),
		(Chem([Bord('2'), Sub('1'), ])	,	Chem([Sub('5'), Bord('0'), ])),
		(Chem([Bord('3'), Sub('0'), ])	,	Chem([Sub('6'), Bord('0'), ])),
		(Chem([Bord('3'), Sub('1'), ])	,	Chem([Sub('7'), Bord('0'), ])),
		(Chem([Sub('0'), Bord('1'), Permut('0'), ])	,	Chem([Sub('1'), Bord('3'), ])),
		(Chem([Sub('1'), Bord('1'), Permut('0'), ])	,	Chem([Sub('2'), Bord('3'), ])),
		(Chem([Sub('2'), Bord('1'), Permut('0'), ])	,	Chem([Sub('3'), Bord('3'), ])),
		(Chem([Sub('3'), Bord('1'), Permut('0'), ])	,	Chem([Sub('4'), Bord('3'), ])),
		(Chem([Sub('4'), Bord('1'), Permut('0'), ])	,	Chem([Sub('5'), Bord('3'), ])),
		(Chem([Sub('5'), Bord('1'), Permut('0'), ])	,	Chem([Sub('6'), Bord('3'), ])),
		(Chem([Sub('6'), Bord('1'), Permut('0'), ])	,	Chem([Sub('7'), Bord('3'), ])),
		(Chem([Sub('7'), Bord('1'), Permut('0'), ])	,	Chem([Sub('0'), Bord('3'), ])),
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
		[Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.258203    ), Coef('Var'  , 0.218833    ), Coef('Var'  , 0.261545    ), Coef('Var'  , 0.262607    ), Coef('Var'  , 0.360687    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.259084    ), Coef('Var'  , 0.220035    ), Coef('Var'  , 0.221358    ), Coef('Var'  , 0.193037    ), Coef('Var'  , 0.241548    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.26004     ), Coef('Var'  , 0.221278    ), Coef('Var'  , 0.182105    ), Coef('Var'  , 0.125013    ), Coef('Var'  , 0.125058    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.12637     ), Coef('Var'  , 0.126542    ), Coef('Var'  , 0.0856419   ), Coef('Var'  , 0.0564964   ), Coef('Var'  , 0.0076879   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  ,-0.00795865  ), Coef('Var'  , 0.0313397   ), Coef('Var'  ,-0.0113261   ), Coef('Var'  ,-0.0124093   ), Coef('Var'  ,-0.110348    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  ,-0.00805283  ), Coef('Var'  , 0.0306993   ), Coef('Var'  , 0.0291354   ), Coef('Var'  , 0.0570616   ), Coef('Var'  , 0.00862077  ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  ,-0.00979934  ), Coef('Var'  , 0.0288918   ), Coef('Var'  , 0.0681132   ), Coef('Var'  , 0.125186    ), Coef('Var'  , 0.125283    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.122113    ), Coef('Var'  , 0.122381    ), Coef('Var'  , 0.163428    ), Coef('Var'  , 0.193008    ), Coef('Var'  , 0.241463    ), ], ])
	etat1.initMat[Chem([Sub('G')])] = FMat([
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], 
		[Coef('Const', 0.125       )], ])
	etat1.initMat[Chem([Sub('1')])] = FMat([
		[Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.125759    ), Coef('Var'  , 0.124697    ), Coef('Var'  , 0.184371    ), Coef('Var'  , 0.218833    ), Coef('Var'  , 0.258203    ), ], 
		[Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Var'  , 0.245103    ), Coef('Var'  , 0.192529    ), Coef('Var'  , 0.221475    ), Coef('Var'  , 0.220035    ), Coef('Var'  , 0.259084    ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Var'  , 0.361961    ), Coef('Var'  , 0.258948    ), Coef('Var'  , 0.257848    ), Coef('Var'  , 0.221278    ), Coef('Var'  , 0.26004     ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.243397    ), Coef('Var'  , 0.192291    ), Coef('Var'  , 0.162029    ), Coef('Var'  , 0.126542    ), Coef('Var'  , 0.12637     ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.124334    ), Coef('Var'  , 0.125355    ), Coef('Var'  , 0.0657656   ), Coef('Var'  , 0.0313397   ), Coef('Var'  ,-0.00795865  ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.00653925  ), Coef('Var'  , 0.0583985   ), Coef('Var'  , 0.0294878   ), Coef('Var'  , 0.0306993   ), Coef('Var'  ,-0.00805283  ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  ,-0.111875    ), Coef('Var'  ,-0.00890072  ), Coef('Var'  ,-0.00771417  ), Coef('Var'  , 0.0288918   ), Coef('Var'  ,-0.00979934  ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.00478198  ), Coef('Var'  , 0.0566819   ), Coef('Var'  , 0.0867372   ), Coef('Var'  , 0.122381    ), Coef('Var'  , 0.122113    ), ], ])
	etat1.initMat[Chem([Sub('2')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  ,-0.00766322  ), Coef('Var'  , 0.03221     ), Coef('Var'  , 0.0776742   ), Coef('Var'  , 0.124697    ), Coef('Var'  , 0.125759    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.126819    ), Coef('Var'  , 0.127766    ), Coef('Var'  , 0.169601    ), Coef('Var'  , 0.192529    ), Coef('Var'  , 0.245103    ), ], 
		[Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.258407    ), Coef('Var'  , 0.221266    ), Coef('Var'  , 0.25958     ), Coef('Var'  , 0.258948    ), Coef('Var'  , 0.361961    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.257918    ), Coef('Var'  , 0.219449    ), Coef('Var'  , 0.216019    ), Coef('Var'  , 0.192291    ), Coef('Var'  , 0.243397    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.257524    ), Coef('Var'  , 0.217694    ), Coef('Var'  , 0.17231     ), Coef('Var'  , 0.125355    ), Coef('Var'  , 0.124334    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.12401     ), Coef('Var'  , 0.122834    ), Coef('Var'  , 0.0812973   ), Coef('Var'  , 0.0583985   ), Coef('Var'  , 0.00653925  ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  ,-0.00855085  ), Coef('Var'  , 0.0286343   ), Coef('Var'  ,-0.00959985  ), Coef('Var'  ,-0.00890072  ), Coef('Var'  ,-0.111875    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  ,-0.00846344  ), Coef('Var'  , 0.030146    ), Coef('Var'  , 0.0331189   ), Coef('Var'  , 0.0566819   ), Coef('Var'  , 0.00478198  ), ], ])
	etat1.initMat[Chem([Sub('3')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  ,-0.102164    ), Coef('Var'  ,-0.00880281  ), Coef('Var'  ,-0.00706601  ), Coef('Var'  , 0.03221     ), Coef('Var'  ,-0.00766322  ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0138129   ), Coef('Var'  , 0.0617319   ), Coef('Var'  , 0.0906744   ), Coef('Var'  , 0.127766    ), Coef('Var'  , 0.126819    ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.127214    ), Coef('Var'  , 0.130703    ), Coef('Var'  , 0.186285    ), Coef('Var'  , 0.221266    ), Coef('Var'  , 0.258407    ), ], 
		[Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Var'  , 0.239207    ), Coef('Var'  , 0.194475    ), Coef('Var'  , 0.22147     ), Coef('Var'  , 0.219449    ), Coef('Var'  , 0.257918    ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Var'  , 0.351838    ), Coef('Var'  , 0.258612    ), Coef('Var'  , 0.2569      ), Coef('Var'  , 0.217694    ), Coef('Var'  , 0.257524    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.23604     ), Coef('Var'  , 0.188212    ), Coef('Var'  , 0.159656    ), Coef('Var'  , 0.122834    ), Coef('Var'  , 0.12401     ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.122459    ), Coef('Var'  , 0.119106    ), Coef('Var'  , 0.0635456   ), Coef('Var'  , 0.0286343   ), Coef('Var'  ,-0.00855085  ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0115941   ), Coef('Var'  , 0.0559637   ), Coef('Var'  , 0.0285354   ), Coef('Var'  , 0.030146    ), Coef('Var'  ,-0.00846344  ), ], ])
	etat1.initMat[Chem([Sub('4')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  ,-0.00843929  ), Coef('Var'  , 0.0294401   ), Coef('Var'  ,-0.0102944   ), Coef('Var'  ,-0.00880281  ), Coef('Var'  ,-0.102164    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  ,-0.00626138  ), Coef('Var'  , 0.0317469   ), Coef('Var'  , 0.0329303   ), Coef('Var'  , 0.0617319   ), Coef('Var'  , 0.0138129   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  ,-0.00422283  ), Coef('Var'  , 0.0339383   ), Coef('Var'  , 0.0751592   ), Coef('Var'  , 0.130703    ), Coef('Var'  , 0.127214    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.126663    ), Coef('Var'  , 0.126932    ), Coef('Var'  , 0.167376    ), Coef('Var'  , 0.194475    ), Coef('Var'  , 0.239207    ), ], 
		[Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.258197    ), Coef('Var'  , 0.220387    ), Coef('Var'  , 0.26008     ), Coef('Var'  , 0.258612    ), Coef('Var'  , 0.351838    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.25527     ), Coef('Var'  , 0.217554    ), Coef('Var'  , 0.216627    ), Coef('Var'  , 0.188212    ), Coef('Var'  , 0.23604     ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.253984    ), Coef('Var'  , 0.215891    ), Coef('Var'  , 0.174627    ), Coef('Var'  , 0.119106    ), Coef('Var'  , 0.122459    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.124809    ), Coef('Var'  , 0.124111    ), Coef('Var'  , 0.0834936   ), Coef('Var'  , 0.0559637   ), Coef('Var'  , 0.0115941   ), ], ])
	etat1.initMat[Chem([Sub('5')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.126411    ), Coef('Var'  , 0.128347    ), Coef('Var'  , 0.0689958   ), Coef('Var'  , 0.0294401   ), Coef('Var'  ,-0.00843929  ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0110678   ), Coef('Var'  , 0.058675    ), Coef('Var'  , 0.0313495   ), Coef('Var'  , 0.0317469   ), Coef('Var'  ,-0.00626138  ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  ,-0.101871    ), Coef('Var'  ,-0.00954313  ), Coef('Var'  ,-0.00555195  ), Coef('Var'  , 0.0339383   ), Coef('Var'  ,-0.00422283  ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0105804   ), Coef('Var'  , 0.0558952   ), Coef('Var'  , 0.0874448   ), Coef('Var'  , 0.126932    ), Coef('Var'  , 0.126663    ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.123503    ), Coef('Var'  , 0.121606    ), Coef('Var'  , 0.180873    ), Coef('Var'  , 0.220387    ), Coef('Var'  , 0.258197    ), ], 
		[Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Var'  , 0.237361    ), Coef('Var'  , 0.190395    ), Coef('Var'  , 0.217706    ), Coef('Var'  , 0.217554    ), Coef('Var'  , 0.25527     ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Var'  , 0.351792    ), Coef('Var'  , 0.2595      ), Coef('Var'  , 0.255424    ), Coef('Var'  , 0.215891    ), Coef('Var'  , 0.253984    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.241156    ), Coef('Var'  , 0.195125    ), Coef('Var'  , 0.163759    ), Coef('Var'  , 0.124111    ), Coef('Var'  , 0.124809    ), ], ])
	etat1.initMat[Chem([Sub('6')])] = FMat([
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0.25        ), Coef('Var'  , 0.253148    ), Coef('Var'  , 0.215709    ), Coef('Var'  , 0.178858    ), Coef('Var'  , 0.128347    ), Coef('Var'  , 0.126411    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.122715    ), Coef('Var'  , 0.122492    ), Coef('Var'  , 0.0832508   ), Coef('Var'  , 0.058675    ), Coef('Var'  , 0.0110678   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  ,-0.00491062  ), Coef('Var'  , 0.0312797   ), Coef('Var'  ,-0.0103262   ), Coef('Var'  ,-0.00954313  ), Coef('Var'  ,-0.101871    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  ,-0.00391716  ), Coef('Var'  , 0.0328624   ), Coef('Var'  , 0.0303551   ), Coef('Var'  , 0.0558952   ), Coef('Var'  , 0.0105804   ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  ,-0.00301391  ), Coef('Var'  , 0.0343849   ), Coef('Var'  , 0.0711675   ), Coef('Var'  , 0.121606    ), Coef('Var'  , 0.123503    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.126477    ), Coef('Var'  , 0.126924    ), Coef('Var'  , 0.16585     ), Coef('Var'  , 0.190395    ), Coef('Var'  , 0.237361    ), ], 
		[Coef('Const', 1           ), Coef('Const', 0.5         ), Coef('Const', 0.25        ), Coef('Var'  , 0.255049    ), Coef('Var'  , 0.218818    ), Coef('Var'  , 0.260356    ), Coef('Var'  , 0.2595      ), Coef('Var'  , 0.351792    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Var'  , 0.254452    ), Coef('Var'  , 0.21753     ), Coef('Var'  , 0.220489    ), Coef('Var'  , 0.195125    ), Coef('Var'  , 0.241156    ), ], ])
	etat1.initMat[Chem([Sub('7')])] = FMat([
		[Coef('Const', 0.25        ), Coef('Const', 0.5         ), Coef('Const', 1           ), Coef('Var'  , 0.360687    ), Coef('Var'  , 0.262607    ), Coef('Var'  , 0.260591    ), Coef('Var'  , 0.215709    ), Coef('Var'  , 0.253148    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.241548    ), Coef('Var'  , 0.193037    ), Coef('Var'  , 0.166653    ), Coef('Var'  , 0.122492    ), Coef('Var'  , 0.122715    ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.125058    ), Coef('Var'  , 0.125013    ), Coef('Var'  , 0.074768    ), Coef('Var'  , 0.0312797   ), Coef('Var'  ,-0.00491062  ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.0076879   ), Coef('Var'  , 0.0564964   ), Coef('Var'  , 0.0323151   ), Coef('Var'  , 0.0328624   ), Coef('Var'  ,-0.00391716  ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  ,-0.110348    ), Coef('Var'  ,-0.0124093   ), Coef('Var'  ,-0.0104157   ), Coef('Var'  , 0.0343849   ), Coef('Var'  ,-0.00301391  ), ], 
		[Coef('Const', 0           ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.00862077  ), Coef('Var'  , 0.0570616   ), Coef('Var'  , 0.0830959   ), Coef('Var'  , 0.126924    ), Coef('Var'  , 0.126477    ), ], 
		[Coef('Const', 0.25        ), Coef('Const', 0           ), Coef('Const', 0           ), Coef('Var'  , 0.125283    ), Coef('Var'  , 0.125186    ), Coef('Var'  , 0.17541     ), Coef('Var'  , 0.218818    ), Coef('Var'  , 0.255049    ), ], 
		[Coef('Const', 0.5         ), Coef('Const', 0.5         ), Coef('Const', 0           ), Coef('Var'  , 0.241463    ), Coef('Var'  , 0.193008    ), Coef('Var'  , 0.217582    ), Coef('Var'  , 0.21753     ), Coef('Var'  , 0.254452    ), ], ])
	
	
	
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
