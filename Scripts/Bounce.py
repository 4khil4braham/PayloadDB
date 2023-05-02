import subprocess
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def run_contest():
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get('https://www.example.com')
    try:
        
        browser.find_element_by_css_selector("element").click()
    except
        print("assign new IP")
        return True


def switch_ip():
    command = "sudo protonvpn c -r"
    proc = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


while True:
    needs_new_IP = False
    if not run_contest():
        print("running contest")
    else:
        switch_ip() 