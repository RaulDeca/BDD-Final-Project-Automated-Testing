Automated Testing Project for Magento Website
This project is an automated testing suite developed in Python using various libraries including Selenium, Behave, Behave HTML Formatter, and Gherkin. The purpose of this project is to automate testing scenarios for the Magento website (https://magento.softwaretestingboard.com/).

Project Overview
The project consists of several test scenarios implemented using the BDD (Behavior-Driven Development) approach. It verifies essential functionalities of the Magento website such as URL verification, login functionality, registration process, and search functionality.

Prerequisites
Python 3.x
PyCharm or any other Python IDE
Selenium WebDriver
Behave
Behave HTML Formatter
Gherkin


Getting Started
Clone the Repository: Clone this repository to your local machine using:
git clone https://github.com/RaulDeca/BDD-Final-Project-Automated-Testing

Install Dependencies: Navigate to the project directory and install the required dependencies using: pip install

Configure WebDriver: Make sure to download the appropriate WebDriver for your browser (e.g., ChromeDriver for Chrome, GeckoDriver for Firefox) and place it in your system PATH or update the environment.py file with the path to the WebDriver.

Run Tests: Execute the test scenarios by running the following command: behave OR behave -f html -o report.html

Test Scenarios
URL Verification: Verifies if the Magento website URL is correct.
Login Error: Checks if an error is displayed when attempting to login with incorrect credentials.
Registration: Tests the registration process by providing correct user information.
Search Functionality: Validates the functionality of the search bar by performing a search and verifying the result page.

