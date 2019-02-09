
from selenium import webdriver
import sys

#requires https://github.com/mozilla/geckodriver/releases to be in the path to function
#tested on x64 Ubuntu 18.04 and mozilla firefox 63
#Author: nuk3s

banner = "_________          _______    _______  _______  ______   ______   _        _______  _______\r\n"
banner +="\__   __/|\     /|(  ____ \  (       )(  ____ \(  __  \ (  __  \ ( \      (  ____ \(  ____ )\r\n"
banner +="   ) (   | )   ( || (    \/  | () () || (    \/| (  \  )| (  \  )| (      | (    \/| (    )|\r\n"
banner +="   | |   | (___) || (__      | || || || (__    | |   ) || |   ) || |      | (__    | (____)|\r\n"
banner +="   | |   |  ___  ||  __)     | |(_)| ||  __)   | |   | || |   | || |      |  __)   |     __)\r\n"
banner +="   | |   | (   ) || (        | |   | || (      | |   ) || |   ) || |      | (      | (\ (   \r\n"
banner +="   | |   | )   ( || (____/\  | )   ( || (____/\| (__/  )| (__/  )| (____/\| (____/\| ) \ \__\r\n"
banner +="   )_(   |/     \|(_______/  |/     \|(_______/(______/ (______/ (_______/(_______/|/   \__/\r\n"
banner +="\r\n"
banner += "usage python meddler.py <pigeon invite code>"

print banner

if len(sys.argv) < 2:
    print "Need your invite code, see usage ^"
    sys.exit()

invite_code=str(sys.argv[1])



driver = webdriver.Firefox()
req='https://pigeonhole.at/' + invite_code
driver.get(req)
driver.delete_all_cookies()
questions  = ''
vote_buttons = []

                                                                                           
#TODO: Prompt user for which poll if more than one
driver.find_element_by_class_name("sessionlist-item-button-wrapper  ").click() # automatically clicks the first poll link

#Finds all question objects
question_containers = driver.find_elements_by_xpath("//div[@class='question-container-item']")


#Generates list of questions and the corrisponding voting buttons
for container in question_containers:
    questions+= container.find_element_by_xpath(".//div[@class='question-content allow-user-select']").get_attribute('innerHTML')
    vote_buttons += container.find_elements_by_xpath(".//div[@class='icon icon-qna-vote-outline question-vote-triangle']")


questions = questions[2:len(questions)-2]
questions = (questions.split('\n \n '))
i=1
for q in questions:
    print "[" + str(i) + "] " + q
    i+=1
option = input("Which vote would you like to upvote? ")
num_times = input("How many times? ")
vote_buttons[option-1].click()


for i in range (1,num_times):
    driver.close()
    driver = webdriver.Firefox()
    driver.get(req)
    driver.delete_all_cookies()
    driver.find_element_by_class_name("sessionlist-item-button-wrapper  ").click() #^^^ all of this is just setup to have a clean start each time

    question_containers = driver.find_elements_by_xpath("//div[@class='question-container-item']") # find all question containers
    for container in question_containers:
        if questions[option-1] in container.find_element_by_xpath(".//div[@class='question-content allow-user-select']").get_attribute('innerHTML'): # if container has out question text
            container.find_element_by_xpath(".//div[@class='icon icon-qna-vote-outline question-vote-triangle']").click() # click it

print "[*] Complete!"    
driver.close()    
