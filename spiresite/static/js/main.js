$(document).ready(function(){
 
    
    $("#srec-slider").slick({
      infinite: true,
      slidesToShow: 3,
      slidesToScroll: 1,
      dots: true,
      arrows: true,
      autoplay: true,
      autoplaySpeed: 3000,
      //infinite: true;
    });

    $("#fame-slider").slick({
      infinite: true,
      slidesToShow: 3,
      slidesToScroll: 1,
      dots: true,
      arrows: true,
      autoplay: true,
      autoplaySpeed: 3000,
      //infinite: true;
    });
    
    $(".slider").slick({
      infinite: true,
      slidesToShow: 3,
      slidesToScroll: 1,
      dots: true,
      arrows: true,
      autoplay: true,
      autoplaySpeed: 3000,
      //infinite: true;
    });


   
     $('#add_more').click(function() {
        cloneMore('div.table:last', 'service');
    });
     function cloneMore(selector, type) {
        var newElement = $(selector).clone(true);
        var total = $('#id_' + type + '-TOTAL_FORMS').val();
        newElement.find(':input').each(function() {
            var name = $(this).attr('name').replace('-' + (total-1) + '-','-' + total + '-');
            var id = 'id_' + name;
            $(this).attr({'name': name, 'id': id}).val('').removeAttr('checked');
        });
        newElement.find('label').each(function() {
            var newFor = $(this).attr('for').replace('-' + (total-1) + '-','-' + total + '-');
            $(this).attr('for', newFor);
        });
        total++;
        $('#id_' + type + '-TOTAL_FORMS').val(total);
        $(selector).after(newElement);
    }


    $("form#profile-form:input").change(function(){
       console.log('changed')
    });



    /** Member profile edit */
    $( "#edit-profile" ).click(function(e) {

      e.preventDefault();

      $(this).hide();

    });
});
