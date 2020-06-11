import re
import reprlib

RE_WORD = re.compile('\w+')


class Sentence:
    def __init__(self, text):
        self.text = text

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        # finditer()는 self.text에서 RE_WORD에 대응되는 단어들의 반복자인 MatchObject 객체를 생성
        # match.group() 메서드는 MatchObject 객체에서 매칭되는 텍스트를 추출
        for match in RE_WORD.finditer(self.text):
            yield match.group()

        # 제너레이터 표현식 사용
        # 호출자가 제너레이터 객체를 받는다.
        return (match.group() for match in RE_WORD.finditer(self.text))

