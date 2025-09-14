# django-quill-safe

A simple and secure integration of the Quill rich text editor into Django projects, using the Quill Delta JSON format.

## Features

* **Secure Content Storage:** Stores and validates Quill Delta JSON in the database, not unsafe raw HTML.
* **Intuitive Integration:** Simple to integrate into any Django model with the `QuillField`.
* **Form Handling:** A dedicated `QuillFormField` and widget for seamless form handling.
* **Read-Only Display:** A `quill_display` template tag for safely rendering content in read-only views.
* **Bundled Assets:** Includes Quill 2.0.3 assets for easy static file integration.

## Installation

```bash
pip install django-quill-safe
````

Add `'quillsafe'` to your project's `INSTALLED_APPS` in `settings.py`:

```python
INSTALLED_APPS = [
    # ... other apps
    'quillsafe',
]
```

## Usage

### 1\. Model Field

To store the rich text content in your database, use the `QuillField` in your Django model. This field is essential as it handles the secure serialization and deserialization of the Quill delta JSON.

```python
from django.db import models
from quillsafe.fields import QuillField

class Article(models.Model):
    title = models.CharField(max_length=255)
    content = QuillField()

    def __str__(self):
        return str(self.title)
```

### 2\. Forms

Use the `QuillFormField` in your Django forms to safely handle Quill's JSON delta content. This form field can be rendered just like any other Django form field.

```python
from django import forms
from quillsafe.fields import QuillFormField

class ArticleForm(forms.Form):
    content = QuillFormField()
```

The form can then be rendered in your template using standard Django template tags:

```django
{{ form }}
{{ form.as_p }}
{{ form|crispy }}
```

### 3\. Enabling the Editor UI

To enable the Quill editor UI in your templates, you must load the necessary CSS and JS assets. You have two options:

  * **Use the included static files:** This library includes Quill version 2.0.3. The assets are bundled with the package and can be loaded using Django's `{% static %}` template tag.

  * **Use a CDN:** You can also replace the local files with a direct CDN link if you prefer.

<!-- end list -->

```django
{% load static %}

<link
    href="{% static 'quillsafe/quill.snow.min.css' %}"
    rel="stylesheet"
/>
<script src="{% static 'quillsafe/quill.min.js' %}"></script>
```

### 4\. Displaying Content in a Read-Only View

To display the stored Quill delta content safely as HTML on templates, use the `quill_display` template tag. This tag renders the content within a read-only Quill editor, populating the data without any menu controls.

First, load the tag in your template and then use it as follows:

```django
{% load quill_tags %}
{% quill_display article.content %}
```

## Data Handling & Security

The `QuillField` stores content in the JSON delta format, not raw HTML. This design is crucial for security as it prevents unvalidated HTML from being stored directly in your database. You can access and manipulate the raw delta JSON directly from your views or models if needed.

## License

[](https://opensource.org/licenses/MIT)

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```
```
