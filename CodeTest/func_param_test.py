class UserDictClass():
    def __init__(*args, **kwargs):
        if not args:
            raise TypeError("descriptor '__init__' of 'UserDict' object "
                            "needs an argument")

        self, *args = args
        temp, *args = args
        #*args = args

        print("[TEMP] ", temp)
        print("[self]", self)

        if len(args) > 1:
            raise TypeError('expected at most 1 arguments, got %d' % len(args))

        if args:
            dict = args[0]
        elif 'dict' in kwargs:
            dict = kwargs.pop('dict')
            import warnings
            warnings.warn("Passing 'dict' as keyword argument is deprecated",
                          DeprecationWarning, stacklevel=2)
        else:
            dict = None

        self.data = {}

customDict = UserDictClass({"key":"value"})