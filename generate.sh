#!/bin/bash

# rm -rf docs/_criteria
# rm -rf docs/_taxonomy
rseng generate taxonomy docs/_taxonomy
rseng generate taxonomy docs/_criteria
rseng generate taxonomy-json docs/_taxonomy/taxonomy.json
