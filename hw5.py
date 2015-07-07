import sys

__author__ = 'stu'
from glob import glob
# import glob
import os
from dominate import document
from dominate.tags import *
from collections import defaultdict

dict_like = defaultdict(list)


def translate_to_html(text, dict_like):
    path = text[text.find('\\'):text.find('txt')]
    # print(path)
    name_html = os.listdir('html')
    if not os.path.exists('html'):
        os.mkdir('html')

    with document(title=path[1:-1])as doc:
        with open(text)as f:
            file = f.readlines()
        h1(file[0])
        for i in file[1:]:
            p(i)


        # ul(li(a(i,href=i))for i in name_html if i != path[1:-1]+'.html')
        ul(li(a(k, href='{}.html'.format(i))) for i, k in dict_like.items() if i != path[1:-1])

    with open('html' + path + 'html', 'w') as html_text:
        html_text.write(doc.render())

    return html_text


def trasfrom(folder):
    try:
        os.mkdir('html')
    except OSError:
        pass
    text = glob(folder + '/*.txt')
    for t in text:
        with open(t) as f:
            dict_like[t[t.find('\\')+1:t.find('.')]] = f.readline().strip()

    for path in text:
        html = translate_to_html(path, dict_like)


def read_cmdline():
    pass
    # if not sys.stdin.isatty():
    #     for i in sys.stdin.readlines()[3:]:
    #         print(i)
    #
    #    # sys.stdin.readlines()
    #
    # return sys.argv[1:]



def main():
    # file_names = read_cmdline()
    # print(file_names)
    trasfrom('index')
    # translate_to_html()
    pass


if __name__ == '__main__':
    main()
