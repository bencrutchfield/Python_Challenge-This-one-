
import os


import csv


input_file = os.path.join('raw_data','employee_data1.csv')
output_file = os.path.join('formated_employee_data1.csv')


emp_id = []
full_name = []
dob = []
formated_dob = []
ssn = []
formated_ssn = []
state = []

first_name = []
last_name = []

dob_year = []
dob_month = []
dob_day = []

us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

with open(input_file, newline='') as csvfile:

    
    csvreader = csv.reader(csvfile, delimiter=',')

   
    for row in csvreader:
        emp_id.append(row[0])
        full_name.append(row[1])
        dob.append(row[2])
        ssn.append(row[3])
        state.append(row[4])   

full_name.pop(0)
dob.pop(0)
ssn.pop(0)
state.pop(0)
emp_id.pop(0)

for i in range(len(full_name)):
    first_name.append(full_name[i].split(" ")[0])
    last_name.append(full_name[i].split(" ")[1])
    dob_year.append(dob[i].split("-")[0])
    dob_month.append(dob[i].split("-")[1])
    dob_day.append(dob[i].split("-")[2])
    formated_dob.append(f"{dob_month[i]}/{dob_day[i]}/{dob_year[i]}")
    ssn[i]= ssn[i].replace(ssn[i][0:6],"***-**")

with open(output_file, 'w', newline='') as csvfile:

    
    csvwriter = csv.writer(csvfile, delimiter=',')

    
    csvwriter.writerow(['Emp ID','First Name','Last Name','DOB','SSN','State'])

    for i in range(len(emp_id)):
        csvwriter.writerow([emp_id[i],first_name[i],last_name[i],formated_dob[i],ssn[i],state[i]])