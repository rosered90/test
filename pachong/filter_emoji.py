# _*_ coding:utf-8 _*_
import re


def filter_emoji(desstr, restr=''):
    '''
    过滤表情
    '''
    try:
        co = re.compile(u'[\U00010000-\U0010ffff]')
    except re.error:
        co = re.compile(u'[\uD800-\uDBFF][\uDC00-\uDFFF]')
    print(co.sub(restr, desstr))
    return co.sub(restr, desstr)


filter_emoji('不会让自己失望😞……这有什么🤔？我在外面等你电话*&^%$#@☎️！我电话📲、')