from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.decorators.clickjacking import xframe_options_exempt


class LoggedInMixin(object):

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoggedInMixin, self).dispatch(*args, **kwargs)


class AllowIFrameMixin(object):

    @method_decorator(xframe_options_exempt)
    def dispatch(self, *args, **kwargs):
        return super(AllowIFrameMixin, self).dispatch(*args, **kwargs)