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
 * Nav change bg on scroll & show logo
 */
$(function () {
  $(document).scroll(function () {
    var $nav = $("#navbar2");
    $nav.toggleClass('scrolled', $(this).scrollTop() > $nav.outerHeight());
  });
});

/**
 * Load abandoned dogs filter features from DB
 */
$.ajax({
  type: "GET",
  url: "/find_dog/filter",
  data: {},
  success: function (response) {
    let breed_count = response[0]
    let state_city = response[1]

    let template_breed_filter = document.querySelector("#template-breed-filter").innerHTML
    let res = "<option selected>전체</option>"
    Object.keys(breed_count).forEach(function (key) {
      res += template_breed_filter
        .replace("{key}", key)
        .replace("{key}", key)
        .replace("{value}", breed_count[key])
    })

    document.querySelector(".filter-breed").innerHTML = res
    console.log(breed_count, state_city)
  }
})

/**
 * Load dog info based on desertionNo from DB
 */
$.ajax({
  type: "GET",
  url: "/dog_posts/dog_info",
  data: {},
  success: function (response) {
    console.log(response)
  }
})

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
  const nav = document.getElementById('navbar2')
  // When the scroll is greater than 200 viewport height, add the scroll-header class to the header tag
  if (this.scrollY >= 80) nav.classList.add('scroll-header');
  else nav.classList.remove('scroll-header')
}
window.addEventListener('scroll', scrollHeader)