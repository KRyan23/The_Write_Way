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

/* For the signin button on suceesful registration */

function checkForSuccess(){
  document.getElementById('success-message-signin').insertAdjacentHTML(
    'afterbegin', `<a class="nav-link active nav-link" aria-label="Sign In" href="/signin">
    <span class="text-menu-style change-text-color">Click Here to Sign In</span></a>`); 
}



changeButtonText();  
validateForms(); 
checkForSuccess();