Feature: Search

  Background: Open home page
    Given I am on the home page

    @cautare
  Scenario: Search works properly for existing items
    When I enter "watch" in the search field
    And I click on the search button
    Then I am redirected to the search results page
    And There are some results displayed