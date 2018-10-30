suspicious_api_dict = {'telephonymanager': ['getsubscriberid','getline1number','getnetworkoperator','getsimoperatorname','getsimoperatorname','getsimserialnumber','getcallstate'],
                       'uuid':['tostring'],
                      'wifiinfo':['getmacaddress'],
                      'wifimanager':['getconnectioninfo','getwifistate'],
                      'locationmanager':['getlastknownlocation','requestlocationupdates'],
                      'contentresolver':['query','delete'],
                       #####
                      '/browser$':['NONE'],
                       #####
                      'android/provider/calllog$calls':['NONE'],
                      'android/provider/contacts$phones':['NONE'],
                      'android/provider/contactscontract$commondatakinds$phone':['NONE'],
                      'android/provider/contacts':['NONE'],
                       ######
                      'audio/media':['getcontenturiforpath'],
                      'images$media':['getcontenturi','insertimage','getbitmap'],
                      'video$media':['getcontenturi','getcontentresolver'],
                      'uri':['parse'],
                      'smsmanager':['getdefault','sendtextmessage','createfrompdu','getdisplaymessagebody','getmessagebody','getoriginatingaddress','getuserdata'],
                      'gsm/smsmanager':['sendtextmessage','createfrompdu','getdisplaymessagebody'],
                      'telephony/itelephony':['endcall'],
                      'audiorecord':['startrecording'],
                      'mediarecorder':['start','stop'],
                      'httpurlconnection':['getoutputstream'],
                      'urlconnection':['getinputstream','getoutputstream'],
                      'sslhttpsurlconnection':['getoutputstream'],
                      'client/httpclient':['execute'],
                      'client/defaulthttpclient':['execute'],
                      'jsonobject':['put'],
                      'devicepolicymanager':['isadminactive','locknow'],
                       #deviceadminreceiver
                      'deviceadminreceiver':['NONE'],
                      'assetmanager':['getassets'],
                      'dexclassloader':['loadclass'],
                       #'secureclassloader'
                      'secureclassloader':['NONE'],
                       #'urlclassloader'
                      'urlclassloader':['NONE'],
                      'runtime':['exec','getruntime'],
                      'system':['load','loadlibrary'],
                      'crypto/cipher':['dofinal','getinstance'],
                      'crypto/keygenerator':['generateKey'],
                       #'secretkeyspec'
                      'secretkeyspec':['NONE'],
                      'class':['getdeclaredmethod'],
                      'reflect/accessibleobject':['setaccessible'],
                      'pendingintent':['getbroadcast','abortbroadcast'],
                       #'fileoutputstream'
                      'fileoutputstream':['NONE'],
                      'zipoutputstream':['close'],
                      'packagemanager':['setcomponentenabledsetting'],
                      'environment':['getexternalstoragedirectory','getexternalstoragestate'],
                      'string':['equalsignorecase','split'],
                      'activitymanager':['restartpackage'],
                      'audiomanager':['setvibratesetting','setringermode'],
                      'context':['getsystemservice']}