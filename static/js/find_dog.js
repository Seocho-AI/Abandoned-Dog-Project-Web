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
 * Navbar box-shadow
 */
function scrollHeader() {
  const nav = document.getElementById('header')
  // When the scroll is greater than 200 viewport height, add the scroll-header class to the header tag
  if (this.scrollY >= 80) nav.classList.add('scroll-header');
  else nav.classList.remove('scroll-header')
}
window.addEventListener('scroll', scrollHeader)

$.ajax({
  type: "GET",
  url: "/abandoned-dogs/list",
  data: {},
  success: function (response) {
    console.log(response)

    let dog_list_template = document.querySelector("#template-dog-list").innerHTML
    let res = ""
    response.forEach(function (el) {
      res += dog_list_template.replace("{breed_name_kr}", el.breed_name_kr)
        .replace("{breed_no}", el.breed_no)
    })
    document.querySelector(".dog-list").innerHTML = res
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