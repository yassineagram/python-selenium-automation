from selenium.webdriver.common.by import By
from behave import given, then
from time import sleep




COLOR_OPTIONS = (By.CSS_SELECTOR, "[class*='ButtonWrapper'] img")
SELECTED_COLOR = (By.CSS_SELECTOR, "[class*='StyledVariationSelectorImage'] [class*='CellVariationHeaderWrapper']")




@given('Open target product {product_id} page')
def open_target(context, product_id):
    context.driver.get(f'https://www.target.com/p/{product_id}')
    sleep(6)




@then('Verify user can click through colors')
def click_and_verify_colors(context):
    expected_colors = ['Black', 'Deep olive', 'White', 'Blue Tint', 'Denim Blue', 'Marine', 'Raven']
    actual_colors = []


    colors = context.driver.find_elements(*COLOR_OPTIONS)
    for color in colors[:3]:
        color.click()
        selected_color = context.driver.find_element(*SELECTED_COLOR).text
        selected_color = selected_color.split('\n')[1]
        actual_colors.append(selected_color)



    assert expected_colors == actual_colors, f'Expected {expected_colors} did not match actual {actual_colors}'