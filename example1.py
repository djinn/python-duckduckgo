from duckduckgo import query, Topic
from sys import argv
visited = []

def build_web_tree(qr, depth=0):
    print ' '* depth * 4 + qr
    ds = query(qr)
    if depth == 2:
        return 
    if ds.error_code != 0:
        return 
    visited.append(qr)
    if ds.related == []:
        return 
    else:
         for r in ds.related:
             if isinstance(r, Topic) == True:
                 r_used = r.name.encode('ascii', 'ignore')
             else:
                 r_used = r.text.encode('ascii', 'ignore').split('-')[0].strip()
             try:
                 visited.index(r_used) 
             except:
                 build_web_tree(r_used, depth=depth+1)
         

if __name__ == '__main__':
    build_web_tree(' '.join(argv[1:]))
