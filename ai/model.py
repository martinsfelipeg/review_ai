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
        text = response.text
        print(text)

        return text


def main():
    extract = ReviewsExtractor()
    prod_id = "601a360bd2a916ecef0e88de72a6531a"

    df = extract.read_table(product_id=prod_id)
    extract.reviews_to_txt(df)
    reviews = extract.load_txt()

    prompt = f"{PROMPT}\n\n{reviews}"

    gemini = Gemini()
    model = gemini.config_model()
    text = gemini.response(model, prompt)

    extract.build_report(ai_response=text)


if __name__ == "__main__":
    main()
