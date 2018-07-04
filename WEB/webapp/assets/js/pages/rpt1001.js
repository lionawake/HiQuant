
/*********************************************************************************
 *
 * js for rpt1001
 * by WD 201710
 *
 *********************************************************************************/

var render_Chart1 = function( xdataW, leg, ssW){
    option= {
            backgroundColor:'#2C3E50',
            color: ['#F1C40F'],
            title: {
                text: '',
                textStyle: {  
                    color: '#00bbf3'  
                    }
             },
            tooltip: {
                trigger: 'axis'
            },
            grid:{
                left: '5%',
                right:'5%'
            },
            legend: {
                data:leg,
                textStyle:{
                    color: '#00bbf3'
                }
            },
        
            xAxis: {
                type: 'category',
                boundaryGap: false,
                axisTick:{show:false},
                axisLabel:{
                    // textStyle:{
                        color:'#00bbf3'
                    // }
                },
                splitLine:{//网格线
                    show: true,
                    lineStyle:{
                        color:['#2C3E50'],
                        type:'solid'
                    }
                },
                data: xdataW
            },
            yAxis: {
                min:0,
                axisTick:{show:false},
                axisLine:{
                    show:false,
                //    onZero:false
                },
                axisLabel:{
                    // textStyle:{
                        color:'#00bbf3'
                    // }
                },
                splitLine:{//网格线
                    show: true,
                    lineStyle:{
                        color:['#00bbf3'],
                        type:'solid'
                    }
                }
            },
            series: ssW
        };
    var chart1 = echarts.init(document.getElementById('chart1'));
    chart1.setOption(option);
}

var render_Chart2 = function(xdata, leg, ssE){
    option= {
            backgroundColor:'#2C3E50',
            color: ['#E74C3C'],
            title: {
                text: '',
                textStyle: {  
                    color: '#00bbf3'  
                    }
             },
            tooltip: {
                trigger: 'axis'
            },
            grid:{
                left: '5%',
                right:'5%'
            },
            legend: {
                data:leg,
                textStyle:{
                    color: '#00bbf3'
                }
            },
        
            xAxis: {
                type: 'category',
                boundaryGap: false,
                axisTick:{show:false},
                axisLabel:{
                    // textStyle:{
                        color:'#00bbf3'
                    // }
                },
                splitLine:{//网格线
                    show: true,
                    lineStyle:{
                        color:['#2C3E50'],
                        type:'solid'
                    }
                },
                data: xdata
            },
            yAxis: {
                min:0,
                axisTick:{show:false},
                axisLine:{
                    show:false,
                //    onZero:false
                },
                axisLabel:{
                    // textStyle:{
                        color:'#00bbf3'
                    // }
                },
                splitLine:{//网格线
                    show: true,
                    lineStyle:{
                        color:['#00bbf3'],
                        type:'solid'
                    }
                }
            },
            series: ssE
        };
    var chart2 = echarts.init(document.getElementById('chart2'));
    chart2.setOption(option);

}

var render_Chart_autoTest = function(xdata, leg, ssE){
    option= {
            backgroundColor:'#2C3E50',
            color: ['#2ECC71', '#F1C40F','#9B59B6','#3498DB'],
            title: {
                text: '',
                textStyle: {  
                    color: '#00bbf3'  
                    }
             },
            tooltip: {
                trigger: 'axis'
            },
            grid:{
                left: '5%',
                right:'5%'
            },
            legend: {
                data:leg,
                textStyle:{
                    color: '#00bbf3'
                }
            },
        
            xAxis: {
                type: 'category',
                boundaryGap: false,
                axisTick:{show:false},
                axisLabel:{
                    // textStyle:{
                        color:'#00bbf3'
                    // }
                },
                splitLine:{//网格线
                    show: true,
                    lineStyle:{
                        color:['#2C3E50'],
                        type:'solid'
                    }
                },
                data: xdata
            },
            yAxis: {
                min:0,
                axisTick:{show:false},
                axisLine:{
                    show:false,
                //    onZero:false
                },
                axisLabel:{
                    // textStyle:{
                        color:'#00bbf3'
                    // }
                },
                splitLine:{//网格线
                    show: true,
                    lineStyle:{
                        color:['#00bbf3'],
                        type:'solid'
                    }
                }
            },
            series: ssE
        };
    var atChart1 = echarts.init(document.getElementById('atChart1'));
    atChart1.setOption(option);

}
var Loader = function(){

    function loadData4Compile(){
        function renderChart(data){
            var xData=[], ssW=[], ssE=[], leg=[], sw=null, se=null;
            _.each( data, function(d){
                leg.push(d.name);
                //提取日期
                _.each( d.result, function(dd){
                    if( _.indexOf(xData, dd.date) == -1){
                        xData.push(dd.date);
                    }
                });
            });

            xData = xData.sort();
            //
            _.each( leg, function(l){
                sw = {
                            name:l,
                            type:'line',
                            smooth:true,
                            data: [],
                            label: {
                                normal: {
                                    show: false,
                                    position: 'top'//值显示
                                }
                            }
                        }
                se = {
                            name:l,
                            type:'line',
                            smooth:true,
                            symbolSize:12,
                            data: [],
                            label: {
                                normal: {
                                    show: false,
                                    position: 'top'//值显示
                                }
                            }
                        }
                var _data = _.where(data, {"name": l});
                _data = _data[0].result;

                _.each(xData, function(xd){
                    var swb = false, seb = false;
                    _.each( _data, function(dd){
                        if( xd == dd.date){
                            if( dd.warn == undefined || dd.warn == null ){
                                sw.data.push(null);
                            }else{
                                sw.data.push(dd.warn);
                            }
                            if( dd.error == undefined || dd.error == null){
                                se.data.push(null);
                            }else{
                                se.data.push(dd.error);
                            }
                            swb = true; seb = true;
                        }

                    });
                    if( swb == false){
                        sw.data.push(null);
                    }
                    if( seb == false){
                        se.data.push(null);
                    }
                });
                ssW.push(sw);
                ssE.push(se);
            });

            // console.log(JSON.stringify(ssW));
            render_Chart1( xData, leg, ssW);
            render_Chart2( xData, leg, ssE);
        }

        ZX.getDataByAjax(
            'rpt/list/data/compile?proj='+$(".projs").find("option:selected").text(),
            'json',
            function(data){
                $('#chart2').removeClass('hidden');
                renderChart(data);
            },
            function(){
                $('#chart1').html('数据提取失败.');
                $('#chart2').addClass('hidden');
            }
        );
    }
    function loadData4AutoTest(t){

        function renderData(data, target){
            var legends = [], xData=[], dda=[];
            _.each(data, function(d){
                legends.push( d.name );
                //提取日期
                _.each( d.result, function(dd){
                    if( _.indexOf(xData, dd.date) == -1){
                        xData.push(dd.date);
                    }
                });
            });
            xData = xData.sort();
            //
            _.each( legends, function(l){
                ad = {
                            name:l,
                            type:'line',
                            smooth:true,
                            data: [],
                            label: {
                                normal: {
                                    show: false,
                                    position: 'top'//值显示
                                }
                            }
                        };
                var _data = _.where(data, {"name": l});
                _data = _data[0].result;

                _.each(xData, function(xd){
                    var adi = false;
                    _.each( _data, function(dd){
                        if( xd == dd.date){
                            switch(target){
                                case '0':
                                    if( dd.autoTest_total_scripts == undefined || dd.autoTest_total_scripts == null || dd.autoTest_total_scripts == '-'){
                                        ad.data.push(null);
                                    }else{
                                        ad.data.push(dd.autoTest_total_scripts);
                                    }
                                    adi = true;
                                    break;
                                case '1':
                                    if( dd.autoTest_TEST_OK == undefined || dd.autoTest_TEST_OK == null || dd.autoTest_TEST_OK == '-' ){
                                        ad.data.push(null);
                                    }else{
                                        ad.data.push(dd.autoTest_TEST_OK);
                                    }
                                    adi = true;
                                    break;
                                case '2':
                                    if( dd.autoTest_TEST_POK == undefined || dd.autoTest_TEST_POK == null || dd.autoTest_TEST_POK == '-' ){
                                        ad.data.push(null);
                                    }else{
                                        ad.data.push(dd.autoTest_TEST_POK);
                                    }
                                    adi = true;
                                    break;
                                case '3':
                                    if( dd.autoTest_TEST_FAIL == undefined || dd.autoTest_TEST_FAIL == null || dd.autoTest_TEST_FAIL == '-' ){
                                        ad.data.push(null);
                                    }else{
                                        ad.data.push(dd.autoTest_TEST_FAIL);
                                    }
                                    adi = true;
                                    break;
                                case '4':
                                    if( dd.autoTest_TEST_SCRIPT_ERROR == undefined || dd.autoTest_TEST_SCRIPT_ERROR == null || dd.autoTest_TEST_SCRIPT_ERROR == '-' ){
                                        ad.data.push(null);
                                    }else{
                                        ad.data.push(dd.autoTest_TEST_SCRIPT_ERROR);
                                    }
                                    adi = true;
                                    break;
                                case '5':
                                    if( dd.autoTest_TEST_NT == undefined || dd.autoTest_TEST_NT == null || dd.autoTest_TEST_NT == '-' ){
                                        ad.data.push(null);
                                    }else{
                                        ad.data.push(dd.autoTest_TEST_NT);
                                    }
                                    adi = true;
                                    break;
                                default: 
                                    break;
                            }
                        }

                    });
                    if( adi == false){
                        ad.data.push(null);
                    }
                });
                dda.push(ad);
            });
            render_Chart_autoTest( xData, legends, dda);
        }

        var proj = $(".projs").find("option:selected").text(),
            month = $(".filter.year").find("option:selected").val()+"-"+$(".filter.month").find("option:selected").val();
        ZX.getDataByAjax(
            'rpt/list/data/autotest?proj='+proj+'&month='+month,
            'json',
            function(data){
                // renderChart(data);
                // console.log(data);
                if( t == undefined || t == null)
                    t = $("input[name='at_chartType'][checked]").attr('value');
                // console.log(t);
                renderData(data, t);
            },
            function(res){
                $('#atChart1').html('数据提取失败.');
            }
        );
    }

    /**
     * 获取前一天报告列表
     * @return {[type]} [description]
     */
    function loadYD(){
        ZX.getDataByAjax(
            'rpt/list/yd',
            'json',
            function(data){
                // console.log(data);
                // $('.list_yd').html('没有数据.');
                ZX.renderList(
                    data,
                    $('.list_yd'),
                    $('#list_yd'),
                    $('.list_yd'),
                    true,
                    function(){

                    }
                );
            },
            function(){
                $('.list_yd').html('数据提取失败.');
            }
        );
    }
    /**
     * 获取本月项目列表
     * @return {[type]} [description]
     */
    function loadProj(){

        ZX.getDataByAjax(
            'rpt/list/proj',
            'json',
            function(data){
                ZX.renderList(
                    data,
                    $('.projs'),
                    $('#projs'),
                    $('.projs'),
                    true,
                    function(){

                    }
                );
                loadYD();
                loadData4Compile();
                loadData4AutoTest();
            },
            function(res){
                if( res != undefined && res.error == '#999'){
                    alert('操作超时，请重新登录.');
                }else{
                    alert('数据提取失败，请联系管理员.');
                }
            }
        );
    }
    return{
        init: function(){
            loadProj();
        },
        load_yd: function(){
            loadYD();
        },
        load_proj: function(){
            loadProj();
        },
        load_data_compile: function(){
            loadData4Compile();
        },
        load_data_autotest: function(t){
            loadData4AutoTest(t);
        }
    }
}();

var Handler = function(){

    return {
        init: function(){
            // 昨天报告点击
            $('body').delegate('.list_yd li', 'click', function(){
                window.open($(this).attr('rel'));
            });
            // 触发工程选择
            $('.projs').change(function(){ 
                // Loader.load_data_compile();
                // Loader.load_data_autotest();
            });
            //自动化测试radio事件
            $("input[name='at_chartType']").click(function(){
                Loader.load_data_autotest($(this).val());
            }); 
            //2017-11-30 触发查询按钮
            $('.btn_search').click( function(){
                Loader.load_data_compile();
                Loader.load_data_autotest();
            });
        }
    }
}();


var PageInit = function(){

    //2017-11-30
    function getYears(){

        var d = new Date();
        var year = d.getFullYear(), mon = d.getMonth() + 1;
        var years = [];
        for( var i = 0; i < 2; i++ ){
            years.push(year-i);
        }
        return years;
    }
    //2017-11-30
    function setFilterMonth(){
        var years = getYears();
        for( var i = 0; i < years.length; i++){
            $('.filter.year').append('<option value="'+years[i]+'">'+years[i]+'</option>');
        }
        for( var i = 1; i < 13; i++){
            $('.filter.month').append('<option value="'+i+'">'+i+'月</option>');
        }
        var d = new Date();
        var mon = d.getMonth() + 1;
        $('.filter.month').find("option[value='"+mon+"']").attr("selected",true);
    }
    function init_view(){
        $('.c_tits').html('<b>'+new Date().Format("yyyy-MM")+'</b> 持续构建统计');
        //2017-11-30
        setFilterMonth();
    }

    return {
        init: function(){
            APPUtils.init_page();
            init_view();
            Loader.init();
            Handler.init();
        }
    }
}();