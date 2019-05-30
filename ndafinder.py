# steps
# go to website
# grab application number from CSV file, search for nda/anda/bla
# go to original approval and grab link for original apporval
# go back and grab latest available label or letter release, maybe both?
# print links to 1st and last into a CSV file to manually look up info
# repeat




# Function/Class that writes to file???


# probably need to have a class that searches the webpage to avoid writing the same code
def first_finder(app_number):
    driver.get("https://www.accessdata.fda.gov/scripts/cder/daf/")
    time.sleep(2)
    driver.find_element_by_name("searchterm").send_keys(app_number)
    time.sleep(3)
    driver.find_element_by_name("search").send_keys(Keys.ENTER)
    time.sleep(4)

    # this part gets 1st label and latest label from current drug url
    try:
        driver.find_element_by_partial_link_text("Approval Date(s) and History, Letters, Labels").click()
        try:
            link = driver.find_element(By.XPATH, "//tbody/tr/td[6]/span/a").get_attribute("href")
            time.sleep(5)
            return link
        except NoSuchElementException:
            result = 0
            time.sleep(5)
            return result
        # got an error on web python. maybe try out on real IDE
    except NoSuchElementException:
        result = 0
        return result


#### END OF IT


def second_finder(app_number):
    try:
        latest_link = driver.find_element(By.XPATH, "//tbody/tr[1]/td[4]/a").get_attribute("href")
        time.sleep(5)
        return latest_link
    except NoSuchElementException:
        result = 0
        time.sleep(5)
        return result
    # got an error on web python. maybe try out on real IDE


#### END OF IT


def third_finder(app_number):
    try:
        latest_other_link = driver.find_element(By.XPATH, "//tbody/tr[2]/td[4]/a").get_attribute("href")
        time.sleep(5)
        return latest_other_link
    except NoSuchElementException:
        result = 0
        time.sleep(5)
        return result
    # got an error on web python. maybe try out on real IDE


#### END OF IT

from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import csv
from itertools import islice

driver = webdriver.Chrome(r"C:\Users\garcia\PycharmProjects\FDAlooker\drivers\chromedriver.exe")

start_index = 105 #beginning index
stop_index = 155 # ending index

with open('application_numbers.csv', 'r') as first_csv:
    first_reader = csv.reader(first_csv)

    next(first_reader)

    filename = "drug_label_search.csv"
    f = open(filename, "w")
    headers = "ApplicationNumber, First_link, Latest_link, Latest_Other_link\n"
    f.write(headers)

    for line in islice(first_reader, start_index, stop_index):
        app_num = line
        first_link = first_finder(app_num)
        second_link = second_finder(app_num)
        third_link = third_finder(app_num)
        time.sleep(30)

        # write the info to CSV file

        f.write(str(app_num) + ",")
        f.write(str(first_link) + ",")
        f.write(str(second_link) + ",")
        f.write(str(third_link) + ",")
        f.write("\n")
    f.close()

# end in quit() rightt?
driver.quit()
#write_function.close()
# f.close()
