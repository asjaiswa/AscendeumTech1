import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def test_dificulty_level():
    n = 10
    time_taken_for_all_iteration = 0
    for i in range(1, n + 1):
        driver = webdriver.Chrome()
        driver.maximize_window()
        # maximizing the browser

        #start_time
        start_time = time.time()
        print(start_time)

        driver.get("https://mathup.com/games/crossbit?mode=daily_challenge")
        # lounching the browser

        wait = WebDriverWait(driver, 10)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//*[text()='Start']")))
        # explicit wait for more control on element

        end_time = time.time()
        #calculating the end time

        time_taken = end_time - start_time
        print(f"Time taken: {time_taken}")
        #calculating the taken time

        time_taken_for_all_iteration = time_taken + time_taken_for_all_iteration
        #calulating time for all iteration to findout the avarage time taken by the script

        driver.close()
        # closing the browser

    print(f"Total Time taken for all iterations: {time_taken_for_all_iteration}")
    #Total Time taken for all iterations

    avg_time_taken = time_taken_for_all_iteration / float(n)
    print(f"Avarage time taken: {avg_time_taken}")
    #printing the avarage time taken by the script

    # we can convert same script in POM


# Output :
# Time taken: 5.461387395858765
# Total Time taken for all iterations: 56.63583016395569
# Avarage time taken: 5.6635830163955685
