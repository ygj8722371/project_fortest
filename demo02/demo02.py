# print("demo02")

# [1,1/2/2/3]
# def qn(n):
#     sum = 0
#     a = 1
#     for i in range(1,n+1):
#         b = i
#         sum+=a/b
#         a,b=b,b+a
#     return sum
# print(qn(3))


from selenium import webdriver





chromeOptions={}
chromeOptions.add_argument('user-agent="Mozilla/5.0 (iPod; U; CPU iPhone OS 2_1 \
                            like Mac OS X; ja-jp) AppleWebKit/525.18.1 (KHTML, like \
                            Gecko) Version/3.1.1 Mobile/5F137 Safari/525.20"')

driver = webdriver.Chrome(chrome_options=chromeOptions)

driver.get('https://www.baidu.com') # 查看IP是否切换。
print(driver.page_source)

# 获取请求头信息
agent = driver.execute_script("return navigator.userAgent")
print(agent)  # 查看请求头是否更改。

# cookies = driver.get_cookies()
# cookie_list = {cookie["name"]:cookie["value"] for cookie in cookies}
# print(cookie_list)
driver.quit()
