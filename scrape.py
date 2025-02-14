import re
from datetime import datetime

# Define the file path and the search string
file_path = 'a.txt'
search_string = 'Mónic7 Lim5:' #'na@cc$TPzz'
password_pattern = r'[A-Za-z0-9@#$%^&*]{6,20}'
url_pattern = r'(https?://\S+|www\.\S+)'
date_pattern = r'\d{2}/\d{2}/\d{4}'

date2 = datetime.strptime('23/9/2021 00:00:00', "%d/%m/%Y %H:%M:%S")
date3 = datetime.strptime('23/11/2025 00:00:00', "%d/%m/%Y %H:%M:%S")

# Open the file and search for passwords, ignoring lines with links
with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
    possible_passwords = []
    for line in [line for line in file if search_string.lower() in line.lower()]:
        Matches()
         
# Remove duplicates (if needed) and print results
unique_passwords = list(sorted(possible_passwords, key=lambda x: x["date"]))
print("Possible passwords found in the chat (excluding links):")
for password in unique_passwords:
    print(password['date'] + ' \t ' + password['match'])

CountUniqueWords():
    

Matches():
    matchdate = re.findall(date_pattern, line)
    if matchdate:
        # Extract the date part (group 1)
        raw_date = matchdate[0]
        # Optionally parse and reformat the date
        try:
            parsed_date = datetime.strptime(raw_date, "%m/%d/%Y")
        except ValueError:
            # If not MM/DD/YYYY, try DD/MM/YYYY
            parsed_date = datetime.strptime(raw_date, "%d/%m/%Y")
        if parsed_date < date2 or parsed_date > date3:
            continue
        else:
            # Skip lines containing URLs
            if re.search(url_pattern, line):
                continue
            
            # Find potential passwords in the line
            matches = re.findall(password_pattern, line)
            a = str(parsed_date)
            for i in range(len(matches)):
                matches[i] = { 'match': matches[i], 'date': str(parsed_date) }

            if matches:
                possible_passwords.extend(matches)