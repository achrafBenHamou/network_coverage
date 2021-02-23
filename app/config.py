class Configuration():
    """ if you have to add data with other providers, you can just add it in the dictionary,
        also for networks,
    """
    data = '../data/file.csv'    # processed data path

    # dictionary of network providers with ids
    providers = {20801: 'Orange',
                 20810: 'SFR',
                 20815: 'Free',
                 20820: 'Bouygues'
                 }

    networks = ["2G","3G","4G"] # list of networks