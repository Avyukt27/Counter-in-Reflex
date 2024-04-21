import reflex as rx


class CounterState(rx.State):
    number: int
    def increment(self):
        self.number += 1
    def decrement(self):
        self.number -= 1

def index() -> rx.Component:
    return rx.flex(
        rx.button(
            "Decrement",
            color_scheme="red",
            size="4",
            on_click=CounterState.decrement,
        ),
        rx.heading(
            CounterState.number,
            font_size="4em",
        ),
        rx.button(
            "Increment",
            color_scheme="grass",
            size="4",
            on_click=CounterState.increment,
        ),
        height="100vh",
        justify="center",
        align="center",
        spacing="3",
    )

app = rx.App()
app.add_page(index)
