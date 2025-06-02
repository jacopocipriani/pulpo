import copy

def expand_static_to_time(static_dict, t_steps):
    """
    Replicate a static dict at each specified time step.

    Args:
        static_dict (dict): e.g. choices/ upper or lower limit= {'...': {...}, …}
        t_steps (sequence): list of time indices, e.g. [0,1,2,…,T]

    Returns:
        dict[int, dict]: {t: deep copy of static_dict for each t in t_steps}
    """
    return {t: copy.deepcopy(static_dict) for t in t_steps}