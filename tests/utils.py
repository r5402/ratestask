def exclude_dictionary_keys(dictionary, keys):
    return {excluded_key: dictionary[excluded_key] for excluded_key in dictionary if excluded_key not in keys}
