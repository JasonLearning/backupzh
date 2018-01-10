#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/10 下午8:52
# @Author  : Jason
# @File    : config.py

MARKDOWN = {
    'h1': ('\n# ', '\n'),
    'h2': ('\n## ', '\n'),
    'code': ('\n```\n', '\n```\n'),
    'ul': ('', ''),
    'ol': ('', ''),
    'li': ('- ', ''),
    'blockquote': ('\n> ', '\n'),
    'i': ('*', '*'),
    'b': ('**', '**'),
    'span': ('', ''),
    'p': ('\n', '\n'),
}

BlOCK_ELEMENTS = {
    'h1': '<h1.*?>(.*?)</h1>',
    'h2': '<h2.*?>(.*?)</h2>',
    'code': '<pre.*?><code.*?>(.*?)</code></pre>',
    'ul': '<ul.*?>(.*?)</ul>',
    'ol': '<ol.*?>(.*?)</ol>',
    'li': '<li.*?>(.*?)</li>',
    'blockquote': '<blockquote.*?>(.*?)</blockquote>',
    'i': '<i.*?>(.*?)</i>',
    'b': '<b.*?>(.*?)</b>',
    'span': '<span.*?>(.*?)</span>',
    'p': '<p\s.*?>(.*?)</p>',
    'img': '<img.*?src="(.*?)".*?>(.*?)</img>',
    'img_with_content': '<img.*?src="(.*?)".*?>(.*?)</img><figcaption>(.*?)</figcaption>',
}


DELETE_ELEMENTS = ['<span.*?>', '</span>', '<div.*?>', '</div>', '<br clear="none"/>', '<center.*?>', '</center>']
