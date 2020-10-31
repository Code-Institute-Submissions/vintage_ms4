// https://stackoverflow.com/questions/63265789/how-do-i-send-my-form-information-on-submit-to-my-email-with-emailjs
const btn = document.getElementById('sub-button');
document.getElementById('subscribe-form')
 .addEventListener('submit', function(event) {
     event.preventDefault();

     btn.value = 'Subscribed';
 });
function sendMail(contactForm) {
    emailjs.send("gmail", "vintage", {
        "from_email": contactForm.email.value,
    }).then(function (response) {
        if (response.status == 200 && response.text == 'OK')
            alert('Your message has been sent Successfully..!!!');
        else
            alert('Sorry there was a problem. Please try again...!!!');
    }, function () {
        alert('Sorry there was a problem. Please try again...!!!');
    });
}