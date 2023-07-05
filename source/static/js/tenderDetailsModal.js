$(document).ready(function () {
    $(document).on('click', '.find-supplier-btn', function () {
        let tenderId = $('#modal-tender_id').text();
        let offerId = $(this).data('offer-id');
        let url = '/find_supplier/' + tenderId + '/' + offerId + '/';
        let popupWindow = window.open(url, 'popup', 'width=1000px,height=600px');

        popupWindow.onunload = function () {
            $.ajax({
                url: '/get_cell_data/',
                type: 'GET',
                data: {
                    'cell_id': tenderId
                },
                success: function (data) {// Convert offer_ids to a string and join them with a comma separator
                    $('#modal-offer_ids').empty().text(data.offer_ids);  // Update the content of modal-offer_ids element
                    $('#modal-products').empty();
                    for (let i = 0; i < data.products.length; i++) {
                        let product = data.products[i];
                        let productHtml = '<div>' +
                            '<p>' + product + '</p>' +
                            '</div>';
                        $('#modal-products').append(productHtml);
                    }
                    $('#modal-suppliers').empty();
                    for (let i = 0; i < data.products.length; i++) {
                        let product = data.products[i];
                        let supplier = data.suppliers[i];
                        let offerId = data.offer_ids[i];
                        let productHtml = '<div>' +
                            '<p>' + product + ' ' + supplier + '</p>' +
                            '<button class="btn btn-primary find-supplier-btn" data-offer-id="' + offerId + '">Подобрать поставщика</>' +
                            '</div>';
                        $('#modal-suppliers').append(productHtml);
                    }

                },
                error: function (xhr, status, error) {
                }
            });
        };
    });
});

$('.modal-trigger').click(function () {
    let cellId = $(this).data('cell-id');

    $.ajax({
        url: '/get_cell_data/',
        type: 'GET',
        data: {
            'cell_id': cellId
        },
        success: function (data) {
            $('#modal-tender_id').text(data.tender_id);
            $('#modal-lot_number').text(data.lot_number);
            $('#modal-customer_name_ru').text(data.customer_name_ru);
            $('#modal-name_ru').text(data.name_ru);
            $('#modal-description_ru').text(data.description_ru);
            $('#modal-price').text(data.price);
            $('#modal-count').text(data.count);
            if (Array.isArray(data.ref_unit)) {
                $('#modal-ref_unit').text(data.ref_unit.map(function (refUnit) {
                    return refUnit.name_ru;
                }).join(', '));
            } else {
                $('#modal-ref_unit').text(data.ref_unit.name_ru);
            }
            $('#modal-amount').text(data.amount);
            $('#modal-supply_date_ru').text(data.supply_date_ru);
            $('#modal-offer_ids').empty().text(data.offer_ids);
            $('#modal-products');
            for (let i = 0; i < data.products.length; i++) {
                let product = data.products[i];
                let productHtml = '<div>' +
                    '<p>' + product + '</p>' +
                    '</div>';
                $('#modal-products').append(productHtml);
            }
            $('#modal-suppliers').empty();
            for (let i = 0; i < data.products.length; i++) {
                let product = data.products[i];
                let supplier = data.suppliers[i];
                let offerId = data.offer_ids[i];
                let productHtml = '<div>' +
                    '<p>' + product + ' ' + supplier + '</p>' +
                    '<button class="btn btn-primary find-supplier-btn" data-offer-id="' + offerId + '">Подобрать поставщика</>' +
                    '</div>';
                $('#modal-suppliers').append(productHtml);
            }

//                $('#modal-price_without_discount').text(data.price_without_discount);
            $('#modal-supplier_discount').text(data.supplier_discount);
//                $('#modal-price_with_discount').text(data.price_with_discount);
            $('#modal-vat').text(data.vat);
            $('#modal-note').text(data.note);
            $('#modal-manager').text(data.manager);
            $('#modal-purchase_price').text(data.purchase_price);
            $('#modal-overall_info').text(data.overall_info);
            $('#modal-publish_date').text(data.publish_date);
            $('#modal-end_date').text(data.end_date);
            $('#modal-ref_trade_method').text(data.ref_trade_method);
            $('#modal-paper_ad_link').text(data.paper_ad_link);
            $('#modal-lot_link').text(data.lot_link);
            $('#modal-profit_rate').text(data.profit_rate);
            $('#modal-delivery_rate').text(data.delivery_rate);
            $('#modal-purchase_price_per_unit').text(data.purchase_price_per_unit);
            $('#modal-bidding_price_per_unit').text(data.bidding_price_per_unit);
            $('#modal-budget_price_per_unit').text(data.budget_price_per_unit);
            $('#modal-overall_profit').text(data.overall_profit);
            $('#modal-overall_purchase_amount').text(data.overall_purchase_amount);
            $('#modal-overall_contract_amount').text(data.overall_contract_amount);
            $('#modal-winning_price').text(data.winning_price);
            $('#modal-commercial_offer_text').text(data.commercial_offer_text);
            $('#modal-status').text(data.status);
            $('#myModal').modal('show');
        },
        error: function (xhr, status, error) {
        }
    });
    $(document).on('click', function (e) {
        if ($(e.target).hasClass('modal')) {
            $('#myModal').modal('hide');
        }
    });
});
