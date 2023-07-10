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
       //start header
      var tenderCount = data.tenders.length;
      var tenderCountElement = document.getElementById('tenderCount');
      tenderCountElement.textContent = 'Количество объявлений: ' + tenderCount;
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
        '№ объявления',
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
      //header end

      var tableBody = document.getElementById('tenderTableBody');
      tableBody.innerHTML = '';

      data.tenders.forEach(function (tender) {
        var row = document.createElement('tr');
        row.className = 'tender-row'

        var checkboxCell = document.createElement('td');
        var checkboxInput = document.createElement('input')

        checkboxInput.type = 'checkbox';
        checkboxInput.className = 'form-check-input';
        checkboxInput.name = 'selectedTenders[]';
        checkboxInput.value = JSON.stringify(tender)
        checkboxCell.appendChild(checkboxInput);
        row.appendChild(checkboxCell);

        var tenderNumber = document.createElement('td');
        tenderNumber.textContent = tender.numberAnno || '';
        tenderNumber.className = 'tender-cell tender-number';
        row.appendChild(tenderNumber);

        tableBody.appendChild(row);

        if (tender.Lots && tender.Lots.length > 0) {
            tender.Lots.forEach(function (tender) {
                var row2 = document.createElement('tr');
                row2.className = 'tender-row'

                var empty1 = document.createElement('td');
                empty1.textContent = '';
                row2.appendChild(empty1);

                var empty2 = document.createElement('td');
                empty2.textContent = '';
                row2.appendChild(empty2);

                var lotNumber = document.createElement('td');
                lotNumber.textContent = tender.lotNumber || '';
                lotNumber.className = 'tender-cell lot-number';
                row2.appendChild(lotNumber);

                var customerNameRu = document.createElement('td');
                customerNameRu.textContent = tender.customerNameRu || '';
                customerNameRu.className = 'tender-cell customer-name-ru';
                row2.appendChild(customerNameRu);

                var nameRu = document.createElement('td');
                nameRu.textContent = tender.nameRu || '';
                nameRu.className = 'tender-cell name-ru';
                row2.appendChild(nameRu);

                var descriptionRu = document.createElement('td');
                descriptionRu.textContent = tender.descriptionRu || '';
                descriptionRu.className = 'tender-cell description-ru';
                row2.appendChild(descriptionRu);

                var price = document.createElement('td');
                price.textContent = tender.Plans && tender.Plans[0] && tender.Plans[0].price || '';
                price.className = 'tender-cell price';
                row2.appendChild(price);

                var count = document.createElement('td');
                count.textContent = tender.Plans && tender.Plans[0] && tender.Plans[0].count || '';
                count.className = 'tender-cell count';
                row2.appendChild(count);

                var refUnit = document.createElement('td');
                refUnit.textContent = tender.Plans && tender.Plans[0] && tender.Plans[0].RefUnits && tender.Plans[0].RefUnits.nameRu || '';
                refUnit.className = 'tender-cell ref-unit';
                row2.appendChild(refUnit);

                var amount = document.createElement('td');
                amount.textContent = tender.Plans && tender.Plans[0] && tender.Plans[0].amount || '';
                amount.className = 'tender-cell amount';
                row2.appendChild(amount);

                var supplyDateRu = document.createElement('td');
                supplyDateRu.textContent = tender.Plans && tender.Plans[0] && tender.Plans[0].supplyDateRu || '';
                supplyDateRu.className = 'tender-cell supply-date-ru';
                row2.appendChild(supplyDateRu);

                tableBody.appendChild(row2);
            })
        }
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
