#Verion 1.1
#Author wendal(wendal1985@gmail.com)
#If you find a bug, pls mail me
#this module is design for Python 2.7, can convert by 2to3

import httplib,urllib

ERROR = 'HTTPSQS_ERROR'

GET_END = 'HTTPSQS_GET_END'

PUT_OK = 'HTTPSQS_PUT_OK'
PUT_ERROR = 'HTTPSQS_PUT_ERROR'
PUT_END = 'HTTPSQS_PUT_END'

RESET_OK = 'HTTPSQS_RESET_OK'
RESET_ERROR = 'HTTPSQS_RESET_ERROR'

MAXQUEUE_OK = 'HTTPSQS_MAXQUEUE_OK'
MAXQUEUE_CANCEL = 'HTTPSQS_MAXQUEUE_CANCEL'

SYNCTIME_OK = 'HTTPSQS_SYNCTIME_OK'
SYNCTIME_CANCEL = 'HTTPSQS_SYNCTIME_CANCEL'

NONE = ''

class Httpsqs(object):

    def __init__(self,host,port=1218):
        self.host = host
        self.port = port
    
    def get(self,poolName):
        return self.getResult({'opt': 'get', 'name': poolName})

    def put(self,poolName,data):
        conn = httplib.HTTPConnection(self.host,self.port)
        conn.request("POST", "/?"+urllib.urlencode({'opt': 'put', 'name': poolName}),data)
        r = conn.getresponse()
        if r.status == httplib.OK :
            data = r.read()
            return data
        return ''

    def status(self,poolName):
        return self.getResult({'opt': 'status', 'name': poolName})
    
    def status_json(self,poolName):
        return self.getResult({'opt': 'status_json', 'name': poolName})

    def reset(self,poolName):
        return self.getResult({'opt': 'reset', 'name': poolName})

    def maxlen(self,poolName,num):
        return self.getResult({'opt': 'maxqueue', 'name': poolName, 'num' : num})

    def synctime(self,poolName,num):
        return self.getResult({'opt': 'synctime', 'name': poolName, 'num' : num})

    def getResult(self,ps):
        try:
            conn = httplib.HTTPConnection(self.host,self.port)
            conn.request("GET", "/?"+urllib.urlencode(ps))
            r = conn.getresponse()
            if r.status == httplib.OK :
                data = r.read()
                return data
        except:
            print("FAIL to connect Httpsqs?")
        return ''

def isOK(data):
    if cmp(data,'') == 0 :
        return False
    if cmp(data,ERROR) == 0 :
        return False
    if cmp(data,GET_END) == 0 :
        return False
    if cmp(data,PUT_ERROR) == 0 :
        return False
    if cmp(data,RESET_ERROR) == 0 :
        return False
    if cmp(data,MAXQUEUE_CANCEL) == 0 :
        return False
    if cmp(data,SYNCTIME_CANCEL) == 0 :
        return False
    return True
    
