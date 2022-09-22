import time

import pandas as pd
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By


driver = webdriver.safari.webdriver.WebDriver()

driver.get("https://www.ratemyprofessors.com/search/teachers?query=*&sid=1078")

# wait ten seconds for page to load, then close the cookie popup window
time.sleep(5)
button = driver.find_element(By.XPATH, '//button[@class="Buttons__Button-sc-19xdot-1 CCPAModal__StyledCloseButton-sc-10x9kq-2 gvGrz"]')
button.click()

# this clicks 'show more' 3 times currently, will need to update with more clicks once bugs fixed

'''
for i in range(1, 254):
    driver.find_element(By.XPATH, '//button[@class="Buttons__Button-sc-19xdot-1 PaginationButton__StyledPaginationButton-txi1dr-1 gjQZal"]').click()
    # waits until elements are loaded
    time.sleep(1)
    '''

try:
    while True:
        driver.find_element(By.XPATH, '//button[@class="Buttons__Button-sc-19xdot-1 PaginationButton__StyledPaginationButton-txi1dr-1 gjQZal"]').click()
        # waits until elements are loaded
        time.sleep(1)
except:
    print("end")
    pass

# get all professors, ratings, and subjects taught
professor = driver.find_elements(By.XPATH, '//div[@class="CardName__StyledCardName-sc-1gyrgim-0 cJdVEK"]')
rating = driver.find_elements(By.XPATH,'//div[@class = "CardNumRating__CardNumRatingNumber-sc-17t4b9u-2 kMhQxZ" or '
                                       '      @class = "CardNumRating__CardNumRatingNumber-sc-17t4b9u-2 fJKuZx" or'
                                       '      @class = "CardNumRating__CardNumRatingNumber-sc-17t4b9u-2 bUneqk" or'
                                       '      @class = "CardNumRating__CardNumRatingNumber-sc-17t4b9u-2 cDKJcc"]')

subject = driver.find_elements(By.XPATH, '//div[@class="CardSchool__Department-sc-19lmz2k-0 haUIRO"]')
difficulty = driver.find_elements(By.XPATH, '//div[@class="CardFeedback__CardFeedbackNumber-lq6nix-2 hroXqf"]')
link = driver.find_elements(By.XPATH, '//a[@class="TeacherCard__StyledTeacherCard-syjs0d-0 dLJIlx"]')


# populate a list with each

professors_list = []
for p in range(len(professor)):
    professors_list.append(professor[p].text)

ratings_list =[]
for r in range(len(rating)):
    ratings_list.append(rating[r].text)

subject_list = []
for d in range(len(subject)):
    subject_list.append(subject[d].text)

difficulty_list = []
for i in range(1, len(difficulty), 2):
    difficulty_list.append(difficulty[i].text)

link_list = []
for x in range(len(link)):
    link_list.append(link[x].get_attribute("href"))

'''
#print for debugging purposes
print(professors_list)
print(ratings_list)
print(subject_list)
# just for separating purpose
print()
'''
#printing the length to make sure they are all equal
print(len(professors_list))
print(len(ratings_list))
print(len(subject_list))
print(len(difficulty_list))
print(len(link_list))

#to csv
df = pd.DataFrame({'professors_list':professors_list, 'ratings_list':ratings_list, 'subjects_list': subject_list, 'difficulty_list': difficulty_list, 'link_list': link_list})
df.to_csv('ucscrmp.csv', index=False)
print(df)


driver.close()