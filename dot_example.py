from duckduckgo import query, Topic
from sys import argv
visited = []
depth_color = {
    0: 'green', 
    1: '#A52A2A',
    2: 'grey',
    3: 'blue'
    }

def build_web_tree(node, qr, depth=0):
    cooked_qr = qr.replace('"', '\\"')
    print '"%s" [label="%s", shape="hexagon", style="filled", color="%s"];' % (cooked_qr, cooked_qr, depth_color[depth])
    if node != None:
        print '"%s" -> "%s";' % (node, cooked_qr)
    ds = query(qr)
    if depth == 3:
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
                 build_web_tree(qr, r_used, depth=depth+1)
         

if __name__ == '__main__':
    print """digraph G {
               ranksep=3;
               ratio=auto;"""
    build_web_tree(None, ' '.join(argv[1:]))
    print "}"
