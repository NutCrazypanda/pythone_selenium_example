from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import os


#target_search = input("Enter code:")

# function to take care of downloading file
def enable_download_headless(browser,download_dir):
    browser.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
    params = {'cmd':'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': download_dir}}
    browser.execute("send_command", params)

# instantiate a chrome options object so you can set the size and headless preference
# some of these chrome options might be uncessary but I just used a boilerplate
# change the <path_to_download_default_directory> to whatever your default download folder is located
chrome_options = Options()
#chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=100x100")
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--verbose')
chrome_options.add_experimental_option("prefs", {
        "download.default_directory": "D:\GitHub\DLBit\Old_mp3",
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing_for_trusted_sources_enabled": False,
        "safebrowsing.enabled": False
})
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-software-rasterizer')

# initialize driver object and change the <path_to_chrome_driver> depending on your directory where your chromedriver should be
#driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="D:\GitHub\DLBit")
driver = webdriver.Chrome('chromedriver', chrome_options=chrome_options)
# change the <path_to_place_downloaded_file> to your directory where you would like to place the downloaded file
download_dir = "D:\GitHub\DLBit\Old_mp3"

# function to handle setting up headless download
enable_download_headless(driver, download_dir)

import time
import requests

driver.get("https://noom11.com/inter/")
lnks=driver.find_elements_by_tag_name("a")
for lnk in lnks:
   # get_attribute() to get all href
   checklnk = lnk.get_attribute('href')
   checklnk = checklnk.find("mp3")
   if checklnk != -1:
      target = lnk.get_attribute('href').replace("%20"," ")
      print(target)
      filename = target.split("/")
      filename = filename[6]
      r = requests.get(target, allow_redirects=True)
      open(filename,'wb').write(r.content)      



#print(imagelink)
print(driver.current_url)

#print(soup)
driver.quit()
