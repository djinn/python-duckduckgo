==================
python-duckduckgo
==================

A Python library for querying the DuckDuckGo API.

Copyright Michael Stephens <me@mikej.st>, released under a BSD-style license.

Source: http://github.com/djinn/python-duckduckgo
Original Source: http://github.com/crazedpsyc/python-duckduckgo
Original Original Source: http://github.com/mikejs/python-duckduckgo (outdated)

This version has been forked from the original to be able to allow cleaner interface. It extensively uses namedtuples instead of data classes. This API only interfaces with JSON API

Installation
============

To install run

    ``python setup.py install``

Usage
=====

    >>> import duckduckgo
    >>> r = duckduckgo.query('DuckDuckGo')
    >>> r.type
    'answer'
    >>> r.result[0]
    Result(html=u'<a href="https://duckduckgo.com/">Official site</a><a href="https://duckduckgo.com/"></a>', text=u'Official site', url=u'https://duckduckgo.com/', icon=Icon(url=u'https://i.duckduckgo.com/i/duckduckgo.com.ico', width=16, height=16))
    >>> r.result[0].text
    u'Official site'
    >>> r.abstract
    Abstract(primary=u'DuckDuckGo is an Internet search engine that uses information from many sources, such as crowdsourced websites like Wikipedia and from partnerships with other search engines like Yandex, Yahoo!, Bing and WolframAlpha to obtain its results.', url=u'https://en.wikipedia.org/wiki/DuckDuckGo', text=u'DuckDuckGo is an Internet search engine that uses information from many sources, such as crowdsourced websites like Wikipedia and from partnerships with other search engines like Yandex, Yahoo!, Bing and WolframAlpha to obtain its results.', source=u'Wikipedia')
    >>> r.abstract.url
    u'https://en.wikipedia.org/wiki/DuckDuckGo'
    >>> r.abstract.source
    u'Wikipedia'
 
    >>> r = duckduckgo.query('Python')
    >>> r.type
    u'disambiguation'
    >>> r.related[1].text
    u'Python (programming language), a computer programming language'
    >>> r.related[1].url
    u'http://duckduckgo.com/Python_(programming_language)'
    >>> r.related[7].topics[0].text # weird, but this is how the DDG API is currently organized
    u'Armstrong Siddeley Python, an early turboprop engine'

    >>> r = duckduckgo.query('1 + 1')
    >>> r.type
    'exclusive'
    >>> r.answer.primary
    u'1 + 1 = 2'
    >>> r.answer.type
    u'calc'

    
    >>> print duckduckgo.query('how to spell test', html=True).answer.primary
<b>Test</b> appears to be spelled correctly!<br/><i>Suggestions:</i> <a href='/?q=define+test'>test</a> <a href='/?q=define+testy'>testy</a> <a href='/?q=define+teat'>teat</a> <a href='/?q=define+tests'>tests</a> <a href='/?q=define+rest'>rest</a> <a href='/?q=define+yest'>yest</a> .
The easiest method of quickly grabbing the best (hopefully) API result is to use duckduckgo.get_zci::
    
Special keyword args for query():
 - useragent   - string, The useragent used to make API calls. This is somewhat irrelevant, as they are not logged or used on DuckDuckGo, but it is retained for backwards compatibility.
 - safesearch  - boolean, enable or disable safesearch.
 - html        - boolean, Allow HTML in responses?

