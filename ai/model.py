import google.generativeai as genai
from config import GEMINI_KEY, GEN_CONFIG, MODEL, PROMPT, SAFETY_SETTINGS
from review_extractor import ReviewsExtractor


class Gemini:
    def __init__(self):
        pass

    def config_model(self):
        genai.configure(api_key=GEMINI_KEY)

        model = genai.GenerativeModel(
            model_name=MODEL,
            generation_config=GEN_CONFIG,
            safety_settings=SAFETY_SETTINGS,
        )

        return model

    def response(self, model, content):
        response = model.generate_content(content)
        print(response.text)


def main():
    extract = ReviewsExtractor()
    prod_id = "ff29d8cb1cd0cd5ea37b80dac9939e1c"

    df = extract.read_table(product_id=prod_id)
    extract.reviews_to_txt(df)
    reviews = extract.load_txt()

    prompt = f"{PROMPT}\n\n{reviews}"

    gemini = Gemini()
    model = gemini.config_model()
    gemini.response(model, prompt)


if __name__ == "__main__":
    main()
