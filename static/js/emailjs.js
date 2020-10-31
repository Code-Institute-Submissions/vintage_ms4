const btn = document.getElementById('sub-button');

document.getElementById('subscribe-form')
 .addEventListener('submit', function(event) {
   event.preventDefault();

   btn.value = 'Subscribing...';

   const serviceID = 'gmail';
   const templateID = 'vintage';

   emailjs.send(serviceID, templateID, 'subscribe-form')
    .then(() => {
      btn.value = 'Subscribe';
      alert('Success!');
    }, (err) => {
      btn.value = 'Subscribe';
      alert(JSON.stringify(err));
    });
});