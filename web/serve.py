#!/usr/bin/env python3
"""Serves this folder at http://localhost:8765/ (a browser does not run the game from file://).
   python3 serve.py [port]"""
import functools
import http.server
import os
import sys

here = os.path.dirname(os.path.abspath(__file__))
port = int(sys.argv[1]) if len(sys.argv) > 1 else 8765
handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=here)
http.server.SimpleHTTPRequestHandler.extensions_map['.wasm'] = 'application/wasm'
if not os.path.exists(os.path.join(here, 'index.data')):
    print('index.data (the game files) is not in this folder yet: see README.txt')
with http.server.ThreadingHTTPServer(('127.0.0.1', port), handler) as server:
    print('Road Rash: open http://localhost:%d/   (Ctrl+C stops)' % port)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
