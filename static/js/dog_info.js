let date = new Date()
let priorDate = new Date(new Date().setDate(date.getDate() - 90))

let currentDate = date.toISOString().slice(0, 10)
let threeMonthBefore = priorDate.toISOString().slice(0, 10)

$('.date-picker-start').append(`<input type="text" id="datePickerStart" class="form-control text-center" value="${threeMonthBefore}">`)
$('.date-picker-end').append(`<input type="text" id="datePickerEnd" class="form-control text-center" value="${currentDate}">`)

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
 * Nav change bg on scroll & show logo
 */
$(function () {
  $(document).scroll(function () {
    var $nav = $("#navbar2");
    $nav.toggleClass('scrolled', $(this).scrollTop() > $nav.outerHeight());
  });
});

/**
 * Load abandoned dogs filter features from DB <option value="{key}">{key} ({value} 마리)</option>
 */
$.ajax({
  type: "GET",
  url: "/find_dog/filter/breed",
  data: {},
  success: function (response) {
    let breeds_list = response
    console.log(breeds_list)

    $('#filter-breed').empty()
    $('#filter-breed').append("<option selected value='전체'>전체</option>")
    for (breeds of breeds_list) {
      $('#filter-breed').append(`<option value="${breeds["breed"]}">${breeds["breed"]} (${breeds["count"]} 마리)</option>`)
    }
  }
})

/**
 * Filter change
 */
$('#city-filter-list-toggle').on('change', function () {
  let selection = $(this).val();
  if (selection !== "전체") {
    $.ajax({
      type: "GET",
      url: "/find_dog/filter/city",
      data: {},
      success: function (response) {
        let city_filter = response[`${selection}`]

        $('#city-filter-list-after').empty()
        $('#city-filter-list-after').append("<option selected value='전체'>전체</option>")
        for (cities of city_filter) {
          $('#city-filter-list-after').append(`<option value="${cities}">${cities}</option>`)
        }
      }
    })
    $("#city-filter-list-before").hide()
    $("#city-filter-list-after").show()
  } else {
    $('#city-filter-list-after').empty()
    $('#city-filter-list-after').append("<option selected value='전체'>전체</option>")
    $("#city-filter-list-before").show()
    $("#city-filter-list-after").hide()
  }
});

/**
 * Filter Time
 */
$(function () {
  $('#datePickerStart').datepicker({
    format: "yyyy-mm-dd", //데이터 포맷 형식(yyyy : 년 mm : 월 dd : 일 )
    // startDate: '-10d', //달력에서 선택 할 수 있는 가장 빠른 날짜. 이전으로는 선택 불가능 ( d : 일 m : 달 y : 년 w : 주)
    // endDate: '+10d', //달력에서 선택 할 수 있는 가장 느린 날짜. 이후로 선택 불가 ( d : 일 m : 달 y : 년 w : 주)
    autoclose: true, //사용자가 날짜를 클릭하면 자동 캘린더가 닫히는 옵션
    calendarWeeks: false, //캘린더 옆에 몇 주차인지 보여주는 옵션 기본값 false 보여주려면 true
    clearBtn: false, //날짜 선택한 값 초기화 해주는 버튼 보여주는 옵션 기본값 false 보여주려면 true
    // datesDisabled: ['2019-06-24', '2019-06-26'], //선택 불가능한 일 설정 하는 배열 위에 있는 format 과 형식이 같아야함.
    // daysOfWeekDisabled: [0, 6], //선택 불가능한 요일 설정 0 : 일요일 ~ 6 : 토요일
    // daysOfWeekHighlighted: [3], //강조 되어야 하는 요일 설정
    disableTouchKeyboard: false, //모바일에서 플러그인 작동 여부 기본값 false 가 작동 true가 작동 안함.
    immediateUpdates: false, //사용자가 보는 화면으로 바로바로 날짜를 변경할지 여부 기본값 :false 
    multidate: false, //여러 날짜 선택할 수 있게 하는 옵션 기본값 :false 
    multidateSeparator: ",", //여러 날짜를 선택했을 때 사이에 나타나는 글짜 2019-05-01,2019-06-01
    templates: {
      leftArrow: '&laquo;',
      rightArrow: '&raquo;'
    }, //다음달 이전달로 넘어가는 화살표 모양 커스텀 마이징 
    showWeekDays: true, // 위에 요일 보여주는 옵션 기본값 : true
    title: "검색 시작일", //캘린더 상단에 보여주는 타이틀
    todayHighlight: true, //오늘 날짜에 하이라이팅 기능 기본값 :false 
    toggleActive: true, //이미 선택된 날짜 선택하면 기본값 : false인경우 그대로 유지 true인 경우 날짜 삭제
    weekStart: 0, //달력 시작 요일 선택하는 것 기본값은 0인 일요일 
    language: "ko" //달력의 언어 선택, 그에 맞는 js로 교체해줘야한다.

  }); //datepicker end
}); //ready end

$(function () {
  $('#datePickerEnd').datepicker({
    format: "yyyy-mm-dd", //데이터 포맷 형식(yyyy : 년 mm : 월 dd : 일 )
    // startDate: '-10d', //달력에서 선택 할 수 있는 가장 빠른 날짜. 이전으로는 선택 불가능 ( d : 일 m : 달 y : 년 w : 주)
    endDate: '+0d', //달력에서 선택 할 수 있는 가장 느린 날짜. 이후로 선택 불가 ( d : 일 m : 달 y : 년 w : 주)
    autoclose: true, //사용자가 날짜를 클릭하면 자동 캘린더가 닫히는 옵션
    calendarWeeks: false, //캘린더 옆에 몇 주차인지 보여주는 옵션 기본값 false 보여주려면 true
    clearBtn: false, //날짜 선택한 값 초기화 해주는 버튼 보여주는 옵션 기본값 false 보여주려면 true
    // datesDisabled: ['2019-06-24', '2019-06-26'], //선택 불가능한 일 설정 하는 배열 위에 있는 format 과 형식이 같아야함.
    // daysOfWeekDisabled: [0, 6], //선택 불가능한 요일 설정 0 : 일요일 ~ 6 : 토요일
    // daysOfWeekHighlighted: [3], //강조 되어야 하는 요일 설정
    disableTouchKeyboard: false, //모바일에서 플러그인 작동 여부 기본값 false 가 작동 true가 작동 안함.
    immediateUpdates: false, //사용자가 보는 화면으로 바로바로 날짜를 변경할지 여부 기본값 :false 
    multidate: false, //여러 날짜 선택할 수 있게 하는 옵션 기본값 :false 
    multidateSeparator: ",", //여러 날짜를 선택했을 때 사이에 나타나는 글짜 2019-05-01,2019-06-01
    templates: {
      leftArrow: '&laquo;',
      rightArrow: '&raquo;'
    }, //다음달 이전달로 넘어가는 화살표 모양 커스텀 마이징 
    showWeekDays: true, // 위에 요일 보여주는 옵션 기본값 : true
    title: "검색 종료일", //캘린더 상단에 보여주는 타이틀
    todayHighlight: true, //오늘 날짜에 하이라이팅 기능 기본값 :false 
    toggleActive: true, //이미 선택된 날짜 선택하면 기본값 : false인경우 그대로 유지 true인 경우 날짜 삭제
    weekStart: 0, //달력 시작 요일 선택하는 것 기본값은 0인 일요일 
    language: "ko" //달력의 언어 선택, 그에 맞는 js로 교체해줘야한다.

  }); //datepicker end
}); //ready end

/**
 * Filter button submit => Find Dog page
 */
function filterSearch() {
  let date_start = document.getElementById("datePickerStart");
  let date_start_selected = date_start.value;

  let date_end = document.getElementById("datePickerEnd");
  let date_end_selected = date_end.value;

  let state = document.getElementById("city-filter-list-toggle");
  let state_selected = state.options[state.selectedIndex].value;

  let city = document.getElementById("city-filter-list-after");
  let city_selected = city.options[city.selectedIndex].value;

  let breed = document.getElementById("filter-breed");
  let breed_selected = breed.options[breed.selectedIndex].value;

  window.location.href = `/find_dog?survey=false&ds=${date_start_selected}&de=${date_end_selected}&state=${state_selected}&city=${city_selected}&breed=${breed_selected}`
}

/**
 * Move to Dog posts page
 */
function moveToDogPosts(item) {
  let desertionNo = $(item).attr("id")
  window.location.href = `/find_dog/dog_info?id=${desertionNo}` // Move to dog posts page
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