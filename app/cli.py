import os
import subprocess
import click


def _run(cmd):
    subprocess.run(cmd, check=True)


def init_app(app):
    @app.cli.group()
    def translate():
        """Translation and localization commands."""
        pass

    @translate.command()
    @click.argument('lang')
    def init(lang):
        """Initialize a new language."""
        _run(['pybabel', 'extract', '-F', 'babel.cfg', '-k', '_', '-k', '_l', '-o', 'messages.pot', 'app'])
        _run(['pybabel', 'init', '-i', 'messages.pot', '-d', 'app/translations', '-l', lang])
        os.remove('messages.pot')

    @translate.command()
    def update():
        """Update all languages."""
        _run(['pybabel', 'extract', '-F', 'babel.cfg', '-k', '_', '-k', '_l', '-o', 'messages.pot', 'app'])
        _run(['pybabel', 'update', '-i', 'messages.pot', '-d', 'app/translations'])
        os.remove('messages.pot')

    @translate.command()
    def compile():
        """Compile all languages."""
        _run(['pybabel', 'compile', '-d', 'app/translations'])
