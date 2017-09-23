$(function() {
    $( "#id_data_badania, #id_data_urodzenia, #id_data" ).datepicker({
        changeYear: true,
        maxDate: '30',
        dayNamesMin: [ "Nd", "Pn", "Wt", "Śr", "Czw", "Pt", "So" ],
        monthNames: [ "Styczeń", "Luty", "Marzec", "Kwiecień", "Maj",
        "Czerwiec", "Lipiec", "Sierpień", "Wrzesień", "Pażdziernik",
        "Listopad", "Grudzień" ],
    });

    $( "#id_start, #id_koniec" ).datetimepicker({
        changeYear: true,
        maxDate: '30',
        dayNamesMin: [ "Nd", "Pn", "Wt", "Śr", "Czw", "Pt", "So" ],
        monthNames: [ "Styczeń", "Luty", "Marzec", "Kwiecień", "Maj",
        "Czerwiec", "Lipiec", "Sierpień", "Wrzesień", "Pażdziernik",
        "Listopad", "Grudzień" ],
    });
});