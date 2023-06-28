function saveSelectedTenders() {
    let selectedTenders = [];
    let tenderCheckboxes = document.querySelectorAll('input[name="selectedTenders[]"]:checked');

    tenderCheckboxes.forEach(function (checkbox) {
        let tenderData = JSON.parse(checkbox.value)
        selectedTenders.push(tenderData);
    });

    let requestOptions = {
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

let saveBtn = document.getElementById('saveBtn');
saveBtn.addEventListener('click', saveSelectedTenders);
