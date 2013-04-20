#!/usr/bin/env python

import os
import sys

try:
    from bottle import Bottle as App, abort, redirect, static_file
except ImportError:
    from flask import Flask as App, abort, redirect, send_from_directory
    static_file = lambda filename, root: send_from_directory(root, filename)

app = App(__name__)

with open('slide.html') as templatefile:
    template = templatefile.read()

slide_dir = sys.argv[1] if len(sys.argv) > 1 else 'slides'

slides = dict(enumerate(sorted((filename for filename in os.listdir(slide_dir) if filename.endswith('.html')), key = lambda filename: int(filename.split('/')[-1].split('.')[0]))))

@app.route('/static/<filename>')
def static(filename):
    return static_file(filename, slide_dir + '/static')

@app.route('/favicon.ico')
@app.route('/slide.png')
def favicon():
    return static_file('slide.png', '')

@app.route('/slide.css')
def css():
    return static_file('slide.css', '')

@app.route('/')
def index():
    return redirect('/0/')

@app.route('/<number>/')
def slide(number):
    num = int(number)
    if num not in slides:
        abort(404)
    return template.format(num, (num - 1) % len(slides), (num + 1) % len(slides), open(slide_dir + '/' + slides[num]).read())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=False)
