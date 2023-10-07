from rest_framework.renderers import JSONRenderer


class CustomRenderer(JSONRenderer):
    """Кастомный рендерер для форматирования ответа API."""

    def render(self, data, accepted_media_type=None, renderer_context=None):
        """Рендеринг данных для API-ответа."""
        status_code = renderer_context["response"].status_code
        response = {"data": data}
        if not str(status_code).startswith("2"):
            response = data

        return super(CustomRenderer, self).render(
            response, accepted_media_type, renderer_context
        )
