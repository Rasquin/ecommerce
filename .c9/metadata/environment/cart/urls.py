{"filter":false,"title":"urls.py","tooltip":"/cart/urls.py","undoManager":{"mark":0,"position":0,"stack":[[{"start":{"row":0,"column":0},"end":{"row":7,"column":1},"action":"insert","lines":["from django.conf.urls import url","from .views import view_cart, add_to_cart, adjust_cart","","urlpatterns = [","    url(r'^$', view_cart, name='view_cart'),","    url(r'^add/(?P<id>\\d+)', add_to_cart, name='add_to_cart'),","    url(r'^adjust/(?P<id>\\d+)', adjust_cart, name='adjust_cart'),","]"],"id":1}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":3,"column":15},"end":{"row":3,"column":15},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1568969628174,"hash":"088683e10f32385107b83cf421c2135ce3d84560"}