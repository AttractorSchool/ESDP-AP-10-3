function saveSelectedTenders() {
  var selectedTenders = [];
  var tenderCheckboxes = document.querySelectorAll('input[name="selectedTenders[]"]:checked');

  tenderCheckboxes.forEach(function (checkbox) {
    var tenderRow = checkbox.closest('.tender-row');
    console.log(tenderRow);

    var tenderData = {
      lotNumber: tenderRow.querySelector('.lot-number').textContent,
      customerNameRu: tenderRow.querySelector('.customer-name-ru').textContent,
      nameRu: tenderRow.querySelector('.name-ru').textContent,
      descriptionRu: tenderRow.querySelector('.description-ru').textContent,
      price: tenderRow.querySelector('.price').textContent.replace('KZT ', ''),
      count: tenderRow.querySelector('.count').textContent,
      refUnit: tenderRow.querySelector('.ref-unit').textContent,
      amount: tenderRow.querySelector('.amount').textContent.replace('KZT ', ''),
      supplyDateRu: tenderRow.querySelector('.supply-date-ru').textContent
    };

    selectedTenders.push(tenderData);
  });

  var requestOptions = {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ selectedTenders: selectedTenders })
  };

  fetch('/save_tenders', requestOptions)
    .then(function (response) {
      if (response.ok) {
        return response.json();
      } else {
        throw new Error('Ошибка запроса. Код ошибки: ' + response.status);
      }
    })
    .then(function (data) {
      console.log(data);
    })
    .then(function () {
        location.reload();
    })
    .catch(function (error) {
      console.log(error);
    });
}


var saveBtn = document.getElementById('saveBtn');
saveBtn.addEventListener('click', saveSelectedTenders);
