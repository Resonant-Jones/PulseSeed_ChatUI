"""UI style definitions."""
# Note: Qt stylesheets do not support 'backdrop-filter'. Use QGraphicsBlurEffect in code instead if you want real blur.
GLASS_BUBBLE = """
QWidget {
    background-color: rgba(255, 255, 255, 0.15);
    border-radius: 16px;
}
"""

WAVEFORM_COLOR = "#00FFAA"
