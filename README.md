# bastianfynboe.xyz

Portfolio for Bastian Fynboe. Plain HTML/CSS/JS, hosted on Vercel.

- Text and image choices: `_build/content.py`
- Rebuild the pages after editing: `python3 _build/build.py`
- Styles: `assets/site.css` · Scripts: `assets/site.js`
- Images: `assets/img/` (each in a 1000 px and a 2000 px version)

## Magazine edition: /issue/

- The portfolio as a flip-through magazine: `issue/index.html` (all text is right there in the HTML, page by page)
- Styles & script: `assets/issue/issue.css`, `assets/issue/issue.js` (page turning by StPageFlip, MIT)
- Fonts: `assets/fonts/issue/` (all OFL)
- After editing css/js, bump `?v=1` in `issue/index.html` so browsers fetch the new version
