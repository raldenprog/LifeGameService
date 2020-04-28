from route.Authentication import Authentication
from route.Cabinet import Cabinet
from route.Event import Event
from route.Favicon import Favicon
from route.Index import Index
from route.Logout import Logout
from route.News import News
from route.News import Comment
from route.Registration import RegistrationRoute
from route.Scoreboard import Scoreboard
from route.Task import Task

routes = {Index: '/',
          RegistrationRoute: '/registration',
          Authentication: '/auth',
          Task: '/task',
          Scoreboard: '/scoreboard',
          Event: '/event',
          Cabinet: '/cabinet',
          Logout: '/logout',
          Favicon: "/favicon.ico",
          News: "/news",
          Comment: "/comment"
          }
