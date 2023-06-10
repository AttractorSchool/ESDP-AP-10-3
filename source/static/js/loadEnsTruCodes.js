document.getElementById('loadEnsTruCodesBtn').addEventListener('click', function() {
  fetch('/enstru_codes')
    .then(function(response) {
      if (response.ok) {
        return response.json();
      } else {
        throw new Error('Ошибка запроса. Код ошибки: ' + response.status);
      }
    })
    .then(function(data) {
      console.log(data);

      var tableHead = document.getElementById('EnsTruTableHead');
      tableHead.innerHTML = '';
      var headerRow = document.createElement('tr');

      var columnTitles = [
        'Код ЕНС ТРУ',
        'Наименование'
      ];

      columnTitles.forEach(function (title) {
        var columnHeader = document.createElement('th');
        columnHeader.scope = 'col';
        columnHeader.textContent = title;
        headerRow.appendChild(columnHeader);
      });

      tableHead.appendChild(headerRow);

      var tableBody = document.getElementById('EnsTruTableBody');
      tableBody.innerHTML = '';

      data.enstru_codes.forEach(function (enstru) {
        var row = document.createElement('tr');
        row.className = 'tender-row'

        var code = document.createElement('td');
        code.textContent = enstru.code || '';
        code.className = 'tender-cell code';
        row.appendChild(code);

        var name = document.createElement('td');
        name.textContent = enstru.name || '';
        name.className = 'tender-cell name';
        row.appendChild(name);

        tableBody.appendChild(row);
      });
    })
    .catch(function(error) {
      console.log(error);
    });
});
