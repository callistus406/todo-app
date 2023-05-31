window.onload = function () {
  var todoForm = document.querySelector(".todo-form");
  todoForm.onsubmit = function (e) {
    e.preventDefault();
  };

  function dropdownMenuHandler(dropdownMenu) {
    if (dropdownMenu.classList.contains("card__dropdown__menu")) {
      if (dropdownMenu.classList.contains("card__dropdown__menu--show")) {
        dropdownMenu.classList.remove("card__dropdown__menu--show");
      } else {
        dropdownMenu.classList.add("card__dropdown__menu--show");
      }
    }
  }

  // card-dropdown
  var cardDropdownToggler = document.querySelectorAll(
    ".card__dropdown__toggler"
  );
  cardDropdownToggler.forEach(function (item) {
    item.onclick = function () {
      var dropdownMenu = item.nextElementSibling;
      dropdownMenuHandler(dropdownMenu);
    };
  });

  var cardDropdownMenu = document.querySelectorAll(".card__dropdown__menu");
  cardDropdownMenu.forEach(function (item) {
    item.onclick = function (e) {
      if (e.srcElement.checked) {
        dropdownMenuHandler(e.currentTarget);
      }
    };
  });

  // filters
  var filtersToggler = document.querySelector(".filters-toggler");
  var filtersMenu = document.querySelector(".filters");
  var filtersTogglerShow = document.querySelector(".filters-toggler__show");
  var filtersTogglerHide = document.querySelector(".filters-toggler__hide");

  filtersToggler.onclick = function (e) {
    if (filtersMenu.classList.contains("filters--show")) {
      filtersMenu.classList.remove("filters--show");
    } else {
      filtersMenu.classList.add("filters--show");
    }

    if (filtersMenu.classList.contains("filters--show")) {
      filtersTogglerShow.style.display = "none";
      filtersTogglerHide.style.display = "block";
    } else {
      filtersTogglerShow.style.display = "block";
      filtersTogglerHide.style.display = "none";
    }
  };
};
