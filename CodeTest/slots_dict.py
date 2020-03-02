class A:
    __slots__ = ["package"]

    def __init__(self):
        self.package = "lab"

    def data(self):
        return self.package

class B:
    __slots__ = ["tool"]

    def __init__(self):
        self.tool = "tool"

    def function(self):
        return self.tool

#class C(B, A):
# 다중 상속시 하나의 부모 클래스만 __slots__을 가질 수 있다.
# TypeError: multiple bases have instance lay-out conflict
class C:
    #__slots__ = ["name"]

    __slots__ = ["name", "__dict__"]
    # slots에 "__dict__" 문자열을 추가하면 인스턴스 속성값을 추가할 수 있다
    # "__weakref__"도 추가할 수 있다.

    def __init__(self):
        self.name = "C"

    def method(self):
        pass

c = C()

# __slots__ 사용시 에러 - AttributeError: 'C' object has no attribute 'identifier'
c.identifier = "id-1234"
print(c.identifier)

#print(c.__dict__)   # {'name': 'C'}
print(c.__slots__)  # ['name']