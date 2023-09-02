# coding=utf-8
from loguru import logger
import sys
import os
from pathlib import Path
import re
import argparse
import re
from functools import partial
import torch
from torch.utils.data import ConcatDataset
from tqdm import tqdm
from nougat import NougatModel
from nougat.utils.dataset import LazyDataset
from nougat.utils.checkpoint import get_checkpoint
import fitz


class PdfModel:
    def __init__(self,
                 model_path,
                 batchsize=12,
                 output_path="./output"):

        self.model_path = model_path
        self.batchsize = batchsize
        self.output_path = output_path

        self.model = self._load()

    def _load(self):
        logger.info(f"Start load model = [{self.model_path}]")
        model = NougatModel.from_pretrained(self.model_path).to(torch.bfloat16)
        if torch.cuda.is_available():
            model.to("cuda")
        model.eval()
        return model

    def parse(self, pdf_path) -> list:
        datasets = []
        try:
            dataset = LazyDataset(
                pdf_path, partial(self.model.encoder.prepare_input,
                                  random_padding=False)
            )
            datasets.append(dataset)
        except fitz.fitz.FileDataError:
            logger.error(f"Failed load {pdf_path}")
            sys.exit()

        dataloader = torch.utils.data.DataLoader(
            ConcatDataset(datasets),
            batch_size=self.batchsize,
            shuffle=False,
            collate_fn=LazyDataset.ignore_none_collate,
        )

        title_content_list = []
        predictions = []
        file_index = 0
        page_num = 0
        for i, (sample, is_last_page) in enumerate(tqdm(dataloader)):
            model_output = self.model.inference(image_tensors=sample)
            # check if model output is faulty
            for j, output in enumerate(model_output["predictions"]):
                if page_num == 0:
                    logger.info(
                        "Processing file %s with %i pages"
                        % (datasets[file_index].name, datasets[file_index].size)
                    )
                page_num += 1
                if output.strip() == "[MISSING_PAGE_POST]":
                    # uncaught repetitions -- most likely empty page
                    predictions.append(
                        f"\n\n[MISSING_PAGE_EMPTY:{page_num}]\n\n")
                    continue
                if model_output["repeats"][j] is not None:
                    if model_output["repeats"][j] > 0:
                        # If we end up here, it means the output is most likely not complete and was truncated.
                        logger.warning(
                            f"Skipping page {page_num} due to repetitions.")
                        predictions.append(
                            f"\n\n[MISSING_PAGE_FAIL:{page_num}]\n\n")
                    else:
                        # If we end up here, it means the document page is too different from the training domain.
                        # This can happen e.g. for cover pages.
                        predictions.append(
                            f"\n\n[MISSING_PAGE_EMPTY:{i*self.batchsize+j+1}]\n\n"
                        )
                else:
                    predictions.append(output)

                if is_last_page[j]:
                    out = "".join(predictions).strip()
                    out = re.sub(r"\n{3,}", "\n\n", out).strip()
                    if self.output_path:
                        out_path = Path(os.path.join(
                            self.output_path, "content.mmd"))
                        out_path.parent.mkdir(parents=True, exist_ok=True)
                        out_path.write_text(out, encoding="utf-8")
                    else:
                        print(out, "\n\n")

                    title = ""
                    content = []
                    for line_idx, line in enumerate(out.split("\n")):
                        line = line.strip()
                        if line == "":
                            line = "\n"

                        if line_idx == 0 and line.startswith("#"):
                            title = line
                            continue

                        # is title
                        if line.startswith("##"):

                            if title != "":
                                title_content_list.append(
                                    (title, "".join(content)))

                                title = line
                                content = []
                            else:
                                title = line
                            continue

                        content.append(line)
                    # title_content_list.append((title, "".join(content)))

                    predictions = []
                    page_num = 0
                    file_index += 1
                    break

        torch.cuda.empty_cache()
        return title_content_list
