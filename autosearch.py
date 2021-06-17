from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import os


target_search = input("Enter code:")

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
        "download.default_directory": "D:\GitHub\DLBit",
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
download_dir = "D:\GitHub\DLBit"

# function to handle setting up headless download
enable_download_headless(driver, download_dir)

# get request to target the site selenium is active on
#driver.get("https://www.transfernow.net/dltransfer/?utm_source=20210610HJMLeciE&utm_medium=MJKzpnkO&utm_content=en")
#imagelink = driver.find_element_by_id("btn-ddl-action").click()
#imagelink = driver.find_element_by_xpath("//button[@class='btn-ddl-action']").click()

# initialize an object to the location on the html page and click on it to download
#search_input = driver.find_element_by_css_selector('#main-col > div > div > div:nth-child(8) > p:nth-child(1) > a > img')
#search_input.click()

#driver.get("http://you_target_web")
#text_input = driver.find_element_by_id("s")
#imagelink = driver.find_element_by_xpath("//img[@src='/main/jj.jpg']").click()
#imagelink = driver.find_element_by_xpath("//a[@name='#21']")
#imagelink = imagelink.get_attribute('innerHTML')
#print(imagelink)
#filestart = imagelink.find("file=")
#imagelink = imagelink[36:98]

driver.get("http://www.google.com")
text_input = driver.find_element_by_name("q")
text_input.send_keys(target_search + Keys.RETURN)



#print(imagelink)
print(driver.current_url)

#print(soup)
#driver.quit()
