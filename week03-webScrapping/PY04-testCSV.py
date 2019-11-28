#writing to a CSV file 
#lab 03 question 8
import csv

employee_file = open('employee_file.csv', mode='w')
#employee_writer is a variable  
employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

employee_writer.writerow(['John Smith', 'Accounting', 'November'])
employee_writer.writerow(['Erica Meyers, what', 'IT', 'March'])

employee_file.close()