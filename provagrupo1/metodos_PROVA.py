def tarefa_nao_enviada():
    lista_nomes = []
    nomes =[]
    resposta_alunos = Resposta.objects.all()
    for responde_aluno in resposta_alunos:
        lista_nomes.append(responde_aluno.ra_aluno)
    total_alunos = Aluno.objects.exclude(id__in=lista_nomes)
    return total_alunos

def prazo_entrega(Id):
    dataatual= datetime.now()
    validacao_questoes = Questao.objects.filter(id)
    if validacao_questoes.data < data_atual:
        return print ( "VOCE NAO PODE FAZER A AVALIAÇÃO. PRAZO ENCERRADO")
    else:
        return "ATIVIDADE DISPONÍVEL"


def aplicacao_teste(user):
    if Resposta.objects.filter(id_aluno = user.id):
        return "EXERCICIO FEITO! AGUARDE SUA NOTA"
    else:
        open(exercicio)

    
def realizou_tarefa():

    lista_nomes = []
    resposta_alunos = Resposta.objects.all()
    total_alunos = Aluno.objects.all()
    for aluno in total_alunos:
        for responde_aluno in resposta_alunos:
            if aluno.id == responde_aluno.ra_aluno:
                lista_nomes.append(aluno.nome)
    return lista_nomes

def verificacao_matricula(Aluno,Id):
    matricula = Matricula.objects.all()
    disciplina = Disciplina_Ofertada.objects.all()
    turmas = Turma.objects.all()
    for matricula in Matricula:
        for turma in Turma:
            if matricula.idTurma == turma.idTurma:
                if turma.id_Disciplina_Ofertada == IdDisciplina:
                    print("VOCE JA ESTA CADASTRADO NESSA MATERIA")
                    break
                else:
                    print ("BEM VINDO AO CURSO")

def inclusao_matricula():
    matricula = Aluno(ra = "123859")
    matricula.save()
    return ("VOCE FOI MATRICULADO")


from medias import Media

P1 = input(float("Digite a nota da primeira prova"))
prova1 = Media()
prova1.P1()

T1 = input(float("Digite a nota total de trabalho do primeiro bimestre"))
trabalho1 = Media()
trabalho1.T1()

media_prova_b1 = P1.calcula_media_primeiro_bim() 
print(media_prova_b1)

media_trabalho_b1 = T1.calcula_media_primeiro_bim() 
print(media_trabalho_b1)

P2 = input(float("Digite a nota da segunda prova"))
prova2 = Media()
prova2.P2()

T2 = input(float("Digite a nota de trabalho do segundo bimestre"))
trabalho2 = Media()
trabalho2.T2()

media_prova_b2 = P2.calcula_media_primeiro_bim() 
print(media_prova_b2)

media_trabalho_b2 = T2.calcula_media_segundo_bim()
print(media_trabalho_b2)


class Media: 
    
    def __init__(self):
        self.p1 = ''
        self.p2 = ''
        self.t1 = ''
        self.t2 = ''

    def calcula_media_primeiro_bim(self,media1):
        if media1 >=7:
            self.media1 = media1
            media1 = (self.p1*0.7 + self.t1*0.3) / 2
            print("Aprovado no primeiro bimestre")
            return media1
        else:
            print("Precisa estudar para o segundo bimestre")
    
    def calcula_media_segundo_bim(self,media2):
        if media2 >=7:
            self.media2 = media2
            media2 = (self.p2*0.7 + self.t2*0.3) / 2
            print("Aprovado no segundo bimestre")
            return media2
        else:
            print("Ficou de exame")

    def calcula_media_final(self):
        if media_final <= 7:
            self.media_final = media_final 
            media_final = (self.media1 + self.media2) / 2
            return media_final
        elif media_final >=4 and <=7:
            print("Exame")
        else: 
            print("Dependencia")

