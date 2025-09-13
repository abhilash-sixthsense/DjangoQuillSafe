from django.forms.widgets import Textarea
from django.utils.safestring import mark_safe
import json

class QuillWidget(Textarea):
    def render(self, name, value, attrs=None, renderer=None):
        if isinstance(value, (dict, list)):
            value = json.dumps(value, indent=2)
        if not attrs:
            attrs = {}

        # Hide the original textarea (inline style for maximum compatibility)
        existing_style = attrs.get('style', '')
        attrs['style'] = f"{existing_style} display:none;".strip()

        textarea_html = super().render(name, value, attrs, renderer)

        textarea_id = attrs.get('id', f'id_{name}')
        quill_div_id = f'quill-editor-{name}'

        html = f'''
<div>
  <div id="{quill_div_id}" style="height: 300px; border: 1px solid #ccc; margin-top: 0.5em;"></div>
  {textarea_html}
</div>

<script>
  document.addEventListener("DOMContentLoaded", function() {{
    var quill = new Quill("#{quill_div_id}", {{
      theme: "snow"
    }});

    var textarea = document.getElementById("{textarea_id}");
    try {{
      var delta = JSON.parse(textarea.value);
      quill.setContents(delta);
    }} catch(e) {{
      quill.setText("");
    }}

    quill.on("text-change", function(delta, oldDelta, source) {{
      textarea.value = JSON.stringify(quill.getContents());
    }});
  }});
</script>
'''
        return mark_safe(html)
