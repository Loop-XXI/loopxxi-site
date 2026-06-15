from pathlib import Path
from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets"
OUT.mkdir(exist_ok=True)


BG = (10, 10, 10)
BONE = (232, 230, 223)
MUTED = (138, 135, 126)
DIM = (80, 77, 70)
SURFACE = (20, 20, 18)
GOLD = (181, 151, 88)


def font(size: int, bold: bool = False):
    candidates = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/liberation2/LiberationSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/liberation2/LiberationSans-Regular.ttf",
    ]
    for c in candidates:
        if Path(c).exists():
            return ImageFont.truetype(c, size)
    return ImageFont.load_default()


def fit_text(draw, text, max_width, start_size, bold=False, min_size=18):
    size = start_size
    while size >= min_size:
        f = font(size, bold)
        if draw.multiline_textbbox((0, 0), text, font=f, spacing=int(size * 0.35))[2] <= max_width:
            return f
        size -= 2
    return font(min_size, bold)


def paste_contained(base, img, box):
    x, y, w, h = box
    img = img.copy()
    img.thumbnail((w, h), Image.Resampling.LANCZOS)
    bx = x + (w - img.width) // 2
    by = y + (h - img.height) // 2
    if img.mode == "RGBA":
        base.alpha_composite(img, (bx, by))
    else:
        base.paste(img, (bx, by))


def loop_lines(draw, width, height, muted=False):
    color = DIM if muted else (46, 44, 39)
    for i in range(5):
        inset = 80 + i * 58
        draw.ellipse((width - 520 - i * 18, inset, width - 80 + i * 18, inset + 260 + i * 22), outline=color, width=1)
        draw.ellipse((80 - i * 18, height - 340 - i * 18, 520 + i * 18, height - 80 + i * 22), outline=color, width=1)


def save_card(path, size, mode):
    w, h = size
    base = Image.new("RGBA", size, BG + (255,))
    d = ImageDraw.Draw(base)
    loop_lines(d, w, h)
    d.rectangle((0, 0, w, h), outline=(32, 31, 28), width=2)

    logo = Image.open(ROOT / "LoopXXI-wordmark.png").convert("RGBA")
    mark = Image.open(ROOT / "LoopXXI-Logo.png").convert("RGBA")

    if mode == "parent-og":
        paste_contained(base, logo, (70, 68, 330, 120))
        title = "Systems that return stronger."
        body = "LoopXXI builds and holds durable systems shaped by feedback, time, and disciplined repetition."
        d.text((80, 335), title, font=fit_text(d, title, 790, 62, True), fill=BONE)
        d.multiline_text((82, 445), body, font=font(30), fill=MUTED, spacing=12)
        paste_contained(base, mark, (880, 230, 220, 220))
        d.text((82, h - 90), "Letter No. I · The First Loop", font=font(23), fill=DIM)

    elif mode == "banner":
        paste_contained(base, logo, (70, 48, 260, 92))
        d.text((420, 76), "Time is part of the machine.", font=font(42, True), fill=BONE)
        d.text((422, 138), "feedback · persistence · compounding", font=font(20), fill=MUTED)

    elif mode == "gateway":
        paste_contained(base, mark, (60, 50, 84, 84))
        d.text((170, 58), "What is Loop Gateway?", font=font(48, True), fill=BONE)
        d.text((172, 122), "AI model access for agent operators.", font=font(24), fill=MUTED)
        items = [
            ("1", "Pay sats", "Top up once over Lightning."),
            ("2", "Get bearer credit", "No account, card, or per-call invoice wait."),
            ("3", "Call 300+ models", "Use any OpenAI SDK with one base URL."),
        ]
        y = 230
        for n, head, body in items:
            d.ellipse((74, y + 6, 126, y + 58), outline=GOLD, width=2)
            d.text((93, y + 16), n, font=font(24, True), fill=GOLD)
            d.text((154, y), head, font=font(30, True), fill=BONE)
            d.text((154, y + 42), body, font=font(22), fill=MUTED)
            y += 135
        d.text((72, h - 78), "L402 · Lightning · OpenAI-compatible", font=font(22), fill=DIM)

    elif mode == "agentready":
        paste_contained(base, mark, (60, 50, 84, 84))
        d.text((170, 58), "What is agentready?", font=font(48, True), fill=BONE)
        d.text((172, 122), "AI code fixes, paid in sats.", font=font(24), fill=MUTED)
        items = [
            ("Send a repo or issue", "Agentready audits the surface and finds the fix path."),
            ("Pay sats", "A clean Lightning payment gates the work."),
            ("Receive code fixes", "Small patches, ready for review, with the failure explained."),
        ]
        y = 235
        for head, body in items:
            d.rounded_rectangle((72, y, w - 72, y + 94), radius=20, fill=SURFACE, outline=(35, 34, 31), width=1)
            d.text((108, y + 18), head, font=font(27, True), fill=BONE)
            d.text((108, y + 54), body, font=font(19), fill=MUTED)
            y += 118
        d.text((72, h - 78), "agent operators · code repair · Lightning settlement", font=font(22), fill=DIM)

    base.convert("RGB").save(OUT / path, quality=95)


save_card("loopxxi-og-card.png", (1200, 630), "parent-og")
save_card("loopxxi-nostr-banner.png", (1500, 500), "banner")
save_card("loop-gateway-explainer.png", (1080, 1080), "gateway")
save_card("agentready-explainer.png", (1080, 1080), "agentready")

print("generated", sorted(p.name for p in OUT.glob("*.png")))
