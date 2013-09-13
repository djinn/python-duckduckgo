from duckduckgo import query

def calculate(text):
    """ There is bc but why not use web api to caculate"""
    return query(text).answer.primary if query(text).type != 'nothing' else None

if __name__ == '__main__':
    import sys
    print calculate(' '.join(sys.argv[1:]))
