import json

from flask import Flask, request
from Util.readJson import readJson

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    with open("welcome.html", "r", encoding="UTF-8") as f:
        data = f.read()
    return data


@app.route("/login", methods=["GET"])
def login():
    username = request.args.get("username")
    password = request.args.get("password")
    # 此处可以连接数据库进行校验
    if username and password:
        # 不为空
        login_info = readJson.read("login.json")
        if username in login_info.keys():
            # 用户名存在
            if password == login_info.get(username):
                # 账号密码正确
                data = readJson.get_value("return.json", "success")
                return json.dumps(data, ensure_ascii=False)
            else:
                data = readJson.get_value("return.json", "error")
                return json.dumps(data, ensure_ascii=False)
        else:
            data = readJson.get_value("return.json", "error")
            return json.dumps(data, ensure_ascii=False)
    else:
        data = readJson.get_value("return.json", "null")
        return json.dumps(data, ensure_ascii=False)


@app.route("/register", methods=["POST"])
def register():
    username = request.form.get("username")
    password = request.form.get("password")
    # 写入login.json
    json_data = readJson.read("login.json")
    if username in json_data.keys():
        data = readJson.get_value("return.json", "error2")
        return json.dumps(data, ensure_ascii=False)
    json_data[username] = password
    print(json_data)
    try:
        readJson.write(json_data, "login.json")
    except Exception as a:
        data = {
            "errorCode": "2002",
            "message": "{}".format(a)
        }
    else:
        data = readJson.get_value("return.json", "success")
        return json.dumps(data, ensure_ascii=False)

    return json.dumps(data, ensure_ascii=False)


if __name__ == '__main__':
    app.run()
