# ==========================
# COLORS
# ==========================

PRIMARY = "#4F46E5"
PRIMARY_HOVER = "#4338CA"

SUCCESS = "#22C55E"
SUCCESS_HOVER = "#16A34A"

DANGER = "#EF4444"
DANGER_HOVER = "#DC2626"

WARNING = "#F59E0B"

GRAY = "#6B7280"
GRAY_HOVER = "#4B5563"

LIGHT_BORDER = "#E5E7EB"

TITLE = "#111827"
TEXT = "#374151"

WHITE = "white"

# ==========================
# FONTS
# ==========================

TITLE_FONT = ("Segoe UI", 30, "bold")

HEADING_FONT = ("Segoe UI", 22, "bold")

SUBTITLE_FONT = ("Segoe UI", 18)

BODY_FONT = ("Segoe UI", 16)

SMALL_FONT = ("Segoe UI", 14)

# ==========================
# BUTTON PRESETS
# NOTE: These only hold style properties (no "width"
# or "height"). Each screen sets width/height per-button,
# and duplicating them here causes:
# TypeError: got multiple values for keyword argument 'height'
# ==========================

BUTTON = {
    "fg_color": PRIMARY,
    "hover_color": PRIMARY_HOVER,
    "text_color": WHITE,
    "corner_radius": 10,
}

SUCCESS_BUTTON = {
    "fg_color": SUCCESS,
    "hover_color": SUCCESS_HOVER,
    "text_color": WHITE,
    "corner_radius": 10,
}

DANGER_BUTTON = {
    "fg_color": DANGER,
    "hover_color": DANGER_HOVER,
    "text_color": WHITE,
    "corner_radius": 10,
}

GRAY_BUTTON = {
    "fg_color": GRAY,
    "hover_color": GRAY_HOVER,
    "text_color": WHITE,
    "corner_radius": 10,
}