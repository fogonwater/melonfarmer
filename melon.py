# -*- coding: utf-8 -*-

import csv, json, os, time
try:
    import requests
except ImportError:
    print('* Missing the requests library. Some functions not available.')

def set_default(obj):
    if isinstance(obj, set):
        return list(obj)
    raise TypeError

def touch(f_path='index.html', times=None):
    with open(f_path, 'a'):
        os.utime(f_path, times)

def get_filenames(f_dir, prefix='', suffix=''):
    """Get list of filenames within a directory. Optionally scope by prefix/suffix."""
    f_names = []
    for r,d,files in os.walk(f_dir):
        for f in files:
            if f.startswith(prefix) and f.endswith(suffix):
                f_names.append('{}/{}'.format(r, f))
    return f_names

def file_exists(f_path):
    if os.path.isfile(f_path):
        return True
    return False

def get_json(url, payload=None, verbose=True):
    """ Get JSON from an online service with optimal URL parameters. """
    r = requests.get(url, params=payload)
    if verbose:
        print('Fetched: {}'.format(r.url))
    if r.status_code != 200:
        print('Error: {}.'.format(r.status_code))
    return r.json()

def read_textfile(f_path):
    """ Open a textfile and return contents as a stripped list."""
    with open(f_path) as f:
        rows = f.readlines()
    return [row.strip() for row in rows]

def read_csv(f_path, fieldnames=[], strip_header=False, skip_rows=0):
    with open(f_path) as f:
        # optionally strip whitespace from header values (e.g. '  depth' -> 'depth')
        if not fieldnames and strip_header:
            fieldnames = [h.strip() for h in f.readline().split(',')]
        if not fieldnames:
            reader = csv.DictReader(f)
        else:
            reader = csv.DictReader(f, fieldnames=fieldnames)
        # Optionall skip n rows. Useful in combination with fieldnames
        for n in range(skip_rows):
            next(reader)
        rows = [ row for row in reader ]
    return rows

def read_json(f_path):
    with open(f_path, 'r') as infile:
        data = json.load(infile)
    print('Read {}.'.format(f_path))
    return data

def write_json(data, f_path):
    with open(f_path, 'w') as outfile:
        json.dump(data, outfile, indent=2, sort_keys=True)
    print('{} written.'.format(f_path))

def write_text(data, f_path):
    with open(f_path, 'w') as f:
        try:
            f.write(data.encode('utf8'))
        except TypeError:
            f.write(data)
    print('Wrote {}.'.format(f_path))

def listdict_to_csv(data, f_path):
    with open(f_path, 'w') as output_file:
        dict_writer = csv.DictWriter(output_file, data[0].keys())
        dict_writer.writeheader()
        dict_writer.writerows(data)
    print('Wrote {} with {} rows.'.format(f_path, len(data)))
    
def list_to_csv(data, f_path):
    with open(f_path, 'w') as f:
        writer = csv.writer(f)
        writer.writerows(data)
    print('Wrote {} with {} rows.'.format(f_path, len(data) - 1))
