@login_required
@staff_log
def weekly_daily_edit(request, weekly_daily_id=None):
	"""
	周报编辑功能
	:param request:
	:return:
	"""
	menu = 12
	menu_leaf = "12-4"
	if request.method == 'POST':
		if weekly_daily_id:
			weekly_daily = get_object_or_404(WeeklyDaily, pk=weekly_daily_id)
			form = WeeklyDailyForm(request.POST, request.FILES, instance=weekly_daily)
		else:
			form = WeeklyDailyForm(request.POST, request.FILES)
		if form.is_valid():
			weekly_daily = form.save(commit=False)
			weekly_daily.create_staff = request.user.staff
			weekly_daily.save()
			messages.success(request, '保存数据成功')
		else:
			messages.error(request, '保存数据失败')
		return HttpResponseRedirect(reverse('weekly_daily') + "?page=" + request.GET.get("page", ""))
	else:
		if weekly_daily_id:
			weekly_daily = get_object_or_404(WeeklyDaily, pk=weekly_daily_id)
			form = WeeklyDailyForm(instance=weekly_daily)
		else:
			# 周报申请人
			weekly_daily_staff = request.user.staff
			# 第几周
			today = datetime.datetime.now()
			week_num = today.strftime("%W")
			# 本周第一天和最后一天
			this_week_start = today - datetime.timedelta(days=today.weekday())
			this_week_end = today + datetime.timedelta(days=6 - today.weekday())
			week_range = this_week_start.strftime('%m/%d') + this_week_end.strftime('-%m/%d')
			form = WeeklyDailyForm()
	return render(request, 'weekly_daily/weekly_daily_edit.html', locals())


@login_required
@staff_log
def weekly_daily_detail(request, weekly_daily_id=None):
	""""
	周报详情
	"""
	weekly_daily = get_object_or_404(WeeklyDaily, pk=weekly_daily_id)
	return render(request, 'weekly_daily/weekly_daily_detail.html', locals())


@login_required
@staff_log
def weekly_daily_delete(request, weekly_daily_id=None):
	"""
	删除周报信息
	:param request: 
	:param weekly_daily_id: 
	:return: 
	"""
	try:
		weekly_daily = get_object_or_404(WeeklyDaily, pk=weekly_daily_id)
		weekly_daily.del_status = 1
		weekly_daily.save()
		messages.success(request, '删除成功')
	except:
		messages.error(request, '删除失败')
	return HttpResponseRedirect(reverse('weekly_daily') + "?page=" + request.GET.get("page", ""))