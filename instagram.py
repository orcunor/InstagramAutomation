from instagramUserInfo import username, password
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
class Instagram:
    def __init__(self, username, password):
        #self.browserProfile = webdriver.ChromeOptions()
        #self.browserProfile.add_experimental_option("prefs",{"intl.accept_languages":"en,en_US"})
        #self.browser = webdriver.Chrome("chromedriver.exe", chrome_options= self.browserProfile)
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password

    def signIn(self):
        self.browser.get("https://www.instagram.com/")
        time.sleep(3)
        self.browser.maximize_window()
        usernameInput = self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input")
        passwordInput = self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input")

        usernameInput.send_keys(self.username)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(2)

    def getFollowers(self):

        self.browser.get(f"https://www.instagram.com/{self.username}")
        time.sleep(2)
        followersLink = self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a")
        followersLink.click()
        time.sleep(2)


        dialog = self.browser.find_element_by_css_selector("div[role=dialog] ul") 
        followerCount = len(dialog.find_elements_by_css_selector("li"))

        print(f"first count: {followerCount}")

        action = webdriver.ActionChains(self.browser)

        while True:
            dialog.click()
            action.key_down(Keys.SPACE).key_down(Keys.SPACE).perform()
            time.sleep(2)

            newCount = len(dialog.find_elements_by_css_selector("li"))

            if followerCount != newCount:
                followerCount = newCount
                print(f"second count: {newCount}")
                time.sleep(3)
            else:
                break
                


        followers = dialog.find_elements_by_css_selector("li")

        followerList = []
        for user in followers:
            link = user.find_element_by_css_selector("a").get_attribute("href")
            followerList.append(link)

        with open ("followers.txt","w",encoding="UTF-8") as file:
            for item in followerList:
                file.write(item + "\n")
    
    def followUser(self, username):
        self.browser.get("https://www.instagram.com/"+ username)
        time.sleep(2)
        
        followButon = self.browser.find_element_by_tag_name("button")
        if followButon.text != "Mesaj Gönder":
            followButon.click()
            time.sleep(2)
            print("takip edildi.")
        else:
            print("zaten takiptesin")

    def unfollowUser(self, username):
        self.browser.get("https://instagram.com/" + username)
        time.sleep(2)

        followButon = self.browser.find_element_by_tag_name("button")
        if followButon.text == "Takip Et":
            followButon.click()
            time.sleep(2)
            
            
        else:
            self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/div[1]/div[2]/span/span[1]/button").click()
            self.browser.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[1]").click()
            print("unfladım")

        
            
                

        
            

        
            



instagram = Instagram(username, password)
instagram.signIn()
#instagram.getFollowers()
#instagram.followUser("denizorr")
#instagram.unfollowUser("denizorr")

# list = ["iss","kod_evreni","greenpeace"]

# for user in list:
#     instagram.followUser(user)
#     time.sleep(3)
