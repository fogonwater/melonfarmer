import csv, json, os, time

import requests

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

    def write_json(self, data, f_path):
        with open(f_path, 'w') as outfile:
            json.dump(data, outfile, indent=2)
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
        f_names = []
        for r,d,files in os.walk(f_dir):
            for f in files:
                if f.endswith(suffix):
                    f_names.append('%s/%s' % (r, f))
        return f_names

    def file_exists(self, fname):
        if os.path.isfile(fname):
            if self.verbose:
                print(' * Skipping record {} exists...'.format(fname))
            return True
        return False