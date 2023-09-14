from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from dotenv import load_dotenv

load_dotenv()


def generate_story(captions, prompts=None):
    input_text = "\n".join(captions)

    prompt_text = ""

    if prompts:
        prompt_text = "\n".join(prompts)

    story_template = """
        given the following captions:
        {captions}

        {prompts}

        please generate a short story based on these captions within 250 words
    """

    story_prompt_template = PromptTemplate(
        input_variables=["captions","prompts"], template=story_template)

    llm = ChatOpenAI(temperature=0.8, model_name="gpt-3.5-turbo")

    chain = LLMChain(llm=llm, prompt=story_prompt_template)

    generated_story = chain.run(captions=input_text,prompts=prompt_text)

    return generated_story


if __name__ == "__main__":
    print("Hello LangChain!")

    # Example array of captions
    captions = [
        "Once upon a time in a small village, there lived a brave knight.",
        "The knight had a loyal steed named Thunder.",
        "One day, a fearsome dragon terrorized the village, and the knight set out to defeat it."
    ]

    # Example prompts (optional)
    prompts = [
        "Add some magic to the story.",
        "Include a wise old wizard who helps the knight on their quest."
    ]

    # Generate a story based on the captions and prompts
    generated_story = generate_story(captions, prompts)

    print("Generated Story:")
    print(generated_story)
