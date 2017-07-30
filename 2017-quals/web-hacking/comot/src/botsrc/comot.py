from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.action_chains import ActionChains
import sys

if(len(sys.argv) < 2):
    print('URL INPUT!!!')
    exit()

url = sys.argv[1]
caps = DesiredCapabilities.PHANTOMJS
caps["phantomjs.page.settings.userAgent"] = "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/603.1.23 (KHTML, like Gecko) Version/10.0 Mobile/14E5239e Safari/602.1"

driver = webdriver.PhantomJS(desired_capabilities=caps)
driver.get('http://[DOMAIN]:PORT')

driver.add_cookie({
  'domain': '.DOMAIN',
  'name': 'session',
  'value': 'b5470b800ef87a7018594959ccf4b339',
  'httponly': 'true',
  'path': '/',
  'expires': 'Session'
})

driver.get('http://[DOMAIN]:[PORT]/notes/'+url)

name = driver.find_element_by_css_selector("html")
ActionChains(driver).move_to_element(name).perform()
