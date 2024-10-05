class MeuError(Exception):
    ...
class OutroError(Exception):
    ...
def levantar():
    exception_ = MeuError('a', 'b', 'c')
    exception_.add_note('nota 1')
    raise exception_
try:
    levantar()
except (MeuError, ZeroDivisionError) as error:
    print(error.__class__.__name__)
    print(error.args)
    print()
    exception_ = OutroError('Vou lançar de novo')
    raise exception_ from error