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
 * Move to Survey page
 */
document.querySelector(".nav-survey").addEventListener("click", moveToSurveyPage)

function moveToSurveyPage() {
  window.location.href = "/survey" // Move to survey page
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
 * DB에서 현재 보호중인 유기견들 불러오기
 */
$.ajax({
  type: "GET",
  url: "/find_dog/list",
  data: {},
  async: false,
  success: function (response) {
    /**
     * Load abandoned dogs thumbnails to find_dog page
     */
    let abandonedDogList = response

    let container = $('#pagination');
    container.pagination({
      dataSource: abandonedDogList,
      pageSize: 48,
      autoHidePrevious: true,
      autoHideNext: true,
      pageRange: 1,
      className: 'paginationjs-theme-blue paginationjs-big',
      callback: function (abandonedDogList, pagination) {
        // template method of yourself
        let template_dog_list = document.querySelector("#template-dog-list").innerHTML
        let res = ""
        for (i = 0; i < abandonedDogList.length; i++) {
          let dogSex;
          if (abandonedDogList[i].sexCd == "M") {
            dogSex = "<i class='fa-solid fa-mars fa-lg' style='color:#04A2F5'></i>"
          } else {
            dogSex = "<i class='fa-solid fa-venus fa-lg' style='color:#E73E77'></i>"
          }
          res += template_dog_list
            .replace("{popfile}", abandonedDogList[i].popfile)
            .replace("{kindCd}", abandonedDogList[i].kindCd)
            // .replace("{sexCd}", abandonedDogList[i].sexCd)
            .replace("{sexCd}", dogSex)
            .replace("{happenDt}", abandonedDogList[i].happenDt.slice(2))
            .replace("{noticeNo}", abandonedDogList[i].noticeNo)
            .replace("{processState}", abandonedDogList[i].processState)
            .replace("{desertionNo}", abandonedDogList[i].desertionNo)
        }
        document.querySelector(".dog-list").innerHTML = res
      }
    })
  }
})


// let container = $('#pagination');
// container.pagination({
//   dataSource: function (abandonedDogList) {
//     $.ajax({
//       type: "GET",
//       url: "/find_dog/list",
//       data: {},
//       success: function (response) {
//         console.log(response)
//         abandonedDogList(response);
//       }
//     });
//   },
//   pageNumber: 1,
//   pageSize: 48,
//   autoHidePrevious: true,
//   autoHideNext: true,
//   pageRange: 1,
//   className: 'paginationjs-theme-blue paginationjs-big',
//   callback: function (abandonedDogList, pagination) {
//     // template method of yourself
//     let template_dog_list = document.querySelector("#template-dog-list").innerHTML
//     let res = ""
//     for (i = 0; i < abandonedDogList.length; i++) {
//       let dogSex;
//       if (abandonedDogList[i].sexCd == "M") {
//         dogSex = "<i class='fa-solid fa-mars fa-lg' style='color:#04A2F5'></i>"
//       } else {
//         dogSex = "<i class='fa-solid fa-venus fa-lg' style='color:#E73E77'></i>"
//       }
//       res += template_dog_list
//         .replace("{popfile}", abandonedDogList[i].popfile)
//         .replace("{kindCd}", abandonedDogList[i].kindCd)
//         // .replace("{sexCd}", abandonedDogList[i].sexCd)
//         .replace("{sexCd}", dogSex)
//         .replace("{happenDt}", abandonedDogList[i].happenDt.slice(2))
//         .replace("{noticeNo}", abandonedDogList[i].noticeNo)
//         .replace("{processState}", abandonedDogList[i].processState)
//         .replace("{desertionNo}", abandonedDogList[i].desertionNo)
//     }
//     document.querySelector(".dog-list").innerHTML = res
//   }
// })

/**
 * Load 10 abandoned dogs thumbnails when bottom of page reached
 */
// $(window).scroll(function () {
//   if (($(window).scrollTop() == $(document).height() - $(window).height()) && (abandonedDogList.length !== 0)) {
//     let dog_list_template = document.querySelector("#template-dog-list").innerHTML
//     let res = ""
//     for (i = 0; i < 10 % abandonedDogList.length; i++) {
//       res += dog_list_template
//         .replace("{popfile}", abandonedDogList[0].popfile)
//         .replace("{kindCd}", abandonedDogList[0].kindCd)
//         .replace("{sexCd}", abandonedDogList[0].sexCd)
//         .replace("{happenDt}", abandonedDogList[0].happenDt)
//         .replace("{noticeNo}", abandonedDogList[0].noticeNo)
//         .replace("{processState}", abandonedDogList[0].processState)
//       abandonedDogList.shift()
//     }

//     document.querySelector(".dog-list").insertAdjacentHTML('beforeend', res)
//     console.log(abandonedDogList)
//   }
// });

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
 * Move to Dog posts page
 */
function moveToDogPosts(item) {
  let desertionNo = $(item).attr("id")
  window.location.href = `/find_dog/dog_info?id=${desertionNo}` // Move to dog posts page

  // $.ajax({
  //   type: "POST",
  //   url: "/find_dog/dog_info/dog_post",
  //   data: {
  //     desertionNo
  //   },
  //   async: false,
  //   success: function (response) {
  //     console.log(response)
  //   }
  // })
}

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