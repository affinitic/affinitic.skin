 jQuery(document).ready(function($) {
    $('a.realisation').each(function() {
        $(this).prepOverlay({
            width: '870px',
            subtype:'ajax',
            urlmatch:'#$',
			urlreplace:'realisations',
 			filter:'#'+$(this).attr("id"),
            mask: {
                color: '#000',
            },
			afterpost : function(obj)
			{
				console.log(obj);
				obj.attr('id','overlay');
			}
        });

    });
    });