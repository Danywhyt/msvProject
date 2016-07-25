/**
 * Created by Dany on 18/07/2016.
 */
$(document).ready(function () {

    $('#search').click(function () {
        $('#search').hide();
        $('#div-src').show(1,function () {
            $('#btn-src').show(1,function () {
                ani = $('#input-src');
                ani.show();
                ani.animate({
                    width: 150+'px'

                });
            });
        });
        return false
    });

    $('#close-src').click(function () {
        $('#div-src').hide(2,function () {
            $('#btn-src').hide();
            $('#input-src').animate({
                width:0+'px'

            });
            $('#search').show(1)
        })


    });
});