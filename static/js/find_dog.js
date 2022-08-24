/**
 * Move to Home page
 */
document.querySelector(".navbar-brand").addEventListener("click", moveToHomePage)
document.querySelector(".nav-home").addEventListener("click", moveToHomePage)

function moveToHomePage() {
  window.location.href = "/" // Move to home page
}

/**
 * Move to Survey page
 */
document.querySelector(".nav-survey").addEventListener("click", moveToSurveyPage)

function moveToSurveyPage() {
  window.location.href = "/survey" // Move to page
}

/**
 * Load abandoned dogs thumbnails to find_dog page
 */
var abandonedDogList = null
$.ajax({
  type: "GET",
  url: "/find_dog/thumbnail_page",
  data: {},
  async: false,
  success: function (response) {
    let dog_list_template = document.querySelector("#template-dog-list").innerHTML
    let res = ""
    response.slice(0, 10).forEach(function (el) {
      res += dog_list_template
        .replace("{popfile}", el.popfile)
        .replace("{kindCd}", el.kindCd)
        .replace("{sexCd}", el.sexCd)
        .replace("{happenDt}", el.happenDt)
        .replace("{noticeNo}", el.noticeNo)
        .replace("{processState}", el.processState)
    })
    document.querySelector(".dog-list").innerHTML = res
    abandonedDogList = response.slice(30)
  }
})

/**
 * Load 10 abandoned dogs thumbnails when bottom of page reached
 */
$(window).scroll(function () {
  if (($(window).scrollTop() == $(document).height() - $(window).height()) && (abandonedDogList.length !== 0)) {
    let dog_list_template = document.querySelector("#template-dog-list").innerHTML
    let res = ""
    for (i = 0; i < 10; i++) {
      res += dog_list_template
        .replace("{popfile}", abandonedDogList[i].popfile)
        .replace("{kindCd}", abandonedDogList[i].kindCd)
        .replace("{sexCd}", abandonedDogList[i].sexCd)
        .replace("{happenDt}", abandonedDogList[i].happenDt)
        .replace("{noticeNo}", abandonedDogList[i].noticeNo)
        .replace("{processState}", abandonedDogList[i].processState)
    }
    for (i = 0; i < 10; i++) {
      abandonedDogList.shift()
    }
    // abandonedDogList.forEach(function (el) {
    //   res += dog_list_template
    //     .replace("{popfile}", el.popfile)
    //     .replace("{kindCd}", el.kindCd)
    //     .replace("{sexCd}", el.sexCd)
    //     .replace("{happenDt}", el.happenDt)
    //     .replace("{noticeNo}", el.noticeNo)
    //     .replace("{processState}", el.processState)
    // })
    document.querySelector(".dog-list").insertAdjacentHTML('beforeend', res)
    console.log(abandonedDogList)
  }
});

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