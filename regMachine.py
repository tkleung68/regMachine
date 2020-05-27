from selenium import webdriver
import time
from datetime import datetime, timedelta

chromedriver = "/Users/user/Desktop/regMachine/chromedriver.exe"
driver = webdriver.Chrome(chromedriver)
acc = ""
pw = ""
CRNs = [10121, 10222]
TIMETICKET = datetime(year=2020,month=5,day=27,hour=15,minute=00,second=00)

def login():
    try:
        driver.get("https://banweb.cityu.edu.hk/pls/PROD/twgkpswd_cityu.P_WWWLogin")
        searchEid = driver.find_element_by_xpath("//input[@type='text']")
        searchEid.send_keys(acc)

        searchPassword = driver.find_element_by_xpath("//input[@type='password']")
        searchPassword.send_keys(pw)

        searchLogin = driver.find_element_by_xpath("//input[@type='submit']")
        searchLogin.click()
        
        if(driver.title == 'Personal Information'):
            return True
    except Exception as e:
        print(e)

    return False


    
    #driver.find_element_by_id("username").send_keys("USERNAME")
    #obj = driver.find_element(By.NAME, "IamBanana")


def locateToRegistrationPage():
    #/html/body/div[3]/span/map/table/tbody/tr[1]/td/table/tbody/tr/td[5]/a
    driver.find_element_by_link_text("Course Registration").click()
    driver.find_element_by_link_text("Main Menu for Web Add/Drop").click()
    driver.find_element_by_link_text("Add or Drop Classes").click()
    driver.find_element_by_xpath("/html/body/div[5]/form/input").click()

def addCourse():
    for i in range(0, len(CRNs)):
        field = driver.find_element_by_id("crn_id" + str(i+1))
        field.send_keys(CRNs[i])
    buttom = driver.find_element_by_xpath("//input[@type='submit'][@name='REG_BTN'][@value='Submit Changes']")
    buttom.click()

def wait():
    correctPeriod = False
    while not correctPeriod:
        now = datetime.now()
        if((now+ timedelta(seconds=30)) >=TIMETICKET):
            print("enter!")
            driver.refresh()
            if("ADD COURSE:" in driver.page_source):
                correctPeriod = True
        else:
            print("waiting")
            if(now.second == 30 or now.second == 50):
                driver.refresh()
                print("refreshed")

if(login()):
    print("login successfully")
    locateToRegistrationPage()
    wait()
    addCourse()
    

