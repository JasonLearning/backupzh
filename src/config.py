#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/10 下午8:52
# @Author  : Jason
# @File    : config.py

MARKDOWN = {
    'h1': ('\n# ', ''),
    'h2': ('\n## ', ''),
    'code': ('\n```\n', '\n```\n'),
    'ul': ('', ''),
    'ol': ('', ''),
    'li': ('- ', ''),
    'blockquote': ('\n> ', ''),
    'i': ('*', '*\n'),
    'b': ('**', '**\n'),
    'bi': ('**', '**\n'),
    'p': ('\n', '\n'),
}

PRE_ELEMENTS = {
    'bi': '<b><i>(.*?)</i></b>',
    'ul': '<ul.*?>(.*?)</ul>',
    'ol': '<ol.*?>(.*?)</ol>',
}

BlOCK_ELEMENTS = {
    'h1': '<h1.*?>(.*?)</h1>',
    'h2': '<h2.*?>(.*?)</h2>',
    'code': '<pre.*?><code.*?>(.*?)</code></pre>',
    'li': '<li.*?>(.*?)</li>',
    'blockquote': '<blockquote.*?>(.*?)</blockquote>',
    'i': '<i.*?>(.*?)</i>',
    'b': '<b.*?>(.*?)</b>',
    'p': '<p>     (.*?)</p>',
    'link': '<a.*?>.*?<span class="LinkCard-title".*?>(.*?)</span>.*?<span class="LinkCard-meta">(.*?)</span>.*?</a>',
    'latex': '<img.*?alt="(.*?)".*?>',
    'img_with_content': '<noscript>.*?src="(.*?)".*?</noscript>.*?<figcaption>(.*?)</figcaption>',
}

INLINE_ELEMENTS_LIST_KEYS = list(BlOCK_ELEMENTS.keys())
DELETE_ELEMENTS = ['<span.*?>', '</span>', '<div.*?>', '</div>']
