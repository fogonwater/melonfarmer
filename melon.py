import csv, json, os, time

import requests

class Farmer:
    def __init__(self):
        self.sleep_dur = 1
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
        print('Read {}.'.format(f_path))
        return self.documents

    def write_json(self, data, dst_path):
        with open(dst_path, 'w') as outfile:
            json.dump(data, outfile, indent=2)
        if self.verbose:
            print dst_path, 'written.'

    def read_csv(self, f_path):
        rows = []
        with open(f_path) as f:
            reader = csv.DictReader(f)
            for row in reader:
                rows.append(row)
        return rows

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

    def sleep(self, backoff=False):
        # TODO - write a backoff function
        time.sleep(self.sleep_dur)