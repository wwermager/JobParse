/* 
 * <copyright file=FinalCountdown.cs company="St. Cloud State University">
 * Copyright (c) 2017 All Rights Reserved
 * </copyright>
 * <author>Jose H. Chacon</author>
 * <date>2017-09-03</date>
 * <summary>EdPost Career Search</summary>
 */

//Google Analytics Code <meta name="scsu-ga" content="UA-2377225-20"> <meta name="scsu-ga-link" content="mnscu.edu" />
var scsuGa = $('meta[name=scsu-ga]').attr('content');
var scsuGaLink = $('meta[name=scsu-ga-link]').attr('content').split(',');
(function (i, s, o, g, r, a, m) {
    i['GoogleAnalyticsObject'] = r;
    i[r] = i[r] || function () {
        (i[r].q = i[r].q || []).push(arguments);
    }, i[r].l = 1 * new Date();
    a = s.createElement(o),
		m = s.getElementsByTagName(o)[0];
    a.async = 1;
    a.src = g;
    m.parentNode.insertBefore(a, m)
})(window, document, 'script', '//www.google-analytics.com/analytics.js', 'ga');
ga('create', scsuGa, 'auto');
ga('require', 'linker'); // Load linker plugin for cross domain tracking.
ga('linker:autoLink', scsuGaLink); // Add domain to the list of domains that needs to be tracked
ga('send', 'pageview');
//Google Analytics Code END

//Facebook Pixel Code <meta name="scsu-fbp" content="870818596372530">
var scsuFbp = $('meta[name=scsu-fbp]').attr('content');
! function (f, b, e, v, n, t, s) {
    if (f.fbq) return;
    n = f.fbq = function () {
        n.callMethod ? n.callMethod.apply(n, arguments) : n.queue.push(arguments);
    };
    if (!f._fbq) f._fbq = n;
    n.push = n;
    n.loaded = !0;
    n.version = '2.0';
    n.queue = [];
    t = b.createElement(e);
    t.async = !0;
    t.src = v;
    s = b.getElementsByTagName(e)[0];
    s.parentNode.insertBefore(t, s)
}(window, document, 'script', '//connect.facebook.net/en_US/fbevents.js');
fbq('init', scsuFbp);
fbq('track', "PageView");
//Facebook Pixel Code END

//Facebook Like Box Plugin
(function (d, s, id) {
    var js, fjs = d.getElementsByTagName(s)[0];
    if (d.getElementById(id)) return;
    js = d.createElement(s);
    js.id = id;
    js.src = "//connect.facebook.net/en_US/all.js#xfbml=1";
    fjs.parentNode.insertBefore(js, fjs);
}(document, 'script', 'facebook-jssdk'));
//Facebook Like Box Plugin END


$(document).ready(function () {
    var $LocationString = $('#StateCityZipString');
    var $MilesDropdown = $('#Radii');
    var $SelectedProcess = $('#process');
    var $KeyWordString = $('#KeyWordString');
    if ($LocationString.length) {
        $(function () {
            var sczvalue = $LocationString.val();
            $MilesDropdown.attr('disabled', 'disabled');
            if (sczvalue.length > 0) {
                //var check = /^\d+$/.test($LocationString.val());
                //if (check == true) {
                $MilesDropdown.removeAttr('disabled');
                //}
            } else {
                $MilesDropdown.attr('disabled', 'disabled');
            }
        });
        $(function () {
            var enterval = $KeyWordString.val();
            if (enterval.length > 0) {
                $SelectedProcess.removeAttr('disabled');
            } else {
                $SelectedProcess.attr('disabled', 'disabled');
            }
        });
        $(function () {
            $LocationString.on('input', function () {
                var sczvalue = $LocationString.val();
                if (sczvalue == "") {
                    $('#Radii option:selected').val(0);
                }
                //if (/^\d+$/.test($(this).val())) {
                if (sczvalue.length > 0) {
                    $MilesDropdown.removeAttr('disabled');
                } else {
                    $MilesDropdown.attr('disabled', 'disabled');
                }
            });
        });
        $(function () {
            $KeyWordString.on('input', function () {
                var enterval = $KeyWordString.val();
                if (enterval.length > 0) {
                    $SelectedProcess.removeAttr('disabled');
                } else {
                    $SelectedProcess.attr('disabled', 'disabled');
                }
            });
        });
        $('#btn-reset').click(function (e) {
            var $form = $(this).closest('form');
            $('#Radii option:selected').val(0);
            $form.find("input[type=text]").val("");
            $form.submit();
        });
    }
    if ($("#datetimepickerinfo").length > 0) {
        $("#datetimepickerinfo").datetimepicker(
                {
                    defaultDate: false,
                    showTodayButton: true,
                    format: 'YYYY-MM-DD',
                    showClose: true,
                    showClear: true,
                    toolbarPlacement: 'top',
                    stepping: 15
                });
    }

});