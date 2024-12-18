odoo.define("global_search.global_search_highlight", function (require) {
  "use strict";

  function waitForElement(selector) {
    const deferred = $.Deferred();

    const checkExist = setInterval(function () {
      if ($(selector).length) {
        clearInterval(checkExist);
        deferred.resolve(); // Element is now in the DOM
      }
    }, 100); // Check every 100ms

    return deferred.promise();
  }

  function removeJightlightedInTable() {
    $("table td").each(function () {
      var text = $(this).text();
      var regEx = /<span class="alert-warning">.*?<\/span>/g;
      $(this).html(text.replace(regEx, "")); // Remove any previous highlighted text
    });
  }

  function highlightInTable() {
    var searchTerm = $("input").val();
    $("table td").each(function () {
      var cellText = $(this).text();
      var regex = new RegExp("(" + searchTerm + ")", "gi");
      var newText = cellText.replace(
        regex,
        '<span class="alert-warning">$1</span>'
      ); // Wrap match in <span>
      $(this).html(newText);
    });
  }

  function handleClick() {
    removeJightlightedInTable();
    setTimeout(() => {
      highlightInTable();
    }, 500);
  }

  $(document).ready(function () {
    waitForElement("input")
      .then(function () {
        if ($("input").val()) {
          handleClick();
        }
        $("button[name='global_search']").on("click", handleClick);
        $("a[role='tab']").on("click", function () {
          setTimeout(() => {
            $("a[role='tab']").on("click", function () {
              handleClick();
            });
          }, 1000);
          handleClick();
        });
      })
      .catch(function (error) {
        console.log("Error while finding global search input in DOM", error);
      });
  });
});
