# -*- coding: utf-8 -*-

import ocr
import yaml_class
'''
图片统一命名格式：'num'+N(编号）+'.jpn'
excel文件名称格式：与图片的N（编号）一一对应
'''
def ocr_pic(N):
    #调用yaml读取函数，已列表形式返回配置数据secret_id，secret_key
    config = yaml_class.get_yaml_data("config.yaml")
    #遍历读取图片，N为图片的个数
    for image_path in range(1, N + 1):
        pic_path = image_path
        # 调用ocr识别图片并转成excel文件
        path_excel = ocr.img_to_excel(
            'excel_list/' + str(pic_path) ,  #excel文件路径+文件名
            'pic_list/' + 'num' + str(image_path) + '.png',  #图片文件路径+文件名
            secret_id=config['secret_id'],
            secret_key=config['secret_key'],
        )

if __name__ == '__main__':
    #入参为图片数量，假设有2张图片
    ocr_pic(1)