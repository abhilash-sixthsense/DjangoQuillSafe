import json
from django.db import models
from django import forms
from django.core.exceptions import ValidationError
from .widgets import QuillWidget

class QuillFormField(forms.CharField):
    widget = QuillWidget

    def to_python(self, value):
        if not value:
            return {}
        if isinstance(value, dict):
            return value
        try:
            return json.loads(value)
        except json.JSONDecodeError:
            raise ValidationError("Enter valid JSON data.")

    def validate(self, value):
        super().validate(value)
        if not isinstance(value, dict):
            raise ValidationError("Invalid format for Quill Delta JSON.")


class QuillField(models.TextField):
    description = "Field to store Quill Delta JSON data"

    def from_db_value(self, value, expression, connection):
        if value is None:
            return {}
        try:
            return json.loads(value)
        except (ValueError, TypeError):
            return {}

    def to_python(self, value):
        if isinstance(value, dict):
            return value
        if value in [None, '']:
            return {}
        try:
            return json.loads(value)
        except (ValueError, TypeError):
            raise ValidationError("Invalid JSON data")

    def get_prep_value(self, value):
        if value is None:
            return ''
        if isinstance(value, dict):
            return json.dumps(value)
        return value

    def formfield(self, **kwargs):
        defaults = {'form_class': QuillFormField,"widget": QuillWidget}
        kwargs.update(defaults)
        return super().formfield(**kwargs)
