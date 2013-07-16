$(document).ready(function(){
    $("#slideUno").carouFredSel({
        circular    : true,
        infinite    : true,
        direction   : "up",
        width       : 510,     // automatically calculated
        height      : 322,     // automatically calculated
        align       : "center",
        padding     : 0,
        items       : {
            visible         : 1,     //  automatically calculated
            width           : 510,     //  automatically calculated
            height          : 322     //  automatically calculated
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
        width       : 510,     // automatically calculated
        height      : 322,     // automatically calculated
        align       : "center",
        padding     : 0,
        items       : {
            visible         : 1,     //  automatically calculated
            width           : 510,     //  automatically calculated
            height          : 322     //  automatically calculated
        },
        scroll      : {
            items           : 1,     //  items.visible
            fx              : "fade",
            easing          : "swing",
            duration        : 400
        },
        auto        : {
            play            : true,
            timeoutDuration : 2000,     //  5 * auto.duration
            delay           : 0,
            pauseOnHover    : true     //  scroll.pauseOnHover
        }
    });
    $("#slideTres").carouFredSel({
        circular    : true,
        infinite    : true,
        direction   : "up",
        width       : 510,     // automatically calculated
        height      : 322,     // automatically calculated
        align       : "center",
        padding     : 0,
        items       : {
            visible         : 1,     //  automatically calculated
            width           : 510,     //  automatically calculated
            height          : 322     //  automatically calculated
        },
        scroll      : {
            items           : 1,     //  items.visible
            fx              : "fade",
            easing          : "swing",
            duration        : 350
        },
        auto        : {
            play            : true,
            timeoutDuration : 1800,     //  5 * auto.duration
            delay           : 0,
            pauseOnHover    : true     //  scroll.pauseOnHover
        }
    });


});