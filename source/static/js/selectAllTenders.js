let selectAllCheckbox = document.getElementById('selectAll');
let tenderCheckboxes = document.querySelectorAll('input[name="selectedTenders[]"]');

if (selectAllCheckbox){
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
}
