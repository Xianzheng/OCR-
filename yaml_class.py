import yaml
def get_yaml_data(yaml_file):
    #1-打开yaml文件
    file = open(yaml_file, 'r', encoding="utf-8")
    #2-读取文件
    file_data = file.read()
    #3-将字符串转化为字典或列表
    data = yaml.safe_load(file_data)
    #4-关闭按文件
    file.close()
    #返回读取的数据内容
    return data