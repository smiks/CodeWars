class Test:
    def __init__(self): pass

    @staticmethod
    def assert_equals(a, b, msg=None):
        if a != b:
            if msg is not None:
                print(msg)
            else:
                print("{0} should be {1} " . format(a, b))
        else:
            print("OK ", a)

    def assert_not_equals(a, b, msg=None):
        if a == b:
            if msg is not None:
                print(msg)
            else:
                print("{0} should be {1} " . format(a, b))
        else:
            print("OK ", a)

    @staticmethod
    def expect(a, msg=None):
        if not a:
            if msg is not None:
                print(msg)
            else:
                print("{0} should be {1} " . format(a, not a))
        else:
            print("OK ", a)

    @staticmethod
    def describe(msg):
        print("\n {0} \n " . format(msg))

    @staticmethod
    def it(msg):
        print("\n {0} \n " . format(msg))

    @staticmethod
    def expect_error(msg, f):
        try:
            f()
            print("\n {0} \n " . format(msg))
        except:
            print("OK")