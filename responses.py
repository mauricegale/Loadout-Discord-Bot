

def handle_response(message) -> str:
    p_message = message.lower()

    if p_message == "hello":
        return "Yoooo"

    if p_message == "!help":
        return "`This is the help message`"

    return "Huhhh"
