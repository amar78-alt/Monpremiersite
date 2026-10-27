"""Client HTTP sans dépendance externe pour l'API Frankfurter."""
import json
import time
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

BASE_URL = "https://api.frankfurter.app"
TIMEOUT_SECONDS = 4


def get_json(path, params=None, retries=1):
    query = "?" + urlencode(params) if params else ""
    url = BASE_URL + path + query
    last_error = None

    for attempt in range(retries + 1):
        started = time.perf_counter()
        req = Request(url, headers={"Accept": "application/json", "User-Agent": "EPSI-Atelier-API-Watch/1.0"})
        try:
            with urlopen(req, timeout=TIMEOUT_SECONDS) as response:
                latency_ms = round((time.perf_counter() - started) * 1000, 2)
                content_type = response.headers.get("Content-Type", "")
                payload = json.loads(response.read().decode("utf-8"))
                return {"status_code": response.status, "content_type": content_type, "json": payload, "latency_ms": latency_ms}
        except HTTPError as exc:
            last_error = RuntimeError("HTTP " + str(exc.code))
            if (exc.code == 429 or exc.code >= 500) and attempt < retries:
                time.sleep(1)
                continue
            raise RuntimeError("Erreur HTTP depuis " + url + ": " + str(exc.code)) from exc
        except (URLError, TimeoutError, OSError, ValueError) as exc:
            last_error = exc
            if attempt < retries:
                time.sleep(1)
                continue
            raise RuntimeError("Échec de la requête vers " + url + ": " + str(exc)) from exc

    raise RuntimeError("Échec de la requête : " + str(last_error))
