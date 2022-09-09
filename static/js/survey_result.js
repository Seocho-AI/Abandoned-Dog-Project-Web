
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
  window.location.href = `/find_dog?ds=2019-01-01&de=${currentDate}&state=전체&city=전체&breed=전체` // Move to find dog page
}

/**
 * Move to Survey page
 */
document.querySelector(".nav-survey").addEventListener("click", moveToSurveyPage)

function moveToSurveyPage() {
  window.location.href = "/survey" // Move to survey page
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