SYSTEM_PROMPT = "Você é um especialista em marketing bancário e retenção de clientes."

def build_user_prompt(user: dict) -> str:
    return (
        f"Crie uma mensagem curta (máximo 120 caracteres) incentivando investimentos, "
        f"personalizada para {user['name']} (segmento: {user.get('segment')}, cidade: {user.get('city')}). "
        f"Seja direto, amigável e sem emojis."
    )
