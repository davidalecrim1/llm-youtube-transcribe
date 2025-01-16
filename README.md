# LLM Youtube Transcribe With Python
Using Python to transcribe YouTube videos and summarize them using a Language Learning Model (LLM).

## Getting Started
This project uses Ollama locally on a Mac M1.

### Prerequisites
- Python 3
- Docker
- [Ollama](https://ollama.com/download)
- [Open-WebUI](https://openwebui.com) or [LM Studio](https://lmstudio.ai/docs)

### Installation

1. **Install Ollama**
   - Download and install Ollama from the [official website](https://ollama.com/download).

2. **Run Open-WebUI using Docker**
   - Download and run Open-WebUI:
     ```sh
     make run-webui
     ```

3. **Update Open-WebUI**
   - To update Open-WebUI, run:
     ```sh
     make update-webui
     ```

### Usage

1. **Set up environment variables**
   - Create a `.env` file with the necessary environment variables.

2. **Run the script**
   - Execute the main.py script:
     ```sh
     python main.py
     ```

3. **Interact with the script**
   - Enter a YouTube URL when prompted.
   - Ask questions about the video transcript.

### Example

```sh
$ python main.py
Enter a YouTube URL: https://www.youtube.com/watch?v=example
Enter a question (or type 'exit' to quit): What is the video about?