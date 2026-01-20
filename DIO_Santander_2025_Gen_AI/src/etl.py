import os
import json
import pandas as pd
from dotenv import load_dotenv

from prompt import SYSTEM_PROMPT, build_user_prompt


# -------------------------
# Helpers
# -------------------------
def is_valid_openai_key(key: str | None) -> bool:
    """Valida minimamente se a chave parece real e não um placeholder."""
    if not key:
        return False

    k = key.strip()

    # placeholders comuns
    bad_markers = [
        "coloque", "sua_api", "sua chave", "your", "apikey", "api_key", "aqui",
        "xxx", "xxxx", "changeme", "replace"
    ]
    if any(m in k.lower() for m in bad_markers):
        return False

    # formato típico começa com "sk-"
    if not k.startswith("sk-"):
        return False

    # tamanho mínimo razoável (evita "sk-123")
    if len(k) < 20:
        return False

    return True


def ensure_parent_dir(filepath: str) -> None:
    os.makedirs(os.path.dirname(filepath), exist_ok=True)


# ---- Transform (IA) ----
def generate_ai_message_openai(user: dict) -> str:
    """
    Gera mensagem usando OpenAI.
    Requer OPENAI_API_KEY válida no .env
    """
    # Importa aqui dentro para não depender da lib quando estiver em mock
    from openai import OpenAI

    api_key = os.getenv("OPENAI_API_KEY")
    if not is_valid_openai_key(api_key):
        raise RuntimeError("OPENAI_API_KEY ausente/invalidada (placeholder).")

    client = OpenAI(api_key=api_key)

    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": build_user_prompt(user)},
        ],
        temperature=0.6,
    )

    return resp.choices[0].message.content.strip()


def generate_message_mock(user: dict) -> str:
    """
    Modo sem IA (para testar pipeline).
    """
    name = user.get("name", "Cliente")
    return f"{name}, investir regularmente ajuda a construir segurança financeira. Comece hoje."


# ---- ETL ----
def extract_users(csv_path: str) -> list[dict]:
    df = pd.read_csv(csv_path)
    return df.to_dict(orient="records")


def transform_users(users: list[dict], use_ai: bool = True) -> list[dict]:
    out = []
    for u in users:
        if use_ai:
            try:
                msg = generate_ai_message_openai(u)
            except Exception as e:
                # fallback automático para mock (sem quebrar a execução)
                print(f"[WARN] OpenAI falhou; usando mock. Motivo: {e}")
                msg = generate_message_mock(u)
        else:
            msg = generate_message_mock(u)

        # mantém estrutura similar ao lab (news)
        u2 = dict(u)
        u2["news"] = u2.get("news", [])
        u2["news"].append({
            "icon": "https://example.com/icons/invest.svg",
            "description": msg
        })
        out.append(u2)

    return out


def load_outputs(users_with_news: list[dict], out_json: str, out_csv: str) -> None:
    ensure_parent_dir(out_json)
    ensure_parent_dir(out_csv)

    # JSON (estrutura completa)
    with open(out_json, "w", encoding="utf-8") as f:
        json.dump(users_with_news, f, ensure_ascii=False, indent=2)

    # CSV (achatado: 1 linha por usuário + última mensagem)
    rows = []
    for u in users_with_news:
        last_msg = u["news"][-1]["description"] if u.get("news") else ""
        rows.append({
            "user_id": u.get("user_id"),
            "name": u.get("name"),
            "segment": u.get("segment"),
            "balance": u.get("balance"),
            "city": u.get("city"),
            "message": last_msg
        })

    pd.DataFrame(rows).to_csv(out_csv, index=False, encoding="utf-8")


def main():
    load_dotenv()

    base_dir = os.path.dirname(os.path.dirname(__file__))
    csv_path = os.path.join(base_dir, "data", "users.csv")
    out_json = os.path.join(base_dir, "output", "messages.json")
    out_csv = os.path.join(base_dir, "output", "messages.csv")

    # liga/desliga IA: só liga se a chave parecer válida
    use_ai = is_valid_openai_key(os.getenv("OPENAI_API_KEY"))

    users = extract_users(csv_path)
    users_with_news = transform_users(users, use_ai=use_ai)
    load_outputs(users_with_news, out_json, out_csv)

    print(f"OK! Gerado: {out_json} e {out_csv} (use_ai={use_ai})")


if __name__ == "__main__":
    main()
