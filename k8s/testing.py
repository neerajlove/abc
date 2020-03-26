import csv

from selenium import webdriver

#<input type="email" class="whsOnd zHQkBf" jsname="YPqjbf" autocomplete="username" spellcheck="false" tabindex="0" 
#aria-label="Email or phone" 
#name="identifier" value="" autocapitalize="none" id="identifierId" dir="ltr" data-initial-dir="ltr" data-initial-value="">
#<span class="RveJvd snByac">Next</span>
browser = webdriver.Firefox("/usr/local/bin/")
#browser = webdriver.Firefox()
#/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/span/span

#from selenium.webdriver.firefox.options import Options as FirefoxOptions
browser.get("https://gmail.com")
emailElem = browser.find_element_by_id('identifierId')
emailElem.send_keys("neerajjoshi120@gmail.com")
browser.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/span/span').click()
browser.implicitly_wait(2)
browser.find_element_by_name('password').send_keys("asdf u all9312!@#$")
#browser.find_element_by_name('Signin').click()


#browser.find_element_by_class_name("quantumWizTextinputPapertextareaInput exportTextarea" )
#filename = "/Users/neeraj.joshi/Downloads/test.csv"
#print(filename)
#with open(filename, 'r') as f:
#kill = csv.reader(f, delimiter=",") 
#array = [ ]
#new = [ ]
 #for line in kill:
  # array.append(line)
   #for input in line:
    # new.append(input)  
#print(new[3])
         
    

  
      
  



