#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 10:21:10 2017

@author: bowenwang
"""
import csv 
import pylab
# Steps:
# 1.try/except/else to open the data file 
# 2.if successful:
# 3. read the data into a dictionary, year as keys
# 4. prompt the user 
# 5. Make sure the user selected a valid year 
# 6. and make sure that year has 12 months 
# 7. If so, draw the graph

def user_chart():
    source ='NYC_Jobs_annual_out.csv'
    try:
        s= open(source,'r')
    except:
        print("File not found or cannot be found")
        
    else:
        reader =csv.reader(s) 
        d ={}
        t_list_values = []
        dep_list =[]
        for row in reader:
            dep = row[1]
            #print dep
            salary = row[9]
            #print salary
            t_list_values.append(row[9])
            dep_list.append(row[1])
            d[dep] = salary
            
             #print salary
        #print t_list_values
          
#==============================================================================
#         t_list_values = []
#         
#         for i in range(len(salary)):
#              t_list_values.append(salary)
#              print salary
#==============================================================================
        #print salary  
        pylab.xlabel("Department")
        pylab.ylabel("Salary")   
        pylab.title("NYC Public salary Anual")
        
#        months = 'Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec'
#        m =months.split()
#        x = list(range(1,13))
       # x = list(range(1,3614))
      #  pylab.xticks(x,dep_list)
        #http://matplotlib.org/gallery.html#ticks_and_spines
        #Figure out how to plot with 3000 data points
        #pylab.plot(dep_list,t_list_values,color="green",linestyle ="dashed",marker ='o',markersize =4)
        #pylab.xticks(x,m)
        pylab.plot(t_list_values,color="green",linestyle ="dashed",marker ='o',markersize =4)
        pylab.show()
user_chart()            
#==============================================================================
# 
#         i = input ("Enter a year")
#     
#         okay_to_print= True
#         if i in d:
#             print("This year is available.")
#             if "*" in d[i]:
#                 print("These data are not valid")
#                 okay_to_print= False 
#                 
#         else:
#             print("This year is not aviablable")
#==============================================================================
