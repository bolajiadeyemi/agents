from dotenv import load_dotenv

load_dotenv()

from openai import OpenAI

client = OpenAI()

def get_temperature(city: str) -> float:
    """Get the temperature for a city."""
    return 20.0


def main():
    user_input = input("Your question: ")
    response = client.responses.create(
        model='gpt-4o',
        input=user_input,
    )

    reply = response.output_text
    print(reply)


if __name__ == "__main__":
    main()
