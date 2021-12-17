/* Declare any variables here */

function changeButtonText(){

    $('.hidden').removeClass('hidden').hide();
    $('.change-text').click(function() {
        $(this).find('span').each(function() { $(this).toggle(); });
    });
    }
      
    changeButtonText();
