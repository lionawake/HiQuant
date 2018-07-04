
$(document).ready(function(){

    function getScrollOpt(h){
        var opt = {
            width: '100%', //可滚动区域宽度
            height: h, //可滚动区域高度
            size: '10px', //滚动条宽度，即组件宽度
            color: '#000', //滚动条颜色
            position: 'right', //组件位置：left/right
            distance: '0px', //组件与侧边之间的距离
            start: 'top', //默认滚动位置：top/bottom
            opacity: .4, //滚动条透明度
            alwaysVisible: false, //是否 始终显示组件
            disableFadeOut: false, //是否 鼠标经过可滚动区域时显示组件，离开时隐藏组件
            railVisible: true, //是否 显示轨道
            railColor: '#333', //轨道颜色
            railOpacity: .2, //轨道透明度
            railDraggable: true, //是否 滚动条可拖动
            railClass: 'slimScrollRail', //轨道div类名 
            barClass: 'slimScrollBar', //滚动条div类名
            wrapperClass: 'slimScrollDiv', //外包div类名
            allowPageScroll: true, //是否 使用滚轮到达顶端/底端时，滚动窗口
            wheelStep: 20, //滚轮滚动量
            touchScrollStep: 200, //滚动量当用户使用手势
            borderRadius: '7px', //滚动条圆角
            railBorderRadius: '7px' //轨道圆角
        };
        return opt;
    }
    var Loader = function(){

        return {
            init: function(){
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
            $('.main-content, .panel_left').css('height', h+'px');
            $('.mask').height($(window).height()-180);
            var pEditor=CodeMirror.fromTextArea(document.getElementById("pContent"),{
                mode:"text/x-python",
                lineNumbers:true,
                theme:"blackboard"
            });
            $('.CodeMirror, .CodeMirror-scroll').css('height', h+'px');
            //滚动条
            $('.panel_paper').slimScroll(getScrollOpt( h ) );
        }

        return {
            init: function(){
                // console.log( zxCookie.getCookieValue(zxCookie.ACCT));
                setView();
                APPUtils.init_base();
                $('.lable_account').text( zxCookie.getCookieValue(zxCookie.ACCT).u );
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