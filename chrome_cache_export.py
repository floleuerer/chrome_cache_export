from ChromiumCacheExplorer.chromium_cache import CacheIndex, CacheEntry
import os
import platform
import shutil
import io
from pathlib import Path

# only export cached files where the domain contains the following string
domain = ''

# will use default path if empty
cache_path = ''

# path
export_path = 'export'

# overwrite existing?
overwrite_existing = False

# get and print a list of all domains in the cache no files will be exported!!!
print_domains = False



def get_chrome_cache_path():
# Get Chrome Default Path
    path = ''
    os_used = platform.system()
    if os_used == 'Darwin':
        home = os.environ['HOME']
        path = f'{home}/Library/Caches/Google/Chrome/Default/Cache/'
    elif os_used == 'Linux':
        home = os.environ['HOME']
        path = f'{home}/.cache/google-chrome/Default/Cache/'
    elif os_used == 'Windows':
        appdata = os.environ['APPDATA']
        path = f'{appdata}/Local/Google/Chrome/User Data/Default/Cache/'
    else:
        raise Exception('OS not supported!')

    return path

if cache_path == '':
    cache_path = get_chrome_cache_path()



if print_domains:
    # Print Domains
    print('Domains in cache:')
    tlds = set()
    for d in domains:
        ds = d.split('.')
        if len(ds) == 1:
            tld = f'{ds[-1]}'
        elif len(ds) > 1: 
            tld = f'{ds[-2]}.{ds[-1]}'
        tlds.add(tld)

    sorted_domains = sorted(list(domains))
    for tld in sorted(list(tlds)):
        print()
        print(tld)
        for d in sorted_domains:
            if f'.{tld}' in d:
                print(f'- {d}')
else:
    # Export
    idx = CacheIndex(cache_path)
    idx.entries()
    entries = [entry for entry in idx.files()]
    domains = set()
    for e in entries:
        if os.path.exists(e):
            ce = CacheEntry(e)
            d = ce.url.split('://')[-1].split('/')[0]
            if print_domains:
                domains.add(d)

            if domain in d:
                print(ce.url)
                
                file_name = ce.url.split('/')[-1].split('?')[0]
                print('fn', file_name)
                export_path = Path(export_path)
                file_path = export_path/file_name
                if not os.path.exists(file_path) or overwrite_existing:
                    try:
                        shutil.copy(str(e),file_path)
                        with io.open(file_path, 'wb') as file:
                            file.write(ce.data)
                        f'{file_name} saved to {export_path}'
                    except Exception as e:
                        print(f'Error: {e}')
                else:
                    print(f'{file_name} already exists - skipping')


