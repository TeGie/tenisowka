$(function() {

    function autoSet(){
        $('.wynik1').each(function(i,e){
            var punkty = $(this).val();
            $('#id_set_'+(i+1)+'_zaw_2').val(-punkty);
        });
    }
    $('.wynik1').bind('click keyup', autoSet);

    function autoWynik1(){
        var wyniki = $('.wynik1'),
            wynik = 0;
        $.each(wyniki, function(i,e){
            if ($(this).val() > 0){
                wynik += 1;
            }
        });
        $('#id_wynik_zaw_1').val(wynik);
    }
    $('#id_wynik_zaw_1').click(autoWynik1);
    $('.wynik1').bind('click keyup', autoWynik1);

    function autoWynik2(){
        var wyniki = $('.wynik2');
            wynik = 0;
        $.each(wyniki, function(i,e){
            if ($(this).val() > 0){
                wynik += 1;
            }
        });
        $('#id_wynik_zaw_2').val(wynik);
    }
    $('#id_wynik_zaw_2').click(autoWynik2);
});