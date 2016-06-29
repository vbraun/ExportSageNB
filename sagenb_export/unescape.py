
try:
    # python 3
    from html import unescape
except ImportError:
    # python 2
    import HTMLParser
    unescape = HTMLParser.HTMLParser().unescape
