# Bolinha Multijogador

Este projeto implementa um jogo multiplayer onde cada jogador é representado por uma bolinha que se move em um campo. O jogo utiliza o protocolo MQTT para comunicação entre os jogadores, permitindo que eles publiquem suas posições e recebam atualizações sobre os movimentos dos outros.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação principal.
- **Paho MQTT**: Biblioteca para implementar o cliente MQTT em Python.
- **Tkinter**: Biblioteca para criar interfaces gráficas.
- **Docker**: Para gerenciar a infraestrutura do servidor MQTT.

## Estrutura do Projeto

- **pub.py**: Script responsável por publicar as posições dos jogadores.
- **sub.py**: Script responsável por assinar as mensagens e receber atualizações sobre os movimentos dos outros jogadores.
- **docker-compose.yaml**: Configuração do Docker para o servidor MQTT.

## Instalação

### Requisitos

Antes de executar o projeto, certifique-se de que você tem o Docker e Python instalados.

### Passos de Instalação

1. **Instale as dependências do Python**:
```bash
   pip install paho-mqtt
```

 ```bash
ou sudo apt-get install python3-paho-mqtt python3-tk
```

2. **Configure e inicie o Docker: Execute o seguinte comando para iniciar o servidor MQTT:**
   
```bash
docker-compose up -d
```

3. **Execute o código: Para iniciar o jogo, execute o seguinte comando:**
```bash
python3 pub.py
```
(É recomendável iniciar o assinante antes do publicador.)






   
