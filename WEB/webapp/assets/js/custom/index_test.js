
$(document).ready(function(){
    var table_run = null, table_fin;

    function formatTable(table, id){
        table = $('#'+id).DataTable( );
        // if( table != null){
            $('.addselect').remove();
            table.destroy(false);
        // }
        var option = {
            "dom": '<"top"f >rt<"bottom"ilp><"clear">',//dom定位
            "dom": 'tiprl',//自定义显示项
            // "scrollY": "220px",//dt高度
            "lengthMenu": [
               [10, 20, 50, -1],
               [10, 20, 50, "全部"]
            ],//每页显示条数设置
            "lengthChange": false,//是否允许用户自定义显示数量
            "bPaginate": true, //翻页功能
            "bFilter": false, //列筛序功能
            "searching": true,//本地搜索
            "ordering": true, //排序功能
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
               "sInfoFiltered": "（数据库中共为 _MAX_ 条记录）",
               // "sProcessing": "<img src='../resources/user_share/row_details/select2-spinner.gif'/> 正在加载数据...",
               "sSearch": "模糊查询：",
               "sUrl": "",
               //多语言配置文件，可将oLanguage的设置放在一个txt文件中，例：Javascript/datatable/dtCH.txt
               "oPaginate": {
                   "sFirst": "首页",
                   "sPrevious": " 上一页 ",
                   "sNext": " 下一页 ",
                   "sLast": " 尾页 "
               }
            },

            "columnDefs": [{
                   orderable: false,
                   targets: 0 }
            ],//第一列禁止排序

            "order": [
               [0, null]
            ],//第一列排序图标改为默认
            initComplete: function () {//列筛选
                var api = this.api();
                api.columns().indexes().flatten().each(function (i) {
                    if (i != 0) {//删除第一列与第二列的筛选框
                        var column = api.column(i);
                        var $span = $('<span class="addselect"><span class="filter_icon">▾</span></span>').appendTo($(column.header()))
                        var select = $('<select ref="'+$(column.header()).attr('ref')+'" tag=""><option value="">全部</option></select>')
                               .appendTo($(column.header()))
                               .on('click', function (evt) {
                                    evt.stopPropagation();
                                    var val = $.fn.dataTable.util.escapeRegex(
                                        $(this).val()
                                    );
                                    //为了获取当前的选择值补充
                                    if( val == undefined || val.length == 0){
                                        val="";
                                    }
                                    $(this).attr('tag', val);
                                    //END 
                                    
                                    column.search(val ? '^' + val + '$' : '', true, false).draw();
                               });
                        column.data().unique().sort().each(function (d, j) {
                           function delHtmlTag(str) {
                               return str.replace(/<[^>]+>/g, "");//去掉html标签
                           }

                           d = delHtmlTag(d)
                           select.append('<option value="' + d + '">' + d + '</option>')
                           $span.append(select)
                        });

                    }
                });

            }

        };
        table = $('#'+id).DataTable( option);
        //隐藏简历编号列
        $('body').find('.toggle-vis').each( function(){
            if( $(this).is(':checked')){
                var hcolumn = table.column($(this).attr('data-column'));
                hcolumn.visible(false);
            }
        });

        //自定义搜索
        $('.dsearch').on('keyup click', function () {
           var tsval = $(".dsearch").val()
           table.search(tsval, false, false).draw();
        });

        //checkbox全选
        $("#checkAll").on("click", function () {
           if ($(this).prop("checked") === true) {
               $("input[name='checkList']").prop("checked", $(this).prop("checked"));
               $('#tbl_simple tbody tr').addClass('selected');
           } else {
               $("input[name='checkList']").prop("checked", false);
               $('#tbl_simple tbody tr').removeClass('selected');
           }
        });

        //显示隐藏列
        $('.toggle-vis').on('change', function (e) {
           e.preventDefault();
           // console.log($(this).attr('data-column'));
           var column = table.column($(this).attr('data-column'));
           column.visible(!column.visible());
        });

        //删除选中行
        $('#'+id+' tbody').on('click', 'tr input[name="checkList"]', function () {
           var $tr = $(this).parents('tr');
           $tr.toggleClass('selected');
           var $tmp = $('[name=checkList]:checkbox');
           $('#checkAll').prop('checked', $tmp.length == $tmp.filter(':checked').length);

        });

        $('.btn_wo_delete').click(function () {
            var ids = [];
            $('#'+id+' .selected').each( function(){
                ids.push($(this).attr('data-role'));
            });
            if( ids.length == 0){
                event_dialog.alert('请选择需要删除的工单.');
                return false;
            }
            function deleteWO(ids){
                Event.deleteWorkOrder(ids, function(){
                    event_dialog.alert('工单删除成功.');
                    table.rows('.selected').remove().draw(false);
                });
            }
            event_dialog.confirm( deleteWO, ids, '您确定要删除工单吗?', '删除工单');
            
        });

        $('.showcol').click(function () {
           $('.showul').toggle();

        })

    }

    var Loader = function(){

        function load_test_run(){

            function renderTbl(data){
                if( table_run) table_run.destroy();
                ZX.renderList(
                        data,
                        $('.tbl_test_run tbody'),
                        $('#list_test_run'),
                        $('.tbl_test_run tbody'),
                        true,
                        function(){
                            formatTable(table_run, "tbl_test_run");
                            View.closeMask();
                        }
                    );
            }
            ZX.getDataByAjax(
                '../sup/unit/json?code=testRun',
                'json',
                function(data){
                    //render
                    renderTbl(data);
                },
                function(){
                    View.closeMask();
                    formatTable();
                    event_dialog.alert('策略数据加载失败.');
                }
            );
        }
        function load_test_fin(){

            function renderTbl(data){
                if( table_fin) table_fin.destroy();
                ZX.renderList(
                        data,
                        $('.tbl_test_fin tbody'),
                        $('#list_test_fin'),
                        $('.tbl_test_fin tbody'),
                        true,
                        function(){
                            formatTable(table_fin, "tbl_test_fin");
                            View.closeMask();
                        }
                    );
            }
            ZX.getDataByAjax(
                '../sup/unit/json?code=testFin',
                'json',
                function(data){
                  console.log(data);
                    //render
                    renderTbl(data);
                },
                function(){
                    View.closeMask();
                    formatTable();
                    event_dialog.alert('策略数据加载失败.');
                }
            );
        }

        return {
            init: function(){
            },
            load_test_run: function(){
                load_test_run();
            },
            load_test_fin: function(){
                load_test_fin();
            }
        }
    }();


    var Event = function(){

        function click_tab(){
            $('.tabs li').click( function(){
                $('.tabs li').removeClass('active');
                $(this).addClass('active');
                $('.tab_items .tab_item').addClass('hidden');
                $('.tab_items .'+$(this).attr('rel')).removeClass('hidden');
                if( $(this).attr('rel')=='unit_run'){
                    Loader.load_test_run();
                }
                if( $(this).attr('rel')=='unit_fin'){
                    Loader.load_test_fin();
                }
            });
        }

        function click_report(){
            $('.tbl_test_fin').delegate( '.bar_item', 'click', function(){
                window.open('test_report.html');
            });
        }
        return {
            init: function(){
                click_tab();
                click_report();
            }
        }
    }();

    var View = function(){

        function setView(){
            $('.main-content, .sidebar').css('height', ($(window).height()-90)+'px');
            $('.main-content').css('width', ($(window).width()-265)+'px');
            $('.mask').height($(window).height()-180);
            $("#iframe_main").iframe_autoresize({
                // "height":0,  
                "width": 1,
                "woffset": 260,
                "hoffset": $('.head-bar').height()
            });
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