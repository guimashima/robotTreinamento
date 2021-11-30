***Variables***
# Main Page
${main_newCarousel}     xpath://div[@class="wrap-text"]//a[contains(.,"New Carousel")]
${main_allCarousels}    xpath://div[@class="wrap-text"]//a[contains(.,"View All")]
${loading}              css:.loading

#Carousel List Page
${allComponents_table}                  css:#list-table
${allComponents_list}                   css:#list-table tbody tr
${allComponents_options}                css:.options                
${allComponents_delete}                 css:.delete-tr              
${allComponents_fastEdit}               css:.show-fast-edit         
${allComponents_edit}                   css:.go-edit                
${allComponents_duplicate}              css:.duplicar-tr            
${allComponents_modalDelete}            css:#modalDelete
${allComponents_btnDeleteConfirm}       css:.delete-confirm
${allComponents_btnFastSave}            css:.fast-save
${allComponents_modalDuplicate}         css:#modalDuplicate
${allComponents_btnConfirmDuplicate}    css:.duplicar-confirm
${allComponents_title}                  css:p.text
${allComponents_status}                 css:span.dropdown-link
${allComponents_btnDraft}               css:.save-rasc
${allComponents_btnNewCarousel}         css:.btn.new-carousel
${allComponents_searchComponent}        css:#search-o
${allComponents_emptyTable}             css:.dataTables_empty

#Carousel Form
${form_carouselForm}             css:#car-form-wrap
${form_componentName}            css:input[name="article-name"]
${form_carouselTitle}            css:input[name="carousel-title"]
${form_carouselType}             css:#tipo
${form_catalogSource}            css:#source
${form_switchBuy}                css:input[name="switch-buy"]
${form_carouselAddFilms}         css:form .add-filmes
${form_carouselAddFilter}        css:.btn-filter
${form_filterForm}               css:.make-filter
${form_newFilter}                css:.new-filter
${form_filterGroupName}          css:input[name="filter-group-name"]
${form_filterType}               css:select[name="filtro"]
${form_filterInsertValue}        css:.insert-field
${form_filterSelectTypeValue}    css:select[name="chose-opt"]
${form_filterInputTypeValue}     css:input[name='chose-opt']
${form_filterOrderby}            css:.make-filter select[name="order-by"]
${form_filterAscdesc}            css:select[name="asc-desc"]
${form_filterLimit}              css:input[name="limit-filter"]
${form_addNewFilter}             css:.add-new-filter
${form_createFilter}             css:.add-filter-block
${form_filterDrag}               css:.filme-row-drag
${form_attachPage}               css:#incluir
${form_startDate}                css:input[name="start"]
${form_startTime}                css:input[name="start-time"]
${form_endDate}                  css:input[name="end"]
${query_endDate}                 input[name="end"]                           #usado para executar um js
${query_startDate}               input[name="start"]                         #usado para executar um js
${form_endTime}                  css:input[name="end-time"]
${form_disableEndDate}           css:input.disable-end
${form_disableEndDateCB}         css:.input-container .solo span
${form_btnViewer}                css:.btn-viewer
${form_btnPublish}               css:.btn.pub
${form_uploadBackgroundImage}    css:#file_cover 
${form_uploadCardImage}          css:#file_card
${form_contentList}              css:#drag-groups .filme-row-drag
${form_contentDrag}              css:.move
${form_editContent}              css:.editar
${form_editAutoContentForm}      css:#modalEditAuto
${form_editManualContentForm}    css:#modalEditManual
${form_btnSaveContentEdit}       css:.edit-save
${form_modalNoPage}              css:#modalNoPage
${form_btnNoPageOK}              css:.ok-no-page
${form_taid}                     css:input[name="ta-id"]
${form_modalReplaceHl}           css:#modalReplaceHl
${form_noReplaceHl}              css:.no-replace
${form_link}                     css:input[name="link"]
${form_linkType}                 css:select[name="link-type"]
${form_linkLabel}                css:input[name="link-label"]
${form_bannerTitle}              css:input[name="banner-title"]
${form_bannerSubtitle}           css:input[name="banner-subtitle"]
${form_bannerOverlay}            css:input[name="banner-overlay"]
${form_description}              css:textarea[name="description"]
${form_switchTA}                 css:input[name="is-ta"]
${form_addBanner}                css:.btn-add-banner
${form_addIcon}                  css:.add-icons
${form_bannerTag}                css:i.tipo.Banner
${form_sortByStatus}             xpath://span[contains(.,'Status')]
${form_statusList}               css:ul.status-items
${form_modalDuplcateBanner}      css:#modalDoubleBanner
${form_modaFileError}            css:#modalFileError
${form_btnCancel}                css:.btn-cancel

# Phone Viewer
${phone_mainId}           css:#phone-wrap
${phone_header}           css:.browser-image
${phone_carouselTitle}    css:.preview-carousel h3
${phone_carouselImage}    css:.carousel-wrap .slick-list
${phone_highlighImage}    css:.phone-viewer .browser-image.banner