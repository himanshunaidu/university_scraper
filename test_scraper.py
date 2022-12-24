import time
from selenium import webdriver
from bs4 import BeautifulSoup, NavigableString, Tag
import pandas as pd

class TestScraper:
    def __init__(self, faculty_path: str):
        self.driver = webdriver.Chrome("D:\Anaconda3\chromedriver") #Could use requests and beautifulsoup4 in tandem like in scholar_scraper instead of selenium
        self.driver.get("https://cse.engin.umich.edu/people/faculty/")
        self.content: str = self.driver.page_source
        self.soup = BeautifulSoup(self.content)
    
    #Ideally, this method should be outsourced because of being University Specific
    def findFacultyUMichExample(soup: BeautifulSoup):
        #Find the entire people list
        people_lists: Tag | NavigableString | None = soup.find("div", attrs = {"class": "people_lists"})
        time.sleep(5)
        if people_lists is None: return None

        faculty: list = []
        # for i in range(26):
        letter_id: str = "people_letter_"+str(0)
        people_letter_list: Tag | NavigableString | None = people_lists.find("div", id = letter_id)

        # if people_letter_list is None: continue
        for faculty in people_letter_list.find_all("div", attrs = "eecs_person_wrapper"):
            faculty_copy: Tag | NavigableString | None = faculty.find("div", attrs = {"class": "eecs_person_copy"})
            faculty_name_list: list = faculty_copy.find("h4").text.split(",")
            faculty_name_list.reverse()
            faculty_name: str = " ".join(faculty_name_list)
            faculty.append(faculty_name)
        
        return faculty
    


        

FACULTY_PATH: str = "https://cse.engin.umich.edu/people/faculty/"

scraper: TestScraper = TestScraper(FACULTY_PATH)
TestScraper.findFacultyUMichExample(scraper.soup)