npm install
npm run build
rm -r ../attendance/static/
cp build/index.html ../attendance/attendance/templates/index.html
cp -r build/static/* ../attendance/static/

