$(document).ready(function() {
    $('.similar-products-btn').click(function() {
        let tenderId = $('#modal-tender_id').text();
        let url = '/similar_products/' + tenderId + '/';
        let popupWindow = window.open(url, 'popup', 'width=1000px,height=600px');

        popupWindow.onunload = function() {
            $.ajax({
                url: '/get_cell_data/',
                type: 'GET',
                data: {
                    'cell_id': tenderId
                },
                success: function(data) {// Convert offer_ids to a string and join them with a comma separator
                    $('#modal-offer_ids').empty().text(data.offer_ids);  // Update the content of modal-offer_ids element
                    $('#modal-products').empty();
                        for (let i = 0; i < data.products.length; i++) {
                        let product = data.products[i];
                        let productHtml = '<div>'+
                            '<p>' + product + '</p>' +
                            '</div>';
                        $('#modal-products').append(productHtml);
                    }
                    $('#modal-suppliers').empty();
                        for (let i = 0; i < data.products.length; i++) {
                        let product = data.products[i];
                        let supplier = data.suppliers[i];
                        let offerId = data.offer_ids[i];
                        let productHtml = '<div>'+
                            '<p>' + product + ' ' + supplier + '</p>' +
                            '<button class="btn btn-primary find-supplier-btn" data-offer-id="' + offerId + '">Подобрать поставщика</>' +
                            '</div>';
                        $('#modal-suppliers').append(productHtml);
                    }

                },
                error: function(xhr, status, error) {
                }
            });
        };
    });
});


