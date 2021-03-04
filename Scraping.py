from typing import List

from selenium import webdriver
import csv
import time
import re
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from datetime import datetime


def writeObject(fileName, elements):
    with open(fileName, mode='a') as employee_file:
        data_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        data_writer.writerow(elements)


dataFolder = "/Users/jitkalra8/Desktop/Data_Jobs/"

driver = webdriver.Chrome("../drivers/chromedriver")

driver.set_page_load_timeout(10);

location_list = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]


driver.get("https://www.linkedin.com/jobs/search?keywords=Data%20Scientist&location=Alabama%20United%20States&trk=homepage-basic_jobs-search-bar_search-submit&redirect=false&position=10&pageNum=0");
#driver.find_element_by_name("keywords").send_keys("Data Scientist")
time.sleep(4)
cityCounter = 0

#locationelement = driver.find_element_by_name("location")
#locationelement.clear()
#time.sleep(4)
wait = WebDriverWait(driver, 10)
search_element = driver.find_element_by_class_name("filter-dropdown__button.filter-button.filter-button--guest-house.filter-button--more-filters")
search_element.click()
wait.until(ec.element_to_be_clickable((By.CLASS_NAME,"filter-collapse__option-button")));

locationFilter = driver.find_element_by_class_name("filter-collapse__option-button")
locationFilter.click()
wait.until(ec.element_to_be_clickable((By.CLASS_NAME,"more-filters__done.button-primary")));

filterElement = driver.find_element_by_class_name("filter-collapse__option-filter")
#labelFilter = filterElement.find_elements_by_class_name("")
cityElements = driver.find_elements_by_class_name("filter-list__list")[4].find_elements_by_class_name("filter-list__list-item")
cityElements[cityCounter].click()

driver.find_element_by_class_name("more-filters__done.button-primary").click()

for input_location in [ "Alabama" ]:
    #locationelement.send_keys(input_location)
    #locationelement.send_keys(Keys.ENTER)
    #time.sleep(4)
    #wait.until(ec.element_to_be_clickable((By.CLASS_NAME,"see-more-jobs")));
    #previousSize = len(driver.find_elements_by_class_name("result-card.job-result-card.result-card--with-hover-state"))
    #while True:
    #    if previousSize % 25 != 0:
    #        break;
    #    button = driver.find_elements_by_class_name("see-more-jobs")[0]
    #    button.click()
    #    wait.until(ec.element_to_be_clickable((By.CLASS_NAME, "see-more-jobs")));
    #    elements = driver.find_elements_by_class_name("result-card.job-result-card.result-card--with-hover-state")
    #    currentSize = len(elements)
    #    if currentSize % 100: print("currentSize -", currentSize)
    #    if previousSize == currentSize :
    #        break
    #    previousSize = currentSize
    count = 0
    #print( "Final Size ", currentSize, "for location", input_location, datetime.now() )
    fileName = dataFolder + input_location.replace(" ", "_").replace(",", "_") + ".csv"
    with open(fileName, mode='w') as csvfile:
        data_writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        data_writer.writerow(['JobType', 'JobCompany', 'JobLink', 'JobLocation', 'JobListTime', 'JobDescription'])
    for element in elements:
        JobType = element.find_element_by_css_selector("h3").text
        jobCompany = element.find_element_by_css_selector("li>div>h4").text
        jobLink = element.find_element_by_css_selector("li>a").get_attribute("href")
        element.find_element_by_css_selector("li>a").click()
        time.sleep(2)
        count = count+1
        if count%50 == 0:
            print( "pending for location ", currentSize-count, input_location, datetime.now() )
        description = driver.find_elements_by_class_name("description")[0].text
        JobText = description.replace("~", "-")
        location = element.find_element_by_css_selector("li>div>div>span").text
        timeListed = element.find_element_by_css_selector("li>div>div>time").get_attribute("datetime")
        writeObject( fileName, [ JobType , jobCompany , jobLink , location , timeListed, JobText ])
    locationelement = driver.find_element_by_name("location")
    locationelement.clear()
    time.sleep(2)

driver.quit()

