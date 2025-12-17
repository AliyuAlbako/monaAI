from transformers import AutoTokenizer, AutoModelForCausalLM
from datetime import datetime
import torch

# Load model once (on startup)
# model_name = "NCAIR1/N-ATLaS"
model_name = "backend\app\models\N-ATLaS-GGUF-Q4_K_M.gguf"

print("Loading N-ATLaS model...")

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
    device_map="auto"
)

def generate_response(user_message):
    messages = [
        {
            "role": "system",
            "content": "You are Mona AI, a friendly multilingual assistant built by Awarri AI technologies."
        },
        {"role": "user", "content": user_message}
    ]

    current_date = datetime.now().strftime("%d %b %Y")

    text = tokenizer.apply_chat_template(
        messages,
        add_generation_prompt=True,
        tokenize=False,
        date_string=current_date
    )

    inputs = tokenizer(
        text,
        return_tensors="pt",
        add_special_tokens=False
    )

    # Move to GPU if available
    if torch.cuda.is_available():
        inputs = inputs.to("cuda")

    output = model.generate(
        **inputs,
        max_new_tokens=200,
        temperature=0.2,
        repetition_penalty=1.08
    )

    decoded = tokenizer.decode(output[0], skip_special_tokens=True)

    # Extract only Mona's final answer
    if "assistant" in decoded:
        decoded = decoded.split("assistant")[-1].strip()

    return decoded
