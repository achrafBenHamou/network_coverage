"""
this function aims to compare two ProviderCoverage objects, and return the best one (best network coverage)
"""
def compare_result(new_provider_coverage,old_provider_coverage):
    if new_provider_coverage.has_4G and old_provider_coverage.has_4G:
        if new_provider_coverage.has_3G and old_provider_coverage.has_3G:
            if new_provider_coverage.has_2G:
                return new_provider_coverage
            else:
                return old_provider_coverage
        else:
            if new_provider_coverage.has_3G:
                return new_provider_coverage
            else :
                return old_provider_coverage
    else:
        if new_provider_coverage.has_4G:
            return new_provider_coverage
        else :
            return old_provider_coverage
