def draw_text(**kwargs):
    """
    kwargs: color, size, text, font, bold
    """

    if len(kwargs) > 5:
        raise ValueError("to many arguments")

    color = kwargs.get("color")
    size = kwargs.get("size")
    font = kwargs.get("font")
    text = kwargs.get("text")
    bold = kwargs.get("bold")

    print(f"Drawing text: {text} with {kwargs}")
    print(color, size, font, text, bold)


draw_text(text="Hola", font="Arial")