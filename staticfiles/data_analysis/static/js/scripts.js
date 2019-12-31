$(document).ready(function () {
    const countbox = ".graph_photo";
    $(window).on("scroll load resize", function () {
        const w_top = $(window).scrollTop();
        const e_top = $(countbox).offset().top;
        const w_height = $(window).height();
        const d_height = $(document).height();
        const e_height = $(countbox).outerHeight();
        if (w_top + 500 >= e_top || w_height + w_top == d_height || e_height + e_top < w_height) {
            $('.graphs_title').delay(2000).animate({'opacity':1}, 'slow');
            $('.graph_photo').delay(3000).animate({'opacity':1}, 'slow');
        }
    });
});

$(document).ready(function(){
    $('.sidenav').sidenav();
});

$('.switch_link').click(function(){
    const y = $(window).scrollTop();
    $('html, body').animate({ scrollTop: y + 400 }, 2000)
});

// $(document).ready(function () {
//     let show = true;
//     const countbox = ".benefits__inner";
//     $(window).on("scroll load resize", function () {
//         if (!show) return false;
//         const w_top = $(window).scrollTop();
//         const e_top = $(countbox).offset().top;
//         const w_height = $(window).height();
//         const d_height = $(document).height();
//         const e_height = $(countbox).outerHeight();
//         if (w_top + 500 >= e_top || w_height + w_top == d_height || e_height + e_top < w_height) {
//             $('.benefits__number').css('opacity', '1');
//             $('.benefits__number').spincrement({
//                 thousandSeparator: "",
//                 duration: 1200
//             });
//             show = false;
//         }
//     });
// });

$(document).ready(function(){
$('.tabs').tabs();
});

$(document).ready(function () {
    let show = true;
    const countbox = ".stats_value";
    $(window).on("scroll load resize", function () {
        if (!show)  $(this).text($(this).text()+ ' proposals');
        const w_top = $(window).scrollTop();
        const e_top = $(countbox).offset().top;
        const w_height = $(window).height();
        const d_height = $(document).height();
        const e_height = $(countbox).outerHeight();
        if (w_top + 500 >= e_top || w_height + w_top == d_height || e_height + e_top < w_height) {
            $('.stats_value').each(function () {
                $(this).prop('Counter', 0).animate({
                    Counter: $(this).text()
                }, {
                    duration: 5000,
                    easing: 'swing',
                    step: function (now) {
                        var thousands = Math.floor(Math.ceil(now) / 1000);
                        if (thousands === 0) {
                            $(this).text(Math.ceil(now) + '  proposals');
                        } else {
                            var hundreds = Math.ceil(now) % 1000;
                            if (!isNaN(thousands)){
                                $(this).text(thousands + ' ' + hundreds + '  proposals');
                            }
                        }
                    }
                });
            });
        }
        show = false;
    });
});

$(document).ready(function () {
    let show = true;
    const countbox = ".price_value";
    $(window).on("scroll load resize", function () {
        if (!show)  $(this).text($(this).text()+ ' proposals');
        const w_top = $(window).scrollTop();
        const e_top = $(countbox).offset().top;
        const w_height = $(window).height();
        const d_height = $(document).height();
        const e_height = $(countbox).outerHeight();
        if (w_top + 500 >= e_top || w_height + w_top == d_height || e_height + e_top < w_height) {
            $('.price_value').each(function () {
                $(this).prop('Counter', 0).animate({
                    Counter: $(this).text()
                }, {
                    duration: 3000,
                    easing: 'swing',
                    step: function (now) {
                        var thousands = Math.floor(Math.ceil(now) / 1000);
                        if (thousands === 0) {
                            $(this).text(Math.ceil(now) + '  $');
                        } else {
                            var hundreds = Math.ceil(now) % 1000;
                            if (!isNaN(thousands)){
                                if (hundreds===0){
                                    hundreds = '000';
                                }
                                $(this).text(thousands + ' ' + hundreds + '  $');
                            }
                        }
                    }
                });
            });
        }
        show = false;
    });
});

$(document).ready(function () {
    let show = true;
    const countbox = ".area_value";
    $(window).on("scroll load resize", function () {
        if (!show)  $(this).text($(this).text()+ ' m²');
        const w_top = $(window).scrollTop();
        const e_top = $(countbox).offset().top;
        const w_height = $(window).height();
        const d_height = $(document).height();
        const e_height = $(countbox).outerHeight();
        if (w_top + 500 >= e_top || w_height + w_top == d_height || e_height + e_top < w_height) {
            $('.area_value').each(function () {
                $(this).prop('Counter', 0).animate({
                    Counter: $(this).text()
                }, {
                    duration: 5000,
                    easing: 'swing',
                    step: function (now) {
                        var thousands = Math.floor(Math.ceil(now) / 1000);
                        if (thousands === 0) {
                            $(this).text(Math.ceil(now) + '  m²');
                        } else {
                            var hundreds = Math.ceil(now) % 1000;
                            if (!isNaN(thousands)){
                                if (hundreds===0){
                                    hundreds = '000';
                                }
                                $(this).text(thousands + ' ' + hundreds + '  m²');
                            }
                        }
                    }
                });
            });
        }
        show = false;
    });
});