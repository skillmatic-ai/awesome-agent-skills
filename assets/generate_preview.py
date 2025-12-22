#!/usr/bin/env python3
"""Generate social preview image for Awesome Agent Skills repository"""

from PIL import Image, ImageDraw, ImageFont
import os

# Dimensions for GitHub social preview
WIDTH = 1280
HEIGHT = 640

# Color scheme - bright and positive theme
BG_COLOR = "#1E293B"  # Lighter slate blue
ACCENT_COLOR = "#A78BFA"  # Bright purple
SECONDARY_COLOR = "#22D3EE"  # Bright cyan
TEXT_COLOR = "#FFFFFF"  # Pure white
SUBTITLE_COLOR = "#CBD5E1"  # Bright light gray

# Create image
img = Image.new('RGB', (WIDTH, HEIGHT), BG_COLOR)
draw = ImageDraw.Draw(img)

# Add gradient-like effect with circles - brighter and more vibrant
for i in range(5):
    x = WIDTH * (0.2 + i * 0.2)
    y = HEIGHT * (0.3 + (i % 2) * 0.4)
    radius = 150 - i * 20
    # Create circular gradient effect with brighter colors
    for r in range(radius, 0, -8):
        color = ACCENT_COLOR if i % 2 == 0 else SECONDARY_COLOR
        # Draw semi-transparent circles
        left = x - r
        top = y - r
        right = x + r
        bottom = y + r
        draw.ellipse([left, top, right, bottom], fill=None, outline=color, width=1)

# Try to use system fonts, fallback to default
try:
    # Try to load a nice font
    title_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 90)
    subtitle_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 40)
    tagline_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 32)
    badge_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 28)
except:
    # Fallback to default font
    title_font = ImageFont.load_default()
    subtitle_font = ImageFont.load_default()
    tagline_font = ImageFont.load_default()
    badge_font = ImageFont.load_default()

# Add main title - start after emoji to avoid white rectangle
title = "Awesome Agent Skills"
emoji = "🎯"

# Calculate positions
title_bbox = draw.textbbox((0, 0), title, font=title_font)
title_width = title_bbox[2] - title_bbox[0]
emoji_bbox = draw.textbbox((0, 0), emoji, font=title_font)
emoji_width = emoji_bbox[2] - emoji_bbox[0]

total_width = emoji_width + 20 + title_width
start_x = (WIDTH - total_width) // 2
title_y = 180

# Draw emoji
draw.text((start_x, title_y), emoji, font=title_font, embedded_color=True)

# Draw title with shadow effect for better contrast
draw.text((start_x + emoji_width + 20 + 2, title_y + 2), title, fill="#000000", font=title_font)
draw.text((start_x + emoji_width + 20, title_y), title, fill=TEXT_COLOR, font=title_font)

# Add tagline
tagline = "The definitive resource for Agent Skills"
tagline_bbox = draw.textbbox((0, 0), tagline, font=subtitle_font)
tagline_width = tagline_bbox[2] - tagline_bbox[0]
tagline_x = (WIDTH - tagline_width) // 2
tagline_y = title_y + 110

# Add shadow for contrast
draw.text((tagline_x + 2, tagline_y + 2), tagline, fill="#000000", font=subtitle_font)
draw.text((tagline_x, tagline_y), tagline, fill=SUBTITLE_COLOR, font=subtitle_font)

# Add description - removed "70+" as it will change
desc = "Skills • Tools • Tutorials • Research"
desc_bbox = draw.textbbox((0, 0), desc, font=tagline_font)
desc_width = desc_bbox[2] - desc_bbox[0]
desc_x = (WIDTH - desc_width) // 2
desc_y = tagline_y + 70

# Add shadow for contrast
draw.text((desc_x + 2, desc_y + 2), desc, fill="#000000", font=tagline_font)
draw.text((desc_x, desc_y), desc, fill=ACCENT_COLOR, font=tagline_font)

# Add bottom badge-like elements - adjusted to fit longer text
badge_y = HEIGHT - 80
badge_texts = ["Claude", "Cursor", "GitHub Copilot", "OpenAI Codex"]
badges = []

# Calculate width for each badge based on text
for text in badge_texts:
    text_bbox = draw.textbbox((0, 0), text, font=badge_font)
    text_width = text_bbox[2] - text_bbox[0]
    badge_width = text_width + 40  # Add padding
    badges.append((text, badge_width))

# Calculate total width and spacing
total_badges_width = sum(w for _, w in badges) + (len(badges) - 1) * 20  # 20px spacing between badges
start_x = (WIDTH - total_badges_width) // 2
current_x = start_x

for text, badge_width in badges:
    # Draw rounded rectangle with shadow for depth
    draw.rounded_rectangle(
        [current_x + 2, badge_y + 2, current_x + badge_width + 2, badge_y + 47],
        radius=22,
        fill="#000000"
    )
    draw.rounded_rectangle(
        [current_x, badge_y, current_x + badge_width, badge_y + 45],
        radius=22,
        fill=None,
        outline=SECONDARY_COLOR,
        width=3
    )
    # Draw text centered
    text_bbox = draw.textbbox((0, 0), text, font=badge_font)
    text_width = text_bbox[2] - text_bbox[0]
    text_x = current_x + (badge_width - text_width) // 2
    text_y = badge_y + 10
    draw.text((text_x, text_y), text, fill=TEXT_COLOR, font=badge_font)
    
    current_x += badge_width + 20  # Move to next badge position

# Save the image
output_path = os.path.join(os.path.dirname(__file__), 'social-preview.png')
img.save(output_path, 'PNG', optimize=True, quality=95)
print(f"Social preview image created: {output_path}")
print(f"Dimensions: {WIDTH}x{HEIGHT}px")
