import csv

data = [["PASSWORD","KEY","PLATFORM USED"]]
def store_data(password: str, key: str, platform: str)-> list[str]:
    data.append([password,key,platform])
    return data

def saveToCSV():
    with open('passwords.csv', 'a') as csv_file:  
        writer = csv.writer(csv_file)
        for item in data[1:]:
            writer.writerow(item)