*** Settings ***
Resource  resource.robot

*** Keywords ***
Login Should Succeed
    Main Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}

Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${confirmation}
    Input Password  password_confirmation  ${confirmation}

Submit Credentials
    [Arguments]  ${button_name}
    Click Button  ${button_name}

Logout
    Click Button  Logout

Login With Username And Password
    [Arguments]  ${username}  ${password}
    Set Username  ${username}
    Set Password  ${password}
    Submit Credentials  Login

Register With Username Password And Confirmation
    [Arguments]  ${username}  ${password}  ${confirmation}
    Set Username  ${username}
    Set Password  ${password}
    Set Password Confirmation  ${confirmation}
    Submit Credentials  Register