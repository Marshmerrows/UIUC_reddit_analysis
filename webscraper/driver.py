from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup

if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.get("https://www.reddit.com/r/UIUC/")

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    for link in soup.find_all('a'):  # find all links on the current webpage, in order to filter
        href = str(link.get('href'))
        href_parts = href.split('/')
        if len(href_parts) > 6 and href_parts[5] == 'comments':  # this link follows a post to its comment section
            driver.get(href)
            for button in driver.find_elements_by_tag_name('button'):
                if button.get_attribute('innerHTML') == 'back to Old Reddit.':
                    button.click()
                    break

            thread_soup = BeautifulSoup(driver.page_source, 'html.parser')
            post = thread_soup.find('div', id='siteTable')
            comments = thread_soup.find('div', class_='commentarea').find_all('div', class_='md')

            print post.find('p', class_='title').get_text()
            print '--------------------------------'

            print post.find('div', class_='usertext-body may-blank-within md-container ').get_text()

            for comment in comments:
                print comment.get_text()
                print '--------------------------------'

    driver.quit()
