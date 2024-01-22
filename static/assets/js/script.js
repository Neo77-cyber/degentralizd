document.addEventListener("DOMContentLoaded", function () {
    const topNav = document.getElementById("topNav");
    const hamburger = document.getElementById("hamburger");
    const menu = document.getElementById("menu");
  
    hamburger.addEventListener("click", function () {
      console.log("clicked");
      menu.classList.toggle("show");
    });
  
    window.addEventListener("scroll", function () {
      if (window.scrollY > 0) {
        topNav.classList.add("scrolled");
      } else {
        topNav.classList.remove("scrolled");
      }
    });
  });
  