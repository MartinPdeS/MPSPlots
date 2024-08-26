# Repository Coverage

[Full report](https://htmlpreview.github.io/?https://github.com/MartinPdeS/MPSPlots/blob/python-coverage-comment-action-data/htmlcov/index.html)

| Name                              |    Stmts |     Miss |   Branch |   BrPart |   Cover |   Missing |
|---------------------------------- | -------: | -------: | -------: | -------: | ------: | --------: |
| MPSPlots/\_\_init\_\_.py          |        5 |        2 |        0 |        0 |     60% |       7-8 |
| MPSPlots/\_version.py             |       11 |        2 |        2 |        1 |     77% |       5-6 |
| MPSPlots/colormaps.py             |       12 |        0 |        2 |        0 |    100% |           |
| MPSPlots/fonts/\_\_init\_\_.py    |        0 |        0 |        0 |        0 |    100% |           |
| MPSPlots/render2D/\_\_init\_\_.py |        9 |        4 |        2 |        0 |     45% |     11-16 |
| MPSPlots/render2D/artist.py       |      392 |       55 |       88 |       17 |     83% |103, 130, 145->exit, 198->208, 236, 239, 305-309, 324-332, 344-370, 416->419, 430->449, 549, 565, 569, 596, 639->642, 642->exit, 655-664, 708, 764-778, 820, 942-955, 1037, 1087, 1098-1114, 1150, 1161-1179 |
| MPSPlots/render2D/axis.py         |      240 |       51 |       70 |       19 |     69% |84, 87-88, 92->91, 99->98, 106, 131-136, 145-150, 159-164, 173-178, 187-189, 198, 210-212, 222-226, 241-243, 308->exit, 453->452, 466->465, 479->478, 504->503, 517->516, 530->529, 543->542, 556->555, 566, 569->568, 582->581, 592, 595->594, 608->607, 618, 621->620, 631, 648->647, 671-674 |
| MPSPlots/render2D/scene.py        |      159 |       32 |       68 |       16 |     70% |41, 48, 60-62, 65-66, 69->68, 73->72, 78->77, 83->82, 93->92, 103, 106-110, 120, 130->133, 136->139, 173-176, 179-181, 198->197, 200, 201->204, 207->206, 209, 210->213, 260-261, 264-265, 268-271, 274->273, 275-279 |
| MPSPlots/render3D/\_\_init\_\_.py |        2 |        0 |        0 |        0 |    100% |           |
| MPSPlots/render3D/artist.py       |      182 |       12 |       34 |        6 |     92% |25, 28-29, 40, 66-68, 85->exit, 103->106, 127, 161-169, 334-336 |
| MPSPlots/render3D/axis.py         |       57 |        5 |       28 |       12 |     80% |27, 30->29, 34->33, 50->49, 54->53, 58->57, 59, 62->61, 66->65, 70->69, 74->73, 78->77, 82->81, 83, 86, 93 |
| MPSPlots/render3D/scene.py        |       50 |        4 |       14 |        3 |     86% |24, 36-37, 55->54, 60->59, 88 |
| MPSPlots/styles/\_\_init\_\_.py   |       14 |        5 |        0 |        0 |     64% |14, 17, 21, 25-26 |
| MPSPlots/tools/\_\_init\_\_.py    |        0 |        0 |        0 |        0 |    100% |           |
| MPSPlots/tools/directories.py     |       17 |        4 |        4 |        1 |     67% |     39-42 |
| MPSPlots/tools/utils.py           |       16 |       14 |        8 |        1 |     12% |8-19, 23-24 |
|                         **TOTAL** | **1166** |  **190** |  **320** |   **76** | **78%** |           |


## Setup coverage badge

Below are examples of the badges you can use in your main branch `README` file.

### Direct image

[![Coverage badge](https://raw.githubusercontent.com/MartinPdeS/MPSPlots/python-coverage-comment-action-data/badge.svg)](https://htmlpreview.github.io/?https://github.com/MartinPdeS/MPSPlots/blob/python-coverage-comment-action-data/htmlcov/index.html)

This is the one to use if your repository is private or if you don't want to customize anything.

### [Shields.io](https://shields.io) Json Endpoint

[![Coverage badge](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/MartinPdeS/MPSPlots/python-coverage-comment-action-data/endpoint.json)](https://htmlpreview.github.io/?https://github.com/MartinPdeS/MPSPlots/blob/python-coverage-comment-action-data/htmlcov/index.html)

Using this one will allow you to [customize](https://shields.io/endpoint) the look of your badge.
It won't work with private repositories. It won't be refreshed more than once per five minutes.

### [Shields.io](https://shields.io) Dynamic Badge

[![Coverage badge](https://img.shields.io/badge/dynamic/json?color=brightgreen&label=coverage&query=%24.message&url=https%3A%2F%2Fraw.githubusercontent.com%2FMartinPdeS%2FMPSPlots%2Fpython-coverage-comment-action-data%2Fendpoint.json)](https://htmlpreview.github.io/?https://github.com/MartinPdeS/MPSPlots/blob/python-coverage-comment-action-data/htmlcov/index.html)

This one will always be the same color. It won't work for private repos. I'm not even sure why we included it.

## What is that?

This branch is part of the
[python-coverage-comment-action](https://github.com/marketplace/actions/python-coverage-comment)
GitHub Action. All the files in this branch are automatically generated and may be
overwritten at any moment.