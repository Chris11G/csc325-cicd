# CSC325 – First CI/CD Pipeline

A small Django + Django REST Framework backend with a four-stage GitHub Actions
pipeline: **Setup → Dependencies → Test → Deploy**. Deploy only runs if every test passes.

## Endpoints
| Method | URL | Response |
|---|---|---|
| GET | `/api/health/` | `{"status": "ok"}` |
| GET | `/api/greeting/?name=Chris` | `{"message": "Hello, Chris!"}` |

## Run locally
```bash
python3 -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate
python3 -m pip install -r requirements.txt
python3 manage.py test             # should report 4 tests, OK
python3 manage.py runserver        # then open http://127.0.0.1:8000/api/health/
```

## Put it on GitHub
```bash
git init
git add .
git commit -m "Initial Django REST backend with CI/CD pipeline"
git branch -M main
git remote add origin https://github.com/<your-username>/<repo-name>.git
git push -u origin main
```
Then open the **Actions** tab — all four jobs should turn green.

## Protect main (assignment step 4)
Settings → Rules → Rulesets → New branch ruleset → target `main` →
enable "Require status checks to pass" and add the **Test** check
(you can also block force pushes / deletions). If the rubric needs a
feature branch, work on `git checkout -b feature/new-endpoint`, push, and open a PR.

## The on-camera change (do NOT commit until recording)
Add a new endpoint in `api/views.py`:
```python
@api_view(["GET"])
def about(request):
    return Response({"course": "CSC325", "student": "Chris Gonzalez"})
```
in `api/urls.py`:
```python
    path("about/", views.about, name="about"),
```
and a test in `api/tests.py`:
```python
class AboutEndpointTests(APITestCase):
    def test_about(self):
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["course"], "CSC325")
```
Run `python3 manage.py test` (5 tests, OK), then on camera:
`git commit -am "Add /api/about endpoint"` and `git push`.

## Optional extra credit: real deployment on Render
1. render.com → New → Web Service → connect this repo.
2. Build command: `python3 -m pip install -r requirements.txt`
   Start command: `gunicorn config.wsgi`
3. Env vars: `DJANGO_DEBUG=False`, `DJANGO_SECRET_KEY=<random string>`,
   `DJANGO_ALLOWED_HOSTS=<your-app>.onrender.com`. Turn **Auto-Deploy off**.
4. Copy the service's **Deploy Hook** URL → GitHub repo Settings → Secrets and
   variables → Actions → new secret `RENDER_DEPLOY_HOOK_URL`.
Now the Deploy stage triggers Render only after tests pass.
Your running example URL: `https://<your-app>.onrender.com/api/health/`
