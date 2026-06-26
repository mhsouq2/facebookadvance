(function(){
  "use strict";

  // Mobile menu toggle
  var menuToggle = document.getElementById('menuToggle');
  var mobileNav = document.getElementById('mobileNav');
  if (menuToggle && mobileNav) {
    menuToggle.addEventListener('click', function(){
      var isHidden = mobileNav.hasAttribute('hidden');
      if (isHidden) {
        mobileNav.removeAttribute('hidden');
        menuToggle.setAttribute('aria-expanded', 'true');
      } else {
        mobileNav.setAttribute('hidden', '');
        menuToggle.setAttribute('aria-expanded', 'false');
      }
    });
  }

  // Mobile search toggle: focus the header search field / route to search page
  var mobileSearchToggle = document.getElementById('mobileSearchToggle');
  if (mobileSearchToggle) {
    mobileSearchToggle.addEventListener('click', function(){
      var input = document.getElementById('main-search');
      if (input) {
        input.scrollIntoView({behavior:'smooth', block:'center'});
        input.focus();
      }
    });
  }

  // Ensure only relevant FAQ items keep state (progressive enhancement only; native <details> already works)
})();
