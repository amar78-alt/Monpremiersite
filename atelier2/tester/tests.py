"""Sept tests de contrat pour l'API Frankfurter."""
from datetime import date
from atelier2.client import get_json


def run_tests():
    results = []

    def record(name, fn):
        try:
            detail, latency = fn()
            results.append({"name": name, "status": "PASS", "details": detail, "latency_ms": latency})
        except Exception as exc:
            results.append({"name": name, "status": "FAIL", "details": str(exc), "latency_ms": None})

    def base_eur():
        r = get_json("/latest", {"from": "EUR"})
        assert r["status_code"] == 200, "Statut HTTP attendu : 200"
        return "HTTP 200 reçu", r["latency_ms"]

    def json_content_type():
        r = get_json("/latest", {"from": "EUR"})
        assert "json" in r["content_type"].lower(), "Content-Type JSON attendu"
        return "Content-Type JSON", r["latency_ms"]

    def required_fields():
        r = get_json("/latest", {"from": "EUR"})
        data = r["json"]
        for field in ("amount", "base", "date", "rates"):
            assert field in data, "Champ obligatoire absent : " + field
        return "Champs obligatoires présents", r["latency_ms"]

    def field_types():
        r = get_json("/latest", {"from": "EUR"})
        data = r["json"]
        assert isinstance(data["amount"], (int, float)), "amount doit être numérique"
        assert isinstance(data["base"], str), "base doit être une chaîne"
        assert isinstance(data["date"], str), "date doit être une chaîne"
        assert isinstance(data["rates"], dict), "rates doit être un objet JSON"
        return "Types des champs conformes", r["latency_ms"]

    def expected_base():
        r = get_json("/latest", {"from": "EUR"})
        assert r["json"]["base"] == "EUR", "La devise de base attendue est EUR"
        return "Devise de base EUR", r["latency_ms"]

    def date_format():
        r = get_json("/latest", {"from": "EUR"})
        parsed = date.fromisoformat(r["json"]["date"])
        assert parsed.isoformat() == r["json"]["date"], "Date attendue au format YYYY-MM-DD"
        return "Date ISO valide", r["latency_ms"]

    def usd_to_eur():
        r = get_json("/latest", {"from": "USD", "to": "EUR"})
        data = r["json"]
        assert r["status_code"] == 200, "Statut HTTP attendu : 200"
        assert data.get("base") == "USD", "La devise de base attendue est USD"
        assert isinstance(data.get("rates"), dict), "rates doit être un objet JSON"
        assert isinstance(data["rates"].get("EUR"), (int, float)), "Le taux EUR doit être numérique"
        return "Taux USD vers EUR présent et numérique", r["latency_ms"]

    record("HTTP 200 sur EUR", base_eur)
    record("Content-Type JSON", json_content_type)
    record("Champs obligatoires", required_fields)
    record("Types des champs", field_types)
    record("Devise de base EUR", expected_base)
    record("Format de date ISO", date_format)
    record("Conversion USD vers EUR", usd_to_eur)
    return results
