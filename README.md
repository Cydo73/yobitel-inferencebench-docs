# InferenceBench documentation sample

An independent documentation set for InferenceBench, written by Mumpe Cydrone. It is not official Yobitel documentation.

Every procedure in this set was run on 2026-10-23 and recorded in the verification log. Each page carries a status:

* Verified: I ran it and checked the result.
* Partly verified: some steps or values were recorded, others were not.
* Draft: not tested yet.

## Build it on your computer

```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
sphinx-build -b html docs docs/_build/html
```

On Windows, activate the environment with `venv\Scripts\activate` instead of the `source` line.

Open `docs/_build/html/index.html` in your browser.

## Publish it on GitHub Pages

1. Create a new GitHub repository and push this folder to the `main` branch.
2. In the repository, open Settings, then Pages, and set the source to GitHub Actions.
3. Push any change. The workflow in `.github/workflows/docs.yml` builds and publishes the site.
