#-*- coding=utf-8 -*-
import re
s = '''<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<link type="text/css" rel="stylesheet" href="../../css/head.css?v=20160105094129" />
<link type="text/css" rel="stylesheet" href="../../css/cdep_common.css?v=20160105094129" />
<link rel="stylesheet" href="../../css/stu_jxjh_style.css" type="text/css"></link>

<script type="text/javascript" src="http://static.njcedu.com/JSLib/CDOJS/Utility.js?v=20160105094129"></script>
<script type="text/javascript" src="http://static.njcedu.com/JSLib/CDOJS/HashMap.js?v=20160105094129"></script>
<script type="text/javascript" src="http://static.njcedu.com/JSLib/CDOJS/CDO.js?v=20160105094129"></script>
<script type="text/javascript" src="http://static.njcedu.com/JSLib/CDOJS/JSON.js?v=20160105094129"></script>
<script type="text/javascript" src="http://static.njcedu.com/JSLib/CDOJS/HttpClient.js?v=20160105094129"></script>
<script type="text/javascript" src="http://static.njcedu.com/js/jquery-1.7.2.min.js?v=20160105094129" ></script>
<script type="text/javascript" src="result.js?v=20160105094129" ></script>
<title>查看试卷 - 新锦成就业教育平台</title>
</head>
<body >





<!-- 分数处理 -->

<!-- 分数处理 end -->
<center>
<div class="stu_ks">
	<h1 class="stu_ks_tit">
		2013级学生三年级第一学期就业创业课程考试
			</h1>
    <table class="ksgl_table" cellpadding="0" cellspacing="0" style="margin:30px auto;">
      	<tr>
          	<td style="background-color:#e4e4e4;">考生</td>
            <td>周世宇 &nbsp;-&nbsp; 131903134</td>
            <td style="background-color:#e4e4e4;">总分/及格分</td>
            <td>
   				100 / 60
            </td>
            <td style="background-color:#e4e4e4;">时长/用时</td>
            <td>90/66分钟</td>
		</tr>
        <tr>
          	<td style="background-color:#e4e4e4;">提交情况</td>
            <td>
            	            		            		            			手动提交
            		            		            	            </td>
            <td style="background-color:#e4e4e4;">开始考试</td>
            <td>
            	            		2016-01-04 11:33:41
            	            </td>
            <td style="background-color:#e4e4e4;">提交时间</td>
            <td>
            	            		2016-01-10 22:02:10
            	            </td>
    	</tr>
	</table>
    
    
    <input type="hidden" id="dtEndTime" value="2016-01-11 23:59:59" />
    <input type="hidden" id="dtStartTime" value="2015-12-28 00:00:00" />
    <input type="hidden" id="nTimeLength" value="90" />
    <input type="hidden" id="lSchoolId" value="204" />
    <input type="hidden" id="lUserId" value="7700006715" />
    <input type="hidden" id="nExaminType" value="0" />
    <input type="hidden" id="lExaminId" value="10200000047" />
    <input type="hidden" id="lPlanId" value="10200000026" />
    <input type="hidden" id="nUsedTime" value="66" />
    <input type="hidden" id="nExaminState" value="2" />
    <input type="hidden" id="nScoreState" value="1" />
</div>
</center>
<div class="xk_con">
    <div class="content">
    	<div class="ks_left ptb30">
    		    		<h1 class="ks_left_tit" id="keguanti">
    			客观题
    			<span class="col666 fs14 ml8">
    			(共100题,每题1分)
    			</span>
    		</h1>
                        <div>
            <ul class="mt30 fl">
                <li class="ks_t_xh">1</li>
                <li class="ks_tm mb10"  id="3070"></li>
                <div class="clear"></div>
                <div id="option3070"></div>
                <p class="tm_xx">
                	正确答案:<span style="color: red;padding-left: 10px" id="correctAnswer_3070">A</span>
                </p>
                <script type="text/javascript">
					var jsonQuestion={title:"就业信息是（ ）的基础。",options:[{name:"A",text:"择业 "},{name:"B",text:"适应职场 "},{name:"C",text:"创业 "},{name:"D",text:"自我认识"}]};
			 		showQuestion(jsonQuestion,3070);
				</script>
            </ul>
            <ul class="fr mr23" style="margin-top:70px;">
            	<span class="fs30 col_red" style="display:none;" id="span_right_3070">√</span>
            	<span class="fs30 col_red" style="display:block;" id="span_wrong_3070">x</span>
            </ul>
            <div class="clear"></div>
            </div>
                        <div>
            <ul class="mt30 fl">
                <li class="ks_t_xh">2</li>
                <li class="ks_tm mb10"  id="3088"></li>
                <div class="clear"></div>
                <div id="option3088"></div>
                <p class="tm_xx">
                	正确答案:<span style="color: red;padding-left: 10px" id="correctAnswer_3088">A</span>
                </p>
                <script type="text/javascript">
					var jsonQuestion={title:"大学生就业难的主要病因包括哪些：①政府过时的政策 ②学生个人能力的普遍下降 ③教育体系的滞后 ④大学扩招的弊端",options:[{name:"A",text:"①③ "},{name:"B",text:"②③④ "},{name:"C",text:"①②④ "},{name:"D",text:"①②③④"}]};
			 		showQuestion(jsonQuestion,3088);
				</script>
            </ul>
            <ul class="fr mr23" style="margin-top:70px;">
            	<span class="fs30 col_red" style="display:none;" id="span_right_3088">√</span>
            	<span class="fs30 col_red" style="display:block;" id="span_wrong_3088">x</span>
            </ul>
            <div class="clear"></div>
            </div>
                        <div>
            <ul class="mt30 fl">
                <li class="ks_t_xh">3</li>
                <li class="ks_tm mb10"  id="2327"></li>
                <div class="clear"></div>
                <div id="option2327"></div>
                <p class="tm_xx">
                	正确答案:<span style="color: red;padding-left: 10px" id="correctAnswer_2327">A</span>
                </p>
                <script type="text/javascript">
					var jsonQuestion={title:"对于自主创业的毕业生，各省、市在人事代理、社会保障、户籍管理、工商税务审批等方面做出了相关的规定，制定了优惠政策，积极予以支持。你认为这一说法：",options:[{name:"A",text:"正确"},{name:"B",text:"错误"}]};
			 		showQuestion(jsonQuestion,2327);
				</script>
            </ul>
            <ul class="fr mr23" style="margin-top:70px;">
            	<span class="fs30 col_red" style="display:none;" id="span_right_2327">√</span>
            	<span class="fs30 col_red" style="display:block;" id="span_wrong_2327">x</span>
            </ul>
            <div class="clear"></div>
            </div>
                        <div>
            <ul class="mt30 fl">
                <li class="ks_t_xh">4</li>
                <li class="ks_tm mb10"  id="3048"></li>
                <div class="clear"></div>
                <div id="option3048"></div>
                <p class="tm_xx">
                	正确答案:<span style="color: red;padding-left: 10px" id="correctAnswer_3048">D</span>
                </p>
                <script type="text/javascript">
					var jsonQuestion={title:"简历撰写中，编年体的内容编排形式最适合：",options:[{name:"A",text:"失业再就业的人 "},{name:"B",text:"初涉职场的人 "},{name:"C",text:"职业转变的人 "},{name:"D",text:"在某职业领域内寻求发展的人"}]};
			 		showQuestion(jsonQuestion,3048);
				</script>
            </ul>
            <ul class="fr mr23" style="margin-top:70px;">
            	<span class="fs30 col_red" style="display:none;" id="span_right_3048">√</span>
            	<span class="fs30 col_red" style="display:block;" id="span_wrong_3048">x</span>
            </ul>
            <div class="clear"></div>
            </div>
                        <div>
            <ul class="mt30 fl">
                <li class="ks_t_xh">5</li>
                <li class="ks_tm mb10"  id="3075"></li>
                <div class="clear"></div>
                <div id="option3075"></div>
                <p class="tm_xx">
                	正确答案:<span style="color: red;padding-left: 10px" id="correctAnswer_3075">A</span>
                </p>
                <script type="text/javascript">
					var jsonQuestion={title:"以下哪一角色处于人际网络金字塔的顶层？",options:[{name:"A",text:"招聘经理 "},{name:"B",text:"老师 "},{name:"C",text:"猎头 "},{name:"D",text:"校友"}]};
			 		showQuestion(jsonQuestion,3075);
				</script>
            </ul>
            <ul class="fr mr23" style="margin-top:70px;">
            	<span class="fs30 col_red" style="display:none;" id="span_right_3075">√</span>
            	<span class="fs30 col_red" style="display:block;" id="span_wrong_3075">x</span>
            </ul>
            <div class="clear"></div>
            </div>
                        <div>
            <ul class="mt30 fl">
                <li class="ks_t_xh">6</li>
                <li class="ks_tm mb10"  id="3278"></li>
                <div class="clear"></div>
                <div id="option3278"></div>
                <p class="tm_xx">
                	正确答案:<span style="color: red;padding-left: 10px" id="correctAnswer_3278">B</span>
                </p>
                <script type="text/javascript">
					var jsonQuestion={title:"一个人搜集、处理、应用就业信息的能力不足以影响他的就业成败。你认为该说法：",options:[{name:"A",text:"正确 "},{name:"B",text:"错误"}]};
			 		showQuestion(jsonQuestion,3278);
				</script>
            </ul>
            <ul class="fr mr23" style="margin-top:70px;">
            	<span class="fs30 col_red" style="display:none;" id="span_right_3278">√</span>
            	<span class="fs30 col_red" style="display:block;" id="span_wrong_3278">x</span>
            </ul>
            <div class="clear"></div>
            </div>
                        <div>
            <ul class="mt30 fl">
                <li class="ks_t_xh">7</li>
                <li class="ks_tm mb10"  id="2268"></li>
                <div class="clear"></div>
                <div id="option2268"></div>
                <p class="tm_xx">
                	正确答案:<span style="color: red;padding-left: 10px" id="correctAnswer_2268">D</span>
                </p>
                <script type="text/javascript">
					var jsonQuestion={title:"现阶段毕业生基本就业渠道有哪些： ①招聘会 ②网络平台招聘 ③通过熟人介绍或社会关系 ④通过中介服务机构介绍",options:[{name:"A",text:"①②④"},{name:"B",text:"①②③"},{name:"C",text:"②③④"},{name:"D",text:"①②③④"}]};
			 		showQuestion(jsonQuestion,2268);
				</script>
            </ul>
            <ul class="fr mr23" style="margin-top:70px;">
            	<span class="fs30 col_red" style="display:none;" id="span_right_2268">√</span>
            	<span class="fs30 col_red" style="display:block;" id="span_wrong_2268">x</span>
            </ul>
            <div class="clear"></div>
            </div>
                        <div>
            <ul class="mt30 fl">
                <li class="ks_t_xh">8</li>
                <li class="ks_tm mb10"  id="3076"></li>
                <div class="clear"></div>
                <div id="option3076"></div>
                <p class="tm_xx">
                	正确答案:<span style="color: red;padding-left: 10px" id="correctAnswer_3076">C</span>
                </p>
                <script type="text/javascript">
					var jsonQuestion={title:"以下哪一项不属于搜集招聘信息的原则？",options:[{name:"A",text:"广 "},{name:"B",text:"准 "},{name:"C",text:"稳 "},{name:"D",text:"早"}]};
			 		showQuestion(jsonQuestion,3076);
				</script>
            </ul>
            <ul class="fr mr23" style="margin-top:70px;">
            	<span class="fs30 col_red" style="display:none;" id="span_right_3076">√</span>
            	<span class="fs30 col_red" style="display:block;" id="span_wrong_3076">x</span>
            </ul>
            <div class="clear"></div>
            </div>
                        <div>
            <ul class="mt30 fl">
                <li class="ks_t_xh">9</li>
                <li class="ks_tm mb10"  id="3064"></li>
                <div class="clear"></div>
                <div id="option3064"></div>
                <p class="tm_xx">
                	正确答案:<span style="color: red;padding-left: 10px" id="correctAnswer_3064">C</span>
                </p>
                <script type="text/javascript">
					var jsonQuestion={title:"以下简历编写的小窍门中，错误的是：",options:[{name:"A",text:"巧妙使用数字和比例，营造比较优势 "},{name:"B",text:"巧妙地标明绩效和成果，突出个人能力 "},{name:"C",text:"巧妙地将优劣势全盘列出，面面俱到 "},{name:"D",text:"巧妙应用黑体和下划线，定位面试官注意范围"}]};
			 		showQuestion(jsonQuestion,3064);
				</script>
            </ul>
            <ul class="fr mr23" style="margin-top:70px;">
            	<span class="fs30 col_red" style="display:none;" id="span_right_3064">√</span>
            	<span class="fs30 col_red" style="display:block;" id="span_wrong_3064">x</span>
            </ul>
            <div class="clear"></div>
            </div>
                        <div>
            <ul class="mt30 fl">
                <li class="ks_t_xh">10</li>
                <li class="ks_tm mb10"  id="3046"></li>
                <div class="clear"></div>
                <div id="option3046"></div>
                <p class="tm_xx">
                	正确答案:<span style="color: red;padding-left: 10px" id="correctAnswer_3046">B</span>
                </p>
                <script type="text/javascript">
					var jsonQuestion={title:"在简历中，（ ）可写可不写。",options:[{name:"A",text:"主要技能 "},{name:"B",text:"兴趣爱好 "},{name:"C",text:"求职目标 "},{name:"D",text:"教育背景"}]};
			 		showQuestion(jsonQuestion,3046);
				</script>
            </ul>
            <ul class="fr mr23" style="margin-top:70px;">
            	<span class="fs30 col_red" style="display:none;" id="span_right_3046">√</span>
            	<span class="fs30 col_red" style="display:block;" id="span_wrong_3046">x</span>
            </ul>
            <div class="clear"></div>
            </div>
                        <div>
            <ul class="mt30 fl">
                <li class="ks_t_xh">11</li>
                <li class="ks_tm mb10"  id="2373"></li>
                <div class="clear"></div>
                <div id="option2373"></div>
                <p class="tm_xx">
                	正确答案:<span style="color: red;padding-left: 10px" id="correctAnswer_2373">D</span>
                </p>
                <script type="text/javascript">
					var jsonQuestion={title:"暑期实习对大学生来说，确实是个提早接触社会、体验职场环境的好机会。然而找到自己想去的实习单位是件不容易的事，很多同学由于缺乏经验而在面试关败下阵来。你觉得大学生应掌握什么策略和技巧，才能让自己在面试大军中脱颖而出？",options:[{name:"A",text:"面试前尽量了解公司背景和相关产品，如能在面试中运用一些专业产品术语，会让对方觉得你比较专业，理解力强 "},{name:"B",text:"掌握基本的面试礼仪，给面试官以积极、职业、干练的形象 "},{name:"C",text:"给对方公司或品牌进行适当的赞美，并对竞争对手有一定的了解和分析 "},{name:"D",text:"以上都是"}]};
			 		showQuestion(jsonQuestion,2373);
				</script>
            </ul>
            <ul class="fr mr23" style="margin-top:70px;">
            	<span class="fs30 col_red" style="display:none;" id="span_right_2373">√</span>
            	<span class="fs30 col_red" style="display:block;" id="span_wrong_2373">x</span>
            </ul>
            <div class="clear"></div>
            </div>
                        <div>
            <ul class="mt30 fl">
                <li class="ks_t_xh">12</li>
                <li class="ks_tm mb10"  id="3112"></li>
                <div class="clear"></div>
                <div id="option3112"></div>
                <p class="tm_xx">
                	正确答案:<span style="color: red;padding-left: 10px" id="correctAnswer_3112">B</span>
                </p>
                <script type="text/javascript">
					var jsonQuestion={title:"关于男士面试时的仪容仪表及穿着，以下说法不正确的是：",options:[{name:"A",text:"要穿西装及素色衬衫"},{name:"B",text:"要穿白色袜子，不可着深色袜子"},{name:"C",text:"头发要整齐，不要遮挡脸部"},{name:"D",text:"要扣好衣服扣子"}]};
			 		showQuestion(jsonQuestion,3112);
				</script>
            </ul>
            <ul class="fr mr23" style="margin-top:70px;">
            	<span class="fs30 col_red" style="display:none;" id="span_right_3112">√</span>
            	<span class="fs30 col_red" style="display:block;" id="span_wrong_3112">x</span>
            </ul>
            <div class="clear"></div>
            </div>
                        <div>
            <ul class="mt30 fl">
                <li class="ks_t_xh">13</li>
                <li class="ks_tm mb10"  id="3124"></li>
                <div class="clear"></div>
                <div id="option3124"></div>
                <p class="tm_xx">
                	正确答案:<span style="color: red;padding-left: 10px" id="correctAnswer_3124">D</span>
                </p>
                <script type="text/javascript">
					var jsonQuestion={title:"关于企业在招聘中遇到的困难，以下说法错误的是：",options:[{name:"A",text:"应聘者简历雷同 "},{name:"B",text:"难以通过面试判断应聘者实际能力 "},{name:"C",text:"面试过程中应聘者回答趋同 "},{name:"D",text:"应聘者简历的个性化程度较高"}]};
			 		showQuestion(jsonQuestion,3124);
				</script>
            </ul>
            <ul class="fr mr23" style="margin-top:70px;">
            	<span class="fs30 col_red" style="display:none;" id="span_right_3124">√</span>
            	<span class="fs30 col_red" style="display:block;" id="span_wrong_3124">x</span>
            </ul>
            <div class="clear"></div>
            </div>
                        <div>
            <ul class="mt30 fl">
                <li class="ks_t_xh">14</li>
                <li class="ks_tm mb10"  id="3115"></li>
                <div class="clear"></div>
                <div id="option3115"></div>
                <p class="tm_xx">
                	正确答案:<span style="color: red;padding-left: 10px" id="correctAnswer_3115">B</span>
                </p>
                <script type="text/javascript">
					var jsonQuestion={title:"关于面试过程中的礼仪，以下哪种说法是正确的？",options:[{name:"A",text:"与面试人员交谈时，两眼视线应落在对方头顶"},{name:"B",text:"应避免急于纠正面试官或与其发生争论"},{name:"C",text:"为了避免紧张，交谈时目光可移向他人他物"},{name:"D",text:"为了避免紧张，谈话时可环抱双臂"}]};
			 		showQuestion(jsonQuestion,3115);
				</script>
            </ul>
            <ul class="fr mr23" style="margin-top:70px;">
            	<span class="fs30 col_red" style="display:none;" id="span_right_3115">√</span>
            	<span class="fs30 col_red" style="display:block;" id="span_wrong_3115">x</span>
            </ul>
            <div class="clear"></div>
            </div>
                        <div>
            <ul class="mt30 fl">
                <li class="ks_t_xh">15</li>
                <li class="ks_tm mb10"  id="2406"></li>
                <div class="clear"></div>
                <div id="option2406"></div>
                <p class="tm_xx">
                	正确答案:<span style="color: red;padding-left: 10px" id="correctAnswer_2406">B</span>
                </p>
                <script type="text/javascript">
					var jsonQuestion={title:"面试是求职过程中的关键环节，面试中良好的对答技巧是获得面试官首肯的关键因素。关于面试中的应答技巧，下列表述错误的是：",options:[{name:"A",text:"说话时要用字准确，简洁明了，语调温和，收放自如"},{name:"B",text:"在对答时，如果认为自己的见解绝对有理，就不用害怕，就要坚持到底"},{name:"C",text:"身体语言的使用要不温不火，切忌过分夸张"},{name:"D",text:"面对较难回答的问题时，不要顾左右而言他，要敢于应对，敢于承认自己的不足"}]};
			 		showQuestion(jsonQuestion,2406);
				</script>
            </ul>
            <ul class="fr mr23" style="margin-top:70px;">
            	<span class="fs30 col_red" style="display:none;" id="span_right_2406">√</span>
            	<span class="fs30 col_red" style="display:block;" id="span_wrong_2406">x</span>
            </ul>
            <div class="clear"></div>
            </div>
                        <div>
            <ul class="mt30 fl">
                <li class="ks_t_xh">16</li>
                <li class="ks_tm mb10"  id="2366"></li>
                <div class="clear"></div>
                <div id="option2366"></div>
                <p class="tm_xx">
                	正确答案:<span style="color: red;padding-left: 10px" id="correctAnswer_2366">B</span>
                </p>
                <script type="text/javascript">
					var jsonQuestion={title:"王明，主修国际贸易专业，学习成绩优秀，毕业后去一家外贸公司应聘，这家公司特别强调员工的沟通能力，王明面试时滔滔不绝，自我感觉非常不错，可是等到面试结果出来，王明却榜上无名。你认为下列选项中，哪一项是王明落选的原因：",options:[{name:"A",text:"王明语言表达能力太差 "},{name:"B",text:"一个好的沟通者不但会说，还要会倾听 "},{name:"C",text:"公司觉得王明沟通能力过强，容易跳槽 "},{name:"D",text:"有其他人比王明更能说"}]};
			 		showQuestion(jsonQuestion,2366);
				</script>
            </ul>
            <ul class="fr mr23" style="margin-top:70px;">
            	<span class="fs30 col_red" style="display:none;" id="span_right_2366">√</span>
            	<span class="fs30 col_red" style="display:block;" id="span_wrong_2366">x</span>
            </ul>
            <div class="clear"></div>
            </div>
                        <div>
            <ul class="mt30 fl">
                <li class="ks_t_xh">17</li>
                <li class="ks_tm mb10"  id="3093"></li>
                <div class="clear"></div>
                <div id="option3093"></div>
                <p class="tm_xx">
                	正确答案:<span style="color: red;padding-left: 10px" id="correctAnswer_3093">B</span>
                </p>
                <script type="text/javascript">
					var jsonQuestion={title:"我们可以有第二次机会来树立自己的第一印象。你认为这种说法：",options:[{name:"A",text:"正确 "},{name:"B",text:"错误"}]};
			 		showQuestion(jsonQuestion,3093);
				</script>
            </ul>
            <ul class="fr mr23" style="margin-top:70px;">
            	<span class="fs30 col_red" style="display:none;" id="span_right_3093">√</span>
            	<span class="fs30 col_red" style="display:block;" id="span_wrong_3093">x</span>
            </ul>
            <div class="clear"></div>
            </div>
                        <div>
            <ul class="mt30 fl">
                <li class="ks_t_xh">18</li>
                <li class="ks_tm mb10"  id="2381"></li>
                <div class="clear"></div>
                <div id="option2381"></div>
                <p class="tm_xx">
                	正确答案:<span style="color: red;padding-left: 10px" id="correctAnswer_2381">D</span>
                </p>
                <script type="text/javascript">
					var jsonQuestion={title:"服装是10秒钟之内给人的第一印象，所以面试时一定要注意着装。但是并不要求你穿名牌衣服，只要简洁、干净、大方，显出你的自信就行了。关于面试时的着装礼仪，下列说法正确的是：",options:[{name:"A",text:"女同学着装应该注意简洁、干净、大方，忌奇装异服，忌暴露，忌不整洁 "},{name:"B",text:"女生穿套裙时，裙子不能太短，首饰不要花哨，化妆越淡越好，以健康、自然为标准，不要过多喷香水 "},{name:"C",text:"男生着装应该以西服为主，应给人以成熟、庄重感，领带下端不要长过腰带，忌服装不整洁，头发应梳整齐，胡子刮干净 "},{name:"D",text:"以上说法都正确"}]};
			 		showQuestion(jsonQuestion,2381);
				</script>
            </ul>
            <ul class="fr mr23" style="margin-top:70px;">
            	<span class="fs30 col_red" style="display:none;" id="span_right_2381">√</span>
            	<span class="fs30 col_red" style="display:block;" id="span_wrong_2381">x</span>
            </ul>
            <div class="clear"></div>
            </div>
                        <div>
            <ul class="mt30 fl">
                <li class="ks_t_xh">19</li>
                <li class="ks_tm mb10"  id="3114"></li>
                <div class="clear"></div>
                <div id="option3114"></div>
                <p class="tm_xx">
                	正确答案:<span style="color: red;padding-left: 10px" id="correctAnswer_3114">D</span>
                </p>
                <script type="text/javascript">
					var jsonQuestion={title:"关于面试中握手的礼仪，以下说法正确的是：",options:[{name:"A",text:"先握手，再问候 "},{name:"B",text:"伸出左手握手 "},{name:"C",text:"天冷可戴着手套握手 "},{name:"D",text:"握手时注视对方，不要旁顾他人他物"}]};
			 		showQuestion(jsonQuestion,3114);
				</script>
            </ul>
            <ul class="fr mr23" style="margin-top:70px;">
            	<span class="fs30 col_red" style="display:none;" id="span_right_3114">√</span>
            	<span class="fs30 col_red" style="display:block;" id="span_wrong_3114">x</span>
            </ul>
            <div class="clear"></div>
            </div>
                        <div>
            <ul class="mt30 fl">
                <li class="ks_t_xh">20</li>
                <li class="ks_tm mb10"  id="3092"></li>
                <div class="clear"></div>
                <div id="option3092"></div>
                <p class="tm_xx">
                	正确答案:<span style="color: red;padding-left: 10px" id="correctAnswer_3092">A</span>
                </p>
                <script type="text/javascript">
					var jsonQuestion={title:"面试通常在你认为开始之前已经开始，在你认为结束之时并未结束。你认为这种说法：",options:[{name:"A",text:"正确 "},{name:"B",text:"错误"}]};
			 		showQuestion(jsonQuestion,3092);
				</script>
            </ul>
            <ul class="fr mr23" style="margin-top:70px;">
            	<span class="fs30 col_red" style="display:none;" id="span_right_3092">√</span>
            	<span class="fs30 col_red" style="display:block;" id="span_wrong_3092">x</span>
            </ul>
            <div class="clear"></div>
            </div>
                        <div>
            <ul class="mt30 fl">
                <li class="ks_t_xh">21</li>
                <li class="ks_tm mb10"  id="2390"></li>
                <div class="clear"></div>
                <div id="option2390"></div>
                <p class="tm_xx">
                	正确答案:<span style="color: red;padding-left: 10px" id="correctAnswer_2390">B</span>
                </p>
                <script type="text/javascript">
					var jsonQuestion={title:"在“无领导小组讨论”中，下列做法不当的是：",options:[{name:"A",text:"有自己的观点和见解，即使与其他人的观点相同，也应该举出自己的论据进行补充"},{name:"B",text:"在与其他人观点不同时，据理力争，即使气氛搞僵也是值得的"},{name:"C",text:"当别人发言时，应该用目光注视对方，认真倾听"},{name:"D",text:"讨论中不要感情用事，怒形于色，言语措词也不要带刺，保持冷静"}]};
			 		showQuestion(jsonQuestion,2390);
				</script>
            </ul>
            <ul class="fr mr23" style="margin-top:70px;">
            	<span class="fs30 col_red" style="display:none;" id="span_right_2390">√</span>
            	<span class="fs30 col_red" style="display:block;" id="span_wrong_2390">x</span>
            </ul>
            <div class="clear"></div>
            </div>
                        <div>
            <ul class="mt30 fl">
                <li class="ks_t_xh">22</li>
                <li class="ks_tm mb10"  id="2395"></li>
                <div class="clear"></div>
                <div id="option2395"></div>
                <p class="tm_xx">
                	正确答案:<span style="color: red;padding-left: 10px" id="correctAnswer_2395">B</span>
                </p>
                <script type="text/javascript">
					var jsonQuestion={title:"与其它的面试相比，无领导小组讨论需要预先设置一个讨论题目。下列选项中，属于无领导小组讨论常用的题目类型的是：（1）开放式问题 （2）两难问题 （3）多项选择问题 （4）操作性问题 （5）资源争夺问题",options:[{name:"A",text:"（1）（3）（4）（5） "},{name:"B",text:"（1）（2）（3）（4）（5） "},{name:"C",text:"（1）（2）（3） "},{name:"D",text:"（1）（2）（4）（5）"}]};
			 		showQuestion(jsonQuestion,2395);
				</script>
            </ul>
            <ul class="fr mr23" style="margin-top:70px;">
            	<span class="fs30 col_red" style="display:none;" id="span_right_2395">√</span>
            	<span class="fs30 col_red" style="display:block;" id="span_wrong_2395">x</span>
            </ul>
            <div class="clear"></div>
            </div>
                        <div>
            <ul class="mt30 fl">
                <li class="ks_t_xh">23</li>
                <li class="ks_tm mb10"  id="3105"></li>
                <div class="clear"></div>
                <div id="option3105"></div>
                <p class="tm_xx">
                	正确答案:<span style="color: red;padding-left: 10px" id="correctAnswer_3105">C</span>
                </p>
                <script type="text/javascript">
					var jsonQuestion={title:"面试结束后，需要：",options:[{name:"A",text:"赶紧托熟人说情 "},{name:"B",text:"尽早打听面试结果 "},{name:"C",text:"无论录用与否都要向对方致谢 "},{name:"D",text:"提出更多的问题"}]};
			 		showQuestion(jsonQuestion,3105);
				</script>
            </ul>
            <ul class="fr mr23" style="margin-top:70px;">
            	<span class="fs30 col_red" style="display:none;" id="span_right_3105">√</span>
            	<span class="fs30 col_red" style="display:block;" id="span_wrong_3105">x</span>
            </ul>
            <div class="clear"></div>
            </div>
                        <div>
            <ul class="mt30 fl">
                <li class="ks_t_xh">24</li>
                <li class="ks_tm mb10"  id="2408"></li>
                <div class="clear"></div>
                <div id="option2408"></div>
                <p class="tm_xx">
                	正确答案:<span style="color: red;padding-left: 10px" id="correctAnswer_2408">C</span>
                </p>
                <script type="text/javascript">
					var jsonQuestion={title:"关于面试中应聘者对服饰的选择与搭配，下列说法错误的是：",options:[{name:"A",text:"着装要合体，讲究线条配置、搭配合理，色调和谐 "},{name:"B",text:"衣着服饰要投雇主所好 "},{name:"C",text:"要凸显自己的个性与时尚，给主试者以深刻的印象 "},{name:"D",text:"服饰要适应应聘职位工作的需要"}]};
			 		showQuestion(jsonQuestion,2408);
				</script>
            </ul>
            <ul class="fr mr23" style="margin-top:70px;">
            	<span class="fs30 col_red" style="display:none;" id="span_right_2408">√</span>
            	<span class="fs30 col_red" style="display:block;" id="span_wrong_2408">x</span>
            </ul>
            <div class="clear"></div>
            </div>
                        <div>
            <ul class="mt30 fl">
                <li class="ks_t_xh">25</li>
                <li class="ks_tm mb10"  id="3094"></li>
                <div class="clear"></div>
                <div id="option3094"></div>
                <p class="tm_xx">
                	正确答案:<span style="color: red;padding-left: 10px" id="correctAnswer_3094">C</span>
                </p>
                <script type="text/javascript">
					var jsonQuestion={title:"关于签证面试，以下说法错误的是：",options:[{name:"A",text:"注重提高外语能力 "},{name:"B",text:"主要侧重申请者的出国目的、经济能力等问题 "},{name:"C",text:"要了解欲申请国家的所有情况 "},{name:"D",text:"面试时清楚陈述自己的理由"}]};
			 		showQuestion(jsonQuestion,3094);
				</script>
            </ul>
            <ul class="fr mr23" style="margin-top:70px;">
            	<span class="fs30 col_red" style="display:none;" id="span_right_3094">√</span>
            	<span class="fs30 col_red" style="display:block;" id="span_wrong_3094">x</span>
            </ul>
            <div class="clear"></div>
            </div>
                        <div>
            <ul class="mt30 fl">
                <li class="ks_t_xh">26</li>
                <li class="ks_tm mb10"  id="3126"></li>
                <div class="clear"></div>
                <div id="option3126"></div>
                <p class="tm_xx">
                	正确答案:<span style="color: red;padding-left: 10px" id="correctAnswer_3126">D</span>
                </p>
                <script type="text/javascript">
					var jsonQuestion={title:"个人求职档案中应该记录的事项包括哪些：①雇主的联系方式 ②求职信 ③接到的雇主回复 ④面试通知",options:[{name:"A",text:"①②③ "},{name:"B",text:"②③④ "},{name:"C",text:"①③④ "},{name:"D",text:"①②③④"}]};
			 		showQuestion(jsonQuestion,3126);
				</script>
            </ul>
            <ul class="fr mr23" style="margin-top:70px;">
            	<span class="fs30 col_red" style="display:none;" id="span_right_3126">√</span>
            	<span class="fs30 col_red" style="display:block;" id="span_wrong_3126">x</span>
            </ul>
            <div class="clear"></div>
            </div>
                        <div>
            <ul class="mt30 fl">
                <li class="ks_t_xh">27</li>
                <li class="ks_tm mb10"  id="2399"></li>
                <div class="clear"></div>
                <div id="option2399"></div>
                <p class="tm_xx">
                	正确答案:<span style="color: red;padding-left: 10px" id="correctAnswer_2399">C</span>
                </p>
                <script type="text/javascript">
					var jsonQuestion={title:"和其它面试形式相比，情景面试有其自身的特点。下列选项中，不属于情景面试特点的是：",options:[{name:"A",text:"情景面试更具有针对性 "},{name:"B",text:"情景面试更具有直接性 "},{name:"C",text:"情景面试更具有真实性 "},{name:"D",text:"情景面试更具有可信性"}]};
			 		showQuestion(jsonQuestion,2399);
				</script>
            </ul>
            <ul class="fr mr23" style="margin-top:70px;">
            	<span class="fs30 col_red" style="display:none;" id="span_right_2399">√</span>
            	<span class="fs30 col_red" style="display:block;" id="span_wrong_2399">x</span>
            </ul>
            <div class="clear"></div>
            </div>
                        <div>
            <ul class="mt30 fl">
                <li class="ks_t_xh">28</li>
                <li class="ks_tm mb10"  id="2376"></li>
                <div class="clear"></div>
                <div id="option2376"></div>
                <p class="tm_xx">
                	正确答案:<span style="color: red;padding-left: 10px" id="correctAnswer_2376">D</span>
                </p>
                <script type="text/javascript">
					var jsonQuestion={title:"一般而言，岗位对求职者除了技能方面外还有许多柔性的要求，而这些柔性的要求很大程度上都是通过面试来考察的。文职岗位要求有很强的表达能力，这样，在面试中我们应该：",options:[{name:"A",text:"在回答考官的问题时，可以尝试运用辩证法，把问题回答的圆满完整，回答问题不要陷入绝对的肯定与否定，应正反两个方面考虑 "},{name:"B",text:"回答问题前首先要冷静思考，理清思路，不要急于回答 "},{name:"C",text:"在面试时要特别注意说话内容、说话语气以及表达出的诚意，切忌颠三倒四，语义不清 "},{name:"D",text:"以上说法都正确"}]};
			 		showQuestion(jsonQuestion,2376);
				</script>
            </ul>
            <ul class="fr mr23" style="margin-top:70px;">
            	<span class="fs30 col_red" style="display:none;" id="span_right_2376">√</span>
            	<span class="fs30 col_red" style="display:block;" id="span_wrong_2376">x</span>
            </ul>
            <div class="clear"></div>
            </div>
                        <div>
            <ul class="mt30 fl">
                <li class="ks_t_xh">29</li>
                <li class="ks_tm mb10"  id="2379"></li>
                <div class="clear"></div>
                <div id="option2379"></div>
                <p class="tm_xx">
                	正确答案:<span style="color: red;padding-left: 10px" id="correctAnswer_2379">D</span>
                </p>
                <script type="text/javascript">
					var jsonQuestion={title:"形体语言是一种很重要的交际手段和表达自己的方式。在面试中，面试官会注意你的每个细节，从这些细节中来评价你的各个方面。因此面试中，我们应该注意的问题是：",options:[{name:"A",text:"不要故意挤压你的手指或者折纸、转笔等，这会被认为是不严肃的表现 "},{name:"B",text:"面试时不要挠头发、胡子、耳朵，这些可能被认为是紧张的表现 "},{name:"C",text:"用手捂着嘴说话也是一种紧张的表现，这样会影响自己在考官心中的印象 "},{name:"D",text:"以上说法都应该注意"}]};
			 		showQuestion(jsonQuestion,2379);
				</script>
            </ul>
            <ul class="fr mr23" style="margin-top:70px;">
            	<span class="fs30 col_red" style="display:none;" id="span_right_2379">√</span>
            	<span class="fs30 col_red" style="display:block;" id="span_wrong_2379">x</span>
            </ul>
            <div class="clear"></div>
            </div>
                        <div>
            <ul class="mt30 fl">
                <li class="ks_t_xh">30</li>
                <li class="ks_tm mb10"  id="2392"></li>
                <div class="clear"></div>
                <div id="option2392"></div>
                <p class="tm_xx">
                	正确答案:<span style="color: red;padding-left: 10px" id="correctAnswer_2392">B</span>
                </p>
                <script type="text/javascript">
					var jsonQuestion={title:"无领导小组讨论面试中，考官设置“两难问题”所重点考察的方面是：",options:[{name:"A",text:"思考问题是否全面、是否有针对性，思路是否清晰，是否有新的观点和见解"},{name:"B",text:"分析能力、语言表达能力以及说服力等"},{name:"C",text:"能动性、合作能力以及在一项实际操作任务中所充当的角色特点"},{name:"D",text:"分析问题、抓住问题本质等方面的能力"}]};
			 		showQuestion(jsonQuestion,2392);
				</script>
            </ul>
            <ul class="fr mr23" style="margin-top:70px;">
            	<span class="fs30 col_red" style="display:none;" id="span_right_2392">√</span>
            	<span class="fs30 col_red" style="display:block;" id="span_wrong_2392">x</span>
            </ul>
            <div class="clear"></div>
            </div>
                        <div>
            <ul class="mt30 fl">
                <li class="ks_t_xh">31</li>
                <li class="ks_tm mb10"  id="2604"></li>
                <div class="clear"></div>
                <div id="option2604"></div>
                <p class="tm_xx">
                	正确答案:<span style="color: red;padding-left: 10px" id="correctAnswer_2604">B</span>
                </p>
                <script type="text/javascript">
					var jsonQuestion={title:"“能力”是企业选聘人才的标准之一。因此，初涉职场的新人应抓住一切机会，甚至创造机会来尽快展现自己的才能和实力，得到他人的认可和刮目相看。对于这一看法，你认为：",options:[{name:"A",text:"正确 "},{name:"B",text:"错误"}]};
			 		showQuestion(jsonQuestion,2604);
				</script>
            </ul>
            <ul class="fr mr23" style="margin-top:70px;">
            	<span class="fs30 col_red" style="display:none;" id="span_right_2604">√</span>
            	<span class="fs30 col_red" style="display:block;" id="span_wrong_2604">x</span>
            </ul>
            <div class="clear"></div>
            </div>
                        <div>
            <ul class="mt30 fl">
                <li class="ks_t_xh">32</li>
                <li class="ks_tm mb10"  id="2625"></li>
                <div class="clear"></div>
                <div id="option2625"></div>
                <p class="tm_xx">
                	正确答案:<span style="color: red;padding-left: 10px" id="correctAnswer_2625">D</span>
                </p>
                <script type="text/javascript">
					var jsonQuestion={title:"职场中，当同事冷漠时，下列做法中合理的是：",options:[{name:"A",text:"不要有任何臆测，你可以不经意地问他“怎么了？” "},{name:"B",text:"以友善态度表示你想协助他 "},{name:"C",text:"如果他因感情或疾病等私人问题影响到工作情绪时，建议他找人谈谈或休假 "},{name:"D",text:"以上说法都正确"}]};
			 		showQuestion(jsonQuestion,2625);
				</script>
            </ul>
            <ul class="fr mr23" style="margin-top:70px;">
            	<span class="fs30 col_red" style="display:none;" id="span_right_2625">√</span>
            	<span class="fs30 col_red" style="display:block;" id="span_wrong_2625">x</span>
            </ul>
            <div class="clear"></div>
            </div>
                        <div>
            <ul class="mt30 fl">
                <li class="ks_t_xh">33</li>
                <li class="ks_tm mb10"  id="2597"></li>
                <div class="clear"></div>
                <div id="option2597"></div>
                <p class="tm_xx">
                	正确答案:<span style="color: red;padding-left: 10px" id="correctAnswer_2597">D</span>
                </p>
                <script type="text/javascript">
					var jsonQuestion={title:"到用人单位报到，是大学毕业生走上新工作岗位的第一步。到单位报到时，毕业生应准备哪些证件? ①报到证 ②毕业证书、学位证书 ③户口迁移证 ④就业协议书",options:[{name:"A",text:"①② "},{name:"B",text:"②③ "},{name:"C",text:"①②③ "},{name:"D",text:"①②③④"}]};
			 		showQuestion(jsonQuestion,2597);
				</script>
            </ul>
            <ul class="fr mr23" style="margin-top:70px;">
            	<span class="fs30 col_red" style="display:none;" id="span_right_2597">√</span>
            	<span class="fs30 col_red" style="display:block;" id="span_wrong_2597">x</span>
            </ul>
            <div class="clear"></div>
            </div>
                        <div>
            <ul class="mt30 fl">
                <li class="ks_t_xh">34</li>
                <li class="ks_tm mb10"  id="2671"></li>
                <div class="clear"></div>
                <div id="option2671"></div>
                <p class="tm_xx">
                	正确答案:<span style="color: red;padding-left: 10px" id="correctAnswer_2671">D</span>
                </p>
                <script type="text/javascript">
					var jsonQuestion={title:"一个团队里面包含各种角色，不同角色类型有不同的特点。以下对团队角色的认识正确的是：",options:[{name:"A",text:"不同角色分工不同，因而其重要性也不同"},{name:"B",text:"不利于团队的角色一定要排斥"},{name:"C",text:"完美的人才可以领导团队"},{name:"D",text:"通过协作弥补不同团队角色的不足"}]};
			 		showQuestion(jsonQuestion,2671);
				</script>
            </ul>
            <ul class="fr mr23" style="margin-top:70px;">
            	<span class="fs30 col_red" style="display:none;" id="span_right_2671">√</span>
            	<span class="fs30 col_red" style="display:block;" id="span_wrong_2671">x</span>
            </ul>
            <div class="clear"></div>
            </div>
                        <div>
            <ul class="mt30 fl">
                <li class="ks_t_xh">35</li>
                <li class="ks_tm mb10"  id="2599"></li>
                <div class="clear"></div>
                <div id="option2599"></div>
                <p class="tm_xx">
                	正确答案:<span style="color: red;padding-left: 10px" id="correctAnswer_2599">A</span>
                </p>
                <script type="text/javascript">
					var jsonQuestion={title:"在职场中，我们不能将“和谐的人际关系”作为自身发展的唯一筹码。你认为这种看法：",options:[{name:"A",text:"正确 "},{name:"B",text:"错误"}]};
			 		showQuestion(jsonQuestion,2599);
				</script>
            </ul>
            <ul class="fr mr23" style="margin-top:70px;">
            	<span class="fs30 col_red" style="display:none;" id="span_right_2599">√</span>
            	<span class="fs30 col_red" style="display:block;" id="span_wrong_2599">x</span>
            </ul>
            <div class="clear"></div>
            </div>
                        <div>
            <ul class="mt30 fl">
                <li class="ks_t_xh">36</li>
                <li class="ks_tm mb10"  id="2606"></li>
                <div class="clear"></div>
                <div id="option2606"></div>
                <p class="tm_xx">
                	正确答案:<span style="color: red;padding-left: 10px" id="correctAnswer_2606">C</span>
                </p>
                <script type="text/javascript">
					var jsonQuestion={title:"影片《蒙娜丽莎的微笑》讲述了上世纪中叶，一位名叫凯瑟琳的艺术史老师努力改变被誉为“没有男子的常青藤”的美国威斯理女子学院教育理念的故事。凯瑟琳拥有开放的自由思想，立志要把新思想传授给学生们。但在当时，美国封建保守思想仍非常严重。威斯理的教育不是教学生们如何获得知识和智慧，而是把学生今后的婚姻定义为教育是否成功的标准。凯瑟琳来到这里后，没有像其他老师那样沿袭该校的传统教学风格，而是大胆地去挑战传统，鼓励学生发掘自己的兴趣，并且支持他们去实践自己的想法。她的做法不仅受到了一些大户人家女儿的挑战，而且受到家长、学校各方的质疑和责难。但是她凭借坚定的信念顽强地坚持了下来，最终赢得了学生们的尊敬和爱戴。这个故事给了我们怎样的职场启示？",options:[{name:"A",text:"明确的职业目标就像一台发电机，足以激发难以想象的能量 "},{name:"B",text:"除非你不工作，否则永远不要以抵触的心态做事，因为那样只能使你的能力大打折扣 "},{name:"C",text:"不要碍于习惯、主观认知等原因，应尽可能地坚持在工作中发挥自己的潜能 "},{name:"D",text:"以上都不对"}]};
			 		showQuestion(jsonQuestion,2606);
				</script>
            </ul>
            <ul class="fr mr23" style="margin-top:70px;">
            	<span class="fs30 col_red" style="display:none;" id="span_right_2606">√</span>
            	<span class="fs30 col_red" style="display:block;" id="span_wrong_2606">x</span>
            </ul>
            <div class="clear"></div>
            </div>
                        <div>
            <ul class="mt30 fl">
                <li class="ks_t_xh">37</li>
                <li class="ks_tm mb10"  id="2592"></li>
                <div class="clear"></div>
                <div id="option2592"></div>
                <p class="tm_xx">
                	正确答案:<span style="color: red;padding-left: 10px" id="correctAnswer_2592">D</span>
                </p>
                <script type="text/javascript">
					var jsonQuestion={title:"（ ）称之为人际交往中的“心理距离效应”，即只有找到合适的人际关系距离，才能建立融洽的关系。",options:[{name:"A",text:"蜗牛法则 "},{name:"B",text:"考拉法则 "},{name:"C",text:"袋鼠法则 "},{name:"D",text:"刺猬法则"}]};
			 		showQuestion(jsonQuestion,2592);
				</script>
            </ul>
            <ul class="fr mr23" style="margin-top:70px;">
            	<span class="fs30 col_red" style="display:none;" id="span_right_2592">√</span>
            	<span class="fs30 col_red" style="display:block;" id="span_wrong_2592">x</span>
            </ul>
            <div class="clear"></div>
            </div>
                        <div>
            <ul class="mt30 fl">
                <li class="ks_t_xh">38</li>
                <li class="ks_tm mb10"  id="2666"></li>
                <div class="clear"></div>
                <div id="option2666"></div>
                <p class="tm_xx">
                	正确答案:<span style="color: red;padding-left: 10px" id="correctAnswer_2666">A</span>
                </p>
                <script type="text/javascript">
					var jsonQuestion={title:"小王是某重点大学计算机系应届毕业生，踌躇满志的他却被公司分配到了一个不受重视的部门，每天做的是打杂跑腿的工作，并且常常受到上司无端的批评和指责，小王对此很是苦恼。小王遇到的这种麻烦在管理学上叫做：",options:[{name:"A",text:"蘑菇定律 "},{name:"B",text:"萝卜定律 "},{name:"C",text:"菠菜定律 "},{name:"D",text:"番茄定律"}]};
			 		showQuestion(jsonQuestion,2666);
				</script>
            </ul>
            <ul class="fr mr23" style="margin-top:70px;">
            	<span class="fs30 col_red" style="display:none;" id="span_right_2666">√</span>
            	<span class="fs30 col_red" style="display:block;" id="span_wrong_2666">x</span>
            </ul>
            <div class="clear"></div>
            </div>
                        <div>
            <ul class="mt30 fl">
                <li class="ks_t_xh">39</li>
                <li class="ks_tm mb10"  id="2636"></li>
                <div class="clear"></div>
                <div id="option2636"></div>
                <p class="tm_xx">
                	正确答案:<span style="color: red;padding-left: 10px" id="correctAnswer_2636">A</span>
                </p>
                <script type="text/javascript">
					var jsonQuestion={title:"职场中的“3Q Very Much”准则，是指IQ（智商＝专业技能）、EQ（情绪商数）、AQ（抗压性）三者并重。请判断这一说法的正误。",options:[{name:"A",text:"正确 "},{name:"B",text:"错误"}]};
			 		showQuestion(jsonQuestion,2636);
				</script>
            </ul>
            <ul class="fr mr23" style="margin-top:70px;">
            	<span class="fs30 col_red" style="display:none;" id="span_right_2636">√</span>
            	<span class="fs30 col_red" style="display:block;" id="span_wrong_2636">x</span>
            </ul>
            <div class="clear"></div>
            </div>
                        <div>
            <ul class="mt30 fl">
                <li class="ks_t_xh">40</li>
                <li class="ks_tm mb10"  id="2623"></li>
                <div class="clear"></div>
                <div id="option2623"></div>
                <p class="tm_xx">
                	正确答案:<span style="color: red;padding-left: 10px" id="correctAnswer_2623">D</span>
                </p>
                <script type="text/javascript">
					var jsonQuestion={title:"人人都有自己的领导。上至国家领导，下至普通百姓，都是如此。工作中，如何与领导相处，下列做法合理的是：",options:[{name:"A",text:"如果领导明确指示你去完成某项工作，那你一定要用最简洁有效的方式明白领导的意图和工作的重点 "},{name:"B",text:"作为下属，在接受命令之后，应该积极开动脑筋，对即将负责的工作有一个初步的认识，告诉领导你的初步解决方案，尤其是对于可能在工作中出现的困难要有充分的认识，对于在自己能力范围之外的困难，应提请领导协调别的部门加以解决 "},{name:"C",text:"在工作进行之中随时向领导汇报 "},{name:"D",text:"以上说法都正确"}]};
			 		showQuestion(jsonQuestion,2623);
				</script>
            </ul>
            <ul class="fr mr23" style="margin-top:70px;">
            	<span class="fs30 col_red" style="display:none;" id="span_right_2623">√</span>
            	<span class="fs30 col_red" style="display:block;" id="span_wrong_2623">x</span>
            </ul>
            <div class="clear"></div>
            </div>
                        <div>
            <ul class="mt30 fl">
                <li class="ks_t_xh">41</li>
                <li class="ks_tm mb10"  id="2650"></li>
                <div class="clear"></div>
                <div id="option2650"></div>
                <p class="tm_xx">
                	正确答案:<span style="color: red;padding-left: 10px" id="correctAnswer_2650">D</span>
                </p>
                <script type="text/javascript">
					var jsonQuestion={title:"大学生初入职场，首当其冲的便是角色转变。应对这种角色转变，下列做法不正确的是：",options:[{name:"A",text:"认真了解企业文化，尽快融入企业"},{name:"B",text:"快速熟悉每位同事，不要拉帮结派"},{name:"C",text:"做事学会任劳任怨，分清轻重缓急"},{name:"D",text:"全身心投入工作，积极与老板套近乎"}]};
			 		showQuestion(jsonQuestion,2650);
				</script>
            </ul>
            <ul class="fr mr23" style="margin-top:70px;">
            	<span class="fs30 col_red" style="display:none;" id="span_right_2650">√</span>
            	<span class="fs30 col_red" style="display:block;" id="span_wrong_2650">x</span>
            </ul>
            <div class="clear"></div>
            </div>
                        <div>
            <ul class="mt30 fl">
                <li class="ks_t_xh">42</li>
                <li class="ks_tm mb10"  id="2629"></li>
                <div class="clear"></div>
                <div id="option2629"></div>
                <p class="tm_xx">
                	正确答案:<span style="color: red;padding-left: 10px" id="correctAnswer_2629">D</span>
                </p>
                <script type="text/javascript">
					var jsonQuestion={title:"对于职场新人来说，跟上司沟通，我们应该注意到的问题是：",options:[{name:"A",text:"作为新人，一个很重要的原则就是要知道他是你的上司，尊重他的权威，做任何事情，让他感受到，他是你的上司，层次很分明，这个角色意识一定要非常明确 "},{name:"B",text:"一定要了解这个上司是一个什么样的人，这是一个很重要的前提 "},{name:"C",text:"跟上司沟通，一定要注意他的细节、他的言语动作，或者是其他的小的细节行为，要学会察言观色的明确一些观点 "},{name:"D",text:"以上说法都正确"}]};
			 		showQuestion(jsonQuestion,2629);
				</script>
            </ul>
            <ul class="fr mr23" style="margin-top:70px;">
            	<span class="fs30 col_red" style="display:none;" id="span_right_2629">√</span>
            	<span class="fs30 col_red" style="display:block;" id="span_wrong_2629">x</span>
            </ul>
            <div class="clear"></div>
            </div>
                        <div>
            <ul class="mt30 fl">
                <li class="ks_t_xh">43</li>
                <li class="ks_tm mb10"  id="2630"></li>
                <div class="clear"></div>
                <div id="option2630"></div>
                <p class="tm_xx">
                	正确答案:<span style="color: red;padding-left: 10px" id="correctAnswer_2630">C</span>
                </p>
                <script type="text/javascript">
					var jsonQuestion={title:"每个人在职场中，由于各种原因，都有可能遇到不公平的待遇，尤其是对于刚刚步入岗位的大学生，受到不公平的待遇是很常见的事情。对于这种情况，下列做法不当的是：",options:[{name:"A",text:"当遇到不公平的待遇时，勿过分计较个人的得失，应从大局出发，让理智有效的控制感情，平和心态，这样有助于避免不良心态的滋生和发展 "},{name:"B",text:"有意识的改变对比的内容，努力创造优势，改变不利的对比反差，从而达到心态平和 "},{name:"C",text:"在遇到不公平的待遇时，应该据理力争，不能改变自己的原则，不惜与老板和公司翻脸，这样才能够维护自己的合法权益不受损害 "},{name:"D",text:"当在职场中受到不公平的待遇时，切忌义气用事，而应冷静理智的处理，保持良好的形象和风度，寻找得体的选择"}]};
			 		showQuestion(jsonQuestion,2630);
				</script>
            </ul>
            <ul class="fr mr23" style="margin-top:70px;">
            	<span class="fs30 col_red" style="display:none;" id="span_right_2630">√</span>
            	<span class="fs30 col_red" style="display:block;" id="span_wrong_2630">x</span>
            </ul>
            <div class="clear"></div>
            </div>
                        <div>
            <ul class="mt30 fl">
                <li class="ks_t_xh">44</li>
                <li class="ks_tm mb10"  id="2616"></li>
                <div class="clear"></div>
                <div id="option2616"></div>
                <p class="tm_xx">
                	正确答案:<span style="color: red;padding-left: 10px" id="correctAnswer_2616">D</span>
                </p>
                <script type="text/javascript">
					var jsonQuestion={title:"工作中有的领导喜欢挑剔和指责下属，认为下属应该把他交待的一切干好，并且从不承认别人的优点，不尊重下属的劳动成果，甚至以为如果找不出下属的毛病，就显示不出自己的水平高。面对这种领导，应如何相处？以下做法错误的是：",options:[{name:"A",text:"要向这种领导多汇报，让他知道你在干什么 "},{name:"B",text:"工作中多请教，使他感到下属的成绩中有他的心血和功劳 "},{name:"C",text:"要在汇报工作时，强调工作中遇到的困难，并重点介绍是如何克服困难的 "},{name:"D",text:"如果有可能，尽量减少汇报的次数，以免增加领导的坏印象"}]};
			 		showQuestion(jsonQuestion,2616);
				</script>
            </ul>
            <ul class="fr mr23" style="margin-top:70px;">
            	<span class="fs30 col_red" style="display:none;" id="span_right_2616">√</span>
            	<span class="fs30 col_red" style="display:block;" id="span_wrong_2616">x</span>
            </ul>
            <div class="clear"></div>
            </div>
                        <div>
            <ul class="mt30 fl">
                <li class="ks_t_xh">45</li>
                <li class="ks_tm mb10"  id="2665"></li>
                <div class="clear"></div>
                <div id="option2665"></div>
                <p class="tm_xx">
                	正确答案:<span style="color: red;padding-left: 10px" id="correctAnswer_2665">D</span>
                </p>
                <script type="text/javascript">
					var jsonQuestion={title:"相互接纳，是指组织与新雇员个人之间的相互关系。关于相互接纳，以下哪项表述是不正确的：",options:[{name:"A",text:"双方必须互相认同和接纳，只有单方的认同，相互接纳便不存在 "},{name:"B",text:"相互接纳是一种心理契约，是一个过程 "},{name:"C",text:"相互接纳这一阶段无确定期限，期限的长短，受工作性质、部门类型、上司风格、组织文化、新雇员的实际等诸多因素的影响 "},{name:"D",text:"以上说法都不对"}]};
			 		showQuestion(jsonQuestion,2665);
				</script>
            </ul>
            <ul class="fr mr23" style="margin-top:70px;">
            	<span class="fs30 col_red" style="display:none;" id="span_right_2665">√</span>
            	<span class="fs30 col_red" style="display:block;" id="span_wrong_2665">x</span>
            </ul>
            <div class="clear"></div>
            </div>
                        <div>
            <ul class="mt30 fl">
                <li class="ks_t_xh">46</li>
                <li class="ks_tm mb10"  id="2644"></li>
                <div class="clear"></div>
                <div id="option2644"></div>
                <p class="tm_xx">
                	正确答案:<span style="color: red;padding-left: 10px" id="correctAnswer_2644">D</span>
                </p>
                <script type="text/javascript">
					var jsonQuestion={title:"小王是一家公司的职员，他的大部分工作都是为他人服务，或者在需要的时候做一些应急的事情。那么你认为有关小王工作的描述中，正确的是：",options:[{name:"A",text:"他的工作无法做计划 "},{name:"B",text:"他只需要做好自己应该做的 "},{name:"C",text:"他没有必要做计划 "},{name:"D",text:"对一些重复出现的事情可以做计划"}]};
			 		showQuestion(jsonQuestion,2644);
				</script>
            </ul>
            <ul class="fr mr23" style="margin-top:70px;">
            	<span class="fs30 col_red" style="display:none;" id="span_right_2644">√</span>
            	<span class="fs30 col_red" style="display:block;" id="span_wrong_2644">x</span>
            </ul>
            <div class="clear"></div>
            </div>
                        <div>
            <ul class="mt30 fl">
                <li class="ks_t_xh">47</li>
                <li class="ks_tm mb10"  id="2626"></li>
                <div class="clear"></div>
                <div id="option2626"></div>
                <p class="tm_xx">
                	正确答案:<span style="color: red;padding-left: 10px" id="correctAnswer_2626">D</span>
                </p>
                <script type="text/javascript">
					var jsonQuestion={title:"大学生初涉职场，对现实的工作和人际关系等新面临的问题产生困扰，心理上会有一定的落差。为了避免职业心理危机，大学生要做到：",options:[{name:"A",text:"尽快平静心情，认真了解企业文化"},{name:"B",text:"不急躁，做事时分清轻重缓急"},{name:"C",text:"克服以前的自由心理，遵守公司章程"},{name:"D",text:"以上说法都正确"}]};
			 		showQuestion(jsonQuestion,2626);
				</script>
            </ul>
            <ul class="fr mr23" style="margin-top:70px;">
            	<span class="fs30 col_red" style="display:none;" id="span_right_2626">√</span>
            	<span class="fs30 col_red" style="display:block;" id="span_wrong_2626">x</span>
            </ul>
            <div class="clear"></div>
            </div>
                        <div>
            <ul class="mt30 fl">
                <li class="ks_t_xh">48</li>
                <li class="ks_tm mb10"  id="2669"></li>
                <div class="clear"></div>
                <div id="option2669"></div>
                <p class="tm_xx">
                	正确答案:<span style="color: red;padding-left: 10px" id="correctAnswer_2669">B</span>
                </p>
                <script type="text/javascript">
					var jsonQuestion={title:"作为职场新人，下列做法不当的是：",options:[{name:"A",text:"注意个人形象，不但要具有内在的涵养与文化素质，也要借助外在形象让自己达到内外统一"},{name:"B",text:"充满激情，什么事情要敢做敢当，要敢于挑战权威，尽快树立自己的威信"},{name:"C",text:"顺应风格，不同的企业文化、不同的管理制度、不同的业务部门，沟通风格都会有所不同"},{name:"D",text:"找准立场，作为新人应该谦虚，发表观点时也不要过于强调自己的观点，多站在别人的立场上考虑问题"}]};
			 		showQuestion(jsonQuestion,2669);
				</script>
            </ul>
            <ul class="fr mr23" style="margin-top:70px;">
            	<span class="fs30 col_red" style="display:none;" id="span_right_2669">√</span>
            	<span class="fs30 col_red" style="display:block;" id="span_wrong_2669">x</span>
            </ul>
            <div class="clear"></div>
            </div>
                        <div>
            <ul class="mt30 fl">
                <li class="ks_t_xh">49</li>
                <li class="ks_tm mb10"  id="2613"></li>
                <div class="clear"></div>
                <div id="option2613"></div>
                <p class="tm_xx">
                	正确答案:<span style="color: red;padding-left: 10px" id="correctAnswer_2613">B</span>
                </p>
                <script type="text/javascript">
					var jsonQuestion={title:"小钱来公司快一个月了，她每天上午发很多有趣的邮件给周围同事，下午则请大家喝奶茶吃点心，三天两头这样，同事们有点接受不了。有的同事甚至开始有意回避小钱。你认为新人小钱在工作中犯了哪种错误？",options:[{name:"A",text:"没有提前了解企业的文化特点 "},{name:"B",text:"没有把握好人际关系相处的度 "},{name:"C",text:"在工作中过多地投入了个人情感 "},{name:"D",text:"以上说法都不对"}]};
			 		showQuestion(jsonQuestion,2613);
				</script>
            </ul>
            <ul class="fr mr23" style="margin-top:70px;">
            	<span class="fs30 col_red" style="display:none;" id="span_right_2613">√</span>
            	<span class="fs30 col_red" style="display:block;" id="span_wrong_2613">x</span>
            </ul>
            <div class="clear"></div>
            </div>
                        <div>
            <ul class="mt30 fl">
                <li class="ks_t_xh">50</li>
                <li class="ks_tm mb10"  id="2658"></li>
                <div class="clear"></div>
                <div id="option2658"></div>
                <p class="tm_xx">
                	正确答案:<span style="color: red;padding-left: 10px" id="correctAnswer_2658">A</span>
                </p>
                <script type="text/javascript">
					var jsonQuestion={title:"小陈毕业之后顺利进入一家外贸公司，专业对口，业务熟练。由于老板比较重视年轻的员工，小陈便时常向老板提出自己对公司的看法和建议，并在业务上取得了一定的成绩，受到了老板的赞赏。飘飘然的小陈开始觉得公司已经离不开他这个得力干将了。于是他对出错的同事，会毫不留情的批评，有时甚至不请示老板自己做决定；开会的时候也时不时抢话，炫耀自己的功绩。一年后，老板把他解雇了。这说明了什么道理，表述最准确的是：",options:[{name:"A",text:"努力工作，适当表现是必须的，但是越俎代庖，居功自傲是职场大忌"},{name:"B",text:"给老板打工，一定要了解老板的脾气秉性，不能和老板对着干"},{name:"C",text:"小陈对自己对同事要求严格，却得不到认可，小陈应该辞职"},{name:"D",text:"以上说法都正确"}]};
			 		showQuestion(jsonQuestion,2658);
				</script>
            </ul>
            <ul class="fr mr23" style="margin-top:70px;">
            	<span class="fs30 col_red" style="display:none;" id="span_right_2658">√</span>
            	<span class="fs30 col_red" style="display:block;" id="span_wrong_2658">x</span>
            </ul>
            <div class="clear"></div>
            </div>
                        <div>
            <ul class="mt30 fl">
                <li class="ks_t_xh">51</li>
                <li class="ks_tm mb10"  id="2638"></li>
                <div class="clear"></div>
                <div id="option2638"></div>
                <p class="tm_xx">
                	正确答案:<span style="color: red;padding-left: 10px" id="correctAnswer_2638">A</span>
                </p>
                <script type="text/javascript">
					var jsonQuestion={title:"有不少初涉职场者被告诫：保持“独特个性”，无论是在求职还是在职业发展上都能有“先声夺人”的优势。而事实上，一些没有多少个性的人在职场中也能如鱼得水，获得成功。对此，以下说法正确的是：",options:[{name:"A",text:"“个性”与“无个性”，是辨证统一的，从某个层面上讲，“无个性”也是个性 "},{name:"B",text:"“有个性”不利于建立良好的人际关系 "},{name:"C",text:"“无个性”本质上就是无原则，这种人亲和力强 "},{name:"D",text:"“独特个性”不利于在职场中获得良好的发展机会"}]};
			 		showQuestion(jsonQuestion,2638);
				</script>
            </ul>
            <ul class="fr mr23" style="margin-top:70px;">
            	<span class="fs30 col_red" style="display:none;" id="span_right_2638">√</span>
            	<span class="fs30 col_red" style="display:block;" id="span_wrong_2638">x</span>
            </ul>
            <div class="clear"></div>
            </div>
                        <div>
            <ul class="mt30 fl">
                <li class="ks_t_xh">52</li>
                <li class="ks_tm mb10"  id="2603"></li>
                <div class="clear"></div>
                <div id="option2603"></div>
                <p class="tm_xx">
                	正确答案:<span style="color: red;padding-left: 10px" id="correctAnswer_2603">D</span>
                </p>
                <script type="text/javascript">
					var jsonQuestion={title:"有些刚步入职场的新人常常会觉得：“我多说话，别人就会认为我爱出风头”，“我做那件事，别人会嘲笑我”……这种“别人”式的想法使之成为“别人”思维的奴隶。如果职场人有了这种 “心理奴隶”的倾向或表现，应怎样调整？以下说法正确的是：",options:[{name:"A",text:"如果在模仿他人之后能感觉到快乐，不妨尽力去模仿，否则，按自己的方式去生活 "},{name:"B",text:"理智地面对别人的另眼相看、批评指责 "},{name:"C",text:"与敢作敢为、乐于助人、志同道合的人做朋友 "},{name:"D",text:"以上都对"}]};
			 		showQuestion(jsonQuestion,2603);
				</script>
            </ul>
            <ul class="fr mr23" style="margin-top:70px;">
            	<span class="fs30 col_red" style="display:none;" id="span_right_2603">√</span>
            	<span class="fs30 col_red" style="display:block;" id="span_wrong_2603">x</span>
            </ul>
            <div class="clear"></div>
            </div>
                        <div>
            <ul class="mt30 fl">
                <li class="ks_t_xh">53</li>
                <li class="ks_tm mb10"  id="2608"></li>
                <div class="clear"></div>
                <div id="option2608"></div>
                <p class="tm_xx">
                	正确答案:<span style="color: red;padding-left: 10px" id="correctAnswer_2608">A</span>
                </p>
                <script type="text/javascript">
					var jsonQuestion={title:"刚参加工作的大学生在和自己同学交流的过程中，很多人都表现出对目前工作的不满和对别人工作的羡慕。当出现这种浮躁心态的时候，应该学会站在企业和社会现实的角度去考虑一些问题。这一说法，你认为：",options:[{name:"A",text:"正确 "},{name:"B",text:"错误"}]};
			 		showQuestion(jsonQuestion,2608);
				</script>
            </ul>
            <ul class="fr mr23" style="margin-top:70px;">
            	<span class="fs30 col_red" style="display:none;" id="span_right_2608">√</span>
            	<span class="fs30 col_red" style="display:block;" id="span_wrong_2608">x</span>
            </ul>
            <div class="clear"></div>
            </div>
                        <div>
            <ul class="mt30 fl">
                <li class="ks_t_xh">54</li>
                <li class="ks_tm mb10"  id="2612"></li>
                <div class="clear"></div>
                <div id="option2612"></div>
                <p class="tm_xx">
                	正确答案:<span style="color: red;padding-left: 10px" id="correctAnswer_2612">B</span>
                </p>
                <script type="text/javascript">
					var jsonQuestion={title:"春秋战国时期，有位夫子备了很多物品，欲前往南方楚国，便向路人问路。路人答：此路非往楚国。夫子说：我的马很壮，没关系。路人又再强调这不是去楚国的方向，夫子依然固执的说：我的车很坚固。路人只好叹息的说：这不是往楚国的方向啊!方向错误，再怎么努力都枉然。这个典故对职场能力提升有怎样的启示？",options:[{name:"A",text:"工作中需要好的领导和指引者 "},{name:"B",text:"明确工作的重点和方向，不走冤枉路 "},{name:"C",text:"多参与工作实践，才不至于纸上谈兵 "},{name:"D",text:"以上都不对"}]};
			 		showQuestion(jsonQuestion,2612);
				</script>
            </ul>
            <ul class="fr mr23" style="margin-top:70px;">
            	<span class="fs30 col_red" style="display:none;" id="span_right_2612">√</span>
            	<span class="fs30 col_red" style="display:block;" id="span_wrong_2612">x</span>
            </ul>
            <div class="clear"></div>
            </div>
                        <div>
            <ul class="mt30 fl">
                <li class="ks_t_xh">55</li>
                <li class="ks_tm mb10"  id="2619"></li>
                <div class="clear"></div>
                <div id="option2619"></div>
                <p class="tm_xx">
                	正确答案:<span style="color: red;padding-left: 10px" id="correctAnswer_2619">B</span>
                </p>
                <script type="text/javascript">
					var jsonQuestion={title:"公司的非直接上级（在特殊情况下）指令传至本岗时，也要坚决执行，但尽量不要向自己的直接上级汇报、反馈，以避免可能的矛盾。这一说法，你认为：",options:[{name:"A",text:"正确 "},{name:"B",text:"错误"}]};
			 		showQuestion(jsonQuestion,2619);
				</script>
            </ul>
            <ul class="fr mr23" style="margin-top:70px;">
            	<span class="fs30 col_red" style="display:none;" id="span_right_2619">√</span>
            	<span class="fs30 col_red" style="display:block;" id="span_wrong_2619">x</span>
            </ul>
            <div class="clear"></div>
            </div>
                        <div>
            <ul class="mt30 fl">
                <li class="ks_t_xh">56</li>
                <li class="ks_tm mb10"  id="2593"></li>
                <div class="clear"></div>
                <div id="option2593"></div>
                <p class="tm_xx">
                	正确答案:<span style="color: red;padding-left: 10px" id="correctAnswer_2593">C</span>
                </p>
                <script type="text/javascript">
					var jsonQuestion={title:"人际交往中，“别人希望你怎样对待他们，你就怎样对待他们”的法则，被称为（ ）。",options:[{name:"A",text:"黄金法则 "},{name:"B",text:"交换法则 "},{name:"C",text:"白金法则 "},{name:"D",text:"对等法则"}]};
			 		showQuestion(jsonQuestion,2593);
				</script>
            </ul>
            <ul class="fr mr23" style="margin-top:70px;">
            	<span class="fs30 col_red" style="display:none;" id="span_right_2593">√</span>
            	<span class="fs30 col_red" style="display:block;" id="span_wrong_2593">x</span>
            </ul>
            <div class="clear"></div>
            </div>
                        <div>
            <ul class="mt30 fl">
                <li class="ks_t_xh">57</li>
                <li class="ks_tm mb10"  id="2635"></li>
                <div class="clear"></div>
                <div id="option2635"></div>
                <p class="tm_xx">
                	正确答案:<span style="color: red;padding-left: 10px" id="correctAnswer_2635">B</span>
                </p>
                <script type="text/javascript">
					var jsonQuestion={title:"大学生到新单位后，首先要合群，努力使自己融入新的集体当中，尤其要学会察言观色，建立自己的小团体或是加入别人的小圈子。请判断这一说法的正误。",options:[{name:"A",text:"正确 "},{name:"B",text:"错误"}]};
			 		showQuestion(jsonQuestion,2635);
				</script>
            </ul>
            <ul class="fr mr23" style="margin-top:70px;">
            	<span class="fs30 col_red" style="display:none;" id="span_right_2635">√</span>
            	<span class="fs30 col_red" style="display:block;" id="span_wrong_2635">x</span>
            </ul>
            <div class="clear"></div>
            </div>
                        <div>
            <ul class="mt30 fl">
                <li class="ks_t_xh">58</li>
                <li class="ks_tm mb10"  id="2652"></li>
                <div class="clear"></div>
                <div id="option2652"></div>
                <p class="tm_xx">
                	正确答案:<span style="color: red;padding-left: 10px" id="correctAnswer_2652">A</span>
                </p>
                <script type="text/javascript">
					var jsonQuestion={title:"关于初入职场的禁忌，下列组合哪项是正确的：①马虎大意，缺乏责任心  ②目中无人，唯我独尊  ③团队合作，乐于奉献  ④好高骛远，居功自傲  ⑤重视纪律，严于律己  ⑥自私自利，自以为是  ⑦纸上谈兵，夸夸其谈  ⑧特立独行，指手画脚",options:[{name:"A",text:"①②⑥ "},{name:"B",text:"③⑥⑧ "},{name:"C",text:"④⑤⑦ "},{name:"D",text:"②③⑤"}]};
			 		showQuestion(jsonQuestion,2652);
				</script>
            </ul>
            <ul class="fr mr23" style="margin-top:70px;">
            	<span class="fs30 col_red" style="display:none;" id="span_right_2652">√</span>
            	<span class="fs30 col_red" style="display:block;" id="span_wrong_2652">x</span>
            </ul>
            <div class="clear"></div>
            </div>
                        <div>
            <ul class="mt30 fl">
                <li class="ks_t_xh">59</li>
                <li class="ks_tm mb10"  id="2591"></li>
                <div class="clear"></div>
                <div id="option2591"></div>
                <p class="tm_xx">
                	正确答案:<span style="color: red;padding-left: 10px" id="correctAnswer_2591">B</span>
                </p>
                <script type="text/javascript">
					var jsonQuestion={title:"赫茨伯格的双因素理论把影响员工满意度的工作环境或工作方面的因素称之为：",options:[{name:"A",text:"激励因素"},{name:"B",text:"保健因素"},{name:"C",text:"不满意因素"},{name:"D",text:"满意因素"}]};
			 		showQuestion(jsonQuestion,2591);
				</script>
            </ul>
            <ul class="fr mr23" style="margin-top:70px;">
            	<span class="fs30 col_red" style="display:none;" id="span_right_2591">√</span>
            	<span class="fs30 col_red" style="display:block;" id="span_wrong_2591">x</span>
            </ul>
            <div class="clear"></div>
            </div>
                        <div>
            <ul class="mt30 fl">
                <li class="ks_t_xh">60</li>
                <li class="ks_tm mb10"  id="2618"></li>
                <div class="clear"></div>
                <div id="option2618"></div>
                <p class="tm_xx">
                	正确答案:<span style="color: red;padding-left: 10px" id="correctAnswer_2618">B</span>
                </p>
                <script type="text/javascript">
					var jsonQuestion={title:"新人入职，要以强烈的责任心对待单位的生存和发展问题，提出合理的建议，对改进本部门工作效率的问题，可以向自己的直接或非直接上级领导进言。这一说法，你认为：",options:[{name:"A",text:"正确 "},{name:"B",text:"错误"}]};
			 		showQuestion(jsonQuestion,2618);
				</script>
            </ul>
            <ul class="fr mr23" style="margin-top:70px;">
            	<span class="fs30 col_red" style="display:none;" id="span_right_2618">√</span>
            	<span class="fs30 col_red" style="display:block;" id="span_wrong_2618">x</span>
            </ul>
            <div class="clear"></div>
            </div>
                        <div>
            <ul class="mt30 fl">
                <li class="ks_t_xh">61</li>
                <li class="ks_tm mb10"  id="2596"></li>
                <div class="clear"></div>
                <div id="option2596"></div>
                <p class="tm_xx">
                	正确答案:<span style="color: red;padding-left: 10px" id="correctAnswer_2596">D</span>
                </p>
                <script type="text/javascript">
					var jsonQuestion={title:"从校园人到职业人的转变，是大学生人生道路上的转折点，这种转变过程中，最重要的是实现（ ）转换。",options:[{name:"A",text:"观念 "},{name:"B",text:"态度 "},{name:"C",text:"情绪 "},{name:"D",text:"角色"}]};
			 		showQuestion(jsonQuestion,2596);
				</script>
            </ul>
            <ul class="fr mr23" style="margin-top:70px;">
            	<span class="fs30 col_red" style="display:none;" id="span_right_2596">√</span>
            	<span class="fs30 col_red" style="display:block;" id="span_wrong_2596">x</span>
            </ul>
            <div class="clear"></div>
            </div>
                        <div>
            <ul class="mt30 fl">
                <li class="ks_t_xh">62</li>
                <li class="ks_tm mb10"  id="2594"></li>
                <div class="clear"></div>
                <div id="option2594"></div>
                <p class="tm_xx">
                	正确答案:<span style="color: red;padding-left: 10px" id="correctAnswer_2594">B</span>
                </p>
                <script type="text/javascript">
					var jsonQuestion={title:"团队是由员工和管理层组成的一个共同体，该共同体合理利用每一个成员的知识和技能协同工作，解决问题，从而（ ）。",options:[{name:"A",text:"创造经济收入 "},{name:"B",text:"达到共同目标 "},{name:"C",text:"提升团队竞争力 "},{name:"D",text:"改善组织环境"}]};
			 		showQuestion(jsonQuestion,2594);
				</script>
            </ul>
            <ul class="fr mr23" style="margin-top:70px;">
            	<span class="fs30 col_red" style="display:none;" id="span_right_2594">√</span>
            	<span class="fs30 col_red" style="display:block;" id="span_wrong_2594">x</span>
            </ul>
            <div class="clear"></div>
            </div>
                        <div>
            <ul class="mt30 fl">
                <li class="ks_t_xh">63</li>
                <li class="ks_tm mb10"  id="2640"></li>
                <div class="clear"></div>
                <div id="option2640"></div>
                <p class="tm_xx">
                	正确答案:<span style="color: red;padding-left: 10px" id="correctAnswer_2640">D</span>
                </p>
                <script type="text/javascript">
					var jsonQuestion={title:"学生到职业人需要怎样的转变，以下说法中错误的是：",options:[{name:"A",text:"思想转变，协调职业理想与现实的矛盾，提高责任意识与自主意识"},{name:"B",text:"角色转变，迈好职场第一步，建立良好的第一印象，上好第一班岗"},{name:"C",text:"人际关系转变，建立和谐的人际关系，注重人脉资源的积累"},{name:"D",text:"只有B和C正确"}]};
			 		showQuestion(jsonQuestion,2640);
				</script>
            </ul>
            <ul class="fr mr23" style="margin-top:70px;">
            	<span class="fs30 col_red" style="display:none;" id="span_right_2640">√</span>
            	<span class="fs30 col_red" style="display:block;" id="span_wrong_2640">x</span>
            </ul>
            <div class="clear"></div>
            </div>
                        <div>
            <ul class="mt30 fl">
                <li class="ks_t_xh">64</li>
                <li class="ks_tm mb10"  id="2622"></li>
                <div class="clear"></div>
                <div id="option2622"></div>
                <p class="tm_xx">
                	正确答案:<span style="color: red;padding-left: 10px" id="correctAnswer_2622">A</span>
                </p>
                <script type="text/javascript">
					var jsonQuestion={title:"职场冷暴力，一般指上司或群体用非暴力的方式刺激对方，致使一方或多方心灵受到严重伤害。它主要体现在让人长期饱受漠视、讥讽，甚至于不能日常工作等。你认为职场中应怎样化解这种冷暴力，请选出下列做法中错误的一项：",options:[{name:"A",text:"“以冷制冷”，加强反击 "},{name:"B",text:"换位思考，理解上司和同事 "},{name:"C",text:"增强自身“免疫力”，培养豁达乐观的个性 "},{name:"D",text:"积极正面理解问题，把想法大胆说出来"}]};
			 		showQuestion(jsonQuestion,2622);
				</script>
            </ul>
            <ul class="fr mr23" style="margin-top:70px;">
            	<span class="fs30 col_red" style="display:none;" id="span_right_2622">√</span>
            	<span class="fs30 col_red" style="display:block;" id="span_wrong_2622">x</span>
            </ul>
            <div class="clear"></div>
            </div>
                        <div>
            <ul class="mt30 fl">
                <li class="ks_t_xh">65</li>
                <li class="ks_tm mb10"  id="2660"></li>
                <div class="clear"></div>
                <div id="option2660"></div>
                <p class="tm_xx">
                	正确答案:<span style="color: red;padding-left: 10px" id="correctAnswer_2660">D</span>
                </p>
                <script type="text/javascript">
					var jsonQuestion={title:"小明工作之后经常抱怨：自己几个月来每天的工作就是给其他同事轮流当学徒工，工作成绩却都记在别人身上；给领导办事，费用却不能报销；自己的工资没有中专生高；自己的领导死脑筋，不会周旋等等。结果他说的这些话传到领导耳朵里，多次遭受领导含沙射影的批评。这说明了什么道理，表述最准确的是：",options:[{name:"A",text:"小明不应该当着同事抱怨，应该找主管领导说明 "},{name:"B",text:"小明的行为是幼稚的表现，不应该随便相信同事 "},{name:"C",text:"小明的领导太小气，小明应该辞职 "},{name:"D",text:"刚到单位，从学徒工干起是正常的，如果事事斤斤计较，就会祸从口出，得不偿失"}]};
			 		showQuestion(jsonQuestion,2660);
				</script>
            </ul>
            <ul class="fr mr23" style="margin-top:70px;">
            	<span class="fs30 col_red" style="display:none;" id="span_right_2660">√</span>
            	<span class="fs30 col_red" style="display:block;" id="span_wrong_2660">x</span>
            </ul>
            <div class="clear"></div>
            </div>
                        <div>
            <ul class="mt30 fl">
                <li class="ks_t_xh">66</li>
                <li class="ks_tm mb10"  id="2610"></li>
                <div class="clear"></div>
                <div id="option2610"></div>
                <p class="tm_xx">
                	正确答案:<span style="color: red;padding-left: 10px" id="correctAnswer_2610">C</span>
                </p>
                <script type="text/javascript">
					var jsonQuestion={title:"孙小明刚进公司做计划部主管时，除了工资，就没享受过另类待遇。一个偶然的机会她得知行政主管赵平的手机费竟实报实销，这让她很不服气！于是孙小明借汇报工作之机向老板提出申请，老板听了很惊讶，说后勤人员不是都没有通讯费吗？“可是赵平就有呀！”老板听了沉吟道：“是吗？我了解一下再说。”这一了解就是两个月，见老板没动静，孙小明又生气又愤恨，终于忍不住和同事抱怨，却被人家一语道破天机：“你知道赵平的手机费是怎么回事？那是老板小秘的电话，只不过借了一下赵平的名字。”孙小明吓出一身冷汗，暗暗自责不懂高低深浅！这个职场案例告诉我们怎样的道理？",options:[{name:"A",text:"工作中要避开上司的软肋，否则将得不到赏识 "},{name:"B",text:"工作中人际关系的复杂程度不是我们所能想象的，应步步小心 "},{name:"C",text:"工作中不要苛求百分百的公平，有些表象，不一定能成为申诉的理由 "},{name:"D",text:"以上说法都不对"}]};
			 		showQuestion(jsonQuestion,2610);
				</script>
            </ul>
            <ul class="fr mr23" style="margin-top:70px;">
            	<span class="fs30 col_red" style="display:none;" id="span_right_2610">√</span>
            	<span class="fs30 col_red" style="display:block;" id="span_wrong_2610">x</span>
            </ul>
            <div class="clear"></div>
            </div>
                        <div>
            <ul class="mt30 fl">
                <li class="ks_t_xh">67</li>
                <li class="ks_tm mb10"  id="2595"></li>
                <div class="clear"></div>
                <div id="option2595"></div>
                <p class="tm_xx">
                	正确答案:<span style="color: red;padding-left: 10px" id="correctAnswer_2595">B</span>
                </p>
                <script type="text/javascript">
					var jsonQuestion={title:"循序渐进，由易至难，独立思考，从而迅速得到结论的处理难题的思维模式，称为（ ）思维。",options:[{name:"A",text:"纳米 "},{name:"B",text:"费米 "},{name:"C",text:"渐进 "},{name:"D",text:"归纳"}]};
			 		showQuestion(jsonQuestion,2595);
				</script>
            </ul>
            <ul class="fr mr23" style="margin-top:70px;">
            	<span class="fs30 col_red" style="display:none;" id="span_right_2595">√</span>
            	<span class="fs30 col_red" style="display:block;" id="span_wrong_2595">x</span>
            </ul>
            <div class="clear"></div>
            </div>
                        <div>
            <ul class="mt30 fl">
                <li class="ks_t_xh">68</li>
                <li class="ks_tm mb10"  id="2647"></li>
                <div class="clear"></div>
                <div id="option2647"></div>
                <p class="tm_xx">
                	正确答案:<span style="color: red;padding-left: 10px" id="correctAnswer_2647">D</span>
                </p>
                <script type="text/javascript">
					var jsonQuestion={title:"初入职场，同事之间的是非，不可不信，也不可全信，对职场纷争一无所知的时候，不能盲目发表意见，应该保持（ ）立场。",options:[{name:"A",text:"同情 "},{name:"B",text:"上司 "},{name:"C",text:"下属 "},{name:"D",text:"中立"}]};
			 		showQuestion(jsonQuestion,2647);
				</script>
            </ul>
            <ul class="fr mr23" style="margin-top:70px;">
            	<span class="fs30 col_red" style="display:none;" id="span_right_2647">√</span>
            	<span class="fs30 col_red" style="display:block;" id="span_wrong_2647">x</span>
            </ul>
            <div class="clear"></div>
            </div>
                        <div>
            <ul class="mt30 fl">
                <li class="ks_t_xh">69</li>
                <li class="ks_tm mb10"  id="2649"></li>
                <div class="clear"></div>
                <div id="option2649"></div>
                <p class="tm_xx">
                	正确答案:<span style="color: red;padding-left: 10px" id="correctAnswer_2649">A</span>
                </p>
                <script type="text/javascript">
					var jsonQuestion={title:"初入职场的女大学生往往是弱势群体。女大学生应该如何应对职场挑战？下列表述不正确的是：",options:[{name:"A",text:"干得好不如嫁得好，应该及早找到职场靠山 "},{name:"B",text:"努力融入团队，证明自己的价值，但不要拉帮结派 "},{name:"C",text:"面对歧视时，不要自暴自弃，要相信自己，敢于承担责任 "},{name:"D",text:"遭遇骚扰时，也不宜过分懦弱，要学会自我保护"}]};
			 		showQuestion(jsonQuestion,2649);
				</script>
            </ul>
            <ul class="fr mr23" style="margin-top:70px;">
            	<span class="fs30 col_red" style="display:none;" id="span_right_2649">√</span>
            	<span class="fs30 col_red" style="display:block;" id="span_wrong_2649">x</span>
            </ul>
            <div class="clear"></div>
            </div>
                        <div>
            <ul class="mt30 fl">
                <li class="ks_t_xh">70</li>
                <li class="ks_tm mb10"  id="2670"></li>
                <div class="clear"></div>
                <div id="option2670"></div>
                <p class="tm_xx">
                	正确答案:<span style="color: red;padding-left: 10px" id="correctAnswer_2670">D</span>
                </p>
                <script type="text/javascript">
					var jsonQuestion={title:" 团队与群体不同，群体可能只是一群乌合之众，而团队必须具备高度的战斗能力，为此，团队需要满足一些条件。以下不属于团队必要条件的是？",options:[{name:"A",text:"自主性 "},{name:"B",text:"思考性 "},{name:"C",text:"合作性 "},{name:"D",text:"一致性"}]};
			 		showQuestion(jsonQuestion,2670);
				</script>
            </ul>
            <ul class="fr mr23" style="margin-top:70px;">
            	<span class="fs30 col_red" style="display:none;" id="span_right_2670">√</span>
            	<span class="fs30 col_red" style="display:block;" id="span_wrong_2670">x</span>
            </ul>
            <div class="clear"></div>
            </div>
                        <div>
            <ul class="mt30 fl">
                <li class="ks_t_xh">71</li>
                <li class="ks_tm mb10"  id="2722"></li>
                <div class="clear"></div>
                <div id="option2722"></div>
                <p class="tm_xx">
                	正确答案:<span style="color: red;padding-left: 10px" id="correctAnswer_2722">A</span>
                </p>
                <script type="text/javascript">
					var jsonQuestion={title:"小李的工作表现一直不错，但是最近他老是闷闷不乐，团队主管与他进行了一次交谈，原来是他的家中出现了一些问题。主管帮他解决了问题，小李的工作积极性又提高了。这种情况说明团队成员和团队管理者之间:",options:[{name:"A",text:"及时沟通的重要性 "},{name:"B",text:"相互理解的重要性 "},{name:"C",text:"相互信任的重要性 "},{name:"D",text:"平等的重要性"}]};
			 		showQuestion(jsonQuestion,2722);
				</script>
            </ul>
            <ul class="fr mr23" style="margin-top:70px;">
            	<span class="fs30 col_red" style="display:none;" id="span_right_2722">√</span>
            	<span class="fs30 col_red" style="display:block;" id="span_wrong_2722">x</span>
            </ul>
            <div class="clear"></div>
            </div>
                        <div>
            <ul class="mt30 fl">
                <li class="ks_t_xh">72</li>
                <li class="ks_tm mb10"  id="2683"></li>
                <div class="clear"></div>
                <div id="option2683"></div>
                <p class="tm_xx">
                	正确答案:<span style="color: red;padding-left: 10px" id="correctAnswer_2683">D</span>
                </p>
                <script type="text/javascript">
					var jsonQuestion={title:"关于如何培养职场中的创新意识，以下说法错误的是：",options:[{name:"A",text:"学会对已知信息进行选择、重新整合、转化并作出预测 "},{name:"B",text:"不断学习新的职业技能 "},{name:"C",text:"保持信息畅通 "},{name:"D",text:"认真落实各项工作任务"}]};
			 		showQuestion(jsonQuestion,2683);
				</script>
            </ul>
            <ul class="fr mr23" style="margin-top:70px;">
            	<span class="fs30 col_red" style="display:none;" id="span_right_2683">√</span>
            	<span class="fs30 col_red" style="display:block;" id="span_wrong_2683">x</span>
            </ul>
            <div class="clear"></div>
            </div>
                        <div>
            <ul class="mt30 fl">
                <li class="ks_t_xh">73</li>
                <li class="ks_tm mb10"  id="3221"></li>
                <div class="clear"></div>
                <div id="option3221"></div>
                <p class="tm_xx">
                	正确答案:<span style="color: red;padding-left: 10px" id="correctAnswer_3221">A</span>
                </p>
                <script type="text/javascript">
					var jsonQuestion={title:"以下哪项不属于中华传统伦理中的荣辱观？",options:[{name:"A",text:"有志者，事竟成 "},{name:"B",text:"宁可毁人，不可毁誉 "},{name:"C",text:"宁可穷而有志，不可富而失节 "},{name:"D",text:"仓廪实而知礼节，衣食足而知荣辱"}]};
			 		showQuestion(jsonQuestion,3221);
				</script>
            </ul>
            <ul class="fr mr23" style="margin-top:70px;">
            	<span class="fs30 col_red" style="display:none;" id="span_right_3221">√</span>
            	<span class="fs30 col_red" style="display:block;" id="span_wrong_3221">x</span>
            </ul>
            <div class="clear"></div>
            </div>
                        <div>
            <ul class="mt30 fl">
                <li class="ks_t_xh">74</li>
                <li class="ks_tm mb10"  id="2691"></li>
                <div class="clear"></div>
                <div id="option2691"></div>
                <p class="tm_xx">
                	正确答案:<span style="color: red;padding-left: 10px" id="correctAnswer_2691">D</span>
                </p>
                <script type="text/javascript">
					var jsonQuestion={title:"工作中，怎样培养自我激励的情绪，高效地达成工作目标？以下说法正确的是：",options:[{name:"A",text:"以工作成就作为驱动力，不断改进 "},{name:"B",text:"主动抓住机会，定立超过别人要求的目标 "},{name:"C",text:"保持乐观心态，把失败视做可控制的情况，而不是个人失误 "},{name:"D",text:"以上都对"}]};
			 		showQuestion(jsonQuestion,2691);
				</script>
            </ul>
            <ul class="fr mr23" style="margin-top:70px;">
            	<span class="fs30 col_red" style="display:none;" id="span_right_2691">√</span>
            	<span class="fs30 col_red" style="display:block;" id="span_wrong_2691">x</span>
            </ul>
            <div class="clear"></div>
            </div>
                        <div>
            <ul class="mt30 fl">
                <li class="ks_t_xh">75</li>
                <li class="ks_tm mb10"  id="3230"></li>
                <div class="clear"></div>
                <div id="option3230"></div>
                <p class="tm_xx">
                	正确答案:<span style="color: red;padding-left: 10px" id="correctAnswer_3230">A</span>
                </p>
                <script type="text/javascript">
					var jsonQuestion={title:"作为企业的一线执行者，应当树立客户意识，建立严格的工作标准，以事为本，追求细节，自觉自发的工作。你认为这一说法：",options:[{name:"A",text:"正确 "},{name:"B",text:"错误"}]};
			 		showQuestion(jsonQuestion,3230);
				</script>
            </ul>
            <ul class="fr mr23" style="margin-top:70px;">
            	<span class="fs30 col_red" style="display:none;" id="span_right_3230">√</span>
            	<span class="fs30 col_red" style="display:block;" id="span_wrong_3230">x</span>
            </ul>
            <div class="clear"></div>
            </div>
                        <div>
            <ul class="mt30 fl">
                <li class="ks_t_xh">76</li>
                <li class="ks_tm mb10"  id="2676"></li>
                <div class="clear"></div>
                <div id="option2676"></div>
                <p class="tm_xx">
                	正确答案:<span style="color: red;padding-left: 10px" id="correctAnswer_2676">D</span>
                </p>
                <script type="text/javascript">
					var jsonQuestion={title:"素质分为自然素质、心理素质、社会素质。关于这三种素质，下列说法正确的是：",options:[{name:"A",text:"自然素质，亦称生理素质或身体素质，是后天培养的 "},{name:"B",text:"心理素质以社会素质为基础，是在后天环境、教育、实践活动诸因素的影响下一次形成的，是先天因素和后天因素的合金 "},{name:"C",text:"社会素质是人们社会属性的集中体现，主要是先天形成的 "},{name:"D",text:"以上说法都不正确"}]};
			 		showQuestion(jsonQuestion,2676);
				</script>
            </ul>
            <ul class="fr mr23" style="margin-top:70px;">
            	<span class="fs30 col_red" style="display:none;" id="span_right_2676">√</span>
            	<span class="fs30 col_red" style="display:block;" id="span_wrong_2676">x</span>
            </ul>
            <div class="clear"></div>
            </div>
                        <div>
            <ul class="mt30 fl">
                <li class="ks_t_xh">77</li>
                <li class="ks_tm mb10"  id="3202"></li>
                <div class="clear"></div>
                <div id="option3202"></div>
                <p class="tm_xx">
                	正确答案:<span style="color: red;padding-left: 10px" id="correctAnswer_3202">C</span>
                </p>
                <script type="text/javascript">
					var jsonQuestion={title:"有效的工作行为包括以下哪些：①明确工作任务 ②合理制定计划 ③充分利用资源 ④及时进行沟通 ⑤分散工作重点 ⑥善于总结经验",options:[{name:"A",text:"①②④⑥"},{name:"B",text:"②③④⑤⑥"},{name:"C",text:"①②③④⑥"},{name:"D",text:"①②③④⑤⑥"}]};
			 		showQuestion(jsonQuestion,3202);
				</script>
            </ul>
            <ul class="fr mr23" style="margin-top:70px;">
            	<span class="fs30 col_red" style="display:none;" id="span_right_3202">√</span>
            	<span class="fs30 col_red" style="display:block;" id="span_wrong_3202">x</span>
            </ul>
            <div class="clear"></div>
            </div>
                        <div>
            <ul class="mt30 fl">
                <li class="ks_t_xh">78</li>
                <li class="ks_tm mb10"  id="2706"></li>
                <div class="clear"></div>
                <div id="option2706"></div>
                <p class="tm_xx">
                	正确答案:<span style="color: red;padding-left: 10px" id="correctAnswer_2706">D</span>
                </p>
                <script type="text/javascript">
					var jsonQuestion={title:"关于职业素质，下列说法正确的是：",options:[{name:"A",text:"职业素质是劳动者在一定的生理和心理条件的基础上，通过教育、劳动实践和自我修养等途径而形成和发展起来的 "},{name:"B",text:"职业素质是在职业活动中发挥重要作用的内在基本品质 "},{name:"C",text:"职业素质的特征：职业性、稳定性、内在性、整体性、发展性 "},{name:"D",text:"以上说法都正确"}]};
			 		showQuestion(jsonQuestion,2706);
				</script>
            </ul>
            <ul class="fr mr23" style="margin-top:70px;">
            	<span class="fs30 col_red" style="display:none;" id="span_right_2706">√</span>
            	<span class="fs30 col_red" style="display:block;" id="span_wrong_2706">x</span>
            </ul>
            <div class="clear"></div>
            </div>
                        <div>
            <ul class="mt30 fl">
                <li class="ks_t_xh">79</li>
                <li class="ks_tm mb10"  id="3235"></li>
                <div class="clear"></div>
                <div id="option3235"></div>
                <p class="tm_xx">
                	正确答案:<span style="color: red;padding-left: 10px" id="correctAnswer_3235">B</span>
                </p>
                <script type="text/javascript">
					var jsonQuestion={title:"个体执行力的四个核心要素包括（ ）、工具、角色和流程。",options:[{name:"A",text:"智力 "},{name:"B",text:"心态 "},{name:"C",text:"体力 "},{name:"D",text:"知识"}]};
			 		showQuestion(jsonQuestion,3235);
				</script>
            </ul>
            <ul class="fr mr23" style="margin-top:70px;">
            	<span class="fs30 col_red" style="display:none;" id="span_right_3235">√</span>
            	<span class="fs30 col_red" style="display:block;" id="span_wrong_3235">x</span>
            </ul>
            <div class="clear"></div>
            </div>
                        <div>
            <ul class="mt30 fl">
                <li class="ks_t_xh">80</li>
                <li class="ks_tm mb10"  id="3192"></li>
                <div class="clear"></div>
                <div id="option3192"></div>
                <p class="tm_xx">
                	正确答案:<span style="color: red;padding-left: 10px" id="correctAnswer_3192">A</span>
                </p>
                <script type="text/javascript">
					var jsonQuestion={title:"职业成功的影响因素因发展路线不同而不同。你认为这种说法：",options:[{name:"A",text:"正确 "},{name:"B",text:"错误"}]};
			 		showQuestion(jsonQuestion,3192);
				</script>
            </ul>
            <ul class="fr mr23" style="margin-top:70px;">
            	<span class="fs30 col_red" style="display:none;" id="span_right_3192">√</span>
            	<span class="fs30 col_red" style="display:block;" id="span_wrong_3192">x</span>
            </ul>
            <div class="clear"></div>
            </div>
                        <div>
            <ul class="mt30 fl">
                <li class="ks_t_xh">81</li>
                <li class="ks_tm mb10"  id="2712"></li>
                <div class="clear"></div>
                <div id="option2712"></div>
                <p class="tm_xx">
                	正确答案:<span style="color: red;padding-left: 10px" id="correctAnswer_2712">A</span>
                </p>
                <script type="text/javascript">
					var jsonQuestion={title:"关于职场成功的忌讳，选项中组合正确的是：①办事拖拉 ②准备不足 ③坚持到底 ④不吸取教训 ⑤有能力，有魅力 ⑥老好人 ⑦不切实际的幻想 ⑧用人不当",options:[{name:"A",text:"①②⑥ "},{name:"B",text:"③⑥⑧ "},{name:"C",text:"④⑤⑦ "},{name:"D",text:"②③⑤"}]};
			 		showQuestion(jsonQuestion,2712);
				</script>
            </ul>
            <ul class="fr mr23" style="margin-top:70px;">
            	<span class="fs30 col_red" style="display:none;" id="span_right_2712">√</span>
            	<span class="fs30 col_red" style="display:block;" id="span_wrong_2712">x</span>
            </ul>
            <div class="clear"></div>
            </div>
                        <div>
            <ul class="mt30 fl">
                <li class="ks_t_xh">82</li>
                <li class="ks_tm mb10"  id="3210"></li>
                <div class="clear"></div>
                <div id="option3210"></div>
                <p class="tm_xx">
                	正确答案:<span style="color: red;padding-left: 10px" id="correctAnswer_3210">A</span>
                </p>
                <script type="text/javascript">
					var jsonQuestion={title:"下列哪一项属于隐性职业素质？",options:[{name:"A",text:"职业道德 "},{name:"B",text:"职业资质 "},{name:"C",text:"职业行为 "},{name:"D",text:"职业技能"}]};
			 		showQuestion(jsonQuestion,3210);
				</script>
            </ul>
            <ul class="fr mr23" style="margin-top:70px;">
            	<span class="fs30 col_red" style="display:none;" id="span_right_3210">√</span>
            	<span class="fs30 col_red" style="display:block;" id="span_wrong_3210">x</span>
            </ul>
            <div class="clear"></div>
            </div>
                        <div>
            <ul class="mt30 fl">
                <li class="ks_t_xh">83</li>
                <li class="ks_tm mb10"  id="2699"></li>
                <div class="clear"></div>
                <div id="option2699"></div>
                <p class="tm_xx">
                	正确答案:<span style="color: red;padding-left: 10px" id="correctAnswer_2699">B</span>
                </p>
                <script type="text/javascript">
					var jsonQuestion={title:"职业道德是增强企业凝聚力的手段。关于这个观点，下列说法不正确的是：",options:[{name:"A",text:"职业道德是协调职工同事关系的法宝 "},{name:"B",text:"职业道德是一种传统式保守性的思维方式，会束缚员工的思维，使其安稳的工作 "},{name:"C",text:"职业道德有利于协调职工与领导之间的关系 "},{name:"D",text:"职业道德有利于协调职工与企业之间的关系"}]};
			 		showQuestion(jsonQuestion,2699);
				</script>
            </ul>
            <ul class="fr mr23" style="margin-top:70px;">
            	<span class="fs30 col_red" style="display:none;" id="span_right_2699">√</span>
            	<span class="fs30 col_red" style="display:block;" id="span_wrong_2699">x</span>
            </ul>
            <div class="clear"></div>
            </div>
                        <div>
            <ul class="mt30 fl">
                <li class="ks_t_xh">84</li>
                <li class="ks_tm mb10"  id="2682"></li>
                <div class="clear"></div>
                <div id="option2682"></div>
                <p class="tm_xx">
                	正确答案:<span style="color: red;padding-left: 10px" id="correctAnswer_2682">B</span>
                </p>
                <script type="text/javascript">
					var jsonQuestion={title:"某公司的老总对一位前来应聘的毕业生说：“你的文凭代表你应有的文化程度，它的价值会体现在你的底薪上，但有效期只有6个月，要想在我这里发展，就必须学会‘充电’。”根据这段材料，你认为以下说法正确的是：",options:[{name:"A",text:"大学生的文凭决定了求职的成功与否"},{name:"B",text:"学会学习是职场生存的前提"},{name:"C",text:"很多企业持有错误的人才观"},{name:"D",text:"以上说法都不对"}]};
			 		showQuestion(jsonQuestion,2682);
				</script>
            </ul>
            <ul class="fr mr23" style="margin-top:70px;">
            	<span class="fs30 col_red" style="display:none;" id="span_right_2682">√</span>
            	<span class="fs30 col_red" style="display:block;" id="span_wrong_2682">x</span>
            </ul>
            <div class="clear"></div>
            </div>
                        <div>
            <ul class="mt30 fl">
                <li class="ks_t_xh">85</li>
                <li class="ks_tm mb10"  id="2700"></li>
                <div class="clear"></div>
                <div id="option2700"></div>
                <p class="tm_xx">
                	正确答案:<span style="color: red;padding-left: 10px" id="correctAnswer_2700">C</span>
                </p>
                <script type="text/javascript">
					var jsonQuestion={title:"关于职业道德与企业发展的关系，下列说法错误的是：",options:[{name:"A",text:"职业道德是企业文化的一部分 "},{name:"B",text:"职业道德能够提高企业的竞争力和凝聚力 "},{name:"C",text:"在残酷的社会竞争中，职业道德在某些程度上会束缚企业的发展，“道德”会降低企业的竞争力 "},{name:"D",text:"职业道德会对一个人职业化发展起到积极的作用"}]};
			 		showQuestion(jsonQuestion,2700);
				</script>
            </ul>
            <ul class="fr mr23" style="margin-top:70px;">
            	<span class="fs30 col_red" style="display:none;" id="span_right_2700">√</span>
            	<span class="fs30 col_red" style="display:block;" id="span_wrong_2700">x</span>
            </ul>
            <div class="clear"></div>
            </div>
                        <div>
            <ul class="mt30 fl">
                <li class="ks_t_xh">86</li>
                <li class="ks_tm mb10"  id="3189"></li>
                <div class="clear"></div>
                <div id="option3189"></div>
                <p class="tm_xx">
                	正确答案:<span style="color: red;padding-left: 10px" id="correctAnswer_3189">B</span>
                </p>
                <script type="text/javascript">
					var jsonQuestion={title:"下列哪一项不能作为职业成功的评判标准？",options:[{name:"A",text:"发挥个人职业潜力"},{name:"B",text:"工作清闲，不需要努力就能完成"},{name:"C",text:"获得成就感和满足感"},{name:"D",text:"社会或他人从财富、社会地位、名誉等角度给予认可"}]};
			 		showQuestion(jsonQuestion,3189);
				</script>
            </ul>
            <ul class="fr mr23" style="margin-top:70px;">
            	<span class="fs30 col_red" style="display:none;" id="span_right_3189">√</span>
            	<span class="fs30 col_red" style="display:block;" id="span_wrong_3189">x</span>
            </ul>
            <div class="clear"></div>
            </div>
                        <div>
            <ul class="mt30 fl">
                <li class="ks_t_xh">87</li>
                <li class="ks_tm mb10"  id="3238"></li>
                <div class="clear"></div>
                <div id="option3238"></div>
                <p class="tm_xx">
                	正确答案:<span style="color: red;padding-left: 10px" id="correctAnswer_3238">D</span>
                </p>
                <script type="text/javascript">
					var jsonQuestion={title:"中层执行者的职责和心态应该包括哪些：（1）强烈的责任感 （2）担任内部教练，使执行成为团队所有成员的习惯 （3）绩效至上，注重结果 （4）培养问题解决能力，积极主动处理问题",options:[{name:"A",text:"（1）（2）（3） "},{name:"B",text:"（2）（3）（4） "},{name:"C",text:"（1）（3）（4） "},{name:"D",text:"（1）（2）（3）（4）"}]};
			 		showQuestion(jsonQuestion,3238);
				</script>
            </ul>
            <ul class="fr mr23" style="margin-top:70px;">
            	<span class="fs30 col_red" style="display:none;" id="span_right_3238">√</span>
            	<span class="fs30 col_red" style="display:block;" id="span_wrong_3238">x</span>
            </ul>
            <div class="clear"></div>
            </div>
                        <div>
            <ul class="mt30 fl">
                <li class="ks_t_xh">88</li>
                <li class="ks_tm mb10"  id="3215"></li>
                <div class="clear"></div>
                <div id="option3215"></div>
                <p class="tm_xx">
                	正确答案:<span style="color: red;padding-left: 10px" id="correctAnswer_3215">B</span>
                </p>
                <script type="text/javascript">
					var jsonQuestion={title:"在工作的过程中，企业文化只是一个虚设的事物，对于个人而言并不重要。你认为这种说法：",options:[{name:"A",text:"正确 "},{name:"B",text:"错误"}]};
			 		showQuestion(jsonQuestion,3215);
				</script>
            </ul>
            <ul class="fr mr23" style="margin-top:70px;">
            	<span class="fs30 col_red" style="display:none;" id="span_right_3215">√</span>
            	<span class="fs30 col_red" style="display:block;" id="span_wrong_3215">x</span>
            </ul>
            <div class="clear"></div>
            </div>
                        <div>
            <ul class="mt30 fl">
                <li class="ks_t_xh">89</li>
                <li class="ks_tm mb10"  id="2713"></li>
                <div class="clear"></div>
                <div id="option2713"></div>
                <p class="tm_xx">
                	正确答案:<span style="color: red;padding-left: 10px" id="correctAnswer_2713">C</span>
                </p>
                <script type="text/javascript">
					var jsonQuestion={title:"从业人员一系列道德行为表现出的比较稳定的特征和倾向是：",options:[{name:"A",text:"职业道德认识 "},{name:"B",text:"职业道德行为 "},{name:"C",text:"职业道德品质 "},{name:"D",text:"职业道德规范"}]};
			 		showQuestion(jsonQuestion,2713);
				</script>
            </ul>
            <ul class="fr mr23" style="margin-top:70px;">
            	<span class="fs30 col_red" style="display:none;" id="span_right_2713">√</span>
            	<span class="fs30 col_red" style="display:block;" id="span_wrong_2713">x</span>
            </ul>
            <div class="clear"></div>
            </div>
                        <div>
            <ul class="mt30 fl">
                <li class="ks_t_xh">90</li>
                <li class="ks_tm mb10"  id="3200"></li>
                <div class="clear"></div>
                <div id="option3200"></div>
                <p class="tm_xx">
                	正确答案:<span style="color: red;padding-left: 10px" id="correctAnswer_3200">C</span>
                </p>
                <script type="text/javascript">
					var jsonQuestion={title:"当领导的做法存在错误时，找到领导诚恳地谈到自己认为该做法存在的不足，并提出建设性的解决方案，这是遵循了工作沟通的哪项原则？",options:[{name:"A",text:"文化匹配原则 "},{name:"B",text:"直面问题原则 "},{name:"C",text:"积极正面原则 "},{name:"D",text:"灵活应对原则"}]};
			 		showQuestion(jsonQuestion,3200);
				</script>
            </ul>
            <ul class="fr mr23" style="margin-top:70px;">
            	<span class="fs30 col_red" style="display:none;" id="span_right_3200">√</span>
            	<span class="fs30 col_red" style="display:block;" id="span_wrong_3200">x</span>
            </ul>
            <div class="clear"></div>
            </div>
                        <div>
            <ul class="mt30 fl">
                <li class="ks_t_xh">91</li>
                <li class="ks_tm mb10"  id="2704"></li>
                <div class="clear"></div>
                <div id="option2704"></div>
                <p class="tm_xx">
                	正确答案:<span style="color: red;padding-left: 10px" id="correctAnswer_2704">D</span>
                </p>
                <script type="text/javascript">
					var jsonQuestion={title:"有关人际关系的描述，下列说法正确的是：",options:[{name:"A",text:"和谐的人际关系，有利于职场新人消除对新环境的陌生感、孤独感，顺利度过适应期 "},{name:"B",text:"良好的人际关系，有利于员工心气顺、信心增、工作舒心、生活惬意 "},{name:"C",text:"良好的人际关系，有利于增强团结，形成上下左右齐心协力、共谋发展的良好局面，既利于集体，也利于个人的生存和发展 "},{name:"D",text:"以上说法都正确"}]};
			 		showQuestion(jsonQuestion,2704);
				</script>
            </ul>
            <ul class="fr mr23" style="margin-top:70px;">
            	<span class="fs30 col_red" style="display:none;" id="span_right_2704">√</span>
            	<span class="fs30 col_red" style="display:block;" id="span_wrong_2704">x</span>
            </ul>
            <div class="clear"></div>
            </div>
                        <div>
            <ul class="mt30 fl">
                <li class="ks_t_xh">92</li>
                <li class="ks_tm mb10"  id="3220"></li>
                <div class="clear"></div>
                <div id="option3220"></div>
                <p class="tm_xx">
                	正确答案:<span style="color: red;padding-left: 10px" id="correctAnswer_3220">D</span>
                </p>
                <script type="text/javascript">
					var jsonQuestion={title:"以下关于“八荣八耻”的表述，不正确的是：",options:[{name:"A",text:"以热爱祖国为荣，以危害祖国为耻 "},{name:"B",text:"以诚实守信为荣，以见利忘义为耻 "},{name:"C",text:"以崇尚科学为荣，以愚昧无知为耻 "},{name:"D",text:"以服务人民为荣，以金钱利益为耻"}]};
			 		showQuestion(jsonQuestion,3220);
				</script>
            </ul>
            <ul class="fr mr23" style="margin-top:70px;">
            	<span class="fs30 col_red" style="display:none;" id="span_right_3220">√</span>
            	<span class="fs30 col_red" style="display:block;" id="span_wrong_3220">x</span>
            </ul>
            <div class="clear"></div>
            </div>
                        <div>
            <ul class="mt30 fl">
                <li class="ks_t_xh">93</li>
                <li class="ks_tm mb10"  id="2677"></li>
                <div class="clear"></div>
                <div id="option2677"></div>
                <p class="tm_xx">
                	正确答案:<span style="color: red;padding-left: 10px" id="correctAnswer_2677">C</span>
                </p>
                <script type="text/javascript">
					var jsonQuestion={title:"关于如何对待批评，下列表述哪项是正确的：",options:[{name:"A",text:"对他人的批评置若罔闻，不屑一顾 "},{name:"B",text:"对他人的批评，无论好坏，进行反击 "},{name:"C",text:"对他人的批评据理力争，有则改之，无则加勉 "},{name:"D",text:"对他人的批评认为没有任何价值"}]};
			 		showQuestion(jsonQuestion,2677);
				</script>
            </ul>
            <ul class="fr mr23" style="margin-top:70px;">
            	<span class="fs30 col_red" style="display:none;" id="span_right_2677">√</span>
            	<span class="fs30 col_red" style="display:block;" id="span_wrong_2677">x</span>
            </ul>
            <div class="clear"></div>
            </div>
                        <div>
            <ul class="mt30 fl">
                <li class="ks_t_xh">94</li>
                <li class="ks_tm mb10"  id="3227"></li>
                <div class="clear"></div>
                <div id="option3227"></div>
                <p class="tm_xx">
                	正确答案:<span style="color: red;padding-left: 10px" id="correctAnswer_3227">C</span>
                </p>
                <script type="text/javascript">
					var jsonQuestion={title:"时间管理所解决的问题是：",options:[{name:"A",text:"如何完成更多工作 "},{name:"B",text:"如何对事务进行优先级排序 "},{name:"C",text:"如何减少时间浪费，以有效完成既定目标 "},{name:"D",text:"如何将工作授权给他人"}]};
			 		showQuestion(jsonQuestion,3227);
				</script>
            </ul>
            <ul class="fr mr23" style="margin-top:70px;">
            	<span class="fs30 col_red" style="display:none;" id="span_right_3227">√</span>
            	<span class="fs30 col_red" style="display:block;" id="span_wrong_3227">x</span>
            </ul>
            <div class="clear"></div>
            </div>
                        <div>
            <ul class="mt30 fl">
                <li class="ks_t_xh">95</li>
                <li class="ks_tm mb10"  id="3242"></li>
                <div class="clear"></div>
                <div id="option3242"></div>
                <p class="tm_xx">
                	正确答案:<span style="color: red;padding-left: 10px" id="correctAnswer_3242">A</span>
                </p>
                <script type="text/javascript">
					var jsonQuestion={title:"以下哪一项不是聆听他人说话时应遵循的原则？",options:[{name:"A",text:"只聆听自己感兴趣的内容 "},{name:"B",text:"适应讲话者的风格 "},{name:"C",text:"鼓励他人表达自己 "},{name:"D",text:"适当引导对方"}]};
			 		showQuestion(jsonQuestion,3242);
				</script>
            </ul>
            <ul class="fr mr23" style="margin-top:70px;">
            	<span class="fs30 col_red" style="display:none;" id="span_right_3242">√</span>
            	<span class="fs30 col_red" style="display:block;" id="span_wrong_3242">x</span>
            </ul>
            <div class="clear"></div>
            </div>
                        <div>
            <ul class="mt30 fl">
                <li class="ks_t_xh">96</li>
                <li class="ks_tm mb10"  id="3219"></li>
                <div class="clear"></div>
                <div id="option3219"></div>
                <p class="tm_xx">
                	正确答案:<span style="color: red;padding-left: 10px" id="correctAnswer_3219">A</span>
                </p>
                <script type="text/javascript">
					var jsonQuestion={title:"明荣知耻，是民族精神和传统美德的升华。你认为这种说法：",options:[{name:"A",text:"正确 "},{name:"B",text:"错误"}]};
			 		showQuestion(jsonQuestion,3219);
				</script>
            </ul>
            <ul class="fr mr23" style="margin-top:70px;">
            	<span class="fs30 col_red" style="display:none;" id="span_right_3219">√</span>
            	<span class="fs30 col_red" style="display:block;" id="span_wrong_3219">x</span>
            </ul>
            <div class="clear"></div>
            </div>
                        <div>
            <ul class="mt30 fl">
                <li class="ks_t_xh">97</li>
                <li class="ks_tm mb10"  id="2696"></li>
                <div class="clear"></div>
                <div id="option2696"></div>
                <p class="tm_xx">
                	正确答案:<span style="color: red;padding-left: 10px" id="correctAnswer_2696">D</span>
                </p>
                <script type="text/javascript">
					var jsonQuestion={title:"工作时同事间难免会有争执与磨擦，当同事愤怒时，下列做法中合理的是：",options:[{name:"A",text:"不要以愤怒回报，但也不用妥协 "},{name:"B",text:"对你自己的意见要坚持，并表明你希望先冷静下来，再讨论问题所在 "},{name:"C",text:"如果他后悔自己的一时失态，立即表示你毫不介意 "},{name:"D",text:"以上说法都正确"}]};
			 		showQuestion(jsonQuestion,2696);
				</script>
            </ul>
            <ul class="fr mr23" style="margin-top:70px;">
            	<span class="fs30 col_red" style="display:none;" id="span_right_2696">√</span>
            	<span class="fs30 col_red" style="display:block;" id="span_wrong_2696">x</span>
            </ul>
            <div class="clear"></div>
            </div>
                        <div>
            <ul class="mt30 fl">
                <li class="ks_t_xh">98</li>
                <li class="ks_tm mb10"  id="3195"></li>
                <div class="clear"></div>
                <div id="option3195"></div>
                <p class="tm_xx">
                	正确答案:<span style="color: red;padding-left: 10px" id="correctAnswer_3195">D</span>
                </p>
                <script type="text/javascript">
					var jsonQuestion={title:"下列关于工作汇报策略的表述，不正确的是：",options:[{name:"A",text:"布置任务时确认时间 "},{name:"B",text:"工作任务完成后汇报 "},{name:"C",text:"大型项目阶段性成果汇报 "},{name:"D",text:"预计不能按期完成的工作，完成时再汇报"}]};
			 		showQuestion(jsonQuestion,3195);
				</script>
            </ul>
            <ul class="fr mr23" style="margin-top:70px;">
            	<span class="fs30 col_red" style="display:none;" id="span_right_3195">√</span>
            	<span class="fs30 col_red" style="display:block;" id="span_wrong_3195">x</span>
            </ul>
            <div class="clear"></div>
            </div>
                        <div>
            <ul class="mt30 fl">
                <li class="ks_t_xh">99</li>
                <li class="ks_tm mb10"  id="2689"></li>
                <div class="clear"></div>
                <div id="option2689"></div>
                <p class="tm_xx">
                	正确答案:<span style="color: red;padding-left: 10px" id="correctAnswer_2689">D</span>
                </p>
                <script type="text/javascript">
					var jsonQuestion={title:"职场中遇到挫折再所难免。那么职场受挫后如何才能防止消极结果的产生呢？以下说法正确的是：",options:[{name:"A",text:"寻找合适的对象积极的倾诉，即将你的痛苦向你认为值得信赖的人倾诉 "},{name:"B",text:"认真分析、审视自己的受挫的过程，多从自身找原因，克服工作中自身存在的问题 "},{name:"C",text:"重新审视自己的职业目标是否合适，设定或调整可行的阶段目标 "},{name:"D",text:"以上都对"}]};
			 		showQuestion(jsonQuestion,2689);
				</script>
            </ul>
            <ul class="fr mr23" style="margin-top:70px;">
            	<span class="fs30 col_red" style="display:none;" id="span_right_2689">√</span>
            	<span class="fs30 col_red" style="display:block;" id="span_wrong_2689">x</span>
            </ul>
            <div class="clear"></div>
            </div>
                        <div>
            <ul class="mt30 fl">
                <li class="ks_t_xh">100</li>
                <li class="ks_tm mb10"  id="3240"></li>
                <div class="clear"></div>
                <div id="option3240"></div>
                <p class="tm_xx">
                	正确答案:<span style="color: red;padding-left: 10px" id="correctAnswer_3240">C</span>
                </p>
                <script type="text/javascript">
					var jsonQuestion={title:"以下哪一项不属于非言语性沟通的渠道？",options:[{name:"A",text:"眼神 "},{name:"B",text:"手势 "},{name:"C",text:"文字 "},{name:"D",text:"音调"}]};
			 		showQuestion(jsonQuestion,3240);
				</script>
            </ul>
            <ul class="fr mr23" style="margin-top:70px;">
            	<span class="fs30 col_red" style="display:none;" id="span_right_3240">√</span>
            	<span class="fs30 col_red" style="display:block;" id="span_wrong_3240">x</span>
            </ul>
            <div class="clear"></div>
            </div>
                		    		
    		            
        </div>
                <div class="ks_right">
        	<div id="div_question_menu" style="position:fixed; background-color:#fff;">
        	<ul class="ks_cs">
            	<li class="r_top_time fs22" id="timer">
            		            			得分：<span class="col_red">0</span>
            		            	</li>
            	                <li class="r_top_sl mt10">
                	客观题：作答 <span class="col_red">100</span> 题，
                	答对<span class="col_red" id="span_objRightCount"></span> 题，得<span class="col_red">0</span> 分。
                </li>
                                            </ul>
            <dl class="ks_r_cen mt20" style="margin-bottom:50px;">
            	            	<dt class="r_cen_dl"><img src="../../image/ks_r_ywhite.png" /><a class="r_cen_tit" href="#keguanti">客观题</a></dt>
	            		            			            		<dd class="rr_cen_dd">
	            			<a class="rr_cen_xh" id="obj_nav_3070" name="obj_nav" onclick="swithClass('3070')" href="#3070">1 - 3</a>
	            		</dd>
	            			            		            			            		            			            		            			            		<dd class="rr_cen_dd">
	            			<a class="rr_cen_xh" id="obj_nav_3048" name="obj_nav" onclick="swithClass('3048')" href="#3048">4 - 6</a>
	            		</dd>
	            			            		            			            		            			            		            			            		<dd class="rr_cen_dd">
	            			<a class="rr_cen_xh" id="obj_nav_2268" name="obj_nav" onclick="swithClass('2268')" href="#2268">7 - 9</a>
	            		</dd>
	            			            		            			            		            			            		            			            		<dd class="rr_cen_dd">
	            			<a class="rr_cen_xh" id="obj_nav_3046" name="obj_nav" onclick="swithClass('3046')" href="#3046">10 - 12</a>
	            		</dd>
	            			            		            			            		            			            		            			            		<dd class="rr_cen_dd">
	            			<a class="rr_cen_xh" id="obj_nav_3124" name="obj_nav" onclick="swithClass('3124')" href="#3124">13 - 15</a>
	            		</dd>
	            			            		            			            		            			            		            			            		<dd class="rr_cen_dd">
	            			<a class="rr_cen_xh" id="obj_nav_2366" name="obj_nav" onclick="swithClass('2366')" href="#2366">16 - 18</a>
	            		</dd>
	            			            		            			            		            			            		            			            		<dd class="rr_cen_dd">
	            			<a class="rr_cen_xh" id="obj_nav_3114" name="obj_nav" onclick="swithClass('3114')" href="#3114">19 - 21</a>
	            		</dd>
	            			            		            			            		            			            		            			            		<dd class="rr_cen_dd">
	            			<a class="rr_cen_xh" id="obj_nav_2395" name="obj_nav" onclick="swithClass('2395')" href="#2395">22 - 24</a>
	            		</dd>
	            			            		            			            		            			            		            			            		<dd class="rr_cen_dd">
	            			<a class="rr_cen_xh" id="obj_nav_3094" name="obj_nav" onclick="swithClass('3094')" href="#3094">25 - 27</a>
	            		</dd>
	            			            		            			            		            			            		            			            		<dd class="rr_cen_dd">
	            			<a class="rr_cen_xh" id="obj_nav_2376" name="obj_nav" onclick="swithClass('2376')" href="#2376">28 - 30</a>
	            		</dd>
	            			            		            			            		            			            		            			            		<dd class="rr_cen_dd">
	            			<a class="rr_cen_xh" id="obj_nav_2604" name="obj_nav" onclick="swithClass('2604')" href="#2604">31 - 33</a>
	            		</dd>
	            			            		            			            		            			            		            			            		<dd class="rr_cen_dd">
	            			<a class="rr_cen_xh" id="obj_nav_2671" name="obj_nav" onclick="swithClass('2671')" href="#2671">34 - 36</a>
	            		</dd>
	            			            		            			            		            			            		            			            		<dd class="rr_cen_dd">
	            			<a class="rr_cen_xh" id="obj_nav_2592" name="obj_nav" onclick="swithClass('2592')" href="#2592">37 - 39</a>
	            		</dd>
	            			            		            			            		            			            		            			            		<dd class="rr_cen_dd">
	            			<a class="rr_cen_xh" id="obj_nav_2623" name="obj_nav" onclick="swithClass('2623')" href="#2623">40 - 42</a>
	            		</dd>
	            			            		            			            		            			            		            			            		<dd class="rr_cen_dd">
	            			<a class="rr_cen_xh" id="obj_nav_2630" name="obj_nav" onclick="swithClass('2630')" href="#2630">43 - 45</a>
	            		</dd>
	            			            		            			            		            			            		            			            		<dd class="rr_cen_dd">
	            			<a class="rr_cen_xh" id="obj_nav_2644" name="obj_nav" onclick="swithClass('2644')" href="#2644">46 - 48</a>
	            		</dd>
	            			            		            			            		            			            		            			            		<dd class="rr_cen_dd">
	            			<a class="rr_cen_xh" id="obj_nav_2613" name="obj_nav" onclick="swithClass('2613')" href="#2613">49 - 51</a>
	            		</dd>
	            			            		            			            		            			            		            			            		<dd class="rr_cen_dd">
	            			<a class="rr_cen_xh" id="obj_nav_2603" name="obj_nav" onclick="swithClass('2603')" href="#2603">52 - 54</a>
	            		</dd>
	            			            		            			            		            			            		            			            		<dd class="rr_cen_dd">
	            			<a class="rr_cen_xh" id="obj_nav_2619" name="obj_nav" onclick="swithClass('2619')" href="#2619">55 - 57</a>
	            		</dd>
	            			            		            			            		            			            		            			            		<dd class="rr_cen_dd">
	            			<a class="rr_cen_xh" id="obj_nav_2652" name="obj_nav" onclick="swithClass('2652')" href="#2652">58 - 60</a>
	            		</dd>
	            			            		            			            		            			            		            			            		<dd class="rr_cen_dd">
	            			<a class="rr_cen_xh" id="obj_nav_2596" name="obj_nav" onclick="swithClass('2596')" href="#2596">61 - 63</a>
	            		</dd>
	            			            		            			            		            			            		            			            		<dd class="rr_cen_dd">
	            			<a class="rr_cen_xh" id="obj_nav_2622" name="obj_nav" onclick="swithClass('2622')" href="#2622">64 - 66</a>
	            		</dd>
	            			            		            			            		            			            		            			            		<dd class="rr_cen_dd">
	            			<a class="rr_cen_xh" id="obj_nav_2595" name="obj_nav" onclick="swithClass('2595')" href="#2595">67 - 69</a>
	            		</dd>
	            			            		            			            		            			            		            			            		<dd class="rr_cen_dd">
	            			<a class="rr_cen_xh" id="obj_nav_2670" name="obj_nav" onclick="swithClass('2670')" href="#2670">70 - 72</a>
	            		</dd>
	            			            		            			            		            			            		            			            		<dd class="rr_cen_dd">
	            			<a class="rr_cen_xh" id="obj_nav_3221" name="obj_nav" onclick="swithClass('3221')" href="#3221">73 - 75</a>
	            		</dd>
	            			            		            			            		            			            		            			            		<dd class="rr_cen_dd">
	            			<a class="rr_cen_xh" id="obj_nav_2676" name="obj_nav" onclick="swithClass('2676')" href="#2676">76 - 78</a>
	            		</dd>
	            			            		            			            		            			            		            			            		<dd class="rr_cen_dd">
	            			<a class="rr_cen_xh" id="obj_nav_3235" name="obj_nav" onclick="swithClass('3235')" href="#3235">79 - 81</a>
	            		</dd>
	            			            		            			            		            			            		            			            		<dd class="rr_cen_dd">
	            			<a class="rr_cen_xh" id="obj_nav_3210" name="obj_nav" onclick="swithClass('3210')" href="#3210">82 - 84</a>
	            		</dd>
	            			            		            			            		            			            		            			            		<dd class="rr_cen_dd">
	            			<a class="rr_cen_xh" id="obj_nav_2700" name="obj_nav" onclick="swithClass('2700')" href="#2700">85 - 87</a>
	            		</dd>
	            			            		            			            		            			            		            			            		<dd class="rr_cen_dd">
	            			<a class="rr_cen_xh" id="obj_nav_3215" name="obj_nav" onclick="swithClass('3215')" href="#3215">88 - 90</a>
	            		</dd>
	            			            		            			            		            			            		            			            		<dd class="rr_cen_dd">
	            			<a class="rr_cen_xh" id="obj_nav_2704" name="obj_nav" onclick="swithClass('2704')" href="#2704">91 - 93</a>
	            		</dd>
	            			            		            			            		            			            		            			            		<dd class="rr_cen_dd">
	            			<a class="rr_cen_xh" id="obj_nav_3227" name="obj_nav" onclick="swithClass('3227')" href="#3227">94 - 96</a>
	            		</dd>
	            			            		            			            		            			            		            			            		<dd class="rr_cen_dd">
	            			<a class="rr_cen_xh" id="obj_nav_2696" name="obj_nav" onclick="swithClass('2696')" href="#2696">97 - 99</a>
	            		</dd>
	            			            		            			            		            			            		            			            		<dd class="rr_cen_dd">
	            			<a class="rr_cen_xh" id="obj_nav_3240" name="obj_nav" onclick="swithClass('3240')" href="#3240">100 - 102</a>
	            		</dd>
	            			            	            	            	
            	                <dt class="r_cen_js"></dt>
            </dl>
            </div>
        </div>
        <div class="clear"></div>
    </div>
</div>


</body>
<!-- 主观题考生答案信息提取 start -->
<script>
	var strQuestionIds1 = "";
	var strQuestionAnswer1 = ;
	var strScoreDetail1 = "";
	//主观题考生答案信息提取
	showAnswer1(strQuestionIds1,strQuestionAnswer1,strScoreDetail1);
</script>
<!-- 主观题考生答案信息提取 end -->
<!-- 客观题考生答案信息提取 start -->
<script>
	var strQuestionIds0 = "3070,3088,2327,3048,3075,3278,2268,3076,3064,3046,2373,3112,3124,3115,2406,2366,3093,2381,3114,3092,2390,2395,3105,2408,3094,3126,2399,2376,2379,2392,2604,2625,2597,2671,2599,2606,2592,2666,2636,2623,2650,2629,2630,2616,2665,2644,2626,2669,2613,2658,2638,2603,2608,2612,2619,2593,2635,2652,2591,2618,2596,2594,2640,2622,2660,2610,2595,2647,2649,2670,2722,2683,3221,2691,3230,2676,3202,2706,3235,3192,2712,3210,2699,2682,2700,3189,3238,3215,2713,3200,2704,3220,2677,3227,3242,3219,2696,3195,2689,3240";
	var strQuestionAnswer0 = "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0";
	//客观题考生答案信息提取
	var strQuestionAnsers = strQuestionAnswer0.split(",");
	var questionIds = strQuestionIds0.split(",");
	var objRightCount = 0;
	if(strQuestionAnsers.length > 0){
		for ( var i = 0; i < questionIds.length; i++) {
			if(strQuestionAnsers[i] != "0"){
				var name = "radio_" + questionIds[i];
				var objs = document.getElementsByName(name);
				for(var j = 0;j< objs.length;j++){
					if(objs[j].value == strQuestionAnsers[i] ){
						objs[j].checked = true;
						var span = document.getElementById("correctAnswer_"+questionIds[i]);
						var span_right = document.getElementById("span_right_"+questionIds[i]);
						var span_wrong = document.getElementById("span_wrong_"+questionIds[i]);
						if(span !=null && span_right!=null && span_wrong!=null){
							if(span.innerText == strQuestionAnsers[i]){
								span_right.style.display="";
								span_wrong.style.display="none";
								objRightCount++;
							}else{
								span_right.style.display="none";
								span_wrong.style.display="";
							}
						}
					}
				}
			}
		}
	}
	var obj_objRightCount = document.getElementById("span_objRightCount");
	if(obj_objRightCount!=null){
		obj_objRightCount.innerText =objRightCount;
	}
</script>
<!-- 客观题考生答案信息提取 end -->


</html>
'''

list_1 = re.findall(r'([A-D])</span>',s)
print len(list_1)
strli = '%2C'.join(list_1)
strli = strli.upper()
print strli
