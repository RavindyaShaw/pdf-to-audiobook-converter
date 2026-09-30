# 🎧 PDF to Audiobook Converter

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?logo=python&logoColor=white)
![gTTS](https://img.shields.io/badge/TTS-gTTS-34A853?logo=google&logoColor=white)
![pypdf](https://img.shields.io/badge/PDF-pypdf-orange)
![Output](https://img.shields.io/badge/Output-MP3-blueviolet)

Turn any text-based PDF into a series of MP3 audio files with a single Python script. Listen to books, study notes, and documents on the go.

---

##  Table of Contents

- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
- [Usage](#-usage)
- [How It Works](#-how-it-works)
- [Configuration](#-configuration)
- [Limitations](#-limitations)
- [Troubleshooting](#-troubleshooting)
- [Roadmap](#-roadmap)
- [Contributing](#-contributing)
- [Author](#-author)

---

##  Features

-  Extracts text from every page of a PDF with **pypdf**
-  Converts text to speech with **Google Text-to-Speech (gTTS)**
-  Splits long documents into chunks of 4,500 characters per audio file
-  Waits 3 seconds between requests to avoid rate limiting
-  Clear error messages for a missing file, an unreadable PDF, or network problems
-  Progress messages in the terminal for every step

---

##  Tech Stack

| Purpose | Library |
|---------|---------|
| Language | Python 3.8+ |
| PDF text extraction | [pypdf](https://github.com/py-pdf/pypdf) |
| Text-to-speech | [gTTS](https://github.com/pndurette/gTTS) |

---

##  Project Structure

```
pdf-to-audiobook-converter/
├── audiobook.py      # Main script
├── book.pdf          # Your input PDF (you provide this)
├── part_1.mp3        # Generated audio
├── part_2.mp3
└── ...
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- An internet connection (gTTS uses Google's online speech service)

### Installation

```bash
# Clone the repository
git clone https://github.com/RavindyaShaw/pdf-to-audiobook-converter.git
cd pdf-to-audiobook-converter

# Install dependencies
pip install pypdf gTTS
```

---

##  Usage

1. Put your PDF in the project folder and name it **`book.pdf`** (or change `pdf_name` in `audiobook.py`).
2. Run the script:

   ```bash
   python audiobook.py
   ```

3. Sample output:

   ```
   Reading PDF pages... Please wait.
   Creating 3 audio file(s)...
   Saved: part_1.mp3
   Waiting 3 seconds before next file...
   Saved: part_2.mp3
   Waiting 3 seconds before next file...
   Saved: part_3.mp3
   Waiting 3 seconds before next file...

   Audiobook conversion completed successfully!
   ```

4. Your audio files (`part_1.mp3`, `part_2.mp3`, ...) appear in the same folder. Play them in order.

---

##  How It Works

```
book.pdf ──► pypdf extracts text ──► split into 4,500-char chunks ──► gTTS ──► part_N.mp3
```

| Step | What happens |
|------|--------------|
| 1 | The script checks that `book.pdf` exists |
| 2 | `pypdf` reads each page and collects the text |
| 3 | The text is split into chunks of up to 4,500 characters |
| 4 | Each chunk is sent to `gTTS` and saved as an MP3 |
| 5 | The script pauses for 3 seconds between files |

---

## 🔧 Configuration

Edit these values in `audiobook.py`:

| Setting | Default | Description |
|---------|---------|-------------|
| `pdf_name` | `"book.pdf"` | Path to the input PDF |
| `max_chars` | `4500` | Maximum characters per audio file |
| `lang` | `"en"` | Speech language code, e.g. `"es"`, `"fr"`, `"de"` |
| `slow` | `False` | Set to `True` for slower speech |
| `time.sleep(3)` | `3` | Seconds to wait between requests |

---

##  Limitations

- **Scanned PDFs are not supported.** Image-only PDFs have no text to extract, so run them through OCR first.
- **Internet is required**, because gTTS calls an online service.
- **Chunks are cut by character count**, so a split can land mid-sentence.
- **Output is many MP3 files**, not one merged audiobook.
- Complex layouts (columns, tables, headers and footers) may come out in a odd order.

---

##  Troubleshooting

| Problem | Solution |
|---------|----------|
| `'book.pdf' was not found` | Place the file next to the script and check the name |
| `No readable text found in the PDF` | The PDF is likely scanned images. Use OCR first |
| `ModuleNotFoundError` | Run `pip install pypdf gTTS` |
| `gTTSError` or connection errors | Check your internet, or increase the `time.sleep` delay |

---

##  Roadmap

- [ ] Accept the PDF path as a command-line argument
- [ ] Split on sentence boundaries instead of raw character count
- [ ] Merge all parts into a single MP3 (e.g. with `pydub`)
- [ ] Add a progress bar with `tqdm`
- [ ] Add OCR support for scanned PDFs
- [ ] Choose a page range to convert
- [ ] Simple GUI for drag-and-drop use

---

##  Contributing

1. Fork the repository
2. Create a branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m "feat: add your feature"`
4. Push the branch: `git push origin feature/your-feature`
5. Open a Pull Request

---

##  Author

**Ravindya Shaw**
GitHub: [@RavindyaShaw](https://github.com/RavindyaShaw)

---

⭐ If this project helped you, consider giving it a star!

