from django import forms

from todo.models import Task, Tag


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            "content",
            "deadline",
            "tags",
        ]

    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(), widget=forms.CheckboxSelectMultiple, required=False
    )
    deadline = forms.DateField(
        widget=forms.DateInput(attrs={"type": "date"}), required=False
    )
