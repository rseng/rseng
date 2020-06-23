#!/bin/bash

echo
echo "************** START: test_client.sh **********************"

# Create temporary testing directory
echo "Creating temporary directory to work in."
here="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

. $here/helpers.sh

# Make sure it's installed
if which rseng >/dev/null; then
    printf "rseng is installed\n"
else
    printf "rseng is not installed\n"
    exit 1
fi

# Create temporary testing directory
tmpdir=$(mktemp -d)
output=$(mktemp ${tmpdir:-/tmp}/rseng_test.XXXXXX)
printf "Created temporary directory to work in. ${tmpdir}\n"

echo
echo "#### Testing rseng generate criteria markdown"
runTest 0 $output rseng generate criteria $tmpdir/_criteria
runTest 0 $output ls $tmpdir/_criteria

echo
echo "#### Testing rseng generate taxonomy markdown"
runTest 0 $output rseng generate taxonomy $tmpdir/_taxonomy
runTest 0 $output ls $tmpdir/_taxonomy

echo
echo "#### Testing rseng generate taxonomy json"
runTest 0 $output rseng generate taxonomy-json $tmpdir/taxonomy.json
runTest 0 $output ls $tmpdir/taxonomy.json

echo
echo "#### Testing rseng generate criteria annotation template"
runTest 0 $output rseng generate criteria-annotation-template $tmpdir/criteria-annotation-template.md
runTest 0 $output ls $tmpdir/criteria-annotation-template.md

echo
echo "#### Testing rseng generate criteria annotation template"
runTest 0 $output rseng generate taxonomy-annotation-template $tmpdir/taxonomy-annotation-template.md
runTest 0 $output ls $tmpdir/taxonomy-annotation-template.md

rm -rf ${tmpdir}
