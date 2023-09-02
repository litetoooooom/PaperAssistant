# 论文阅读助手

## 当前具备的功能

能够对论文进行翻译和总结

## 流程逻辑

1. 使用 [nougat](https://github.com/facebookresearch/nougat) 对 PDF 文件进行解析

2. 使用 [seamless-m4t-large](https://huggingface.co/facebook/seamless-m4t-large) 对段落进行翻译

3. 使用 [Baichuan-13B](https://huggingface.co/baichuan-inc/Baichuan-13B-Chat) 对段落进行总结

## 安装

1. 参考 [nougat](https://github.com/facebookresearch/nougat)的安装流程。论文解读可参考[Meta新作：Nougat - 论文阅读报告生成](https://mp.weixin.qq.com/s/A986J7OgjixhbRULI4WnjA)

2. 参考 [seamless_communication](https://github.com/facebookresearch/seamless_communication/tree/main#installation)的安装流程

3. 下载 [Baichuan-13B](https://huggingface.co/baichuan-inc/Baichuan-13B-Chat) 模型

4. `pip install -i requirements.txt`

## 一键启动

1. `python main.py --config config/test.yml --file test.pdf`

## 效果预览

```text
To validate the capacity of the LLM-based AI agents to strategically plan for the tool order, we designed the prompt as shown in Figure 7 of Appendix B. This design is motivated by the goal to assess the ability of LLM-based AI agents to understand complex problems, subsequently decomposing them into a sequence of simpler tasks executed by appropriately selected tools. Specifically, we require the LLM-based AI agent to follow our instructions, select tools from our pre-defined tool set with detailed function descriptions, conform to the given format strictly, and understand the demonstrations to learn from them.

translate: 为了验证基于 LLM 的 AI 代理对工具顺序进行战略规划的能力,我们设计了按附录 B 的图 7 所示的提示.这个设计的动机是评估基于 LLM 的 AI 代理理解复杂问题的能力,然后将其分解成由适当选择的工具执行的简单任务序列.具体来说,我们要求基于 LLM 的 AI 代理遵循我们的指示,从我们的预定义的工具集中选择具有详细功能描述的工具,严格遵守给定的格式,并理解从它们中学习的演示.

summary: 我们设计了一个提示，如附录B中的图7所示，以评估基于LLM的AI代理在策略性规划工具顺序方面的能力。这个设计旨在评估LLM-based AI代理理解复杂问题的能力，然后将它们分解成一系列由适当选择的工具执行的简单任务。具体来说，我们要求基于LLM的AI代理遵循我们的指示，从预定义的工具集中选择工具，严格遵守给定的格式，并理解演示以便从中学习。
```

```text
###### Abstract

With recent advancements in natural language processing, Large Language Models (LLMs) have emerged as powerful tools for various real-world applications. Despite their prowess, the intrinsic generative abilities of LLMs may prove insufficient for handling complex tasks which necessitate a combination of task planning and the usage of external tools. In this paper, we first propose a structured framework tailored for LLM-based AI Agents and discuss the crucial capabilities necessary for tackling intricate problems. Within this framework, we design two distinct types of agents (i.e., one-step agent and sequential agent) to execute the inference process. Subsequently, we instantiate the framework using various LLMs and evaluate their Task Planning and Tool Usage (TPTU) abilities on typical tasks. By highlighting key findings and challenges, our goal is to provide a helpful resource for researchers and practitioners to leverage the power of LLMs in their AI applications. Our study emphasizes the substantial potential of these models, while also identifying areas that need more investigation and improvement.

translate: 随着自然语言处理的近期进步,大型语言模型 (LLM) 已经成为各种现实应用的强大工具.尽管它们具有实力,但LLM的内在生成能力可能不足以处理复杂的任务,需要任务规划和使用外部工具的组合.在本文中,我们首先提出了针对基于LLM的人工智能代理的结构化框架,并讨论解决复杂问题的关键能力.在这个框架内,我们设计了两种不同的代理类型 (即一步代理和顺序代理)来执行推理过程.随后,我们使用各种LLM将框架实例化,并评估它们在典型任务上的任务规划和利用工具 (TUTP) 能力.

summary: 随着自然语言处理技术的最新进展，大型语言模型(LLM)已经成为各种现实世界应用的强大工具。尽管它们具有很强的能力，但LLM固有的生成能力可能不足以应对需要结合任务规划和外部工具的复杂任务。在这篇论文中，我们首先提出了一种针对基于LLM的AI代理的结构化框架，并讨论了解决复杂问题所需的关键能力。在这个框架中，我们设计了两种类型的代理(即一步代理和序列代理)来执行推理过程。然后，我们使用不同的LLM来实现这个框架，并在典型任务上评估它们的任务规划和工具使用(TPTU)能力。通过强调关键发现和挑战，我们的目标是为研究人员和实践者提供一个有用的资源，以便在他们的AI应用中利用LLM的力量。我们的研究强调了这些模型的巨大潜力，同时也指出了需要更多调查和改进的领域。
```