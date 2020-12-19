from time import sleep
from selenium import webdriver

class Twitter():
    def get_followers(self, url):
        driver = webdriver.Chrome(
            executable_path='\\Users\\Acer\\Downloads\\manatel\\exercise4\\chromedriver')
        driver.get(url)
        sleep(3)
        followers_count = driver.find_element_by_partial_link_text(
            'Followers').text
        return followers_count.split()[0]

def main():
    url = input("Enter the complete url of the twitter user: ")
    twitter = Twitter()
    followers_count = twitter.get_followers(url)
    print(f"The user has {followers_count} followers")


if __name__ == '__main__':
    main()
