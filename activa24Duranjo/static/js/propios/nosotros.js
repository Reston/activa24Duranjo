$(document).ready(function(){
    $("#slideUno").carouFredSel({
        circular    : true,
        infinite    : true,
        direction   : "up",
        width       : "auto",     // automatically calculated
        height      : "auto",     // automatically calculated
        align       : "center",
        padding     : 0,
        items       : {
            visible         : 1,     //  automatically calculated
            width           : "auto",     //  automatically calculated
            height          : "auto"     //  automatically calculated
        },
        scroll      : {
            items           : 1,     //  items.visible
            fx              : "fade",
            easing          : "swing",
            duration        : 500
        },
        auto        : {
            play            : true,
            timeoutDuration : 2500,     //  5 * auto.duration
            delay           : 0,
            pauseOnHover    : true     //  scroll.pauseOnHover
        }
    });
    $("#slideDos").carouFredSel({
        circular    : true,
        infinite    : true,
        direction   : "up",
        width       : "auto",     // automatically calculated
        height      : "auto",     // automatically calculated
        align       : "center",
        padding     : 0,
        items       : {
            visible         : 1,     //  automatically calculated
            width           : "auto",     //  automatically calculated
            height          : "auto"     //  automatically calculated
        },
        scroll      : {
            items           : 1,     //  items.visible
            fx              : "fade",
            easing          : "swing",
            duration        : 500
        },
        auto        : {
            play            : true,
            timeoutDuration : 2500,     //  5 * auto.duration
            delay           : 0,
            pauseOnHover    : true     //  scroll.pauseOnHover
        }
    });
    $("#slideTres").carouFredSel({
        circular    : true,
        infinite    : true,
        direction   : "up",
        width       : "auto",     // automatically calculated
        height      : "auto",     // automatically calculated
        align       : "center",
        padding     : 0,
        items       : {
            visible         : 1,     //  automatically calculated
            width           : "auto",     //  automatically calculated
            height          : "auto"     //  automatically calculated
        },
        scroll      : {
            items           : 1,     //  items.visible
            fx              : "fade",
            easing          : "swing",
            duration        : 500
        },
        auto        : {
            play            : true,
            timeoutDuration : 2500,     //  5 * auto.duration
            delay           : 0,
            pauseOnHover    : true     //  scroll.pauseOnHover
        }
    });

});