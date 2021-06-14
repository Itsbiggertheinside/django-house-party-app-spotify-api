def safe_execute(returnable, *args):
    try:
        return returnable
    except Exception as e:
        return {'error': 'Error with issue {}'.format(e)}