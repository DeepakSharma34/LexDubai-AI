from app.services.chat_service import ChatService


def main():

    chatbot = ChatService()

    question = "What is the probation period?"

    response = chatbot.ask(question)

    print("\nAnswer\n")
    print(response["answer"])

    print("\nSources\n")

    for source in response["sources"]:
        print(
            f"Article {source['article']} | Page {source['page']}"
        )


if __name__ == "__main__":
    main()