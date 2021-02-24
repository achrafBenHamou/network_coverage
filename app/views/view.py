from app import config

providers = config.Configuration.providers  # get dictionary of providers
networks = config.Configuration.networks    # ["2G","3G","4G"]

def getZipCodefromResource(resource):
    """ Input : response of geo api
        Output : Zip Code  """
    try:
        response = resource['features'][0]['properties']
        zip_code = response['postcode']
        return zip_code
    except Exception as e:
        print(e)
        return 0

def resourcePresentation(resource_list):
    """     this function takes list of rows finded in csv data,
            and reform it for given the response to user
            Input Example :
            [['20801', '102980', '6847973', '1', '1', '0', '42100'],
            ['20810', '102980', '6847973', '1', '1', '0', '42100'],
            ['20820', '102980', '6847973', '1', '1', '1', '42100'],
            ['20815', '102980', '6847973', '1', '1', '0', '42100']]  """
    try:
        output = {}
        for l in resource_list:
            l = list(map(lambda x: int(float(x)), l))                   # transform all elements of list to integer
            network_output ={}
            for i in range (3,len(networks)+3):             # treat just the 3th to 5th elements of list
                if (l[i]==1):
                    network_output[networks[i - 3]] = True  # example : {"2G" : True}
                else:
                    network_output[networks[i - 3]] = False
            output[providers[l[0]]] = network_output
        return output
    except Exception as e:
        print(e)
        return {"Result ": "resources not availables for this address"}

