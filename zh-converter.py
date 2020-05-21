
import argparse
import zhconv
import json

ZH_MAP = {
    'cn': 'zh-cn',
    'hk': 'zh-hk',
    'tw': 'zh-tw',
    'sg': 'zh-sg',
    'hans': 'zh-hans',
    'hant': 'zh-hant'
}


def zh_translate(content, model):
    '''实现翻译接口'''
    model = ZH_MAP[model]
    return zhconv.convert(content, model)


def translate(context, model):
    result = zh_translate(context, model)

    print('-----------')
    print('原文: {}'.format(context))
    print('---')
    print('译文: {}'.format(result))
    print('-----------')
    return result


parser = argparse.ArgumentParser(description='python3 zh translate')
parser.add_argument('--type', '-t', help='taget type:  cn,hk,tw,sg,hans,hant ')
parser.add_argument('--word', '-w', help='translate zh word')
parser.add_argument('--file', '-f', help='translate file path')

args = parser.parse_args()

mode = args.type or 'cn'

if args.word:
    translate(args.word, mode)

elif args.file:
    translate_result = None
    with open(args.file) as f:
        context = f.readlines()
        translate_result = translate("".join(context), mode)

    if translate_result:
        with open('./translated.txt', 'w') as t:
            t.writelines(translate_result)
