$(document).ready(() => {

  $('[data-toggle-target]').click(function() {
    let target_name = $(this).attr('data-toggle-target');
    let targets = $(`[data-toggle-name=${target_name}]`);
    targets.toggle();
  });

  $('[data-toggle-hide]').hide();

})

function checkElementLocation() {
  let $window = $(window);
  let bottom_of_window = $window.scrollTop() + $window.height();

  $('.fade-in-section').each(function(i) {
    let $that = $(this);
    let top_of_object = $that.position().top;

    // if element is in viewport, add the animate class
    if (bottom_of_window > top_of_object) {
      $(this).addClass('is-visible');
    }
  });
}

function updateFillerElements() {
  $(".filler-splash").height($(".bg-splash").height());
}

function fullWidthElements() {
  $(".full-width").width($("body").width());
}

// if in viewport, show the animation
$(document).ready(function() {
  checkElementLocation();
  updateFillerElements();
  fullWidthElements();
});

$(window).on('scroll', function() {
  checkElementLocation();
});

$(window).on('resize', function() {
  updateFillerElements();
  fullWidthElements();
});
