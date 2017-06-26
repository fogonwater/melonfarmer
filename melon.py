# -*- coding: utf-8 -*-

import csv, json, os, time
try:
    import requests
except ImportError:
    pass

def set_default(obj):
    if isinstance(obj, set):
        return list(obj)
    raise TypeError

def touch(f_path='index.html', times=None):
    with open(f_path, 'a'):
        os.utime(f_path, times)

def get_filenames(f_dir, prefix='', suffix=''):
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

def get_json(url, verbose=True):
    if verbose:
        print('Fetching: {}'.format(url))
    r = requests.get(url)
    if r.status_code != 200:
        print('Error: {}.'.format(r.status_code))
    return r.json()

def read_csv(f_path, fieldnames=[], strip_header=False):
    with open(f_path) as f:
        # optionally strip whitespace from header values (e.g. '  depth' -> 'depth')
        if not fieldnames and strip_header:
            fieldnames = [h.strip() for h in f.next().split(',')]
        if not fieldnames:
            reader = csv.DictReader(f)
        else:
            reader = csv.DictReader(f, fieldnames=fieldnames)
        rows = [ row for row in reader ]
    return rows

def read_json(f_path):
    with open(f_path, 'r') as infile:
        data = json.load(infile)
    print('Read {}.'.format(f_path))
    return data

def write_json(data, f_path):
    with open(f_path, 'w') as outfile:
        json.dump(
            data,
            outfile,
            indent=2,
            sort_keys=True
        )
    print('{} written.'.format(f_path))

def write_text(data, f_path):
    with open(f_path, 'w') as f:
        f.write(data.encode('utf8'))

def list_to_csv(data, f_path):
    with open(f_path, 'wb') as f:
        writer = csv.writer(f)
        writer.writerows(data)
    print('Wrote {}.'.format(f_path))



class Farmer:
    def __init__(self):
        self.verbose = False

    def get(self, url):
        if self.verbose:
            print('Fetching: {}'.format(url))
        r = requests.get(url)
        if r.status_code != 200:
            print('Error: {}.'.format(r.status_code))
        return r

    def get_json(self, url):
        if self.verbose:
            print('Fetching: {}'.format(url))
        r = requests.get(url)
        if r.status_code != 200:
            print('Error: {}.'.format(r.status_code))
        return r.json()

    def post_json(self, payload, url):
        headers = {'content-type': 'application/json'}
        r = requests.post(
            url,
            data=json.dumps(payload),
            headers=headers
        )
        if r.status_code in [200, 201, 202]:
            if self.verbose:
                print('Status: {}.'.format(r.status_code))
            return r
        else:
            print('Error: {}.'.format(r.status_code))

    def read_json(self, f_path):
        with open(f_path, 'r') as infile:
            self.documents = json.load(infile)
        if self.verbose:
            print('Read {}.'.format(f_path))
        return self.documents

    def write_json(self, data, f_path, ensure_ascii=True):
        with open(f_path, 'w') as outfile:
            json.dump(
                data,
                outfile,
                indent=2,
                default=set_default,
                ensure_ascii=ensure_ascii,
                sort_keys=True
            )
        if self.verbose:
            print f_path, 'written.'

    def read_csv(self, f_path, fieldnames=[]):
        with open(f_path) as f:
            if not fieldnames:
                reader = csv.DictReader(f)
            else:
                reader = csv.DictReader(f, fieldnames=fieldnames)
            rows = [ row for row in reader]
        return rows

    def list_to_csv(self, data, f_path):
        with open(f_path, 'wb') as f:
            writer = csv.writer(f)
            writer.writerows(data)
        if self.verbose:
            print('Wrote {}.'.format(f_path))

    def get_filenames(self, f_dir, suffix=''):
        f_paths = []
        for r,d,files in os.walk(f_dir):
            for f in files:
                if f.endswith(suffix):
                    f_paths.append('%s/%s' % (r, f))
        return f_paths

    def file_exists(self, f_path):
        if os.path.isfile(f_path):
            if self.verbose:
                print(' * Skipping item {} exists...'.format(f_path))
            return True
        return False
