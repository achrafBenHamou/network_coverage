
def ResourceRepresentation(Providers_data):
    """
    this function takes list of ProviderCoverge objects as parameter
    """
    if len(Providers_data) != 0:
        output = {}
        for element in Providers_data :
            output [element.name] = {"2G":element.has_2G,
                                     "3G":element.has_3G,
                                     "4G":element.has_4G}
        return output
    return {"Result ": "resources are not available for this address"}



