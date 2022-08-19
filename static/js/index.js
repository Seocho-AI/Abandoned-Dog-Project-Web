/**
 * Navbar links active state on scroll
 */
let navbarlinks = document.querySelectorAll('#dog-navbar a');

function navbarlinksActive() {
  navbarlinks.forEach(navbarlink => {

    if (!navbarlink.hash) return;

    let section = document.querySelector(navbarlink.hash);
    if (!section) return;

    let position = window.scrollY + 200;

    if (position >= section.offsetTop && position <= (section.offsetTop + section.offsetHeight)) {
      navbarlink.classList.add('active');
    } else {
      navbarlink.classList.remove('active');
    }
  })
}
window.addEventListener('load', navbarlinksActive);
document.addEventListener('scroll', navbarlinksActive);

/**
 * Navbar box-shadow
 */
function scrollHeader(){
  const nav = document.getElementById('header')
  // When the scroll is greater than 200 viewport height, add the scroll-header class to the header tag
  if(this.scrollY >= 80) nav.classList.add('scroll-header'); else nav.classList.remove('scroll-header')
}
window.addEventListener('scroll', scrollHeader)

/**
 * Move to Find Dog page
 */
document.getElementById("abandoned-dog-page-btn").addEventListener("click", moveToAbandonedDogPage)

function moveToAbandonedDogPage() {
  window.location.href = "/abandoned-dogs" // Move to result page
}

/**
 * Move to Survey page
 */
document.getElementById("survey-page-btn").addEventListener("click", moveToSurveyPage)

function moveToSurveyPage() {
  window.location.href = "/survey" // Move to result page
}

// {
//   "dog_description": "구약성서에 나오는 노아의 방주를 탔던 개라는 설이 있을 정도로 역사가 오래된 개다. 중동지역이 원산지이며 교역로를 따라 기원전 5000년경에 아프가니스탄에 정착하여 영양, 가젤, 늑대 등의 사냥에 이용되었다. 기원전 6세기경에 제작된 그리스의 태피스트리에도 등장하며 제1차 세계대전 이후부터 서구 세계에 알려지기 시작해 1886년 영국에 반입되었고 1926년 미국에 소개되었다. 뾰족한 얼굴과 비단 같은 긴 털, 아먼드 모양의 동양적인 두 눈은 귀족의 풍모를 풍긴다. 등은 곧게 펴며 근육질의 몸은 아주 튼튼하다. 온몸을 뒤덮은 털은 아프가니스탄과 중동지역의 혹독한 바람으로부터 자신을 보호하기 위해 발달하였다. 독립심이 강해 사람에게 다정하게 다가오지 않으며 예민하고 신경질적인 면도 있지만 계속적인 품종개량으로 이전보다 믿음직스러워졌고 유순해졌다. 시각에 의존해서 사냥을 했기 때문에 움직이는 물체에 예민하므로 사람이 없을 때는 주의해야 한다. 현대식 주택에서 안락한 생활을 하며 주인이나 가족의 보살핌을 받지 못하면 금세 수척해지고 기가 죽는다. 어려서 훈련을 엄격히 해놓아야 하운드종 특유의 장난기와 거친 면을 고칠 수 있다.",
//   "recommend_reason": "아프간하운드 추천의 내용",
//   "dog_img": "여기에 아프간하운드 사진",
//   "dog_cost": "입양 하면 99999원이 듭니다!"
// }

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