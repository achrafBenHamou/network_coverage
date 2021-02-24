from app.model.data_provider import getNetworkCoverage
from app.service.entry_point import getAddressResource
from app.views.view import getZipCodefromResource, resourcePresentation


def get_data(address):
    resource = getAddressResource(address)         # get resource using Geo API
    zip_code = getZipCodefromResource(resource)    # get Zip Code from the response of Geo API
    resource = getNetworkCoverage(zip_code)        # get network coverage data of a city using its Zip code
    response = resourcePresentation(resource)      # reform resource presentation
    return response
