from asyncore import write
import csv

header = ['name', 'area', 'country_code2', 'country_code3']
data = [('Afghanistan', 652090, 'AF', 'AFG'),
        ('India', 2652090, 'IN', 'IND'),
        ('Pakistan', 752090, 'PK', 'PAK'),
        ('China', 3652090, 'CH', 'CHN')]

with open('countries.csv', 'w', encoding='UTF8',newline='') as f:
    writer = csv.writer(f)
    # write the header
    writer.writerow(header)
    for row in data:
        # write the data
        writer.writerow(row)

f.close()

with open('countries.csv', 'r', encoding='UTF8') as f:
    csv_reader = csv.reader(f)
    for line in csv_reader:
        print(line)

f.close()

with open('countries.csv', 'a', encoding='UTF8') as f:
    write = csv.writer(f,lineterminator='\n')
    write.writerow(['Nepal',350040,'NP','NEP'])

f.close()