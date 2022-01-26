from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


def UserData():
    global username
    username = input("Enter your Username: ")
    print(username)
    global password
    password = input("Enter your Password: ")
    print(password)
    global url
    url = "http://instagram.com"
    global profileurl
    profileurl = url + "/" + username + "/"


def LoginAct():
    # Opens browser
    global driver
    driver = webdriver.Chrome()
    # link to open in browser
    driver.get(url)
    sleep(4)
    # inputs in login page
    driver.find_element_by_xpath(('//input[@name="username"]')).send_keys((username))
    driver.find_element_by_xpath(('//input[@name="password"]')).send_keys((password))
    driver.find_element_by_xpath('//button[@type="submit"]').click()
    sleep(3)
    # notification pop up!
    driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
    sleep(3)
    driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()


def SuggestionFollow():
    LoopCnt = input("Enter your LoopCnt: ")
    print(LoopCnt)
    FollowCnt = input("Enter your FollowCnt: ")
    print(FollowCnt)
    Stime = input("Sleep Time: ")
    for i in range((int(LoopCnt))):
        sleep(2)
        for i in range((int(FollowCnt))):
            driver.find_element_by_xpath('//button/div[text()="Follow"]').click()
            sleep(int(Stime))
        driver.refresh()


def SuggestionUnfollow():
    LoopCnt = input("Enter your LoopCnt: ")
    print(LoopCnt)
    FollowCnt = input("Enter your FollowCnt: ")
    print(FollowCnt)
    Stime = input("Sleep Time: ")
    for i in range((int(LoopCnt))):
        sleep(2)
        driver.get(profileurl)
        sleep(2)
        driver.find_element_by_partial_link_text("following").click()
        sleep(3)
        for i in range((int(FollowCnt))):
            driver.find_element_by_xpath('//button[text()="Following"]').click()
            sleep(2)
            driver.find_element_by_xpath('//button[text()="Unfollow"]').click()
            sleep(int(Stime))
        driver.refresh()


def FollowByRequest():
    LoopCnt = input("Enter your LoopCnt: ")
    print(LoopCnt)
    FollowCnt = input("Enter your FollowCnt: ")
    print(FollowCnt)
    Stime = input("Sleep Time: ")
    for i in range((int(LoopCnt))):
        sleep(2)
        driver.find_element_by_partial_link_text("following").click()
        sleep(2)
        for i in range((int(FollowCnt))):
            sleep(2)
            driver.find_element_by_xpath(
                '//body/div/div/div/div/ul/div/li/div/div/button[text()="Follow"]'
            ).click()
            sleep(int(Stime))
        driver.refresh()


def Search():
    global Search
    Choise = input("Enter (1) for Name or (2) for HashTag: ")
    Search = input("Enter Search Word: ")
    Choise = int(Choise)

    if Choise == 1:
        searchUrl = url + "/" + Search + "/"
        driver.get(searchUrl)
        sleep(3)
        FollowByRequest()

    else:
        searchUrl = url + "/explore/tags/" + Search + "/"
        driver.get(searchUrl)


def FollowedUserUnfollow():
    # get users to unfollow from file
    userurl = url + "/" + username + "/"
    for i in range((int(LoopCnt))):
        sleep(2)
        driver.get(userurl)
        sleep(2)
        driver.find_element_by_partial_link_text("following").click()
        sleep(3)
        for i in range((int(FollowCnt))):
            driver.find_element_by_xpath('//button[text()="Following"]').click()
            sleep(2)
            driver.find_element_by_xpath('//button[text()="Unfollow"]').click()
            sleep(int(Stime))
        driver.refresh()


# Inputs Username Pwd
UserData()
# open Browser Logs In
LoginAct()
ProfileName = driver.find_element_by_css_selector("a.FPmhX.notranslate.MBL3Z").text
print(ProfileName)
Menu = input(
    "Enter (1) for AutoRandomFollow or \
                    (2) for Follow Followers of specific account or \
                    (3) for AutoRandomUnFollow"
)
Menu = int(Menu)
# Follows All In Suggestions // Provide (LoopCnt,FollowCnt)
if Menu == 1:
    SuggestionFollow()
# Follow Followers of specific Account or Hashtag
if Menu == 2:
    Search()
# Unfollow people accessing from Logged in users Account Following
if Menu == 3:
    SuggestionUnfollow()
if Menu == 4:
    FollowedUserUnfollow()

# thandora_digital_marketing
