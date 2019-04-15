# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：    project_view.py
   Description :
   Author :       Hu Hang
   date：          2019/4/12
-------------------------------------------------
"""
__author__ = 'huahng'


from flask import Flask

from flask_restful import Resource, Api

from pyconfig.pyconfig_server.util.path_enum import path_enum

from pyconfig.pyconfig_server.server import config_project_inst


app = Flask(__name__)
api = Api(app)

class project_view(Resource):

    def get(self, project_name):
        ret = config_project_inst.get_project_info(project_name)
        res = {}
        for v in ret.get(path_enum.project_info.value + "/{project}".format(project=project_name), []):
           res.update({v['key'].split('/')[-1]: v['value']})
        return (res)


class get_all_project(Resource):

    def get(self):
        return config_project_inst.get_all_project()

api.add_resource(project_view, '/<string:project_name>')
api.add_resource(get_all_project, '/get_all')

if __name__ == '__main__':
    app.run(debug=True)