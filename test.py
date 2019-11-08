import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver= webdriver.Chrome('D:\Chrome\chromedriver.exe')  # Optional argument, if not specified will search path.
driver.get('https://thedigitalcraft.com');
#driver.save_screenshot("home-page.png")
#################################################################################################

element = driver.find_element_by_id("live-events")
element.click()

driver.save_screenshot("live-events.png")
time.sleep(2)
element=driver.find_element_by_id("first_name")
element.send_keys("Tushar")

element=driver.find_element_by_id("last_name")
element.send_keys("Naik")

element=driver.find_element_by_id("email")

element.send_keys("some@place.com")

element=driver.find_element_by_id("question")
element.send_keys("I have a great question")
driver.save_screenshot("live-events-info.png")
time.sleep(2)
element=driver.find_element_by_xpath('//*[@id="live-event-questions"]/button')
element.send_keys(Keys.RETURN)
################################################################################################

element=driver.find_element_by_id("private-training")
element.click()
driver.save_screenshot("private-training.png")
time.sleep(2)
#########################################################################################
element=driver.find_element_by_id("home")
element.click()
########################################################################################
element=driver.find_element_by_id('course-videos')
element.click()
driver.save_screenshot("courses-videos.png")
time.sleep(2)
driver.get('https://www.youtube.com/playlist?list=PLAkMqlQoeMej0QeA-8QjJCYZ0Q5x1gnJF')
driver.get('https://thedigitalcraft.com');

########################################################################################
element=driver.find_element_by_id("open-source")
element.click()
driver.save_screenshot("open-source.png")
time.sleep(2)
driver.get('https://github.com/thedigicraft/Atom.CMS3')
driver.get('https://thedigitalcraft.com');
#######################################################################################
element=driver.find_element_by_id("youtube-channel")
element.click()
driver.save_screenshot("youtube-channel.png")
time.sleep(2)
driver.get('https://thedigitalcraft.com');
# ######################################################################################
element=driver.find_element_by_id("facebook-page")
element.click()
driver.save_screenshot("facebook-page.png")
time.sleep(2)
driver.get('https://thedigitalcraft.com');
##################################################################################
element=driver.find_element_by_id("twitter-page")
element.click()
driver.save_screenshot("twitter-page.png")
time.sleep(2)
driver.get('https://thedigitalcraft.com');
################################################################################
time.sleep(5)
driver.quit()