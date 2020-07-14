import time

from selenium.webdriver import Chrome

chromeDriver = 'C:\\temp\\chromedriver.exe'

driver = Chrome(chromeDriver)

driver.get('https://auth.skt-id.co.kr/auth/authorize.do?service_type=14&scope=openid&response_type=id_token%20token&client_id=7f65f663-0435-4212-9076-3b81349ffb74&client_secret=eyJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiQTI1NktXIn0.l3p4mpHyRTYlY9XU5iImYURAhsWrvheTMWBtLOfNDWudhYkKWeT2-g.WsWegOMMyEBxFM2q.73DBLX32fnHiuvtZGKX_hlwXIHQUGqJ3OCgMXzvRU394LvJzeDHANaAiqOo4a3MtsezT-kyG1Mp2OrDSnmQuzpujCa1aM0Euzyq2WGFPrwA8NZC0nKFtyOBz4vFysuKkPF5TKXm5xPrxAHAaGznZoiN1Hz93nUvSNxA1.BwzziWoK9iUdpsa8te_jFA&client_type=WEB&redirect_uri=https%3A%2F%2Fmember.11st.co.kr%2Ftid%2Fcallback&state=8eea55b59d39419b7574daee39c4865e2bed11664f3e32b29e1b89ac5c9303edb20a1ad0&nonce=8eea55b59d39419b7574daee39c4865e2bed11664f3e32b29e1b89ac5c9303edb20a1ad0&chnl_q=login&frame_refer_host=https%3A%2F%2Flogin.11st.co.kr')

time.sleep(3)

input_login = driver.find_element_by_id("userId")
input_login.send_keys("asdfasdfasdf")

input_pw = driver.find_elements_by_id("password")
input_pw.send_keys("asdfasdfasdf")

btn = driver.find_element_by_class_name("btn-seceondary")

time.sleep(3)
btn.click()
time.sleep(3)

driver.quit()
