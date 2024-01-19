import os
import re
import time
from collections import defaultdict


# 敏感词过滤
class BSFilter:

  def __init__(self):
    self.keywords = []
    self.kwsets = set([])
    self.bsdict = defaultdict(set)
    self.pat_en = re.compile(r'^[0-9a-zA-Z]+$')  # english phrase or not
    self.re_list = (
      re.compile(r'([1-9]{1})(\d{18}|\d{16}|\d{15})'), # 银行卡
      re.compile(r'((\+|00)86)?1[3-9]\d{9}'), # 手机
      re.compile(r'\d{3}-\d{8}|\d{4}-\d{7}'), # 电话
    )

  def add(self, keyword):

    keyword = keyword.lower()
    if keyword not in self.kwsets:
      self.keywords.append(keyword)
      self.kwsets.add(keyword)
      index = len(self.keywords) - 1
      for word in keyword.split():
        if self.pat_en.search(word):
          self.bsdict[word].add(index)
        else:
          for char in word:
            self.bsdict[char].add(index)

  def parse(self, path):
    with open(path, 'r', encoding='UTF-8') as f:
      for keyword in f.readlines():
        self.add(keyword.strip())

  def filter(self, message, repl="*"):
    sen_text = ""
    ini_message = message.lower()
    message = message.lower()

    # 正则匹配
    for r in self.re_list:
      if r.search(message):
        message = r.sub(repl, message)

    for word in message.split():
      if self.pat_en.search(word):
        for index in self.bsdict[word]:
          message = message.replace(self.keywords[index], repl)
      else:
        for char in word:
          for index in self.bsdict[char]:
            message = message.replace(self.keywords[index], repl)

    if ini_message == message:
      sen_text = ""
    else:
      result_str = message.split(repl)
      for item in result_str:
        ini_message = ini_message.replace(item, "")
      sen_text = ini_message
    return message, sen_text


def filter_sen_txt(input_str):
  filter = BSFilter()
  filter.parse(os.getcwd() + "/paddleApp/sensi_words.txt")
  result, sen_text = filter.filter(input_str.replace('*', ''), repl="*")
  return result, sen_text


if __name__ == '__main__':
  text_item = '我是一个银行卡 6216606100004508323 sdf'
  r = re.compile(r'([1-9]{1})(\d{18}|\d{16}|\d{15})')  # 银行卡
  item_sen = r.sub('*', text_item)
  print(item_sen)
