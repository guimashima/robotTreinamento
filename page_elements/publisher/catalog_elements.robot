***Variables***
# Main Page
${main_exploreContent}    css:.wrap-text a[href*=catalog]
${main_iconCam}           css:.icon-cam
${main_sslaCatalog}       css:a[href*="catalog?source=ssla"]
${main_brCatalog}         css:a[href*="catalog?source=br"]
${main_blimCatalog}       css:a[href*="catalog?source=blim"]
${main_catalogIcon}       xpath:.//div[@id='side-bar']//span[contains(.,'Catalog')]

#Catalog Page
${catalog_modalFilm}                css:#filmes-wrap
${catalog_firstFilm}                css:div[class="filme-item"]
${catalog_listFilms}                css:.filme-item
${catalog_radioFilm}                css:.ck-mark
${catalog_btnNext}                  css:.btn.next
${catalog_btnCancelEdit}            css:.edit-cancel
${catalog_contentTitle}             css:h4
${catalog_modalEditContent}         css:#modalEditMovie
${catalog_contentDescriptioin}      css:textarea[name="about-filme"]
${catalog_contentID}                css:.put-id
${catalog_saveEdit}                 css:.edit-save
${catalog_searchCatalog}            css:input[name="search"]
${catalog_serachParameter}          css:#opt-param
${catalog_searchSelectCaret}        css:b.caret
${catalog_paramProgramID}           css:label[title="Program ID"]
${catalog_selectedContentGenres}    css:.multiselect-selected-text b
${catalog_contentGenres}            css:select[name="genres"]
${catalog_searchFilter}             css:#filtro-itens
${catalog_contentLiveTag}           css:.LIVE
${catalog_contentMovieTag}          css:.MOVIE
${catalog_contentSerieTag}          css:.SERIE
${catalog_contentEpisodeTag}        css:.EPISODE
${catalog_contentSelectTag}         css:select[name="keywords"]
${catalog_contentSelectGenre}       css:select[name="genres"]
${catalog_btnMultiSelect}           css:.multiselect
${catalog_input}                    css:input[type="text"]
${catalog_btnAddTag}                css:.add-tag
${catalog_allSelectedValues}        css:span.multiselect-selected-text b
${catalog_addIcon}                  css:.add-icon
${catalog_removeIcon}               css:.rmv-icon
${catalog_uploadIconImg}            css:#file
${catalog_sendIcon}                 css:.enviar-img
${catalog_iconList}                 css:.slick-dots li
${catalog_iconLoading}              css:.loading.carrossel-container
${catalog_sourceTitle}              css:.box-search h2
${catalog_checkboxVOD-EPG}          css:input[name="vod-epg"]
${catalog_selectChannels}           css:#opt-channels
${catalog_selectOptions}            css:label.checkbox
${catalog_selectCategory}           css:#filtro-category
${catalog_btnSearch}                css:.go-search