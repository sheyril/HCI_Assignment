import requests
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import xlsxwriter

num: int = 5

do_not_scan = (
    '#',
    '.pdf',
    '.doc',
    '.docx',
    '.xls',
    '.xlsx',
    '.ppt',
    '.pptx',
    '.doc',
    '.docx',
    '.odt',
    '.ods',
    '.jpg',
    '.png',
    '.zip',
    '.rar',
    '.mpeg',
    '.apk',
    '.exe',
)

# Also, we don't want to validate special links
do_not_validate = (
    'javascript:',
    'mailto:',
    'tel:',
)

while num != 0:
    workbook = xlsxwriter.Workbook("HCI Assignment 2_" + str(num) + ".xlsx")
    worksheet = workbook.add_worksheet("BITS")

    worksheet.write('A1', 'Website')
    worksheet.write('B1', 'Link')
    worksheet.write('C1', 'Broadband Provider')
    worksheet.write('D1', 'Front End Link Load Time (in ms)')
    worksheet.write('E1', 'Back End Link Load Time (in ms)')
    worksheet.write('F1', 'Net Link Load Time (in ms)')
    worksheet.write('G1', 'Link is dead or timed out (Y/N)')

    rowIndex = 2

    options = Options()
    options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"

    capabilities = DesiredCapabilities.FIREFOX.copy()
    capabilities['platform'] = "WINDOWS"
    capabilities['acceptInsecureCerts'] = True

    driver = webdriver.Firefox(options=options, desired_capabilities=capabilities)

    url = "https://www.usa.gov/"
    driver.get(url)

    # driver.find_element(By.CSS_SELECTOR, ".close").click()
    # only for NREGA website
    links = driver.find_elements_by_css_selector("a")
    links_hrefs = [link.get_attribute('href') for link in links]
    for link in links_hrefs:
        link_url = link
        if link_url and not link_url.startswith(do_not_validate) and not link_url.endswith(do_not_scan):
            try:
                if requests.head(link_url).status_code >= 200 or requests.head(
                        link_url).status_code < 400:
                    driver.get(link_url)
                    print(link_url + " is valid")
                    navigationStart = driver.execute_script("return window.performance.timing.navigationStart")
                    responseStart = driver.execute_script("return window.performance.timing.responseStart")
                    domComplete = driver.execute_script("return window.performance.timing.domComplete")

                    backendPerformance_calc = responseStart - navigationStart
                    frontendPerformance_calc = domComplete - responseStart

                    print("Back End: %s ms" % backendPerformance_calc)
                    print("Front End: %s ms" % frontendPerformance_calc)
                    # driver.find_element(By.CSS_SELECTOR, ".close").click()
                    driver.back()

                    worksheet.write('A' + str(rowIndex), url)
                    worksheet.write('B' + str(rowIndex), link_url)
                    worksheet.write('C' + str(rowIndex), "Airtel Fiber")
                    worksheet.write('D' + str(rowIndex), frontendPerformance_calc)
                    worksheet.write('E' + str(rowIndex), backendPerformance_calc)
                    worksheet.write('F' + str(rowIndex), frontendPerformance_calc + backendPerformance_calc)
                    worksheet.write('G' + str(rowIndex), "N")

                else:
                    print(link_url + " is Broken link")
                    worksheet.write('A' + str(rowIndex), url)
                    worksheet.write('B' + str(rowIndex), link_url)
                    worksheet.write('C' + str(rowIndex), "Airtel Fiber")
                    worksheet.write('D' + str(rowIndex), "NA")
                    worksheet.write('E' + str(rowIndex), "NA")
                    worksheet.write('F' + str(rowIndex), "NA")
                    worksheet.write('G' + str(rowIndex), "Y")
            except:
                print(link_url + " is also broken")
                worksheet.write('A' + str(rowIndex), url)
                worksheet.write('B' + str(rowIndex), link_url)
                worksheet.write('C' + str(rowIndex), "Airtel Fiber")
                worksheet.write('D' + str(rowIndex), "NA")
                worksheet.write('E' + str(rowIndex), "NA")
                worksheet.write('F' + str(rowIndex), "NA")
                worksheet.write('G' + str(rowIndex), "Y")
        rowIndex += 1

    workbook.close()
    num -= 1
