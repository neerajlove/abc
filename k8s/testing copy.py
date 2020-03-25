import csv
import math

from selenium import webdriver

#browser = webdriver.Firefox("/usr/local/bin/")

#browser.get("https://forms.gle/QdsBB7FjscS2KYnq6")
#names = browser.find_element_by_name('entry.2005620554')
#ar1 = names.send_keys("name") 
#Phoneno = browser.find_element_by_name('entry.1045781291')
#ar2 = Phoneno.send_keys("4567")
#emailid = browser.find_element_by_name('entry.828990748')
#ar3 = emailid.send_keys("qwwe") 
#date = browser.find_element_by_name('entry.1166974658')
#ar4 = date.send_keys("date")
 #select = browser.find_element_by_xpath('/html/body/div/div[2]/form/div/div/div[3]/div[1]/div/div/span/span').click()



filename = "/Users/neeraj.joshi/Downloads/test.csv"
print(filename)
with open(filename, 'r') as f:
 kill = csv.reader(f, delimiter=",") 
 array = [ ]
 new = [ ]
 for line in kill:
   array.append(line)
   a = (len(array))
   print(a)
   for j in range(101):
    print [array[j]
     j += 1
    print [array[j]
  
#print(len(array))
#print(array)  
 
 

  #back = browser.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[4]/a').click()

  
      
  



