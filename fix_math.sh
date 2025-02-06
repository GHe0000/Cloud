find _posts -name "*.md" -exec perl -pi -e 's/(?<!\$)\$(?!\$)/\$\$/g' {} \;
