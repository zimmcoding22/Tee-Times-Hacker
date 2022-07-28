
# email = "mytalents13@gmail.com"
# password = "bethpagegolf"
# email = "beaulardner@aol.com"
# password = "Beau1991"
#pip3 install -r requirements.txt for installation

#BGCH is a web crawler that leverages selenium to retrieve tee times faster than other web traffic.
class BGCH():

    def __init__(self, num_players, course, start_time, end_time, email, password):
        self.proxy = "108.62.155.174:3128"  #taking random proxys from http://www.freeproxylists.net/
        self.firefox_capabilities = webdriver.DesiredCapabilities.FIREFOX
        self.firefox_capabilities['marionette'] = True
        self.firefox_capabilities['proxy'] = {"proxyType": "MANUAL", "httpProxy": self.proxy, "ftpProxy": self.proxy, "sslProxy": self.proxy}
        self.driver = webdriver.Firefox(capabilities=self.firefox_capabilities)
        self.num_players = num_players
        self.course = course
        self.start_time = start_time
        self.end_time = end_time
        self.email = email
        self.password = password
        #self.driver = webdriver.Firefox() #without proxy, comment above code out
        self.driver.get("https://foreupsoftware.com/index.php/booking/19765/2431#/teetimes")
        self.click_times()
        sleep(300) #you have 5 minutes to book the time manually
        self.driver.quit()

    def click_times(self):
        driver = self.driver
        residentButtonXpath = "//div[@id='page']//button[1]"
        loginButtonXpath = "//button[@class='btn btn-lg btn-primary login']"
        primaryLoginButtonXpath = "//button[@class='btn btn-primary login col-xs-12 col-md-2']"
        reserveTimeButtonXpath = "//a[@class='btn btn-primary']"
        reservationsButtonXpath = "//ul[@class='nav navbar-nav']//li[1]"
        monthScrollXpath = "//div[@class='datepicker-days']//th[@class='next'][contains(text(),'»')]"
        courseSelectXpath = "//option[contains(text(),'" + self.course + "')]"
        #reservationsButtonXpath = "//a[contains(text(),'teetimes')]"
        today = str(datetime.now())[:10].replace('-', '')
        today_month_number = today[4:6]
        today = datetime.strptime(today, "%Y%m%d")
        end_date = today + timedelta(days=7)
        tee_time_month_number = str(end_date)[5:7]
        day_number = str(int(str(end_date)[8:10]))
        dayActiveButtonXpath = "//td[@class='day'][contains(text(),'" + day_number + "')]"
        #dayActiveButtonXpath = "//td[@class='day'][contains(text(),'2')]"
        #times generated on page are random for the most part. This list accounts for all possible times.
        preferred_times = ["8:30am", "8:31am", "8:32am", "8:33am", "8:34am", "8:35am", "8:36am", "8:37am", "8:38am", "8:39am", "8:40am", "8:41am", "8:42am", "8:43am", "8:44am", "8:45am", "8:46am", 
                           "8:47am", "8:48am", "8:49am", "8:50am", "8:51am", "8:52am", "8:53am", "8:54am", "8:55am", "8:56am", "8:57am", "8:58am", "8:59am", "9:00am", "9:01am", "9:02am", 
                           "9:03am", "9:04am", "9:05am", "9:06am", "9:07am", "9:08am", "9:09am", "9:10am", "9:11am", "9:12am", "9:13am", "9:14am", "9:15am", "9:16am", "9:17am", "9:18am", 
                           "9:19am", "9:20am", "9:21am", "9:22am", "9:23am", "9:24am", "9:25am", "9:26am", "9:27am", "9:28am", "9:29am", "9:30am", "9:31am", "9:32am", "9:33am", "9:34am", "9:35am", "9:36am", "9:37am", "9:38am", "9:39am", "9:40am", "9:41am", "9:42am", "9:43am", "9:44am", "9:45am", "9:46am", 
                           "9:47am", "9:48am", "9:49am", "9:50am", "9:51am", "9:52am", "9:53am", "9:54am", "9:55am", "9:56am", "9:57am", "9:58am", "9:59am", "10:00am", "10:01am", "10:02am", 
                           "10:03am", "10:04am", "10:05am", "10:06am", "10:07am", "10:08am", "10:09am", "10:10am", "10:11am", "10:12am", "10:13am", "10:14am", "10:15am", "10:16am", "10:17am", "10:18am", 
                           "10:19am", "10:20am", "10:21am", "10:22am", "10:23am", "10:24am", "10:25am", "10:26am", "10:27am", "10:28am", "10:29am", "10:30am", "10:31am", "10:32am", "10:33am", "10:34am", 
                           "10:35am", "10:36am", "10:37am", "10:38am", "10:39am", "10:40am", "10:41am", "10:42am", "10:43am", "10:44am", "10:45am", "10:46am", "10:47am", "10:48am", "10:49am", "10:50am", 
                           "10:51am", "10:52am", "10:53am", "10:54am", "10:55am", "10:56am", "10:57am", "10:58am", "10:59am", "11:00am", "11:01am", "11:02am", "11:03am", "11:04am", "11:05am", "11:06am", 
                           "11:07am", "11:08am", "11:09am", "11:10am", "11:11am", "11:12am", "11:13am", "11:14am", "11:15am", "11:16am", "11:17am", "11:18am", "11:19am", "11:20am", "11:21am", "11:22am", 
                           "11:23am", "11:24am", "11:25am", "11:26am", "11:27am", "11:28am", "11:29am", "11:30am", "11:31am", "11:32am", "11:33am", "11:34am", "11:35am", "11:36am", "11:37am", "11:38am", 
                           "11:39am", "11:40am", "11:41am", "11:42am", "11:43am", "11:44am", "11:45am", "11:46am", "11:47am", "11:48am", "11:49am", "11:50am", "11:51am", "11:52am", "11:53am", "11:54am", 
                           "11:57am", "11:58am", "11:59am", "12:00pm", "12:01pm", "12:02pm", "12:03pm", "12:04pm", "12:05pm", "12:06pm", "12:07pm", "12:08pm", "12:09pm", "12:10pm", "12:11pm", "12:12pm", 
                           "12:13pm", "12:14pm", "12:15pm", "12:16pm", "12:17pm", "12:18pm", "12:19pm", "12:20pm", "12:21pm", "12:22pm", "12:23pm", "12:24pm", "12:25pm", "12:26pm", "12:27pm", "12:28pm", 
                           "12:29pm", "12:30pm", "12:31pm", "12:32pm", "12:33pm", "12:34pm", "12:35pm", "12:36pm", "12:37pm", "12:38pm", "12:39pm" , "12:40pm", "12:41pm", "12:42pm", "12:43pm", "12:44pm", 
                           "12:45pm", "12:46pm", "12:47pm", "12:48pm", "12:49pm", "12:50pm", "12:51pm", "12:52pm", "12:53pm", "12:54pm", "12:55pm", "12:56pm", "12:57pm", "12:58pm", "12:59pm", "1:00pm", 
                           "1:01pm", "1:02pm", "1:03pm", "1:04pm", "1:05pm", "1:06pm", "1:07pm", "1:08pm", "1:09pm", "1:10pm", "1:11pm", "1:12pm", "1:13pm", "1:14pm", "1:15pm", "1:16pm", "1:17pm", "1:18pm", 
                           "1:19pm", "1:20pm", "1:21pm", "1:22pm", "1:23pm", "1:24pm", "1:25pm", "1:26pm", "1:27pm", "1:28pm", "1:29pm", "1:30pm", "1:31pm", "1:32pm", "1:33pm", "1:34pm", "1:35pm", "1:36pm", 
                           "1:37pm", "1:38pm", "1:39pm", "1:40pm", "1:41pm", "1:42pm", "1:43pm", "1:44pm", "1:45pm", "1:46pm", "1:47pm", "1:48pm", "1:49pm", "1:50pm", "1:51pm", "1:52pm", "1:53pm", "1:54pm", 
                           "1:55pm", "1:56pm", "1:57pm", "1:58pm", "1:59pm", "2:00pm", "2:01pm", "2:02pm", "2:03pm", "2:04pm", "2:05pm", "2:06pm", "2:07pm", "2:08pm", "2:09pm", "2:10pm", "2:11pm", "2:12pm", "2:13pm", 
                           "2:14pm", "2:15pm", "2:16pm", "2:17pm", "2:18pm", "2:19pm", "2:20pm", "2:21pm", "2:22pm", "2:23pm", "2:24pm", "2:25pm", "2:26pm", "2:27pm", "2:28pm", "2:29pm", "2:30pm", "2:31pm", 
                           "2:32pm", "2:33pm", "2:34pm", "2:35pm", "2:36pm", "2:37pm", "2:38pm", "2:39pm", "2:40pm", "2:41pm", "2:42pm", "2:43pm", "2:44pm", "2:45pm", "2:46pm", "2:47pm", "2:48pm", "2:49pm", 
                           "2:50pm", "2:51pm", "2:52pm", "2:53pm", "2:54pm", "2:55pm", "2:56pm", "2:57pm", "2:58pm", "2:59pm", "3:00pm", "3:01pm", "3:02pm", "3:03pm", "3:04pm", "3:05pm", "3:06pm", "3:07pm", 
                           "3:08pm", "3:09pm", "3:10pm", "3:11pm", "3:12pm", "3:13pm", "3:14pm", "3:15pm", "3:16pm", "3:17pm", "3:18pm", "3:19pm", "3:20pm", "3:21pm", "3:22pm", "3:23pm", "3:24pm", "3:25pm", 
                           "3:26pm", "3:27pm", "3:28pm", "3:29pm", "3:30pm", "3:31pm", "3:32pm", "3:33pm", "3:34pm", "3:35pm", "3:36pm", "3:37pm", "3:38pm", "3:39pm", "3:40pm", "3:41pm", "3:42pm", "3:43pm", 
                           "3:44pm", "3:45pm", "3:46pm", "3:47pm", "3:48pm", "3:49pm", "3:50pm", "3:51pm", "3:52pm", "3:53pm", "3:54pm", "3:55pm", "3:56pm", "3:57pm", "3:58pm", "3:59pm", "4:00pm", "4:01pm", 
                           "4:02pm", "4:03pm", "4:04pm", "4:05pm", "4:06pm", "4:07pm", "4:08pm", "4:09pm", "4:10pm", "4:11pm", "4:12pm", "4:13pm", "4:14pm", "4:15pm", "4:16pm", "4:17pm", "4:18pm", "4:19pm", 
                           "4:20pm", "4:21pm", "4:22pm", "4:23pm", "4:24pm", "4:25pm", "4:26pm", "4:27pm", "4:28pm", "4:29pm", "4:30pm"]   

        #testAttemptXpath = "//h4[@class='start']"
        numberOfPlayersXpath = "//a[contains(text()," + self.num_players + ")]"
        emailFieldId = "login_email"
        passwordFieldId = "login_password"
        residentButtonElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(residentButtonXpath))
        residentButtonElement.click()
        loginButtonElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(loginButtonXpath))
        loginButtonElement.click()
        emailFieldElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(emailFieldId))
        passwordFieldElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(passwordFieldId))
        emailFieldElement.clear()
        emailFieldElement.send_keys(self.email)
        passwordFieldElement.clear()
        passwordFieldElement.send_keys(self.password)
        primaryLoginButtonElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(primaryLoginButtonXpath))
        primaryLoginButtonElement.click()
        sleep(3) #wait for javascript to load on screen.
        reservationsButtonElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(reservationsButtonXpath))
        reservationsButtonElement.click()
        #comment out the above two lines and uncomment the below two lines if there aren't any existing reservations
        #reserveTimeButtonElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(reserveTimeButtonXpath))
        #reserveTimeButtonElement.click()
        numberOfPlayersElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(numberOfPlayersXpath))
        numberOfPlayersElement.click()
        courseSelectElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(courseSelectXpath))
        courseSelectElement.click()
        #need to click reservations again to get back to calendar page
        # residentButtonElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(residentButtonXpath))
        # residentButtonElement.click()
        if (today_month_number != tee_time_month_number):
          monthScrollButtonElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(monthScrollXpath))
          monthScrollButtonElement.click()
        #click precisely at 7pm
        opening_time = "19:00:00"
        while (True):
            current_time = str(datetime.now())[11:19]
            current_seconds = str(datetime.now())[17:19]
            if (int(current_seconds) % 10 == 0):
                print("BGCH waiting. Current Time: ", current_time)
            if (current_time == opening_time):
                break
        print("clicking day active")
        dayActiveButtonElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(dayActiveButtonXpath))
        dayActiveButtonElement.click()
        def click_on_time(time): #thread worker
            try:
                attemptXpath = "//h4[contains(text(),'" + time + "')]"
                attemptElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(attemptXpath))
                attemptElement.click()
            except Exception as e:
                print(e)
        #spawn threads for each time so that we can click on all of them simultaneously
        start, end = 0, 0
        for i, time in enumerate(preferred_times):
          if (time == self.start_time):
            start = i
          if (time == self.end_time):
            end = i
        jobs = []
        for time in preferred_times[start:end]:
            t = Thread(target=click_on_time, args=(time,))
            t.start()
            jobs.append(t)
        print(jobs)
        for j in jobs:
            j.join()

num_players = sys.argv[1]
course = sys.argv[2]
start_time = sys.argv[3]
end_time = sys.argv[4]
email = sys.argv[5]
password = sys.argv[6]
print("showing args")
print(sys.argv)

try:
  for arg in sys.argv:
    print("arg: ", arg)
    if (arg == ''):
      error_message = "Make sure all values are filled in correctly. Inputs are displayed below. \n\n"
      inputs = ""
      for i, arg in enumerate(sys.argv):
        if (i == 0):
          continue
        inputs+=arg + '\n'
      error_message+=inputs
      easygui.msgbox(msg=error_message, title="Error Message", ok_button="ok")
      raise Exception(error_message)
  bgch = BGCH(num_players, course, start_time, end_time, email, password)
except Exception as e:
  print("error: ", e)
 
  
