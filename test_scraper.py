import time
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

class TestScraper:
    def __init__(self, faculty_path):
        self.driver = webdriver.Chrome("D:\Anaconda3\chromedriver")
        self.driver.get("https://cse.engin.umich.edu/people/faculty/")
        self.content = self.driver.page_source
        self.soup = BeautifulSoup(self.content)
    
    def findFaculty(self):
        #Find the entire people list
        people_lists = self.soup.find('div', id = "people_lists")
        time.sleep(5)

        faculty = []

        for i in range(26):
            letter_id = "people_letter_"+str(i)

        

FACULTY_PATH = "https://cse.engin.umich.edu/people/faculty/"

scraper = TestScraper(FACULTY_PATH)