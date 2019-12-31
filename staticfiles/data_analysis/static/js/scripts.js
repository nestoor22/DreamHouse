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

