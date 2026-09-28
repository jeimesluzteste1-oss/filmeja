import os
from PIL import Image, ImageDraw

def create_filmeja_icon(size=512):
    # Cria imagem RGBA
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # 1. Fundo com cantos arredondados (Gradiente Vermelho Rubi / Cinema)
    radius = int(size * 0.22)
    
    # Criar gradiente vertical
    base_mask = Image.new('L', (size, size), 0)
    mask_draw = ImageDraw.Draw(base_mask)
    margin = int(size * 0.04)
    mask_draw.rounded_rectangle([margin, margin, size - margin, size - margin], radius=radius, fill=255)

    gradient = Image.new('RGBA', (size, size))
    for y in range(size):
        ratio = y / size
        # Interpolação de #e50914 (229, 9, 20) até #7d0309 (125, 3, 9)
        r = int(229 * (1 - ratio) + 110 * ratio)
        g = int(9 * (1 - ratio) + 3 * ratio)
        b = int(20 * (1 - ratio) + 9 * ratio)
        for x in range(size):
            gradient.putpixel((x, y), (r, g, b, 255))
            
    img.paste(gradient, (0, 0), base_mask)
    draw = ImageDraw.Draw(img)

    # 2. Desenhar contorno sutil do quadro de filme (película)
    line_w = max(2, int(size * 0.035))
    film_inset = int(size * 0.16)
    film_rect = [film_inset, film_inset, size - film_inset, size - film_inset]
    draw.rounded_rectangle(film_rect, radius=int(size * 0.08), outline=(255, 255, 255, 180), width=line_w)

    # 3. Pequenas perfurações de película nos cantos
    hole_r = int(size * 0.03)
    holes = [
        (film_inset + int(size * 0.07), film_inset + int(size * 0.07)),
        (size - film_inset - int(size * 0.07), film_inset + int(size * 0.07)),
        (film_inset + int(size * 0.07), size - film_inset - int(size * 0.07)),
        (size - film_inset - int(size * 0.07), size - film_inset - int(size * 0.07))
    ]
    for hx, hy in holes:
        draw.ellipse([hx - hole_r, hy - hole_r, hx + hole_r, hy + hole_r], fill=(255, 255, 255, 140))

    # 4. Triângulo de Play centralizado e destacado (Branco puro)
    # Centro aproximado (size/2, size/2)
    cx, cy = size / 2, size / 2
    pw = size * 0.28
    ph = size * 0.32
    # Deslocamento sutil para o centro visual do triângulo
    x_left = cx - pw * 0.4
    x_right = cx + pw * 0.6
    y_top = cy - ph * 0.5
    y_bottom = cy + ph * 0.5

    play_points = [
        (x_left, y_top),
        (x_right, cy),
        (x_left, y_bottom)
    ]
    draw.polygon(play_points, fill=(255, 255, 255, 255))

    return img

def main():
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    public_dir = os.path.join(root, 'public')
    app_dir = os.path.join(root, 'src', 'app')
    os.makedirs(public_dir, exist_ok=True)

    master = create_filmeja_icon(512)

    # Salva versões PNG
    master.save(os.path.join(public_dir, 'icon-512.png'), 'PNG')
    
    icon_192 = master.resize((192, 192), Image.Resampling.LANCZOS)
    icon_192.save(os.path.join(public_dir, 'icon-192.png'), 'PNG')

    icon_180 = master.resize((180, 180), Image.Resampling.LANCZOS)
    icon_180.save(os.path.join(public_dir, 'apple-touch-icon.png'), 'PNG')

    icon_32 = master.resize((32, 32), Image.Resampling.LANCZOS)
    icon_32.save(os.path.join(public_dir, 'icon.png'), 'PNG')

    icon_16 = master.resize((16, 16), Image.Resampling.LANCZOS)
    icon_48 = master.resize((48, 48), Image.Resampling.LANCZOS)

    # Salva favicon.ico com múltiplos tamanhos embutidos (16, 32, 48)
    favicon_path = os.path.join(public_dir, 'favicon.ico')
    master.save(favicon_path, format='ICO', sizes=[(16, 16), (32, 32), (48, 48)])
    
    # Também coloca na pasta app para garantir compatibilidade nativa do Next.js
    master.save(os.path.join(app_dir, 'favicon.ico'), format='ICO', sizes=[(16, 16), (32, 32), (48, 48)])

    print("[OK] Favicons e icones gerados com sucesso em public/ e src/app/!")

if __name__ == '__main__':
    main()
