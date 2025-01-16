from dotenv import load_dotenv
import langchain_helper

load_dotenv()

if __name__ == "__main__":
    url = input("Enter a YouTube URL: ")
    llm = langchain_helper.create_llama_model()
    db = langchain_helper.create_vector_db_from_youtube_url(url)

    while True:
        question = input("Enter a question (or type 'exit' to quit): ")
        if question.lower() == 'exit':
            break

        print("\nUser Question: \n" + str(question))

        response = langchain_helper.generate_response(llm, db, question)
        print("\nLLM Response: \n" + str(response.content))
