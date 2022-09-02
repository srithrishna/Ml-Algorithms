# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 23:41:37 2022

@author: J SRI THRISHNA
"""

def mean(rahul):
    num=len(rahul)
    summ=sum(rahul)
    rahul=summ/num
    print("the mean of rahul is",rahul)
mean([10,0,100,20,50])

def median(rahul):
    num=len(rahul)
    rahul.sort()
    if (num%2)==0:
        median1=rahul[num//2]
        median2=rahul[num//2-1]
        median=(median1+median2)/2
        print(median)
    else:
        median=rahul[num//2]
        print("the median of rahul's score is",median)

median([10,0,100,20,50])

from statistics import mode
def modes(rahul):
     if len(rahul)==len(set(rahul)):
          print("no mode found")
     else:
          print(statistics.mode(rahul))    
modes([10,0,100,20,50])

from statistics import stdev
def stand(rahul):
     print("the standard deviation of raghul",stdev(rahul))
     
stand([10,0,100,20,50])

def mean(ajay):
    num=len(ajay)
    summ=sum(ajay)
    ajay=summ/num
    print("the mean of ajay is",ajay)

mean([40,30,40,30,40])

def median(ajay):
    num=len(ajay)
    ajay.sort()
    if (num%2)==0:
        median1=ajay[num//2]
        median2=ajay[num//2-1]
        medians=(median1+median2)/2
        print("the median of ajay's score is",medians)
    else:
        medians=ajay[num//2]
        print("the median of ajay's score is",medians)
median([40,30,40,30,40])

from statistics import mode
def modes(ajay):
     if len(ajay)==len(set(ajay)):
          print("no mode found")
     else:
          print(mode(ajay))    
          
modes([40,30,40,30,40])

from statistics import stdev
def stand(ajay):
     print("the standard deviation of ajay",stdev(ajay))
stand([40,30,40,30,40])