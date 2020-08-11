from collections import abc


class FrozenJSON:
    def __init__(self, mapping):
        self.__data = dict(mapping)

    def __getattr__(self, name):
        # print(type(self.__data))
        # print(dir(self.__data))

        if hasattr(self.__data, name):
            return getattr(self.__data, name)
        else:
            return FrozenJSON.build(self.__data[name])

    @classmethod
    def build(cls, obj):
        if isinstance(obj, abc.Mapping):            # dict
            # print('type : abc.Mapping')
            return cls(obj)
        elif isinstance(obj, abc.MutableSequence):  # list
            # print('type : abc.MutableSequence')
            return [cls.build(item) for item in obj]
        else:
            return obj
