import docx
doc = docx.Document("統計數據-專任(案)教師數_修正.docx")
for i, para in enumerate(doc.paragraphs):
    if para.text.strip():
        print(f"{i}: {para.text}")