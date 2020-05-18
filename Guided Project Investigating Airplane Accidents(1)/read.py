aviation_data = []
aviation_list = []

with open('AviationData.txt', 'r') as file:
    for row in file:
        aviation_data.append(row)
        line = row.split('|')
        cleaned_lines = [] # remove whitespace from each split
        for item in line:
            item = item.strip()
            cleaned_lines.append(item)
        aviation_list.append(cleaned_lines)

# print(aviation_data[1]) # first item in both lists
# print(aviation_list[1])

# search for lax code in a list of lists
lax_code = []

# Done by nested for loops
for r in aviation_list:
    for i in r:
        if i == 'LAX94LA336':
            lax_code.append(r)

# print(lax_code)

# Linear search function only search each row
def linear_search(code):
    lax_code = []
    for row in aviation_list:
        if code in row:
            lax_code.append(row)
    return lax_code

lin_search_lax = linear_search('LAX94LA336')
# print(lin_search_lax)

# Log time search function using binary search
def log_search(data,target):
    # define boundaries
    start = 0
    end = len(data) - 1
    while start <= end:
        middle = (start + end) // 2 # get an integer division
        midpoint = data[middle]
        if midpoint > target:
            end = middle - 1
        elif midpoint < target:
            start = middle + 1
        else:
            return midpoint

with open('AviationData.txt', 'r') as f:
    aviation_data_log = f.read()
    aviation_data_log = sorted(aviation_data_log.split())
    log_search_lax = log_search(aviation_data_log, 'LAX94LA336')
    # print(log_search_lax)

# Generate Hash table
aviation_dict_list = []
keys = aviation_data[0].split(' | ')
aviation_data_no_head = aviation_data[1:]
for row in aviation_data_no_head:
    row_split = row.split(' | ')
    a_dict = {}
    for i in range(len(row_split)):
        a_dict[keys[i]] = row_split[i]
    aviation_dict_list.append(a_dict)
# print(aviation_dict_list[0])

lax_dict = []
for dictionary in aviation_dict_list:
    if 'LAX94LA336' in dictionary.values():
        lax_dict.append(dictionary)
# print(lax_dict)

# Count number of accidents occuring in each state in US
from collections import Counter

state_accidents_count = []
for dictionary in aviation_dict_list:
    if 'Country' in dictionary:
        if dictionary['Country'] == 'United States':
            state_value = dictionary['Location'].split(', ') # Get the 2 letter state code
            try:
                state = state_value[1]
            except:
                state = ''
            if len(state) == 2:
                state_accidents_count.append(state)

state_accidents = Counter(state_accidents_count)
# print(state_accidents)

# Count how many fatilities and serious injuries occurred during each month and year
# We need Event Date (it is mm/dd/yyyy) Total Serious Injuries and Total Fatal Injuries

month_info = []
for dictionary in aviation_dict_list:
    month_data = []
    if 'Event Date' in dictionary:
        split_date = dictionary['Event Date'].split('/')
        try:
            serious_injuries = int(dictionary['Total Serious Injuries'])
        except:
            serious_injuries = 0
        try:
            fatal_injuries = int(dictionary['Total Fatal Injuries'])
        except:
            fatal_injuries = 0
        try:
            month_year = split_date[0]+'/'+split_date[2]
        except:
            month_year = ''
        if len(month_year) == 7:
            month_data.append(month_year)
            month_data.append(serious_injuries)
            month_data.append(fatal_injuries)
    month_info.append(month_data)

injury_and_fatilities_by_month = {}
for month in month_info:
    try:
        month_year = month[0]
        serious_injuries = month[1]
        fatal_injuries = month[2]
    except:
        continue
    if month_year not in injury_and_fatilities_by_month:
        injury_and_fatilities_by_month[month_year] = {'Serious Injuries':serious_injuries,'Fatal Injuries':fatal_injuries}
    else:
        injury_and_fatilities_by_month[month_year]['Serious Injuries'] += serious_injuries
        injury_and_fatilities_by_month[month_year]['Fatal Injuries'] += fatal_injuries

print(injury_and_fatilities_by_month)


            










    
    
    
        
        
    


          