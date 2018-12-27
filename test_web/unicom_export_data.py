old

{% extends 'common_list.html' %}
{% load static %}
{% load dajaxice_templatetags %}
{% block title %}员工周报审核列表{% endblock %}
{% block headcss %}
    <link rel="stylesheet" href="{% static 'framework/inspinia/css/datepicker3.css' %}">
    <style>
    </style>
{% endblock %}

{% block content-header %}
    <h1>员工周报审核模块</h1>
    <ol class="breadcrumb">
        <li><a href="{% url "control_index" %}"><i class="fa fa-home"></i> 首页</a></li>
        <li class="active">员工周报审核列表</li>
    </ol>
{% endblock %}

{% block search_conditions %}



    <div class="col-lg-3">
        <div class="form-group">
            <div class="input-group m-b">
                <span class="input-group-addon">周数</span>
                <input class="form-control" id="week_num" name='week_num'
                       {% if request.GET.week_num %}value="{{ request.GET.week_num }}"{% else %} value="{{ week_num }}" {% endif %} type="text">
            </div>
        </div>
    </div>


    <div class="col-lg-3">
        <div class="form-group">
            <div class="input-group m-b">
                <span class="input-group-addon">操作人员</span>
                <select name="create_staff" id="create_staff" class="form-control chosen-select"  tabindex="2">
                    <option value=""></option>
                    {% for staff in staff_list %}
                    <option  value="{{ staff.id }}" {% if request.GET.create_staff|add:'0' == staff.id  %} selected="selected" {% endif %}>{{ staff.name }}</option>
                    {% endfor %}
                </select>
            </div>
        </div>
    </div>

{% endblock %}
{% block box-title %}员工周报审核列表<span style="color:red;">(第{{ weekly_week_num }}周- 日期范围：{{ weekly_week_range }})</span><br/>
<!--查询周数和默认显示的周数是不一样的-->
{% if filter_tag %}
    <p style="font-size:14px;margin-top:10px;font-weight: bold;">第<span style="color:red; font-weight: bold;">{{ filter_week_num }}</span>周提交的周报个数：{{ filter_weekly_num }}&nbsp;&nbsp;&nbsp;
        未提交的周报个数：{{ pre_no_submit_num }}</p>
{% else %}
    <p style="font-size:14px;margin-top:10px;font-weight: bold;">上周提交的周报个数：{{ pre_weekly_list }}&nbsp;&nbsp;&nbsp;
        未提交的周报个数：{{ pre_no_submit_num }}</p>
    <p style="font-size:14px; font-weight: bold;">本周提交的周报个数：{{ this_weekly_list }}&nbsp;&nbsp;&nbsp;未提交的周报个数：{{ this_no_submit_num }}</p>
{% endif %}
{% endblock %}

{% block list_button %}
{% endblock %}

{% block box-body %}
        {% load bootstrap_pagination %}
        {% bootstrap_paginate weekly_list range=15 %}
    <table id="table" class="table table-striped table-bordered table-hover" >
        <thead>
        <tr>
            <th>序号</th>
            <th>周报报告人</th>
            <th>职位</th>
            <th>岗位</th>
            <th>周数</th>
            <th>时间范围</th>
            <th>是否为补写周报</th>
            <th>提交状态</th>
            <th>操作人员</th>
            <th>周报创建时间</th>
            <th>{% block list_menu_th %}操作{% endblock %}</th>
        </tr>
        </thead>
        <tbody>
        {% load bootstrap_pagination %}
        {% for weekly in weekly_list %}
            <tr>
                <td>{{ page_count|add:forloop.counter }}</td>
                <td>{{ weekly.weekly_staff.name }}</td>
                <td>{{ weekly.weekly_staff.position_name|default_if_none:'' }}</td>
                <td>{{ weekly.weekly_staff.department_name|default_if_none:'' }}</td>
                <td>{{ weekly.week_num }}</td>
                <td>{{ weekly.week_range }}</td>
                <td><a class="btn btn-xs {% if weekly.submit_status == 1%} btn-success
                {% elif weekly.submit_status == 0   %} btn-default
                {% elif weekly.submit_status == 2   %} btn-warning {% endif %}">{{ weekly.get_submit_status_display }}</a></td>
                <td>{{ weekly.create_staff.name }}</td>
                <td>{{ weekly.create_time|date:"Y-m-d" }}</td>
                <td>
                    {% block list_menu %}
	                    <div class="btn-group">
	                    <button data-toggle="dropdown" class="btn btn-info btn-xs dropdown-toggle">
                                状态操作 <span class="caret"></span></button>
                         <ul class="dropdown-menu">
{#                            <li>#}
{#                            <a href="{% url 'weekly_edit' weekly.id %}?page={{ request.GET.page }}" style="margin-left: 5px;"> 修改</a>#}
{#                            </li>#}
                            <li>
                            <a href="{% url 'weekly_detail' weekly.id %}" style="margin-left: 5px;">详情</a>
                            </li>
{#                             <li>#}
{#                                <a onclick="show_confirm({{ weekly.id }}, {{ request.GET.page|default:"1" }})" style="margin-left: 5px;">删除</a>#}
{#                             </li>#}
                         </ul>
	                    </div>
                        <a href="{% url 'weekly_daily_list' weekly.id %}" class="btn btn-xs btn-info">具体周报信息</a>
                        <a href="#modal-weekly_show-{{ weekly.id }}" data-toggle="modal" class="btn btn-xs btn-info">简阅浏览周报</a>
                        {% if weekly.submit_status != 2 %}
                        <a href="#modal-view-draw-{{ weekly.id }}" data-toggle="modal" class="btn btn-xs btn-warning">撤回周报</a>
                        {% endif %}
                        <!--简阅浏览周报-->
                        <div id="modal-weekly_show-{{ weekly.id }}" class="modal fade" aria-hidden="true" >
                            <div class="modal-dialog" style="width:70%;">
                                <div class="modal-content">
                                    <div class="modal-body">
                                        <div class="row">
                                            <div class="col-sm-12 b-r"><h3 class="m-t-none m-b" align="center">{{ weekly.weekly_staff.name }}-周报信息</h3>
                                                <table id="table" class="table table-striped table-bordered table-hover" >
                                                    <thead>
                                                    <tr>
                                                        <th>星期几</th>
                                                        <th>今天的任务</th>
                                                        <th>工作进度</th>
                                                        <th>是否加班</th>
                                                    </tr>
                                                    </thead>
                                                    <tbody>
                                                    {% for weekly_daily in weekly.weekly_daily_list %}
                                                        <tr>
                                                            <td style="width: 5%;">{{ weekly_daily.get_detail_week_display }}</td>
                                                            <td style="width: 71%; height: 120px;"><div style="height: 100%;overflow-y: scroll">{{ weekly_daily.content|safe|default_if_none:'' }}</div></td>
                                                            <td style="width: 7%;">{{ weekly_daily.get_work_completion_ratio_display }}</td>
                                                            <td style="width: 7%;">{{ weekly_daily.get_overtime_display }}</td>
                                                        </tr>
                                                    {% endfor %}
                                                    </tbody>
                                                </table>
                                                <div class="form-group">
                                                    <label class="col-sm-9 control-label">本周工作总结</label>
                                                    <div class="col-sm-12" style="border:solid 1px #d3d3d3;">
                                                        {{ weekly.week_conclusion|safe}}
                                                    </div>
                                                </div>
                                                <div class="form-group" >
                                                    <label class="col-sm-9 control-label" style="margin-top: 20px;">下周工作安排</label>
                                                    <div class="col-sm-12" style="border:solid 1px #d3d3d3;">
                                                        {{ weekly.next_week_arrange|safe }}
                                                    </div>
                                                </div>

                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <!--撤回理由-->
                        <div id="modal-view-draw-{{ weekly.id }}" class="modal fade" aria-hidden="true" >
                            <div class="modal-dialog">
                                <div class="modal-content">
                                    <div class="modal-body">
                                        <div class="row">
                                            <div class="col-sm-12 b-r"><h3 class="m-t-none m-b" align="center">请填写审核不通过的原因</h3>
                                                <form role="form" action="{% url 'leadership_no_audit_weekly' weekly.id %}"
                                                      method="post" enctype="multipart/form-data">
                                                    {% csrf_token %}
                                                <div class="form-horizontal">

                                                    <div class="form-group" >
                    {#                                    <span class="col-sm-1 control-label" ></span>#}
                                                        <div style="text-align: center">
                                                            <textarea name="audit_opinion" id="audit_opinion" cols="80" rows="10"></textarea>
                                                        </div>
                                                    </div>
                                                    <div>
                                                        <button class="btn btn-info pull-right"><i class="fa fa-share"></i>提交审核结果
                                                        </button>
                                                    </div>
                                                </div>
                                                </form>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    {% endblock %}
                </td>
            </tr>
        {% endfor %}
        </tbody>
    </table>
    {% bootstrap_paginate weekly_list range=15  %}
{% endblock %}

{% block js %}
    <script src="{% static 'framework/inspinia/js/bootstrap-datepicker.js' %}"></script>
    <script src="{% static 'framework/inspinia/js/locales/bootstrap-datepicker.zh-CN.js' %}" charset="UTF-8"></script>
    <script>
		function clean_get_param(the_form) {
			$(':input[value=""]').attr('name', '');
			return true;
		}

		 function show_confirm(id, page) {
            delete_confirm("你是否要删除该数据？", function () {
                window.location.href = "/daily/weekly/" + id + "/delete?page=" + page;
            });
        }
         function submit_confirm(id, page) {
             delete_confirm("你是否要提交该周报？", function () {
                 window.location.href = "/daily/weekly/" + id + "/submit?page=" + page;
             });
         }


    </script>
{% endblock %}