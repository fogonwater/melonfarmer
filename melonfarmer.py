import json, os, time

import requests
from bs4 import BeautifulSoup

class MelonFarmer:
    def __init__(self):
        self.sleep_dur = 1

    def read_json(self, f_path):
        with open(f_path, 'r') as infile:
            self.documents = json.load(infile)
        print 'Read %s.' % (f_path)

    def get(self, url):
        print url
        r = requests.get(url)
        if r.status_code != 200:
            print 'Error: %s.' % r.status_code
        return r

    def post_json(self, payload, url):
        headers = {'content-type': 'application/json'}
        r = requests.post(
            url,
            data=json.dumps(payload),
            headers=headers
        )
        if r.status_code == 200:
            return r
        else:
            print 'Error: %s.' % r.status_code
            return

    def write_json(self, js, dst_path, quiet=True):
        with open(dst_path, 'w') as outfile:
            json.dump(js, outfile, indent=2)
        if not quiet:
            print dst_path, 'written.'

    def get_json_filenames(self, f_dir):
        f_names = []
        for r,d,files in os.walk(f_dir):
            for f in files:
                if f.endswith('.json'):
                    f_names.append('%s/%s' % (r, f))
        return f_names

    def file_exists(self, fname, quiet=True):
        if os.path.isfile(fname):
            if not quiet:
                print '\n * Skipping record %s exists...\n' % (fname)
            return True
        return False

    def sleep(self, backoff=False):
        # TODO - write a backoff function
        time.sleep(self.sleep_dur)