# Created by yassine at 2/1/24
Feature: Test main features in Target.com


  Scenario: Verifies that “Your cart is empty” message is shown
    Given Open Target main page
    When Click on Cart icon
    Then Verify “Your cart is empty” message is shown