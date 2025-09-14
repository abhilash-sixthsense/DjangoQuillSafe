Usage
=====

Installation
------------

Install the package via pip:

.. code-block:: bash

    pip install django-quill-safe

Add 'quillsafe' to your Django project's INSTALLED_APPS in settings.py:

.. code-block:: python

    INSTALLED_APPS = [
        # other apps
        'quillsafe',
    ]

Enabling the Editor UI
----------------------

To enable the Quill editor UI, you must load the necessary CSS and JS assets in your templates. You have two options:

* **Use the included static files:** This library includes Quill version 2.0.3. The assets are bundled with the package and can be loaded using Django's `{% static %}` template tag.

* **Use a CDN:** You can also replace the local files with a direct CDN link if you prefer.

.. code-block:: django

    {% load static %}

    <link
        href="{% static 'quillsafe/quill.snow.min.css' %}"
        rel="stylesheet"
    />
    <script src="{% static 'quillsafe/quill.min.js' %}"></script>


Model Field
---------------------

To store the rich text content in your database, use the `QuillField` in your Django model. This field is essential as it handles the secure serialization and deserialization of the Quill delta JSON.

.. code-block:: python

    from quillsafe.fields import QuillField

    class Article(models.Model):
        title = models.CharField(max_length=255)
        content = QuillField()

        def __str__(self):
            return str(self.title)

Form Field & Usage
------------------

Use the `QuillFormField` in your Django forms to safely handle Quill's JSON delta content. This form field can be rendered just like any other Django form field, for example:

.. code-block:: python

    from django import forms
    from quillsafe.fields import QuillFormField

    class ArticleForm(forms.Form):
        content = QuillFormField()

.. code-block:: django

    {{ form }}
    {{ form.as_p }}
    {{ form|crispy }}

Displaying Content in a Read-Only View
---------------------------------------

To display the stored Quill delta content safely as HTML on templates, use the `quill_display` template tag. This tag renders the content within a read-only Quill editor, populating the data without any menu controls.

Load the tag and use it as follows:

.. code-block:: django

    {% load quill_tags %}
    {% quill_display article.content %}

You can customize the appearance by styling the container or integrating a custom Quill read-only mode in your templates.

Handling Raw Data
-----------------

The field stores content in the JSON delta format, not raw HTML. This design ensures safer content management by preventing unvalidated HTML from being stored directly in your database.

You can access and manipulate the raw delta JSON directly from your views or models if needed.
