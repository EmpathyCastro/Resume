from flask_script import Manager

from receiver import app

manager = Manager(app)


if __name__ == '__main__':
    manager.run()
