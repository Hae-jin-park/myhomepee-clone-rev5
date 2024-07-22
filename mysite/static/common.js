var url = new URL(window.location.href);
var windowWidth = $(window).width();
$(document).ready(function () {
  console.log(url);
  if (windowWidth < 768) {
    $('.left-sidebar').hide();
  } else {
    $('.left-sidebar').show();
  }
  if (url.pathname == '/') {
    $('.logo').hide();
  }
  $('#ham-button')
    .off()
    .on('click', function (e) {
      $('.main-nav').toggle();
    });
});

$(window).resize(function () {
  var windowWidth = $(window).width();
  if (windowWidth < 768) {
    $('#trigger').prop('checked', false);
    $('.main-nav').hide();
    $('.left-sidebar').hide();
  } else {
    $('.left-sidebar').show();
    $('.main-nav').hide();
  }
});
