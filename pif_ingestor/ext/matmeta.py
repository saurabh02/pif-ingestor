from pypif import pif


def add_metadata(pif, metadata):
    base = matmeta_to_pif(metadata)
    return update_pif(base, pif)


def matmeta_to_pif(metadata):
    try:
        from matmeta.payload_metaclass import CITPayload
    except ImportError:
        raise ImportError("Install package `matmeta` in order to use meta-data input")
    return pif.loads(CITPayload(**metadata).metapayload) 


def _deep_update(old, new):
    for k, v in new:
        if k not in old:
            old[k] = new[k]
        elif isinstance(old[k], list) and isinstance(new[k], list):
            old[k].extend(new[k])
        elif isinstance(old[k], dict) and isinstance(new[k], dict):
            _deep_update(old[k], new[k])
        else:
            old[k] = new[k]


def update_pif(old, new):
    old_d = old.as_dictionary()
    new_d = new.as_dictionary()
    _deep_update(old_d, new_d)
    return pif.loads(pif.dumps(old_d))
