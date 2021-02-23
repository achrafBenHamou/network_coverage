class Configuration():
    """ if you need to add data with other network providers, you can just add its ids and names in the dictionary,
        and the same thing for networks
    """
    data = '../data/file.csv'    # processed data path

    # dictionary of network providers with ids
    providers = {20801: 'Orange',
                 20810: 'SFR',
                 20815: 'Free',
                 20820: 'Bouygues'
                 }

    networks = ["2G","3G","4G"] # list of networks