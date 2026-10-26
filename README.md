# Xuqin Wang — personal website

GitHub Pages site: <https://xuqinwang.github.io>. The original AcademicPages appearance is retained, with one Markdown file per page and no content collections or generators.

## Where to edit

| Visible content | File |
| --- | --- |
| About / research interests | [pages/about.md](pages/about.md) |
| All publications, authors, summaries, and links | [pages/publications.md](pages/publications.md) |
| Work and research experience | [pages/experience.md](pages/experience.md) |
| Education | [pages/education.md](pages/education.md) |
| Skills, languages, and service | [pages/skills.md](pages/skills.md) |
| CV download / overview | [pages/cv.md](pages/cv.md) |
| Shared sidebar: name, photo, bio, email, social links | [_config.yml](_config.yml), under `author` |
| Navigation labels and page order | [_data/navigation.yml](_data/navigation.yml) |

Edit the Markdown below the `---` front matter. The `permalink` controls the public URL; filenames can differ. To add a paper, copy an entry in `pages/publications.md`; label submitted work “Under review” without naming the submission conference, separately from accepted work. No YAML publication records or per-paper files are needed.

Content was updated from `../CV_XuqinWang.pages`. The existing `files/CV_XuqinWang_TUM.pdf` is an older version and is labeled accordingly on the CV page. Export the current Pages document as PDF, replace that file, and update the download label in `pages/cv.md`. The original filename is retained so existing download links continue to work. The Pages source remains outside the public repository.

## Preview

With Ruby and Bundler installed, run from this directory:

```sh
bundle install
bundle exec jekyll serve --config _config.yml,_config.dev.yml
```

Open <http://localhost:4000>. Restart Jekyll after changing configuration. To check a production build:

```sh
bundle exec jekyll build
python3 tests/check_site.py _site
```

Commit and push this repository using its existing GitHub Pages workflow when ready. No Pages source-directory change is required.

## Theme files

`_layouts/` contains two shared page wrappers; `_includes/` contains the header, sidebar, footer, and asset loading. `_sass/` and `assets/` retain the theme styles, fonts, and responsive navigation. Ordinary content changes do not require editing these files. `package.json` and the JavaScript sources are retained for rebuilding the existing theme bundle if needed.

Unused template posts, publications, talks, teaching examples, archive pages, generators, and sample media have been removed; they remain recoverable from Git history. Existing `/about/`, `/about.html`, `/cv/`, `/resume`, and `/resume/` URLs are preserved. Removed sample URLs intentionally return 404. The existing ClustrMaps widget remains on the About page.

Theme attribution and its license are retained in [LICENSE](LICENSE).
