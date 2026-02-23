import requests
import json

# =====================================================
# 🔐 HARD-CODED OPENROUTER API KEY
# =====================================================

OPENROUTER_API_KEY = "xx"
# =====================================================
# STRICT SYSTEM CONTEXT
# =====================================================

SYSTEM_CONTEXT = """
You are an AI Disaster Intelligence Assistant.

System Capabilities:
- Post-disaster damage detection using CNN.
- Compensation estimation (₹0-₹5,00,000).
- Weather and crowd risk scoring.

STRICT RULES:
- Do NOT invent laws, policies, or government departments.
- Do NOT provide website links.
- Do NOT fabricate relief camp names.
- If location data is missing, politely ask for it.
- Use only Indian Rupees (₹).
- Stay concise and professional.
"""

# =====================================================
# CHAT FUNCTION
# =====================================================

def chat_with_ai(messages):

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "mistralai/mistral-7b-instruct",
            "messages": messages,
            "temperature": 0.2
        }
    )

    result = response.json()

    if "choices" in result:
        return result["choices"][0]["message"]["content"]
    else:
        return f"API Error: {result}"

# =====================================================
# MAIN CHAT LOOP
# =====================================================

if __name__ == "__main__":

    print("\n========== AI DISASTER CHAT ASSISTANT ==========")
    print("Type 'exit' to stop.\n")

    conversation = [
        {"role": "system", "content": SYSTEM_CONTEXT}
    ]

    while True:

        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("AI: Session ended. Stay safe.")
            break

        conversation.append({"role": "user", "content": user_input})

        ai_reply = chat_with_ai(conversation)

        print("\nAI:", ai_reply, "\n")

        conversation.append({"role": "assistant", "content": ai_reply})