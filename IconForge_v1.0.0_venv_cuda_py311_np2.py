#IconForge_v1.0.0_venv_cuda_py311_np2.py
#PowerShell 1-liner: . C:\Users\ansem\Documents\GitHub\_venvs\venv_cuda_py311_np2\Scripts\Activate.ps1; python .\IconForge_v1.0.0_venv_cuda_py311_np2.py
import sys
import os
from pathlib import Path
from datetime import datetime
from typing import Iterable
from PIL import Image
from PySide6.QtCore import QPointF, QRectF, Qt
from PySide6.QtGui import QColor, QFont, QIcon, QLinearGradient, QPainter, QPainterPath, QPen, QPixmap
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QFileDialog,
    QLineEdit,
    QMessageBox,
    QTabWidget,
    QCheckBox,
    QComboBox,
    QGroupBox,
    QTextEdit,
    QProgressBar,
)


def detect_active_venv() -> str:
    if getattr(sys, "frozen", False):
        return "standalone_exe"
    venv_path = os.environ.get("VIRTUAL_ENV", "").strip()
    if venv_path:
        return Path(venv_path).name
    return Path(sys.executable).resolve().parent.parent.name


EXPECTED_VENVS = [
    "venv_cuda_py311_np2",
    "venv_cuda_py311_np1",
    "venv_cuda_py313_np2",
    "venv_cuda_py308_np1",
    "venv_realportrait_py311_np1",
]
active_venv = detect_active_venv()
if active_venv != "standalone_exe" and active_venv not in EXPECTED_VENVS:
    print(
        "WAARSCHUWING: actieve venv komt niet overeen met EXPECTED_VENVS.\n"
        f"Actief: {active_venv}\n"
        f"Verwacht: {', '.join(EXPECTED_VENVS)}",
        file=sys.stderr,
    )
    sys.exit(1)
APP_VENV = active_venv
APP_NAME = "IconForge"
APP_VERSION = "v1.0.0"
APP_PATH = Path(__file__).resolve()
APP_DIR = Path(getattr(sys, "_MEIPASS", APP_PATH.parent))
APP_ICON_PATH = APP_DIR / "IconForge.ico"
APP_LOGO_PATH = APP_DIR / "IconForge_logo.png"
APP_TEXT_LOGO_PATH = APP_DIR / "IconForge_text.png"
APP_NAME_APP_VERSION = f"{APP_NAME} {APP_VERSION}"
APP_TITLE = f"{APP_NAME} - {APP_VERSION}"
SUPPORTED_EXTENSIONS = {".png", ".jpg", ".jpeg", ".webp", ".bmp", ".tiff"}
ICO_EXTENSION = ".ico"
DEFAULT_ICON_SIZES = [16, 32, 48, 64, 128, 256]
THEME_FORGE_DARK = "Forge Dark"
THEME_CUDA_BLUE = "CUDA Blue"


ICONFORGE_THEME_QSS = """
    QWidget {
        background-color: #1E1E1E;
        color: #EAEAEA;
        font-family: 'Segoe UI';
        font-size: 13px;
    }
    QTabWidget::pane {
        border: 1px solid #333333;
        background-color: #1A1A1A;
    }
    QTabBar::tab {
        background-color: #2A2A2A;
        color: #DADADA;
        padding: 10px 16px;
        margin-right: 2px;
        border-top-left-radius: 6px;
        border-top-right-radius: 6px;
    }
    QTabBar::tab:selected {
        background-color: #00B4D8;
        color: #081018;
        font-weight: bold;
    }
    QPushButton {
        background-color: #2C2C2C;
        border: 1px solid #444444;
        border-radius: 8px;
        padding: 8px 12px;
        font-weight: 600;
    }
    QPushButton:hover {
        background-color: #383838;
    }
    QPushButton#primaryButton {
        background-color: rgba(0, 180, 216, 0.25);
        border: 1px solid #00B4D8;
        color: #EFFFFF;
    }
    QPushButton#primaryButton:hover {
        background-color: rgba(0, 180, 216, 0.38);
    }
    QLineEdit, QTextEdit, QComboBox {
        background-color: #111111;
        border: 1px solid #333333;
        border-radius: 6px;
        padding: 8px;
        color: #F0F0F0;
    }
    QGroupBox {
        border: 1px solid #333333;
        border-radius: 8px;
        margin-top: 10px;
        padding-top: 12px;
        font-weight: 700;
    }
    QGroupBox::title {
        subcontrol-origin: margin;
        left: 12px;
        padding: 0 4px;
    }
    QLabel#appTitle {
        font-size: 28px;
        font-weight: 900;
        color: #F8FBFF;
    }
    QLabel#appSubtitle {
        color: #9AA4AD;
        font-size: 13px;
    }
    QLabel#statusOk {
        color: #63E6BE;
        font-weight: 700;
    }
    QLabel#statusError {
        color: #FF6B6B;
        font-weight: 700;
    }
    QProgressBar {
        border: 1px solid #333333;
        border-radius: 7px;
        text-align: center;
        background-color: #111111;
        color: #F0F0F0;
        min-height: 24px;
    }
    QProgressBar::chunk {
        background-color: #00B4D8;
        border-radius: 6px;
    }
"""


CUDA_THEME_QSS = """
    QWidget {
        background: #050812;
        color: #eef5ff;
        font-family: 'Segoe UI', Arial;
        font-size: 13px;
    }
    QTabWidget::pane {
        border: 1px solid #203752;
        background: #070d18;
    }
    QTabBar::tab {
        background: #0a1220;
        color: #c5dbf2;
        padding: 10px 16px;
        margin-right: 2px;
        border-top-left-radius: 6px;
        border-top-right-radius: 6px;
        font-weight: 700;
    }
    QTabBar::tab:selected {
        background: #13243a;
        color: #ffffff;
        border-bottom: 2px solid #36bffa;
    }
    QPushButton {
        background: qlineargradient(x1:0,y1:0,x2:0,y2:1, stop:0 #19304d, stop:1 #0f2035);
        border: 1px solid #315578;
        border-radius: 8px;
        padding: 8px 12px;
        color: #e6f4ff;
        font-weight: 800;
    }
    QPushButton:hover {
        background: #1c426c;
        border-color: #67d4ff;
    }
    QPushButton:pressed {
        background: #0c1a2c;
    }
    QPushButton#primaryButton {
        background: #36bffa;
        border-color: #8ee4ff;
        color: #03111f;
    }
    QPushButton#primaryButton:hover {
        background: #67d4ff;
    }
    QLineEdit, QTextEdit, QComboBox {
        background: #060d18;
        border: 1px solid #263d58;
        border-radius: 7px;
        padding: 8px;
        color: #edf4ff;
    }
    QGroupBox {
        border: 1px solid #234164;
        border-radius: 8px;
        margin-top: 10px;
        padding-top: 12px;
        font-weight: 900;
        color: #dcecff;
    }
    QGroupBox::title {
        subcontrol-origin: margin;
        left: 12px;
        padding: 0 4px;
    }
    QLabel#appTitle {
        font-size: 30px;
        font-weight: 900;
        color: #ffffff;
    }
    QLabel#appSubtitle {
        color: #c5dbf2;
        font-size: 13px;
    }
    QLabel#statusOk {
        color: #7EE787;
        font-weight: 900;
    }
    QLabel#statusError {
        color: #FF6B6B;
        font-weight: 900;
    }
    QProgressBar {
        border: 1px solid #263d58;
        border-radius: 9px;
        background: #060d18;
        color: #edf4ff;
        text-align: center;
        font-weight: 900;
        min-height: 24px;
    }
    QProgressBar::chunk {
        background: qlineargradient(x1:0,y1:0,x2:1,y2:0, stop:0 #36bffa, stop:1 #7ee787);
        border-radius: 8px;
    }
"""


def generate_requirements_file() -> Path:
    requirements_dir = Path(r"C:\Users\ansem\Documents\github\requirements")
    requirements_dir.mkdir(parents=True, exist_ok=True)
    req_path = requirements_dir / f"requirements_iconforge_{APP_VERSION}_{APP_VENV}.txt"

    try:
        pillow_version = Image.__version__
    except Exception:
        pillow_version = "unknown"

    lines = [
        f"# Gegenereerd op {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        f"Pillow=={pillow_version}" if pillow_version != "unknown" else "Pillow",
        "PySide6",
    ]
    req_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return req_path


def normalize_sizes(size_values: Iterable[int]) -> list[tuple[int, int]]:
    unique_sorted = sorted({int(v) for v in size_values if int(v) > 0})
    return [(v, v) for v in unique_sorted]


def fit_image_in_square(img: Image.Image, square_size: int) -> Image.Image:
    fitted = img.copy()
    fitted.thumbnail((square_size, square_size), Image.Resampling.LANCZOS)

    canvas = Image.new("RGBA", (square_size, square_size), (0, 0, 0, 0))
    offset_x = (square_size - fitted.width) // 2
    offset_y = (square_size - fitted.height) // 2
    canvas.paste(fitted, (offset_x, offset_y), fitted)
    return canvas


def is_supported_image(path: Path) -> bool:
    return path.is_file() and path.suffix.lower() in SUPPORTED_EXTENSIONS


def is_supported_ico(path: Path) -> bool:
    return path.is_file() and path.suffix.lower() == ICO_EXTENSION


def iter_supported_images(folder: Path, recursive: bool) -> list[Path]:
    iterator = folder.rglob("*") if recursive else folder.glob("*")
    return sorted([path for path in iterator if is_supported_image(path)])


def convert_image_to_ico(input_path: Path, output_path: Path, icon_sizes: list[tuple[int, int]]) -> None:
    if not input_path.exists():
        raise FileNotFoundError(f"Bestand niet gevonden: {input_path}")

    if input_path.suffix.lower() not in SUPPORTED_EXTENSIONS:
        raise ValueError(
            "Niet ondersteund bestandstype. Gebruik: "
            + ", ".join(sorted(SUPPORTED_EXTENSIONS))
        )

    with Image.open(input_path) as img:
        if img.mode != "RGBA":
            img = img.convert("RGBA")
        output_path.parent.mkdir(parents=True, exist_ok=True)
        largest_size = max(size[0] for size in icon_sizes)
        prepared_img = fit_image_in_square(img, largest_size)
        prepared_img.save(output_path, format="ICO", sizes=icon_sizes)


def get_ico_sizes(input_path: Path) -> list[tuple[int, int]]:
    with Image.open(input_path) as img:
        ico = getattr(img, "ico", None)
        if ico and hasattr(ico, "sizes"):
            return sorted((int(width), int(height)) for width, height in ico.sizes())

        sizes: set[tuple[int, int]] = set()
        frame_count = getattr(img, "n_frames", 1)
        for frame_index in range(frame_count):
            img.seek(frame_index)
            sizes.add((int(img.width), int(img.height)))
        return sorted(sizes)


def export_ico_size(input_path: Path, output_path: Path, icon_size: tuple[int, int], output_format: str) -> None:
    with Image.open(input_path) as img:
        ico = getattr(img, "ico", None)
        if ico and hasattr(ico, "getimage"):
            frame = ico.getimage(icon_size)
        else:
            frame = None
            frame_count = getattr(img, "n_frames", 1)
            for frame_index in range(frame_count):
                img.seek(frame_index)
                if (img.width, img.height) == icon_size:
                    frame = img.copy()
                    break
            if frame is None:
                raise ValueError(f"ICO-formaat niet gevonden: {icon_size[0]}x{icon_size[1]}")

        output_path.parent.mkdir(parents=True, exist_ok=True)
        if output_format == "JPG":
            rgba_frame = frame.convert("RGBA")
            background = Image.new("RGB", rgba_frame.size, (255, 255, 255))
            background.paste(rgba_frame, mask=rgba_frame.getchannel("A"))
            background.save(output_path, format="JPEG", quality=95)
        else:
            frame.convert("RGBA").save(output_path, format="PNG")


class IconForgeLogo(QWidget):
    def __init__(self, compact: bool = False) -> None:
        super().__init__()
        self.compact = compact
        if compact:
            self.setFixedSize(260, 118)
        else:
            self.setMinimumHeight(210)

    def paintEvent(self, event) -> None:
        del event
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        rect = QRectF(8, 8, self.width() - 16, self.height() - 16)
        background = QLinearGradient(rect.topLeft(), rect.bottomRight())
        background.setColorAt(0.0, QColor("#0A1220"))
        background.setColorAt(0.55, QColor("#05080E"))
        background.setColorAt(1.0, QColor("#0D1624"))

        card = QPainterPath()
        card.addRoundedRect(rect, 22, 22)
        painter.fillPath(card, background)
        painter.setPen(QPen(QColor("#2D3A4E"), 2))
        painter.drawPath(card)

        glow_pen = QPen(QColor(0, 180, 255, 150), 3)
        painter.setPen(glow_pen)
        painter.drawArc(QRectF(rect.left() + 130, rect.top() + 18, 250, 160), 30 * 16, 205 * 16)

        film_rect = QRectF(rect.left() + 38, rect.top() + 42, 180, 108)
        painter.setBrush(QColor("#111A2A"))
        painter.setPen(QPen(QColor("#B7C8E8"), 2))
        painter.drawRoundedRect(film_rect, 10, 10)
        painter.setBrush(QColor("#05080E"))
        for y in range(52, 136, 22):
            painter.drawRoundedRect(QRectF(film_rect.left() + 10, rect.top() + y, 18, 14), 3, 3)
            painter.drawRoundedRect(QRectF(film_rect.right() - 28, rect.top() + y, 18, 14), 3, 3)

        play = QPainterPath()
        play.moveTo(film_rect.center().x() - 20, film_rect.center().y() - 31)
        play.lineTo(film_rect.center().x() - 20, film_rect.center().y() + 31)
        play.lineTo(film_rect.center().x() + 36, film_rect.center().y())
        play.closeSubpath()
        play_gradient = QLinearGradient(play.boundingRect().topLeft(), play.boundingRect().bottomRight())
        play_gradient.setColorAt(0.0, QColor("#5DF5FF"))
        play_gradient.setColorAt(1.0, QColor("#0087FF"))
        painter.fillPath(play, play_gradient)
        painter.setPen(QPen(QColor("#7AF7FF"), 2))
        painter.drawPath(play)

        tray = QRectF(rect.left() + 300, rect.top() + 92, 210, 76)
        painter.setBrush(QColor("#0D1522"))
        painter.setPen(QPen(QColor("#7893BC"), 2))
        painter.drawRoundedRect(tray, 8, 8)
        for offset in (0, 18, 36):
            folder = QRectF(tray.left() + 16 + offset, tray.top() - 42 - offset * 0.18, 128, 56)
            painter.setBrush(QColor("#152239"))
            painter.setPen(QPen(QColor("#B7C8E8"), 2))
            painter.drawRoundedRect(folder, 8, 8)

        arrow = QPainterPath()
        arrow.moveTo(rect.left() + 170, rect.top() + 150)
        arrow.cubicTo(rect.left() + 210, rect.top() + 188, rect.left() + 260, rect.top() + 188, rect.left() + 302, rect.top() + 150)
        arrow.lineTo(rect.left() + 302, rect.top() + 168)
        arrow.lineTo(rect.left() + 345, rect.top() + 132)
        arrow.lineTo(rect.left() + 302, rect.top() + 96)
        arrow.lineTo(rect.left() + 302, rect.top() + 115)
        arrow.cubicTo(rect.left() + 250, rect.top() + 150, rect.left() + 205, rect.top() + 150, rect.left() + 170, rect.top() + 150)
        arrow.closeSubpath()
        arrow_gradient = QLinearGradient(arrow.boundingRect().topLeft(), arrow.boundingRect().bottomRight())
        arrow_gradient.setColorAt(0.0, QColor("#004CCB"))
        arrow_gradient.setColorAt(1.0, QColor("#5DF5FF"))
        painter.fillPath(arrow, arrow_gradient)
        painter.setPen(QPen(QColor("#4CEEFF"), 2))
        painter.drawPath(arrow)

        painter.setFont(QFont("Segoe UI", 22 if self.compact else 30, QFont.Weight.Bold))
        painter.setPen(QColor("#19BFFF"))
        painter.drawText(QRectF(rect.left() + 38, rect.bottom() - 58, 170, 44), Qt.AlignmentFlag.AlignLeft, "Icon")
        painter.setPen(QColor("#F2F4F8"))
        painter.drawText(QRectF(rect.left() + 146, rect.bottom() - 58, 220, 44), Qt.AlignmentFlag.AlignLeft, "Forge")


class IconForgeApp(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.selected_file: Path | None = None
        self.selected_folder: Path | None = None
        self.selected_ico_file: Path | None = None
        self.requirements_path = generate_requirements_file()
        self.size_checkboxes: dict[int, QCheckBox] = {}
        self.theme_name = THEME_CUDA_BLUE
        self.init_ui()

    def init_ui(self) -> None:
        self.setWindowTitle(APP_TITLE)
        if APP_ICON_PATH.exists():
            self.setWindowIcon(QIcon(str(APP_ICON_PATH)))
        elif APP_LOGO_PATH.exists():
            self.setWindowIcon(QIcon(str(APP_LOGO_PATH)))
        self.resize(980, 760)
        self.setAcceptDrops(True)
        self.apply_theme()

        root = QVBoxLayout(self)
        root.setContentsMargins(12, 12, 12, 12)
        root.setSpacing(10)

        tabs = QTabWidget()
        tabs.addTab(self.build_bestand_tab(), "Bestand")
        tabs.addTab(self.build_instellingen_tab(), "Instellingen")
        tabs.addTab(self.build_info_tab(), "Info")
        root.addWidget(tabs)

    def build_bestand_tab(self) -> QWidget:
        tab = QWidget()
        layout = QVBoxLayout(tab)
        layout.setSpacing(12)

        header_row = QHBoxLayout()
        header_row.setSpacing(22)
        header_row.setContentsMargins(18, 8, 18, 8)

        logo_label = QLabel()
        logo_label.setFixedSize(116, 116)
        logo_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        if APP_LOGO_PATH.exists():
            pixmap = QPixmap(str(APP_LOGO_PATH))
            logo_label.setPixmap(
                pixmap.scaled(
                    116,
                    116,
                    Qt.AspectRatioMode.KeepAspectRatio,
                    Qt.TransformationMode.SmoothTransformation,
                )
            )
        header_row.addWidget(logo_label)

        text_logo_label = QLabel()
        text_logo_label.setMinimumSize(340, 96)
        text_logo_label.setMaximumHeight(116)
        text_logo_label.setAlignment(Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignLeft)
        if APP_TEXT_LOGO_PATH.exists():
            text_pixmap = QPixmap(str(APP_TEXT_LOGO_PATH))
            text_logo_label.setPixmap(
                text_pixmap.scaled(
                    420,
                    104,
                    Qt.AspectRatioMode.KeepAspectRatio,
                    Qt.TransformationMode.SmoothTransformation,
                )
            )
        else:
            text_logo_label.setText("IconForge")
            text_logo_label.setObjectName("appTitle")
        header_row.addWidget(text_logo_label, 1)
        layout.addLayout(header_row)

        drop_hint = QLabel("Sleep een afbeelding of map naar dit venster om direct te selecteren.")
        drop_hint.setStyleSheet("color: #9AA4AD; font-style: italic;")
        layout.addWidget(drop_hint)

        single_group = QGroupBox("1. Enkel bestand")
        single_layout = QVBoxLayout(single_group)

        single_row = QHBoxLayout()
        self.input_path_edit = QLineEdit()
        self.input_path_edit.setReadOnly(True)
        self.input_path_edit.setPlaceholderText("Nog geen bestand geselecteerd")
        single_row.addWidget(self.input_path_edit, 1)

        browse_file_btn = QPushButton("Bestand kiezen...")
        browse_file_btn.clicked.connect(self.browse_file)
        single_row.addWidget(browse_file_btn)
        single_layout.addLayout(single_row)

        self.file_info_label = QLabel("Ondersteund: PNG, JPG, JPEG, WEBP, BMP, TIFF")
        single_layout.addWidget(self.file_info_label)

        self.output_path_edit = QLineEdit()
        self.output_path_edit.setReadOnly(True)
        self.output_path_edit.setPlaceholderText("Output wordt automatisch bepaald")
        single_layout.addWidget(self.output_path_edit)

        single_buttons = QHBoxLayout()
        open_file_folder_btn = QPushButton("Open outputmap bestand")
        open_file_folder_btn.clicked.connect(self.open_output_folder_for_file)
        single_buttons.addWidget(open_file_folder_btn)

        convert_btn = QPushButton("Converteer bestand naar .ico")
        convert_btn.setObjectName("primaryButton")
        convert_btn.clicked.connect(self.convert_selected_file)
        single_buttons.addWidget(convert_btn)
        single_layout.addLayout(single_buttons)
        layout.addWidget(single_group)

        ico_export_group = QGroupBox("2. ICO export naar PNG/JPG")
        ico_export_layout = QVBoxLayout(ico_export_group)

        ico_row = QHBoxLayout()
        self.ico_input_path_edit = QLineEdit()
        self.ico_input_path_edit.setReadOnly(True)
        self.ico_input_path_edit.setPlaceholderText("Nog geen .ico bestand geselecteerd")
        ico_row.addWidget(self.ico_input_path_edit, 1)

        browse_ico_btn = QPushButton(".ico kiezen...")
        browse_ico_btn.clicked.connect(self.browse_ico_file)
        ico_row.addWidget(browse_ico_btn)
        ico_export_layout.addLayout(ico_row)

        ico_options_row = QHBoxLayout()
        ico_options_row.addWidget(QLabel("Grootte:"))
        self.ico_size_combo = QComboBox()
        self.ico_size_combo.setMinimumWidth(120)
        ico_options_row.addWidget(self.ico_size_combo)

        ico_options_row.addWidget(QLabel("Opslaan als:"))
        self.ico_format_combo = QComboBox()
        self.ico_format_combo.addItems(["PNG", "JPG"])
        self.ico_format_combo.setMinimumWidth(90)
        ico_options_row.addWidget(self.ico_format_combo)
        ico_options_row.addStretch(1)
        ico_export_layout.addLayout(ico_options_row)

        self.ico_export_info_label = QLabel("Kies een .ico bestand om beschikbare maten te laden.")
        ico_export_layout.addWidget(self.ico_export_info_label)

        export_ico_btn = QPushButton("Exporteer gekozen .ico-formaat")
        export_ico_btn.setObjectName("primaryButton")
        export_ico_btn.clicked.connect(self.export_selected_ico_size)
        ico_export_layout.addWidget(export_ico_btn)

        layout.addWidget(ico_export_group)

        batch_group = QGroupBox("3. Batch map")
        batch_layout = QVBoxLayout(batch_group)

        batch_row = QHBoxLayout()
        self.folder_path_edit = QLineEdit()
        self.folder_path_edit.setReadOnly(True)
        self.folder_path_edit.setPlaceholderText("Nog geen map geselecteerd")
        batch_row.addWidget(self.folder_path_edit, 1)

        browse_folder_btn = QPushButton("Map kiezen...")
        browse_folder_btn.clicked.connect(self.browse_folder)
        batch_row.addWidget(browse_folder_btn)
        batch_layout.addLayout(batch_row)

        options_row = QHBoxLayout()
        self.recursive_checkbox = QCheckBox("Submappen meenemen")
        self.recursive_checkbox.setChecked(False)
        options_row.addWidget(self.recursive_checkbox)

        self.skip_existing_checkbox = QCheckBox("Bestaande .ico overslaan")
        self.skip_existing_checkbox.setChecked(False)
        options_row.addWidget(self.skip_existing_checkbox)
        options_row.addStretch(1)
        batch_layout.addLayout(options_row)

        self.batch_info_label = QLabel("Nog geen map gekozen.")
        batch_layout.addWidget(self.batch_info_label)

        batch_buttons = QHBoxLayout()
        open_batch_folder_btn = QPushButton("Open gekozen map")
        open_batch_folder_btn.clicked.connect(self.open_selected_folder)
        batch_buttons.addWidget(open_batch_folder_btn)

        batch_convert_btn = QPushButton("Converteer hele map")
        batch_convert_btn.setObjectName("primaryButton")
        batch_convert_btn.clicked.connect(self.convert_selected_folder)
        batch_buttons.addWidget(batch_convert_btn)
        batch_layout.addLayout(batch_buttons)

        self.batch_progress = QProgressBar()
        self.batch_progress.setMinimum(0)
        self.batch_progress.setMaximum(100)
        self.batch_progress.setValue(0)
        batch_layout.addWidget(self.batch_progress)

        self.batch_summary_label = QLabel("Batch nog niet gestart.")
        batch_layout.addWidget(self.batch_summary_label)

        self.batch_log = QTextEdit()
        self.batch_log.setReadOnly(True)
        self.batch_log.setPlaceholderText("Batchlog verschijnt hier...")
        batch_layout.addWidget(self.batch_log)

        layout.addWidget(batch_group)

        self.status_label = QLabel("Klaar voor conversie.")
        layout.addWidget(self.status_label)
        return tab

    def build_instellingen_tab(self) -> QWidget:
        tab = QWidget()
        layout = QVBoxLayout(tab)
        layout.setSpacing(12)

        theme_group = QGroupBox("Thema")
        theme_layout = QVBoxLayout(theme_group)
        theme_layout.addWidget(QLabel("Standaard: CUDA Blue. Alternatief: Forge Dark."))
        self.theme_combo = QComboBox()
        self.theme_combo.addItems([THEME_CUDA_BLUE, THEME_FORGE_DARK])
        self.theme_combo.setCurrentText(self.theme_name)
        self.theme_combo.currentTextChanged.connect(self.set_theme)
        theme_layout.addWidget(self.theme_combo)
        layout.addWidget(theme_group)

        sizes_group = QGroupBox("ICO-formaten")
        sizes_layout = QVBoxLayout(sizes_group)
        sizes_layout.addWidget(QLabel("Selecteer welke icon sizes in het .ico-bestand worden opgeslagen."))

        row1 = QHBoxLayout()
        row2 = QHBoxLayout()
        for idx, size in enumerate(DEFAULT_ICON_SIZES):
            checkbox = QCheckBox(f"{size}x{size}")
            checkbox.setChecked(True)
            self.size_checkboxes[size] = checkbox
            if idx < 3:
                row1.addWidget(checkbox)
            else:
                row2.addWidget(checkbox)
        sizes_layout.addLayout(row1)
        sizes_layout.addLayout(row2)
        layout.addWidget(sizes_group)

        logic_group = QGroupBox("Conversielogica")
        logic_layout = QVBoxLayout(logic_group)
        logic_layout.addWidget(QLabel("Passing: afbeelding blijft volledig zichtbaar binnen een vierkant canvas."))
        logic_layout.addWidget(QLabel("Alpha: transparantie blijft behouden waar mogelijk."))
        logic_layout.addWidget(QLabel("Opvulling: lege ruimte wordt transparant ingevuld indien nodig."))
        logic_layout.addWidget(QLabel("Output: zelfde bestandsnaam als bron, met .ico extensie."))
        logic_layout.addWidget(QLabel("Batch: converteert alle ondersteunde bestanden in de gekozen map."))
        layout.addWidget(logic_group)

        layout.addStretch(1)
        return tab

    def apply_theme(self) -> None:
        self.setStyleSheet(CUDA_THEME_QSS if self.theme_name == THEME_CUDA_BLUE else ICONFORGE_THEME_QSS)

    def set_theme(self, theme_name: str) -> None:
        self.theme_name = theme_name
        self.apply_theme()

    def build_info_tab(self) -> QWidget:
        tab = QWidget()
        layout = QVBoxLayout(tab)

        info = QTextEdit()
        info.setReadOnly(True)
        info.setPlainText(
            f"Applicatie : {APP_NAME}\n"
            f"Versie     : {APP_VERSION}\n"
            f"APP_NAME_APP_VERSION: {APP_NAME_APP_VERSION}\n"
            f"Actieve venv: {active_venv}\n"
            f"Bestand    : {APP_PATH.name}\n"
            f"Volledig pad: {APP_PATH}\n"
            f"Requirements: {self.requirements_path}\n\n"
            "Specificaties:\n"
            "- Professionele image-to-ICO converter voor losse bestanden en batchmappen.\n"
            "- Ondersteunt PNG, JPG, JPEG, WEBP, BMP en TIFF.\n"
            "- Bewaart meerdere ICO-formaten in één .ico-bestand.\n"
            "- Kan bestaande .ico bestanden per formaat exporteren naar PNG of JPG.\n"
            "- Houdt transparantie intact en past beelden in zonder afsnijden.\n"
            "- Batchopties: submappen meenemen en bestaande .ico overslaan.\n"
        )
        layout.addWidget(info)
        return tab

    def browse_file(self) -> None:
        start_dir = str(Path.home() / "Downloads")
        filters = "Afbeeldingen (*.png *.jpg *.jpeg *.webp *.bmp *.tiff)"
        file_path, _ = QFileDialog.getOpenFileName(self, "Kies afbeelding", start_dir, filters)
        if not file_path:
            return

        self.apply_selected_file(Path(file_path))

    def browse_ico_file(self) -> None:
        start_dir = str(Path.home() / "Downloads")
        filters = "ICO bestanden (*.ico)"
        file_path, _ = QFileDialog.getOpenFileName(self, "Kies .ico bestand", start_dir, filters)
        if not file_path:
            return

        self.apply_selected_ico_file(Path(file_path))

    def browse_folder(self) -> None:
        start_dir = str(Path.home() / "Downloads")
        folder_path = QFileDialog.getExistingDirectory(self, "Kies map", start_dir)
        if not folder_path:
            return

        self.apply_selected_folder(Path(folder_path))

    def apply_selected_file(self, path: Path) -> None:
        self.selected_file = path
        self.input_path_edit.setText(str(self.selected_file))
        self.output_path_edit.setText(str(self.selected_file.with_suffix(".ico")))
        self.file_info_label.setText(
            f"Geselecteerd: {self.selected_file.name} | Extensie: {self.selected_file.suffix.lower()}"
        )
        self.set_status("Bestand geselecteerd. Klaar voor conversie.", ok=True)

    def apply_selected_ico_file(self, path: Path) -> None:
        if not is_supported_ico(path):
            self.set_status("Selecteer een geldig .ico bestand.", ok=False)
            return

        self.selected_ico_file = path
        self.ico_input_path_edit.setText(str(path))
        self.ico_size_combo.clear()

        try:
            sizes = get_ico_sizes(path)
        except Exception as exc:
            self.ico_export_info_label.setText(f"Kon .ico maten niet lezen: {exc}")
            self.set_status(f"ICO-leesfout: {exc}", ok=False)
            return

        for width, height in sizes:
            self.ico_size_combo.addItem(f"{width}x{height}", (width, height))

        self.ico_export_info_label.setText(
            f"Gevonden formaten: {', '.join(f'{width}x{height}' for width, height in sizes)}"
        )
        self.set_status(".ico bestand geselecteerd. Kies grootte en exportformaat.", ok=True)

    def apply_selected_folder(self, path: Path) -> None:
        self.selected_folder = path
        self.folder_path_edit.setText(str(self.selected_folder))
        count = len(iter_supported_images(self.selected_folder, self.recursive_checkbox.isChecked()))
        self.batch_info_label.setText(f"Gevonden ondersteunde bronbestanden: {count}")
        self.batch_summary_label.setText("Batch klaar om te starten.")
        self.batch_log.clear()
        self.batch_progress.setValue(0)
        self.set_status("Map geselecteerd. Batch klaar.", ok=True)

    def dragEnterEvent(self, event) -> None:
        mime_data = event.mimeData()
        if not mime_data.hasUrls():
            event.ignore()
            return

        for url in mime_data.urls():
            local_path = url.toLocalFile()
            if not local_path:
                continue
            path = Path(local_path)
            if path.is_dir() or is_supported_image(path) or is_supported_ico(path):
                event.acceptProposedAction()
                return

        event.ignore()

    def dropEvent(self, event) -> None:
        for url in event.mimeData().urls():
            local_path = url.toLocalFile()
            if not local_path:
                continue

            path = Path(local_path)
            if path.is_dir():
                self.apply_selected_folder(path)
                event.acceptProposedAction()
                return

            if is_supported_image(path):
                self.apply_selected_file(path)
                event.acceptProposedAction()
                return

            if is_supported_ico(path):
                self.apply_selected_ico_file(path)
                event.acceptProposedAction()
                return

        self.set_status("Sleep een ondersteund afbeeldingsbestand, .ico bestand of map naar het venster.", ok=False)
        event.ignore()

    def get_selected_icon_sizes(self) -> list[tuple[int, int]]:
        selected = [size for size, checkbox in self.size_checkboxes.items() if checkbox.isChecked()]
        if not selected:
            raise ValueError("Selecteer minimaal één ICO-grootte in Instellingen.")
        return normalize_sizes(selected)

    def convert_selected_file(self) -> None:
        if self.selected_file is None:
            self.set_status("Selecteer eerst een bronbestand.", ok=False)
            return

        try:
            output_path = self.selected_file.with_suffix(".ico")
            icon_sizes = self.get_selected_icon_sizes()
            convert_image_to_ico(self.selected_file, output_path, icon_sizes)
            self.output_path_edit.setText(str(output_path))
            self.set_status(f"Succes. ICO opgeslagen als: {output_path.name}", ok=True)
        except Exception as exc:
            self.set_status(f"Fout: {exc}", ok=False)
            QMessageBox.critical(self, "Conversiefout", str(exc))

    def export_selected_ico_size(self) -> None:
        if self.selected_ico_file is None:
            self.set_status("Selecteer eerst een .ico bestand.", ok=False)
            return

        if self.ico_size_combo.currentIndex() < 0:
            self.set_status("Geen .ico formaat gekozen.", ok=False)
            return

        icon_size = self.ico_size_combo.currentData()
        output_format = self.ico_format_combo.currentText()
        suffix = ".jpg" if output_format == "JPG" else ".png"
        output_path = self.selected_ico_file.with_name(
            f"{self.selected_ico_file.stem}_{icon_size[0]}x{icon_size[1]}{suffix}"
        )

        try:
            export_ico_size(self.selected_ico_file, output_path, icon_size, output_format)
            self.ico_export_info_label.setText(f"Opgeslagen als: {output_path.name}")
            self.set_status(f"Succes. ICO-formaat opgeslagen als: {output_path.name}", ok=True)
        except Exception as exc:
            self.set_status(f"ICO-exportfout: {exc}", ok=False)
            QMessageBox.critical(self, "ICO-exportfout", str(exc))

    def convert_selected_folder(self) -> None:
        if self.selected_folder is None:
            self.set_status("Selecteer eerst een map voor batchconversie.", ok=False)
            return

        try:
            icon_sizes = self.get_selected_icon_sizes()
            recursive = self.recursive_checkbox.isChecked()
            skip_existing = self.skip_existing_checkbox.isChecked()
            files = iter_supported_images(self.selected_folder, recursive)

            if not files:
                self.batch_progress.setValue(0)
                self.batch_summary_label.setText("Geen ondersteunde bronbestanden gevonden.")
                self.set_status("Geen ondersteunde bronbestanden gevonden.", ok=False)
                return

            self.batch_log.clear()
            self.batch_progress.setValue(0)
            self.batch_progress.setMaximum(len(files))

            success_count = 0
            skipped_count = 0
            error_count = 0

            for index, src in enumerate(files, start=1):
                dst = src.with_suffix(".ico")
                try:
                    if skip_existing and dst.exists():
                        skipped_count += 1
                        self.batch_log.append(f"SKIP | {src.name} -> bestaat al")
                    else:
                        convert_image_to_ico(src, dst, icon_sizes)
                        success_count += 1
                        self.batch_log.append(f"OK   | {src.name} -> {dst.name}")
                except Exception as exc:
                    error_count += 1
                    self.batch_log.append(f"ERR  | {src.name} -> {exc}")

                self.batch_progress.setValue(index)
                self.batch_summary_label.setText(
                    f"Verwerkt: {index}/{len(files)} | OK: {success_count} | SKIP: {skipped_count} | FOUT: {error_count}"
                )
                QApplication.processEvents()

            ok = error_count == 0
            self.set_status(
                f"Batch gereed. OK: {success_count} | SKIP: {skipped_count} | FOUT: {error_count}",
                ok=ok,
            )
        except Exception as exc:
            self.set_status(f"Batchfout: {exc}", ok=False)
            QMessageBox.critical(self, "Batchfout", str(exc))

    def open_output_folder_for_file(self) -> None:
        if self.selected_file is None:
            self.set_status("Geen bronbestand geselecteerd.", ok=False)
            return
        self.open_folder(self.selected_file.parent)

    def open_selected_folder(self) -> None:
        if self.selected_folder is None:
            self.set_status("Geen map geselecteerd.", ok=False)
            return
        self.open_folder(self.selected_folder)

    def open_folder(self, folder: Path) -> None:
        if os.name == "nt":
            os.startfile(str(folder))
        else:
            QMessageBox.information(self, "Pad", str(folder))

    def set_status(self, message: str, ok: bool) -> None:
        self.status_label.setText(message)
        self.status_label.setObjectName("statusOk" if ok else "statusError")
        self.status_label.style().unpolish(self.status_label)
        self.status_label.style().polish(self.status_label)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = IconForgeApp()
    window.show()
    sys.exit(app.exec())
