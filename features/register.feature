@register
Feature: register
  registring steps here

  @signin
  Scenario: sign up on automationpractice website
    Given the home page is displayed
    When user clicks on <sign in> button
    Then new page with <create an account> is displayed

