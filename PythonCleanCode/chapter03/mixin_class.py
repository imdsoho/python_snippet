from collections.abc import Iterable, Iterator, Container

class BaseTokenizer:
    def __init__(self, str_token):
        self.str_token = str_token

    def __iter__(self):
        print("1")
        # 컨테이너 객체의 __iter__() 메소드가 제너레이터로 구현되면,
        # __iter__()와 __next__() 메소드를 제공하는 이터레이터 객체를 자동으로 돌려줍니다.
        yield from self.str_token.split("-")

class UpperIterableMixin:
    def __iter__(self):
        print("2")
        return map(str.upper, super().__iter__())

class lowerIterableMixin:
    def __iter__(self):
        print("3")
        return map(str.lower, super().__iter__())

#class Tokenizer(BaseTokenizer): pass
#class Tokenizer(UpperIterableMixin): pass   # TypeError: object() takes no parameters

class Tokenizer(UpperIterableMixin, lowerIterableMixin, BaseTokenizer): pass
# 결과값 - ['ABCD', 'EFGH']

#class Tokenizer(lowerIterableMixin, UpperIterableMixin, BaseTokenizer): pass
# 결과값 - ['abcd', 'efgh']

tk = Tokenizer("abcd-EFGH")
for token in tk:
    print(token)

#print(Tokenizer.__mro__)
#print(issubclass(lowerIterableMixin, Iterable))

print(isinstance(tk.__iter__(), Iterator))



