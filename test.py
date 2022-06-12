# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 06:35:11 2022

@author: Lenovo
"""
sub1= input("Enter your marks ")
sub2= input("Enter your marks ")
sub3=input("Enter your marks ")
sub1=int(sub1)
sub2=int(sub2)
sub3=int(sub3)

from result import *
tot= total(sub1,sub2,sub3)
ave= average(tot)
res=result(ave)
print(tot,ave,res)
