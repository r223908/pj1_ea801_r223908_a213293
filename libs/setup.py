from machine import Pin, ADC, I2C, PWM
import neopixel, utime
import ssd1306

# ==========================================
# 1. Variáveis Globais e Cores (SEMPRE PRIMEIRO)
# Tudo que a interrupção usa precisa vir antes dela
# ==========================================
corVermelha = (20, 0, 0)
corAzul = (0, 0, 20)
corVerde = (0, 20, 0)

cor_travada = corVermelha  # Motor começa vermelho
ultimo_tempo_btn = 0
ultimo_tempo_pisca = utime.ticks_ms()
indice_frame = 0

# ==========================================
# 2. Variáveis de Controle do Motor Virtual
# ==========================================
CENTRO_JOYSTICK = 32768
ZONA_MORTA = 4000
MAX_LEDS_POR_SEGUNDO = 100  # Ajuste a velocidade máxima aqui

# ==========================================
# 3. Configuração dos Botões (A, B e C)
# ==========================================
botao_a = Pin(5, Pin.IN, Pin.PULL_UP)
botao_b = Pin(6, Pin.IN, Pin.PULL_UP)
botao_c = Pin(10, Pin.IN, Pin.PULL_UP)


# ==========================================
# 4. Configuração do Joystick
# ==========================================
joystick_x = ADC(Pin(27))
joystick_y = ADC(Pin(26))
joystick_sw = Pin(22, Pin.IN, Pin.PULL_UP)

# ==========================================
# 5. Configuração do Display OLED (SSD1306)
# ==========================================
# Usando os pinos I2C corretos da BitDogLab V7 (SDA=14, SCL=15)
i2c = I2C(1, scl=Pin(3), sda=Pin(2), freq=400000)
display = ssd1306.SSD1306_I2C(128, 64, i2c, addr=0x3C)
display.fill(0)
display.show()

# ==========================================
# 6. Configuração da Matriz de LEDs
# ==========================================
NUM_LEDS = 25
np = neopixel.NeoPixel(Pin(7), NUM_LEDS)

LED_MEIO = 12

# Buffer circular da animação do motor
FRAMES_MOTOR = [
    [14, 13], [15, 16], [16, 24], [16, 23], [17, 22],
    [18, 21], [18, 20], [18, 19], [10, 11], [8, 9],
    [0, 8], [1, 8], [2, 7], [3, 6], [4, 6], [5, 6]
]

# ==========================================
# 7. Configuração do Buzzer
# ==========================================
# O Buzzer A da BitDogLab costuma ficar no GPIO 21
buzzer = PWM(Pin(21))
buzzer.duty_u16(0) # Garante que ele comece mudo (Volume 0)