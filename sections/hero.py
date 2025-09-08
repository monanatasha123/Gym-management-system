from nicegui import ui,app


def render():
    # big container
    with ui.element("div").style("background-image: url(./assets/hero.jpg); background-repeat:no-repeat background-size:cover").classes("h-screen w-screen flex flex-col bg-center justify-center items-centeR"):
        # navbar
        with ui.element("nav").classes(
            "flex flex-row justify-between items-center w-full p-4 bg-black/70 fixed left-0 top-0 z-10"
        ):
            ui.label("LOGO").classes("text-black font-bold text-2xl") 

            #navlinks
           
            
            navLinks =[
                 {"title": "Home", "path":"/"},
                 {"title": "About" ,"path":"/"},
                 {"title":"Services","path":"/"},
                 {"title":"Membership","path":"/"},
                 {"title":"Contact","path":"/"},
                 {"title": "Gallery","path":"/"}
            ]
            with ui.row().classes("gap-6"):
                for item in navLinks:
                    ui.link(item["title"], item["path"]).classes("no-underline uppercase")

            with ui.row().classes("text-4xl"):
                ui.icon("facebook")
                ui.icon("person") 
                ui.icon("notifications") 
                ui.icon("search") 
                ui.icon("people")
                
        

        # text
        with ui.element("div").classes("text-3xl text-black font-bold text-center mt-20"):
            ui.label("Welcome to").classes("text-5xl drop-shadow-lg")
            ui.html("<hi>Fitness Arena</h1>").classes("text-8xl text-black-800 drop-shadow-xl")
            ui.button("MENU" , color="black-800").classes("mt-6 px-6 py-3 text-lg rounded-full shadow-lg")