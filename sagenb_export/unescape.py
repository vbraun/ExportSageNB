

try:
    import HTMLParser
except ImportError:
    pass
else:
    unescape = HTMLParser.HTMLParser().unescape


try:
    import html
except ImportError:
    pass
else:
    unescape = html.unescape
        
    


