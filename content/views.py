import datetime

from django.views.generic import TemplateView

from .utils import check_for_error, get_game_id


class HomePageTemplateView(TemplateView):
    template_name = "content/home.html"
    http_method_names = ["get", "post"]

    def get_context_data(self, *args, **kwargs):
        context = super(HomePageTemplateView, self).get_context_data()
        today = datetime.date.today()
        game_id = get_game_id(135, today)
        context["error"] = check_for_error(game_id, "Tatis Jr")[0]
        context["color"] = check_for_error(game_id, "Tatis Jr")[1]
        return context
