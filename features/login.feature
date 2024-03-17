Feature: Login Page

  Background: Open login page
    Given I am on the login page

  @smoke @regression
  Scenario: Check that the URL is correct
    Then The URL of the Login Page is correct

  @regression
  Scenario Outline: Log in with unregistered email
    When I enter "<username>" as email
    And I enter "<password>" as password
    And I click the login button
    Then I should see "The account sign-in was incorrect" message
    Examples:
      | username              | password |
      | mailtest@gmail.com    | 12345678 |
      | mailtest2@gmail.com   | 56789155 |
      | testmail@gmail.com    | abcdefg  |