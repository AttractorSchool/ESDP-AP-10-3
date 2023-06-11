$(document).ready(function() {
    $('#upload-form').on('submit', function(e) {
        e.preventDefault();
        var form = $(this);
        var formData = new FormData(form[0]);

        $.ajax({
            url: form.attr('action'),
            type: form.attr('method'),
            data: formData,
            processData: false,
            contentType: false,
            xhr: function() {
                var xhr = new window.XMLHttpRequest();
                xhr.upload.addEventListener('progress', function(e) {
                    if (e.lengthComputable) {
                        var percent = Math.round((e.loaded / e.total) * 100);
                        $('#progress-bar').css('width', percent + '%');
                        $('#progress-bar').text(percent + '%');
                    }
                });
                return xhr;
            },
            beforeSend: function() {
                $('#upload-button').attr('disabled', 'disabled');
                $('#progress-container').show();
                $('#progress-bar').css('width', '0%');
                $('#progress-bar').text('0%');
                $('#progress-status').text('');
            },
            success: function(data) {
                $('#progress-bar').css('width', '100%');
                $('#progress-bar').text('100%');
                $('#progress-status').text('Файл успешно загружен!');
                location.reload();
            },
            error: function(xhr, textStatus, errorThrown) {
                $('#progress-bar').css('width', '0%');
                $('#progress-bar').text('0%');
                $('#progress-status').text('Ошибка загрузки файла!');
            },
            complete: function() {
                $('#upload-button').removeAttr('disabled');
                $('#progress-container').hide();
                $('#excel-file-input').val('');
            }
        });
    });
});
