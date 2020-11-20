$(document).ready(function(){
      $("#id_gross_weight, #id_tare_weight").on("keyup", function() {
        var net_weight = $("#id_gross_weight").val() - $("#id_tare_weight").val()
        $("#id_net_weight").val(net_weight);
      });

      $('input[type=text]').keyup(function(){
            return $(this).val($(this).val().toUpperCase());
        });
});