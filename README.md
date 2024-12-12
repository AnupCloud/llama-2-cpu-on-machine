# llama-2-cpu-on-machine

# How to run?
##An Intelligent Document Retrieval and Question-Answering System powered by RAG Architecture

### Steps 1:

clone the repository

```bash
git clone https://github.com/AnupCloud/llama-2-cpu-on-machine.git
```

### Steps 2:

Create a virtual environment

```bash
conda create -n cpullama python=3.10.11 -y
```

```bash
conda activate cpullama
```

```bash
pip install -r requirements.txt
```

```bash
python app.py
```


### Download the quantize model from the link provided in model folder & keep the model in the model directory:

```ini
## In case of Mac system
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source $HOME/.cargo/env

##verify install for rusts and cargo
rustc --version
cargo --version


## Download the Llama 2 Model:
llama-2-7b-chat.ggmlv3.q4_0.bin
## From the following link:
https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/tree/main


## From the following link:
https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/tree/main
```
