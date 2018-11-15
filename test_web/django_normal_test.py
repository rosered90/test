# _*_ coding::utf-8 _*_
# 在django项目中测试
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "framework.settings.dev")
django.setup()


# from smartShelf.base.device.models import Device
# from smartShelf.interface.api4.views import parse_data_txt

# data_file = 'F:\\data\\web\\smart_shelf\\media\\receive_file\\2018\\11\\14\\VS_9997_1542112850_data.txt'
# device = Device.objects.filter(identify_code='VS_9997').first()
# res = parse_data_txt(data_file, device)