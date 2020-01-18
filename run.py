import click
from application import create_app


@click.command()
@click.option('-h', '--host', help='Bind host', default='localhost', show_default=True)
@click.option('-p', '--port', help='Bind port', default=8000, type=int, show_default=True)
@click.option('-e', '--env', help='Running env, override environment FLASK_ENV.', default='development', show_default=True)
def main(**kwargs):
    app = create_app(kwargs['env'])
    app.run(host=kwargs['host'], port=kwargs['port'])


if __name__ == '__main__':
    main()
