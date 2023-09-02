# coding=utf-8
import sys
import argparse
import yaml
from pathlib import Path
from loguru import logger

from paperassistant.models import PdfModel, Translator, LLM

parser = argparse.ArgumentParser(
    formatter_class=lambda prog: argparse.HelpFormatter(prog, max_help_position=54))
parser.add_argument('--config', type=str, help="Add config file path")
parser.add_argument('--file', type=str, help="pdf file")

args = parser.parse_args()
if not args.config:
    logger.error("Missing config file")
    sys.exit()

with Path(args.config) as p:
    if p.exists():
        user_config = yaml.safe_load(open(p, "r").read())
    else:
        logger.error(f"Not find file [{p}]")
        sys.exit()

logger.info(f"Start load model = [{user_config['pdf_model']}]")
pdf_model = PdfModel(user_config["pdf_model"])

logger.info(f"Start load model = [{user_config['translate_model']}]")
translator_model = Translator(user_config["translate_model"])

logger.info(f"Start load model = [{user_config['llm_model']}]")
llm_model = LLM(user_config["llm_model"])