import sys
import time
from URLS import Base
import mail_stuff

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

register_add_drop ='#PG_MYMENU_HMPG_Data > div >\
table > tbody > tr:nth-child(1) > td > table > tbody > tr:nth-child(6) >\
td > table > tbody > tr:nth-child(2) > td:nth-child(3) > table > tbody >\
tr:nth-child(2) > td > table > tbody > tr:nth-child(7) > td:nth-child(2) > a'

flag = False

browser = webdriver.Chrome()
browser.get(Base.url)
browser.find_element_by_id('userid').send_keys(Base.uid)
browser.find_element_by_id('pwd').send_keys(Base.pwd + Keys.RETURN)

try:
	element = WebDriverWait(browser, 10).until(
		EC.visibility_of_element_located((By.CSS_SELECTOR, register_add_drop)))
	element.click()
except TimeoutException:
	print('failed')
	browser.close()
	sys.exit(0)


browser.switch_to_frame(browser.find_element_by_xpath('//*[@id="ptifrmcontent"]/div/iframe'))

while not flag:
	# add classes button to refresh
	browser.find_element_by_xpath('//*[@id="win0divDERIVED_SSTSNAV_SSTS_NAV_SUBTABS"]/div/table/tbody/tr[2]/td[5]/a').click()

	# get contents of shopping cart:
	entries = browser.find_elements_by_xpath('//*[@id="SSR_REGFORM_VW$scroll$0"]/tbody/tr') # grabs table

	# for i in range(2,len(entries)): # 2 because first 2 rows are rubbish
		# entries[i].click()
		
	for i in range(0,len(entries)-2):
		status = browser.find_element_by_xpath('//*[@id="win0divDERIVED_REGFRM1_SSR_STATUS_LONG${}"]/div/img'.format(i))
		status.click()
		if 'CLOSED' not in status.get_attribute("src"):
			flag = True
			mail_stuff.send_mail()
			
			#proceed to step 2 of 3 button
			browser.find_element_by_id('DERIVED_REGFRM1_LINK_ADD_ENRL$82$').click()

			try:
				element = WebDriverWait(browser, 10).until(
					EC.visibility_of_element_located((By.ID, 'DERIVED_REGFRM1_SSR_PB_SUBMIT')))
				element.click()
			except TimeoutException:
				print('failed')
				browser.close()
				sys.exit(0)
			
			# get into next iframe again -- NOT NEEDED
			# browser.switch_to_frame(browser.find_element_by_xpath('//*[@id="ptifrmtgtframe"]'))
			
			# finish !
			# browser.find_element_by_id('DERIVED_REGFRM1_SSR_PB_SUBMIT').click()

browser.close()
sys.exit()


# search button
browser.find_element_by_id('DERIVED_REGFRM1_SSR_PB_SRCH').click()

# return to shopping cart
browser.find_element_by_xpath('//*[@id="CLASS_SRCH_WRK2_SSR_PB_CLOSE"]').click()



''' START BROWSER METHODS:

find_element
find_element_by_id
find_element_by_name
find_element_by_tag_name
find_element_by_class_name
find_element_by_link_text
find_element_by_partial_link_text
find_element_by_css_selector
find_element_by_xpath

find_elements
find_elements_by_id
find_elements_by_name
find_elements_by_tag_name
find_elements_by_class_name
find_elements_by_link_text
find_elements_by_partial_link_text
find_elements_by_css_selector
find_elements_by_xpath

current_url
get_cookies
set_window_size
error_handler
close
set_page_load_timeout
delete_cookie
get_screenshot_as_file
desired_capabilities
maximize_window
page_source
execute_async_script
set_window_position
switch_to_frame
add_cookie
_switch_to
window_handles
start_client
log_types
delete_all_cookies
execute
set_script_timeout
get_window_size
get_cookie
orientation
get_screenshot_as_png
switch_to_window
get_window_position
switch_to_active_element
_is_remote
execute_script
command_executor
_wrap_value
file_detector
service
switch_to_alert
get
_file_detector
capabilities
refresh
mobile
forward
create_web_element
application_cache
create_options
file_detector_context
session_id
back
quit
launch_app
stop_client
current_window_handle
start_session
switch_to
save_screenshot
name
get_screenshot_as_base64
title
w3c
implicitly_wait
get_log
_unwrap_value
_web_element_cls
_mobile
switch_to_default_content

END BROWSER METHODS: '''