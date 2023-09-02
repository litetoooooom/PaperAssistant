# coding=utf-8
from loguru import logger

import paperassistant.shared as shared

_title_content = shared.pdf_model.parse(shared.args.file)

fw = open("save.txt", "w")
for title, content in _title_content:
    fw.write(f"{title}\n")

    logger.info(f"{title}")
    if len(content) >= 1024:
        for text in content.split("\n"):
            text = text.strip()
            if text == "":
                fw.write("\n")
                continue
            
            fw.write(f"{text}\n")
            try:
                trans_text = shared.translator_model.T2TT(text)
                fw.write(f"\ntranslate: {trans_text}\n")
            except:
                logger.warning("Failed to translate.")

            summary_text = shared.llm_model.summary(text)
            fw.write(f"\nsummary: {summary_text}\n")
    else:
        fw.write(f"{content}\n")
        trans_text = shared.translator_model.T2TT(content)
        fw.write(f"\ntranslate: {trans_text}\n")

        summary_text = shared.llm_model.summary(content)
        fw.write(f"\nsummary: {summary_text}\n")

    fw.flush()
