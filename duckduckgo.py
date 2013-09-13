import urllib
import urllib2
import json as j
import sys
from collections import namedtuple

__version__ = 0.242


def query(query, useragent='python-duckduckgo '+str(__version__), safesearch=True, html=False, meanings=True, **kwargs):
    """
    Query DuckDuckGo, returning a Results object.

    Here's a query that's unlikely to change:

    >>> result = query('1 + 1')
    >>> result.type
    'nothing'
    >>> result.answer.text
    '1 + 1 = 2'
    >>> result.answer.type
    'calc'

    Keword arguments:
    useragent: UserAgent to use while querying. Default: "python-duckduckgo %d" (str)
    safesearch: True for on, False for off. Default: True (bool)
    html: True to allow HTML in output. Default: False (bool)
    meanings: True to include disambiguations in results (bool)
    Any other keyword arguments are passed directly to DuckDuckGo as URL params.
    """ % __version__

    safesearch = '1' if safesearch else '-1'
    html = '0' if html else '1'
    meanings = '0' if meanings else '1'
    params = {
        'q': query,
        'o': 'json',
        'kp': safesearch,
        'no_redirect': '1',
        'no_html': html,
        'd': meanings,
        }
    params.update(kwargs)
    encparams = urllib.urlencode(params)
    url = 'http://api.duckduckgo.com/?' + encparams

    request = urllib2.Request(url, headers={'User-Agent': useragent})
    response = urllib2.urlopen(request)
    json = j.loads(response.read())
    response.close()

    return process_results(json)


Response = namedtuple('Response', ['type', 'api_version',
                                   'heading', 'result',
                                   'related', 'definition',
                                   'abstract', 'redirect',
                                   'answer'])

Result = namedtuple('Result', ['html',
                               'text', 'url',
                               'icon'])
Related = namedtuple('Related', ['html', 'text',
                                 'url', 'icon'])
Definition = namedtuple('Definition', ['primary','url', 'source'])

Abstract = namedtuple('Abstract', ['primary', 'url', 
                                   'text', 'source'])
Redirect = namedtuple('Redirect', ['primary',])
Icon = namedtuple('Icon', ['url', 'width', 'height'])
Topic = namedtuple('Topic',['name', 'results'])
Answer = namedtuple('Answer', ['primary', 'type'])




def result_deserialize(dataset, obj_type):
    d = dataset
    topics = None
    if 'Topics' in d:
        results = [result_deserialize(t, Result) for t in d['Topics']]
        return Topic(d['Name'], results=results)
    text = d['Text']
    url = d['FirstURL']
    html = d['Result']
    i_url = d['Icon']['URL']
    i_width = d['Icon']['Width']
    i_height = d['Icon']['Height']
    icon = None
    if i_url != '':
        icon = Icon(url=i_url, width=i_width,
                    height=i_height)
    dt = obj_type(text=text, url=url, html=html,
                      icon=icon)
    return dt



def search_deserialize(dataset, prefix, obj_type):
    keys = dataset.keys()
    required = filter(lambda x: x.startswith(prefix) and x != prefix, keys)
    unq_required = [r.split(prefix)[1].lower() for r in required]
    args = {ur: dataset[r] for ur, r in map(None, unq_required, required)}
    if prefix in dataset:
        args['primary'] = dataset[prefix]
    return obj_type(**args)



def process_results(json):
    resp_type = {'A': 'answer', 
                 'D': 'disambiguation',
                 'C': 'category',
                 'N': 'name',
                 'E': 'exclusive', 
                 '': 'nothing'}.get(json.get('Type',''), '')

    redirect = search_deserialize(json, 'Redirect', Redirect)
    abstract = search_deserialize(json, 'Abstract', Abstract)
    definition = search_deserialize(json, 'Definition', Definition)
    js_results = json.get('Results', [])
    results = [result_deserialize(jr, Result) for jr in js_results]
    js_related = json.get('RelatedTopics', [])
    related = [result_deserialize(jr, Related) for jr in js_related]
    answer = search_deserialize(json, 'Answer', Answer)
    return Response(type=resp_type, api_version=__version__,
                    heading='', redirect=redirect,
                    abstract=abstract,
                    definition=definition,
                    answer=answer,
                    related=related,
                    result=results)

def main():
    if len(sys.argv) > 1:
        q = query(' '.join(sys.argv[1:]))
        print q
    else:
        print('Usage: %s [query]' % sys.argv[0])

if __name__ == '__main__':
    main()
