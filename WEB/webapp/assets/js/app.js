/*--------------------------------------------------------------------
 *JAVASCRIPT "app.js"
 *Version:    1.0.0 - 2017
 *author:     Andrew
 *target:     school system(2B)
-----------------------------------------------------------------------*/

/* -------------------------------- -------------------------- -------------------------- -------------------------- 

 app 1.0.0
 for APP

-------------------------------- -------------------------- -------------------------- -------------------------- */

var event_dialog = function(){
    return {
        alert: function(str){
            var d = dialog({
                title: '消息',
                content: str,
                button: [{
                        value: '确定'
                    }
                ]
            });

            d.showModal();
        },
        confirm: function( fn, us, content, btnName){
            var d = dialog({
                title: '消息',
                content: content,
                button: [{
                        value: btnName,
                        callback: function () {
                            var that = this;
                            if( fn != undefined){
                                that.title('提交中..');
                                fn(us);
                            }
                            return true;
                        },
                        autofocus: true
                    },{
                        value: '取消'
                    }
                ]
            });

            d.showModal();
        }
    }
}();

var APP_CONST = function(){
    return {
        ISDEBUG: 0,
        WEBROOT: '',
        LOGINURI: 'login.html',
        getCopyrightInfo:function(){
            return ""
        },
        SESSION_TIME_OUT : '登录已超时，请重新登录.',

       }
}();

var APPUtils = function(){

    //登录
    function handler_login(){
        //用户登录
        function handler_login(){
            
            var $u = $('#login_username'),
                $p = $('#login_p_v'),
                $ph = $('#login_p');
                
            function validate_login(){
                $('.err').show().hide();
                // var reg_mail = /^\w+((-\w+)|(\.\w+))*\@[A-Za-z0-9]+((\.|-)[A-Za-z0-9]+)*\.[A-Za-z0-9]+$/; //验证邮箱的正则表达式
                // if( !reg_mail.test( $u.val() ) ){
                //     $('.luerr_format').hide().show();
                //     return false;
                // }
                if( $.trim( $u.val()).length == 0 ){
                    $('.luerr').hide().show();
                    return false;
                }
                if( $.trim( $p.val()).length == 0 ){
                    $('.lperr').hide().show();
                    return false;
                }
                return true;
            }
            function validate_vc(){
                if( $('.login_vc_p').hasClass('active')){
                    var cvc = 'cvc='+$('#input_vc').val();
                    console.log(cvc);
                    if( $.trim( cvc).length == 0){
                        return false;
                    }
                    var result = false;
                    ZX.postDataByAjax(
                        'sup/cvc?'+cvc,
                        null,
                        function(){
                            result = true;
                        }
                    );
                    return result;
                }else{
                    return true;
                }
            }
            //清除操作
            $u.on( 'input', function(){
                $('.lerr').show().hide();
                $p.val('');
            });
            $p.on('input', function(){
                $('.lerr').show().hide();
            });
            
            //保存cookie操作
            function saveCookie(){
                ZX.getSession(
                    function(data){
                        var account = $.parseJSON( '{"u": "'+ $.trim( $u.val()) +'", "s":"'+$ph.val() +'", "r":"'+data.roleId+'"}' );
                        if( $('._remember_me').is(':checked')){
                            zxCookie.createCookie(false);//创建长期有效Cookie
                        }else{
                            zxCookie.createCookie(true);//创建临时Cookie
                        }
                        zxCookie.setCookieValue( zxCookie.ACCT, account);
                        // var sys = $.url().param('sys');
                        // if( sys == undefined || sys == 0){
                            location.href='custom/index.html';
                        // }else{
                        //     location.href='index.html';
                        // }
                    },
                    function(){
                        alert('服务故障，请联系管理员');
                    },
                    'sup/account/session'
                );
            }
            function login(){
                if( validate_login() ){
                    $ph.val( base64encode( ZX.encode($p.val() ) ));
                    $('.lloading').hide().show();
                    if( !validate_vc()){
                        $('.lloading').show().hide();
                        $('.lcvcerr').hide().show();
                        //重置验证码
                        handler_vc_change();
                        return false;
                    }else{
                        //form, url, success_callback, failed_callback
                        ZX.formSubmitByAjax(
                            $('#form_login'),
                            'sup/account/login',
                            function(res){
                                zxCookie.removeCookie( zxCookie.ZXT);
                                saveCookie();
                            },
                            function(){
                                $('.lloading').show().hide();
                                $('.lserr').hide().show();
                                //输入错误计数
                                if( !$('.login_vc_p').hasClass('active')){
                                    var ec = zxCookie.getCookieValue( zxCookie.VC).ec;
                                    if( ec > 1){
                                        $('.login_vc_p').addClass('active');
                                    }else{
                                        ec = ec+1;
                                        var jec = $.parseJSON( '{"ec": '+ec+'}' );
                                        zxCookie.setCookieValue( zxCookie.VC, jec);
                                    }
                                }
                            }
                        );
                    }
                }
            }
            $('.btn-login').on( 'click', function(e){
                login();
                e.preventDefault();
            });
            document.onkeydown=function(event){
                e = event ? event :(window.event ? window.event : null);
                if(e.keyCode==13){
                    //执行的方法
                    login();
                }
            };
        };


        /************************************************************
        // 验证码,刷新验证码
        /************************************************************/
        function handler_vc_change(){
            //时间戳   
            //为了使每次生成图片不一致，即不让浏览器读缓存，所以需要加上时间戳   
            function chgUrl(url){   
                var timestamp = (new Date()).valueOf();   
                url = url.substring(0,17);    
                url = url + "?timestamp=" + timestamp;   
                return url;   
            }
            var imgSrc = $(".login_vc"), src = imgSrc.attr("src");   
            imgSrc.attr("src",chgUrl(src)); 
        }
        function handler_vc_refresh(){
            
            $('.btn_refresh_vc').click( function(){
                handler_vc_change();
            });  
        }

        /************************************************************
        // focused input
        /************************************************************/
        function focusLogin(){
            if(($('#login_username').val() =='' && $('#login_p_v').val()=='') ||$('#login_username').val() =='' ){
                $('#login_username').focus();
            }else if($('#login_p_v').val() ==''){
                $('#login_p_v').focus();
            }
        }


        var ec = $.parseJSON( '{"ec": 0}' );
        zxCookie.createCookie(true);
        zxCookie.setCookieValue( zxCookie.VC, ec);

        handler_login();
        handler_vc_refresh();
        focusLogin();
    }
    //登出
    function logout(url){
        ZX.getDataByAjax(
                '../sup/account/logout',
                'json',
                function(){
                    zxCookie.removeCookie();
                    location.href= url;
                },
                function(){
                    zxCookie.removeCookie();
                    location.href= url;
                }
            );
    }
    //重置密码
    function handler_revertPwd(){
        $('.btn-revert').click(function(e) {
            $('.lcvcerr').show().hide();
            $('.revert').show().hide();

            var reg_mail = /^\w+((-\w+)|(\.\w+))*\@[A-Za-z0-9]+((\.|-)[A-Za-z0-9]+)*\.[A-Za-z0-9]+$/; //验证邮箱的正则表达式
            if( $('#login_username').val().length == 0 || !reg_mail.test($('#login_username').val()) ){
                $('.luerr_format').hide().show();
                return false;
            }
            if( $('#verifyCode').val().length == 0){
                $('.lcvcerr').hide().show();
                return false;
            }
            //url, dataType, success_callback, failed_callback
            var code = $('#verifyCode').val(),
                username = $('#login_username').val();
            ZX.getDataByAjax(
                    'sup/account/revertpwd/'+username+'/'+code,
                    'json',
                    function(res){
                        $('.login-main div').show().hide();
                        $('.revert').hide().show();
                    },
                    function(res){
                        $('.lloading').show().hide();
                        if( res.error != null && res.error.length > 0){
                            $('.lserr_server').text(res.error).hide().show();
                        }else{
                            $('.lcvcerr').hide().show();
                        }
                    }
                );
        });
        $('#verifyCode').on('input', function(){
            $('.lcvcerr').show().hide();
            $('.revert').show().hide();
        });

    }
    function handler_logout(){
        APPUtils.logout_handler( $('#btn_logout'), '../login.html');
    }
    //修改密码
    function handler_changepwd(){
        APPUtils.changepwd_handler( $('#btn_changePwd'));
    }
    //账户管理
    function handler_actManager(){
        APPUtils.actManager_handler( $('#btn_actManager'));
    }
    //在线检测cookies
    function checkOnline(){
        if( !zxCookie.hasCookie()){
            logout(APPUtils.LOGINHTML);
        }
    }
    return {
        LOGINHTML:"login_custom.html?sys=1",
        WELCOMEHTML:"index.html",
        /*******************************************
         *
         * login handler
         *
         ******************************************/
        init_login: function(){
            $.cookie.json = true;
            handler_login();
        },
        /*******************************************
         *
         * logout handler
         *
         ******************************************/
        logout_handler: function( $btn, url){
            $btn.on('click', function(){
                //url, dataType, success_callback, failed_callback
                logout(url);
            });
        },
        /*******************************************
         *
         * revert passwd handler
         *
         ******************************************/
        init_revert: function(){
            handler_revertPwd();
        },

        /*******************************************
         *
         * 加载蒙版取消
         *
         ******************************************/
         removeLoading: function(){
            $('body').css('overflow', 'auto');
            $(".rpt-loading").show().hide();
         },
        /*******************************************
         *
         * changepwd handler
         *
         ******************************************/
        changepwd_handler: function( $btn){
            
            function validate_changePwd(){
                $('.err').show().hide();
                if( $('.user_password').val() == '' ||
                    $('.user_password_new').val() == '' || 
                    $('.index_changePwd_confirmPwd').val() == ''){
                    $('.cperr03').hide().show();
                    return false;
                }
                if( $('.user_password_new').val() != $('.index_changePwd_confirmPwd').val()){
                    $('.cperr01').hide().show();
                    return false;
                }
                
                var p = $('.user_password').val();
                    op = zxCookie.getCookieValue( zxCookie.ACCT);
                //通过临时Cookie判断帐户的密码
                var ep = base64encode( ZX.encode(p) );
                if( op == null || ep != op.s){
                    $('.cperr02').hide().show();
                    return false;
                }
                return true;
            }
                
            $btn.on('click', function(){
                
                $('.usr-changepwd-panel input').val('');
                $('.err').show().hide();
                $.blockUI({
                    message: $('.usr-changepwd-panel'),
                    css: {
                        background: '#34495E',
                        border: '0px',
                        cursor: 'default',
                        top: '20%',
                        left: '30%',
                        width: 'auto',
                        padding: '0px 0px 40px',
                        opacity:'0.9'
                    },
                    overlayCSS: {
                        cursor: 'default'
                    }
                });
                
                $('.settings-changePwd').click(function() {
                    if( validate_changePwd()){
                        //初始化提交数据
                        $('#password_new').val( $('.user_password_new').val() );
                        $('#password').val( $('.user_password').val() );
                        $('#username').val( zxCookie.getCookieValue( zxCookie.ACCT).u);
                        //form, url, success_callback, failed_callback
                        ZX.formSubmitByAjax(
                            $('#form-settings-pwd'),
                            '../sup/account/changepwd',
                            function(){
                                zxCookie.removeCookie();
                                $.unblockUI();
                               location.href="../login.html";
                            },
                            function(){
                                $('.cperr00').hide().show();
                                return false;
                            }
                        );
                    }
                });
                $('.settings-changePwd-cancel').click(function() {
                    $.unblockUI();
                    return false;
                });
            });
        },
        actManager_handler:function($btn){
            var table;
            $btn.on('click', function(){
                draw(true);
            });
            function draw(needOpen){
                if(table!=undefined) table.destroy();
                ZX.getDataByAjax(
                    "../sup/account/list",
                    "json",
                    function(res){
                        ZX.renderList(
                            res,
                            $(".usr-actManager-panel tbody"),
                            $("#users"),
                            $(".usr-actManager-panel tbody"),
                            true
                        )
                        open(needOpen);
                    },
                    function(){
                        open(needOpen);
                    }
                )
                function open(needOpen){
                    table = $(".usr-actManager-panel table").DataTable({
                        "bPaginate": true, //翻页功能
                        "bFilter": true, //列筛序功能
                        "searching": true,//本地搜索
                        "ordering": true,
                        "Info": true,//页脚信息
                        "autoWidth": true,//自动宽度
                        "oLanguage": {//国际语言转化
                           "oAria": {
                               "sSortAscending": " - click/return to sort ascending",
                               "sSortDescending": " - click/return to sort descending"
                           },
                           "sLengthMenu": "显示 _MENU_ 记录",
                           "sZeroRecords": "对不起，查询不到任何相关数据",
                           "sEmptyTable": "未有相关数据",
                           "sLoadingRecords": "正在加载数据-请等待...",
                           "sInfo": "当前显示 _START_ 到 _END_ 条，共 _TOTAL_ 条记录。",
                           "sInfoEmpty": "当前显示0到0条，共0条记录",
                           "sInfoFiltered": "",
                           // "sProcessing": "<img src='../resources/user_share/row_details/select2-spinner.gif'/> 正在加载数据...",
                           "sSearch": "查询：",
                           "sUrl": "",
                           //多语言配置文件，可将oLanguage的设置放在一个txt文件中，例：Javascript/datatable/dtCH.txt
                           "oPaginate": {
                               "sFirst": "首页",
                               "sPrevious": " 上一页 ",
                               "sNext": " 下一页 ",
                               "sLast": " 尾页 "
                           }
                        },
                    });
                    if(needOpen){
                        $.blockUI({
                            message: $('.usr-actManager-panel'),
                            css: {
                                background: '#fff',
                                border: '0px',
                                cursor: 'default',
                                top: '8%',
                                left: '50%',
                                width: '80%',
                                margin:'0px 0px 0px -40%',
                                padding: '30px',
                                borderRadius:'5px',
                                opacity:'0.9'
                            },
                            overlayCSS: {
                                cursor: 'default'
                            }
                        });
                    }
                }
            }
            $(".usr-actManager-panel .close").click(function(){
                $.unblockUI();
            });
            $("body").delegate(".actDel","click",function(){
                var userName = $(this).parent().parent().find(".userName").text().trim();
                event_dialog.confirm( del, userName, '您确定要删除 '+userName+' 吗?', '删除');
                function del(userName){
                    ZX.getDataByAjax(
                        "../sup/account/delete?username="+userName,
                        "json",
                        function(res){
                            event_dialog.alert('删除成功.');
                            draw();
                        },
                        function(){
                            event_dialog.alert('删除失败.');
                        }
                    );
                }
            })
            $(".actAdd").click(function(){
                var userName = $("input[name=userName]").val();
                var personName = $("input[name=personName]").val();
                var phone = $("input[name=phone]").val();
                var email = $("input[name=email]").val();
                var role = $("input[name=isAdmin]:checked").val();
                var data = {"userName":userName,"personName":personName,"phone":phone,"email":email,"role":role};
                ZX.postDataByAjax(
                    "../sup/account/reg",
                    JSON.stringify(data),
                    function(res){
                        event_dialog.alert('添加成功.初始密码为 123456');
                        draw();
                    },
                    function(res){
                        event_dialog.alert("添加失败");
                    }
                )
            });
        },
        setEmpty: function(){
            var emptyHtml = '<div class="data-empty" style="position: absolute;top: 50%;width: 100%;text-align: center;">'+
                                '<span class="empty-iv">&#9731</span>'+
                                '<h4>没有找到相关内容</h4>'+
                            '</div>';
            $('.empty-need').html( emptyHtml);
        },
        init_base: function(){
            $.cookie.json = true;
            // init_view();
            handler_logout();
            handler_changepwd();
            handler_actManager();
            //添加logo事件
            // handler_logo();
        },
        init_page: function(){
            $.cookie.json = true;
            checkOnline();
            var act = zxCookie.getCookieValue(zxCookie.ACCT);
            var roleId = Number(act.r);
            if( roleId - 99 == 0){
                $('.menu_home').removeClass('hidden');
            }else{
                $('.menu_home').remove();
            }
            APPUtils.init_base();
        }
    }
}();
/* -------------------------------- -------------------------- -------------------------- -------------------------- 

 app 1.0.0
 for page

-------------------------------- -------------------------- -------------------------- -------------------------- */

var PageUtils = function() {

    /**
     * 获取uri的相对层数
     * 
     **/
    var getUriLevel = function(){
        var pathName=window.document.location.pathname;
        if( APP_CONST.WEBROOT != '' && APP_CONST.WEBROOT != null){
            return pathName.split('/').length - 3;
        }else{
            return pathName.split('/').length - 2;
        }
    }

    /**
     * 构建相对路径
     * 
     **/
    var getUriAbs = function(){
        var pos = getUriLevel();
        var r = '';
        for( var i = 0; i < pos; i++){
            r = r+'../';
        }
        return r;
    }

    var initView = function(){

        $('head').append('<link rel="shortcut icon" href="'+getUriAbs()+'assets/img/logo.ico" />');
    }

    var checkExplorer = function() {
        var explorer = window.navigator.userAgent;
        if (explorer.indexOf("QQBrowser") >= 0 || explorer.indexOf("QQ") >= 0) {
            return texplorer = "txQQ";//"腾讯QQ";
        } else if (explorer.indexOf("Safari") >= 0 && explorer.indexOf("MetaSr") >= 0) {
            return texplorer = "sg";//"搜狗";
        } else if (!!window.ActiveXObject || "ActiveXObject" in window) { //IE
            if (!window.XMLHttpRequest) {
                return texplorer = "IE6";
            } else if (window.XMLHttpRequest && !document.documentMode) {
                return texplorer = "IE7";
            } else if (!-[1, ] && document.documentMode && !("msDoNotTrack" in window.navigator)) {
                return texplorer = "IE8";
            } else { //IE9 10 11
                var hasStrictMode = (function() { "use strict";
                    return this === undefined; }());
                if (hasStrictMode) {
                    if (!!window.attachEvent) {
                        return texplorer = "IE10"; } else {
                        return texplorer = "IE11"; }
                } else {
                    return texplorer = "IE9";
                }
            }
        } else { //非IE
            if (explorer.indexOf("LBBROWSER") >= 0) {
                return texplorer = "lbb";//"猎豹";
            } else if (explorer.indexOf("360ee") >= 0) {
                return texplorer = "360ee";//"360极速浏览器";
            } else if (explorer.indexOf("360se") >= 0) {
                return texplorer = "360se";//"360安全浏览器";
            } else if (explorer.indexOf("se") >= 0) {
                return texplorer = "se";//"搜狗浏览器";
            } else if (explorer.indexOf("aoyou") >= 0) {
                return texplorer = "aoyou";//"遨游浏览器";
            } else if (explorer.indexOf("qqbrowser") >= 0) {
                return texplorer = "qqbrowser";//"QQ浏览器";
            } else if (explorer.indexOf("baidu") >= 0) {
                return texplorer = "baidu";//"百度浏览器";
            } else if (explorer.indexOf("Firefox") >= 0) {
                return texplorer = "ff";//"火狐";
            } else if (explorer.indexOf("Maxthon") >= 0) {
                return texplorer = "maxthon";//"遨游";
            } else if (explorer.indexOf("Chrome") >= 0) {
                return texplorer = "chrome";//"谷歌（或360伪装）";
            } else if (explorer.indexOf("Opera") >= 0) {
                return texplorer = "opera";//"欧朋";
            } else if (explorer.indexOf("TheWorld") >= 0) {
                return texplorer = "tw";//"世界之窗";
            } else if (explorer.indexOf("Safari") >= 0) {
                return texplorer = "safari";//"苹果";

            } else {
                return texplorer = "other";
            }
        }
    }
    return {
        /**
         * 页面共用元素的初始化
         * @return null
         */
        init: function(){
            $.cookie.json = true;
        }
    }
}();

/* -------------------------------- -------------------------- -------------------------- -------------------------- 

 app 1.0.0
 for frame

-------------------------------- -------------------------- -------------------------- -------------------------- */

var FrameUtils = function() {

    return {
        loading: function(text) {
            // window.parent.loading();
            $('body').append('<div class="pageRefresh"></div>');
            $(".pageRefresh").fakeLoader({
                bgColor: "#2C3E50",
                spinner: "spinner2",
                text:text
            });
        },
        unloading: function() {
            // window.parent.unloading();
            $('body .pageRefresh').remove();
        },
        refresh: function(){
            $('body').append('<div class="pageRefresh"></div>');
            $(".pageRefresh").fakeLoader({
                bgColor: "#2C3E50",
                spinner: "spinner2"
            });
        },
        refreshStop: function(){
            $('body .pageRefresh').remove();
        }
    }
}();
/* -------------------------------- -------------------------- -------------------------- -------------------------- 

 app 1.0.0
 jquery 扩展函数

-------------------------------- -------------------------- -------------------------- -------------------------- */
/**
 * 基于dialog的alert
 * @param  {[type]} text 提示信息
 * @return {[type]}      null
 */
// window.alert = function(text) {

//     $.dialog({
//         contentHtml : '<p>'+text+'</p>'
//     });
// };

 /*
  * 下拉选择框
  ***********************************/
(function($) {
    var dropdown = $('.dropdown');
    dropdown.on('show.bs.dropdown', function(e) {
        $(this).find('.dropdown-menu').first().stop(true, true).slideDown();
    });
    dropdown.on('hide.bs.dropdown', function(e) {
        $(this).find('.dropdown-menu').first().stop(true, true).slideUp();
    });
}(jQuery));

 /*
  * outlook bar
  ***********************************/
var Accordion = function (el, multiple) {
    this.el = el || {};
    this.multiple = multiple || false;
    var links = this.el.find('.link');
    links.on('click', {
        el: this.el,
        multiple: this.multiple
    }, this.dropdown);
};
Accordion.prototype.dropdown = function (e) {
    var $el = e.data.el;
    $this = $(this), $next = $this.next();
    $next.slideToggle();
    $this.parent().toggleClass('open');
    if (!e.data.multiple) {
        $el.find('.submenu').not($next).slideUp().parent().removeClass('open');
    }
    ;
};


 /*
  * 设置contenteditable只能输入文本
  ***********************************/
function setContentEdit4text(){
    $('[contenteditable]').each(function() {
        // 干掉IE http之类地址自动加链接
        try {
            document.execCommand("AutoUrlDetect", false, false);
        } catch (e) {}
        
        $(this).on('paste', function(e) {
            e.preventDefault();
            var text = null;
        
            if(window.clipboardData && clipboardData.setData) {
                // IE
                text = window.clipboardData.getData('text');
            } else {
                text = (e.originalEvent || e).clipboardData.getData('text/plain') || prompt('在这里输入文本');
            }
            if (document.body.createTextRange) {    
                if (document.selection) {
                    textRange = document.selection.createRange();
                } else if (window.getSelection) {
                    sel = window.getSelection();
                    var range = sel.getRangeAt(0);
                    
                    // 创建临时元素，使得TextRange可以移动到正确的位置
                    var tempEl = document.createElement("span");
                    tempEl.innerHTML = "&#FEFF;";
                    range.deleteContents();
                    range.insertNode(tempEl);
                    textRange = document.body.createTextRange();
                    textRange.moveToElementText(tempEl);
                    tempEl.parentNode.removeChild(tempEl);
                }
                textRange.text = text;
                textRange.collapse(false);
                textRange.select();
            } else {
                // Chrome之类浏览器
                document.execCommand("insertText", false, text);
            }
        });
    });
}
/**
 * 清除class
 * @param value 需要清除的class
 */
(function(removeClass) {
    jQuery.fn.removeClass = function(value) {
        if (value && typeof value.test === 'function') {
            for (var i = 0, l = this.length; i < l; i++) {
                if (window.CP.shouldStopExecution(2)) {
                    break;
                }
                var elem = this[i];
                if (elem.nodeType === 1 && elem.className) {
                    var classNames = elem.className.split(/\s+/);
                    for (var n = classNames.length; n--;) {
                        if (window.CP.shouldStopExecution(1)) {
                            break;
                        }
                        if (value.test(classNames[n])) {
                            classNames.splice(n, 1);
                        }
                    }
                    window.CP.exitedLoop(1);
                    elem.className = jQuery.trim(classNames.join(' '));
                }
            }
            window.CP.exitedLoop(2);
        } else {
            removeClass.call(this, value);
        }
        return this;
    };
}(jQuery.fn.removeClass));

/**
 * 页面section跳转控制
 * @param  {[type]} options [description]
 * @return null
 */
jQuery.fn.gotoSection = function(options){
    var obj = jQuery(this);
    var defaults = {target:'', timer:1000};
    var o = jQuery.extend(defaults,options);
    var _rel = jQuery(this).attr("href");//.substr(1);
    if( _rel.length == 0 || $('.'+_rel) == undefined) return false;
    var _targetTop = jQuery("."+_rel).offset().top -50;
    jQuery("html,body").animate({scrollTop:_targetTop},o.timer);
    return false;
};

/*
 * scrollLoading for img
 * usage: 
 *       <img data-url="../xx.jpg"  class="imgs"
 *       $(".imgs").scrollLoading();  
 * options
 * 
 *
 */
(function($) {  
    $.fn.scrollLoading = function(options) {  
        var defaults = {  
            attr: "data-url",  
            container: $(window),  
            callback: $.noop  
        };  
        var params = $.extend({}, defaults, options || {});  
        params.cache = [];  
        $(this).each(function() {  
            var node = this.nodeName.toLowerCase(), url = $(this).attr(params["attr"]);  
            //重组  
            var data = {  
                obj: $(this),  
                tag: node,  
                url: url  
            };  
            params.cache.push(data);  
        });  
          
        var callback = function(call) {  
            if ($.isFunction(params.callback)) {  
                params.callback.call(call.get(0));  
            }  
        };  
        //动态显示数据  
        var loading = function() {  
              
            var contHeight = params.container.height();  
            if ($(window).get(0) === window) {  
                contop = $(window).scrollTop();  
            } else {  
                contop = params.container.offset().top;  
            }         
              
            $.each(params.cache, function(i, data) {  
                var o = data.obj, tag = data.tag, url = data.url, post, posb;  
  
                if (o) {  
                    post = o.offset().top - contop, post + o.height();  
      
                    if ((post >= 0 && post < contHeight) || (posb > 0 && posb <= contHeight)) {  
                        if (url) {  
                            //在浏览器窗口内  
                            if (tag === "img") {  
                                //图片，改变src  
                                callback(o.attr("src", url));         
                            } else {  
                                o.load(url, {}, function() {  
                                    callback(o);  
                                });  
                            }         
                        } else {  
                            // 无地址，直接触发回调  
                            callback(o);  
                        }  
                        data.obj = null;      
                    }  
                }  
            });   
        };  
          
        //事件触发  
        //加载完毕即执行  
        loading();  
        //滚动执行  
        params.container.bind("scroll", loading);  
    };  
})(jQuery); 

/*
 * 日期格式化函数
 * usage: 
 *      var _date = new Date( param).Format("yyyy-MM-dd");
 *
 */
Date.prototype.Format = function(format) {
    var o = {
        "M+": this.getMonth() + 1, //month
        "d+": this.getDate(), //day
        "h+": this.getHours(), //hour
        "m+": this.getMinutes(), //minute
        "s+": this.getSeconds(), //second
        "q+": Math.floor((this.getMonth() + 3) / 3), //quarter
        "S": this.getMilliseconds() //millisecond
        }
        if( format == null || format.length == 0 || format == undefined){
            format = 'yyyy-MM-dd';
        }
 
        if (/(y+)/.test(format)) {
            format = format.replace(RegExp.$1, (this.getFullYear() + "").substr(4 - RegExp.$1.length));
        }
 
        for (var k in o) {
            if (new RegExp("(" + k + ")").test(format)) {
            format = format.replace(RegExp.$1, RegExp.$1.length == 1 ? o[k] : ("00" + o[k]).substr(("" + o[k]).length));
        }
    }
    return format;
}

/* -------------------------------- -------------------------- -------------------------- -------------------------- 

 app 1.0.0
 jquery 方法扩展

-------------------------------- -------------------------- -------------------------- -------------------------- */
jQuery.fn.extend({

    /**
     * 在同辈元素中向上或向下移动
     * @param  {[type]} direction) 'up'或'down'
     * @return null
     */
    move: function(direction){
        var me = this;
        var another = null;
        if(direction == 'up'){
            another = me.prev();
            another.before(me);
        }else if(direction == 'down'){
            another = me.next();
            another.after(me);
        }
        return this;
    },
    /**
     * iframe自适应窗口
     * @param option height boolean; width boolean; woffset: width偏移量; hoffset: height偏移量
     */
    iframe_autoresize: function(option) {

        var $this = $(this);
        var defaults = {
            "height": 1,
            "width": 0,
            'woffset': 0,
            'hoffset': 0
        };
        var opts = $.extend(defaults, option);
        resize($this);

        function resize() {
            var $cur = $($this.get(0)); //仅处理第一个  
            //设置高度  
            if (opts.height != 0) {
                var height = $(window).height();
                if (opts.height < 0) {
                    height = height + opts.height;
                    if ($(window).height() - height + opts.height < 4 && $.browser.msie) {
                        //IE的4像素问题
                        $("html").css("overflow-y", "hidden");
                    }
                } else {
                    if (opts.height > 1) {
                        opts.height = 1;
                    }
                    height = $(window).height() * opts.height - opts.hoffset;
                    if ($(window).height() - height < 4) {
                        //解决IE的4像素问题，IE的应用可能有一些限制  
                        $("html").css("overflow-y", "hidden");
                    }
                }
                $cur.height(height);
            }

            //设置宽度  
            if (opts.width != 0) {
                var width = $(window).width();
                if (opts.width < 0) {
                    width = width + opts.width;
                } else {
                    if (opts.width > 1) {
                        opts.width = 1;
                    }
                    width = $(window).width() * opts.width;
                }
                $cur.width(width - opts.woffset);
            }
        }

        $(window).resize(function() {
            resize();
        });
    }
});

/* -------------------------------- -------------------------- -------------------------- -------------------------- 

 app 1.0.0
 jquery 组件扩展

-------------------------------- -------------------------- -------------------------- -------------------------- */
/**
 * dataTables属性规范
 */
PluginExt = function(){

    var dataTblLanguage = {
            "sLengthMenu": "每页显示 _MENU_ 条记录",
            "sInfo": "从 _START_ 到 _END_ /共 _TOTAL_ 条数据",
            "sInfoEmpty": "显示第0 至0 项结果，共0 项",
            "sInfoFiltered": "(从 _MAX_ 条数据中检索)",
            "sSearch": "搜索: ",
            "oPaginate": {
                "sFirst": "首页",
                "sPrevious": "前一页",
                "sNext": "后一页",
                "sLast": "尾页"
            },
            "sZeroRecords": "没有检索到数据",
            "sProcessing": '数据处理中...'
        }
    var dataTblOpts = {
                    "bAutoWidth": true, //自适应宽度
                    // "sScrollX" :"100%",
                    // "sScrollXInner" :"130%",
                    // "bScrollCollapse" :false,

                    "bProcessing": true, //显示是否加载
                    "bPaginate": false,
                    "bLengthChange": false,
                    "info": false,
                    "oLanguage": dataTblLanguage,
                    "bSort": false,
                    "scrollCollapse": true,
                    "paging": false,
                    "bFilter": false
                }
    return {
        getLangCN: function(){
            return dataTblLanguage;
        },
        /**
         * 获取datatable的基础options
         * @return 基础options
         */
        getDTOpts: function(){
            return dataTblOpts;
        },
        /**
         * 获取表头fixed的option
         * @return 表头fixed的option
         */
        getDTOpts_fh: function( ){
            return  $.extend(true, dataTblOpts, {
                        "fixedHeader": true
                    });
        },
        /**
         * 获取锁定列的datatable的options
         * @param  锁定列数目
         * @return 锁定列的datatable的options
         */
        getDTOpts_fc: function(fixColCount){
            if( fixColCount == undefined ) fixColCount = 1;
            var r = $.extend(true, dataTblOpts, {
                        "fixedColumns": {
                            "leftColumns": fixColCount
                        }
                    });
            return r;
        },
        /**
         * 获取锁定表头和列的datatable的options
         * @param  锁定列数目
         * @return 锁定表头和列的datatable的options
         */
        getDTOpts_fhc: function(fixColCount){
            if( fixColCount == undefined ) fixColCount = 1;
            var r = $.extend(true, dataTblOpts, {
                        "fixedHeader": true,
                        "fixedColumns": {
                            "leftColumns": fixColCount
                        }
                    });
            return r;
        }
    }
}();

/*
 * zxt table depend jquery.datatables
 * usage:
 *      $selector.zxtable({option});
 *      $selector: table的DOM
 * option:
        url: 获取数据的url,
        data: 如果采用静态数据绘制，则直接传递该属性，并且不传递url,默认null
        template: 模板ID,
        renderTbody: 是否将数据直接绘制在tbody中,默认false
        exportURL: 导出excel的url,

        needDataTable: 是否启用datatables, 默认false
        needToolbar: 是否启用Datatables的taoolbar，默认true,
        needSort: datatables是否需要排序,
        orderby: datatables的排序,
        fixedHeader: 是否锁定header，依赖dataTables.fixedHeader.min.js,
        fixedColumn: 是否锁定列，默认不锁定,
        fixedColumnOption: 锁定列的配置，exp:{leftColumns: 1,rightColumns: 1}, 依赖dataTables.fixedColumns.min.js
        dtOption: 自定义datatables的option,

        callBack: 回调函数
 *
 */
jQuery.fn.zxtable = function (options) {
    var setting = {
        url: null,
        data: null,
        template: '#zxtable_template',
        renderTbody: false,
        exportURL: null,

        needDataTable: false,
        needToolbar: true,
        needSort:false,
        ordering: true,
        orderby: null,
        fixedHeader: true,
        fixedColumn: false,
        fixedColumnOption: {},
        scrollY: null,
        scrollX:null,
        dtOption: null,

        callBack: undefined
    };
    jQuery.extend(setting, options);

    var $table = this;
    var table ;
    function renderTable(datas) {
        
        function error(){
            //清理加载
            //终止进度条
            // Pace.stop( );

            // Pace.on( 'done', function(){
            //     $('.pace .pace-progress').addClass('error');
            //     $($(window.parent.document).find('.rpt_error')[0]).css('display', 'block');
            //     $($(window.parent.document).find('.rpt_summary')[0]).height(400);
            // });
            $table.html('<tr><td>没有检索到数据.</td></tr>');
        }
        if ( datas == undefined || datas == null || datas.length == 0 || _.keys(datas).length == 0 ) {
            error();
            return false;
        }
        if( setting.callBack != undefined && $.isFunction( setting.callBack) ){
            var r = setting.callBack( datas);
            if( r == false){
                error();
                return false;                
            }else if( r == -1){
                return;
            }
        }
        //基于dataTables插件的操作
        if (!jQuery().DataTable) {
            return;
        }   

        // begin table
        if( setting.needDataTable != undefined && setting.needDataTable == true){

            if( setting.orderby == undefined || setting.orderby == null){
                setting.orderby = [];
            }
            var _dtOption = {
                "bAutoWidth": true, //自适应宽度
                "bProcessing": true, //显示是否加载
                "bPaginate": false,
                "bLengthChange": false,
                "info": false,
                "iDisplayLength": 1500,
                "ordering": setting.ordering,
                "order" : setting.orderby,
                "bSort" : setting.needSort,
                // "scrollX": true,
                // "scrollCollapse": true,
                "fixedHeader": setting.fixedHeader,
                "oLanguage": PluginExt.getLangCN()//,
                // "dom": '<"toolbar">'
            };
            //工具栏
            if( setting.exportURL != null && setting.needToolbar == true){
                _dtOption.dom = '<"toolbar">frtip';
            }else if( setting.exportURL != null && setting.needToolbar == false){
                _dtOption.dom = '<"toolbar">';
            }else if( setting.exportURL == null && setting.needToolbar == true){
                _dtOption.dom = 'frtip';
            }else{
                _dtOption.dom = '';
            }
            //锁定表头
            if( setting.fixedColumn == true){
                // _dtOption.scrollX = true;
                // _dtOption.scrollCollapse = true;
                if( setting.scrollY == null){
                    setting.scrollY = '400px';
                }
                _dtOption.scrollY = setting.scrollY;
            }

            table = $table.DataTable( );
            //防止对象重复
            table.destroy(false);
            table.fixedHeader.disable();
            //构建DT对象
            if( setting.dtOption == null || setting.dtOption == undefined){
                table = $table.DataTable( _dtOption);
            }else{
                table = $table.DataTable( setting.dtOption);
            }
            if( setting.exportURL != null && setting.needToolbar == true){
                $(".toolbar").html('<b><a href="'+setting.exportURL+'" class="btn btn-default">导出 <i class="icon-upload-alt"></i></a></b>').css({
                    'position': 'absolute',
                    'margin-top': '8px',
                    'margin-left': '20px'
                });
            }
            
        }else{
            if( setting.exportURL != null){
                $(".toolbar").html('<b><a href="'+setting.exportURL+'" class="btn btn-default">导出 <i class="icon-upload-alt"></i></a></b>').css({
                    'position': 'absolute',
                    'margin-top': '8px',
                    'margin-left': '20px'
                });
            }
        }

        //清理加载
        // Pace.stop();
    };
    if( setting.url != null && setting.url != ''){
        ZX.loadListAndRender( setting.url, this, $( setting.template), this, true, renderTable);
    }else{
        if( setting.data != null){
            
            if( setting.renderTbody == false){
                ZX.renderList( setting.data, $table, $( setting.template), $table, true, renderTable);
            }
            else{
                ZX.renderList( setting.data, $(this.find('tbody')[0]), $( setting.template), $(this.find('tbody')[0]), true, renderTable);
            }
        }else{
            return false;
        }
        
    }
    return table;
}


/*******************************************************************************************
 * 表单数据的JSON序列化
 * usage: 
 *      $form.serializeJson();
 * note: 
 *      这里使用的是元素的name属性
 *
 *******************************************************************************************/ 
$.fn.serializeJson=function(){
    var serializeObj={};
    var array=this.serializeArray();
    var str=this.serialize();
    $(array).each(function(){
        if(serializeObj[this.name]){
            if($.isArray(serializeObj[this.name])){
                serializeObj[this.name].push(this.value);
            }else{
                serializeObj[this.name]=[serializeObj[this.name],this.value];
            }
        }else{
            serializeObj[this.name]=this.value;
        }
    });
    return serializeObj;
};
/* -------------------------------- -------------------------- -------------------------- -------------------------- 

 系统封装接口

-------------------------------- -------------------------- -------------------------- -------------------------- */

var ZX = function(){
    var request;//for form submit
    /**
     * 获取backbone的view对象
     * @param  {el,model}
     * @return backbone的view对象
     */
    function getVItem(options){
        var VItem = Backbone.View.extend({
            render: function(){
                $(this.el).append(this.template(this.model.toJSON()));
            }
        });
        return new VItem(options);
    }
    /**
     * 获取backbone的collection对象
     * @param  {el}
     * @return backbone的collection对象
     */
    function getVCItems(options){
        var VCItems = Backbone.View.extend({
            initialize: function(){
            },
            render: function ( maxRenderCount ) {
                var _this = this;
                var tpl = _this.template;
                var _curCount = 0;
                if( undefined == maxRenderCount || null == maxRenderCount ){
                    this.collection.each(function(model){
                        _this.addItem(model, tpl);
                    });
                }else{
                    this.collection.each(function(model){
                        if(_curCount++ < maxRenderCount)
                            _this.addItem(model, tpl);
                        else
                            return;
                    });
                }
                
            },
            addItem:function(model, tpl){
                var itemView = getVItem({
                    model:model,
                    el: this.el
                });
                itemView.template = tpl;
                itemView.render();
            }
        });
        return new VCItems(options);
    }
    /*
     * BB.collection的fetch，并render
     * usage:
     * 
     * var url = "/rptGradeScoreData",//数据fetch链接
     *
     *     $el = $('.tab_summary tbody'), //render的DOM
     *
     *     $tmp = $('#rpt_grade_score_SummaryData'), //BB template's Id
     *
     *     $container = $('.tab_summary'); //render的DOM
     *
     *     renderFn = fn; //callback方法，在render过程中需要额外处理的函数
     *     
     *     maxRenderCount 最大绘制数量，当maxRenderCount == 10，那么最多只画10条数据。
     *
     * ZX.loadListAndRender( url, $el, $tmp, $container);
    */ 
    var loadListAndRender = function( _url, $el, $tmp, $containerDOM, forClear, renderFn, maxRenderCount){
        var MListData = Backbone.Model.extend();
        var CListData = Backbone.Collection.extend({model: MListData});

        var listDatas = new CListData();
        listDatas.url = _url;
        var vClistData = getVCItems({el: $el});

        listDatas.fetch({
            success: function(){
                   
                    if( forClear){
                        $containerDOM.html('');
                    }
                    if( !_.isEmpty( listDatas.toJSON()[0])){
                        var datas = listDatas.toJSON()[0];
                        if( undefined != datas.success && true != datas.success && false == datas.success){
                            $containerDOM.html( ZXMSG.LOADFAILED);
                            return;
                        }
                        vClistData.collection = listDatas;
                        vClistData.template = _.template( $tmp.html());
                        vClistData.render();
                    }else{
                        //console.warn('THE DATA LIST IS EMPTY');
                    }
                    if(renderFn != undefined && renderFn !== null){
                        listDatas = listDatas.toJSON();//强制转换为JSON
                        renderFn( listDatas);
                    }
            },
            error: function(){
                $containerDOM.html( ZXMSG.LOADFAILED);
            }
        });
    }  

    var _formSubmitByAjax = function( form, url, async, success_callback, failed_callback){
            if( request){
                request.abort();
            }
            var $inputs = form.find("input, select, button, textarea");
            var formData = JSON.stringify(form.serializeJson() );
            if(async == undefined ){
                async = false;
            }
            // $inputs.prop("disabled", true);
            request = $.ajax({
                url: url,
                type: "POST",
                contentType: "application/json;charset=UTF-8",
                dataType :'JSON',
                data: formData,
                async: async
            });
            request.done( function (res, textStatus, jqXHR){
                if( res.success == true){
                    if( success_callback != undefined && success_callback != null){
                        if( res.data != undefined && res.data != null){
                            success_callback(res.data);
                        }else{
                            success_callback();
                        }
                    }
                    return true;
                }else{
                    if( failed_callback != undefined && failed_callback != null){
                        failed_callback(res);
                    }
                    request.abort();//e.stopPropagation();event.preventDefault();
                    return false;
                }
            });

            request.fail( function (jqXHR, textStatus, errorThrown){
                if( failed_callback != undefined && failed_callback != null){
                    failed_callback(jqXHR);
                }
                request.abort();
                return false;                
            });

            // 重新启用input
            // request.always(function () {
            //     $inputs.prop("disabled", false);
            // });
        }
    return {
        /***********************************************************************************
         *
         * function for validate
         *
         **********************************************************************************/
        validate: function( value, type){
            switch(type){
                case 'mail':
                    var reg = /^([a-zA-Z0-9_-])+@([a-zA-Z0-9_-])+((\.[a-zA-Z0-9_-]{2,3}){1,2})$/;
                    if (!reg.test( value)) {
                        return false;
                    }
                    return true;
                case 'pwd':
                    break;
                default:
                    break;
            }
        }
        /***********************************************************************************
         *
         * function for load page content
         *
         **********************************************************************************/
         ,loadStaticHtml: function( _url, $el,goTop, isHtml, callback){
            $.ajax({
                type: "GET",
                cache: false,
                url: _url,
                dataType: "html",
                success: function (res) {
                    if( isHtml == true){
                        $el.html(res);
                    }else{
                        $el.text(res);
                    }
                    if(goTop == undefined || goTop == null || goTop =="" ){
                        $('html,body').animate({scrollTop:0},0);//回到顶端
                    }
                    if( callback != undefined && callback !== null){
                        callback();
                    }
                },
                error: function (xhr, ajaxOptions, thrownError) {
                    if( isHtml == true){
                        $el.html('');
                    }else{
                        $el.text('');
                    }
                },
                async: false
            });
         }
        /***********************************************************************************
         *
         * function for data control
         *
         **********************************************************************************/
        /*
         * BB.collection的fetch，并render
         * usage:
         * 
         * var url = "/rptGradeScoreData",//数据fetch链接
         *
         *     $el = $('.tab_summary tbody'), //render的DOM
         *
         *     $tmp = $('#rpt_grade_score_SummaryData'), //BB template's Id
         *
         *     $container = $('.tab_summary'); //render的DOM
         *
         *     renderFn = fn; //callback方法，在render过程中需要额外处理的函数
         *     
         *     maxRenderCount 最大绘制数量，当maxRenderCount == 10，那么最多只画10条数据。
         *
         * ZX.loadListAndRender( url, $el, $tmp, $container);
        */ 
        ,loadListAndRender: function( _url, $el, $tmp, $containerDOM, forClear, renderFn, maxRenderCount){
            loadListAndRender(_url, $el, $tmp, $containerDOM, forClear, renderFn, maxRenderCount);
        }  
        /*
         * BB.collection的fetch，并render
         * usage:
         * 
         * var url = "/rptGradeScoreData",//数据fetch链接
         *
         *     $el = $('.tab_summary tbody'), //render的DOM
         *
         *     $tmp = $('#rpt_grade_score_SummaryData'), //BB template's Id
         *
         *     $container = $('.tab_summary'); //render的DOM
         *
         *     renderFn = fn; //callback方法，在render过程中需要额外处理的函数
         *
         * ZX.loadListAndRender( url, $el, $tmp, $container);
        */      
        ,loadListAndRender: function( _url, $el, $tmp, $containerDOM, forClear, renderFn ){
            loadListAndRender(_url, $el, $tmp, $containerDOM, forClear, renderFn, null);
        }
        /********************
        根据listDatas绘制页面
        ********************/
        ,renderList: function(datas, $el, $tmp, $containerDOM, forClear, renderFn){
            var MListData = Backbone.Model.extend();
            var CListData = Backbone.Collection.extend({model: MListData});

            var listDatas = new CListData(datas);
            var vClistData = getVCItems({el: $el});

            if( forClear){
                $containerDOM.html('');
            }
            if( !_.isEmpty( listDatas.toJSON()[0])){
                vClistData.collection = listDatas;
                vClistData.template = _.template( $tmp.html());
                vClistData.render();
            }else{
                // console.warn('THE DATA LIST IS EMPTY');
            }
            if(renderFn != undefined && renderFn !== null){
                var number_arr=new Array();  
                //将参数中除去第一个参数的其余参数赋值给数组number_arr  
                var i =6;  
                for(i;i<arguments.length;i++){  
                    number_arr[i-6] = arguments[i];  
                } 
                listDatas = listDatas.toJSON();//强制转换为JSON
                number_arr.push(listDatas);
                renderFn( number_arr);
            }

        }
        //通过ajax方式调用后台数据
        //url：调用路径
        //dataType：数据传输类型，'html'/'json'
        //success_callback: 数据调用成功后的回调函数
        //failed_callback： 数据调用失败后的回调函数
        ,getDataByAjax: function( url, dataType, success_callback, failed_callback){
            if( url.indexOf('?') != -1){
                url = url+'&_r='+_.random(10, 100000);
            }else{
                url = url+'?_r='+_.random(10, 100000);
            }

            request = $.ajax({
                type: "GET",
                cache: false,
                url: url,
                dataType: dataType,
                success: function(res){
                    if( res.success == true){
                        if( success_callback != undefined && success_callback != null){
                            if( res.data != undefined && res.data != null){
                                success_callback(res.data);
                            }else{
                                success_callback();
                            }
                        }
                    }else{
                        if( failed_callback != undefined && failed_callback != null){
                            failed_callback(res);
                        }
                    }
                    result = true;
                },
                error: function(xhr, ajaxOptions, thrownError){
                        if( failed_callback != undefined && failed_callback != null){
                            failed_callback("operate failed");
                        }
                        return false;
                },
                async: true
            });
        }
        //同步方式获取数据
        ,ajaxDataSync : function( url, success_callback, failed_callback){
            if( url.indexOf('?') != -1){
                url = url+'&_r='+_.random(10, 100000);
            }else{
                url = url+'?_r='+_.random(10, 100000);
            }

            request = $.ajax({
                type: "GET",
                cache: false,
                url: url,
                dataType: "json",
                success: function(res){
                    if( res.success == true){
                        if( success_callback != undefined && success_callback != null){
                            if( res.data != undefined && res.data != null){
                                success_callback(res.data);
                            }else{
                                success_callback();
                            }
                        }
                    }else{
                        if( failed_callback != undefined && failed_callback != null){
                            failed_callback(res);
                        }
                    }
                    result = true;
                },
                error: function(xhr, ajaxOptions, thrownError){
                        if( failed_callback != undefined && failed_callback != null){
                            failed_callback("operate failed");
                        }
                        return false;
                },
                async: false
            });
        }
        
        //通过ajax方式调用后台数据
        //url：调用路径
        //dataType：数据传输类型，'json'
        //success_callback: 数据调用成功后的回调函数
        //failed_callback： 数据调用失败后的回调函数
        ,postDataByAjax: function(url, data, success_callback, failed_callback){
            if( request){
                request.abort();
            }
            request = $.ajax({
                type:"POST",
                url:url,
                data:data,
                contentType: "application/json;charset=utf-8",
                dataType: 'json',
                async: false
            });
            request.done( function (res, textStatus, jqXHR){
                if( res.success == true){
                    if( success_callback != undefined && success_callback != null){
                        if( res.data != undefined && res.data != null){
                            success_callback(res.data);
                        }else{
                            success_callback();
                        }
                    }
                    return true;
                }else{
                    if( failed_callback != undefined && failed_callback != null){
                        failed_callback(res);
                    }
                    request.abort();//e.stopPropagation();event.preventDefault();
                    return false;
                }
            });

            request.fail( function (jqXHR, textStatus, errorThrown){
                if( failed_callback != undefined && failed_callback != null){
                    failed_callback(jqXHR);
                }
                request.abort();
                return false;                
            });
        }
        ,formSubmitByAjax: function( form, url, success_callback, failed_callback){
            _formSubmitByAjax(form, url, false, success_callback, failed_callback);
        }
        //获取session的基本方法
        //scucess_call: 获取session成功后的操作函数
        //failed_call: 获取session失败后的操作函数
        ,getSession: function( scucess_call, failed_call, url){
            var _url = 'sys/account/session',
                type = 'json';
            if( url == undefined || url == null || $.trim(url).length == 0){

            }else{
                _url = url;
            }
            ZX.getDataByAjax( _url, type, scucess_call, failed_call);
        },
        /***********************************************************************************
         *
         * function for MD5 encode
         *
         **********************************************************************************/
        encode: function( v){
            return $.md5(v);
        },
        
        isEmail:function (str){
            var re=/^\w+((-\w+)|(\.\w+))*\@[A-Za-z0-9]+((\.|-)[A-Za-z0-9]+)*\.[A-Za-z0-9]+$/;
          if (re.test(str) != true) {
            return false;
          }else{
            return true;
          }
        },

        //判断是否有列表中的危险字符
        isValidReg: function (chars){
          var re=/<|>|\[|\]|\{|\}|『|』|※|○|●|◎|§|△|▲|☆|★|◇|◆|□|▼|㊣|﹋|⊕|⊙|〒|ㄅ|ㄆ|ㄇ|ㄈ|ㄉ|ㄊ|ㄋ|ㄌ|ㄍ|ㄎ|ㄏ|ㄐ|ㄑ|ㄒ|ㄓ|ㄔ|ㄕ|ㄖ|ㄗ|ㄘ|ㄙ|ㄚ|ㄛ|ㄜ|ㄝ|ㄞ|ㄟ|ㄢ|ㄣ|ㄤ|ㄥ|ㄦ|ㄧ|ㄨ|ㄩ|■|▄|▆|\*|@|#|\^|\\/;
          if (re.test( chars) == true) {
            return false;
          }else{
            return true;
          }
        },

        //判断字符串是否大于规定的长度
        isValidLength: function (chars, len) {
          if (chars.length < len) {
            return false;
          }
          return true;
        },

        //判断字符串是为网址不区分大小写
        isValidURL: function ( chars ) {
          var re=/^([hH][tT]{2}[pP]:\/\/|[hH][tT]{2}[pP][sS]:\/\/)(\S+\.\S+)$/;
          if (!isNULL(chars)) {
            chars = jsTrim(chars);
            if (chars.match(re) == null)
              return false;
            else
              return true;
          }
          return false;
        },

        //判断字符串是否为小数
        isValidDecimal: function ( chars ) {
          var re=/^\d*\.?\d{1,2}$/;
          if (chars.match(re) == null)
            return false;
          else
            return true;
        },

        //判断字符串是否为整数
        isNumber: function ( chars ) {
          var re=/^\d*$/;
          if (chars.match(re) == null)
            return false;
          else
            return true;
        },

        //判断字符串是否为浮点数
        isFloat: function ( str ) {
          for(i=0;i<str.length;i++)  {
             if ((str.charAt(i)<"0" || str.charAt(i)>"9")&& str.charAt(i) != '.'){
              return false;
             }
          }
          return true;
        },

        //判断字符是否为A-Za-z英文字母
        isLetters: function ( str ){
          var re=/^[A-Za-z]+$/;
          if (str.match(re) == null)
            return false;
          else
            return true;
        },

        //判断字符串是否邮政编码
        isValidPost: function ( chars ) {
          var re=/^\d{6}$/;
          if (chars.match(re) == null)
            return false;
          else
            return true;
        },

        //判断字符是否空NULL
        isNULL: function ( chars ) {
          if (chars == null)
            return true;
          if (jsTrim(chars).length==0)
            return true;
          return false;
        }
    }
}();

/* -------------------------------- -------------------------- -------------------------- -------------------------- 

 系统cookies管理

-------------------------------- -------------------------- -------------------------- -------------------------- */
var zxCookie = function(){
    
    var cookieExp = 365,
        cookieDomain = 'www.wd.cn',
        cookiePath = '/';
    
    var getCookieObj = function(cookieName){
        var v = $.cookie( cookieName);
        if( v == undefined || v ==null){
            return null;
        }else{
            return v;   
        }           
    }
    
    return {
        /**
         * 常量定义
         */
        ACCT: 'act',
        ZX: 'cn.wd',
        ZXT: 'com.wd',
        FOCUS:'cn.wd.ext',//永久cookie
        FOCUS_PMT:'com.wd.ext',//临时cookie
        VC: 'errCount',
        LACT: 'lact',
        createCookie: function( isTmp, needRemove){
            if( needRemove == undefined || needRemove == true) zxCookie.removeCookie();
            if( !isTmp){
                $.cookie( zxCookie.ZXT, {}, { path: '/', domain: '', secure: false, raw: false});
            }else{
                $.cookie( zxCookie.ZX, {}, { expires: 365, path: '/', domain: '', secure: false, raw: false});
            }
        },
        /**
         * create cookie data
         * @param {Object} k JSON key
         * @param {Object} value JSON value
         */
        setCookieValue: function( k, value, _cookieName){

            var cookieName = getCookieObj( zxCookie.ZX) == null? zxCookie.ZXT:zxCookie.ZX;
            if(_cookieName != undefined ){
                cookieName = _cookieName;
            }
            var cv = getCookieObj( cookieName);
            if( cv ==null){
                // console.warn('The cookie obj is null, please create!');
                return;
            }
            var v = $.parseJSON( '{"'+k+'": '+JSON.stringify(value)+'}');
            _.extend( cv, v);
            zxCookie.removeCookie( cookieName);
            if( cookieName == zxCookie.ZX){
                $.cookie( cookieName, cv, { expires: 365, path: '/', domain: '', secure: false, raw: false});
            }else if(cookieName == zxCookie.ZXT){
                $.cookie( cookieName, cv, { path: '/', domain: '', secure: false, raw: false});
            }else{
                return;
            }
        },
        /**
        *set cookie root path
        */
        setRootCookieValue:function(k, value){
            $.cookie( k, value, { expires: 365, path: '/', domain: '', secure: false, raw: false});
        },
        /**
         * get data by cookie's key 
         * @param {Object} k key
         */
        getCookieValue: function( k){

            var cv = getCookieObj( zxCookie.ZXT);
            if( cv ==null){
                cv = getCookieObj( zxCookie.ZX);
                if (cv == null ) return null;
                var r = _.pick( cv, k);
                if( _.isEmpty(r) || r == undefined || r == null)  return null;
                return _.values(r)[0];
            }else{
                var r = _.pick( cv, k);
                if( _.isEmpty(r) || r == undefined || r == null){
                    cv = getCookieObj( zxCookie.ZX);
                    r = _.pick( cv, k);
                    if( _.isEmpty(r) || r == undefined || r == null)  return null;
                } 
                return _.values(r)[0];
            }           
        },
        getCookieActInfoValue: function(k){
            var act = zxCookie.getCookieValue(zxCookie.ACCT);
            if( act == null || act == undefined) return null;
            var r = _.pick( act, k);
            // alert(k)ji
            if( _.isEmpty(r)) return null;
            return _.values(r)[0];
        },
        getRootCookieValue:function(k){
            var cv = getCookieObj( k);
            return cv;  
        },
        /**
         * Does the object contain the given key?
         * @param {Object} key
         */
        hasCookie: function(k){
            if( k == undefined || k == null){
                if( getCookieObj( zxCookie.ZX)==null && getCookieObj( zxCookie.ZXT) == null){
                    return false;
                }else{
                    return true;
                }
            }else{
                var r = zxCookie.getCookieValue( k);
                if( r == null) return false;
                return true;
            }
        },
        /**
         * destroy Cookie
         */
        removeCookie: function( cookieName){
            if( cookieName == undefined){
                $.removeCookie(zxCookie.ZX, {path:'/'}); 
                $.removeCookie(zxCookie.ZXT, {path:'/'}); 
            }else{
                $.removeCookie(cookieName, {path:'/'}); 
            }
        }
    }
}();

/**
 * MD5计算
 */
(function($){var rotateLeft=function(lValue,iShiftBits){return(lValue<<iShiftBits)|(lValue>>>(32-iShiftBits));}
var addUnsigned=function(lX,lY){var lX4,lY4,lX8,lY8,lResult;lX8=(lX&0x80000000);lY8=(lY&0x80000000);lX4=(lX&0x40000000);lY4=(lY&0x40000000);lResult=(lX&0x3FFFFFFF)+(lY&0x3FFFFFFF);if(lX4&lY4)return(lResult^0x80000000^lX8^lY8);if(lX4|lY4){if(lResult&0x40000000)return(lResult^0xC0000000^lX8^lY8);else return(lResult^0x40000000^lX8^lY8);}else{return(lResult^lX8^lY8);}}
var F=function(x,y,z){return(x&y)|((~x)&z);}
var G=function(x,y,z){return(x&z)|(y&(~z));}
var H=function(x,y,z){return(x^y^z);}
var I=function(x,y,z){return(y^(x|(~z)));}
var FF=function(a,b,c,d,x,s,ac){a=addUnsigned(a,addUnsigned(addUnsigned(F(b,c,d),x),ac));return addUnsigned(rotateLeft(a,s),b);};var GG=function(a,b,c,d,x,s,ac){a=addUnsigned(a,addUnsigned(addUnsigned(G(b,c,d),x),ac));return addUnsigned(rotateLeft(a,s),b);};var HH=function(a,b,c,d,x,s,ac){a=addUnsigned(a,addUnsigned(addUnsigned(H(b,c,d),x),ac));return addUnsigned(rotateLeft(a,s),b);};var II=function(a,b,c,d,x,s,ac){a=addUnsigned(a,addUnsigned(addUnsigned(I(b,c,d),x),ac));return addUnsigned(rotateLeft(a,s),b);};var convertToWordArray=function(string){var lWordCount;var lMessageLength=string.length;var lNumberOfWordsTempOne=lMessageLength+8;var lNumberOfWordsTempTwo=(lNumberOfWordsTempOne-(lNumberOfWordsTempOne%64))/64;var lNumberOfWords=(lNumberOfWordsTempTwo+1)*16;var lWordArray=Array(lNumberOfWords-1);var lBytePosition=0;var lByteCount=0;while(lByteCount<lMessageLength){lWordCount=(lByteCount-(lByteCount%4))/4;lBytePosition=(lByteCount%4)*8;lWordArray[lWordCount]=(lWordArray[lWordCount]|(string.charCodeAt(lByteCount)<<lBytePosition));lByteCount++;}
lWordCount=(lByteCount-(lByteCount%4))/4;lBytePosition=(lByteCount%4)*8;lWordArray[lWordCount]=lWordArray[lWordCount]|(0x80<<lBytePosition);lWordArray[lNumberOfWords-2]=lMessageLength<<3;lWordArray[lNumberOfWords-1]=lMessageLength>>>29;return lWordArray;};var wordToHex=function(lValue){var WordToHexValue="",WordToHexValueTemp="",lByte,lCount;for(lCount=0;lCount<=3;lCount++){lByte=(lValue>>>(lCount*8))&255;WordToHexValueTemp="0"+lByte.toString(16);WordToHexValue=WordToHexValue+WordToHexValueTemp.substr(WordToHexValueTemp.length-2,2);}
return WordToHexValue;};var uTF8Encode=function(string){string=string.replace(/\x0d\x0a/g,"\x0a");var output="";for(var n=0;n<string.length;n++){var c=string.charCodeAt(n);if(c<128){output+=String.fromCharCode(c);}else if((c>127)&&(c<2048)){output+=String.fromCharCode((c>>6)|192);output+=String.fromCharCode((c&63)|128);}else{output+=String.fromCharCode((c>>12)|224);output+=String.fromCharCode(((c>>6)&63)|128);output+=String.fromCharCode((c&63)|128);}}
return output;};$.extend({md5:function(string){var x=Array();var k,AA,BB,CC,DD,a,b,c,d;var S11=7,S12=12,S13=17,S14=22;var S21=5,S22=9,S23=14,S24=20;var S31=4,S32=11,S33=16,S34=23;var S41=6,S42=10,S43=15,S44=21;string=uTF8Encode(string);x=convertToWordArray(string);a=0x67452301;b=0xEFCDAB89;c=0x98BADCFE;d=0x10325476;for(k=0;k<x.length;k+=16){AA=a;BB=b;CC=c;DD=d;a=FF(a,b,c,d,x[k+0],S11,0xD76AA478);d=FF(d,a,b,c,x[k+1],S12,0xE8C7B756);c=FF(c,d,a,b,x[k+2],S13,0x242070DB);b=FF(b,c,d,a,x[k+3],S14,0xC1BDCEEE);a=FF(a,b,c,d,x[k+4],S11,0xF57C0FAF);d=FF(d,a,b,c,x[k+5],S12,0x4787C62A);c=FF(c,d,a,b,x[k+6],S13,0xA8304613);b=FF(b,c,d,a,x[k+7],S14,0xFD469501);a=FF(a,b,c,d,x[k+8],S11,0x698098D8);d=FF(d,a,b,c,x[k+9],S12,0x8B44F7AF);c=FF(c,d,a,b,x[k+10],S13,0xFFFF5BB1);b=FF(b,c,d,a,x[k+11],S14,0x895CD7BE);a=FF(a,b,c,d,x[k+12],S11,0x6B901122);d=FF(d,a,b,c,x[k+13],S12,0xFD987193);c=FF(c,d,a,b,x[k+14],S13,0xA679438E);b=FF(b,c,d,a,x[k+15],S14,0x49B40821);a=GG(a,b,c,d,x[k+1],S21,0xF61E2562);d=GG(d,a,b,c,x[k+6],S22,0xC040B340);c=GG(c,d,a,b,x[k+11],S23,0x265E5A51);b=GG(b,c,d,a,x[k+0],S24,0xE9B6C7AA);a=GG(a,b,c,d,x[k+5],S21,0xD62F105D);d=GG(d,a,b,c,x[k+10],S22,0x2441453);c=GG(c,d,a,b,x[k+15],S23,0xD8A1E681);b=GG(b,c,d,a,x[k+4],S24,0xE7D3FBC8);a=GG(a,b,c,d,x[k+9],S21,0x21E1CDE6);d=GG(d,a,b,c,x[k+14],S22,0xC33707D6);c=GG(c,d,a,b,x[k+3],S23,0xF4D50D87);b=GG(b,c,d,a,x[k+8],S24,0x455A14ED);a=GG(a,b,c,d,x[k+13],S21,0xA9E3E905);d=GG(d,a,b,c,x[k+2],S22,0xFCEFA3F8);c=GG(c,d,a,b,x[k+7],S23,0x676F02D9);b=GG(b,c,d,a,x[k+12],S24,0x8D2A4C8A);a=HH(a,b,c,d,x[k+5],S31,0xFFFA3942);d=HH(d,a,b,c,x[k+8],S32,0x8771F681);c=HH(c,d,a,b,x[k+11],S33,0x6D9D6122);b=HH(b,c,d,a,x[k+14],S34,0xFDE5380C);a=HH(a,b,c,d,x[k+1],S31,0xA4BEEA44);d=HH(d,a,b,c,x[k+4],S32,0x4BDECFA9);c=HH(c,d,a,b,x[k+7],S33,0xF6BB4B60);b=HH(b,c,d,a,x[k+10],S34,0xBEBFBC70);a=HH(a,b,c,d,x[k+13],S31,0x289B7EC6);d=HH(d,a,b,c,x[k+0],S32,0xEAA127FA);c=HH(c,d,a,b,x[k+3],S33,0xD4EF3085);b=HH(b,c,d,a,x[k+6],S34,0x4881D05);a=HH(a,b,c,d,x[k+9],S31,0xD9D4D039);d=HH(d,a,b,c,x[k+12],S32,0xE6DB99E5);c=HH(c,d,a,b,x[k+15],S33,0x1FA27CF8);b=HH(b,c,d,a,x[k+2],S34,0xC4AC5665);a=II(a,b,c,d,x[k+0],S41,0xF4292244);d=II(d,a,b,c,x[k+7],S42,0x432AFF97);c=II(c,d,a,b,x[k+14],S43,0xAB9423A7);b=II(b,c,d,a,x[k+5],S44,0xFC93A039);a=II(a,b,c,d,x[k+12],S41,0x655B59C3);d=II(d,a,b,c,x[k+3],S42,0x8F0CCC92);c=II(c,d,a,b,x[k+10],S43,0xFFEFF47D);b=II(b,c,d,a,x[k+1],S44,0x85845DD1);a=II(a,b,c,d,x[k+8],S41,0x6FA87E4F);d=II(d,a,b,c,x[k+15],S42,0xFE2CE6E0);c=II(c,d,a,b,x[k+6],S43,0xA3014314);b=II(b,c,d,a,x[k+13],S44,0x4E0811A1);a=II(a,b,c,d,x[k+4],S41,0xF7537E82);d=II(d,a,b,c,x[k+11],S42,0xBD3AF235);c=II(c,d,a,b,x[k+2],S43,0x2AD7D2BB);b=II(b,c,d,a,x[k+9],S44,0xEB86D391);a=addUnsigned(a,AA);b=addUnsigned(b,BB);c=addUnsigned(c,CC);d=addUnsigned(d,DD);}
var tempValue=wordToHex(a)+wordToHex(b)+wordToHex(c)+wordToHex(d);return tempValue.toLowerCase();}});})(jQuery);


/************************************************************************
 *
 * Jquery 扩展函数
 *
 ************************************************************************/
var base64EncodeChars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";
var base64DecodeChars = new Array(
    -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
    -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
    -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 62, -1, -1, -1, 63,
    52, 53, 54, 55, 56, 57, 58, 59, 60, 61, -1, -1, -1, -1, -1, -1,
    -1,  0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14,
    15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, -1, -1, -1, -1, -1,
    -1, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
    41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, -1, -1, -1, -1, -1);

function base64encode(str) {
    var out, i, len;
    var c1, c2, c3;

    len = str.length;
    i = 0;
    out = "";
    while(i < len) {
    c1 = str.charCodeAt(i++) & 0xff;
    if(i == len)
    {
        out += base64EncodeChars.charAt(c1 >> 2);
        out += base64EncodeChars.charAt((c1 & 0x3) << 4);
        out += "==";
        break;
    }
    c2 = str.charCodeAt(i++);
    if(i == len)
    {
        out += base64EncodeChars.charAt(c1 >> 2);
        out += base64EncodeChars.charAt(((c1 & 0x3)<< 4) | ((c2 & 0xF0) >> 4));
        out += base64EncodeChars.charAt((c2 & 0xF) << 2);
        out += "=";
        break;
    }
    c3 = str.charCodeAt(i++);
    out += base64EncodeChars.charAt(c1 >> 2);
    out += base64EncodeChars.charAt(((c1 & 0x3)<< 4) | ((c2 & 0xF0) >> 4));
    out += base64EncodeChars.charAt(((c2 & 0xF) << 2) | ((c3 & 0xC0) >>6));
    out += base64EncodeChars.charAt(c3 & 0x3F);
    }
    return out;
}

function base64decode(str) {
    var c1, c2, c3, c4;
    var i, len, out;

    len = str.length;
    i = 0;
    out = "";
    while(i < len) {
    /* c1 */
    do {
        c1 = base64DecodeChars[str.charCodeAt(i++) & 0xff];
    } while(i < len && c1 == -1);
    if(c1 == -1)
        break;

    /* c2 */
    do {
        c2 = base64DecodeChars[str.charCodeAt(i++) & 0xff];
    } while(i < len && c2 == -1);
    if(c2 == -1)
        break;

    out += String.fromCharCode((c1 << 2) | ((c2 & 0x30) >> 4));

    /* c3 */
    do {
        c3 = str.charCodeAt(i++) & 0xff;
        if(c3 == 61)
        return out;
        c3 = base64DecodeChars[c3];
    } while(i < len && c3 == -1);
    if(c3 == -1)
        break;

    out += String.fromCharCode(((c2 & 0XF) << 4) | ((c3 & 0x3C) >> 2));

    /* c4 */
    do {
        c4 = str.charCodeAt(i++) & 0xff;
        if(c4 == 61)
        return out;
        c4 = base64DecodeChars[c4];
    } while(i < len && c4 == -1);
    if(c4 == -1)
        break;
    out += String.fromCharCode(((c3 & 0x03) << 6) | c4);
    }
    return out;
}

function utf16to8(str) {
    var out, i, len, c;

    out = "";
    len = str.length;
    for(i = 0; i < len; i++) {
    c = str.charCodeAt(i);
    if ((c >= 0x0001) && (c <= 0x007F)) {
        out += str.charAt(i);
    } else if (c > 0x07FF) {
        out += String.fromCharCode(0xE0 | ((c >> 12) & 0x0F));
        out += String.fromCharCode(0x80 | ((c >>  6) & 0x3F));
        out += String.fromCharCode(0x80 | ((c >>  0) & 0x3F));
    } else {
        out += String.fromCharCode(0xC0 | ((c >>  6) & 0x1F));
        out += String.fromCharCode(0x80 | ((c >>  0) & 0x3F));
    }
    }
    return out;
}

function utf8to16(str) {
    var out, i, len, c;
    var char2, char3;

    out = "";
    len = str.length;
    i = 0;
    while(i < len) {
    c = str.charCodeAt(i++);
    switch(c >> 4)
    { 
      case 0: case 1: case 2: case 3: case 4: case 5: case 6: case 7:
        // 0xxxxxxx
        out += str.charAt(i-1);
        break;
      case 12: case 13:
        // 110x xxxx   10xx xxxx
        char2 = str.charCodeAt(i++);
        out += String.fromCharCode(((c & 0x1F) << 6) | (char2 & 0x3F));
        break;
      case 14:
        // 1110 xxxx  10xx xxxx  10xx xxxx
        char2 = str.charCodeAt(i++);
        char3 = str.charCodeAt(i++);
        out += String.fromCharCode(((c & 0x0F) << 12) |
                       ((char2 & 0x3F) << 6) |
                       ((char3 & 0x3F) << 0));
        break;
    }
    }

    return out;
}

function CharToHex(str) {
    var out, i, len, c, h;
    out = "";
    len = str.length;
    i = 0;
    while(i < len) 
    {
        c = str.charCodeAt(i++);
        h = c.toString(16);
        if(h.length < 2)
            h = "0" + h;
        
        out += "\\x" + h + " ";
        if(i > 0 && i % 8 == 0)
            out += "\r\n";
    }

    return out;
}

function doEncode() {
    var src = document.getElementById('src').value;
    document.getElementById('dest').value = base64encode(utf16to8(src));
}

function doDecode() {
    var src = document.getElementById('src').value;
    var opts = document.getElementById('opt');

    if(opts.checked)
    {
        document.getElementById('dest').value = CharToHex(base64decode(src));
    }
    else
    {
        document.getElementById('dest').value = utf8to16(base64decode(src));
    }
}

/*!
 * jQuery Cookie Plugin v1.3.1
 * https://github.com/carhartl/jquery-cookie
 *
 */
(function(a){if(typeof define==="function"&&define.amd){define(["jquery"],a)}else{a(jQuery)}}(function(e){var a=/\+/g;function d(g){return g}function b(g){return decodeURIComponent(g.replace(a," "))}function f(g){if(g.indexOf('"')===0){g=g.slice(1,-1).replace(/\\"/g,'"').replace(/\\\\/g,"\\")}try{return c.json?JSON.parse(g):g}catch(h){}}var c=e.cookie=function(p,o,u){if(o!==undefined){u=e.extend({},c.defaults,u);if(typeof u.expires==="number"){var q=u.expires,s=u.expires=new Date();s.setDate(s.getDate()+q)}o=c.json?JSON.stringify(o):String(o);return(document.cookie=[c.raw?p:encodeURIComponent(p),"=",c.raw?o:encodeURIComponent(o),u.expires?"; expires="+u.expires.toUTCString():"",u.path?"; path="+u.path:"",u.domain?"; domain="+u.domain:"",u.secure?"; secure":""].join(""))}var g=c.raw?d:b;var r=document.cookie.split("; ");var v=p?undefined:{};for(var n=0,k=r.length;n<k;n++){var m=r[n].split("=");var h=g(m.shift());var j=g(m.join("="));if(p&&p===h){v=f(j);break}if(!p){v[h]=f(j)}}return v};c.defaults={};e.removeCookie=function(h,g){if(e.cookie(h)!==undefined){e.cookie(h,"",e.extend({},g,{expires:-1}));return true}return false}}));
(function(b) {
    b.fn.fakeLoader = function(m) {
        var f = b.extend({ timeToHide: null, pos: "fixed", top: "0px", left: "0px", width: "100%", height: "100%", zIndex: "2000", bgColor: "#2ecc71", spinner: "spinner7", imagePath: "", opacity: 0.5 }, m);
        var l = '<div class="fl spinner1"><div class="double-bounce1"></div><div class="double-bounce2"></div></div>';
        var k = '<div class="fl spinner2"><div class="spinner-container container1"><div class="circle1"></div><div class="circle2"></div><div class="circle3"></div><div class="circle4"></div></div><div class="spinner-container container2"><div class="circle1"></div><div class="circle2"></div><div class="circle3"></div><div class="circle4"></div></div><div class="spinner-container container3"><div class="circle1"></div><div class="circle2"></div><div class="circle3"></div><div class="circle4"></div></div></div>';
        var j = '<div class="fl spinner3"><div class="dot1"></div><div class="dot2"></div></div>';
        var i = '<div class="fl spinner4"></div>';
        var h = '<div class="fl spinner5"><div class="cube1"></div><div class="cube2"></div></div>';
        var g = '<div class="fl spinner6"><div class="rect1"></div><div class="rect2"></div><div class="rect3"></div><div class="rect4"></div><div class="rect5"></div></div>';
        var e = '<div class="fl spinner7"><div class="circ1"></div><div class="circ2"></div><div class="circ3"></div><div class="circ4"></div></div>';
        var d = b(this);
        var c = { position: f.pos, width: f.width, height: f.height, top: f.top, left: f.left };
        d.css(c);
        d.each(function() {
            var n = f.spinner;
            switch (n) {
                case "spinner1":
                    d.html(l);
                    break;
                case "spinner2":
                    d.html(k);
                    break;
                case "spinner3":
                    d.html(j);
                    break;
                case "spinner4":
                    d.html(i);
                    break;
                case "spinner5":
                    d.html(h);
                    break;
                case "spinner6":
                    d.html(g);
                    break;
                case "spinner7":
                    d.html(e);
                    break;
                default:
                    d.html(l)
            }
            if (f.text != "" && f.text!=undefined) {
                d.html('<div class="fl"><span style="color:#fff;font-size:25px;letter-spacing:2px;">'+f.text+'</span></div>');
                a();
            }
            if (f.imagePath != "") {
                d.html('<div class="fl"><img src="' + f.imagePath + '"></div>');
                a();
            }
            a();
        });
        if (f.timeToHide != null) { setTimeout(function() { b(d).fadeOut() }, f.timeToHide) };
        return this.css({ backgroundColor: f.bgColor, zIndex: f.zIndex, opacity: f.opacity })
    };

    function a() {
        var c = b(window).width();
        var e = b(window).height();
        var d = b(".fl").outerWidth();
        var f = b(".fl").outerHeight();
        b(".fl").css({ position: "absolute", left: (c / 2) - (d / 2), top: (e / 2) - (f / 2) })
    }
    b(window).load(function() {
        a();
        b(window).resize(function() { a() })
    })
}(jQuery));/*!
 dialog 1.1.0
*/
;(function(win,$){var wrap,overlay,content,title,close,cancelBtn,okBtn,delBtn,settings,timer;var _renderDOM=function(){if($('.dialog-wrap').length>0){return}clearTimeout(timer);settings.onBeforeShow();$('body').append(dialogWrapper=$('<div class="dialog-wrap '+settings.dialogClass+'"></div>'));dialogWrapper.append(overlay=$('<div class="dialog-overlay"></div>'),content=$('<div class="dialog-content"></div>'));switch(settings.type){case'alert':if(settings.showTitle){content.append(title=$('<div class="dialog-content-hd"><h4 class="dialog-content-title">'+settings.titleText+'</h4></div>'))}content.append(contentBd=$('<div class="dialog-content-bd">'+settings.contentHtml+'</div>'));content.append(contentFt=$('<div class="dialog-content-ft"></div>'));contentFt.append(okBtn=$('<a class="dialog-btn dialog-btn-ok '+settings.buttonClass.ok+'" href="javascript:;">'+settings.buttonText.ok+'</a>'));break;case'confirm':if(settings.showTitle){content.append(title=$('<div class="dialog-content-hd"><h4 class="dialog-content-title">'+settings.titleText+'</h4></div>'))}content.append(contentBd=$('<div class="dialog-content-bd">'+settings.contentHtml+'</div>'));content.append(contentFt=$('<div class="dialog-content-ft"></div>'));contentFt.append(cancelBtn=$('<a class="dialog-btn dialog-btn-cancel '+settings.buttonClass.cancel+'" href="javascript:;">'+settings.buttonText.cancel+'</a>'),okBtn=$('<a class="dialog-btn dialog-btn-ok '+settings.buttonClass.ok+'" href="javascript:;">'+settings.buttonText.ok+'</a>'));break;case'info':var infoContent=settings.contentHtml||'<img class="info-icon" src="'+settings.infoIcon+'" alt="'+settings.infoText+'" /><p class="info-text">'+settings.infoText+'</p>';content.append(contentBd=$('<div class="dialog-content-bd">'+infoContent+'</div>'));dialogWrapper.addClass('dialog-wrap-info');content.addClass('dialog-content-info');break;default:break}setTimeout(function(){dialogWrapper.addClass('dialog-wrap-show');settings.onShow()},10)};var _bindEvent=function(){$(okBtn).on('click',function(e){var r=settings.onClickOk(e);if(r==false)return false;$.dialog.close();return false});$(cancelBtn).on('click',function(e){settings.onClickCancel(e);$.dialog.close();return false});if(settings.overlayClose){overlay.on('click',function(e){$.dialog.close()})}if(settings.autoClose>0){_autoClose()}};var _autoClose=function(){clearTimeout(timer);timer=window.setTimeout(function(){$.dialog.close()},settings.autoClose)};$.dialog=function(options){settings=$.extend({},$.fn.dialog.defaults,options);$.dialog.init();return this};$.dialog.init=function(){_renderDOM();_bindEvent()};$.dialog.close=function(){settings.onBeforeClosed();dialogWrapper.removeClass('dialog-wrap-show');setTimeout(function(){dialogWrapper.remove();settings.onClosed()},200)};$.dialog.update=function(params){if(params.infoText){content.find('.info-text').html(params.infoText)}if(params.infoIcon){content.find('.info-icon').attr('src',params.infoIcon)}if(params.autoClose>0){window.setTimeout(function(){$.dialog.close()},params.autoClose)}};$.fn.dialog=function(options){return this};$.fn.dialog.defaults={type:'alert',titleText:'信息提示',showTitle:true,contentHtml:'',dialogClass:'',autoClose:0,overlayClose:false,drag:false,buttonText:{ok:'确定',cancel:'取消',delete:'删除'},buttonClass:{ok:'',cancel:'',delete:''},infoText:'',infoIcon:'',onClickOk:function(e){},onClickCancel:function(e){},onClickClose:function(){},onBeforeShow:function(){},onShow:function(){},onBeforeClosed:function(){},onClosed:function(){}}})(window,window.Zepto||window.jQuery);

/*
    瀑布模式布局
    usage:

        $("#container").mpmansory(
            {
                childrenClass: 'item', // default is a div
                columnClasses: 'padding', //add classes to items
                breakpoints:{
                    lg: 3, 
                    md: 4, 
                    sm: 6,
                    xs: 12
                },
                distributeBy: { order: false, height: false, attr: 'data-order', attrOrder: 'asc' }, //default distribute by order, options => order: true/false, height: true/false, attr => 'data-order', attrOrder=> 'asc'/'desc'
                onload: function (items) {
                    //make somthing with items
                } 
            }
        );
*/
!function(r){r.fn.mpmansory=function(t){var n=r.extend({childrenClass:"",breakpoints:{lg:4,md:4,sm:6,xs:12},distributeBy:{attr:"data-order",attrOrder:"asc",order:!1,height:!1},onload:function(r){return!0}},t)
return Array.min=function(r){return Math.min.apply(Math,r)},r.emptyArray=function(r){for(var t=0;t<r.length;t++)r[t].remove()
return new Array},r.fn.initialize=function(t,n){for(var e=[],i=0;t>i;i++){var a=r("<div></div>")
a.addClass(n),r(this).append(a),e.push(a)}return e},r.fn.distributeItemsByHeight=function(r,t){for(var n=0;n<t.length;n++){for(var e=new Array,i=0;i<r.length;i++)e.push(r[i].height())
var a=Array.min(e)==Number.POSITIVE_INFINITY||Array.min(e)==Number.NEGATIVE_INFINITY?0:Array.min(e)
r[e.indexOf(a)].append(t[n])}},r.fn.getCurrentColumnSize=function(){return r(window).width()>1200?"lg":r(window).width()>992?"md":r(window).width()>720?"sm":r(window).width()>480?"xs":(r(window).width()>320,"xs")},r.fn.distributeItemsByOrder=function(r,t){for(var n=0,e=0;e<t.length;e++)n==r.length&&(n=0),r[n].append(t[e]),n++},r.fn.orderItemsByAttr=function(t,n){for(var e=new Array,i=0;i<t.length;i++)e.push(r(t[i]).attr(n.attr))
"asc"==n.attrOrder?e.sort(function(r,t){return r-t}):e.sort(function(r,t){return t-r})
for(var a=new Array,s=0;s<e.length;s++){var o=r.grep(t,function(t){return r(t).attr(n.attr)==e[s]})
a.push(o)}return a},r.fn.distributeItemsByAttr=function(t,n,e){for(var i=0,a=0,s=0;s<n.length;s++)i==t.length&&(i=0),n[s].length>1?(a==n[s].length&&(a=0),t[i].append(r(n[s][a])),a++):t[i].append(r(n[s])),i++},r.fn.apply=function(t,n,e,i){var a=r(this),s=(a.getCurrentColumnSize(),n),o="col-lg-"+t.breakpoints.lg+" col-md-"+t.breakpoints.md+" col-sm-"+t.breakpoints.sm+" col-xs-"+t.breakpoints.xs+" "+t.columnClasses
return e=r(this).initialize(s,o),t.distributeBy.order?a.distributeItemsByOrder(e,i):t.distributeBy.height?a.distributeItemsByHeight(e,i):t.distributeBy.attr&&a.distributeItemsByAttr(e,a.orderItemsByAttr(i,t.distributeBy),t.distributeBy),{wrappers:e,items:i}},this.each(function(){var t=r(this),e=t.getCurrentColumnSize(),i=12/n.breakpoints[e],a=t.children(""!=n.childrenClass?"."+n.childrenClass:"div"),s=new Array,o=t.apply(n,i,s,a)
s=o.wrappers,r(window).on("resize",function(u){t.getCurrentColumnSize()!=e&&(i=12/n.breakpoints[t.getCurrentColumnSize()],s=r.emptyArray(s),o=t.apply(n,i,s,a),s=o.wrappers,e=t.getCurrentColumnSize())}),n.hasOwnProperty("onload")&&n.onload(a)})}}(jQuery)

/*
 * PDSort: drag and drop sorting.
 * @param {Object} options
 *        target[string]:       可选，jQuery事件委托选择器字符串，默认'li'
 *        cloneStyle[object]:   可选，设置占位符元素的样式
 *        floatStyle[object]:   可选，设置拖动元素的样式
 *        down[function]:       可选，鼠标按下时执行的函数
 *        move[function]:       可选，鼠标移动时执行的函数
 *        up[function]:         可选，鼠标抬起时执行的函数
*/
;(function($){$.fn.PDSort=function(options){var $doc=$(document),fnEmpty=function(){},settings=$.extend(true,{down:fnEmpty,move:fnEmpty,up:fnEmpty,target:'li',cloneStyle:{'background-color':'#eee'},floatStyle:{'position':'fixed','box-shadow':'10px 10px 20px 0 #eee','webkitTransform':'rotate(4deg)','mozTransform':'rotate(4deg)','msTransform':'rotate(4deg)','transform':'rotate(4deg)'}},options);return this.each(function(){var that=$(this),height='height',width='width';if(that.css('box-sizing')=='border-box'){height='outerHeight';width='outerWidth'}that.on('mousedown.PDSort',settings.target,function(e){if(e.which!=1){return}var tagName=e.target.tagName.toLowerCase();if(tagName=='input'||tagName=='textarea'||tagName=='select'){return}var THIS=this,$this=$(THIS),offset=$this.offset(),disX=e.pageX-offset.left,disY=e.pageY-offset.top,clone=$this.clone().css(settings.cloneStyle).css('height',$this[height]()).empty(),hasClone=1,thisOuterHeight=$this.outerHeight(),thatOuterHeight=that.outerHeight(),upSpeed=thisOuterHeight,downSpeed=thisOuterHeight,maxSpeed=thisOuterHeight*3;settings.down.call(THIS);$doc.on('mousemove.PDSort',function(e){if(hasClone){$this.before(clone).css('width',$this[width]()).css(settings.floatStyle).appendTo($this.parent());hasClone=0}var left=e.pageX-disX,top=e.pageY-disY,prev=clone.prev(),next=clone.next().not($this);$this.css({left:left,top:top});if(prev.length&&top<prev.offset().top+prev.outerHeight()/2){clone.after(prev)}else if(next.length&&top+thisOuterHeight>next.offset().top+next.outerHeight()/2){clone.before(next)}var thatScrollTop=that.scrollTop(),thatOffsetTop=that.offset().top,scrollVal;if(top<thatOffsetTop){downSpeed=thisOuterHeight;upSpeed=++upSpeed>maxSpeed?maxSpeed:upSpeed;scrollVal=thatScrollTop-upSpeed}else if(top+thisOuterHeight-thatOffsetTop>thatOuterHeight){upSpeed=thisOuterHeight;downSpeed=++downSpeed>maxSpeed?maxSpeed:downSpeed;scrollVal=thatScrollTop+downSpeed}that.scrollTop(scrollVal);settings.move.call(THIS)}).on('mouseup.PDSort',function(){$doc.off('mousemove.PDSort mouseup.PDSort');if(!hasClone){clone.before($this.removeAttr('style')).remove();settings.up.call(THIS)}});return false})})}})(jQuery);

/*
 *
 * GO UP Version 1.1.0
 * (https://github.com/Ryuk87)
 *
 */
!function(t){"use strict";function e(t,e,i){if("show"==e)switch(i){case"fade":t.fadeIn();break;case"slide":t.slideDown();break;default:t.fadeIn()}else switch(i){case"fade":t.fadeOut();break;case"slide":t.slideUp();break;default:t.fadeOut()}}function i(e,i){var o=!0;e.on("click",function(){1==o&&(o=!1,t("html, body").animate({scrollTop:0},i,function(){o=!0}))})}t.goup=function(o){var n=t.extend({location:"right",locationOffset:20,bottomOffset:10,containerSize:40,containerRadius:10,containerClass:"goup-container",arrowClass:"goup-arrow",alwaysVisible:!1,trigger:500,entryAnimation:"fade",goupSpeed:"slow",hideUnderWidth:500,containerColor:"#000",arrowColor:"#fff",title:"",titleAsText:!1,titleAsTextClass:"goup-text",zIndex:1},o);"right"!=n.location&&"left"!=n.location&&(n.location="right"),n.locationOffset<0&&(n.locationOffset=0),n.bottomOffset<0&&(n.bottomOffset=0),n.containerSize<20&&(n.containerSize=20),n.containerRadius<0&&(n.containerRadius=0),n.trigger<0&&(n.trigger=0),n.hideUnderWidth<0&&(n.hideUnderWidth=0);var r=/(^#[0-9A-F]{6}$)|(^#[0-9A-F]{3}$)/i;r.test(n.containerColor)||(n.containerColor="#000"),r.test(n.arrowColor)||(n.arrowColor="#fff"),""===n.title&&(n.titleAsText=!1),isNaN(n.zIndex)&&(n.zIndex=1);var a=t("body"),s=t(window),d=t("<div>");d.addClass(n.containerClass);var l=t("<div>");l.addClass(n.arrowClass),d.html(l),a.append(d);var c={position:"fixed",width:n.containerSize,height:n.containerSize,background:n.containerColor,cursor:"pointer",display:"none","z-index":n.zIndex};if(c.bottom=n.bottomOffset,c[n.location]=n.locationOffset,c["border-radius"]=n.containerRadius,d.css(c),n.titleAsText){var f=t("<div>");a.append(f),f.addClass(n.titleAsTextClass).text(n.title),f.attr("style",d.attr("style")),f.css("background","transparent").css("width",n.containerSize+40).css("height","auto").css("text-align","center").css(n.location,n.locationOffset-20);var h=parseInt(f.height())+10,p=parseInt(d.css("bottom")),u=h+p;d.css("bottom",u)}else d.attr("title",n.title);var g=.25*n.containerSize,y={width:0,height:0,margin:"0 auto","padding-top":Math.ceil(.325*n.containerSize),"border-style":"solid","border-width":"0 "+g+"px "+g+"px "+g+"px","border-color":"transparent transparent "+n.arrowColor+" transparent"};l.css(y);var w=!1;s.resize(function(){s.outerWidth()<=n.hideUnderWidth?(w=!0,e(d,"hide",n.entryAnimation),"undefined"!=typeof f&&e(f,"hide",n.entryAnimation)):(w=!1,s.trigger("scroll"))}),s.outerWidth()<=n.hideUnderWidth&&(w=!0,d.hide(),"undefined"!=typeof f&&f.hide()),n.alwaysVisible?(e(d,"show",n.entryAnimation),"undefined"!=typeof f&&e(f,"show",n.entryAnimation)):s.scroll(function(){s.scrollTop()>=n.trigger&&!w&&(e(d,"show",n.entryAnimation),"undefined"!=typeof f&&e(f,"show",n.entryAnimation)),s.scrollTop()<n.trigger&&!w&&(e(d,"hide",n.entryAnimation),"undefined"!=typeof f&&e(f,"hide",n.entryAnimation))}),s.scrollTop()>=n.trigger&&!w&&(e(d,"show",n.entryAnimation),"undefined"!=typeof f&&e(f,"show",n.entryAnimation)),i(d,n.goupSpeed),"undefined"!=typeof f&&i(f,n.goupSpeed)}}(jQuery);
/* ===========================================================
 * jquery-jumpto.js v1
 * https://github.com/peachananr/jumpto
 *
 * ========================================================== */
!function($){
  
  var defaults = {
    firstLevel: "> h2",
    secondLevel: false,
    innerWrapper: ".jumpto-block",
    offset: 400,
    animate: 1000,
    navContainer: false,
    anchorTopPadding: 20,
    showTitle: "Jump To",
    closeButton: true
    };
    
    function isScrolledIntoView(elem)
  {
      var docViewTop = $(window).scrollTop();
      var docViewBottom = docViewTop + ($(window).height() /4);
      
      var elemTop = $(elem).offset().top;
      var elemBottom = elemTop + $(elem).height();

      return ((elemBottom <= docViewBottom) && (elemTop >= docViewTop));
  }
    
  $.fn.jumpto = function(options){
    var settings = $.extend({}, defaults, options),
        el = $(this),
        html = "",
        block = $(settings.innerWrapper),
        selectors = "",
        title = "",
        close ="";
        
    el.addClass("jumpto-cotainer");
    
    redrawMenu = function(){
      $(selectors.slice(0,-2)).each(function( index ) {
        if (isScrolledIntoView($(this))) {
          $(".jumpto-subnav a").removeClass("active").parent().find(" a[href='#"+$(this).attr("id")+"']").addClass("active")
          
          if($("a[href='#"+$(this).attr("id")+"']").parent().parent().hasClass("jumpto-second")) {
            $("a[href='#"+$(this).attr("id")+"']").closest(".jumpto-second").show()
          }
          if($("a[href='#"+$(this).attr("id")+"']").parent().parent().hasClass("jumpto-first")) {
            $("a[href='#"+$(this).attr("id")+"']").closest(".jumpto-first").find(".jumpto-second").hide()
          }
          if($("a[href='#"+$(this).attr("id")+"']").parent().find(".jumpto-second")) {
            $("a[href='#"+$(this).attr("id")+"']").parent().find(".jumpto-second").show()
          }
        }
      });
      if($(document).scrollTop() > settings.offset) {
        $(".jumpto-subnav").removeClass("bottom").addClass("fixed");
      } else {
        $(".jumpto-subnav").removeClass("bottom fixed");
      }
      if( !el.hasClass('hidden') && $(document).scrollTop() > el.outerHeight(true)) {
        $(".jumpto-subnav").addClass("bottom fixed");
      }
    }
    
    block.find(settings.firstLevel).each(function( index ) {
      var b = $(this),
          i = index,
          inner_html = "";
      if ( b.parent().find(settings.secondLevel).length > 0) {
        inner_html += "<ul class='jumpto-second'>"
        b.parent().find(settings.secondLevel).each(function( index ) {
          var id = "jumpto_" + i + "_" + index;
          $(this).attr("id", id);
          link_to = "<a href='#" + id + "'>" + $(this).text() + "</a>"
          inner_html += "<li>" + link_to + "</li>"
          selectors += "#"+id + ", ";
        });
        inner_html += "</ul>"
        var id = "jumpto_" + i;
        b.attr("id", id);
        link_to = "<a href='#" + id + "'>" + b.text() + "</a>"
        selectors += "#"+id + ", ";
        html += "<li>" + link_to + inner_html + "</li>"
      } else {
        var id = "jumpto_" + i;
        link_to = "<a href='#" + id + "'>" + b.text() + "</a>"
        b.attr("id", id);
        selectors += "#"+id + ", ";
        html += "<li>" + link_to + "</li>"
      }
    });
    if (settings.showTitle != false) {
      var title = "<div class='jumpto-title'>"+settings.showTitle+"</div>"
    }
    
    if (settings.closeButton != false) {
      var close = "<div class='jumpto-close'><a href='#' id='jumpto-close'>Close</a></div>"
    }
    if(settings.navContainer == false) {
      $(this).append("<nav class='jumpto-subnav'>"+ title +"<ul class='jumpto-first'>" + html + "</ul>"+ close +"</nav>")
    }else{
      $(settings.navContainer).addClass("jumpto-subnav").html(title +"<ul class='jumpto-first'>" + html + "</ul>"+ close)
    }
    
    
    $('.jumpto-subnav a[href*="#"]:not([href="#"])').click(function() {
      if (location.pathname.replace(/^\//,'') == this.pathname.replace(/^\//,'') 
          || location.hostname == this.hostname) {
    
        var target = $(this.hash);
        target = target.length ? target : $('[name=' + this.hash.slice(1) +']');
        if (target.length) {
          $('html,body').animate({
            scrollTop: target.offset().top - settings.anchorTopPadding
          }, settings.animate, 'swing');
          return false;
        }
      }
    });
    
    $(window).scroll(function() {
      redrawMenu()
    });
    
    $(".jumpto-subnav #jumpto-close").click(function() {
      var btn = $(this)
      btn.parent().parent().find("> .jumpto-first").slideToggle( "slow", function() {
          if ($(this).is(":visible")) {
            btn.html("Close");
          } else {
            btn.html("Open");
          }
        });
        return false;
    });
    
    setInterval(function() {
      var track = [];
      $(selectors.slice(0,-2)).each(function( index ) {
        track.push(isScrolledIntoView($(this)))
      });
      if($.inArray(true, track) == -1) {
        $(".jumpto-subnav a").removeClass("active")
        $(".jumpto-subnav .jumpto-second").hide()
      }
    }, 500);
  }
}(window.jQuery);

/*
 * Purl (A JavaScript URL parser) v2.3.1
 * url 的 参数获取
 */
 ;(function(factory){if(typeof define==='function'&&define.amd){define(factory)}else{window.purl=factory()}})(function(){var tag2attr={a:'href',img:'src',form:'action',base:'href',script:'src',iframe:'src',link:'href',embed:'src',object:'data'},key=['source','protocol','authority','userInfo','user','password','host','port','relative','path','directory','file','query','fragment'],aliases={'anchor':'fragment'},parser={strict:/^(?:([^:\/?#]+):)?(?:\/\/((?:(([^:@]*):?([^:@]*))?@)?([^:\/?#]*)(?::(\d*))?))?((((?:[^?#\/]*\/)*)([^?#]*))(?:\?([^#]*))?(?:#(.*))?)/,loose:/^(?:(?![^:@]+:[^:@\/]*@)([^:\/?#.]+):)?(?:\/\/)?((?:(([^:@]*):?([^:@]*))?@)?([^:\/?#]*)(?::(\d*))?)(((\/(?:[^?#](?![^?#\/]*\.[^?#\/.]+(?:[?#]|$)))*\/?)?([^?#\/]*))(?:\?([^#]*))?(?:#(.*))?)/},isint=/^[0-9]+$/;function parseUri(url,strictMode){var str=decodeURI(url),res=parser[strictMode||false?'strict':'loose'].exec(str),uri={attr:{},param:{},seg:{}},i=14;while(i--){uri.attr[key[i]]=res[i]||''}uri.param['query']=parseString(uri.attr['query']);uri.param['fragment']=parseString(uri.attr['fragment']);uri.seg['path']=uri.attr.path.replace(/^\/+|\/+$/g,'').split('/');uri.seg['fragment']=uri.attr.fragment.replace(/^\/+|\/+$/g,'').split('/');uri.attr['base']=uri.attr.host?(uri.attr.protocol?uri.attr.protocol+'://'+uri.attr.host:uri.attr.host)+(uri.attr.port?':'+uri.attr.port:''):'';return uri}function getAttrName(elm){var tn=elm.tagName;if(typeof tn!=='undefined')return tag2attr[tn.toLowerCase()];return tn}function promote(parent,key){if(parent[key].length===0)return parent[key]={};var t={};for(var i in parent[key])t[i]=parent[key][i];parent[key]=t;return t}function parse(parts,parent,key,val){var part=parts.shift();if(!part){if(isArray(parent[key])){parent[key].push(val)}else if('object'==typeof parent[key]){parent[key]=val}else if('undefined'==typeof parent[key]){parent[key]=val}else{parent[key]=[parent[key],val]}}else{var obj=parent[key]=parent[key]||[];if(']'==part){if(isArray(obj)){if(''!==val)obj.push(val)}else if('object'==typeof obj){obj[keys(obj).length]=val}else{obj=parent[key]=[parent[key],val]}}else if(~part.indexOf(']')){part=part.substr(0,part.length-1);if(!isint.test(part)&&isArray(obj))obj=promote(parent,key);parse(parts,obj,part,val)}else{if(!isint.test(part)&&isArray(obj))obj=promote(parent,key);parse(parts,obj,part,val)}}}function merge(parent,key,val){if(~key.indexOf(']')){var parts=key.split('[');parse(parts,parent,'base',val)}else{if(!isint.test(key)&&isArray(parent.base)){var t={};for(var k in parent.base)t[k]=parent.base[k];parent.base=t}if(key!==''){set(parent.base,key,val)}}return parent}function parseString(str){return reduce(String(str).split(/&|;/),function(ret,pair){try{pair=decodeURIComponent(pair.replace(/\+/g,' '))}catch(e){}var eql=pair.indexOf('='),brace=lastBraceInKey(pair),key=pair.substr(0,brace||eql),val=pair.substr(brace||eql,pair.length);val=val.substr(val.indexOf('=')+1,val.length);if(key===''){key=pair;val=''}return merge(ret,key,val)},{base:{}}).base}function set(obj,key,val){var v=obj[key];if(typeof v==='undefined'){obj[key]=val}else if(isArray(v)){v.push(val)}else{obj[key]=[v,val]}}function lastBraceInKey(str){var len=str.length,brace,c;for(var i=0;i<len;++i){c=str[i];if(']'==c)brace=false;if('['==c)brace=true;if('='==c&&!brace)return i}}function reduce(obj,accumulator){var i=0,l=obj.length>>0,curr=arguments[2];while(i<l){if(i in obj)curr=accumulator.call(undefined,curr,obj[i],i,obj);++i}return curr}function isArray(vArg){return Object.prototype.toString.call(vArg)==="[object Array]"}function keys(obj){var key_array=[];for(var prop in obj){if(obj.hasOwnProperty(prop))key_array.push(prop)}return key_array}function purl(url,strictMode){if(arguments.length===1&&url===true){strictMode=true;url=undefined}strictMode=strictMode||false;url=url||window.location.toString();return{data:parseUri(url,strictMode),attr:function(attr){attr=aliases[attr]||attr;return typeof attr!=='undefined'?this.data.attr[attr]:this.data.attr},param:function(param){return typeof param!=='undefined'?this.data.param.query[param]:this.data.param.query},fparam:function(param){return typeof param!=='undefined'?this.data.param.fragment[param]:this.data.param.fragment},segment:function(seg){if(typeof seg==='undefined'){return this.data.seg.path}else{seg=seg<0?this.data.seg.path.length+seg:seg-1;return this.data.seg.path[seg]}},fsegment:function(seg){if(typeof seg==='undefined'){return this.data.seg.fragment}else{seg=seg<0?this.data.seg.fragment.length+seg:seg-1;return this.data.seg.fragment[seg]}}}}purl.jQuery=function($){if($!=null){$.fn.url=function(strictMode){var url='';if(this.length){url=$(this).attr(getAttrName(this[0]))||''}return purl(url,strictMode)};$.url=purl}};purl.jQuery(window.jQuery);return purl});

/*  
 * Generate a random uuid.  
 *  
 * USAGE: Math.uuid(length, radix)  
 *   length - the desired number of characters  
 *   radix  - the number of allowable values for each character.  
 *  
 * EXAMPLES:  
 *   // No arguments  - returns RFC4122, version 4 ID  
 *   >>> Math.uuid()  
 *   "92329D39-6F5C-4520-ABFC-AAB64544E172"  
 *  
 *   // One argument - returns ID of the specified length  
 *   >>> Math.uuid(15)     // 15 character ID (default base=62)  
 *   "VcydxgltxrVZSTV"  
 *  
 *   // Two arguments - returns ID of the specified length, and radix. (Radix must be <= 62)  
 *   >>> Math.uuid(8, 2)  // 8 character ID (base=2)  
 *   "01001010"  
 *   >>> Math.uuid(8, 10) // 8 character ID (base=10)  
 *   "47473046"  
 *   >>> Math.uuid(8, 16) // 8 character ID (base=16)  
 *   "098F4D35"  
 */  
(function() {   
  // Private array of chars to use   
  var CHARS = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'.split('');   
    
  Math.uuid = function (len, radix) {   
    var chars = CHARS, uuid = [], i;   
    radix = radix || chars.length;   
    
    if (len) {   
      // Compact form   
      for (i = 0; i < len; i++) uuid[i] = chars[0 | Math.random()*radix];   
    } else {   
      // rfc4122, version 4 form   
      var r;   
    
      // rfc4122 requires these characters   
      uuid[8] = uuid[13] = uuid[18] = uuid[23] = '-';   
      uuid[14] = '4';   
    
      // Fill in random data.  At i==19 set the high bits of clock sequence as   
      // per rfc4122, sec. 4.1.5   
      for (i = 0; i < 36; i++) {   
        if (!uuid[i]) {   
          r = 0 | Math.random()*16;   
          uuid[i] = chars[(i == 19) ? (r & 0x3) | 0x8 : r];   
        }   
      }   
    }   
    
    return uuid.join('');   
  };   
    
  // A more performant, but slightly bulkier, RFC4122v4 solution.  We boost performance   
  // by minimizing calls to random()   
  Math.uuidFast = function() {   
    var chars = CHARS, uuid = new Array(36), rnd=0, r;   
    for (var i = 0; i < 36; i++) {   
      if (i==8 || i==13 ||  i==18 || i==23) {   
        uuid[i] = '-';   
      } else if (i==14) {   
        uuid[i] = '4';   
      } else {   
        if (rnd <= 0x02) rnd = 0x2000000 + (Math.random()*0x1000000)|0;   
        r = rnd & 0xf;   
        rnd = rnd >> 4;   
        uuid[i] = chars[(i == 19) ? (r & 0x3) | 0x8 : r];   
      }   
    }   
    return uuid.join('');   
  };   
    
  // A more compact, but less performant, RFC4122v4 solution:   
  Math.uuidCompact = function() {   
    return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {   
      var r = Math.random()*16|0, v = c == 'x' ? r : (r&0x3|0x8);   
      return v.toString(16);   
    });   
  };   
})(); 