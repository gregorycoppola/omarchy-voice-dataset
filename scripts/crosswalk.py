#!/usr/bin/env python3
"""Compatibility entry point: views now come from catalog.json."""
from export_catalog import export

if __name__ == '__main__':
    export()
    print('Exported catalog views; the historical source crosswalk is unchanged.')
