
from flask import Flask, jsonify, request

app = Flask(__name__)

tarefas = [
    {"id": 1, "titulo": "Estudar Python", "concluida": False}
]

@app.route("/tarefas", methods=["GET"])
def listar_tarefas():
    return jsonify(tarefas)

@app.route("/tarefas", methods=["POST"])
def adicionar_tarefa():
    dados = request.json

    nova_tarefa = {
        "id": len(tarefas) + 1,
        "titulo": dados["titulo"],
        "concluida": False
    }

    tarefas.append(nova_tarefa)

    return jsonify(nova_tarefa), 201

@app.route("/tarefas/<int:id>", methods=["PUT"])
def concluir_tarefa(id):

    for tarefa in tarefas:

        if tarefa["id"] == id:
            tarefa["concluida"] = True
            return jsonify(tarefa)

    return jsonify({"erro": "Tarefa não encontrada"}), 404

@app.route("/tarefas/<int:id>", methods=["DELETE"])
def remover_tarefa(id):

    for tarefa in tarefas:

        if tarefa["id"] == id:
            tarefas.remove(tarefa)
            return jsonify({"mensagem": "Tarefa removida"})

    return jsonify({"erro": "Tarefa não encontrada"}), 404

app.run(debug=True)
