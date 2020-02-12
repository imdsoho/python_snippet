def wrong_user_display(user_metadata:dict = {"name": "John", "age": 30}):
    print(id(user_metadata))

    name = user_metadata.pop("name")
    age = user_metadata.pop("age")

    return f"{name} ({age})"

#print(">", locals())
#print(">>", locals()['wrong_user_display'])

result = wrong_user_display()       # id(user_metadata) = 2696494217832
print(result)

data = {"name":"Jane", "age":25}
print(id(data))                     # id(user_metadata) = 2696494217904
result = wrong_user_display(data)   # id(user_metadata) = 2696494217904
print(result)

# ERROR
result = wrong_user_display()       # id(user_metadata) = 2696494217832

'''기본 값을 사용해 함수를 호출하면 기본 데이터로 사용될 사전을 한 번만 생성하고
user_metadata는 이것을 가리킨다.
이 값은 프로그램이 실행되는 동안에 계속 메모리에 남아있게 되는데 함수의 본체에서
객체를 수정한다.
두 번째 기본인자를 사용하는 함수 호출 시, 에러가 발생한다.
첫 번째 호출 시 key 값을 지워버렸기 때문이다.'''

