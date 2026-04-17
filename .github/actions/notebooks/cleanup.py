import os
import requests

job_url_path = "/tmp/job_url.txt"

# Check if file exists
if os.path.exists(job_url_path):
    with open(job_url_path, "r") as f:
        job_url = f.read().strip()
else:
    job_url = None

if not job_url:
    print("No job_url found, nothing to cancel.")
    raise SystemExit(0)

token = os.environ["INPUT_TOKEN"]
headers = {"Authorization": f"token {token}"}

try:
    r = requests.delete(job_url, headers=headers, timeout=10)
    r.raise_for_status()
    print("Job cancelled via cleanup")
except Exception as e:
    print(f"Could not delete job: {e}")
