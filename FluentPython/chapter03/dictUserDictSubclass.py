class StrKeyDict0(dict):
    def __missing__(self, key):
        '''
        dict[k] 연산자를 사용하는 경우 __getitem__() 메서드 호출 시
        존재하지 않는 키 값을 처리
        '''
        print(f"{key} - 키 없음")

        if isinstance(key, str):
            print("key instance check")
            raise KeyError(key)

        return self[str(key)]

    def get(self, key, default=None):
        '''
        key가 없는 경우라도, __missing__() 호출하지 않음         
        '''
        print(f"get({key}) call")
        try:
            return self[key]
        except KeyError:
            return default

    def __contains__(self, key):
        '''
        key가 없는 경우라도, __missing__() 호출하지 않음         
        '''
        return key in self.keys() or str(key) in self.keys()

from collections import UserDict

class StrKeyDict(UserDict):
    def __missing__(self, key):
        print(f"{key} - 키 없음")

        if isinstance(key, str):
            print("key instance check")
            raise KeyError(key)

        return self[str(key)]

    def __contains__(self, key):
        return str(key) in self.data

    def __setitem__(self, key, item):
        self.data[str(key)] = item


#dict0 = StrKeyDict0([('2','two'), ('4','four')])
dict0 = StrKeyDict([('2','two'), ('4','four')])

print("[1] ", dict0[2])             #2 - 키 없음
                                    #[1]  two

print("[2] ", 2 in dict0)           # True

print("[3] ", dict0.get(2))         # two

print("[4] ", dict0.get(1, 999))    # key 없는 경우, default 999

#print("[5] ", dict0[1])             # 1 - 키 없음 (int type 키 검색 -> 키없음 -> str(key) 변환 -> 검색(*))
                                    # 1 - 키 없음 (str(key)로 변환하여 검색(*) - 키 없음 - KeyError 발생)
                                    # key instance check
                                    # KeyError: '1'



