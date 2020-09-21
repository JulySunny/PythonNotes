# coding=utf-8
# !/usr/bin/ env python
"""
快速开始
"""
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

from bs4 import BeautifulSoup

soup = BeautifulSoup(html_doc, 'html.parser')
print(soup.prettify())
print("======================华丽的分割线======================")
# 1.获取标签 .xxx
print(soup.title)
print("======================华丽的分割线======================")
# 2.获取标签名称 .name
print(soup.title.name)
print("======================华丽的分割线======================")
# 3.获取标签内容 .string
print(soup.title.string)
print("======================华丽的分割线======================")
# 4.获取父节点 .parent
print(soup.title.parent)
print("======================华丽的分割线======================")
# 5.获取特定标签
print(soup.p)
print("======================华丽的分割线======================")
# 6.
print("======================华丽的分割线======================")
print("======================华丽的分割线======================")
print("======================华丽的分割线======================")
print("======================华丽的分割线======================")
print("======================华丽的分割线======================")

