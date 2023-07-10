let editButton = document.querySelector('.edit-tender');
let saveButton = document.querySelector('.save-tender');

editButton.addEventListener('click', function() {
    enableEditing();
});

saveButton.addEventListener('click', function() {
    if (areFieldsHidden()) {
        toggleToEditButton();
    } else {
        saveChanges();
    }
});

function enableEditing() {
    let supplierDiscountElement = document.getElementById('modal-supplier_discount');
    let vatElement = document.getElementById('modal-vat');
    let noteElement = document.getElementById('modal-note');
    let purchasePriceElement = document.getElementById('modal-purchase_price');

    let supplierDiscountValue = supplierDiscountElement.textContent;
    supplierDiscountElement.innerHTML = '<input type="text" style="margin-left: 0px;" id="edit-supplier_discount" ' +
        'value="' + supplierDiscountValue + '">';

    let vatValue = vatElement.textContent;
    vatElement.innerHTML = '<input type="text" style="margin-left: 83px;" id="edit-vat" value="' + vatValue + '">';

    let noteValue = noteElement.textContent;
    noteElement.innerHTML = '<input type="text" style="margin-left: 20px;" id="edit-note" value="' + noteValue + '">';

    let purchasePriceValue = purchasePriceElement.textContent;
    purchasePriceElement.innerHTML = '<input type="text" style="margin-left: 20px;" id="edit-purchase_price" ' +
        'value="' + purchasePriceValue + '">';

    editButton.style.display = 'none';

    if (areFieldsHidden()) {
        toggleToEditButton();
    } else {
        saveButton.style.display = 'inline-block';
    }
}

function saveChanges() {
    let supplierDiscountElement = document.getElementById('modal-supplier_discount');
    let vatElement = document.getElementById('modal-vat');
    let noteElement = document.getElementById('modal-note');
    let purchasePriceElement = document.getElementById('modal-purchase_price');

    let updatedSupplierDiscountInput = document.getElementById('edit-supplier_discount');
    let updatedVatInput = document.getElementById('edit-vat');
    let updatedNoteInput = document.getElementById('edit-note');
    let updatedPurchasePriceInput = document.getElementById('edit-purchase_price');

    let updatedSupplierDiscount = updatedSupplierDiscountInput ? updatedSupplierDiscountInput.value : '';
    let updatedVat = updatedVatInput ? updatedVatInput.value : '';
    let updatedNote = updatedNoteInput ? updatedNoteInput.value : '';
    let updatedPurchasePrice = updatedPurchasePriceInput ? updatedPurchasePriceInput.value : '';

    let tenderId = document.getElementById('modal-tender_id').textContent.trim();
    let url = '/update_tender/';
    let csrftoken = getCookie('csrftoken');

    if (areFieldsHidden()) {
        toggleToEditButton();
        return;
    }

    $.ajax({
        url: url,
        type: 'POST',
        headers: { 'X-Requested-With': 'XMLHttpRequest' },
        data: {
            tender_id: tenderId,
            supplier_discount: updatedSupplierDiscount,
            vat: updatedVat,
            note: updatedNote,
            purchase_price: updatedPurchasePrice,
            csrfmiddlewaretoken: csrftoken
        },
        success: function(response) {
            supplierDiscountElement.textContent = response.supplier_discount;
            vatElement.textContent = response.vat;
            noteElement.textContent = response.note;
            purchasePriceElement.textContent = response.purchase_price;

            disableEditing();
        },
        error: function(response) {
            console.log('Error:', response);
        }
    });
}

function areFieldsHidden() {
    let supplierDiscountInput = document.getElementById('edit-supplier_discount');
    let vatInput = document.getElementById('edit-vat');
    let noteInput = document.getElementById('edit-note');
    let purchasePriceInput = document.getElementById('edit-purchase_price');

    return (
        (supplierDiscountInput && supplierDiscountInput.style.display === 'none') ||
        (vatInput && vatInput.style.display === 'none') ||
        (noteInput && noteInput.style.display === 'none') ||
        (purchasePriceInput && purchasePriceInput.style.display === 'none')
    );
}

function toggleToEditButton() {
    saveButton.style.display = 'none';
    editButton.style.display = 'inline-block';
}

function disableEditing() {
    editButton.style.display = 'inline-block';
    saveButton.style.display = 'none';
}
