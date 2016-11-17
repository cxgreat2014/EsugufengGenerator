#!/usr/bin/env python3

from requests import get
from random import randint, shuffle
from time import sleep
import sys

use_real_random = True
if len(sys.argv)>1:
    if sys.argv[1] == "0":
        use_real_random=False

two_chars = ['朱砂', '天下', '杀伐', '人家', '韶华', '风华', '繁华', '血染', '墨染', '白衣', '素衣', '嫁衣',
             '倾城', '孤城', '空城', '旧城', '半城', '旧人', '伊人', '心疼', '春风', '古琴', '无情', '迷离',
             '断弦', '焚尽', '散乱', '陌路', '乱世', '笑靥', '浅笑', '明眸', '轻叹', '烟火', '一生', '三生',
             '浮生', '桃花', '梨花', '落花', '烟花', '离殇', '情殇', '爱殇', '剑殇', '灼伤', '仓皇', '匆忙',
             '陌上', '清商', '焚香', '墨香', '微凉', '断肠', '痴狂', '凄凉', '黄梁', '未央', '成双', '无恙',
             '虚妄', '凝霜', '洛阳', '长安', '江南', '忘川', '千年', '纸伞', '烟雨', '回眸', '公子', '红尘',
             '红颜', '红衣', '红豆', '红线', '青丝', '青史', '青冢', '白发', '白首', '白骨', '黄土', '黄泉',
             '奈何', '烟沙', '碧落', '紫陌']
four_chars = ['情深缘浅', '情深不寿', '莫失莫忘', '夜色朦胧', '阴阳相隔', '如花美眷', '似水流年', '眉目如画',
              '曲终人散', '繁华落尽', '不诉离殇', '一声轻叹', '一世长安']
sentence = ['xx，xx，xx了xx。', 'xxxx，xxxx，不过是一场xxxx。', '你说xxxx，我说xxxx，最后不过xxxx。',
            'xx，xx，许我一场xxxx。', '一x一x一xx，半x半x半xx。', '你说xxxxxxxx，后来xxxxxxxx。',
            'xxxx，xxxx，终不敌xxxx。', 'xxxx之间，xxxx，xxxxxxxxx。',
            'xx，xx，许我一场xxxx。xx，xx，许我一场xxxx。xx，xx，许我一场xxxx。',
            'xxxx，xxxx，不过是一场xxxx。xxxx，xxxx，不过是一场xxxx。xxxx，xxxx，不过是一场xxxx。']

sentence_sum = len(sentence) - 1


def get_random_int(max_int):
    if not use_real_random:
        return randint(0, max_int)
    if max_int is 0:
        return 0
    random_result = get('https://www.random.org/integers/?num=1&min=0&max={0}&col=1&base=10&format=plain&rnd=new'.format(max_int)).content
    try:
        int(random_result)
    except:
        print(random_result)
    return int(random_result)


def get_sentence():
    shuffle(sentence)
    shuffle(two_chars)
    shuffle(four_chars)
    model = sentence[get_random_int(sentence_sum)]
    while 'xxxx' in model:
        four_chars_list = four_chars.copy()
        four_chars_sum = len(four_chars_list) - 1
        in_replace = four_chars_list[get_random_int(four_chars_sum)]
        model = model.replace("xxxx", in_replace, 1)
        four_chars_list.remove(in_replace)
    while 'xx' in model:
        two_chars_list = two_chars.copy()
        two_chars_sum = len(two_chars_list) - 1
        in_replace = two_chars_list[get_random_int(two_chars_sum)]
        model = model.replace("xx", in_replace, 1)
        two_chars_list.remove(in_replace)
    while 'x' in model:
        if get_random_int(1):
            model = model.replace("x", '殇', 1)
        else:
            two_chars_list = two_chars.copy()
            two_chars_sum = len(two_chars_list) - 1
            in_replace = two_chars_list[get_random_int(two_chars_sum)]
            model = model.replace("x", in_replace[get_random_int(1)], 1)
            two_chars_list.remove(in_replace)
    return model


while True:
    print(get_sentence())
    if not use_real_random:
        sleep(1)
