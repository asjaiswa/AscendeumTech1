from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def test_dificulty_level():
    n = 10
    for i in range(1, n+1):
        driver = webdriver.Chrome()
        driver.maximize_window()
        #maximizing the browser

        driver.get("https://mathup.com/games/crossbit?mode=championship")
        #lounching the browser

        wait = WebDriverWait(driver, 10)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//*[text()='Start']"))).click()
        #explicit wait for more control on element

        dificulty_level_value = driver.find_element(By.XPATH,
                                                    "(//div[@class='GamePostStart_basic-info-wrapper__IGqxn']/div/div)[2]/div[2]").text
        print(dificulty_level_value)
        #printing the expected value

        assert dificulty_level_value == "Difficulty\nEasy"
        #assertion for validation

        driver.close()
        #closing the browser

    #we can convert same script in POM

# Output :

# Difficulty Easy
