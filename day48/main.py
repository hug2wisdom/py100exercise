from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

chrome_driver_path = "E:\chromedriver_win32\chromedriver.exe"
chrome_service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=chrome_service)
driver.get(url="https://www.python.org/")
# time.sleep(10)
# input_item = driver.find_element(by=By.NAME, value="q")
# print(input_item.get_property("placeholder"))
activities = driver.find_elements(by=By.XPATH, value='//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li')
# activity_time = activities[0].find_element(by=By.TAG_NAME, value="time")
# print(activity_time.text)

activities_list = [{"activity_time": activity.find_element(by=By.TAG_NAME, value="time").text,
                    "activity_content": activity.find_element(by=By.TAG_NAME, value="a").text}
                   for activity in activities]

activities_dict = {str(i): activities_list[i] for i in range(0, len(activities_list))}
print(activities_dict)

driver.quit()
