from django.utils.encoding import force_unicode
from django.utils.safestring import mark_safe
from django import forms


class BootstrapRadioFieldRenderer(forms.widgets.RadioFieldRenderer):

    def render(self):
        """Outputs a <ul> for this set of radio fields."""
        return mark_safe(u'<ul class="list-inline">\n%s\n</ul>' %
                         u'\n'.join([u'<li>%s</li>'
                                     % force_unicode(w) for w in self]))