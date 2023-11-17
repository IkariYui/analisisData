import csv

def createCSVUsers(list, nameArchive):
    with open('data/'+nameArchive, mode='w', newline='', encoding='utf-8') as archiveCSV:
        writer = csv.writer(archiveCSV)
        writer.writerow(['Name', 'Password',  'Age', 'Gender', 'Salary'])
        writer.writerows(list)

def createCSVSnacks (list, nameArchive):
    with open('data/' +nameArchive, mode='w', newline='', encoding='utf-8') as archiveCSV:
        writer = csv.writer(archiveCSV)
        writer.writerow(['Name', 'Price', 'Cuantity', 'totalPrice'])        
        writer.writerows(list)


def createCSVSowing (list, nameArchive):
    with open('data/' +nameArchive, mode='w', newline='', encoding='utf-8') as archiveCSV:
        writer = csv.writer(archiveCSV)
        writer.writerow(['Municipality', 'Treetype', 'Quantity'])        
        writer.writerows(list)
