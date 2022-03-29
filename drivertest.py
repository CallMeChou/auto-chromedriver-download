#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@File    : drivertest.py
@Time    : 2022/03/29 09:30:34
@Author  : chou
@Contact : chou2079986882@gmail.com
@Version : 0.1
@Desc    : None 
'''

from selenium import webdriver
import time
import json
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


#获取cookie
def cookie_get():
    # 以下三行为无头模式运行，无头模式不开启浏览器
    chrome_options = Options()
    # chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    # 设置访问链接
    driver.get("https://yqfk.zhxy.net/Login/Index")
    # 输入密码，点击登录
    driver.find_element(By.XPATH, '''//input[starts-with(@id,'lr_username')]''').send_keys('0720100012')  # 账号
    driver.find_element(By.XPATH, '''//input[starts-with(@id,'lr_password')]''').send_keys('liuboxhu888')  # 密码
    driver.find_element(By.XPATH, '''//div[starts-with(@class,'lr-login-btn')]''').click()
    wait = WebDriverWait(driver, 4, 0.5)
    wait.until(EC.element_to_be_clickable((By.XPATH,'''//li[starts-with(@title,'疫情报告')]''')))
    driver.find_element(By.XPATH,'''//li[starts-with(@title,'疫情报告')]''').click()
    # 获取cookie
    cookie_items = driver.get_cookies()
    cookie_str = ""
    # 组装cookie字符串
    for item_cookie in cookie_items:
        item_str = item_cookie["name"] + "=" + item_cookie["value"] + "; "
        cookie_str += item_str
    return cookie_str

print(cookie_get())

#抓包获取到的

"""👇👇👇"""
# cookies = "sys_uitheme=4; __RequestVerificationToken=ckNHAggXkg9s8XkwzeZ6N0DktPanowPiK-5WnwbvfSkLQSjwI6HmrM1j6MJlU-acjeWNx5BBHexDmTt25OCgGvhIFGchDSXvnENj2SPGQFM1; ASP.NET_SessionId=lgsqm4w1tfc2s5f0awxjlckp; ShuoYun_ADMS_V7_Mark=d7075116-2757-4e79-96ca-25069e536bf2; ShuoYun_ADMS_V7_Token=6161f62b-77ea-4652-bf7a-702459277db0"

# 自动获取的👇
# ShuoYun_ADMS_V7_Token=2c1200ce-699e-4129-8b69-1f9379cc6818; ShuoYun_ADMS_V7_Mark=cbee98f7-c3c9-4c56-bce1-dae41d522620; ASP.NET_SessionId=4gtzasm0gwjx0psn0seboabk; __RequestVerificationToken=2cCcP1GjBTcxkYK6sjwKEFgPQt4AwDk8xjXS63gY5h28hpxdedTpKDHvB-s_T4KHvW5oAvtRRI6304I9SKlBlfiOk22tbstRpfHPVFtTmwQ1; sys_uitheme=4;