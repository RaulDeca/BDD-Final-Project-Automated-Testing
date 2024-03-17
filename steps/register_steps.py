from behave import *

@given("I am on the register page")
def step_impl(context):
    context.register_page.open()

@then('The URL of the Register page is correct')
def step_impl(context):
    context.register_page.verify_url()

@when('I enter "{text}" in the first name input')
def step_impl(context, text):
    context.register_page.set_first_name(text)

@when('I enter "{text}" in the last name input')
def step_impl(context, text):
    context.register_page.set_last_name(text)

@when('I enter a random email address in the email input')
def step_impl(context):
    context.register_page.set_unique_email()

@when('I enter "{text}" in the password input')
def step_impl(context, text):
    context.register_page.set_password(text)

@when('I enter "{text}" in the password confirm input')
def step_impl(context, text):
    context.register_page.set_password_confirm(text)

@when('I click the Register button')
def step_impl(context):
    context.register_page.click_register_button()

@then('Success message is displayed')
def step_impl(context):
    context.register_page.verify_success_message_displayed()

@then('The success message is "{text}"')
def step_impl(context, text):
    context.register_page.verify_success_message_contains_text(text)

@then('First name error is displayed')
def step_impl(context):
    context.register_page.verify_first_name_error_displayed()

@then('Last name error is displayed')
def step_impl(context):
    context.register_page.verify_last_name_error_displayed()

@then('Email error is displayed')
def step_impl(context):
    context.register_page.verify_email_error_displayed()

@then('Password error is displayed')
def step_impl(context):
    context.register_page.verify_password_error_displayed()

@then('Confirm password error is displayed')
def step_impl(context):
    context.register_page.verify_confirm_password_error_displayed()





