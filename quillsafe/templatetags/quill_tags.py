import uuid
import json
from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.simple_tag
def quill_display(content, height="50px"):
    quill_id = f"quill_display_{uuid.uuid4().hex[:8]}"

    try:
        json_content = json.dumps(content)
    except Exception:
        json_content = '{}'

    html = f"""
<div id="{quill_id}" style="border:1px solid #ccc; min-height: {height};"></div>
<script type="application/json" id="{quill_id}_data">
{json_content}
</script>

<script>
document.addEventListener("DOMContentLoaded", function() {{
    var container = document.getElementById("{quill_id}");
    var data = JSON.parse(document.getElementById("{quill_id}_data").textContent);
    var quill = new Quill(container, {{
      theme: "snow",
      readOnly: true,
      modules: {{ toolbar: false }}
    }});
    quill.setContents(data);
}});
</script>
"""
    return mark_safe(html)
