import logging

import colorlog

handler = colorlog.StreamHandler()
handler.setFormatter(colorlog.ColoredFormatter(
    '%(log_color)s %(asctime)s [%(filename)s] %(levelname)s %(message)s',
    log_colors={
        'INFO': 'black',
        'DEBUG': 'cyan',
        'WARNING': 'yellow',
        'ERROR': 'red'
    }
))

log = colorlog.getLogger()
log.addHandler(handler)
log.setLevel(logging.DEBUG)