// Обработчик клика по кнопке "Добавить"
document.getElementById('addEnsTruCodeButton').addEventListener('click', function () {
    // Открытие модального окна с формой добавления данных
    $('#addEnsTruCodeModal').modal('show');
});

// Обработчик клика по кнопке "Сохранить"
document.getElementById('saveEnsTruCodeButton').addEventListener('click', function () {
    // Получение данных из формы
    var ensTruCode = document.getElementById('ensTruCodeInput').value;

    // AJAX-запрос для сохранения данных
    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/save-ens-tru-code', true);
    xhr.setRequestHeader('Content-type', 'application/json');
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            // Здесь можно выполнить дополнительные действия после сохранения данных
            console.log('Код ЕНС ТРУ успешно сохранен');
            $('#addEnsTruCodeModal').modal('hide');
        }
    };
    xhr.send(JSON.stringify({ ensTruCode: ensTruCode }));
});