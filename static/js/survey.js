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
  window.location.href = "/abandoned-dogs" // Move to page
}

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
        name: "user_age",
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
        name: "a_adaptability",
        title: "a_adaptability",
        colCount: 0,
        // isRequired: true,
        choices: [{
            "value": "1",
            "text": "1"
          },
          {
            "value": "2",
            "text": "2"
          },
          {
            "value": "3",
            "text": "3"
          },
          {
            "value": "4",
            "text": "4"
          },
          {
            "value": "5",
            "text": "5"
          }
        ]
      },
      {
        type: "radiogroup",
        name: "a1_adapts_well_to_apartment_living",
        title: "a1_adapts_well_to_apartment_living",
        colCount: 0,
        // isRequired: true,
        choices: [{
            "value": "1",
            "text": "1"
          },
          {
            "value": "2",
            "text": "2"
          },
          {
            "value": "3",
            "text": "3"
          },
          {
            "value": "4",
            "text": "4"
          },
          {
            "value": "5",
            "text": "5"
          }
        ]
      },
      {
        type: "radiogroup",
        name: "a2_good_for_novice_owners",
        title: "a2_good_for_novice_owners",
        colCount: 0,
        // isRequired: true,
        choices: [{
            "value": "1",
            "text": "1"
          },
          {
            "value": "2",
            "text": "2"
          },
          {
            "value": "3",
            "text": "3"
          },
          {
            "value": "4",
            "text": "4"
          },
          {
            "value": "5",
            "text": "5"
          }
        ]
      },
      {
        type: "radiogroup",
        name: "a3_sensitivity_level",
        title: "a3_sensitivity_level",
        colCount: 0,
        // isRequired: true,
        choices: [{
            "value": "1",
            "text": "1"
          },
          {
            "value": "2",
            "text": "2"
          },
          {
            "value": "3",
            "text": "3"
          },
          {
            "value": "4",
            "text": "4"
          },
          {
            "value": "5",
            "text": "5"
          }
        ]
      },
      {
        type: "radiogroup",
        name: "a4_tolerates_being_alone",
        title: "a4_tolerates_being_alone",
        colCount: 0,
        // isRequired: true,
        choices: [{
            "value": "1",
            "text": "1"
          },
          {
            "value": "2",
            "text": "2"
          },
          {
            "value": "3",
            "text": "3"
          },
          {
            "value": "4",
            "text": "4"
          },
          {
            "value": "5",
            "text": "5"
          }
        ]
      },
      {
        type: "radiogroup",
        name: "a5_tolerates_cold_weather",
        title: "a5_tolerates_cold_weather",
        colCount: 0,
        // isRequired: true,
        choices: [{
            "value": "1",
            "text": "1"
          },
          {
            "value": "2",
            "text": "2"
          },
          {
            "value": "3",
            "text": "3"
          },
          {
            "value": "4",
            "text": "4"
          },
          {
            "value": "5",
            "text": "5"
          }
        ]
      },
      {
        type: "radiogroup",
        name: "a6_tolerates_hot_weather",
        title: "a6_tolerates_hot_weather",
        colCount: 0,
        // isRequired: true,
        choices: [{
            "value": "1",
            "text": "1"
          },
          {
            "value": "2",
            "text": "2"
          },
          {
            "value": "3",
            "text": "3"
          },
          {
            "value": "4",
            "text": "4"
          },
          {
            "value": "5",
            "text": "5"
          }
        ]
      },
      {
        type: "radiogroup",
        name: "b_all_around_friendliness",
        title: "b_all_around_friendliness",
        colCount: 0,
        // isRequired: true,
        choices: [{
            "value": "1",
            "text": "1"
          },
          {
            "value": "2",
            "text": "2"
          },
          {
            "value": "3",
            "text": "3"
          },
          {
            "value": "4",
            "text": "4"
          },
          {
            "value": "5",
            "text": "5"
          }
        ]
      },
      {
        type: "radiogroup",
        name: "b1_affectionate_with_family",
        title: "b1_affectionate_with_family",
        colCount: 0,
        // isRequired: true,
        choices: [{
            "value": "1",
            "text": "1"
          },
          {
            "value": "2",
            "text": "2"
          },
          {
            "value": "3",
            "text": "3"
          },
          {
            "value": "4",
            "text": "4"
          },
          {
            "value": "5",
            "text": "5"
          }
        ]
      },
      {
        type: "radiogroup",
        name: "b2_incredibly_kid_friendly_dogs",
        title: "b2_incredibly_kid_friendly_dogs",
        colCount: 0,
        // isRequired: true,
        choices: [{
            "value": "1",
            "text": "1"
          },
          {
            "value": "2",
            "text": "2"
          },
          {
            "value": "3",
            "text": "3"
          },
          {
            "value": "4",
            "text": "4"
          },
          {
            "value": "5",
            "text": "5"
          }
        ]
      },
      {
        type: "radiogroup",
        name: "b3_dog_friendly",
        title: "b3_dog_friendly",
        colCount: 0,
        // isRequired: true,
        choices: [{
            "value": "1",
            "text": "1"
          },
          {
            "value": "2",
            "text": "2"
          },
          {
            "value": "3",
            "text": "3"
          },
          {
            "value": "4",
            "text": "4"
          },
          {
            "value": "5",
            "text": "5"
          }
        ]
      },
      {
        type: "radiogroup",
        name: "b4_friendly_toward_strangers",
        title: "b4_friendly_toward_strangers",
        colCount: 0,
        // isRequired: true,
        choices: [{
            "value": "1",
            "text": "1"
          },
          {
            "value": "2",
            "text": "2"
          },
          {
            "value": "3",
            "text": "3"
          },
          {
            "value": "4",
            "text": "4"
          },
          {
            "value": "5",
            "text": "5"
          }
        ]
      },
      {
        type: "radiogroup",
        name: "c_health_grooming",
        title: "c_health_grooming",
        colCount: 0,
        // isRequired: true,
        choices: [{
            "value": "1",
            "text": "1"
          },
          {
            "value": "2",
            "text": "2"
          },
          {
            "value": "3",
            "text": "3"
          },
          {
            "value": "4",
            "text": "4"
          },
          {
            "value": "5",
            "text": "5"
          }
        ]
      },
      {
        type: "radiogroup",
        name: "c1_amount_of_shedding",
        title: "c1_amount_of_shedding",
        colCount: 0,
        // isRequired: true,
        choices: [{
            "value": "1",
            "text": "1"
          },
          {
            "value": "2",
            "text": "2"
          },
          {
            "value": "3",
            "text": "3"
          },
          {
            "value": "4",
            "text": "4"
          },
          {
            "value": "5",
            "text": "5"
          }
        ]
      },
      {
        type: "radiogroup",
        name: "c2_drooling_potential",
        title: "c2_drooling_potential",
        colCount: 0,
        // isRequired: true,
        choices: [{
            "value": "1",
            "text": "1"
          },
          {
            "value": "2",
            "text": "2"
          },
          {
            "value": "3",
            "text": "3"
          },
          {
            "value": "4",
            "text": "4"
          },
          {
            "value": "5",
            "text": "5"
          }
        ]
      },
      {
        type: "radiogroup",
        name: "c3_easy_to_groom",
        title: "c3_easy_to_groom",
        colCount: 0,
        // isRequired: true,
        choices: [{
            "value": "1",
            "text": "1"
          },
          {
            "value": "2",
            "text": "2"
          },
          {
            "value": "3",
            "text": "3"
          },
          {
            "value": "4",
            "text": "4"
          },
          {
            "value": "5",
            "text": "5"
          }
        ]
      },
      {
        type: "radiogroup",
        name: "c4_general_health",
        title: "c4_general_health",
        colCount: 0,
        // isRequired: true,
        choices: [{
            "value": "1",
            "text": "1"
          },
          {
            "value": "2",
            "text": "2"
          },
          {
            "value": "3",
            "text": "3"
          },
          {
            "value": "4",
            "text": "4"
          },
          {
            "value": "5",
            "text": "5"
          }
        ]
      },
      {
        type: "radiogroup",
        name: "c5_potential_for_weight_gain",
        title: "c5_potential_for_weight_gain",
        colCount: 0,
        // isRequired: true,
        choices: [{
            "value": "1",
            "text": "1"
          },
          {
            "value": "2",
            "text": "2"
          },
          {
            "value": "3",
            "text": "3"
          },
          {
            "value": "4",
            "text": "4"
          },
          {
            "value": "5",
            "text": "5"
          }
        ]
      },
      {
        type: "radiogroup",
        name: "c6_size",
        title: "c6_size",
        colCount: 0,
        // isRequired: true,
        choices: [{
            "value": "1",
            "text": "1"
          },
          {
            "value": "2",
            "text": "2"
          },
          {
            "value": "3",
            "text": "3"
          },
          {
            "value": "4",
            "text": "4"
          },
          {
            "value": "5",
            "text": "5"
          }
        ]
      },
      {
        type: "radiogroup",
        name: "d_trainability",
        title: "d_trainability",
        colCount: 0,
        // isRequired: true,
        choices: [{
            "value": "1",
            "text": "1"
          },
          {
            "value": "2",
            "text": "2"
          },
          {
            "value": "3",
            "text": "3"
          },
          {
            "value": "4",
            "text": "4"
          },
          {
            "value": "5",
            "text": "5"
          }
        ]
      },
      {
        type: "radiogroup",
        name: "d1_easy_to_train",
        title: "d1_easy_to_train",
        colCount: 0,
        // isRequired: true,
        choices: [{
            "value": "1",
            "text": "1"
          },
          {
            "value": "2",
            "text": "2"
          },
          {
            "value": "3",
            "text": "3"
          },
          {
            "value": "4",
            "text": "4"
          },
          {
            "value": "5",
            "text": "5"
          }
        ]
      },
      {
        type: "radiogroup",
        name: "d2_intelligence",
        title: "d2_intelligence",
        colCount: 0,
        // isRequired: true,
        choices: [{
            "value": "1",
            "text": "1"
          },
          {
            "value": "2",
            "text": "2"
          },
          {
            "value": "3",
            "text": "3"
          },
          {
            "value": "4",
            "text": "4"
          },
          {
            "value": "5",
            "text": "5"
          }
        ]
      },
      {
        type: "radiogroup",
        name: "d3_potential_for_mouthiness",
        title: "d3_potential_for_mouthiness",
        colCount: 0,
        // isRequired: true,
        choices: [{
            "value": "1",
            "text": "1"
          },
          {
            "value": "2",
            "text": "2"
          },
          {
            "value": "3",
            "text": "3"
          },
          {
            "value": "4",
            "text": "4"
          },
          {
            "value": "5",
            "text": "5"
          }
        ]
      },
      {
        type: "radiogroup",
        name: "d4_prey_drive",
        title: "d4_prey_drive",
        colCount: 0,
        // isRequired: true,
        choices: [{
            "value": "1",
            "text": "1"
          },
          {
            "value": "2",
            "text": "2"
          },
          {
            "value": "3",
            "text": "3"
          },
          {
            "value": "4",
            "text": "4"
          },
          {
            "value": "5",
            "text": "5"
          }
        ]
      },
      {
        type: "radiogroup",
        name: "d5_tendency_to_bark_or_howl",
        title: "d5_tendency_to_bark_or_howl",
        colCount: 0,
        // isRequired: true,
        choices: [{
            "value": "1",
            "text": "1"
          },
          {
            "value": "2",
            "text": "2"
          },
          {
            "value": "3",
            "text": "3"
          },
          {
            "value": "4",
            "text": "4"
          },
          {
            "value": "5",
            "text": "5"
          }
        ]
      },
      {
        type: "radiogroup",
        name: "d6_wanderlust_potential",
        title: "d6_wanderlust_potential",
        colCount: 0,
        // isRequired: true,
        choices: [{
            "value": "1",
            "text": "1"
          },
          {
            "value": "2",
            "text": "2"
          },
          {
            "value": "3",
            "text": "3"
          },
          {
            "value": "4",
            "text": "4"
          },
          {
            "value": "5",
            "text": "5"
          }
        ]
      },
      {
        type: "radiogroup",
        name: "e_exercise_needs",
        title: "e_exercise_needs",
        colCount: 0,
        // isRequired: true,
        choices: [{
            "value": "1",
            "text": "1"
          },
          {
            "value": "2",
            "text": "2"
          },
          {
            "value": "3",
            "text": "3"
          },
          {
            "value": "4",
            "text": "4"
          },
          {
            "value": "5",
            "text": "5"
          }
        ]
      },
      {
        type: "radiogroup",
        name: "e1_energy_level",
        title: "e1_energy_level",
        colCount: 0,
        // isRequired: true,
        choices: [{
            "value": "1",
            "text": "1"
          },
          {
            "value": "2",
            "text": "2"
          },
          {
            "value": "3",
            "text": "3"
          },
          {
            "value": "4",
            "text": "4"
          },
          {
            "value": "5",
            "text": "5"
          }
        ]
      },
      {
        type: "radiogroup",
        name: "e2_intensity",
        title: "e2_intensity",
        colCount: 0,
        // isRequired: true,
        choices: [{
            "value": "1",
            "text": "1"
          },
          {
            "value": "2",
            "text": "2"
          },
          {
            "value": "3",
            "text": "3"
          },
          {
            "value": "4",
            "text": "4"
          },
          {
            "value": "5",
            "text": "5"
          }
        ]
      },
      {
        type: "radiogroup",
        name: "e3_exercise_needs",
        title: "e3_exercise_needs",
        colCount: 0,
        // isRequired: true,
        choices: [{
            "value": "1",
            "text": "1"
          },
          {
            "value": "2",
            "text": "2"
          },
          {
            "value": "3",
            "text": "3"
          },
          {
            "value": "4",
            "text": "4"
          },
          {
            "value": "5",
            "text": "5"
          }
        ]
      },
      {
        type: "radiogroup",
        name: "e4_potential_for_playfulness",
        title: "e4_potential_for_playfulness",
        colCount: 0,
        // isRequired: true,
        choices: [{
            "value": "1",
            "text": "1"
          },
          {
            "value": "2",
            "text": "2"
          },
          {
            "value": "3",
            "text": "3"
          },
          {
            "value": "4",
            "text": "4"
          },
          {
            "value": "5",
            "text": "5"
          }
        ]
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