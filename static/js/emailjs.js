function sendMail(contactForm) {
    emailjs.send("gmail", "vintage", {
        "from_email": contactForm.email.value,
    }).then(
        function (response) {
            console.log("Email Sent!", response);
        },
        function (error) {
            console.log("Email Not Sent...", error);
        });
    return false;
}