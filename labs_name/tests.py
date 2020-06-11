import time

from selenium import webdriver

URL_ROOT = 'https://olhaburtso01.github.io/'

fp = webdriver.FirefoxProfile()
fp.set_preference('security.mixed_content.block_active_content', False)
fp.set_preference('security.mixed_content.block_display_content', True)
driver = webdriver.Firefox(fp)

driver.get(URL_ROOT + 'index.html')

# test 1
assert 'Healthy' in driver.title

# test 2
nav_ul = driver.find_element_by_id('navigation')
children = nav_ul.find_elements_by_css_selector("*")
assert len(children) == 3 * 2
for child in children:
    child.click()
    time.sleep(1)
children[2].click()

# test 3
search_field = driver.find_element_by_id('search-query')
search_field.send_keys('BHT')
time.sleep(1)
driver.find_element_by_class_name('search-button').click()
time.sleep(3)

# test 4
search_result = driver.find_element_by_id('search-result')
required_fields = (
    'Supplements',
    'Class',
    'Purpose',
    'Side effects'
)
for required_field in required_fields:
    assert required_field in search_result.text
time.sleep(3)

# test 5
driver.find_element_by_class_name('search-button-inverse').click()
time.sleep(1)
alert = driver.switch_to.alert
alert.accept()
time.sleep(1)


print('TESTS PASSED SUCCESSFULLY')
driver.close()
