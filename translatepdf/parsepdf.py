#! python3
# -*- coding: utf-8 -*-

# https://pypi.python.org/pypi/pdfminer3k/ pdfminer3k需要下载执行安装 pip上的很久没更新了，无法使用
import os
import sys
import random
from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LTTextBoxHorizontal, LAParams
# from pdfminer.pdfinterp import PDFTextExtractionNotAllowe


def parse(path):
    '''
    解析pdf文件
    '''
    with open(path, 'rb') as fp:  # 以二进制读模式打开
        #用文件对象来创建一个pdf文档分析器
        # 创建一个与文档关联的解析器
        praser = PDFParser(fp)
        # 创建一个PDF文档
        doc = PDFDocument()
        # 连接「分析器 与文档对象」 连接两者
        praser.set_document(doc)
        doc.set_parser(praser)

        # 提供初始化密码
        # 如果没有密码 就创建一个空的字符串
        doc.initialize('')

        # 检测文档是否提供txt转换，不提供就忽略
        if not doc.is_extractable:
            print('can\'t parse')
            pass
            # raise PDFTextExtractionNotAllowed
        else:
            # 创建PDf 资源管理器 来管理共享资源
            rsrcmgr = PDFResourceManager()
            # 创建一个PDF设备对象
            laparams = LAParams()
            device = PDFPageAggregator(rsrcmgr, laparams=laparams)
            # 创建一个PDF解释器对象
            interpreter = PDFPageInterpreter(rsrcmgr, device)

            # 循环遍历列表，每次处理一个page的内容
            results = []
            for page in doc.get_pages():  # doc.get_pages() 获取page列表
                interpreter.process_page(page)
                # 接受该页面的LTPage对象
                layout = device.get_result()
                # 这里layout是一个LTPage对象 里面存放着 这个page解析出的各种对象 一般包括LTTextBox, LTFigure, LTImage, LTTextBoxHorizontal 等等 想要获取文本就获得对象的text属性，
                for x in layout:
                    if (isinstance(x, LTTextBoxHorizontal)):
                        results.append(x.get_text())
                    return results
            return results


if __name__ == '__main__':
    print(parse())
