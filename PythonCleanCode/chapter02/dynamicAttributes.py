class DynamicAttributes:
    def __init__(self, attribute):
        self.attribute = attribute

    def __getattr__(self, attr):
        if attr.startswith("fallback_"):
            name = attr.replace("fallback_", "'")

            return f"[fallback resolved] {name}"
        else:
            print("not fallback")

            # AttributeError를 발생시키지 않으면 "default" 값 대신 None 값을 반환
            raise AttributeError(f"{self.__class__.__name__} 에는 {attr} 속성이 없음")


dyn = DynamicAttributes("value")

result = getattr(dyn, "something", "default value")
print(result)
