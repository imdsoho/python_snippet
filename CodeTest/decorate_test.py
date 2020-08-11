
def route(rule, **options):
    print('[route]')

    def decorator(f):
        endpoint = options.pop("endpoint", None)
        add_url_rule(rule, endpoint, f, **options)

        print('[decorator]', type(f), f)
        return f

    return decorator


def add_url_rule(
        rule,
        endpoint=None,
        view_func=None,
        provide_automatic_options=None,
        **options):
    print('[add_url_rule]', rule, endpoint, view_func, provide_automatic_options, options)


@route("/", endpoint='hello', methods = ['GET'])
def index():
    print('[index]')


if __name__ == '__main__':
    print('[main]')
    index()
