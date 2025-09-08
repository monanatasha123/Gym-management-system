from nicegui import ui


def render():
    with ui.element("div").classes("w-screen h-screen flex-row items-center"):

        with ui.element("div").classes(
            "w-[50%] h- screen flex flex-col justify-center items-center text-center p-6"
        ):
            ui.label("Fitness Areana").classes("text-black-600 italic-3xl")
            ui.label("WELCOME").classes(
                "text-3xl font extrabold text-black-300"
            )



