def write_file(filename="", text=""):
    """Writes a string to a text file"""
    with open(filename, "w", encoding="utf-8") as f:
        write = f.write(text)
        return len(text)
