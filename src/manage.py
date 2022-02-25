import sys
import argparse
from flask.cli import FlaskGroup
from app import create_app, settings


application = create_app()

cli = FlaskGroup(application)


if __name__ == '__main__':
    parser_settings = argparse.ArgumentParser(add_help=False)
    parser = argparse.ArgumentParser(prog=f"{sys.argv[0].split(settings.FILEPATH_SEPERATOR)[-1]}", description=f"{settings.PROJECT_NAME} {settings.VERSION}")
    parser.version = settings.VERSION
    parser.add_argument('-v', '--version', action='version', version=settings.VERSION)

    parser.add_argument(
                        dest='command',
                        nargs='*',
                        type=str,
                        default=None,
                        help=f"command, default: None"
                    )
    parser.add_argument(
                        '-host',
                        '--host',
                        dest='host',
                        default='0.0.0.0',
                        required=False,
                        help=f"host, default: 0.0.0.0"
                    )   
    parser.add_argument(
                        '-port',
                        '--port',
                        dest='port',
                        default=5000,
                        required=False,
                        help=f"host, default: 5000"
                    )                                      
    parser.add_argument(
                        '-d',
                        '--debug', 
                        dest='debug',
                        action='store_true',
                        default=not settings.DEBUG,
                        required=False,
                        help=f"Run server with debug mode, default: {settings.DEBUG}"
                    )

    args = parser.parse_args(sys.argv[1:])
    if args.command==['runserver']:
       application.run(debug=args.debug, host=args.host, port=args.port)
    
    else:
        print("##")
        application.app_context().push()
        cli(args.command)    



#python manage.py db upgrade e5a27228f45b
