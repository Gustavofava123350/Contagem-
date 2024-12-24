import flet as ft
from datetime import datetime, timedelta
import asyncio

# Função para atualizar a contagem regressiva
async def update_timer(page):
    while True:
        now = datetime.now()
        delta = countdown_time - now
        if delta > timedelta(0):
            timer_label.value = str(delta).split(".")[0]  # Exibe apenas horas, minutos e segundos
            page.update()
        else:
            timer_label.value = "Tempo esgotado!"
            page.update()
            break
        await asyncio.sleep(1)

# Definindo o tempo para contagem regressiva: 22 horas, 44 minutos e adicionando 1000 segundos a partir de agora
countdown_time = datetime.now() + timedelta(hours=22, minutes=44) + timedelta(seconds=1000)

# Função principal para configurar a interface
async def main(page: ft.Page):
    global timer_label
    timer_label = ft.Text(value="", style="displayLarge")
    
    # Centralizar o conteúdo
    page.add(ft.Column(
        controls=[timer_label],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    ))
    
    # Iniciar a contagem regressiva
    await update_timer(page)

# Inicialização da aplicação
ft.app(target=main)
