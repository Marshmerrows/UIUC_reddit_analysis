from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
import sys

#SAVE_PATH = "../res_all/res2/"
#START_URL = "https://www.reddit.com/r/UIUC/new/"

SAVE_PATH = sys.argv[1]
START_URL = sys.argv[2]
postnum = 0

driver = webdriver.Firefox()
driver.get(START_URL)

while True:
    for button in driver.find_elements_by_tag_name('button'): # this finds the "old reddit" button
        if button.get_attribute('innerHTML') == 'back to Old Reddit.':
            button.click()
            break
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    # find the next button real quick :D
    next_href = None
    next_span = soup.find('span', class_='next-button')
    if next_span:
        next_span = next_span.find_all(href=True)
        for tag in next_span:
            if tag['rel'] == 'nofollow next':
                print ">:("
                next_href = tag['href']

    # find the main part of the page (get rid of annoying banner posts every time)
    print next_href
    site_table = soup.find('div', id='siteTable')
    if site_table:
        soup = site_table
        print "siteTable found"
    else:
        print "siteTable not found"

    for link in soup.find_all('a'):  # find all links on the current webpage, in order to filter
        href = str(link.get('href'))
        href_parts = href.split('/')
        if len(href_parts) > 6 and href_parts[5] == 'comments':  # this link follows a post to its comment section
            driver.get(href)

            f = open(SAVE_PATH + "file{}".format(postnum), "w+")
            print "writing to {}".format(f.name)
            postnum += 1

            for button in driver.find_elements_by_tag_name('button'): # this finds the "old reddit" button
                if button.get_attribute('innerHTML') == 'back to Old Reddit.':
                    button.click()
                    break

            try:
                for morecomments in driver.find_elements_by_class_name('morecomments'):
                    try:
                        anchor = morecomments.find_element_by_tag_name('a')
                        anchor.click()
                    except:
                        print "Error in Morecomments??"
            except:
                print "Error in Morecomments??"

            thread_soup = BeautifulSoup(driver.page_source, 'html.parser')

            post = thread_soup.find('div', id='siteTable')
            if post:
                title = post.find('p', class_='title')
                if title:
                    title = post.find('a')
                    if title:
                        title_text = title.get_text()
                        print title_text
                        f.write(title_text.encode('utf-8') + '\n')
                    else:
                        f.write('\n')
                else:
                    f.write('\n')

                f.write('----\n')

                post = post.find('div', class_='usertext-body may-blank-within md-container ')
                if post:
                    f.write(post.get_text().encode('utf-8') + '\n')
                else:
                    f.write('\n')
            else:
                f.write('\n')
                f.write('----\n')
                f.write('\n')

            f.write('----\n')

            comments = thread_soup.find('div', class_='commentarea')
            if comments:
                comments = comments.find_all('div', class_='md')
                if comments:
                    for comment in comments:
                        f.write(comment.get_text().encode('utf-8') + '\n')
                        f.write('----\n')
                else:
                    f.write('\n')
            else:
                f.write('\n')

            f.close()
    if next_href:
        driver.get(next_href)
    else:
        break

#driver.quit()
