##Who has the most openings?
##Which departments have the highest and the lowest paying positions (based on current job openings)?
##Which jobs do you think are the hardest to fill? (What makes you say that?)

import csv 
   
source = "NYC_Jobs (1) .csv"

s =open(source,'r')
reader =csv.reader(s)
target = "NYC_Jobs_out.csv"
t = open(target,'w')
writer =csv.writer(t)

temp_most_opening= 0
for row in reader:
    if row[3].isdigit():
        if int(row[3])>temp_most_opening:      
            temp_most_opening =int(row[3])

writer.writerow (("The number of most openings position is:",temp_most_opening))
print "The number of most openings position is:",temp_most_opening
s.close()

s =open(source,'r')
reader =csv.reader(s)           
temp_hig_salary= 0
for row in reader:
    if row[9].isdigit():
        if int(row[9])>temp_hig_salary:      
            temp_hig_salary =int(row[9])
writer.writerow (("The higest paying position is :",temp_hig_salary))
print "The higest paying position is :",temp_hig_salary

        
s.close()

s =open(source,'r')
reader =csv.reader(s)

temp_low_salary= []

for row in reader:
    temp_low_salary.append(row[9])
x =int(min(temp_low_salary))
writer.writerow (("The lowest paying position is :",x))
print "The lowest paying position is :",x

s.close()


s =open(source,'r')
reader =csv.reader(s)
temp_low_salary_dept =""
temp_low_salary_dept_row=[]
for row in reader:
    if row[9].isdigit():
        if int(row[9]) == x:      
            temp_low_salary_dept = row[1]
            temp_low_salary_dept_row=row

writer.writerow (("The department which has the lowest paying position is ",temp_hig_salary_dept))  
writer.writerow (temp_low_salary_dept_row)  
print "The department which has the lowest paying position is :",temp_low_salary_dept
s.close()

s =open(source,'r')
reader =csv.reader(s)
temp_hig_salary_dept =""
temp_hig_salary_dept_row=[]
for row in reader:
    if row[9].isdigit():
        if int(row[9]) == temp_hig_salary:      
            temp_hig_salary_dept = row[1] 
            temp_hig_salary_dept_row= row

writer.writerow (("The department which has the highest paying position is ",temp_hig_salary_dept))  
writer.writerow (temp_hig_salary_dept_row)              
print "The department which has the highest paying position is :",temp_hig_salary_dept
s.close()

s =open(source,'r')
reader =csv.reader(s)
temp_most_openings_dept =""
temp_most_openings_dept_row=[]
for row in reader:
    if row[3].isdigit():
        if int(row[3]) == temp_most_opening:      
            temp_most_openings_dept = row[1]
            temp_most_openings_dept_row= row

writer.writerow (("The department which has the most opening position is: ",temp_most_openings_dept))
writer.writerow (temp_most_openings_dept_row)            
print "The department which has the most opening position is :",temp_most_openings_dept

s.close()
t.close()
