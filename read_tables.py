import docx
doc = docx.Document("統計數據-專任(案)教師數_修正.docx")
for i, table in enumerate(doc.tables):
    print(f"Table {i}:")
    for row in table.rows:
        for cell in row.cells:
            print(cell.text.strip(), end=' | ')
        print()
    print()