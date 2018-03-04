import argparse
import os
import shutil
import sys
import copy
import nbformat
from nbconvert import MarkdownExporter


def replace_by_dict(string, dic):
    pattern = re.compile(r'\b(' + '|'.join(dic.keys()) + r')\b')
    result = pattern.sub(lambda x: dic[x.group()], string)
    return result


def strip_code_source(cell):
    if cell['cell_type'] == 'code':
        newcell = copy.deepcopy(cell)
        newcell['source'] = ''
        return newcell
    else:
        return cell


def convert(notebook_fname):
    root = '..'
    basename, ext = os.path.splitext(notebook_fname)
    title = basename[11:].replace('-', ' ')

    header = [
         "---"
        ,"title: " + title
        ,"layout: post"
        ,"---"
    ]

    asset_dir = '/assets/posts/' + basename
    asset_realpath = root + asset_dir + '/'
    if not os.path.exists(asset_realpath):
        os.makedirs(asset_realpath)

    post_dir = '/_posts'
    post_realpath = root + post_dir


    strip_code = True
    notebook = nbformat.read(notebook_fname, as_version=4)

    if strip_code:
        notebook['cells'] = [strip_code_source(c) for c in notebook['cells']]

    exporter = MarkdownExporter()
    body, resources = exporter.from_notebook_node(notebook)

    if strip_code:
        body = body.replace('```python\n\n```', '')

    output_paths = {k: asset_dir + '/' +  k for k in resources['outputs'].keys()}
    newbody = replace_by_dict(body, output_paths)
    markdown_lines = header + newbody.split('\n')

    for fname, data in resources['outputs'].items():
        with open(asset_realpath + fname, 'wb') as f:
            f.write(data)

    markdown_fname = basename + '.md'
    with open(markdown_fname, 'w') as mdfile:
        mdfile.write('\n'.join(markdown_lines))

    shutil.move(markdown_fname, post_realpath + '/' + markdown_fname)
    
    
    
def main():    
    parser = argparse.ArgumentParser()
    parser.add_argument('notebooks', nargs='*', help='Name(s) of notebooks to convert.')
    parser.add_argument('--strip-code', action='store_true', default=False
                        , help='Flag to remove code from Markdown output.')


    args = parser.parse_args()
    print(args)
    
if __name__ == '__main__':
    main()