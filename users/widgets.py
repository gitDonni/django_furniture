from django.forms.widgets import ClearableFileInput


class CustomClearableFileInput(ClearableFileInput):
    template_name = 'widgets/custom_input.html'

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        context['widget']['is_initial'] = bool(value)  # value — это текущий файл
        return context