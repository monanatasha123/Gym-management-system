from nicegui import ui,app
from sections import hero,welcome

# Expose the ssets folder to the nicegui server
app.add_static_files("/assets", "assets")

ui.add_head_html('<link rel="stylesheet" href="/assets/reset.css" />')
hero.render()

ui.run()