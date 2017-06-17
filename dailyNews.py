#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

import webbrowser

urls = [
    'https://news.ycombinator.com/',
    'https://techcrunch.com/'
]

for url in urls:
    webbrowser.open_new_tab(url)
