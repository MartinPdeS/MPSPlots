# Repository Coverage

[Full report](https://htmlpreview.github.io/?https://github.com/MartinPdeS/MPSPlots/blob/python-coverage-comment-action-data/htmlcov/index.html)

| Name                              |    Stmts |     Miss |   Branch |   BrPart |   Cover |   Missing |
|---------------------------------- | -------: | -------: | -------: | -------: | ------: | --------: |
| MPSPlots/\_\_init\_\_.py          |        5 |        2 |        0 |        0 |     60% |       7-8 |
| MPSPlots/\_version.py             |       13 |        3 |        2 |        1 |     73% |      8-11 |
| MPSPlots/colormaps.py             |       12 |        0 |        2 |        0 |    100% |           |
| MPSPlots/directories.py           |       15 |        4 |        4 |        1 |     63% |     35-38 |
| MPSPlots/fonts/\_\_init\_\_.py    |        0 |        0 |        0 |        0 |    100% |           |
| MPSPlots/render2D/\_\_init\_\_.py |        9 |        4 |        2 |        0 |     45% |     11-16 |
| MPSPlots/render2D/artist.py       |      392 |       55 |       50 |       17 |     81% |103, 130, 145->exit, 198->208, 236, 239, 305-309, 324-332, 344-370, 416->419, 430->449, 549, 565, 569, 596, 639->642, 642->exit, 655-664, 708, 764-778, 820, 942-955, 1037, 1087, 1098-1114, 1150, 1161-1179 |
| MPSPlots/render2D/axis.py         |      240 |       51 |       36 |        3 |     71% |84, 87-88, 106, 131-136, 145-150, 159-164, 173-178, 187-189, 198, 210-212, 222-226, 241-243, 308->exit, 566, 592, 618, 631, 671-674 |
| MPSPlots/render2D/scene.py        |      157 |       31 |       46 |        8 |     71% |41, 57-59, 62-63, 100, 103-107, 117, 127->130, 133->136, 170-173, 176-178, 197, 198->201, 206, 207->210, 257-258, 261-262, 265-268, 272-276 |
| MPSPlots/render3D/\_\_init\_\_.py |        2 |        0 |        0 |        0 |    100% |           |
| MPSPlots/render3D/artist.py       |      182 |       12 |       10 |        5 |     91% |25, 28-29, 40, 66-68, 103->106, 127, 161-169, 334-336 |
| MPSPlots/render3D/axis.py         |       57 |        5 |        4 |        1 |     90% |27, 59, 83, 86, 93 |
| MPSPlots/render3D/scene.py        |       50 |        4 |        8 |        1 |     88% |24, 36-37, 88 |
| MPSPlots/styles/\_\_init\_\_.py   |       14 |        5 |        0 |        0 |     64% |15, 19, 23, 27-28 |
| MPSPlots/tools/\_\_init\_\_.py    |        0 |        0 |        0 |        0 |    100% |           |
| MPSPlots/tools/utils.py           |       16 |       14 |        8 |        1 |     12% |8-19, 23-24 |
|                         **TOTAL** | **1164** |  **190** |  **172** |   **38** | **78%** |           |


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