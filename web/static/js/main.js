$(document).ready(() => {


  $('[data-toggle-target]').click(function() {
    let target_name = $(this).attr('data-toggle-target');
    let targets = $(`[data-toggle-name=${target_name}]`);
    targets.toggle();
  });

  $('[data-toggle-hide]').hide();

})
