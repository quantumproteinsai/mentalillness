import re
def helical(path):
    """Rise and twist from a cif, handling BOTH the scalar and the loop_ forms.

    The scalar-only regex crossed a newline into the loop_ header on 8WZX and returned
    rise = 1.0 (the first field of the data row) with twist = None. A wrong rise builds a
    wrong assembly and would have been invisible in the output.
    """
    t = open(path, errors='ignore').read()
    m_r = re.search(r'_em_helical_entity\.axial_rise_per_subunit[ \t]+([-\d.]+)[ \t]*\n', t)
    m_t = re.search(r'_em_helical_entity\.angular_rotation_per_subunit[ \t]+([-\d.]+)[ \t]*\n', t)
    if m_r and m_t:
        return float(m_r.group(1)), float(m_t.group(1))
    # loop_ form: collect the header order, then read the first data row
    mm = re.search(r'((?:_em_helical_entity\.\w+[ \t]*\n)+)((?:[^\n_#][^\n]*\n)+)', t)
    if not mm:
        return None, None
    keys = [k.strip().split('.')[1] for k in mm.group(1).strip().split('\n')]
    row = mm.group(2).strip().split('\n')[0].split()
    if len(row) != len(keys):
        return None, None
    d = dict(zip(keys, row))
    try:
        return float(d['axial_rise_per_subunit']), float(d['angular_rotation_per_subunit'])
    except (KeyError, ValueError):
        return None, None
