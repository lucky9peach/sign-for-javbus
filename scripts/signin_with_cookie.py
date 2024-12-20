import os
import requests

# 从环境变量中获取cookie字符串
cookie_str = os.environ.get('FORUM_COOKIE')

base_url = 'https://www.javbus.com/forum/'
signin_url = base_url + 'plugin.php?id=xxx_signin'  # 根据实际情况修改

session = requests.Session()
session.headers.update({'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64)'})

# 将Cookie字符串解析成字典并设置到session
cookies = {}
for c in cookie_str.split(';'):
    c = c.strip()
    if '=' in c:
        key, val = c.split('=', 1)
        cookies[key.strip()] = val.strip()
session.cookies.update(cookies)

# 使用session访问签到页面
signin_res = session.get(signin_url)
signin_res.raise_for_status()

# 判断签到是否成功（根据页面返回内容判断）
if "签到成功" in signin_res.text or "已签到" in signin_res.text:
    print("已成功签到（使用Cookie）！")
else:
    print("无法确认是否签到成功，请检查返回内容。")
