# chrome_cache_export
Python script to export files of the Google Chrome Cache (also tested with Chromium)

## Clone repo
Clone the repo with Submodule.
```
git clone --recurse-submodules https://github.com/floleuerer/chrome_cache_export.git
```

## Requirements

Requires `Python >= 3.6` and `pyyaml`.

```
pip install pyyaml
```

## Usage

### Export all cached Files
```
python chrome_cache_export.py
```

### config.yml

If using Chromium the cache_path has to be set. Default is using Google Chrome paths.

To change the default parameters edit `config.yml`.
```
# only export cached files where the domain contains the following string
domain: ''

# location of the cache - will use default path if empty
cache_path: ''

# export path
export_path: 'export'

# overwrite existing?
overwrite_existing: True

# get and print a list of all domains in the cache no files will be exported!!!
print_domains: False
```