$(document).ready(function(){
    $(".sidebar-btn").click(function(){

        if( $(".base-sidebar").css('left') == '0px') {
            $(".base-sidebar span").removeClass('glyphicon glyphicon-remove');

            $(".base-sidebar span").addClass('glyphicon glyphicon-align-justify');

        }
        if( $(".base-sidebar").css('left') != '0px') {
            $(".base-sidebar span").removeClass('glyphicon glyphicon-align-justify');
            $(".base-sidebar span").addClass('glyphicon glyphicon-remove');


        }

        $(".base-sidebar").toggleClass("active");





    });
});