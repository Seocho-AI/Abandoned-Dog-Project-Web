let date = new Date()
let priorDate = new Date(new Date().setDate(date.getDate() - 90))

let currentDate = date.toISOString().slice(0, 10)
let threeMonthBefore = priorDate.toISOString().slice(0, 10)

/**
 * Move to Home page
 */
document.querySelector(".navbar-brand").addEventListener("click", moveToHomePage)

function moveToHomePage() {
  window.location.href = "/" // Move to home page
}

/**
 * Move to Find Dog page
 */
document.getElementById("abandoned-dog-page-btn").addEventListener("click", moveToAbandonedDogPage)

function moveToAbandonedDogPage() {
  // $.ajax({
  //   type: "GET",
  //   url: `/find_dog?ds=2019-01-01&de=${currentDate}&state=전체&city=전체&breed=전체`,
  //   data: {},
  //   success: function (response) {
  //     console.log(response)
  //   }
  // })
  window.location.href = `/find_dog?survey=false&ds=2019-01-01&de=${currentDate}&state=전체&city=전체&breed=전체` // Move to find dog page
}

/**
 * Move to Survey page
 */
document.getElementById("survey-page-btn").addEventListener("click", moveToSurveyPage)

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
 * Getting abandoned-dog statistics from DB and show on Homepage
 */
$.ajax({
  type: "GET",
  url: "/dog_statistics",
  data: {},
  success: function (response) {
    let rescued_today = document.querySelector(".rescued-today")
    let adopt_in_year = document.querySelector(".adopt-in-year")
    let death_in_year = document.querySelector(".death-in-year")
    let protect_in_year = document.querySelector(".protect-in-year")

    rescued_today.textContent = response[0]
    adopt_in_year.textContent = response[1]
    death_in_year.textContent = response[2]
    protect_in_year.textContent = response[3]
  }
})

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
function scrollHeader() {
  const nav = document.getElementById('header')
  // When the scroll is greater than 200 viewport height, add the scroll-header class to the header tag
  if (this.scrollY >= 80) nav.classList.add('scroll-header');
  else nav.classList.remove('scroll-header')
}
window.addEventListener('scroll', scrollHeader)

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