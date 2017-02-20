#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 09:55:21 2017

@author: bowenwang
"""


import matplotlib.pyplot as plt

def pie1():
    labels = ('DEPT OF HEALTH-Physician in Charge','DEPT. OF HOMELESS SERVICES-ADMINISTRATIVE DIRECTOR OF SOC','DEPT OF DESIGN & CONSTRUCTION-Executive Director','DEPT OF ENVIRONMENT PROTECTION-Deputy Commissioner','DEPT OF INFO TECH & TELECOMM-Cyber Security Program Lead ')
    sizes  = [225363,215942,208298,203566,200000] #completely made-up numbers!
    explode = [0.1,0,0,0,0]

    figure1,ax1 = plt.subplots()
    ax1.pie(sizes,explode=explode,labels=labels,shadow=False, \
            autopct='%1.1f%%')
    ax1.axis('equal')
    plt.title("NYC Top 5 Public job Salary composition")
    plt.show()

    
pie1()