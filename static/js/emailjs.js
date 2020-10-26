const btn = document.getElementById('sub-button');

document.getElementById('subscribe-form')
 .addEventListener('submit', function(event) {
   event.preventDefault();

   btn.value = 'Subscribing...';

   const serviceID = 'service_q2l54nc';
   const templateID = 'template_8jquzfe';

   emailjs.send(serviceID, templateID, this)
    .then(() => {
      btn.value = 'Subscribe';
      alert('Success!');
    }, (err) => {
      btn.value = 'Subscribe';
      alert(JSON.stringify(err));
    });
});