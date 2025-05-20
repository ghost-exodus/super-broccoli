from selenium import webdriver
from selenium.webdriver import ActionChains 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import csv
import time
stock=input("enter subject name   ")
# Setup
DRIVER_PATH = "C:\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe"
options = Options()
options.add_argument("start-maximized")

driver = webdriver.Chrome(service=Service(DRIVER_PATH), options=options)
actions = ActionChains(driver)
# Load search page
driver.get(f"https://www.business-standard.com/search?q={stock}")


for i in range(6):
   load_more_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'Loadmore_loadmorebtn')]/button"))
)
   actions.move_to_element(load_more_button).click().perform()

   time.sleep(1)  # wait 1 second between clicks

# Wait for outer container to load (so page is "ready")
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "listingstyle_cardlistlist__dfq57"))
   
)


   




# Scroll down to force JS to counter lazy loading
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(3)  # wait for JS to load results

# Now grab all smallcard-title headlines
headline_elements = driver.find_elements(By.XPATH, "//a[contains(@class, 'smallcard-title')]")





if not headline_elements:
    print("⚠️ No headlines found. The structure might have changed.")
data=[]
# Extract and print headlines
for element in headline_elements:
    title = element.text.strip()
    link = element.get_attribute("href")
    if stock  in title.lower(): 
     data.append(title)
    
        
    
driver.quit()


with open('datascraped.csv', 'w', newline='',encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows([[title] for title in data])

