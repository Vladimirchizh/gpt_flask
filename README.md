### Using flask for Generative transformers

    git clone https://github.com/Vladimirchizh/gpt_flask.git
    
Go to the model directory if you aren't there already

    cd gpt_flask

Launching docker

    docker build -t gpt_model -f Dockerfile .

Start

    docker run -d -p 8080:8080 gpt_model    
