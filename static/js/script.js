/* For mobile menu */
document.addEventListener('DOMContentLoaded', function() {
    var options;
    var elems = document.querySelectorAll('.sidenav');
    var instances = M.Sidenav.init(elems, options);
  });
/* For Carousel */
document.addEventListener('DOMContentLoaded', function() {
  var options;
  var elems = document.querySelectorAll('.carousel');
  var instances = M.Carousel.init(elems, options);
});