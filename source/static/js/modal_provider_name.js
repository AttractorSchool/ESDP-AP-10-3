let buttons = document.querySelectorAll('td.modal-provider-name button[data-target="#myCustomModal"]');


  buttons.forEach(function(button) {
    button.addEventListener('click', function() {
      let modal = document.getElementById('myCustomModal');
      modal.style.display = 'block';


      let closeButton = document.querySelector('#myCustomModal .custom-close');
      closeButton.addEventListener('click', function() {
        modal.style.display = 'none';
      });
    });
  });

document.querySelector('.custom-close').addEventListener('click', function() {
    let modal = document.getElementById('myCustomModal');
    modal.style.display = "none";
});

window.addEventListener('click', function(event) {
    let modal = document.getElementById('myCustomModal');
    if (event.target === modal) {
        modal.style.display = 'none';
    }
});

