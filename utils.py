def list_from_file(filename: str) -> "list[str]":
    """Receives a txt filepath and returns a list without newline char"""
    with open(filename, "r") as list_file:
        lines: 'list[str]' = list_file.readlines()
    lines = [ line.replace("\n", "") for line in lines ]
    
    return lines