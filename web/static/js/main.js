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
    let top_of_object = $that.position().top - $(window).height()*0.1;

    // if element is in viewport, add the animate class
    if (bottom_of_window > top_of_object) {
      $(this).addClass('is-visible');
    }
  });
}

// if in viewport, show the animation
$(document).ready(function() {
  checkElementLocation();
});

$(window).on('scroll', function() {
  checkElementLocation();
});
