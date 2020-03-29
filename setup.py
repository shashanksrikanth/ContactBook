from setuptools import setup

setup(
    name='database-initialization',
    version='0.1',
    author_email='sshashank1999@gmail.com',
    package_data={},
    install_requires=['click'],
    entry_points={
        'console_scripts': ['database-initialization = contactbook.database:initialize_database']
    }
)

setup(
    name='register-user',
    version='0.1',
    author_email='sshashank1999@gmail.com',
    package_data={},
    install_requires=['click', 'werkzeug'],
    entry_points={
        'console_scripts': ['register-user = contactbook.register:register_user']
    }
)

setup(
    name='run-contactbook',
    version='0.1',
    author_email='sshashank1999@gmail.com',
    package_data={},
    install_requires=['click', 'werkzeug'],
    entry_points={
        'console_scripts': ['run-contactbook = contactbook.loginAndUse:run_commands']
    }
)