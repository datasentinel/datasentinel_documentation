from flask import Flask, send_from_directory
import os
import cherrypy

full_path = os.path.abspath(__file__)
dir_path = os.path.dirname(full_path)

app = Flask(__name__, static_url_path=dir_path)


@app.route('/<path:path>')
def send_files(path):

    if path == 
    return send_from_directory('_build/html', path)


if __name__ == "__main__":

    # app.run(port=8324)

    cherrypy.tree.graft(app, '/')

    config = {'server.socket_host': '0.0.0.0',
              'server.socket_port': 8324,
              'engine.autoreload.on': False,
              'log.screen': True,
              'log.access_file': '{}/doc_access.log'.format(dir_path),
              'log.error_file': '{}/doc_error_access.log'.format(dir_path),
              'thread_pool': 15
              }

    cherrypy.config.update(config)

    cherrypy.engine.start()
