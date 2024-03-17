Feature: Registration page

    Background: Open register page
      Given I am on the register page

    Scenario: Check that the URL is correct
      Then The URL of the Register page is correct

    Scenario: Registering with empty mandatory fields
      When I click the register button
      Then First name error is displayed
      And Last name error is displayed
      And Email error is displayed
      And Password error is displayed
      And Confirm password error is displayed

    Scenario: Register new account with valid data
      When I enter "PY" in the first name input
      When I enter "TA" in the last name input
      When I enter a random email address in the email input
      When I enter "parola123456A" in the password input
      When I enter "parola123456A" in the password confirm input
      When I click the Register button
      Then Success message is displayed
      Then The success message is "Thank you for registering with Main Website Store."

