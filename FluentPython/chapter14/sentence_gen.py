import re
import reprlib

RE_WORD = re.compile('\w+')


class Sentence:
    '''
    제너레이터 객체
    '''
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    # 제너레이터 함수
    def __iter__(self):
        for word in self.words:
            yield word

        return
