var table = null;
var id;
var LQ_WS = function(){
    function getUrlRoot(){
        var u = window.location.href, p = window.location.protocol;
        if(p.indexOf('https') != -1){
            u = u.substring( 8, u.lastIndexOf('/'));
        }else{
            u = u.substring( 7, u.lastIndexOf('/'));
        }
        return u;
    }
    var wsUri ="ws://"+getUrlRoot()+"/../ws/lq"; 
    var $output = $('.output ul');  
    var webSocket;
 
    function onMessage(event) {
        var result = $(event.data).text().trim();
        if(result=="end"){
            table.draw(false);
            FrameUtils.unloading();
            return;
        }
        var s = '<li style="color:#0C6;">' + event.data+'</li>';
        $output.append(s);
        //保持div随内容变化，自动滚动到底
        $('.output').slimScroll({ scrollTo: $('.output ul').height() });
    }
    function onOpen(event) {
        
    }
    function onClose(evt) { 

    } 
    function onError(event) {
        $output.append('<li style="color:#f00;"><i class="icon-chevron-right"></i>系统异常!</li>');
    }
    return {
        start: function(data) {
            FrameUtils.loading("任务执行中...");
            webSocket = new WebSocket( wsUri);
            webSocket.onopen = function(event) {
                webSocket.send(JSON.stringify(data));
                $(".output_div").addClass("active");
                 //id = setInterval(function(){ 
                     //var l = $('.output ul').find('li').length;
                     //if( l > 300){//清理数据，防止数据量过大，客户端使用受影响
                      //console.log("清理")
                         //$('.output ul li').slice(0, l-300).remove();
                    // }
                // },2000); 
            };

            webSocket.onerror = function(event) {
                onError(event);
            };
         
            webSocket.onmessage = function(event) {
                onMessage(event);
            };

            webSocket.onclose = function(event) { 
                onClose(event);
                clearInterval(id);
            }; 
        },
        close: function(){
            if( webSocket != undefined){
                webSocket.close();
            }
        }
    }
}();
$(document).ready(function(){
    var pEditor;

    var $start = "<span class='btn btn-success btn-xs cz start'>开始</span>",
        $edit = "<span class='btn btn-default btn-xs cz edit'>编辑</span>",
        $del = "<span class='btn btn-danger btn-xs cz delete'>删除</span>",
        $report = "<span class='btn btn-default btn-xs cz report'>报告</span>";
                            

    function formatTable(){
        table = $('#tbl_simple').DataTable( );
        // if( table != null){
            // $('.addselect').remove();
            table.destroy(false);
        // }
        // table = $('#tbl_simple').DataTable({
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
            "ordering": false,
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
               "sSearch": "模板名查询：",
               "sUrl": "",
               //多语言配置文件，可将oLanguage的设置放在一个txt文件中，例：Javascript/datatable/dtCH.txt
               "oPaginate": {
                   "sFirst": "首页",
                   "sPrevious": " 上一页 ",
                   "sNext": " 下一页 ",
                   "sLast": " 尾页 "
               }
            },

            // "columnDefs": [{
            //        orderable: false,
            //        targets: 0 
            //      }
            // ],//第一列禁止排序

            // "order": [
            //    [0, null]
            // ],//第一列排序图标改为默认
            serverSide:true,
            ajax:function(data,callback,settings){
                var param = {};
                var json = {};
                json["spName"] = data.search.value;
                param.json = JSON.stringify(json);
                param.pageSize = data.length;
                param.pageStart = data.start;
                var sortStr = "";
                _.each($(".sort_item"),function(d){
                    var value = $(d).find("select").val();
                    if(value!=-1){
                      sortStr+= ","+value+" "+$(d).find(".sort.active").attr("type");
                    }
                })
                if(sortStr!="") sortStr=sortStr.substring(1);
                param.sortStr = sortStr;
                $.ajax({
                    type: "GET",
                    url:"../lq/spt/find",
                    cache: false, //禁用缓存
                    data: param, //传入组装的参数
                    dataType: "json",
                    success:function(res){
                        if(res.success==true){
                            _.each(res.data.data,function(d){
                                d.first = '<input type="checkbox" name="checkList"></td>';
                                d.createTime = new Date(d.createTime).Format("yyyy-MM-dd hh:mm:ss");
                                d.code = "<textarea>"+d.code+"</textarea>";
                                var testStatus = "";
                                var cz = "";
                                switch(d.testStatus){
                                    case 0:
                                        testStatus = "<span style='color:#3498DB'>未开始</span>";
                                        cz += $start+$edit+$del;
                                        break;
                                    case 1:
                                        testStatus = "<span style='color:#E67E22'>进行中</span>";
                                        cz += $edit+$del+$report;
                                        break;
                                    case 2:
                                        testStatus = "<span style='color:#2ECC71'>已完成</span>";
                                        cz += $edit+$del+$report;
                                        break;
                                    default:
                                        testStatus = "系统错误";
                                        break;
                                }
                                d.testStatus = testStatus;
                                d.cz = cz;
                            })
                            var returnData = {};
                            returnData.draw = data.draw;
                            returnData.recordsTotal = data.length;
                            if(res.data.num!=undefined){
                                returnData.recordsFiltered = res.data.num;
                            }else{
                              returnData.recordsFiltered = 0;
                            }
                            returnData.data = res.data.data;
                            callback(returnData);
                        }else{
                            var returnData = {};
                            returnData.recordsFiltered = 0;
                            returnData.data = [];
                            callback(returnData);
                        }
                    },
                })
            },
            createdRow: function( row, data, dataIndex ) {
                $(row).attr("spId",data.spId);
                $(row).attr("testStatus",data.testStatus);
            },
            columns: [{
                  "data": "first",
                  "sClass":"first",
              },{
                  "data": "spId",
                  "sClass":"spId",
              },{
                  "data": "spName",
                  "sClass":"spName"
              },{
                  "data":"createTime",
                  "sClass":"createTime"
              },{
                  "data":"author",
                  "sClass":"author"
              },{
                  "data":"testStatus",
                  "sClass":"testStatus"
              },{
                  "data":"cz",
                  "sClass":"czTd"
              },{
                  "data":"code",
                  "sClass":"code hidden"
              }],
            // initComplete: function () {//列筛选
            //     var api = this.api();
            //     api.columns().indexes().flatten().each(function (i) {
            //         if (i != 0) {//删除第一列与第二列的筛选框
            //             var column = api.column(i);
            //             var $span = $('<span class="addselect"><span class="filter_icon">▾</span></span>').appendTo($(column.header()))
            //             var select = $('<select ref="'+$(column.header()).attr('ref')+'" tag=""><option value="">全部</option></select>')
            //                    .appendTo($(column.header()))
            //                    .on('click', function (evt) {
            //                         evt.stopPropagation();
            //                         var val = $.fn.dataTable.util.escapeRegex(
            //                             $(this).val()
            //                         );
            //                         //为了获取当前的选择值补充
            //                         if( val == undefined || val.length == 0){
            //                             val="";
            //                         }
            //                         $(this).attr('tag', val);
            //                         //END 
                                    
            //                         column.search(val ? '^' + val + '$' : '', true, false).draw();
            //                    });
            //             column.data().unique().sort().each(function (d, j) {
            //                function delHtmlTag(str) {
            //                    return str.replace(/<[^>]+>/g, "");//去掉html标签
            //                }

            //                d = delHtmlTag(d)
            //                select.append('<option value="' + d + '">' + d + '</option>')
            //                $span.append(select)
            //             });

            //         }
            //     });
            // }
        };
        table = $('#tbl_simple').DataTable( option);
        table.on( 'draw', function () {
            // $('.jqmeter-container.zero').jQMeter({
            //     goal:'100',
            //     raised:'0',
            //     width:'80px',
            //     height:'20px',
            //     barColor:"#2dd47b;",
            // });
            // $('.jqmeter-container.complete').jQMeter({
            //     goal:'100',
            //     raised:'100',
            //     width:'80px',
            //     height:'20px',
            //     barColor:"#2dd47b;",
            //     animationSpeed:0,
            //     counterSpeed:400,
            // });
        });
        //列显示/隐藏
        $('body').find('.toggle-vis').each( function(){
            if( $(this).is(':checked')){
                var hcolumn = table.column($(this).attr('data-column'));
                hcolumn.visible(false);
            }
        });
        // 自定义搜索
        $('.dsearch').on('keyup click', function () {
           var tsval = $(".dsearch").val();
           table.search(tsval, false, false).draw();
        });
        //自定义分页
        $(".table_count").change(function(){
            var len = $(this).val();
            table.page.len(len).draw(false);
        });



        // });

        //添加索引列
        // table.on('order.dt search.dt',
        //        function () {
        //            table.column(0, {
        //                search: 'applied',
        //                order: 'applied'
        //            }).nodes().each(function (cell, i) {
        //                cell.innerHTML = i + 1;
        //            });
        //        }).draw();

        

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
        $('#tbl_simple tbody').on('click', 'tr input[name="checkList"]', function () {
           var $tr = $(this).parents('tr');
           $tr.toggleClass('selected');
           var $tmp = $('[name=checkList]:checkbox');
           $('#checkAll').prop('checked', $tmp.length == $tmp.filter(':checked').length);

        });

        $('.showcol').click(function () {
           $('.showul').toggle();
        })
    }

    var Loader = function(){

        function load_policys(){
            formatTable()
            // function renderTbl(data){
            //     if( table) table.destroy();
            //     ZX.renderList(
            //             data,
            //             $('.tbl_policys tbody'),
            //             $('#list_policys'),
            //             $('.tbl_policys tbody'),
            //             true,
            //             function(){
            //                 formatTable();
            //                 View.closeMask();
            //             }
            //         );
            // }
            // ZX.getDataByAjax(
            //     '../lq/pt/find?pageStart=0&pageSize=2',
            //     'json',
            //     function(data){
            //         //render
            //         renderTbl(data);
            //     },
            //     function(){
            //         View.closeMask();
            //         formatTable();
            //         event_dialog.alert('策略数据加载失败.');
            //     }
            // );
        }

        return {
            init: function(){
              load_policys();
            }
        }
    }();


    var Event = function(){
        function findStatus(){
            ZX.getDataByAjax(
                "../lq/spt/findStatus",
                "json",
                function(res){
                    if(res==null){
                        event_dialog.alert('查找任务状态出错!');
                        $(".data", window.parent.document).text(0);
                    }else{
                        $(".waiting", window.parent.document).text(res.status0==null?0:res.status0);
                        $(".running", window.parent.document).text(res.status1==null?0:res.status1);
                        $(".fin", window.parent.document).text(res.status2==null?0:res.status2);
                    }
                },
                function(){
                    event_dialog.alert('查找任务状态出错!');
                    $(".data", window.parent.document).text(0);
                }
            );
        }
        //编译检查
        // function ptCheck(){
        //     $(".ptCheck").click(function(){
        //         //TODO 调用编译检查脚本
        //         var data = {};
        //         data["code"] = $("#pContent").text();
        //         FrameUtils.loading("编译检查中...");
        //         ZX.postDataByAjax(
        //             "../tool/codeCheck",
        //             JSON.stringify(data),
        //             function(res){
        //                 FrameUtils.unloading();
        //                 if(res==null){
        //                     $(".ptCheckResult").removeClass("right").removeClass("wrong").addClass("wrong");
        //                     event_dialog.alert("编译检查失败!");
        //                 }else{
        //                     $(".ptCheckResult").removeClass("right").removeClass("wrong").addClass("right");
        //                     event_dialog.alert("编译检查通过!");
        //                 }
        //             },
        //             function(){
        //                 FrameUtils.unloading();
        //                 $(".ptCheckResult").removeClass("right").removeClass("wrong").addClass("wrong");
        //                 event_dialog.alert("编译检查失败!");
        //             }
        //         )
        //     });
        // }
        //模板保存
        function ptSave(){
          $(".ptSave").click(function(){
              var data = {};
              data["spName"] = $("input[name=policyName]").val();
              data["author"] = $(".lable_account").text();
              data["code"] = pEditor.getValue();
              function save(){
                  FrameUtils.loading("模板保存中...");
                  ZX.postDataByAjax(
                      "../lq/spt/save",
                      JSON.stringify(data),
                      function(res){
                          FrameUtils.unloading();
                          if(res==null){
                              event_dialog.alert("模板保存失败!");
                          }else{
                              event_dialog.alert("模板保存成功!");
                              table.ajax.reload();
                          }
                          findStatus();
                      },
                      function(){
                          FrameUtils.unloading();
                          event_dialog.alert("模板保存失败!");
                          findStatus();
                      }
                  )
              }
              function update(spId){
                  data["spId"] = spId;
                  FrameUtils.loading("模板修改中...");
                  ZX.postDataByAjax(
                      "../lq/spt/update",
                      JSON.stringify(data),
                      function(res){
                          FrameUtils.unloading();
                          if(res==null){
                              event_dialog.alert("模板修改失败!");
                          }else{
                              event_dialog.alert("模板修改成功!");
                              table.ajax.reload(function(){
                                  $("#tbl_simple tr[spId="+spId+"]").find(".edit").trigger("click");
                              });
                          }
                      },
                      function(){
                          FrameUtils.unloading();
                          event_dialog.alert("模板修改失败!");
                      }
                  )
              }
              if(data.spName==null||data.spName.trim()==""){
                  event_dialog.alert("模板名称不能为空!");
              }else{
                  // if($(".ptCheckResult").hasClass("right")){
                      var spId = $(this).attr("spId");
                      if(spId==null||spId==undefined){
                          event_dialog.confirm( save, null, '您确定要提交模板吗?', '提交模板');
                      }else{
                          event_dialog.confirm( update, spId, '您确定要修改'+spId+'号模板吗?', '提交模板');
                      }
                  // }else{
                  //     event_dialog.alert("请先编译检查通过");
                  // }
              }
          });
        }
        //删除模板
        function ptDelete(){
            $('.btn_wo_delete').click(function () {
                var ids = [];
                $('#tbl_simple .selected').each( function(){
                    ids.push($(this).attr("spId"));
                });
                if( ids.length == 0){
                    event_dialog.alert('请选择需要删除的模板.');
                    return false;
                }
                function deleteWO(ids){
                    FrameUtils.loading("模板删除中...");
                    ZX.getDataByAjax(
                        "../lq/spt/deletes?ids="+ids,
                        'json',
                        function(res){
                            FrameUtils.unloading();
                            if(res==null){
                                event_dialog.alert('模板删除失败!');
                            }else{
                                event_dialog.alert('模板删除成功!');
                                table.ajax.reload();
                            }
                            findStatus();
                        },
                        function(){
                            FrameUtils.unloading();
                            event_dialog.alert('模板删除失败!');
                            findStatus();
                        }
                    )
                    // Event.deleteWorkOrder(ids, function(){
                    //     event_dialog.alert('模板删除成功.');
                    //     table.rows('.selected').remove().draw(false);
                    // });
                }
                event_dialog.confirm( deleteWO, ids, '您确定要删除模板吗?', '删除模板');
            });
        }
        //操作栏按钮
        function ptCz(){
            //创建
            $(".create").click(function(){
                $(".ptSave").attr("spId",null);
                $("input[name=policyName]").val('');
                pEditor.setValue("填写模板代码\n在这里输入您的代码");
                $(".edit").removeClass("active");
            });
            //开始
            $("body").delegate(".start","click",function(){
                var $this = $(this);
                var spId = $this.parent().parent().attr("spId");
                var data = {};
                data["spId"] = spId;
                //data["code"] = $this.parent().next().text();
                data["spName"] = $this.parent().parent().find(".spName").text().trim();
                data["author"] = $this.parent().parent().find(".author").text().trim();
                event_dialog.confirm( start, data, '您确定进行任务回测吗?', '开始');
                function start(data){
                    $this.parent().parent().find(".testStatus").html("<span style='color:#E67E22'>进行中</span>");
                    var waitNum = parseFloat($(".waiting", window.parent.document).text().trim());
                    $(".waiting", window.parent.document).text(--waitNum);
                    var runNum = parseFloat($(".running", window.parent.document).text().trim());
                    $(".running", window.parent.document).text(++runNum);
                    LQ_WS.start(data);
                }
            })
            //停止
            $("body").delegate(".stop","click",function(){
                var $this = $(this);
                var spId = $(this).parent().parent().attr("spId");
                event_dialog.confirm( stop, null, '您确定停止任务吗?', '停止');
                function stop(){
                    var data = {};
                    data["spId"] = spId;
                    data["testStatus"]=0;
                    ZX.postDataByAjax(
                        "../lq/spt/update",
                        JSON.stringify(data),
                        function(res){
                            if(res==null){
                                event_dialog.alert("任务停止失败!");
                            }else{
                                table.draw(false);
                                //TODO 任务停止脚本
                            }
                        },
                        function(){
                            event_dialog.alert("任务停止失败!");
                        }
                    );
                }
            })
            //编辑
            $("body").delegate(".edit","click",function(){
                var spId = $(this).parent().parent().attr("spId");
                if($(this).hasClass("active")){
                    $(".ptSave").attr("spId",null);
                    $("input[name=policyName]").val('');
                    pEditor.setValue("填写模板代码\n在这里输入您的代码");
                    // $(".ptStatus").removeClass("ed");
                    $(this).removeClass("active");
                }else{
                    $(".ptSave").attr("spId",spId);
                    $(".edit").removeClass("active");
                    $("input[name=policyName]").val($(this).parent().parent().find(".spName").text());
                    pEditor.setValue($(this).parent().parent().find(".code textarea").text());
                    // $(".ptStatus").addClass("ed");
                    $(this).addClass("active");
                }
            })
            //删除
            $("body").delegate(".delete","click",function(){
                var spId = $(this).parent().parent().attr("spId");
                function deleteWO(ids){
                    FrameUtils.loading("模板删除中...");
                    ZX.getDataByAjax(
                        "../lq/spt/deletes?ids="+spId,
                        'json',
                        function(res){
                            FrameUtils.unloading();
                            if(res==null){
                                event_dialog.alert('模板删除失败!');
                            }else{
                                var nowSpId = $(".ptSave").attr("spId");
                                _.each(spId,function(id){
                                    if(id==nowSpId){
                                        $(".ptSave").attr("spId",null);
                                    }
                                })
                                event_dialog.alert('模板删除成功!');
                                table.ajax.reload();
                            }
                            findStatus();
                        },
                        function(){
                            FrameUtils.unloading();
                            event_dialog.alert('模板删除失败!');
                            findStatus();
                        }
                    )
                }
                event_dialog.confirm( deleteWO, spId, '您确定要删除'+spId+'号模板吗?', '删除模板');
            });
            //报告
            $("body").delegate(".report","click",function(){
                var spId = $(this).parent().parent().attr("spId");
                window.open ("lq_strategy.html?spId="+spId);
            })
        }
        //排序
        function ptSort(){
            $(".sort").click(function(){
              $(this).parent().find(".sort").removeClass("active");
              $(this).addClass("active")
              table.draw(false);
            });
            $(".sort_item select").change(function(){
                table.draw(false);
            })
        }
        //进程面板关闭
        function clsOutput(){
            $(".cls").click(function(e){
                if(e.stopPropagation()){
                    e.stopPropagation();
                }else{
                    e.cancelBubble = true;
                }
                $(".output_div").removeClass("active");
            });
        }
        //进程面板打开
        function openOutput(){
          $(".output_b").click(function(){
              if($(".output_div").hasClass("active")) return;
              $(".output_div").addClass("active");
          });
        }
        return {
            init: function(){
                // ptCheck();
                ptSave();
                ptDelete();
                ptCz();
                ptSort();
                clsOutput();
                openOutput();
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
            pEditor = CodeMirror.fromTextArea(document.getElementById("pContent"),{
                mode:"text/x-python",
                lineNumbers:true,
                theme:"blackboard"
            });
            // pEditor.on("change",function(instance, changeObj){
            //     $(".ptCheckResult").removeClass("right").removeClass("wrong");
            // })
        }
        function initOutput(){
            $('.output').slimScroll({
                scrollTo: $('.output').height(),
                height: 300,
                color: '#ffcc00',
                allowPageScroll:false,
                wheelStep:1
            });
        }

        return {
            init: function(){
                // console.log( zxCookie.getCookieValue(zxCookie.ACCT));
                setView();
                initOutput();
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