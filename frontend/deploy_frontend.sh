set -e
npm install
rm -r ../attendance/static/
mkdir ../attendance/static
npm run build
cp build/index.html ../attendance/attendance/templates/index.html
cp -r build/static/* ../attendance/static/
