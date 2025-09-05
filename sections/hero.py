from nicegui import ui,app


def render():
    # big container
    with ui.element("div").style("background-image: url(./assets/hero.jpg)").classes("h-screen w-screen flex flex-col bg-center justify-center items-center"):
        # navbar
        with ui.element("nav").classes("flex flex row justify-between w-screen fixed left-0 top-0 px-20 py-10"):
            #logo
            ui.label("LOGO").classes("text-white font-bold text-2xl") 

            #navlinks
           
            
            navLinks =[
                 {"title": "Home", "path":"/"},
                 {"title": "About" ,"path":"/"},
                 {"title":"Services","path":"/"},
                 {"title":"Membership","path":"/"},
                 {"title":"Contact","path":"/"},
                 {"title": "Gallery","path":"/"}
            ]
            with ui.row():
                for item in navLinks:
                    ui.link(item["title"], item["path"]).classes("no-underline uppercase")

            with ui.row().classes("text-4xl"):
                ui.icon("facebook")
                ui.icon("person") 
                ui.icon("notifications") 
                ui.icon("search") 
                ui.icon("people")
                
        

        # text
        with ui.element("div").classes("text-3xl text-white font-bold text-center"):
            ui.label("Welcome to").classes("text-4xl")
            ui.html("<hi>Fitness Arena</h1>").classes("text-7xl")
            ui.button("Look Menu")