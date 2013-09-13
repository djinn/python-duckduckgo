from duckduckgo import query

def wikipedia_presence(text):
    """Find if a query has wikipedia article"""
    return query(text).abstract.url if query(text).abstract != None and query(text).abstract.source == 'Wikipedia' else None

if __name__ == '__main__':
    import sys
    print wikipedia_presence(' '.join(sys.argv[1:]))
