from pypdf import PdfReader
from gtts import gTTS
import os
import time

# PDF to Audiobook Converter

try:
    pdf_name = "book.pdf"

    # Check if the file exists
    if not os.path.exists(pdf_name):
        raise FileNotFoundError

    pdf_reader = PdfReader(pdf_name)
    extracted_text = ""

    print("Reading PDF pages... Please wait.")

    for page in pdf_reader.pages:
        page_text = page.extract_text()
        if page_text:
            extracted_text += page_text + "\n"

    if not extracted_text.strip():
        print("Error: No readable text found in the PDF.")
        exit()

    max_chars = 4500
    total_parts = (len(extracted_text) + max_chars - 1) // max_chars

    print(f"Creating {total_parts} audio file(s)...")

    for part_number, start in enumerate(range(0, len(extracted_text), max_chars), start=1):
        text_chunk = extracted_text[start:start + max_chars]

        tts = gTTS(
            text=text_chunk,
            lang="en",
            slow=False
        )

        output_file = f"part_{part_number}.mp3"
        tts.save(output_file)

        print(f"Saved: {output_file}")
        print("Waiting 3 seconds before next file...")
        time.sleep(3)

    print("\nAudiobook conversion completed successfully!")

except FileNotFoundError:
    print("Error: 'book.pdf' was not found in the current folder.")

except Exception as e:
    print("Error:", e)
