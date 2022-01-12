var validPassword = "Not A Match" ;
var inValidPassword = "Your all set!";
var recapcha=false;

/* To Display, Read/Hide Story when clicked */
function changeButtonText(){

    $('.hidden').removeClass('hidden').hide();
    $('.change-text').click(function() {
        $(this).find('span').each(function() { $(this).toggle(); });
    });
    }
      
/* Needed for bootstrap form validation to work */
/* From https://getbootstrap.com/docs/5.0/forms/validation/ */
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

/* For the signin button on successful registration */

function checkForSuccess(){
  document.getElementById('success-message-signin').insertAdjacentHTML(
    'afterbegin', `<a class="nav-link active nav-link" aria-label="Sign In" href="/signin">
    <span class="text-menu-style change-text-color">Click Here to Sign In</span></a>`);
  document.getElementById('signup-form').style.cssText="display: none;";
}

/*  For password checking */

$(document).ready(function () {
  $("#passwordField2").keyup(checkPasswordMatch);
 });

function checkPasswordMatch() {
   let p1 = $("#passwordField1").val();
   let p2 = $("#passwordField2").val();
   
   if (p1 !== p2){
      $("#validPassword").html(validPassword).addClass('password-check-failure');
      $('#submitForm').addClass('disabled');
   }else{
      $("#validPassword").html(inValidPassword).addClass('password-check-success').removeClass('password-check-failure');
      $('#submitForm').removeClass('disabled');
  }
}

/* For Recapcha validation */

function verifyRecapcha() {
  $('#recapcha-message').css('color', '#198754');
  recapcha = true;  
}
function isRecapchaValid(){
  setTimeout(() => {
  $('#recapcha-message').css("fontSize", "1.1em").css('color', 'rgb(220, 53, 69)');
  }, 1000);
  return recapcha;
  }
  
changeButtonText();  
validateForms(); 
checkForSuccess();

