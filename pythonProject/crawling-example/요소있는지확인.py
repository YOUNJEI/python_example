from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

TIMEOUT_SECONDS = 5

# Chrome options
options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(options=options)

def crawling(url, isuSrtCd):
    try:
        # open browser
        driver.get(url)
        element = WebDriverWait(driver, TIMEOUT_SECONDS).until(EC.presence_of_element_located((By.ID, 'perBandCht')))

        # chart data buttons
        buttons = []
        buttons.append([driver.find_element(By.ID, 'perBandCht')])    # PER
        buttons.append([driver.find_element(By.ID, 'pbrBandCht')])    # PBR
        buttons.append([driver.find_element(By.ID, 'balanceCht')])    # 대차잔고비중
        buttons.append([driver.find_element(By.ID, 'sellCht')])       # 차입공매도비중
        buttons.append([driver.find_element(By.ID, 'mainChart01')])   # 투자의견 목표주가 (과거 히스토리)

        # financialHighlight
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        print(soup.has_attr('#highlight_D_A > table > tbody'))
        table = soup.select_one('#highlight_D_A > table > tbody')
        lines = table.select('tr')

        # chart data
        for button in buttons:
            button[0].click()
            driver.switch_to.window(driver.window_handles[-1])
            element = WebDriverWait(driver, TIMEOUT_SECONDS).until(EC.presence_of_element_located((By.CLASS_NAME, 'clf')))

            soup = BeautifulSoup(driver.page_source, 'html.parser')

            table = soup.select_one('#chartDataGrid > table')
            lines = table.select('tbody > tr')
            #button[1](lines, isuSrtCd)
            driver.close()
            driver.switch_to.window(driver.window_handles[0])

        # 컨센서스
        consensusBtn = driver.find_element(By.CSS_SELECTOR, '#compGnb > ul > li.gnb_dp1.gnb_ac > ul > li.gnb_dp2.gnb_dp2_start > a:nth-child(6)')
        consensusBtn.click()
        element = WebDriverWait(driver, TIMEOUT_SECONDS).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#bodycontent3 > tr > td')))
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        table = soup.select_one('#compBody > div.section.ul_de > div:nth-child(3) > div.um_table > table')

        lines = table.select('tbody > tr')
        lines = lines[1:]

    finally:
        if len(driver.window_handles) > 1:
            exit_list = driver.window_handles[1:]
            for e in exit_list:
                driver.switch_to.window(e)
                driver.close()

if __name__ == "__main__":
    print('> 크롤링 데이터 적재 시작')

    stockList = []
    stockList.append('A088980')
    total = len(stockList)
    print('> TO DO: ' + str(total))
    success = 0
    fail = 0
    for stock in stockList:
        url = 'https://comp.fnguide.com/SVO2/ASP/SVD_main.asp?pGB=1&gicode='
        url += stock
        url += '&cID=&MenuYn=Y&ReportGB=&NewMenuID=11&stkGb=&strResearchYN='

        try:
            crawling(url, stock[0])
            success += 1

        except Exception:
            print(url)
            import traceback
            traceback.print_exc()
            fail += 1


    print('> 크롤링 데이터 적재 완료.')
    print('total: ' + str(total))
    print('success: ' + str(success))
    print('fail: ' + str(fail))

    exit_list = driver.window_handles[0:]
    for e in exit_list:
        driver.switch_to.window(e)
        driver.close()
        driver.quit()