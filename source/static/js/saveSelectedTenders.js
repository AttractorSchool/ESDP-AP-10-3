function saveSelectedTenders() {
  var selectedTenders = [];
  var tenderCheckboxes = document.querySelectorAll('input[name="selectedTenders[]"]:checked');

  tenderCheckboxes.forEach(function (checkbox) {

    console.log(checkbox.value)

//    var tenderRow = checkbox.closest('.tender-row');
//    console.log(tenderRow);
//
//    var tenderData = {
//      trdBuyNumberAnno: tenderRow.querySelector('.tender-number').textContent,
//      lotNumber: tenderRow2.querySelector('.lot-number').textContent,
//      customerNameRu: tenderRow2.querySelector('.customer-name-ru').textContent,
//      nameRu: tenderRow2.querySelector('.name-ru').textContent,
//      descriptionRu: tenderRow2.querySelector('.description-ru').textContent,
//      price: tenderRow2.querySelector('.price').textContent.replace('KZT ', ''),
//      count: tenderRow2.querySelector('.count').textContent,
//      refUnit: tenderRow2.querySelector('.ref-unit').textContent,
//      amount: tenderRow2.querySelector('.amount').textContent.replace('KZT ', ''),
//      supplyDateRu: tenderRow2.querySelector('.supply-date-ru').textContent
//    };
//    console.log(tenderData);
//
    selectedTenders.push(checkbox.value);
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
//    .then(function () {
//        location.reload();
//    })
    .catch(function (error) {
      console.log(error);
    });
}


var saveBtn = document.getElementById('saveBtn');
saveBtn.addEventListener('click', saveSelectedTenders);
