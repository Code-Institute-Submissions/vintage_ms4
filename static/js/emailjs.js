// https://stackoverflow.com/questions/63265789/how-do-i-send-my-form-information-on-submit-to-my-email-with-emailjs

function sendMail(contactForm) {
    emailjs.send("gmail", "vintage", {
        "from_email": contactForm.email.value,
    }).then(
        function() {
             alert("Email sent successfully!");


        },
         function(error) {
            alert("FAILED!"+error);
        });
}