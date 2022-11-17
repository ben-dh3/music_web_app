#!/bin/sh

# Run this file to remove the example code from the project.
# ; ./remove_example_code.sh

echo "This will remove the example code from the project."
echo "DO NOT RUN THIS IF YOU HAVE ADDED YOUR OWN CODE."
echo "It may accidentally delete your code!"
echo "Continue? [y/N]"
read -r response
if [ "$response" != "y" ]; then
    echo "Aborting."
    exit 1
fi

rm lib/book_repository.py
rm lib/book.py
rm tests/test_book_repository.py
rm tests/test_book.py
rm tests/test_example_routes.py
rm example_routes.py

grep -v book_store seed_dev_database.py > seed_dev_database.py.tmp
mv seed_dev_database.py.tmp seed_dev_database.py

sed -n "/== Example Code Below ==/q;p" app.py > app.py.tmp
mv app.py.tmp app.py

rm remove_example_code.sh

echo "Completed."
