#!/bin/bash

# rm -rf _criteria
# rm -rf _taxonomy
rseng generate taxonomy _taxonomy
rseng generate criteria _criteria
rseng generate taxonomy-json _taxonomy/taxonomy.json
