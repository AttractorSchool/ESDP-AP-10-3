let modal = document.getElementById("myModal");
  let modalText = document.getElementById("modal-text");
  let closeButton = document.getElementsByClassName("close")[0];
  let modalContent = document.querySelector('.modal-content');
  let tableTender = document.getElementById('tenderTable');

  function closeModal() {
    modal.style.display = "none";
    modalContent.style.overflowY = 'hidden';
  }

 tableTender.addEventListener("click", function(event) {
  if (event.target.classList.contains("modal-trigger")) {
    let proposedProductName = event.target.getAttribute("data-proposed-product-name");
    let supplier = event.target.getAttribute("data-supplier");
    let supplierDiscount = event.target.getAttribute("data-supplier-discount");
    let vat = event.target.getAttribute("data-vat");
    let note = event.target.getAttribute("data-note");
    let manager = event.target.getAttribute("data-manager");
    let purchasePrice = event.target.getAttribute("data-purchase-price");
    let overallInfo = event.target.getAttribute("data-overall-info");
    let date = event.target.getAttribute("data-date");
    let deadline = event.target.getAttribute("data-deadline");
    let procurementType = event.target.getAttribute("data-procurement-type");
    let paperAdLink = event.target.getAttribute("data-paper-ad-link");
    let lotLink = event.target.getAttribute("data-lot-link");
    let profitRate = event.target.getAttribute("data-profit-rate");
    let deliveryRate = event.target.getAttribute("data-delivery-rate");
    let purchasePricePerUnit = event.target.getAttribute("data-purchase-price-per-unit");
    let biddingPricePerUnit = event.target.getAttribute("data-bidding-price-per-unit");
    let budgetPricePerUnit = event.target.getAttribute("data-budget-price-per-unit");
    let overallProfit = event.target.getAttribute("data-overall-profit");
    let overallPurchaseAmount = event.target.getAttribute("data-overall-purchase-amount");
    let overallContractAmount = event.target.getAttribute("data-overall-contract-amount");
    let winningPrice = event.target.getAttribute("data-winning-price");
    let commercialOfferText = event.target.getAttribute("data-commercial-offer-text");
    let status = event.target.getAttribute("data-status");

    let contentHTML =
                      '<br><strong>Предложенное наименование продукта:</strong> ' + proposedProductName +
                      '<br><strong>Поставщик:</strong> ' + supplier +
                      '<br><strong>Скидка поставщика:</strong> ' + supplierDiscount +
                      '<br><strong>НДС:</strong> ' + vat +
                      '<br><strong>Примечание:</strong> ' + note +
                      '<br><strong>Менеджер:</strong> ' + manager +
                      '<br><strong>Цена закупки:</strong> ' + purchasePrice +
                      '<br><strong>Общая информация:</strong> ' + overallInfo +
                      '<br><strong>Дата:</strong> ' + date +
                      '<br><strong>Дедлайн:</strong> ' + deadline +
                      '<br><strong>Тип закупки:</strong> ' + procurementType +
                      '<br><strong>Ссылка на бумажное объявление:</strong> ' + paperAdLink +
                      '<br><strong>Ссылка на лот:</strong> ' + lotLink +
                      '<br><strong>Процент прибыли:</strong> ' + profitRate +
                      '<br><strong>Процент доставки:</strong> ' + deliveryRate +
                      '<br><strong>Цена закупки за единицу:</strong> ' + purchasePricePerUnit +
                      '<br><strong>Цена конкурентной заявки за единицу:</strong> ' + biddingPricePerUnit +
                      '<br><strong>Цена бюджетной заявки за единицу:</strong> ' + budgetPricePerUnit +
                      '<br><strong>Общая прибыль:</strong> ' + overallProfit +
                      '<br><strong>Общая сумма закупки:</strong> ' + overallPurchaseAmount +
                      '<br><strong>Общая сумма контракта:</strong> ' + overallContractAmount +
                      '<br><strong>Цена победителя:</strong> ' + winningPrice +
                      '<br><strong>Текст коммерческого предложения:</strong> ' + commercialOfferText +
                      '<br><strong>Статус:</strong> ' + status;

    modalText.innerHTML = contentHTML;
    modal.style.display = "block";
    modalContent.style.overflowY = 'hidden';
  }
});


  closeButton.addEventListener("click", closeModal);
  window.addEventListener("click", function (event) {
    if (event.target == modal) {
      closeModal();
    }
  });