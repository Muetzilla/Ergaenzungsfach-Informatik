import requests

def yahoo_fx_rate(base: str, quote: str = "CHF") -> float:
    """
    Holt den aktuellen FX-Kurs BASE/QUOTE über die Yahoo-Finance-Chart-API.
    """
    symbol = f"{base}{quote}=X"
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{symbol}"
    headers = {
        "User-Agent": "Mozilla/5.0"  # wichtig, sonst liefert Yahoo manchmal HTML statt JSON
    }
    params = {"interval": "1d"}

    resp = requests.get(url, headers=headers, params=params)
    if resp.status_code != 200:
        raise RuntimeError(f"HTTP {resp.status_code} von Yahoo für {symbol}")

    try:
        data = resp.json()
    except Exception:
        raise RuntimeError(f"Antwort von Yahoo war kein JSON:\n{resp.text[:200]}...")

    try:
        result = data["chart"]["result"][0]
        meta = result["meta"]
        price = meta["regularMarketPrice"]
        return float(price)
    except Exception as e:
        raise RuntimeError(f"Konnte Kurs für {symbol} nicht extrahieren: {e}\nAntwort: {data}")

# --- Beispielnutzung ---
if __name__ == "__main__":
    for c in ["EUR", "USD", "GBP", "JPY", "CAD", "AUD", "NOK"]:
        try:
            print(f"1 {c} -> CHF =", yahoo_fx_rate(c, "CHF"))
        except Exception as e:
            print("Fehler bei", c, ":", e)
