$(document).ready ( function(){
 
 $('#register').validate(
 {
  rules: {
    firstname: {
      minlength: 2,
      required: true
    },
    lastname: {
      required: true
    },
    password: {
      minlength: 2,
      required: true
    }
  },
  messages: {
        firstname: "Please enter your first name",
        lastname: "Please enter your last name",
        password: {
            required: "Please provide a password",
            minlength: "Your password must be at least 5 characters long"
        }
  },
  highlight: function(element) {
    $(element).closest('.form-group').removeClass('success').addClass('error');
  },
  success: function(element) {
    element
    .text('OK!').addClass('valid')
    .closest('.form-group').removeClass('error').addClass('success');
  }
 });
}); // end document.ready