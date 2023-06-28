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
                success: function(data) {
                    $('#modal-tender_id').text(data.tender_id);
                    $('#modal-lot_number').text(data.lot_number);
                    $('#modal-products').text(data.products);
                    $('#modal-suppliers').text(data.suppliers);

                    $('#myModal').modal('show');
                },
                error: function(xhr, status, error) {
                }
            });
        };
    });
});


