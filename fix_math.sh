#!/bin/bash
find _posts -name "*.md" -exec perl -pi -e 's/(?<!\$)\$(?!\$)/\$\$/g' {} \;
cat _posts/2025-2-7-常数变易法.md;
