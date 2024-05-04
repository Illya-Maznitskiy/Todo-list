from django import forms

from todo_app.models import Tag, Task


class TaskForm(forms.ModelForm):
    deadline = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={"type": "datetime-local"}),
        required=False
    )
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Task
        exclude = ["done"]
        widgets = {
            "content": forms.TextInput(attrs={"size": "30"}),
        }

        help_texts = {
            "content": "Write your task",
        }
