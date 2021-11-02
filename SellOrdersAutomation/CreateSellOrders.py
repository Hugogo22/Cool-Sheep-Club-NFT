from time import sleep
from os import path

from selenium.webdriver import Firefox, FirefoxOptions
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import number_of_windows_to_be

# Add the link to your firefox profile here
# Example : C:\\Users\\YourName\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\something.default\\
PathToProfile = ""

if (PathToProfile == ""):
    PathToProfile = input("Enter the path to your firefox profile (Something like \"C:\\Users\\YourName\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\something.default\\\"): ")

# Add your contract address here
ContractAddress = ""

if (ContractAddress == ""):
    ContractAddress = input("Enter your contract address : ")

opt = FirefoxOptions()
opt.add_argument("-profile")
opt.add_argument(PathToProfile)
s = Service(path.join(path.dirname(__file__), "geckodriver.exe"))

file = open(path.join(path.dirname(__file__), "../NftGeneration/pricestest.txt"), "r")

nbstart = int(input("What is the start (included) of the range of nft you want to sell? "))
nbend = int(input("What is the end (included) of the range of nft you want to sell? (You have to switch to firefox and login to metamask once you have answered) "))

for i in range(1, nbstart):
    file.readline()

with Firefox(service=s, options=opt) as driver:

    driver.implicitly_wait(10)
    driver.maximize_window()
    original_window = driver.current_window_handle
    wait = WebDriverWait(driver, 10)

    sleep(15)

    for i in range(nbstart, nbend+1):

        price = file.readline().split(" ")[2]

        driver.get("https://opensea.io/assets/matic/" + ContractAddress + "/" + str(i) + "/sell")
        driver.find_element(By.NAME, "price").send_keys(price)

        driver.find_element(By.CSS_SELECTOR, "button[type=\"submit\"]").click()
        driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div/section/div/div/section/div/div/div/div/div/div/div/button").click()

        wait.until(number_of_windows_to_be(2))
        for window_handle in driver.window_handles:
            if window_handle != original_window:
                driver.switch_to.window(window_handle)
                break

        driver.find_element(By.CSS_SELECTOR, ".btn--rounded.btn-primary").click()
        driver.switch_to.window(original_window)

    sleep(5)

