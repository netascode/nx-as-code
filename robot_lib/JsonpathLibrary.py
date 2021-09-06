#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
import jsonpath

class JsonpathLibrary(object):

    def get_items_by_path(self, json_object, json_path):
        match_object = jsonpath.jsonpath(json_object, json_path)
        match_string = json.dumps(match_object[0])
        return match_string

    def get_items_by_path_raw(self, json_object, json_path):
        match_object = jsonpath.jsonpath(json_object, json_path)
        return match_object[0]
