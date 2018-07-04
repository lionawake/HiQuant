
/*********************************************************************************
 *
 * js for account
 * by Andrew 201603
 *
 *********************************************************************************/
var accounts = [];

/*************************************************************
 *
 * 事件的弹窗管理
 *
 ************************************************************/
var event_dialog = function(){
    return {
        toolbar_alert: function(str){
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
        ed_delete_account: function( fn, us){
            var d = dialog({
                title: '消息',
                content: '您确定要删除账号吗?',
                button: [{
                        value: '删除账号',
                        callback: function () {
                            var that = this;
                            if( fn != undefined){
                                that.title('提交中..');
                                fn(us);
                            }
                            return true;
                        },
                        autofocus: true
                    },
                    {
                        value: '取消'
                    }
                ]
            });

            d.showModal();
        },
        ed_reset_pwd: function( fn, us){
            var d = dialog({
                title: '消息',
                content: '您确定要重置账户的密码吗?',
                button: [{
                        value: '重置账号密码',
                        callback: function () {
                            var that = this;
                            if( fn != undefined){
                                that.title('提交中..');
                                fn(us);
                            }
                            return true;
                        },
                        autofocus: true
                    },
                    {
                        value: '取消'
                    }
                ]
            });

            d.showModal();
        }
    }
}();

/*************************************************************
 *
 * account列表区域的功能控制
 *
 ************************************************************/
//列表区域的主工具栏
var init_handler_Account = function(){

    //新建
    function handler_create(){
        
        function validate_create(){
            $('.err').show().hide();
            if( $.trim( $('.personName').val() ) == '' ||
                $.trim( $('.userName').val() ) == ''){
                $('.cperr03').hide().show();
                return false;
            }
            var reg_mail = /^\w+((-\w+)|(\.\w+))*\@[A-Za-z0-9]+((\.|-)[A-Za-z0-9]+)*\.[A-Za-z0-9]+$/; //验证邮箱的正则表达式
            if( $('.email').val() != '' && !reg_mail.test( $('.email').val() )){
                $('.cperr01').hide().show();
                $('.email').focus();
                return false;
            }
            return true;
        }

        $('#bar_cAccount').click(function(e) {

            $('.system_account_new input[type="text"]').val('');
            $('.system_account_new input[type="email"]').val('');
            $('.err').show().hide();
            $.blockUI({
                message: $('.system_account_new'),
                css: {
                    background: '#fff',
                    border: '0px',
                    cursor: 'default',
                    top: '10%',
                    left: '20%',
                    width: 'auto',
                    padding: '0px 0px 40px'
                },
                overlayCSS: {
                    cursor: 'default'
                }
            });
            $('.system_btn_submit_NewAccount').unbind('click');
            $('.system_btn_submit_NewAccount').click(function() {
                if( validate_create()){
                    //form, url, success_callback, failed_callback
                    ZX.formSubmitByAjax(
                        $('.form_sys_account_new'),
                        'sup/account/reg',
                        function(){
                            $.unblockUI();
                            event_dialog.toolbar_alert('创建账户成功.');
                            //重新加载数据
                            handler_loadAccount.loadData( );
                        },
                        function(res){
                            console.log(res);
                            if( res != undefined && res.error != undefined){
                                $('.cperr00').text(res.error);
                            }else{
                                $('.cperr00').text('创建账户失败，请稍后重试.');
                            }
                            $('.cperr00').hide().show();
                            return false;
                        }
                    );
                }
            });
            $('.system_btn_cancel_NewAccount').click(function() {
                $.unblockUI();
                return false;
            });
        });

    }

    //编辑
    function handler_modify(){
        //前台清理
        $('#bar_mAccount').click(function(e) {

        });

    }
    //删除
    function handler_delete(){
        $('#bar_dAccount').click(function(e) {

            var us = [];
            $('.tbl_td .account_selector').each(function(){
                if( $(this).is(':checked')){
                    us.push( $(this).attr('rel') );
                }
            }); 
            if( us.length == 0){
                event_dialog.toolbar_alert('请选择需要删除的账户.');
                return false;
            }
            function deleteAccount( us ){            
                ZX.getDataByAjax(
                    'sup/account/delete?username='+us,
                    'json',
                    function(data){
                        event_dialog.toolbar_alert('账户删除成功.');
                        handler_loadAccount.loadData( );
                    },
                    function(){
                        event_dialog.toolbar_alert('删除失败，请稍后重试.');
                    }
                );
            }
            //需要提示
            event_dialog.ed_delete_account(deleteAccount, us);
        });

    }
    //重置面膜
    function handler_resetpwd(){
        $('#bar_rAccount').click(function(e) {
            var us = [];
            $('.tbl_td .account_selector').each(function(){
                if( $(this).is(':checked')){
                    us.push( $(this).attr('rel') );
                }
            });  
            if( us.length == 0){
                event_dialog.toolbar_alert('请选择需要重置密码的账户.');
                return false;
            }

            function resetpwd( us ){
                // var userName = $('.tbl_td input[type="checkbox"]').attr('checked').attr('rel');            
                ZX.getDataByAjax(
                    'sup/account/reset?username='+us,
                    'json',
                    function(data){
                        event_dialog.toolbar_alert('重置密码成功，密码重置为:12345678');
                    },
                    function(){
                        alert('删除失败，请稍后重试.');
                    }
                );
            }
            //需要提示
            event_dialog.ed_reset_pwd(resetpwd, us);
        });

    }

    return {
        init_default: function(){
            handler_create();
            // handler_modify();
            handler_resetpwd();
            handler_delete();

        }
    }
}();

/*************************************************************
 *
 * account页面加载数据并render
 *
 ************************************************************/
var handler_loadAccount = function(){

    return {
        renderAccounts: function( data, $temp ){

            //render
            ZX.renderList(
                    data,
                    $('.bodymain .accountList'),
                    $temp,
                    $('.bodymain .accountList'),
                    true,
                    function(){

                    }
                );
        },
        loadData: function(){
            // getDataByAjax: function( url, dataType, success_callback, failed_callback)
            ZX.getDataByAjax(
                    'sup/account/list',
                    'json',
                    function(data){
                        accounts = data;
                        handler_loadAccount.renderAccounts( accounts, $('#accountList_list'));
                    },
                    function(){

                    }
                );
        }
    }
}();

var Init_Handler = function(){

    function menus_evt(){
        $('.tabs li').click( function(e){
            $('.tabs li').removeClass('active');
            $(this).addClass('active');

            $('.tab').addClass('hidden');
            $('.tab.'+$(this).attr('rel')).removeClass('hidden');
        });
    }
    menus_evt();
    init_handler_Account.init_default();
}
/*************************************************************
 *
 * 页面展现控制
 *
 ************************************************************/
var init_page_sys = function(){

    return {
        init: function(){
            Init_Handler();
            handler_loadAccount.loadData( );
        }
    }
}();