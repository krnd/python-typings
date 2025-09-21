from .pytesseract import ALTONotSupported as ALTONotSupported
from .pytesseract import Output as Output
from .pytesseract import TesseractError as TesseractError
from .pytesseract import TesseractNotFoundError as TesseractNotFoundError
from .pytesseract import TSVNotSupported as TSVNotSupported
from .pytesseract import get_languages as get_languages
from .pytesseract import get_tesseract_version as get_tesseract_version
from .pytesseract import image_to_alto_xml as image_to_alto_xml
from .pytesseract import image_to_boxes as image_to_boxes
from .pytesseract import image_to_data as image_to_data
from .pytesseract import image_to_osd as image_to_osd
from .pytesseract import image_to_pdf_or_hocr as image_to_pdf_or_hocr
from .pytesseract import image_to_string as image_to_string
from .pytesseract import (
    run_and_get_multiple_output as run_and_get_multiple_output,
)
from .pytesseract import run_and_get_output as run_and_get_output

__version__: str
