from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from common.libs.ViewQueries import ViewQueries
from .forms import LoginForm
from monkey.libs.loggers import logger


def index(request: HttpRequest):
    # vq = IndexViewQuery(request)
    return render(request, 'user/index.html', {
    })


def login(request: HttpRequest):
    if request.user.is_authenticated:
        return redirect(request, '')

    def response(message: str = '', *, hide_error=False):
        return render(request, 'user/index.html', {
            'form': form,
            'message': message,
            'hide_error': hide_error,
        })

    # postのときはログイン処理を行っているとみなして対応
    form = None
    if request.method == 'GET':
        logger.info('get')
        form = LoginForm(request.GET)
        return response(hide_error=True)

    if request.method == 'POST':
        logger.info('post')
        form = LoginForm(request.POST)

        if not form.is_valid():
            return response('入力に問題があります')

        # 認証
        logger.info('post2')
        user = authenticate(
            request,
            username=form['username'].value(),
            password=form['password'].value())

        logger.info('post3')
        if not user:
            return response('username または passwordが違います')

        # ログインしてリダイレクト
        logger.info('post4')
        django_login(request, user)
        return redirect(form['next'].value())

    logger.info('post99')
    return response()


def logout(request: HttpRequest):
    django_logout(request)
    return redirect('/')
