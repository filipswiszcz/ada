class Util:

    def __init__(self) -> None:
        pass

    def get_global_properties(self):
        global_properties = {}
        try:
            with open("global.properties", "r", encoding = "UTF-8") as output:
                for line in output:
                    if line.strip() and not line.strip().startswith("#"):
                        property = line.strip().split(":")
                        key, value = property[0].strip(), ":".join(property[1:]).strip().strip('"')
                        global_properties[key] = value
            return global_properties
        except Exception: return "Error occured while getting global properties."
        