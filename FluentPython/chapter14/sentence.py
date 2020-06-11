import re
import reprlib

RE_WORD = re.compile('\w+')


class Sentence:
    '''
    1. 객체가 __iter__() 메서드를 구현하는지 확인. 이 메서드를 호출해서 반복자를 가져온다.
    2. __iter__() 메서드가 구현되어 있지 않지만 __getitem__()이 구현되어 있다면, 파이썬은 인덱스 0에서 시작해서 항목을 순서대로 반복자를 생성한다.
    3. 이 과정이 모두 실패하면 Type Error: '객체' object is not iterable 에러 발생
    '''
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __getitem__(self, index):
        return self.words[index]

    def __len__(self):
        return len(self.words)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

