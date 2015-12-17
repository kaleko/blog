compile the site with: make html
always work on master branch
the only things on gh-pages branch are what's in the output/ folder
to publish, do:
ghp-import output
git push origin gh-pages
