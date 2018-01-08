# 原理
使用 ClangFormat + Python 脚本批量格式化代码

# 安装
1. `brew install clang-format`
2. 复制 `.clang-format` 到用户根目录（一般为放所有工程文件的总目录）
如果找不到 `.clang-format`，则使用 cmd+shift+. 来显示隐藏文件

# 使用
+ 执行 `python Clang_format.py` 对当前脚本文件所在目录的的代码文件进行格式化（可以直接把 .clang-format 和 python 文件放到项目里面）
+ 执行 `python Clang_format.py targetDirectory` 对指定目录的代码文件进行格式化（建议）
