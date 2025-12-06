import datetime

from constance import config
from django.views.generic import TemplateView

from .utils import check_for_error, get_game_id


class HomePageTemplateView(TemplateView):
    template_name = "content/home.html"
    http_method_names = ["get", "post"]

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data()
        today = datetime.date.today()
        game_id = get_game_id(config.PLAYER_TEAM_ID, today)
        context["error"] = check_for_error(game_id, config.PLAYER_LAST_NAME)[0]
        context["color"] = check_for_error(game_id, config.PLAYER_LAST_NAME)[1]
        context["is_injured"] = config.IS_INJURED
        context["is_suspended"] = config.IS_SUSPENDED
        return context
