 jQuery(document).ready(function($) {
    $('a.realisation').each(function() {
		console.log($(this).attr("id")+">*");
        $(this).prepOverlay({
            width: '870px',
            subtype:'ajax',
            urlmatch:'#$',
			urlreplace:'realisations',
 			filter:'#'+$(this).attr("id")+">*",
            mask: {
                color: '#000',
            },
        });

    });
    });