$().jquery

/* To Display, Read/Hide Story when clicked */
function changeButtonText(){

    $('.hidden').removeClass('hidden').hide();
    $('.change-text').click(function() {
        $(this).find('span').each(function() { $(this).toggle(); });
    });
    }
      
/* Needed for bootstrap form validation to work */
function validateForms() {
  'use strict'

var forms = document.querySelectorAll('.needs-validation')

  Array.prototype.slice.call(forms)
    .forEach(function (form) {
      form.addEventListener('submit', function (event) {
        if (!form.checkValidity()) {
          event.preventDefault()
          event.stopPropagation()
        }

        form.classList.add('was-validated')
      }, false)
    })
  }


changeButtonText();  
validateForms();