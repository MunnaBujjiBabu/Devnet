import csv
sample_file = open('/Users/bmunna/Documents/GitHub/MunnaBujjiBabu_personal/Devnet/csvdata.csv')
sample_reader = csv.reader(sample_file)
sample_data = list(sample_reader)
print(sample_data[1])

with open('/Users/bmunna/Documents/GitHub/MunnaBujjiBabu_personal/Devnet/csvdata.csv') as data:
    csv_list = list(csv.reader(data))
    for i in csv_list:
        device = i[0]
        ip_address = i[1]
        location = i[2]
        print("device: ", device, "ip_address: ", ip_address, "location: ", location)