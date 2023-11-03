import pandas as pd
from bs4 import BeautifulSoup

def createTable(dataFrame, name):
    archiveHTML=dataFrame.to_html()
    archiveRoute=f'tables/{name}.html'
    
    header='''
        <!DOCTYPE html>
        <html>
            <head>
            <title>Tables</title>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
            </head>
        </html>
    '''
    soup=BeautifulSoup(archiveHTML,'html.parser')
    
    for tr in soup.find_all('tr'):
        tr.attrs.pop('style', None)
        
    archiveHTML=str(soup)
    archiveHTML=archiveHTML.replace('<table border="1" class="dataframe">', '<table class="table table-striped">')    
    with open(archiveRoute, "w") as archive:
        archive.write(f"{header}\n{archiveHTML}\n</body>\n</html>\n")