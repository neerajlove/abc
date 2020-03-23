import csv
import os
import requests
from bs4 import BeautifulSoup
# open html file and parsing lxml 
with open ('/Users/neeraj.joshi/Downloads/index.html') as html_file:
 soup = BeautifulSoup(html_file, 'lxml')
 #row = soup.find_all('tr')
 #column = row.find_all('td')
 #print(soup)
# create a file by any name and in order to write it in write mode type w
filename = '/Users/neeraj.joshi/Downloads/test.csv'
csv_writer = csv.writer(open(filename, 'w'))
# storing data in data variable

#assume tr as a columns
for tree in soup.find_all('tr'):
  data = []
 #assume td as rows 
  for todd in tree.find_all('td'): 
     #print(todd.text) "appending data of td into array data made up there  "

     data.append(todd.text)  
     print(data)
  csv_writer.writerow(data)  
 
    




        