print('모듈 실행')


def function():
    print("일반 def()")


def route():
    print("데코레이터 함수 생성")

    def decorator(f):
        print("데코레이터 함수 내부")
        return f

    return decorator


@route()
def call_decorator():
    print("데코레이터 함수 사용 함수")


class MyClass():
    def __init__(self):
        print("클래스 생성")


def main():
    print("메인 메소드 호출")
    my_cls = MyClass()


if __name__ == "__main__":
    print("프로그램 시작")

    main()
    function()

