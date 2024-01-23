
# Client часть
START               = '0000'
INFO                = '0001'
GET_ACCESSCODE      = '0011'
RESET_ACCESSCODE    = '0021'
AUTH                = '0002'
MENU                = '0003'
SETTINGS            = '0004'
TRAFFIC_ON          = '0005'
TRAFFIC_OFF         = 'xxxx'

BTN_AUTH = 'Авторизация'
BTN_INFO = 'Информация'

BTN_GET_ACCESSCODE = 'Получить'
BTN_RESET_ACCESSCODE = 'Восстановить'

BTN_ON = 'ON'
BTN_OFF = 'OFF'
BTN_SETTINGS = 'Настройки'

CLIENT_MSG = {
    TRAFFIC_ON: 'on'
}


# Server часть
CODE            = 'utf-8'            
CONNECT         = '9000'
SUCC_CONNECT    = '9900'
ERR_CONNECT     = '9x00'
SUCC_AUTH       = '9999'
ERR_AUTH        = '999x'

SEND_REQUEST    = '0***'
ERR_REQUEST     = 'x***'
REPORT          = '1***'
LATES_NEWS      = '!!!!'

REPORT_MSG = { 
    SUCC_CONNECT:   'succsessfull connection',
    ERR_CONNECT:    'error connection',
    SUCC_AUTH:      'succsessfull auth',
    ERR_AUTH:       'error auth',
    REPORT:         'send report',
    TRAFFIC_ON:     'confirm traffic ON',
    TRAFFIC_OFF:    'confirm traffic OFF'
}

REQUEST_MSG = {
    TRAFFIC_ON: 'request traffic ON',
    TRAFFIC_OFF: 'request traffic OFF'
}













