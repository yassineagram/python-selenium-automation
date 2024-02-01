from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open Target main page')
def open_target_main_page(context):
    context.driver.get("http://www.target.com/")


@when('Click on Cart icon')
def Click_on_cart_icon(context):
    context.driver.find_element_by_css_selector("[aria-label='cart 0 items']").click()
    sleep(6)


@then('Verify “Your cart is empty” message is shown')
def verify_message_shown(context):
    actual_result = context.driver.find_element_by_css_selector("[class='styles__StyledHeading-sc-1xmf98v-0 lfA-Dem']").text
    assert 'Your cart is empty' in actual_result, f'The cart is not in {actual_result}'
    print('test case passed')





