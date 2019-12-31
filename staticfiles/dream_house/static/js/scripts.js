$(document).ready(function(){
    $('.sidenav').sidenav();
});
$(document).ready(function(){
 $('select').formSelect();
});

$(document).ready(function () {
$(".predict_price").click(function() {
  $.get("/predict_price_form/", function(data) {
        $("#fill_parameters").html(data);
      $('select').formSelect();
      $('html, body').animate({scrollTop:$('#fill_parameters').position().top}, 1000);
      });
    });
});

$(document).ready(function () {
    $(".load_user_info").click(function() {
        $.get("/user_parameters/", function(data) {
            $("#loaded_content").html(data);
        });
    });
});
$(document).ready(function () {
    $(".load_user_subscribes").click(function() {
        $.get("/user_subscribes/", function(data) {
            $("#loaded_content").html(data);
        });
    });
});

$(document).ready(function () {
  $(".load_user_settings").click(function() {
      $.get("/user_settings/", function(data) {
          $("#loaded_content").html(data);
      });
  });
});
$('[data-toggle="datepicker"]').datepicker();

$(document).ready(function () {
    $(".change_user_settings").click(function() {
        $.get("/change_user_settings_page/", function(data) {
            $("#loaded_content").html(data);
        });
    });
});

$(document).ready(function(){
    $('.sidenav').sidenav();
});
