      $(document).ready(function() {
        $('.similar-products-btn').click(function() {
            let tenderId = $('#modal-tender_id').text();
            let url = '/similar_products/' + tenderId + '/';
            window.open(url, 'popup', 'width=1000px,height=600px');
        });
    });