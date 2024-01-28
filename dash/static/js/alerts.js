function closeAlert() {
  alertContainer.classList.remove("show");
  setTimeout(function () {
    alertContainer.style.display = "none";
  }, 300); // Adjust the duration of the fade (in milliseconds)
}

var alertContainer = document.getElementById("alertContainer");

// Use JavaScript to close the alert after 3 seconds
var timeoutId = setTimeout(closeAlert, 3000);

// Close the alert if the dismiss button is clicked
alertContainer
  .querySelector(".btn-close")
  .addEventListener("click", function () {
    clearTimeout(timeoutId); // Cancel the automatic close
    closeAlert();
  });
