find _post -name "*.md" -exec perl -pi -e 's/(?<!\$)\$(?!\$)/\$\$/g' {} \;
