
"""
this function takes dictionnary of ProviderCoverge objects as parameter
"""
def resource_representation(Providers_data):
    if len(Providers_data) != 0:
        output = {}
        for element in Providers_data.keys() :
            output [element] = {"2G":Providers_data [element].has_2G,
                                "3G":Providers_data [element].has_3G,
                                "4G":Providers_data [element].has_4G}
        return output
    return {"Result ": "resources are not available for this address"}





