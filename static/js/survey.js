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

// const SURVEY_ID = 1;

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
        name: "dog_experience",
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
        name: "age",
        title: "나이대가 어떻게 되세요?",
        // isRequired: true,
        choices: [
          "10대",
          "20대",
          "30대",
          "40대",
          "50대",
          "60대 이상"
        ]
      },
      {
        type: "radiogroup",
        name: "house_type",
        title: "주거 형태가 어떻게 되나요?",
        // isRequired: true,
        choices: [
          "다가구 주택",
          "단독주택",
          "아파트",
          "원룸",
          "기타"
        ]
      },
      {
        type: "radiogroup",
        name: "only_apartment",
        title: "아파트에 살기 적합한 강아지들 위주로 입양 하고 싶으신가요?",
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
        name: "kids",
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
        isRequired: true,
        visibleIf: "{spend-time} = '조금 : 1 ~ 5 시간' || {spend-time} = '적절한 : 6 ~ 10 시간' || {spend-time} = '많이 : 10+ 시간' ",
        choices: [
          "실내 활동",
          "둘다 왔다 갔다 한다",
          "야외 활동"
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
      }
    ]
  }]
};

/**
 * Showing Alert To User
 */
// function alertResults(sender) {
//   const results = JSON.stringify(sender.data);
//   alert(results);
//   // saveSurveyResults(
//   //     "https://your-web-service.com/" + SURVEY_ID,
//   //     sender.data
//   // )
// }

// survey.onComplete.add(alertResults);

/**
 * Targeting HTML Survey div to JS
 */
window.survey = new Survey.Model(json);

$("#surveyElement").Survey({
  model: survey
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
    url: "/survey",
    dataType: "json",
    data: answer_give,
    success: function (response) {
      alert("보내기 성공")

      var recommend_info = response // Storing dog info from DB

      /**
       * Storing various dog infos as variables
       */
      var breed_name = `${recommend_info.breed_name} ${recommend_info.breed_name_kr}` // 종 이름 (영어 + 한국어어
      var breed_desc = recommend_info.dog_info_json.dog_description // 종 설명
      var breed_img = recommend_info.dog_info_json.dog_img // 종 사진
      var breed_cost = recommend_info.dog_info_json.dog_cost // 키우는 비용
      var recommend_reason = recommend_info.dog_info_json.recommend_reason // 추천 이유

      /**
       * Storing user survey answers as a variable
       */
      var survey_dog_experience = sender.data.dog_experience // Answer 1
      var survey_age = sender.data.age // Answer 2
      var survey_house_type = sender.data.house_type // Answer 3
      var survey_only_apartment = sender.data.only_apartment // Answer 4
      var survey_dog_size = sender.data.dog_size // Answer 5
      var survey_kids = sender.data.kids // Answer 6
      var survey_spend_time = sender.data.spend_time // Answer 7
      var survey_spend_type = sender.data.spend_type // Answer 8
      var survey_bark_tolerance = sender.data.bark_tolerance // Answer 9

      /**
       * Filling the survey result page based on recommended breed and user's answer
       */
      document.querySelector('.recommended-dog-title').innerHTML = `당신의 강아지 추천은: ${breed_name}`
      document.querySelector('.recommended-dog-image').innerHTML = breed_img
      document.querySelector('.recommended-dog-description').innerHTML = breed_desc
      document.querySelector('.recommended-dog-answer-title').innerHTML = "귀하께서 알려주신 정보"
      document.querySelector('.recommended-dog-answer-1').innerHTML = survey_dog_experience
      document.querySelector('.recommended-dog-answer-2').innerHTML = survey_age
      document.querySelector('.recommended-dog-answer-3').innerHTML = survey_house_type
      document.querySelector('.recommended-dog-answer-4').innerHTML = survey_only_apartment
      document.querySelector('.recommended-dog-answer-5').innerHTML = survey_dog_size
      document.querySelector('.recommended-dog-answer-6').innerHTML = survey_kids
      document.querySelector('.recommended-dog-answer-7').innerHTML = survey_spend_time
      document.querySelector('.recommended-dog-answer-8').innerHTML = survey_spend_type
      document.querySelector('.recommended-dog-answer-9').innerHTML = survey_bark_tolerance
      document.querySelector('.recommended-dog-info-title').innerHTML = `${breed_name} 정보`
      document.querySelector('.recommended-dog-reason').innerHTML = recommend_reason
      document.querySelector('.recommended-dog-traits').innerHTML = "특징~ 몸무게 5kg / 키: 20cm / 기타 등등 . . ."
      document.querySelector('.recommended-dog-cost').innerHTML = breed_cost
      document.querySelector('.recommended-dog-btn').innerHTML = "현재 공고중인 유기견 찾기"
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