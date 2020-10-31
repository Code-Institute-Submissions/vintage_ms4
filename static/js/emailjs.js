// https://stackoverflow.com/questions/63265789/how-do-i-send-my-form-information-on-submit-to-my-email-with-emailjs
//Getting the name and email from the DOM
let email = document.getElementById('email').value
//Getting the button from the DOM
let submitButton = document.getElementById('sub-button')

//Add event listener on click to the button - notice i added the event as argument to the function
submitButton.addEventListener('click', function(event){

    //prevent the reload of the page. here i prevent the event.
    event.preventDefault()

    //Sending the email with the name and email
    emailjs.send("gmail", "vintage", {
        "from_email": contactForm.email.value,
    })
        .then(
            function (response) {
                console.log("SUCCESS", response);
                alert("Email sent successfully!");

            },
            function (error) {
                console.log("FAILED", error);
                 alert("FAILED!"+error);

            }

        );
})



