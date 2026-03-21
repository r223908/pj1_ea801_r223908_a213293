from setup import *

# Função de Interrupção dos Botões
def trata_interrupcao_botao(pino):
    # A linha abaixo é OBRIGATÓRIA para modificar variáveis de fora da função
    global cor_travada, ultimo_tempo_btn
    
    tempo_atual = utime.ticks_ms()
    
    # "Debounce" de 200ms
    if utime.ticks_diff(tempo_atual, ultimo_tempo_btn) > 200:
        if pino == botao_a:
            cor_travada = corVermelha
        elif pino == botao_b:
            cor_travada = corAzul
        elif pino == botao_c:
            cor_travada = corVerde
            
        ultimo_tempo_btn = tempo_atual

# Atribuir as interrupções aos botões
botao_a.irq(trigger=Pin.IRQ_FALLING, handler=trata_interrupcao_botao)
botao_b.irq(trigger=Pin.IRQ_FALLING, handler=trata_interrupcao_botao)
botao_c.irq(trigger=Pin.IRQ_FALLING, handler=trata_interrupcao_botao)

def printOled(desvio):
    # Limpa a tela antes de desenhar os novos dados
    display.fill(0) 
    
    # Cabeçalho
    display.text("BitDogLab V7", 16, 0)
    display.text("-" * 16, 0, 10)
    
    # 1. Lógica para descobrir a velocidade (%) e o sentido
    if abs(desvio) <= ZONA_MORTA:
        porcentagem = 0
        texto_sentido = "Parado"
    else:
        # Fator de 0.0 a 1.0 transformado em 0 a 100
        fator = (abs(desvio) - ZONA_MORTA) / (32768 - ZONA_MORTA)
        porcentagem = int(fator * 100)
        
        # Trava em 100% caso o ADC do joystick passe um pouquinho do limite
        if porcentagem > 100:
            porcentagem = 100
            
        # Define o sentido baseado no eixo Y (se precisar inverter, é só trocar o < por > aqui)
        if desvio < 0:
            texto_sentido = "Horario"
        else:
            texto_sentido = "Anti-horario"

    # 2. Plota as informações calculadas
    display.text("Sentido:", 0, 25)
    display.text(texto_sentido, 0, 35) # Coloquei na linha de baixo para não cortar o texto
    display.text(f"Velocidade: {porcentagem}%", 0, 50)
    
    # Envia para a telinha
    display.show()

def buzzerSound():
    # Se o valor for 0 (pressionado), liga o som. Se for 1 (solto), desliga.
    if joystick_sw.value() == 0:
        buzzer.freq(1000)        # Frequência do som (1000 Hz = um apito médio/agudo)
        buzzer.duty_u16(32768)   # Volume em 50% (metade de 65535)
    else:
        buzzer.duty_u16(0)       # Volume 0 (Desliga o buzzer)


ultimo_tempo_pisca = utime.ticks_ms()
ultimo_tempo_oled = utime.ticks_ms() # <-- ADICIONE ESTA LINHA
estado_led_motor = False

# Garante que todos os LEDs começam apagados
for i in range(NUM_LEDS):
    np[i] = (0, 0, 0)
np.write()

# ==========================================
# Ciclo Principal (Independente dos Botões)
# ==========================================
while True:
    # 1. Pega o tempo atual logo no início para todo mundo usar
    tempo_atual = utime.ticks_ms()
    
    # 2. Lemos o joystick
    valor_y = joystick_y.read_u16()
    desvio = valor_y - CENTRO_JOYSTICK
    
    # 3. Atualizamos a tela APENAS a cada 100ms (10 vezes por segundo)
    if utime.ticks_diff(tempo_atual, ultimo_tempo_oled) >= 100:
        printOled(desvio)
        ultimo_tempo_oled = tempo_atual

    # Limpa TODOS os LEDs da matriz de uma vez. 
    np.fill((0, 0, 0))

    buzzerSound()
    # 1. Zona Morta (Parado)
    if abs(desvio) <= ZONA_MORTA:
        np[LED_MEIO] = cor_travada  
    # 2. Fora da Zona Morta (Em movimento)
    else:
        fator_velocidade = (abs(desvio) - ZONA_MORTA) / (32768 - ZONA_MORTA)
        leds_por_segundo = fator_velocidade * MAX_LEDS_POR_SEGUNDO
        
        if leds_por_segundo < 0.1:
            leds_por_segundo = 0.1

        # Removi o "* 2" da sua fórmula original porque 
        # agora queremos avançar um frame inteiro a cada ciclo
        intervalo_ms = int(1000 / leds_por_segundo)

        tempo_atual = utime.ticks_ms()
        if utime.ticks_diff(tempo_atual, ultimo_tempo_pisca) >= intervalo_ms:
            # Lógica do Buffer Circular
            if desvio < 0:
                # Gira para um lado (avança na lista)
                indice_frame = (indice_frame + 1) % len(FRAMES_MOTOR)
            else:
                # Gira para o outro lado (retrocede na lista)
                indice_frame = (indice_frame - 1) % len(FRAMES_MOTOR)
                
            ultimo_tempo_pisca = tempo_atual

        # Acende os LEDs correspondentes ao frame atual na cor vermelha
        for led in FRAMES_MOTOR[indice_frame]:
            np[led] = cor_travada

    # Envia o desenho para a matriz fisicamente
    np.write()
    utime.sleep(0.01)