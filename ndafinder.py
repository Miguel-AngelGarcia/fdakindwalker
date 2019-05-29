# steps
# go to website
# grab application number from CSV file, search for nda/anda/bla
# go to original approval and grab link for original apporval
# go back and grab latest available label or letter release, maybe both?
# print links to 1st and last into a CSV file to manually look up info
# repeat




# Function/Class that writes to file???
def write_function(app_num, first_link, second_link, third_link):
    filename = "drug_label_search.csv"
    f = open(filename, "w")

    headers = "ApplicationNumber, First_link, Latest_link, Latest_Other_link\n"
    f.write(headers)

    f.write(str(app_num) + ",")
    f.write(str(first_link) + ",")
    f.write(str(second_link) + ",")
    f.write(str(third_link) + " , " + '\n')


# probably need to have a class that searches the webpage to avoid writing the same code
def first_finder(app_number):
    driver.get("https://www.accessdata.fda.gov/scripts/cder/daf/")
    driver.find_element_by_name("searchterm").send_keys(app_number)
    time.sleep(3)
    driver.find_element_by_name("search").send_keys(Keys.ENTER)
    time.sleep(5)

    # this part gets 1st label and latest label from current drug url
    driver.find_element_by_partial_link_text("Approval Date(s) and History, Letters, Labels").click()
    try:
        driver.find_element_by_tag_name("Review (PDF)").click()
        #link = driver.current_url()
        #time.sleep(15)
        #return link
    except NoSuchElementException:
        result = 0
        time.sleep(8)
        return result
        pass
    # got an error on web python. maybe try out on real IDE


#### END OF IT


def second_finder(app_number):
    driver.get("https://www.accessdata.fda.gov/scripts/cder/daf/")
    driver.find_element_by_name("searchterm").send_keys(app_number)
    time.sleep(3)
    driver.find_element_by_name("search").send_keys(Keys.ENTER)
    time.sleep(5)

    # this part gets 1st label and latest label from current drug url
    driver.find_element_by_partial_link_text("Approval Date(s) and History, Letters, Labels").click()
    try:
        driver.find_element_by_partial_link_text("Label").click()
        latest_link = driver.current_url()
        time.sleep(15)
        return latest_link
    except NoSuchElementException:
        result = 0
        time.sleep(8)
        return result
        pass
    # got an error on web python. maybe try out on real IDE


#### END OF IT


def third_finder(app_number):
    driver.get("https://www.accessdata.fda.gov/scripts/cder/daf/")
    driver.find_element_by_name("searchterm").send_keys(app_number)
    time.sleep(3)
    driver.find_element_by_name("search").send_keys(Keys.ENTER)
    time.sleep(5)

    # this part gets 1st label and latest label from current drug url
    driver.find_element_by_partial_link_text("Approval Date(s) and History, Letters, Labels").click()
    try:
        driver.find_element_by_partial_link_text("Letter").click()
        latest_other_link = driver.current_url()
        time.sleep(15)
        return latest_other_link
    except NoSuchElementException:
        result = 0
        time.sleep(8)
        return result
        pass
    # got an error on web python. maybe try out on real IDE


#### END OF IT

from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import csv
from itertools import islice

driver = webdriver.Chrome(r"C:\Users\garcia\PycharmProjects\FDAlooker\drivers\chromedriver.exe")

with open('application_numbers.csv', 'r') as first_csv:
    first_reader = csv.reader(first_csv)

    next(first_reader)

    for line in islice(first_reader, 8,9):
        app_num = line
        first_link = first_finder(app_num)
        second_link = second_finder(app_num)
        third_link = third_finder(app_num)

        write_function(app_num, first_link, second_link, third_link)

# end in quit() rightt?
driver.quit()
#write_function.close()
# f.close()
