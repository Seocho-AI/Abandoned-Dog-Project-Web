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
    document.querySelector(".dog-list").innerHTML=res
  }
})