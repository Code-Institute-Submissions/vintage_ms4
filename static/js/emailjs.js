const btn = document.getElementById('button');

document.getElementById('subscribe-form')
 .addEventListener('submit', function(event) {
   event.preventDefault();

   btn.value = 'Subscribing...';

   const serviceID = 'default_service';
   const templateID = 'template_8jquzfe';

   emailjs.sendForm(serviceID, templateID, this)
    .then(() => {
      btn.value = 'Subscribe';
      alert('Success!');
    }, (err) => {
      btn.value = 'Subscribe';
      alert(JSON.stringify(err));
    });
});