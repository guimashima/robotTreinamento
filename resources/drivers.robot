***Keywords***
Set chrome options
    ${options}          Create Chrome Options
    Call Method         ${options}      add_argument    incognito
    Create Webdriver    Chrome                   chrome_options=${options}

Set edge options
    ${options}          Create Edge Options
    Create Webdriver        Edge        capabilities=${options}

Set firefox options
    ${firefoxProfile}    Create Firefox profile
    Open Browser         ${HUB_URL}           firefox    ff_profile_dir=${firefoxProfile}

Set Browser Options
    ${status}         Run keyword And Return Status    Should Contain         ${BROWSER}    chrome
    Run Keyword If    ${status}                        Set chrome options
    ${status}         Run keyword And Return Status    Should Contain         ${BROWSER}    firefox
    Run Keyword If    ${status}                        Set firefox options
    ${status}         Run keyword And Return Status    Should Contain         ${BROWSER}    edge
    Run Keyword If    ${status}                        Set edge options