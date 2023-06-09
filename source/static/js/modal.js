
    $('.modal-trigger').click(function () {
        let cellId = $(this).data('cell-id');

        $.ajax({
            url: '/get_cell_data/',
            type: 'GET',
            data: {
                'cell_id': cellId
            },
            success: function (data) {
                $('#modal-lot').text(data.lot);
                $('#modal-company').text(data.company);
                $('#modal-name').text(data.name);
                $('#modal-price_per_unit').text(data.price_per_unit);
                $('#modal-quantity').text(data.quantity);
                $('#modal-planned_amount').text(data.planned_amount);
                $('#modal-delivery_deadline').text(data.delivery_deadline);
                $('#modal-proposed_product_name').text(data.proposed_product_name);
                $('#modal-supplier').text(data.supplier);
                $('#modal-price_without_discount').text(data.price_without_discount);
                $('#modal-supplier_discount').text(data.supplier_discount);
                $('#modal-price_with_discount').text(data.price_with_discount);
                $('#modal-vat').text(data.vat);
                $('#modal-note').text(data.note);
                $('#modal-manager').text(data.manager);
                $('#modal-purchase_price').text(data.purchase_price);
                $('#modal-date').text(data.date);
                $('#modal-deadline').text(data.deadline);
                $('#modal-procurement_type').text(data.procurement_type);
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
