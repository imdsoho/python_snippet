from collections.abc import Sequence
from collections import UserDict
from datetime import datetime
from collections.abc import Iterable, Iterator, Sequence

class NotGoodTransactionalPolicy(UserDict):
    def change_in_policy(self, customer_id, **new_policy_data):
        self[customer_id].update(**new_policy_data)

user_data = {"fee":100.0, "expiration_date":datetime(2020, 1, 2)}
policy = NotGoodTransactionalPolicy({"client001": user_data})

print(policy["client001"])

class GoodTransactionalPolicy():
    def __init__(self, policy_data, **extra_data):
        self._data = {**policy_data, **extra_data}

    def change_in_policy(self, customer_id, **new_policy_data):
        self._data[customer_id].update(**new_policy_data)

    def __getitem__(self, customer_id):
        # 인스턴스["key"] 으로 값을 사용한다. - 반드시 필요
        return self._data[customer_id]

    # __len__ 메소드는 없어도 오류 발생하지 않는다.
    def __len__(self):
        print("__len__")
        return len(self._data)


user_data = {"fee":200.0, "expiration_date":datetime(2020, 2, 1)}
goog_policy = GoodTransactionalPolicy({"client001": user_data})

print(goog_policy["client001"])


user_data = {"name":"python"}
class NewClassName:
    def __init__(self, data):
        self._data = {**data}

    def __getitem__(self, item):
        return self._data[item]

    def __len__(self):
        return len(self._data)


new_class = NewClassName({"user": user_data})
print(new_class['user'])
print(type(new_class))
print(isinstance(new_class, Iterator))      # False
print(isinstance(new_class, Iterable))      # False
print(isinstance(new_class, Sequence))      # False

