let date = new Date()
let priorDate = new Date(new Date().setDate(date.getDate() - 90))

let currentDate = date.toISOString().slice(0, 10)
let threeMonthBefore = priorDate.toISOString().slice(0, 10)

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
  window.location.href = `/find_dog?survey=false&ds=2019-01-01&de=${currentDate}&state=전체&city=전체&breed=전체` // Move to find dog page
}

/**
 * Move to Survey page
 */
document.querySelector(".nav-survey").addEventListener("click", moveToSurveyPage)

function moveToSurveyPage() {
  window.location.href = "/survey" // Move to survey page
}

/**
 * Move to selected dog page
 */
function moveToSelectedDog(item) {
  let desertionNo = $(item).attr("id")
  let trait_score_diff = $(item).attr("score_diff")
  // trait_score_diff = JSON.parse(trait_score_diff)
  // console.log(trait_score_diff)
  // console.log(typeof trait_score_diff)
  window.location.href = `/find_dog/dog_info?survey=true&id=${desertionNo}&trait_score_diff=${trait_score_diff}` // Move to dog posts page
}

/**
 * Move to recommended dog list page
 */
function moveToRecDocListPage() {
  let rec_list = $(".rec_list").attr("id")
  let rec_list_score = $(".rec_list_score").attr("id")
  let tot_trait_score_diff = $(".tot_trait_score_diff").attr("id")

  rec_list = rec_list.slice(1, -1).replaceAll("'", "").split(", ")
  tot_trait_score_diff_temp = JSON.parse(tot_trait_score_diff)
  tot_trait_score_diff = {}

  for (let i = 0; i < 100; i++) {
    let d_no = rec_list[i]
    if (tot_trait_score_diff_temp[d_no]) {
      tot_trait_score_diff[d_no] = tot_trait_score_diff_temp[d_no]
    }
  }

  // console.log(tot_trait_score_diff)
  tot_trait_score_diff = JSON.stringify(tot_trait_score_diff)


  // console.log(rec_list)
  // console.log(tot_trait_score_diff_temp)
  // console.log(tot_trait_score_diff)
  window.location.href = `/find_dog?survey=true&rec_list=${rec_list}&rec_list_score=${rec_list_score}&tot_trait_score_diff=${tot_trait_score_diff}` // Move to find dog page
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