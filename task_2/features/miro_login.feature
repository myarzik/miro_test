Feature: Miro login page
  Testing of https://miro.com/login page

  Background:
    Given the "/login" endpoint is opened


  Scenario: Checking the necessary elements
    When the "Login" page is displayed
    Then the item "logo" is visible
    And the item "sign up button" is visible
    And the item "sign in title" is visible
    And the item "sign in social panel" is visible
    And the item "email input" is visible
    And the item "password input" is visible
    And the item "password recover button" is visible
    And the item "sign in button" is visible
    And the item "sign in SSO button" is visible

  Scenario: Checking the sign up button
    When the "Login" page is displayed
    And press the element "sign up button"
    Then the current url is "https://miro.com/signup/"

  Scenario: Checking the password recover button
    When the "Login" page is displayed
    And press the element "password recover button"
    Then the current url is "https://miro.com/recover/"

  Scenario: Checking the sign in SSO button
    When the "Login" page is displayed
    And press the element "sign in SSO button"
    Then the current url is "https://miro.com/sso/login/"

  Scenario: Checking the logo clicking
    When the "Login" page is displayed
    And press the element "logo"
    Then the current url is "https://miro.com/"
    
  Scenario: trying to sign in without credentials
    When the "Login" page is displayed
    And press the element "sign in button"
    Then the current url is "https://miro.com/login/"
    And the item "enter email notice" is visible
    And the item "enter password notice" is visible

  Scenario: trying to sign in without password
    When the "Login" page is displayed
    And enter the text "123" to the "email input"
    And press the element "sign in button"
    Then the current url is "https://miro.com/login/"
    And the item "enter password notice" is visible

  Scenario: trying to sign in without email
    When the "Login" page is displayed
    And enter the text "123" to the "password input"
    And press the element "sign in button"
    Then the current url is "https://miro.com/login/"
    And the item "enter email notice" is visible

  Scenario: trying to sign in with wrong credentials
    When the "Login" page is displayed
    And enter the text "123" to the "email input"
    And enter the text "123" to the "password input"
    And press the element "sign in button"
    Then the current url is "https://miro.com/login/"
    And the item "wrong credentials notice" is visible

  #Need to change credentials for passing this scenario
  Scenario: trying to sign in with proper credentials
    When the "Login" page is displayed
    And enter the text "proper email" to the "email input"
    And enter the text "proper password" to the "password input"
    And press the element "sign in button"
    Then the current url is "https://miro.com/app/"