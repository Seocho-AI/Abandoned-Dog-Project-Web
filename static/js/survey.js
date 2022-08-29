/**
 * Move to Home page
 */
document.querySelector(".navbar-brand").addEventListener("click", moveToHomePage)
document.querySelector(".nav-home").addEventListener("click", moveToHomePage)

function moveToHomePage() {
  window.location.href = "/" // Move to home page
}

/**
 * Move to Find Dog page
 */
document.querySelector(".nav-find-dog").addEventListener("click", moveToAbandonedDogPage)

function moveToAbandonedDogPage() {
  window.location.href = "/find_dog" // Move to page
}

/**
 * Nav change bg on scroll
 */
$(function () {
  $(document).scroll(function () {
    var $nav = $("#header");
    $nav.toggleClass('scrolled', $(this).scrollTop() > $nav.height());
  });
});

/**
 * Survey Theme Change
 */
Survey.StylesManager.applyTheme("defaultV2"); // Survey Themes : defaultV2, modern

/**
 * Survey Page/Questions (Question on separate page)
 */
// var json = {
//   firstPageIsStarted: true,
//   title: "나에게 맞는 AI 기반 유기견 추천!",
//   description: "모든 질문에 답을 하면 귀하에게 적합한 유기견(종)을 찾아드립니다!",
//   startSurveyText: "나에게 맞는 유기견 찾기!",
//   showProgressBar: "top",
//   locale: "ko",
//   pages: [{
//     elements: [{
//       type: "html",
//       html: "나에게 맞는 유기견을 입양하는 것은 신중한 고민과 선택이 필요합니다. <br> <br> 입양자의 입장에서는 \"어떤 유기견이 나랑 잘 맞을까?\" \"이 유기견이 우리 가족과 잘 어울릴까?\" 라는 질문들이 스쳐지나갈 수도 있습니다. <br> <br> 책임감 있는 유기견 주인이 되기 위한 첫 번째 단계는 유기견을 집에 데려오기도 전에 시작됩니다. <br> <br> 결정을 내리기 전에 질문 항목들을 신중하고 진지하게 평가 해주세요. <br> <br> 그러면 유기견과 함께 길고 행복한 삶을 살게 될 거에요!"
//     }]
//   }, {
//     elements: [{
//       type: "radiogroup",
//       name: "dog_experience",
//       title: "강아지를 키운 경험",
//       // isRequired: true,
//       choices: [
//         "강아지를 처음 키운다",
//         "강아지를 키우고 있다",
//         "강아지를 키운 적이 있다"
//       ]
//     }]
//   }, {
//     elements: [{
//       type: "radiogroup",
//       name: "age",
//       title: "나이대가 어떻게 되세요?",
//       // isRequired: true,
//       choices: [
//         "10대",
//         "20대",
//         "30대",
//         "40대",
//         "50대",
//         "60대 이상"
//       ]
//     }]
//   }, {
//     elements: [{
//       type: "radiogroup",
//       name: "house_type",
//       title: "주거 형태가 어떻게 되나요?",
//       // isRequired: true,
//       choices: [
//         "다가구 주택",
//         "단독주택",
//         "아파트",
//         "원룸",
//         "기타"
//       ]
//     }]
//   }, {
//     elements: [{
//       type: "radiogroup",
//       name: "only_apartment",
//       title: "아파트에 살기 적합한 강아지들 위주로 입양 하고 싶으신가요?",
//       colCount: 0,
//       // isRequired: true,
//       choices: [
//         "예",
//         "아니오"
//       ]
//     }]
//   }, {
//     elements: [{
//       type: "radiogroup",
//       name: "dog_size",
//       title: "선호 하시는 유기견의 크기가 있나요?",
//       // isRequired: true,
//       choices: [
//         "소형견",
//         "중형견",
//         "대형견"
//       ]
//     }]
//   }, {
//     elements: [{
//       type: "radiogroup",
//       name: "kids",
//       title: "아이를 키우고 있나요? (초등학생)",
//       colCount: 0,
//       // isRequired: true,
//       choices: [
//         "예",
//         "아니오"
//       ]
//     }]
//   }, {
//     elements: [{
//         type: "radiogroup",
//         name: "spend_time",
//         title: "유기견이랑 얼마나 많은 시간을 보내실 수 있나요? (주)",
//         // isRequired: true,
//         choices: [
//           "조금 : 1 ~ 5 시간",
//           "적절한 : 6 ~ 10 시간",
//           "많이 : 10+ 시간"
//         ]
//       },
//       {
//         type: "radiogroup",
//         name: "spend_type",
//         title: "시간을 같이 보낸다면 어떤 활동을 선호 하시나요?",
//         isRequired: true,
//         visibleIf: "{spend-time} = '조금 : 1 ~ 5 시간' || {spend-time} = '적절한 : 6 ~ 10 시간' || {spend-time} = '많이 : 10+ 시간' ",
//         choices: [
//           "실내 활동",
//           "둘다 왔다 갔다 한다",
//           "야외 활동"
//         ]
//       }
//     ]
//   }, {
//     elements: [{
//       type: "rating",
//       name: "bark_tolerance",
//       title: "강아지 짖는 소리를 얼마나 잘 참으시나요? (1 : 많이 안짖었으면 좋겠다 | 10 : 상관 없다)",
//       // isRequired: true,
//       rateMin: 1,
//       rateMax: 10,
//       minRateDescription: "(필요할 때만 짖는다)",
//       maxRateDescription: "(자주 짖는다)"
//     }]
//   }]
// };

/**
 * Survey Page/Questions (Question on one page)
 */
var myCss = {
  "root": "sd-root-modern",
  "rootMobile": "sd-root-modern--mobile",
  "container": "sd-container-modern",
  "header": "sd-title sd-container-modern__title",
  "body": "sd-body",
  "bodyEmpty": "sd-body sd-body--empty",
  "footer": "sd-footer sd-body__navigation sd-clearfix",
  "title": "sd-title",
  "description": "sd-description",
  "logo": "sd-logo",
  "logoImage": "sd-logo__image",
  "headerText": "sd-header__text",
  "headerClose": "sd-hidden",
  "navigationButton": "",
  "bodyNavigationButton": "sd-btn",
  "completedPage": "sd-completedpage",
  "timerRoot": "sd-body__timer",
  "navigation": {
    "complete": "sd-btn--action sd-navigation__complete-btn",
    "prev": "sd-navigation__prev-btn",
    "next": "sd-navigation__next-btn",
    "start": "sd-navigation__start-btn",
    "preview": "sd-navigation__preview-btn",
    "edit": ""
  },
  "panel": {
    "title": "sd-title sd-element__title sd-panel__title",
    "titleExpandable": "sd-element__title--expandable",
    "titleExpanded": "sd-element__title--expanded",
    "titleCollapsed": "sd-element__title--collapsed",
    "titleOnExpand": "sd-panel__title--expanded",
    "titleOnError": "sd-panel__title--error",
    "titleBar": "sd-action-title-bar",
    "description": "sd-description sd-panel__description",
    "container": "sd-element sd-element--complex sd-panel sd-row__panel",
    "withFrame": "sd-element--with-frame",
    "content": "sd-panel__content",
    "icon": "sd-panel__icon",
    "iconExpanded": "sd-panel__icon--expanded",
    "footer": "sd-panel__footer",
    "requiredText": "sd-panel__required-text",
    "header": "sd-panel__header sd-element__header sd-element__header--location-top",
    "collapsed": "sd-element--collapsed",
    "expanded": "sd-element--expanded",
    "nested": "sd-element--nested",
    "invisible": "sd-element--invisible",
    "navigationButton": ""
  },
  "paneldynamic": {
    "mainRoot": "sd-element  sd-question sd-question--paneldynamic sd-element--complex sd-question--complex sd-row__question",
    "empty": "sd-question--empty",
    "root": "sd-paneldynamic",
    "navigation": "sd-paneldynamic__navigation",
    "title": "sd-title sd-element__title sd-question__title",
    "button": "sd-action sd-paneldynamic__btn",
    "buttonRemove": "sd-action--negative sd-paneldynamic__remove-btn",
    "buttonAdd": "sd-paneldynamic__add-btn",
    "buttonPrev": "sd-paneldynamic__prev-btn sd-action--icon sd-action",
    "buttonPrevDisabled": "sd-action--disabled",
    "buttonNextDisabled": "sd-action--disabled",
    "buttonNext": "sd-paneldynamic__next-btn sd-action--icon sd-action",
    "progressContainer": "sd-paneldynamic__progress-container",
    "progress": "sd-progress",
    "progressBar": "sd-progress__bar",
    "progressText": "sd-paneldynamic__progress-text",
    "separator": "sd-paneldynamic__separator",
    "panelWrapper": "sd-paneldynamic__panel-wrapper",
    "footer": "sd-paneldynamic__footer",
    "footerButtonsContainer": "sd-paneldynamic__buttons-container",
    "panelWrapperInRow": "sd-paneldynamic__panel-wrapper--in-row",
    "progressBtnIcon": "icon-progressbuttonv2",
    "noEntriesPlaceholder": "sd-paneldynamic__placeholder sd-question__placeholder"
  },
  "progress": "sd-progress sd-body__progress",
  "progressBar": "sd-progress__bar",
  "progressText": "sd-progress__text",
  "progressButtonsContainerCenter": "sd-progress-buttons__container-center",
  "progressButtonsContainer": "sd-progress-buttons__container",
  "progressButtonsImageButtonLeft": "sd-progress-buttons__image-button-left",
  "progressButtonsImageButtonRight": "sd-progress-buttons__image-button-right",
  "progressButtonsImageButtonHidden": "sd-progress-buttons__image-button--hidden",
  "progressButtonsListContainer": "sd-progress-buttons__list-container",
  "progressButtonsList": "sd-progress-buttons__list",
  "progressButtonsListElementPassed": "sd-progress-buttons__list-element--passed",
  "progressButtonsListElementCurrent": "sd-progress-buttons__list-element--current",
  "progressButtonsListElementNonClickable": "sd-progress-buttons__list-element--nonclickable",
  "progressButtonsPageTitle": "sd-progress-buttons__page-title",
  "progressButtonsPageDescription": "sd-progress-buttons__page-description",
  "progressTextInBar": "sd-hidden",
  "page": {
    "root": "sd-page sd-body__page",
    "emptyHeaderRoot": "sd-page__empty-header",
    "title": "sd-title sd-page__title",
    "description": "sd-description sd-page__description"
  },
  "pageTitle": "sd-title sd-page__title",
  "pageDescription": "sd-description sd-page__description",
  "row": "sd-row sd-clearfix",
  "rowMultiple": "sd-row--multiple",
  "pageRow": "sd-page__row",
  "question": {
    "mainRoot": "sd-element sd-question sd-row__question",
    "flowRoot": "sd-element sd-question sd-row__question sd-row__question--flow",
    "withFrame": "sd-element--with-frame",
    "asCell": "sd-table__cell",
    "answered": "sd-question--answered",
    "header": "sd-question__header sd-element__header",
    "headerLeft": "sd-question__header--location--left",
    "headerTop": "sd-question__header--location-top sd-element__header--location-top",
    "headerBottom": "sd-question__header--location--bottom",
    "content": "sd-question__content",
    "contentLeft": "sd-question__content--left",
    "titleLeftRoot": "sd-question--left",
    "titleOnAnswer": "sd-question__title--answer",
    "titleOnError": "sd-question__title--error",
    "title": "sd-title sd-element__title sd-question__title",
    "titleExpandable": "sd-element__title--expandable",
    "titleExpanded": "sd-element__title--expanded",
    "titleCollapsed": "sd-element__title--collapsed",
    "titleBar": "sd-action-title-bar",
    "requiredText": "sd-question__required-text",
    "number": "sd-element__num",
    "description": "sd-description sd-question__description",
    "descriptionUnderInput": "sd-description sd-question__description",
    "comment": "sd-input sd-comment",
    "other": "sd-input sd-comment",
    "required": "sd-question--required",
    "titleRequired": "sd-question__title--required",
    "indent": 20,
    "footer": "sd-question__footer",
    "formGroup": "sd-question__form-group",
    "hasError": "sd-question--error",
    "collapsed": "sd-element--collapsed",
    "expanded": "sd-element--expanded",
    "nested": "sd-element--nested",
    "invisible": "sd-element--invisible",
    "composite": "sd-element--complex"
  },
  "image": {
    "mainRoot": "sd-question sd-question--image",
    "root": "sd-image",
    "image": "sd-image__image",
    "adaptive": "sd-image__image--adaptive",
    "withFrame": ""
  },
  "html": {
    "mainRoot": "sd-question sd-row__question sd-question--html",
    "root": "sd-html",
    "withFrame": ""
  },
  "error": {
    "root": "sd-question__erbox",
    "icon": "",
    "item": "",
    "tooltip": "sd-question__erbox--tooltip",
    "outsideQuestion": "sd-question__erbox--outside-question",
    "aboveQuestion": "sd-question__erbox--above-question",
    "belowQuestion": "sd-question__erbox--below-question",
    "locationTop": "sd-question__erbox--location--top",
    "locationBottom": "sd-question__erbox--location--bottom"
  },
  "checkbox": {
    "root": "sd-selectbase",
    "rootRow": "sd-selectbase--row",
    "rootMultiColumn": "sd-selectbase--multi-column",
    "item": "sd-item sd-checkbox sd-selectbase__item",
    "itemOnError": "sd-item--error",
    "itemSelectAll": "sd-checkbox--selectall",
    "itemNone": "sd-checkbox--none",
    "itemDisabled": "sd-item--disabled sd-checkbox--disabled",
    "itemChecked": "sd-item--checked sd-checkbox--checked",
    "itemHover": "sd-item--allowhover sd-checkbox--allowhover",
    "itemInline": "sd-selectbase__item--inline",
    "label": "sd-selectbase__label",
    "labelChecked": "",
    "itemControl": "sd-visuallyhidden sd-item__control sd-checkbox__control",
    "itemDecorator": "sd-item__svg sd-checkbox__svg",
    "itemSvgIconId": "#icon-v2check",
    "controlLabel": "sd-item__control-label",
    "materialDecorator": "sd-item__decorator sd-checkbox__decorator",
    "other": "sd-input sd-comment sd-selectbase__other",
    "column": "sd-selectbase__column"
  },
  "radiogroup": {
    "root": "sd-selectbase",
    "rootRow": "sd-selectbase--row",
    "rootMultiColumn": "sd-selectbase--multi-column",
    "item": "sd-item sd-radio sd-selectbase__item",
    "itemOnError": "sd-item--error",
    "itemInline": "sd-selectbase__item--inline",
    "label": "sd-selectbase__label",
    "labelChecked": "",
    "itemDisabled": "sd-item--disabled sd-radio--disabled",
    "itemChecked": "sd-item--checked sd-radio--checked",
    "itemHover": "sd-item--allowhover sd-radio--allowhover",
    "itemControl": "sd-visuallyhidden sd-item__control sd-radio__control",
    "itemDecorator": "sd-item__svg sd-radio__svg",
    "controlLabel": "sd-item__control-label",
    "materialDecorator": "sd-item__decorator sd-radio__decorator",
    "other": "sd-input sd-comment sd-selectbase__other",
    "clearButton": "",
    "column": "sd-selectbase__column"
  },
  "boolean": {
    "mainRoot": "sd-element sd-question sd-row__question sd-question--boolean",
    "root": "sv_qcbc sv_qbln sd-scrollable-container",
    "rootRadio": "sv_qcbc sv_qbln sd-scrollable-container sd-scrollable-container--compact",
    "item": "sd-boolean",
    "radioItem": "sd-item",
    "radioItemChecked": "sd-item--checked sd-radio--checked",
    "radioLabel": "sd-selectbase__label",
    "radioControlLabel": "sd-item__control-label",
    "radioFieldset": "sd-selectbase",
    "itemOnError": "sd-boolean--error",
    "control": "sd-boolean__control sd-visuallyhidden",
    "controlCheckbox": "sd-boolean__control sd-visuallyhidden",
    "itemChecked": "sd-boolean--checked",
    "itemIndeterminate": "sd-boolean--indeterminate",
    "itemDisabled": "sd-boolean--disabled",
    "label": "sd-boolean__label",
    "switch": "sd-boolean__switch",
    "disabledLabel": "sd-checkbox__label--disabled",
    "itemDecorator": "sd-checkbox__hidden",
    "materialDecorator": "sd-checkbox__rectangle",
    "itemRadioDecorator": "sd-item__svg sd-radio__svg",
    "materialRadioDecorator": "sd-item__decorator sd-radio__decorator",
    "sliderText": "sd-boolean__thumb-text",
    "slider": "sd-boolean__thumb",
    "itemControl": "sd-visuallyhidden sd-item__control sd-radio__control"
  },
  "text": {
    "root": "sd-input sd-text",
    "small": "sd-row__question--small",
    "controlDisabled": "sd-input--disabled",
    "onError": "sd-input--error"
  },
  "multipletext": {
    "root": "sd-multipletext",
    "itemLabel": "sd-multipletext__item-container sd-input",
    "itemLabelOnError": "sd-multipletext__item-container--error",
    "item": "sd-multipletext__item",
    "itemTitle": "sd-multipletext__item-title",
    "row": "sd-multipletext__row",
    "cell": "sd-multipletext__cell"
  },
  "dropdown": {
    "root": "sd-selectbase",
    "small": "sd-row__question--small",
    "selectWrapper": "",
    "other": "sd-input sd-comment sd-selectbase__other",
    "onError": "sd-input--error",
    "label": "sd-selectbase__label",
    "item": "sd-item sd-radio sd-selectbase__item",
    "itemDisabled": "sd-item--disabled sd-radio--disabled",
    "itemChecked": "sd-item--checked sd-radio--checked",
    "itemHover": "sd-item--allowhover sd-radio--allowhover",
    "itemControl": "sd-visuallyhidden sd-item__control sd-radio__control",
    "itemDecorator": "sd-item__svg sd-radio__svg",
    "cleanButton": "sd-dropdown_clean-button",
    "cleanButtonSvg": "sd-dropdown_clean-button-svg",
    "cleanButtonIconId": "icon-clear",
    "control": "sd-input sd-dropdown",
    "controlValue": "sd-dropdown__value",
    "controlDisabled": "sd-input--disabled",
    "controlEmpty": "sd-dropdown--empty",
    "controlLabel": "sd-item__control-label",
    "materialDecorator": "sd-item__decorator sd-radio__decorator"
  },
  "imagepicker": {
    "mainRoot": "sd-element sd-question sd-row__question",
    "root": "sd-selectbase sd-imagepicker",
    "rootColumn": "sd-imagepicker--column",
    "item": "sd-imagepicker__item",
    "itemOnError": "sd-imagepicker__item--error",
    "itemInline": "sd-imagepicker__item--inline",
    "itemChecked": "sd-imagepicker__item--checked",
    "itemDisabled": "sd-imagepicker__item--disabled",
    "itemHover": "sd-imagepicker__item--allowhover",
    "label": "sd-imagepicker__label",
    "itemDecorator": "sd-imagepicker__item-decorator",
    "imageContainer": "sd-imagepicker__image-container",
    "itemControl": "sd-imagepicker__control sd-visuallyhidden",
    "image": "sd-imagepicker__image",
    "itemText": "sd-imagepicker__text",
    "other": "sd-input sd-comment",
    "itemNoImage": "sd-imagepicker__no-image",
    "itemNoImageSvgIcon": "sd-imagepicker__no-image-svg",
    "itemNoImageSvgIconId": "#icon-no-image",
    "column": "sd-selectbase__column sd-imagepicker__column"
  },
  "matrix": {
    "mainRoot": "sd-element sd-question sd-row__question sd-element--complex sd-question--complex sd-question--table",
    "tableWrapper": "sd-matrix",
    "root": "sd-table sd-matrix__table",
    "rootVerticalAlignTop": "sd-table--align-top",
    "rootVerticalAlignMiddle": "sd-table--align-middle",
    "rootAlternateRows": "sd-table--alternate-rows",
    "rowError": "sd-matrix__row--error",
    "cell": "sd-table__cell sd-matrix__cell",
    "row": "sd-table__row",
    "headerCell": "sd-table__cell sd-table__cell--header",
    "rowTextCell": "sd-table__cell sd-matrix__cell sd-table__cell--row-text",
    "label": "sd-item sd-radio sd-matrix__label",
    "itemOnError": "sd-item--error",
    "itemValue": "sd-visuallyhidden sd-item__control sd-radio__control",
    "itemChecked": "sd-item--checked sd-radio--checked",
    "itemDisabled": "sd-item--disabled sd-radio--disabled",
    "itemHover": "sd-radio--allowhover",
    "materialDecorator": "sd-item__decorator sd-radio__decorator",
    "itemDecorator": "sd-item__svg sd-radio__svg",
    "cellText": "sd-matrix__text",
    "cellTextSelected": "sd-matrix__text--checked",
    "cellTextDisabled": "sd-matrix__text--disabled",
    "cellResponsiveTitle": "sd-matrix__responsive-title"
  },
  "matrixdropdown": {
    "mainRoot": "sd-element sd-question sd-row__question sd-element--complex sd-question--complex sd-question--table",
    "rootScroll": "sd-question--scroll",
    "root": "sd-table sd-matrixdropdown",
    "rootVerticalAlignTop": "sd-table--align-top",
    "rootVerticalAlignMiddle": "sd-table--align-middle",
    "rootAlternateRows": "sd-table--alternate-rows",
    "cell": "sd-table__cell",
    "row": "sd-table__row",
    "headerCell": "sd-table__cell sd-table__cell--header",
    "rowTextCell": "sd-table__cell sd-table__cell--row-text",
    "cellRequiredText": "sd-question__required-text",
    "detailButton": "sd-table__cell--detail-button",
    "detailButtonExpanded": "sd-table__cell--detail-button--expanded",
    "detailIcon": "sd-detail-panel__icon",
    "detailIconExpanded": "sd-detail-panel__icon--expanded",
    "detailIconId": "icon-expanddetail",
    "detailIconExpandedId": "icon-collapsedetail",
    "actionsCell": "sd-table__cell sd-table__cell--actions",
    "emptyCell": "sd-table__cell--empty",
    "verticalCell": "sd-table__cell--vertical",
    "cellQuestionWrapper": "sd-table__question-wrapper"
  },
  "matrixdynamic": {
    "mainRoot": "sd-element sd-question sd-row__question sd-element--complex sd-question--complex sd-question--table",
    "rootScroll": "sd-question--scroll",
    "empty": "sd-question--empty",
    "root": "sd-table sd-matrixdynamic",
    "cell": "sd-table__cell",
    "row": "sd-table__row",
    "headerCell": "sd-table__cell sd-table__cell--header",
    "rowTextCell": "sd-table__cell sd-table__cell--row-text",
    "cellRequiredText": "sd-question__required-text",
    "button": "sd-action sd-matrixdynamic__btn",
    "detailRow": "sd-table__row sd-table__row--detail",
    "detailButton": "sd-table__cell--detail-button",
    "detailButtonExpanded": "sd-table__cell--detail-button--expanded",
    "detailIcon": "sd-detail-panel__icon",
    "detailIconExpanded": "sd-detail-panel__icon--expanded",
    "detailIconId": "icon-expanddetail",
    "detailIconExpandedId": "icon-collapsedetail",
    "detailPanelCell": "sd-table__cell--detail-panel",
    "actionsCell": "sd-table__cell sd-table__cell--actions",
    "buttonAdd": "sd-matrixdynamic__add-btn",
    "buttonRemove": "sd-action--negative sd-matrixdynamic__remove-btn",
    "iconAdd": "",
    "iconRemove": "",
    "dragElementDecorator": "sd-drag-element__svg",
    "iconDragElement": "#icon-v2dragelement_16x16",
    "footer": "sd-matrixdynamic__footer",
    "emptyRowsSection": "sd-matrixdynamic__placeholder sd-question__placeholder",
    "iconDrag": "sv-matrixdynamic__drag-icon",
    "ghostRow": "sv-matrix-row--drag-drop-ghost-mod",
    "emptyCell": "sd-table__cell--empty",
    "verticalCell": "sd-table__cell--vertical",
    "cellQuestionWrapper": "sd-table__question-wrapper"
  },
  "rating": {
    "rootDropdown": "sd-scrollable-container sd-scrollable-container--compact sd-selectbase",
    "root": "sd-scrollable-container sd-rating",
    "rootWrappable": "sd-scrollable-container sd-rating sd-rating--wrappable",
    "item": "sd-rating__item",
    "itemOnError": "sd-rating__item--error",
    "itemHover": "sd-rating__item--allowhover",
    "selected": "sd-rating__item--selected",
    "minText": "sd-rating__item-text sd-rating__min-text",
    "itemText": "sd-rating__item-text",
    "maxText": "sd-rating__item-text sd-rating__max-text",
    "itemDisabled": "sd-rating__item--disabled",
    "control": "sd-input sd-dropdown",
    "controlValue": "sd-dropdown__value",
    "controlDisabled": "sd-input--disabled",
    "controlEmpty": "sd-dropdown--empty",
    "onError": "sd-input--error"
  },
  "comment": {
    "root": "sd-input sd-comment",
    "small": "sd-row__question--small",
    "controlDisabled": "sd-input--disabled",
    "onError": "sd-input--error"
  },
  "expression": "",
  "file": {
    "root": "sd-file",
    "other": "sd-input sd-comment",
    "placeholderInput": "sd-visuallyhidden",
    "preview": "sd-file__preview",
    "fileSign": "",
    "fileList": "sd-file__list",
    "fileSignBottom": "sd-file__sign",
    "fileDecorator": "sd-file__decorator",
    "onError": "sd-file__decorator--error",
    "fileDecoratorDrag": "sd-file__decorator--drag",
    "fileInput": "sd-visuallyhidden",
    "noFileChosen": "sd-description sd-file__no-file-chosen",
    "chooseFile": "sd-file__choose-btn",
    "chooseFileAsText": "sd-action sd-file__choose-btn--text",
    "chooseFileAsTextDisabled": "sd-action--disabled",
    "chooseFileAsIcon": "sd-context-btn sd-file__choose-btn--icon",
    "chooseFileIconId": "icon-choosefile",
    "disabled": "sd-file__choose-btn--disabled",
    "removeButton": "sd-context-btn sd-context-btn--negative sd-file__btn sd-file__clean-btn",
    "removeButtonBottom": "",
    "removeButtonIconId": "icon-clear",
    "removeFile": "sd-hidden",
    "removeFileSvg": "",
    "removeFileSvgIconId": "icon-delete",
    "wrapper": "sd-file__wrapper",
    "defaultImage": "sd-file__default-image",
    "defaultImageIconId": "icon-defaultfile",
    "leftIconId": "icon-arrowleft",
    "rightIconId": "icon-arrowright",
    "removeFileButton": "sd-context-btn sd-context-btn--negative sd-file__remove-file-button",
    "dragAreaPlaceholder": "sd-file__drag-area-placeholder",
    "imageWrapper": "sd-file__image-wrapper",
    "single": "sd-file--single",
    "singleImage": "sd-file--single-image",
    "mobile": "sd-file--mobile"
  },
  "signaturepad": {
    "mainRoot": "sd-element sd-question sd-question--signature sd-row__question",
    "root": "sd-signaturepad sjs_sp_container",
    "small": "sd-row__question--small",
    "controls": "sjs_sp_controls sd-signaturepad__controls",
    "placeholder": "sjs_sp_placeholder",
    "clearButton": "sjs_sp_clear sd-context-btn sd-context-btn--negative sd-signaturepad__clear",
    "clearButtonIconId": "icon-clear"
  },
  "saveData": {
    "root": "",
    "saving": "",
    "error": "",
    "success": "",
    "saveAgainButton": ""
  },
  "window": {
    "root": "sv_window",
    "body": "sv_window_content",
    "header": {
      "root": "sv_window_title",
      "title": "",
      "button": "",
      "buttonExpanded": "",
      "buttonCollapsed": ""
    }
  },
  "ranking": {
    "root": "sv-ranking",
    "rootMobileMod": "sv-ranking--mobile",
    "rootDragMod": "sv-ranking--drag",
    "rootDisabled": "sd-ranking--disabled",
    "rootDesignMode": "sv-ranking--design-mode",
    "item": "sv-ranking-item",
    "itemContent": "sv-ranking-item__content sd-ranking-item__content",
    "itemIndex": "sv-ranking-item__index",
    "controlLabel": "sv-ranking-item__text",
    "itemGhostNode": "sv-ranking-item__ghost",
    "itemIconContainer": "sv-ranking-item__icon-container",
    "itemIcon": "sv-ranking-item__icon",
    "itemIconHoverMod": "sv-ranking-item__icon--hover",
    "itemIconFocusMod": "sv-ranking-item__icon--focus",
    "itemGhostMod": "sv-ranking-item--ghost",
    "itemDragMod": "sv-ranking--drag",
    "itemOnError": "sv-ranking-item--error"
  },
  "buttongroup": {
    "root": "sv-button-group",
    "item": "sv-button-group__item",
    "itemIcon": "sv-button-group__item-icon",
    "itemDecorator": "sv-button-group__item-decorator",
    "itemCaption": "sv-button-group__item-caption",
    "itemHover": "sv-button-group__item--hover",
    "itemSelected": "sv-button-group__item--selected",
    "itemDisabled": "sv-button-group__item--disabled",
    "itemControl": "sv-visuallyhidden"
  },
  "actionBar": {
    "root": "sd-action-bar",
    "item": "sd-action",
    "itemPressed": "sd-action--pressed",
    "itemAsIcon": "sd-action--icon",
    "itemIcon": "sd-action__icon",
    "itemTitle": "sd-action__title"
  },
  "variables": {
    "mobileWidth": "--sd-mobile-width",
    "imagepickerGapBetweenItems": "--sd-imagepicker-gap",
    "themeMark": "--sv-defaultV2-mark"
  },
  "tagbox": {
    "root": "sd-selectbase",
    "small": "sd-row__question--small",
    "selectWrapper": "",
    "other": "sd-input sd-comment sd-selectbase__other",
    "onError": "sd-input--error",
    "label": "sd-selectbase__label",
    "item": "sd-item sd-radio sd-selectbase__item",
    "itemDisabled": "sd-item--disabled sd-radio--disabled",
    "itemChecked": "sd-item--checked sd-radio--checked",
    "itemHover": "sd-item--allowhover sd-radio--allowhover",
    "itemControl": "sd-visuallyhidden sd-item__control sd-radio__control",
    "itemDecorator": "sd-item__svg sd-radio__svg",
    "cleanButton": "sd-tagbox_clean-button sd-dropdown_clean-button",
    "cleanButtonSvg": "sd-tagbox_clean-button-svg sd-dropdown_clean-button-svg",
    "cleanButtonIconId": "icon-clear",
    "cleanItemButton": "sd-tagbox-item_clean-button",
    "cleanItemButtonSvg": "sd-tagbox-item_clean-button-svg",
    "cleanItemButtonIconId": "icon-clear_16x16",
    "control": "sd-input sd-tagbox sd-dropdown",
    "controlValue": "sd-tagbox__value sd-dropdown__value",
    "controlDisabled": "sd-input--disabled",
    "controlEmpty": "sd-dropdown--empty sd-tagbox--empty",
    "controlLabel": "sd-item__control-label",
    "materialDecorator": "sd-item__decorator sd-radio__decorator"
  }
};
var json = {
  firstPageIsStarted: false,
  title: "나에게 맞는 AI 기반 유기견 추천!",
  description: "모든 질문에 답을 하면 귀하에게 적합한 유기견(종)을 찾아드립니다!",
  startSurveyText: "나에게 맞는 유기견 찾기!",
  showProgressBar: "top",
  locale: "ko",
  pages: [{
    elements: [{
        type: "html",
        html: "나에게 맞는 유기견을 입양하는 것은 신중한 고민과 선택이 필요합니다. <br> <br> 입양자의 입장에서는 \"어떤 유기견이 나랑 잘 맞을까?\" \"이 유기견이 우리 가족과 잘 어울릴까?\" 라는 질문들이 스쳐지나갈 수도 있습니다. <br> <br> 책임감 있는 유기견 주인이 되기 위한 첫 번째 단계는 유기견을 집에 데려오기도 전에 시작됩니다. <br> <br> 결정을 내리기 전에 질문 항목들을 신중하고 진지하게 평가 해주세요. <br> <br> 그러면 유기견과 함께 길고 행복한 삶을 살게 될 거에요! <br><br><br>"
      },
      {
        type: "radiogroup",
        name: "user_age",
        title: "나이대가 어떻게 되세요?",
        // isRequired: true,
        choices: [{
            "value": "20대이하",
            "text": "20대 이하"
          },
          {
            "value": "30대",
            "text": "30대"
          },
          {
            "value": "40대",
            "text": "40대"
          },
          {
            "value": "50대",
            "text": "50대"
          },
          {
            "value": "60대이상",
            "text": "60대 이상"
          }
        ]
      },
      {
        type: "radiogroup",
        name: "user_sex",
        title: "성별이 어떻게 되세요?",
        // isRequired: true,
        choices: [
          "남성",
          "여성",
          "기타"
        ]
      },
      {
        type: "radiogroup",
        name: "user_house_type",
        title: "주거 형태가 어떻게 되나요?",
        // isRequired: true,
        choices: [{
            "value": "다가구주택",
            "text": "다가구 주택"
          },
          {
            "value": "단독주택",
            "text": "단독주택"
          },
          {
            "value": "아파트",
            "text": "아파트"
          },
          {
            "value": "원룸",
            "text": "원룸"
          },
          {
            "value": "기타",
            "text": "기타"
          }
        ]
      },
      {
        type: "radiogroup",
        name: "user_dog_experience",
        title: "강아지를 키운 경험",
        // isRequired: true,
        choices: [
          "강아지를 처음 키운다",
          "강아지를 키우고 있다",
          "강아지를 키운 적이 있다"
        ]
      },
      {
        type: "radiogroup",
        name: "neighbor_agreement",
        title: "주민 동의 여부",
        // isRequired: true,
        choices: [
          "예",
          "아니오"
        ]
      },
      {
        type: "radiogroup",
        name: "user_family_size",
        title: "가족 구성원은 어떻게 되나요?",
        // isRequired: true,
        choices: [
          "1인",
          "2인",
          "3인",
          "4인",
          "5인 이상"
        ]
      },
      {
        type: "radiogroup",
        name: "user_kids",
        title: "아이를 키우고 있나요? (초등학생)",
        colCount: 0,
        // isRequired: true,
        choices: [
          "예",
          "아니오"
        ]
      },
      {
        type: "radiogroup",
        name: "dog_size",
        title: "선호 하시는 유기견의 크기가 있나요?",
        // isRequired: true,
        choices: [
          "소형견",
          "중형견",
          "대형견"
        ]
      },
      {
        type: "radiogroup",
        name: "shedding_level",
        title: "털날림 정도",
        colCount: 0,
        // isRequired: true,
        choices: [
          "예",
          "아니오"
        ]
      },
      {
        type: "rating",
        name: "bark_tolerance",
        title: "강아지 짖는 소리를 얼마나 잘 참으시나요? (1 : 많이 안짖었으면 좋겠다 | 10 : 상관 없다)",
        // isRequired: true,
        rateMin: 1,
        rateMax: 10,
        minRateDescription: "(필요할 때만 짖는다)",
        maxRateDescription: "(자주 짖는다)"
      },
      {
        type: "radiogroup",
        name: "spend_time",
        title: "유기견이랑 얼마나 많은 시간을 보내실 수 있나요? (주)",
        // isRequired: true,
        choices: [
          "조금 : 1 ~ 5 시간",
          "적절한 : 6 ~ 10 시간",
          "많이 : 10+ 시간"
        ]
      },
      {
        type: "radiogroup",
        name: "spend_type",
        title: "시간을 같이 보낸다면 어떤 활동을 선호 하시나요?",
        // isRequired: true,
        choices: [
          "실내 활동",
          "둘다 왔다 갔다 한다",
          "야외 활동"
        ]
      },
      {
        type: "radiogroup",
        name: "dog_sex",
        title: "어떤 성별의 강아지를 원하시나요?",
        // isRequired: true,
        choices: [
          "수컷",
          "암컷",
          "상관 없음"
        ]
      },
      {
        type: "radiogroup",
        name: "dog_environment",
        title: "반려견이 지낼 장소는 어디 입니까?",
        colCount: 0,
        // isRequired: true,
        choices: [
          "실내",
          "실외",
          "실내외 둘다",
          "별도의 공간 (보일러실, 농장, 베란다 등)"
        ]
      },
      {
        type: "radiogroup",
        name: "dog_support_agreement",
        title: "양육비 동의 여부",
        colCount: 0,
        // isRequired: true,
        choices: [
          "예",
          "아니오"
        ]
      },
      {
        type: "radiogroup",
        name: "dog_health_agreement",
        title: "유기견 건강 인지 여부",
        colCount: 0,
        // isRequired: true,
        choices: [
          "예",
          "아니오"
        ]
      },
      {
        type: "radiogroup",
        name: "want_dog_age",
        title: "원하시는 유기견 나이",
        colCount: 0,
        // isRequired: true,
        choices: [
          "2022(년생)",
          "2021(년생)"
        ]
      },
      {
        type: "radiogroup",
        name: "neuter_yn",
        title: "유기견 중성화 여부",
        colCount: 0,
        // isRequired: true,
        choices: [{
            "value": "Y",
            "text": "예"
          },
          {
            "value": "N",
            "text": "아니오"
          }
        ]
      }
    ]
  }]
};

/**
 * Targeting HTML Survey div to JS
 */
window.survey = new Survey.Model(json);

$("#surveyElement").Survey({
  model: survey,
  css: myCss
});

/**
 * Actions when survey is complete
 */
survey.onComplete.add(function (sender) {
  var answer_give = JSON.stringify(sender.data) // User survey answer in JSON

  /**
   * Sending user answer to server
   */
  $.ajax({
    type: "POST",
    contentType: "application/json",
    url: "/survey/result",
    dataType: "json",
    data: answer_give,
    success: function (response) {
      alert("보내기 성공")
      alert(response)
      console.log(response)
    }
  })
});

/**
 * Survey Animation
 */
function animate(animitionType, duration) {
  if (!duration)
    duration = 1000;

  var element = document.getElementById("surveyElement");
  $(element).velocity(animitionType, {
    duration: duration
  });
}
var doAnimantion = true;
survey.onCurrentPageChanging.add(function (sender, options) {
  if (!doAnimantion)
    return;

  options.allowChanging = false;
  setTimeout(function () {
    doAnimantion = false;
    sender.currentPage = options.newCurrentPage;
    doAnimantion = true;
  }, 500);
  animate("slideUp", 500);
});
survey.onCurrentPageChanged.add(function (sender) {
  animate("slideDown", 500);
});
survey.onCompleting.add(function (sender, options) {
  if (!doAnimantion)
    return;

  options.allowComplete = false;
  setTimeout(function () {
    doAnimantion = false;
    sender.doComplete();
    doAnimantion = true;
  }, 500);
  animate("slideUp", 500);
});
animate("slideDown", 1000);

/**
 * AOS JS Initiation
 */
window.addEventListener('load', () => {
  AOS.init({
    duration: 1000,
    easing: 'ease-in-out',
    once: false,
    mirror: false
  })
})

/**
 * Navbar box-shadow
 */
function scrollHeader() {
  const nav = document.getElementById('header')
  // When the scroll is greater than 200 viewport height, add the scroll-header class to the header tag
  if (this.scrollY >= 80) nav.classList.add('scroll-header');
  else nav.classList.remove('scroll-header')
}
window.addEventListener('scroll', scrollHeader)