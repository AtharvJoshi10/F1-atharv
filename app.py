
import os
from flask import Flask, render_template

app = Flask(__name__)

DASHBOARD_URL = os.getenv(
    "TABLEAU_DASHBOARD_URL",
    "https://public.tableau.com/views/Atharvjoshi/F1RaceIntelligenceDashboard?:language=en-US&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link"
)

# Replace this with the actual published story URL.
STORY_URL = os.getenv(
    "TABLEAU_STORY_URL",
    "https://public.tableau.com/views/Atharvjoshistory/Story1?:language=en-US&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link"
)

@app.route("/")
def index():
    return render_template(
        "index.html",
        dashboard_url=DASHBOARD_URL,
        story_url=STORY_URL,
        active_page="dashboard"
    )

@app.route("/story")
def story():
    return render_template(
        "index.html",
        dashboard_url=DASHBOARD_URL,
        story_url=STORY_URL,
        active_page="story"
    )

@app.route("/health")
def health():
    return {"status": "ok"}, 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", "5000"))
    app.run(host="127.0.0.1", port=port, debug=False)
