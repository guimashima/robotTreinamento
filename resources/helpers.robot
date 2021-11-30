**Settings**
Resource    libraries.robot
Resource    page_objects.robot
Resource    keywords.robot
Resource    drivers.robot

**Variables**


***Keywords***
Open Browser
    Set browser options
    Goto                                https://www.google.com
    Set Selenium Timeout                                30
    Maximize Browser Window
    
Close Session
    Capture Page Screenshot
    Close Browser

Create Header and Parameter Dictionary
    ${headers}         Create Dictionary
    ${parameters}      Create Dictionary
    Set Test Variable       ${headers}
    Set Test Variable       ${parameters}
