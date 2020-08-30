# chrome_cache_export
Python script to export files of the Google Chrome Cache (also tested with Chromium)

## Clone repo
Clone the repo with Submodule.
```
git clone --recurse-submodules https://github.com/floleuerer/chrome_cache_export.git
```

## Usage

### Export all cached Files
```
python chrome_cache_export.py
```

### Config

If using Chromium the cache_path has to be set. Default is using Google Chrome paths.

```
# only export cached files where the domain contains the following string
domain = ''

# will use default path if empty
cache_path = ''

# path
export_path = Path('export')

# overwrite existing?
overwrite_existing = False

# get and print a list of all domains in the cache
print_domains = True
```