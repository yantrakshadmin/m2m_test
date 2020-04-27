$(document).ready(function(){
  $("#add_form").click(function(){
   var total = $('.man_class').find('#id_form-TOTAL_FORMS').val();
   var init = $('.man_class').find('#id_form-INITIAL_FORMS').val();
   var extra = total-init+1;
   var total = parseInt(total, 10)+1;
   var pathname = window.location.pathname.split('/');
   if(pathname.length == 5){
     pk = pathname[2];
   }else{
     pk = 0;
   }
  $.ajax({
        url: '/exams/getset/',
        data : {extra:extra,pk:pk},
    })
    .done(function(response) {
        $('.setclass').append(response);
        $('.man_class').find('#id_form-TOTAL_FORMS').val(total)
    });
});

$("#remove_form").click(function(){
   var total = $('.man_class').find('#id_form-TOTAL_FORMS').val();
   var init = $('.man_class').find('#id_form-INITIAL_FORMS').val();
   var extra = total - init;
   if(total>1){
    var total = parseInt(total, 10)-1;
    $('.man_class').find('#id_form-TOTAL_FORMS').val(total);
    var init = parseInt(init, 10)-1;
    if(extra==0){
      $('.man_class').find('#id_form-INITIAL_FORMS').val(init);
    }
    var sub_id = $(this).parent().find('.setelement').last().find('.sub_id').html();
    $(this).parent().find('.setelement').last().remove();
    $.ajax({
        url: '/exams/'+sub_id+/sub_delete/,
    })
    .done(function(response) {
       alert(response);
    });   
  }
});
});