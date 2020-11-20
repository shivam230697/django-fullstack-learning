    $(document).ready(function(){
      $("#myInput").on("keyup", function() {
        var value = $(this).val().toLowerCase();
        $("#myTable tr").each(function() {
<!--          $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1);-->
               if ($(this).text().toLowerCase().indexOf(value) > -1){
                    $(this).show();
               }
               else{
                    $(this).hide();
               }

        });
      });

<!--       $("#input").on("keyup", function() {-->
<!--        var value = $(this).val().toLowerCase();-->
<!--        $("#myTable tr").each(function() {-->
<!--              if ($(this).text().toLowerCase().indexOf(value) > -1){-->
<!--                $(this).show();-->
<!--                $(this).indexOf(value);-->
<!--              }-->
<!--              else{-->
<!--                $(this).hide();-->
<!--              }-->

<!--        });-->
<!--      });-->

    });
