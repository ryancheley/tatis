import datetime

from django.views.generic import TemplateView

from .utils import check_for_error, get_game_id
from .models import InjuredList, SuspendedList


class HomePageTemplateView(TemplateView):
    template_name = "content/home.html"
    http_method_names = ["get", "post"]

    def get_context_data(self, *args, **kwargs):
        context = super(HomePageTemplateView, self).get_context_data()
        today = datetime.date.today()
        game_id = get_game_id(135, today)
        is_injured = InjuredList.objects.get_or_create(pk=1)[0]
        is_suspended = SuspendedList.objects.get_or_create(pk=1)[0]
        context["error"] = check_for_error(game_id, "Tatis Jr")[0]
        context["color"] = check_for_error(game_id, "Tatis Jr")[1]
        context["is_injured"] = is_injured.is_injured
        context["is_suspended"] = is_suspended.is_suspended
        return context
