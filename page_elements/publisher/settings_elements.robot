***Variables***
# Publisher Main page
${settingsIcon}    css:#side-bar a[href*="settings"]
${homeIcon}        css:#side-bar a[href*="home"]

# Settings page
${settings_contentLimit}        css:input[name="limite-itens"]
${settings_carouselTypeInput}        css:input[name="type-carousel"]
${settings_pageTypeInput}       css:input[name="type-page"]
${settings_pageType}            css:.type-page
${settings_carouselType}            css:.type-carousel
${settings_updateListButton}    css:.update-list
${settings_monetarySymbol}      css:input[name="monetary-symbol"]
${settings_carouselTypeList}    css:.item-type span
${settings_settingsEdit}        css:.edit
${settings_editedIcon}          css:.edited
${settings_saveSettings}        css:.config-save
${settings_settingsSaved}       css:#modalSaved
${settings_settingsSavedOK}     css:button[data-dismiss="modal"]
${settings_maxLimit}            css:#modalMaxLimit
${settings_typeList}            css:.item-type
${settings_removeTypeIcon}      css:.remove
${settings_editTypeIcon}      css:.edit
${settings_inputTypeTextbox}    css:input[type="text"]
