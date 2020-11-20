$(document).ready(function(){
        $('input[type=text]').keyup(function(){
            return $(this).val($(this).val().toUpperCase());
        });
});
