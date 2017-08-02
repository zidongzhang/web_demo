# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
import json
from elasticsearch import Elasticsearch, RequestsHttpConnection

from googletrans import Translator
# Create your views here.

def index(request):
    template = loader.get_template('tag_profile/index.html')
    context = {}
    return HttpResponse(template.render(context, request))


def func_trans(str_in):
    translator = Translator()
   
    word_translate = translator.translate(str_in)

    return word_translate.text


def tag_search(request):

    es_client = Elasticsearch(
        hosts=[{'host': "", 'port': 443}],
        use_ssl=True,
        verify_certs=True,
        connection_class=RequestsHttpConnection
    )
    uuid = request.GET["uuid"]
    version = request.GET["version"]

    es_body = {
        "query" : {
            "bool": {
                "must": { "match": {"_id": uuid}
                        }
            }
        }
    }

    result = {}
    if version == "1":
        res = es_client.search(index="user_profile", body=es_body)
    elif version == "2":
        res = es_client.search(index="user_profile_v2", body=es_body)



    if "hits" not in res or "hits" not in res["hits"] or 0 >= len(res["hits"]["hits"]) :
        result["errno"] = 1
        if version == "1":
            result["result"] = "资料库①内没有这个用户"
        elif version == "2":
            result["result"] = "资料库②内没有这个用户"

    
    else:
        result["errno"] = 0
        result["result"] = res["hits"]["hits"][0]["_source"]
        
        for i in range(len(result["result"]["tag_profile"])):
            trans_result = func_trans(result["result"]["tag_profile"][i]["key"])
            result["result"]["tag_profile"][i]["translated"] = trans_result
    

    result = HttpResponse(json.dumps(result), content_type="application/json")

    return result


