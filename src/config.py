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
    'bi': ('**', '**'),
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
    'bi': '<b.*?><i.*?>(.*?)</i></b>',
    'i': '<i.*?>(.*?)</i>',
    'b': '<b.*?>(.*?)</b>',
    'span': '<span.*?>(.*?)</span>',
    'p': '<p\s.*?>(.*?)</p>',
    'img': '<img.*?src="(.*?)".*?>(.*?)</img>',
    'img_with_content': '<img.*?src="(.*?)".*?>(.*?)</img><figcaption>(.*?)</figcaption>',
}


DELETE_ELEMENTS = ['<span.*?>', '</span>', '<div.*?>', '</div>', '<br clear="none"/>', '<center.*?>', '</center>']
"""
MARKDOWN = {
    'h1': ('\n# ', '\n'),
    'h2': ('\n## ', '\n'),
    'h3': ('\n### ', '\n'),
    'h4': ('\n#### ', '\n'),
    'h5': ('\n##### ', '\n'),
    'h6': ('\n###### ', '\n'),
    'code': ('`', '`'),
    'ul': ('', ''),
    'ol': ('', ''),
    'li': ('- ', ''),
    'blockquote': ('\n> ', '\n'),
    'em': ('*', '*'),
    'strong': ('**', '**'),
    'block_code': ('\n```\n', '\n```\n'),
    'span': ('', ''),
    'p': ('\n', '\n'),
    'p_with_out_class': ('\n', '\n'),
    'inline_p': ('', ''),
    'inline_p_with_out_class': ('', ''),
    'b': ('**', '**'),
    'i': ('*', '*'),
    'del': ('~~', '~~'),
    'hr': ('\n---', '\n\n'),
    'thead': ('\n', '|------\n'),
    'tbody': ('\n', '\n'),
    'td': ('|', ''),
    'th': ('|', ''),
    'tr': ('', '\n'),
    'table': ('', '\n'),
    'e_p': ('', '\n')
}

BlOCK_ELEMENTS = {
    'h1': '<h1.*?>(.*?)</h1>',
    'h2': '<h2.*?>(.*?)</h2>',
    'h3': '<h3.*?>(.*?)</h3>',
    'h4': '<h4.*?>(.*?)</h4>',
    'h5': '<h5.*?>(.*?)</h5>',
    'h6': '<h6.*?>(.*?)</h6>',
    'hr': '<hr/>',
    'blockquote': '<blockquote.*?>(.*?)</blockquote>',
    'ul': '<ul.*?>(.*?)</ul>',
    'ol': '<ol.*?>(.*?)</ol>',
    'block_code': '<pre.*?><code.*?>(.*?)</code></pre>',
    'p': '<p\s.*?>(.*?)</p>',
    'p_with_out_class': '<p>(.*?)</p>',
    'thead': '<thead.*?>(.*?)</thead>',
    'tr': '<tr.*?>(.*?)</tr>'
}


INLINE_ELEMENTS = {
    'td': '<td.*?>((.|\n)*?)</td>',  # td element may span lines
    'tr': '<tr.*?>((.|\n)*?)</tr>',
    'th': '<th.*?>(.*?)</th>',
    'b': '<b.*?>(.*?)</b>',
    'i': '<i.*?>(.*?)</i>',
    'del': '<del.*?>(.*?)</del>',
    'inline_p': '<p\s.*?>(.*?)</p>',
    'inline_p_with_out_class': '<p>(.*?)</p>',
    'code': '<code.*?>(.*?)</code>',
    'span': '<span.*?>(.*?)</span>',
    'ul': '<ul.*?>(.*?)</ul>',
    'ol': '<ol.*?>(.*?)</ol>',
    'li': '<li.*?>(.*?)</li>',
    'img': '<img.*?src="(.*?)".*?>(.*?)</img>',
    'img_single': '<img.*?src="(.*?)".*?/>',
    'img_single_no_close': '<img.*?src="(.*?)".*?>',
    'a': '<a.*?href="(.*?)".*?>(.*?)</a>',
    'em': '<em.*?>(.*?)</em>',
    'strong': '<strong.*?>(\s*)(.*?)(\s*)</strong>',
    'tbody': '<tbody.*?>((.|\n)*)</tbody>',
}

DELETE_ELEMENTS = ['<span.*?>', '</span>', '<div.*?>', '</div>', '<br clear="none"/>', '<center.*?>', '</center>']
"""
