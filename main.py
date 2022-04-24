import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
import pandas as pd


#update path with the path to your geckodriver (lookup how to install)
PATH = r"C:\Users\cambe\Downloads\geckodriver.exe"
s = Service(PATH)
driver = webdriver.Firefox(service=s)

driver.get("https://www.ratemyprofessors.com/search/teachers?query=*&sid=1245")

#wait ten seconds for page to load, then close the cookie popup window
time.sleep(10)
button = driver.find_element(By.XPATH, '//button[@class="Buttons__Button-sc-19xdot-1 CCPAModal__StyledCloseButton-sc-10x9kq-2 gvGrz"]')
button.click()

#this clicks 'show more' 3 times currently, will need to update with more clicks once bugs fixed
for i in range(1, 3):
    driver.find_element(By.XPATH, '//button[@class="Buttons__Button-sc-19xdot-1 PaginationButton__StyledPaginationButton-txi1dr-1 gjQZal"]').click()
    # waits until elements are loaded
    time.sleep(3)

#get all professors, ratings, and subjects taught
professor = driver.find_elements(By.XPATH, '//div[@class="CardName__StyledCardName-sc-1gyrgim-0 cJdVEK"]')
rating = driver.find_elements(By.XPATH,'//div[@class = "CardNumRating__CardNumRatingNumber-sc-17t4b9u-2 kMhQxZ" or '
                                       '      @class = "CardNumRating__CardNumRatingNumber-sc-17t4b9u-2 fJKuZx" or'
                                       '      @class = "CardNumRating__CardNumRatingNumber-sc-17t4b9u-2 bUneqk" or'
                                       '      @class = "CardNumRating__CardNumRatingNumber-sc-17t4b9u-2 cDKJcc"]')
subject = driver.find_elements(By.XPATH, '//div[@class="CardSchool__Department-sc-19lmz2k-0 haUIRO"]')

#populate a list with each
professors_list = []
for p in range(len(professor)):
    professors_list.append(professor[p].text)

ratings_list =[]
for r in range(len(rating)):
    ratings_list.append(rating[r].text)

subject_list = []
for d in range(len(subject)):
    subject_list.append(subject[d].text)

#print for debugging purposes
print(professors_list)
print(ratings_list)
print(subject_list)
# just for separating purpose
print()
#printing the length to make sure they are all equal
print(len(professors_list))
print(len(ratings_list))
print(len(subject_list))


#TODO: once debugged, format into a CSV
df = pd.DataFrame([professors_list, ratings_list, subject_list])
df.to_csv('rmp.csv')
driver.close()
