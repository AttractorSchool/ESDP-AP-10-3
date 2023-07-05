$(document).ready(function() {
    $("#datepicker").datepicker({
      onSelect: function(date) {
        $.ajax({
          url: "/your-backend-url/",
          method: "POST",
          data: {
            selected_date: date
          },
          success: function(response) {
            // Обработка успешного ответа от backend
          },
          error: function(xhr) {
            // Обработка ошибки
          }
        });
      }
    });
});
