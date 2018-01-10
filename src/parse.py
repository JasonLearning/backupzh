#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/10 下午9:12
# @Author  : Jason
# @File    : parse.py
import re
import os
import warnings
from src.config import *


class Element:
    def __init__(self, start_pos, end_pos, content, tag, folder, is_block=False):
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.content = content
        self._elements = []
        self.is_block = is_block
        self.tag = tag
        self.folder = folder
        self._result = None

        if self.is_block:
            self.parse_inline()

    def __str__(self):
        wrapper = MARKDOWN.get(self.tag)
        self._result = '{}{}{}'.format(wrapper[0], self.content, wrapper[1])
        return self._result

    def parse_inline(self):
        self.content = self.content.replace('\r', '')  # windows \r character
        self.content = self.content.replace('\xc2\xa0', ' ')  # no break space
        self.content = self.content.replace('&quot;', '\"')  # html quote mark

        for m in re.finditer("<img(.*?)en_todo.*?>", self.content):
            # remove img and change to [ ] and [x]
            # evernote specific parsing
            imgSrc = re.search('src=".*?"', m.group())
            imgLoc = imgSrc.group()[5:-1]  # remove source and " "
            imgLoc = imgLoc.replace('\\', '/')  # \\ folder slash rotate
            if os.stat(self.folder + "/" + imgLoc).st_size < 250:
                self.content = self.content.replace(m.group(), "[ ] ")
            else:
                self.content = self.content.replace(m.group(), "[x] ")

        if "e_" in self.tag:  # evernote-specific parsing
            for m in re.finditer(BlOCK_ELEMENTS['table'], self.content, re.I | re.S | re.M):
                # hmm can there only be one table?
                inner = Element(start_pos=m.start(),
                                end_pos=m.end(),
                                content=''.join(m.groups()),
                                tag='table', folder=self.folder,
                                is_block=True)
                self.content = inner.content
                return  # no need for further parsing ?

            # if no table, parse as usual
            self.content = self.content.replace('<hr/>', '\n---\n')
            self.content = self.content.replace('<br/>', '')

        if self.tag == "table":  # for removing tbody
            self.content = re.sub(BlOCK_ELEMENTS['tbody'], '\g<1>', self.content)

        INLINE_ELEMENTS_LIST_KEYS = list(BlOCK_ELEMENTS.keys())
        INLINE_ELEMENTS_LIST_KEYS.sort()
        for tag in INLINE_ELEMENTS_LIST_KEYS:
            pattern = BlOCK_ELEMENTS[tag]

            if tag == 'a':
                self.content = re.sub(pattern, '[\g<2>](\g<1>)', self.content)
            elif tag == 'img':
                self.content = re.sub(pattern, '![\g<2>](\g<1>)', self.content)
            elif tag == 'img_single':
                self.content = re.sub(pattern, '![](\g<1>)', self.content)
            elif tag == 'img_single_no_close':
                self.content = re.sub(pattern, '![](\g<1>)', self.content)
            elif self.tag == 'ul' and tag == 'li':
                self.content = re.sub(pattern, '- \g<1>\n', self.content)
            elif self.tag == 'ol' and tag == 'li':
                self.content = re.sub(pattern, '1. \g<1>\n', self.content)
            elif self.tag == 'thead' and tag == 'tr':
                self.content = re.sub(pattern, '\g<1>\n', self.content.replace('\n', ''))
            elif self.tag == 'tr' and tag == 'th':
                self.content = re.sub(pattern, '|\g<1>', self.content.replace('\n', ''))
            elif self.tag == 'tr' and tag == 'td':
                self.content = re.sub(pattern, '|\g<1>|', self.content.replace('\n', ''))
                self.content = self.content.replace("||", "|")  # end of column also needs a pipe
            elif self.tag == 'table' and tag == 'td':
                self.content = re.sub(pattern, '|\g<1>|', self.content)
                self.content = self.content.replace("||", "|")  # end of column also needs a pipe
                self.content = self.content.replace('|\n\n', '|\n')  # replace double new line
                self.construct_table()
            else:
                wrapper = MARKDOWN.get(tag)
                if tag == "strong":
                    self.content = re.sub(pattern, '{}\g<2>{}'.format(wrapper[0], wrapper[1]), self.content)
                else:
                    self.content = re.sub(pattern, '{}\g<1>{}'.format(wrapper[0], wrapper[1]), self.content)

        if self.tag == "e_p" and self.content[-1:] != '\n' and len(self.content) > 2:
            # focusing on div, add new line if not there (and if content is long enough)
            self.content += '\n'

    def construct_table(self):
        # this function, after self.content has gained | for table entries,
        # adds the |---| in markdown to create a proper table

        temp = self.content.split('\n', 3)
        for elt in temp:
            if elt != "":
                count = elt.count("|")  # count number of pipes
                break
        pipe = "\n|"  # beginning \n for safety
        for i in range(count - 1):
            pipe += "---|"
        pipe += "\n"
        self.content = pipe + pipe + self.content + "\n"  # TODO: column titles?
        self.content = self.content.replace('|\n\n', '|\n')  # replace double new line
        self.content = self.content.replace("<br/>\n", "<br/>")  # end of column also needs a pipe


class Tomd:
    def __init__(self, html='', folder='', file='', options=None):
        self.html = html  # actual data
        self.folder = folder
        self.file = file
        self.options = options  # haven't been implemented yet
        self._markdown = self.convert(self.html, self.options)

    def convert(self, html="", options=None):
        if html == "":
            html = self.html
        # main function here
        elements = []
        for tag, pattern in BlOCK_ELEMENTS.items():
            for m in re.finditer(pattern, html, re.I | re.S | re.M):
                # now m contains the pattern without the tag
                element = Element(start_pos=m.start(),
                                  end_pos=m.end(),
                                  content=''.join(m.groups()),
                                  tag=tag,
                                  folder=self.folder,
                                  is_block=True)
                can_append = True
                for e in elements:
                    if e.start_pos < m.start() and e.end_pos > m.end():
                        can_append = False
                    elif e.start_pos > m.start() and e.end_pos < m.end():
                        elements.remove(e)
                if can_append:
                    elements.append(element)
        elements.sort(key=lambda element: element.start_pos)
        self._markdown = ''.join([str(e) for e in elements])

        for index, element in enumerate(DELETE_ELEMENTS):
            self._markdown = re.sub(element, '', self._markdown)
        return self._markdown

    @property
    def markdown(self):
        self.convert(self.html, self.options)
        return self._markdown

    def export(self, folder=False):
        if len(self.file) < 1:
            warnings.warn("file not specified, renamed to tmp.md")
            file = "tmp.md"
        else:
            file = self.file.replace('.html', '.md')  # rename to md
        if len(self.folder) < 2:
            warnings.warn("folder not specified, will save to pwd")
        elif not folder:
            file = self.folder + '/' + file
        else:  # if folder is specified
            file = folder + '/' + file
        f = open(file, 'w')
        f.write(self._markdown)
        f.close()


_inst = Tomd()
convert = _inst.convert
