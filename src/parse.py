#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/10 下午9:12
# @Author  : Jason
# @File    : parse.py
import re
import os
from src.config import *


class Element:
    def __init__(self, start_pos, end_pos, content, tag, folder, is_block=False):
        self.start_pos = start_pos
        self.end_pos = end_pos
        if len(content) == 1:
            self.content = content[0]
        else:
            self.content = content
        self._elements = []
        self.is_block = is_block
        self.tag = tag
        self.folder = folder
        self._result = None

        if self.is_block:
            self.parse_inline()

    def __str__(self):
        try:
            wrapper = MARKDOWN.get(self.tag)
            self._result = '{}{}{}'.format(wrapper[0], self.content, wrapper[1])
        except Exception as e:
            print(e)
            self._result = '\n' + self.content
        return self._result

    def parse_inline(self):
        if isinstance(self.content, tuple):
            if self.tag == 'link':
                self.content = '[{name}]({link})'.format(
                    name=self.content[0],
                    link=self.content[1],
                )
            if self.tag == 'img_with_content':
                self.content = '![{name}]({pic})'.format(
                    pic=self.content[0],
                    name=self.content[1],
                )
            self.tag = 'Fuck'
            return

        for m in re.finditer("<img(.*?)en_todo.*?>", self.content):
            # remove img and change to [ ] and [x]
            # evernote specific parsing
            img_src = re.search('src=".*?"', m.group())
            img_loc = img_src.group()[5:-1]  # remove source and " "
            img_loc = img_loc.replace('\\', '/')  # \\ folder slash rotate
            if os.stat(self.folder + "/" + img_loc).st_size < 250:
                self.content = self.content.replace(m.group(), "[ ] ")
            else:
                self.content = self.content.replace(m.group(), "[x] ")

        INLINE_ELEMENTS_LIST_KEYS.sort()
        for tag in INLINE_ELEMENTS_LIST_KEYS:
            pattern = BlOCK_ELEMENTS[tag]

            if tag == 'a':
                self.content = re.sub(pattern, '[\g<2>](\g<1>)', self.content)
            elif tag == 'img':
                self.content = re.sub(pattern, '![\g<2>](\g<1>)', self.content)
            elif tag == 'img_with_content':
                self.content = re.sub(pattern, '![\g<2>](\g<1>)', self.content)
            elif self.tag == 'ul' and tag == 'li':
                self.content = re.sub(pattern, '- \g<1>\n', self.content)
            elif self.tag == 'ol' and tag == 'li':
                self.content = re.sub(pattern, '1. \g<1>\n', self.content)

        self.content = self.content.replace('\r', '')
        self.content = self.content.replace('\xc2\xa0', ' ')
        self.content = self.content.replace('&quot;', '\"')


class Tomd:
    def __init__(self, html='', folder='', file='', options=None):
        self.html = str(html)  # actual data
        self.folder = folder
        self.file = file
        self.elements = []
        self.options = options  # haven't been implemented yet
        self._markdown = self.convert(self.options)

    def handle(self, tag, pattern):
        for m in re.finditer(pattern, self.html, re.I | re.S | re.M):
            # now m contains the pattern without the tag
            element = Element(start_pos=m.start(),
                              end_pos=m.end(),
                              content=m.groups(),
                              tag=tag,
                              folder=self.folder,
                              is_block=True)
            can_append = True
            fork_elements = self.elements
            for e in fork_elements:
                if e.start_pos <= m.start() and e.end_pos >= m.end():
                    can_append = False
                elif e.start_pos > m.start() and e.end_pos < m.end():
                    self.elements.remove(e)
            if can_append:
                self.elements.append(element)

    def convert(self, options=None):
        for tag, pattern in PRE_ELEMENTS.items():
            self.handle(tag, pattern)
        for tag, pattern in BlOCK_ELEMENTS.items():
            self.handle(tag, pattern)
        self.elements.sort(key=lambda ele: ele.start_pos)
        self._markdown = '\n'.join([str(e) for e in self.elements])

        for index, element in enumerate(DELETE_ELEMENTS):
            self._markdown = re.sub(element, '', self._markdown)
        self._markdown = self._markdown.replace('<b>', '**')
        self._markdown = self._markdown.replace('</b>', '**')
        self._markdown = self._markdown.replace('<i>', '*')
        self._markdown = self._markdown.replace('</i>', '*')
        return self._markdown

    @property
    def markdown(self):
        return self._markdown


if __name__ == "__main__":
    t = Tomd("""<p><b>123</b></p><p><b><i>456</i></b></p><p><i>789</i></p><h2>123</h2><blockquote>456</blockquote><div class="highlight"><pre><code class="language-text"><span></span>789
</code></pre></div><ol><li>1</li><li>2</li><li>3</li></ol><ul><li>4</li><li>5</li><li>6</li></ul><a target="_blank" href="http://link.zhihu.com/?target=http%3A//www.baidu.com" data-draft-node="block" data-draft-type="link-card" data-image="https://pic3.zhimg.com/v2-b15c113aeddbeb606d938010b88cf8e6_180x120.jpg" data-image-width="540" data-image-height="258" class="LinkCard"><span class="LinkCard-backdrop" style="background-image:url(https://pic3.zhimg.com/v2-b15c113aeddbeb606d938010b88cf8e6_180x120.jpg);"></span><span class="LinkCard-content"><span><span class="LinkCard-title" data-text="true">百度一下，你就知道</span><span class="LinkCard-meta">www.baidu.com</span></span><span class="LinkCard-imageCell"><img class="LinkCard-image LinkCard-image--horizontal" alt="图标" src="https://pic3.zhimg.com/v2-b15c113aeddbeb606d938010b88cf8e6_180x120.jpg"></span></span></a><a target="_blank" href="http://link.zhihu.com/?target=http%3A//www.baidu.com" data-draft-node="block" data-draft-type="link-card" data-image="https://pic3.zhimg.com/v2-b15c113aeddbeb606d938010b88cf8e6_180x120.jpg" data-image-width="540" data-image-height="258" class="LinkCard"><span class="LinkCard-backdrop" style="background-image:url(https://pic3.zhimg.com/v2-b15c113aeddbeb606d938010b88cf8e6_180x120.jpg);"></span><span class="LinkCard-content"><span><span class="LinkCard-title" data-text="true">百度一下，你就知道</span><span class="LinkCard-meta">www.baidu.com</span></span><span class="LinkCard-imageCell"><img class="LinkCard-image LinkCard-image--horizontal" alt="图标" src="https://pic3.zhimg.com/v2-b15c113aeddbeb606d938010b88cf8e6_180x120.jpg"></span></span></a><figure><noscript>&lt;img src="https://pic2.zhimg.com/v2-789ca25f333ce6c96f1319ba75008a2e_b.jpg" data-size="normal" data-rawwidth="200" data-rawheight="200" class="content_image" width="200"&gt;</noscript><span><div data-reactroot="" class="VagueImage content_image" data-src="https://pic2.zhimg.com/50/v2-789ca25f333ce6c96f1319ba75008a2e_hd.jpg" style="width: 200px; height: 200px;"><div class="VagueImage-mask is-active"></div></div></span><figcaption>123</figcaption></figure><p><img src="http://www.zhihu.com/equation?tex=55%2F23" alt="55/23" eeimg="1"> </p><p></p>
""")
    print(t.markdown)
