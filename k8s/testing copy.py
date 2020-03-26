import csv
import math

from selenium import webdriver

browser = webdriver.Firefox()

browser.get("https://forms.gle/QdsBB7FjscS2KYnq6")



#names = browser.find_element_by_name('entry.2005620554')
#ar1 = names.send_keys("name") 
#phoneno = browser.find_element_by_name('entry.1045781291')
#ar2 = Phoneno.send_keys("4567")
#emailid = browser.find_element_by_name('entry.828990748')
#ar3 = emailid.send_keys("qwwe") 
#date = browser.find_element_by_name('entry.1166974658')
#ar4 = date.send_keys("date")
select = browser.find_element_by_xpath('/html/body/div/div[2]/form/div/div/div[3]/div[1]/div/div/span/span').click()

"""inputs = []
inputs.append(names)
inputs.append(phoneno)
inputs.append(emailid)
inputs.append(date)
"""

filename = "/Users/neeraj.joshi/Downloads/test.csv"
print(filename)
with open(filename, 'r') as f:
 kill = csv.reader(f, delimiter=",") 
 array = [ ]

 for line in kill:
   array.append(line)
   a = (len(array))
   
 for row in array:
       browser.get("https://forms.gle/QdsBB7FjscS2KYnq6")
       inputs = browser.find_elements_by_tag_name("input")
       print(inputs)
       if(len(row) != 0):
             index = 0 
             for i in inputs:
                 if(i.get_attribute("type") != "hidden"):
                         i.send_keys(row[index])
                         index += 1
             browser.find_element_by_xpath('/html/body/div/div[2]/form/div/div/div[3]/div[1]/div/div/span/span').click()
                        
browser.close()


"""
for i in range(100):
    names.send_keys(dd[i])
    phoneno.send_keys(dd[i+1])
    emailid.send_keys(dd[i+2]) 
    date.send_keys(dd[i+3])
    select = browser.find_element_by_xpath('/html/body/div/div[2]/form/div/div/div[3]/div[1]/div/div/span/span').click()
    back = browser.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[4]/a').click()


"""