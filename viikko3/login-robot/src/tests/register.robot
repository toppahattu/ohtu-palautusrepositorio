*** Settings ***
Resource  resource.robot
Resource    login.robot
Test Setup  Create User And Input New Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  kissa  kissa123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  kalle456
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  ka  kissa123
    Output Should Contain  Username must be at least 3 characters long and contain only letters a-z

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials  Kalle  kissa123
    Output Should Contain  Username must be at least 3 characters long and contain only letters a-z

Register With Valid Username And Too Short Password
    Input Credentials  kissa  kissa
    Output Should Contain  Password must be at least 8 characters long and not contain only letters

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  kissa  kissakissa
    Output Should Contain  Password must be at least 8 characters long and not contain only letters

*** Keywords ***
Create User And Input New Command
    Create User  kalle  kalle123
    Input New Command