. ./util/.env

DAY=$(date '+%-d')
YEAR=$(date '+%Y')

curl --silent \
    -H "Cookie: session=$AOC_SESSION_COOKIE" \
    -H 'Content-Type: application/x-www-form-urlencoded' \
    -H 'Referer: https://adventofcode.com/$YEAR/day/$DAY' \
    -d "level=$1&answer=$2" \
    -X POST "https://adventofcode.com/$YEAR/day/$DAY/answer" \
    | sed -n '/<main>/,/<\/main>/p'
