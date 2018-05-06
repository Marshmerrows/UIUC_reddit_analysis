from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup as bs

if __name__ == "__main__":
    driver = webdriver.Firefox()
    driver.get("https://www.reddit.com/r/UIUC/")

    soup = bs(driver.page_source, 'html.parser')
    for link in soup.find_all('a'):  # find all links on the current webpage, in order to filter
        href = str(link.get('href'))
        href_parts = href.split('/')
        if len(href_parts) > 5 and href_parts[5] == 'comments':  # this link follows a post to its comment section
            driver.get(href)
            try:
                title = driver.find_element_by_class_name('content').get_attribute('innerHTML')
                print title
            except NoSuchElementException:
                print "RIP no title"
    driver.quit()
