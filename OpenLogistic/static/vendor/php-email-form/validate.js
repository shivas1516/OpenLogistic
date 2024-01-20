/**
 * Simple Form Validation in JavaScript
 */
(function () {
  "use strict";

  let forms = document.querySelectorAll('.php-email-form');

  forms.forEach(function (form) {
    form.addEventListener('submit', function (event) {
      event.preventDefault();

      let formData = new FormData(form);

      // Add your custom form validation logic here
      let isValid = validateForm(formData);

      if (isValid) {
        // If form is valid, you can proceed with form submission
        form.submit();
      } else {
        // If form is not valid, display error messages
        displayError(form, 'Please fill in all required fields.');
      }
    });
  });

  function validateForm(formData) {
    // Add your custom form validation logic here
    // Return true if the form is valid, false otherwise
    // For example, you can check if required fields are filled

    // Example: Check if the 'senderName' field is filled
    if (!formData.get('sender_name')) {
      return false;
    }

    // Add more validation checks as needed

    return true; // Form is considered valid if it passes all checks
  }

  function displayError(form, error) {
    // Remove any existing error messages
    let existingError = form.querySelector('.invalid-feedback');
    if (existingError) {
      existingError.remove();
    }

    // Create and display the new error message
    let errorMessage = document.createElement('div');
    errorMessage.className = 'invalid-feedback';
    errorMessage.innerHTML = error;

    // Display the error message for the first input field
    let firstInput = form.querySelector('.form-control');
    if (firstInput) {
      firstInput.parentNode.appendChild(errorMessage);
    }
  }

})();
