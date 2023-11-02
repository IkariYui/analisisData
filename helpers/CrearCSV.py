import csv

def createCSVUsers(list, nameArchive):
    with open('data/'+nameArchive, mode='w', newline='', encoding='utf-8') as archiveCSV:
        writer = csv.writer(archiveCSV)
        writer.writerow(['Name', 'Password', 'Age'])
        writer.writerows(list)

def createCSVSnacks (list, nameArchive):
    with open('data/' +nameArchive, mode='w', newline='', encoding='utf-8') as archiveCSV:
        writer = csv.writer(archiveCSV)
        writer.writerow(['Name', 'Drink', 'Cuantity'])        
        writer.writerows(list)


