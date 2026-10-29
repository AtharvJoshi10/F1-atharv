# F1 Race Intelligence

Flask website that embeds the existing Tableau Public dashboard and story.

## Local setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Open https://f1-vl5m.onrender.com/

- Dashboard: `/`
- Story: `/story`
- Health check: `/health`

## Render deployment

1. Push this folder to a GitHub repository.
2. In Render, create a new Blueprint or Web Service.
3. For a Blueprint, select the repository containing `render.yaml`.
4. For a manual Web Service, use:
   - Build command: `pip install -r requirements.txt`
   - Start command: `gunicorn app:app`
5. Deploy and test both `/` and `/story`.

## Optional environment variables

- `TABLEAU_DASHBOARD_URL`
- `TABLEAU_STORY_URL`

Set these in Render if the published Tableau URLs change.

Note: the Tableau views must be published and accessible to the public for visitors to see them.
