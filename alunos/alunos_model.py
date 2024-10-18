from config import db

class Aluno(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    idade = db.Column(db.Integer)
    turma = db.Column(db.String(20))
    data_nascimento = db.Column(db.String(10))
    nota_primeiro_semestre = db.Column(db.Float)
    nota_segundo_semestre = db.Column(db.Float)
    media_final = db.Column(db.Float)

    def __init__(self, nome, idade, turma, data_nascimento, nota_primeiro_semestre, nota_segundo_semestre, media_final):
        self.nome = nome
        self.idade = idade
        self.turma = turma
        self.data_nascimento = data_nascimento
        self.nota_primeiro_semestre = nota_primeiro_semestre
        self.nota_segundo_semestre = nota_segundo_semestre
        self.media_final = media_final

    def to_dict(self):
        return {'id': self.id, 'nome': self.nome,'idade': self.idade ,'turma': self.turma, 'data_nascimento': self.data_nascimento, 'nota_primeiro_semestre':self.nota_primeiro_semestre, 'nota_segundo_semestre':self.nota_segundo_semestre,'media_final':self.media_final}

class AlunoNaoEncontrado(Exception):
    pass

def aluno_por_id(id_aluno):
    aluno = Aluno.query.get(id_aluno)
    if not aluno:
        raise AlunoNaoEncontrado
    return aluno.to_dict()

def listar_alunos():
    alunos = Aluno.query.all()
    return [aluno.to_dict() for aluno in alunos]

def adicionar_aluno(aluno_data):
    novo_aluno = Aluno(nome=aluno_data['nome'], idade=aluno_data['idade'], turma=aluno_data['turma'], data_nascimento=aluno_data['data_nascimento'], nota_primeiro_semestre=aluno_data['nota_primeiro_semestre'], nota_segundo_semestre=aluno_data['nota_segundo_semestre'], media_final=aluno_data['media_final'])
    db.session.add(novo_aluno)
    db.session.commit()

def atualizar_aluno(id_aluno, novos_dados):
    aluno = Aluno.query.get(id_aluno)
    if not aluno:
        raise AlunoNaoEncontrado
    aluno.nome = novos_dados['nome']
    aluno.idade = novos_dados['idade']
    aluno.turma = novos_dados['turma']
    aluno.data_nascimento = novos_dados['data_nascimento']
    aluno.nota_primeiro_semestre = novos_dados['nota_primeiro_semestre']
    aluno.nota_segundo_semestre = novos_dados['nota_segundo_semestre']
    aluno.media_final = novos_dados['media_final']
    db.session.commit()

def excluir_aluno(id_aluno):
    aluno = Aluno.query.get(id_aluno)
    if not aluno:
        raise AlunoNaoEncontrado
    db.session.delete(aluno)
    db.session.commit()
