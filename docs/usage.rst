Usage
=====

Installation
------------

Install the package via pip:

.. code-block:: bash

   pip install django-quill-safe

Add to your Django project's settings:

.. code-block:: python

   INSTALLED_APPS = [
       # other apps
       'quillsafe',
   ]

Include Quill static files in your templates
--------------------------------------------

To enable the Quill editor UI, make sure to load Quill’s CSS and JS assets in your base template or relevant templates:

.. code-block:: django

   {% load static %}

   <link
       href="{% static 'quillsafe/quill.snow.min.css' %}"
       rel="stylesheet"
   />
   <script src="{% static 'quillsafe/quill.min.js' %}"></script>

Form Field and Widget
---------------------

Use the `QuillFormField` in your Django forms to safely handle Quill JSON delta content.

.. code-block:: python

   from django import forms
   from quillsafe.fields import QuillFormField

   class ArticleForm(forms.Form):
       content = QuillFormField()

Displaying Content Safely
-------------------------

To display the stored Quill delta content as HTML on templates without saving raw HTML, use the `quill_display` template tag.

Load the tag and use it as follows:

.. code-block:: django

   {% load quill_tags %}
   {% quill_display article.content %}

You can customize the appearance by styling the container or integrating Quill in read-only mode.

Handling Raw Data
-----------------

The field stores only the JSON delta format, not raw HTML, ensuring safer content management.

You can access and manipulate the raw delta JSON directly in your views or models.
