from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = "/Users/adithya/chromedriver"
driver = webdriver.Chrome(PATH)

driver.get("https://www.amazon.com")

search = driver.find_element_by_id("twotabsearchtextbox")
search.send_keys("laptop")
search.send_keys(Keys.RETURN)
final_items = []
final_prices = []
try:
    main = WebDriverWait(driver, 10).until(
        #EC.presence_of_element_located((By.XPATH, '//*[@id="search"]/div[1]/div[2]/div/span[3]/div[2]'))
        EC.presence_of_element_located((By.ID, 'search'))
    )
    #print(main.text)
    desktop_window = main.find_element_by_css_selector('.s-desktop-width-max.s-desktop-content.sg-row')
    #print(desktop_window.text)
    item_list = desktop_window.find_element_by_css_selector('.sg-col-20-of-24.sg-col-28-of-32.sg-col-16-of-20.sg-col.sg-col-32-of-36.sg-col-8-of-12.sg-col-12-of-16.sg-col-24-of-28')
    #print(item_list.text)
    item_list_inner = item_list.find_element_by_class_name('sg-col-inner')
    #print(item_list.text)
    result_list = item_list_inner.find_element_by_css_selector('.s-main-slot.s-result-list.s-search-results.sg-row')

    items = result_list.find_elements_by_css_selector("[data-component-type='s-search-result']")
    for item in items:
        if not isinstance(item,str):
            item_inner = item.find_element_by_class_name('sg-col-inner')
            #print(item_inner.text)
            #item_widget = item_inner.find_element_by_css_selector('.celwidget.slot=MAIN.template=SEARCH_RESULTS.widgetId=search-results')
            item_widget = item_inner.find_element_by_xpath('.//span[@class = "celwidget slot=MAIN template=SEARCH_RESULTS widgetId=search-results"]')
            #print(item_widget.text)
            content_margin = item_widget.find_element_by_css_selector('.s-include-content-margin.s-border-bottom.s-latency-cf-section')
            #print(content_margin.text)
            section_spacing = content_margin.find_elements_by_class_name('sg-row')[1]
            #print(section_spacing.text)
            sg_col = section_spacing.find_element_by_css_selector('.sg-col-4-of-12.sg-col-8-of-16.sg-col-16-of-24.sg-col-12-of-20.sg-col-24-of-32.sg-col.sg-col-28-of-36.sg-col-20-of-28')
            #print(sg_col.text)
            sg_col_inner = sg_col.find_element_by_class_name('sg-col-inner')

            # a_section = sg_col_inner.find_element_by_css_selector('.a-section.a-spacing-none')
            #
            # a_size_mini = a_section.find_element_by_css_selector('.a-size-mini.a-spacing-none.a-color-base.s-line-clamp-2')
            #
            # a_link_normal = a_size_mini.find_element_by_css_selector('.a-link-normal.a-text-normal')
            #
            #a_size_medium = a_link_normal.find_element_by_css_selector('.a-size-medium.a-color-base.a-text-normal')

            #print(a_size_medium.text)

            # price
            sg_row = sg_col_inner.find_elements_by_css_selector('.sg-row')[1]

            try:
                a_size_medium = sg_col_inner.find_element_by_css_selector('.a-size-medium.a-color-base.a-text-normal')
                item_1 = str(a_size_medium.text)
                a_price_whole = sg_row.find_element_by_css_selector('.a-price-whole')
                price = a_price_whole.text.replace(",", "")
                #print(price, item, "\n")
                final_items.append(item_1)
                #print(item_1)
                final_prices.append(int(price))
            except:
                print("Item price not available")
                #e = sys.exc_info()[0]
                #print(e)

            #print(a_price_whole.text, "\n")
    print("finished printing")
    #print(items)
    #for i,item in enumerate(final_items):
        #print("Item", final_items[i], "Price", final_prices[i])
except:
    driver.quit()
    print("failed")
    e = sys.exc_info()[0]
    print(e)

#main = self.driver.find_elements_by_xpath('//ul[@id="s-results-list-atf"]/li/div/div/div/div[2]/div[1]/a')


driver.quit()

good_ones = []
for i,item in enumerate(final_items):
    # i5 or ryzen 5
    # 8GB ram or 16GB ram
    # 1080p screen
    # under $500
    if int(final_prices[i]) <= 700:
        if "i5" in item.lower() or "ryzen 5" in item.lower():
            if "8gb" in item.lower() or "12gb" in item.lower() or "16gb" in item.lower():
                if "1080" in item.lower() or "full hd" in item.lower():
                    good_ones.append(True)
                    print("Item", final_items[i], "Price", final_prices[i])
                else:
                    good_ones.append(False)
            else:
                good_ones.append(False)
        else:
            good_ones.append(False)
    else:
        good_ones.append(False)
