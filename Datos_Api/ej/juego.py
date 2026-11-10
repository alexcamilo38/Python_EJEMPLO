
from ursina import *
import math

# Inicializar la aplicación
app = Ursina()

# Configuración de la ventana y estética llamativa
window.title = "Mi Juego 3D en Python"
window.borderless = False
window.color = color.rgb(15, 15, 25)

# --- ENTORNO ---
# Suelo con cuadrícula y cielo oscuro futurista
ground = Entity(model='plane', scale=(60, 1, 60), color=color.dark_gray, texture='white_cube')
sky = Sky(color=color.rgb(20, 20, 40))

# --- JUGADOR ---
# Cubo principal que controlas con las teclas
player = Entity(model='cube', color=color.cyan, scale=(1, 2, 1), position=(0, 1, 0))

# --- OBJETOS ANIMADOS Y MULTIFUNCIONALES ---
# Creamos una lista de objetos flotantes con animaciones independientes
animated_objects = []
colors_list = [color.red, color.orange, color.yellow, color.green, color.magenta]

for i in range(5):
    obj = Entity(
        model='cube', 
        color=colors_list[i], 
        position=(i * 4 - 8, 1.5, 6), 
        scale=1.2
    )
    animated_objects.append(obj)

# Variables de control para el mouse (Clic derecho)
is_right_clicking = False

def input(key):
    global is_right_clicking
    # Detectar cuando se presiona o suelta el clic derecho
    if key == 'right mouse down':
        is_right_clicking = True
    elif key == 'right mouse up':
        is_right_clicking = False

def update():
    # 1. MOVIMIENTO CON TECLAS ESPECÍFICAS (WASD o Flechas)
    speed = 6 * time.dt
    if held_keys['w'] or held_keys['up arrow']:
        player.z += speed
    if held_keys['s'] or held_keys['down arrow']:
        player.z -= speed
    if held_keys['a'] or held_keys['left arrow']:
        player.x -= speed
    if held_keys['d'] or held_keys['right arrow']:
        player.x += speed

    # 2. CONTROL CON CLIC DERECHO DEL MOUSE
    global is_right_clicking
    if is_right_clicking:
        # Si mantienes presionado el clic derecho, rotas la cámara con el movimiento del mouse
        camera.rotation_y += mouse.velocity[0] * 120
        camera.rotation_x -= mouse.velocity[1] * 120

    # 3. ANIMACIONES Y MULTIFUNCIONALIDAD
    # Hacemos que los objetos floten y roten constantemente para dar dinamismo
    for index, obj in enumerate(animated_objects):
        obj.rotation_y += 40 * time.dt
        obj.rotation_x += 20 * time.dt
        # Efecto de levitación usando funciones trigonométricas
        obj.y = 1.5 + math.sin(time.time() * 3 + index) * 0.8

# Ejecutar el juego
app.run()