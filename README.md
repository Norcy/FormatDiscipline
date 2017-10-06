# 原理
使用 ClangFormat + Python 脚本批量格式化代码

# 安装
1. `brew install clang-format`
2. 复制 `.clang-format` 到用户根目录（一般为放所有工程文件的总目录）

# 使用
+ 执行 `python Clang-format.py` 对当前目录的代码文件进行格式化（较危险）
+ 执行 `python Clang-format.py targetDirectory` 对指定目录的代码文件进行格式化（建议）
