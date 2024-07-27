import requests
from datetime import datetime, timedelta
import locale

# Definir a localidade para português do Brasil
locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')

# Função para fazer a requisição POST
def fazer_requisicao_post(mes, dia, horarios):
    url = f'https://thtato-20e86-default-rtdb.firebaseio.com/meses/{mes}/dias/{dia}.json'
    headers = {'Content-Type': 'application/json'}
    response = requests.put(url, json=horarios, headers=headers)  # Use PUT to ensure the structure is correct
    if response.status_code == 200:
        print("Requisição POST bem-sucedida!")
    else:
        print(f"Falha na requisição POST - Status code: {response.status_code}")

# Função para gerar todas as datas de 2024
def gerar_datas_2024():
    ano = 2024
    data_inicio = datetime(ano, 1, 1)
    data_fim = datetime(ano, 12, 31)
    delta = timedelta(days=1)
    data_atual = data_inicio

    while data_atual <= data_fim:
        yield data_atual
        data_atual += delta

# Gerar e enviar dados para cada data em 2024
for data in gerar_datas_2024():
    data_formatada = data.strftime('%d/%m/%Y')  # Formato dd/mm/aaaa
    mes = data.strftime('%m')  # Formato de dois dígitos para o mês
    dia = data.strftime('%d')  # Formato de dois dígitos para o dia
    dia_da_semana = data.strftime('%A')  # Nome completo do dia da semana em português

    # Preparar os dados para enviar
    if dia_da_semana == 'terÃ§a-feira':
        dia_da_semana = 'terca-feira'

    if dia_da_semana == 'sÃ¡bado':
        dia_da_semana = 'sabado'

    horarios = {}
    for hora in range(10, 21):
        horario_str = f'{hora:02d}:00'
        horarios[horario_str] = {
            'horario': horario_str,
            'disponibilidade': True
        }

    nova_tarefa = {
        'data': data_formatada,
        'mes': mes,
        'dia': dia,
        'diadasemana': dia_da_semana,
        'horarios': horarios
    }

    # Enviar a requisição POST para cada dia com seus horários
    fazer_requisicao_post(mes, dia, nova_tarefa)
