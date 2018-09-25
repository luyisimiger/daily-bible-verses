import re

_p_remove_i = re.compile(r'{\\i (.*)}')
_p_remove_par = re.compile(r'\\par')


def _remove_i(text):
    return _p_remove_i.sub(r"\1", text)

def _remove_par(text):
    return _p_remove_par.sub(r"", text)

def to_plain_text(text):
    
    txt = text
    txt = _remove_i(txt)
    txt = _remove_par(txt)

    return txt
