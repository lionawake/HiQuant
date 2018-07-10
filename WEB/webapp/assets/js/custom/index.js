
$(document).ready(function(){

    var Loader = function(){
        function findStatus(){
            ZX.getDataByAjax(
                "../lq/spt/findStatus",
                "json",
                function(res){
                    if(res==null){
                        event_dialog.alert('查找任务状态出错!');
                        $(".data").text(0);
                    }else{
                        $(".waiting").text(res.status0==null?0:res.status0);
                        $(".running").text(res.status1==null?0:res.status1);
                        $(".fin").text(res.status2==null?0:res.status2);
                    }
                },
                function(){
                    event_dialog.alert('查找任务状态出错!');
                    $(".data").text(0);
                }
            );
        }
        return {
            init: function(){
                findStatus();
            }
        }
    }();


    var Event = function(){
        function click_menus(){
            $('.menus li').click( function(){
                $('.menus li').removeClass('active');
                $(this).addClass('active');
                $('#iframe_main').attr('src', $(this).attr('ref'));
            });
            $('.menus li').eq(0).trigger("click");
        }
        return {
            init: function(){
                click_menus();
            }
        }
    }();

    var View = function(){

        function setView(){
            var h = $(window).height()-90;
            $('.main-content, .sidebar, #iframe_main').css('height', h+'px');
            $('.main-content').css('width', ($(window).width()-265)+'px');
            $('.mask').height($(window).height()-180);
            // $("#iframe_main").iframe_autoresize({
            //     "height":h,  
            //     "width": 1,
            //     "woffset": 265,
            //     "hoffset": $('.navbar').height()
            // });
        }

        return {
            init: function(){
                // console.log( zxCookie.getCookieValue(zxCookie.ACCT));
                setView();
                APPUtils.init_base();
                $('.lable_account').text( zxCookie.getCookieValue(zxCookie.ACCT).u );
                var r = zxCookie.getCookieValue(zxCookie.ACCT).r;
                if(r!=0 && r!=1){
                    $("#btn_actManager").parent().remove();
                }else{
                    $("#btn_actManager").removeClass("hide");
                }
                Loader.init();
                Event.init();
            },
            closeMask: function(){
                $('.mask').addClass('hidden');
            }
        }
    }();

    View.init();
});