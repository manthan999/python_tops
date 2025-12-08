import django
from django.conf import settings
from django.template import Engine, Context
import os

# Configure Django template settings manually (no project needed)
settings.configure(
    TEMPLATES=[
        {
            "BACKEND": "django.template.backends.django.DjangoTemplates",
            "DIRS": [os.path.join(os.path.dirname(__file__), "templates")],
        }
    ]
)

django.setup()

def render_html(template_name, context_data):
    # Load template engine
    engine = Engine(dirs=settings.TEMPLATES[0]["DIRS"])
    
    # Get the template
    template = engine.get_template(template_name)

    # Render with context
    return template.render(Context(context_data))


if __name__ == "__main__":
    html = render_html("hello.html", {"name": "ChatGPT"})
    print(html)
