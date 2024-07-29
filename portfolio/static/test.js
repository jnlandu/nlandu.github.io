  // Get the button
  const backToTopButton = document.querySelector('.back-to-top-button')
  var backToTopButtonShown = false;
  var origBackToTopButtonClassName = backToTopButton.className;
  
  // Check if already needs to be displayed before any scrolling is done
  if (window.scrollY > scrollTriggerHeight) {
      backToTopButton.className = origBackToTopButtonClassName + ' show';
      backToTopButtonShown = true;
  }
  
  // Set up showing and hiding back-to-top button on scroll
  window.onscroll = function(event) {
      if (window.scrollY > 100 && !backToTopButtonShown) {
          backToTopButton.className = origBackToTopButtonClassName + ' show';
          backToTopButtonShown = true;
      } else if (window.scrollY <= scrollTriggerHeight && backToTopButtonShown) {
          backToTopButton.className = origBackToTopButtonClassName;
          backToTopButtonShown = false;
      }
  }
  // Creates a closure for the 'scrollPosition' so those functions can be executed in a timeout
  function makeScrollToTimeoutFunction(scrollPosition) {
      return function () {
          window.scroll(0, scrollPosition);
      }
  }
  
  //  Set up scroll to top
  backToTopButton.onclick = function (event) {
      
      // Create timeout scroll to functions
      var timeoutFunctions = [];
      var scrollToOffset = 20;
      var start = window.scrollY;
      var end = 0;
      var scrollToPosition = start - scrollToOffset;
      while (scrollToPosition > end) {
          timeoutFunctions.push(makeScrollToTimeoutFunction(scrollToPosition));
          scrollToPosition = scrollToPosition - scrollToOffset;
          scrollToPosition = scrollToPosition < 0 ? 0 : scrollToPosition; // set to 0 if less than 0
      }
  
      var scrollTimeoutOffset = 0;
      timeoutFunctions.forEach(function (timeoutFunction, index) {
          setTimeout(function() {
             timeoutFunction();
          }, 50 + scrollTimeoutOffset);
          scrollTimeoutOffset += 2;
      });
  }
  