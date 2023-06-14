
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
                $('#modal-ref_unit').text(data.ref_unit);
                $('#modal-amount').text(data.amount);
                $('#modal-supply_date_ru').text(data.supply_date_ru);
                $('#modal-products').text(data.products);
                $('#modal-suppliers').text(data.suppliers);
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
