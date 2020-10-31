// https://stackoverflow.com/questions/63265789/how-do-i-send-my-form-information-on-submit-to-my-email-with-emailjs
const btn = document.getElementById('sub-button');

function sendMail(contactForm) {
    emailjs.send("gmail", "vintage", {
        "from_email": contactForm.email.value,
    }).then(() => {
        btn.value = 'Subscribe';
        alert('Success!');
    }, (err) => {
        btn.value = 'Subscribe';
        alert(JSON.stringify(err));
    });

}