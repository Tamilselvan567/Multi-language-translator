from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from googletrans import Translator

app = FastAPI(title="Multi-Language Translator API")

translator = Translator()

# Input Model
class TranslationRequest(BaseModel):
    text: str
    src_lang: str = "auto"   # auto detect if not given
    dest_lang: str

@app.post("/translate")
async def translate_text(request: TranslationRequest):
    try:
        translated = translator.translate(
            request.text,
            src=request.src_lang,
            dest=request.dest_lang
        )

        return {
            "original_text": request.text,
            "translated_text": translated.text,
            "source_language": translated.src,
            "target_language": request.dest_lang
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Optional: check API
@app.get("/")
async def home():
    return {"message": "Multi-Language Translator API is running 🚀"}