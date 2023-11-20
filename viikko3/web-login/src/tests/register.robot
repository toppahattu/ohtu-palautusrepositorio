*** Settings ***
Resource  resource.robot
Resource  login_resource.robot
Suite Setup  Open And Configure Browser
Test Teardown  Reset Application
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Register With Username Password And Confirmation  kissa  kissa123  kissa123
    Register Should Succeed

Register With Too Short Username And Valid Password
    Register With Username Password And Confirmation  ki  kissa123  kissa123
    Register Should Fail With Message  Username must be at least 3 characters long and contain only letters a-z

Register With Valid Username And Invalid Password
# salasana ei sisällä halutunlaisia merkkejä
    Register With Username Password And Confirmation  kissa  kissakis  kissakis
    Register Should Fail With Message  Password must be at least 8 characters long and not contain only letters

Register With Nonmatching Password And Password Confirmation
    Register With Username Password And Confirmation  kissa  kissa123  kissa12
    Register Should Fail With Message  Password and password confirmation do not match

Login After Successful Registration
    Register With Username Password And Confirmation  kissa  kissa123  kissa123
    Register Should Succeed
    Go To Main Page
    Main Page Should Be Open
    Logout
    Login Page Should Be Open
    Login With Username And Password  kissa  kissa123
    Login Should Succeed

Login After Failed Registration
    Register With Username Password And Confirmation  kissa  kissa123  kissa12
    Register Should Fail With Message  Password and password confirmation do not match
    Go To Login Page
    Login Page Should Be Open
    Login With Username And Password  kissa  kissa123
    Login Should Fail With Message  Invalid username or password
