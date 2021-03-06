#! /usr/bin/env python

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand


import app


manager = Manager(app.app)
migrate = Migrate(app.app, app.db)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
