$(function() {
    $( "#id_med_check_date, #id_birth_date, #id_date" ).datepicker({
        changeYear: true,
        maxDate: '30',
        dayNamesMin: [ "Nd", "Pn", "Wt", "Śr", "Czw", "Pt", "So" ],
        monthNames: [ "Styczeń", "Luty", "Marzec", "Kwiecień", "Maj",
        "Czerwiec", "Lipiec", "Sierpień", "Wrzesień", "Pażdziernik",
        "Listopad", "Grudzień" ],
    });

    $( "#id_start, #id_end" ).datetimepicker({
        timeInput: true,
        changeYear: true,
        maxDate: '30',
        dayNamesMin: [ "Nd", "Pn", "Wt", "Śr", "Czw", "Pt", "So" ],
        monthNames: [ "Styczeń", "Luty", "Marzec", "Kwiecień", "Maj",
        "Czerwiec", "Lipiec", "Sierpień", "Wrzesień", "Pażdziernik",
        "Listopad", "Grudzień" ],
    });
});
