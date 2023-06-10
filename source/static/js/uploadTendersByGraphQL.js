function fetchData() {
  var searchValue = document.getElementById('searchValueInput').value;
  var data = {
    search_value: searchValue
  };

  var requestOptions = {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(data)
  };

  fetch('/parse_tenders', requestOptions)
    .then(function (response) {
      if (response.ok) {
        return response.json();
      } else {
        throw new Error('Ошибка запроса. Код ошибки: ' + response.status);
      }
    })
    .then(function (data) {
      console.log(data);

      var tableHead = document.getElementById('tenderTableHead');
      tableHead.innerHTML = '';

      var headerRow = document.createElement('tr');

      var checkboxCell = document.createElement('th');
      var checkboxInput = document.createElement('input');
      checkboxInput.type = 'checkbox';
      checkboxInput.className = 'form-check-input';
      checkboxInput.id = 'selectAll';
      var checkboxLabel = document.createElement('label');
      checkboxLabel.htmlFor = 'selectAll';
      checkboxLabel.textContent = 'Все';

      checkboxCell.appendChild(checkboxInput);
      checkboxCell.appendChild(checkboxLabel);
      headerRow.appendChild(checkboxCell);

      var columnTitles = [
        '№ лота',
        'Учреждение',
        'Наименование',
        'Доп. инфо Т.С.',
        'Цена за единицу',
        'Количество',
        'Единица измерения',
        'Плановая сумма',
        'Срок поставки'
      ];

      columnTitles.forEach(function (title) {
        var columnHeader = document.createElement('th');
        columnHeader.scope = 'col';
        columnHeader.textContent = title;
        headerRow.appendChild(columnHeader);
      });

      tableHead.appendChild(headerRow);

      var tableBody = document.getElementById('tenderTableBody');
      tableBody.innerHTML = '';

      data.tenders.forEach(function (tender) {
        var row = document.createElement('tr');
        row.className = 'tender-row'

        var checkboxCell = document.createElement('td');
        var checkboxInput = document.createElement('input');
        checkboxInput.type = 'checkbox';
        checkboxInput.className = 'form-check-input';
        checkboxInput.name = 'selectedTenders[]';
        checkboxInput.value = tender.id;
        checkboxCell.appendChild(checkboxInput);
        row.appendChild(checkboxCell);

        var lotNumber = document.createElement('td');
        lotNumber.textContent = tender.lotNumber || '';
        lotNumber.className = 'tender-cell lot-number';
        row.appendChild(lotNumber);

        var customerNameRu = document.createElement('td');
        customerNameRu.textContent = tender.customerNameRu || '';
        customerNameRu.className = 'tender-cell customer-name-ru';
        row.appendChild(customerNameRu);

        var nameRu = document.createElement('td');
        nameRu.textContent = tender.nameRu || '';
        nameRu.className = 'tender-cell name-ru';
        row.appendChild(nameRu);

        var descriptionRu = document.createElement('td');
        descriptionRu.textContent = tender.descriptionRu || '';
        descriptionRu.className = 'tender-cell description-ru';
        row.appendChild(descriptionRu);

        var price = document.createElement('td');
        price.textContent = (tender.Plans && tender.Plans[0] && tender.Plans[0].amount != 0) ? 'KZT ' + tender.Plans[0].amount : '';
        price.className = 'tender-cell price';
        row.appendChild(price);

        var count = document.createElement('td');
        count.textContent = tender.Plans && tender.Plans[0] && tender.Plans[0].count || '';
        count.className = 'tender-cell count';
        row.appendChild(count);

        var refUnit = document.createElement('td');
        refUnit.textContent = tender.Plans && tender.Plans[0] && tender.Plans[0].RefUnits && tender.Plans[0].RefUnits.nameRu || '';
        refUnit.className = 'tender-cell ref-unit';
        row.appendChild(refUnit);

        var amount = document.createElement('td');
        amount.textContent = (tender.Plans && tender.Plans[0] && tender.Plans[0].amount != 0) ? 'KZT ' + tender.Plans[0].amount : '';
        amount.className = 'tender-cell amount';
        row.appendChild(amount);

        var supplyDateRu = document.createElement('td');
        supplyDateRu.textContent = tender.Plans && tender.Plans[0] && tender.Plans[0].supplyDateRu || '';
        supplyDateRu.className = 'tender-cell supply-date-ru';
        row.appendChild(supplyDateRu);


        tableBody.appendChild(row);
      });
    })

    .then(function () {
      var tenderCells = document.querySelectorAll('.tender-cell');

      tenderCells.forEach(function(cell) {
        cell.addEventListener('click', function() {
          if (this.classList.contains('expanded')) {
            this.classList.remove('expanded');
          } else {
            this.classList.add('expanded');
          }
        });
      });
    })

    .then(function () {
    var selectAllCheckbox = document.getElementById('selectAll');
    var tenderCheckboxes = document.querySelectorAll('input[name="selectedTenders[]"]');

    selectAllCheckbox.addEventListener('change', function () {
        if (this.checked) {
            tenderCheckboxes.forEach(function (checkbox) {
                checkbox.checked = true;
            });
        } else {
            tenderCheckboxes.forEach(function (checkbox) {
                checkbox.checked = false;
            });
        }
});
    })

    .catch(function (error) {
      console.log(error);
    });
}

var loadTendersBtn = document.getElementById('loadTendersBtn');
loadTendersBtn.addEventListener('click', fetchData);
