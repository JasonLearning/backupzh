#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/15 下午9:34
# @Author  : Jason
# @File    : test_MD.py

from src.parse import Tomd

t = """
<p>
<b>123</b>
</p>
<p><b><i>456</i></b></p>
<p><i>789</i></p>
<h2>123</h2>
<blockquote>456</blockquote>
<div class="highlight">
<pre>
<code class="language-text"><span></span>789
</code>
</pre>
</div>
<ol><li>1</li><li>2</li><li>3</li></ol>
<ul><li>4</li><li>5</li><li>6</li></ul>

<a target="_blank" href="http://link.zhihu.com/?target=http%3A//www.baidu.com" data-draft-node="block" data-draft-type="link-card" data-image="https://pic3.zhimg.com/v2-b15c113aeddbeb606d938010b88cf8e6_180x120.jpg" data-image-width="540" data-image-height="258" class="LinkCard">
<span class="LinkCard-backdrop" style="background-image:url(https://pic3.zhimg.com/v2-b15c113aeddbeb606d938010b88cf8e6_180x120.jpg);">
</span>
<span class="LinkCard-content"><span>
<span class="LinkCard-title" data-text="true">百度一下，你就知道</span>
<span class="LinkCard-meta">www.baidu.com</span>
</span>
<span class="LinkCard-imageCell">
<img class="LinkCard-image LinkCard-image--horizontal" alt="图标" src="https://pic3.zhimg.com/v2-b15c113aeddbeb606d938010b88cf8e6_180x120.jpg">
</span></span>
</a>

<a target="_blank" href="http://link.zhihu.com/?target=http%3A//www.baidu.com" data-draft-node="block" data-draft-type="link-card" data-image="https://pic3.zhimg.com/v2-b15c113aeddbeb606d938010b88cf8e6_180x120.jpg" data-image-width="540" data-image-height="258" class="LinkCard"><span class="LinkCard-backdrop" style="background-image:url(https://pic3.zhimg.com/v2-b15c113aeddbeb606d938010b88cf8e6_180x120.jpg);"></span><span class="LinkCard-content"><span><span class="LinkCard-title" data-text="true">百度一下，你就知道</span><span class="LinkCard-meta">www.baidu.com</span></span><span class="LinkCard-imageCell"><img class="LinkCard-image LinkCard-image--horizontal" alt="图标" src="https://pic3.zhimg.com/v2-b15c113aeddbeb606d938010b88cf8e6_180x120.jpg"></span></span></a>


<figure>
<noscript>&lt;img src="https://pic2.zhimg.com/v2-789ca25f333ce6c96f1319ba75008a2e_b.jpg" data-size="normal" data-rawwidth="200" data-rawheight="200" class="content_image" width="200"&gt;
</noscript>
<span><div data-reactroot="" class="VagueImage content_image" data-src="https://pic2.zhimg.com/50/v2-789ca25f333ce6c96f1319ba75008a2e_hd.jpg" style="width: 200px; height: 200px;"><div class="VagueImage-mask is-active"></div></div></span>
<figcaption>123</figcaption>
</figure>
<p><img src="http://www.zhihu.com/equation?tex=55%2F23" alt="55/23" eeimg="1"> </p>
<p></p>
"""

s = """<p><b>123</b></p><p><b><i>456</i></b></p><p><i>789</i></p><h2>123</h2><blockquote>456</blockquote><div class="highlight"><pre><code class="language-text"><span></span>789
</code></pre></div><ol><li>1</li><li>2</li><li>3</li></ol><ul><li>4</li><li>5</li><li>6</li></ul><a target="_blank" href="http://link.zhihu.com/?target=http%3A//www.baidu.com" data-draft-node="block" data-draft-type="link-card" data-image="https://pic3.zhimg.com/v2-b15c113aeddbeb606d938010b88cf8e6_180x120.jpg" data-image-width="540" data-image-height="258" class="LinkCard"><span class="LinkCard-backdrop" style="background-image:url(https://pic3.zhimg.com/v2-b15c113aeddbeb606d938010b88cf8e6_180x120.jpg);"></span><span class="LinkCard-content"><span><span class="LinkCard-title" data-text="true">百度一下，你就知道</span><span class="LinkCard-meta">www.baidu.com</span></span><span class="LinkCard-imageCell"><img class="LinkCard-image LinkCard-image--horizontal" alt="图标" src="https://pic3.zhimg.com/v2-b15c113aeddbeb606d938010b88cf8e6_180x120.jpg"></span></span></a><a target="_blank" href="http://link.zhihu.com/?target=http%3A//www.baidu.com" data-draft-node="block" data-draft-type="link-card" data-image="https://pic3.zhimg.com/v2-b15c113aeddbeb606d938010b88cf8e6_180x120.jpg" data-image-width="540" data-image-height="258" class="LinkCard"><span class="LinkCard-backdrop" style="background-image:url(https://pic3.zhimg.com/v2-b15c113aeddbeb606d938010b88cf8e6_180x120.jpg);"></span><span class="LinkCard-content"><span><span class="LinkCard-title" data-text="true">百度一下，你就知道</span><span class="LinkCard-meta">www.baidu.com</span></span><span class="LinkCard-imageCell"><img class="LinkCard-image LinkCard-image--horizontal" alt="图标" src="https://pic3.zhimg.com/v2-b15c113aeddbeb606d938010b88cf8e6_180x120.jpg"></span></span></a><figure><noscript>&lt;img src="https://pic2.zhimg.com/v2-789ca25f333ce6c96f1319ba75008a2e_b.jpg" data-size="normal" data-rawwidth="200" data-rawheight="200" class="content_image" width="200"&gt;</noscript><span><div data-reactroot="" class="VagueImage content_image" data-src="https://pic2.zhimg.com/50/v2-789ca25f333ce6c96f1319ba75008a2e_hd.jpg" style="width: 200px; height: 200px;"><div class="VagueImage-mask is-active"></div></div></span><figcaption>123</figcaption></figure><p><img src="http://www.zhihu.com/equation?tex=55%2F23" alt="55/23" eeimg="1"> </p><p></p>
"""
print(s[200:253])