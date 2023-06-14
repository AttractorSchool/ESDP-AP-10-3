// Обработчик клика по кнопке "Сохранить"
document.getElementById('saveEnsTruCodeButton').addEventListener('click', function () {
    // Получение данных из формы
    var ensTruCode = document.getElementById('ensTruCodeInput').value;
    var ensTruName = document.getElementById('ensTruNameInput').value;

    // AJAX-запрос для сохранения данных
    fetch('/enstru_create', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-CSRFToken': getCookie('csrftoken')
        },
        body: 'ensTruCode=' + encodeURIComponent(ensTruCode) + '&ensTruName=' + encodeURIComponent(ensTruName)
    })
    .then(function (response) {
        if (response.ok) {
            // Здесь можно выполнить дополнительные действия после сохранения данных
            console.log('Код ЕНС ТРУ успешно сохранен');
            $('#addEnsTruCodeModal').modal('hide');

            // Обновление данных в таблице
            var tableBody = document.getElementById('EnsTruTableBody');
            var newRow = document.createElement('tr');
            var codeCell = document.createElement('td');
            codeCell.textContent = ensTruCode;
            var nameCell = document.createElement('td');
            nameCell.textContent = ensTruName;
            newRow.appendChild(codeCell);
            newRow.appendChild(nameCell);
            tableBody.appendChild(newRow);

            document.getElementById('ensTruCodeInput').value = '';
            document.getElementById('ensTruNameInput').value = '';

            document.getElementById('loadEnsTruCodesBtn').click();
        }
    })
    .catch(function (error) {
        console.error('Ошибка при выполнении AJAX-запроса:', error);
    });
});
