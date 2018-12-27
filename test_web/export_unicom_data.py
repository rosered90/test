@login_required
@staff_log
def installment_list(request):
	"""
	分期合同列表
	:param request:
	:return:
	"""
	menu = 6
	menu_leaf = "6-1"
	staff_list = Staff.objects.filter(del_status=0).exclude(status=11)  # 操作人员
	installment_list = ContractInstallment.objects.filter(del_status=0).order_by('-create_time')
	client_list = Client.objects.filter(del_status=0)  # 需方和供方
	source_list = ContractInstallment.SOURCE.items()
	type_list = ContractInstallment.TYPE.items()
	status_list = ContractInstallment.STATUS.items()
	pay_way_list = ContractInstallment.PAY_WAY.items()
	payment_list = ContractInstallment.PAYMENT.items()
	#  查询字段
	kwargs = {
		'supplier__id': 'supplier',
		'demand__id': 'demand',
		'source': 'source',
		'type': 'type',
		'status': 'status',
		'pay_way': 'pay_way',
		'payment': 'payment',
		'create_staff__id': 'create_staff',
		'amount__contains': 'amount',
		'related_detail__code': 'code',
	}
	kwargs = filter_kwargs(request, kwargs)
	installment_list = installment_list.filter(**kwargs)
	# 求付款金额和未付款金额 付部分款金额
	no_payment_money = installment_list.filter(payment=0).aggregate(Sum('amount'))['amount__sum'] or 0
	no_payment_money = format(no_payment_money, '.2f')
	payment_money = installment_list.filter(payment=1).aggregate(Sum('amount'))['amount__sum'] or 0
	payment_money = format(payment_money, '.2f')
	part_payment_money = installment_list.filter(payment=2).aggregate(Sum('amount'))['amount__sum'] or 0
	part_payment_money = format(part_payment_money, '.2f')
	installment_list, page_count, page_size = get_page_info(request, installment_list)
	return render(request, 'installment/installment_list.html', locals())


@login_required
@staff_log
def installment_edit(request, installment_id=None):
	"""
	分期合同编辑
	:param request:
	:return:
	"""
	menu = 6
	menu_leaf = "6-1"
	# 需方和供方的列表
	client_list = Client.objects.filter(del_status=0)
	source_type = ContractInstallment.SOURCE.items()  # 来源类型
	type_list = ContractInstallment.TYPE.items()  # 订单类型
	installment_status = ContractInstallment.STATUS.items()  # 签订状态
	installment_pay_way = ContractInstallment.PAY_WAY.items()  # 付款方式
	installment_payment = ContractInstallment.PAYMENT.items()  # 付款状态
	if request.method == "POST":
		if installment_id:
			installment = get_object_or_404(ContractInstallment, pk=installment_id)
			form = ContractInstallmentForm(request.POST, request.FILES, instance=installment)
		else:
			form = ContractInstallmentForm(request.POST, request.FILES)
		if form.is_valid():
			installment = form.save(commit=False)
			installment.create_staff = request.user.staff
			installment.save()
			# 分期合同的订单号根据分期合同的签订金额来看
			if installment.signed_time:
				signed_time_str = installment.signed_time.strftime('%Y%m%d')
				installment.installment_order = 'qg' + str(signed_time_str) + str(installment.id).rjust(4, '0')
				installment.save()
			messages.success(request, "保存数据成功")
		else:
			messages.error(request, "保存数据失败")
		return HttpResponseRedirect(reverse('installment_list') + "?page=" + request.GET.get("page", ""))
	else:
		if installment_id:
			installment = get_object_or_404(ContractInstallment, pk=installment_id)
			form = ContractInstallmentForm(instance=installment)
		else:
			form = ContractInstallmentForm()
	return render(request, 'installment/installment_edit.html', locals())


@login_required
@staff_log
def installment_detail(request,installment_id=None):
	"""
	分期合同详情
	"""
	menu = 6
	menu_leaf = "6-1"
	installment = get_object_or_404(ContractInstallment, pk=installment_id)
	detail_list = installment.related_detail.filter(del_status=0)
	return render(request, 'installment/installment_detail.html', locals())


@login_required
@staff_log
def installment_delete(request, installment_id=None):
	"""
	分期合同删除
	"""
	try:
		installment = get_object_or_404(ContractInstallment, pk=installment_id)
		installment.del_status = 1
		installment.save()
		messages.success(request, "删除成功")
	except:
		messages.error(request, "删除失败")
	return HttpResponseRedirect(reverse('installment_list') + "?page=" + request.GET.get("page", ""))