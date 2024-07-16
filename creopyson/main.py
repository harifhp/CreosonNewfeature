# example_script.py

import creopyson


def main():
    # 创建与CREOSON服务器的连接
    cnx = creopyson.Client()

    try:
        print("Attempting to connect to CREOSON server...")
        cnx.connect()
        print("Connected to CREOSON server.")

        # 调用新增的功能激活视图并保存当前方向为新视图
        creopyson.activate_and_save(cnx, "TOP", "LLMVIEW")
        print("View activated and new view saved successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # 断开连接
        cnx.disconnect()


if __name__ == "__main__":
    main()
