import os, sys, zmq
from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
from pyramid.config import Configurator
from pyramid.events import NewRequest
from pyramid.session import UnencryptedCookieSessionFactoryConfig

from rundb import RunDb

def main(global_config, **settings):
  """ This function returns a Pyramid WSGI application.
  """
  session_factory = UnencryptedCookieSessionFactoryConfig('fishtest')
  config = Configurator(settings=settings,
                        session_factory=session_factory,
                        root_factory='fishtest.models.RootFactory')

  # Authentication
  with open(os.path.expanduser('~/fishtest.secret'), 'r') as f:
    secret = f.read()
  def groupfinder(username, request):
    return request.userdb.get_user_groups(username)
  config.set_authentication_policy(AuthTktAuthenticationPolicy(secret, callback=groupfinder, hashalg='sha512'))
  config.set_authorization_policy(ACLAuthorizationPolicy())

  context = zmq.Context()

  clop_socket = context.socket(zmq.PUB)
  clop_socket.bind('tcp://127.0.0.1:5001')

  rundb = RunDb(clop_socket=clop_socket)
  def add_rundb(event):
    event.request.rundb = rundb
    event.request.userdb = rundb.userdb
    event.request.clopdb = rundb.clopdb
    event.request.actiondb = rundb.actiondb
  config.add_subscriber(add_rundb, NewRequest)

  config.add_static_view('css', 'static/css', cache_max_age=3600)
  config.add_static_view('js', 'static/js', cache_max_age=3600)
  config.add_static_view('img', 'static/img', cache_max_age=3600)
  config.add_route('home', '/')
  config.add_route('login', '/login')
  config.add_route('signup', '/signup')
  config.add_route('users', '/users')
  config.add_route('actions', '/actions')
  config.add_route('tests', '/tests')
  config.add_route('tests_run', '/tests/run')
  config.add_route('tests_modify', '/tests/modify')
  config.add_route('tests_view', '/tests/view/{id}')
  config.add_route('tests_delete', '/tests/delete')
  config.add_route('tests_stop', '/tests/stop')
  config.add_route('tests_user', '/tests/user/{username}')

  # API
  config.add_route('api_request_task', '/api/request_task')
  config.add_route('api_update_task', '/api/update_task')
  config.add_route('api_failed_task', '/api/failed_task')
  config.add_route('api_stop_run', '/api/stop_run')
  config.add_route('api_request_build', '/api/request_build')
  config.add_route('api_build_ready', '/api/build_ready')
  config.add_route('api_request_version', '/api/request_version')
  config.add_route('api_request_clop', '/api/request_clop')

  config.scan()
  return config.make_wsgi_app()
