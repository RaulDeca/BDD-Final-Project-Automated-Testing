from behave import *

@given("I am on the privacy page")
def step_impl(context):
    context.login_page.open()

@then('The url of the Privacy page is correct')
def step_impl(context):
    context.login_page.verify_url()